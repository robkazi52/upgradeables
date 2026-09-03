# Authoring Bundle

A curated composition, not an always-on monolith. Activate components only
when their individual triggers apply and preserve repository precedence.

## Components and default load order

- [`style-alignment`](../../upgradeables/output/style-alignment/UPGRADEABLE.md)
- [`pedagogical-alignment`](../../upgradeables/output/pedagogical-alignment/UPGRADEABLE.md)
- [`safe-rewrite`](../../upgradeables/editing-repair/safe-rewrite/UPGRADEABLE.md)
- [`citation-fidelity`](../../upgradeables/validation/citation-fidelity/UPGRADEABLE.md)
- [`placeholder-suppression`](../../upgradeables/output/placeholder-suppression/UPGRADEABLE.md)

## Composition boundary

Remove redundant or inactive controls. Validators do not add facts. Any state,
persistence, or parallel execution must be backed by a real host mechanism.
