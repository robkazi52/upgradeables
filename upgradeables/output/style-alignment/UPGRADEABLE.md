# Style-Alignment Module

## Summary

Conforms output to an authorized voice and presentation contract without changing facts, reasoning, evidence status, or task compliance.

## Purpose

Make artifacts consistent with audience, publication, or organizational style while keeping truth and requirements dominant.

## Problem Solved

Style can be inconsistent or inappropriate, but style imitation and polishing can also distort claims, citations, uncertainty, or required structure.

## Where It Fits in the OS

Roles: output style constraint, surface-form adapter. Pipeline stages: style contract extraction, surface transformation, semantic and style validation.

This component acts within those stages; it does not take over the complete task or outrank the host Skill.

## Best-Fit Activities / Tasks

- house-style editing
- voice matching
- channel adaptation
- consistent multi-author documents
- format and tone normalization

## When Not to Use

- the requested style impersonates a living person or conflicts with policy
- exact quoted language must remain untouched
- facts or reasoning are not yet stable

## Scope

Canonical package: `style-alignment@1.1.0`. ID: `T3-15`. Functional classes: output. Activation: `U1-common-conditional`. Mechanism basis: `recovered`. Activation cost: `low` (architectural burden, not measured compute).

## Trigger Conditions

- a style or voice is specified

## Non-Triggers

- the requested style impersonates a living person or conflicts with policy
- exact quoted language must remain untouched
- facts or reasoning are not yet stable

## Inputs / Required State

- artifact
- authorized style guide or exemplar
- semantic invariant ledger
- exact-text zones
- task and channel constraints

## Outputs / Produced State

- style-aligned artifact
- style conformance assessment
- semantic and citation preservation check

## Mechanism

Translate the authorized style request into an observable style vector—tone, formality, sentence rhythm, vocabulary level, structure, formatting, and disallowed tendencies—while extracting a separate semantic invariant ledger. Transform surface choices toward the style vector, protect quoted and zero-drift zones, then score both conformance and semantic preservation; truth, task, and citation constraints veto any stylistic gain.

## Procedure

1. Extract the authorized style source and convert it into observable positive and negative constraints.
2. Lock facts, reasoning relations, requirements, citations, uncertainty, and exact-text zones.
3. Revise diction, rhythm, organization, and formatting only where the style contract permits.
4. Compare the result against the style vector using representative passages rather than vague resemblance.
5. Run a semantic and citation diff; revert any stylistic change that alters truth, logic, or attribution.

## Always-Do Rules

- use explicit style dimensions
- keep style subordinate to truth and task
- protect quotes and zero-drift zones
- validate semantic preservation after styling

## Never-Do / Avoid Rules

- invent facts or confidence to sound more authoritative
- mimic unauthorized personal quirks
- let brand voice erase required warnings
- treat subjective vibe as the only acceptance test

## Interaction Rules

### `safe-rewrite`

Safe Rewrite provides the semantic invariant checks during style transformation.

### `pedagogical-alignment`

Pedagogical Alignment adjusts conceptual accessibility independently of voice.

### `citation-fidelity`

Citation Fidelity ensures moved or rewritten claims remain correctly supported.

## Compatible Upgradeables

- `safe-rewrite` — Safe Rewrite provides the semantic invariant checks during style transformation.
- `pedagogical-alignment` — Pedagogical Alignment adjusts conceptual accessibility independently of voice.
- `citation-fidelity` — Citation Fidelity ensures moved or rewritten claims remain correctly supported.

## Counterbalancing Upgradeables

### `grounding-no-invention`

Grounding vetoes stylish additions that lack source support.

### `explanation-minimality-scaffold`

Minimality prevents style requirements from producing ornamental excess.

## Potential Redundancy

### `safe-rewrite`

Safe Rewrite governs preservation across any rewrite; Style Alignment supplies the specific target dimensions and conformance check.

### `pedagogical-alignment`

Both adapt to users, but style changes voice and form while pedagogy changes conceptual scaffolding.

## Conflict / Precedence Rules

- Truth, safety, citation fidelity, and explicit task constraints outrank the style guide.
- Exact quotations and legally controlled text are excluded from stylistic transformation.
- When two style authorities conflict, use the source explicitly designated for this artifact or ask rather than blend them silently.

## Failure Boundary

- fact drift for tone
- vague imitation
- citation detachment
- over-stylization
- conflicting style authorities
- modification of exact-text zones

## Strong-Model Scaling

May skip:

- publishing the full style vector for a short answer
- scoring every sentence independently

Keep mandatory:

- explicit target dimensions
- truth and task veto
- semantic and citation back-check

## Recommended Skill Types

- communication and content generation
- document and code transformation

## Example Composition

**Task context:** Convert contributions from several authors into one neutral technical guide.

**Why it activates:** Voice and formatting vary while facts and citations are already approved.

**Inputs/state:** A house guide specifies concise neutral prose, heading conventions, and prohibited marketing language.

**Action:** Builds a style vector, normalizes voice and headings, removes promotional phrasing, and confirms claims, uncertainty, and citations remain unchanged.

**Does not:** Add confident benefit claims to make the guide sound polished.

**Result/state change:** A consistent guide that retains the approved semantic record.

**Companions:** ['safe-rewrite', 'citation-fidelity', 'pedagogical-alignment']

## Tests

See [`tests/cases.json`](tests/cases.json) for six structured behavior cases and [`tests/composition.md`](tests/composition.md) for the human-readable expectations. Behavioral cases are specifications until run through a real model adapter; CI validates their structure, not model quality.

## Provenance / Historical Aliases

Primary source ID: `T3-15` in `OS_Upgradeable_to_Skills_Translation_Catalog_v2_Recovery_Merged.md`. Registry generation: `consolidated-2026-09`. Historical aliases: None.

Source support: `sufficiently-recovered`. Mechanism basis: `recovered`.

Structured source references:

- OS_Upgradeable_to_Skills_Translation_Catalog_v2_Recovery_Merged.md — OS Philosophy and Upgradeable-to-Skill Translation Catalog (current_consolidated_catalog)
- OS_Upgradeables_Historical_Recovery_Inventory.md — 8. Tier-3 / Paper-Author alignment family recovered from late-November work (historical_recovery_inventory)
- OS_Upgradeables_Deep_Context_Recovery_Addendum_2026-09-03.md — 19.1 Evidence-grounded authoring (historical_assistant_artifact)
