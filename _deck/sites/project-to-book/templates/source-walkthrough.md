# {{MODULE_NAME}} Source Walkthrough

## Architecture Overview

| File | Lines | Responsibility |
|------|-------|----------------|
| {{FILE_1}} | {{LINES_1}} | {{PURPOSE_1}} |
| {{FILE_2}} | {{LINES_2}} | {{PURPOSE_2}} |

## Core Data Structures

```{{LANGUAGE}}
// {{FILE}}:{{START_LINE}}-{{END_LINE}}
{{STRUCT_DEFINITION}}
```

**Fields Explanation**:
- `{{FIELD_1}}`: [What it stores, why it exists]
- `{{FIELD_2}}`: [What it stores, why it exists]

## {{FEATURE_1_NAME}}

### Entry Point

```{{LANGUAGE}}
// {{FILE}}:{{LINE}}
func {{FUNCTION_NAME}}(params) ReturnType {
    // ...
}
```

### Call Chain

```
{{FUNCTION_A}}()
  └─ {{FUNCTION_B}}()
       └─ {{FUNCTION_C}}()
```

### Key Code

```{{LANGUAGE}}
// {{FILE}}:{{START}}-{{END}}
{{KEY_CODE_SNIPPET}}
```

**Why this design**: [Explanation of trade-offs and decisions]

## {{FEATURE_2_NAME}}

...

## Design Decisions Summary

| Decision | Reason | Trade-off |
|----------|--------|-----------|
| {{DECISION_1}} | {{REASON_1}} | {{TRADEOFF_1}} |
| {{DECISION_2}} | {{REASON_2}} | {{TRADEOFF_2}} |
