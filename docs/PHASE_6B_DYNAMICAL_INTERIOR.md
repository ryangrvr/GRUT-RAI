# Phase 6B — Dynamical Non-Equilibrium Interior Branch

## Status

**STATIC OBSTRUCTION CONFIRMED ROBUST — DYNAMICAL PROCESSING INSUFFICIENT**

Classification: **GLOBAL ROBUST OBSTRUCTION — CONCENTRATED COLLAPSE PROCESSING CANNOT RESTORE METRIC POSITIVITY**

Phase 6B extends Phase 6's static analysis to the dynamical regime where the
scalar field has nonzero time derivative Phi_dot != 0.  The principal finding
is that the Phase 6 critical processing estimate (11.5% of natural rate) is an
artifact of the UNIFORM processing assumption.  For physically motivated
r-dependent profiles, the threshold is dramatically higher, and dynamical
collapse naturally produces concentrated processing that is insufficient to
achieve global metric positivity.

---

## A. Mission and Context

Phase 6 established that the static equilibrium gives f(R_eq) = -17.71 at
canonical parameters — the scalar field equilibrium makes the metric positivity
problem WORSE through mass accumulation.  Phase 6 also showed that adding
uniform kinetic processing energy epsilon = (1/2)*Phi_dot^2 could restore
f(R_eq) = 0 at only 11.5% of the natural GRUT processing rate.

**Phase 6B asks five questions:**

1. What happens when Phi_dot is r-dependent?
2. Does f(r,t) > 0 hold during dynamical evolution?
3. Is the critical threshold local or global, transient or robust?
4. Does anisotropy change the threshold?
5. Is the 11.5% figure physically meaningful?

**The answers:**

1. The threshold is DRAMATICALLY profile-dependent (11.5% to 106%)
2. f(r,t) > 0 is NEVER achieved globally during realistic collapse
3. The obstruction is GLOBAL and ROBUST
4. Anisotropy contributes < 1% (self-quenching at f = 0)
5. The 11.5% is an optimistic artifact of uniformity, not a physical bound

---

## B. Stress-Energy with Phi-dot

