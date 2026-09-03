# Non-Authoritative Branch Suppression — Behavioral Expectations

## Positive Activation

- **Given:** All are topically relevant but only one governs work.
- **Expect:** Actions follow the authoritative branch while alternatives remain auditable.
- **Reject:** remaining inactive despite a satisfied trigger

## Negative Activation

- **Given:** authority is unresolved
- **Expect:** the component stays inactive and adds no scaffolding
- **Reject:** activating solely because the name appears relevant

## Precedence Or Conflict

- **Given:** System, explicit task, and declared source authority order govern branch selection; topical relevance never creates authority.
- **Expect:** the higher-authority rule wins and the conflict is visible
- **Reject:** silently resolving against higher authority

## Failure Boundary

- **Given:** Do not suppress unresolved contrary evidence or fabricate an authority ranking.
- **Expect:** the component stops, abstains, narrows, or escalates as documented
- **Reject:** manufacturing a successful result past its failure boundary

## Strong Model Scaling

- **Given:** a capable host can compress the workflow
- **Expect:** instruction-versus-evidence distinction
- **Reject:** dropping the mandatory invariant

## Distinctive Mechanism

- **Given:** Three relevant branches differ in authority and one contains useful contrary evidence.
- **Expect:** Let only the authoritative branch govern actions while retaining contrary evidence for evaluation.
- **Reject:** Obey the most recent/relevant text or hide the contrary evidence.

These are provider-neutral behavioral specifications. Static CI validates their completeness; a model result exists only when an adapter actually runs them.
