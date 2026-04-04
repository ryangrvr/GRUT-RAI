# Book XV — Target Alpha: GRUT-RAI Layer-3 State Model

---

## 1. Entity Types

| Entity | Description | Source |
|--------|-------------|--------|
| `layer3_picard` | Extended D9 Picard with metric update step | XV Alpha §4 |
| `metric_update_step` | dm/dr = 4πr²ρ_total → f(r) = 1−2m(r)/r inside iteration | XV Alpha §4.4 |
| `structural_evidence` | Three convergent lines supporting low-λ survival | XV Alpha §6 |

---

## 2. Exact-Layer3 Fields

| Variable | Type | Value |
|----------|------|-------|
| `system_defined` | bool | **true** |
| `code_modifications_specified` | bool | **true** |
| `code_modifications_lines` | str | "~100–200" |
| `computation_run` | bool | **false** |
| `implementation_difficulty` | str | "MODERATE (well-defined engineering task)" |

---

## 3. λ-Window Fields

| Variable | Type | Value |
|----------|------|-------|
| `lambda_primary` | list | [5, 10, 25] |
| `lambda_control` | list | [50] |
| `lambda_verification` | list | [100] |
| `low_lambda_confidence` | str | "HIGH (5, 10); MODERATE (25)" |
| `high_lambda_outcome` | str | "LIKELY FAILS (100, 200)" |

---

## 4. Convergence Fields

| Variable | Type | Value |
|----------|------|-------|
| `convergence_strategy` | str | "Extend D9 Picard with metric update; start from D9 converged profiles" |
| `under_relaxation` | str | "ω = 0.5 with fallback; additional metric under-relaxation may be needed" |
| `convergence_criteria` | str | "max|Δf_defect| + max|Δm| + max|Δf_metric| < 10⁻⁴" |
| `convergence_achieved` | bool | **false** (not run) |

---

## 5. Positivity-Survival Fields

| Variable | Type | Value |
|----------|------|-------|
| `structural_evidence_lines` | int | 3 |
| `evidence_convergent` | bool | true |
| `evidence_1_d7_scaling` | str | "Source amplification > gravitational penalty by 12.7×" |
| `evidence_2_d9_shifts` | str | "All D9 Picard shifts constructive (positive)" |
| `evidence_3_portal_sign` | str | "Portal coupling stabilizing (positive effective mass)" |
| `exact_positivity_confirmed` | bool | **false** (not computed) |

---

## 6. Branch-Robustness Fields

| Variable | Type | Value |
|----------|------|-------|
| `lambda_5_branch` | str | "LIKELY ROBUST (est. f_min ~+0.26; structural HIGH)" |
| `lambda_10_branch` | str | "LIKELY ROBUST (est. f_min ~+0.24; structural HIGH)" |
| `lambda_25_branch` | str | "LIKELY CONDITIONAL (est. f_min ~+0.15; structural MODERATE)" |
| `lambda_50_branch` | str | "MARGINAL (est. f_min ~+0.01)" |
| `lambda_100_branch` | str | "LIKELY FAILS (est. f_min ~−0.14)" |

---

## 7. Frontier-Strength Fields

| Variable | Type | Value |
|----------|------|-------|
| `surplus_demonstrated` | int | 0 |
| `surplus_status` | str | "Structurally supported conditional; pending exact computation" |
| `frontier_strength` | str | "MODESTLY STRENGTHENED from XIV (computation well-defined + convergent structural evidence)" |
| `bridge_worthiness` | str | "STABILIZED (would strengthen materially if computation confirms)" |
| `equilibrium_path_alive` | bool | true |

---

## 8. Next-Stage Fields

| Variable | Type | Value |
|----------|------|-------|
| `next_stage` | str | "Implement and run Layer 3 Picard extension at λ = 5, 10, 25" |
| `next_type` | str | "CODE IMPLEMENTATION (not analytical audit)" |
| `if_confirms` | str | "Surplus moves toward demonstrated in low-λ regime; bridge case strengthens" |
| `if_fails` | str | "Equilibrium path closed; Track 2 (transient collapse) sole remaining" |

---

## 9. Verdict Fields

| Field | Value |
|-------|-------|
| `xv_alpha_global_verdict` | `B_structurally_supported_conditional_with_defined_implementation` |
| `computation_run` | `NO` |
| `structural_confidence` | `HIGH at λ=5,10; MODERATE at λ=25` |
| `surplus_restored` | `NO (pending)` |
| `equilibrium_alive` | `YES` |
| `next_priority` | `implement_and_run_layer3` |
| `cost_change` | `ZERO` |

---

## 10. Minimal Serialized State

```json
{
  "program_phase": "BOOK_XV_ALPHA",
  "verdict": "B_structurally_supported_conditional",

  "layer3": {
    "system_defined": true,
    "code_modifications": "~100-200 lines",
    "computation_run": false,
    "structural_confidence": {"lambda_5": "HIGH", "lambda_10": "HIGH", "lambda_25": "MODERATE"},
    "evidence_lines": 3,
    "evidence_convergent": true
  },

  "frontier": {
    "surplus_demonstrated": 0,
    "surplus_conditional": "2-3 (structurally supported)",
    "equilibrium_alive": true,
    "bridge_worthiness": "STABILIZED",
    "next": "implement_and_run_layer3_picard"
  },

  "cost": {"committed": "16/11/1/6", "change": "ZERO"}
}
```

---

*Layer-3 State Model complete. System defined. Computation not run. Three convergent structural evidence lines. Frontier modestly strengthened. Next: implement and run.*
