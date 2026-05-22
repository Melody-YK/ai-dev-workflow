# Capability Contracts

Use these contracts to route work to any suitable skill or agent.

Core principle:

> Capability providers may vary; workflow artifact contracts stay stable.

A provider may use its own analysis method and may preserve richer provider-native outputs, but it must write them into the workflow-defined locations and update the phase summary/control artifact.

## Provider availability and fallback

Before starting a phase, check whether the preferred provider is actually available in the current runtime. If not available:

- Run or equivalently perform `scripts/check_providers.py` and record provider health in `STATUS.md`.
- Do not keep the Provider column as if the unavailable provider executed the phase.
- Prefer bundled providers under `providers/` when external providers are unavailable.
- If no bundled provider exists, stop for user action.
- In fallback/adapter mode, document the fallback provider, quality risk, missing method-specific capabilities, and compensating checks.
- Do not mark a phase `DONE` if fallback output is shallower than the provider-native quality bar; use `DONE_DEGRADED`, `NEEDS_REVIEW`, or `BLOCKED`.

## 01 Requirements Analysis

**Input**
- `00_INTAKE.md`
- Source PRD or raw request
- Existing project context if available

**Capability needed**
- Discover actors, goals, constraints, entities, flows, states, permissions, edge cases, and acceptance criteria.
- Identify ambiguity and ask/record clarification questions.
- Produce a provider-native full requirements analysis under `requirements/requirements.md` without compressing useful structure into a short summary.
- Preserve requirements-analyst-style depth: personas, activity flows, user story map, detailed user stories, acceptance criteria, INVEST or equivalent checks, diagrams when useful, functional/non-functional requirements, roles/permissions, and edge cases.

**Default provider**
- `requirements-analyst`

**Output**
- `01_REQUIREMENTS.md` as the workflow-level summary, index, approval, and handoff artifact.
- `requirements/reverse.md` for optional reverse requirements from existing code.
- `requirements/discovery.md` for raw goals, stakeholders, constraints, and success criteria.
- `requirements/sort.md` for value sorting, priority, delivery-scope fit, and dependency notes.
- `requirements/requirements.md` for the full provider-native requirements analysis, comparable in depth to standalone `requirements-analyst` output.
- `requirements/datamodel.md` for entities, relationships, states, and data constraints.
- `requirements/clarification.md` for ambiguity resolution and stakeholder decisions.
- `requirements/validation.md` for acceptance criteria, validation rules, scenarios, and edge cases.
- `requirements/prd.md` for the formalized PRD/specification.
- `requirements/open-questions.md` for unresolved questions.
- `requirements/traceability.md` for PRD-to-requirement mapping and later design/prototype/implementation/verification links.

Additional provider-native artifacts are allowed under `requirements/` if they improve handoff quality.

**Done when**
- Detailed requirements artifacts exist under `requirements/`.
- `requirements/requirements.md` is a deep native requirements-analysis document, not a terse extracted summary.
- Actors, personas, workflows, story map or equivalent flow breakdown, detailed user stories, acceptance criteria, states, data entities, permissions, functional requirements, non-functional requirements, validation criteria, and open questions are explicit.
- `01_REQUIREMENTS.md` summarizes the outcome and links the detailed artifacts without replacing them.
- Human approval or required changes are recorded.

## 02 Product & Engineering Review

Detailed provider contract: `references/provider-contracts/review-pack.md`.

**Input**
- `01_REQUIREMENTS.md`
- `requirements/discovery.md`
- `requirements/sort.md`
- `requirements/requirements.md`
- `requirements/datamodel.md`
- `requirements/clarification.md`
- `requirements/validation.md`
- `requirements/prd.md`
- `requirements/open-questions.md`
- `requirements/traceability.md`
- Source PRD
- Existing codebase constraints

**Capability needed**
- Product review: challenge scope, user value, non-goals, and current delivery boundary.
- Engineering review: produce architecture, data model direction, state machine, APIs/integrations, migrations, and maintainability notes.
- Security/risk review: check permissions, auditability, data safety, abuse cases, compliance, and delivery risks.
- QA review: define acceptance scenarios, regression paths, manual QA, and test matrix.

