#!/usr/bin/env python3
"""State-machine helper for ai-dev-workflow.

This script does deterministic orchestration bookkeeping. It does not generate phase
content; Claude/provider adapters still do that. The script makes phase state,
provider health, and gate failures explicit so the model cannot honestly mark a
phase DONE without validator evidence.
"""
from __future__ import annotations

import argparse
import datetime as dt
import pathlib
import re
import subprocess
import sys
from dataclasses import dataclass

ROOT = pathlib.Path(__file__).resolve().parents[1]
VALIDATOR = ROOT / "scripts" / "validate_artifacts.py"
PROVIDER_CHECK = ROOT / "scripts" / "check_providers.py"

PHASE_GATES = {
    "01": "01-full",
    "02": "02-full",
    "03": "03-full",
    "04-plan": "04-plan",
    "04-complete": "04-complete",
    "05": "05-complete",
}

PHASE_STATE_HINTS = {
    "01": "NEEDS_REQUIREMENTS_DEPTH",
    "02": "NEEDS_GSTACK_DEPTH",
    "03": "NEEDS_PROTOTYPE_DEPTH",
    "04-plan": "NEEDS_IMPLEMENTATION_PLAN",
    "04-complete": "BLOCKED_ARTIFACT_DRIFT",
    "05": "BLOCKED_ARTIFACT_DRIFT",
}

PHASE_LABELS = {
    "01": "01_REQUIREMENTS",
    "02": "02_PRODUCT_ENG_REVIEW",
    "03": "03_PROTOTYPE",
    "04-plan": "04_IMPLEMENTATION_PLAN",
    "04-complete": "04_IMPLEMENTATION_COMPLETE",
    "05": "05_VERIFICATION_REVIEW",
}

STATUS_PHASE_ROWS = {
    "01": "01 需求工程",
    "02": "02 产品与工程评审",
    "03": "03 原型",
    "04-plan": "04 实现",
    "04-complete": "04 实现",
    "05": "05 验证与评审",
}

@dataclass
class GateResult:
    phase: str
    gate: str
    rc: int
    output: str


def now() -> str:
    return dt.datetime.now().astimezone().isoformat(timespec="seconds")


def read(path: pathlib.Path) -> str:
    return path.read_text(encoding="utf-8") if path.exists() else ""


def write(path: pathlib.Path, text: str) -> None:
    path.write_text(text, encoding="utf-8")


def status_path(workflow_dir: pathlib.Path) -> pathlib.Path:
    return workflow_dir / "STATUS.md"


def append_section(path: pathlib.Path, heading: str, body: str) -> None:
    text = read(path).rstrip()
    stamp = now()
    addition = f"\n\n## {heading} — {stamp}\n\n{body.strip()}\n"
    write(path, text + addition)


def replace_current_phase(text: str, phase: str) -> str:
    label = PHASE_LABELS.get(phase, phase)
    return re.sub(r"^- 当前阶段：.*$", f"- 当前阶段：{label}", text, flags=re.M)


def replace_checkpoint(text: str, checkpoint: str) -> str:
    return re.sub(r"^- 检查点状态：.*$", f"- 检查点状态：{checkpoint}", text, flags=re.M)


def replace_last_update(text: str) -> str:
    return re.sub(r"^- 最后更新：.*$", f"- 最后更新：{now()}", text, flags=re.M)


def replace_phase_row_state(text: str, phase: str, state: str) -> str:
    row_label = STATUS_PHASE_ROWS.get(phase)
    if not row_label:
        return text
    pattern = re.compile(rf"^(\|\s*{re.escape(row_label)}\s*\|[^|]*\|\s*)([^|]*?)(\s*\|.*)$", re.M)
    return pattern.sub(rf"\g<1>{state}\g<3>", text)


def update_status(workflow_dir: pathlib.Path, phase: str, checkpoint: str, state: str | None = None) -> None:
    path = status_path(workflow_dir)
    text = read(path)
    if not text:
        print(f"STATUS.md not found: {path}", file=sys.stderr)
        return
    text = replace_current_phase(text, phase)
    text = replace_checkpoint(text, checkpoint)
    text = replace_last_update(text)
    if state:
        text = replace_phase_row_state(text, phase, state)
    write(path, text)


