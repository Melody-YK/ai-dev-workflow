---
name: review-pack
description: Bundled product, engineering, security-risk, QA, and release review provider for ai-dev-workflow. Use when phase 02 or phase 05 needs multi-role challenge/review. This is a compact internal provider, not a full vendored copy of garrytan/gstack.
---

# Bundled Review Pack Provider

This provider gives `ai-dev-workflow` an internal review capability. It borrows the idea of multi-role review, but it is not a full garrytan/gstack installation or substitute for gstack commands like /office-hours, /plan-ceo-review, /review, /qa, or /ship.


## Fidelity tier

`review-pack` is `COMPACT_FALLBACK` by default. It is useful when no external review provider is available, but it must not be presented as full `garrytan/gstack` capability.

When used instead of external `garrytan/gstack`, record:

- missing upstream commands/capabilities, such as `/office-hours`, `/plan-ceo-review`, `/plan-eng-review`, `/review`, `/qa`, `/ship`, browser/deploy/gbrain integrations where relevant;
- compensating checks performed inside ai-dev-workflow;
- whether the phase result is `DONE_DEGRADED`, `NEEDS_REVIEW`, or explicitly accepted by the user.

## Roles

Run reviews with distinct stances. Do not merge them into generic summaries too early.

- Product reviewer: scope, user value, non-goals, MVP boundary, decision risks.
- Engineering reviewer: architecture, data model, state machine, API/integration, migration, maintainability.
- Security/risk reviewer: permissions, auditability, data safety, abuse cases, compliance, operational risk.
- QA reviewer: acceptance scenarios, edge cases, regression paths, manual QA, test matrix.
- Release reviewer for phase 05: release readiness, rollback, observability, documentation, remaining risk.

## Phase 02 outputs

Write provider-native notes first:

- `reviews/product-review.md`
- `reviews/engineering-review.md`
- `reviews/security-risk-review.md`
- `reviews/qa-review.md`

Then update `02_TECHNICAL_DESIGN.md` as summary/gate/handoff only.

## Phase 05 outputs

Update `05_REVIEW.md` with:

- requirements coverage review
- architecture/code review findings
- security/risk review findings
- QA review results
- test/build/lint/manual QA evidence
- release readiness verdict
- fixed/accepted/deferred/blocked risk disposition

## Decision brief rule

When a human decision is needed, provide context-specific options plus a custom/freeform option. Each option must include applicability, benefits, costs/risks, and downstream impact. A recommendation is allowed only with rationale.

## Contract reference

For detailed output contract, read `references/review-pack.md`.
