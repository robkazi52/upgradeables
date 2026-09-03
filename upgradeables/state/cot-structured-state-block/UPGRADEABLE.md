# CoT-Structured State Block

## Summary

Represent task and reasoning state explicitly without claiming access to hidden or private chain-of-thought.

## Purpose

Provide a reusable `state-schema` mechanism rather than
a complete task identity or monolithic prompt.

## Problem Solved

Prevents the workflow failure implied by the trigger while keeping the
intervention bounded and inspectable.

## Scope

Functional classes: state. Activation:
`U1-common-conditional`. This modern classification is not a historical tier.

## Trigger Conditions

- structured intermediate task state must survive across steps

## Non-Triggers

- the declared trigger is absent or the control would add no material value

## Inputs / Required State

- current explicit task state
- authorized state update or source event

## Outputs / Produced State

- updated explicit state
- conflict or unavailable-persistence status

## Mechanism

Store explicit, auditable reasoning-state atoms such as InputFacts, Inference, Phase, and Topic; apply phase separation, topic isolation, truth gates, and risk-dependent vetoes without recording private chain-of-thought.

The name is architectural identity, not a claim of a physical, biological,
hidden, or private-reasoning mechanism.

## Procedure

1. Capture source-backed InputFacts.
2. Record only concise task-relevant inferences with epistemic status.
3. Label semantic Phase and Topic.
4. Apply domain/topic isolation and high-risk truth gates.
5. Return an auditable state object or fail-closed status.

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
- `sequential-memory-state-engine`

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

Activate `cot-structured-state-block` only after task framing, combine it with the declared
compatible controls, then validate its output before final commitment.

## Tests

See [`tests/composition.md`](tests/composition.md) for positive, negative,
conflict, and scaling cases.

## Provenance / Historical Aliases

Source ID: `STATE-2025-12-03-T3` in `OS_Upgradeable_to_Skills_Translation_Catalog_v2_Recovery_Merged.md`. Registry generation:
`consolidated-2026-09`. Aliases: None.
Exact recovered name and role; modern implementations expose task state only.
