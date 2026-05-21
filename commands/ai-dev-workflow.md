---
description: Run the ai-dev-workflow artifact-driven PRD development workflow
argument-hint: PRD path or feature request, e.g. "PRD.md" or "基于 PRD.md 初始化工作流"
---

# ai-dev-workflow

Use the `ai-dev-workflow` skill. Do not search npm, pip, brew, or install a package named `ai-dev-workflow`.

Read the skill instructions from this plugin:

```text
skills/ai-dev-workflow/SKILL.md
```

Then follow the workflow contract exactly.

User request / arguments:

```text
$ARGUMENTS
```

Default behavior when initializing from a PRD:

1. Locate the source PRD from `$ARGUMENTS`; default to `PRD.md` in the current project if not specified.
2. Initialize `.ai-workflow/<feature-slug>/` using `skills/ai-dev-workflow/scripts/init_workflow.py` or by copying the templates from `skills/ai-dev-workflow/assets/templates/`.
3. Only complete `00_INTAKE.md` and `STATUS.md` unless the user explicitly asks to continue.
4. Do **not** create `.brain/`.
5. Do **not** use `brain-dev`.
6. Do **not** split the project into implementation phases before `01 Requirements Engineering` completes.
7. Stop after intake and ask whether to continue to `01 Requirements`.

Expected workflow directory:

```text
.ai-workflow/<feature-slug>/
├── 00_INTAKE.md
├── 01_REQUIREMENTS.md
├── requirements/
├── 02_TECHNICAL_DESIGN.md
├── 03_PROTOTYPE.md
├── 04_IMPLEMENTATION.md
├── 05_REVIEW.md
└── STATUS.md
```
