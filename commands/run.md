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

Do not mark a phase DONE by prose. Use `scripts/orchestrate.py gate <workflow-dir> <phase>` / validator evidence as the authority. If a gate fails, repair and rerun; if it still fails after bounded attempts, stop with the specific blocked state.
