# Zero-Drift Zones

## Summary

Mark specific source units as semantically immutable and verify every derivative against exact or declared equivalence rules.

## Purpose

Protect facts, identifiers, quotations, obligations, safety limits, and other high-consequence content from transformation drift.

## Problem Solved

Even careful paraphrase can alter numbers, negation, qualifiers, identities, or binding language that must remain unchanged.

## Where It Fits in the OS

Roles: immutable semantic region, fidelity boundary, high-consequence validation. Pipeline stages: source annotation, transformation planning, generation guard, final verification.

This component acts within those stages; it does not take over the complete task or outrank the host Skill.

## Best-Fit Activities / Tasks

- legal and policy transformation
- source-grounded summaries
- code/API migration
- safety-critical instructions

## When Not to Use

- the user explicitly authorizes change to the marked content
- immutability scope cannot be identified
- everything is marked zero-drift and no useful transformation remains

## Scope

Canonical package: `zero-drift-zones@1.1.0`. ID: `T3-14`. Functional classes: drift-control, truth-grounding. Activation: `U1-common-conditional`. Mechanism basis: `recovered`. Activation cost: `low` (architectural burden, not measured compute).

## Trigger Conditions

- Activate when the task requires content contains fidelity-locked atoms.

## Non-Triggers

- the user explicitly authorizes change to the marked content
- immutability scope cannot be identified
- everything is marked zero-drift and no useful transformation remains

## Inputs / Required State

- authoritative source spans
- high-consequence atom classification
- preservation rule
- allowed formatting changes
- validation tools

## Outputs / Produced State

- identified zero-drift zones
- stable atom IDs
- equivalence tests
- violation report or validated derivative

## Mechanism

Identify minimal semantic atoms whose alteration would invalidate the task, assign stable IDs and source spans, and specify their preservation rule: exact text, exact value/unit, or meaning-equivalent statement with required qualifiers. Carry the IDs through all transforms and require a deterministic check or source-grounded review before acceptance.

## Procedure

1. Locate high-consequence atoms such as names, numbers, negations, conditions, quotations, obligations, and safety thresholds.
2. Minimize each zone so surrounding exposition can still change.
3. Choose exact-string, structured-value, or semantic-equivalence preservation rules.
4. Attach stable source pointers and propagate the zone contract downstream.
5. Validate every derivative and block or repair failures.
6. Remove or change a zone only through explicit source/task authority.

## Always-Do Rules

- keep zones minimal and explicit
- include units, qualifiers, and negation
- preserve provenance
- validate before acceptance

## Never-Do / Avoid Rules

- declare the whole artifact immutable by convenience
- paraphrase an exact-quote zone
- round or normalize values without authorization
- silently drop a failed zone

## Interaction Rules

### `controlled-drift-corridors`

Zero-drift is the zero-width endpoint embedded among more flexible corridors.

### `drift-immunity-propagation`

Carries zone contracts through downstream derivatives.

### `drift-suppression`

Detects and repairs zone violations.

## Compatible Upgradeables

- `controlled-drift-corridors` — Zero-drift is the zero-width endpoint embedded among more flexible corridors.
- `drift-immunity-propagation` — Carries zone contracts through downstream derivatives.
- `drift-suppression` — Detects and repairs zone violations.

## Counterbalancing Upgradeables

### `drift-spectra-scaling`

Prevents zero-drift from being over-applied by assigning flexible content to other bands.

### `clarification-gateway`

Clarifies whether exact wording or semantic equivalence is required.

## Potential Redundancy

### `working-memory-lock-in`

WM Lock keeps critical items salient; zero-drift zones define their transformation invariance.

### `mode-lock-in`

A mode may mandate fidelity globally, but zones identify and test concrete immutable atoms.

## Conflict / Precedence Rules

- Latest authorized source correction may replace a zone, with version history retained.
- When exact wording and required target format conflict, preserve the semantic atom and surface the formatting exception for authority review.

## Failure Boundary

- Block release when a required zone fails validation.
- Do not claim semantic equivalence where domain expertise or source context is insufficient.

## Strong-Model Scaling

May skip:

- exact-string checks for plainly nonverbatim meaning-equivalence zones
- formal IDs for a single short quoted value

Keep mandatory:

- minimal immutable atoms
- qualifier/unit preservation
- source pointers
- blocking validation

## Recommended Skill Types

- document and code transformation
- high-stakes evidence work
- long-context workflows
- source-grounded research

## Example Composition

**Task context:** Summarize a clinical protocol for a quick-reference card.

**Why it activates:** Dose, units, contraindication, and exception clause cannot drift while explanation can compress.

**Inputs/state:** Cited protocol spans, structured dose values, required exact warning, and equivalence rules.

**Action:** Marks those atoms as zero-drift, propagates their IDs, and checks the card before release.

**Does not:** It does not freeze all explanatory prose or simplify away the exception.

**Result/state change:** A shorter card with verified critical content.

**Companions:** ['controlled-drift-corridors', 'drift-immunity-propagation', 'drift-suppression']

## Tests

See [`tests/cases.json`](tests/cases.json) for six structured behavior cases and [`tests/composition.md`](tests/composition.md) for the human-readable expectations. Behavioral cases are specifications until run through a real model adapter; CI validates their structure, not model quality.

## Provenance / Historical Aliases

Primary source ID: `T3-14` in `OS_Upgradeable_to_Skills_Translation_Catalog_v2_Recovery_Merged.md`. Registry generation: `consolidated-2026-09`. Historical aliases: Zero-Drift Citation / Quote / Definition Zones.

Source support: `sufficiently-recovered`. Mechanism basis: `recovered`.

Structured source references:

- OS_Upgradeable_to_Skills_Translation_Catalog_v2_Recovery_Merged.md — OS Philosophy and Upgradeable-to-Skill Translation Catalog (current_consolidated_catalog)
- OS_Upgradeables_Historical_Recovery_Inventory.md — ECL / Drift Sink (historical_recovery_inventory)
- OS_Upgradeables_Deep_Context_Recovery_Addendum_2026-09-03.md — Zero-drift (historical_assistant_artifact)
