# Book XV — Target Delta: Scalar Solve Matrix

---

## Table 1 — Scalar EOM Definition

| Component | Specification |
|-----------|-------------|
| EOM | □Φ + Φ/τ² − X/τ = 0 |
| Radial reduction | Φ'' + (2/r + f'/(2f))Φ' + (1/(fτ²))(Φ − Xτ) = 0 |
| Background metric | f(r) = 1 − 2M/r (Schwarzschild) |
| Source | X(r) = m_total(r)/r² (Schwarzschild + defect energy) |
| Static equilibrium | Φ_eq = X·τ (from EOM with Φ'' = Φ' = 0) |

---

## Table 2 — Solver Implementation

| Aspect | Value |
|--------|-------|
| Method | scipy.solve_bvp |
| Grid | 300 points, R_eq+0.001 to R_ext |
| Inner BC | Φ'(R_eq) = 0 (regularity) |
| Outer BC | Φ(R_ext) = X(R_ext)·τ (equilibrium) |
| Initial guess | Φ = X·τ everywhere |
| Tolerance | 10⁻⁶ |
| Convergence | **YES** |

---

## Table 3 — BVP Solution Profile

| r | Φ_sol | Φ_eq (X·τ) | ρ_kin (spatial) | ρ_net | ε_proxy (D7/D8) |
|---|-------|-----------|----------------|-------|-----------------|
| 0.345 | **−6.13** | +9.70 | 0.030 | +52.2 | 23.6 |
| 0.501 | **−5.67** | +4.59 | 0.056 | +28.1 | 5.28 |
| 0.752 | **−4.65** | +2.01 | 0.116 | +13.5 | 1.01 |
| 1.00 | **−3.34** | +1.10 | 0.160 | +6.35 | 0.31 |
| 1.50 | **−1.12** | +0.40 | 1.83 | +2.55 | 0.04 |
| 2.00 | +0.15 | +0.15 | 0.88 | +0.87 | 0.006 |

---

## Table 4 — Amplification Comparison

| Quantity | D7/D8 proxy | Independent BVP | Ratio |
|----------|------------|----------------|-------|
| Energy type | Temporal kinetic (1/2)Φ̇² | Spatial kinetic (1/2)(Φ')²f | DIFFERENT |
| Value at R_eq | 23.6 | 0.03 | **0.001** |
| Physical regime | Dynamic processing | Static profile | **MISMATCHED** |
| Mechanism | Active relaxation at A_eff ~ 2 | Spatial gradient of Φ(r) | DIFFERENT |
| **Comparable?** | — | — | **NO** |

---

## Table 5 — Energy Mechanism Comparison

| Aspect | D7/D8 proxy (XV Beta) | BVP non-equilibrium branch |
|--------|----------------------|---------------------------|
| Energy source | (1/2)Φ̇² (temporal kinetic) | V − ΦJ (potential + coupling; Φ < 0, J > 0) |
| Sign mechanism | Kinetic always positive | V > 0 + (−ΦJ) > 0 because Φ < 0 |
| Physical regime | Dynamic approach to equilibrium | Static non-equilibrium spatial profile |
| Constitutive relevance | Models the relaxation process | Constitutive dynamics would push Φ → X > 0 |
| Physical status | Proxy model (unvalidated temporal rate) | Mathematical branch (constitutive stability unclear) |

---

## Table 6 — Defect Necessity (Unchanged from XV Gamma)

| Role | Status |
|------|--------|
| Direct energy contribution | 0.04% (negligible) |
| Function | Catalytic trigger for source amplification |
| Changed by XV Delta? | NO — defect role unchanged by BVP result |

---

## Table 7 — Hard-Criteria Matrix

| Criterion | Assessment |
|-----------|-----------|
| EOM clarity | **PASS** |
| Successful solve | **PASS** (BVP converges) |
| Comparability to proxy | **FAIL** (regime mismatch: temporal vs spatial) |
| Physical credibility | **PROBLEMATIC** (Φ < 0 branch; constitutive stability unclear) |
| Sign/energy interpretation | DIFFERENT mechanism; same positive sign |
| Surplus restored | **NOT SUPPORTED** (proxy unvalidated) |
| Next stage | Time-dependent analysis or terminal freeze |

---

## Table 8 — Limitations

| Limitation | Severity |
|-----------|----------|
| **Temporal vs spatial regime mismatch** | **FUNDAMENTAL** |
| **BVP finds non-equilibrium branch (Φ < 0)** | **SIGNIFICANT** |
| **1000× kinetic discrepancy** | EXPECTED (different physics) |
| **A_eff validation requires time-dependent solve** | **KEY GAP** |
| **Constitutive stability of BVP branch unknown** | **MODERATE** |

---

## Table 9 — Frontier Consequence

| Question | Answer |
|----------|--------|
| A_eff validated? | **NO — regime mismatch; static BVP cannot test temporal amplification** |
| A_eff invalidated? | **NO — static BVP is wrong tool** |
| Surplus restored? | **NO — still unresolved** |
| Frontier status | **RECENTERED** — time-dependent analysis needed |
| Next options | Time-dependent solve (hard) / constitutive-stability analysis (moderate) / terminal freeze (honest) |

---

## Table 10 — Final Classification

| Aspect | Status |
|--------|--------|
| Verdict | **A — does not validate proxy; regime mismatch; amplification unresolved** |
| BVP result | Converged; found Φ < 0 non-equilibrium branch |
| Comparison to proxy | REGIME MISMATCHED (temporal vs spatial) |
| Kinetic energy ratio | 0.001 (expected; different physics) |
| Surplus | NOT RESTORED (proxy unvalidated) |
| Next step | Terminal freeze or time-dependent analysis |

---

*Scalar Solve Matrix complete. Ten tables. BVP converges but regime-mismatched with proxy. A_eff neither validated nor invalidated. Surplus unresolved.*
