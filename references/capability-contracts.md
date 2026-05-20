# Capability Contracts

Use these contracts to route work to any suitable skill or agent.

## 01 Requirements Analysis

**Input**
- `00_INTAKE.md`
- Source PRD or raw request
- Existing project context if available

**Capability needed**
- Discover actors, goals, constraints, entities, flows, states, permissions, edge cases, and acceptance criteria.
- Identify ambiguity and ask/record clarification questions.
- Produce a normalized requirements artifact.

**Default provider**
- `requirements-analyst`

**Output**
- `01_REQUIREMENTS.md`
- Optional linked artifacts: PRD, RTM, API sketch, data model, validation notes.

**Done when**
- Actors, workflows, states, data entities, permissions, functional requirements, non-functional requirements, and open questions are explicit.

## 02 Product & Engineering Review

**Input**
- `01_REQUIREMENTS.md`
- Source PRD
- Existing codebase constraints

**Capability needed**
- Challenge scope and product wedge.
- Recommend MVP boundaries.
- Produce architecture, data model direction, state machine, integration plan, risks, and test strategy.

**Default provider**
- `gstack` review concepts: office-hours, plan-ceo-review, plan-eng-review.

**Output**
- `02_TECHNICAL_DESIGN.md`

**Done when**
- Build scope, non-goals, architecture, interfaces, risks, test matrix, and human decisions are recorded.

## 03 Prototype

**Input**
- `01_REQUIREMENTS.md`
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

**Done when**
- Evidence is recorded and remaining risks are classified as accepted, fixed, deferred, or blocked.
