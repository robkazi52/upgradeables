# Basic composition example

**Situation:** a workflow pauses, hands off, or persists.

**Composition:** establish a task lock, activate `state-snapshot`, preserve
explicit state and evidence boundaries, then pass the result through the
workflow's applicable validator.

**Expected:** the component performs only its documented purpose and reports
uncertainty or failure instead of manufacturing missing support.
