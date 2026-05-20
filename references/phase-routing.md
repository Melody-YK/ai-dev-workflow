# Phase Routing

## 00 Intake

Use this orchestrator. Do not invoke downstream skills yet. Normalize the request and create workflow artifacts.

## 01 Requirements

Use `requirements-analyst` when the source is a PRD, business process, product idea, or unclear requirement. Ask it to write into `01_REQUIREMENTS.md`, not only to chat.

Suggested handoff:

```text
Read <workflow>/00_INTAKE.md and the linked source PRD. Produce normalized requirements in <workflow>/01_REQUIREMENTS.md. Preserve open questions instead of guessing. Include actors, entities, state machine, permissions, functional requirements, non-functional requirements, acceptance criteria, and traceability notes.
```

## 02 Product & Engineering Review

Use gstack-style review after requirements exist. Do not let it replace the requirements artifact. Ask it to challenge and refine the build plan.

Suggested handoff:

```text
Read <workflow>/01_REQUIREMENTS.md and source PRD. Perform product scope review and engineering review. Write <workflow>/02_TECHNICAL_DESIGN.md with recommended MVP, non-goals, architecture, data model direction, state transitions, APIs/integrations, risks, and test matrix. Surface decisions for human approval.
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
Read <workflow>/01_REQUIREMENTS.md, <workflow>/02_TECHNICAL_DESIGN.md, and the source PRD. First write a prototype plan into <workflow>/03_PROTOTYPE.md with pages, source requirements, user flows, mock data, and out-of-scope items. Wait for approval before generating pages. After approval, create <workflow>/prototype/index.html, <workflow>/prototype/css/style.css, and one HTML file per flow under <workflow>/prototype/pages/. Keep it pure static HTML/CSS unless Level 2 is explicitly approved.
```

## 04 Implementation

Use superpowers after design and prototype approval. First write a plan, then execute only after approval unless the user asks for unattended execution.

Suggested handoff:

```text
Read <workflow>/02_TECHNICAL_DESIGN.md, <workflow>/03_PROTOTYPE.md, and the approved prototype if present. Create an implementation plan in <workflow>/04_IMPLEMENTATION.md with small TDD-oriented tasks, exact files, commands, expected results, and checkpoints. Do not implement until approved.
```

## 05 Verification

Use superpowers verification and optional gstack review/qa depending on project type.

Suggested handoff:

```text
Review the implementation against <workflow>/01_REQUIREMENTS.md, <workflow>/02_TECHNICAL_DESIGN.md, and <workflow>/03_PROTOTYPE.md. Run available tests/build/lint/manual QA. Write evidence, issues, fixes, prototype coverage, and release readiness to <workflow>/05_REVIEW.md.
```
