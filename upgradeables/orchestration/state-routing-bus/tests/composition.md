# State Routing Bus — Behavioral Expectations

## Positive Activation

- **Given:** The writer needs decisions and source pointers but not the worker's full context.
- **Expect:** The writer receives traceable state or the workflow reports a handoff failure.
- **Reject:** remaining inactive despite a satisfied trigger

## Negative Activation

- **Given:** all work occurs inside one uninterrupted component
- **Expect:** the component stays inactive and adds no scaffolding
- **Reject:** activating solely because the name appears relevant

## Precedence Or Conflict

- **Given:** Host, system, domain, and explicit user authority take precedence over this component.
- **Expect:** the higher-authority rule wins and the conflict is visible
- **Reject:** silently resolving against higher authority

## Failure Boundary

- **Given:** no real host-supported handoff channel exists
- **Expect:** the component stops, abstains, narrows, or escalates as documented
- **Reject:** manufacturing a successful result past its failure boundary

## Strong Model Scaling

- **Given:** a capable host can compress the workflow
- **Expect:** explicit payload, provenance, receiver boundary, and delivery status
- **Reject:** dropping the mandatory invariant

## Distinctive Mechanism

- **Given:** separate modules need to transfer task state across a real boundary
- **Expect:** a typed provenance-bearing envelope is validated, transmitted, and acknowledged
- **Reject:** claiming hidden shared memory or passing an unbounded context dump

These are provider-neutral behavioral specifications. Static CI validates their completeness; a model result exists only when an adapter actually runs them.
