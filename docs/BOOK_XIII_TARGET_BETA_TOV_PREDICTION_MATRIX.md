# Book XIII — Target Beta: TOV Prediction Matrix

## Companion Reference Tables for Book XIII Beta

---

## Table 1 — Modified TOV System Definition

| Equation | Expression | Source | Status |
|----------|-----------|--------|--------|
| Mass function | dm/dr = 4πr²ρ_total | Phase 4 §D | CLOSED |
| Lapse function | dν/dr = [m + 4πr³p_r] / [r(r − 2m)] | Phase 4 §D | CLOSED |
| Anisotropic TOV | dp_r/dr = −(ρ + p_r)dν/dr + (2/r)(p_⊥ − p_r) | Phase 4 §D | CLOSED |
| Φ field equation | Φ'' + (2/r + ν' − h'/(2h))Φ' + h(Φ/τ² − X/τ) = 0 | Phase 4 (covariant EOM) | CLOSED |
| ρ_Φ | (1/2)(Φ')²h + Φ²/(2τ²) − ΦX/τ | Phase 4 §B | Algebraic |
| p_r,Φ | (1/2)(Φ')²h − Φ²/(2τ²) + ΦX/τ | Phase 4 §B | Algebraic |
| p_⊥,Φ | −(1/2)(Φ')²h − Φ²/(2τ²) + ΦX/τ | Phase 4 §B | Algebraic |
| **System closure** | **4 ODEs; all components algebraically specified** | — | **CLOSED** |

---

## Table 2 — EOS / Parameter Strategy

| Choice | Options | EOS-independent? | Required for |
|--------|---------|-----------------|-------------|
| Nuclear EOS (outer zone) | SLy, APR, BSk family, etc. | NO (standard NS choice) | M-R curves |
| τ | ~10⁻⁵ s (structurally motivated) | YES (canon-motivated) | All predictions |
| X(r) | Fixed-background or self-consistent | YES (structural) | Integration |
| Central Φ_c | Scan parameter | YES (free) | Branch structure |
| R_core (zone transition) | Self-consistently determined | YES (emergent) | Two-zone model |
| **Structural predictions** | — | **YES (EOS-independent)** | Buchdahl, two-zone, mass deficit |
| **Quantitative M-R curves** | — | **NO (EOS-dependent)** | Data comparison |

---

## Table 3 — Structural Predictions (Available Without Full Numerical Integration)

| # | Prediction | Basis | GR counterpart | GRUT-distinctive? |
|---|-----------|-------|---------------|-------------------|
| 1 | **Relaxed Buchdahl bound: C > 8/9 permitted** | ρ_eq < 0 violates Buchdahl hypothesis | C ≤ 8/9 (perfect fluid, ρ ≥ 0) | **YES — theorem-level** |
| 2 | **Two-zone architecture: nuclear outer + GRUT inner** | T^Φ sector activates at high compactness | Single-zone nuclear (standard NS) | **YES — new architecture class** |
| 3 | **Non-monotonic mass profile: dm/dr < 0 in inner zone** | ρ_eq < 0 → mass decreases inward | dm/dr > 0 always in GR (ρ > 0) | **YES — qualitatively new** |

---

## Table 4 — Qualitative Branch Structure (Inferred)

| Branch | Central density regime | GRUT interior activated? | Mass behavior | Compactness | Status |
|--------|----------------------|-------------------------|-------------|------------|--------|
| Standard | Low to moderate | NO | M increases with ρ_c | C < 8/9 | Standard GR-compatible |
| Near maximum mass | High | Partially | M peaks (standard turning point) | C approaches 8/9 | Standard GR |
| **GRUT-modified** | **Very high** | **YES** | **M decreases (mass deficit)** | **C can exceed 8/9** | **New branch (stability unknown)** |
| **Ultra-compact remnant** | **Extreme** | **Extensive inner zone** | **Low total M (large deficit)** | **C ≫ 8/9** | **Structural prediction (stability unknown)** |

---

## Table 5 — Stability / Branch-Status

| Configuration | Stability | Method required | Status |
|--------------|-----------|----------------|--------|
| Standard branch | STABLE (below turning point) | Known (standard TOV) | Established |
| Standard maximum mass | UNSTABLE above | Turning-point criterion | Established |
| GRUT-modified branch | **UNKNOWN** | Numerical M(ρ_c) + turning-point | **NOT COMPUTED** |
| Ultra-compact (C > 8/9) | **UNKNOWN** | Dynamical perturbation analysis | **NOT COMPUTED** |

---

## Table 6 — Comparison-Readiness

| Observable | GRUT prediction type | Comparison-ready? | Gap |
|-----------|---------------------|------------------|-----|
| M(R) mass-radius | STRUCTURAL (branch existence) | **NOT YET** | Numerical M-R curves needed |
| M_max | CONDITIONAL (may shift) | **NOT YET** | Numerical turning-point analysis needed |
| C > 8/9 existence | STRUCTURAL (Buchdahl violated) | **PARTIALLY** | Exact maximum C unknown |
| Non-monotonic m(r) | STRUCTURAL (ρ < 0 interior) | NOT DIRECTLY OBSERVABLE | Internal structure |
| Tidal Λ(M) | NOT COMPUTED | **NOT YET** | Perturbation theory needed |

---

## Table 7 — Hard-Criteria Pass/Fail Matrix

| Criterion | Assessment |
|-----------|-----------|
| System closure | **PASS** (four coupled ODEs; all components specified) |
| Quantitative outputs | **PARTIAL** (structural predictions derived; M-R curves uncomputed) |
| Traceability to surplus | **PASS** (all from ρ_eq < 0, Phase 4 / D1–D10) |
| Distinct from GR | **PASS** (relaxed Buchdahl, two-zone, non-monotonic m(r)) |
| EOS robustness | **STRUCTURAL predictions EOS-independent; M-R curves EOS-dependent** |
| Phenomenological specificity | **MODERATE** (specific but not comparison-ready) |
| Worth follow-up | **YES** (numerical integration is tractable) |

---

## Table 8 — Limitation / Failure Table

| Limitation | Severity | Resolution |
|-----------|----------|-----------|
| Full M-R curves uncomputed | **KEY** | Numerical integration of §4 system |
| X(r) self-consistency not solved | MODERATE | Picard iteration (as in D9) |
| Zone-transition physics approximate | MODERATE | Define GRUT-activation criterion |
| GRUT-branch stability unknown | SIGNIFICANT | Turning-point or perturbation analysis |
| Tidal deformability unformulated | SIGNIFICANT | Even-parity perturbation theory |
| **All limitations are COMPUTATIONAL** | — | Standard ODE/BVP numerics |

---

## Table 9 — Final Classification

| Aspect | Status |
|--------|--------|
| Verdict | **B — partial but real quantitative program** |
| System | CLOSED (four coupled ODEs) |
| Structural predictions | THREE (Buchdahl relaxed; two-zone; mass deficit) |
| Numerical M-R | UNCOMPUTED (tractable) |
| Branch stability | UNKNOWN |
| Comparison readiness | CONDITIONAL (predictions specific; curves needed) |
| Frontier status | STRENGTHENED |
| Next step | Numerical GRUT TOV integration |

---

*TOV Prediction Matrix complete. Nine reference tables covering system definition, EOS strategy, structural predictions, branch structure, stability, comparison readiness, hard criteria, limitations, and final classification.*
