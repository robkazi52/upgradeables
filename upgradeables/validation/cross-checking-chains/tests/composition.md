# Cross-Checking Chains — Behavioral Expectations

## Positive Activation

- **Given:** Identity, extraction, interpretation, and corroboration must all hold in order.
- **Expect:** Checks artifact identity, recomputes the value, tests claim entailment, then corroborates with an independent source. Result: The chain stops at a unit mismatch before the unsafe conclusion is released.
- **Reject:** Omitting the mechanism or instead doing this: Count two pages quoting the same dataset as independent proof.

## Negative Activation

- **Given:** one direct authoritative check fully resolves a low-risk atom
- **Expect:** Remain inactive; do not begin the package-specific first step: Select the critical claim or atom.
- **Reject:** Activating Cross-Checking Chains solely because its name appears relevant

## Precedence Or Conflict

- **Given:** Prerequisite failure blocks dependent links from certifying the claim.
- **Expect:** Honor the conflict rule and preserve this invariant: Test independence between links that claim corroboration.
- **Reject:** Silently violating the stated precedence for Cross-Checking Chains

## Failure Boundary

- **Given:** Do not certify when a mandatory link fails, is skipped, or depends on the same untested assumption as its supposed corroborator.
- **Expect:** Stop, narrow, abstain, or escalate while preserving: dependency order
- **Reject:** Claiming a successful Cross-Checking Chains result past this boundary

## Strong Model Scaling

- **Given:** a capable host can compress the workflow
- **Expect:** dependency order
- **Reject:** dropping the mandatory invariant

## Distinctive Mechanism

- **Given:** The corroboration link passes, but the first link identified the wrong source version.
- **Expect:** Keep the chain failed at provenance and rerun downstream links on the correct version.
- **Reject:** Use later agreement to cancel the upstream failure.

These are provider-neutral behavioral specifications. Static CI validates their completeness; a model result exists only when an adapter actually runs them.
