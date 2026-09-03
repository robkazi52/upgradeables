# Domain / Mode Isolation

## Summary

Partition active instructions, vocabulary, state, and tools by domain so material from one operating context cannot silently govern another.

## Purpose

Prevent cross-domain contamination while permitting explicit, reviewed transfers of shared facts.

## Problem Solved

A model working across legal, medical, technical, or creative contexts may leak assumptions, authority rules, or terminology between them.

## Where It Fits in the OS

Roles: state partitioning, authority containment, context hygiene. Pipeline stages: domain classification, context loading, mode transition, output validation.

This component acts within those stages; it does not take over the complete task or outrank the host Skill.

## Best-Fit Activities / Tasks

- mixed-domain workspaces
- multi-tenant assistants
- regulated workflows
- parallel specialist agents

## When Not to Use

- the task is genuinely single-domain
- the supposed domains share identical authority and semantics
- partitioning would hide a required cross-domain dependency

## Scope

Canonical package: `domain-mode-isolation@1.1.0`. ID: `T3-10`. Functional classes: state, drift-control, orchestration. Activation: `U0-foundational`. Mechanism basis: `recovered`. Activation cost: `low` (architectural burden, not measured compute).

## Trigger Conditions

- multiple domains or semantic modes coexist

## Non-Triggers

- the task is genuinely single-domain
- the supposed domains share identical authority and semantics
- partitioning would hide a required cross-domain dependency

## Inputs / Required State

- domain classification
- domain-specific instructions
- source permissions
- shared facts
- transition event

## Outputs / Produced State

- isolated domain contexts
- approved cross-domain projections
- leakage check
- active-domain marker

## Mechanism

Create a named compartment for each active domain with its own instructions, terms, sources, permissions, and state. Route new material into the matching compartment; make cross-domain transfer an explicit projection with provenance, and validate the final output against the selected domain rather than the union of all modes.

## Procedure

1. Classify the task and enumerate domains that are actually needed.
2. Create separate domain scopes for instructions, sources, vocabulary, and mutable state.
3. Load only the selected scope into each domain operation.
4. Transfer shared facts through an explicit provenance-bearing bridge.
5. On transition, unload or deactivate the old domain scope and validate for leakage.

## Always-Do Rules

- name the active domain
- keep domain-specific authority local
- audit cross-domain transfers

## Never-Do / Avoid Rules

- blend incompatible domain rules silently
- copy an entire domain context to enable one shared fact
- let a lower-authority domain override the active domain

## Interaction Rules

### `mode-lock-in`

Mode Lock keeps the selected operating regime stable inside a domain.

### `structured-state-projection`

Carries only approved fields across domain boundaries.

### `scoped-loader`

Loads the correct domain resources after classification.

## Compatible Upgradeables

- `mode-lock-in` — Mode Lock keeps the selected operating regime stable inside a domain.
- `structured-state-projection` — Carries only approved fields across domain boundaries.
- `scoped-loader` — Loads the correct domain resources after classification.

## Counterbalancing Upgradeables

### `clarification-gateway`

Resolves ambiguous domain classification before isolation hardens it.

### `state-routing-bus`

Allows explicit movement where strict compartments must still cooperate.

## Potential Redundancy

### `mode-lock-in`

Isolation separates domains; lock-in stabilizes one mode, so do not create duplicate partitions for each label.

### `stateblock`

Keep domain partitions within or referenced by one canonical state owner.

## Conflict / Precedence Rules

- System and task authority outrank domain-local preferences.
- When a fact must cross domains, transfer the fact and provenance, not the source domain's behavioral rules.

## Failure Boundary

- Pause when the domain is ambiguous and different classifications change safety or authority.
- Do not claim isolation if the host cannot control context or tool exposure; emulate with explicit labels and validation.

## Strong-Model Scaling

May skip:

- physical context separation for a trivial benign two-topic answer
- verbose transition manifests

Keep mandatory:

- active-domain marker
- authority separation
- explicit transfer boundary
- leakage validation

## Recommended Skill Types

- document and code transformation
- long-context workflows
- multi-step task execution
- skill and agent workflows

## Example Composition

**Task context:** A workspace contains employment-law advice and creative recruiting copy.

**Why it activates:** Legal constraints must inform but not be rewritten by the creative mode.

**Inputs/state:** Separate legal sources and brand guidelines plus an approved fact bridge.

**Action:** Keeps legal authority in the legal compartment and projects only approved constraints to the writing compartment.

**Does not:** It does not treat brand tone as legal authority or expose the full legal workspace to the copywriter.

**Result/state change:** Creative copy respects cited constraints without domain-rule leakage.

**Companions:** ['mode-lock-in', 'structured-state-projection', 'scoped-loader']

## Tests

See [`tests/cases.json`](tests/cases.json) for six structured behavior cases and [`tests/composition.md`](tests/composition.md) for the human-readable expectations. Behavioral cases are specifications until run through a real model adapter; CI validates their structure, not model quality.

## Provenance / Historical Aliases

Primary source ID: `T3-10` in `OS_Upgradeable_to_Skills_Translation_Catalog_v2_Recovery_Merged.md`. Registry generation: `consolidated-2026-09`. Historical aliases: None.

Source support: `sufficiently-recovered`. Mechanism basis: `recovered`.

Structured source references:

- OS_Upgradeable_to_Skills_Translation_Catalog_v2_Recovery_Merged.md — OS Philosophy and Upgradeable-to-Skill Translation Catalog (current_consolidated_catalog)
- OS_Upgradeables_Historical_Recovery_Inventory.md — 14. Domain OS / bundle instances (historical_recovery_inventory)
- OS_Upgradeables_Deep_Context_Recovery_Addendum_2026-09-03.md — 6.2 T3 structured reasoning-state representation (historical_assistant_artifact)