Extending Phase 6's static stress-energy with the temporal kinetic term:

    rho     = (1/2)*e^{-2nu}*Phi_dot^2 + (1/2)*f*(Phi')^2 + V(Phi) - Phi*J
    p_r     = (1/2)*e^{-2nu}*Phi_dot^2 + (1/2)*f*(Phi')^2 - V(Phi) + Phi*J
    p_perp  = (1/2)*e^{-2nu}*Phi_dot^2 - (1/2)*f*(Phi')^2 - V(Phi) + Phi*J

NEC conditions:

| Combination | Formula | Sign |
|:---|:---|:---|
| rho + p_r | e^{-2nu}*Phi_dot^2 + f*(Phi')^2 | >= 0 |
| rho + p_perp | e^{-2nu}*Phi_dot^2 | >= 0, NOT saturated when Phi_dot != 0 |
| p_r - p_perp | f*(Phi')^2 | Self-quenches at f = 0 |

**Key result**: The NEC tangential condition rho + p_perp = e^{-2nu}*Phi_dot^2
is strictly positive when Phi_dot != 0.  This LIFTS the w = -1 degeneracy
from the static equilibrium.

---

## C. Profile Library

Four Phi_dot(r) profile types were tested, each amplitude-scanned:

| Profile | Formula | A_crit (global) | A_crit (R_eq) | Physical motivation |
|:---|:---|:---|:---|:---|
| Uniform | Phi_dot = A | 0.475 | 0.421 | Phase 6 comparison |
| Natural | Phi_dot = A * X(r)/tau | 1.080 | 1.062 | Gravitational source |
| Relaxation | Phi_dot = A * delta_X/tau | No global | 4.33 | Collapse perturbation |
| Gaussian | Phi_dot = A * exp(-...) | No global | 2.74 | Localized processing |

**Most efficient**: Uniform (spatially constant energy fills the entire barrier)
**Least efficient globally**: Natural (concentrated at small r, can't fix intermediate radii)
**No global threshold**: Relaxation and Gaussian (too localized)

---

## D. The Uniform Approximation is Optimistic

Phase 6's critical processing analysis found:

    epsilon_crit = 0.0885
    Phi_dot_crit = 0.421
    Ratio to natural = 11.5%

This assumed UNIFORM epsilon everywhere in the barrier.  Phase 6B reveals:

| Profile | A_crit at R_eq | Ratio to natural rate |
|:---|:---|:---|
| Uniform | 0.421 | 11.5% |
| Natural | 1.062 | 106.2% |

The natural profile Phi_dot(r) = A * M/(tau*r^2) concentrates processing
energy at small r (near R_eq) where it's needed most, but this concentration
means intermediate radii receive too little energy.  For the metric to be
positive everywhere, the amplitude must exceed the natural rate.

**The 11.5% figure is not a physical bound.**  It applies only to the
physically unmotivated scenario of spatially uniform processing energy.
The gravitationally motivated natural profile requires 106% of the natural
rate — a 9x discrepancy.

---

## E. Analytical Threshold for the Natural Profile

For the natural profile Phi_dot(r) = A * X(r)/tau:

    epsilon(r) = A^2 * M^2 / (2*tau^2*r^4)
    rho_total(r) = (A^2 - 1) * M^2 / (2*tau^2*r^4)

The mass integral from R_ext inward:

    m(R_eq) = M - (A^2 - 1) * Delta_m_eq

where Delta_m_eq = 2.618 is the Phase 6 equilibrium mass excess.

For f(R_eq) = 0:  m(R_eq) = R_eq/2

    M - (A^2 - 1)*Delta_m_eq = R_eq/2
    A^2 = 1 + (M - R_eq/2) / Delta_m_eq = 1 + 0.333/2.618 = 1.127

    A_crit = sqrt(1.127) = 1.062

This matches the numerical threshold scan to within 0.1%.

---

## F. Quasi-Static Time Evolution

Time-stepping protocol:

1. Initialize: Phi(r,0) = X_0(r) = M/r^2 (pre-collapse equilibrium)
2. Perturb: sudden mass change -> X_new(r) != X_old(r)
3. Each step: Phi_dot = (X_new - Phi)/tau (GRUT first-order relaxation)
4. Solve radial constraints at each step -> f(r,t)
5. Track: f_min(t), f(R_eq,t), Phi_dot_max(t)

**Results at canonical parameters (collapse_amplitude = 0.5):**

| Quantity | Value |
|:---|:---|
| Phi_dot_max at t=0 | 4.49 |
| Phi_dot at 3*tau | 4.6% of peak (matches exp(-3) = 5.0%) |
| f(R_eq) at t=0 | -16.77 (improved from -17.71) |
| f(R_eq) at late times | -17.71 (returns to static) |
| f positive everywhere | NEVER |
| f_min(t) range | [-28.3, -24.7] |

**The collapse processing is equivalent to the RELAXATION profile** with
A ~ 1.  Since the relaxation profile has no global threshold (it's too
concentrated), the dynamical processing from a physical collapse perturbation
NEVER achieves global metric positivity.

---

## G. Threshold Classification

| Property | Classification | Evidence |
|:---|:---|:---|
| Spatial extent | GLOBAL | f < 0 over 83% of radial grid |
| Temporal persistence | ROBUST | f never positive at any time step |
| Combined | **global_robust** | Static obstruction persists dynamically |
| Fraction r with f < 0 | 83% | Most of barrier region |
| Heals within simulation | NO | — |

The classification is **global_robust**: the metric negativity violation
extends over most of the barrier region and is not healed by the transient
processing energy from collapse.

This contrasts with the Phase 6 expectation of "global_transient" based on
the uniform processing estimate.  The discrepancy arises because the actual
collapse dynamics produce concentrated (not uniform) processing.

---

## H. Anisotropy Self-Quenching

The spatial gradient contribution to the stress-energy is:

    p_r - p_perp = f * (Phi')^2

This is proportional to f and therefore VANISHES at the critical metric
surface f = 0.

| Quantity | Isotropic (Phi'=0) | Anisotropic (full Phi') | Difference |
|:---|:---|:---|:---|
| A_crit (natural) | 1.082 | 1.087 | 0.50% |

The anisotropy effect is 0.50%, well below 1%.  The self-quenching mechanism
ensures that the isotropic approximation is accurate for threshold
determination.

**Physical explanation**: At the critical surface where f crosses zero, the
spatial gradient kinetic energy 0.5*f*(Phi')^2 contributes zero energy
density.  The threshold is therefore entirely determined by the temporal
kinetic term and the equilibrium energy density, both of which are independent
of the spatial gradient.

---

## I. Physical Interpretation

The negative energy density at the equilibrium (rho < 0) arises from the
dissipative coupling term -Phi*J dominating over the potential energy V.
The scalar field kinetic processing energy epsilon = (1/2)*Phi_dot^2 is
a positive contribution that can counteract this.

However, the SPATIAL DISTRIBUTION of processing energy matters critically:

1. **Uniform processing** spreads energy throughout the barrier, efficiently
   counteracting the mass accumulation everywhere.  But there is no physical
   mechanism for spatially uniform Phi_dot.

2. **Natural processing** (Phi_dot ~ X/tau ~ M/r^2/tau) concentrates
   energy at small r where the gravitational source is strong.  This
   leaves intermediate radii underprocessed.

3. **Collapse processing** (Phi_dot ~ delta_X/tau) is even more concentrated,
   resembling the relaxation profile.  It cannot fix the metric globally.

**The hierarchy of efficiency:**

    Uniform >> Natural > Gaussian > Relaxation

More concentrated profiles require more total processing energy to achieve
the same metric improvement.

---

## J. Way Forward

The global_robust classification of the static equilibrium obstruction
under dynamical processing suggests several directions:

1. **Non-quasi-static dynamics**: Wave propagation effects (not captured
   in the quasi-static approximation) might redistribute processing energy.

2. **Self-consistent source evolution**: The source X(r,t) = m(r,t)/r^2
   evolves with m, potentially creating a feedback that redistributes
   processing.

3. **Route B (Galley) formulation**: Different effective stress-energy
   might produce different spatial distribution of processing.

4. **External forcing**: Non-equilibrium driving could maintain processing
   energy without relying on transient collapse dynamics.

5. **Modified equilibrium**: A different static equilibrium (Phi != X)
   might have different mass accumulation properties.

---

## K. Computational Artifacts

| File | Purpose |
|:---|:---|
| `grut/dynamical_interior.py` | Core module: profiles, snapshots, evolution, classification |
| `benchmark_phase6b_dynamical_interior.py` | Benchmark: 82 checks, all pass |
| `tests/test_dynamical_interior.py` | pytest: 90 tests, all pass |

**Engine**: Python 3.9+ with numpy
**Methods**:
- Radial snapshot: trapezoidal mass integral on log-spaced grid
- Threshold scan: amplitude sweep with linear interpolation for zero-crossing
- Profile library: 4 types (uniform, natural, relaxation, gaussian)
- Time evolution: explicit Euler with GRUT first-order relaxation
- Classification: spatial (local/global) x temporal (transient/robust)
- Anisotropy: compare include_phi_prime True vs False threshold scans

---

## L. Explicit Nonclaims

1. The quasi-static evolution uses constraint equations at each time
   step without solving the full hyperbolic Einstein-scalar PDE.
   Wave propagation effects are not captured.

2. The lapse factor e^{-2nu} is approximated as 1 when computing
   kinetic energy.  The true lapse evolves self-consistently.

3. The collapse perturbation is parameterized, not self-consistent.

4. The 11.5% Phase 6 result is specific to UNIFORM processing energy
   and is therefore OPTIMISTIC.  The natural profile threshold is ~106%.

5. The transient metric positivity window depends on the collapse
   amplitude and timescale, both free parameters.

6. The Phi' spatial gradient is computed from the equilibrium derivative,
   not from the evolved Phi(r,t).

7. Whether the dynamical processing window prevents singularity
   formation requires global analysis not addressed here.

8. The quasi-static approximation breaks down when Phi changes
   on timescales shorter than the light-crossing time of the barrier.

9. No observational predictions are made.

10. The threshold classification depends on the specific perturbation.

11. V(Phi) = Phi^2/(2*tau^2) is the Route A candidate potential.

12. Self-consistency is limited: X(r,t) = m(r,t)/r^2 uses constraint
    mass, not a fully coupled solution.

13. Tau is fixed at the canonical value.

---

## Phase 1-6B Result Lock

    Phase 1 (T^Phi):              LOCKED (DeltaT = 0, Factorization Theorem)
    Phase 2 (Phi_-):              LOCKED (consistent, not attractor, IR-dominated)
    Phase 3 (h_-):                LOCKED (consistent, vacuum stable, sourced unstable)
    Phase 4 (Einstein+T^Phi):     LOCKED (rho<0, ODE correct, SIGN CORRECTED: mass accumulates)
    Phase 5 (Route A KG):         LOCKED (T^Phi universal, omega^2=k^2+1/tau^2, w=-1)
    Phase 6 (TOV Integration):    LOCKED (f(R_eq) = -17.71 static, Phi_dot_crit/Phi_dot_nat = 11.5%)
    Phase 6B (Dynamical Interior): LOCKED (uniform optimistic, natural A_crit = 1.06, global_robust)
    Metric Factorization:          LOCKED (diss kernel silent in metric sector)
    Route B overall:               COMPLETE (physical-limit derived)
    Phase V obstruction:           CONFIRMED GENUINE at static equilibrium
    Critical processing (uniform): 11.5% of natural rate (OPTIMISTIC, not physical bound)
    Critical processing (natural): 106% of natural rate (physically motivated)
    Interior metric:               NOT ACHIEVED statically; NOT ACHIEVED dynamically (global_robust)
    Modified TOV:                  SINGULAR (no smooth self-consistent static solution)
    Anisotropy:                    SELF-QUENCHING at f=0 (< 1% effect on threshold)
    Profile dependence:            UNIFORM >> NATURAL > GAUSSIAN > RELAXATION
