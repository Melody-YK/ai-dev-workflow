#!/usr/bin/env python3
"""Check ai-dev-workflow provider availability.

This is a best-effort local filesystem preflight for Claude Code/OpenClaw runs.
It reports external providers plus bundled fallback providers shipped with this repo.
"""
from __future__ import annotations

import argparse
import json
from pathlib import Path
from typing import Iterable


def exists_any(paths: Iterable[Path]) -> tuple[bool, str | None]:
    for path in paths:
        if path.exists():
            return True, str(path)
    return False, None


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--repo-root", default=Path(__file__).resolve().parents[1])
    parser.add_argument("--json", action="store_true")
    args = parser.parse_args()

    repo = Path(args.repo_root).expanduser().resolve()
    home = Path.home()

    checks = []

    req_external, req_external_path = exists_any([
        home / ".claude" / "skills" / "requirements-analyst" / "SKILL.md",
        home / ".claude" / "plugins" / "cache" / "requirements-analyst" / "SKILL.md",
        home / "Desktop" / "learn-powers" / "powers" / "requirements-analyst" / "POWER.md",
    ])
    req_bundled, req_bundled_path = exists_any([
        repo / "providers" / "requirements-analyst" / "SKILL.md",
    ])
    checks.append({
        "capability": "requirements-analysis",
        "preferred": "requirements-analyst",
        "externalAvailable": req_external,
        "externalPath": req_external_path,
        "bundledAvailable": req_bundled,
        "bundledPath": req_bundled_path,
        "recommendedProvider": "external requirements-analyst" if req_external else ("bundled requirements-analyst" if req_bundled else "none"),
        "status": "available" if (req_external or req_bundled) else "missing",
    })

    gstack_external, gstack_external_path = exists_any([
        home / ".claude" / "skills" / "gstack",
        home / ".claude" / "skills" / "review-pack" / "SKILL.md",
    ])
    gstack_bundled, gstack_bundled_path = exists_any([
        repo / "providers" / "review-pack" / "SKILL.md",
    ])
    checks.append({
        "capability": "product-engineering-review",
        "preferred": "review-pack",
        "externalAvailable": gstack_external,
        "externalPath": gstack_external_path,
        "bundledAvailable": gstack_bundled,
        "bundledPath": gstack_bundled_path,
        "recommendedProvider": "external garrytan/gstack or review-pack" if gstack_external else ("bundled review-pack" if gstack_bundled else "none"),
        "status": "available" if (gstack_external or gstack_bundled) else "missing",
    })

    super_external, super_external_path = exists_any([
        home / ".claude" / "plugins" / "cache" / "claude-plugins-official" / "superpowers" / "5.1.0" / ".claude-plugin" / "plugin.json",
        home / ".claude" / "skills" / "superpowers" / "SKILL.md",
    ])
    super_adapter, super_adapter_path = exists_any([
        repo / "providers" / "superpowers-adapter" / "SKILL.md",
    ])
    checks.append({
        "capability": "implementation-verification-discipline",
        "preferred": "superpowers",
        "externalAvailable": super_external,
        "externalPath": super_external_path,
        "bundledAvailable": super_adapter,
        "bundledPath": super_adapter_path,
        "recommendedProvider": "external superpowers" if super_external else ("superpowers-adapter PROVIDER_DEGRADED" if super_adapter else "none"),
        "status": "available" if super_external else ("degraded" if super_adapter else "missing"),
    })

    result = {"repoRoot": str(repo), "providers": checks}
    if args.json:
        print(json.dumps(result, ensure_ascii=False, indent=2))
    else:
        for item in checks:
            print(f"{item['capability']}: {item['status']} -> {item['recommendedProvider']}")
            if item.get("externalPath"):
                print(f"  external: {item['externalPath']}")
            if item.get("bundledPath"):
                print(f"  bundled:  {item['bundledPath']}")
    return 0 if all(i["status"] in {"available", "degraded"} for i in checks) else 1


if __name__ == "__main__":
    raise SystemExit(main())
