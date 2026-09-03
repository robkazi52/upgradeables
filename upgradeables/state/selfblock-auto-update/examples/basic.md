# Basic composition example

**Situation:** the host can update explicit state after steps.

**Composition:** establish a task lock, activate `selfblock-auto-update`, preserve
explicit state and evidence boundaries, then pass the result through the
workflow's applicable validator.

**Expected:** the component performs only its documented purpose and reports
uncertainty or failure instead of manufacturing missing support.
