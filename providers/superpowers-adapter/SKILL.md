---
name: superpowers-adapter
description: Adapter/fallback provider for ai-dev-workflow implementation planning, disciplined execution, and verification when the external superpowers plugin is unavailable or needs workflow-specific artifact mapping.
---

# Superpowers Adapter

Prefer the external official `superpowers` plugin when available. This adapter exists to map superpowers-style discipline onto `ai-dev-workflow` artifacts and to provide degraded fallback behavior when the external provider is unavailable.

## Use in ai-dev-workflow

- Phase 04 planning: use writing-plans discipline to create `implementation/IMPLEMENTATION_PLAN.md`.
- Phase 04 execution: execute approved plan in small verifiable steps.
- Phase 05 verification: use verification-before-completion and requesting-code-review discipline.

## Fidelity tier

When external `superpowers` is installed and actually used, this adapter is `ADAPTER_FULL`: it maps superpowers discipline into ai-dev-workflow artifacts.

If external `superpowers` is unavailable, this adapter is only degraded fallback. Mark provider health as `PROVIDER_DEGRADED` unless the output can meet the full contract with equivalent evidence. Record missing external capability and compensating checks in `STATUS.md` and phase artifacts.

## Contract reference

Read `references/superpowers-execution.md` for the authoritative workflow mapping.
