# Domain Core Builder — Behavioral Expectations

## Positive Activation

- **Given:** Several investigation and reporting Genes need the same entities, evidence ranking, and causal map.
- **Expect:** A reusable sourced Core queried by multiple behaviors.
- **Reject:** remaining inactive despite a satisfied trigger

## Negative Activation

- **Given:** the need is purely behavioral
- **Expect:** the component stays inactive and adds no scaffolding
- **Reject:** activating solely because the name appears relevant

## Precedence Or Conflict

- **Given:** Source evidence outranks a convenient decision map.
- **Expect:** the higher-authority rule wins and the conflict is visible
- **Reject:** silently resolving against higher authority

## Failure Boundary

- **Given:** knowledge-behavior conflation
- **Expect:** the component stops, abstains, narrows, or escalates as documented
- **Reject:** manufacturing a successful result past its failure boundary

## Strong Model Scaling

- **Given:** a capable host can compress the workflow
- **Expect:** source provenance
- **Reject:** dropping the mandatory invariant

## Distinctive Mechanism

- **Given:** A recurring domain needs facts, evidence ranking, reasoning maps, and decision logic for several task behaviors.
- **Expect:** The skill emits a sourced Core with the recovered fields and separate Gene interfaces.
- **Reject:** The skill emits a behavior prompt, task-state snapshot, or unsourced domain summary.

These are provider-neutral behavioral specifications. Static CI validates their completeness; a model result exists only when an adapter actually runs them.
