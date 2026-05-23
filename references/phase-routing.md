# Phase Routing


## Language rule

The orchestrator owns user-visible language consistency. Detect the primary language from the user request and source PRD, then keep all phase summaries, decision briefs, checkpoint prompts, and artifact prose in that language. Provider-native skills may contain English instructions, but their mapped workflow outputs and assistant replies must be localized. Technical identifiers, file paths, commands, API operation IDs, and enum values may remain English.

Core routing rule:

> Use provider skills as capability providers, not as owners of the workflow format.

AI Dev Workflow owns the artifact locations, handoff rules, status updates, and human gates. Provider-native rich outputs are welcome when useful, but they must live inside the workflow directory and be indexed by the phase summary/control artifact.

## 00 Intake

Use this orchestrator. Normalize the request and create workflow artifacts.

Default/manual mode: do not invoke downstream skills yet; pause for confirmation before 01.

Guided-auto/continuous mode: 00 is not a hard human gate. After artifacts are initialized and provider preflight is recorded, immediately continue into 01. If 01 has blocking questions, ask them as a decision brief; do not ask a separate “是否进入 01” confirmation.

## 01 Requirements

Use `requirements-analyst` when the source is a PRD, business process, product idea, or unclear requirement. Before starting, verify that external `requirements-analyst` is available. If unavailable, use bundled `providers/requirements-analyst/SKILL.md`; update `STATUS.md` Provider health with the actual provider. If both external and bundled providers are unavailable, pause for user action. In fallback mode, preserve the same output depth and do not mark 01 as clean `DONE` unless the quality bar is met.

Do not force all requirements output into one file. Preserve useful `requirements-analyst`-style detailed outputs under `requirements/`, and use `01_REQUIREMENTS.md` as the summary, index, approval, and handoff artifact.

Full-fidelity gate: before marking 01 clean `DONE`, run `scripts/validate_artifacts.py <workflow> --gate 01-full`. If it fails, keep 01 as `NEEDS_REQUIREMENTS_DEPTH` / `DONE_DEGRADED` and either expand the provider-native artifacts or ask the user to accept degraded output. `EXTERNAL_FULL` means the real provider is available and used; it does not waive the output-depth gate.

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
- api.yaml as the workflow-owned OpenAPI/API contract when any API boundary exists; if no API boundary exists, keep it and mark not-applicable with the reason.
- open-questions.md for ambiguities that require human confirmation.
- traceability.md for mapping source PRD items to requirements.
Then update <workflow>/01_REQUIREMENTS.md with only an executive summary, links to the detailed artifacts, key assumptions, open question summary, handoff notes, and approval status.
Preserve open questions instead of guessing.
For guided-auto mode, do not merely list blocking open questions and wait for a separate phase-confirmation. Ask the user with a decision brief immediately: dynamic option count, recommended option with rationale when useful, and an “Other / custom” free-text option for every decision. Persist answers to clarification.md, open-questions.md, STATUS.md, and traceability.md when relevant. After the user answers, continue 01 automatically unless new blocking questions remain.
Do not mark phase 01 DONE if requirements/requirements.md is much thinner than a direct requirements-analyst output.
Run `scripts/validate_artifacts.py <workflow> --gate 01-full` before marking 01 DONE.
```

## 02 Product & Engineering Review

Use `gstack-adapter` after requirements exist when real external `garrytan/gstack` is installed. Invoke/map the relevant gstack slices (`/plan-ceo-review`, `/plan-eng-review`, optional `/plan-design-review`, `/plan-devex-review`, `/cso`, `/qa`) into workflow artifacts. If gstack is missing, `review-pack` may be used only as `COMPACT_FALLBACK`; do not mark the phase clean `DONE` unless the user explicitly accepts degraded depth. See `providers/gstack-adapter/references/gstack-mapping.md` and `references/provider-contracts/review-pack.md`.

Full-fidelity gate: before marking 02 clean `DONE`, run `scripts/validate_artifacts.py <workflow> --gate 02-full`. If it fails, do not claim full gstack quality. Keep the phase as `NEEDS_GSTACK_DEPTH`, `DONE_DEGRADED`, or `PROVIDER_DEGRADED` until full review notes and traceability updates exist. Phase 02 must update the primary `requirements/traceability.md` design column for reviewed feature rows; appending a short “评审决策追溯” section while the main matrix still says `TBD` is not sufficient.

Suggested handoff:

```text
Read <workflow>/01_REQUIREMENTS.md, all files under <workflow>/requirements/, and the source PRD.
Perform product review, engineering review, security/risk review, and QA review.
First write provider-native review notes:
- <workflow>/reviews/product-review.md
- <workflow>/reviews/engineering-review.md
- <workflow>/reviews/security-risk-review.md
- <workflow>/reviews/qa-review.md
Then write <workflow>/02_TECHNICAL_DESIGN.md as a workflow summary/control artifact with executive summary, recommended current delivery scope, non-goals, product review summary, engineering review summary, architecture, data model direction, state transitions, APIs/integrations, API contract review, risk register, and QA/test matrix. If an API boundary exists, review/update/freeze <workflow>/requirements/api.yaml; do not claim API alignment from prose alone.
If the review accepts, changes, defers, or rejects important requirements, update <workflow>/requirements/traceability.md, especially the primary feature table's design-decision column. Map core/MUST rows to concrete design modules, APIs, state transitions, permissions/security controls, and review decisions. Do not claim traceability was updated unless the main matrix cells actually changed from `TBD`.
Surface decisions for human approval.
Run `scripts/validate_artifacts.py <workflow> --gate 02-full` before marking 02 DONE.
```

## 03 Prototype

Use prototype generation after requirements and product/engineering review exist. Follow the `requirements-analyst` prototype discipline: static files, prototype plan first, page generation one at a time, and page-to-requirement mapping.

Full-fidelity gate: before entering 04, run `scripts/validate_artifacts.py <workflow> --gate 03-full`. If it fails, do not treat the prototype as approved/complete; update approval, actual page filenames, and traceability first.

Do not self-approve the prototype. In guided-auto, generating a complete prototype is not the same as receiving human approval to enter 04. If the artifact says `awaiting human approval`, `待确认`, or equivalent, keep 03 as waiting for approval and do not check “user approved prototype”.

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
Run `scripts/validate_artifacts.py <workflow> --gate 03-full` before entering 04.
If the gate fails because approval is pending, ask the user to approve/request changes; do not rewrite the artifact to fake approval.
```

