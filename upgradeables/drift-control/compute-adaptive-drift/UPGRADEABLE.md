# Compute-Adaptive Drift Constraining

## Summary

Adjust the amount of drift-checking structure to available model/tool capacity while leaving truth, authority, and zero-drift invariants unchanged.

## Purpose

Maintain semantic reliability across weak and strong runtimes without burdening every runtime identically.

## Problem Solved

A light model may need explicit checkpoints and narrow transformations, while a strong model can safely compress process; a fixed protocol either under-controls or overburdens.

## Where It Fits in the OS

Roles: capability adaptation, drift-control scaling, runtime policy. Pipeline stages: runtime assessment, plan construction, checkpoint scheduling, validation.

This component acts within those stages; it does not take over the complete task or outrank the host Skill.

## Best-Fit Activities / Tasks

- cross-model skills
- variable tool availability
- cost-limited execution
- mixed-capability agents

## When Not to Use

- adaptation would weaken factual or safety invariants
- runtime capability is unknown in a high-risk task
- the task already uses the strict minimum safe protocol

## Scope

Canonical package: `compute-adaptive-drift@1.1.0`. ID: `T4-10`. Functional classes: drift-control, meta-control. Activation: `U2-specialized`. Mechanism basis: `normalized-from-recovered`. Activation cost: `medium` (architectural burden, not measured compute).

## Trigger Conditions

- compute/depth varies across a task

## Non-Triggers

- adaptation would weaken factual or safety invariants
- runtime capability is unknown in a high-risk task
- the task already uses the strict minimum safe protocol

## Inputs / Required State

- task risk
- zero-drift invariants
- runtime capability evidence
- tool availability
- calibration results

## Outputs / Produced State

- runtime-specific control profile
- checkpoint schedule
- step and corridor settings
- unchanged semantic acceptance tests

## Mechanism

Classify the task risk and runtime's demonstrated capacity, then choose an enforcement profile: weaker or unverified runtimes receive smaller steps, explicit state, more frequent source checks, and tighter drift corridors; stronger verified runtimes may combine steps and reduce scaffolding. The semantic acceptance tests, authority hierarchy, citations, and zero-drift fields never relax.

## Procedure

1. Classify consequence of drift and identify non-negotiable invariants.
2. Assess demonstrated context, reasoning, tool, and verification capacity without trusting branding alone.
3. Choose checkpoint frequency, step size, scaffold depth, and corridor width.
4. Run a calibration or early sample against the same semantic tests.
5. Tighten controls on failure; relax only process overhead after repeated success.
6. Record the chosen profile and validate the final result identically across runtimes.

## Always-Do Rules

- hold truth and authority invariants constant
- adapt from observed capability
- tighten on uncertainty
- use identical outcome tests

## Never-Do / Avoid Rules

- treat more compute as permission to invent
- weaken citations or safety gates
- infer capability solely from model name
- hide which controls were relaxed

## Interaction Rules

### `controlled-drift-corridors`

Changes permitted transformation width as one dimension of the runtime profile.

### `drift-suppression`

Scales detection and correction frequency.

### `micro-scaffolding`

Adds task-local structure for runtimes that need more execution support.

## Compatible Upgradeables

- `controlled-drift-corridors` — Changes permitted transformation width as one dimension of the runtime profile.
- `drift-suppression` — Scales detection and correction frequency.
- `micro-scaffolding` — Adds task-local structure for runtimes that need more execution support.

## Counterbalancing Upgradeables

### `zero-drift-zones`

Keeps immutable fields fixed regardless of compute.

### `future-proof-mode-selector`

May remove redundant ceremony after outcome capability is demonstrated.

## Potential Redundancy

### `domain-normalized-drift`

Domain defaults set the baseline; compute adaptation adjusts process around that baseline, not the domain truth standard.

### `drift-spectra-scaling`

Spectra maps task regions; compute adaptation maps runtime capacity.

## Conflict / Precedence Rules

- Task risk and zero-drift requirements cap any relaxation due to compute.
- When capability evidence conflicts, use the stricter profile until a calibration passes.

## Failure Boundary

- Do not relax controls for high-impact claims without demonstrated validation performance.
- Fall back to the strict profile when runtime behavior is unstable or unobservable.

## Strong-Model Scaling

May skip:

- step-by-step micro-scaffolds after calibration
- redundant intermediate restatement
- high-frequency checks for low-drift regions

Keep mandatory:

- zero-drift fields
- authority hierarchy
- source grounding
- outcome-level semantic tests

## Recommended Skill Types

- document and code transformation
- long-context workflows
- multi-step task execution
- skill and agent workflows

## Example Composition

**Task context:** The same source-grounded comparison skill runs on a compact model and a frontier model.

**Why it activates:** They differ in reliable context handling but must meet the same evidence standard.

**Inputs/state:** High-risk claims, model calibration results, source tools, and fixed citation tests.

**Action:** Gives the compact model smaller source batches and per-claim checks; permits the frontier model to batch low-risk extraction after it passes calibration.

**Does not:** It does not let either model omit citations or alter locked facts.

**Result/state change:** Different process overhead, identical semantic acceptance boundary.

**Companions:** ['controlled-drift-corridors', 'drift-suppression', 'zero-drift-zones']

## Tests

See [`tests/cases.json`](tests/cases.json) for six structured behavior cases and [`tests/composition.md`](tests/composition.md) for the human-readable expectations. Behavioral cases are specifications until run through a real model adapter; CI validates their structure, not model quality.

## Provenance / Historical Aliases

Primary source ID: `T4-10` in `OS_Upgradeable_to_Skills_Translation_Catalog_v2_Recovery_Merged.md`. Registry generation: `consolidated-2026-09`. Historical aliases: CADC.

Source support: `strongly-derivable`. Mechanism basis: `normalized-from-recovered`.

Structured source references:

- OS_Upgradeable_to_Skills_Translation_Catalog_v2_Recovery_Merged.md — OS Philosophy and Upgradeable-to-Skill Translation Catalog (current_consolidated_catalog)
- OS_Upgradeables_Historical_Recovery_Inventory.md — ECL / Drift Sink (historical_recovery_inventory)
- OS_Upgradeables_Deep_Context_Recovery_Addendum_2026-09-03.md — 10.3 Drift widths (historical_assistant_artifact)
