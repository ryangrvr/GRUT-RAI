# Book XIV — Target Alpha: GRUT-RAI Combined TOV State Model

## Machine-Readable State Model for Equilibrium-Survival Reasoning

---

## 1. Entity Types

| Entity | Description | Source |
|--------|-------------|--------|
| `layer_1_additive` | D6 additive scalar+defect on fixed Schwarzschild | D6 |
| `layer_2_portal_picard` | D9 defect under portal feedback; Picard iteration; convergent | D9 |
| `layer_3_metric_backreaction` | Full combined energy → self-consistent metric (ESTIMATED) | XIV Alpha |
| `equilibrium_branch` | A positive-metric combined equilibrium at specific λ | XIV Alpha |

---

## 2. Combined-Equilibrium Fields

| Variable | Type | Value | Description |
|----------|------|-------|-------------|
| `five_sector_action_defined` | bool | true | D8 §5.1: S_grav + S_macro + S_defect + S_trigger + S_portal |
| `coupled_field_equations_defined` | bool | true | Einstein + scalar EOM + defect hedgehog EOM |
| `layer_1_computed` | bool | true | D6 additive on fixed Schwarzschild |
| `layer_2_computed` | bool | true | D9 Picard iteration; convergent |
| `layer_3_computed` | bool | **false** | Metric back-reaction ESTIMATED, not computed |
| `d9_fmin_range` | str | "+0.37 to +0.46" | D9 self-consistent results (ALL λ positive) |
| `d9_all_constructive` | bool | true | All portal-coupling shifts are positive |

---

## 3. Proxy / Self-Consistent Fields

| Variable | Type | Value | Description |
|----------|------|-------|-------------|
| `defect_profile_self_consistent` | bool | **true** | D9 Picard iteration converges |
| `scalar_field_proxy` | bool | true | A_eff(r) model used; full Φ(r) not solved |
| `metric_self_consistent` | bool | **false** | Schwarzschild held fixed in D1–D10 |
| `metric_backreaction_estimated` | bool | true | Structural estimate from D7 scaling |
| `proxy_dependence_remaining` | str | "metric (Schwarzschild background)" | Layer 3 gap |

---

## 4. Branch-Existence Fields

| Variable | Type | Value | Description |
|----------|------|-------|-------------|
| `low_lambda_survives` | enum | LIKELY_YES | λ = 5–10: estimated f_min ~ +0.24 to +0.26 |
| `mid_lambda_survives` | enum | MARGINAL | λ = 25–50: estimated f_min ~ +0.01 to +0.15 |
| `high_lambda_survives` | enum | LIKELY_NO | λ ≥ 100: estimated f_min negative |
| `viable_window` | str | "~{5, 10, 25} (3 of 6 tested)" | Narrowed from full D1–D10 range |
| `window_narrowed` | bool | true | From 6 to ~3 values |

---

## 5. Positivity-Survival Fields

| Variable | Type | Value | Description |
|----------|------|-------|-------------|
| `d1d10_positivity_fully_survives` | bool | **false** | High λ likely fails under back-reaction |
| `d1d10_positivity_partially_survives` | bool | **true** | Low λ likely survives |
| `surplus_status` | str | "PARTIALLY_RECOVERED (low λ conditional)" | Up from "0 demonstrated"; not fully "demonstrated" |
| `surplus_authority` | str | "C2 (strong frontier) for low λ; C5 (failed) for high λ" | Split by parameter |

---

## 6. Stability Fields

| Variable | Type | Value |
|----------|------|-------|
| `stability_assessed` | bool | false |
| `surviving_branches_stable` | enum | UNKNOWN |
| `stability_gap` | str | "dynamical perturbation analysis not performed" |

---

## 7. Limitation / Failure Fields

| Variable | Type | Value |
|----------|------|-------|
| `metric_backreaction_exact` | bool | false |
| `high_lambda_fails` | bool | true (estimated) |
| `low_lambda_marginal` | bool | true (λ = 25 near threshold) |
| `scalar_adverse_permanent` | bool | true |
| `stability_open` | bool | true |

