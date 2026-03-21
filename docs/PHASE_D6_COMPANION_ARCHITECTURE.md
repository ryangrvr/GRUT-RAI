# Phase D6 — Companion Architecture and Dual-Sector Metric Integration

This is an analytical assessment phase, not locked canon.

---

## A. Mission & Context

D5 classified the source coupling as `source_coupling_insufficient`. The minimal quadratic coupling into the O(3) defect ODE cannot recover the Component A amplitude — the EL-derived sign acts as an effective mass increase rather than a driving force.

D6 tests a different strategy: rather than coupling the two sectors within a single ODE, treat them as **independent additive sectors** in the effective stress-energy:

- **Sector 1 (Macro)**: GRUT scalar-memory — provides Component A (~1/r^4)
- **Sector 2 (Defect)**: Curvature-triggered O(3) hedgehog — provides Component B (~1/r^2)

The combined T_total = T_macro + T_defect is injected into the Phase 6 metric framework to test whether global metric positivity is restored.

| Prior Phase | Status |
|-------------|--------|
| Phase 6: f(R_eq) | LOCKED (-17.71) |
| Phase 6B: A_crit | LOCKED (1.062) |
| Phase 6C: deficit | LOCKED (Component A + Component B) |
| Route C (all kernels) | LOCKED (insufficient) |
| Route B (all channels) | LOCKED (closed) |
| Source-Law Program I | LOCKED (partially viable, no GRUT-native) |
| Defect D1 | LOCKED (provisional candidate formulated) |
| Defect D2 | LOCKED (defect_candidate_numerically_viable) |
| Unification D3 | LOCKED (scalar_triplet_embedding_most_promising) |
| Unification D4 | LOCKED (component_a_shape_recovered_but_interpretation_not_yet_verified) |
| Source-Coupled D5 | LOCKED (source_coupling_insufficient) |

**Goal**: Determine whether the dual-sector additive architecture restores metric positivity for at least one macro baseline (A=1 or A=A_crit) across the lambda scan.

---

## B. Two Macro Baselines

Two macro baselines are tested at every lambda value:

| Baseline | Scalar A | Scientific Strength | Interpretation |
|----------|----------|---------------------|----------------|
| Companion-Baseline (A=1) | 1.0 | Strong | Clean structural test: macro provides plain Component A, defect must supply the missing Component B to close the deficit |
| Companion-Critical (A=A_crit) | 1.062 | Weaker | Permissive test: macro already near rescue by itself, defect provides additional support |

A positive result at A=1 is the stronger scientific statement. A positive result only at A=A_crit is weaker (could be "overshoot + defect").

---

## C. Curvature Trigger and Activation Law

### Kretschner curvature

    sqrt(K)(r) = sqrt(48) * M / r^3

| Location | sqrt(K) |
|----------|---------|
| R_eq = 1/3 | 93.53 |
| r = 0.5 | 27.71 |
| R_ext = 2.0 | 0.43 |

Core-to-exterior ratio: **216x**.

### Activation law

The defect SSB occurs when the curvature trigger exceeds the broken-phase mass:

    xi * sqrt(K)(r) > |m_0^2| = lambda * eta^2

This defines:

    K_crit = lambda * eta^2 / xi

    r_act = (xi * sqrt(48) * M / (lambda * eta^2))^(1/3)

At default parameters (xi=1, lambda=8*pi, eta^2=1/(8*pi)):

    K_crit = 1.0
    r_act = 1.5131

The activation function Theta(r) = Heaviside(xi*sqrt(K)(r) - lambda*eta^2) specifies:
- **Active at R_eq**: YES (93.53 >> 1.0)
- **Active at R_ext**: NO (0.43 < 1.0)

---

## D. Macro Sector (Analytic)

    epsilon_macro(r) = A^2 * M^2 / (2*tau^2*r^4) = A^2 * RHO_EQ_COEFF / r^4
    Sigma_macro(r) = A^2 * MASS_COEFF * (1/r - 1/R_ext)

| Quantity | A=1 | A=A_crit |
|----------|-----|----------|
| Sigma_macro(R_eq) | 2.618 | 2.953 |

