# Book XV — Target Delta: GRUT-RAI Scalar Solve State Model

---

## 1. Scalar-EOM Fields

| Field | Value |
|-------|-------|
| `eom_defined` | `true` |
| `eom_radial` | `Phi'' + (2/r + f'/(2f))Phi' + (1/(f*tau^2))(Phi - X*tau) = 0` |
| `background` | `Schwarzschild + defect energy (combined X(r))` |
| `bvp_converged` | `true` |

## 2. Solved-Profile Fields

| Field | Value |
|-------|-------|
| `phi_sol_Req` | `-6.13 (NEGATIVE; non-equilibrium)` |
| `phi_eq_Req` | `+9.70 (= X*tau; POSITIVE)` |
| `branch_type` | `NON_EQUILIBRIUM (Phi < 0 when X > 0)` |
| `rho_net_Req` | `+52.2 (large positive; from V - Phi*J with Phi < 0)` |
| `spatial_kinetic_Req` | `0.030 (tiny)` |

## 3. Amplification-Comparison Fields

| Field | Value |
|-------|-------|
| `proxy_eps_Req` | `23.6 (temporal kinetic from A_eff ~ 2)` |
| `independent_kinetic_Req` | `0.030 (spatial gradient)` |
| `ratio` | `0.001 (1000x discrepancy)` |
| `comparison_valid` | `false (REGIME MISMATCH: temporal vs spatial)` |
| `a_eff_validated` | `false` |
| `a_eff_invalidated` | `false` |
| `comparison_status` | `UNRESOLVED (static BVP wrong tool for temporal question)` |

## 4. Sign / Energy Fields

| Field | Value |
|-------|-------|
| `bvp_energy_positive` | `true (rho_net = +52.2)` |
| `bvp_energy_mechanism` | `V - Phi*J with Phi < 0, J > 0 (potential + coupling)` |
| `proxy_energy_mechanism` | `(1/2)Phi_dot^2 (temporal kinetic)` |
| `mechanisms_same` | `false (DIFFERENT physics)` |

## 5. Constitutive-Stability Fields

| Field | Value |
|-------|-------|
| `phi_negative_at_equilibrium` | `NO (constitutive drives Phi -> X > 0)` |
| `bvp_branch_constitutively_stable` | `UNKNOWN (stability analysis not performed)` |
| `bvp_branch_physical` | `UNCLEAR (Phi < 0 is non-equilibrium)` |

## 6. Frontier Fields

| Field | Value |
|-------|-------|
| `surplus_restored` | `false (proxy unvalidated)` |
| `equilibrium_alive` | `true (not closed; unresolved)` |
| `frontier_status` | `RECENTERED: proxy amplification unresolved; time-dependent analysis needed` |
| `bridge_worthiness` | `UNCHANGED (still too weak)` |

## 7. Next-Stage Fields

| Field | Value |
|-------|-------|
| `option_a` | `Time-dependent scalar solve (hard; directly tests A_eff)` |
| `option_b` | `Constitutive-stability analysis of BVP branch (moderate)` |
| `option_c` | `Book XV Terminal freeze (honest; regime-mismatch acknowledged)` |
| `recommended` | `option_c (terminal freeze; fundamental regime issue identified)` |

## 8. Verdict Fields

| Field | Value |
|-------|-------|
| `xv_delta_verdict` | `A_does_not_validate_proxy_regime_mismatch` |
| `comparison_valid` | `false` |
| `proxy_validated` | `false` |
| `proxy_invalidated` | `false` |
| `surplus_restored` | `false` |
| `cost_change` | `ZERO` |

## 9. Minimal Serialized State

```json
{
  "program_phase": "BOOK_XV_DELTA",
  "stage": "independent_scalar_solve_amplification_validation",

  "bvp_result": {
    "converged": true,
    "phi_sol_Req": -6.13,
    "phi_eq_Req": 9.70,
    "branch": "NON_EQUILIBRIUM (Phi < 0)",
    "spatial_kinetic_Req": 0.030,
    "rho_net_Req": 52.2
  },

  "comparison": {
    "proxy_eps_Req": 23.6,
    "ratio": 0.001,
    "regime_match": false,
    "reason": "temporal vs spatial; fundamentally different physics",
    "a_eff_validated": false,
    "a_eff_invalidated": false,
    "status": "UNRESOLVED"
  },

  "frontier": {
    "surplus_restored": false,
    "equilibrium_alive": true,
    "status": "proxy_unvalidated_time_dependent_needed",
    "next": "terminal_freeze_or_time_dependent_analysis"
  },

  "cost": {"committed": "16/11/1/6", "change": "ZERO"}
}
```

---

*Scalar Solve State Model complete. BVP converges but regime-mismatched. A_eff neither validated nor invalidated. Frontier: proxy unresolved.*
