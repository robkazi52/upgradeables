# Cross-Checking Chains — Behavioral Expectations

## Positive Activation

- **Given:** Identity, extraction, interpretation, and corroboration must all hold in order.
- **Expect:** The chain stops at a unit mismatch before the unsafe conclusion is released.
- **Reject:** remaining inactive despite a satisfied trigger

## Negative Activation

- **Given:** one direct authoritative check fully resolves a low-risk atom
- **Expect:** the component stays inactive and adds no scaffolding
- **Reject:** activating solely because the name appears relevant

## Precedence Or Conflict

- **Given:** Prerequisite failure blocks dependent links from certifying the claim.
- **Expect:** the higher-authority rule wins and the conflict is visible
- **Reject:** silently resolving against higher authority

## Failure Boundary

- **Given:** Do not certify when a mandatory link fails, is skipped, or depends on the same untested assumption as its supposed corroborator.
- **Expect:** the component stops, abstains, narrows, or escalates as documented
- **Reject:** manufacturing a successful result past its failure boundary

## Strong Model Scaling

- **Given:** a capable host can compress the workflow
- **Expect:** dependency order
- **Reject:** dropping the mandatory invariant

## Distinctive Mechanism

- **Given:** The corroboration link passes, but the first link identified the wrong source version.
- **Expect:** Keep the chain failed at provenance and rerun downstream links on the correct version.
- **Reject:** Use later agreement to cancel the upstream failure.

These are provider-neutral behavioral specifications. Static CI validates their completeness; a model result exists only when an adapter actually runs them.
