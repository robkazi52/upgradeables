# Explanation Minimality Scaffold

## Summary

Modern operationalization that emits the smallest explanation sufficient for the reader to understand, trust, and act on the answer.

## Purpose

Remove explanatory material that does not change comprehension, verification, decision, or safe execution while retaining required rationale and caveats.

## Problem Solved

Verbose explanations hide the answer and decision-relevant constraints, but blind shortening can remove the causal bridge, evidence, or warning a reader needs.

## Where It Fits in the OS

Roles: output compression scaffold, sufficiency gate. Pipeline stages: response planning, draft compression, final readability check.

This component acts within those stages; it does not take over the complete task or outrank the host Skill.

## Best-Fit Activities / Tasks

- direct answers
- status updates
- executive summaries
- routine technical guidance
- high-volume assistant outputs

## When Not to Use

- the user requests a tutorial or exhaustive rationale
- high-stakes action requires full assumptions and warnings
- a novel argument needs its derivation to be auditable

## Scope

Canonical package: `explanation-minimality-scaffold@1.1.0`. ID: `JAN26-08`. Functional classes: output. Activation: `U1-common-conditional`. Mechanism basis: `modern-interpretation`. Activation cost: `low` (architectural burden, not measured compute).

## Trigger Conditions

- verbosity can obscure the answer

## Non-Triggers

- the user requests a tutorial or exhaustive rationale
- high-stakes action requires full assumptions and warnings
- a novel argument needs its derivation to be auditable

## Inputs / Required State

- answer or artifact
- target reader
- requested depth
- risk tier
- required evidence and caveats

## Outputs / Produced State

- minimal sufficient explanation
- retained rationale and caveats
- deletion-tested final response

## Mechanism

Set an explanation contract consisting of the outcome, the minimum causal or evidentiary bridge, required caveats, and the next action. Draft those blocks first, then test every additional sentence with a deletion probe: if removal does not impair correctness, comprehension, verification, safety, or actionability for the target reader, delete it. This mechanism is modern; only the exact historical scaffold name was recovered.

**Modern operational interpretation:** The procedure below is useful current guidance, not a claim that the full historical mechanism was recovered.

## Procedure

1. Identify the reader, requested depth, decision or action, and risk tier.
2. List mandatory explanation blocks: answer, indispensable why, evidence or method needed for trust, caveats, and next action.
3. Draft one compact block for each mandatory need.
4. Run a deletion probe sentence by sentence against correctness, comprehension, verification, safety, and actionability.
5. Restore any deleted bridge whose absence creates a knowledge jump; stop when remaining content is necessary or explicitly requested.

## Always-Do Rules

- lead with the outcome
- preserve qualifications that change action
- include enough bridge for the target reader to verify or follow the result
- label the mechanism as modern

## Never-Do / Avoid Rules

- equate minimality with unexplained assertion
- remove safety or uncertainty language for brevity
- repeat the same conclusion in several formats without need
- claim this procedure is historically recovered

## Interaction Rules

### `pedagogical-alignment`

Pedagogical Alignment defines what the reader needs before Minimality removes surplus explanation.

### `bounded-exit`

Bounded ExIt supplies the recovered marginal-value stop principle for further polishing.

## Compatible Upgradeables

- `pedagogical-alignment` — Pedagogical Alignment defines what the reader needs before Minimality removes surplus explanation.
- `bounded-exit` — Bounded ExIt supplies the recovered marginal-value stop principle for further polishing.

## Counterbalancing Upgradeables

### `citation-fidelity`

Citation Fidelity prevents compression from detaching claims from required source support.

## Potential Redundancy

### `pedagogical-alignment`

Both shape explanation, but pedagogy adapts conceptual accessibility while minimality controls how much explanatory material survives.

## Conflict / Precedence Rules

- User-requested detail and risk-mandated disclosure override brevity.
- When a deletion creates ambiguity about scope, uncertainty, or authority, restore the qualifying content.
- Citation or evidence requirements are not optional surplus.

## Failure Boundary

- terse but unactionable output
- missing causal bridge
- removed caveat
- repetition disguised as clarity
- invented historical mechanism

## Strong-Model Scaling

May skip:

- an explicit deletion log
- formal block labels in the final response

Keep mandatory:

- reader-and-risk calibration
- mandatory-block check
- deletion probe

## Recommended Skill Types

- direct answers
- status updates
- executive summaries
- routine technical guidance
- high-volume assistant outputs

## Example Composition

**Task context:** Report that a repository build passed and identify what changed.

**Why it activates:** The user needs outcome, material changes, validation, and next step—not a narration of every command.

**Inputs/state:** Nineteen profiles were added, JSON validation passed, and four profiles have explicit source limitations.

**Action:** States the completed artifact, count, validation result, and source-gap caveat in a few sentences.

**Does not:** Paste the full validation log or omit the source-gap caveat to stay short.

**Result/state change:** A compact handoff that remains trustworthy and actionable.

**Companions:** ['pedagogical-alignment', 'bounded-exit']

## Tests

See [`tests/cases.json`](tests/cases.json) for six structured behavior cases and [`tests/composition.md`](tests/composition.md) for the human-readable expectations. Behavioral cases are specifications until run through a real model adapter; CI validates their structure, not model quality.

## Provenance / Historical Aliases

Primary source ID: `JAN26-08` in `OS_Upgradeables_Historical_Recovery_Inventory.md`. Registry generation: `training-scaffolding-2026-01-05`. Historical aliases: None.

Source support: `modern-operationalization`. Mechanism basis: `modern-interpretation`.

Structured source references:

- OS_Upgradeable_to_Skills_Translation_Catalog_v2_Recovery_Merged.md — C. JANUARY 5, 2026 TRAINING / SCAFFOLDING UPGRADEABLES (current_consolidated_catalog)
- OS_Upgradeables_Historical_Recovery_Inventory.md — 5. January 5, 2026 — training/scaffolding Upgradeables snapshot (historical_recovery_inventory)
- OS_Upgradeables_Deep_Context_Recovery_Addendum_2026-09-03.md — 9. BOUNDED EXIT — DEEPER HISTORICAL USE (historical_assistant_artifact)
