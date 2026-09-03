# External State Automation — Behavioral Expectations

## Positive Activation

- **Given:** Verified decisions and source pointers need durable continuation.
- **Expect:** The next session restores traceable state or receives an explicit failure/staleness warning.
- **Reject:** remaining inactive despite a satisfied trigger

## Negative Activation

- **Given:** the task ends in one session and needs no continuation
- **Expect:** the component stays inactive and adds no scaffolding
- **Reject:** activating solely because the name appears relevant

## Precedence Or Conflict

- **Given:** Host, system, domain, and explicit user authority take precedence over this component.
- **Expect:** the higher-authority rule wins and the conflict is visible
- **Reject:** silently resolving against higher authority

## Failure Boundary

- **Given:** no authorized storage capability is available
- **Expect:** the component stops, abstains, narrows, or escalates as documented
- **Reject:** manufacturing a successful result past its failure boundary

## Strong Model Scaling

- **Given:** a capable host can compress the workflow
- **Expect:** capability declaration, minimum-state serialization, write verification, and restore validation
- **Reject:** dropping the mandatory invariant

## Distinctive Mechanism

- **Given:** a task must continue across sessions using an actual storage system
- **Expect:** state is minimally serialized, written, verified, restored, and reconciled
- **Reject:** claiming memory without a real write or storing unbounded conversation data

These are provider-neutral behavioral specifications. Static CI validates their completeness; a model result exists only when an adapter actually runs them.
