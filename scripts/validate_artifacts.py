#!/usr/bin/env python3
"""Validate required AI dev workflow artifacts exist and basic placeholders are visible."""
from __future__ import annotations

import argparse
import pathlib
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
        help="Also require gstack-style review notes under reviews/.",
    )
    parser.add_argument(
        "--require-prototype-files",
        action="store_true",
        help="Also require generated prototype files under prototype/.",
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

    return 1 if failed else 0


if __name__ == "__main__":
    raise SystemExit(main())
