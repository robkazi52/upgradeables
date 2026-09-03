# StateBlock — Behavioral Expectations

## Positive Activation

- **Given:** They need a shared current objective, source set, status, and unresolved-risk record.
- **Expect:** Coordination and validation use the same current task truth.
- **Reject:** remaining inactive despite a satisfied trigger

## Negative Activation

- **Given:** a trivial one-turn task needs no persistent state
- **Expect:** the component stays inactive and adds no scaffolding
- **Reject:** activating solely because the name appears relevant

## Precedence Or Conflict

- **Given:** System and explicit task authority govern locked fields; evidence updates factual fields only through their declared owners.
- **Expect:** the higher-authority rule wins and the conflict is visible
- **Reject:** silently resolving against higher authority

## Failure Boundary

- **Given:** Do not proceed on dependent actions when required state is contradictory or unknown.
- **Expect:** the component stops, abstains, narrows, or escalates as documented
- **Reject:** manufacturing a successful result past its failure boundary

## Strong Model Scaling

- **Given:** a capable host can compress the workflow
- **Expect:** single source of truth
- **Reject:** dropping the mandatory invariant

## Distinctive Mechanism

- **Given:** Several workers need current constraints, progress, and decisions.
- **Expect:** Maintain one schema-defined, versioned canonical state with controlled projections.
- **Reject:** Rely on scattered narrative summaries or multiple competing truth records.

These are provider-neutral behavioral specifications. Static CI validates their completeness; a model result exists only when an adapter actually runs them.
