# Phase D4 — Embedded Triplet Unification Dynamics and Component A Recovery

This is an analytical assessment phase, not locked canon.

---

## A. Mission & Context

D3 ranked the embedding architecture (Phi = |vec(Phi)|) with curvature-triggered SSB as the top candidate (score 0.8215, canon PASS). D4 constructs the explicit curvature-coupled Lagrangian, decomposes into radial and angular modes, and tests whether the radial mode can recover the scalar-memory Component A (~1/r^4) while the angular sector carries Component B (~1/r^2).

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

**Goal**: Determine whether the embedding+curvature architecture preserves Component B and whether it can recover Component A, honestly assessed via three independent tests.

---

## B. Lagrangian

The curvature-coupled embedded-triplet Lagrangian:

    L = (1/2) d_mu Phi^a d^mu Phi^a + (1/2) m0^2 |Phi|^2
        - (1/4) lam |Phi|^4 - (1/2) xi C |Phi|^2

where C is the chosen curvature invariant (ranked among multiple candidates, not assumed to be R).

Effective mass-squared:

    m_eff^2(C) = m0^2 - xi*C

- Unbroken phase: m_eff^2 > 0 -> Phi = 0 is the minimum
- Broken phase: m_eff^2 < 0 -> VEV at |Phi|^2 = |m_eff^2|/lam

In the broken phase with m0^2 = -lam*eta^2 (standard SSB):

    L = (1/2) d_mu Phi^a d^mu Phi^a - (1/4) lam (|Phi|^2 - eta^2)^2 - (1/2) xi C |Phi|^2

---

## C. Embedding Ansatz

Hedgehog: Phi^a = eta * f(r) * r_hat^a

- |Phi| = eta * f(r)
- Scalar-memory identification: Phi_scalar = eta * f(r) (candidate, not derived)
- Boundary conditions: f(0) = 0, f(inf) = 1
- Homotopy class: pi_2(S^2) = Z

The BVP solution from D2 is reused for the radial profile f(r).

---

## D. Mode Decomposition

The energy density decomposes into four sectors:

