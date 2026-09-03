# State Routing Bus — Behavioral Expectations

## Positive Activation

- **Given:** The writer needs decisions and source pointers but not the worker's full context.
- **Expect:** Validates and sends a bounded envelope, then records the writer's acknowledgement. Result: The writer receives traceable state or the workflow reports a handoff failure.
- **Reject:** Omitting the mechanism or instead doing this: Does not claim secret shared memory or transfer private reasoning.

## Negative Activation

- **Given:** all work occurs inside one uninterrupted component
- **Expect:** Remain inactive; do not begin the package-specific first step: Define the sender, receiver, state schema, and permitted payload fields.
- **Reject:** Activating State Routing Bus solely because its name appears relevant

## Precedence Or Conflict

- **Given:** Host, system, domain, and explicit user authority take precedence over this component.
- **Expect:** Honor the conflict rule and preserve this invariant: Preserve the defining invariant: explicit payload, provenance, receiver boundary, and delivery status.
- **Reject:** Silently violating the stated precedence for State Routing Bus

## Failure Boundary

- **Given:** no real host-supported handoff channel exists
- **Expect:** Stop, narrow, abstain, or escalate while preserving: explicit payload, provenance, receiver boundary, and delivery status
- **Reject:** Claiming a successful State Routing Bus result past this boundary

## Strong Model Scaling

- **Given:** a capable host can compress the workflow
- **Expect:** explicit payload, provenance, receiver boundary, and delivery status
- **Reject:** dropping the mandatory invariant

## Distinctive Mechanism

- **Given:** separate modules need to transfer task state across a real boundary
- **Expect:** a typed provenance-bearing envelope is validated, transmitted, and acknowledged
- **Reject:** claiming hidden shared memory or passing an unbounded context dump

These are provider-neutral behavioral specifications. Static CI validates their completeness; a model result exists only when an adapter actually runs them.
