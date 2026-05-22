---
name: "requirements-analyst"
displayName: "Requirements Analyst"
description: "6-phase requirements engineering: Discovery → Sort → Analysis → Clarification → Validation → Specification"
keywords: ["requirements", "PRD", "user stories", "MoSCoW", "FURPS+"]
author: "Kiro User"
---

# Requirements Analyst Power

## General Principles

1. **Cross-Platform**: Detect OS, use appropriate commands
2. **Intent-Based**: Instructions describe *what*, AI determines *how*
3. **Semantic Recognition**: Understand user intent, not keyword matching

---

## Startup Flow

### 1. Language Detection (AUTO)

**Auto-detect language from user's input**:
- If user writes in Chinese → Use Chinese for all outputs
- If user writes in English → Use English for all outputs

**Language applies to**:
- All conversation outputs
- All generated document content
- **ALL template headings, labels, and field names**

### 2. Load Core Protocol

After language confirmed, load `steering/00-interaction-protocol.md`.

### 3. Spec Selection

1. Check `.kiro/specs/` for existing spec folders
2. If exists: List specs with phase status, let user select or create new
3. If empty: Ask for new spec name (lowercase, alphanumeric, hyphens only)
4. Detect phase status:
   - `reverse.md` → Reverse command done (can proceed to Phase 2 or 3)
   - `discovery.md` → Phase 1 done
   - `sort.md` → Phase 2 done
   - `requirements.md` → Phase 3 done
   - `clarification.md` → Phase 4 done
   - `validation.md` → Phase 5 done
   - `prd.md` → Phase 6 done
5. Suggest next phase based on status

---

## Phase Intent Recognition

Recognize user intent semantically → load corresponding phase file:

| Phase | Intent | Steering File |
|-------|--------|---------------|
| Reverse | Extract requirements from existing code | `command-reverse.md` |
| 1 | Discover/collect requirements | `phase1-requirements-discovery.md` |
| 2 | Prioritize/sort by value | `phase2-requirements-value-sorting.md` |
| 3 | Analyze into stories/use cases | `phase3-requirements-analysis.md` |
| 4 | Clarify ambiguities | `phase4-requirements-clarification.md` |
| 5 | Validate quality | `phase5-requirements-validation.md` |
| 6 | Formalize into PRD | `phase6-requirements-specification.md` |

**Rules**:
- If user has existing codebase without documentation → Reverse command
- If user provides raw requirements document → Phase 3 (no need to "discover")
- Skip completed phases based on existing files
- Ask if intent is ambiguous

---

## Steering Files

All in `steering/` directory:

- `00-interaction-protocol.md` - Core interaction guidelines
- `command-*.md` - Auxiliary commands (reverse, prototype)
- `phase[1-6]-*.md` - Phase instructions
- `helper-*.md` - Standards (diagram, multi-role validation)
- `template-*.md` - Output templates

---

## File Dependencies

When loading a phase, also load its dependencies:

| Phase | Output Template | Helper | Deliverables |
|-------|-----------------|--------|--------------|
| 1 | `template-discovery.md` | - | - |
| 2 | `template-sort.md` | - | - |
| 3 | `template-analysis.md`, `template-data-model.md` | `helper-diagram-standards.md` | - |
| 4 | `template-clarification.md` | - | - |
| 5 | `template-validation.md` | `helper-multi-role-validation.md` | - |
| 6 | `template-prd.md` | - | `template-openapi.md`, `template-rtm.md` |

## ⛔ Context Loading Rule (MANDATORY)

**CRITICAL**: Track loaded files in memory. NEVER reload files already in current conversation context.

**DO**:
- ✅ Check if steering/template file was already loaded in this conversation
- ✅ Skip loading if file content is already in context
- ✅ Reference previously loaded content directly

**DO NOT**:
- ❌ Reload the same steering file multiple times
- ❌ Reload the same template file multiple times
- ❌ Re-read files that are already in conversation context

**Verification**:
- [ ] Before loading any file, confirm it's NOT already in context
- [ ] If already loaded, use existing content without re-reading

---

### Execution Rules (MANDATORY)

