# Phase D1 — Defect-Sector Admissibility and Hedgehog ODE Derivation

This is a candidate extension program, not locked canon.

---

## A. Mission & Context

The tested classical GRUT strong-field interior program is closed within scope:

| Phase | Result | Status |
|-------|--------|--------|
| Phase 6 | f(R_eq) = -17.71 | LOCKED |
| Phase 6B | A_crit = 1.062 | LOCKED |
| Phase 6C | epsilon_min = Component A (1/r^4) + Component B (1/r^2) | LOCKED |
| Route C (Markov) | epsilon ~ 1/r^4 only | LOCKED (insufficient) |
| Route B (all channels) | Closed within Galley CTP | LOCKED |
| Route C (non-Markov) | Source profile locking: 1/r^4 for any kernel | LOCKED |
| Source-Law Program I | Partially viable, no GRUT-native mechanism | LOCKED |

The Source-Law Program I identified defect/topological (Q/r) as the cleanest shape-compatible source class for generating Component B. Phase D1 opens Omni-ToE v3 by formalizing the minimal symmetry-breaking defect sector.

**Goal**: Formulate the candidate extension cleanly enough that it can be tested in Phase D2.

---

## B. Field-Content Admissibility

The criterion for monopole-type defects in 3 spatial dimensions is that the second homotopy group pi_2(M) of the vacuum manifold M must be non-trivial.

| Field | Components | Vacuum manifold | pi_2 | Monopole? |
|-------|-----------|----------------|------|-----------|
| Real scalar | 1 | {+eta, -eta} (discrete) | 0 | NO |
| Complex scalar | 2 | S^1 (circle) | 0 | NO |
| **O(3) triplet** | **3** | **S^2 (2-sphere)** | **Z** | **YES** |

A single real scalar has a discrete vacuum manifold. It supports domain walls (pi_0 non-trivial) but not monopoles. A complex scalar has vacuum manifold S^1 and supports vortices/strings (pi_1 = Z) but not monopoles.

The O(3) triplet is the **minimal field content** whose vacuum manifold has non-trivial pi_2, supporting monopole/hedgehog configurations classified by integer winding number.

---

## C. Symmetry-Breaking Potential

The Mexican-hat potential for the O(3) triplet Phi = (Phi_1, Phi_2, Phi_3):

    V(Phi) = -(1/2) mu^2 |Phi|^2 + (1/4) lambda |Phi|^4

The vacuum expectation scale:

    eta = mu / sqrt(lambda)

Key values (for Component B coefficient matching):
- eta_target = 1/sqrt(8*pi) ~ 0.1995
- eta^2 = 1/(8*pi) ~ 0.03979 = COMP_B_COEFF
- lambda = mu^2/eta^2 = 8*pi*mu^2

**Important**: eta is a symmetry-breaking amplitude scale, NOT a literal electric or gauge charge. No gauge field is introduced in this phase.

The coefficient-matching condition eta^2 = 1/(8*pi) is a shape-and-normalization requirement. It is not yet a derived physical identification.

---

## D. Hedgehog Ansatz and ODE Derivation

### Ansatz

The spherically symmetric hedgehog configuration:

    Phi_a(r) = eta * f(r) * x_hat_a

where x_hat_a = x_a/r is the unit radial vector.

