---
name: requirements-analyst
description: Bundled provider for requirements engineering inside ai-dev-workflow. Use for PRD/business-process analysis, requirements discovery, value sorting, user stories, clarification, validation, PRD/spec generation, API contract drafting, and static requirements-driven prototypes when an external requirements-analyst power/skill is unavailable.
---

# Bundled Requirements Analyst Provider

This provider is bundled with `ai-dev-workflow` so phase 01 and phase 03 do not depend on a separately installed `requirements-analyst` power.


## Fidelity tier

This provider is intended to be `BUNDLED_SOURCE_SLICE`, not a loose rewrite. To claim requirements-analyst capability for a phase, load and use the relevant source-derived steering/templates under `references/steering/`.

If the agent only follows the short summary in this file and does not load the required steering/template files for the active subtask, record the run as `COMPACT_FALLBACK` / `DONE_DEGRADED` instead of full requirements-analyst output.

## When used by ai-dev-workflow

- Phase 01 Requirements: produce deep provider-native requirements artifacts under `.ai-workflow/<feature>/requirements/`.
- Phase 03 Prototype: produce requirements-driven static prototype artifacts under `.ai-workflow/<feature>/prototype/`.
- Fallback when an external `requirements-analyst` is unavailable.

## Required workflow contract

Always obey the parent `ai-dev-workflow` artifact contract. This provider supplies method depth; it does not own phase gates or artifact locations.

For phase 01, produce or update:

- `requirements/discovery.md`
- `requirements/sort.md`
- `requirements/requirements.md`
- `requirements/datamodel.md`
- `requirements/clarification.md`
- `requirements/validation.md`
- `requirements/prd.md`
- `requirements/open-questions.md`
- `requirements/traceability.md`
- `requirements/api.yaml` when an API/service boundary exists; otherwise explicitly mark API not applicable.
- `01_REQUIREMENTS.md` as summary/index/gate only.

Phase 01 must preserve the requirements-analyst order:

1. Discovery
2. Value sorting
3. Requirements analysis
4. Clarification
5. Validation
6. Specification / PRD

Do not create or update `requirements/validation.md` as final validation while `requirements/open-questions.md` still contains blocking questions or `requirements/clarification.md` lacks explicit user/human answers. Writing recommendations, defaults, or assumed decisions into `clarification.md` is not clarification. If clarification is needed, ask the user before validation and before phase 02.

When asking clarification questions inside `ai-dev-workflow`, prefer a compact decision brief that groups related questions. One-question-at-a-time is allowed only if the user asks for that interaction style or the next answer materially changes the remaining questions. Every persisted decision must include provenance such as `用户确认：...` / `confirmed by user: ...`.

For phase 03, produce or update:

- `03_PROTOTYPE.md`
- `prototype/index.html`
- `prototype/css/style.css`
- `prototype/pages/*.html`
- traceability updates linking pages to requirements/user stories.

## Method references

Load only the reference needed for the current subtask:

- Core interaction rules: `references/steering/00-interaction-protocol.md`
- Discovery: `references/steering/phase1-requirements-discovery.md`
- Value sorting: `references/steering/phase2-requirements-value-sorting.md`
- Requirements analysis/user stories: `references/steering/phase3-requirements-analysis.md`
- Clarification: `references/steering/phase4-requirements-clarification.md`
- Validation: `references/steering/phase5-requirements-validation.md`
- PRD/specification: `references/steering/phase6-requirements-specification.md`
- Reverse requirements: `references/steering/command-reverse.md`
- Prototype: `references/steering/command-prototype.md`
- API/OpenAPI contract: `references/steering/template-openapi.md`

Original source format is preserved at `references/POWER.md` for compatibility and audit.

## Quality bar

Do not compress the provider output into short tables. Preserve requirements-analyst depth: personas, activities, story map or equivalent flow breakdown, detailed user stories, acceptance criteria, INVEST/equivalent checks, entities, state transitions, permissions, edge cases, non-functional requirements, and validation scenarios.

Full requirements-analyst quality is output-gated, not just provider-availability-gated. Before marking phase 01 full `DONE`, run `scripts/validate_artifacts.py <workflow-dir> --gate 01-full`. Before entering implementation from prototype, run `scripts/validate_artifacts.py <workflow-dir> --gate 03-full`. If either gate fails, expand the source-derived artifacts or mark the phase `DONE_DEGRADED` / `NEEDS_REQUIREMENTS_DEPTH` instead of claiming full requirements-analyst fidelity.
