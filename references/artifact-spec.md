# Artifact Spec

## Core principle

Capability providers may vary; workflow artifact contracts stay stable.

AI Dev Workflow defines artifact locations, status fields, handoff rules, and gates. Provider-native rich outputs are allowed when useful, but they must live inside the workflow directory and be indexed by the relevant phase summary/control artifact.

## STATUS.md

Required fields:

- Feature
- Workflow directory
- Source PRD
- Current phase
- Checkpoint status
- Last updated
- Contract principle
- Phase table
- Detailed artifacts
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

Every phase summary/control artifact should include:

- Purpose
- Inputs
- Outputs or expected outputs
- Summary/details appropriate to phase
- Open questions or review feedback
- Approval or completion decision when applicable
- Completion checklist

Phase files are not required to contain every detailed provider output. Prefer linking to detailed artifacts when a provider produces richer structure.

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

## Requirements artifacts

Requirements use a summary/control file plus a detailed artifact directory.

Required files after requirements analysis:

```text
01_REQUIREMENTS.md
requirements/
├── reverse.md              # optional
├── discovery.md
├── sort.md
├── requirements.md
├── datamodel.md
├── clarification.md
├── validation.md
├── prd.md
├── api.yaml                # required when any API boundary exists; otherwise mark not-applicable
├── open-questions.md
└── traceability.md
```

Rules:

- `01_REQUIREMENTS.md` records purpose, inputs, provider contract, requirements sub-phase status, detailed artifact index, executive summary, key decisions/assumptions, open questions summary, handoff, and approval decision.
- Detailed provider-native requirements output should live under `requirements/` instead of being compressed into `01_REQUIREMENTS.md`.
- `requirements/open-questions.md` preserves ambiguity instead of guessing.
- `requirements/traceability.md` starts with PRD-to-requirement mapping and can be extended later with design, prototype, implementation, and verification links.
- `requirements/api.yaml` is the workflow-owned API contract when any frontend/backend, client/server, service-to-service, or external HTTP boundary exists. It is not optional in those projects. If no API boundary exists, keep the file and mark it not-applicable with the reason.
- Each API operation should include method, path, auth/security, request shape, response shape, owner, traceability to requirement/prototype, and status (`planned`, `approved`, `implemented`, `verified`, `deferred`, or `rejected`).
- Additional files under `requirements/` are allowed if they improve handoff quality and are linked from `01_REQUIREMENTS.md`.

## Review artifacts

02 Product & Engineering Review uses a summary/control file plus provider-native review notes.

Required files after 02 review:

```text
02_TECHNICAL_DESIGN.md
reviews/
├── product-review.md
├── engineering-review.md
├── security-risk-review.md
└── qa-review.md
```

Rules:

- `02_TECHNICAL_DESIGN.md` records the executive summary, recommended delivery scope, non-goals, key decisions, architecture/design summary, risk summary, QA strategy summary, traceability updates, human decisions, and approval gate.
- Human decisions must be written as comparable decision briefs. Every option must include applicability, benefits, costs/tradeoffs, and downstream impact. Recommended options may have extra rationale, but non-recommended options must not be blank.
- Detailed gstack-style review output should live under `reviews/` instead of being compressed into `02_TECHNICAL_DESIGN.md`.
- Review notes must challenge and decide; they should not merely restate requirements.
- If an API boundary exists, 02 must review and freeze/update `requirements/api.yaml`; a prose statement such as “API aligned” is insufficient without operation-level contract evidence.
- If 02 changes, defers, or rejects requirements, `requirements/traceability.md` must be updated truthfully.

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

## Implementation artifacts

04 Implementation uses a workflow summary/control file plus a provider-native deep implementation plan.

Required files after implementation planning:

```text
04_IMPLEMENTATION.md
implementation/
└── IMPLEMENTATION_PLAN.md
```

Rules:

- 04 does not rerun full brainstorming by default. 01/02/03 own requirements clarification, option review, decision confirmation, and prototype validation.
- 04 may perform only a lightweight pre-plan sanity check to identify blockers that would prevent implementation planning.
- If no blocker exists, the provider should proceed directly to superpowers-style `writing-plans`.
- `implementation/IMPLEMENTATION_PLAN.md` is the authoritative deep implementation plan. It should preserve small executable units, file-level tasks, test/verification-first order, per-step commands, pass criteria, failure handling, risks, rollback/recovery notes, and traceability.
- `04_IMPLEMENTATION.md` is the workflow summary/control artifact: it indexes the deep plan, records gates, status, execution log, verification evidence, changed files, blockers, and approval decisions.
- Do not compress provider-native deep planning output into `04_IMPLEMENTATION.md` tables. Summaries are allowed only if they link to the full plan.
- A module outline alone is not sufficient. Each implementation unit should state traceability, files, test/verification-first step, expected initial result, implementation action, commands, pass criteria, and failure handling.
- If an API boundary exists, implementation must keep backend routes and frontend/client calls aligned with `requirements/api.yaml`. 04 must record a route/client/contract parity check before claiming implementation done.

## Verification artifacts

05 Verification & Review is evidence-driven. The agent must infer the verification checklist from workflow artifacts, not from a long user prompt.

Rules:

- Read 01/02/03/04 artifacts, `implementation/IMPLEMENTATION_PLAN.md`, approved prototype files, implementation diff, and current code.
- Run available test / build / lint / typecheck commands; record unavailable commands with reason and impact.
- Check requirements coverage, prototype coverage, role/permission coverage, state transitions, core paths, exception paths, API contract consistency, and release readiness.
- If an API boundary exists, compare `requirements/api.yaml` with backend route inventory and frontend/client API calls. Any mismatch must be recorded as an issue; mismatches blocking core pages or flows prevent a Ready conclusion.
- If a frontend exists, run browser smoke/manual QA and record network/console evidence. Backend-only scripts cannot prove frontend usability.
- At minimum, validate or explicitly mark not-applicable: create ticket, submit, three-level audit, dispatch, execute, verify/archive, reject, cancel, suspend, unauthorized access.
- `05_REVIEW.md` must include evidence, issues, severity, reproduction or inspection basis, suggested fix or disposition, remaining risk, and release recommendation.
- Do not add major new features in 05. If feature gaps are found, record them as issues or blockers unless the user explicitly approves implementation work.
