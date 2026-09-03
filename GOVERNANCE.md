# Governance

Upgradeables uses lightweight maintainer-led governance. Anyone may propose a
change; canonical registry changes require review. Review prioritizes explicit
mechanisms, tests, source provenance, interoperability, and non-duplication.

Stable IDs are never reassigned. Historical provenance cannot be silently
rewritten, and unresolved history may be resolved only through evidence-backed
proposals. Deprecation preserves discoverable lineage. Provider adapters evolve
separately from the model-agnostic specification. Host safety always has higher
authority.

`core` status is rare and requires broad demonstrated utility. Maintainers may
reject a new primitive when a mode, recipe, bundle, reference, or composition
already expresses it. Project naming or trademark governance may be introduced
separately if an ecosystem develops; this document creates no trademark policy.

Contributors propose a slug but do not allocate a canonical ID. Maintainers assign
the ID and registry generation when accepting a proposal, after collision and
provenance review. Deprecation requires a retained record, reason, replacement or
explicit lack of replacement, `superseded_by`/alias metadata, migration note, and
a release-note entry. Emergency security fixes may merge before normal review but
receive retrospective provenance and validation.