1. **Load Before Execute**: MUST load template + helper files BEFORE starting phase work (if not already loaded)
2. **Copy Then Edit Workflow**:
   - First, copy template file to target location (e.g., `cp template-analysis.md .kiro/specs/[name]/requirements.md`)
   - Then edit the copied file section by section using Edit tool
   - This allows user to see progress immediately instead of waiting for full generation
3. **Section by Section**: Edit ONE section at a time, do NOT generate entire document at once
4. **Incremental Edit**: Complete each section before moving to the next
5. **Language Compliance**: Translate ALL template headings, labels, table headers, and field names to match user's input language. English templates are structure references only

**Language Compliance Checklist (MANDATORY)**:
Before submitting ANY output, verify:
- [ ] User language detected: Chinese/English
- [ ] ALL headings translated to detected language
- [ ] ALL labels translated to detected language
- [ ] ALL field names translated to detected language
- [ ] ALL table headers translated to detected language
- [ ] NO mixed language content (Chinese user = 100% Chinese output)

## ⛔ Phase Completion Prompt (MANDATORY)

**CRITICAL**: After completing ANY phase, MUST prompt user with available next steps using AskUserQuestion tool.

**DO**:
- ✅ Summarize what was completed in current phase
- ✅ List all valid next phase options
- ✅ Use AskUserQuestion tool to let user choose
- ✅ Wait for user selection before proceeding

**DO NOT**:
- ❌ Auto-proceed to next phase without asking
- ❌ Only show one option when multiple are valid
- ❌ Skip the prompt and continue working
- ❌ Use text prompt instead of AskUserQuestion tool

**Phase Flow Table**:

| Completed | Next Options | Load Files (if iterating) | Notes |
|-----------|--------------|---------------------------|-------|
| Phase 1 | Phase 2 | - | - |
| Phase 2 | Phase 3 | - | - |
| Phase 3 | Phase 4 | - | - |
| Phase 4 | Phase 5, **Phase 3** | `clarification.md` | Re-analyze if scope changed |
| Phase 5 (Pass) | Phase 6 | - | All validations passed |
| Phase 5 (Fail: Authenticity) | **Phase 4** | `validation.md` | Need stakeholder confirmation |
| Phase 5 (Fail: Completeness-missing) | **Phase 3** | `validation.md` | Need to add requirements |
| Phase 5 (Fail: Completeness-unclear) | **Phase 4** | `validation.md` | Need to resolve ambiguities |
| Phase 5 (Fail: Consistency) | **Phase 3** | `validation.md` | Need to restructure |
| Phase 5 (Fail: Feasibility) | **Phase 3/4** | `validation.md` | Depends on issue type |
| Phase 5 (Fail: Verifiability) | **Phase 4** | `validation.md` | Need acceptance criteria |
| Phase 6 | Prototype, Complete | `.kiro/templates/` (if custom) | - |

**Verification** (Check BEFORE completing phase):
- [ ] Phase deliverable file written to `.kiro/specs/`
- [ ] Summary of completed work prepared
- [ ] AskUserQuestion called with valid next options
- [ ] NOT proceeding until user responds

---

## Auxiliary Commands

| Command | Intent | Steering File | Description |
|---------|--------|---------------|-------------|
| Reverse | Extract requirements from code | `command-reverse.md` | Reverse engineer existing codebase to extract requirements |
| Prototype | Generate UI prototype | `command-prototype.md` | Create static HTML prototype from requirements |

**Triggers**:
- **Reverse**: User says "逆向", "reverse", "提取需求", "extract requirements", "分析代码", "analyze codebase", "现有项目"
- **Prototype**: User says "原型", "prototype", "生成原型", "create prototype"

---

## Output Structure

```
.kiro/specs/[spec-name]/
├── reverse.md          # From Reverse command (optional entry point)
├── discovery.md        # Phase 1
├── sort.md             # Phase 2
├── requirements.md     # Phase 3
├── data-model.md       # Phase 3
├── clarification.md    # Phase 4
├── validation.md       # Phase 5
├── prd.md              # Phase 6
├── api.yaml            # Phase 6
├── rtm.md              # Phase 6
└── prototype/          # Prototype command
    ├── index.html
    ├── css/
    └── pages/
```