---

## E. Defect Sector (Numerical)

The D2 hedgehog BVP is solved at matched eta^2 = 1/(8*pi) and interpolated onto the interior grid [R_eq, R_ext].

    Sigma_defect(r) = integral_r^R_ext 4*pi*r'^2 * epsilon_defect dr'

At default lambda = 8*pi:
- Sigma_defect(R_eq) = 0.416
- Defect fraction of total Sigma at R_eq: ~14% (A=1), ~12% (A=A_crit)

---

## F. Sector Dominance

At A=1 (default lambda):
- **Crossover radius**: ~1.67 (macro = defect)
- **At R_eq**: Macro dominates by ~279x (1/r^4 >> 1/r^2 at small r)
- **At R_ext**: Defect dominates (1/r^2 > 1/r^4 at large r)

This is the expected structure: macro provides the deep-core support (Component A), defect provides the intermediate-radius support (Component B).

---

## G. Metric Injection

    f_corrected(r) = -2*(delta(r) - Sigma_total(r))/r

where delta(r) = m(r) - r/2 and Sigma_total = Sigma_macro + Sigma_defect.

At default lambda = 8*pi:

| Baseline | f_min | Metric Positive |
|----------|-------|-----------------|
| A=1 | +0.498 | YES |
| A=A_crit | +0.500 | YES |

---

## H. Lambda Scan

Six lambda values scanned at both baselines:

| lambda | f_min (A=1) | Positive (A=1) | f_min (A_crit) | Positive (A_crit) | Defect frac (A=1) |
|--------|-------------|----------------|----------------|-------------------|--------------------|
| 5 | -0.977 | NO | +0.391 | YES | 6.1% |
| 10 | -0.493 | NO | +0.500 | YES | 8.8% |
| 25 | +0.492 | YES | +0.500 | YES | 13.7% |
| 50 | +0.500 | YES | +0.500 | YES | 17.2% |
| 100 | +0.500 | YES | +0.500 | YES | 19.9% |
| 200 | +0.500 | YES | +0.500 | YES | 21.7% |

**Key findings**:

1. **A=1 + defect restores metric positivity for lambda >= 25.** This is the strong result.
2. **A=A_crit + defect works for all lambda values.** This is the weaker (permissive) result.
3. **Defect fraction increases with lambda** (6% to 22%), as expected — larger lambda gives a more localized core and stronger angular gradient tail.
4. **Viable lambda window for A=1**: [25, 50, 100, 200].
5. **The threshold is between lambda=10 and lambda=25.**

---

## I. Cross-Term Inventory

Four neglected cross-terms explicitly documented:

| # | Name | Severity | Description |
|---|------|----------|-------------|
| 1 | Back-reaction | moderate | Defect stress-energy modifies metric, which modifies BVP domain |
| 2 | Scalar-defect coupling | moderate | Portal coupling |Phi|^2 |phi|^2 between sectors |
| 3 | Trigger self-consistency | minor | sqrt(K) evaluated on Schwarzschild, not corrected metric |
| 4 | Defect feedback on macro driver | significant | Defect modifies effective X(r) driving macro amplitude |

