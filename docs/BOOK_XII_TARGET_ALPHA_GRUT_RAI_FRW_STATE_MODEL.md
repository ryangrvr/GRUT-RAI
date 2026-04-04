# Book XII — Target Alpha: GRUT-RAI FRW State Model

## Machine-Readable State Model for FRW Gate-1 Reasoning

---

## 1. Entity Types

| Entity | Description | Source |
|--------|-------------|--------|
| `frw_background` | Flat FRW cosmological background a(t), H(t) | Standard |
| `phi_sector` | GRUT Φ field in homogeneous FRW; T^Φ as source | Phase 4 xAct + XII Alpha |
| `dynamical_regulator` | Three-regime cosmological surplus from Φ dynamics | XII Alpha (new) |
| `commitment_gate_1` | FRW cosmological computation / screening viability | XI Epsilon |

---

## 2. FRW / Effective-Fluid Fields

| Variable | Type | Domain | Description |
|----------|------|--------|-------------|
| `rho_phi` | float | (−∞, ∞) | Effective Φ energy density: kinetic + displacement − equilibrium |
| `p_phi` | float | (−∞, ∞) | Effective Φ pressure |
| `w_phi` | float | (−∞, ∞) | Effective EOS: p_Φ/ρ_Φ; diverges at zero-crossing |
| `h_tau_ratio` | float | (0, ∞) | Dimensionless H·τ; controls regime |
| `regime` | enum | {FAST, TRANSITION, SLOW} | Current cosmological regime |
| `rho_phi_sign` | enum | {POSITIVE, ZERO, NEGATIVE} | Current sign of ρ_Φ |

---

## 3. Surplus-Status Fields

| Variable | Type | Value | Description |
|----------|------|-------|-------------|
| `original_screening_claim` | str | "COLLAPSED" | Dark-energy replacement: ρ_eq < 0, anti-accelerating |
| `revised_surplus` | str | "CONDITIONAL" | Dynamical three-regime regulator controlled by τ |
| `surplus_type` | str | "dynamical_cosmological_regulator" | New surplus category |
| `surplus_mechanism` | str | "H·τ ratio controls positive→negative ρ_Φ transition" | Mechanism |
| `surplus_distinct_from_gr` | bool | true | GR + Λ cannot produce three-regime transition |
| `surplus_falsifiable` | bool | true | If τ constrained, transition epoch H ~ 1/τ is predicted |
| `bounce_achieved` | bool | false | Appendix A: softened, not bounced |

---

## 4. Pathology Fields

| Variable | Type | Value | Description |
|----------|------|-------|-------------|
| `rho_eq_sign` | str | "NEGATIVE" | ρ_eq = −X²/(2τ²) < 0 at equilibrium |
| `late_time_h2_risk` | enum | PRESENT_IF_PHI_DOMINATES | H² < 0 if negative ρ_Φ dominates |
| `late_time_mitigant` | str | "X → 0 decouples Φ; or other sources dominate" | Condition for avoiding pathology |
| `zero_crossing_pathological` | bool | false | Standard feature of dynamical-DE models |
| `perturbation_sector` | str | "ENTIRELY_OPEN" | Background only; no perturbation analysis |
| `source_x_derived` | bool | false | X(t) is an extension assumption |

---

## 5. Commitment-Gate Fields

| Variable | Type | Value | Description |
|----------|------|-------|-------------|
| `gate_1_status` | enum | **CONDITIONAL_REVISED** | Survives with revised surplus |
| `gate_1_original_claim` | str | "COLLAPSED (dark-energy replacement)" | Original screening fails |
| `gate_1_revised_surplus` | str | "SURVIVES (dynamical regulator)" | New surplus |
| `ggb_portfolio` | str | "Surplus 1: DEMONSTRATED. Surplus 2: CONDITIONAL/REVISED. Surplus 3: OPEN." | Updated portfolio |
| `ggb_portfolio_score` | str | "~1.5/3" | Modestly strengthened |
| `next_gate` | str | "gate_2_gw_mixing_tau_constraint" | Next stage |

---

## 6. Uncertainty / Fragility Fields

