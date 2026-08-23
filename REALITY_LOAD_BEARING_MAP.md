# Reality Load-Bearing Map

The audit's most valuable output (charter §8.3). **Blast radii are sets with overlaps, never addable integers.**
Edge-graph only; prose graph (~0.78x additional) not machine-extracted.

## The chain (corrected arithmetic)

**One nested chain carries 28 of 71 nodes (39% of the register):**

```
background_time_translation_flow -> rung1_inin_action -> rung2_kms_gate -> ...
```

Root: `background_time_translation_flow` — booked 2026-08-18 as an OMISSION, tier `assumed`, Δ+1,
sub_status: *"NOT a physics claim about de Sitter."*

| node | reach | subset of root? | overlap with root | verdict |
|---|---|---|---|---|
| background_time_translation_flow | 28 | YES | 28 | UNRESOLVED-BLOCKED |
| rung1_inin_action | 27 | YES | 27 | HOLDS-NARROWER |
| rung2_kms_gate | 20 | YES | 20 | UNRESOLVED-BLOCKED |

**UNION of the three: 28. Do NOT sum the reach column.**

## Top 15 by individual blast radius (for reference only; NOT additive)

| rank | id | tier | verdict | downstream |
|---|---|---|---|---|
| 1 | background_time_translation_flow | assumed | UNRESOLVED-BLOCKED | 28 |
| 2 | rung1_inin_action | shown | HOLDS-NARROWER | 27 |
| 3 | rung2_kms_gate | shown | UNRESOLVED-BLOCKED | 20 |
| 4 | rung3_single_pole | derived-pending | HOLDS-NARROWER | 9 |
| 5 | rung9a_value | shown | UNRESOLVED-BLOCKED | 9 |
| 6 | p_tt_ansatz | assumed | HOLDS-NARROWER | 5 |
| 7 | entropy_area_unruh | assumed | UNRESOLVED-BLOCKED | 5 |
| 8 | rung5_gr_limit | assumed | NULL-ASSERTED | 4 |
| 9 | rung4_love_kk | shown | HOLDS-NARROWER | 3 |
| 10 | born_rule | assumed | NULL-ASSERTED | 3 |
| 11 | eft_operator_basis | to-derive | UNRESOLVED-BLOCKED | 3 |
| 12 | vc_universal_metric_coupling | postulate | UNRESOLVED-BLOCKED | 3 |
| 13 | rung6_qm_limit | assumed | UNRESOLVED-BLOCKED | 2 |
| 14 | rung7_wz | to-derive | UNRESOLVED-BLOCKED | 2 |
| 15 | mu_linear | derived-pending | UNRESOLVED-BLOCKED | 2 |