---
inclusion: agent
description: "Reverse engineering workflow - extract requirements from existing codebase"
keywords: ["reverse", "逆向", "extract", "codebase", "existing", "legacy", "现有代码", "提取需求"]
---

# Reverse Command

**Command Objective**: Reverse engineer an existing codebase to extract and document requirements, enabling requirements analysis for legacy or undocumented projects.

**Your Role**: Professional Requirements Analyst with Code Analysis Skills

---

## Purpose

Extract requirements from existing projects by:
- **Analyzing codebase**: Understand technology stack, architecture, and patterns
- **Extracting product context**: Identify purpose, users, and business logic
- **Documenting features**: Map functionality and user-facing capabilities
- **Synthesizing requirements**: Convert code analysis into structured requirements

## When to Use

- Onboarding to an existing project without documentation
- Adopting requirements methodology for legacy codebases
- Creating requirements documentation for undocumented projects
- Understanding unfamiliar codebases quickly
- Preparing for major refactoring or modernization
- Generating requirements baseline before enhancement projects

## Prerequisites

**Required**:
- An existing codebase to analyze
- Access to source files, configuration files, and package manifests

**Helpful but optional**:
- Existing README or documentation
- Git history for context
- Running application for behavior observation
- Access to stakeholders who understand the system

---

## Quick Reference

| Step | Focus | Output | Critical? |
|------|-------|--------|-----------|
| 1. Project Discovery | Scan codebase structure | Project overview | ✅ Yes |
| 2. Tech Stack Analysis | Identify technologies | Technology inventory | ✅ Yes |
| 3. Architecture Analysis | Map structure & patterns | Architecture summary | ✅ Yes |
| 4. Product Context | Understand purpose & users | Product context summary | ✅ Yes |
| 5. Feature Extraction | Identify business features | Feature inventory | ✅ Yes |
| 6. Requirements Synthesis | Convert to requirements | Requirements list | ✅ Yes |
| 7. User Review | Validate with user | Confirmed requirements | ✅ Yes |

---

## Output

**File**: `.kiro/specs/[spec-name]/reverse.md`

> After completion, user can proceed to Phase 2 (Sort) or Phase 3 (Analysis) with the extracted requirements.

---

## Pre-Check (GATE CHECK)

**MUST satisfy these conditions before starting**:

| Check Item | Requirement | Status |
|-----------|-------------|--------|
| Codebase Access | MUST have read access to source code | [ ] |
| Project Scope | MUST identify analysis boundaries | [ ] |
| User Available | MUST have user available to validate findings | [ ] |

**If check fails**: STOP. Resolve access issues before proceeding.

---

## Operating Constraints

**NON-DESTRUCTIVE**: This workflow only reads and analyzes; it generates new files but does NOT modify existing code.

**USER CONFIRMATION**: All extracted requirements require user review and approval.

**ITERATIVE REFINEMENT**: Generated requirements are drafts; expect multiple rounds of refinement with user input.

**EVIDENCE-BASED**: Every requirement must trace back to specific code evidence.

**MERMAID FIRST (MANDATORY)**: When documenting flows, processes, sequences, or relationships:
- **MUST** use Mermaid syntax as the primary representation
- **NEVER** use plain text descriptions as a substitute for diagrams
- Supported diagram types:
  - `sequenceDiagram` - For API calls, service interactions, user journeys
  - `flowchart` - For business logic, decision trees, process flows
  - `erDiagram` - For data models and entity relationships
  - `classDiagram` - For component structures and dependencies
- Plain text descriptions are supplementary only, not replacements

---

## Execution Flow

### Step 1: Project Discovery

Scan the project to gather initial context:

**File System Analysis**:
- Identify root directory and project boundaries
- Detect monorepo vs single project structure
- Find configuration files (package.json, pyproject.toml, Cargo.toml, etc.)
- Locate source directories and entry points

**Version Control Analysis** (if available):
- Check git history for project age and activity
- Identify main contributors
- Review recent changes for active areas

**Output**: Project overview summary for user confirmation

```markdown
## Project Overview

**Root**: [path]
**Type**: [monorepo/single-project/library/application]
**Primary Language**: [detected language]
**Package Manager**: [npm/pip/cargo/etc.]
**Age**: [first commit date if available]
**Activity**: [last commit, commit frequency]
```

### Step 2: Technology Stack Analysis

Analyze dependencies and configuration to determine the tech stack:

