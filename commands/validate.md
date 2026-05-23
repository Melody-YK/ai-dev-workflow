---
description: Validate ai-dev-workflow artifacts with all authoritative phase gates
argument-hint: .ai-workflow/<feature>
---

# validate ai-dev-workflow

Run deterministic validation for `$ARGUMENTS`.

Use:

```bash
python3 <plugin-root>/scripts/orchestrate.py validate-all <workflow-dir> --all
```

Report gate rc values and the first failures. Do not reinterpret failed gates as success.
