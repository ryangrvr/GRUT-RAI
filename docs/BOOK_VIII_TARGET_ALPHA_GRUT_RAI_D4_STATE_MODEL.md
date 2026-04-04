# Book VIII — Target Alpha: GRUT-RAI D4 State Model

## Machine-Readable State Model for D4-Under-M4 Reasoning

---

## 1. Entity Types

| Entity | Description | Source |
|--------|-------------|--------|
| `proto_cell` | Self-limiting reproducing compartment with M4-conditional metabolism | Book IV–VII |
| `daughter` | Post-fission proto-cell inheriting a content subset | Book IV Psi |
| `hic_scaffold` | Fixed-site energy-transduction scaffold (concerted mode) | Book V Delta |
| `carrier` | K=2-scale diffusible proto-currency (loaded/unloaded) | Book VII Beta |
| `functional_cluster` | Spatially correlated group of templates + catalysts + HICs | Book VI Alpha (Route D) |
| `boundary_mesh` | K=6/K=7 cross-linked compartment shell | Book IV Tau |
| `fission_plane` | Mechanical rupture site at boundary weak-point | Book IV Psi |

---

## 2. Division-Control State Variables

| Variable | Type | Domain | Description |
|----------|------|--------|-------------|
| `d_level_unconditional` | enum | {D0, D1, D2, D3, D4, D5} | Current unconditional division level |
| `d_level_conditional` | enum | {NONE, D3_PLUS, D4_CONDITIONAL} | Division level under M4 backing |
| `nonviable_rate_d3` | float | [0.0, 1.0] | Estimated nonviable-daughter fraction at D3 |
| `nonviable_rate_d4_cond` | float | [0.0, 1.0] | Estimated nonviable-daughter fraction at D4-conditional |
| `division_timing_cv` | float | [0.0, 1.0] | Coefficient of variation of time-to-division |
| `content_quality_at_fission` | float | [0.0, 1.0] | Fraction of non-degraded catalysts at division |
| `boundary_coverage_directed` | float | [0.0, 1.0] | Fraction of boundary receiving directed maintenance |
| `post_fission_recovery_available` | bool | — | Whether carrier-driven recovery exists for daughters |
| `partition_bias_active` | bool | — | Whether spatial-cluster partition bias (Route D) is active |
| `timing_bias_active` | bool | — | Whether content-load-responsive timing (Route A) is active |
| `quality_filter_active` | bool | — | Whether P2-mediated quality bias (Route C) is active |

---

## 3. M4-Backing Fields

| Variable | Type | Domain | Description |
|----------|------|--------|-------------|
| `m_level_conditional` | enum | {M3, M4_CONDITIONAL} | Current conditional metabolic level |
| `m_level_unconditional` | enum | {M2, M3} | Unconditional metabolic floor |
| `carrier_committed` | bool | — | Whether carrier bridge is provisionally committed |
| `dg_barrier_regime` | enum | {WEAK, MARGINAL, ROBUST} | Current carrier barrier regime |
| `dg_barrier_kT` | float | [0, ∞) | Carrier conformational barrier in kT units |
| `eta_carrier` | float | [0.0, 1.0] | Carrier utilization efficiency |
| `directed_fraction` | float | [0.0, 1.0] | Combined directed energetic fraction |
| `carrier_processes` | list[str] | — | Processes receiving carrier support (P1, P2, P3, P4) |

---

## 4. Daughter-State Fields

| Variable | Type | Domain | Description |
|----------|------|--------|-------------|
| `daughter_hic_count` | int | [0, N_hic_parent] | Number of HICs inherited by daughter |
| `daughter_functional_completeness` | float | [0.0, 1.0] | Fraction of essential functional types present |
| `daughter_carrier_flux` | float | [0, ∞) | Carrier events per cycle available to daughter |
| `daughter_recovery_feasible` | bool | — | Whether daughter can recover via carrier-driven repair |
| `daughter_deficit_depth` | enum | {NONE, MARGINAL, DEEP} | Severity of partition deficit |
| `daughter_viability` | enum | {VIABLE, MARGINAL_RECOVERABLE, MARGINAL_NONRECOVERABLE, NONVIABLE} | Post-fission viability classification |

---

## 5. Transition Rules

### 5.1 D-Level Determination

```
IF m_level_conditional == M4_CONDITIONAL
   AND dg_barrier_regime == ROBUST
   AND carrier_committed == true:
   d_level_conditional = D4_CONDITIONAL
   nonviable_rate = nonviable_rate_d4_cond  // ~0.01–0.03
   boundary_coverage_directed = 0.70–0.90
   post_fission_recovery_available = true
ELSE:
   d_level_conditional = NONE
   nonviable_rate = nonviable_rate_d3  // ~0.03–0.08
   boundary_coverage_directed = 0.20–0.30
   post_fission_recovery_available = false

d_level_unconditional = D3  // always, regardless of M4 status
```

