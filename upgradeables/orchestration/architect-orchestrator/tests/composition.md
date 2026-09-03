# Architect Orchestrator — Behavioral Expectations

## Positive Activation

- **Given:** The task requires component architecture and a validated complete package, not one isolated primitive.
- **Expect:** Builds a modular plan, selects components, coordinates drafting and critique, repairs local defects, and emits the finished Skill plus state. Result: A minimal coherent Skill and a compact record of decisions are produced.
- **Reject:** Omitting the mechanism or instead doing this: Does not act as the research domain expert or load every available component.

## Negative Activation

- **Given:** the task is a narrow domain execution job with no architecture decision
- **Expect:** Remain inactive; do not begin the package-specific first step: Lock the goal, constraints, deliverable, authority, and completion criteria.
- **Reject:** Activating Architect Orchestrator solely because its name appears relevant

## Precedence Or Conflict

- **Given:** Host, system, domain, and explicit user authority take precedence over this component.
- **Expect:** Honor the conflict rule and preserve this invariant: Preserve the defining invariant: explicit modular interfaces, authority resolution, independent critique, and continuation state.
- **Reject:** Silently violating the stated precedence for Architect Orchestrator

## Failure Boundary

- **Given:** required module interfaces or authority relationships cannot be resolved
- **Expect:** Stop, narrow, abstain, or escalate while preserving: explicit modular interfaces, authority resolution, independent critique, and continuation state
- **Reject:** Claiming a successful Architect Orchestrator result past this boundary

## Strong Model Scaling

- **Given:** a capable host can compress the workflow
- **Expect:** explicit modular interfaces, authority resolution, independent critique, and continuation state
- **Reject:** dropping the mandatory invariant

## Distinctive Mechanism

- **Given:** a design task requires several modules with dependencies and separate critique
- **Expect:** the orchestrator produces a modular plan, coordinates execution, critiques, repairs locally, synthesizes, and emits continuation state
- **Reject:** returning a flat component list or impersonating the domain execution agent

These are provider-neutral behavioral specifications. Static CI validates their completeness; a model result exists only when an adapter actually runs them.
