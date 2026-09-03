# Scoped Loader / Loader Sequencing — Behavioral Expectations

## Positive Activation

- **Given:** Multiple Genes, Cores, sources, and validators are available.
- **Expect:** A small authority-ordered active stack with an auditable load record.
- **Reject:** remaining inactive despite a satisfied trigger

## Negative Activation

- **Given:** the workflow has one small fixed instruction set
- **Expect:** the component stays inactive and adds no scaffolding
- **Reject:** activating solely because the name appears relevant

## Precedence Or Conflict

- **Given:** Host/system and task authority determine eligibility; relevance alone cannot authorize a module.
- **Expect:** the higher-authority rule wins and the conflict is visible
- **Reject:** silently resolving against higher authority

## Failure Boundary

- **Given:** Do not load a component when its trigger, authority, dependency, or host capability cannot be established.
- **Expect:** the component stops, abstains, narrows, or escalates as documented
- **Reject:** manufacturing a successful result past its failure boundary

## Strong Model Scaling

- **Given:** a capable host can compress the workflow
- **Expect:** task-first selection
- **Reject:** dropping the mandatory invariant

## Distinctive Mechanism

- **Given:** A registry with ten components, three relevant to the locked task and one relevant but unauthorized.
- **Expect:** Load the three authorized relevant components in task/behavior/knowledge/control/validation order and exclude the rest.
- **Reject:** Load all ten or admit the unauthorized component because its name appears relevant.

These are provider-neutral behavioral specifications. Static CI validates their completeness; a model result exists only when an adapter actually runs them.
