# Workflow Overview

This workflow keeps the process small and controllable while allowing stronger skills to be swapped in later.

## Default flow

```text
Raw PRD / user request
→ 00 Intake
→ 01 Requirements
→ 02 Product & Engineering Review
→ 03 Prototype
→ 04 Implementation Planning & Build
→ 05 Verification & Review
→ Retro / learning
```

## Design principles

1. Artifact-first: each phase writes a file that the next phase reads.
2. Capability contracts over fixed skills: phases depend on inputs/outputs, not a permanent vendor/tool.
3. Human checkpoints: phase transitions stop for approval by default.
4. Prototype before implementation: validate user flows and UI structure before coding production behavior.
5. Minimal automation first: scripts initialize and validate, agents perform judgment work.
6. Replaceable skills: `requirements-analyst`, `gstack`, and `superpowers` are defaults, not hard dependencies.

## Prototype philosophy

Prototype means a requirements-driven static HTML/CSS prototype, not a production frontend.

Default prototype constraints:

- Pure static files.
- `prototype/index.html` opens directly in a browser.
- No server, build step, CDN, or framework.
- No JavaScript unless Level 2 interactive prototype is explicitly approved.
- Pages map back to requirements/user stories.

The prototype phase is a validation tool: it should reveal misunderstood flows, missing pages, wrong roles, unclear states, and bad UX before implementation begins.

## Recommended first test

Use an existing PRD. Initialize a workflow directory, then run one phase at a time. After each phase, inspect artifacts and decide whether the phase contract is strong enough.
