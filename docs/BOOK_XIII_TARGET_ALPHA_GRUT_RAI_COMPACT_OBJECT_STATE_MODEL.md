# Book XIII — Target Alpha: GRUT-RAI Compact-Object State Model

## Machine-Readable State Model for Compact-Object Phenomenology Reasoning

---

## 1. Entity Types

| Entity | Description | Source |
|--------|-------------|--------|
| `grut_interior` | GRUT-modified compact-object interior with ρ_eq < 0 and f > 0 | D1–D10; Phase 4 |
| `modified_tov` | Phase 4 TOV system with T^Φ source | Phase 4 §D |
| `compactness_deviation` | Ultra-compact equilibria beyond Buchdahl bound (C > 8/9) | XIII Alpha Family A |
| `grut_remnant` | Singularity-free ultra-compact remnant; new compact-object class | XIII Alpha Family D |
| `mr_curve` | Mass-radius relation from GRUT TOV (uncomputed) | Next-step target |

---

## 2. Interior / Surplus Fields

| Variable | Type | Value | Description |
|----------|------|-------|-------------|
| `rho_eq` | str | "−X²/(2τ²) < 0" | Negative equilibrium energy density |
| `f_min_range` | str | "+0.37 to +0.46" | D1–D10 metric positivity |
| `mass_deficit` | str | "dm/dr < 0 near equilibrium" | Interior mass decreases inward |
| `nec_status` | str | "SATURATED (ρ + p = 0)" | NEC-saturating at equilibrium |
| `anisotropy` | str | "p_r − p_⊥ = (Φ')²/h ≥ 0" | Anisotropic pressure |
| `two_component` | str | "Component A (1/r⁴ scalar memory) + Component B (1/r² hedgehog defect)" | Interior support architecture |

---

## 3. Signature Fields

| Variable | Type | Value | Description |
|----------|------|-------|-------------|
| `family_a_compactness` | enum | **STRUCTURAL** | Ultra-compact equilibria; C > 8/9 possible |
| `family_b_max_mass` | enum | CONDITIONAL | TOV limit shift; requires numerical integration |
| `family_c_tidal` | enum | CONDITIONAL | Λ(M) modification; requires perturbation theory |
| `family_d_remnant` | enum | **STRUCTURAL** | New compact-object class; singularity-free |
| `family_e_postmerger` | enum | FAILS | Requires dynamical simulation; formalism absent |
| `family_f_pseudo` | enum | DISQUALIFIED | Interior effect propagates via TOV matching |
| `surviving_structural` | int | 2 | Families A and D |
| `surviving_conditional` | int | 2 | Families B and C |

---

## 4. Phenomenology-Strength Fields

| Variable | Type | Value | Description |
|----------|------|-------|-------------|
| `compactness_testable` | bool | true | In principle testable via NICER/X-ray M-R |
| `remnant_testable` | enum | CONDITIONAL | Depends on exterior properties (shadow, geodesics) |
| `tidal_testable` | bool | true | In principle testable via GW merger data |
| `max_mass_testable` | bool | true | In principle testable via massive-pulsar observations |
| `any_quantified` | bool | **false** | Numerical GRUT TOV not yet integrated |
| `computation_path_defined` | bool | **true** | Phase 4 provides the system; integration is the gap |

---

## 5. Limitation / Failure Fields

| Variable | Type | Value | Description |
|----------|------|-------|-------------|
| `numerical_tov_integrated` | bool | **false** | Key gap: M-R curves not yet computed |
| `tidal_perturbation_formulated` | bool | false | Even-parity perturbation for anisotropic interior unformulated |
| `remnant_exterior_computed` | bool | false | Geodesic/shadow/photosphere properties unknown |
| `nuclear_eos_matched` | bool | false | Transition from nuclear exterior to GRUT interior unspecified |
| `dynamical_collapse_available` | bool | false | Full numerical GR + T^Φ simulation absent |

---

## 6. Frontier-Status Fields

| Variable | Type | Value | Description |
|----------|------|-------|-------------|
| `frontier_strengthened` | bool | **true** | Two structural signature families + defined computation path |
| `bridge_worthiness_changed` | bool | false | Not yet — but defines path to change |
| `phenomenology_program_viable` | bool | **true** | GRUT TOV integration is tractable and defined |
| `next_computational_target` | str | "GRUT TOV numerical integration → M-R curves" | Highest-leverage next step |

---

## 7. Uncertainty / Fragility Fields

