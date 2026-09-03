# Structured Refinement Cycles

## Summary

Revises an artifact in ordered, non-mixing passes: factual correction, structural repair, style repair, then final validation.

## Purpose

Prevent one revision pass from trading away correctness while improving structure or style.

## Problem Solved

Mixed editing objectives make it hard to know whether factual, structural, and stylistic defects were fixed or newly introduced.

## Where It Fits in the OS

Roles: multi-pass revision scaffold, defect-class separator. Pipeline stages: factual pass, structural pass, style pass, release validation.

This component acts within those stages; it does not take over the complete task or outrank the host Skill.

## Best-Fit Activities / Tasks

- drafts with several defect classes
- reports requiring source and style review
- prompt or specification cleanup
- publication preparation

## When Not to Use

- only one bounded defect exists
- the artifact requires complete regeneration
- the source truth is not yet established

## Scope

Canonical package: `structured-refinement@1.1.0`. ID: `T2-02`. Functional classes: editing-repair, validation. Activation: `U1-common-conditional`. Mechanism basis: `recovered`. Activation cost: `low` (architectural burden, not measured compute).

## Trigger Conditions

- revision has multiple defect classes

## Non-Triggers

- only one bounded defect exists
- the artifact requires complete regeneration
- the source truth is not yet established

## Inputs / Required State

- artifact
- defect inventory
- locked facts and decisions
- style target
- acceptance criteria

## Outputs / Produced State

- pass-separated revisions
- frozen semantic ledger
- final cross-class validation

## Mechanism

Classify defects before editing and run passes in dependency order: facts and source mapping first, structure and requirement coverage second, style and pedagogy third, final validation last. Accepted decisions are locked between passes, and a later pass may not silently reopen an earlier one.

## Procedure

1. Inventory defects and assign each to factual, structural, stylistic, or validation class.
2. Correct facts, citations, and locked constraints; freeze the accepted semantic ledger.
3. Repair ordering, dependencies, section roles, and requirement coverage without changing the frozen facts.
4. Adjust voice, clarity, and pedagogy without changing facts or structure except where explicitly authorized.
5. Run an independent final check across all classes and use Bounded ExIt to decide whether another pass is justified.

## Always-Do Rules

- separate defect classes
- fix upstream factual issues before downstream polish
- lock accepted decisions between passes
- perform a cross-class final validation

## Never-Do / Avoid Rules

- combine fact correction and free stylistic invention
- let a later pass silently undo an earlier one
- polish a structure already known to be globally invalid

## Interaction Rules

### `safe-rewrite`

Safe Rewrite protects frozen semantics during style and format passes.

### `bounded-exit`

Bounded ExIt decides whether another class-specific pass has sufficient value.

### `micro-repair`

Micro-Repair implements each localized correction selected within a pass.

## Compatible Upgradeables

- `safe-rewrite` — Safe Rewrite protects frozen semantics during style and format passes.
- `bounded-exit` — Bounded ExIt decides whether another class-specific pass has sufficient value.
- `micro-repair` — Micro-Repair implements each localized correction selected within a pass.

## Counterbalancing Upgradeables

### `regenerative-rewrite`

Regeneration replaces the entire cycle when architecture or source mapping is systemically unrecoverable.

## Potential Redundancy

### `bounded-exit`

Both govern iteration, but Structured Refinement defines pass content and order while Bounded ExIt controls continuation.

### `safe-rewrite`

Safe Rewrite is one preservation rule used inside multiple refinement passes.

## Conflict / Precedence Rules

- Factual correctness outranks structural elegance and style.
- A later pass that discovers an upstream defect returns explicitly to the relevant pass and revalidates downstream results.
- If the defect inventory shows architecture failure, stop the cycle and escalate.

## Failure Boundary

- mixed-objective drift
- later-pass regression
- style masking factual defects
- cycling on globally broken structure

## Strong-Model Scaling

May skip:

- physically separate drafts for each pass when an auditable diff is available

Keep mandatory:

- dependency order
- between-pass locks
- final cross-class review

## Recommended Skill Types

- drafts with several defect classes
- reports requiring source and style review
- prompt or specification cleanup
- publication preparation

## Example Composition

**Task context:** Prepare a sourced public guide for release.

**Why it activates:** The draft has two incorrect dates, a duplicated section, and inconsistent voice.

**Inputs/state:** Authoritative dates, required section list, and style guide are available.

**Action:** Fixes dates and citations, then removes structural duplication, then aligns voice, and finally checks all three classes.

**Does not:** Rewrite the dated sentences for tone before establishing correct dates.

**Result/state change:** A release-ready guide with traceable pass boundaries and no semantic regression.

**Companions:** ['safe-rewrite', 'bounded-exit', 'micro-repair']

## Tests

See [`tests/cases.json`](tests/cases.json) for six structured behavior cases and [`tests/composition.md`](tests/composition.md) for the human-readable expectations. Behavioral cases are specifications until run through a real model adapter; CI validates their structure, not model quality.

## Provenance / Historical Aliases

Primary source ID: `T2-02` in `OS_Upgradeable_to_Skills_Translation_Catalog_v2_Recovery_Merged.md`. Registry generation: `consolidated-2026-09`. Historical aliases: None.

Source support: `sufficiently-recovered`. Mechanism basis: `recovered`.

Structured source references:

- OS_Upgradeable_to_Skills_Translation_Catalog_v2_Recovery_Merged.md — T2-02. Structured Refinement Cycles (current_consolidated_catalog)
- OS_Upgradeables_Historical_Recovery_Inventory.md — 1. Canonical current consolidated inventory (historical_recovery_inventory)
