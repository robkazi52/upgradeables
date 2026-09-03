# Decision-First Scaffold

## Summary

Provisional scaffold that makes the decision to be produced explicit before collecting supporting analysis.

## Purpose

Keep analysis shaped around a decision, options, and decision criteria rather than accumulating directionless detail.

## Problem Solved

A solver can perform substantial analysis without defining what choice, recommendation, or commitment the analysis must support.

## Where It Fits in the OS

Roles: reasoning scaffold, decision framing. Pipeline stages: task framing, pre-analysis.

This component acts within those stages; it does not take over the complete task or outrank the host Skill.

## Best-Fit Activities / Tasks

- recommendations
- go/no-go reviews
- option selection
- resource allocation

## When Not to Use

- the task asks only for faithful extraction or description
- the decision owner or available options are unknown
- framing a decision would falsely narrow an exploratory task

## Scope

Canonical package: `decision-first-scaffold@1.1.0`. ID: `JAN26-04`. Functional classes: planning-reasoning, output. Activation: `U1-common-conditional`. Mechanism basis: `provisional`. Activation cost: `low` (architectural burden, not measured compute).

## Trigger Conditions

- Activate when the task requires analysis risks becoming directionless.

## Non-Triggers

- the task asks only for faithful extraction or description
- the decision owner or available options are unknown
- framing a decision would falsely narrow an exploratory task

## Inputs / Required State

- decision request
- decision owner
- candidate options
- constraints
- criteria

## Outputs / Produced State

- decision frame
- criterion-linked analysis plan
- recommendation or evidence-gap decision

## Mechanism

Modern conservative interpretation: write a decision sentence with owner, options, criteria, and deadline or commitment point; then admit analysis only when it changes an option score, exposes a constraint, or reduces a named uncertainty. The historical corpus recovers the exact name but not this mechanism.

**Modern operational interpretation:** The procedure below is useful current guidance, not a claim that the full historical mechanism was recovered.

## Procedure

1. State the decision in one sentence, including who will act.
2. List viable options, including defer or gather-more-evidence where legitimate.
3. Lock decision criteria and non-negotiable constraints.
4. Map each analysis question to a criterion or uncertainty.
5. Produce a recommendation with the evidence and unresolved uncertainty that drives it.

## Always-Do Rules

- label the procedure as a modern interpretation
- distinguish decision criteria from supporting information
- preserve an explicit no-decision outcome when evidence is insufficient

## Never-Do / Avoid Rules

- claim the procedure is historically recovered
- force a decision into a descriptive task
- bury the actual decision below background analysis

## Interaction Rules

### `task-set-lock-in`

Task-Set Lock-In preserves the framed decision and constraints across a long run.

### `dominant-driver-isolation-scaffold`

Driver isolation can identify which criterion should dominate the recommendation.

## Compatible Upgradeables

- `task-set-lock-in` — Task-Set Lock-In preserves the framed decision and constraints across a long run.
- `dominant-driver-isolation-scaffold` — Driver isolation can identify which criterion should dominate the recommendation.

## Counterbalancing Upgradeables

### `anti-tunnel-vision`

Anti-Tunnel Vision prevents a decision-first frame from becoming first-option lock-in.

## Potential Redundancy

### `task-set-lock-in`

Both stabilize direction, but this provisional scaffold defines the decision while Task-Set Lock-In preserves an already defined task.

## Conflict / Precedence Rules

- If the user requests exploration without commitment, do not impose a final choice.
- If evidence cannot support any option, return the missing evidence rather than a fabricated recommendation.

## Failure Boundary

- invented historical mechanics
- premature option closure
- analysis unrelated to a criterion
- false certainty

## Strong-Model Scaling

May skip:

- a formal decision matrix for a simple binary choice

Keep mandatory:

- explicit decision statement
- criterion linkage
- uncertainty-aware outcome

## Recommended Skill Types

- analysis and decision support
- communication and content generation
- document and code transformation
- review and quality assurance

## Example Composition

**Task context:** Choose whether to migrate a service this quarter.

**Why it activates:** The team has collected architecture notes without defining the commitment.

**Inputs/state:** Two target platforms, a deadline, compliance constraints, and uncertain migration effort are known.

**Action:** Frames the quarter-specific go/no-go decision, maps compliance, cost, and migration risk to the two options, and recommends a gated pilot.

**Does not:** Treat every platform fact as equally decision-relevant.

**Result/state change:** A criterion-linked recommendation with a named evidence gate.

**Companions:** ['anti-tunnel-vision', 'task-set-lock-in']

## Tests

See [`tests/cases.json`](tests/cases.json) for six structured behavior cases and [`tests/composition.md`](tests/composition.md) for the human-readable expectations. Behavioral cases are specifications until run through a real model adapter; CI validates their structure, not model quality.

## Provenance / Historical Aliases

Primary source ID: `JAN26-04` in `OS_Upgradeables_Historical_Recovery_Inventory.md`. Registry generation: `training-scaffolding-2026-01-05`. Historical aliases: None.

Source support: `source-gap`. Mechanism basis: `provisional`.

Structured source references:

- OS_Upgradeable_to_Skills_Translation_Catalog_v2_Recovery_Merged.md — OS Philosophy and Upgradeable-to-Skill Translation Catalog (current_consolidated_catalog)
- OS_Upgradeables_Historical_Recovery_Inventory.md — 5. January 5, 2026 — training/scaffolding Upgradeables snapshot (historical_recovery_inventory)
