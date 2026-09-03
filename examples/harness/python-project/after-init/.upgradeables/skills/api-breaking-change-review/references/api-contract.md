# Synthetic API contract

This reference belongs only to the synthetic example and test fixture.

- Package: `example-api`
- Supported series: `1.x`
- Public function: `greet(name: str, punctuation: str = "!") -> str`
- Compatibility promise: existing valid calls in the supported series keep the same
  positional parameters, defaults, return type, and documented exceptions.
- A removal, rename, new required argument, changed default, or changed return type
  requires a major version and migration note.
