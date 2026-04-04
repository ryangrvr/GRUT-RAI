# Book XI — Target Alpha: GRUT-RAI Strong-Field Timing State Model

## Machine-Readable State Model for Binary-Pulsar and Gravitational-Sector Reasoning

---

## 1. Entity Types

| Entity | Description | Source |
|--------|-------------|--------|
| `binary_system` | Compact binary with orbital period P, eccentricity e, masses m₁, m₂ | Observational |
| `p_dot_observable` | Orbital period derivative due to gravitational radiation | Observational (Hulse-Taylor) |
| `scalar_field_phi` | GRUT native field; first-order dissipative dynamics | GRUT core |
| `effective_metric` | Conformal metric slaved to Φ; no independent dynamics | Appendix W-E |
| `tensor_metric` | Independent spin-2 metric with gravitational-wave DOF | GR (absent in native GRUT) |
| `screened_potential` | Yukawa/Helmholtz static sector | Appendix W-F |

---

## 2. Timing / Observable Fields

| Variable | Type | Domain | Description |
|----------|------|--------|-------------|
| `p_dot_gr` | float | < 0 | GR-predicted P-dot from quadrupole formula |
| `p_dot_observed` | float | < 0 | Measured P-dot (corrected for Galactic acceleration) |
| `p_dot_grut_native` | enum | {UNDEFINED, WRONG_SCALING, COMPATIBLE, MATCHING} | GRUT native prediction status |
| `p_dot_grut_effective` | enum | {UNDEFINED, GR_IMPORTED, COMPATIBLE} | GRUT-as-matter-within-GR status |
| `agreement_threshold` | float | 0.002 | ~0.2% tolerance |
| `tensor_gw_present` | bool | — | Whether tensor gravitational waves exist in the formalism |
| `quadrupole_formula_derivable` | bool | — | Whether the GR quadrupole formula is reproducible |

---

## 3. Native / Effective Mapping Fields

| Variable | Type | Domain | Description |
|----------|------|--------|-------------|
| `family_a_native` | str | "FAILS" | Scalar radiation: wrong multipole |
| `family_b_effective` | str | "CONDITIONAL" | GR + GRUT matter: imports GR gravity |
| `family_c_trend` | str | "FAILS" | Correct sign; wrong scaling/magnitude |
| `family_d_obstruction` | str | "CONFIRMED" | Structural: scalar ≠ tensor |
| `strongest_route` | str | "B_conditional" | Only viable if GRUT = matter theory within GR |
| `native_route_exists` | bool | false | No native tensor-gravity route |

---

## 4. Failure-Mode Fields

| Variable | Type | Value | Description |
|----------|------|-------|-------------|
| `radiative_failure` | bool | true | No tensor GW; scalar radiation has wrong multipole |
| `conservative_failure` | bool | true | Screened Yukawa potential; not 1/r |
| `field_content_failure` | bool | true | Scalar (spin-0) instead of tensor (spin-2) |
| `dissipative_overshoot` | bool | true | τ-dissipation adds decay beyond GR prediction |
| `mapping_imports_gr` | bool | true | Family B imports GR gravitational sector |
| `failure_type` | enum | STRUCTURAL | Not parametric; not computational; fundamental |

---

## 5. Uncertainty / Fragility Fields

| Variable | Type | Value | Source |
|----------|------|-------|--------|
| `gravity_sector_addressed` | bool | false | First gravity-side audit |
| `compatibility_level` | enum | G0_NATIVE | No native account |
| `compatibility_if_matter_theory` | enum | G3_VIA_GR | Automatic via Einstein equations |
| `program_identity_resolved` | bool | false | ToE vs matter theory decision pending |
| `gravitational_bridge_needed` | enum | YES_IF_TOE | Needed only if GRUT claims to replace GR |
| `emergent_gravity_viable` | enum | UNKNOWN | Not assessed; no structural path visible |

---

## 6. Verdict Fields

| Field | Value | Authority |
|-------|-------|----------|
| `binary_pulsar_gate` | `FAIL_NATIVE` / `CONDITIONAL_VIA_GR` | Book XI Alpha |
| `gravity_classification` | `G0_native` | Book XI Alpha |
| `failure_localized` | `YES` | Radiative + conservative + field content |
| `failure_type` | `STRUCTURAL` | Scalar ≠ tensor |
| `architectural_decision_needed` | `YES` | ToE vs matter theory vs emergent gravity |
| `book_xi_alpha_changes_state` | `YES` | Gravity gap precisely characterized |
| `new_cost` | `0` | Diagnostic audit only |
| `global_verdict` | `A` | Does not clear gate; failure localized |