**Dependency Analysis**:
- Parse package manifests (package.json, requirements.txt, Cargo.toml, go.mod, etc.)
- Identify frameworks (React, Django, Spring, etc.)
- Detect testing frameworks
- Find build tools and CI/CD configuration

**Configuration Analysis**:
- Parse config files (tsconfig.json, .eslintrc, pytest.ini, etc.)
- Identify linting and formatting tools
- Detect environment configuration patterns

**Infrastructure Detection**:
- Find Dockerfile, docker-compose.yml
- Detect cloud provider configurations (AWS, GCP, Azure)
- Identify database configurations

**Output**: Technology inventory

### Step 3: Architecture Analysis

Understand the project's architecture and patterns:

**Directory Structure Analysis**:
- Map folder hierarchy
- Identify architectural patterns (MVC, Clean Architecture, Hexagonal, etc.)
- Detect module boundaries
- Find shared/common code locations

**Code Pattern Detection**:
- Identify naming conventions (files, functions, classes)
- Detect API patterns (REST, GraphQL, gRPC)
- Find data access patterns (ORM, raw SQL, repositories)
- Identify error handling approaches

**Dependency Graph**:
- Map internal module dependencies
- Identify circular dependencies
- Find entry points and core modules

**Data Model Extraction** (MERMAID REQUIRED):
- Parse ORM models (Sequelize, TypeORM, Prisma, Django models, etc.) → generate `erDiagram`
- Analyze database migration files for schema structure → update `erDiagram`
- Extract TypeScript/Java/Python type definitions
- Identify foreign key relationships and constraints → reflect in `erDiagram`

**Output**: Architecture summary with Mermaid diagrams

### Step 4: Product Context Extraction

Understand what the product does and who it serves:

**Documentation Analysis**:
- Parse existing README files
- Extract from code comments and docstrings
- Review API documentation if present
- Check for user guides or wikis

**Code Semantics Analysis**:
- Analyze route handlers/controllers for features
- Identify domain models and their relationships
- Extract business logic from service layers
- Detect user-facing functionality

**Configuration Clues**:
- Environment variables for feature flags
- Localization files for user-facing text
- Permission/role configurations

**Output**: Product context summary

### Step 5: Feature Extraction

Extract business features from code analysis:

**Route/Endpoint Analysis**:
- Scan all HTTP endpoints
- Extract WebSocket handlers
- Identify background jobs/tasks
- Map event handlers

**Business Logic Analysis**:
- Analyze service layer code
- Extract validation rules
- Identify business workflows
- Find authorization rules

**User Interface Analysis** (if applicable):
- Map UI components to features
- Extract form fields and validations
- Identify user workflows
- Document navigation flows

**Business Flow Extraction** (MERMAID REQUIRED):
- Scan route handlers for user-initiated flows → generate `sequenceDiagram`
- Trace service method call chains → generate `sequenceDiagram`
- Identify decision logic and branches → generate `flowchart`
- Map async/event-driven flows → generate `sequenceDiagram` with async notation

**Service Interface Extraction**:
- Scan route definitions for all HTTP endpoints
- Parse OpenAPI/Swagger specs if available
- Identify WebSocket handlers and event emitters
- Document authentication requirements per endpoint
- Extract rate limiting configurations

**Technical Debt Detection**:
- Scan for TODO, FIXME, HACK comments
- Identify deprecated code and APIs
- Find commented-out code blocks
- Detect inconsistent patterns suggesting rushed implementation

**Output**: Feature inventory with code evidence

```markdown
## Feature Inventory

| Feature ID | Feature Name | Code Location | Evidence |
|------------|--------------|---------------|----------|
| F-001 | User Login | `src/auth/login.ts:45` | POST /api/login endpoint |
| F-002 | Data Export | `src/export/csv.ts:12` | exportToCSV function |
```

### Step 6: Requirements Synthesis

Convert extracted features into requirements format:

**For Each Feature**:
1. Identify the user need it serves
2. Extract functional behavior
3. Document constraints and validations
4. Identify non-functional aspects (performance, security)

**Requirements Format**:

```markdown
### REQ-001: [Requirement Name]

**Source**: [Feature ID and code location]
**Type**: Functional / Non-Functional
**Priority**: [To be determined in Sort phase]

**Description**:
[What the system does, derived from code analysis]

**Evidence**:
- File: [path]
- Function/Class: [name]
- Behavior: [observed behavior]

**Acceptance Criteria** (inferred):
- [ ] [Criterion derived from code]
- [ ] [Criterion derived from tests if available]

**Notes**:
[Any uncertainties or assumptions marked with [INFERRED]]
```

