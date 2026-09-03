# Non-Compensable Constraint Veto (`fermionic-veto@1.1.0`)

Recovered name: Fermionic Veto Strengthening

Purpose: Preserve non-compensable constraints during aggregation and synthesis.

Activate when: a defined critical condition must have veto authority.

Do not use when: the alleged defect is merely a soft preference; the veto predicate cannot be defined or evidenced.

Requires: none.

## Runtime mechanism

Declare a narrow set of exclusion predicates before scoring. Evaluate them independently of aggregate quality; if any predicate is evidenced, quarantine the candidate and require removal of the disqualifying state plus revalidation. The fermionic metaphor is operational only: incompatible states do not share the certified result, and the veto is never diluted by votes or averages.

## Procedure

1. Define non-compensable predicates and required evidence.
2. Run veto checks independently from quality scoring.
3. Record the exact predicate, evidence, and affected candidate.
4. Exclude or quarantine any triggered candidate.
5. Permit repair only if the disqualifying state is removed rather than relabeled.

## Guardrails

- Mandatory even on strong models: independent hard-constraint check whenever aggregate scoring is used.
- Conflict/precedence: Verified veto evidence outranks aggregate score or validator majority; If veto evidence conflicts, quarantine pending targeted adjudication rather than silently clearing it.
- Stop or fail when: Do not certify or execute a candidate while a verified non-compensable predicate remains active.

Full package and provenance: [`fermionic-veto`](../../upgradeables/validation/fermionic-veto/UPGRADEABLE.md).
