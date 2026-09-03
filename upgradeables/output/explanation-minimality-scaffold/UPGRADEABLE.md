# Explanation Minimality Scaffold

## Summary

Use the shortest explanation that remains accurate, sufficient, and appropriate for the audience.

## Purpose

Provide a reusable `skill-component` mechanism rather than
a complete task identity or monolithic prompt.

## Problem Solved

Prevents the workflow failure implied by the trigger while keeping the
intervention bounded and inspectable.

## Scope

Functional classes: output. Activation:
`U1-common-conditional`. This modern classification is not a historical tier.

## Trigger Conditions

- verbosity can obscure the answer

## Non-Triggers

- the declared trigger is absent or the control would add no material value

## Inputs / Required State

- locked task goal and constraints
- relevant source or workflow state

## Outputs / Produced State

- bounded component result
- explicit uncertainty or failure status when applicable

## Mechanism

Apply the named behavior as an explicit, bounded control over the declared input and state, then record the result or failure status.

The name is architectural identity, not a claim of a physical, biological,
hidden, or private-reasoning mechanism.

## Procedure

1. Confirm the task lock, authority layer, and trigger.
2. Read only the required state and evidence.
3. Apply the documented bounded behavior.
4. Check protected truth, state, safety, and output invariants.
5. Emit the result or an explicit unsupported/blocked status.

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

- `pedagogical-alignment`

## Counterbalancing Upgradeables

- `None declared`

## Potential Redundancy

- `None declared`

## Conflict / Precedence Rules

Host/system safety, domain policy, the active OS, and the task lock take
precedence. On an unresolved material conflict, narrow, abstain, or escalate.

## Failure Boundary

- do not claim success when required evidence, state, host capability, or validation is unavailable

## Strong-Model Scaling

May skip: verbose intermediate scaffolding when the host model is reliable and the task is simple.
Keep mandatory: truth, state, safety, and integrity invariants whenever the task still requires them.

## Recommended Skill Types

- `authoring`
- `coding-debugging`
- `general-agent-workflow`

## Example Composition

Activate `explanation-minimality-scaffold` only after task framing, combine it with the declared
compatible controls, then validate its output before final commitment.

## Tests

See [`tests/composition.md`](tests/composition.md) for positive, negative,
conflict, and scaling cases.

## Provenance / Historical Aliases

Source ID: `JAN26-08` in `OS_Upgradeable_to_Skills_Translation_Catalog_v2_Recovery_Merged.md`. Registry generation:
`training-scaffolding-2026-01-05`. Aliases: None.
Exact name recovery; operational mechanism is a conservative modern interpretation.
