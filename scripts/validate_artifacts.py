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

FULL_REQUIREMENTS_FILES = {
    "requirements/discovery.md": 5000,
    "requirements/sort.md": 4000,
    "requirements/requirements.md": 20000,
    "requirements/datamodel.md": 10000,
    "requirements/clarification.md": 3000,
    "requirements/validation.md": 6000,
    "requirements/prd.md": 12000,
    "requirements/traceability.md": 6000,
    "requirements/api.yaml": 12000,
}

FULL_REVIEW_FILES = {
    "reviews/product-review.md": 7000,
    "reviews/engineering-review.md": 9000,
    "reviews/security-risk-review.md": 7000,
    "reviews/qa-review.md": 7000,
}

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


def count_matches(text: str, pattern: str) -> int:
    return len(re.findall(pattern, text, re.M | re.I))


def validate_min_size(workflow_dir: pathlib.Path, files: dict[str, int], gate_name: str) -> bool:
    failed = False
    for relative, min_chars in files.items():
        path = workflow_dir / relative
        if not path.exists():
            failed |= fail(f"{gate_name} missing {relative}")
            continue
        size = len(read_text(path).strip())
        if size < min_chars:
            failed |= fail(f"{gate_name} {relative} too thin ({size} chars < {min_chars})")
    return failed


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


def validate_01_full(workflow_dir: pathlib.Path) -> bool:
    """Require provider-native requirements-analyst depth, not summary output."""
    failed = validate_min_size(workflow_dir, FULL_REQUIREMENTS_FILES, "01-full")
    req = read_text(workflow_dir / "requirements" / "requirements.md") if (workflow_dir / "requirements" / "requirements.md").exists() else ""
    discovery = read_text(workflow_dir / "requirements" / "discovery.md") if (workflow_dir / "requirements" / "discovery.md").exists() else ""
    validation = read_text(workflow_dir / "requirements" / "validation.md") if (workflow_dir / "requirements" / "validation.md").exists() else ""
    traceability = read_text(workflow_dir / "requirements" / "traceability.md") if (workflow_dir / "requirements" / "traceability.md").exists() else ""
    api = read_text(workflow_dir / "requirements" / "api.yaml") if (workflow_dir / "requirements" / "api.yaml").exists() else ""

    required_req_markers = [
        "用户角色",
        "用户故事地图",
        "验收条件",
        "gherkin",
        "INVEST",
        "非功能需求",
        "角色与权限",
        "状态机",
        "边界情况",
    ]
    missing = contains_required_markers(req, required_req_markers)
    if missing:
        failed |= fail(f"01-full requirements.md missing full-analysis markers: {', '.join(missing)}")
    story_count = count_matches(req, r"^###\s+US-\d+")
    if story_count < 12:
        failed |= fail(f"01-full requirements.md has too few user stories ({story_count} < 12)")
    scenario_count = count_matches(req, r"^Scenario:")
    if scenario_count < 20:
        failed |= fail(f"01-full requirements.md has too few Gherkin scenarios ({scenario_count} < 20)")
    if "规则同" in req or "同 US-" in req:
        failed |= fail("01-full requirements.md contains shortcut wording like `规则同` / `同 US-*`; each story must be independently testable")

    for marker in ["Power-Interest", "用户旅程", "竞品", "关键洞察"]:
        if marker not in discovery:
            failed |= fail(f"01-full discovery.md missing marker: {marker}")
    for marker in ["Authenticity", "Completeness", "Consistency", "Feasibility", "Verifiability", "Traceability"]:
        if marker not in validation:
            failed |= fail(f"01-full validation.md missing validation dimension: {marker}")
    for marker in ["设计", "原型", "实现", "验证"]:
        if marker not in traceability:
            failed |= fail(f"01-full traceability.md must include lifecycle column/coverage for: {marker}")
    if count_matches(traceability, r"\|[^\n]*\|") < 30:
        failed |= fail("01-full traceability.md is too sparse for full lifecycle traceability")
    operation_count = count_matches(api, r"^\s+operationId:")
    if operation_count < 20 and "not-applicable" not in api.lower():
        failed |= fail(f"01-full api.yaml has too few operationId entries ({operation_count} < 20) for API-bearing project")
    for marker in ["security:", "requestBody:", "responses:", "x-traceability", "status:"]:
        if marker not in api and "not-applicable" not in api.lower():
            failed |= fail(f"01-full api.yaml missing API contract marker: {marker}")
    return failed


