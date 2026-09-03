# Drift Immunity Propagation — Behavioral Expectations

## Positive Activation

- **Given:** Each stage could round, relabel, or detach the figures from their period.
- **Expect:** Final figures retain source identity and protected semantics through the pipeline.
- **Reject:** remaining inactive despite a satisfied trigger

## Negative Activation

- **Given:** no downstream artifact derives from protected material
- **Expect:** the component stays inactive and adds no scaffolding
- **Reject:** activating solely because the name appears relevant

## Precedence Or Conflict

- **Given:** Original verified source and higher-authority constraints outrank downstream paraphrases.
- **Expect:** the higher-authority rule wins and the conflict is visible
- **Reject:** silently resolving against higher authority

## Failure Boundary

- **Given:** Do not label a derivative immune when its invariant cannot be tested.
- **Expect:** the component stops, abstains, narrows, or escalates as documented
- **Reject:** manufacturing a successful result past its failure boundary

## Strong Model Scaling

- **Given:** a capable host can compress the workflow
- **Expect:** stable invariant identity
- **Reject:** dropping the mandatory invariant

## Distinctive Mechanism

- **Given:** A zero-drift fact passes through three transformations and two agents.
- **Expect:** Carry identity, provenance, scope, and predicate through every boundary and test each derivative.
- **Reject:** Lock it only at extraction and trust later summaries to preserve it.

These are provider-neutral behavioral specifications. Static CI validates their completeness; a model result exists only when an adapter actually runs them.
