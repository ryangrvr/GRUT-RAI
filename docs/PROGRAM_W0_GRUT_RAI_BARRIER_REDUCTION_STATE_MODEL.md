# Program W0 — GRUT-RAI Barrier-Reduction State Model

## Machine-Readable State Model for Carrier-Debt Reasoning

---

## 1. Entity Types

| Entity | Description | Source |
|--------|-------------|--------|
| `k2_composite` | K=2-scale gauge-singlet bound pair of solitons | Book IV Beta |
| `k2_ground_state` | (N=1, ℓ=0, S=0) para-singlet; "unloaded" carrier | Book IV Beta §7 |
| `k2_excited_metastable` | (N=2, ℓ=0, S=0) selection-rule-protected; "loaded" carrier | W0 identification |
| `k2_excited_unstable` | (N=2, ℓ=1, S=1) E1-allowed; fast decay | Book IV Beta §7.3 |
| `soliton` | Topological soliton; constituent of composites | Book IV Alpha |
| `gauge_boson` | SU(2) gauge field quantum; mediates binding and transitions | Book IV Beta |
| `hic_scaffold` | Fixed-site energy transducer; loads carriers | Book V Delta |
| `target_site` | Remote scaffold site with quenching-compatible geometry | Book VII Beta |

---

## 2. Barrier / Support Variables

| Variable | Type | Domain | Description |
|----------|------|--------|-------------|
| `alpha_g` | float | (0, ∞) | Gauge coupling α_g = g²/(2π) |
| `m_sk_over_kT` | float | (1, ∞) | Soliton-to-thermal mass ratio |
| `e_bind` | float | (0, ∞) | Ground-state binding energy: α_g² M_sk / 4 |
| `delta_e_12` | float | (0, ∞) | First excitation energy: (3/16) α_g² M_sk |
| `delta_g_barrier` | float | (0, ∞) | Effective barrier height (identified with delta_e_12) |
| `delta_g_over_kT` | float | (0, ∞) | Barrier in thermal units: (3/16) α_g² (M_sk/kT) |
| `robust_regime_condition` | float | — | α_g² × (M_sk/kT); must be ≥ 149 for robust |
| `barrier_regime` | enum | {WEAK, MARGINAL, ROBUST} | Classification based on delta_g_over_kT |
| `loaded_state_identity` | str | — | "(N=2, ℓ=0, S=0) selection-rule-protected" |
| `metastability_mechanism` | str | — | "Dipole selection rule: Δℓ=±1 forbids ℓ=0→ℓ=0 E1 transition" |

---

## 3. Bound Fields

| Variable | Type | Domain | Description |
|----------|------|--------|-------------|
| `barrier_lower_bound` | float | (0, ∞) | ΔG_barrier ≥ (3/16) α_g² M_sk (hydrogenic, weak coupling) |
| `barrier_binding_ratio` | float | fixed: 0.75 | ΔE₁₂ / E_bind = 3/4 (exact for unperturbed Coulomb) |
| `hard_core_correction` | float | ~O(R_sk/a₀)² | Level shift from hard core; small in weak coupling |
| `robust_threshold_dimensionless` | float | 149 | α_g²(M_sk/kT) threshold for ΔG ≥ 28 kT |
| `selection_rule_exactness` | bool | true | Δℓ = ±1 for E1 is exact for any central potential |
| `two_boson_suppression` | str | "O(α_g²) relative to E1" | Qualitative suppression factor; absolute rate not computed |

---

## 4. Debt-Status Fields

| Variable | Type | Domain | Description |
|----------|------|--------|-------------|
| `carrier_postulate_status` | enum | {BRIDGE, REDUCED, ERASED} | Status of carrier functional-class postulate |
| `e_carrier_status` | enum | {MATCHED, SUPPORTED, DERIVED} | Epistemic status of E_carrier parameter |
| `tau_carrier_status` | enum | {MATCHED, SUPPORTED, DERIVED} | Epistemic status of τ_carrier parameter |
| `dg_barrier_status` | enum | {MATCHED, SUPPORTED, APPROXIMATELY_DERIVED} | Epistemic status of ΔG_barrier |
| `loaded_state_status` | enum | {POSTULATED, IDENTIFIED, DERIVED} | Epistemic status of loaded-state identity |
| `metastability_status` | enum | {POSTULATED, IDENTIFIED, DERIVED} | Epistemic status of metastability mechanism |
| `overall_debt_status` | enum | {UNCHANGED, WEAKLY_REDUCED, REDUCED, STRONGLY_REDUCED, ERASED} | Aggregate debt classification |
| `debt_change_description` | str | — | Human-readable summary of what changed |

