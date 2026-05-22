---
name: gstack-adapter
description: Adapter for using the real external garrytan/gstack skills inside ai-dev-workflow. Use when phase 02 or 05 needs full gstack review/QA capability and ~/.claude/skills/gstack is installed. This adapter maps gstack outputs into .ai-workflow artifacts; it does not vendor or replace gstack.
---

# gstack Adapter

This adapter exists to preserve full `garrytan/gstack` capability while keeping `ai-dev-workflow` artifacts stable.

It is **not** a bundled copy of gstack. It is `ADAPTER_FULL` only when the real external gstack installation is present and the relevant gstack command skills are invoked.

Required external paths for full review/QA capability:

- `~/.claude/skills/gstack/plan-ceo-review/SKILL.md`
- `~/.claude/skills/gstack/plan-eng-review/SKILL.md`
- `~/.claude/skills/gstack/review/SKILL.md`
- `~/.claude/skills/gstack/qa/SKILL.md`

Optional but useful when present:

- `~/.claude/skills/gstack/office-hours/SKILL.md`
- `~/.claude/skills/gstack/plan-design-review/SKILL.md`
- `~/.claude/skills/gstack/plan-devex-review/SKILL.md`
- `~/.claude/skills/gstack/cso/SKILL.md`
- `~/.claude/skills/gstack/ship/SKILL.md`


## Language mapping

When mapping gstack outputs into ai-dev-workflow, preserve the user's primary language for workflow artifacts and final replies. For Chinese PRDs or Chinese user instructions, write review findings, summaries, decision briefs, and handoff notes in Chinese even if the upstream gstack skill content is English. Keep only technical identifiers, commands, paths, API operation IDs, and enum values in English when appropriate.

## Phase 02 mapping

Use gstack as the reviewer, not as the workflow owner.

Recommended gstack slices:

1. Product/scope challenge: `/plan-ceo-review`
2. Engineering/architecture challenge: `/plan-eng-review`
3. Design/devex review when relevant: `/plan-design-review`, `/plan-devex-review`
4. Security/risk review when relevant: `/cso` or gstack security/risk review capability if installed

Write or map results to:

- `reviews/product-review.md`
- `reviews/engineering-review.md`
- `reviews/security-risk-review.md`
- `reviews/qa-review.md`
- `02_TECHNICAL_DESIGN.md` as workflow summary/gate only
- `requirements/traceability.md` for accepted/changed/deferred/rejected requirement decisions

## Phase 05 mapping

Recommended gstack slices:

1. `/review` for code/architecture review
2. `/qa` for browser/manual QA where an app can run
3. `/cso` for security/risk-sensitive projects when installed
4. `/ship` only as a release-readiness opinion, not as automatic deployment unless the user explicitly approves deployment

Write or map results to:

- `05_REVIEW.md`
- `reviews/product-review.md` / `engineering-review.md` / `security-risk-review.md` / `qa-review.md` if updated
- `requirements/traceability.md` for verification evidence
- `STATUS.md` Provider health and phase status

## Fidelity rules

- If external gstack is installed and invoked for the relevant slice: record `ADAPTER_FULL`.
- If external gstack is missing but `review-pack` is used: record `COMPACT_FALLBACK`, not gstack.
- If only some gstack slices run, record exactly which slices ran and which did not.
- Do not claim “gstack review passed” unless the corresponding external gstack command skill actually ran or was explicitly loaded and followed.
- Full gstack quality is output-gated, not just availability-gated. Before marking phase 02 full `DONE`, run `scripts/validate_artifacts.py <workflow-dir> --gate 02-full`; if it fails, record `NEEDS_GSTACK_DEPTH` or `DONE_DEGRADED` and expand the provider-native review notes.

## Installation note

Do not silently install gstack during a workflow run. If full gstack is required and missing, pause and ask the user to install or approve installation. Suggested upstream install command from gstack README:

```bash
git clone --single-branch --depth 1 https://github.com/garrytan/gstack.git ~/.claude/skills/gstack && cd ~/.claude/skills/gstack && ./setup
```
