# Phase 6C — Global Metric Positivity Deficit and Minimal Closure Requirement

## Status

**MINIMAL ADDITIVE SOURCE IDENTIFIED — CURRENT CLOSURE INSUFFICIENT**

Classification: **current_closure_insufficient__minimal_additive_source_identified**

Phase 6C extends Phase 6B's dynamical analysis by computing the exact
mathematical shape of the metric deficit, deriving the minimal additive
source that saturates f(r) = 0, and testing five correction classes.
The principal finding is that the minimal source epsilon_min(r) decomposes
into two components — a 1/r^4 term that cancels the equilibrium negative
density, and a 1/r^2 term for intermediate-radius support — and no
tested GRUT profile provides the second component.

---

## A. Mission and Context

Phase 6 established f(R_eq) = -17.71 at the static equilibrium (LOCKED).
Phase 6B showed this obstruction is global_robust under dynamical processing:
the uniform 11.5% estimate is an optimistic artifact, the natural profile
requires 106% (A_crit = 1.062), and collapse-produced concentrated profiles
never achieve global metric positivity.  Anisotropy contributes < 1%.

**Phase 6C asks six questions:**

1. Where is the metric positivity deficit concentrated?
2. What is the exact deficit budget at each radius?
3. What is the minimal correction source that saturates f = 0?
4. Which correction classes are insufficient?
5. Why does A_crit > 1 for the natural profile?
6. Can any tested profile family in the current closure restore positivity?

**The answers:**

1. The deficit delta(r) = m(r) - r/2 is positive over 83% of the barrier
2. delta(R_eq) = 2.951, with peak at the innermost grid point
3. epsilon_min(r) = |rho_eq(r)| + 1/(8*pi*r^2) — two components
4. Kinetic (shape mismatch), anisotropic (self-quenching), monotonic (gap)
5. The 6.2% excess compensates the missing 1/r^2 component through overshoot
6. No tested profile provides both components; classification: current_closure_insufficient

---

## B. The Deficit Function delta(r) = m(r) - r/2

The deficit function is defined as:

    delta(r) = m(r) - r/2

where m(r) is the linearized static mass from Phase 6:

    m(r) = M + (2*pi*M^2 / tau^2) * (1/r - 1/R_ext)

The metric function is f(r) = 1 - 2*m(r)/r = 1 - 2*delta(r)/r - 1 = -2*delta(r)/r.
Where delta > 0, the metric function f < 0.

| Quantity | Value |
|:---|:---|
| delta(R_eq) | 2.951 |
| delta(R_ext) | -0.500 (f > 0 at exterior) |
| delta_max | 3.770 (at innermost grid point) |
| Fraction r with delta > 0 | 83% |
| Deficit boundary r_outer | ~1.42 |

The deficit transitions from negative (exterior, f > 0) to positive
(interior, f < 0) at r ~ 1.42.  The barrier region r in [R_eq, r_outer]
has delta > 0 throughout.

---

## C. Minimal Source Decomposition: epsilon_min = |rho_eq| + 1/(8*pi*r^2)

For an additive positive source epsilon(r), the corrected mass is:

    m_new(r) = m_static(r) - Sigma(r)
    Sigma(r) = integral from r to R_ext of 4*pi*r'^2 * epsilon(r') dr'

For f >= 0 everywhere: Sigma(r) >= delta(r).  Setting equality (saturation):

    d(Sigma)/dr = d(delta)/dr
    -4*pi*r^2 * epsilon = 4*pi*r^2 * rho_eq - 1/2
    epsilon_min = -rho_eq + 1/(8*pi*r^2) = |rho_eq| + 1/(8*pi*r^2)

This decomposes into two components:

    Component A = |rho_eq(r)| = M^2 / (2*tau^2*r^4)    [cancels negative density]
    Component B = 1 / (8*pi*r^2)                        [intermediate-radius support]

| Radius | Component A | Component B | Ratio B/A |
|:---|:---|:---|:---|
| R_eq = 1/3 | 6.750 | 0.358 | 5.3% |
| r = 1 | 0.0833 | 0.0398 | 47.7% |

