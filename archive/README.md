# Historical Archive

The files under `source/` are immutable recovery/source artifacts copied from the
user's canonical corpus. Operational registry entries may normalize names into
slugs, but historical names and registry-generation boundaries remain preserved.

Unknown expansions and unrecovered family members are intentionally not guessed.
A modern equivalence is a traceability decision, never a retroactive rename. Use
`SOURCE_TO_REGISTRY_MAP.md` to audit dispositions and `registry/unresolved/` for
structured gaps. The archive remains authoritative for what was recovered even as
operational packages evolve.

`build-spec/` preserves repository-build handoffs separately from the source
corpus because they govern construction rather than historical content. Every
archived file is covered by [`SOURCE_SHA256SUMS`](SOURCE_SHA256SUMS).