---

## 8. Frontier-Strength Fields

| Variable | Type | Value |
|----------|------|-------|
| `frontier_modestly_restored` | bool | true |
| `surplus_partially_recovered` | bool | true |
| `bridge_worthiness` | str | "STABILIZED_AT_NARROW_CONDITIONAL (up from FURTHER_WEAKENED)" |
| `equilibrium_path_alive` | bool | true |
| `equilibrium_window_narrowed` | bool | true |

---

## 9. Verdict Fields

| Field | Value | Authority |
|-------|-------|----------|
| `xiv_alpha_global_verdict` | `B_conditional_narrowed_survival` | XIV Alpha |
| `equilibrium_survives` | `CONDITIONAL (low λ)` | XIV Alpha |
| `proxy_partially_removed` | `YES (D9 defect; metric still fixed)` | XIV Alpha |
| `surplus_status` | `PARTIALLY_RECOVERED` | XIV Alpha |
| `next_stage` | `book_xiv_terminal_or_exact_layer3` | XIV Alpha |
| `cost_change` | `ZERO` | Analytical audit |

---

## 10. Minimal Serialized Example

```json
{
  "program_phase": "BOOK_XIV_ALPHA",
  "stage": "combined_self_consistent_tov_equilibrium_viability",

  "self_consistency_layers": {
    "layer_1_additive": {"status": "COMPUTED", "f_positive": "most_lambda"},
    "layer_2_portal_picard": {"status": "COMPUTED", "f_positive": "ALL_lambda", "convergent": true},
    "layer_3_metric_backreaction": {"status": "ESTIMATED", "low_lambda": "likely_survives", "high_lambda": "likely_fails"}
  },

  "equilibrium_window": {
    "d9_all_lambda": "f > 0 (6 of 6)",
    "estimated_post_backreaction": "f > 0 (~3 of 6: lambda = 5, 10, 25)",
    "narrowed": true,
    "high_lambda_fails": true
  },

  "surplus": {
    "pre_xiv": "0 demonstrated + 2-3 conditional",
    "post_xiv": "PARTIALLY_RECOVERED: low-lambda equilibrium conditional; high-lambda fails",
    "authority": "C2 (low lambda); C5 (high lambda)"
  },

  "frontier": {
    "modestly_restored": true,
    "equilibrium_alive": true,
    "window_narrowed": true,
    "bridge_worthiness": "stabilized_at_narrow_conditional"
  },

  "cost": {"change": "ZERO", "committed": "16/11/1/6"},

  "verdict": {
    "global": "B",
    "equilibrium_survives": "CONDITIONAL_LOW_LAMBDA",
    "next": "book_xiv_terminal"
  }
}
```

---

## 11. Integration Notes

### What GRUT-RAI Must Update

1. **D9 Picard iteration is ALREADY substantial self-consistency.** Books XI–XIII did not credit D9 properly. The defect profile IS iteratively solved under portal feedback.
2. **Layer 3 (metric back-reaction) is the remaining gap.** Structurally estimated; not exactly computed.
3. **Equilibrium window NARROWS under estimated back-reaction.** Low λ (5–25): likely survives. High λ (≥100): likely fails.
4. **Surplus PARTIALLY RECOVERED.** From "0 demonstrated" toward "conditional at low λ."
5. **Bridge-worthiness stabilized.** From "further weakened" to "stabilized at narrow conditional."

### What GRUT-RAI Must NOT Do

- Treat structural back-reaction estimate as exact computation
- Treat D9 as full metric self-consistency (it is defect-profile self-consistency)
- Treat low-λ survival as full D1–D10 restoration (only ~3 of 6 values survive)
- Treat any surviving branch as stable (stability not assessed)
- Ignore the high-λ failure

---

*GRUT-RAI Combined TOV State Model complete. Three layers identified. D9 already substantial. Metric back-reaction estimated. Low λ likely survives. High λ likely fails. Equilibrium narrowed but alive.*