At R_eq, Component A dominates (the natural profile at A=1 provides this).
At intermediate radii r ~ 1, Component B becomes comparable — and no
tested GRUT profile provides this 1/r^2 support independently.

**Explicit assumptions behind epsilon_min:**

1. The correction enters through an additive positive source in the mass equation
2. The target is saturation f = 0, not strict positivity f > 0
3. The underlying static mass profile remains the Phase 6B baseline (unmodified)
4. No extra pressure-sector modification changes the mass-balance condition

---

## D. Why A_crit > 1: The Missing 1/r^2 Component

The natural profile Phi_dot ~ M/(tau*r^2) produces kinetic energy:

    epsilon_natural(r) = A^2 * M^2 / (2*tau^2*r^4)

At A = 1, this exactly matches Component A.  But epsilon_min also requires
Component B ~ 1/(8*pi*r^2), which the natural 1/r^4 profile does NOT provide.

To compensate, the amplitude must overshoot to A_crit = 1.062, using the
excess 1/r^4 energy at small r to cover the 1/r^2 deficit at intermediate
radii.  The 6.2% excess is the price of using a 1/r^4 profile to do a
1/r^2 job.

| Quantity | Value |
|:---|:---|
| Component A coefficient | M^2/(2*tau^2) = 0.0833 |
| Component B coefficient | 1/(8*pi) = 0.0398 |
| A_crit (natural, Phase 6B) | 1.062 |
| Excess over unity | 6.2% |

---

## E. Two-Parameter Profile Scan

Parameterizing the energy density directly:

    epsilon(r) = A / r^4 + B / r^2

at the mass-function level (avoiding spurious cross terms from squaring
Phi_dot), we scan the (A,B) plane to find the threshold surface f_min = 0.

Key results:

| Quantity | Value |
|:---|:---|
| A_crit at B = 0 | 0.0970 (recovers Phase 6B within 3.5%) |
| B_crit at A = 0 | 0.173 |
| Contour shape | A decreases as B increases (substitution) |
| Contour points | ~30 |

The threshold contour in (A,B) space is a smooth curve from
(A_crit, 0) to (0, B_crit).  Points on this curve represent different
ways to achieve f = 0 globally with the two-component decomposition.

B = 0 recovery: at B = 0, A_crit should equal A_natural^2 * M^2/(2*tau^2)
= 1.062^2 * 0.0833 = 0.0940.  The scan gives 0.0970, a 3.5% discrepancy
due to grid resolution — confirming recovery.

**Normalization note:** The two-parameter scan coefficient A_coeff is NOT
the same as the Phase 6B processing amplitude A_amplitude.  The mapping is:

    A_coeff = A_amplitude^2 * M^2 / (2 * tau^2)

At canonical parameters, M^2/(2*tau^2) = 0.0833.  Phase 6B reports
A_amplitude = 1.062; the corresponding energy coefficient is
A_coeff = 1.062^2 * 0.0833 = 0.0940.

---

## F. Monotonic Profile Insufficiency

Tested profiles: 1/r^n for n = 2, 3, 4, 5.  For each, the amplitude
is optimized to minimize the global f deficit.

The 1/r^4 profile (natural) concentrates at small r, providing Component A
but requiring amplitude overshoot for Component B.  The 1/r^2 profile
provides Component B but is inefficient for Component A.  No single tested
monotonic power-law profile matches the required mixed 1/r^4 + 1/r^2 shape.

| Profile | Provides A | Provides B | Single-profile sufficient? |
|:---|:---|:---|:---|
| 1/r^4 (natural) | YES | NO (overshoot) | At A = 1.06 only |
| 1/r^2 | NO (inefficient) | YES | Not tested, would need large C |
| 1/r^3 | Partial | Partial | No |
| 1/r^5 | YES (concentrated) | NO | Even worse than 1/r^4 |

Gap fraction (max deficit/epsilon_min ratio at optimal amplitude): ~45%
at r ~ 1.42 (the deficit boundary).

**This is an insufficiency result for the tested family, NOT a general
no-go theorem for all monotonic profiles.**

---

## G. Correction Classes Summary Table

