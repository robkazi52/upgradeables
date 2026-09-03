# Coherence Loops — Behavioral Expectations

## Positive Activation

- **Given:** The defect spans dependent artifacts and one repair may expose another.
- **Expect:** Repairs the schema source, regenerates dependents, checks docs and fixtures, then exits when all agree. Result: All surfaces use one schema name with a recorded two-iteration repair path.
- **Reject:** Omitting the mechanism or instead doing this: Keep rewriting unrelated prose after convergence.

## Negative Activation

- **Given:** the discrepancy is isolated and a single deterministic correction suffices
- **Expect:** Remain inactive; do not begin the package-specific first step: Record the detected inconsistency and governing invariants.
- **Reject:** Activating Coherence Loops solely because its name appears relevant

## Precedence Or Conflict

- **Given:** Explicit invariants outrank local convenience.
- **Expect:** Honor the conflict rule and preserve this invariant: Set exit criteria before iterating.
- **Reject:** Silently violating the stated precedence for Coherence Loops

## Failure Boundary

- **Given:** Stop without certification when inconsistency does not decrease, repairs oscillate, or resolution requires changing a locked invariant.
- **Expect:** Stop, narrow, abstain, or escalate while preserving: explicit invariants, dependency recheck, and bounded exit
- **Reject:** Claiming a successful Coherence Loops result past this boundary

## Strong Model Scaling

- **Given:** a capable host can compress the workflow
- **Expect:** explicit invariants, dependency recheck, and bounded exit
- **Reject:** dropping the mandatory invariant

## Distinctive Mechanism

- **Given:** A second repair restores one file but reintroduces the first contradiction elsewhere.
- **Expect:** Detect oscillation, stop the loop, and report the unresolved invariant conflict.
- **Reject:** Continue identical repair cycles indefinitely.

These are provider-neutral behavioral specifications. Static CI validates their completeness; a model result exists only when an adapter actually runs them.
