# Versioning Specification

The repository and each operational package use Semantic Versioning where
practical. Cosmetic corrections are patch changes; compatible procedure or
metadata improvements are minor; contract-breaking behavior changes are major.
Identity changes normally create a migration and alias.

Historical IDs are immutable provenance keys scoped to their registry generation.
Modern slugs must not be recycled for unrelated concepts. Deprecation retains the
record, aliases, replacement, and migration guidance.
