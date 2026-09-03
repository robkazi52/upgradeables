# Bounded ExIt

## Summary

Run evaluate-repair cycles with an explicit quality threshold and iteration budget.

## Purpose

Provide a reusable `parent-skill-mode` mechanism rather than
a complete task identity or monolithic prompt.

## Problem Solved

Prevents the workflow failure implied by the trigger while keeping the
intervention bounded and inspectable.

## Scope

Functional classes: planning-reasoning, validation. Activation:
`U1-common-conditional`. This modern classification is not a historical tier.

## Trigger Conditions

- a draft needs iterative improvement

## Non-Triggers

- the declared trigger is absent or the control would add no material value

## Inputs / Required State

- locked task state
- available component manifests and authority rules

## Outputs / Produced State

- bounded activation or routing plan
- explicit component state and unresolved conflicts

## Mechanism

Evaluate the current output, select the highest-value defect, repair it, and stop at a quality threshold, iteration budget, or diminishing-return boundary. The ExIt acronym expansion remains unresolved.

The name is architectural identity, not a claim of a physical, biological,
hidden, or private-reasoning mechanism.

## Procedure

1. Evaluate against the locked goal and output contract.
2. Identify the highest-value remaining defect.
3. Apply the smallest sufficient repair.
4. Re-evaluate the changed result.
5. Stop when the threshold, budget, or diminishing-return rule is met.

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

- `micro-repair`
- `parallel-qms`

## Counterbalancing Upgradeables

- `None declared`

## Potential Redundancy

- `None declared`

## Conflict / Precedence Rules

Host/system safety, domain policy, the active OS, and the task lock take
precedence. On an unresolved material conflict, narrow, abstain, or escalate.

## Failure Boundary

- do not activate unavailable components or silently resolve an authority conflict

## Strong-Model Scaling

May skip: verbose intermediate scaffolding when the host model is reliable and the task is simple.
Keep mandatory: truth, state, safety, and integrity invariants whenever the task still requires them.

## Recommended Skill Types

- `general-agent-workflow`
- `high-stakes-reasoning`
- `research`
- `source-grounded-analysis`

## Example Composition

Activate `bounded-exit` only after task framing, combine it with the declared
compatible controls, then validate its output before final commitment.

## Tests

See [`tests/composition.md`](tests/composition.md) for positive, negative,
conflict, and scaling cases.

## Provenance / Historical Aliases

Source ID: `T2-01` in `OS_Upgradeable_to_Skills_Translation_Catalog_v2_Recovery_Merged.md`. Registry generation:
`consolidated-2026-09`. Aliases: None.
