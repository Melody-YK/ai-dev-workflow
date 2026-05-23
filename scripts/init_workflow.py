#!/usr/bin/env python3
"""Initialize a lightweight AI dev workflow artifact directory."""
from __future__ import annotations

import argparse
import datetime as dt
import pathlib
import re
import sys

ROOT = pathlib.Path(__file__).resolve().parents[1]
TEMPLATES = ROOT / "assets" / "templates"


def slugify(value: str) -> str:
    value = value.strip().lower()
    value = re.sub(r"[^a-z0-9]+", "-", value)
    value = re.sub(r"-+", "-", value).strip("-")
    return value or "feature"


def read_summary(path: pathlib.Path, max_chars: int = 1200) -> str:
    text = path.read_text(encoding="utf-8", errors="replace")
    lines = []
    for line in text.splitlines():
        if line.strip():
            lines.append(line.rstrip())
        if sum(len(x) for x in lines) > max_chars:
            break
    summary = "\n".join(lines)
    if len(summary) > max_chars:
        summary = summary[:max_chars].rstrip() + "…"
    return summary


def detect_language(*texts: str) -> str:
    """Return the workflow artifact language from user/source text.

    This is intentionally simple and deterministic. It only decides the
    workflow contract language, not code identifiers or API names.
    """
    combined = "\n".join(texts)
    cjk = len(re.findall(r"[\u4e00-\u9fff]", combined))
    latin_words = len(re.findall(r"\b[A-Za-z]{3,}\b", combined))
    if cjk >= 20 or cjk >= max(8, latin_words // 3):
        return "zh-CN"
    return "en"


def render(template: str, values: dict[str, str]) -> str:
    for key, value in values.items():
        template = template.replace("{{" + key + "}}", value)
    return template


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--project-root", required=True, type=pathlib.Path)
    parser.add_argument("--source-prd", required=True, type=pathlib.Path)
    parser.add_argument("--feature", required=True)
    parser.add_argument("--force", action="store_true")
    parser.add_argument(
        "--mode",
        choices=("manual", "guided-auto"),
        default="manual",
        help="manual pauses after 00; guided-auto marks 00 as auto-continue into 01.",
    )
    args = parser.parse_args()

    project_root = args.project_root.resolve()
    source_prd = args.source_prd.resolve()
    if not source_prd.exists():
        print(f"source PRD not found: {source_prd}", file=sys.stderr)
        return 2

    feature_slug = slugify(args.feature)
    workflow_dir = project_root / ".ai-workflow" / feature_slug
    workflow_dir.mkdir(parents=True, exist_ok=True)

    created_at = dt.datetime.now().astimezone().isoformat(timespec="seconds")
    raw_summary = read_summary(source_prd)
    artifact_language = detect_language(args.feature, raw_summary)

    if artifact_language.startswith("zh"):
        next_action = (
            "guided-auto：直接进入 01 需求工程；仅对阻塞澄清问题提出 decision brief。"
            if args.mode == "guided-auto"
            else "继续进入 01 需求发现/澄清判断；如有阻塞澄清问题，直接提出 decision brief。"
        )
    else:
        next_action = (
            "guided-auto: continue directly into 01 Requirements; ask a decision brief only for blocking clarification questions."
            if args.mode == "guided-auto"
            else "Continue into 01 Requirements discovery/clarification; ask decision briefs for blocking clarification questions."
        )

    values = {
        "FEATURE_NAME": args.feature,
        "FEATURE_SLUG": feature_slug,
        "SOURCE_PRD": str(source_prd),
        "WORKFLOW_DIR": str(workflow_dir),
        "CREATED_AT": created_at,
        "RAW_SUMMARY": raw_summary,
        "ARTIFACT_LANGUAGE": artifact_language,
        "CURRENT_PHASE": "01_REQUIREMENTS",
        "CHECKPOINT_STATUS": "AUTO_CONTINUE_TO_01" if args.mode == "guided-auto" else "READY_FOR_01_DISCOVERY",
        "PHASE_00_STATUS": "DONE",
        "PHASE_01_STATUS": "READY",
        "PHASE_02_STATUS": "NOT_STARTED",
        "PHASE_03_STATUS": "NOT_STARTED",
        "PHASE_04_STATUS": "NOT_STARTED",
        "PHASE_05_STATUS": "NOT_STARTED",
        "NEXT_ACTION": next_action,
    }

    for template_path in sorted(TEMPLATES.glob("*.md")):
        target = workflow_dir / template_path.name
        if target.exists() and not args.force:
            print(f"skip existing {target}")
            continue
        target.write_text(render(template_path.read_text(encoding="utf-8"), values), encoding="utf-8")
        print(f"wrote {target}")

    for detail_dir in ["requirements", "reviews"]:
        for template_path in sorted(x for x in (TEMPLATES / detail_dir).iterdir() if x.is_file()):
            relative = template_path.relative_to(TEMPLATES)
            target = workflow_dir / relative
            target.parent.mkdir(parents=True, exist_ok=True)
            if target.exists() and not args.force:
                print(f"skip existing {target}")
                continue
            target.write_text(render(template_path.read_text(encoding="utf-8"), values), encoding="utf-8")
            print(f"wrote {target}")

    for relative_dir in ["prototype/css", "prototype/pages", "implementation"]:
        directory = workflow_dir / relative_dir
        directory.mkdir(parents=True, exist_ok=True)
        print(f"ensured {directory}")

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
