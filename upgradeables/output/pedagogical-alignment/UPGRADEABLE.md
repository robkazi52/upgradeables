# Pedagogical Alignment Constraint

## Summary

Matches conceptual granularity, terminology, sequencing, and examples to the reader while preserving full technical accuracy.

## Purpose

Make correct content learnable and usable for a specified audience without diluting claims or inventing simplifications.

## Problem Solved

An explanation can be accurate but inaccessible because it assumes missing prerequisites, uses undefined jargon, or presents abstractions before concrete anchors.

## Where It Fits in the OS

Roles: audience adaptation constraint, instructional output shaper. Pipeline stages: audience modeling, explanation design, comprehension validation.

This component acts within those stages; it does not take over the complete task or outrank the host Skill.

## Best-Fit Activities / Tasks

- tutorials
- documentation
- stakeholder briefings
- technical-to-nontechnical translation
- onboarding

## When Not to Use

- the audience and purpose cannot be inferred and the choice materially changes content
- exact legal or technical wording must remain verbatim
- simplification would conceal decision-relevant uncertainty

## Scope

Canonical package: `pedagogical-alignment@1.1.0`. ID: `T3-16`. Functional classes: output, framing-intake. Activation: `U1-common-conditional`. Mechanism basis: `recovered`. Activation cost: `low` (architectural burden, not measured compute).

## Trigger Conditions

- an audience or teaching level is known

## Non-Triggers

- the audience and purpose cannot be inferred and the choice materially changes content
- exact legal or technical wording must remain verbatim
- simplification would conceal decision-relevant uncertainty

## Inputs / Required State

- technical content
- target audience
- learning or action goal
- prerequisite assumptions
- terminology constraints

## Outputs / Produced State

- audience-aligned explanation
- defined terminology
- validated examples or analogies
- preserved limitations

## Mechanism

Build a compact audience model—known prerequisites, target capability, jargon tolerance, and action context—then choose the smallest conceptual steps that bridge from that model to the target. Define or replace jargon at first use, order prerequisite before dependent ideas, add an example only where it resolves a likely misconception, and run an accuracy-backcheck against the unsimplified claim.

## Procedure

1. Identify the reader's likely starting knowledge and the capability they need after reading.
2. List prerequisites and terms that the explanation currently assumes.
3. Sequence content from familiar anchor through the minimum conceptual bridge to the target.
4. Define necessary jargon or replace it with accurate plain language; add a representative example where abstraction alone is likely to fail.
5. Back-check every simplification, analogy, and example against the original technical claim and retain important limitations.

## Always-Do Rules

- preserve accuracy before accessibility
- make prerequisite order explicit
- define unavoidable jargon
- check analogies for where they break

## Never-Do / Avoid Rules

- talk down to the reader
- remove uncertainty or boundary conditions to sound simple
- use an analogy that changes the mechanism
- assume more domain knowledge than the audience model supports

## Interaction Rules

### `explanation-minimality-scaffold`

Minimality removes surplus after Pedagogical Alignment determines which conceptual bridges the reader actually needs.

### `style-alignment`

Style Alignment matches authorized voice while pedagogy matches comprehension needs.

## Compatible Upgradeables

- `explanation-minimality-scaffold` — Minimality removes surplus after Pedagogical Alignment determines which conceptual bridges the reader actually needs.
- `style-alignment` — Style Alignment matches authorized voice while pedagogy matches comprehension needs.

## Counterbalancing Upgradeables

### `citation-fidelity`

Citation Fidelity keeps adapted explanations tied to evidence when wording and examples change.

## Potential Redundancy

### `style-alignment`

Both adapt output, but style concerns voice and conventions while pedagogy concerns prerequisite knowledge and learning sequence.

## Conflict / Precedence Rules

- Accuracy, scope, and uncertainty outrank ease of explanation.
- Exact source language is preserved in quoted or zero-drift zones and explained around rather than rewritten.
- If audience level is materially ambiguous, provide a concise default plus an offer or branch for deeper detail.

## Failure Boundary

- oversimplification
- undefined jargon
- misleading analogy
- missing prerequisite
- correct but unusable abstraction

## Strong-Model Scaling

May skip:

- printing an explicit audience profile for a familiar user
- examples when the concept is already concrete

Keep mandatory:

- internal prerequisite model
- accuracy back-check
- boundary-preserving simplification

## Recommended Skill Types

- communication and content generation
- document and code transformation
- multi-step task execution
- skill and agent workflows

## Example Composition

**Task context:** Explain an API breaking change to product managers.

**Why it activates:** They need impact and rollout logic, not implementation-level type-system detail.

**Inputs/state:** The technical migration guide, compatibility window, affected workflows, and rollback limitations are known.

**Action:** Starts with user-visible impact, defines compatibility window in plain language, sequences rollout dependencies, and includes one workflow example while preserving rollback limits.

**Does not:** Replace the mechanism with a false everyday analogy or omit the irreversible deadline.

**Result/state change:** A technically faithful explanation that supports planning decisions.

**Companions:** ['style-alignment', 'explanation-minimality-scaffold']

## Tests

See [`tests/cases.json`](tests/cases.json) for six structured behavior cases and [`tests/composition.md`](tests/composition.md) for the human-readable expectations. Behavioral cases are specifications until run through a real model adapter; CI validates their structure, not model quality.

## Provenance / Historical Aliases

Primary source ID: `T3-16` in `OS_Upgradeable_to_Skills_Translation_Catalog_v2_Recovery_Merged.md`. Registry generation: `consolidated-2026-09`. Historical aliases: None.

Source support: `sufficiently-recovered`. Mechanism basis: `recovered`.

Structured source references:

- OS_Upgradeable_to_Skills_Translation_Catalog_v2_Recovery_Merged.md — OS Philosophy and Upgradeable-to-Skill Translation Catalog (current_consolidated_catalog)
- OS_Upgradeables_Historical_Recovery_Inventory.md — 8. Tier-3 / Paper-Author alignment family recovered from late-November work (historical_recovery_inventory)
- OS_Upgradeables_Deep_Context_Recovery_Addendum_2026-09-03.md — 19.1 Evidence-grounded authoring (historical_assistant_artifact)
