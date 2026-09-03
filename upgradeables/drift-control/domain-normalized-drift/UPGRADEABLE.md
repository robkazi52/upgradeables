# Domain-Normalized Drift Field

## Summary

Set the initial drift tolerance from domain consequences and conventions, then refine it for the specific task.

## Purpose

Avoid applying casual creative tolerance to precision domains or unnecessary rigidity to expressive domains.

## Problem Solved

The same semantic change has different acceptability in legal, medical, coding, scientific, and creative work.

## Where It Fits in the OS

Roles: domain risk normalization, default corridor selection, policy baseline. Pipeline stages: domain classification, risk assessment, corridor initialization, validation planning.

This component acts within those stages; it does not take over the complete task or outrank the host Skill.

## Best-Fit Activities / Tasks

- cross-domain skills
- domain-specific rewriting
- regulated advice
- mixed precision/creative systems

## When Not to Use

- domain is ambiguous and stakes are high
- a task-specific explicit policy already controls every region
- domain stereotypes would replace evidence

## Scope

Canonical package: `domain-normalized-drift@1.1.0`. ID: `T4-11`. Functional classes: drift-control. Activation: `U2-specialized`. Mechanism basis: `normalized-from-recovered`. Activation cost: `medium` (architectural burden, not measured compute).

## Trigger Conditions

- domains have materially different fidelity needs

## Non-Triggers

- domain is ambiguous and stakes are high
- a task-specific explicit policy already controls every region
- domain stereotypes would replace evidence

## Inputs / Required State

- domain classification
- consequence assessment
- versioned domain profile
- task constraints
- source conventions

## Outputs / Produced State

- domain-normalized baseline
- override record
- initial validation and corridor policy

## Mechanism

Classify the operative domain and consequence classes, load a versioned domain profile describing default treatment of facts, terminology, citations, uncertainty, formatting, and creative latitude, then override it with explicit task instructions and region-level evidence. The profile supplies defaults only; it never determines truth or authority.

## Procedure

1. Identify the operative domain and mixed-domain boundaries.
2. Assess consequences of factual, terminological, structural, and stylistic drift.
3. Select a versioned domain default profile.
4. Apply higher-authority task constraints and source-specific requirements.
5. Instantiate region-level corridors and validation checks.
6. Record overrides and reassess if the domain changes.

## Always-Do Rules

- treat domain values as defaults
- version the profile
- override with explicit authority and evidence
- separate mixed domains

## Never-Do / Avoid Rules

- assume a domain from keywords alone when stakes matter
- use domain norms to invent facts
- let a broad profile erase task-specific constraints

## Interaction Rules

### `domain-mode-isolation`

Keeps different domain profiles from leaking across boundaries.

### `controlled-drift-corridors`

Turns the domain baseline into task-specific enforceable widths.

### `drift-spectra-scaling`

Refines the baseline across content types inside the domain.

## Compatible Upgradeables

- `domain-mode-isolation` — Keeps different domain profiles from leaking across boundaries.
- `controlled-drift-corridors` — Turns the domain baseline into task-specific enforceable widths.
- `drift-spectra-scaling` — Refines the baseline across content types inside the domain.

## Counterbalancing Upgradeables

### `clarification-gateway`

Resolves ambiguous domain or intended audience before normalization.

### `zero-drift-zones`

Overrides any permissive domain default for immutable items.

## Potential Redundancy

### `compute-adaptive-drift`

Domain normalization sets semantic defaults; compute adaptation changes runtime control overhead.

### `controlled-drift-corridors`

Once explicit corridors exist, do not enforce a second conflicting domain bound.

## Conflict / Precedence Rules

- Explicit task/source authority outranks the domain profile.
- For mixed-domain content, apply the stricter relevant profile at shared boundaries unless an authorized rule says otherwise.

## Failure Boundary

- Do not select a permissive profile when domain classification or consequence is uncertain.
- Escalate profile conflicts in regulated or safety-critical work.

## Strong-Model Scaling

May skip:

- formal profile loading for a simple familiar low-risk task
- domain defaults fully superseded by explicit task corridors

Keep mandatory:

- consequence assessment
- task override precedence
- mixed-domain boundary handling
- zero-drift exceptions

## Recommended Skill Types

- communication and content generation
- document and code transformation
- long-context workflows
- skill and agent workflows

## Example Composition

**Task context:** Rewrite both clinical cautions and patient-facing welcome copy.

**Why it activates:** The artifact crosses a precision domain and a low-stakes expressive region.

**Inputs/state:** Healthcare domain profile, brand style, cited cautions, and explicit audience.

**Action:** Starts with narrow clinical defaults and broader stylistic defaults, then applies section-specific corridors.

**Does not:** It does not let brand tone soften contraindications or force clinical prose rigidity onto the greeting.

**Result/state change:** Domain-appropriate drift limits across one mixed artifact.

**Companions:** ['domain-mode-isolation', 'controlled-drift-corridors', 'zero-drift-zones']

## Tests

See [`tests/cases.json`](tests/cases.json) for six structured behavior cases and [`tests/composition.md`](tests/composition.md) for the human-readable expectations. Behavioral cases are specifications until run through a real model adapter; CI validates their structure, not model quality.

## Provenance / Historical Aliases

Primary source ID: `T4-11` in `OS_Upgradeable_to_Skills_Translation_Catalog_v2_Recovery_Merged.md`. Registry generation: `consolidated-2026-09`. Historical aliases: DNDF.

Source support: `strongly-derivable`. Mechanism basis: `normalized-from-recovered`.

Structured source references:

- OS_Upgradeable_to_Skills_Translation_Catalog_v2_Recovery_Merged.md — OS Philosophy and Upgradeable-to-Skill Translation Catalog (current_consolidated_catalog)
- OS_Upgradeables_Historical_Recovery_Inventory.md — ECL / Drift Sink (historical_recovery_inventory)
- OS_Upgradeables_Deep_Context_Recovery_Addendum_2026-09-03.md — 10.3 Drift widths (historical_assistant_artifact)
