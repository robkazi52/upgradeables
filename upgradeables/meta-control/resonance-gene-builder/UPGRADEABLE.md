# Resonance Gene Builder

## Summary

Builds a compact Behavior Gene that coordinates a recurring relationship among already-defined modules while preserving authority and suppressing irrelevant effects.

## Purpose

Make useful cross-module reinforcement explicit and reusable without merging modules, duplicating content, or granting hidden communication.

## Problem Solved

The same module combinations repeatedly need ordering, data handoff, reinforcement, or conflict suppression, but ad hoc coupling becomes implicit and inconsistent.

## Where It Fits in the OS

Roles: cross-module coupling-rule builder, specialized Behavior Gene factory. Pipeline stages: relationship observation, coupling specification, composition testing, versioned publication.

This component acts within those stages; it does not take over the complete task or outrank the host Skill.

## Best-Fit Activities / Tasks

- recurring validator-generator pairings
- stable Core-Gene couplings
- multi-module evidence workflows
- repeated authority-sensitive compositions

## When Not to Use

- the need is a general task behavior unrelated to module coupling
- the modules interact only once
- the host lacks an explicit state or data-transfer path

## Scope

Canonical package: `resonance-gene-builder@1.1.0`. ID: `A-06`. Functional classes: meta-control, orchestration. Activation: `U4-meta-architecture`. Mechanism basis: `normalized-from-recovered`. Activation cost: `high` (architectural burden, not measured compute).

## Trigger Conditions

- the same module relationship recurs

## Non-Triggers

- the need is a general task behavior unrelated to module coupling
- the modules interact only once
- the host lacks an explicit state or data-transfer path

## Inputs / Required State

- recurring module relationship
- participant interfaces
- authority order
- state or evidence flow
- success and failure examples

## Outputs / Produced State

- versioned Resonance Gene
- coupling and suppression rules
- compatibility matrix
- composition tests

## Mechanism

Identify a repeated module relationship and encode a narrow coupling Gene containing activation pattern, participants, directional inputs and outputs, ordering, reinforcement rule, suppression rule, authority precedence, termination, and failure behavior. Test the coupling with one participant absent, with conflicting instructions, and with irrelevant output. Reinforcement means clearer coordination through real state or context, never repeated claims or imagined latent links.

## Procedure

1. Collect repeated cases where the same modules should coordinate and isolate the stable relationship.
2. Name participants, trigger, direction of state or evidence flow, and completion condition.
3. Specify which outputs reinforce the next module and which irrelevant or conflicting effects are suppressed.
4. Declare authority ordering, unavailable-module behavior, and conflict escalation.
5. Test normal coupling, missing participant, conflict, repetition, and termination cases.
6. Package the coupling as a versioned Behavior Gene with provenance and compatibility notes.

## Always-Do Rules

- use explicit host-supported interfaces
- preserve module identities and authority
- define both reinforcement and suppression
- test termination and missing-module behavior

## Never-Do / Avoid Rules

- claim hidden inter-module communication
- use repetition as amplification
- merge the coupled modules into one opaque component
- use this builder for ordinary standalone behavior

## Interaction Rules

### `behavior-gene-builder`

The general builder supplies the Gene schema; Resonance Gene Builder specializes it for module coupling.

### `resonance`

Resonance identifies and coordinates reinforcing module effects that the Gene makes reusable.

### `architect-orchestrator`

The architect loads the coupling only when its participant pattern is active.

## Compatible Upgradeables

- `behavior-gene-builder` — The general builder supplies the Gene schema; Resonance Gene Builder specializes it for module coupling.
- `resonance` — Resonance identifies and coordinates reinforcing module effects that the Gene makes reusable.
- `architect-orchestrator` — The architect loads the coupling only when its participant pattern is active.

## Counterbalancing Upgradeables

### `domain-mode-isolation`

Isolation prevents the coupling from leaking across unrelated domains or modes.

## Potential Redundancy

### `behavior-gene-builder`

General versus specialized: Behavior Gene Builder creates any recurring behavior; Resonance Gene Builder creates only cross-module relationship rules.

### `resonance`

Resonance executes coordination; the builder authors and validates reusable coupling genes.

## Conflict / Precedence Rules

- Global authority ordering outranks a coupling's preferred flow.
- Missing participants disable or degrade the coupling explicitly rather than being hallucinated.
- Conflicting participant outputs are surfaced to the declared resolver, not amplified.

## Failure Boundary

- implicit coupling
- repetition amplification
- hidden-channel claims
- authority inversion
- nonterminating module feedback

## Strong-Model Scaling

May skip:

- verbose prose around a compact coupling manifest

Keep mandatory:

- explicit interfaces
- authority rule
- suppression behavior
- termination test

## Recommended Skill Types

- high-stakes evidence work
- multi-step task execution
- skill and agent workflows

## Example Composition

**Task context:** Citation Fidelity should validate claims immediately after Safe Rewrite in every evidence-grounded authoring flow.

**Why it activates:** The same directional module relationship recurs across several authoring Genes.

**Inputs/state:** Both module contracts, claim-citation state, failure statuses, and authority rules are defined.

**Action:** Builds a coupling Gene that passes changed claims to the validator, blocks finalization on mismatch, suppresses duplicate style output, and terminates after pass or explicit repair route.

**Does not:** Merge rewriting and citation logic or claim they communicate outside explicit state.

**Result/state change:** One reusable, testable module relationship.

**Companions:** ['behavior-gene-builder', 'resonance', 'architect-orchestrator']

## Tests

See [`tests/cases.json`](tests/cases.json) for six structured behavior cases and [`tests/composition.md`](tests/composition.md) for the human-readable expectations. Behavioral cases are specifications until run through a real model adapter; CI validates their structure, not model quality.

## Provenance / Historical Aliases

Primary source ID: `A-06` in `OS_Upgradeable_to_Skills_Translation_Catalog_v2_Recovery_Merged.md`. Registry generation: `consolidated-2026-09`. Historical aliases: Resonance Genes.

Source support: `strongly-derivable`. Mechanism basis: `normalized-from-recovered`.

Structured source references:

- OS_Upgradeable_to_Skills_Translation_Catalog_v2_Recovery_Merged.md — OS Philosophy and Upgradeable-to-Skill Translation Catalog (current_consolidated_catalog)
- OS_Upgradeables_Historical_Recovery_Inventory.md — 11. Advanced architecture Upgradeables retained (historical_recovery_inventory)
- OS_Upgradeables_Deep_Context_Recovery_Addendum_2026-09-03.md — 14. BEHAVIOR GENE + CORE SEPARATION — HISTORICAL GENESIS (historical_assistant_artifact)
