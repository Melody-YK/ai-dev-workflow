---
description: Resume ai-dev-workflow from STATUS.md with forced phase gates and repair loops
argument-hint: .ai-workflow/<feature> [guided-auto]
---

# continue ai-dev-workflow

Resume the workflow at `$ARGUMENTS` using the orchestrated contract.

1. Read `references/orchestration.md`.
2. Read `STATUS.md` in the workflow directory.
3. Determine the current phase and blocked state.
4. Use `scripts/orchestrate.py mark-running <workflow> <phase>` before doing phase work.
5. Use the matching orchestrator contract:
   - 01: `agents/requirements-orchestrator.md`
   - 02: `agents/gstack-review-orchestrator.md`
   - 04/05: `agents/superpowers-implementation-orchestrator.md`
6. Run `scripts/orchestrate.py gate <workflow> <phase>` before marking any clean phase completion.
7. If the gate fails, repair and rerun up to 3 attempts. Stop with the specific `NEEDS_*` / `BLOCKED_*` state if it still fails.
8. Guided-auto skips ordinary continue prompts but not real human gates.

Never continue to the next phase because prose says DONE. Gate output is authoritative.
