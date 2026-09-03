# Regenerative Rewrite

## Summary

Rebuild an output when local repair cannot restore global structure or coherence, while preserving locked truths.

## Purpose

Provide a reusable `skill-component` mechanism rather than
a complete task identity or monolithic prompt.

## Problem Solved

Prevents the workflow failure implied by the trigger while keeping the
intervention bounded and inspectable.

## Scope

Functional classes: editing-repair. Activation:
`U2-specialized`. This modern classification is not a historical tier.

## Trigger Conditions

- architecture or source mapping is globally broken

## Non-Triggers

- the declared trigger is absent or the control would add no material value

## Inputs / Required State

- source artifact
- authorized change request
- protected facts and invariants

## Outputs / Produced State

- bounded patch or revised artifact
- preservation and validation status

## Mechanism

Classify the defect and apply the smallest authorized edit that can restore correctness while protecting facts, citations, and invariants.

The name is architectural identity, not a claim of a physical, biological,
hidden, or private-reasoning mechanism.

## Procedure

1. Locate and classify the defect.
2. Lock surrounding facts and invariants.
3. Apply the smallest sufficient repair class.
4. Compare the result with the source and requested change.
5. Escalate or stop if the protected invariants cannot be preserved.

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

- `task-set-lock-in`
- `surgery-edit`

## Counterbalancing Upgradeables

- `micro-repair`

## Potential Redundancy

- `None declared`

## Conflict / Precedence Rules

Host/system safety, domain policy, the active OS, and the task lock take
precedence. On an unresolved material conflict, narrow, abstain, or escalate.

## Failure Boundary

- escalate the repair class or stop when protected invariants cannot be preserved

## Strong-Model Scaling

May skip: verbose intermediate scaffolding when the host model is reliable and the task is simple.
Keep mandatory: truth, state, safety, and integrity invariants whenever the task still requires them.

## Recommended Skill Types

- `authoring`
- `coding-debugging`
- `general-agent-workflow`

## Example Composition

Activate `regenerative-rewrite` only after task framing, combine it with the declared
compatible controls, then validate its output before final commitment.

## Tests

See [`tests/composition.md`](tests/composition.md) for positive, negative,
conflict, and scaling cases.

## Provenance / Historical Aliases

Source ID: `T2-03` in `OS_Upgradeable_to_Skills_Translation_Catalog_v2_Recovery_Merged.md`. Registry generation:
`consolidated-2026-09`. Aliases: None.