def run_command(cmd: list[str], cwd: pathlib.Path | None = None) -> tuple[int, str]:
    proc = subprocess.run(cmd, cwd=str(cwd) if cwd else None, text=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
    return proc.returncode, proc.stdout


def run_gate(workflow_dir: pathlib.Path, phase: str) -> GateResult:
    gate = PHASE_GATES[phase]
    rc, out = run_command([sys.executable, str(VALIDATOR), str(workflow_dir), "--gate", gate])
    return GateResult(phase=phase, gate=gate, rc=rc, output=out)


def run_provider_check(project_root: pathlib.Path) -> str:
    rc, out = run_command([sys.executable, str(PROVIDER_CHECK)], cwd=project_root)
    prefix = f"provider preflight rc={rc}\n"
    return prefix + out


def record_gate(workflow_dir: pathlib.Path, result: GateResult) -> None:
    log_dir = workflow_dir / "logs"
    log_dir.mkdir(exist_ok=True)
    log_path = log_dir / f"gate-{result.gate}-{now().replace(':', '').replace('+', '-')}.log"
    log_path.write_text(result.output, encoding="utf-8")

    checkpoint = f"{result.gate} gate {'PASSED' if result.rc == 0 else 'FAILED'} rc={result.rc}"
    state = "DONE" if result.rc == 0 else PHASE_STATE_HINTS.get(result.phase, "BLOCKED_ARTIFACT_DRIFT")
    update_status(workflow_dir, result.phase, checkpoint, state=state)

    artifact_name = {
        "01": "01_REQUIREMENTS.md",
        "02": "02_TECHNICAL_DESIGN.md",
        "03": "03_PROTOTYPE.md",
        "04-plan": "04_IMPLEMENTATION.md",
        "04-complete": "04_IMPLEMENTATION.md",
        "05": "05_REVIEW.md",
    }[result.phase]
    failures = "\n".join(line for line in result.output.splitlines() if line.startswith("FAIL")) or result.output.strip() or "(no output)"
    append_section(
        workflow_dir / artifact_name,
        f"Gate evidence `{result.gate}`",
        f"Command: `python3 {VALIDATOR} {workflow_dir} --gate {result.gate}`\n\nExit code: `{result.rc}`\n\nLog: `{log_path}`\n\n```text\n{failures[:6000]}\n```",
    )


def cmd_preflight(args: argparse.Namespace) -> int:
    workflow_dir = args.workflow_dir.resolve()
    project_root = args.project_root.resolve() if args.project_root else workflow_dir.parents[1]
    output = run_provider_check(project_root)
    append_section(status_path(workflow_dir), "Provider preflight evidence", f"```text\n{output}\n```")
    print(output)
    return 0


def cmd_mark_running(args: argparse.Namespace) -> int:
    workflow_dir = args.workflow_dir.resolve()
    update_status(workflow_dir, args.phase, f"{PHASE_LABELS.get(args.phase, args.phase)} RUNNING", state="RUNNING")
    print(f"marked {args.phase} RUNNING in {workflow_dir / 'STATUS.md'}")
    return 0


def cmd_gate(args: argparse.Namespace) -> int:
    workflow_dir = args.workflow_dir.resolve()
    result = run_gate(workflow_dir, args.phase)
    record_gate(workflow_dir, result)
    print(result.output, end="")
    print(f"gate {result.gate} rc={result.rc}")
    return result.rc


def cmd_validate_all(args: argparse.Namespace) -> int:
    workflow_dir = args.workflow_dir.resolve()
    phases = ["01", "02", "03", "04-plan", "04-complete", "05"] if args.all else args.phases
    worst = 0
    for phase in phases:
        result = run_gate(workflow_dir, phase)
        print(f"== {phase} / {result.gate} rc={result.rc} ==")
        failures = [line for line in result.output.splitlines() if line.startswith("FAIL")]
        print("\n".join(failures[:40]) if failures else "PASS")
        if result.rc != 0:
            worst = result.rc
    return worst


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    sub = parser.add_subparsers(dest="command", required=True)

    p = sub.add_parser("preflight")
    p.add_argument("workflow_dir", type=pathlib.Path)
    p.add_argument("--project-root", type=pathlib.Path)
    p.set_defaults(func=cmd_preflight)

    p = sub.add_parser("mark-running")
    p.add_argument("workflow_dir", type=pathlib.Path)
    p.add_argument("phase", choices=sorted(PHASE_GATES))
    p.set_defaults(func=cmd_mark_running)

    p = sub.add_parser("gate")
    p.add_argument("workflow_dir", type=pathlib.Path)
    p.add_argument("phase", choices=sorted(PHASE_GATES))
    p.set_defaults(func=cmd_gate)

    p = sub.add_parser("validate-all")
    p.add_argument("workflow_dir", type=pathlib.Path)
    p.add_argument("phases", nargs="*", choices=sorted(PHASE_GATES))
    p.add_argument("--all", action="store_true")
    p.set_defaults(func=cmd_validate_all)

    args = parser.parse_args()
    return args.func(args)


if __name__ == "__main__":
    raise SystemExit(main())
