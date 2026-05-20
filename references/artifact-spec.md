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
- Outputs or expected outputs
- Summary/details appropriate to phase
- Open questions or review feedback
- Completion checklist

## Naming

Use uppercase two-digit phase prefixes:

- `00_INTAKE.md`
- `01_REQUIREMENTS.md`
- `02_TECHNICAL_DESIGN.md`
- `03_PROTOTYPE.md`
- `04_IMPLEMENTATION.md`
- `05_REVIEW.md`

Feature slug rules:

- lowercase ASCII
- words separated by hyphen
- derived from product/feature name

## Prototype artifact

Prototype is a first-class phase artifact, not an implementation shortcut.

Required files after prototype generation:

```text
prototype/
├── index.html
├── css/
│   └── style.css
└── pages/
    └── <flow-page>.html
```

Prototype rules:

- `03_PROTOTYPE.md` records the prototype plan, page-to-requirement mapping, mock data, review feedback, and approval decision.
- `prototype/index.html` is the entry page and navigation hub.
- `prototype/css/style.css` contains local shared styles.
- `prototype/pages/*.html` contains flow/page screens.
- All links must be relative.
- Default prototype uses HTML + CSS only.
- No JavaScript, CDN, backend, build tools, or CSS frameworks unless explicitly approved.

Prototype approval should be recorded before implementation starts. If prototype is skipped, record the reason in `03_PROTOTYPE.md` and `STATUS.md`.
