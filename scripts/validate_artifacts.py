#!/usr/bin/env python3
"""Validate AI dev workflow artifacts and phase completion gates."""
from __future__ import annotations

import argparse
import pathlib
import re
import sys

REQUIRED = [
    "00_INTAKE.md",
    "01_REQUIREMENTS.md",
    "02_TECHNICAL_DESIGN.md",
    "03_PROTOTYPE.md",
    "04_IMPLEMENTATION.md",
    "05_REVIEW.md",
    "STATUS.md",
]

REQUIREMENTS_DETAIL_PATHS = [
    "requirements",
    "requirements/discovery.md",
    "requirements/sort.md",
    "requirements/requirements.md",
    "requirements/datamodel.md",
    "requirements/clarification.md",
    "requirements/validation.md",
    "requirements/prd.md",
    "requirements/open-questions.md",
    "requirements/traceability.md",
]

REVIEW_DETAIL_PATHS = [
    "reviews",
    "reviews/product-review.md",
    "reviews/engineering-review.md",
    "reviews/security-risk-review.md",
    "reviews/qa-review.md",
]

PROTOTYPE_OPTIONAL_PATHS = [
    "prototype/index.html",
    "prototype/css/style.css",
    "prototype/pages",
]

PLACEHOLDER_PATTERNS = [
    r"\bTBD\b",
    r"\bpending\b",
    r"⏳\s*待确认",
    r"计划审批状态：TBD",
    r"执行审批状态：TBD",
    r"状态：TBD",
    r"建议：TBD",
]


def read_text(path: pathlib.Path) -> str:
    return path.read_text(encoding="utf-8", errors="replace")


def fail(message: str) -> bool:
    print(f"FAIL {message}")
    return True


def contains_required_markers(text: str, markers: list[str]) -> list[str]:
    return [marker for marker in markers if marker not in text]


def has_non_placeholder_table_row(text: str, header: str) -> bool:
    """Heuristic: after a section header, find a table row with real content.

    This intentionally rejects template rows such as `|  |  | pending | |`.
    """
    idx = text.find(header)
    if idx < 0:
        return False
    section = text[idx :]
    next_header = re.search(r"\n##\s+", section[len(header) :])
    if next_header:
        section = section[: len(header) + next_header.start()]
    for line in section.splitlines():
        stripped = line.strip()
        if not stripped.startswith("|") or "---" in stripped:
            continue
        cells = [cell.strip() for cell in stripped.strip("|").split("|")]
        joined = " ".join(cells)
        if not joined or joined in {"命令 目的 结果 证据 / 日志", "文件 变更说明 对应需求 / 设计"}:
            continue
        if re.search(r"\w|[\u4e00-\u9fff]", joined) and not re.fullmatch(r"(?:pending|planned|TBD|open|low / medium / high / blocking|fixed / accepted / deferred / blocked|accepted / deferred / blocked / decision-needed|unit / integration / e2e / manual|app-load-smoke / authenticated-page-smoke / core-flow-browser-smoke|\s)+", joined, re.I):
            if any(cell and cell.lower() not in {"pending", "planned", "tbd", "open"} for cell in cells):
                return True
    return False


def validate_04_plan(workflow_dir: pathlib.Path) -> bool:
    failed = False
    plan = workflow_dir / "implementation" / "IMPLEMENTATION_PLAN.md"
    if not plan.exists():
        failed |= fail("04-plan missing implementation/IMPLEMENTATION_PLAN.md")
        return failed
    text = read_text(plan)
    if len(text.strip()) < 1500:
        failed |= fail("04-plan implementation/IMPLEMENTATION_PLAN.md is too thin (<1500 chars)")
    required = [
        "Traceability",
        "Files",
        "Test/verification first",
        "Commands",
        "Pass criteria",
        "Failure handling",
    ]
    missing = contains_required_markers(text, required)
    if missing:
        failed |= fail(f"04-plan missing required execution-unit markers: {', '.join(missing)}")
    if not re.search(r"^###\s+Step\s+\d+", text, re.M):
        failed |= fail("04-plan missing `### Step <n>` execution units")
    return failed


