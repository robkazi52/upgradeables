# External State Automation

## Summary

Serialize task state to real files, memory, databases, or project documents only when the host provides persistence.

## Purpose

Provide a reusable `state-manager` mechanism rather than
a complete task identity or monolithic prompt.

## Problem Solved

Prevents the workflow failure implied by the trigger while keeping the
intervention bounded and inspectable.

## Scope

Functional classes: state, persistence. Activation:
`U2-specialized`. This modern classification is not a historical tier.

## Trigger Conditions

- continuation requires real external state

## Non-Triggers

- the declared trigger is absent or the control would add no material value

## Inputs / Required State

- current explicit task state
- authorized state update or source event

## Outputs / Produced State

- updated explicit state
- conflict or unavailable-persistence status

## Mechanism

Represent or update task state through explicit host-visible fields. Reconcile changes with locked state and record unavailable persistence honestly.

The name is architectural identity, not a claim of a physical, biological,
hidden, or private-reasoning mechanism.

## Procedure

1. Read the current explicit state and authority rules.
2. Validate the proposed update against locked fields and provenance.
3. Apply only authorized field changes.
4. Retire or mark superseded state without erasing provenance.
5. Emit the updated state or a conflict/unavailable-persistence status.

## Always-Do Rules

- Preserve higher-authority instructions and locked facts.
- Label assumptions and unavailable host capabilities.
- Keep activation proportional to risk and value.

## Never-Do / Avoid Rules

- Do not invent evidence, hidden state, persistence, or execution.
- Do not remain active when the trigger is absent.
- Do not expose or require private chain-of-thought.

## Interaction Rules

Load after the task boundary is known. Validators inspect or veto but do not
author supporting facts. State changes must use explicit state mechanisms.

## Compatible Upgradeables

- `state-snapshot`
- `stateblock`

## Counterbalancing Upgradeables

- `None declared`

## Potential Redundancy

- `None declared`

## Conflict / Precedence Rules

Host/system safety, domain policy, the active OS, and the task lock take
precedence. On an unresolved material conflict, narrow, abstain, or escalate.

## Failure Boundary

- do not claim state was retained or persisted without a real host-visible mechanism

## Strong-Model Scaling

May skip: verbose intermediate scaffolding when the host model is reliable and the task is simple.
Keep mandatory: truth, state, safety, and integrity invariants whenever the task still requires them.

## Recommended Skill Types

- `general-agent-workflow`
- `long-context-corpus`

## Example Composition

Activate `external-state-automation` only after task framing, combine it with the declared
compatible controls, then validate its output before final commitment.

## Tests

See [`tests/composition.md`](tests/composition.md) for positive, negative,
conflict, and scaling cases.

## Provenance / Historical Aliases

Source ID: `T2-20` in `OS_Upgradeable_to_Skills_Translation_Catalog_v2_Recovery_Merged.md`. Registry generation:
`consolidated-2026-09`. Aliases: None.
