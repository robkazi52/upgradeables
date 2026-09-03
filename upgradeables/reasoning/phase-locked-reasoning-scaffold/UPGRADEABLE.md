# Phase-Locked Reasoning Scaffold

## Summary

Keeps recovered semantic phases separate so factual, evidentiary, probabilistic, and heuristic claims do not silently substitute for one another.

## Purpose

Prevent cross-phase contamination while still allowing explicitly governed transitions between reasoning modes.

## Problem Solved

A plausible interpretation or heuristic can be written as a fact, or an evidence-management step can drift into unsupported synthesis, when phase boundaries are implicit.

## Where It Fits in the OS

Roles: reasoning scaffold, semantic phase boundary. Pipeline stages: evidence processing, analysis, synthesis, final validation.

This component acts within those stages; it does not take over the complete task or outrank the host Skill.

## Best-Fit Activities / Tasks

- evidence-grounded writing
- multi-source research
- risk analysis
- long workflows with distinct reasoning modes

## When Not to Use

- a single atomic transformation has no phase transition
- phase labels would add more complexity than the task
- the underlying source classification is itself unknown

## Scope

Canonical package: `phase-locked-reasoning-scaffold@1.1.0`. ID: `JAN26-01`. Functional classes: planning-reasoning, state. Activation: `U2-specialized`. Mechanism basis: `normalized-from-recovered`. Activation cost: `medium` (architectural burden, not measured compute).

## Trigger Conditions

- semantic phase leakage is a risk

## Non-Triggers

- a single atomic transformation has no phase transition
- phase labels would add more complexity than the task
- the underlying source classification is itself unknown

## Inputs / Required State

- source claims
- phase definitions
- allowed transformations
- provenance

## Outputs / Produced State

- phase-tagged reasoning trace
- labeled transitions
- claim-status-safe output

## Mechanism

Assign each working claim to the recovered semantic phase appropriate to its status, keep phase-specific operations and admissible transformations explicit, and require a labeled transition when a claim moves from evidence or fact into interpretation, probability, or heuristic use. The exact scaffold mechanics are derived from recovered semantic phase separation; they are not directly preserved as a historical procedure.

## Procedure

1. Declare the phases needed for the task and what claim types each admits.
2. Tag inputs and intermediate claims with their current phase.
3. Within a phase, perform only operations allowed for that claim type.
4. At a transition, record the source claim, transformation, assumptions, and destination phase.
5. Before output, audit that interpretations, probabilities, and heuristics are not stated as source facts.

## Always-Do Rules

- retain provenance across phase transitions
- label inferential transformations
- audit the final wording against claim status

## Never-Do / Avoid Rules

- allow an interpretation to overwrite its source fact
- treat phase separation as a license to ignore cross-phase consistency
- claim the normalized procedure is verbatim historical recovery

## Interaction Rules

### `domain-mode-isolation`

Domain/Mode Isolation prevents rules from one operational mode from leaking into another; phase locking does the same for semantic claim status.

### `citation-fidelity`

Citation Fidelity anchors factual and evidentiary phases to their sources.

## Compatible Upgradeables

- `domain-mode-isolation` — Domain/Mode Isolation prevents rules from one operational mode from leaking into another; phase locking does the same for semantic claim status.
- `citation-fidelity` — Citation Fidelity anchors factual and evidentiary phases to their sources.

## Counterbalancing Upgradeables

### `multi-layer-consistency`

Consistency checks ensure that separation does not permit mutually contradictory claims to coexist across phases.

## Potential Redundancy

### `domain-mode-isolation`

Both isolate contexts, but phase locking separates semantic status inside a workflow while domain-mode isolation separates broader operating modes.

## Conflict / Precedence Rules

- A transition cannot increase certainty beyond its evidence without an explicit warrant.
- When phase-specific outputs conflict, factual and source-locked constraints take precedence and the conflict remains visible.

## Failure Boundary

- phase leakage
- unlabeled inference
- false precision
- isolated phases that evade global consistency

## Strong-Model Scaling

May skip:

- printing phase labels when the task is one-step and claim status is unambiguous

Keep mandatory:

- internal claim-status separation
- explicit transition warrants for consequential inference
- final status audit

## Recommended Skill Types

- evidence-grounded writing
- multi-source research
- risk analysis
- long workflows with distinct reasoning modes

## Example Composition

**Task context:** Summarize evidence for a policy outcome.

**Why it activates:** The sources report observations, while the requested conclusion requires interpretation and uncertainty.

**Inputs/state:** Quoted findings, study limitations, and stakeholder heuristics are available.

**Action:** Keeps reported findings in the factual/evidentiary phase, labels the synthesis as interpretation, and states probability without converting it into fact.

**Does not:** Attribute the synthesized policy conclusion directly to a source that did not make it.

**Result/state change:** A readable conclusion whose evidence, inference, and uncertainty remain distinguishable.

**Companions:** ['citation-fidelity', 'multi-layer-consistency']

## Tests

See [`tests/cases.json`](tests/cases.json) for six structured behavior cases and [`tests/composition.md`](tests/composition.md) for the human-readable expectations. Behavioral cases are specifications until run through a real model adapter; CI validates their structure, not model quality.

## Provenance / Historical Aliases

Primary source ID: `JAN26-01` in `OS_Upgradeables_Historical_Recovery_Inventory.md`. Registry generation: `training-scaffolding-2026-01-05`. Historical aliases: None.

Source support: `strongly-derivable`. Mechanism basis: `normalized-from-recovered`.

Structured source references:

- OS_Upgradeable_to_Skills_Translation_Catalog_v2_Recovery_Merged.md — C. JANUARY 5, 2026 TRAINING / SCAFFOLDING UPGRADEABLES (current_consolidated_catalog)
- OS_Upgradeables_Historical_Recovery_Inventory.md — 5. January 5, 2026 — training/scaffolding Upgradeables snapshot (historical_recovery_inventory)
- OS_Upgradeables_Deep_Context_Recovery_Addendum_2026-09-03.md — 10.2 Semantic phase separation (historical_assistant_artifact)
