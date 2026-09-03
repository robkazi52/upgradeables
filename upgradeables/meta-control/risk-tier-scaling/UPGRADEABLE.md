# Risk-Tier Scaling

## Summary

Raises reasoning depth, independent verification, and veto strength as consequence, uncertainty, or irreversibility increases.

## Purpose

Apply proportionate rigor so low-risk tasks remain efficient and high-risk claims or actions receive stronger evidence and fail-closed handling.

## Problem Solved

Uniform validation either wastes effort on low-consequence work or exposes consequential decisions to the same weak checks used for routine output.

## Where It Fits in the OS

Roles: risk classifier, mandatory-rigor controller. Pipeline stages: risk triage, control selection, pre-commit validation, risk reclassification.

This component acts within those stages; it does not take over the complete task or outrank the host Skill.

## Best-Fit Activities / Tasks

- medical, legal, financial, or safety-sensitive work
- irreversible changes
- uncertain external actions
- mixed-risk artifacts

## When Not to Use

- a binding protocol already specifies the exact controls
- the task is harmless and fully reversible
- risk labels cannot change any behavior

## Scope

Canonical package: `risk-tier-scaling@1.1.0`. ID: `T3-05`. Functional classes: meta-control, validation. Activation: `U1-common-conditional`. Mechanism basis: `recovered`. Activation cost: `low` (architectural burden, not measured compute).

## Trigger Conditions

- task risk varies or must be classified

## Non-Triggers

- a binding protocol already specifies the exact controls
- the task is harmless and fully reversible
- risk labels cannot change any behavior

## Inputs / Required State

- potential consequences
- uncertainty and evidence quality
- reversibility
- scope of impact
- tier-control matrix

## Outputs / Produced State

- task and regional risk tiers
- mandatory control set
- reclassification record
- commit, abstain, or escalate decision

## Mechanism

Classify the whole task and any higher-risk subregions using consequence, uncertainty, reversibility, scope of impact, and evidence quality. Map the result to explicit control floors: light single-path checks for routine work, stronger source and consistency checks for material work, and independent verification, hard vetoes, checkpointing, and fail-closed behavior for high-risk work. Reclassify when new evidence raises or lowers risk.

## Procedure

1. Identify potential harms, affected parties, uncertainty, reversibility, and blast radius.
2. Assign a risk tier to the task and separately to any exceptional subregion.
3. Select the tier's mandatory reasoning, evidence, independent-check, and veto controls.
4. Fund those controls through Cognitive Governor and route depth with DDA.
5. Reassess risk before irreversible action and whenever new evidence changes consequence or uncertainty.
6. Commit only when the tier's acceptance gates pass; otherwise abstain, escalate, or narrow the action.

## Always-Do Rules

- assess consequence and uncertainty separately
- use the highest applicable tier at mixed-risk boundaries
- make tier controls observable
- reclassify on new evidence

## Never-Do / Avoid Rules

- assign risk from domain label alone
- lower a tier to fit budget
- average away a safety-critical minority risk
- use high rigor everywhere without consequence

## Interaction Rules

### `dynamic-depth-allocation`

DDA concentrates extra work on high-tier regions while preserving baseline coverage.

### `fail-closed-abstention`

High-tier unverifiable results route to abstention instead of forced output.

### `cognitive-governor`

The governor reserves enough total budget to meet the tier's mandatory floor.

## Compatible Upgradeables

- `dynamic-depth-allocation` — DDA concentrates extra work on high-tier regions while preserving baseline coverage.
- `fail-closed-abstention` — High-tier unverifiable results route to abstention instead of forced output.
- `cognitive-governor` — The governor reserves enough total budget to meet the tier's mandatory floor.

## Counterbalancing Upgradeables

### `reasoning-throughput-governor`

Throughput preserves efficiency for low-tier work without weakening high-tier gates.

## Potential Redundancy

### `dynamic-depth-allocation`

Risk Tier sets mandatory rigor; DDA distributes discretionary and required depth among regions.

### `safe-mode`

SAFE is an execution profile appropriate to consequential work; Risk Tier decides when and how much rigor is required.

## Conflict / Precedence Rules

- A required tier cannot be lowered because of cost or deadline.
- When tier controls cannot be completed, return blocked or abstain.
- Mixed-risk tasks use local higher tiers without forcing unrelated routine regions into maximum review.

## Failure Boundary

- domain-label risk
- budget-driven downgrading
- maximum-rigor default
- stale risk classification
- soft score overriding hard veto

## Strong-Model Scaling

May skip:

- formal tier narration for obviously low-risk routine output

Keep mandatory:

- consequence and uncertainty assessment
- high-risk independent checks
- hard veto and fail-closed behavior

## Recommended Skill Types

- medical, legal, financial, or safety-sensitive work
- irreversible changes
- uncertain external actions
- mixed-risk artifacts

## Example Composition

**Task context:** Update a README and rotate a production signing key in one release.

**Why it activates:** The tasks share a release but have radically different consequence and reversibility.

**Inputs/state:** Documentation tests, key owners, backup key, audit log, and rollback procedure exist.

**Action:** Applies a light review to README wording and high-tier independent verification, checkpoints, and fail-closed cutover to the key rotation.

**Does not:** Average both tasks into a medium tier or burden README punctuation with key-rotation controls.

**Result/state change:** Proportionate rigor with the irreversible boundary fully protected.

**Companions:** ['dynamic-depth-allocation', 'fail-closed-abstention', 'cognitive-governor']

## Tests

See [`tests/cases.json`](tests/cases.json) for six structured behavior cases and [`tests/composition.md`](tests/composition.md) for the human-readable expectations. Behavioral cases are specifications until run through a real model adapter; CI validates their structure, not model quality.

## Provenance / Historical Aliases

Primary source ID: `T3-05` in `OS_Upgradeable_to_Skills_Translation_Catalog_v2_Recovery_Merged.md`. Registry generation: `consolidated-2026-09`. Historical aliases: None.

Source support: `sufficiently-recovered`. Mechanism basis: `recovered`.

Structured source references:

- OS_Upgradeable_to_Skills_Translation_Catalog_v2_Recovery_Merged.md — T3-05. Risk-Tier Scaling (current_consolidated_catalog)
- OS_Upgradeables_Historical_Recovery_Inventory.md — 8. Tier-3 / Paper-Author alignment family recovered from late-November work (historical_recovery_inventory)
- OS_Upgradeables_Deep_Context_Recovery_Addendum_2026-09-03.md — 8.2 QMS-RTS — Risk-Tier-Split QMS (historical_assistant_artifact)
