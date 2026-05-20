# Workflow Overview

This workflow keeps the process small and controllable while allowing stronger skills to be swapped in later.

## Default flow

```text
Raw PRD / user request
→ 00 Intake
→ 01 Requirements
→ 02 Product & Engineering Review
→ 03 Implementation Planning & Build
→ 04 Verification & Review
→ Retro / learning
```

## Design principles

1. Artifact-first: each phase writes a file that the next phase reads.
2. Capability contracts over fixed skills: phases depend on inputs/outputs, not a permanent vendor/tool.
3. Human checkpoints: phase transitions stop for approval by default.
4. Minimal automation first: scripts initialize and validate, agents perform judgment work.
5. Replaceable skills: `requirements-analyst`, `gstack`, and `superpowers` are defaults, not hard dependencies.

## Recommended first test

Use an existing PRD. Initialize a workflow directory, then run one phase at a time. After each phase, inspect artifacts and decide whether the phase contract is strong enough.
