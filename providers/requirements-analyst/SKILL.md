---
name: requirements-analyst
description: Bundled provider for requirements engineering inside ai-dev-workflow. Use for PRD/business-process analysis, requirements discovery, value sorting, user stories, clarification, validation, PRD/spec generation, API contract drafting, and static requirements-driven prototypes when an external requirements-analyst power/skill is unavailable.
---

# Bundled Requirements Analyst Provider

This provider is bundled with `ai-dev-workflow` so phase 01 and phase 03 do not depend on a separately installed `requirements-analyst` power.

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
