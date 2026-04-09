# Sector 4 — Gravity: Mathematical Scaffold

## Symbol table

| Symbol | Meaning | Status |
|--------|---------|--------|
| G_mu_nu | Einstein tensor | External (GR) |
| T_mu_nu^Phi | Constitutive-field stress-energy | Computed |
| Phi | Constitutive scalar field | GRUT primitive |
| tau | Constitutive relaxation time | A2 |
| f(r) | Metric function (1 - 2m(r)/r) | Computed |
| m(r) | Mass function | Computed |
| R_eq | Equilibrium radius | Computed |
| rho_eq | Equilibrium energy density = -M^2/(2 tau^2 r^4) | Derived |

## 1. Gravity identity

GRUT does NOT derive gravity. Einstein's field equations are taken as given:

    G_mu_nu = 8 pi G / c^4 * T_mu_nu

GRUT provides the SOURCE T_mu_nu through the constitutive field Phi:

    T_mu_nu^Phi = (constitutive stress-energy from Phi dynamics)

This is a matter theory within standard GR, not a gravity theory.

## 2. Semiclassical coupling structure

The constitutive scalar Phi obeys the directed-response law on a curved background:

    tau d_t Phi + Phi = X[g_mu_nu]

where X depends on the metric (through curvature coupling). The metric is sourced by T^Phi through Einstein's equations. This creates a coupled system:

    metric -> curvature -> X[g] -> Phi -> T^Phi -> metric (backreaction loop)

**Status:** The forward direction (metric -> Phi evolution) is implemented. The full backreaction loop is NOT self-consistently closed in general.

## 3. Static TOV interior (LOCKED NEGATIVE RESULT)

For a static, spherically symmetric interior with scalar equilibrium:

    rho_eq(r) = -M^2 / (2 tau^2 r^4)

The TOV-like ODE system gives:

    f(R_eq) = -17.71     [WORSENS interior; more negative than Schwarzschild f = -5]
    m(R_eq) = 3.118 km   [mass accumulation confirmed]

**Verdict:** The constitutive scalar field makes the interior metric WORSE, not better. This is a locked negative result. Static scalar-only singularity resolution is RULED OUT.

## 4. Dynamical interior (TRANSIENT)

Adding time dependence (Phi_dot != 0):

- Kinetic contribution lifts NEC saturation: w != -1 during processing
- Critical amplitude A_crit ~ 0.93 (vs uniform 11.5%)
- Metric positivity is TRANSIENT: f > 0 during a processing window of order tau
- At late times, f returns to f < 0

**Verdict:** Dynamic processing provides temporary metric improvement but NOT permanent singularity resolution.

## 5. Singularity resolution — all routes failed

10 routes tested, all FROZEN:

| Route | Mechanism | Result |
|-------|-----------|--------|
| Scalar-only static | rho_eq sources TOV | f = -17.71 (WORSENS) |
| Scalar-only dynamic | time-dependent Phi | Transient only |
| Defect (D6) | Topological defect energy | Additive support, insufficient alone |
| D7/D8 combined | Portal coupling + amplification | Sign error: A_eff = 0.11, not 2.0 |
| Self-consistent defect | Picard iteration | f ~ 0.7, not positive |
| Five correction classes | 1/r^n, exponential, etc. | All insufficient for deficit |

**Status:** FROZEN. No identified path to singularity resolution.

## 6. Weak-field exterior

The constitutive equilibrium modifies the exterior Schwarzschild metric:

    delta_f(r) = -4 pi M^2 / (tau^2 r^2)

PPN deviation: delta_beta = 4 pi / tau^2 (geometric units).

At any physical tau: delta_beta ~ 10^-16 (observationally silent).

**Status:** Analytically constrained. Consistent with solar system tests. No observable prediction.

## 7. Relation to Sector 3

The gravitational DECOHERENCE sector (Sector 3) is the only gravity-facing sub-sector with novel predictive content. It operates semiclassically: the Newtonian gravitational self-energy enters the CTP influence functional. Sector 3 does NOT require full backreaction, graviton, or singularity resolution.

Sector 4 documents the BROADER gravity sector, including the failed strong-field program and the established semiclassical identity.

## 8. Missing ingredients (explicit)

| Ingredient | Status | Difficulty |
|------------|--------|------------|
| Graviton | Not present | Extreme |
| Full backreaction | Not closed | Very high |
| UV completion | Not present | Extreme |
| Singularity resolution | All routes failed | Unknown (needs new mechanism) |
| Native gravity derivation | Not claimed | Extreme |
| Emergent spacetime | Not present | Extreme |