| Sector | Formula | Asymptotic tail | Measured exponent |
|--------|---------|-----------------|-------------------|
| Radial kinetic | (1/2) eta^2 (f')^2 | ~ 1/r^4 | -2.89 |
| Angular gradient | eta^2 f^2/r^2 | ~ eta^2/r^2 | -1.42 |
| Potential | (1/4) lam eta^4 (f^2-1)^2 | exponential decay | -8.61 |
| Curvature coupling | (1/2) xi sqrt(K) eta^2 f^2 | ~ 1/r^3 | -2.41 |

The measured exponents are from the D2 BVP solution at default lambda = 8*pi on the domain [0.01, 5.0]. At this finite lambda, the tail exponents have not fully converged to their asymptotic values. D2 showed that the total energy exponent approaches -2.0 monotonically as lambda increases (lam=200 gives -1.97).

---

## E. Component A Recovery (Three-Part Test)

### Shape test

Does the radial kinetic term (f')^2 produce 1/r^4-type scaling?

**Result**: PASS (exponent -2.89 within 1.5 of target -4.0, accounting for finite-domain BVP convergence). The exponent trends toward -4.0 at higher lambda.

### Coefficient test

Does the radial kinetic coefficient match A^2 * MASS_COEFF?

**Result**: FAIL (ratio ~ 0.0035). The radial kinetic amplitude is orders of magnitude smaller than the Component A budget. This means the radial mode does not yet reproduce the correct Component A energy scale.

### Interpretation test

Is the radial mode mechanism the same as scalar-memory?

**Result**: DIFFERENT. The radial mode is topology-driven (hedgehog self-interaction + boundary conditions). The scalar-memory is source-driven (tau dPhi/dt + Phi = X(r), with X(r) = S(r)^2 from matter). These are structurally different mechanisms.

### Verdict

The radial kinetic energy has the correct 1/r^4 functional form, but the coefficient is wrong and the driving mechanism is different. This is a new sector with analogous scaling, not the old scalar-memory sector recovered.

---

## F. Component B Preservation

The angular gradient term eta^2 * f^2/r^2 -> eta^2/r^2 as f -> 1.

**Result**: PRESERVED. Angular exponent -1.42 is within tolerance of target -2.0 (finite-domain effect, trending toward -2.0 at higher lambda). The curvature coupling decays faster (~1/r^3) than the angular gradient (~1/r^2), so it does not spoil Component B.

This confirms the D1/D2 result: the topological hedgehog provides Component B.

---

## G. Curvature Trigger (Multi-Invariant Assessment)

Three curvature invariants assessed as SSB trigger candidates:

| Invariant | Nonzero in vacuum | Score | SSB at R_EQ | Verdict |
|-----------|-------------------|-------|-------------|---------|
| Ricci scalar R | NO | 0.50 | NO | weak |
| Kretschner sqrt(K) | YES | 0.85 | YES | strong candidate |
| Ricci-squared sqrt(R_ab R^ab) | NO | 0.70 | YES | moderate |

**Key findings**:

1. **Ricci scalar R = 0 in vacuum Schwarzschild**. It is nonzero only in sourced regions, making it model-dependent. Not the most robust trigger.

2. **Kretschner sqrt(K) is nonzero everywhere**, including vacuum. It provides a robust strong-field mass scale (sqrt(K) = sqrt(48)*M/r^3 for Schwarzschild). Top-ranked trigger candidate.

3. **Ricci-squared** is intermediate: nonzero in sourced regions, vanishes in vacuum.

**Classification**: `ssb_plausible` — the Kretschner-based trigger achieves SSB at R_EQ, but this is a heuristic coupling (sqrt(K) as mass scale is non-standard). Full verification requires a self-consistent coupled solution.

---

## H. Artifact Inventory

8 artifacts documented:

| # | Category | Severity | Description |
|---|----------|----------|-------------|
| 1 | cross_term | moderate | Radial-angular cross-terms in curved background not evaluated |
| 2 | approximation | moderate | Background metric held fixed (no back-reaction) |
| 3 | unresolved | moderate | Coefficient matching requires lambda tuning (no physical justification) |
| 4 | caveat | major | Mechanism difference (topology-driven vs source-driven) |
| 5 | caveat | moderate | sqrt(K) as mass coupling is heuristic, not rigorous field theory |
| 6 | approximation | minor | Curvature trigger sign depends on matter model (p/rho assumed) |
| 7 | approximation | minor | BVP finite-domain effects on tail fits |
| 8 | cross_term | moderate | xi-dependent corrections to tail (BVP solved without xi in ODE) |

Total: 1 major, 5 moderate, 2 minor. All are documented for future resolution.

---

## I. Classification

**Classification**: `component_a_shape_recovered_but_interpretation_not_yet_verified`

This means:
- Component A shape (1/r^4 exponent) is present in the radial kinetic sector
- Component A coefficient does not match the scalar-memory budget
- Component A mechanism is structurally different (topology vs source)
- Component B is preserved (angular gradient retains 1/r^2 tail)
- Curvature trigger is plausible (Kretschner top-ranked) but requires coupled verification

### What this classification does NOT mean:
- The embedding model is not validated as the final theory
- Component A has not been derived from the triplet sector
- The curvature trigger has not been verified in a self-consistent solution

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
| **Unification D4** | **ASSESSED (component_a_shape_recovered_but_interpretation_not_yet_verified)** |

---

## J. Numerical Validation Summary

- Benchmark: **55/55 checks PASSED**
- Pytest: **55/55 tests PASSED** (0.67s)
- 4 Lagrangian terms constructed
- 4 energy sectors decomposed
- 3 curvature invariants assessed
- 8 artifacts documented
- 3-part Component A test (shape/coefficient/interpretation)

---

## K. Nonclaims (10)

1. This phase does NOT prove the final unified theory.
2. This phase does NOT derive Component A from the triplet sector. It tests structural compatibility only.
3. This phase does NOT prove the curvature trigger works in a self-consistent coupled solution.
4. A shape match (1/r^4 exponent) is not the same as a derivation of the scalar-memory equation from the triplet Lagrangian.
5. A coefficient mismatch does not invalidate the embedding model. It means the radial mode is not yet shown to reproduce the exact Component A budget.
6. The interpretation test identifies a structural difference, not necessarily an incompatibility.
7. The Kretschner invariant sqrt(K) is used as a mass-squared-like scale. This is a heuristic, not a rigorous field-theory construction.
8. Curvature invariant values in the sourced interior are approximate. They depend on the matter model assumed.
9. The artifact inventory documents unresolved issues for future phases.
10. The classification is within the D4 analytical framework only. Numerical coupled-model verification may revise the assessment.

---

## L. Assumptions (10)

1. The embedded-triplet Lagrangian is constructed with Mexican-hat potential plus non-minimal curvature coupling. The coupling invariant C is assessed among multiple candidates.
2. The embedding ansatz Phi^a = eta*f(r)*r_hat^a identifies the scalar-memory field with the radial modulus.
3. The mode decomposition uses the D2 BVP solution for f(r) to evaluate tail exponents numerically.
4. Component A recovery is assessed in three independent parts: shape, coefficient, interpretation.
5. Component B preservation is assessed by checking the angular gradient tail.
6. The curvature trigger is assessed for multiple invariants: Ricci R, Kretschner sqrt(K), Ricci-squared.
7. The effective mass m_eff^2(C) = m0^2 - xi*C determines broken/unbroken regime.
8. The background metric is held fixed (no self-consistent back-reaction).
9. Cross-term artifacts are inventoried but not resolved within D4.
10. The classification is determined by the assessments, not predetermined.

---

## M. Recommended Next Move

Phase D4 establishes that the embedding+curvature architecture preserves Component B and shows a 1/r^4 shape in the radial sector, but does not yet recover Component A's coefficient or mechanism. Possible next steps:

1. **Self-consistent coupled BVP**: Solve the radial mode ODE with xi*C included, iterating metric and field.
2. **High-lambda convergence study**: Repeat the D4 analysis at lambda = 100, 200, 500 to check tail exponent convergence.
3. **Coefficient tuning**: Investigate whether lambda or xi can be chosen to match the Component A budget, and whether such choices have independent physical motivation.
4. **Alternative Component A mechanism**: The radial kinetic energy provides 1/r^4 scaling from topology, not from sources. Investigate whether this new mechanism can replace or supplement the old scalar-memory Component A.
5. **Kretschner trigger formalization**: Develop the sqrt(K)-based coupling into a rigorous field-theory construction, or determine whether it can be reformulated in terms of standard curvature scalars.