### 5.2 Daughter Viability Classification

```
AFTER fission:
   IF daughter_functional_completeness >= 0.95
      AND daughter_hic_count >= 3:
      daughter_viability = VIABLE
   ELIF daughter_functional_completeness >= 0.80
      AND daughter_hic_count >= 3
      AND post_fission_recovery_available == true:
      daughter_deficit_depth = MARGINAL
      daughter_viability = MARGINAL_RECOVERABLE
   ELIF daughter_functional_completeness >= 0.80
      AND (daughter_hic_count < 3 OR post_fission_recovery_available == false):
      daughter_deficit_depth = MARGINAL
      daughter_viability = MARGINAL_NONRECOVERABLE
   ELSE:
      daughter_deficit_depth = DEEP
      daughter_viability = NONVIABLE
```

### 5.3 Post-Fission Recovery

```
IF daughter_viability == MARGINAL_RECOVERABLE:
   recovery_events = daughter_hic_count * carrier_cycle_rate * eta_carrier
   missing_objects = (1.0 - daughter_functional_completeness) * N_essential
   IF recovery_events >= missing_objects:
      daughter_viability -> VIABLE  // after recovery period
   ELSE:
      daughter_viability -> MARGINAL_NONRECOVERABLE  // insufficient carrier flux
```

### 5.4 Fallback to M3

```
IF dg_barrier_kT < 23:
   dg_barrier_regime = WEAK
   m_level_conditional = M3  // carrier non-functional
   d_level_conditional = NONE
   post_fission_recovery_available = false
   boundary_coverage_directed = 0.20–0.30  // local P3 only
   nonviable_rate = nonviable_rate_d3
```

---

## 6. Fallback-Condition Fields

| Condition | Threshold | Effect on D-level |
|-----------|-----------|------------------|
| ΔG_barrier < 23 kT | Carrier non-functional | D4-conditional → D3 (full revert) |
| ΔG_barrier 23–28 kT | Carrier marginal (η = 0.1–0.6) | D4-conditional → D3+ (partial gains) |
| ΔG_barrier ≥ 28 kT | Carrier robust (η > 0.95) | D4-conditional justified |
| Daughter inherits < 3 HICs | Recovery infeasible | That daughter: D3-level viability |
| Carrier congestion (unlikely) | > 300 carriers in proto-cell | Not reached in current scaffold |

---

## 7. Uncertainty / Fragility Fields

| Variable | Type | Value | Source |
|----------|------|-------|--------|
| `dg_barrier_derived` | bool | false | Not determined from first principles |
| `dg_barrier_plausible_range` | str | "25–40 kT" | Structural estimate for K=2 covalent composites |
| `d4_fragility` | enum | MODERATE | Sharp lower boundary at 28 kT; no upper limit |
| `d4_to_d3_transition` | enum | SHARP | Binary: works (≥28 kT) or doesn't (<23 kT) |
| `nonviable_rate_uncertainty` | str | "±1–2% absolute" | Stochastic partition + parameter sensitivity |
| `recovery_fraction_uncertainty` | str | "±30% relative" | Depends on HIC inheritance and carrier flux |
| `boundary_coverage_uncertainty` | str | "±15% relative" | Depends on carrier-discharge-pocket distribution |

---

## 8. Verdict Fields

| Field | Value | Authority |
|-------|-------|----------|
| `d4_conditional_justified` | `CONDITIONAL` | Book VIII Alpha |
| `d4_unconditional_justified` | `NO` | Book VIII Alpha |
| `d5_inheritance_robust_justified` | `NO` | Book VIII Alpha |
| `d4_rests_on` | `["family_C_boundary_conditioning", "family_D_post_fission_recovery"]` | Book VIII Alpha |
| `d4_strengthened_d3` | `["family_A_timing", "family_B_repair", "family_E_partition"]` | Book VIII Alpha |
| `book_viii_alpha_changes_state` | `YES` | D4-conditional verified (was projected) |
| `new_cost` | `0` | Twenty-fourth zero-cost target |
| `global_verdict` | `B` | M4 conditionally upgrades to D4-cond; unconditional D4 absent |

---

## 9. Minimal Serialized Example

