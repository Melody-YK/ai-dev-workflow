# Artifact Spec

## STATUS.md

Required fields:

- Feature
- Workflow directory
- Source PRD
- Current phase
- Checkpoint status
- Last updated
- Phase table
- Decisions
- Open questions
- Next action

Checkpoint statuses:

- `NOT_STARTED`
- `IN_PROGRESS`
- `WAITING_FOR_HUMAN_CONFIRMATION`
- `BLOCKED`
- `DONE`

## Phase files

Every phase artifact should include:

- Purpose
- Inputs
- Outputs
- Summary
- Details appropriate to phase
- Open questions
- Completion checklist

## Naming

Use uppercase two-digit phase prefixes:

- `00_INTAKE.md`
- `01_REQUIREMENTS.md`
- `02_TECHNICAL_DESIGN.md`
- `03_IMPLEMENTATION.md`
- `04_REVIEW.md`

Feature slug rules:

- lowercase ASCII
- words separated by hyphen
- derived from product/feature name
