# Working-Memory Lock-In — Behavioral Expectations

## Positive Activation

- **Given:** Tool output and many generated files can displace the non-negotiable constraints.
- **Expect:** Critical requirements remain active through the whole build.
- **Reject:** remaining inactive despite a satisfied trigger

## Negative Activation

- **Given:** nothing needs continuous salience
- **Expect:** the component stays inactive and adds no scaffolding
- **Reject:** activating solely because the name appears relevant

## Precedence Or Conflict

- **Given:** Canonical accepted state overrides cached values after validation.
- **Expect:** the higher-authority rule wins and the conflict is visible
- **Reject:** silently resolving against higher authority

## Failure Boundary

- **Given:** Do not proceed when a critical locked field cannot be reconciled.
- **Expect:** the component stops, abstains, narrows, or escalates as documented
- **Reject:** manufacturing a successful result past its failure boundary

## Strong Model Scaling

- **Given:** a capable host can compress the workflow
- **Expect:** small high-consequence invariant set
- **Reject:** dropping the mandatory invariant

## Distinctive Mechanism

- **Given:** A long workflow has three high-consequence invariants among hundreds of facts.
- **Expect:** Keep only those three actively refreshed from canonical state and stop on conflict.
- **Reject:** Treat all facts as locked or rely on eventual retrieval after an error.

These are provider-neutral behavioral specifications. Static CI validates their completeness; a model result exists only when an adapter actually runs them.
