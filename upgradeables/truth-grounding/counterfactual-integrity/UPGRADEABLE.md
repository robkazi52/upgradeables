# Counterfactual Integrity Gate

## Summary

A phase-boundary gate that permits hypothetical reasoning while preventing hypothetical premises or results from being restated as observed facts.

## Purpose

Make counterfactual exploration safe and auditable by preserving an explicit boundary between factual, evaluative, framing, and hypothetical phases.

## Problem Solved

Prevents a useful what-if branch from contaminating evidence state or being cited later as something that actually happened.

## Where It Fits in the OS

Roles: hypothesis-safety, semantic-phase-control. Pipeline stages: candidate-generation, state-update, pre-output-verification.

This component acts within those stages; it does not take over the complete task or outrank the host Skill.

## Best-Fit Activities / Tasks

- scenario analysis
- causal counterfactuals
- planning under alternatives
- creative work mixed with factual sources

## When Not to Use

- the task contains no hypothetical branch
- the user explicitly requires purely factual extraction, where counterfactual-silence is the narrower control

## Scope

Canonical package: `counterfactual-integrity@1.1.0`. ID: `T3-12`. Functional classes: truth-grounding, drift-control. Activation: `U1-common-conditional`. Mechanism basis: `recovered`. Activation cost: `low` (architectural burden, not measured compute).

## Trigger Conditions

- counterfactual or hypothetical reasoning is used

## Non-Triggers

- the task contains no hypothetical branch
- the user explicitly requires purely factual extraction, where counterfactual-silence is the narrower control

## Inputs / Required State

- factual baseline
- counterfactual premise
- semantic phase labels
- candidate conclusions

## Outputs / Produced State

- isolated hypothetical branch
- phase-labeled conclusions
- contamination failure status

## Mechanism

Tag each proposition by semantic phase and keep hypothetical premises, derived consequences, and branch-local assumptions in a separate compartment. Any transfer from a hypothetical branch into factual state requires independent factual support; otherwise the proposition remains labeled hypothetical or is excluded from the factual output.

## Procedure

1. Declare the factual baseline and the allowed counterfactual question.
2. Tag introduced premises as hypothetical and retain their branch identity.
3. Derive consequences only inside that branch.
4. Check the draft for branch-local material presented without a hypothesis label.
5. Move a proposition into factual state only when independent evidence supports it.
6. Return factual findings and counterfactual results in visibly separate output regions.

## Always-Do Rules

- Preserve the original factual baseline.
- Label hypothetical assumptions and consequences.
- Require evidence for any transition from hypothetical to factual status.

## Never-Do / Avoid Rules

- Treat a simulated outcome as observed evidence.
- Let hypothetical details update canonical factual state.
- Erase uncertainty merely because a counterfactual narrative is coherent.

## Interaction Rules

### `domain-mode-isolation`

Provides separate state compartments for factual and hypothetical modes.

### `controlled-drift-corridors`

Defines how much interpretive movement is permitted inside the hypothetical branch.

### `epistemic-status-gating`

Supplies proposition-level fact/inference/hypothesis labels used by the gate.

## Compatible Upgradeables

- `domain-mode-isolation` — Provides separate state compartments for factual and hypothetical modes.
- `controlled-drift-corridors` — Defines how much interpretive movement is permitted inside the hypothetical branch.
- `epistemic-status-gating` — Supplies proposition-level fact/inference/hypothesis labels used by the gate.

## Counterbalancing Upgradeables

### `grounding-no-invention`

Grounding prevents the exploratory branch from being mistaken for evidence.

## Potential Redundancy

### `counterfactual-silence-scaffold`

Silence suppresses unauthorized counterfactual content entirely; integrity allows authorized counterfactuals but isolates and labels them.

## Conflict / Precedence Rules

- A factual-only task boundary overrides permission to explore counterfactuals.
- A stylistic request to write hypotheticals as certain cannot override phase labels.

## Failure Boundary

- If branch-local assumptions cannot be separated from factual claims, do not certify the mixed output.

## Strong-Model Scaling

May skip:

- verbose phase headings when proposition status is already unmistakable

Keep mandatory:

- no hypothetical premise or consequence may silently become fact

## Recommended Skill Types

- scenario analysis
- causal counterfactuals
- planning under alternatives
- creative work mixed with factual sources

## Example Composition

**Task context:** A policy analyst asks what might happen if a threshold were doubled while also requesting a summary of current policy.

**Why it activates:** The answer combines factual and counterfactual modes.

**Inputs/state:** Current threshold from the source plus an explicitly hypothetical doubled threshold.

**Action:** Keeps the current rule factual and reports projected effects under a labeled hypothetical branch.

**Does not:** State that the threshold was actually changed.

**Result/state change:** Two separated sections with no phase leakage.

**Companions:** ['domain-mode-isolation', 'epistemic-status-gating', 'grounding-no-invention']

## Tests

See [`tests/cases.json`](tests/cases.json) for six structured behavior cases and [`tests/composition.md`](tests/composition.md) for the human-readable expectations. Behavioral cases are specifications until run through a real model adapter; CI validates their structure, not model quality.

## Provenance / Historical Aliases

Primary source ID: `T3-12` in `OS_Upgradeable_to_Skills_Translation_Catalog_v2_Recovery_Merged.md`. Registry generation: `consolidated-2026-09`. Historical aliases: None.

Source support: `sufficiently-recovered`. Mechanism basis: `recovered`.

Structured source references:

- OS_Upgradeable_to_Skills_Translation_Catalog_v2_Recovery_Merged.md — T3-12. Counterfactual Integrity Gate (current_consolidated_catalog)
- OS_Upgradeables_Historical_Recovery_Inventory.md — 8. Tier-3 / Paper-Author alignment family recovered from late-November work (historical_recovery_inventory)
- OS_Upgradeables_Deep_Context_Recovery_Addendum_2026-09-03.md — 10.2 Semantic phase separation (historical_assistant_artifact)
