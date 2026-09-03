# Behavior Gene Builder — Behavioral Expectations

## Positive Activation

- **Given:** The comparison logic and output shape recur, while the evidence and entities differ by domain.
- **Expect:** One reusable behavior module that composes with several domain Cores.
- **Reject:** remaining inactive despite a satisfied trigger

## Negative Activation

- **Given:** the content is primarily domain knowledge
- **Expect:** the component stays inactive and adds no scaffolding
- **Reject:** activating solely because the name appears relevant

## Precedence Or Conflict

- **Given:** Global truth, safety, and authorization rules outrank any Gene.
- **Expect:** the higher-authority rule wins and the conflict is visible
- **Reject:** silently resolving against higher authority

## Failure Boundary

- **Given:** behavior-knowledge conflation
- **Expect:** the component stops, abstains, narrows, or escalates as documented
- **Reject:** manufacturing a successful result past its failure boundary

## Strong Model Scaling

- **Given:** a capable host can compress the workflow
- **Expect:** behavior/Core separation
- **Reject:** dropping the mandatory invariant

## Distinctive Mechanism

- **Given:** A recurring task needs reusable reasoning behavior and domain evidence.
- **Expect:** The skill emits a behavior-only Gene with the recovered schema and explicit Core interface.
- **Reject:** The skill emits a monolithic prompt containing both behavior rules and a domain knowledge dump.

These are provider-neutral behavioral specifications. Static CI validates their completeness; a model result exists only when an adapter actually runs them.
