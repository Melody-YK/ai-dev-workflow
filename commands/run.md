---
description: Run the artifact-driven ai-dev-workflow from PRD intake through verification
argument-hint: PRD path or feature request, e.g. "PRD.md" or "基于 PRD.md 初始化工作流"
---

# run ai-dev-workflow

Load and follow the `run` skill from this plugin, then read the orchestration contract before phase work:

```text
skills/ai-dev-workflow/SKILL.md
references/orchestration.md
```

User request / arguments:

```text
$ARGUMENTS
```

Follow the skill's own workflow contract, artifact locations, phase gates, provider-routing rules, and forced gate loop.

User brevity does not weaken the contract. If the arguments only contain a PRD path or a simple request, still use canonical artifacts and gates. Do not invent alternate filenames or phase structure.

Before phase work, ensure the workflow directory contains the canonical artifacts (`00_INTAKE.md`, `01_REQUIREMENTS.md`, `02_TECHNICAL_DESIGN.md`, `03_PROTOTYPE.md`, `04_IMPLEMENTATION.md`, `05_REVIEW.md`, `STATUS.md`). If missing, initialize them with `scripts/init_workflow.py`; do not hand-create aliases like `02_REVIEW.md` or `04_PLAN.md`.

Human gates are default behavior unless the user explicitly requests unattended/continuous execution. Pause for blocking requirements clarifications, prototype approval, and implementation execution approval.

Do not mark a phase DONE by prose. Use `scripts/orchestrate.py gate <workflow-dir> <phase>` / validator evidence as the authority. If a gate fails, repair and rerun; if it still fails after bounded attempts, stop with the specific blocked state.
