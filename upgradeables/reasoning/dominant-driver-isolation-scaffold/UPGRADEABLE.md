# Dominant-Driver Isolation Scaffold

## Summary

Provisional scaffold for identifying the smallest set of variables that accounts for most of an outcome.

## Purpose

Separate high-leverage causes or constraints from correlated, downstream, or low-impact factors.

## Problem Solved

When many causes are plausible, analysis can spread effort evenly and miss the factor that controls the decision or failure.

## Where It Fits in the OS

Roles: causal reasoning scaffold, attention allocator. Pipeline stages: diagnosis, prioritization, intervention selection.

This component acts within those stages; it does not take over the complete task or outrank the host Skill.

## Best-Fit Activities / Tasks

- root-cause analysis
- business driver analysis
- performance bottleneck diagnosis
- risk prioritization

## When Not to Use

- the system is known to require irreducibly joint causes
- available evidence supports only correlation
- the task requires a complete safety hazard inventory rather than prioritization

## Scope

Canonical package: `dominant-driver-isolation-scaffold@1.1.0`. ID: `JAN26-03`. Functional classes: planning-reasoning. Activation: `U1-common-conditional`. Mechanism basis: `provisional`. Activation cost: `low` (architectural burden, not measured compute).

## Trigger Conditions

- Activate when the task requires many possible causes compete.

## Non-Triggers

- the system is known to require irreducibly joint causes
- available evidence supports only correlation
- the task requires a complete safety hazard inventory rather than prioritization

## Inputs / Required State

- target outcome
- candidate causes or constraints
- measurements
- system boundary
- intervention options

## Outputs / Produced State

- ranked drivers
- evidence for marginal leverage
- single-driver or coupled-driver conclusion
- intervention focus

## Mechanism

Modern conservative interpretation: enumerate candidate drivers, define the target outcome, estimate each candidate's unique explanatory or intervention leverage, and test the leading driver against the strongest alternative and interaction effects. The historical sources recover only the scaffold's exact name.

**Modern operational interpretation:** The procedure below is useful current guidance, not a claim that the full historical mechanism was recovered.

## Procedure

1. Define the outcome and the time or system boundary.
2. List candidate drivers and distinguish causes, constraints, symptoms, and proxies.
3. Estimate each candidate's marginal effect using available comparisons, traces, or counterfactuals.
4. Test the leader against the strongest rival and check whether a pairwise interaction changes the ranking.
5. Select the dominant driver or report that no single driver is defensible; route effort accordingly.

## Always-Do Rules

- state the target outcome before ranking drivers
- separate causal evidence from correlation
- test the top-ranked driver against at least one rival

## Never-Do / Avoid Rules

- claim single-cause dominance when evidence supports a coupled system
- drop safety-critical minority risks
- present the provisional mechanics as recovered

## Interaction Rules

### `anti-tunnel-vision`

Anti-Tunnel Vision supplies a rival-driver check against fixation.

### `critical-atomic-verification`

Critical Atomic Verification can verify the key measurements on which driver ranking depends.

## Compatible Upgradeables

- `anti-tunnel-vision` — Anti-Tunnel Vision supplies a rival-driver check against fixation.
- `critical-atomic-verification` — Critical Atomic Verification can verify the key measurements on which driver ranking depends.

## Counterbalancing Upgradeables

### `multi-layer-consistency`

Multi-Layer Consistency checks whether local driver selection neglects a conflicting system-level dependency.

## Potential Redundancy

### `anti-tunnel-vision`

Both compare alternatives, but Driver Isolation ranks causal leverage while Anti-Tunnel Vision guards search breadth.

## Conflict / Precedence Rules

- A safety-critical factor is not discarded solely because its probability or average effect is lower.
- If interaction terms dominate marginal effects, return a coupled-driver result rather than forcing one winner.

## Failure Boundary

- correlation presented as cause
- single-factor oversimplification
- ranking without an outcome definition
- ignoring interactions

## Strong-Model Scaling

May skip:

- formal scoring when one measured bottleneck overwhelmingly dominates

Keep mandatory:

- rival test
- interaction check
- causal-evidence label

## Recommended Skill Types

- root-cause analysis
- business driver analysis
- performance bottleneck diagnosis
- risk prioritization

## Example Composition

**Task context:** Subscription churn increased.

**Why it activates:** Price, onboarding failures, outages, and seasonality all correlate with churn.

**Inputs/state:** Cohort data and incident timing permit marginal comparisons.

**Action:** Defines 30-day churn, separates the onboarding failure cohort, compares it with price-change cohorts, and reports onboarding failure as dominant only after interaction checks.

**Does not:** Choose the most salient anecdote or suppress a smaller safety-related concern.

**Result/state change:** A defensible intervention priority and limits on the causal claim.

**Companions:** ['anti-tunnel-vision', 'critical-atomic-verification']

## Tests

See [`tests/cases.json`](tests/cases.json) for six structured behavior cases and [`tests/composition.md`](tests/composition.md) for the human-readable expectations. Behavioral cases are specifications until run through a real model adapter; CI validates their structure, not model quality.

## Provenance / Historical Aliases

Primary source ID: `JAN26-03` in `OS_Upgradeables_Historical_Recovery_Inventory.md`. Registry generation: `training-scaffolding-2026-01-05`. Historical aliases: None.

Source support: `source-gap`. Mechanism basis: `provisional`.

Structured source references:

- OS_Upgradeable_to_Skills_Translation_Catalog_v2_Recovery_Merged.md — C. JANUARY 5, 2026 TRAINING / SCAFFOLDING UPGRADEABLES (current_consolidated_catalog)
- OS_Upgradeables_Historical_Recovery_Inventory.md — 5. January 5, 2026 — training/scaffolding Upgradeables snapshot (historical_recovery_inventory)
