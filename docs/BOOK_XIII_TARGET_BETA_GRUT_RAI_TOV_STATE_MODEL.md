# Book XIII — Target Beta: GRUT-RAI TOV State Model

## Machine-Readable State Model for Modified TOV / M-R Prediction Reasoning

---

## 1. Entity Types

| Entity | Description | Source |
|--------|-------------|--------|
| `modified_tov_system` | Closed 4-ODE system: m, ν, p_r, Φ with T^Φ source | Phase 4 §D + XIII Beta |
| `two_zone_object` | Compact object with nuclear outer zone + GRUT inner zone | XIII Beta §6.2 |
| `structural_prediction` | Quantitative result derivable from system structure without full numerical integration | XIII Beta §6 |
| `mr_curve` | Mass-radius relation from TOV integration (uncomputed) | XIII Beta target |

---

## 2. TOV / EOS / Central-Condition Fields

| Variable | Type | Value | Description |
|----------|------|-------|-------------|
| `system_closed` | bool | **true** | Four coupled ODEs; all components specified |
| `tov_equations` | str | "dm/dr, dν/dr, dp_r/dr, Φ'' EOM" | Phase 4 §D |
| `t_phi_algebraic` | bool | true | ρ_Φ, p_r,Φ, p_⊥,Φ algebraically from Φ, Φ', m, r |
| `nuclear_eos_required` | bool | true | Outer-zone closure; standard NS EOS (SLy, APR, etc.) |
| `central_phi` | str | "Φ_c (free parameter; scan)" | Integration initial condition |
| `tau` | str | "~10⁻⁵ s (structurally motivated)" | GRUT constitutive timescale |
| `x_prescription` | str | "fixed-background (Picard) or self-consistent" | Source function |

---

## 3. Output Fields

| Variable | Type | Value | Description |
|----------|------|-------|-------------|
| `prediction_1_buchdahl` | str | "STRUCTURAL: C > 8/9 permitted (ρ_eq < 0 violates Buchdahl hypothesis)" | Theorem-level |
| `prediction_2_two_zone` | str | "STRUCTURAL: nuclear outer + GRUT inner (ρ < 0); new architecture class" | Qualitatively new |
| `prediction_3_mass_deficit` | str | "QUANTIFIABLE: dm/dr < 0 in inner zone; m(r) non-monotonic; Δm from Phase 4 §E" | Traceable to ρ_eq |
| `mr_curves_computed` | bool | **false** | Full numerical integration not yet performed |
| `branch_structure_inferred` | str | "Standard → GRUT-modified → ultra-compact (qualitative)" | From structural analysis |

---

## 4. Stability Fields

| Variable | Type | Value | Description |
|----------|------|-------|-------------|
| `standard_branch_stable` | bool | true | Below turning point (standard TOV) |
| `grut_branch_stable` | enum | **UNKNOWN** | Requires numerical M(ρ_c) |
| `ultra_compact_stable` | enum | **UNKNOWN** | Requires dynamical perturbation |
| `turning_point_computed` | bool | false | Needs numerical M-R sequence |

---

## 5. Phenomenology-Strength Fields

| Variable | Type | Value | Description |
|----------|------|-------|-------------|
| `structural_predictions` | int | **3** | Buchdahl, two-zone, mass deficit |
| `predictions_eos_independent` | bool | true | All three are structural (ρ < 0 sign) |
| `quantitative_curves_available` | bool | false | M-R curves not computed |
| `comparison_ready` | bool | false | Need curves for NICER/LIGO comparison |
| `computation_tractable` | bool | **true** | Standard ODE/BVP numerics |
| `computation_performed` | bool | **false** | Key gap |

---

## 6. Limitation / Failure Fields

| Variable | Type | Value | Description |
|----------|------|-------|-------------|
| `mr_curves_gap` | enum | KEY | Full M-R curves uncomputed |
| `self_consistency_gap` | enum | MODERATE | X(r) self-consistency not fully solved |
| `zone_transition_gap` | enum | MODERATE | Activation criterion heuristic |
| `stability_gap` | enum | SIGNIFICANT | GRUT branch stability unknown |
| `tidal_gap` | enum | SIGNIFICANT | Perturbation theory unformulated |
| `all_gaps_computational` | bool | **true** | Physics defined; computation needed |

---

## 7. Frontier-Status Fields

