# Phase Routing

Core routing rule:

> Use provider skills as capability providers, not as owners of the workflow format.

AI Dev Workflow owns the artifact locations, handoff rules, status updates, and human gates. Provider-native rich outputs are welcome when useful, but they must live inside the workflow directory and be indexed by the phase summary/control artifact.

## 00 Intake

Use this orchestrator. Do not invoke downstream skills yet. Normalize the request and create workflow artifacts.

## 01 Requirements

Use `requirements-analyst` when the source is a PRD, business process, product idea, or unclear requirement.

Do not force all requirements output into one file. Preserve useful `requirements-analyst`-style detailed outputs under `requirements/`, and use `01_REQUIREMENTS.md` as the summary, index, approval, and handoff artifact.

Suggested handoff:

```text
Read <workflow>/00_INTAKE.md and the linked source PRD.
Use requirements-analyst as the analysis method, not as a competing output template.

Important quality rule:
<workflow>/requirements/requirements.md is the provider-native full requirements analysis document. It should be comparable in depth to running requirements-analyst directly, not a short summary table.

Produce detailed requirements artifacts under <workflow>/requirements/:
- discovery.md for stakeholder discovery, raw goals, constraints, success criteria, and initial scope.
- sort.md for prioritization and delivery-scope reasoning.
- requirements.md as the full native requirements-analysis document, including personas, activity/user-flow diagrams, story map, detailed user stories, acceptance criteria, INVEST or equivalent quality checks, functional/non-functional requirements, roles/permissions, edge cases, and constraints.
- datamodel.md for entities, relationships, key fields, lifecycle states, and data constraints.
- clarification.md for resolved ambiguities, assumptions, and stakeholder decisions.
- validation.md for acceptance criteria, validation rules, testable scenarios, consistency checks, and requirement quality checks.
- prd.md for the formalized specification distilled from the full analysis.
- open-questions.md for ambiguities that require human confirmation.
- traceability.md for mapping source PRD items to requirements.
Then update <workflow>/01_REQUIREMENTS.md with only an executive summary, links to the detailed artifacts, key assumptions, open question summary, handoff notes, and approval status.
Preserve open questions instead of guessing.
Do not mark phase 01 DONE if requirements/requirements.md is much thinner than a direct requirements-analyst output.
```

## 02 Product & Engineering Review

Use gstack-style review after requirements exist. Do not let it replace the requirements artifacts. Ask it to act as product, engineering, security/risk, and QA reviewer. See `references/provider-contracts/gstack-review.md`.

Suggested handoff:

```text
Read <workflow>/01_REQUIREMENTS.md, all files under <workflow>/requirements/, and the source PRD.
Perform product review, engineering review, security/risk review, and QA review.
Write <workflow>/02_TECHNICAL_DESIGN.md with recommended current delivery scope, non-goals, product review, engineering review, architecture, data model direction, state transitions, APIs/integrations, risk register, and QA/test matrix.
If the review accepts, changes, defers, or rejects important requirements, update <workflow>/requirements/traceability.md or record the needed update in 02_TECHNICAL_DESIGN.md.
Surface decisions for human approval.
```

## 03 Prototype

Use prototype generation after requirements and product/engineering review exist. Follow the `requirements-analyst` prototype discipline: static files, prototype plan first, page generation one at a time, and page-to-requirement mapping.

Default Level 1 prototype:

- HTML + CSS only.
- No JavaScript.
- No CDN, backend, build tool, or CSS framework.
- `prototype/index.html` is the navigation hub.
- All other pages go under `prototype/pages/`.
- Use local shared CSS at `prototype/css/style.css`.

Use Level 2 interactive prototype only if the user explicitly approves it.

Suggested handoff:

```text
Read <workflow>/01_REQUIREMENTS.md, <workflow>/requirements/requirements.md, <workflow>/requirements/datamodel.md, <workflow>/requirements/clarification.md, <workflow>/requirements/validation.md, <workflow>/requirements/prd.md, <workflow>/02_TECHNICAL_DESIGN.md, and the source PRD.
First write a prototype plan into <workflow>/03_PROTOTYPE.md with pages, source requirements, user flows, mock data, and out-of-scope items.
Wait for approval before generating pages.
After approval, create <workflow>/prototype/index.html, <workflow>/prototype/css/style.css, and one HTML file per flow under <workflow>/prototype/pages/.
Keep it pure static HTML/CSS unless Level 2 is explicitly approved.
Map pages back to requirements/user stories and update traceability when useful.
```

## 04 Implementation

Use superpowers after design and prototype approval. See `references/provider-contracts/superpowers-execution.md`. First write a plan, then execute only after approval unless the user asks for unattended execution.

Suggested handoff:

```text
Read <workflow>/02_TECHNICAL_DESIGN.md, <workflow>/03_PROTOTYPE.md, the approved prototype if present, and the detailed requirements artifacts under <workflow>/requirements/.
Create an implementation plan in <workflow>/04_IMPLEMENTATION.md with small TDD-oriented tasks, exact files, commands, expected results, checkpoints, rollback/recovery notes, and traceability updates.
Do not implement until approved. If execution is approved, update execution log, changed files, verification commands, and blockers as work proceeds.
```

## 05 Verification

Use superpowers verification and optional gstack review/QA/risk review depending on project type. See `references/provider-contracts/superpowers-execution.md` and `references/provider-contracts/gstack-review.md`.

Suggested handoff:

```text
Review the implementation against <workflow>/01_REQUIREMENTS.md, the detailed requirements artifacts under <workflow>/requirements/, <workflow>/02_TECHNICAL_DESIGN.md, and <workflow>/03_PROTOTYPE.md.
Run available tests/build/lint/manual QA.
Perform or request code/architecture review and risk/QA review when useful.
Write evidence, issues, fixes, prototype coverage, risk classification, and release readiness to <workflow>/05_REVIEW.md.
Update <workflow>/requirements/traceability.md with verification evidence when useful.
```
