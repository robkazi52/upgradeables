# Runtime Compatibility Mode Selector (`future-proof-mode-selector@1.1.0`)

Recovered name: Future-Proof Mode Selector

Purpose: Keep workflows portable across frontier and smaller models, tool environments, and future hosts without weakening invariant controls.

Activate when: an implementation targets models with different capabilities.

Do not use when: the host and task profile are fixed; capability cannot be tested and no conservative fallback exists.

Requires: none.

## Runtime mechanism

Probe real host affordances—context, tools, state persistence, structured outputs, reliability evidence, and execution permissions—then combine them with task risk to choose a named light, standard, or heavy scaffold profile. Use model-size drift scaling as one capability signal, never as the selector itself; capability claims must be observed or declared, and truth, safety, state, and integrity invariants remain mandatory in every profile.

## Procedure

1. Declare the task's risk, state, tool, and validation requirements.
2. Probe or read the host's actual capabilities and permissions without assuming hidden persistence or tools.
3. Map capability and risk to a predeclared operating profile with explicit enabled and omitted controls.
4. Run a readiness check and select a conservative fallback when any required affordance is absent.
5. Monitor failures that invalidate the profile and switch modes at a checkpoint.

## Guardrails

- Mandatory even on strong models: risk overlay; real capability check; invariant preservation.
- Conflict/precedence: Task-risk requirements override host convenience; Absent required capability routes to fallback or blocked, never simulated capability.
- Stop or fail when: capability hallucination; model-brand heuristics.

Full package and provenance: [`future-proof-mode-selector`](../../upgradeables/meta-control/future-proof-mode-selector/UPGRADEABLE.md).
