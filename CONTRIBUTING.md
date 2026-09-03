# Contributing

Contributions may add primitives, modes, recipes, bundles, tests, documentation,
or model/provider adapters. Search `registry/registry.json` first. A new primitive
must name its closest prior art, explain the material difference, and show why
composition is insufficient.

1. Fork and branch from `main`.
2. Copy the appropriate template from `templates/`.
3. Add or update machine-readable metadata and provenance.
4. Add positive, negative, conflict, and composition tests as applicable.
5. Run every command in README's validation section.
6. Open a pull request using the checklist.

Do not invent missing history, reuse IDs, collapse acronym collisions, claim host
capabilities that are not present, or let a validator add unsupported facts.
By contributing, you agree that your contribution is licensed under Apache-2.0.