## 04 Implementation

Use superpowers after design and prototype approval. See `references/provider-contracts/superpowers-execution.md`. First write a plan, then execute only after approval unless the user asks for unattended execution.

04 has two separate gates:

1. **Planning gate**: create/update `implementation/IMPLEMENTATION_PLAN.md` and `04_IMPLEMENTATION.md`; do not write product code yet.
2. **Execution gate**: only after explicit user approval or an explicit unattended-execution request may product code be changed. During execution, keep `04_IMPLEMENTATION.md` current; do not leave it as the template while code changes exist.

If code has already been changed but `04_IMPLEMENTATION.md` still has template rows, `TBD` approvals, empty execution logs, empty verification commands, or empty changed-file lists, the phase must be marked `BLOCKED_ARTIFACT_DRIFT` / not complete. Backfill evidence before entering 05; do not silently proceed.

Do not rerun full brainstorming by default. 01/02/03 already cover requirements clarification, option review, decision confirmation, and prototype validation. In 04, perform only a short pre-plan sanity check for blockers; if none exist, go directly to superpowers writing-plans.

Keep the provider-native deep plan separate from the workflow summary:

```text
implementation/IMPLEMENTATION_PLAN.md  # authoritative deep writing-plans output
04_IMPLEMENTATION.md                   # summary, gates, status, execution evidence
```

Do not compress the deep implementation plan into `04_IMPLEMENTATION.md` tables.

Suggested handoff:

```text
Read <workflow>/02_TECHNICAL_DESIGN.md, <workflow>/03_PROTOTYPE.md, the approved prototype if present, and the detailed requirements artifacts under <workflow>/requirements/.
Do a short pre-plan sanity check in <workflow>/04_IMPLEMENTATION.md, including whether <workflow>/requirements/api.yaml is present/applicable when an API boundary exists. If api.yaml is missing for an API-bearing project, enter API_CONTRACT_DEGRADED and either backfill a baseline contract before implementation or explicitly limit the work and use degraded terminology. If there are no implementation-planning blockers, create the authoritative deep implementation plan in <workflow>/implementation/IMPLEMENTATION_PLAN.md with small TDD-oriented tasks, exact files, commands, expected results, checkpoints, rollback/recovery notes, API contract parity checks including request/response schema, enum/required-field checks, semantic-risk notes, and traceability updates. Keep <workflow>/04_IMPLEMENTATION.md as the workflow summary/gate/evidence index.
Run `scripts/validate_artifacts.py <workflow> --gate 04-plan` before asking for implementation approval. Do not implement until approved. If execution is approved, update execution log, changed files, verification commands, and blockers as work proceeds. Before marking 04 complete or entering 05, run `scripts/validate_artifacts.py <workflow> --gate 04-complete`; if it fails, fix the artifacts or mark the phase blocked.
```

## 05 Verification

Use superpowers verification and optional `gstack-adapter` review/QA/risk review when real external gstack is installed. If only review-pack is available, record `COMPACT_FALLBACK` and degraded release confidence. See `references/provider-contracts/superpowers-execution.md`, `providers/gstack-adapter/references/gstack-mapping.md`, and `references/provider-contracts/review-pack.md`.

Suggested handoff:

```text
Enter 05 Verification & Review using the workflow contract. Do not rely on the user prompt to enumerate checks.
Read <workflow>/01_REQUIREMENTS.md, detailed artifacts under <workflow>/requirements/, <workflow>/02_TECHNICAL_DESIGN.md, <workflow>/03_PROTOTYPE.md, approved <workflow>/prototype/, <workflow>/04_IMPLEMENTATION.md, <workflow>/implementation/IMPLEMENTATION_PLAN.md, and the current implementation code.
Run available test/build/lint/typecheck/manual QA. If a command cannot run, record why and the impact.
Check requirement coverage, prototype/page/role/state coverage, core paths, exception paths, permissions, API contract/backend route/frontend client parity, browser smoke evidence levels where applicable, code/architecture risks, semantic side effects of fixes, and release readiness. If api.yaml is missing for an API-bearing project, mark API_CONTRACT_DEGRADED and perform route parity only without claiming complete contract parity. Before finishing, run a cross-artifact consistency scan over 05_REVIEW, STATUS, and traceability.
Write evidence, issues, fixes or recommendations, risk classification, and release readiness to <workflow>/05_REVIEW.md.
Update <workflow>/requirements/traceability.md with verification evidence when useful.
Before claiming verification complete, run `scripts/validate_artifacts.py <workflow> --gate 05-complete`. If the gate fails, the release recommendation must be `Blocked` or the missing evidence must be filled.
```
