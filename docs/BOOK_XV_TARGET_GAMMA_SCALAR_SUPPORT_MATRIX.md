# Book XV — Target Gamma: Scalar Support Matrix

---

## Table 1 — Scalar Source Reconstruction

| Step | Formula | Value at R_eq (λ=25) | Source |
|------|---------|---------------------|--------|
| Defect sigma | Σ_defect from D9 Picard | 0.446 | D9 convergent BVP |
| Effective mass | m_eff = M + β_XR × Σ_defect | 0.946 | D7/D8 amplification model |
| Amplified rate | A_eff = A_crit × m_eff/M | 2.01 | D7/D8 amplification model |
| Macro energy | ε = A_eff² × M²/(2τ²r⁴) | 27.24 | D7/D8 profile ansatz |
| Macro support | Σ_macro = ∫4πr²ε dr | 9.73 | Integration of above |
| Metric | f = 1 − 2(M − Σ_total)/r | +59.1 | D9/D6 injection formula |

---

## Table 2 — Sign / Normalization Audit

| Contribution | Expression | Sign | Value at R_eq | Physically anchored? |
|-------------|-----------|------|--------------|---------------------|
| Macro kinetic | (1/2)Φ̇² = A_eff²M²/(2τ²r⁴) | **+** | +27.24 | **CONDITIONAL** (profile ansatz) |
| Equilibrium deficit | −M²/(2τ²r⁴) | **−** | −6.75 | YES (Phase 4 derived) |
| Defect gradient | η²[(f')²+f²/r²]+V | **+** | +0.01 | YES (D9 BVP) |
| **Net ρ** | Sum | **+** | **+20.50** | **CONDITIONAL on A_eff** |

---

## Table 3 — Energy-Condition Audit

| Condition | At A_eff ~ 2 | At A = 1 | At A = 0 (static) |
|-----------|-------------|---------|-------------------|
| WEC (ρ ≥ 0) | **SATISFIED** (+20.5) | Barely (+0.86) | **VIOLATED** (−6.75) |
| NEC (ρ + p_r ≥ 0) | **SATISFIED** (Φ̇² > 0) | Satisfied | **SATURATED** (= 0) |
| Interior type | REPULSIVE (f > 1) | Near Schwarzschild | ADVERSE (f = −17.71) |

---

## Table 4 — Compactness / Mass Profile

| Radius | m(r) | f(r) | 2m/r | Interpretation |
|--------|------|------|------|---------------|
| R_eq = 1/3 | −9.7 | +59.1 | −58.1 | **REPULSIVE interior** |
| r = 0.5 | −5.5 | +22.8 | −22.0 | Repulsive |
| r = 1.0 | −1.3 | +3.6 | −2.6 | Repulsive |
| r = 1.5 | −0.06 | +1.08 | −0.08 | Near flat |
| R_ext = 2.0 | +0.5 | +0.50 | +0.50 | Schwarzschild |

**The interior is NOT compact. It is repulsive throughout (f > 1; no horizon; no trapping).**

---

## Table 5 — Defect Necessity Reclassification

| Aspect | Previous framing | Post-Gamma reality |
|--------|-----------------|-------------------|
| Defect energy fraction | "Crucial Component B" | **0.04% of total** |
| Defect role | "Structural support" | **Catalytic trigger for A_eff amplification** |
| Without defect (A = A_crit) | "Fails" | Net ρ ≈ +0.86 (barely positive; marginal) |
| With defect (A_eff ~ 2) | "Rescues" | Net ρ ≈ +20.5 (overwhelming; 24× marginal case) |
| Frontier description | "Defect-assisted equilibrium" | **Scalar-kinetic-dominated with defect-catalyzed amplification** |

---

## Table 6 — Independent Scalar-Solve Readiness

| Requirement | Status | Difficulty |
|-------------|--------|-----------|
| Scalar EOM known | YES (Phase 4 §D) | — |
| Background (Schwarzschild + defect) known | YES (D9 provides profiles) | — |
| Boundary conditions standard | YES (Φ → X at large r; regular at origin) | — |
| Code pathway | PARTIALLY EXISTS (tov_interior.py solves static; dynamic case needs extension) | MODERATE |
| **What it would determine** | **Whether Φ(r) naturally produces A_eff ~ 2 on the combined background** | — |
| Estimated effort | ~150–300 lines of code | — |

---

## Table 7 — Hard-Criteria Matrix

| Criterion | Assessment |
|-----------|-----------|
| Source transparency | **PASS** (fully reconstructed) |
| Sign clarity | **PASS** (all correct) |
| Normalization credibility | **CONDITIONAL** (correct for assumed profile; A_eff unverified) |
| Negative-mass interpretation | **REPULSIVE INTERIOR** (not compact support) |
| Defect necessity | **RECLASSIFIED** (catalyst 0.04%, not structure) |
| A_eff proxy status | **EFFECTIVE MODEL** (D7/D8; not independently solved) |
| Restored surplus | **NOT JUSTIFIED** (pending A_eff validation) |
| Next stage | **INDEPENDENT SCALAR SOLVE** |

---

## Table 8 — Limitations

| Limitation | Severity |
|-----------|----------|
| A_eff proxy from D7/D8 model | **CRITICAL** |
| No independent Φ(r) solve | **CRITICAL** |
| Repulsive interior (not compact) | **SIGNIFICANT** |
| Defect negligible as energy source | **INTERPRETIVE** |
| Profile ansatz at A_eff ~ 2 unverified | **MODERATE** |

---

## Table 9 — Frontier Consequence

| Question | Answer |
|----------|--------|
| Frontier strengthened? | **RECENTERED** — from "equilibrium restored" to "scalar-support testing" |
| Strongest question? | **Independent scalar solve** — validates or invalidates A_eff |
| Framing? | **Scalar-support reality testing** (not compact-object equilibrium) |
| Surplus restored? | **NO** — proxy-supported conditional |

---

## Table 10 — Final Classification

| Aspect | Status |
|--------|--------|
| Verdict | **A — primarily proxy amplification; does not yet restore physically credible surplus** |
| XV Beta positivity | REAL within D7/D8 model |
| Physical credibility | UNRESOLVED (A_eff ~ 2 not independently derived) |
| Interior geometry | REPULSIVE (f > 1; not compact) |
| Defect role | CATALYST (0.04% energy; triggers amplification) |
| Next step | Independent scalar field solve on combined background |

---

*Scalar Support Matrix complete. Ten tables. Positivity is proxy-driven. A_eff ~ 2 not independently derived. Interior repulsive. Defect is catalyst. Next: independent scalar solve.*
