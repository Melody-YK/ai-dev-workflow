# Evaluation Guide

This guide defines how to judge whether AI Dev Workflow is useful, reliable, and worth keeping.

The goal is not to reward long documents. The goal is to prove that the workflow makes AI-assisted development more controllable, resumable, and verifiable than a raw chat-driven coding session.

## Evaluation thesis

A good AI development workflow should improve six things:

1. Requirement clarity
2. Scope control
3. Handoff quality
4. Execution readiness
5. Verification evidence
6. Learning and repeatability

If the workflow does not improve these, it is just ceremony.

## References and borrowed ideas

This rubric borrows from common software engineering evaluation ideas:

- Requirements traceability: every important requirement should connect to design, implementation, and verification.
- SDLC quality gates: each phase should have explicit exit criteria before the next phase starts.
- Definition of Done: completion requires evidence, not claims.
- V-model thinking: requirements and design should map to later validation and verification.
- SWE-bench-style evaluation: real software tasks should be judged by whether the final system actually passes tests or resolves the issue, not by how plausible the plan sounds.
- Agent workflow evaluation: a later agent should be able to resume from persisted artifacts without private chat context.

These are adapted for a lightweight artifact-first workflow, not copied as a heavyweight process framework.

## What to evaluate

Evaluate one workflow run, usually one PRD or feature request.

Required inputs:

```text
PRD or raw feature request
.ai-workflow/<feature>/00_INTAKE.md
.ai-workflow/<feature>/01_REQUIREMENTS.md
.ai-workflow/<feature>/02_TECHNICAL_DESIGN.md
.ai-workflow/<feature>/03_IMPLEMENTATION.md
.ai-workflow/<feature>/04_REVIEW.md
.ai-workflow/<feature>/STATUS.md
Implementation diff, if implementation was executed
Test/build/lint output, if implementation was executed
```

## Scoring scale

Use 0 to 3 for each criterion:

| Score | Meaning |
|---|---|
| 0 | Missing or unusable |
| 1 | Present but shallow, vague, or hard to act on |
| 2 | Useful and mostly complete |
| 3 | Strong, specific, actionable, and independently verifiable |

Total score:

```text
Maximum: 63 points
Passing MVP: 42+ points and no critical gate failure
Strong workflow: 53+ points and no critical gate failure
```

Critical gate failures automatically fail the run even if the numeric score is high.

## Rubric

### 1. Requirement normalization

Artifact: `01_REQUIREMENTS.md`

| Criterion | Score |
|---|---|
| Actors, goals, workflows, entities, states, permissions, and constraints are explicit | 0-3 |
| Requirements are testable and not just copied from the PRD | 0-3 |
| Open questions and ambiguities are preserved instead of guessed | 0-3 |

Strong signal:

```text
The original PRD reads like business narrative; 01_REQUIREMENTS.md reads like something design and engineering can build from.
```

### 2. Traceability

Artifacts: `01_REQUIREMENTS.md`, `02_TECHNICAL_DESIGN.md`, `03_IMPLEMENTATION.md`, `04_REVIEW.md`

| Criterion | Score |
|---|---|
| Important PRD requirements map to requirements/design/implementation/review artifacts | 0-3 |
| Non-goals and deferred items are explicit | 0-3 |
| Verification references the original requirements rather than only checking code mechanically | 0-3 |

Strong signal:

```text
A reviewer can answer: where was this requirement handled, tested, deferred, or rejected?
```

### 3. Scope control

Artifact: `02_TECHNICAL_DESIGN.md`

| Criterion | Score |
|---|---|
| The workflow challenges overbroad scope and proposes a realistic MVP | 0-3 |
| It identifies risks, dependencies, edge cases, and tradeoffs | 0-3 |
| It records human decisions instead of silently choosing strategic/product direction | 0-3 |

Strong signal:

```text
The workflow does not blindly implement the full PRD. It recommends the smallest useful slice and explains what waits.
```

### 4. Handoff and resumability

Artifacts: all `.ai-workflow/<feature>/` files, especially `STATUS.md`

| Criterion | Score |
|---|---|
| A fresh agent can understand current state without chat history | 0-3 |
| `STATUS.md` accurately records phase, decisions, open questions, and next action | 0-3 |
| Phase artifacts contain enough context for the next phase to proceed safely | 0-3 |

Strong signal:

```text
Open a new session, provide only .ai-workflow/<feature>/, and the agent can say what happened and what to do next.
```

### 5. Implementation readiness

Artifact: `03_IMPLEMENTATION.md`

| Criterion | Score |
|---|---|
| Tasks are small, ordered, and executable | 0-3 |
| File paths, commands, expected outputs, and verification steps are concrete | 0-3 |
| TDD or another explicit verification-first approach is used where appropriate | 0-3 |

Strong signal:

```text
Another agent can execute the plan without asking for hidden context or inventing major missing design decisions.
```

### 6. Verification quality

Artifact: `04_REVIEW.md`

