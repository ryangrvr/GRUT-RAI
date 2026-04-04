# BOOK XVI TARGET BETA — GRUT-RAI WEAK-FIELD STATE MODEL

**Companion state model for:** Book XVI Beta — Irreducible Constitutive Gravity and Tau-Constraint Audit
**Program:** GRUT Omni-ToE
**Phase:** G (Portal-UI Anamnesis)
**Date:** 2026-04-04
**Classification:** Machine-Usable State Model

---

## 1. Irreducible-Claim Fields

| Field | Value |
|---|---|
| `claim_formula` | `rho_eq = -X^2 / (2 tau^2)` |
| `claim_eos` | `w = -1` |
| `claim_derivation_steps` | 3 |
| `claim_xact_verified` | `true` |
| `claim_postulates` | 1 |
| `claim_free_parameters` | 1 (`tau`) |

---

## 2. Reduction Fields

| Field | Value |
|---|---|
| `vs_gr_massive_scalar` | `REDUCIBLE_AT_EQUILIBRIUM` |
| `vs_r_squared` | `NOT_EQUIVALENT` (different scaling: `1/r^4` vs `1/r^6`) |
| `vs_semiclassical` | `NOT_EQUIVALENT` (different origin: classical vs quantum) |
| `equilibrium_irreducible` | `false` |
| `dynamics_irreducible` | `true` |

---

## 3. Weak-Field Derivation Fields

| Field | Value |
|---|---|
| `correction_formula` | `delta_f = -4 pi * M^2 / (tau^2 * r^2)` |
| `ppn_deviation` | `delta_beta = 4 pi / tau^2_geometric` |
| `source_identification` | `AMBIGUOUS` (`X = M/r^2` or `X = 0`) |
| `ricci_exterior` | `R = 0` (Schwarzschild vacuum) |

---

## 4. Observable / PPN Fields

| Field | Value |
|---|---|
| `mercury_delta_beta_at_tdyn` | `3.8e-22` |
| `earth_delta_beta_at_tdyn` | `1.1e-23` |
| `cassini_threshold` | `2.3e-5` |
| `any_detection_possible` | `false` |

---

## 5. Tau-Constraint Fields

| Field | Value |
|---|---|
| `cassini_tau_min_s` | `2.5e-3` |
| `nordtvedt_tau_min_s` | `1.2e-3` |
| `physical_tau_values` | `t_dyn >> 1 s always` |
| `tau_threatens_detection` | `false` |
| `tau_collapse` | `false` (formal bound exists but not physically relevant) |

---

## 6. Frontier-Status Fields

| Field | Value |
|---|---|
| `equilibrium_gravity_claim` | `REDUCIBLE_AND_SILENT` |
| `dynamics_claim` | `SURVIVES` (native dissipation, Lyapunov, time-reversal) |
| `weak_field_frontier` | `COLLAPSED` |
| `gravity_frontier` | `WEAKENED_SHARPLY` |
| `structural_novelty_locus` | `DYNAMICS_ONLY` |

---

## 7. Verdict Fields

| Field | Value |
|---|---|
| `global_verdict` | `A_REDUCIBLE_AND_SILENT` |
| `irreducibility` | `FAILS_AT_EQUILIBRIUM` |
| `observational_distinctness` | `SILENT` |
| `next_step` | Accept weak-field silence; gravity novelty is dynamical not equilibrium |

---

## JSON Serialization

```json
{
  "book": "XVI",
  "target": "Beta",
  "title": "Weak-Field State Model",
  "date": "2026-04-04",
  "irreducible_claim": {
    "claim_formula": "rho_eq = -X^2 / (2 tau^2)",
    "claim_eos": "w = -1",
    "claim_derivation_steps": 3,
    "claim_xact_verified": true,
    "claim_postulates": 1,
    "claim_free_parameters": 1,
    "free_parameter_name": "tau"
  },
  "reduction": {
    "vs_gr_massive_scalar": "REDUCIBLE_AT_EQUILIBRIUM",
    "vs_r_squared": "NOT_EQUIVALENT",
    "vs_semiclassical": "NOT_EQUIVALENT",
    "equilibrium_irreducible": false,
    "dynamics_irreducible": true
  },
  "weak_field_derivation": {
    "correction_formula": "delta_f = -4pi * M^2 / (tau^2 * r^2)",
    "ppn_deviation": "delta_beta = 4pi / tau^2_geometric",
    "source_identification": "AMBIGUOUS",
    "ricci_exterior": "R = 0"
  },
  "observable_ppn": {
    "mercury_delta_beta_at_tdyn": 3.8e-22,
    "earth_delta_beta_at_tdyn": 1.1e-23,
    "cassini_threshold": 2.3e-5,
    "any_detection_possible": false
  },
  "tau_constraint": {
    "cassini_tau_min_s": 2.5e-3,
    "nordtvedt_tau_min_s": 1.2e-3,
    "physical_tau_values": "t_dyn >> 1 s always",
    "tau_threatens_detection": false,
    "tau_collapse": false
  },
  "frontier_status": {
    "equilibrium_gravity_claim": "REDUCIBLE_AND_SILENT",
    "dynamics_claim": "SURVIVES",
    "weak_field_frontier": "COLLAPSED",
    "gravity_frontier": "WEAKENED_SHARPLY",
    "structural_novelty_locus": "DYNAMICS_ONLY"
  },
  "verdict": {
    "global_verdict": "A_REDUCIBLE_AND_SILENT",
    "irreducibility": "FAILS_AT_EQUILIBRIUM",
    "observational_distinctness": "SILENT",
    "next_step": "accept weak-field silence; gravity novelty is dynamical not equilibrium"
  }
}
```

---

*End of Book XVI Target Beta — GRUT-RAI Weak-Field State Model.*