def traceability_rows_before_section(traceability: str, section: str) -> list[list[str]]:
    """Return markdown table rows before a later phase section.

    Phase 02 must update the primary traceability matrix, not only append a
    narrative review section. This helper intentionally inspects the rows before
    `## 评审决策追溯` so later prototype/implementation sections cannot mask stale
    design cells.
    """
    scope = traceability.split(section, 1)[0] if section in traceability else traceability
    rows: list[list[str]] = []
    for line in scope.splitlines():
        stripped = line.strip()
        if not stripped.startswith("|") or "---" in stripped:
            continue
        cells = [cell.strip() for cell in stripped.strip("|").split("|")]
        if cells and cells[0] in {"来源PRD章节", "PRD实体", "PRD服务", "编排服务", "维度", "PRD章节"}:
            continue
        rows.append(cells)
    return rows


def is_filled_traceability_cell(value: str) -> bool:
    value = value.strip()
    if not value:
        return False
    return not re.fullmatch(r"(?:TBD|pending|planned|[-—]|⏳.*)", value, re.I)


def validate_02_traceability_design(traceability: str) -> bool:
    failed = False
    if not traceability.strip():
        failed |= fail("02-full missing requirements/traceability.md")
        return failed

    rows = traceability_rows_before_section(traceability, "## 评审决策追溯")
    feature_rows = [row for row in rows if row and row[0].startswith("三-") and len(row) >= 9]
    if not feature_rows:
        failed |= fail("02-full traceability.md missing primary feature traceability rows")
        return failed

    non_tbd_design_rows = [row for row in feature_rows if is_filled_traceability_cell(row[4])]
    must_rows = [row for row in feature_rows if any(marker in row[2] for marker in ["F-001", "F-002", "F-003", "F-006", "F-007", "F-008", "F-009", "F-011", "F-012", "F-014", "F-016", "F-004"])]
    must_rows_without_design = [row for row in must_rows if not is_filled_traceability_cell(row[4])]

    if len(non_tbd_design_rows) < max(8, len(feature_rows) // 2):
        failed |= fail(
            f"02-full traceability.md design column is too sparse "
            f"({len(non_tbd_design_rows)}/{len(feature_rows)} feature rows filled); "
            "gstack must map reviewed requirements to concrete design modules/APIs/state/security decisions"
        )
    if must_rows_without_design:
        missing = ", ".join(row[2] for row in must_rows_without_design[:12])
        failed |= fail(f"02-full traceability.md missing design mapping for core/MUST requirements: {missing}")

    design_text = "\n".join(row[4] for row in feature_rows)
    for marker in ["API", "状态", "权限", "模块"]:
        if marker not in design_text:
            failed |= fail(f"02-full traceability.md design mappings must include concrete {marker} references")
    return failed


def validate_02_full(workflow_dir: pathlib.Path) -> bool:
    """Require full gstack-adapter depth and provenance, not compact review notes."""
    failed = validate_01_full(workflow_dir)
    failed |= validate_min_size(workflow_dir, FULL_REVIEW_FILES, "02-full")
    design = read_text(workflow_dir / "02_TECHNICAL_DESIGN.md") if (workflow_dir / "02_TECHNICAL_DESIGN.md").exists() else ""
    traceability = read_text(workflow_dir / "requirements" / "traceability.md") if (workflow_dir / "requirements" / "traceability.md").exists() else ""
    reviews = "\n".join(read_text(workflow_dir / rel) for rel in FULL_REVIEW_FILES if (workflow_dir / rel).exists())

    if "ADAPTER_FULL" in design:
        for marker in ["plan-ceo-review", "plan-eng-review"]:
            if marker not in design and marker not in reviews:
                failed |= fail(f"02-full claims ADAPTER_FULL but lacks gstack slice provenance: {marker}")
    for marker in ["Assumptions", "Tradeoffs", "Alternatives", "Non-goals", "Risk", "Decision", "Implementation", "Test"]:
        if marker not in reviews and marker.lower() not in reviews.lower():
            failed |= fail(f"02-full review notes missing full-gstack review marker: {marker}")
    for marker in ["accepted", "deferred", "rejected", "changed", "评审结论", "设计决策"]:
        if marker not in traceability:
            failed |= fail(f"02-full traceability.md missing review-decision marker: {marker}")
    failed |= validate_02_traceability_design(traceability)
    if "COMPACT_FALLBACK" in design and "DONE" in design:
        failed |= fail("02-full cannot be clean DONE when only COMPACT_FALLBACK review-pack ran")
    return failed


def validate_03_full(workflow_dir: pathlib.Path) -> bool:
    """Require requirements-analyst-style prototype closure and traceability."""
    failed = validate_02_full(workflow_dir)
    proto = workflow_dir / "03_PROTOTYPE.md"
    text = read_text(proto) if proto.exists() else ""
    status_text = read_text(workflow_dir / "STATUS.md") if (workflow_dir / "STATUS.md").exists() else ""
    if len(text.strip()) < 6000:
        failed |= fail(f"03-full 03_PROTOTYPE.md too thin ({len(text.strip())} chars < 6000)")
    for marker in ["原型计划", "页面到需求映射", "Mock 数据", "原型范围外", "评审反馈", "审批决策"]:
        if marker not in text:
            failed |= fail(f"03-full 03_PROTOTYPE.md missing marker: {marker}")
    if re.search(r"状态：\s*TBD", text) or "进入实现计划前，用户已批准原型" in text and "[ ] 进入实现计划前，用户已批准原型" in text:
        failed |= fail("03-full prototype approval is still TBD/unchecked")
    approval_pending_patterns = [
        r"awaiting\s+human\s+approval",
        r"awaiting\s+approval",
        r"waiting\s+for\s+approval",
        r"待人工确认",
        r"等待.*确认",
        r"等待.*审批",
        r"待确认",
        r"待审批",
    ]
    combined_approval_text = f"{text}\n{status_text}"
    for pattern in approval_pending_patterns:
        if re.search(pattern, combined_approval_text, re.I):
            failed |= fail(f"03-full cannot pass while prototype approval is still pending: {pattern}")
    pages_dir = workflow_dir / "prototype" / "pages"
    pages = sorted(p.name for p in pages_dir.glob("*.html")) if pages_dir.exists() else []
    if len(pages) < 8:
        failed |= fail(f"03-full too few prototype pages ({len(pages)} < 8)")
    traceability = read_text(workflow_dir / "requirements" / "traceability.md") if (workflow_dir / "requirements" / "traceability.md").exists() else ""
    missing_pages = [page for page in pages if page not in traceability and f"prototype/pages/{page}" not in traceability]
    if missing_pages:
        failed |= fail(f"03-full traceability.md missing actual prototype page filenames: {', '.join(missing_pages[:8])}")
    for stale in ["create-ticket.html", "review-ticket.html", "execute-ticket.html", "suspend-ticket.html", "verify-ticket.html", "query-tickets.html"]:
        if stale in traceability and not (workflow_dir / "prototype" / "pages" / stale).exists():
            failed |= fail(f"03-full traceability.md references stale/nonexistent prototype page: {stale}")
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
        choices=["01-full", "02-full", "03-full", "04-plan", "04-complete", "05-complete"],
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

    if args.gate == "01-full":
        failed |= validate_01_full(workflow_dir)
    elif args.gate == "02-full":
        failed |= validate_02_full(workflow_dir)
    elif args.gate == "03-full":
        failed |= validate_03_full(workflow_dir)
    elif args.gate == "04-plan":
        failed |= validate_04_plan(workflow_dir)
    elif args.gate == "04-complete":
        failed |= validate_04_complete(workflow_dir)
    elif args.gate == "05-complete":
        failed |= validate_05_complete(workflow_dir)

    return 1 if failed else 0


if __name__ == "__main__":
    raise SystemExit(main())
