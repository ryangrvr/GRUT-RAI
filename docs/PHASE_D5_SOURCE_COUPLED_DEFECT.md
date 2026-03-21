# Phase D5 — Source-Coupled Defect Dynamics and Component A Amplitude Recovery

This is an analytical assessment phase, not locked canon.

---

## A. Mission & Context

D4 classified the embedding+curvature architecture as `component_a_shape_recovered_but_interpretation_not_yet_verified`. The radial kinetic energy has the correct 1/r^4 functional form, but the coefficient ratio is 0.0035 — about 286x too weak. The missing amplitude might come from source-driving: the old scalar-memory model has Phi driven by X(r) ~ M/r^2 from matter.

D5 couples the triplet magnitude back to the GRUT source X(r) and tests whether this recovers the amplitude while preserving the topological Component B tail.

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

**Goal**: Determine whether minimal source coupling can recover the Component A amplitude (coefficient ratio ~ 1) while preserving Component B, honestly assessed via bounded gamma scan.

---

## B. Dimensional / Normalization Map

### Units convention

All D1-D5 computations use geometric units G = c = 1, with the Schwarzschild radius r_s = 2GM = 1 as the fundamental length scale.

| Quantity | Symbol | Value | Units/Dimensions |
|----------|--------|-------|------------------|
| Radial coordinate | r | — | r_s (Schwarzschild radii) |
| Reference length | r_* | 1.0 | r_s |
| External mass | M_ext | 0.5 | r_s / 2 (in G=c=1) |
| Equilibrium radius | R_eq | 1/3 | r_s |
| Defect profile | f(r) | 0 -> 1 | dimensionless |
| VEV | eta | 1/sqrt(8*pi) ~ 0.1995 | [1] in geometric units |
| VEV squared | eta^2 | 1/(8*pi) ~ 0.0398 | [1] |
| Self-coupling | lambda | 8*pi ~ 25.13 | dimensionless (in r_s-units) |
| Source coupling | gamma | scanned | dimensionless |
| Curvature coupling | xi | carried from D4 | dimensionless |
| Kretschner | sqrt(K) | sqrt(48)*M/r^3 | [1/r_s^2] |

### GRUT source bridge

The GRUT collapse driver in standard units:

    X_GRUT(R) = GM / R^2

In geometric units with r_s = 1, this becomes:

    X(r) = M_ext / r^2 = 0.5 / r^2

Reference source scale: X_* = M_ext / r_s^2 = 0.5

Dimensionless source: X_tilde(r_tilde) = X(r) / X_* = 1 / r_tilde^2

Since r_s = 1, the dimensional and dimensionless forms are numerically identical. No additional rescaling is needed — the GRUT driver enters the hedgehog ODE directly.

### ODE nondimensionalization

The dimensionless hedgehog ODE coefficients:

    Lambda_bar = lam * eta^2 = 1.0  (controls core size)
    Gamma_bar  = gamma * M_ext = gamma * 0.5  (source coupling strength)
    delta_core = 1/sqrt(Lambda_bar) = 1.0 r_s  (defect core scale)

Full sourced ODE (numerically identical to dimensionless form):

    f'' + (2/r)f' - (2/r^2)f - lam*eta^2*f*(f^2-1) - gamma*(M/r^2)*f = 0

---

## C. Source Coupling Candidates

Two structurally minimal couplings assessed:

### Quadratic (preferred)

    L_int = -(1/2) gamma X(r) |Phi|^2 = -(1/2) gamma X(r) eta^2 f^2

- Preserves O(3) symmetry
- Mirrors curvature coupling pattern (xi*C*|Phi|^2)
- Source-density-dependent effective mass
- 1 new parameter (gamma)

### Linear (comparison)

    L_int = -gamma |Phi| X(r) = -gamma eta f X(r)

- Breaks O(3) Mexican-hat symmetry explicitly
- Yukawa-like direct coupling
- 1 new parameter (gamma)

---

## D. Euler-Lagrange Sign Derivation

**Critical**: The source term sign is derived from the Lagrangian, not assumed.

### Quadratic coupling

    L_int = -(1/2) gamma X eta^2 f^2
    dL_int/df = -gamma X eta^2 f
    In EOM (divided by eta^2): -gamma X f

The **derived sign is NEGATIVE** for gamma > 0 and X > 0. This means positive gamma acts as an effective mass increase, opposing the hedgehog vacuum — not a driving force toward larger gradients.

