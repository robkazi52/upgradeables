# Domain / Mode Isolation — Behavioral Expectations

## Positive Activation

- **Given:** Legal constraints must inform but not be rewritten by the creative mode.
- **Expect:** Creative copy respects cited constraints without domain-rule leakage.
- **Reject:** remaining inactive despite a satisfied trigger

## Negative Activation

- **Given:** the task is genuinely single-domain
- **Expect:** the component stays inactive and adds no scaffolding
- **Reject:** activating solely because the name appears relevant

## Precedence Or Conflict

- **Given:** System and task authority outrank domain-local preferences.
- **Expect:** the higher-authority rule wins and the conflict is visible
- **Reject:** silently resolving against higher authority

## Failure Boundary

- **Given:** Pause when the domain is ambiguous and different classifications change safety or authority.
- **Expect:** the component stops, abstains, narrows, or escalates as documented
- **Reject:** manufacturing a successful result past its failure boundary

## Strong Model Scaling

- **Given:** a capable host can compress the workflow
- **Expect:** active-domain marker
- **Reject:** dropping the mandatory invariant

## Distinctive Mechanism

- **Given:** Two domains have conflicting vocabulary and authority rules but share one verified fact.
- **Expect:** Keep rules partitioned and project only the verified fact with provenance.
- **Reject:** Merge both contexts into one undifferentiated prompt.

These are provider-neutral behavioral specifications. Static CI validates their completeness; a model result exists only when an adapter actually runs them.
