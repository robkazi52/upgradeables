# Sequential Memory State Engine (SMSE)

## Summary

Update StateBlock incrementally while preserving source chunk boundaries, provenance, and locked state.

## Purpose

Provide a reusable `state-manager` mechanism rather than
a complete task identity or monolithic prompt.

## Problem Solved

Prevents the workflow failure implied by the trigger while keeping the
intervention bounded and inspectable.

## Scope

Functional classes: state, persistence. Activation:
`U1-common-conditional`. This modern classification is not a historical tier.

## Trigger Conditions

- state changes across steps or source chunks

## Non-Triggers

- the declared trigger is absent or the control would add no material value

## Inputs / Required State

- current explicit task state
- authorized state update or source event

## Outputs / Produced State

- updated explicit state
- conflict or unavailable-persistence status

## Mechanism

Process bounded source chunks through fact extraction, compartment routing, state growth, explicit reasoning hooks, canonical working memory, drift guard, and working-memory heartbeat snapshots.

The name is architectural identity, not a claim of a physical, biological,
hidden, or private-reasoning mechanism.

## Procedure

1. Ingest one bounded source chunk.
2. Extract only explicit facts with source provenance.
3. Route facts to the correct topic/domain compartment.
4. Grow state for genuinely new topics without overwriting locked compartments.
5. Expose explicit state-field hooks to downstream reasoning modules.
6. Treat StateBlock as canonical working memory for this workflow.
7. Reject or flag reasoning unsupported by source/state.
8. Refresh locks, focus, drift status, and a continuation snapshot at meaningful heartbeats.

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

- `stateblock`
- `stable-long-context`

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

Activate `sequential-memory-state-engine` only after task framing, combine it with the declared
compatible controls, then validate its output before final commitment.

## Tests

See [`tests/composition.md`](tests/composition.md) for positive, negative,
conflict, and scaling cases.

## Provenance / Historical Aliases

Source ID: `T2-10` in `OS_Upgradeable_to_Skills_Translation_Catalog_v2_Recovery_Merged.md`. Registry generation:
`consolidated-2026-09`. Aliases: SMSE.
