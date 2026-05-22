#!/usr/bin/env python3
"""Check ai-dev-workflow provider availability and fidelity.

The key distinction is fidelity, not just presence:
- EXTERNAL_FULL: real upstream skill/plugin is installed and should be invoked.
- BUNDLED_SOURCE_SLICE: source-derived subset is bundled and must be loaded directly.
- ADAPTER_FULL: adapter can map a real external provider into workflow artifacts.
- COMPACT_FALLBACK: lightweight approximation; useful, but not equivalent.
- MISSING: no usable provider.
"""
from __future__ import annotations

import argparse
import json
from pathlib import Path
from typing import Any, Iterable


def first_existing(paths: Iterable[Path]) -> str | None:
    for path in paths:
        if path.exists():
            return str(path)
    return None


def all_existing(paths: Iterable[Path]) -> bool:
    return all(path.exists() for path in paths)


def provider(
    *,
    capability: str,
    preferred: str,
    status: str,
    fidelity_tier: str,
    recommended: str,
    external_path: str | None = None,
    bundled_path: str | None = None,
    source_path: str | None = None,
    missing: list[str] | None = None,
    notes: list[str] | None = None,
) -> dict[str, Any]:
    return {
        "capability": capability,
        "preferred": preferred,
        "status": status,
        "fidelityTier": fidelity_tier,
        "recommendedProvider": recommended,
        "externalAvailable": external_path is not None,
        "externalPath": external_path,
        "sourcePath": source_path,
        "bundledAvailable": bundled_path is not None,
        "bundledPath": bundled_path,
        "missing": missing or [],
        "notes": notes or [],
    }


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--repo-root", default=Path(__file__).resolve().parents[1])
    parser.add_argument("--json", action="store_true")
    args = parser.parse_args()

    repo = Path(args.repo_root).expanduser().resolve()
    home = Path.home()
    checks: list[dict[str, Any]] = []

    # requirements-analyst: a Claude-discoverable SKILL is EXTERNAL_FULL.
    # The old POWER.md source is useful, but not directly invokable by Claude Code.
    req_skill = first_existing([
        home / ".claude" / "skills" / "requirements-analyst" / "SKILL.md",
        home / ".claude" / "plugins" / "cache" / "requirements-analyst" / "SKILL.md",
    ])
    req_source = first_existing([
        home / "Desktop" / "learn-powers" / "powers" / "requirements-analyst" / "POWER.md",
    ])
    req_bundled = first_existing([
        repo / "providers" / "requirements-analyst" / "SKILL.md",
    ])
    if req_skill:
        checks.append(provider(
            capability="requirements-analysis",
            preferred="requirements-analyst",
            status="available",
            fidelity_tier="EXTERNAL_FULL",
            recommended="external requirements-analyst",
            external_path=req_skill,
            bundled_path=req_bundled,
            source_path=req_source,
        ))
    elif req_bundled:
        checks.append(provider(
            capability="requirements-analysis",
            preferred="requirements-analyst",
            status="available",
            fidelity_tier="BUNDLED_SOURCE_SLICE",
            recommended="bundled requirements-analyst source slice",
            bundled_path=req_bundled,
            source_path=req_source,
            notes=["Load providers/requirements-analyst/references/steering files for the active subtask; otherwise downgrade to COMPACT_FALLBACK."],
        ))
    else:
        checks.append(provider(
            capability="requirements-analysis",
            preferred="requirements-analyst",
            status="missing",
            fidelity_tier="MISSING",
            recommended="none",
            source_path=req_source,
            missing=["requirements-analyst SKILL.md or bundled provider"],
        ))

    # garrytan/gstack: only the real installed gstack gives EXTERNAL_FULL.
    # review-pack is deliberately just a compact fallback.
    gstack_root = first_existing([
        home / ".claude" / "skills" / "gstack",
    ])
    gstack_required = [
        home / ".claude" / "skills" / "gstack" / "plan-ceo-review" / "SKILL.md",
        home / ".claude" / "skills" / "gstack" / "plan-eng-review" / "SKILL.md",
        home / ".claude" / "skills" / "gstack" / "review" / "SKILL.md",
        home / ".claude" / "skills" / "gstack" / "qa" / "SKILL.md",
    ]
    gstack_full = gstack_root is not None and all_existing(gstack_required)
    gstack_missing = [str(path) for path in gstack_required if not path.exists()]
    gstack_adapter = first_existing([repo / "providers" / "gstack-adapter" / "SKILL.md"])
    review_pack = first_existing([repo / "providers" / "review-pack" / "SKILL.md"])
    if gstack_full:
        checks.append(provider(
            capability="product-engineering-review",
            preferred="garrytan/gstack",
            status="available",
            fidelity_tier="ADAPTER_FULL",
            recommended="gstack-adapter over external garrytan/gstack",
            external_path=gstack_root,
            bundled_path=gstack_adapter,
            notes=["Use gstack command skills for phase-specific slices; map outputs into .ai-workflow artifacts."],
        ))
    elif review_pack:
        checks.append(provider(
            capability="product-engineering-review",
            preferred="garrytan/gstack",
            status="degraded",
            fidelity_tier="COMPACT_FALLBACK",
            recommended="bundled review-pack only; install garrytan/gstack for full capability",
            external_path=gstack_root,
            bundled_path=review_pack,
            missing=gstack_missing or ["~/.claude/skills/gstack"],
            notes=["review-pack is not full gstack; phase should be DONE_DEGRADED/NEEDS_REVIEW unless user accepts reduced depth."],
        ))
    else:
        checks.append(provider(
            capability="product-engineering-review",
            preferred="garrytan/gstack",
            status="missing",
            fidelity_tier="MISSING",
            recommended="install garrytan/gstack",
            external_path=gstack_root,
            missing=gstack_missing or ["~/.claude/skills/gstack", "providers/review-pack/SKILL.md"],
        ))

    # superpowers: adapter is full only when the external plugin/skill is actually present.
    super_external = first_existing([
        home / ".claude" / "plugins" / "cache" / "claude-plugins-official" / "superpowers" / "5.1.0" / ".claude-plugin" / "plugin.json",
        home / ".claude" / "skills" / "superpowers" / "SKILL.md",
    ])
    super_adapter = first_existing([
        repo / "providers" / "superpowers-adapter" / "SKILL.md",
    ])
    checks.append(provider(
        capability="implementation-verification-discipline",
        preferred="superpowers",
        status="available" if super_external else ("degraded" if super_adapter else "missing"),
        fidelity_tier="ADAPTER_FULL" if super_external else ("COMPACT_FALLBACK" if super_adapter else "MISSING"),
        recommended="external superpowers via adapter" if super_external else ("superpowers-adapter PROVIDER_DEGRADED" if super_adapter else "none"),
        external_path=super_external,
        bundled_path=super_adapter,
        missing=[] if super_external else ["external superpowers plugin/skill"],
    ))

    result = {"repoRoot": str(repo), "providers": checks}
    if args.json:
        print(json.dumps(result, ensure_ascii=False, indent=2))
    else:
        for item in checks:
            print(f"{item['capability']}: {item['status']} [{item['fidelityTier']}] -> {item['recommendedProvider']}")
            if item.get("externalPath"):
                print(f"  external: {item['externalPath']}")
            if item.get("sourcePath"):
                print(f"  source:   {item['sourcePath']}")
            if item.get("bundledPath"):
                print(f"  bundled:  {item['bundledPath']}")
            for missing in item.get("missing", []):
                print(f"  missing:  {missing}")
            for note in item.get("notes", []):
                print(f"  note:     {note}")
    return 0 if all(i["status"] in {"available", "degraded"} for i in checks) else 1


if __name__ == "__main__":
    raise SystemExit(main())
