# Resonance

## Summary

Coordinate active modules that should reinforce one another while suppressing irrelevant effects and preserving authority boundaries.

## Purpose

Coordinate active modules that should reinforce one another while suppressing irrelevant effects and preserving authority boundaries.

## Problem Solved

Useful modules can produce noisy, duplicated, or conflicting effects when their interactions are left implicit.

## Where It Fits in the OS

Roles: cross-module alignment, interaction control. Pipeline stages: post-selection coordination, mid-process coupling, pre-synthesis alignment.

This component acts within those stages; it does not take over the complete task or outrank the host Skill.

## Best-Fit Activities / Tasks

- multi-module Skills
- evidence-to-state coordination
- composed agent workflows

## When Not to Use

- only one module is active
- the proposed reinforcement would amplify repetition, exaggeration, or an authority conflict

## Scope

Canonical package: `resonance@1.1.0`. ID: `A-05`. Functional classes: orchestration, drift-control. Activation: `U2-specialized`. Mechanism basis: `recovered`. Activation cost: `medium` (architectural burden, not measured compute).

## Trigger Conditions

- several active modules must align

## Non-Triggers

- only one module is active
- the proposed reinforcement would amplify repetition, exaggeration, or an authority conflict

## Inputs / Required State

- active module contracts and outputs
- declared coupling relationship
- authority and boundary rules

## Outputs / Produced State

- coordinated module handoff
- suppressed noise and explicit unresolved conflicts

## Mechanism

Identify the specific outputs or constraints through which selected modules should reinforce one another, declare the direction and limit of that coupling, and suppress unrelated effects. Check hierarchy before amplification so a lower-authority module cannot become stronger through repetition. Amplification means clearer coordination and usable handoff, not duplicated content.

## Procedure

1. List active modules and the exact relationship that should be reinforced.
2. Verify their authority, source, and state boundaries are compatible.
3. Define the bounded handoff or mutual constraint that creates the useful coupling.
4. Suppress duplicate, irrelevant, or conflicting module effects.
5. Check the coordinated result and dissolve the coupling when its trigger ends.

## Always-Do Rules

- Preserve the defining invariant: explicit relationship, bounded effect, noise suppression, and authority preservation.
- Record material routing, transition, and failure decisions in explicit task state.

## Never-Do / Avoid Rules

- amplifying content through repetition or fusing modules into one authority
- Never claim hidden state, unavailable host capability, or authority beyond the active Skill.

## Interaction Rules

### `state-routing-bus`

Carries the explicit state fields used in the coupling.

### `domain-mode-isolation`

Keeps reinforcement from crossing incompatible domain boundaries.

## Compatible Upgradeables

- `state-routing-bus` — Carries the explicit state fields used in the coupling.
- `domain-mode-isolation` — Keeps reinforcement from crossing incompatible domain boundaries.

## Counterbalancing Upgradeables

### `domain-mode-isolation`

Stops a useful coupling from becoming uncontrolled context blending.

## Potential Redundancy

### `cross-context-resonance-lock`

The lock preserves one cross-context relationship; Resonance coordinates reinforcing effects among active modules more broadly.

## Conflict / Precedence Rules

- Host, system, domain, and explicit user authority take precedence over this component.
- If the modules have incompatible authority or source boundaries, stop or escalate rather than forcing a nominal success.

## Failure Boundary

- the modules have incompatible authority or source boundaries
- the coupling produces repetition or exaggeration instead of clearer coordination

## Strong-Model Scaling

May skip:

- formal coupling state when one obvious handoff is sufficient

Keep mandatory:

- explicit relationship, bounded effect, noise suppression, and authority preservation

## Recommended Skill Types

- multi-module Skills
- evidence-to-state coordination
- composed agent workflows

## Example Composition

**Task context:** An evidence extractor and StateBlock updater must work together before synthesis.

**Why it activates:** Their outputs should reinforce source fidelity without duplicating the source corpus.

**Inputs/state:** Module contracts, extracted evidence pointers, state schema, and authority rules.

**Action:** Routes verified evidence pointers into state and suppresses duplicate narrative output.

**Does not:** Does not merge module identities, repeat evidence for emphasis, or elevate a lower-authority signal.

**Result/state change:** Synthesis receives compact grounded state and no duplicate noise.

**Companions:** State Routing Bus transports fields; Domain Isolation enforces boundaries.

## Tests

See [`tests/cases.json`](tests/cases.json) for six structured behavior cases and [`tests/composition.md`](tests/composition.md) for the human-readable expectations. Behavioral cases are specifications until run through a real model adapter; CI validates their structure, not model quality.

## Provenance / Historical Aliases

Primary source ID: `A-05` in `OS_Upgradeable_to_Skills_Translation_Catalog_v2_Recovery_Merged.md`. Registry generation: `consolidated-2026-09`. Historical aliases: Resonance Locks.

Source support: `sufficiently-recovered`. Mechanism basis: `recovered`.

Structured source references:

- OS_Upgradeable_to_Skills_Translation_Catalog_v2_Recovery_Merged.md — A-05. Resonance (current_consolidated_catalog)
