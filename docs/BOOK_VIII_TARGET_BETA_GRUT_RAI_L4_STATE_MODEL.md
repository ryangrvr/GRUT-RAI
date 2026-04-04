# Book VIII — Target Beta: GRUT-RAI L4 State Model

## Machine-Readable State Model for L4-Under-M4 Reasoning

---

## 1. Entity Types

| Entity | Description | Source |
|--------|-------------|--------|
| `lineage` | Multi-generation descent chain of proto-cells | Book VI Beta |
| `generation` | One division cycle producing two daughters | Book IV Psi |
| `essential_class` | A functional type required for proto-cell viability | Book VI Beta §4 |
| `copy_number` | Pre-division count of an essential class | Book VI Beta §7.1 |
| `partition_event` | Content distribution at fission | Book VI Alpha Route D |
| `recovery_event` | Post-fission carrier-driven repair of under-equipped daughter | Book VIII Alpha Family D |
| `lineage_branch` | A distinct descendant chain within a branching lineage | Book VI Beta §5.2 |

---

## 2. Lineage-Robustness State Variables

| Variable | Type | Domain | Description |
|----------|------|--------|-------------|
| `l_level_unconditional` | enum | {L0, L1, L2, L3, L4, L5} | Current unconditional lineage level |
| `l_level_conditional` | enum | {NONE, L3_PLUS, L4_CONDITIONAL} | Lineage level under M4 backing |
| `p_any_loss_l3` | float | [0.0, 1.0] | Per-gen essential-type loss at L3 |
| `p_any_loss_l4_cond` | float | [0.0, 1.0] | Per-gen essential-type loss at L4-conditional |
| `single_lineage_half_life_l3` | int | [1, ∞) | Generations (non-branching) at L3 |
| `single_lineage_half_life_l4` | int | [1, ∞) | Generations (non-branching) at L4-conditional |
| `individual_daughter_robust` | bool | — | Whether individual daughters are robust without branching |
| `branching_required` | bool | — | Whether lineage persistence depends on branching redundancy |
| `recovery_available` | bool | — | Whether post-fission carrier-driven recovery operates |

---

## 3. M4-Backing Fields

| Variable | Type | Domain | Description |
|----------|------|--------|-------------|
| `m_level_conditional` | enum | {M3, M4_CONDITIONAL} | Conditional metabolic level |
| `d_level_conditional` | enum | {D3, D4_CONDITIONAL} | Conditional division level |
| `carrier_committed` | bool | — | Carrier bridge status |
| `dg_barrier_regime` | enum | {WEAK, MARGINAL, ROBUST} | Carrier barrier regime |
| `directed_fraction` | float | [0.0, 1.0] | Combined directed energetic fraction |
| `carrier_backed_replication` | bool | — | Whether system-wide P1 replication is active |
| `carrier_backed_repair` | bool | — | Whether system-wide P4 repair is active |

---

## 4. Essential-Class Fields

| Variable | Type | Domain | Description |
|----------|------|--------|-------------|
| `n_essential_classes` | int | [1, ∞) | Number of distinct essential functional classes |
| `copy_numbers` | dict[str, int] | class → N | Pre-division copy count per essential class |
| `partition_bias` | float | [0.0, 1.0] | Bias correction from spatial correlation (Route D) |
| `p_loss_per_type` | dict[str, float] | class → p | Per-generation loss probability per essential class |
| `bottleneck_class` | str | — | Essential class with highest p_loss (typically HIC) |
| `bottleneck_N` | int | [1, ∞) | Copy number of bottleneck class |
| `recovery_fraction` | float | [0.0, 1.0] | Fraction of marginal failures rescued by carrier recovery |

---

## 5. Transition Rules

### 5.1 L-Level Determination

```
IF m_level_conditional == M4_CONDITIONAL
   AND d_level_conditional == D4_CONDITIONAL
   AND dg_barrier_regime == ROBUST
   AND carrier_committed == true:

   // Compute M4-backed copy numbers
   FOR EACH class in essential_classes:
      copy_numbers[class] = n_m3[class] * m4_replication_multiplier  // ~1.5-2x

   // Compute per-type loss with M4 parameters
   partition_bias = bias_m4  // ~0.35-0.45
   FOR EACH class in essential_classes:
      p_loss_per_type[class] = (0.5)^copy_numbers[class] * (1 - partition_bias)

   // Apply recovery correction
   p_any_before_recovery = 1 - PRODUCT(1 - p_loss_per_type[class] for class)
   p_any_loss_l4_cond = p_any_before_recovery * (1 - recovery_fraction)

   IF p_any_loss_l4_cond <= 0.015:
      l_level_conditional = L4_CONDITIONAL
      individual_daughter_robust = true
      branching_required = false
   ELIF p_any_loss_l4_cond <= 0.03:
      l_level_conditional = L3_PLUS
      individual_daughter_robust = false
      branching_required = true
   ELSE:
      l_level_conditional = NONE  // still L3

ELSE:
   l_level_conditional = NONE
   p_any_loss = p_any_loss_l3  // ~0.04
   individual_daughter_robust = false
   branching_required = true

l_level_unconditional = L3  // always
```

