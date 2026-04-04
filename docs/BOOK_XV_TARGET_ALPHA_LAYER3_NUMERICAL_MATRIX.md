# Book XV — Target Alpha: Layer-3 Numerical Matrix

---

## Table 1 — Exact Layer-3 System

| Component | Equation / Field | D9 treatment | Layer 3 treatment |
|-----------|-----------------|-------------|------------------|
| Mass function m(r) | dm/dr = 4πr²ρ_total | FIXED (Schwarzschild) | **UPDATED each iteration** |
| Metric f(r) | 1 − 2m(r)/r | FIXED (1 − 2M/r) | **UPDATED from m(r)** |
| Defect f_defect(r) | Hedgehog ODE + portal | ITERATED (Picard) | ITERATED (on updated metric) |
| Macro A_eff(r) | D7/D8 amplitude model | Proxy | Proxy (unchanged) |
| Portal V_portal(r) | g_p Φ² |Φ⃗|² | From A_eff + f_defect | From A_eff + f_defect |

---

## Table 2 — Code Modification Requirements

| Modification | Existing file | Change required | Difficulty |
|-------------|-------------|----------------|-----------|
| Mass-function integration | self_consistent_coupling.py | Add dm/dr integration step in Picard loop | LOW |
| Metric-function update | self_consistent_coupling.py | Replace f = 1−2M/r with f(r) = 1−2m(r)/r | LOW |
| BVP on non-Schwarzschild | numerical_monopole.py | Pass f_metric(r) as background to BVP solver | MODERATE |
| Joint convergence | self_consistent_coupling.py | Add |Δm| and |Δf_metric| checks | LOW |
| **Total** | **~100–200 lines** | — | **MODERATE** |

---

## Table 3 — Structural Evidence for Low-λ Survival

| Evidence source | Finding | Direction | Confidence |
|----------------|---------|-----------|-----------|
| D7 back-reaction analysis | Source amplification > gravitational penalty by 12.7× | CONSTRUCTIVE | HIGH |
| D9 Picard iteration | All self-consistency shifts are POSITIVE (f_min increases) | CONSTRUCTIVE | HIGH |
| D8 portal sign | Portal coupling is STABILIZING (positive effective mass for defect) | CONSTRUCTIVE | HIGH |
| **Combined** | **Three convergent lines → low-λ f > 0 structurally supported** | **CONSTRUCTIVE** | **HIGH at λ=5,10; MODERATE at λ=25** |

---

## Table 4 — λ-Window Structural Assessment

| λ | D9 f_min | XIV Est. Δf | Est. corrected | Confidence | Classification |
|---|---------|------------|----------------|-----------|---------------|
| 5 | +0.376 | ~−0.12 | ~+0.26 | HIGH | LIKELY ROBUST |
| 10 | +0.417 | ~−0.18 | ~+0.24 | HIGH | LIKELY ROBUST |
| 25 | +0.448 | ~−0.30 | ~+0.15 | MODERATE | LIKELY CONDITIONAL |
| 50 | +0.457 | ~−0.45 | ~+0.01 | LOW | MARGINAL |
| 100 | +0.457 | ~−0.60 | ~−0.14 | HIGH (failure) | LIKELY FAILS |
| 200 | +0.452 | ~−0.80 | ~−0.35 | HIGH (failure) | LIKELY FAILS |

---

## Table 5 — Hard-Criteria Matrix

| Criterion | Assessment |
|-----------|-----------|
| System clarity | **PASS** (fully defined; code modifications enumerated) |
| Solve attempted | **NO** (computation not run) |
| Positivity survival | **STRUCTURALLY SUPPORTED** (three evidence lines; not exact) |
| Proxy independence | **PARTIAL** (metric fixing removed; macro proxy persists) |
| Branch robustness | **LIKELY ROBUST at λ=5,10** |
| Frontier strength | **MODESTLY STRENGTHENED** (well-defined + structurally supported) |

---

## Table 6 — Limitations

| Limitation | Severity |
|-----------|----------|
| Computation NOT RUN | KEY GAP |
| Macro amplitude still proxy | MODERATE |
| BVP solver needs modification | MODERATE (well-defined) |
| Nonlinear feedback untested | MODERATE |
| λ = 25 marginal | MODERATE |
| High-λ fails | EXPECTED |

---

## Table 7 — Frontier Consequence

| Question | Answer |
|----------|--------|
| Surplus restored? | **NO** (pending computation) |
| Equilibrium alive? | **YES** (structurally supported; computation defined) |
| Bridge-worthiness? | **STABILIZED** (would strengthen if computation confirms) |
| Next step? | **Implement and run Layer 3 Picard extension** |

---

## Table 8 — Final Classification

| Aspect | Status |
|--------|--------|
| Verdict | **B — structurally supported conditional with defined implementation** |
| Computation status | Fully defined; NOT run |
| Structural confidence | HIGH at low λ (5, 10); MODERATE at λ = 25 |
| Surplus | 0 demonstrated (pending) |
| Implementation path | ~100–200 lines code modification |
| Next | Implement and run |

---

*Layer-3 Numerical Matrix complete. Eight tables.*
