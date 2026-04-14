# GRUT v7 — Appendix C: Constitutive Gravity and Field Equations

## How GR Emerges from the CTP Constitutive Structure

---

## C.0 — Purpose

This appendix derives the constitutive gravity equation from S_CTP and shows
how General Relativity is recovered as the instantaneous-response limit. This
is the most important structural bridge in the framework: it connects the
abstract CTP action to the physical spacetime dynamics.

---

## C.1 — From S_CTP to the Constitutive Gravity Equation

The CTP effective action for gravity uses the metric g_mn as the dynamical variable.
In the Keldysh basis: g_r = (g+ + g-)/2, g_a = g+ - g-.

The retarded variation (Axiom A1):

    delta S_CTP / delta g_a |_{g_a=0} = 0

gives the retarded equation of motion for the metric. At the classical level,
this IS the Einstein equation:

    G_mn + Lambda g_mn = 8 pi G T_mn

The constitutive PROJECTION replaces the second time derivative in the Einstein
equation with a first-order relaxation:

    d^2 g / dt^2  →  (1/tau_grav) dg/dt

This gives the constitutive gravity equation:

    G_mn + tau_grav P_mn^ab u^l nabla_l G_ab = 8 pi G T_mn               (C.1)

where P_mn^ab is the transverse (Israel-Stewart) projector and u^mu is the
preferred timelike direction (cosmological rest frame).

---

## C.2 — Status of the Projection

| Sector | Underlying dynamics | Projection status |
|:---|:---|:---|
| QM (Schrodinger) | First-order | EXACT (no projection) |
| Decoherence | Noise kernel | EXACT (no projection) |
| Gravity (Einstein) | Second-order | HEURISTIC (projection) |
| Cosmology (Friedmann) | Second-order | HEURISTIC (projection) |

**The three independent derivation routes** (main document, Section 4) show that
the first-order form is universal for coarse-grained open systems. The projection
is not arbitrary — it is the Markovian limit of the Mori-Zwanzig memory kernel.
But it IS a limit, and the exact kernel may have non-Markovian corrections.

**Critical finding (projection-dependence audit):** All DERIVED and COMPUTED
results in GRUT are projection-INDEPENDENT. The decoherence rate comes from
the noise kernel. The cosmological constant comes from the 3-loop anomaly
structure. The projection affects only STRUCTURAL results (graviton propagator,
singularity regularization, GW effects — all observationally dead or already
labeled as structural).

---

## C.3 — Recovery of GR

In the limit tau_grav → 0 (instantaneous response):

    G_mn + tau_grav × (...) → G_mn = 8 pi G T_mn

which IS the Einstein equation. The constitutive correction is multiplicative:

    G_R^GRUT(omega) = G_R^GR(omega) / (1 - i omega tau_grav)

At low frequencies (omega tau_grav << 1): GRUT = GR.
At LIGO frequencies (100 Hz): |correction| < 10^-10. Undetectable.

---

## C.4 — What the Constitutive Term Adds

The tau_grav term in (C.1) provides:

1. **UV completion:** The graviton propagator falls as 1/omega^3 (vs 1/omega^2 in GR).
   No ghost (extra pole is purely imaginary, dissipative). Spectral function positive.

2. **Singularity regularization:** H bounded at ~1/tau_Planck by the dissipative cap.
   The curvature K_Kretschner is bounded at Planck scale for FRW and Schwarzschild.

3. **Memory:** The constitutive equation has retarded memory through the kernel
   K(t-t') = (1/tau) exp(-(t-t')/tau). This provides the channel for BH information
   transfer (99.94% recovery in the tau_0 branch).

4. **Cosmological fixed point:** At the de Sitter attractor, dG/dt = 0 and the
   constitutive term vanishes. The fixed point IS the GR de Sitter solution.
   The constitutive dynamics determine HOW the universe reaches de Sitter,
   not WHAT the de Sitter state is.

---

## C.5 — The Bianchi Identity

The Einstein tensor satisfies nabla^m G_mn = 0 (Bianchi identity). The constitutive
term must preserve this for consistency:

| Form | nabla^m (LHS) = 0? | Status |
|:---|:---|:---|
| Naive (tau dG/dt) | FAILS | The tau term violates Bianchi |
| Projected (P^ab projector) | PASSES | Israel-Stewart projector preserves it |
| Linearized (h_mn perturbation) | PASSES | Commutator vanishes in flat background |

The projected form (C.1) is the unique first-order extension of GR that
preserves the Bianchi identity at linearized level. This is not a choice —
it is forced by consistency.

---

## C.6 — Limitations

- The projection is heuristic for the full nonlinear Einstein equation
- Non-Markovian corrections (higher-order memory) are not included
- The preferred frame u^mu breaks manifest Lorentz invariance (cosmological frame)
- Full tensor stability (Bardeen potentials + vector modes) is not verified
- Self-consistent tau_grav(H) requires the exact CTP influence functional

**These limitations affect only STRUCTURAL results.** All COMPUTED and DERIVED
results are projection-independent (see main document, Projection-Dependence Audit).

---

*D. Ryan Grover, April 2026.*
