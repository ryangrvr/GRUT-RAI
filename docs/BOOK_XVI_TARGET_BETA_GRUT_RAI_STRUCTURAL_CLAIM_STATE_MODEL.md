# Book XVI — Target Beta: GRUT-RAI Structural Claim State Model

---

## 1. Irreducible Claim Fields

| Field | Value |
|-------|-------|
| `irreducible_claim` | `constitutive_dissipation_plus_phase4_tphi` |
| `claim_equation` | `rho_eq = -X^2/(2*tau^2)` |
| `claim_eos` | `w = -1 (NEC-saturated)` |
| `claim_derivation_steps` | `3 (algebraic; from one postulate)` |
| `claim_verification` | `xAct computer algebra (Phase 4)` |
| `claim_postulate_count` | `1 (tau dPhi/dt + Phi = X)` |
| `claim_free_parameters` | `1 (tau)` |

## 2. Criteria Evaluation Fields

| Field | Value |
|-------|-------|
| `c1_not_gr_matter` | `PASS (GR has no constitutive scalar with this T^Phi)` |
| `c2_adversarial_math` | `PASS (Lyapunov theorem + 3-step algebra + xAct)` |
| `c3_no_amplification` | `PASS (exact equilibrium result; no proxy)` |
| `survives_all_criteria` | `true` |

## 3. Candidate Verdict Fields

| Field | Value |
|-------|-------|
| `candidate_1_time_reversal` | `SURVIVES (Lyapunov theorem)` |
| `candidate_2_tphi` | `SURVIVES (Phase 4 xAct)` |
| `candidate_3_decoherence` | `FAILS_C2 (postulated operator content)` |
| `candidate_4_biology` | `PASSES_EXTENSION_LEVEL (26 zero-cost; bridge-dependent)` |
| `candidate_5_vacuum_response` | `ARCHITECTURAL_FOUNDATION (postulate, not claim)` |
| `surviving_candidates` | `2 (1 inseparable claim)` |

## 4. Prediction Fields

| Field | Value |
|-------|-------|
| `sharpest_prediction` | `rho_eq(r) = -M^2/(2*tau^2*r^4) near any mass M` |
| `gr_matter_prediction` | `rho = 0 (vacuum exterior)` |
| `difference` | `negative energy halo scaling as M^2/r^4` |
| `controlling_parameter` | `tau (one free parameter)` |
| `prediction_sign` | `NEGATIVE (adverse for compact objects; anti-accelerating)` |
| `prediction_eos` | `w = -1` |

## 5. Adverse Consequence Fields

| Field | Value |
|-------|-------|
| `compact_object_consequence` | `WORSENED (XIII Gamma: f = -17.71; mass accumulates inward)` |
| `cosmological_consequence` | `ANTI-ACCELERATING (XII Alpha: rho_eq < 0 decelerates)` |
| `singularity_consequence` | `SOFTENED_NOT_BOUNCED (Appendix A)` |
| `dark_energy_replacement` | `PERMANENTLY_FAILED (XII Alpha: wrong sign)` |
| `consequences_are_predictions` | `true (not bugs)` |

## 6. Vulnerability Fields

| Field | Value |
|-------|-------|
| `lyapunov_vulnerability` | `NONE (algebraic theorem)` |
| `rho_eq_sign_vulnerability` | `NONE ((1/2 - 1) = -1/2 is fixed)` |
| `tau_vulnerability` | `HIGH (free parameter; determines all magnitudes)` |
| `minimal_coupling_vulnerability` | `MODERATE (a choice; conformal gives different T^Phi)` |
| `x_profile_vulnerability` | `LOW (Newtonian leading order; GR corrections exist)` |

## 7. Program Scope Fields

| Field | Value |
|-------|-------|
| `native_derived` | `forward semigroup, Lyapunov, rho_eq, w=-1, modified TOV` |
| `extension_level` | `soliton matter, gauge, HIC, carrier, CCBG, 26 zero-cost bio targets` |
| `conditional` | `Lindblad decoherence (postulated L), cosmological regulator (tau-dependent)` |
| `absent` | `fermions (3-layer obstruction), Born rule, outcome selection` |
| `collapsed` | `compact-object metric support (XVI Alpha sign error)` |

## 8. Next-Stage Fields

| Field | Value |
|-------|-------|
| `priority_1` | `constrain tau from observation` |
| `priority_2` | `compute rho_eq effect on binary-pulsar timing precision` |
| `priority_3` | `compute 3-regime H*tau cosmological signature` |
| `priority_4` | `gravitational lensing prediction from equilibrium scalar` |
| `priority_5` | `second-wave quantum (Q-II)` |
| `priority_6` | `fermion obstruction resolution` |

## 9. Revised Identity Fields

| Field | Value |
|-------|-------|
| `program_identity` | `Dissipative-vacuum-response constitutive architecture with one irreducible structural claim` |
| `irreducible_core` | `rho_eq = -X^2/(2tau^2), w = -1 on any GR background` |
| `one_postulate` | `tau dPhi/dt + Phi = X` |
| `one_free_parameter` | `tau` |
| `toe_status` | `CONDITIONALLY_REOPENABLE (if tau constrained + fermion obstruction resolved)` |
| `gravity_identity` | `Matter/organization theory within Einstein gravity; equilibrium scalar modifies T_ab` |

## 10. Minimal Serialized State

```json
{
  "program_phase": "BOOK_XVI_BETA",
  "stage": "irreducible_structural_claim_identification",

  "irreducible_claim": {
    "equation": "rho_eq = -X^2/(2*tau^2)",
    "eos": "w = -1",
    "derivation": "3-step algebra from tau*dPhi/dt + Phi = X + Phase 4",
    "verification": "xAct computer algebra",
    "postulates": 1,
    "free_parameters": 1,
    "adversarial_robust": true
  },

  "candidates": {
    "1_time_reversal": "SURVIVES",
    "2_tphi": "SURVIVES",
    "3_decoherence": "FAILS_C2",
    "4_biology": "EXTENSION_LEVEL",
    "5_vacuum": "FOUNDATION"
  },

  "prediction": {
    "sharpest": "rho_eq(r) = -M^2/(2*tau^2*r^4) near mass M",
    "gr_comparison": "GR predicts rho = 0 in vacuum",
    "sign": "NEGATIVE",
    "consequence": "adverse (worsens interiors; anti-accelerates)",
    "controlling_parameter": "tau"
  },

  "program": {
    "compact_object_frontier": "COLLAPSED (XVI Alpha)",
    "biology_scaffold": "INTACT (extension level)",
    "quantum": "CONDITIONAL (postulated L)",
    "surplus": {"demonstrated": 0, "conditional": 0},
    "next": "constrain tau from observation"
  },

  "cost": {"committed": "16/11/1/6", "change": "ZERO"}
}
```

---

*Structural Claim State Model complete. One irreducible claim. One postulate. One free parameter. Adverse consequences are predictions. Next: constrain tau.*
