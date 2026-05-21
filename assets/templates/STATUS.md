# Workflow Status — {{FEATURE_NAME}}

- Feature: {{FEATURE_NAME}}
- Workflow directory: `{{WORKFLOW_DIR}}`
- Source PRD: `{{SOURCE_PRD}}`
- Current phase: {{CURRENT_PHASE}}
- Checkpoint status: {{CHECKPOINT_STATUS}}
- Last updated: {{CREATED_AT}}

## Contract principle

AI Dev Workflow owns the phase contract, status, gates, and artifact locations. Capability providers such as `requirements-analyst`, gstack-style review, and `superpowers` provide methods and detailed outputs, but they do not replace the workflow contract.

## Phases

| Phase | Artifact | Status | Provider |
|---|---|---|---|
| 00 Intake | `00_INTAKE.md` | {{PHASE_00_STATUS}} | ai-dev-workflow |
| 01 Requirements | `01_REQUIREMENTS.md` + `requirements/` | {{PHASE_01_STATUS}} | requirements-analyst |
| 02 Product & Engineering Review | `02_TECHNICAL_DESIGN.md` | {{PHASE_02_STATUS}} | gstack-style review |
| 03 Prototype | `03_PROTOTYPE.md` + `prototype/` | {{PHASE_03_STATUS}} | requirements-driven prototype generation |
| 04 Implementation | `04_IMPLEMENTATION.md` | {{PHASE_04_STATUS}} | superpowers |
| 05 Verification & Review | `05_REVIEW.md` | {{PHASE_05_STATUS}} | superpowers + optional gstack |

## Detailed artifacts

### Requirements

- `requirements/discovery.md`
- `requirements/sort.md`
- `requirements/requirements.md`
- `requirements/datamodel.md`
- `requirements/clarification.md`
- `requirements/validation.md`
- `requirements/prd.md`
- `requirements/open-questions.md`
- `requirements/traceability.md`

## Decisions

- None yet.

## Open questions

- [ ] Confirm whether to continue to 01 Requirements.

## Next action

{{NEXT_ACTION}}
