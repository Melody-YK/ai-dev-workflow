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

## 03 Implementation

Use superpowers after design approval. First write a plan, then execute only after approval unless the user asks for unattended execution.

Suggested handoff:

```text
Read <workflow>/02_TECHNICAL_DESIGN.md. Create an implementation plan in <workflow>/03_IMPLEMENTATION.md with small TDD-oriented tasks, exact files, commands, expected results, and checkpoints. Do not implement until approved.
```

## 04 Verification

Use superpowers verification and optional gstack review/qa depending on project type.

Suggested handoff:

```text
Review the implementation against <workflow>/01_REQUIREMENTS.md and <workflow>/02_TECHNICAL_DESIGN.md. Run available tests/build/lint/manual QA. Write evidence, issues, fixes, and release readiness to <workflow>/04_REVIEW.md.
```
