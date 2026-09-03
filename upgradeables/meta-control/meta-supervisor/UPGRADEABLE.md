# Meta-Supervisor Bundle

## Summary

Monitor process health, active modes, state, loops, contradictions, and module interactions.

## Purpose

Provide a reusable `orchestrator` mechanism rather than
a complete task identity or monolithic prompt.

## Problem Solved

Prevents the workflow failure implied by the trigger while keeping the
intervention bounded and inspectable.

## Scope

Functional classes: meta-control, orchestration, validation. Activation:
`U4-meta-architecture`. This modern classification is not a historical tier.

## Trigger Conditions

- complex scaffolding itself needs supervision

## Non-Triggers

- the declared trigger is absent or the control would add no material value

## Inputs / Required State

- locked task state
- available component manifests and authority rules

## Outputs / Produced State

- bounded activation or routing plan
- explicit component state and unresolved conflicts

## Mechanism

Select and sequence only available components whose triggers match, pass explicit state between them, and resolve authority before execution.

The name is architectural identity, not a claim of a physical, biological,
hidden, or private-reasoning mechanism.

## Procedure

1. Confirm task identity, risk, and authority.
2. Inspect available component manifests and triggers.
3. Select the minimum sufficient composition and load order.
4. Pass explicit bounded state through the selected interfaces.
5. Emit the plan/result plus unresolved conflicts and unavailable capabilities.

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

- `meta-awareness`
- `stuck-pattern-reset`
- `contradiction-micro-repair`

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

- `architecture-skill-building`
- `general-agent-workflow`
- `high-stakes-reasoning`
- `multi-agent-orchestration`
- `research`
- `source-grounded-analysis`

## Example Composition

Activate `meta-supervisor` only after task framing, combine it with the declared
compatible controls, then validate its output before final commitment.

## Tests

See [`tests/composition.md`](tests/composition.md) for positive, negative,
conflict, and scaling cases.

## Provenance / Historical Aliases

Source ID: `T4-01` in `OS_Upgradeable_to_Skills_Translation_Catalog_v2_Recovery_Merged.md`. Registry generation:
`consolidated-2026-09`. Aliases: None.
