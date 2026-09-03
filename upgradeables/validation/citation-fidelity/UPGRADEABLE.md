# Citation Fidelity Gate

## Summary

Verify that each citation exists and actually supports its attached claim without adjacent-source borrowing or meaning drift.

## Purpose

Provide a reusable `validator` mechanism rather than
a complete task identity or monolithic prompt.

## Problem Solved

Prevents the workflow failure implied by the trigger while keeping the
intervention bounded and inspectable.

## Scope

Functional classes: validation, truth-grounding. Activation:
`U1-common-conditional`. This modern classification is not a historical tier.

## Trigger Conditions

- output contains citations or source-attributed claims

## Non-Triggers

- the declared trigger is absent or the control would add no material value

## Inputs / Required State

- claim
- citation
- supporting source passage

## Outputs / Produced State

- pass
- fail
- repair-required
- unverifiable

## Mechanism

Bind each claim to its cited source passage; verify source existence, exact quotes, paraphrase meaning, and that support was not borrowed from an adjacent claim. Return a status without rewriting evidence.

The name is architectural identity, not a claim of a physical, biological,
hidden, or private-reasoning mechanism.

## Procedure

1. Split the output into cited claims.
2. Locate the cited source passage for each claim.
3. Compare the claim or quote with that passage for direct support and preserved meaning.
4. Return pass, fail, repair-required, or unverifiable for each claim.
5. Do not certify the output while a material citation is failed or unverifiable.

## Always-Do Rules

- Preserve higher-authority instructions and locked facts.
- Label assumptions and unavailable host capabilities.
- Keep activation proportional to risk and value.

## Never-Do / Avoid Rules

- Do not invent evidence, hidden state, persistence, or execution.
- Do not remain active when the trigger is absent.
- Do not expose or require private chain-of-thought.

## Interaction Rules

Load after the task boundary is known. Validators inspect or veto but do not
author supporting facts. State changes must use explicit state mechanisms.

## Compatible Upgradeables

- `grounding-no-invention`
- `critical-atomic-verification`

## Counterbalancing Upgradeables

- `None declared`

## Potential Redundancy

- `None declared`

## Conflict / Precedence Rules

Host/system safety, domain policy, the active OS, and the task lock take
precedence. On an unresolved material conflict, narrow, abstain, or escalate.

## Failure Boundary

- if support cannot be verified, do not certify the citation

## Strong-Model Scaling

May skip: nothing; the invariant remains active whenever citations are emitted.
Keep mandatory: a citation must actually support its attached claim.

## Recommended Skill Types

- `general-agent-workflow`
- `high-stakes-reasoning`
- `research`
- `source-grounded-analysis`

## Example Composition

Activate `citation-fidelity` only after task framing, combine it with the declared
compatible controls, then validate its output before final commitment.

## Tests

See [`tests/composition.md`](tests/composition.md) for positive, negative,
conflict, and scaling cases.

## Provenance / Historical Aliases

Source ID: `T3-13` in `OS_Upgradeable_to_Skills_Translation_Catalog_v2_Recovery_Merged.md`. Registry generation:
`consolidated-2026-09`. Aliases: None.