def validate_04_complete(workflow_dir: pathlib.Path) -> bool:
    failed = validate_04_plan(workflow_dir)
    impl = workflow_dir / "04_IMPLEMENTATION.md"
    text = read_text(impl)
    for pattern in [r"计划审批状态：TBD", r"执行审批状态：TBD"]:
        if re.search(pattern, text):
            failed |= fail(f"04-complete unresolved approval placeholder: {pattern}")
    required_sections = [
        "## 执行日志",
        "## 验证命令",
        "## 变更文件",
        "## 回滚 / 恢复说明",
        "## 追踪关系更新",
    ]
    for section in required_sections:
        if section not in text:
            failed |= fail(f"04-complete missing section: {section}")
    for section in ["## 执行日志", "## 验证命令", "## 变更文件"]:
        if not has_non_placeholder_table_row(text, section):
            failed |= fail(f"04-complete has no real evidence rows in {section}")
    if "[ ] 验证命令已运行并记录结果" in text:
        failed |= fail("04-complete checklist still says verification commands were not recorded")
    if "[ ] 变更文件清单已填写" in text:
        failed |= fail("04-complete checklist still says changed files were not recorded")
    return failed


def validate_05_complete(workflow_dir: pathlib.Path) -> bool:
    failed = validate_04_complete(workflow_dir)
    review = workflow_dir / "05_REVIEW.md"
    text = read_text(review)
    for pattern in PLACEHOLDER_PATTERNS:
        if re.search(pattern, text, re.I):
            failed |= fail(f"05-complete unresolved placeholder/pending marker: {pattern}")
    evidence_sections = [
        "## 需求覆盖情况",
        "## 原型覆盖情况",
        "## 测试 / build / lint 证据",
        "## API 合同一致性证据",
        "## Browser / 前端 Smoke 证据",
        "## 代码 / 架构评审发现",
        "## 安全 / 风险复查",
    ]
    for section in evidence_sections:
        if section not in text:
            failed |= fail(f"05-complete missing section: {section}")
        elif not has_non_placeholder_table_row(text, section):
            failed |= fail(f"05-complete has no real evidence rows in {section}")
    if re.search(r"状态：\s*TBD|建议：\s*TBD", text):
        failed |= fail("05-complete release readiness is still TBD")
    if "[ ] 已记录测试/build/lint 证据" in text:
        failed |= fail("05-complete checklist still says test/build/lint evidence is missing")
    if "[ ] 若存在前端，已按 app-load" in text:
        failed |= fail("05-complete checklist still says browser smoke evidence is missing")
    if "[ ] 已完成最终一致性扫描" in text:
        failed |= fail("05-complete final consistency scan is unchecked")
    return failed


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("workflow_dir", type=pathlib.Path)
    parser.add_argument(
        "--require-requirements-details",
        action="store_true",
        help="Also require detailed requirements files under requirements/.",
    )
    parser.add_argument(
        "--require-review-notes",
        action="store_true",
        help="Also require review-pack notes under reviews/.",
    )
    parser.add_argument(
        "--require-prototype-files",
        action="store_true",
        help="Also require generated prototype files under prototype/.",
    )
    parser.add_argument(
        "--gate",
        choices=["04-plan", "04-complete", "05-complete"],
        help="Run stricter phase gate validation before claiming a phase is complete.",
    )
    args = parser.parse_args()
    workflow_dir = args.workflow_dir.resolve()

    if not workflow_dir.exists():
        print(f"missing workflow dir: {workflow_dir}", file=sys.stderr)
        return 2

    failed = False
    for name in REQUIRED:
        path = workflow_dir / name
        if not path.exists():
            print(f"MISSING {name}")
            failed = True
            continue
        text = path.read_text(encoding="utf-8", errors="replace")
        if not text.strip():
            print(f"EMPTY {name}")
            failed = True
        else:
            print(f"OK {name}")

    if args.require_requirements_details:
        for relative in REQUIREMENTS_DETAIL_PATHS:
            path = workflow_dir / relative
            if not path.exists():
                print(f"MISSING {relative}")
                failed = True
            elif path.is_file() and not path.read_text(encoding="utf-8", errors="replace").strip():
                print(f"EMPTY {relative}")
                failed = True
            else:
                print(f"OK {relative}")

    if args.require_review_notes:
        for relative in REVIEW_DETAIL_PATHS:
            path = workflow_dir / relative
            if not path.exists():
                print(f"MISSING {relative}")
                failed = True
            elif path.is_file() and not path.read_text(encoding="utf-8", errors="replace").strip():
                print(f"EMPTY {relative}")
                failed = True
            else:
                print(f"OK {relative}")

    if args.require_prototype_files:
        for relative in PROTOTYPE_OPTIONAL_PATHS:
            path = workflow_dir / relative
            if not path.exists():
                print(f"MISSING {relative}")
                failed = True
            else:
                print(f"OK {relative}")

    if args.gate == "04-plan":
        failed |= validate_04_plan(workflow_dir)
    elif args.gate == "04-complete":
        failed |= validate_04_complete(workflow_dir)
    elif args.gate == "05-complete":
        failed |= validate_05_complete(workflow_dir)

    return 1 if failed else 0


if __name__ == "__main__":
    raise SystemExit(main())
