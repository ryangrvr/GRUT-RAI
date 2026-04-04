# Book XV — Target Beta: Layer 3 Execution Matrix

---

## Table 1 — File Modifications

| File | Action | Lines | Purpose |
|------|--------|-------|---------|
| `grut/layer3_backreaction.py` | **CREATED** | ~290 | Layer 3 exact back-reaction computation |
| All existing modules | UNCHANGED | 0 | D9, BVP, TOV solvers untouched |

---

## Table 2 — Execution Setup

| Parameter | Value |
|-----------|-------|
| λ tested | 5, 10, 25, 50, 100 |
| g_portal | 1.0 |
| scalar_A | 1.062 (A_crit) |
| β_XR | 1.0 |
| Convergence tol | 10⁻⁴ |
| Max iterations | 30 |
| Starting point | D9 converged profiles |

---

## Table 3 — λ-by-λ Results

| λ | f(R_eq) | f_min (location) | m(R_eq) | ε_macro(R_eq) | ε_defect(R_eq) | f > 0 |
|---|---------|-----------------|---------|---------------|----------------|-------|
| 5 | +28.5 | 0.50 (R_ext) | −4.6 | ~15 | ~0.010 | **YES** |
| 10 | +36.4 | 0.50 (R_ext) | −5.9 | ~19 | ~0.010 | **YES** |
| 25 | +59.1 | 0.50 (R_ext) | −9.7 | ~22 | ~0.010 | **YES** |
| 50 | +90.4 | 0.50 (R_ext) | −14.9 | — | — | **YES** |
| 100 | +136.1 | 0.50 (R_ext) | −22.5 | — | — | **YES** |

---

## Table 4 — Convergence

| λ | D9 converged | Layer 3 iterations | Layer 3 converged |
|---|-------------|-------------------|------------------|
| 5 | YES | 20 | YES |
| 10 | YES | 21 | YES |
| 25 | YES | 30 | YES |
| 50 | YES | 30 | YES |
| 100 | YES | 30 | YES |

---

## Table 5 — Energy Dominance

| Component | Contribution at R_eq (λ=25) | Fraction |
|-----------|---------------------------|----------|
| ε_macro (scalar kinetic at A_eff~2) | ~22.4 | **99.96%** |
| ε_defect (hedgehog gradient) | ~0.010 | 0.04% |
| **Total** | ~22.4 | 100% |

**The entire f > 0 story is the macro scalar kinetic energy at A_eff ~ 2.**

---

## Table 6 — Caveats

| Caveat | Severity | Detail |
|--------|----------|--------|
| **A_eff proxy dependence** | **CRITICAL** | Result entirely driven by A_eff ~ 2 from D7/D8 amplification model |
| **m(r) < 0 at small r** | **SIGNIFICANT** | Energy support exceeds gravitational mass |
| **Defect sector negligible** | MODERATE | 0.04% of total energy; irrelevant to metric positivity |
| **Layer 3 correction negligible** | LOW | Back-reaction < 0.1% of D9 result |
| **XIV Alpha estimates were wrong** | INFORMATIONAL | High λ does NOT fail; amplification overwhelms penalty |

---

## Table 7 — Frontier Consequence

| Question | Answer |
|----------|--------|
| f > 0 at Layer 3? | **YES — overwhelmingly (f = 28–136 at R_eq)** |
| Layer 3 correction size | NEGLIGIBLE (< 0.1%) |
| Surplus restored? | **CONDITIONAL** — depends on A_eff proxy realism |
| Equilibrium path closed? | **NO** — f > 0 at ALL tested λ |
| Bridge-worthiness? | **CONDITIONAL** — pending A_eff validation |
| Next question | Is A_eff ~ 2 from the D7/D8 model physically realized? |

---

## Table 8 — Final Classification

| Aspect | Status |
|--------|--------|
| Verdict | **B — conditional survival; stronger than structural estimate; A_eff caveat** |
| f > 0 | YES at ALL λ |
| Back-reaction | NEGLIGIBLE |
| Physical concern | Negative m(r); A_eff proxy dependence |
| Surplus | CONDITIONALLY RESTORED (pending A_eff validation) |
| Equilibrium path | ALIVE (not closing) |
| Next step | Validate A_eff proxy vs independent scalar field solve |

---

*Execution Matrix complete. Eight tables. f > 0 at all λ. Surplus conditionally restored. A_eff caveat is critical.*