| Variable | Type | Value | Source |
|----------|------|-------|--------|
| `d1_d10_proxy_closure` | bool | true | D1–D10 used macro-field proxy, not full coupled solution |
| `schwarzschild_background` | bool | true | D1–D10 on Schwarzschild background |
| `lambda_range_tested` | str | "{5, 10, 25, 50, 100, 200}" | D1–D10 parameter range |
| `compactness_quantified` | bool | false | Exact modified Buchdahl bound not computed |
| `remnant_stability_assessed` | bool | false | Remnant may or may not be dynamically stable |

---

## 8. Verdict Fields

| Field | Value | Authority |
|-------|-------|----------|
| `xiii_alpha_global_verdict` | `B_partial_real_phenomenology` | XIII Alpha |
| `structural_families` | `2 (A: compactness, D: remnant)` | XIII Alpha |
| `conditional_families` | `2 (B: max mass, C: tidal)` | XIII Alpha |
| `failed_families` | `1 (E: post-merger)` | XIII Alpha |
| `frontier_strengthened` | `YES` | XIII Alpha |
| `computation_path_defined` | `YES` | XIII Alpha |
| `next_step` | `GRUT_TOV_numerical_integration` | XIII Alpha |
| `cost_change` | `ZERO` | Diagnostic audit |

---

## 9. Minimal Serialized Example

```json
{
  "program_phase": "BOOK_XIII_ALPHA",
  "stage": "compact_object_observational_signatures",

  "surplus_basis": {
    "singularity_resolution": "DEMONSTRATED (D1-D10; f_min > 0)",
    "mechanism": "rho_eq = -X^2/(2tau^2) < 0; mass reduction; metric positivity restored",
    "tov_system": "Phase 4 §D: closed modified TOV with T^Phi"
  },

  "signatures": {
    "A_compactness": {"status": "STRUCTURAL", "consequence": "ultra-compact equilibria C > 8/9", "testable_by": "NICER_M-R"},
    "B_max_mass": {"status": "CONDITIONAL", "consequence": "shifted TOV limit", "requires": "numerical_tov"},
    "C_tidal": {"status": "CONDITIONAL", "consequence": "modified Lambda(M)", "requires": "perturbation_theory"},
    "D_remnant": {"status": "STRUCTURAL", "consequence": "new compact-object class (not BH, not gravastar)", "requires": "exterior_properties"},
    "E_postmerger": {"status": "FAILS", "reason": "dynamical_simulation_absent"},
    "F_pseudo": {"status": "DISQUALIFIED", "reason": "interior_effect_propagates_via_TOV"}
  },

  "phenomenology": {
    "program_viable": true,
    "structural_families": 2,
    "conditional_families": 2,
    "any_quantified": false,
    "computation_path": "GRUT TOV integration → M-R curves → data comparison"
  },

  "frontier": {
    "strengthened": true,
    "bridge_worthiness_changed": false,
    "direction": "compact-object phenomenology via GRUT TOV"
  },

  "cost": {
    "change": "ZERO",
    "committed": "16/11/1/6"
  },

  "verdict": {
    "global": "B",
    "phenomenology_survives": true,
    "strongest": ["A_compactness", "D_remnant"],
    "next": "GRUT_TOV_numerical_integration"
  }
}
```

---

## 10. Integration Notes

### 10.1 What GRUT-RAI Must Update from XIII Alpha

1. **Two structural compact-object signatures identified.** Family A (modified compactness limit; C > 8/9) and Family D (GRUT ultra-compact remnant; new object class).
2. **Computational path defined.** GRUT TOV numerical integration → M-R curves → data comparison (NICER, massive pulsars).
3. **Frontier strengthened with phenomenological direction.** No longer "one internal result"; now "one internal result with two structural external consequences and a defined computation program."
4. **Bridge-worthiness not yet changed.** But the path to change is clear: if M-R predictions are quantified and falsifiable, the commitment case strengthens.

### 10.2 What GRUT-RAI Must NOT Update

- No claim of observational confirmation (signatures identified, not detected)
- No claim of compact-object theory closure (formalism gaps remain)
- No claim of black-hole replacement (different physics, not upgraded GR)
- No claim of detectability (assessment not performed)
- No change to committed cost (16/11/1/6)
- No change to GGB commitment status (still uncommitted)

---

*GRUT-RAI Compact-Object State Model complete. Two structural signature families. Computation path defined. Frontier strengthened. Next: GRUT TOV numerical integration.*
