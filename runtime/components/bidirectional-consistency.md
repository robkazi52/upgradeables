# Bidirectional Consistency (`bidirectional-consistency@1.1.0`)

Purpose: Expose lossy, non-invertible, or spuriously plausible transformations that one-way review misses.

Activate when: causal, logical, quantitative, or evidence claims are central.

Do not use when: the transformation is intentionally irreversible and no reverse contract is claimed; creative output has no declared source mapping.

Requires: none.

## Runtime mechanism

Run a forward check from source conditions to proposed result, then independently read the result backward to enumerate which source conditions it actually entails. Compare the reconstructed set with the locked source atoms; missing, invented, or many-to-one-collapsed atoms fail even when the forward narrative is fluent.

## Procedure

1. Lock the source atoms and declared transformation contract.
2. Verify that each source atom has a forward image in the result.
3. Hide the source and reconstruct its implied atoms from the result alone.
4. Compare reconstructed atoms with the locked set.
5. Classify omissions, inventions, and ambiguity introduced by the mapping.

## Guardrails

- Mandatory even on strong models: independent backward reconstruction for lossy or high-stakes transformations.
- Conflict/precedence: The declared transformation contract determines which information may be lost; A reverse contradiction on a locked atom overrides stylistic forward plausibility.
- Stop or fail when: Do not certify when a material source constraint has no forward image or when the result implies a contradictory source condition.

Full package and provenance: [`bidirectional-consistency`](../../upgradeables/validation/bidirectional-consistency/UPGRADEABLE.md).