### Sourced ODE

Standard hedgehog (D2):

    f'' + (2/r)f' - (2/r^2)f - lam*eta^2*f*(f^2-1) = 0

Sourced (quadratic):

    f'' + (2/r)f' - (2/r^2)f - lam*eta^2*f*(f^2-1) - gamma*M*f/r^2 = 0

The source term -gamma*M*f/r^2 combines with the angular barrier -2f/r^2, effectively increasing the centrifugal barrier. This explains why the source coupling slightly modifies the profile but cannot drive a large amplitude increase.

---

## E. Energy Decomposition

Four sectors (3 pure defect + 1 interaction), cleanly separated:

| Sector | Formula | Character |
|--------|---------|-----------|
| Radial kinetic | (1/2) eta^2 (f')^2 | ~ 1/r^4 (Component A candidate) |
| Angular gradient | eta^2 f^2/r^2 | ~ eta^2/r^2 (Component B) |
| Potential | (1/4) lam eta^4 (f^2-1)^2 | Exponential decay |
| Interaction | (1/2) gamma X eta^2 f^2 | Sign-definite positive (Hamiltonian) |

The interaction term is reported separately from the pure defect sectors. It enters the Hamiltonian as +(1/2)*gamma*X*eta^2*f^2 (sign flip from Lagrangian to Hamiltonian for potential terms).

---

## F. Component A Recovery (Three-Part Test)

### Shape test

Does the radial kinetic term produce 1/r^4 scaling?

**Result**: PASS (exponent -2.72, within tolerance 1.5 of target -4.0). Same finite-domain BVP convergence effect as D4.

### Coefficient test

Does the coefficient match the Component A budget (COMP_A_TARGET ~ 1.181)?

**Result**: FAIL (ratio ~ 0.0043 at default gamma=1.0). The source coupling produces a marginal improvement from the D4 baseline (0.0035) but remains ~230x too weak.

### Mechanism test

Is the mechanism source-driven?

**Result**: HYBRID. With gamma > 0, the mechanism is topology-driven + source-driven. However, the source contribution is insufficient to meaningfully change the amplitude.

### Verdict

Classification: `source_coupling_insufficient`

---

## G. Component B Preservation (Four-Part Test)

| Check | Result | Detail |
|-------|--------|--------|
| 1. Tail exponent | PASS | -1.26 within tolerance 1.0 of target -2.0 |
| 2. Tail coefficient | PASS | Within factor-of-3 of eta^2 (BVP convergence) |
| 3. Monotonic f -> 1 | PASS | No overshoot (f_max = 1.000) |
| 4. No oscillation | PASS | Oscillation-free in tail |

Classification: `preserved` (at baseline gamma=1.0)

---

## H. Gamma Scan

Bounded scan over 9 values [0.0, 0.1, 0.5, 1.0, 2.0, 5.0, 10.0, 20.0, 50.0]:

| gamma | Converged | Comp A ratio | Comp B preserved | f_max | Pathology |
|-------|-----------|-------------|------------------|-------|-----------|
| 0.0 | YES | 0.0035 | YES | 1.000 | NO |
| 0.1 | YES | 0.0036 | YES | 1.000 | NO |
| 0.5 | YES | 0.0039 | YES | 1.000 | NO |
| 1.0 | YES | 0.0043 | YES | 1.000 | NO |
| 2.0 | YES | 0.0048 | YES | 1.000 | NO |
| 5.0 | YES | 0.0049 | NO | 1.000 | NO |
| 10.0 | YES | 0.0028 | NO | 1.000 | NO |
| 20.0 | YES | 0.0005 | NO | 1.000 | NO |
| 50.0 | YES | 0.0000 | NO | 1.000 | NO |

**Key findings**:

1. **All 9 BVPs converge** — no numerical instability at any gamma.
2. **Peak ratio ~ 0.0049 at gamma ~ 5** — barely above the D4 baseline (0.0035), a ~40% improvement that is still 200x too weak.
3. **Ratio DECREASES at high gamma** — the source coupling becomes counterproductive beyond gamma ~ 5, suppressing the radial kinetic energy.
4. **Component B preserved for gamma <= 2** — the topological tail is robust at moderate coupling.
5. **No viable window** — no gamma gives both significant A improvement AND B preservation.

Best gamma: 2.0 (best ratio with B preserved, no pathology).
Viable window: None (no gamma exceeds 1.5x baseline improvement).

---

## I. Pathology Inventory

| # | Category | Severity | Description |
|---|----------|----------|-------------|
| 1 | component_b_degradation | moderate | B not preserved for 4 gamma values (5, 10, 20, 50) |
| 2 | counterproductive | moderate | Source coupling reduces ratio for 2 gamma values (20, 50) |

Total: 0 critical, 2 moderate, 0 minor. No runaways, no overshoot, no BVP failures.

---

## J. Classification

**Classification**: `source_coupling_insufficient`

This means:
- The quadratic source coupling L_int = -(1/2)*gamma*X*|Phi|^2 is structurally too weak to recover the Component A amplitude
- The EL-derived sign (negative for gamma > 0) increases the effective mass, opposing the hedgehog vacuum rather than driving amplitude growth
- The coupling produces marginal improvement (~40% at best) but remains ~200x below the Component A budget
- Component B is preserved at moderate gamma (0-2) but degrades at large gamma
- No critical pathologies; all BVPs converge

### What this classification does NOT mean:
- It does NOT invalidate D1-D4 (the topological structure, Component B, and shape recovery all stand)
- It does NOT rule out other coupling mechanisms or sign conventions
- It does NOT prove that source-coupling is fundamentally impossible — only that this specific minimal coupling is insufficient

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
| **Source-Coupled D5** | **ASSESSED (source_coupling_insufficient)** |

---

## K. Numerical Validation Summary

- Benchmark: **60/60 checks PASSED**
- Pytest: **60/60 tests PASSED** (0.91s)
- 2 source couplings defined (quadratic, linear)
- 4 Lagrangian terms constructed
- 9 gamma values scanned (all converge)
- 3-part Component A test (shape/coefficient/mechanism)
- 4-part Component B test (exponent/coefficient/monotonic/oscillation)
- 2 pathologies documented
- Normalization map explicitly constructed

---

## L. Nonclaims (10)

1. This phase does NOT prove the final unified field theory.
2. A successful amplitude recovery establishes numerical viability, not final canon.
3. A failed D5 result does NOT invalidate D1-D4.
4. The source coupling is a tested candidate mechanism, not a unique derivation.
5. Both Component A recovery and Component B preservation must hold for a positive result.
6. The interaction energy term may be sign-indefinite and is not guaranteed physical.
7. The gamma scan is bounded and disciplined, not exhaustive.
8. The BVP uses finite-domain approximation.
9. The source profile X(r) = M/r^2 is a diagnostic candidate.
10. The classification is within the D5 numerical framework only.

---

## M. Assumptions (10)

1. The GRUT source profile is X(r) = M/r^2 (from source_law_program).
2. Two source couplings assessed: quadratic (preferred) and linear (comparison).
3. The source term sign is derived from Euler-Lagrange variation.
4. The curvature trigger is fixed to D4 Kretschner sqrt(K).
5. The gamma scan includes gamma=0 as D4 baseline.
6. The interaction energy is reported separately from pure defect sectors.
7. Component A recovery assessed in three parts.
8. Component B preservation assessed in four parts.
9. BVP uses scipy.solve_bvp on domain [0.01, 5.0].
10. Background metric held fixed (no back-reaction).

---

## N. Recommended Next Move

D5 establishes that the minimal quadratic source coupling is insufficient. The EL-derived sign is the key structural reason: the coupling acts as an effective mass increase rather than a driving force. Possible next steps:

1. **Opposite sign convention**: L_int = +(1/2)*gamma*X*|Phi|^2 would give a positive source term, reducing the effective mass. This is less natural from a Lagrangian standpoint but structurally different.

2. **Source-driven scalar-memory as separate sector**: Rather than coupling X(r) into the triplet ODE, treat Component A as a genuinely separate sector (the scalar-memory equation tau*dPhi/dt + Phi = X) that coexists with the topological Component B. This is the "two-sector" interpretation.

3. **Higher-order couplings**: Terms like gamma*X^2*|Phi|^2 or derivative couplings gamma*(dX/dr)*|Phi|^2 could produce different sign structure.

4. **Self-consistent coupled BVP**: Solve the triplet + metric system simultaneously, where the triplet energy back-reacts on the metric and the curvature feeds back into the triplet equation.

5. **Lambda-convergence study**: Repeat D5 at lambda = 100, 200, 500 to check whether the ratio improves as the tail exponents converge toward their asymptotic values.