| Variable | Type | Value | Source |
|----------|------|-------|--------|
| `source_x_assumed` | bool | true | Extension assumption (Appendix A, A3) |
| `perturbation_sector_open` | bool | true | Must be addressed for observational comparison |
| `tau_unconstrained` | bool | true | τ relative to H₀ unknown |
| `current_regime_unknown` | bool | true | H₀·τ could be > 1 (fast) or < 1 (slow) |
| `observational_adequacy_untested` | bool | true | No comparison to SN/CMB/BAO data |
| `regulator_structural_robustness` | enum | MODERATE | Three-regime behavior is generic for constitutive relaxation; specific timing depends on X form and τ |

---

## 7. Verdict Fields

| Field | Value | Authority |
|-------|-------|----------|
| `xii_alpha_global_verdict` | `B_gate_1_conditional_revised` | XII Alpha |
| `original_claim_status` | `COLLAPSED` | XII Alpha §5–6 |
| `revised_surplus_status` | `CONDITIONAL` | XII Alpha §6 |
| `gate_1_alive` | `YES_revised` | XII Alpha §9 |
| `ggb_strengthened` | `MODESTLY` | XII Alpha §9 |
| `next_gate` | `gate_2_gw_mixing` | XII Alpha §12 |
| `cost_change` | `ZERO` | Diagnostic audit |

---

## 8. Minimal Serialized Example

```json
{
  "program_phase": "BOOK_XII_ALPHA",
  "stage": "frw_cosmological_computation_screening_viability",

  "gate_1": {
    "status": "CONDITIONAL_REVISED",
    "original_claim": "COLLAPSED (dark-energy replacement; rho_eq < 0 anti-accelerating)",
    "revised_surplus": "CONDITIONAL (dynamical three-regime regulator controlled by H*tau)",
    "three_regimes": {
      "fast": {"h_tau": ">1", "rho_phi": "positive", "role": "subdominant_correction"},
      "transition": {"h_tau": "~1", "rho_phi": "crosses_zero", "role": "transition_epoch"},
      "slow": {"h_tau": "<1", "rho_phi": "negative", "role": "anti_accelerating"}
    },
    "bounce": false,
    "perturbation_sector": "OPEN"
  },

  "surplus_portfolio": {
    "surplus_1_singularity": "DEMONSTRATED",
    "surplus_2_cosmological": "CONDITIONAL_REVISED (dynamical regulator; not dark-energy replacement)",
    "surplus_3_gw": "OPEN",
    "score": "~1.5/3"
  },

  "pathology": {
    "rho_eq_negative": true,
    "late_time_risk": "present_if_phi_dominates",
    "zero_crossing": "not_pathological",
    "source_assumed": true,
    "perturbations_open": true
  },

  "cost": {
    "change": "ZERO",
    "committed": "16/11/1/6",
    "hypothetical_ggb": "17/12/2/8"
  },

  "verdict": {
    "global": "B",
    "gate_1_alive": true,
    "original_claim_dead": true,
    "revised_surplus_real": true,
    "next": "gate_2_gw_mixing_tau_constraint"
  }
}
```

---

## 9. Integration Notes

### 9.1 What GRUT-RAI Must Update from XII Alpha

1. **Gate 1: CONDITIONAL/REVISED.** The original "cosmological screening as Λ replacement" claim collapses (ρ_eq < 0). A revised surplus survives: the dynamical cosmological regulator (three-regime, H·τ-controlled).
2. **Surplus 2 reframed.** No longer "dark-energy replacement." Now "dynamical cosmological regulation" — a three-regime expansion-history modification controlled by τ. Genuine beyond-GR; distinct from GR + Λ.
3. **GGB portfolio modestly strengthened.** From 1/3 to ~1.5/3 demonstrated/conditional surpluses.
4. **No longer claim:** "native w = −1 replacing Λ" or "cosmological screening as dark energy." These are dead.
5. **Next gate:** Gate 2 (GW mixing + τ-constraint). τ-constraint would make the dynamical-regulator prediction falsifiable.

### 9.2 What GRUT-RAI Must NOT Update

- No change to committed cost (16/11/1/6)
- No claim of cosmological closure (background only; perturbations open)
- No claim of dark-energy solution (equilibrium ρ < 0 is anti-accelerating)
- No claim of GGB commitment (still gated)
- No change to validated baseline (matter-within-GR)

---

*GRUT-RAI FRW State Model complete. Gate 1: conditional/revised. Original screening collapsed. Dynamical regulator survives. Portfolio ~1.5/3. Gate 2 next.*
