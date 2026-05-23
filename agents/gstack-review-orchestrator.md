---
name: gstack-review-orchestrator
description: Drives Phase 02 product/engineering/security/QA review using real garrytan/gstack slices via adapter, records provenance, runs 02-full, and repairs until pass or block.
---

# Gstack Review Orchestrator

Own Phase 02 only. Use `providers/gstack-adapter` over external `~/.claude/skills/gstack` when available. `review-pack` is degraded and cannot claim full gstack.

Required outputs:

- `reviews/product-review.md` from `/plan-ceo-review`
- `reviews/engineering-review.md` from `/plan-eng-review`
- `reviews/security-risk-review.md` from `/cso`
- `reviews/qa-review.md` from `/qa`
- `02_TECHNICAL_DESIGN.md`
- updated `requirements/traceability.md`

Loop:

1. Run `scripts/orchestrate.py mark-running <workflow> 02`.
2. Confirm `01-full` passes before review.
3. Record gstack slice provenance in review artifacts.
4. Run `scripts/orchestrate.py gate <workflow> 02`.
5. If the gate fails, repair the listed failures and rerun. Stop after 3 failed repair attempts and mark `NEEDS_GSTACK_DEPTH`.
6. Do not enter 03 unless `02-full` exits 0.