### Step 7: User Review and Validation

Present findings for user validation:

```text
Reverse Engineering Complete
============================

Project: [PROJECT_NAME]
Language: [PRIMARY_LANGUAGE]
Framework: [MAIN_FRAMEWORK]
Type: [APPLICATION_TYPE]

Analysis Summary:
  - Files scanned: [N]
  - Modules detected: [N]
  - Features identified: [N]
  - API endpoints found: [N]
  - Requirements extracted: [N]
  - Technical debt items: [N]

Would you like to:
  A) Review each requirement before saving
  B) Save all and review later
  C) Ask questions about specific findings
  D) Re-analyze specific areas
```

**Interactive Refinement**:

**Review Mode**:
- Display each extracted requirement section by section
- Allow user to approve, modify, or reject each item
- Mark uncertain items with [NEEDS CLARIFICATION]
- Incorporate user corrections into final output

**Question Mode**:
- Answer questions about detected patterns
- Explain reasoning for specific conclusions
- Provide evidence from code for each assertion

**Regeneration Mode**:
- Re-analyze specific aspects with user guidance
- Incorporate additional context provided by user
- Update extracted requirements with new information

---

## Analysis Guidelines

### Evidence-Based Conclusions

- **Every requirement must have code evidence**
- Quote specific files and line numbers when possible
- Mark uncertain conclusions with [INFERRED] tag
- Distinguish between detected facts and assumptions

### Handling Ambiguity

- When patterns are inconsistent, document all variations
- Ask user to clarify when multiple interpretations exist
- Default to most common pattern when choosing conventions
- Mark areas needing user input with [NEEDS CLARIFICATION]

### Scope Boundaries

- Focus on primary application code, not vendored/generated code
- Skip node_modules, __pycache__, build artifacts
- Respect .gitignore patterns for exclusion
- Limit analysis depth for very large monorepos

---

## Exit Criteria

**CRITICAL**: Complete ALL items below to finish:

| Exit Item | Qualification Standard | Status |
|-----------|----------------------|--------|
| **Project Overview** | Project scope and tech stack documented | [ ] |
| **Architecture Diagram** | At least one Mermaid diagram created | [ ] |
| **Feature Inventory** | All major features identified with evidence | [ ] |
| **Requirements List** | Requirements extracted (≥10 items for typical project) | [ ] |
| **Technical Debt** | TODO/FIXME/deprecated items catalogued | [ ] |
| **User Validation** | User has reviewed and confirmed findings | [ ] |

---

## Output File Template

Generate `.kiro/specs/[spec-name]/reverse.md`:

```markdown
# Reverse Engineering Report

## 1. Project Overview

**Project**: [Name]
**Analyzed**: [Date]
**Scope**: [What was analyzed]

## 2. Technology Stack

| Category | Technology |
|----------|------------|
| Language | [e.g., TypeScript] |
| Framework | [e.g., React, Express] |
| Database | [e.g., PostgreSQL] |
| Testing | [e.g., Jest, Cypress] |

## 3. Architecture

[Mermaid diagram here]

### Key Patterns
- [Pattern 1]
- [Pattern 2]

## 4. Data Model

[erDiagram here]

## 5. Feature Inventory

| ID | Feature | Location | Status |
|----|---------|----------|--------|
| F-001 | [Name] | [Path] | Confirmed |

## 6. Extracted Requirements

### Functional Requirements

#### REQ-001: [Name]
...

### Non-Functional Requirements

#### NFR-001: [Name]
...

## 7. Technical Debt & Known Issues

| ID | Type | Location | Description |
|----|------|----------|-------------|
| TD-001 | TODO | [Path:Line] | [Description] |
| TD-002 | Deprecated | [Path] | [What is deprecated] |

## 8. Gaps and Uncertainties

- [Items marked INFERRED]
- [Items marked NEEDS CLARIFICATION]

## 9. Recommended Next Steps

1. Proceed to Phase 2 (Sort) to prioritize requirements
2. Or proceed to Phase 3 (Analysis) if priorities are clear
```

---

## Next Steps

After completing this command:

```
Reverse engineering complete.

Next, you can:
1. Run **Phase 2 (Sort)** to prioritize the extracted requirements
2. Run **Phase 3 (Analysis)** to analyze into user stories
3. Review and refine the extracted requirements manually
4. Share findings with stakeholders for validation
```
