# Adapter-First Experimentation (`adapter-first-experimentation@1.1.0`)

Purpose: Protect a working OS or workflow from speculative capabilities while preserving a path for evidence-based evolution.

Activate when: a new capability may destabilize a base workflow.

Do not use when: the change is a mandatory security repair; no stable interface can isolate the capability.

Requires: none.

## Runtime mechanism

Define an adapter contract around the proposed capability, route only an explicit test cohort through it, and preserve the unchanged base as control and rollback. Compare quality, cost, latency, drift, and failure behavior against predeclared acceptance thresholds; promote only the demonstrated stable interface, otherwise revise or retire the adapter without contaminating core rules.

## Procedure

1. State the hypothesis, acceptance metrics, test cohort, and non-negotiable invariants.
2. Expose the smallest stable interface needed by the capability.
3. Implement or specify it as a detachable adapter with base-path fallback and isolated state.
4. Run representative and adversarial trials against the unchanged base.
5. Compare benefit, regressions, operating cost, and rollback behavior.

## Guardrails

- Mandatory even on strong models: detachable boundary; control comparison; invariant gate.
- Conflict/precedence: Security and integrity repairs follow their mandated path rather than waiting for experimental promotion; If the adapter cannot be isolated from base state or authority, do not trial it in production.
- Stop or fail when: base contamination; unmeasured promotion.

Full package and provenance: [`adapter-first-experimentation`](../../upgradeables/meta-control/adapter-first-experimentation/UPGRADEABLE.md).
