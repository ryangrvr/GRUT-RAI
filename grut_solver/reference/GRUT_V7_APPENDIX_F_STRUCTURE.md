# GRUT v7 — Appendix F: Emergence of Structure

## Constitutive Perturbation Growth — An Honest Negative

---

## F.0 — Purpose

This appendix tests whether the constitutive equation can describe
the growth of cosmic structure (density perturbations → galaxies).
The result is an HONEST NEGATIVE: the first-order constitutive equation
cannot grow perturbations. Structure formation requires the full
second-order Jeans equation.

---

## F.1 — The Constitutive Perturbation Equation

The standard Jeans equation for density contrast delta = delta_rho/rho:

    d^2(delta)/dt^2 + 2H d(delta)/dt = 4 pi G rho delta              (F.1)

This is SECOND-ORDER. The constitutive projection replaces d^2/dt^2 with
(1/tau) d/dt:

    tau d(delta)/dt + delta = delta_target(delta, t)                    (F.2)

with delta_target = delta × (1 + tau × 4 pi G rho) for growth modes.

---

## F.2 — The Computation

Evolving (F.2) from matter-radiation equality (z ~ 3400, t ~ 50,000 yr)
to today (z = 0, t = 13.8 Gyr) using the KMS-derived tau:

| Epoch | delta (standard) | delta (constitutive) | Ratio |
|:---|:---|:---|:---|
| Equality (50,000 yr) | 1.0 × 10^-5 | 1.0 × 10^-5 | 1.000 |
| 100 Myr | 1.6 × 10^-3 | 1.0 × 10^-5 | 0.006 |
| 1 Gyr | 7.4 × 10^-3 | 1.0 × 10^-5 | 0.001 |
| Today (13.8 Gyr) | 3.4 × 10^-2 | 1.0 × 10^-5 | 0.0003 |

**Growth factor (equality → today):**
- Standard (Jeans): D = 3,375
- Constitutive: D = 1.0

**The constitutive equation produces ZERO perturbation growth.**

---

## F.3 — Why It Fails

The Jeans instability is fundamentally second-order: it requires
ACCELERATION (d^2 delta/dt^2), not just velocity (d delta/dt).
A mass element falls toward an overdensity with increasing speed —
this acceleration is what makes perturbations grow.

The constitutive projection replaces acceleration with relaxation:
the system approaches its target at rate 1/tau. But with tau_KMS ~ 10^-22 s,
the system reaches its target INSTANTANEOUSLY at each step. And the target
at each step barely differs from the current state:

    delta_target - delta = tau × 4 pi G rho × delta ~ 10^-28 × delta

After one age of the universe: total growth = exp(10^-29) = 1.000000.

---

## F.4 — What This Means for GRUT

This is CONSISTENT with the projection-dependence audit (main document):

| Result type | Depends on projection? | Works? |
|:---|:---|:---|
| Lambda_grav (decoherence) | NO (noise kernel) | YES |
| H_inf (cosmological constant) | NO (3-loop CTP) | YES |
| eta_B (baryogenesis) | NO (CTP anomaly) | YES |
| Perturbation growth | YES (second-order → first-order) | **NO** |
| GW phase shift | YES | Dead (10^-39 rad) |
| QNM modification | YES | Dead (10^-80) |

Every result that depends on the constitutive projection is either
observationally dead OR fails to reproduce known physics. Every result
that is projection-independent works.

**The constitutive projection is not load-bearing.** The framework's
successes come from the CTP action's noise kernel, anomaly structure,
and algebraic properties — none of which use the projection. The
projection provides a pedagogical organizing principle (one equation
for all sectors) but the actual predictions bypass it.

---

## F.5 — Structure Formation in GRUT

Structure formation in GRUT must come from the FULL second-order Jeans
equation, not the constitutive first-order approximation:

    d^2(delta)/dt^2 + 2H d(delta)/dt = 4 pi G rho delta

This is standard GR perturbation theory. GRUT modifies H(t) through the
constitutive cosmology (Appendix B), which gives H within 0.4% of Friedmann.
The perturbation growth therefore proceeds essentially identically to
standard cosmology (with <1% modification from the H(t) difference).

**What GRUT provides for structure formation:**
- The expansion history H(t) (from constitutive cosmology, 0.4% accurate)
- The initial perturbation spectrum (from CTP noise, qualitatively)
- The decoherence threshold (determining when structures become classical)

**What GRUT does NOT provide:**
- A first-principles constitutive perturbation equation that works
- A prediction for sigma_8 or the matter power spectrum shape
- Any modification to standard structure formation

---

## F.6 — Stability Under Noise: What IS Computable

While perturbation GROWTH requires second-order dynamics, the STABILITY
of structures once formed is a first-order question that the constitutive
equation can address.

A structure is stable in GRUT if:
1. It is a fixed point: z* = z_target[z*]
2. All eigenvalues |lambda_i| < 1 (attractor)
3. CTP noise amplitude < basin width (survives fluctuations)

| Structure | Binding [eV] | Lambda_grav [Hz] | Xi (1 s) | Stable? |
|:---|:---|:---|:---|:---|
| Nuclei | ~10^6 | ~10^-50 | ~10^-50 | Quantum-stable |
| Atoms | ~10 | ~10^-50 | ~10^-50 | Quantum-stable |
| Molecules | ~0.1 | ~10^-40 | ~10^-40 | Quantum-stable |
| Proteins | ~0.01 | ~10^-16 | ~10^-16 | Near boundary |
| Cells | ~k_BT | ~10^-5 | ~10^-5 | Marginally classical |
| Planets | ~GM^2/R | ~10^30 | ~10^30 | Classical-locked |

The constitutive equation correctly predicts which structures PERSIST
(all of them, from atoms to planets), even though it cannot predict
how they FORM (which requires second-order gravitational instability).

---

## F.7 — Limitations

- **Perturbation growth: HONEST NEGATIVE.** The constitutive first-order
  equation cannot grow density perturbations. This is a fundamental
  limitation of the projection for second-order dynamics.
- Structure formation must use the standard Jeans equation with H(t)
  from the constitutive cosmology as input
- The stability analysis (F.6) is qualitative, not a detailed computation
- No sigma_8 prediction, no power spectrum shape, no BAO scale

---

*D. Ryan Grover, April 2026.*
*GRUT v7 Appendix F: Emergence of Structure.*
