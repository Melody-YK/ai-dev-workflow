# Capability Contracts

Use these contracts to route work to any suitable skill or agent.

Core principle:

> Capability providers may vary; workflow artifact contracts stay stable.

A provider may use its own analysis method and may preserve richer provider-native outputs, but it must write them into the workflow-defined locations and update the phase summary/control artifact.

## 01 Requirements Analysis

**Input**
- `00_INTAKE.md`
- Source PRD or raw request
- Existing project context if available

**Capability needed**
- Discover actors, goals, constraints, entities, flows, states, permissions, edge cases, and acceptance criteria.
- Identify ambiguity and ask/record clarification questions.
- Produce detailed requirements artifacts without compressing useful structure into a single summary.

**Default provider**
- `requirements-analyst`

**Output**
- `01_REQUIREMENTS.md` as the workflow-level summary, index, approval, and handoff artifact.
- `requirements/reverse.md` for optional reverse requirements from existing code.
- `requirements/discovery.md` for raw goals, stakeholders, constraints, and success criteria.
- `requirements/sort.md` for value sorting, priority, delivery-scope fit, and dependency notes.
- `requirements/requirements.md` for detailed requirements.
- `requirements/datamodel.md` for entities, relationships, states, and data constraints.
- `requirements/clarification.md` for ambiguity resolution and stakeholder decisions.
- `requirements/validation.md` for acceptance criteria, validation rules, scenarios, and edge cases.
- `requirements/prd.md` for the formalized PRD/specification.
- `requirements/open-questions.md` for unresolved questions.
- `requirements/traceability.md` for PRD-to-requirement mapping and later design/prototype/implementation/verification links.

Additional provider-native artifacts are allowed under `requirements/` if they improve handoff quality.

**Done when**
- Detailed requirements artifacts exist under `requirements/`.
- Actors, workflows, states, data entities, permissions, functional requirements, non-functional requirements, validation criteria, and open questions are explicit.
- `01_REQUIREMENTS.md` summarizes the outcome and links the detailed artifacts.
- Human approval or required changes are recorded.

## 02 Product & Engineering Review

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
- Challenge scope and product wedge.
- Recommend current delivery boundaries.
- Produce architecture, data model direction, state machine, integration plan, risks, and test strategy.

**Default provider**
- `gstack` review concepts: office-hours, plan-ceo-review, plan-eng-review.

**Output**
- `02_TECHNICAL_DESIGN.md`
- Updates to `requirements/traceability.md` when requirements are accepted, changed, deferred, or rejected.

**Done when**
- Build scope, non-goals, architecture, interfaces, risks, test matrix, and human decisions are recorded.
- Changes to requirements are reflected in traceability or open questions.

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

**Input**
- `02_TECHNICAL_DESIGN.md`
- `03_PROTOTYPE.md`
- Approved `prototype/` if generated
- Requirements artifacts under `requirements/`
- Codebase context

**Capability needed**
- Convert design and approved prototype into small implementation tasks.
- Prefer TDD for behavior changes.
- Execute with clear file paths, commands, and verification.

**Default provider**
- `superpowers`: writing-plans, test-driven-development, subagent-driven-development or executing-plans.

**Output**
- `04_IMPLEMENTATION.md`
- Code changes
- Test results

**Done when**
- Plan is executable, implementation is complete or blockers are explicit, and verification commands have been run.

## 05 Verification & Review

**Input**
- Implementation diff
- `01_REQUIREMENTS.md`
- Requirements artifacts under `requirements/`
- `02_TECHNICAL_DESIGN.md`
- `03_PROTOTYPE.md`
- `04_IMPLEMENTATION.md`

**Capability needed**
- Verify requirements coverage.
- Verify prototype coverage when applicable.
- Run tests/lint/build/manual QA as applicable.
- Review code quality and production readiness.

**Default provider**
- `superpowers`: verification-before-completion, requesting-code-review.
- Optional `gstack`: review, qa, cso.

**Output**
- `05_REVIEW.md`
- Updates to `requirements/traceability.md` with verification evidence when useful.

**Done when**
- Evidence is recorded and remaining risks are classified as accepted, fixed, deferred, or blocked.
