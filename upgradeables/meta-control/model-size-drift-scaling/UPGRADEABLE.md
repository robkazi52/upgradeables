# Drift-Stability Scaling with Model Size

## Summary

Scales optional drift-control scaffolding from measured base-model reliability while retaining truth, state, safety, and integrity invariants at every capability level.

## Purpose

Avoid fossilized over-scaffolding on more reliable models without mistaking model strength for permission to remove essential controls.

## Problem Solved

Static prompts can burden stronger models with redundant repetition, while naive capability optimism can strip grounding and state guards that remain necessary.

## Where It Fits in the OS

Roles: model-reliability scaling policy, scaffold simplification controller. Pipeline stages: model evaluation, control classification, scaffold scaling, regression monitoring.

This component acts within those stages; it does not take over the complete task or outrank the host Skill.

## Best-Fit Activities / Tasks

- cross-model deployments
- model upgrades
- prompt simplification
- reliability-sensitive drift control

## When Not to Use

- there is no comparative reliability evidence
- the control is a non-negotiable invariant
- environment limitations rather than model behavior are the dominant issue

## Scope

Canonical package: `model-size-drift-scaling@1.1.0`. ID: `T4-18`. Functional classes: meta-control, drift-control. Activation: `U4-meta-architecture`. Mechanism basis: `normalized-from-recovered`. Activation cost: `high` (architectural burden, not measured compute).

## Trigger Conditions

- adapting a workflow across model capability levels

## Non-Triggers

- there is no comparative reliability evidence
- the control is a non-negotiable invariant
- environment limitations rather than model behavior are the dominant issue

## Inputs / Required State

- model reliability evidence
- control inventory and classification
- task family
- regression thresholds
- risk requirements

## Outputs / Produced State

- model-specific scaffold tier
- retained and compressed control map
- regression evidence
- reactivation rules

## Mechanism

Classify controls as invariant, compensatory, or convenience scaffolds; measure each target model on task-relevant drift, instruction retention, state consistency, and validation behavior; reduce only compensatory repetition whose function is demonstrably supplied by the base model. Preserve invariant truth, safety, authority, and external-state checks and restore removed scaffolds automatically when regression thresholds fail. DSS-MS scales control density by measured reliability; FPMS decides the wider host profile.

## Procedure

1. Inventory controls and classify each as invariant, compensatory, or convenience.
2. Evaluate the target model on representative drift, state, truth, and failure cases.
3. Map measured reliability to a predeclared scaffold tier.
4. Remove or compress one compensatory control class at a time while retaining invariants.
5. Run regression and adversarial tests against the prior configuration.
6. Publish the model-specific profile with reactivation thresholds and monitor for regressions.

## Always-Do Rules

- use task-relevant evidence rather than size labels alone
- preserve invariants
- change one control class at a time
- keep reactivation thresholds

## Never-Do / Avoid Rules

- assume frontier means drift-free
- remove external capability checks
- treat benchmark score as universal reliability
- drop safety or truth controls for latency

## Interaction Rules

### `future-proof-mode-selector`

FPMS combines this reliability profile with tools, state, environment, and risk to choose an operating mode.

### `risk-tier-scaling`

Risk tiers can require heavy validation even on a highly reliable model.

## Compatible Upgradeables

- `future-proof-mode-selector` — FPMS combines this reliability profile with tools, state, environment, and risk to choose an operating mode.
- `risk-tier-scaling` — Risk tiers can require heavy validation even on a highly reliable model.

## Counterbalancing Upgradeables

### `meta-awareness`

Meta-Awareness detects process regressions that should reactivate compensatory scaffolds.

## Potential Redundancy

### `future-proof-mode-selector`

DSS-MS generates model-reliability scaling; FPMS performs the broader multi-factor selection.

### `cognitive-governor`

Cognitive Governor budgets effort per task; DSS-MS configures scaffold density per model profile.

## Conflict / Precedence Rules

- Invariant controls do not scale away.
- High task risk may force a heavier profile than average model reliability suggests.
- If evidence is absent or mixed, retain the prior conservative control tier.

## Failure Boundary

- size-as-capability assumption
- invariant removal
- benchmark overgeneralization
- irreversible simplification
- regression without reactivation

## Strong-Model Scaling

May skip:

- redundant restatement and low-value self-reminders proven unnecessary for the task family

Keep mandatory:

- truth and safety gates
- explicit external-state checks
- task-relevant regression tests
- reactivation path

## Recommended Skill Types

- cross-model deployments
- model upgrades
- prompt simplification
- reliability-sensitive drift control

## Example Composition

**Task context:** Move a skill suite from an older model to a more reliable frontier model.

**Why it activates:** Repeated planning reminders may be unnecessary, but source fidelity and tool-state checks remain essential.

**Inputs/state:** Matched evaluations, control inventory, risk tiers, and rollback profiles are available.

**Action:** Compresses proven-redundant planning prompts, retains grounding and state checks, runs regressions, and publishes a reversible frontier profile.

**Does not:** Remove citations and safety gates because the new model is larger.

**Result/state change:** Lower overhead without loss of measured integrity.

**Companions:** ['future-proof-mode-selector', 'risk-tier-scaling']

## Tests

See [`tests/cases.json`](tests/cases.json) for six structured behavior cases and [`tests/composition.md`](tests/composition.md) for the human-readable expectations. Behavioral cases are specifications until run through a real model adapter; CI validates their structure, not model quality.

## Provenance / Historical Aliases

Primary source ID: `T4-18` in `OS_Upgradeable_to_Skills_Translation_Catalog_v2_Recovery_Merged.md`. Registry generation: `consolidated-2026-09`. Historical aliases: DSS-MS.

Source support: `sufficiently-recovered`. Mechanism basis: `normalized-from-recovered`.

Structured source references:

- OS_Upgradeable_to_Skills_Translation_Catalog_v2_Recovery_Merged.md — T4-18. Drift-Stability Scaling with Model Size (DSS-MS) (current_consolidated_catalog)
- OS_Upgradeables_Historical_Recovery_Inventory.md — 10. Tier-4 / Meta-Supervisor recovered family (historical_recovery_inventory)
- OS_Upgradeables_Deep_Context_Recovery_Addendum_2026-09-03.md — 16. COPILOT / DOCUMENT-BASED IMPLEMENTATION CONSTRAINTS (historical_assistant_artifact)
