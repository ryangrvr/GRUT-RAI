# Phase D2 — Numerical Monopole Integration and Interior Metric Viability

This is a tested candidate extension, not locked canon.

---

## A. Mission & Context

Phase D1 formulated the O(3) triplet hedgehog defect as a provisional candidate extension with asymptotic tail eta^2/r^2 matching Component B. Phase D2 numerically solves the hedgehog BVP, extracts the full energy profile, and injects it into the established interior metric framework to test metric positivity restoration.

| Prior Phase | Status |
|-------------|--------|
| Phase 6: f(R_eq) | LOCKED (-17.71) |
| Phase 6B: A_crit | LOCKED (1.062) |
| Phase 6C: deficit | LOCKED (Component A + Component B) |
| Route C (all kernels) | LOCKED (insufficient) |
| Route B (all channels) | LOCKED (closed) |
| Source-Law Program I | LOCKED (partially viable, no GRUT-native) |
| Defect D1 | LOCKED (provisional candidate formulated) |

**Goal**: Determine whether the BVP-derived defect profile, combined with the scalar memory sector, can restore metric positivity in the interior.

---

## B. Numerical Method

### BVP Formulation

The hedgehog ODE from D1:

    f'' + (2/r)f' - (2/r^2)f - lam*eta^2*f*(f^2-1) = 0

is solved as a two-point BVP with scipy.solve_bvp:
- y[0] = f, y[1] = f'
- BC: f(r_min) ~ 0, f(r_max) = 1
- Initial guess: D1 analytic profile f(r) = r/sqrt(r^2 + delta^2)

The free parameter c_1 (slope at origin) is determined by the solver matching both boundaries simultaneously.

### Near-Origin Series

    f(r) ~ c_1 * r * (1 - lam*eta^2*r^2/10)

c_1 is estimated from delta_core = 1/sqrt(lam*eta^2) for the initial guess. The BVP solver refines this to c_1_effective.

---

## C. Core Regularity

The BVP solution is regular at the origin:
- f(r_min=0.01) ~ 0.015 (small, as expected)
- c_1_effective ~ 1.52 (default lambda=25)
- Max BVP residual: ~1e-6

Core energy density is finite and integrable. The core peak increases with lambda (smaller core, higher concentration), from ~0.015 (lam=5) to ~0.44 (lam=200).

---

## D. BVP Solution Quality

- Convergence: scipy.solve_bvp converges for all 6 tested lambda values
- Max RMS residual: < 1e-4 for all cases
- Boundary matching: f(r_max) = 1.000 to within 1e-4
- Profile: smooth monotonic increase from ~0 to 1

---

## E. Energy Profile