---

## 7. Minimal Serialized Example

```json
{
  "program_phase": "BOOK_XI_ALPHA",
  "sector": "gravitational_cosmological",
  "stage": "binary_pulsar_radiation_strong_field_timing",

  "binary_pulsar_gate": {
    "status_native": "FAIL",
    "status_effective": "CONDITIONAL_VIA_GR",
    "failure_type": "STRUCTURAL",
    "failure_modes": [
      "radiative: no tensor GW (scalar field → wrong multipole)",
      "conservative: screened Yukawa potential (not 1/r)",
      "field_content: scalar spin-0 (not tensor spin-2)",
      "dissipative: tau-relaxation adds orbital decay beyond GR"
    ]
  },

  "compatibility": {
    "native": "G0_no_viable_account",
    "as_matter_within_GR": "G3_strong_compatibility_via_GR",
    "precision_native": "NOT_ACHIEVED"
  },

  "mapping_routes": {
    "A_native_direct": "FAILS",
    "B_effective_GR": "CONDITIONAL_imports_GR",
    "C_qualitative_trend": "FAILS",
    "D_structural_obstruction": "CONFIRMED"
  },

  "architectural_decision": {
    "needed": true,
    "options": [
      {"id": 1, "name": "gravitational_bridge", "cost": "HIGH", "identity": "ToE"},
      {"id": 2, "name": "matter_theory_within_GR", "cost": "ZERO", "identity": "matter_theory"},
      {"id": 3, "name": "emergent_gravity", "cost": "ZERO_if_successful", "identity": "ToE"}
    ],
    "recommended_next": "book_xi_beta_gravitational_architecture_decision"
  },

  "cost": {
    "total_postulates": 16,
    "total_parameters": 11,
    "total_fields": 1,
    "total_dof": 6,
    "book_xi_alpha_added": {"postulates": 0, "parameters": 0},
    "gravity_bridge_cost": "unknown_pending_xi_beta"
  },

  "biology_side": {
    "status": "FROZEN",
    "affected_by_xi_alpha": false,
    "resumable": true
  },

  "verdict": {
    "global": "A",
    "gate_cleared": false,
    "failure_localized": true,
    "next_stage": "book_xi_beta_gravitational_architecture_decision"
  }
}
```

---

## 8. Integration Notes

### 8.1 What GRUT-RAI Must Update from Book XI Alpha

1. **Gravity sector: G0 native.** The native scalar architecture does not produce tensor gravitational radiation. Binary-pulsar gate: FAIL (native).
2. **Failure localized precisely.** Radiative (no tensor GW), conservative (screened potential), field content (scalar ≠ tensor), dissipative (overshoot).
3. **Conditional compatibility via GR.** If GRUT is defined as a matter theory within GR, the binary-pulsar test passes via Einstein gravity. Classification: G3 (via GR).
4. **Architectural decision needed.** The program must decide: install a gravitational bridge (sixth bridge), accept matter-theory status, or pursue emergent gravity.
5. **Biology-side unaffected.** Books IV–X results are independent of the gravitational sector. The biology-side scaffold remains frozen and valid.
6. **Zero cost added.** Diagnostic audit only.

### 8.2 What GRUT-RAI Must NOT Update

- No claim of native binary-pulsar compatibility (G0 native)
- No claim of passing the gravitational gate
- No change to biology-side scaffold (frozen; independent)
- No change to cost (16/11/1/6)
- No claim that the failure can be fixed by parameter tuning (structural, not parametric)
- No claim of final ToE closure

### 8.3 The Program-Defining Question

Book XI Alpha exposes the deepest question in the GRUT program:

**Is GRUT a Theory of Everything, or a Theory of Matter?**

- If ToE: GRUT must contain or derive tensor gravity. The binary-pulsar failure must be resolved by bridge or emergence. The cost will be substantial.
- If matter theory: GRUT couples to standard GR through T_μν. The binary-pulsar test passes via GR. GRUT's contribution is the matter/organization sector (solitons, composites, proto-cells, metabolism, adaptation, transport). The gravitational sector belongs to Einstein.

This decision determines the program's identity and scope. It cannot be deferred.

---

*GRUT-RAI Strong-Field Timing State Model complete. Binary-pulsar gate: FAIL native / CONDITIONAL via GR. Failure structural (scalar ≠ tensor). Architectural decision needed: gravitational bridge vs matter theory vs emergent gravity. Biology-side unaffected.*
