# Domain / Mode Isolation (`domain-mode-isolation@1.1.0`)

Purpose: Prevent cross-domain contamination while permitting explicit, reviewed transfers of shared facts.

Activate when: multiple domains or semantic modes coexist.

Do not use when: the task is genuinely single-domain; the supposed domains share identical authority and semantics.

Requires: none.

## Runtime mechanism

Create a named compartment for each active domain with its own instructions, terms, sources, permissions, and state. Route new material into the matching compartment; make cross-domain transfer an explicit projection with provenance, and validate the final output against the selected domain rather than the union of all modes.

## Procedure

1. Classify the task and enumerate domains that are actually needed.
2. Create separate domain scopes for instructions, sources, vocabulary, and mutable state.
3. Load only the selected scope into each domain operation.
4. Transfer shared facts through an explicit provenance-bearing bridge.
5. On transition, unload or deactivate the old domain scope and validate for leakage.

## Guardrails

- Mandatory even on strong models: active-domain marker; authority separation; explicit transfer boundary.
- Conflict/precedence: System and task authority outrank domain-local preferences; When a fact must cross domains, transfer the fact and provenance, not the source domain's behavioral rules.
- Stop or fail when: Pause when the domain is ambiguous and different classifications change safety or authority; Do not claim isolation if the host cannot control context or tool exposure; emulate with explicit labels and validation.

Full package and provenance: [`domain-mode-isolation`](../../upgradeables/state/domain-mode-isolation/UPGRADEABLE.md).
