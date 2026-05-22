---
inclusion: agent
---

# Command: Prototype

**Objective**: Generate static HTML prototype from requirements to visualize UI flows and validate user experience.

---

## Quick Reference

| Aspect | Guideline |
|--------|-----------|
| Input | `requirements.md` (user stories, use cases) |
| Output | `prototype/` directory with static HTML |
| Style | Clean, minimal CSS (no frameworks) |
| Generation | ONE page at a time |

### STRICT: Pure Static Files Only

**MUST**:
- Pure HTML + CSS only
- Open `index.html` directly in browser (file:// protocol)
- All links use relative paths
- Inline or local CSS (no CDN)

**FORBIDDEN**:
- JavaScript (no .js files)
- External CDN/dependencies
- Server-side technology
- Build tools (npm, webpack, etc.)
- CSS frameworks (Bootstrap, Tailwind, etc.)

---

## Pre-Check

**MUST verify before starting**:

- [ ] `requirements.md` exists with user stories
- [ ] User flows/use cases are documented
- [ ] Spec folder path confirmed

**If check fails**: Ask user to complete Phase 3 first.

---

## Output Structure (STRICT)

```
.kiro/specs/[spec-name]/prototype/
├── index.html          # ONLY index.html in root
├── css/
│   └── style.css       # Shared styles
└── pages/
    ├── [flow-1].html   # ALL other HTML files MUST be here
    ├── [flow-2].html
    └── ...
```

### Directory Rules (MANDATORY)

| Rule | Description |
|------|-------------|
| **index.html** | ONLY file in prototype root (besides css/) |
| **pages/** | ALL other HTML files MUST go here |
| **css/** | All CSS files here |

**FORBIDDEN**: Creating HTML files outside `pages/` (except index.html)

---

## Execution Flow

### Step 1: Analyze Requirements

Read `requirements.md` and extract:
- User stories with UI implications
- Use case flows (main + alternative)
- Data entities to display
- User actions/interactions

### Step 2: Plan Pages

List pages to generate based on flows:

```markdown
## Prototype Plan

| # | Page | Source | Description |
|---|------|--------|-------------|
| 1 | index.html | - | Navigation hub |
| 2 | [name].html | US-XXX | [Flow description] |
| ... | ... | ... | ... |

Proceed with generation? (Y/N)
```

**Wait for user confirmation before generating.**

### Step 3: Generate Shared CSS

Create `prototype/css/style.css` with:
- Clean, minimal design
- Responsive layout
- Consistent color scheme
- Form and button styles
- Navigation styles

### Step 4: Generate Pages (ONE AT A TIME)

For each page:

1. **Announce**: "Generating [page-name].html for [user-story]"
2. **Create HTML** with:
   - Semantic HTML5 structure
   - Link to shared CSS
   - Navigation to other pages
   - Mock data based on data model
   - Interactive states (hover, active)
   - Form inputs where applicable
3. **Write to file** immediately
4. **Confirm**: "Created [page-name].html"

### Step 5: Generate Index

Create `prototype/index.html`:
- List all prototype pages
- Brief description of each flow
- Links to all pages

---

## HTML Requirements

### Structure
```html
<!DOCTYPE html>
<html lang="[selected-language]">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>[Page Title] - Prototype</title>
    <link rel="stylesheet" href="css/style.css">
</head>
<body>
    <nav><!-- Navigation --></nav>
    <main><!-- Page content --></main>
    <footer><!-- Prototype info --></footer>
</body>
</html>
```

### Content Guidelines
- Use realistic mock data (not "Lorem ipsum")
- Show all UI states (empty, loading, error, success)
- Include form validation hints
- Add comments linking to requirement IDs

---

## Completion Report

```markdown
## Prototype Generated

**Location**: `.kiro/specs/[spec-name]/prototype/`

### Pages Created

| Page | Source | Status |
|------|--------|--------|
| index.html | - | Created |
| [page].html | US-XXX | Created |
| ... | ... | ... |

### How to View

Open `prototype/index.html` in a browser.

### Next Steps

- Review prototype with stakeholders
- Note feedback for requirement updates
- Return to Clarify/Analyze if changes needed
```
