# Explore-Then-Commit Mode (`hybrid-mode@1.1.0`)

Recovered name: HYBRID Mode

Purpose: Combine broad planning capability with conservative implementation without letting speculative branch assumptions leak into committed work.

Activate when: work includes both broad design and grounded execution.

Do not use when: the task needs only narrow execution; the task is pure open exploration with no commitment.

Requires: none.

## Runtime mechanism

Run POWER only to generate and compare bounded plans, then collapse to one plan and construct a handoff containing locked goals, selected decisions, rejected assumptions, evidence needs, risks, and execution invariants. A supervisor validates the handoff before activating SAFE, which executes only the committed plan with narrow drift and atomic checks. Re-enter POWER only through a checkpoint when execution exposes an architecture-level defect.

## Procedure

1. Declare HYBRID and define separate planning and execution completion criteria.
2. Use POWER to generate, evaluate, and collapse candidate plans.
3. Create a transition state with the selected plan, locked constraints, evidence, risks, unresolved items, and retired branches.
4. Have the supervisor verify that the plan is executable and no speculative assumptions remain active.
5. Switch explicitly to SAFE and execute with grounding, narrow drift, and atomic validation.

## Guardrails

- Mandatory even on strong models: explicit collapse; handoff state; supervisor gate.
- Conflict/precedence: No POWER branch may execute until one plan passes collapse and handoff validation; SAFE findings can reopen design only through a recorded checkpoint.
- Stop or fail when: mode leakage; uncollapsed execution.

Full package and provenance: [`hybrid-mode`](../../upgradeables/meta-control/hybrid-mode/UPGRADEABLE.md).
