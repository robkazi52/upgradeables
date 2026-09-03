# Basic composition example

**Situation:** many downstream modules consume locked decisions.

**Composition:** establish a task lock, activate `drift-immunity-propagation`, preserve
explicit state and evidence boundaries, then pass the result through the
workflow's applicable validator.

**Expected:** the component performs only its documented purpose and reports
uncertainty or failure instead of manufacturing missing support.
