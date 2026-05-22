# gstack to ai-dev-workflow mapping

`ai-dev-workflow` uses gstack as an external capability provider. gstack owns its review/QA method; ai-dev-workflow owns artifact locations and gates.

## Phase 02

| Need | Preferred gstack slice | Workflow artifact |
| --- | --- | --- |
| Product/scope/taste challenge | `/plan-ceo-review` | `reviews/product-review.md` |
| Architecture/data/API/testing challenge | `/plan-eng-review` | `reviews/engineering-review.md` |
| UX/design critique | `/plan-design-review` when UI-heavy | `reviews/product-review.md` or `reviews/design-review.md` |
| Developer experience/API/SDK critique | `/plan-devex-review` when dev-facing | `reviews/engineering-review.md` |
| Security/risk critique | `/cso` when security-sensitive | `reviews/security-risk-review.md` |
| QA strategy | `/qa` planning output when usable | `reviews/qa-review.md` |

## Phase 05

| Need | Preferred gstack slice | Workflow artifact |
| --- | --- | --- |
| Code review | `/review` | `05_REVIEW.md`, `reviews/engineering-review.md` |
| Browser QA | `/qa` | `05_REVIEW.md`, `reviews/qa-review.md` |
| Security/risk audit | `/cso` | `05_REVIEW.md`, `reviews/security-risk-review.md` |
| Release readiness | `/ship` only with explicit user approval for release action | `05_REVIEW.md`, `STATUS.md` |

## Required evidence

Record:

- exact gstack slice/command used;
- whether the external gstack installation path was present;
- files read by the gstack slice;
- output artifact path;
- unresolved issues and accepted/deferred risks.
