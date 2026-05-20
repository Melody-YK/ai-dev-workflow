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

## 03 Implementation Planning & Build

**Input**
- `02_TECHNICAL_DESIGN.md`
- Codebase context

**Capability needed**
- Convert design into small implementation tasks.
- Prefer TDD for behavior changes.
- Execute with clear file paths, commands, and verification.

**Default provider**
- `superpowers`: writing-plans, test-driven-development, subagent-driven-development or executing-plans.

**Output**
- `03_IMPLEMENTATION.md`
- Code changes
- Test results

**Done when**
- Plan is executable, implementation is complete or blockers are explicit, and verification commands have been run.

## 04 Verification & Review

**Input**
- Implementation diff
- `01_REQUIREMENTS.md`
- `02_TECHNICAL_DESIGN.md`
- `03_IMPLEMENTATION.md`

**Capability needed**
- Verify requirements coverage.
- Run tests/lint/build/manual QA as applicable.
- Review code quality and production readiness.

**Default provider**
- `superpowers`: verification-before-completion, requesting-code-review.
- Optional `gstack`: review, qa, cso.

**Output**
- `04_REVIEW.md`

**Done when**
- Evidence is recorded and remaining risks are classified as accepted, fixed, or blocked.
