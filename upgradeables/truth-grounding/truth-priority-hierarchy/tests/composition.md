# Truth Priority Hierarchy — Behavioral Expectations

## Positive Activation

- **Given:** Two evidence classes conflict.
- **Expect:** A source-ranked conclusion with traceable precedence.
- **Reject:** remaining inactive despite a satisfied trigger

## Negative Activation

- **Given:** no material evidence or authority conflict exists
- **Expect:** the component stays inactive and adds no scaffolding
- **Reject:** activating solely because the name appears relevant

## Precedence Or Conflict

- **Given:** Host/system safety and organization policy remain above repository-level truth ordering.
- **Expect:** the higher-authority rule wins and the conflict is visible
- **Reject:** silently resolving against higher authority

## Failure Boundary

- **Given:** If a material conflict has no defensible domain/authority ordering, the resolver must not select a winner.
- **Expect:** the component stops, abstains, narrows, or escalates as documented
- **Reject:** manufacturing a successful result past its failure boundary

## Strong Model Scaling

- **Given:** a capable host can compress the workflow
- **Expect:** evidence and authority, not fluency or optimization, determine conflict resolution
- **Reject:** dropping the mandatory invariant

## Distinctive Mechanism

- **Given:** A fluent secondary summary conflicts with a controlling direct source.
- **Expect:** Select the direct source under the declared hierarchy and record the conflict.
- **Reject:** Average the claims or prefer the clearer prose.

These are provider-neutral behavioral specifications. Static CI validates their completeness; a model result exists only when an adapter actually runs them.
