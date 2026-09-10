# OBJECT_REGISTRY_QA_01 (lab-only quality audit)

Commit: `0cf4a9a76faab2e4ed1fb819938ef1dbd4aa9121`

## 1. Category assignment
- potentially multi-object records: **187** of 2370

Combinations (context contains >1 category's terminology):
- projection_P + slow_variable_coarse_graining: 41
- slow_variable_coarse_graining + system_bath_partition: 28
- response_object + slow_variable_coarse_graining: 25
- cutoff_separation_scale + gauge_field_redefinition: 22
- gauge_field_redefinition + projection_P: 13
- cutoff_separation_scale + slow_variable_coarse_graining: 10
- projection_P + response_object: 6
- inner_product_state + response_object: 5
- gauge_field_redefinition + system_bath_partition: 4
- cutoff_separation_scale + projection_P: 4
- cutoff_separation_scale + system_bath_partition: 4
- inner_product_state + response_object + slow_variable_coarse_graining: 4
- cutoff_separation_scale + gauge_field_redefinition + projection_P + system_bath_partition: 4
- inner_product_state + slow_variable_coarse_graining: 3
- cutoff_separation_scale + inner_product_state + projection_P + slow_variable_coarse_graining + system_bath_partition: 3
- cutoff_separation_scale + gauge_field_redefinition + inner_product_state: 3
- cutoff_separation_scale + gauge_field_redefinition + inner_product_state + projection_P + slow_variable_coarse_graining + system_bath_partition: 2
- gauge_field_redefinition + response_object: 2
- cutoff_separation_scale + inner_product_state + slow_variable_coarse_graining: 1
- cutoff_separation_scale + inner_product_state: 1
- inner_product_state + system_bath_partition: 1
- cutoff_separation_scale + inner_product_state + system_bath_partition: 1

Examples (first 20, exact locations preserved):
- PHYSICS_LEDGER/ROOT1_KERNEL_ORIGIN.md:169 — assigned gauge_field_redefinition, also contains ['gauge_field_redefinition', 'system_bath_partition']
- PHYSICS_LEDGER/ROOT1_KERNEL_ORIGIN.md:170 — assigned system_bath_partition, also contains ['gauge_field_redefinition', 'system_bath_partition']
- PHYSICS_LEDGER/WALL_A_SESSION_BOUNDARY.md:27 — assigned projection_P, also contains ['gauge_field_redefinition', 'projection_P']
- PHYSICS_LEDGER/WALL_A_SESSION_BOUNDARY.md:27 — assigned gauge_field_redefinition, also contains ['gauge_field_redefinition', 'projection_P']
- PHYSICS_LEDGER/WALL_KR_D4_DUAL_GAUGE_RESULT.json:140 — assigned projection_P, also contains ['gauge_field_redefinition', 'projection_P']
- PHYSICS_LEDGER/WALL_KR_D4_DUAL_GAUGE_RESULT.json:140 — assigned gauge_field_redefinition, also contains ['gauge_field_redefinition', 'projection_P']
- PHYSICS_LEDGER/WALL_KR_D4_KTERM_COMPLETION_RESULT.json:36 — assigned gauge_field_redefinition, also contains ['gauge_field_redefinition', 'projection_P']
- PHYSICS_LEDGER/WALL_KR_D4_KTERM_COMPLETION_RESULT.json:216 — assigned gauge_field_redefinition, also contains ['gauge_field_redefinition', 'projection_P']
- PHYSICS_LEDGER/WALL_KR_D5_EXECUTION_RESULT.json:191 — assigned projection_P, also contains ['cutoff_separation_scale', 'projection_P']
- PHYSICS_LEDGER/WALL_KR_D5_EXECUTION_RESULT.json:191 — assigned cutoff_separation_scale, also contains ['cutoff_separation_scale', 'projection_P']
- PHYSICS_LEDGER/WALL_KR_FOUNDATIONAL_LADDER_RESULT.json:45 — assigned system_bath_partition, also contains ['slow_variable_coarse_graining', 'system_bath_partition']
- PHYSICS_LEDGER/WALL_KR_FOUNDATIONAL_LADDER_RESULT.json:46 — assigned slow_variable_coarse_graining, also contains ['slow_variable_coarse_graining', 'system_bath_partition']
- PHYSICS_LEDGER/WALL_KR_INDEPENDENCE_AUDIT_RESULT.json:53 — assigned system_bath_partition, also contains ['slow_variable_coarse_graining', 'system_bath_partition']
- PHYSICS_LEDGER/WALL_KR_INDEPENDENCE_AUDIT_RESULT.json:54 — assigned slow_variable_coarse_graining, also contains ['slow_variable_coarse_graining', 'system_bath_partition']
- PHYSICS_LEDGER/WALL_KR_U3_AQFT_RECONCILIATION.md:82 — assigned slow_variable_coarse_graining, also contains ['projection_P', 'slow_variable_coarse_graining']
- PHYSICS_LEDGER/WALL_KR_U3_AQFT_RECONCILIATION.md:82 — assigned projection_P, also contains ['projection_P', 'slow_variable_coarse_graining']
- PHYSICS_LEDGER/WALL_KR_U3_AQFT_RECONCILIATION.md:85 — assigned slow_variable_coarse_graining, also contains ['cutoff_separation_scale', 'slow_variable_coarse_graining']
- PHYSICS_LEDGER/WALL_KR_U3_AQFT_RECONCILIATION.md:85 — assigned cutoff_separation_scale, also contains ['cutoff_separation_scale', 'slow_variable_coarse_graining']
- PHYSICS_LEDGER/WALL_KR_U3_AQFT_RECONCILIATION.md:119 — assigned projection_P, also contains ['projection_P', 'slow_variable_coarse_graining']
- PHYSICS_LEDGER/WALL_KR_U3_AQFT_RECONCILIATION.md:120 — assigned slow_variable_coarse_graining, also contains ['projection_P', 'slow_variable_coarse_graining']

## 2. Contradiction flags (flagged, NOT resolved)

### PHYSICS_LEDGER/wall_a_assembly2.py:830 (gauge / field-redefinition freedom)
- flagged pair: gauge-invariant / gauge-dependent
- context: "artifacts -- no gauge-fixing term was ever added to the h-action, so the bare "         "off-shell kernel can carry gauge-dependent pole pieces outside the "         "gauge-invariant basis; (b) on-shell/TT projection may be REQUIRED before "
- same object?: UNRESOLVED
- actually contradictory: UNRESOLVED (not adjudicated; requires conceptual judgment)

### PHYSICS_LEDGER/wall_a_assembly2.py:831 (gauge / field-redefinition freedom)
- flagged pair: gauge-invariant / gauge-dependent
- context: "off-shell kernel can carry gauge-dependent pole pieces outside the "         "gauge-invariant basis; (b) on-shell/TT projection may be REQUIRED before "         "basis closure is meaningful; (c) genuine new counterterm structure (would "
- same object?: UNRESOLVED
- actually contradictory: UNRESOLVED (not adjudicated; requires conceptual judgment)

### calc/delta4_stability.py:11 (gauge / field-redefinition freedom)
- flagged pair: gauge-invariant / gauge-dependent
- context: the anomaly-induced sector is ill-defined at late times and the α leg is unanchored in a dS universe. If it is confined to the gauge-dependent σ and cancels in observables, α anchors. This calc isolates WHICH stress terms can inherit the growth, carrying Q². It does NOT decide the gauge-invariant an
- same object?: UNRESOLVED
- actually contradictory: UNRESOLVED (not adjudicated; requires conceptual judgment)

### calc/delta4_stability.py:12 (gauge / field-redefinition freedom)
- flagged pair: gauge-invariant / gauge-dependent
- context: If it is confined to the gauge-dependent σ and cancels in observables, α anchors. This calc isolates WHICH stress terms can inherit the growth, carrying Q². It does NOT decide the gauge-invariant answer (that is the literature/specialist piece) — it locates the danger. Units H=1. Pure stdlib.
- same object?: UNRESOLVED
- actually contradictory: UNRESOLVED (not adjudicated; requires conceptual judgment)

## 3. Object-level specification counts

| object | terms | explicit defs | partial | unresolved | NOT-SPECIFIED fields | docs |
|---|---|---|---|---|---|---|
| system/bath partition | 3 | 0 | 24 | 1 | 783 | 42 |
| slow-variable selection / coarse-graining | 3 | 4 | 49 | 8 | 1713 | 44 |
| projection P | 6 | 7 | 76 | 2 | 2940 | 112 |
| inner product / state | 6 | 2 | 16 | 3 | 293 | 14 |
| cutoff / separation scale | 6 | 0 | 312 | 14 | 5217 | 174 |
| gauge / field-redefinition freedom | 3 | 4 | 305 | 49 | 6908 | 179 |
| response-object definition | 8 | 4 | 41 | 10 | 2356 | 79 |

## 4. Information loss / duplication

- duplicate evidence records: 0
- one source line producing records in multiple categories: 139
- cross-object associations lost by one-category assignment: 187
- 'NOT SPECIFIED' overreach risks at registry level: 21

### Evidence-model recommendation
Registry should adopt many-to-many record→category mapping before dependency/equivalence analysis.