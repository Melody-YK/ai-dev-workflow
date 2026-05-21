---
description: Initialize ai-dev-workflow from a PRD and stop after 00 Intake
argument-hint: PRD path, e.g. PRD.md
---

# ai-dev-init

Use the `ai-dev-workflow` skill. Do not search npm/pip/brew. Do not use `brain-dev`.

Read:

```text
skills/ai-dev-workflow/SKILL.md
```

Arguments:

```text
$ARGUMENTS
```

Initialize only:

```text
.ai-workflow/<feature-slug>/00_INTAKE.md
.ai-workflow/<feature-slug>/STATUS.md
```

Use `skills/ai-dev-workflow/scripts/init_workflow.py` if possible. If arguments do not specify a PRD path, use `PRD.md` in the current directory.

After initialization, stop and ask whether to continue to `01 Requirements`.