```json
{
  "program_phase": "BOOK_VIII_ALPHA",
  "stage": "regulated_division_reassessment_under_M4",

  "d_level": {
    "unconditional": "D3",
    "conditional": "D4_CONDITIONAL",
    "d4_justified": "CONDITIONAL",
    "d4_unconditional": false,
    "d5_justified": false,
    "nonviable_rate_d3": "0.03-0.08",
    "nonviable_rate_d4_cond": "0.01-0.03"
  },

  "m4_backing": {
    "m_level_conditional": "M4_CONDITIONAL",
    "m_level_unconditional": "M3",
    "carrier_committed": true,
    "dg_barrier_regime": "ROBUST",
    "dg_barrier_required_kT": 28,
    "eta_carrier_robust": 0.95,
    "directed_fraction_m4": "0.30-0.34"
  },

  "division_control": {
    "routes_d3": ["A_timing", "C_quality", "D_partition"],
    "families_d4_qualifying": ["C_boundary_conditioning", "D_post_fission_recovery"],
    "families_strengthened_d3": ["A_timing_sharpened", "B_repair_before_fission", "E_partition_reliability"],
    "families_disqualified": ["F_pseudo_upgrade"],
    "timing_bias_active": true,
    "quality_filter_active": true,
    "partition_bias_active": true,
    "boundary_conditioning_active": true,
    "post_fission_recovery_active": true,
    "boundary_coverage_directed": "0.70-0.90",
    "division_timing_cv_reduction": "0.15-0.25"
  },

  "daughter_model": {
    "viability_classes": [
      {"class": "VIABLE", "frequency": "0.90-0.95", "criterion": "completeness >= 0.95, HICs >= 3"},
      {"class": "MARGINAL_RECOVERABLE", "frequency": "0.03-0.06", "criterion": "completeness 0.80-0.95, HICs >= 3, carrier active"},
      {"class": "MARGINAL_NONRECOVERABLE", "frequency": "0.01-0.02", "criterion": "completeness 0.80-0.95, HICs < 3 or no carrier"},
      {"class": "NONVIABLE", "frequency": "0.01-0.02", "criterion": "completeness < 0.80"}
    ],
    "net_nonviable_d4": "0.01-0.03",
    "net_nonviable_d3_fallback": "0.03-0.08"
  },

  "fragility": {
    "dg_barrier_derived": false,
    "d4_fragility": "MODERATE",
    "d4_to_d3_transition": "SHARP",
    "fallback_regime": "D3_unconditional"
  },

  "cost": {
    "total_postulates": 15,
    "total_parameters": 9,
    "total_fields": 1,
    "total_dof": 6,
    "book_viii_alpha_added": {"postulates": 0, "parameters": 0, "fields": 0, "dof": 0},
    "zero_cost_targets": 24
  },

  "verdict": {
    "global": "B",
    "d4_conditional": "JUSTIFIED_CONDITIONAL",
    "d4_unconditional": "NOT_JUSTIFIED",
    "d5_inheritance_robust": "NOT_JUSTIFIED",
    "state_change": true,
    "next_audit": "book_viii_beta_lineage_robustness_reassessment_under_M4"
  }
}
```

---

## 10. Integration Notes

### 10.1 What GRUT-RAI Must Update from Book VIII Alpha

1. **D-level dual state formalized:** D3 unconditional / D4-conditional. Use D4-conditional for M4-regime reasoning; use D3 for fallback/unconditional reasoning.
2. **D4-conditional verified, not merely projected.** Book VII Gamma §8 projected D4-conditional. Book VIII Alpha verified it through dedicated audit with route-by-route analysis, hard-criteria evaluation, and false-positive screening.
3. **Two genuinely new capabilities:** Full-boundary conditioning (Family C) and post-fission recovery (Family D). These are M4-dependent and absent at D3.
4. **Daughter viability model:** Four-class classification (viable, marginal-recoverable, marginal-nonrecoverable, nonviable). Use for lineage modeling in Book VIII Beta.
5. **Nonviable rate updated:** D3 = ~3–8%; D4-conditional = ~1–3%.
6. **Zero-cost target count:** 24 (incremented by 1).

### 10.2 What GRUT-RAI Must NOT Update

- No change to total cost (15/9/1/6)
- No change to carrier commitment status (still provisional)
- No change to M-level (still M4-conditional / M3-unconditional)
- No promotion to unconditional D4
- No promotion to D5 / inheritance robustness
- No change to L-level or A-level (those are Book VIII Beta and Gamma)

---

*GRUT-RAI D4 State Model complete. Entity types, state variables, transition rules, fallback conditions, fragility fields, verdict fields, and minimal serialized example provided. D4-conditional verified; D3 retained as unconditional floor.*
