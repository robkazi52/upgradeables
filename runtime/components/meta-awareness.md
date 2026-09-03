# Workflow Health Monitor (`meta-awareness@1.1.0`)

Recovered name: Meta-Awareness Pack

Purpose: Turn process-health signals into explicit observations that a supervisor can route to repair, pause, or continuation.

Activate when: process failure signals must be observed.

Do not use when: a simple task has no meaningful process state; the requested analysis concerns sentience or identity rather than task-process health.

Requires: none.

## Runtime mechanism

Maintain a small observable health frame: declared mode, current goal and state version, active modules, progress signal, repeated action signature, unresolved contradictions, and authority conflicts. Compare these observations with expected workflow state at checkpoints and emit pass, fail, repair-required, or unverifiable plus evidence; the pack diagnoses and reports but does not silently reroute or rewrite the task.

## Procedure

1. Read declared mode, locked goal, state version, active modules, and expected next transition.
2. Collect observable indicators of progress, repetition, contradiction, state staleness, and module conflict.
3. Compare indicators with thresholds and workflow expectations.
4. Classify health as pass, fail, repair-required, or unverifiable and attach the triggering evidence.
5. Send the finding to Meta-Supervisor or the owning workflow without changing authority or inventing internal mental-state explanations.

## Guardrails

- Mandatory even on strong models: observable-only claims; mode and state checks at consequential transitions; evidence-bearing status.
- Conflict/precedence: An unverifiable signal cannot be reported as a failure or a pass; Observed authority conflict is surfaced to the supervisor, not resolved by the sensor.
- Stop or fail when: anthropomorphic narratives; unobservable-state claims.

Full package and provenance: [`meta-awareness`](../../upgradeables/meta-control/meta-awareness/UPGRADEABLE.md).
