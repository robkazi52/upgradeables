# Grounding / No-Invention

## Summary

Keep factual output within supplied or verified evidence and label or omit unsupported material.

## Purpose

Provide a reusable `validator` mechanism rather than
a complete task identity or monolithic prompt.

## Problem Solved

Prevents the workflow failure implied by the trigger while keeping the
intervention bounded and inspectable.

## Scope

Functional classes: truth-grounding, validation. Activation:
`U0-foundational`. This modern classification is not a historical tier.

## Trigger Conditions

- work relies on documents, data, external facts, or consequential claims

## Non-Triggers

- the declared trigger is absent or the control would add no material value

## Inputs / Required State

- candidate factual claims
- supplied or verified evidence boundary

## Outputs / Produced State

- supported claims
- labeled inference
- omitted/uncertain unsupported claims

## Mechanism

Evaluate the candidate against declared evidence, constraints, and invariants, then return a status or veto. Inspection never supplies missing facts.

The name is architectural identity, not a claim of a physical, biological,
hidden, or private-reasoning mechanism.

## Procedure

1. Confirm the trigger and governing criteria.
2. Identify the candidate units that require checking.
3. Evaluate each unit against available evidence and invariants.
4. Return pass, fail, repair-required, or unverifiable with defect locations.
5. Block certification when the failure boundary is reached.

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

- `citation-fidelity`
- `fail-closed-abstention`

## Counterbalancing Upgradeables

- `None declared`

## Potential Redundancy

- `None declared`

## Conflict / Precedence Rules

Host/system safety, domain policy, the active OS, and the task lock take
precedence. On an unresolved material conflict, narrow, abstain, or escalate.

## Failure Boundary

- when an essential claim lacks support, fail closed instead of filling the gap

## Strong-Model Scaling

May skip: verbose intermediate scaffolding when the host model is reliable and the task is simple.
Keep mandatory: truth, state, safety, and integrity invariants whenever the task still requires them.

## Recommended Skill Types

- `general-agent-workflow`
- `high-stakes-reasoning`
- `research`
- `source-grounded-analysis`

## Example Composition

Activate `grounding-no-invention` only after task framing, combine it with the declared
compatible controls, then validate its output before final commitment.

## Tests

See [`tests/composition.md`](tests/composition.md) for positive, negative,
conflict, and scaling cases.

## Provenance / Historical Aliases

Source ID: `T1-04` in `OS_Upgradeable_to_Skills_Translation_Catalog_v2_Recovery_Merged.md`. Registry generation:
`consolidated-2026-09`. Aliases: None.
