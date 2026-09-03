# Invariance Stress Scaffold

## Summary

A provisional scaffold for testing whether a result retains its claimed core properties under controlled, meaning-preserving perturbations.

## Purpose

Operationalize the recovered name without pretending the original January 2026 mechanics were recovered.

## Problem Solved

A conclusion may depend on incidental wording, ordering, or representation despite claiming to be robust to those changes.

## Where It Fits in the OS

Roles: provisional-robustness-probe, representation-sensitivity-detector. Pipeline stages: post-draft validation, pre-release stress testing.

This component acts within those stages; it does not take over the complete task or outrank the host Skill.

## Best-Fit Activities / Tasks

- prompt robustness checks
- policy interpretation
- classification stability
- summary validation

## When Not to Use

- the transformed feature is itself decision-relevant
- the invariants cannot be stated
- the task requires the unrecovered historical implementation

## Scope

Canonical package: `invariance-stress-scaffold@1.1.0`. ID: `JAN26-09`. Functional classes: validation, editing-repair. Activation: `U1-common-conditional`. Mechanism basis: `modern-interpretation`. Activation cost: `low` (architectural burden, not measured compute).

## Trigger Conditions

- a patch or rewrite must preserve invariants

## Non-Triggers

- the transformed feature is itself decision-relevant
- the invariants cannot be stated
- the task requires the unrecovered historical implementation

## Inputs / Required State

- artifact or prompt
- declared invariants
- bounded perturbations
- meaning-changing controls
- comparison metrics

## Outputs / Produced State

- invariance matrix
- sensitivity findings
- narrowed robustness claim
- unresolved source-gap notice

## Mechanism

Define the properties claimed invariant, generate a small controlled set of transformations that should preserve those properties—such as reordering independent facts, paraphrasing without modal change, or changing irrelevant formatting—and compare outputs. Any decision-relevant change is reported as sensitivity; this is a modern stress-test interpretation, not a recovered historical algorithm.

**Modern operational interpretation:** The procedure below is useful current guidance, not a claim that the full historical mechanism was recovered.

## Procedure

1. State the claimed invariant and observable pass condition.
2. Separate semantics-preserving perturbations from meaning-changing controls.
3. Construct a bounded perturbation set and preserve provenance.
4. Run the task independently on original and perturbed inputs.
5. Compare conclusions, confidence, constraints, and safety behavior.
6. Classify differences as acceptable presentation variation or invariant breach.
7. Report sensitivity and narrow the original robustness claim.

## Always-Do Rules

- Declare why each perturbation should preserve the target property.
- Include at least one meaning-changing control to confirm the test can detect legitimate change.
- Label this mechanism as modern interpretation.

## Never-Do / Avoid Rules

- Call arbitrary input changes invariance tests.
- Require identical wording when only conclusions should be invariant.
- Attribute this procedure to unrecovered historical source.

## Interaction Rules

### `safe-rewrite`

Defines transformations intended to preserve meaning.

### `crispr-edit`

Can isolate a single controlled perturbation.

### `multi-layer-consistency`

Checks whether discovered sensitivity propagates across representation layers.

## Compatible Upgradeables

- `safe-rewrite` — Defines transformations intended to preserve meaning.
- `crispr-edit` — Can isolate a single controlled perturbation.
- `multi-layer-consistency` — Checks whether discovered sensitivity propagates across representation layers.

## Counterbalancing Upgradeables

### `controlled-drift-corridors`

Prevents an overly rigid invariant definition from banning harmless surface variation inside a declared corridor.

## Potential Redundancy

### `parallel-qms`

Monte QMS perturbs assumptions, wording, or structure as a validator mode; this scaffold is a standalone, explicitly provisional invariance protocol.

## Conflict / Precedence Rules

- Meaning-changing controls are not invariant breaches.
- Safety behavior must remain at least as conservative under semantics-preserving perturbations.

## Failure Boundary

- Do not claim robustness when decision-relevant output changes under a justified semantics-preserving perturbation.

## Strong-Model Scaling

May skip:

- large perturbation suites for low-risk one-off output

Keep mandatory:

- explicit invariant and at least one controlled counterfactual comparison when robustness is claimed

## Recommended Skill Types

- prompt robustness checks
- policy interpretation
- classification stability
- summary validation

## Example Composition

**Task context:** A review classifier is claimed to find unsafe assumptions regardless of bullet order.

**Why it activates:** Order is supposed to be irrelevant to the safety judgment.

**Inputs/state:** Original review, reordered version, faithful paraphrase, and one version removing a safety fact as control.

**Action:** Compares findings across preserving variants and confirms the control legitimately changes the result.

**Does not:** Treat removal of a safety fact as a preserving perturbation.

**Result/state change:** A missed finding after bullet reorder exposes order sensitivity and narrows the reliability claim.

**Companions:** ['safe-rewrite', 'crispr-edit', 'multi-layer-consistency']

## Tests

See [`tests/cases.json`](tests/cases.json) for six structured behavior cases and [`tests/composition.md`](tests/composition.md) for the human-readable expectations. Behavioral cases are specifications until run through a real model adapter; CI validates their structure, not model quality.

## Provenance / Historical Aliases

Primary source ID: `JAN26-09` in `OS_Upgradeables_Historical_Recovery_Inventory.md`. Registry generation: `training-scaffolding-2026-01-05`. Historical aliases: None.

Source support: `source-gap`. Mechanism basis: `modern-interpretation`.

Structured source references:

- OS_Upgradeable_to_Skills_Translation_Catalog_v2_Recovery_Merged.md — C. JANUARY 5, 2026 TRAINING / SCAFFOLDING UPGRADEABLES (current_consolidated_catalog)
- OS_Upgradeables_Historical_Recovery_Inventory.md — Invariance Stress Scaffold (historical_recovery_inventory)
- OS_Upgradeables_Deep_Context_Recovery_Addendum_2026-09-03.md — 20. RECOVERY GAPS AFTER DEEP PASS 2.0 (historical_assistant_artifact)
