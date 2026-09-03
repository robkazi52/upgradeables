# Domain Core Builder — Behavioral Expectations

## Positive Activation

- **Given:** Several investigation and reporting Genes need the same entities, evidence ranking, and causal map.
- **Expect:** Encodes entities, evidence hierarchy, data requirements, causal graph, decision logic, failure modes, and interfaces for an investigation Gene and citation validator. Result: A reusable sourced Core queried by multiple behaviors.
- **Reject:** Omitting the mechanism or instead doing this: Hard-code an executive writing tone or invent facts for missing logs.

## Negative Activation

- **Given:** the need is purely behavioral
- **Expect:** Remain inactive; do not begin the package-specific first step: Define domain boundaries, target decisions, and excluded neighboring domains.
- **Reject:** Activating Domain Core Builder solely because its name appears relevant

## Precedence Or Conflict

- **Given:** Source evidence outranks a convenient decision map.
- **Expect:** Honor the conflict rule and preserve this invariant: separate knowledge from behavior
- **Reject:** Silently violating the stated precedence for Domain Core Builder

## Failure Boundary

- **Given:** knowledge-behavior conflation
- **Expect:** Stop, narrow, abstain, or escalate while preserving: source provenance
- **Reject:** Claiming a successful Domain Core Builder result past this boundary

## Strong Model Scaling

- **Given:** a capable host can compress the workflow
- **Expect:** source provenance
- **Reject:** dropping the mandatory invariant

## Distinctive Mechanism

- **Given:** A recurring domain needs facts, evidence ranking, reasoning maps, and decision logic for several task behaviors.
- **Expect:** The skill emits a sourced Core with the recovered fields and separate Gene interfaces.
- **Reject:** The skill emits a behavior prompt, task-state snapshot, or unsourced domain summary.

These are provider-neutral behavioral specifications. Static CI validates their completeness; a model result exists only when an adapter actually runs them.
