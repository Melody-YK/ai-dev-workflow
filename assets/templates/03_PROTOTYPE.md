# 03 Prototype — {{FEATURE_NAME}}

## Purpose

Create a requirements-driven static prototype to validate user flows, page structure, roles, permissions, and UX before formal implementation.

## Inputs

- `01_REQUIREMENTS.md`
- `requirements/requirements.md`
- `requirements/datamodel.md`
- `requirements/validation.md`
- `02_TECHNICAL_DESIGN.md`
- Source PRD: `{{SOURCE_PRD}}`

## Prototype level

Default: Level 1 static prototype.

- Level 1: HTML + CSS only, page navigation through links, no JavaScript.
- Level 2: Optional interactive prototype with minimal vanilla JavaScript, only if explicitly approved.

## Prototype constraints

Default constraints follow the `requirements-analyst` prototype approach:

- Pure static files.
- Open `prototype/index.html` directly in a browser.
- Use relative links only.
- Use local CSS only.
- No CDN.
- No backend.
- No build tools.
- No CSS frameworks.
- No JavaScript unless Level 2 is explicitly approved.

## Prototype boundary

Prototype is a decision artifact, not a shadow product.

Prototype should validate page structure, user paths, information priority, key states, role/permission differences, empty/error states, and core UX decisions.

Prototype should not implement real backend calls, full business logic, full permissions systems, full state management, production component abstractions, pixel-perfect visual design, or production-ready code structure.

## Prototype plan

_To be completed before generating pages._

| # | Page | Source requirement / flow | Description | Status |
|---|---|---|---|---|
| 1 | `index.html` | Navigation hub | Prototype entry and page map | Planned |

## Page-to-requirement mapping

_To be completed during prototype planning/generation. Update `requirements/traceability.md` when useful._

| Page | Requirement / user story | Flow covered | Notes |
|---|---|---|---|
|  |  |  |  |

## Generated files

Expected structure:

```text
prototype/
├── index.html
├── css/
│   └── style.css
└── pages/
    └── <flow-page>.html
```

## Mock data

_To be documented during generation._

## Out of prototype scope

_To be documented before generation._

## Review feedback

_To be filled after stakeholder/user review._

## Approval decision

- Status: TBD
- Approved by:
- Decision notes:

## Completion checklist

- [ ] Prototype plan reviewed before page generation
- [ ] `prototype/index.html` exists
- [ ] `prototype/css/style.css` exists
- [ ] All non-index HTML pages are inside `prototype/pages/`
- [ ] Pages use realistic mock data
- [ ] Pages map back to requirements/user stories
- [ ] Mock data, fake interactions, unavailable buttons, and uncovered capabilities are explicitly marked
- [ ] Prototype can be opened without server/build step
- [ ] User approved prototype before implementation planning
