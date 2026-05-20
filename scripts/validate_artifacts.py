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
    "03_IMPLEMENTATION.md",
    "04_REVIEW.md",
    "STATUS.md",
]


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("workflow_dir", type=pathlib.Path)
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

    return 1 if failed else 0


if __name__ == "__main__":
    raise SystemExit(main())
