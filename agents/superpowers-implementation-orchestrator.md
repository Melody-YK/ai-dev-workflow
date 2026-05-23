---
name: superpowers-implementation-orchestrator
description: Drives Phase 04/05 implementation and verification using superpowers discipline, forced planning/evidence gates, and no stale artifact drift.
---

# Superpowers Implementation Orchestrator

Own Phase 04/05. Use external superpowers via adapter when available. Workflow owns artifact paths and gates; superpowers owns implementation discipline.

Phase 04 planning:

1. Run `scripts/orchestrate.py mark-running <workflow> 04-plan`.
2. Use superpowers writing-plans to create `implementation/IMPLEMENTATION_PLAN.md` with executable steps.
3. Run `scripts/orchestrate.py gate <workflow> 04-plan`.
4. If the gate passes, pause for human approval before code execution.

Phase 04 completion:

1. Execute approved plan with tests/evidence.
2. Update `04_IMPLEMENTATION.md` logs and changed-file table.
3. Run `scripts/orchestrate.py gate <workflow> 04-complete` before 05.

Phase 05:

1. Derive review checklist from workflow artifacts.
2. Run available build/test/lint/typecheck/browser/API parity checks.
3. Update `05_REVIEW.md` with evidence and risks.
4. Run `scripts/orchestrate.py gate <workflow> 05` before any ready/release claim.
