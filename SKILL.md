---
name: ai-dev-workflow
description: Orchestrate a lightweight, artifact-driven AI development workflow from PRD/intake through requirements analysis, product/engineering review, static prototype generation, implementation planning, build, and verification. Use when the user wants to run requirements-analyst, gstack, and superpowers together in a controlled workflow, create .ai-workflow artifacts, generate a requirements-driven prototype, or test an AI development process on a PRD.
---

# AI Dev Workflow

Run a controlled, artifact-driven software development workflow. This skill is an orchestrator: it does not copy the work of `requirements-analyst`, `gstack`, or `superpowers`; it routes phases, manages artifacts, and enforces human checkpoints.

## Core rule

Use files as the interface between phases. Do not rely on chat history as the source of truth.

Default workspace for a feature:

```text
.ai-workflow/<feature-slug>/
├── 00_INTAKE.md
├── 01_REQUIREMENTS.md
├── 02_TECHNICAL_DESIGN.md
├── 03_PROTOTYPE.md
├── prototype/
│   ├── index.html
│   ├── css/
│   │   └── style.css
│   └── pages/
├── 04_IMPLEMENTATION.md
├── 05_REVIEW.md
└── STATUS.md
```

## When starting a workflow

1. Identify the source PRD or intake text.
2. Create a feature slug from the product/feature name.
3. Initialize artifacts from `assets/templates/`.
4. Copy or summarize the source PRD into `00_INTAKE.md` with a pointer to the original file.
5. Set `STATUS.md` to phase `01_REQUIREMENTS` and checkpoint `WAITING_FOR_HUMAN_CONFIRMATION`.
6. Ask the user whether to run the next phase.

If the user explicitly asks to continue without stopping, proceed, but still update `STATUS.md` at each phase boundary.

## Phase routing

| Phase | Purpose | Primary capability | Default tool/skill |
|---|---|---|---|
| 00 Intake | Capture source request and constraints | Intake normalization | This orchestrator |
| 01 Requirements | Turn request into explicit requirements/spec | Requirements analysis | `requirements-analyst` |
| 02 Product & Engineering Review | Challenge scope and produce technical design | Product/architecture review | `gstack` concepts: office-hours, plan-ceo-review, plan-eng-review |
| 03 Prototype | Generate a requirements-driven static prototype | Prototype planning and static HTML/CSS generation | `requirements-analyst` prototype approach |
| 04 Implementation | Write plan and build with discipline | TDD execution | `superpowers`: writing-plans, subagent-driven-development or executing-plans |
| 05 Verification & Review | Prove the result works | Verification/review/QA | `superpowers` verification + optional `gstack` review/qa |

Read `references/phase-routing.md` when deciding which capability to invoke. Read `references/capability-contracts.md` when writing handoff prompts. Read `references/artifact-spec.md` when creating or validating artifacts.

## Prototype rules

Default Prototype is Level 1:

- Pure static HTML + CSS.
- Open `prototype/index.html` directly in a browser.
- No JavaScript unless the user explicitly approves Level 2 interactive prototype.
- No CDN, backend, build tools, or CSS frameworks.
- Generate a prototype plan first, then pages one at a time.
- `prototype/index.html` is the navigation hub.
- All other HTML files go under `prototype/pages/`.
- Map every page back to requirements/user stories.

## Human gates

Pause after each phase unless the user says to run unattended:

- After 00: confirm the normalized intake.
- After 01: confirm requirements and unresolved questions.
- After 02: confirm design decisions and prototype scope.
- After 03: confirm prototype approval or requested changes.
- After 04 planning: confirm whether to execute.
- After 05: confirm accept/rework/retro.

## Quality gates

Before moving to the next phase, check:

- Required artifact exists and has no unresolved `TBD` unless listed in Open Questions.
- Decisions are recorded in `STATUS.md`.
- Inputs consumed and outputs produced are listed.
- The next phase has a clear handoff prompt.
- Prototype approval is recorded before implementation unless explicitly skipped.

Use `scripts/validate_artifacts.py <workflow-dir>` for a basic structural check. Use `--require-prototype-files` after prototype generation.

## Output style

Report concisely:

- Created/updated files
- Current phase
- Blockers or open decisions
- Exact next action the user can approve