| Variable | Type | Value | Description |
|----------|------|-------|-------------|
| `frontier_strengthened` | bool | **true** | Three structural predictions + closed system + tractable numerical path |
| `bridge_worthiness_changed` | bool | false | Not yet; M-R curves would change this |
| `next_computation` | str | "Numerical GRUT TOV integration → M-R curves" | Highest-leverage next step |
| `phenomenology_viable` | bool | **true** | Real quantitative program exists |

---

## 8. Verdict Fields

| Field | Value | Authority |
|-------|-------|----------|
| `xiii_beta_global_verdict` | `B_partial_real_quantitative_program` | XIII Beta |
| `system_closed` | `YES` | XIII Beta §4 |
| `structural_predictions` | `3 (Buchdahl, two-zone, mass deficit)` | XIII Beta §6 |
| `mr_curves_computed` | `NO` | XIII Beta |
| `grut_distinctive` | `YES` | XIII Beta §6 (all three absent in GR) |
| `frontier_strengthened` | `YES` | XIII Beta §11 |
| `next_step` | `numerical_grut_tov_integration` | XIII Beta |
| `cost_change` | `ZERO` | Analytical audit |

---

## 9. Minimal Serialized Example

```json
{
  "program_phase": "BOOK_XIII_BETA",
  "stage": "modified_tov_integration_mass_radius_prediction",

  "tov_system": {
    "closed": true,
    "equations": "4 coupled ODEs (m, ν, p_r, Φ) + algebraic T^Phi",
    "source": "Phase 4 xAct §B-D",
    "integrable": true,
    "integrated": false
  },

  "structural_predictions": [
    {"id": 1, "name": "relaxed_buchdahl", "type": "THEOREM_LEVEL", "content": "C > 8/9 permitted (rho_eq < 0 violates hypothesis)", "eos_independent": true},
    {"id": 2, "name": "two_zone_architecture", "type": "STRUCTURAL", "content": "nuclear outer + GRUT inner (rho < 0); new class", "eos_independent": true},
    {"id": 3, "name": "mass_deficit_interior", "type": "QUANTIFIABLE", "content": "dm/dr < 0 in inner zone; Delta_m from Phase 4 §E", "eos_independent": true}
  ],

  "branch_structure": {
    "standard": "GR-compatible; C < 8/9; stable below turning point",
    "grut_modified": "mass deficit; C can exceed 8/9; stability UNKNOWN",
    "ultra_compact": "extensive inner zone; high C; stability UNKNOWN"
  },

  "gaps": {
    "mr_curves": "NOT_COMPUTED (KEY GAP; tractable)",
    "stability": "UNKNOWN (requires numerical turning-point)",
    "tidal": "UNFORMULATED (requires perturbation theory)",
    "self_consistency": "MODERATE (Picard iteration available)",
    "all_computational": true
  },

  "frontier": {
    "strengthened": true,
    "bridge_worthiness_changed": false,
    "next": "numerical_grut_tov_integration"
  },

  "cost": {
    "change": "ZERO",
    "committed": "16/11/1/6"
  },

  "verdict": {
    "global": "B",
    "system_closed": true,
    "predictions": 3,
    "mr_computed": false,
    "frontier_strengthened": true,
    "next": "numerical_tov_integration"
  }
}
```

---

## 10. Integration Notes

### 10.1 What GRUT-RAI Must Update from XIII Beta

1. **Modified TOV system CLOSED.** Four coupled ODEs; all T^Φ components algebraically specified; boundary conditions defined.
2. **Three structural predictions derived.** Relaxed Buchdahl (C > 8/9); two-zone architecture (nuclear + GRUT); non-monotonic mass profile (dm/dr < 0 interior).
3. **All three are EOS-independent.** Follow from ρ_eq < 0 sign, not from nuclear-EOS choice.
4. **All three are GRUT-distinctive.** Absent in GR under standard energy conditions.
5. **Full M-R curves NOT computed.** This is the key gap. Numerical integration is tractable (standard ODE/BVP) but unperformed.
6. **Frontier strengthened.** Three concrete predictions + closed system + defined computational path.

### 10.2 What GRUT-RAI Must NOT Update

- No claim of M-R curves computed (they are not)
- No claim of comparison readiness for NICER/LIGO (curves needed)
- No claim of stability for GRUT/ultra-compact branches (unknown)
- No claim of tidal deformability predictions (unformulated)
- No change to committed cost (16/11/1/6)
- No change to GGB commitment status

---

*GRUT-RAI TOV State Model complete. System closed. Three structural predictions. M-R curves uncomputed (tractable gap). Frontier strengthened. Next: numerical integration.*