### 5.2 Lineage Half-Life Computation

```
single_lineage_half_life = CEIL(ln(2) / p_any_loss)

// L3:  ln(2) / 0.04  ≈ 17 generations
// L4-cond (mid): ln(2) / 0.006 ≈ 115 generations
// L4-cond (cons): ln(2) / 0.015 ≈ 46 generations
```

### 5.3 Recovery Application

```
IF recovery_available AND daughter.hic_count >= 3:
   FOR EACH missing_class in daughter.deficit_classes:
      IF daughter has >= 1 copy of missing_class:
         // Carrier-driven amplification from 1 to viable
         daughter.deficit_classes.remove(missing_class)
         daughter.viability -> VIABLE
      ELSE:
         // Complete absence: recovery cannot help
         // (no template to copy from)
         daughter remains NONVIABLE
```

### 5.4 Fallback to M3

```
IF dg_barrier_regime != ROBUST:
   l_level_conditional = NONE
   copy_numbers = n_m3  // revert to L3 steady state
   partition_bias = bias_m3  // ~0.30
   recovery_available = false
   p_any_loss = p_any_loss_l3  // ~0.04
   individual_daughter_robust = false
   branching_required = true
```

---

## 6. Fallback-Condition Fields

| Condition | Threshold | Effect on L-level |
|-----------|-----------|------------------|
| ΔG_barrier < 23 kT | Carrier non-functional | L4-conditional → L3 (full revert) |
| ΔG_barrier 23–28 kT | Carrier marginal | L4-conditional → L3+ (partial) |
| ΔG_barrier ≥ 28 kT | Carrier robust | L4-conditional justified |
| N_HIC < 4 per subtype | HIC bottleneck dominant | L4 capped by HIC loss (~4% per gen from HIC alone) |
| N_HIC ≥ 6 per subtype | HIC bottleneck resolved | L4 achievable across full essential-class inventory |
| Daughter inherits < 3 HICs | Recovery infeasible | That daughter: L3-level viability |

---

## 7. Uncertainty / Fragility Fields

| Variable | Type | Value | Source |
|----------|------|-------|--------|
| `n_m4_uncertainty` | str | "±2 copies" | Copy numbers depend on carrier replication rate |
| `partition_bias_uncertainty` | str | "±0.10" | Spatial correlation strength uncertain |
| `recovery_fraction_uncertainty` | str | "±0.15" | Depends on HIC inheritance and carrier flux |
| `hic_bottleneck_resolved` | bool | UNCERTAIN | N_HIC at M4 = 3–6; resolution parameter-dependent |
| `p_any_loss_uncertainty` | str | "factor of ~2–3×" | Combines N, bias, and recovery uncertainties |
| `half_life_uncertainty` | str | "factor of ~2–3×" | Follows from p_any_loss uncertainty |
| `l4_fragility` | enum | MODERATE | Sharp carrier dependence; HIC bottleneck |
| `l4_to_l3_transition` | enum | SHARP | Binary: carrier works → L4; carrier fails → L3 |

---

## 8. Verdict Fields

| Field | Value | Authority |
|-------|-------|----------|
| `l4_conditional_justified` | `CONDITIONAL` | Book VIII Beta |
| `l4_unconditional_justified` | `NO` | Book VIII Beta |
| `l5_justified` | `NO` | Book VIII Beta |
| `l4_dominant_driver` | `copy_deepening_exponential` | Family A |
| `l4_new_capability` | `post_fission_carrier_recovery` | Family B |
| `l4_bottleneck` | `hic_copy_number` | Rate-limiting class |
| `book_viii_beta_changes_state` | `YES` | L4-conditional verified |
| `new_cost` | `0` | Twenty-fifth zero-cost target |
| `global_verdict` | `B` | M4 conditionally upgrades to L4-cond; unconditional L4 absent |

---

## 9. Minimal Serialized Example