The three-term energy density:

    epsilon(r) = (1/2)*eta^2*(f')^2 + eta^2*f^2/r^2 + (1/4)*lam*eta^4*(f^2-1)^2

Key numerical results at default lambda=25:
- Core peak epsilon: 0.0558
- Integrated defect mass: 1.83
- Tail exponent: -1.66 (approaches -2.0 at higher lambda)
- Tail coefficient: 0.042 (target eta^2 = 0.0398)

The tail exponent monotonically approaches -2.0 as lambda increases:
- lam=5: -0.83
- lam=10: -1.24
- lam=25: -1.66
- lam=50: -1.84
- lam=100: -1.93
- lam=200: -1.97

---

## F. Two Coupling Modes

### Case A — Additive Diagnostic

Scalar memory at A_crit = 1.062 (critical overshoot) plus defect on top. Tests whether the defect stacked on the existing near-critical scalar rescue heals the metric.

### Case B — Reduced-Scalar / Hybrid

Scalar memory at A = 1.0 (baseline, just enough for Component A) plus defect providing Component B independently. This is the interpretively cleaner test: the defect must supply the missing 1/r^2 component.

---

## G. Metric Injection

The metric injection uses the established formula:

    delta(r) = m(r) - r/2
    m(r) = M + MASS_COEFF * (1/r - 1/R_ext)
    Sigma_scalar = A^2 * MASS_COEFF * (1/r - 1/R_ext)
    Sigma_defect = integral_r^R_ext 4*pi*r'^2 * epsilon_defect dr'
    f_corrected = -2*(delta - Sigma_total)/r

**Important**: The metric injection is evaluated only on the interior domain [R_EQ, R_ext] = [1/3, 2.0]. The BVP domain extends to r_max = 5.0 (to allow f -> 1), but the mass profile and Sigma formulas are valid only in the interior.

### Results (default lambda=25)

| Quantity | Case A | Case B |
|----------|--------|--------|
| Scalar amplitude | 1.062 | 1.000 |
| f_min | 0.500 | 0.492 |
| f_min location | r = R_ext | r = R_EQ |
| Metric positive | YES | YES |
| Defect fraction at R_EQ | 12.3% | 13.7% |
| Defect fraction at r=0.5 | 18.7% | 20.6% |
| Defect fraction at r=1.0 | 36.2% | 39.0% |

---

## H. Lambda Scan

Six lambda values tested at fixed eta^2 = 1/(8*pi):

| Lambda | Tail exponent | f_min (A) | f_min (B) | Positive A | Positive B | Defect frac @ R_EQ |
|--------|--------------|-----------|-----------|------------|------------|-------------------|
| 5 | -0.83 | 0.39 | -0.98 | YES | NO | 6.1% |
| 10 | -1.24 | 0.50 | -0.49 | YES | NO | 8.8% |
| 25 | -1.66 | 0.50 | 0.49 | YES | YES | 13.7% |
| 50 | -1.84 | 0.50 | 0.50 | YES | YES | 17.2% |
| 100 | -1.93 | 0.50 | 0.50 | YES | YES | 19.9% |
| 200 | -1.97 | 0.50 | 0.50 | YES | YES | 21.7% |

### Key findings

1. **Case A is always viable**: The A_crit scalar overshoot (A^2 ~ 1.128) already nearly closes the deficit. Any defect contribution makes f positive everywhere.

2. **Case B has a critical lambda**: Between lambda = 10 and lambda = 25, the defect becomes strong enough to independently supply Component B. Below this threshold, the defect tail is too shallow (exponent too far from -2.0).

3. **Defect fraction increases with lambda**: At R_EQ, the defect provides 6-22% of total Sigma depending on lambda. At larger radii (r=1.0), the fraction reaches 36-39%.

4. **f_min = 0.50 at R_ext**: When the metric is globally positive, the minimum is at the exterior boundary where f = 1 - 2M/R_ext = 0.5 (Schwarzschild value). The interior f is everywhere above this.

---

## I. Compatibility

1. **Component A intact**: The scalar memory sector is unchanged by defect addition. Sigma_scalar remains the analytic A^2*MASS_COEFF*(1/r - 1/R_ext) contribution.

2. **Coupling is additive**: T_total = T_scalar + T_defect. No replacement or hybridization of the scalar sector.

3. **Locked results preserved**: Phase 6 metric (f(R_eq) = -17.71) was computed WITHOUT the defect. The defect is a candidate extension that adds a new source term.

4. **Defect provides Component B shape**: The tail exponent approaches -2.0 monotonically as lambda increases, confirming the D1 asymptotic analysis.

---

## J. Classification

**Classification**: `defect_candidate_numerically_viable`

This means:
- The BVP solver converges for all tested lambda values
- The defect energy profile has the correct asymptotic 1/r^2 shape
- In Case A (additive), the metric is globally positive for ALL tested lambda values
- In Case B (hybrid), the metric is globally positive for lambda >= 25
- The defect provides 6-22% of total Sigma at R_EQ

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
| **Defect D2** | **TESTED (defect_candidate_numerically_viable)** |

---

## K. Numerical Validation Summary

- Benchmark: **58/58 checks PASSED**
- Pytest: **58/58 tests PASSED** (0.89s)
- BVP convergence: 6/6 lambda values
- Phase 6 baseline verified: f(R_eq) = -17.71
- Metric positivity tested for both coupling modes
- Sigma accounting at 4 key radii

---

## L. Nonclaims (10)

1. This phase does NOT prove the final particle sector.
2. This phase does NOT prove the defect sector is GRUT canon.
3. This phase does NOT identify eta as a literal electric charge.
4. A successful metric rescue establishes numerical viability, not full physical derivation.
5. A failed metric rescue does NOT invalidate D1 admissibility.
6. The additive coupling (Case A) may overstack support terms. Case B is the cleaner test.
7. The BVP solver uses finite-domain approximation (r_min > 0, r_max < infinity).
8. The static mass profile is inherited, not re-derived with the defect sector included self-consistently.
9. The lambda scan explores a bounded range.
10. The classification is within the tested numerical framework only.

---

## M. Assumptions (10)

1. The hedgehog ODE is solved as a two-point BVP. c_1 is the free matching parameter.
2. The near-origin expansion is used to initialize the BVP guess near r_min > 0.
3. The coefficient-matching condition eta^2 = 1/(8*pi) is held fixed. Lambda is scanned.
4. Two coupling modes are tested: Case A (A_crit + defect) and Case B (A=1 + defect).
5. The metric injection uses the established formula from Phase 6.
6. The static mass profile is inherited from Phase 6.
7. Sigma_scalar is the analytic scalar-memory contribution.
8. Sigma_defect is computed by numerical integration of the BVP-derived profile.
9. The lambda scan is bounded and disciplined, not exhaustive.
10. The background metric is held fixed. No self-consistent back-reaction.

---

## N. Recommended Next Move

Phase D2 establishes numerical viability. The next steps depend on the program direction:

1. **Self-consistent back-reaction**: Iterate the metric with the defect included as a source.
2. **Physical derivation of eta**: Can eta^2 = 1/(8*pi) be derived from GRUT parameters?
3. **Scalar-memory relation**: What is the relation between the O(3) triplet and the original GRUT scalar?
4. **Lambda determination**: What physical principle selects the coupling lambda?
5. **Stability analysis**: Is the hedgehog solution stable against small perturbations?