### Gradient decomposition

    partial_i Phi_a = eta * [f'(r) * x_hat_i * x_hat_a + (f(r)/r) * (delta_{ia} - x_hat_i * x_hat_a)]

    (partial Phi)^2 = eta^2 * [(f')^2 + 2 * f^2 / r^2]

The first term is the radial kinetic contribution; the second is the angular gradient (topological contribution).

### Energy functional

    E = 4*pi * integral_0^inf dr r^2 [(1/2)*eta^2*(f')^2 + eta^2*f^2/r^2 + V(f)]

where V(f) = (1/4)*lambda*eta^4*(f^2 - 1)^2.

### ODE derivation

The integrand (with r^2 measure absorbed):

    L = (1/2)*eta^2*r^2*(f')^2 + eta^2*f^2 + (1/4)*lambda*eta^4*r^2*(f^2-1)^2

Euler-Lagrange equation d/dr[dL/df'] - dL/df = 0:

    dL/df' = eta^2 * r^2 * f'
    d/dr[...] = eta^2 * r^2 * [f'' + (2/r)*f']

    dL/df = 2*eta^2*f + lambda*eta^4*r^2*f*(f^2-1)

Setting d/dr[dL/df'] = dL/df and dividing by eta^2*r^2:

    **f'' + (2/r)*f' - (2/r^2)*f - lambda*eta^2*f*(f^2-1) = 0**

### Boundary conditions

    f(0) = 0     (regularity at the origin)
    f(inf) = 1   (approach to vacuum manifold)

### D1 analytic profile

For admissibility purposes, Phase D1 uses the smooth interpolating profile:

    f(r) = r / sqrt(r^2 + delta^2)

This satisfies f(0) = 0, f(inf) = 1, and provides the correct energy decomposition structure. Full shooting integration of the ODE is deferred to Phase D2.

---

## E. Energy-Density Decomposition

The energy density for the hedgehog configuration:

    epsilon(r) = (1/2)*eta^2*(f')^2          [radial kinetic / core term]
              +  eta^2*f^2/r^2               [angular gradient / topological tail]
              + (1/4)*lambda*eta^4*(f^2-1)^2  [potential term]

**Behavior**:
- At small r (core): all three terms contribute; radial kinetic and potential are concentrated near the core width delta.
- At large r (tail): f -> 1, f' -> 0, (f^2-1) -> 0. Only the angular gradient term survives.

Numerical verification (analytic profile):
- Tail exponent: -1.992 (target: -2.0)
- Angular gradient fraction at large r: 0.998

---

## F. Asymptotic Component B Proof

### Exact asymptotic analysis

As r -> infinity with f(r) -> 1 and f'(r) -> 0:

1. Radial kinetic: (1/2)*eta^2*(f')^2 -> 0
2. Angular gradient: eta^2*f^2/r^2 -> **eta^2/r^2**
3. Potential: (1/4)*lambda*eta^4*(f^2-1)^2 -> 0

**Surviving term: epsilon(r) -> eta^2/r^2**

This is the key admissibility result. The asymptotic energy density of the hedgehog configuration scales as 1/r^2, matching the shape of Component B from the interior deficit program (Phase 6C).

### Coefficient-matching condition

Component B requires: epsilon_B = 1/(8*pi*r^2)

The hedgehog tail provides: epsilon_tail = eta^2/r^2

Matching: **eta^2 = 1/(8*pi)**

This is a shape-and-normalization matching condition. It determines what value of eta would be required for the defect tail to exactly reproduce Component B. Whether this value emerges from a physical derivation is a question for Phase D2.

### Numerical verification

- Fitted tail exponent: -1.992 (deviation from -2.0: 7.5e-3)
- Ratio test: epsilon*r^2 at r_max = 0.039777 vs eta^2 = 0.039789 (match to 0.03%)
- Shape compatible: YES

---

## G. Compatibility Inventory for Phase D2

Six unresolved questions that must be addressed before this candidate can be promoted beyond "provisional candidate extension":

### Q1. Core Regularity (HIGH)
Does the monopole core energy remain integrable and numerically manageable near r = 0? Is the core compatible with the TOV-style integrator used in the GRUT interior program?

### Q2. Coupling to GRUT Structure (HIGH)
How does the triplet defect sector couple to the existing GRUT source law and Einstein equations? Is the coupling additive (T_total = T_memory + T_defect), replacement, or hybrid?

### Q3. Compatibility with Locked Results (HIGH)
Does this extension leave Component A (1/r^4 from scalar memory) intact? Does it destabilize previously locked classical structures (Phase 6, 6B, 6C)?

### Q4. Relation to Prior GRUT Scalar-Memory Field (HIGH)
What is the relation between the O(3) triplet defect field and the original GRUT scalar-memory field Phi? Is the triplet: (a) a replacement of the scalar, (b) an embedding (scalar as one component), (c) a companion sector coupled to the scalar, or (d) a next-sector extension with independent dynamics? This is the major conceptual hinge for GRUT integration.

### Q5. Physical Viability (MEDIUM)
Is the candidate merely shape-compatible, or is it dynamically viable? Phase D2 must solve: (a) full shooting solution of the hedgehog ODE, (b) integrated energy and mass profile, (c) self-consistent Einstein-defect system.

### Q6. Interpretation of eta (MEDIUM)
What physical interpretation does eta carry? Is it a fundamental constant, a derived scale from GRUT parameters, or a new free parameter? Can eta be related to existing GRUT constants (tau, M, alpha_vac) through a consistency condition?

---

## H. Final Classification

**Classification**: `provisional_candidate_extension_formulated`

This means:
- The candidate extension has been mathematically formulated
- The key asymptotic 1/r^2 tail has been derived
- Shape compatibility with Component B has been demonstrated
- The coefficient-matching condition eta^2 = 1/(8*pi) has been identified
- But physical viability, GRUT compatibility, and integration remain open pending Phase D2

### Phase lock update

| Phase | Status |
|-------|--------|
| Phase 6: f(R_eq) | LOCKED (-17.71) |
| Phase 6B: A_crit | LOCKED (1.062) |
| Phase 6C: deficit | LOCKED (Component A + Component B) |
| Route C (Markov) | LOCKED (insufficient) |
| Route B (all channels) | LOCKED (closed within Galley CTP) |
| Route C (non-Markov) | LOCKED (source profile locking) |
| Source-Law Program I | LOCKED (partially viable, no GRUT-native) |
| **Defect Sector D1** | **FORMULATED (provisional candidate extension)** |

---

## I. Numerical Validation Summary

- Benchmark: **57/57 checks PASSED**
- Pytest: **59/59 tests PASSED** (0.32s)
- All analytic profile computations verified
- Tail exponent within 0.008 of target -2.0
- Coefficient match confirmed to 0.03% precision
- ODE derived from Euler-Lagrange; residual quantified on analytic profile

---

## J. Nonclaims (10)

1. This phase does NOT prove the final particle sector of the theory.
2. This phase does NOT derive the defect from the already-locked GRUT core.
3. This phase does NOT show that the defect restores the metric by itself.
4. This phase does NOT identify eta with a literal electric charge.
5. This phase does NOT justify metaphysical or observer-based interpretations.
6. This phase only formulates a candidate extension and proves asymptotic shape compatibility.
7. The coefficient-matching condition eta^2 = 1/(8*pi) is a normalization requirement, not a derived physical identification.
8. The analytic interpolating profile is an approximation; the true solution requires shooting integration (deferred to D2).
9. The compatibility inventory is not exhaustive.
10. The classification means the extension is formulated and shape-compatible, but NOT yet physically viable or GRUT-integrated.

---

## K. Assumptions (10)

1. The candidate extension seeks a topological defect sector with tail ~ eta^2/r^2.
2. Topological admissibility requires non-trivial pi_2(M) for the vacuum manifold.
3. The O(3) triplet with Mexican-hat SSB is the minimal admissible field content.
4. eta is a symmetry-breaking amplitude scale, not a charge.
5. The hedgehog ansatz is the standard spherically symmetric monopole configuration.
6. Energy decomposition follows from the standard minimally coupled scalar Lagrangian.
7. The analytic interpolating profile is used as the primary D1 vehicle; full ODE solving is deferred.
8. The asymptotic tail is exact in the f->1 limit and independent of the core solution.
9. The background metric is held fixed (no back-reaction).
10. This phase formulates a candidate extension only; viability is pending Phase D2.

---

## L. Recommended Next Move

Phase D2 should:
1. Solve the hedgehog ODE via shooting integration
2. Compute the full mass/energy profile m_defect(r)
3. Address the scalar-memory relation question (the major conceptual hinge)
4. Test whether the defect sector can coexist with the existing GRUT structure without destabilizing locked results
5. Determine whether eta can be derived from GRUT parameters or is a new free constant
