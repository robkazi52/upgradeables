# No-Unrequested-Scenarios Guard (`counterfactual-silence-scaffold@1.1.0`)

Recovered name: Counterfactual Silence Scaffold

Purpose: Protect factual extraction and reporting tasks from unsolicited counterfactual elaboration.

Activate when: factual output could be contaminated by hypothetical content.

Do not use when: the task explicitly requests scenarios, hypotheses, or counterfactual analysis; creative generation is the primary authorized mode.

Requires: none.

## Runtime mechanism

After a factual-only mode is locked, inspect the candidate for propositions introduced through if, might-have, imagined, alternative-history, or unstated causal premises. Remove those propositions unless they are explicitly reported as source content; preserve ordinary uncertainty statements and supported inference rather than suppressing all modal language.

## Procedure

1. Confirm that the task contract excludes hypothetical reasoning.
2. Identify candidate statements that introduce a non-source counterfactual premise or imagined outcome.
3. Distinguish those statements from source-reported hypotheticals and honest uncertainty.
4. Delete or quarantine unauthorized counterfactual additions.
5. Recheck that the factual answer remains complete and does not fill gaps by implication.

## Guardrails

- Mandatory even on strong models: unauthorized hypothetical premises must not enter factual output.
- Conflict/precedence: An explicit user request for counterfactual analysis deactivates this scaffold and activates counterfactual integrity instead; Source fidelity outranks a blanket silence rule when the source itself discusses a hypothetical.
- Stop or fail when: If factual and counterfactual propositions cannot be distinguished reliably, request review rather than deleting uncertain content wholesale.

Full package and provenance: [`counterfactual-silence-scaffold`](../../upgradeables/truth-grounding/counterfactual-silence-scaffold/UPGRADEABLE.md).
