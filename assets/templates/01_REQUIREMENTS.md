# 01 Requirements — {{FEATURE_NAME}}

## Purpose

Normalize the intake/PRD into detailed requirements artifacts that downstream product review, prototype, implementation, and verification phases can trust.

This file is the workflow-level summary and control artifact for phase 01. It does not replace the native detailed outputs of `requirements-analyst`; it indexes them, records decisions, and defines the handoff contract.

## Inputs

- `00_INTAKE.md`
- Source PRD: `{{SOURCE_PRD}}`

## Provider contract

Default provider: `requirements-analyst`.

Use `requirements-analyst` as the analysis method, not as a competing workflow owner. Preserve its rich detailed outputs under `requirements/`, then summarize and link them from this file.

Do not compress all requirements analysis into this summary file if richer provider-native artifacts are useful.

## Expected detailed artifacts

Create or update these files during phase 01:

```text
requirements/
├── reverse.md              # optional, for existing codebases
├── discovery.md
├── sort.md
├── requirements.md
├── datamodel.md
├── clarification.md
├── validation.md
├── prd.md
├── api.yaml                # optional
├── open-questions.md
└── traceability.md
```

Minimum expectations:

| Artifact | Purpose | Status |
|---|---|---|
| `requirements/reverse.md` | Optional reverse analysis from existing code when docs are missing | Optional |
| `requirements/discovery.md` | Raw goals, stakeholders, constraints, and success criteria | Planned |
| `requirements/sort.md` | Value sorting, priority, MVP fit, and dependency notes | Planned |
| `requirements/requirements.md` | Detailed actors, goals, user stories, flows, functional and non-functional requirements | Planned |
| `requirements/datamodel.md` | Domain entities, relationships, key fields, lifecycle states, permissions-relevant data | Planned |
| `requirements/clarification.md` | Ambiguities, assumptions, stakeholder decisions, and resolved questions | Planned |
| `requirements/validation.md` | Acceptance criteria, validation rules, testable scenarios, edge cases, and quality checks | Planned |
| `requirements/prd.md` | Formalized PRD/specification after validation | Planned |
| `requirements/api.yaml` | Optional OpenAPI/API sketch when useful | Optional |
| `requirements/open-questions.md` | Ambiguities and decisions that require human confirmation | Planned |
| `requirements/traceability.md` | Mapping from source PRD items to requirements, prototype pages, implementation tasks, and verification evidence | Planned |

Additional provider-native files are allowed if they improve handoff quality. Link them here and record why they exist.

## Executive summary

_To be completed after detailed requirements artifacts are produced._

## Key decisions and assumptions

_To be completed during requirements analysis. Mark assumptions clearly and move human decisions into Open Questions when uncertain._

## Open questions summary

See `requirements/open-questions.md` for details.

- [ ] TBD

## Handoff to product & engineering review

Downstream phases must read this file plus the detailed artifacts under `requirements/`. Do not rely only on this summary.

Required handoff inputs for phase 02:

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
- Source PRD: `{{SOURCE_PRD}}`

## Approval decision

- Status: TBD
- Approved by:
- Decision notes:

## Completion checklist

- [ ] Detailed requirements artifacts exist under `requirements/`
- [ ] Requirements are explicit and testable
- [ ] Domain entities and lifecycle states are documented
- [ ] Validation and acceptance criteria are documented
- [ ] Open questions are recorded instead of guessed
- [ ] Traceability back to source PRD is started
- [ ] Human approved requirements before product & engineering review
