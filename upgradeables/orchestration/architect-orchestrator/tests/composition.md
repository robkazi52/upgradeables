# Architect Orchestrator — Behavioral Expectations

## Positive Activation

- **Given:** The task requires component architecture and a validated complete package, not one isolated primitive.
- **Expect:** A minimal coherent Skill and a compact record of decisions are produced.
- **Reject:** remaining inactive despite a satisfied trigger

## Negative Activation

- **Given:** the task is a narrow domain execution job with no architecture decision
- **Expect:** the component stays inactive and adds no scaffolding
- **Reject:** activating solely because the name appears relevant

## Precedence Or Conflict

- **Given:** Host, system, domain, and explicit user authority take precedence over this component.
- **Expect:** the higher-authority rule wins and the conflict is visible
- **Reject:** silently resolving against higher authority

## Failure Boundary

- **Given:** required module interfaces or authority relationships cannot be resolved
- **Expect:** the component stops, abstains, narrows, or escalates as documented
- **Reject:** manufacturing a successful result past its failure boundary

## Strong Model Scaling

- **Given:** a capable host can compress the workflow
- **Expect:** explicit modular interfaces, authority resolution, independent critique, and continuation state
- **Reject:** dropping the mandatory invariant

## Distinctive Mechanism

- **Given:** a design task requires several modules with dependencies and separate critique
- **Expect:** the orchestrator produces a modular plan, coordinates execution, critiques, repairs locally, synthesizes, and emits continuation state
- **Reject:** returning a flat component list or impersonating the domain execution agent

These are provider-neutral behavioral specifications. Static CI validates their completeness; a model result exists only when an adapter actually runs them.