| Criterion | Score |
|---|---|
| Test/build/lint/manual QA evidence is recorded with commands and outcomes | 0-3 |
| Requirements coverage is checked against earlier artifacts | 0-3 |
| Remaining risks are classified as fixed, accepted, deferred, or blocked | 0-3 |

Strong signal:

```text
The run ends with evidence, not “looks good” prose.
```

### 7. Workflow efficiency and friction

Artifacts: `STATUS.md`, user feedback, run notes

| Criterion | Score |
|---|---|
| The workflow adds useful control without excessive ceremony | 0-3 |
| Human checkpoints are placed at meaningful decision points | 0-3 |
| The process reduces rework, confusion, or duplicated context compared with raw chat | 0-3 |

Strong signal:

```text
The user feels the gates improve control instead of slowing everything down for no reason.
```

## Critical gate failures

Any of these fail the run:

- The workflow implements code before requirements/design approval when approval was required.
- The implementation claims completion without running any meaningful verification when verification was possible.
- A fresh agent cannot determine current phase or next action from artifacts.
- Major PRD requirements disappear without being marked as deferred, rejected, or out of scope.
- The workflow silently invents product, security, compliance, or integration decisions that require human approval.

## Comparison test: raw chat vs workflow

The best way to prove value is to compare two runs on the same PRD.

### Run A: raw chat baseline

Prompt:

```text
Read this PRD and implement it.
```

Record:

- Output quality
- Missing requirements
- Scope drift
- Test evidence
- Ease of resuming in a new session
- Number of clarification loops or rework points

### Run B: AI Dev Workflow

Run:

```text
00 Intake
→ 01 Requirements
→ 02 Product & Engineering Review
→ 03 Implementation
→ 04 Verification & Review
```

Record the same metrics.

### Expected improvement

| Dimension | Raw chat often does | Workflow should do |
|---|---|---|
| Requirements | Mixes business prose with assumptions | Normalizes and makes testable |
| Scope | Tries to do everything or chooses randomly | Narrows intentionally |
| Handoff | Depends on chat history | Depends on artifacts |
| Execution | Starts coding too early | Plans before coding |
| Verification | Claims completion | Records evidence |
| Resume | Hard for another agent | Clear from `STATUS.md` |

## Fresh-agent handoff test

This is the most important practical test.

1. Start a new agent/session.
2. Provide only:

```text
.ai-workflow/<feature>/STATUS.md
.ai-workflow/<feature>/01_REQUIREMENTS.md
.ai-workflow/<feature>/02_TECHNICAL_DESIGN.md
```

3. Ask:

```text
What is the current project state, what decisions have been made, what is blocked, and what should happen next?
```

Pass criteria:

- The answer identifies the correct phase.
- The next action matches `STATUS.md`.
- Open questions and risks are mentioned.
- No hidden chat context is required.

## PRD-to-verification traceability test

Pick 5 important PRD requirements.

For each one, fill this table:

| PRD requirement | Requirements section | Design section | Implementation task | Verification evidence | Status |
|---|---|---|---|---|---|
|  |  |  |  |  | covered/deferred/rejected/missing |

Pass criteria:

- 4 of 5 are covered, explicitly deferred, or explicitly rejected.
- 0 of 5 silently disappear.

## Evaluation report template

Copy this into `.ai-workflow/<feature>/EVALUATION.md` after a run.

```markdown
# Evaluation — <feature>

## Summary

- Source PRD:
- Workflow directory:
- Evaluator:
- Date:
- Final score: /63
- Result: pass/fail/strong

## Scores

| Area | Score | Notes |
|---|---:|---|
| Requirement normalization | /9 |  |
| Traceability | /9 |  |
| Scope control | /9 |  |
| Handoff and resumability | /9 |  |
| Implementation readiness | /9 |  |
| Verification quality | /9 |  |
| Workflow efficiency and friction | /9 |  |

## Critical gate failures

- [ ] None
- [ ] Code before approval
- [ ] Completion without verification
- [ ] Cannot resume from artifacts
- [ ] Requirement disappeared silently
- [ ] Human decision silently invented

## Fresh-agent handoff result

Describe what happened when a fresh agent received only the artifacts.

## Traceability sample

| PRD requirement | Requirements | Design | Implementation | Verification | Status |
|---|---|---|---|---|---|
|  |  |  |  |  |  |

## What worked

- 

## What failed or felt heavy

- 

## Workflow changes to make

- 
```

## Recommended MVP acceptance standard

For the first public version of this workflow, accept it only if:

1. A fresh agent can resume from artifacts.
2. Requirements become clearer and more testable than the PRD.
3. Design review narrows scope or records why full scope is justified.
4. Implementation plan is executable without hidden chat context.
5. Verification records real evidence.
6. The workflow beats raw chat on at least 4 of these 6 dimensions: clarity, scope control, handoff, implementation readiness, verification, rework reduction.

One-line standard:

```text
The workflow is good if it turns AI development from chat-driven improvisation into artifact-driven, resumable, and verifiable execution.
```
