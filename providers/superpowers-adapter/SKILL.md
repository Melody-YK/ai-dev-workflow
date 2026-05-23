---
name: superpowers-adapter
description: Adapter/fallback provider for ai-dev-workflow implementation planning, disciplined execution, and verification when the external superpowers plugin is unavailable or needs workflow-specific artifact mapping.
---

# Superpowers Adapter

Prefer the external official `superpowers` plugin when available. This adapter exists to map superpowers discipline onto `ai-dev-workflow` artifacts and to provide source-slice fallback behavior when the external provider is unavailable or the host cannot invoke plugin skills natively.

This is not just a prose summary. Source-derived superpowers skill files are bundled under `references/source-skills/`; load the relevant source skill before producing Phase 04/05 artifacts. If you only follow this short file or `references/superpowers-execution.md`, mark the result as `COMPACT_FALLBACK` / `SUPERPOWERS_STYLE`, not full-fidelity superpowers output.


## Language mapping

When mapping superpowers-style planning/execution/verification into ai-dev-workflow, use the user's primary language for workflow artifacts and user-visible summaries. For Chinese PRDs or Chinese user instructions, write implementation plans, verification notes, blockers, and phase summaries in Chinese, while keeping code symbols, commands, file paths, and API identifiers unchanged.

## Use in ai-dev-workflow

- Phase 04 planning: load `references/source-skills/writing-plans/SKILL.md` and use its native plan shape to create `implementation/IMPLEMENTATION_PLAN.md`.
- Phase 04 execution: after explicit approval, load `references/source-skills/subagent-driven-development/SKILL.md` when subagents are available, otherwise load `references/source-skills/executing-plans/SKILL.md`; execute in small verifiable steps.
- Phase 04 testing discipline: load `references/source-skills/test-driven-development/SKILL.md` for testable implementation tasks.
- Phase 05 verification: load `references/source-skills/verification-before-completion/SKILL.md` and `references/source-skills/requesting-code-review/SKILL.md`.

## Fidelity tier

When external `superpowers` is installed and actually invoked by the host runtime, this adapter is `ADAPTER_FULL`: it maps native superpowers output into ai-dev-workflow artifacts.

When native invocation is unavailable but the bundled source skill files are loaded and followed, record `BUNDLED_SOURCE_SLICE`: source-derived superpowers discipline was used, but not the host plugin invocation.

If neither native invocation nor source-skill loading is used, this adapter is only degraded fallback. Mark provider health as `COMPACT_FALLBACK` / `PROVIDER_DEGRADED`. Record missing external capability and compensating checks in `STATUS.md` and phase artifacts.

## Required invocation evidence

Phase artifacts must state which tier was used and which source/native skills drove the work, for example:

```text
Superpowers fidelity: BUNDLED_SOURCE_SLICE
Planning source: references/source-skills/writing-plans/SKILL.md
Execution source: pending user approval; recommended superpowers:subagent-driven-development
```

Do not claim `ADAPTER_FULL` from provider availability alone.

## Contract reference

Read `references/superpowers-execution.md` for the workflow mapping. Read the relevant file under `references/source-skills/` for the native superpowers procedure before writing or executing artifacts.
