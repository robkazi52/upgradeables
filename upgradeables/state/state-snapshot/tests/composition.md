# State Snapshot — Behavioral Expectations

## Positive Activation

- **Given:** The second session must know exactly which sources and claims were accepted at handoff.
- **Expect:** The review resumes from a reproducible checkpoint.
- **Reject:** remaining inactive despite a satisfied trigger

## Negative Activation

- **Given:** a snapshot would persist prohibited sensitive data
- **Expect:** the component stays inactive and adds no scaffolding
- **Reject:** activating solely because the name appears relevant

## Precedence Or Conflict

- **Given:** A newer validated canonical state outranks an older snapshot.
- **Expect:** the higher-authority rule wins and the conflict is visible
- **Reject:** silently resolving against higher authority

## Failure Boundary

- **Given:** Do not restore when integrity, task identity, or schema compatibility cannot be established.
- **Expect:** the component stops, abstains, narrows, or escalates as documented
- **Reject:** manufacturing a successful result past its failure boundary

## Strong Model Scaling

- **Given:** a capable host can compress the workflow
- **Expect:** immutable version identity
- **Reject:** dropping the mandatory invariant

## Distinctive Mechanism

- **Given:** Live state may change after an agent handoff begins.
- **Expect:** Freeze and identify one validated version, then reconcile later events on resume.
- **Reject:** Copy an unversioned mutable summary and call it current state.

These are provider-neutral behavioral specifications. Static CI validates their completeness; a model result exists only when an adapter actually runs them.
