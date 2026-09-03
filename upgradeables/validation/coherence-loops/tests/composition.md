# Coherence Loops — Behavioral Expectations

## Positive Activation

- **Given:** The defect spans dependent artifacts and one repair may expose another.
- **Expect:** All surfaces use one schema name with a recorded two-iteration repair path.
- **Reject:** remaining inactive despite a satisfied trigger

## Negative Activation

- **Given:** the discrepancy is isolated and a single deterministic correction suffices
- **Expect:** the component stays inactive and adds no scaffolding
- **Reject:** activating solely because the name appears relevant

## Precedence Or Conflict

- **Given:** Explicit invariants outrank local convenience.
- **Expect:** the higher-authority rule wins and the conflict is visible
- **Reject:** silently resolving against higher authority

## Failure Boundary

- **Given:** Stop without certification when inconsistency does not decrease, repairs oscillate, or resolution requires changing a locked invariant.
- **Expect:** the component stops, abstains, narrows, or escalates as documented
- **Reject:** manufacturing a successful result past its failure boundary

## Strong Model Scaling

- **Given:** a capable host can compress the workflow
- **Expect:** explicit invariants, dependency recheck, and bounded exit
- **Reject:** dropping the mandatory invariant

## Distinctive Mechanism

- **Given:** A second repair restores one file but reintroduces the first contradiction elsewhere.
- **Expect:** Detect oscillation, stop the loop, and report the unresolved invariant conflict.
- **Reject:** Continue identical repair cycles indefinitely.

These are provider-neutral behavioral specifications. Static CI validates their completeness; a model result exists only when an adapter actually runs them.