The additive approximation T_total = T_macro + T_defect is a **working hypothesis**, not justified from first principles. The most significant cross-term (#4) is that the macro amplitude A is treated as a free parameter independent of the defect sector.

---

## J. Classification

**Classification**: `companion_architecture_viable`

This means:
- The dual-sector additive architecture restores global metric positivity at A=1 for lambda >= 25
- Both Component A (macro) and Component B (defect) contribute as designed
- The defect sector provides 6-22% of the total Sigma (increasing with lambda)
- The result holds at the strong baseline (A=1), not just the permissive baseline (A=A_crit)

### What this classification does NOT mean:
- It does NOT prove the unified theory
- It does NOT justify the additive approximation (4 cross-terms neglected)
- It does NOT derive A=1 from first principles (A is a free parameter)
- It does NOT prove the curvature trigger is the correct mechanism
- The result is within the numerical framework only

### Phase lock update

| Phase | Status |
|-------|--------|
| Phase 6: f(R_eq) | LOCKED (-17.71) |
| Phase 6B: A_crit | LOCKED (1.062) |
| Phase 6C: deficit | LOCKED (Component A + Component B) |
| Route C (all kernels) | LOCKED (insufficient) |
| Route B (all channels) | LOCKED (closed) |
| Source-Law Program I | LOCKED (partially viable, no GRUT-native) |
| Defect D1 | LOCKED (provisional candidate formulated) |
| Defect D2 | LOCKED (defect_candidate_numerically_viable) |
| Unification D3 | LOCKED (scalar_triplet_embedding_most_promising) |
| Unification D4 | LOCKED (component_a_shape_recovered_but_interpretation_not_yet_verified) |
| Source-Coupled D5 | LOCKED (source_coupling_insufficient) |
| **Companion D6** | **ASSESSED (companion_architecture_viable)** |

---

## K. Numerical Validation Summary

- Benchmark: **60/60 checks PASSED**
- Pytest: **60/60 tests PASSED** (0.85s)
- Regression: **175/175 tests PASSED** (D4+D5+D6, 1.42s)
- 2 sectors defined (macro, defect)
- 2 macro baselines tested (A=1, A=A_crit)
- 6 lambda values scanned (all BVPs converge)
- 4 cross-terms inventoried
- Activation law explicitly defined
- Budget at key radii reported

---

## L. Nonclaims (10)

1. This phase does NOT prove the final unified theory.
2. A viable companion result establishes numerical feasibility, not physical derivation.
3. The additive stress-energy approximation neglects all cross-terms.
4. A positive D6 result at A=A_crit alone is weaker scientifically (could be 'overshoot + defect').
5. The best result is A=1 + defect restoring positivity.
6. The lambda scan is bounded, not exhaustive.
7. The curvature trigger threshold is a diagnostic, not a first-principles derivation.
8. Defect sector energy computed on Schwarzschild background, not self-consistent corrected metric.
9. The metric injection uses linearized deficit framework inherited from Phase 6.
10. Classification is within the D6 numerical framework only.

---

## M. Assumptions (10)

1. Dual-sector additive approximation: T_total = T_macro + T_defect (no cross-terms).
2. Macro sector uses the GRUT scalar-memory energy density: epsilon_macro = A^2 * M^2 / (2*tau^2*r^4).
3. Defect sector uses the D2 hedgehog BVP solution at matched eta^2 = 1/(8*pi).
4. Two macro baselines tested: A=1 (clean structural test) and A=A_crit=1.062 (permissive test).
5. Sigma_macro is analytic: A^2 * MASS_COEFF * (1/r - 1/R_ext).
6. Sigma_defect is numerical: integral_r^R_ext 4*pi*r'^2 * epsilon_defect dr'.
7. Curvature trigger activation law: defect active when xi * sqrt(K)(r) > |m_0^2| = lambda * eta^2.
8. Lambda scan over [5, 10, 25, 50, 100, 200] at both A=1 and A=A_crit.
9. Cross-terms explicitly inventoried and documented as neglected.
10. Background metric held fixed (Schwarzschild); no back-reaction.

---

## N. Recommended Next Move

D6 establishes that the companion architecture is viable: A=1 + defect restores metric positivity for lambda >= 25. Possible next steps:

1. **Self-consistent coupled system**: Solve the metric + defect BVP simultaneously, with back-reaction. This would address cross-term #1 (back-reaction) and partially #3 (trigger self-consistency).

2. **Lambda convergence study**: Refine the threshold between lambda=10 and lambda=25 with finer scan (lambda = 15, 18, 20, 22).

3. **Source-amplitude derivation**: Derive the effective A from the GRUT dynamics rather than treating it as a free parameter. This addresses cross-term #4.

4. **Activation law refinement**: Test whether a smooth activation function (sigmoid instead of Heaviside) changes the viable lambda window.

5. **Component B budget accounting**: Quantify exactly how much of Component B comes from the defect angular gradient vs. the defect potential term.
