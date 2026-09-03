# Skill Recipe Index

Recipes classify component defaults as required (R), automatically recommended
(A), conditional (C), optional (O), or normally excluded (X).

- `R`: mandatory once this recipe is selected; otherwise reject the recipe and
  document a different route.
- `A`, `C`, and `O`: include only when the component's trigger applies.
- `X`: exclude unless a task-specific reason justifies it.

Recipes are starting points, not always-on stacks. `R` is structurally required
but can remain dormant until its phase trigger. For normal execution, use one
compact file in [`runtime/recipes/`](../runtime/recipes/) or run
`python scripts/query_registry.py --recipe <recipe-slug> --runtime`. The
`resolved/` and source files are deeper review and contribution views.

- [Research Skill](resolved/research-skill.md)
- [Source-Grounded Analysis](resolved/source-grounded-analysis.md)
- [High-Stakes Reasoning](resolved/high-stakes-reasoning.md)
- [Medical Evidence](resolved/medical-evidence.md)
- [Legal Evidence](resolved/legal-evidence.md)
- [Coding / Debugging](resolved/coding-debugging.md)
- [Code / Pull Request Review](resolved/code-review.md)
- [Long-Context / Corpus](resolved/long-context-corpus.md)
- [Authoring](resolved/authoring.md)
- [Creative Ideation](resolved/creative-ideation.md)
- [Education / Explanation](resolved/education-explanation.md)
- [Decision Support](resolved/decision-support.md)
- [Architecture / Skill Building](resolved/architecture-skill-building.md)
- [Multi-Agent / Orchestration](resolved/multi-agent-orchestration.md)
- [Deterministic Intake / Routing](resolved/deterministic-intake-routing.md)
- [Long-Context Source Fidelity](resolved/long-context-source-fidelity.md)
- [Perception & Spatial Reasoning](resolved/perception-reasoning.md)
