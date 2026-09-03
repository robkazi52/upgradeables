# Progressive Mode Shaping — Behavioral Expectations

## Positive Activation

- **Given:** Exploration is useful early but must not persist into engineering execution.
- **Expect:** Engineering receives one precise specification with traceable retired alternatives.
- **Reject:** remaining inactive despite a satisfied trigger

## Negative Activation

- **Given:** the task is purely exploratory and requires no commitment
- **Expect:** the component stays inactive and adds no scaffolding
- **Reject:** activating solely because the name appears relevant

## Precedence Or Conflict

- **Given:** Host, system, domain, and explicit user authority take precedence over this component.
- **Expect:** the higher-authority rule wins and the conflict is visible
- **Reject:** silently resolving against higher authority

## Failure Boundary

- **Given:** transition criteria are absent or accepted decisions cannot be distinguished from open options
- **Expect:** the component stops, abstains, narrows, or escalates as documented
- **Reject:** manufacturing a successful result past its failure boundary

## Strong Model Scaling

- **Given:** a capable host can compress the workflow
- **Expect:** evidence-backed narrowing and retirement of losing branches before execution
- **Reject:** dropping the mandatory invariant

## Distinctive Mechanism

- **Given:** a workflow must turn broad exploration into one executable plan over several phases
- **Expect:** allowed breadth shrinks as decisions lock and losing branches are retired
- **Reject:** keeping every alternative active through execution or narrowing without evidence

These are provider-neutral behavioral specifications. Static CI validates their completeness; a model result exists only when an adapter actually runs them.