**Default provider**
- `review-pack` internal concepts: product, engineering, security/risk, QA, and release review. External `garrytan/gstack` may be used only when installed and explicitly selected.

**Output**
- `02_TECHNICAL_DESIGN.md`
- Updates to `requirements/traceability.md` when requirements are accepted, changed, deferred, or rejected.

**Done when**
- Current delivery scope, non-goals, product review, engineering review, risk register, QA/test strategy, and human decisions are recorded.
- Changes to requirements are reflected in traceability or open questions.
- No blocking security, permission, audit, state-flow, or testing issue is left ownerless.

## 03 Prototype

**Input**
- `01_REQUIREMENTS.md`
- `requirements/requirements.md`
- `requirements/datamodel.md`
- `requirements/validation.md`
- `02_TECHNICAL_DESIGN.md`
- Source PRD if needed

**Capability needed**
- Convert requirements and user flows into a static prototype plan.
- Generate pure static HTML/CSS pages one at a time.
- Map pages to requirements/user stories.
- Use realistic mock data.
- Capture feedback and approval before implementation.

**Default provider**
- `requirements-analyst` prototype approach.
- Optional future providers: text-to-UI, wireframe-to-code, screenshot-to-code style generators, if they respect artifact and review gates.

**Output**
- `03_PROTOTYPE.md`
- `prototype/index.html`
- `prototype/css/style.css`
- `prototype/pages/*.html`
- Updates to `requirements/traceability.md` for page-to-requirement links when useful.

**Done when**
- Prototype plan is approved.
- Static prototype can be opened without server/build step.
- Page-to-requirement mapping is recorded.
- User approves prototype or explicitly skips prototype before implementation.

## 04 Implementation Planning & Build

Detailed provider contract: `references/provider-contracts/superpowers-execution.md`.

**Input**
- `02_TECHNICAL_DESIGN.md`
- `03_PROTOTYPE.md`
- Approved `prototype/` if generated
- Requirements artifacts under `requirements/`
- Codebase context and test framework

**Capability needed**
- `writing-plans`: convert design and approved prototype into small implementation tasks with files, commands, dependencies, expected results, and checkpoints.
- `test-driven-development`: define failing tests or verification scenarios before implementation when practical.
- `executing-plans`: execute in small steps and record deviations, blockers, and results.
- `subagent-driven-development`: optionally delegate isolated implementation sub-tasks while preserving the main workflow artifact contract.
- `verification-before-completion`: run tests/build/lint/manual checks before claiming completion.

**Default provider**
- `superpowers`: writing-plans, test-driven-development, subagent-driven-development or executing-plans.

**Output**
- `04_IMPLEMENTATION.md`
- Code changes
- Test results and verification logs
- Rollback/recovery notes when relevant

**Done when**
- Plan is executable and approved.
- Implementation is complete or blockers are explicit.
- Tests/verification have been run or exceptions are documented and approved.
- Changed files and requirement traceability are recorded.

## 05 Verification & Review

Detailed provider contracts:
- `references/provider-contracts/superpowers-execution.md`
- `references/provider-contracts/review-pack.md`

**Input**
- Implementation diff
- `01_REQUIREMENTS.md`
- Requirements artifacts under `requirements/`
- `02_TECHNICAL_DESIGN.md`
- `03_PROTOTYPE.md`
- `04_IMPLEMENTATION.md`

**Capability needed**
- `superpowers` verification-before-completion: verify requirements coverage, prototype coverage, and test/build/lint/manual QA evidence.
- `superpowers` requesting-code-review: request or simulate review, then record findings and fixes.
- Optional external `garrytan/gstack` review: release readiness, QA review, engineering review, security/risk review.

**Default provider**
- `superpowers`: verification-before-completion, requesting-code-review.
- Optional external `garrytan/gstack`: review, qa, cso/risk review.

**Output**
- `05_REVIEW.md`
- Updates to `requirements/traceability.md` with verification evidence when useful.

**Done when**
- Evidence is recorded for requirements, prototype, tests/build/lint, manual QA when applicable, and code/risk review.
- Remaining risks are classified as fixed, accepted, deferred, or blocked.
- Release readiness is Ready / Ready with accepted risks / Blocked.
- No blocking issue is marked as ready.