---

## 5. Uncertainty / Fragility Fields

| Variable | Type | Value | Source |
|----------|------|-------|--------|
| `alpha_g_determined` | bool | false | Free parameter of gauge bridge |
| `m_sk_kT_determined` | bool | false | Free parameter (soliton mass / temperature) |
| `two_boson_rate_computed` | bool | false | Required for absolute τ_carrier; not done |
| `dissipation_coupling_assessed` | bool | false | GRUT native dissipation × bound-state interaction |
| `quenching_cross_section_computed` | bool | false | Required for discharge rate at targets |
| `loading_resonance_verified` | bool | false | HIC discharge energy ≈ ΔE₁₂ matching |
| `non_hydrogenic_corrections_assessed` | bool | false | Hard-core + short-range level shifts |
| `barrier_fragility` | enum | MODERATE | Generic support but free parameters remain |
| `mechanism_fragility` | enum | LOW | Selection rule is exact for central potentials |
| `parameter_range_fragility` | enum | LOW | Robust regime achieved across broad range |

---

## 6. Derivation-Route Fields

| Variable | Type | Value | Description |
|----------|------|-------|-------------|
| `route_a_status` | str | "necessary_but_insufficient" | Energy scale only; no metastability |
| `route_b_status` | str | "survives" | Energy scale + selection-rule metastability |
| `route_c_status` | str | "fails" | Centrifugal barrier; ℓ=1 radiatively unstable |
| `route_d_status` | str | "conditional" | Strong-coupling orientational; outside primary regime |
| `route_e_status` | str | "warning_applied" | Pseudo-support critique partially valid |
| `strongest_route` | str | "B" | Selection-rule metastability |
| `route_b_mechanism` | str | "(N=2,ℓ=0) dipole-forbidden → long-lived → quench at target" | Full mechanism chain |

---

## 7. Verdict Fields

| Field | Value | Authority |
|-------|-------|----------|
| `w0_global_verdict` | `B` | barrier_partially_supported_but_not_forced |
| `barrier_natively_supported` | `PARTIAL` | Supported but not forced |
| `barrier_forced` | `NO` | Free parameters remain |
| `debt_reduced` | `YES` | Mechanism + inequality + loaded-state identification |
| `debt_erased` | `NO` | Free parameters; decay rate not computed |
| `book_vii_strengthened` | `YES` | Barrier connected to binding physics; robust regime shown generic |
| `mainline_book_viii_affected` | `NO` | W0 affects confidence, not structure |
| `new_cost` | `0` | W0 adds no postulates or parameters |
| `carrier_postulate_retired` | `NO` | Functional-class postulate retained |

---

## 8. Minimal Serialized Example

