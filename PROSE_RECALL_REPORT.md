# Prose Recall Report

Emitted. Precision and recall reported SEPARATELY, never merged.

| metric | value | note |
|---|---|---|
| HIGH-pass edges | 50 | unchanged from v1; precision diagnostic |
| short-form refs (LOW) | 31 | candidate edges only; hand-check owed |
| ontology-term refs (LOW) | 34 | map to R1-ONTOLOGY after validation |
| substring collisions | 0 | v1 result stands |

## Integrity gates

- corpus files scanned: 28
- duplicate ids: none (fails loudly)
- emitted totals equal graph totals: YES (same source)
- high and low counted separately: YES

## Hand-validation status

Stratified sample of LOW-confidence pass NOT yet hand-checked. Until then the LOW counts are
candidates, not dependencies, and must not enter blast radius. Logged as blocker.