# CRISPR Editing

## Summary

Applies a precisely bounded change to an OS, prompt, skill, document, or architecture while proving that named invariants outside the edit remain intact.

## Purpose

Make high-confidence micro-edits to structured systems without collateral semantic or interface drift.

## Problem Solved

Even a small requested change can accidentally alter neighboring rules, precedence, identifiers, citations, schemas, or behavior when treated as free-form rewriting.

## Where It Fits in the OS

Roles: precision structural editor, invariant-preserving patch operator. Pipeline stages: change planning, targeted modification, invariance validation.

This component acts within those stages; it does not take over the complete task or outrank the host Skill.

## Best-Fit Activities / Tasks

- one rule change in a prompt or skill
- small schema-compatible config edit
- precise clause replacement
- localized architecture adjustment

## When Not to Use

- the governing structure is wrong
- multiple interfaces must be redesigned
- the target boundary cannot be isolated
- the requested change conflicts with locked truth or policy

## Scope

Canonical package: `crispr-edit@1.1.0`. ID: `A-07`. Functional classes: editing-repair. Activation: `U2-specialized`. Mechanism basis: `recovered`. Activation cost: `medium` (architectural burden, not measured compute).

## Trigger Conditions

- a change is small and local

## Non-Triggers

- the governing structure is wrong
- multiple interfaces must be redesigned
- the target boundary cannot be isolated
- the requested change conflicts with locked truth or policy

## Inputs / Required State

- target artifact and exact region
- requested semantic delta
- protected invariants
- dependency map
- validation probes

## Outputs / Produced State

- minimal patch
- before/after diff
- invariant test results
- acceptance or escalation decision

## Mechanism

Construct a patch contract before editing: exact target coordinates, requested semantic delta, protected invariants, allowed collateral region, and validation probes. Snapshot the target plus its immediate dependency boundary, apply the smallest diff that realizes the delta, and compare before/after behavior on both the changed case and invariant cases. A patch that requires broad remapping is rejected and escalated to Surgery rather than stretched into disguised rewrite.

## Procedure

1. Identify the exact editable unit and the request's semantic delta.
2. Enumerate invariants: facts, IDs, interfaces, precedence, citations, unaffected behaviors, and formatting contracts that must not change.
3. Trace immediate inbound and outbound dependencies to set a finite collateral boundary.
4. Create and apply the smallest patch inside that boundary.
5. Run a positive probe for the new behavior and negative probes for each protected invariant.
6. Inspect the diff for unrelated changes; accept, revert-and-redesign, or escalate to Surgery if the boundary cannot hold.

## Always-Do Rules

- declare target and invariants before editing
- keep a before-state for comparison
- test both the intended change and unchanged behaviors
- inspect the actual diff

## Never-Do / Avoid Rules

- use search-and-replace without checking semantic scope
- rename or reorder unrelated elements for cleanliness
- claim success from syntax alone
- continue expanding the patch boundary until it becomes a macro rewrite

## Interaction Rules

### `invariance-stress-scaffold`

Invariance Stress turns the protected set into explicit negative tests.

### `micro-repair`

Micro-Repair is the lighter local repair discipline used inside a CRISPR patch.

### `critical-atomic-verification`

Atomic verification validates the exact facts, tokens, or rules touched.

## Compatible Upgradeables

- `invariance-stress-scaffold` — Invariance Stress turns the protected set into explicit negative tests.
- `micro-repair` — Micro-Repair is the lighter local repair discipline used inside a CRISPR patch.
- `critical-atomic-verification` — Atomic verification validates the exact facts, tokens, or rules touched.

## Counterbalancing Upgradeables

### `surgery-edit`

Surgery takes over when the edit cannot preserve the current architecture or interfaces within a bounded region.

## Potential Redundancy

### `micro-repair`

Both minimize change, but CRISPR adds a structured target contract, dependency boundary, and invariant test matrix for OS-like artifacts.

### `safe-rewrite`

Safe Rewrite protects facts during prose transformation; CRISPR applies a precise semantic patch to any structured artifact.

## Conflict / Precedence Rules

- Locked safety, truth, and authorization invariants cannot be included in the requested delta.
- If the new behavior and protected invariants cannot coexist, stop and expose the conflict.
- If more than the bounded dependency region must change, route to Surgery with a migration plan.

## Failure Boundary

- collateral semantic drift
- syntactically valid but behaviorally wrong patch
- unbounded patch growth
- missing dependency update
- false invariance claims

## Strong-Model Scaling

May skip:

- a long written patch contract for a trivial typo with no dependencies

Keep mandatory:

- explicit invariant set
- bounded dependency inspection
- positive and negative probes
- diff review

## Recommended Skill Types

- one rule change in a prompt or skill
- small schema-compatible config edit
- precise clause replacement
- localized architecture adjustment

## Example Composition

**Task context:** Change a skill so web browsing is required for current prices but remains optional for stable historical facts.

**Why it activates:** One trigger rule changes while safety, citation, and other browsing rules must remain stable.

**Inputs/state:** The trigger paragraph, neighboring precedence rules, and tests are available.

**Action:** Defines the one-condition delta, lists preserved rules, patches only the current-price branch, tests current and historical prompts, and confirms no unrelated diff.

**Does not:** Rewrite the whole browsing policy or silently alter source requirements.

**Result/state change:** A narrow behavioral change with invariant evidence.

**Companions:** ['invariance-stress-scaffold', 'critical-atomic-verification']

## Tests

See [`tests/cases.json`](tests/cases.json) for six structured behavior cases and [`tests/composition.md`](tests/composition.md) for the human-readable expectations. Behavioral cases are specifications until run through a real model adapter; CI validates their structure, not model quality.

## Provenance / Historical Aliases

Primary source ID: `A-07` in `OS_Upgradeable_to_Skills_Translation_Catalog_v2_Recovery_Merged.md`. Registry generation: `consolidated-2026-09`. Historical aliases: None.

Source support: `sufficiently-recovered`. Mechanism basis: `recovered`.

Structured source references:

- OS_Upgradeable_to_Skills_Translation_Catalog_v2_Recovery_Merged.md — A-07. CRISPR Editing (current_consolidated_catalog)
- OS_Upgradeables_Historical_Recovery_Inventory.md — 11. Advanced architecture Upgradeables retained (historical_recovery_inventory)
- OS_Upgradeables_Deep_Context_Recovery_Addendum_2026-09-03.md — 19.5 OS / Skill construction (historical_assistant_artifact)
