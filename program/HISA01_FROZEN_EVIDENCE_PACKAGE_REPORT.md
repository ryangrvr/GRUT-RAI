# HISA-01 Frozen Adjudication Package — Report

## A. Package identity and source HEAD

- Package: `HISA01_FROZEN_EVIDENCE_PACKAGE.json`
- Source HEAD: `0cf4a9a76faab2e4ed1fb819938ef1dbd4aa9121`
- Built from: `HISA01_HIGH_INFORMATION_MANIFEST.json`, `OBJECT_EVIDENCE_03.json`, `OBJECT_IDENTITY_AUDIT_01.json`, `OBJECT_IDENTITY_AUDIT_02.json`
- Boundary: **construction only**. No adjudication, no referent, no typing, no relation classification, no SAME/DIFFERENT recommendation, no ranking.

## B. Exact number of statements

- **31 / 31** manifest statements present.

## C. Exact provenance coverage

- 31/31 statements carry `source_path` + `source_line` provenance into the lossless `OBJECT_EVIDENCE_03.json` substrate (`evidence_record_ids` chain).
- 31/31 exact source lines mechanically verified against `git show 0cf4a9a76faab2e4ed1fb819938ef1dbd4aa9121:<file>`. Unmatched: 0.

## D. Duplicate handling

- Provenance status distribution: {'UNIQUE': 31}
- No duplicate/provenance copy was promoted to independent evidence; duplicate status carried verbatim from the manifest.

## E. Context-window rules

- Bounded context windows reproduced exactly as stored in OBJECT_EVIDENCE_03 (`contexts` map, key = candidate term). No expansion with repository knowledge. Any expansion would require a separate evidence item.

## F. Statements whose exact evidence cannot be reproduced

- **NONE** (all 31 verified byte-for-byte at HEAD where the file is tracked).

## G. Prior classification potentially contaminated by a known classifier false positive

- Statements carrying a prior audit classification that originates from a lexical-trigger classifier (audit-01: SAME_CONSTRUCTION/RELATED_NOT_IDENTIFIED; audit-02: RELATED_CANDIDATE), i.e. **candidates for contamination**, NOT verdicts: 8 → ['provenance/claims.baseline.json:55', 'provenance/claims.json:79', 'provenance/claims.baseline.json:269', 'provenance/claims.baseline.json:201', 'provenance/claims.json:22', 'provenance/claims.baseline.json:250', 'PHYSICS_LEDGER/WALL_KR_D4_KTERM_COMPLETION_RESULT.json:28', 'PHYSICS_LEDGER/WALL_KR_D4_KTERM_COMPLETION_RESULT.json:210']

## H. Statements carrying contradictory-source / ambiguity flags

- Count: 19 → ['provenance/claims.baseline.json:55', 'provenance/claims.json:79', 'provenance/claims.baseline.json:269', 'program/CANDIDATE_MINING_02.md:274', 'program/CANDIDATE_MINING_02.md:275', 'provenance/claims.json:22', 'calc/mz_inheritance.py:18', 'provenance/claims.baseline.json:180', 'PHYSICS_LEDGER/WALL_KR_D4_KTERM_COMPLETION_RESULT.json:36', 'PHYSICS_LEDGER/WALL_KR_D4_KTERM_COMPLETION_RESULT.json:216', 'program/CANDIDATE_MINING_02.md:223', 'provenance/claims.baseline.json:639', 'PHYSICS_LEDGER/WALL_A_A4_RESULT.json:28', 'calc/mz_inheritance.py:513', 'provenance/claims.baseline.json:250', 'PHYSICS_LEDGER/WALL_KR_D4_KTERM_COMPLETION_RESULT.json:28', 'PHYSICS_LEDGER/WALL_KR_D4_KTERM_COMPLETION_RESULT.json:210', 'PHYSICS_LEDGER/WALL_KR_U3_SPECIFICATION.md:76', 'calc/mz_inheritance.py:530']
- Flags are carried verbatim from the prior audits; nothing was resolved.

## I. SHA-256 hashes of the frozen package files

```
a0fd00c03b16e9a232ffe4fd19b95138e972527fe747ad7f0c34498a834b8343  HISA01_FROZEN_EVIDENCE_PACKAGE.json
```

## Mechanical validation

- v1_count_31: PASS
- v2_every_canonical_id: PASS
- v3_every_provenance: PASS
- v4_exact_line_matches_substrate: PASS
- v5_no_silent_substitution: PASS
- v6_no_duplicate_promoted: PASS
- v7_no_adjudication_fields: PASS
- v8_canonical_files_unmodified: PASS

**VALIDATION OVERALL: PASS**

> Note: `canonical_statement_id` is `NOT SPECIFIED` in the evidence substrate (the manifest field is empty); per policy it was not inferred.
