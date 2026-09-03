# Model Consumption Guide

This is the execution entrypoint for an LLM or coding agent given the repository.
Read `spec/SKILL_TRANSLATION_SPEC.md`, `spec/PRECEDENCE_SPEC.md`, and
`registry/registry.json`; use `recipes/recipes.json` to select a task-family seed.

## Deterministic selection procedure

1. Write the task identity, activation boundary, output contract, source boundary,
   risk, evidence sensitivity, and state/persistence needs.
2. Select the closest recipe. Start with its R entries, evaluate A entries, include
   C/O only when their own triggers match, and normally exclude X.
3. Select at most one primary Behavior Gene and the minimum authorized Core(s).
4. Read each selected package's metadata. Resolve `requires`; consider
   `recommended_with`; explicitly assess counterbalances, conflicts, and potential
   redundancy. Preserve the precedence specification.
5. Remove every component without an active trigger. Do not turn the recipe into an
   always-on stack.
6. Choose an implementation form for each retained component: instructions, mode,
   validator, state schema/manager, reference, script, orchestrator, or bundle.
7. Copy `templates/SKILL_IMPLEMENTATION_TEMPLATE.md` into the target Skill folder.
   Put deep content in `references/`, deterministic checks in `scripts/`, and only
   necessary output materials in `assets/`.
8. Cite each selected slug and version. State unavailable host capabilities; never
   simulate hidden persistence, private reasoning, or parallel agents as real.
9. Add positive, negative, conflict, unsupported-claim, long-context, composition,
   and strong-model-scaling tests as applicable. Run the repository validators.

## Worked selection

For a source-grounded research Skill, read the `research-skill` recipe. Retain the
required task lock, loader, StateBlock, and grounding controls. Citation Fidelity
activates only when emitting cited claims. Multi-Truth Gating and Critical Atomic
Verification scale with claim importance/risk. Neuro-Focus should be counterbalanced
by Anti-Tunnel Vision when fixation is plausible. The worked output is at
`implementations/community/example-research-skill/SKILL.md`.

## Non-negotiable output contract

Never merge Skills, Behavior Genes, Cores, validators, and Upgradeables into one
prompt type. Never infer unresolved definitions. Treat historical IDs as scoped to
their generation. Translate metaphors into visible mechanisms. A provider adapter
may evolve but cannot redefine the canonical registry.