```json
{
  "program": "W0",
  "type": "bridge_debt_reduction_audit",
  "scope": "carrier_barrier_only",

  "barrier_target": {
    "robust_threshold_kT": 28,
    "dimensionless_condition": "alpha_g^2 * (M_sk/kT) >= 149",
    "barrier_binding_ratio": 0.75,
    "regime_classification": {
      "weak": "alpha_g^2*(M_sk/kT) < 123",
      "marginal": "123 <= alpha_g^2*(M_sk/kT) < 149",
      "robust": "alpha_g^2*(M_sk/kT) >= 149"
    }
  },

  "lower_stack_support": {
    "energy_scale": {
      "formula": "delta_E_12 = (3/16) * alpha_g^2 * M_sk",
      "source": "K=2 hydrogenic spectrum (Book IV Beta)",
      "status": "derived"
    },
    "metastability_mechanism": {
      "loaded_state": "(N=2, ell=0, S=0)",
      "protection": "Dipole selection rule: Delta_ell = +-1 forbids ell=0 -> ell=0 E1",
      "exactness": "exact for any central potential",
      "status": "derived"
    },
    "discharge_mechanism": {
      "type": "collisional_quenching",
      "description": "Non-central perturbation at target site mixes ell=0 and ell=1, enabling fast de-excitation",
      "status": "structurally_plausible_not_derived"
    }
  },

  "derivation_routes": {
    "A_binding_depth": "necessary_but_insufficient",
    "B_selection_rule": "SURVIVES",
    "C_centrifugal": "FAILS",
    "D_collective_coordinate": "conditional_strong_coupling",
    "E_pseudo_support": "warning_applied"
  },

  "debt_status": {
    "pre_w0": {
      "dg_barrier": "matched_parameter",
      "loaded_state": "postulated",
      "metastability": "postulated",
      "overall": "full_bridge_debt"
    },
    "post_w0": {
      "dg_barrier": "approximately_derived_inequality",
      "loaded_state": "lower_stack_identified",
      "metastability": "lower_stack_derived",
      "overall": "REDUCED_strong"
    }
  },

  "open_questions": [
    "two_gauge_boson_decay_rate_not_computed",
    "dissipation_background_coupling_not_assessed",
    "loading_resonance_HIC_to_excitation_not_verified",
    "quenching_cross_section_not_computed",
    "non_hydrogenic_corrections_not_assessed"
  ],

  "cost": {
    "w0_added_postulates": 0,
    "w0_added_parameters": 0,
    "total_unchanged": "15/9/1/6"
  },

  "verdict": {
    "global": "B",
    "outcome_class": "barrier_partially_supported_but_not_forced",
    "debt_reduced": true,
    "debt_erased": false,
    "book_vii_strengthened": true,
    "mainline_affected": false
  }
}
```

---

## 9. Integration Notes

### 9.1 What GRUT-RAI Should Update from W0

1. **Carrier barrier epistemic class:** Upgrade from "matched parameter" to "lower-stack-supported (approximately derived inequality)." The barrier is no longer a free-floating assumption — it is connected to the binding energy of the K=2 composite through ΔG ≈ (3/4)E_bind.

2. **Loaded-state identity:** The carrier's loaded state is now identified as the (N=2, ℓ=0, S=0) excited bound state of the K=2 composite, not an unspecified "conformational switch."

3. **Metastability mechanism:** Upgrade from "assumed Arrhenius barrier" to "quantum selection-rule protection (Δℓ = ±1 forbids single-gauge-boson decay of ℓ=0 → ℓ=0)."

4. **Robust-regime condition:** Record the derivable inequality α_g²(M_sk/kT) ≥ 149 as the formal condition. Note that this is generically satisfied for thermally stable scaffolds with moderate gauge coupling.

5. **Carrier revocation condition:** Refine from "ΔG shown below 28 kT" to "α_g²(M_sk/kT) shown < 149, which would imply either very weak gauge coupling or marginally stable solitons."

### 9.2 What GRUT-RAI Must NOT Update

- No change to total cost (15/9/1/6)
- No change to carrier postulate count (still 1 postulate + 2 parameters)
- No change to M4-conditional status (still conditional)
- No claim of debt erasure
- No claim of unconditional M4
- No change to HIC bridge debt (W0 scope is carrier only)
- No change to mainline Book VIII sequence

### 9.3 Forward-Facing Open Items

If a future W1 program is pursued, it should address:

1. **Two-gauge-boson decay rate computation:** Determine the absolute lifetime of the (N=2, ℓ=0) state. If τ_2γ ≫ τ_diffusion (~2 ms), the metastability is confirmed quantitatively. If τ_2γ ~ τ_diffusion, the carrier is marginal. If τ_2γ ≪ τ_diffusion, the selection-rule mechanism fails and the barrier reverts to the Book VII matched-parameter status.

2. **Collisional quenching cross-section:** Determine the rate at which a compatible target site de-excites the loaded carrier. If quenching is efficient at target sites but negligible during free diffusion, the carrier operational model is confirmed.

3. **Dissipation coupling analysis:** Determine whether the GRUT native dissipation (τ dΦ/dt + Φ = X) affects the bound-state spectrum or the metastable-state lifetime.

4. **Non-hydrogenic corrections:** Assess the impact of hard-core level shifts and short-range corrections on ΔE₁₂.

Each of these would further reduce or confirm the current debt level.

---

*GRUT-RAI Barrier-Reduction State Model complete. Entity types, barrier/support variables, bound fields, debt-status fields, uncertainty fields, derivation-route fields, verdict fields, and minimal serialized example provided. Carrier debt reduced (strong). Mechanism identified. Barrier inequality derived. Postulate retained.*
