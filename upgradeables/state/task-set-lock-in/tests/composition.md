# Task-Set Lock-In — Behavioral Expectations

## Positive Activation

- **Given:** Many attractive documentation additions could distract from required build and validation outputs.
- **Expect:** Completion is evaluated against the original concrete specification.
- **Reject:** remaining inactive despite a satisfied trigger

## Negative Activation

- **Given:** the task is still materially ambiguous
- **Expect:** the component stays inactive and adds no scaffolding
- **Reject:** activating solely because the name appears relevant

## Precedence Or Conflict

- **Given:** System and latest explicit authorized user scope changes override older task-set versions.
- **Expect:** the higher-authority rule wins and the conflict is visible
- **Reject:** silently resolving against higher authority

## Failure Boundary

- **Given:** Do not claim completion when a required artifact or quality gate lacks evidence.
- **Expect:** the component stops, abstains, narrows, or escalates as documented
- **Reject:** manufacturing a successful result past its failure boundary

## Strong Model Scaling

- **Given:** a capable host can compress the workflow
- **Expect:** objective
- **Reject:** dropping the mandatory invariant

## Distinctive Mechanism

- **Given:** During execution, a related but non-required feature appears useful.
- **Expect:** Keep it out of scope unless an authorized scope-change updates the task set.
- **Reject:** Replace a required deliverable with the attractive adjacent feature.

These are provider-neutral behavioral specifications. Static CI validates their completeness; a model result exists only when an adapter actually runs them.
