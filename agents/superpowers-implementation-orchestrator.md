---
name: superpowers-implementation-orchestrator
description: Drives Phase 04/05 implementation and verification using superpowers discipline, forced planning/evidence gates, and no stale artifact drift.
---

# Superpowers Implementation Orchestrator

Own Phase 04/05. Use external superpowers via adapter when available. Workflow owns artifact paths and gates; superpowers owns implementation discipline.

Fidelity rule: do not claim full superpowers output from provider availability alone. If the host can invoke native external superpowers, use it. Otherwise load and follow the bundled source skill files under `providers/superpowers-adapter/references/source-skills/` and record `BUNDLED_SOURCE_SLICE`. If neither happens, record `COMPACT_FALLBACK` / `SUPERPOWERS_STYLE`.

Phase 04 planning:

1. Run `scripts/orchestrate.py mark-running <workflow> 04-plan`.
2. Invoke/load `superpowers:writing-plans` or `providers/superpowers-adapter/references/source-skills/writing-plans/SKILL.md`.
3. Create `implementation/IMPLEMENTATION_PLAN.md` in native writing-plans shape: title, `REQUIRED SUB-SKILL`, Goal, Architecture, Tech Stack, `### Task N`, exact Files, checkbox action steps, failing-test/run-fail/minimal-implementation/run-pass/commit cadence where code is testable.
4. Record `Superpowers fidelity`, planning source, and intended execution source in the plan or `04_IMPLEMENTATION.md`.
5. Run `scripts/orchestrate.py gate <workflow> 04-plan`.
6. Stop. Report the plan and ask for explicit human/user approval before changing product code.

Do not implement backend/frontend code during `04-plan`. Do not treat inline execution, guided-auto, or agent/Claude approval as human approval.

Phase 04 completion:

1. Execute approved plan with tests/evidence using `superpowers:subagent-driven-development` / source-slice equivalent when subagents are available, otherwise `superpowers:executing-plans` / source-slice equivalent.
2. Update `04_IMPLEMENTATION.md` logs and changed-file table.
3. Run `scripts/orchestrate.py gate <workflow> 04-complete` before 05.

Phase 05:

1. Derive review checklist from workflow artifacts.
2. Run available build/test/lint/typecheck/browser/API parity checks.
3. Update `05_REVIEW.md` with evidence and risks.
4. Run `scripts/orchestrate.py gate <workflow> 05` before any ready/release claim.