```json
{
  "program_phase": "BOOK_VIII_BETA",
  "stage": "lineage_robustness_reassessment_under_M4",

  "l_level": {
    "unconditional": "L3",
    "conditional": "L4_CONDITIONAL",
    "l4_justified": "CONDITIONAL",
    "l4_unconditional": false,
    "l5_justified": false,
    "p_any_loss_l3": "0.03-0.08",
    "p_any_loss_l4_cond": "0.005-0.015",
    "half_life_l3_gen": "9-23",
    "half_life_l4_cond_gen": "50-140"
  },

  "m4_backing": {
    "m_level_conditional": "M4_CONDITIONAL",
    "d_level_conditional": "D4_CONDITIONAL",
    "carrier_committed": true,
    "dg_barrier_regime": "ROBUST",
    "directed_fraction_m4": "0.30-0.34"
  },

  "essential_classes": {
    "count": 4,
    "classes": ["templates", "replication_catalysts", "assembly_catalysts", "hic_scaffolds"],
    "copy_numbers_m3": {"templates": "6-8", "catalysts": "3-5", "assembly": "3-5", "hic": "2-4"},
    "copy_numbers_m4": {"templates": "8-12", "catalysts": "5-8", "assembly": "5-8", "hic": "3-6"},
    "bottleneck": "hic_scaffolds",
    "bottleneck_N_m4": "3-6"
  },

  "lineage_dynamics": {
    "partition_bias_m3": 0.30,
    "partition_bias_m4": "0.35-0.45",
    "recovery_fraction_m4": "0.30-0.50",
    "recovery_available_m3": false,
    "individual_daughter_robust_m4": true,
    "branching_required_m4": false,
    "p_single_line_100gen_l3": 0.017,
    "p_single_line_100gen_l4_mid": 0.55,
    "recovery_loop": "self-stabilizing: higher N → lower loss → more viable daughters → higher N"
  },

  "lineage_routes": {
    "A_copy_deepening": "dominant_driver_strengthened_l3",
    "B_recovery": "genuinely_new_l4_qualifying",
    "C_repair_continuity": "supporting_borderline_new",
    "D_package": "SURVIVES_package_level",
    "E_enrichment": "supporting_strengthened_l3",
    "F_pseudo": "partially_applies_disqualified"
  },

  "fragility": {
    "carrier_dependent": true,
    "hic_bottleneck": "SIGNIFICANT",
    "copy_number_uncertainty": "factor_2",
    "l4_fragility": "MODERATE",
    "fallback_regime": "L3_unconditional"
  },

  "cost": {
    "total_postulates": 15,
    "total_parameters": 9,
    "total_fields": 1,
    "total_dof": 6,
    "book_viii_beta_added": {"postulates": 0, "parameters": 0},
    "zero_cost_targets": 25
  },

  "verdict": {
    "global": "B",
    "l4_conditional": "JUSTIFIED_CONDITIONAL_MID_RANGE",
    "l4_unconditional": "NOT_JUSTIFIED",
    "l5_justified": "NOT_JUSTIFIED",
    "state_change": true,
    "next_audit": "book_viii_gamma_adaptive_dynamics_reassessment_under_M4"
  }
}
```

---

## 10. Integration Notes

### 10.1 What GRUT-RAI Must Update from Book VIII Beta

1. **L-level dual state formalized:** L3 unconditional / L4-conditional. Use L4-conditional for M4-regime reasoning; use L3 for fallback/unconditional reasoning.
2. **L4-conditional verified, not merely projected.** Book VII Gamma §8 projected L3→L4 approaches. Book VIII Beta verified L4-conditional through dedicated multi-generation analysis.
3. **Per-gen loss updated:** L3 = ~4%; L4-conditional = ~0.5–1.5% (mid-range M4).
4. **Single-lineage half-life updated:** L3 = ~16 gen; L4-conditional = ~50–140 gen.
5. **Individual daughter robustness:** At L4-conditional, individual daughters are individually robust. Branching redundancy is helpful but not required.
6. **HIC bottleneck identified:** HIC scaffolds are the rate-limiting class. N_HIC ≥ 5–6 required for full L4.
7. **Zero-cost target count:** 25.

### 10.2 What GRUT-RAI Must NOT Update

- No change to total cost (15/9/1/6)
- No change to carrier commitment status (still provisional)
- No change to M-level (still M4-conditional / M3-unconditional)
- No change to D-level (still D4-conditional / D3-unconditional)
- No promotion to unconditional L4
- No promotion to L5
- No change to A-level (that is Book VIII Gamma)

---

*GRUT-RAI L4 State Model complete. Entity types, state variables, transition rules, essential-class fields, fallback conditions, fragility fields, verdict fields, and minimal serialized example provided. L4-conditional verified. L3 retained as unconditional floor. HIC bottleneck identified.*
