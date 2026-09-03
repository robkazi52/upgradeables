# Domain / Mode Isolation — Behavioral Expectations

## Positive Activation

- **Given:** Legal constraints must inform but not be rewritten by the creative mode.
- **Expect:** Keeps legal authority in the legal compartment and projects only approved constraints to the writing compartment. Result: Creative copy respects cited constraints without domain-rule leakage.
- **Reject:** Omitting the mechanism or instead doing this: It does not treat brand tone as legal authority or expose the full legal workspace to the copywriter.

## Negative Activation

- **Given:** the task is genuinely single-domain
- **Expect:** Remain inactive; do not begin the package-specific first step: Classify the task and enumerate domains that are actually needed.
- **Reject:** Activating Domain / Mode Isolation solely because its name appears relevant

## Precedence Or Conflict

- **Given:** System and task authority outrank domain-local preferences.
- **Expect:** Honor the conflict rule and preserve this invariant: name the active domain
- **Reject:** Silently violating the stated precedence for Domain / Mode Isolation

## Failure Boundary

- **Given:** Pause when the domain is ambiguous and different classifications change safety or authority.
- **Expect:** Stop, narrow, abstain, or escalate while preserving: active-domain marker
- **Reject:** Claiming a successful Domain / Mode Isolation result past this boundary

## Strong Model Scaling

- **Given:** a capable host can compress the workflow
- **Expect:** active-domain marker
- **Reject:** dropping the mandatory invariant

## Distinctive Mechanism

- **Given:** Two domains have conflicting vocabulary and authority rules but share one verified fact.
- **Expect:** Keep rules partitioned and project only the verified fact with provenance.
- **Reject:** Merge both contexts into one undifferentiated prompt.

These are provider-neutral behavioral specifications. Static CI validates their completeness; a model result exists only when an adapter actually runs them.
