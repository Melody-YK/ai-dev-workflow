# AI Dev Workflow

AI Dev Workflow is a lightweight, artifact-first orchestrator skill for controlled AI software development workflows.

It turns a PRD or raw feature request into a staged development pipeline:

```text
PRD → Requirements → Product & Engineering Review → Implementation → Verification
```

The workflow is designed around fixed artifacts, human checkpoints, and replaceable capability providers such as `requirements-analyst`, gstack-style review, and `superpowers`.

## Why this exists

AI coding agents are powerful, but unmanaged workflows easily become chat-driven, context-heavy, and hard to resume.

This project keeps the process controllable by making each phase produce a durable file that the next phase consumes.

## Core principles

- **Artifact-first**: phase outputs are saved as files, not buried in chat history.
- **Human-gated**: each major phase pauses for review by default.
- **Capability-based**: phases depend on capability contracts, not permanent vendor/tool choices.
- **Replaceable skills**: `requirements-analyst`, gstack-style review, and `superpowers` are defaults, not hard dependencies.
- **Small first**: no complex state machine until real usage proves it is needed.

## Default workflow

```text
00 Intake
01 Requirements
02 Product & Engineering Review
03 Implementation Planning & Build
04 Verification & Review
```

Default artifact directory:

```text
.ai-workflow/<feature-slug>/
├── 00_INTAKE.md
├── 01_REQUIREMENTS.md
├── 02_TECHNICAL_DESIGN.md
├── 03_IMPLEMENTATION.md
├── 04_REVIEW.md
└── STATUS.md
```

## Skill routing

| Phase | Purpose | Default capability |
|---|---|---|
| 00 Intake | Capture source request and initialize artifacts | `ai-dev-workflow` |
| 01 Requirements | Convert PRD into explicit requirements | `requirements-analyst` |
| 02 Product & Engineering Review | Challenge scope, define MVP, review architecture | gstack-style review |
| 03 Implementation | Plan and build with TDD discipline | `superpowers` |
| 04 Verification & Review | Prove the result works | `superpowers` + optional gstack QA/review |

## Quick start

Initialize a workflow for a PRD:

```bash
python3 scripts/init_workflow.py \
  --project-root "/path/to/project" \
  --source-prd "/path/to/project/PRD.md" \
  --feature "feature-name"
```

Validate required artifacts:

```bash
python3 scripts/validate_artifacts.py "/path/to/project/.ai-workflow/<feature-slug>"
```

Print current workflow status:

```bash
python3 scripts/status.py "/path/to/project/.ai-workflow/<feature-slug>"
```

## Usage

See [USAGE.md](USAGE.md) for the full Chinese usage guide.

## Evaluation

See [EVALUATION.md](EVALUATION.md) for the rubric used to judge whether a workflow run is clear, resumable, executable, and verifiable.

## Repository layout

```text
ai-dev-workflow/
├── SKILL.md
├── USAGE.md
├── references/
│   ├── workflow-overview.md
│   ├── capability-contracts.md
│   ├── phase-routing.md
│   └── artifact-spec.md
├── assets/templates/
└── scripts/
```

## Current status

This is an early MVP intended for real workflow testing. The first goal is to validate whether the artifacts and phase gates produce better AI development handoffs.

## License

MIT
