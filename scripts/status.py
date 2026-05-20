#!/usr/bin/env python3
"""Print workflow STATUS.md."""
from __future__ import annotations

import argparse
import pathlib


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("workflow_dir", type=pathlib.Path)
    args = parser.parse_args()
    status = args.workflow_dir / "STATUS.md"
    print(status.read_text(encoding="utf-8"))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
