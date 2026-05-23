# Orchestrated workflow contract

`ai-dev-workflow` is a workflow package, not a single prompt. Treat each phase as a state-machine transition with explicit provider routing, mandatory gates, and recovery loops.

## State machine

Canonical states:

- `NOT_STARTED`
- `READY`
- `RUNNING`
- `NEEDS_HUMAN_INPUT`
- `NEEDS_REQUIREMENTS_DEPTH`
- `NEEDS_GSTACK_DEPTH`
- `NEEDS_PROTOTYPE_DEPTH`
- `NEEDS_IMPLEMENTATION_PLAN`
- `BLOCKED_ARTIFACT_DRIFT`
- `PROVIDER_DEGRADED`
- `DONE_DEGRADED`
- `DONE`

A phase may be marked `DONE` only after its required gate exits with code 0 and the gate evidence is written into the phase artifact and `STATUS.md`.

## Provider registry

| Capability | Preferred provider | Full condition | Degraded alternatives |
|---|---|---|---|
| `requirements-analysis` | external `requirements-analyst` | `EXTERNAL_FULL`, real steering/templates loaded, `01-full` passes | bundled source slice only if it still loads copied steering/templates; otherwise degraded |
| `product-engineering-review` | `gstack-adapter` over external `garrytan/gstack` | `ADAPTER_FULL`, real gstack slices/provenance recorded, `02-full` passes | `review-pack` is `COMPACT_FALLBACK`, never full |
| `implementation-verification-discipline` | external `superpowers` via adapter | `ADAPTER_FULL`, plan/evidence gates pass | fallback/degraded only with explicit user acceptance |

Provider availability is necessary but never sufficient. The artifact gate is authoritative.

## Forced gate loop

For each phase:

1. Mark the phase `RUNNING` in `STATUS.md`.
2. Run provider preflight when the phase depends on an external provider.
3. Read the provider adapter instructions and required reference files.
4. Produce provider-native artifacts in the workflow-owned paths.
5. Run the required validator gate.
6. If the gate fails:
   - write the failed command and first failures into the phase artifact;
   - set phase state to the specific `NEEDS_*` or `BLOCKED_*` state;
   - repair only the failed phase inputs/outputs;
   - rerun the same gate;
   - repeat up to 3 repair attempts.
7. If the gate still fails after 3 attempts, stop and ask the user whether to continue degraded, change provider/model, or revise scope.
8. If the gate passes, write the command, exit code, and timestamp into the phase artifact and `STATUS.md`, then and only then mark the phase `DONE`.

## Phase gates

| Phase | Required gate before clean DONE / transition |
|---|---|
| 01 Requirements | `scripts/validate_artifacts.py <workflow-dir> --gate 01-full` |
| 02 Product & Engineering Review | `scripts/validate_artifacts.py <workflow-dir> --gate 02-full` |
| 03 Prototype | `scripts/validate_artifacts.py <workflow-dir> --gate 03-full`; generation complete is not human approval |
| 04 Planning | `scripts/validate_artifacts.py <workflow-dir> --gate 04-plan` before implementation execution |
| 04 Complete | `scripts/validate_artifacts.py <workflow-dir> --gate 04-complete` before 05 |
| 05 Complete | `scripts/validate_artifacts.py <workflow-dir> --gate 05-complete` before final “ready” claims |

## Human gates in guided-auto

Guided-auto skips ordinary “continue to next phase?” confirmations, but does not skip real human decisions.

Always pause for:

- blocking open requirements decisions;
- provider degradation acceptance;
- prototype approval before implementation;
- implementation execution after 04 planning; this is a hard stop and requires explicit human/user approval, not agent self-approval or inline execution;
- release readiness exceptions or unresolved high risks.

Do not convert “artifact generated” into “user approved”.

## Recovery commands

Use `/ai-dev-workflow:continue` to resume from `STATUS.md` and run only the current blocked/next phase.
Use `/ai-dev-workflow:validate` to run all applicable gates and print the authoritative state.