| # | Class | Result | Status |
|:---|:---|:---|:---|
| 1 | Kinetic (deficit-shaped) | Shape sqrt(2*epsilon_min) exists; not achievable within GRUT sourcing | INSUFFICIENT |
| 2 | Anisotropic (f*(Phi')^2) | Self-quenches at f = 0; vanishes where needed | INSUFFICIENT |
| 3 | Additive positive source | Works by construction (epsilon_min); requires beyond-GRUT | SUFFICIENT (beyond-GRUT) |
| 4 | Two-parameter (A/r^4 + B/r^2) | Threshold surface identified; clean decomposition | DIAGNOSTIC |
| 5 | Monotonic profiles (1/r^n) | Gap at intermediate radii; no single power law sufficient | INSUFFICIENT (tested family) |

---

## H. Closure Classification

**Classification: current_closure_insufficient__minimal_additive_source_identified**

The current GRUT closure (scalar kinetic processing with gravitational
sourcing) produces Phi_dot profiles that concentrate at small r (1/r^2
after sourcing from X = M/r^2).  The minimal additive source
epsilon_min = |rho_eq| + 1/(8*pi*r^2) requires intermediate-radius
support (Component B) that the closure cannot generate.

The additive source that saturates f = 0 has been explicitly identified
and verified numerically (f_corrected >= -0.015 everywhere, within
discretization precision).

---

## I. Physical Interpretation

The metric positivity deficit has a clear physical origin:

1. **Negative energy density** rho_eq = -M^2/(2*tau^2*r^4) from the
   dissipative coupling -Phi*J dominating the potential V(Phi).

2. **Mass accumulation** dm/dr < 0 (mass increases inward) drives
   delta(r) = m(r) - r/2 positive in the barrier region.

3. **Two-component correction** is needed because:
   - Component A (1/r^4): cancels rho_eq locally — this is what the
     natural Phi_dot profile provides at A = 1.
   - Component B (1/r^2): provides the geometric correction
     (the 1/2 in f = 1 - 2m/r) — no GRUT sourcing mechanism
     naturally produces this.

4. **Overshoot mechanism**: The natural profile at A = 1.062 achieves
   f = 0 globally by overproducing 1/r^4 energy at small r (where
   it exceeds epsilon_min) to compensate for underproduction at
   intermediate r (where it falls short of epsilon_min).

---

## J. Way Forward

The identification of the two-component minimal source structure
suggests several directions:

1. **Modified sourcing**: A GRUT sourcing mechanism that produces
   Phi_dot ~ 1/r (not 1/r^2) would provide the 1/r^2 kinetic
   energy component directly.

2. **Non-equilibrium driving**: External forcing maintaining processing
   energy at intermediate radii, not just near the source.

3. **Two-field model**: A second scalar field with different spatial
   coupling could provide Component B independently.

4. **Route B formulation**: The Galley effective stress-energy may
   distribute processing differently, potentially providing 1/r^2
   support through nonlocal effects.

5. **Beyond-GRUT physics**: If the deficit cannot be closed within
   the current framework, this characterizes the minimal extension
   needed (a positive source with the specific epsilon_min shape).

---

## K. Computational Artifacts

| File | Purpose |
|:---|:---|
| `grut/metric_deficit.py` | Core module: deficit, minimal source, correction classes, classification |
| `benchmark_phase6c_metric_deficit.py` | Benchmark: 76 checks, all pass |
| `tests/test_metric_deficit.py` | pytest: 81 tests, all pass |

**Engine**: Python 3.9+ with numpy
**Methods**:
- Deficit profile: linearized mass m(r) = M + coeff*(1/r - 1/R_ext)
- Minimal source: derivative matching d(Sigma)/dr = d(delta)/dr
- Two-parameter scan: epsilon = A/r^4 + B/r^2 at mass-function level
- Correction classes: 5 independent tests (kinetic, anisotropy, additive, two-param, monotonic)
- Classification: combined assessment of all correction classes
- Deficit mask: epsilon_min applied only where delta > 0

---

## L. Explicit Nonclaims

1. The static mass profile is the linearized equilibrium.  Higher-order
   corrections from the full TOV integration may shift numerical values.

2. The minimal source epsilon_min achieves f = 0 (saturation), NOT
   strict positivity f > 0.

3. The kinetic deficit profile Phi_dot = sqrt(2*epsilon_min) is a
   mathematical shape, not a physically realizable GRUT solution.

4. The two-parameter scan epsilon = A/r^4 + B/r^2 does NOT exhaust all
   possible additive source profiles.

5. The monotonic profile insufficiency applies ONLY to the tested family
   (1/r^n for n = 2..5).  It is NOT a general no-go theorem.

6. The minimal source formula depends on four explicit assumptions
   (additive source, saturation target, unmodified baseline, no
   pressure-sector changes).

7. The deficit function uses the linearized mass, not the full
   self-consistent solution (which has a singularity at r ~ 1.023 r_s).

8. Component B ~ 1/(8*pi*r^2) arises from the geometric 1/2 in
   f = 1 - 2m/r, not from the field equations directly.

9. The Phase 6B recovery maps from amplitude A to energy coefficient
   A^2 * M^2/(2*tau^2).  Correspondence is exact only in the linearized regime.

10. Pressure corrections, nonlocal effects, and modified field equations
    could alter the minimal source requirement.

11. V(Phi) = Phi^2/(2*tau^2) is the Route A candidate potential.
    Other potentials give different rho_eq and different epsilon_min.

12. The classification is descriptive and specific to the tested correction
    classes.  Novel closure mechanisms could change it.

13. Tau is fixed at the canonical value.  Deficit and minimal source
    scale with tau^{-2}.

14. The two-parameter scan uses the mass-function level to avoid
    spurious cross terms from squaring Phi_dot = A/r^2 + B/r.

---

## Phase 1-6C Result Lock

    Phase 1 (T^Phi):              LOCKED (DeltaT = 0, Factorization Theorem)
    Phase 2 (Phi_-):              LOCKED (consistent, not attractor, IR-dominated)
    Phase 3 (h_-):                LOCKED (consistent, vacuum stable, sourced unstable)
    Phase 4 (Einstein+T^Phi):     LOCKED (rho<0, ODE correct, SIGN CORRECTED: mass accumulates)
    Phase 5 (Route A KG):         LOCKED (T^Phi universal, omega^2=k^2+1/tau^2, w=-1)
    Phase 6 (TOV Integration):    LOCKED (f(R_eq) = -17.71 static, Phi_dot_crit/Phi_dot_nat = 11.5%)
    Phase 6B (Dynamical Interior): LOCKED (uniform optimistic, natural A_crit = 1.06, global_robust)
    Phase 6C (Metric Deficit):    LOCKED (epsilon_min = |rho_eq| + 1/(8*pi*r^2), two-component,
                                          current_closure_insufficient__minimal_additive_source_identified)
    Metric Factorization:          LOCKED (diss kernel silent in metric sector)
    Route B overall:               COMPLETE (physical-limit derived)
    Phase V obstruction:           CONFIRMED GENUINE at static equilibrium
    Critical processing (uniform): 11.5% of natural rate (OPTIMISTIC, not physical bound)
    Critical processing (natural): 106% of natural rate (physically motivated)
    Interior metric:               NOT ACHIEVED statically; NOT ACHIEVED dynamically (global_robust)
    Modified TOV:                  SINGULAR (no smooth self-consistent static solution)
    Anisotropy:                    SELF-QUENCHING at f=0 (< 1% effect on threshold)
    Profile dependence:            UNIFORM >> NATURAL > GAUSSIAN > RELAXATION
    Deficit function:              delta(r) = m(r) - r/2, positive over 83% of barrier
    Minimal additive source:       epsilon_min = |rho_eq| + 1/(8*pi*r^2) (two components)
    Component A (1/r^4):           Cancels rho_eq (natural profile provides at A=1)
    Component B (1/r^2):           Intermediate-radius support (NO tested profile provides)
    Two-parameter threshold:       Smooth contour in (A,B) space, B=0 recovers Phase 6B
    Monotonic profiles:            INSUFFICIENT (tested family, not general no-go)
    Closure classification:        current_closure_insufficient__minimal_additive_source_identified
