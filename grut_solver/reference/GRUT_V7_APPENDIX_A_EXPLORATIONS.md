# GRUT v7 — Appendix A: Exploratory Results

## Constitutive Cosmology, Kernel Unification, and the Bridge Parameter

*Results from the v7 exploration session. These are computed but exploratory —
they extend the framework beyond the core v7 document.*

---

## A1. Toy Constitutive Cosmology

The constitutive equation tau dH/dt + H = H_target(t) reproduces the full
expansion history of the universe when tau is derived from the CTP
fluctuation-dissipation theorem.

### The KMS-derived relaxation time

    tau_KMS = hbar / (2 pi k_B T)

This is DERIVED from the KMS (Kubo-Martin-Schwinger) condition for thermal
equilibrium in the CTP formalism. The same CTP structure that gives the
noise kernel (and therefore Lambda_grav) also gives the dissipation kernel
(and therefore tau).

### Results

| Epoch | H_constitutive | H_standard | Deviation |
|:---|:---|:---|:---|
| 1 second | 5.000 × 10^-1 | 5.000 × 10^-1 | 0.00% |
| 1 minute | 8.367 × 10^-3 | 8.333 × 10^-3 | 0.41% |
| 1 hour | 1.394 × 10^-4 | 1.389 × 10^-4 | 0.41% |
| 1 year | 1.591 × 10^-8 | 1.585 × 10^-8 | 0.41% |
| 50,000 yr | 3.178 × 10^-13 | 4.220 × 10^-13 | 24.7% (transition) |
| 1 Gyr | 2.120 × 10^-17 | 2.111 × 10^-17 | 0.41% |
| 9.8 Gyr | 2.162 × 10^-18 | 2.153 × 10^-18 | 0.44% |
| 13.8 Gyr | 1.885 × 10^-18 | 1.885 × 10^-18 | 0.00% |

Mean deviation: 0.43%. BBN-safe (deviation ~ 10^-20%). CMB-safe.

### Features

- No singularity: H bounded (requires full constitutive gravity, not KMS alone)
- Radiation era: reproduced to 0.4%
- Matter era: reproduced to 0.4%
- Vacuum approach: H → H_inf exactly (fixed point)
- Arrow of time: structural (Axiom A1, retarded variation)
- Three-phase structure: radiation → matter → vacuum

### Honest negatives

- H_target(t) encodes standard Friedmann cosmology as input
- The 25% at matter-radiation equality is a toy artifact (hard switch in target)
- Singularity regularization requires full constitutive gravity, not just H(t)
- This is a TOY MODEL — quantitative precision requires CTP-derived H_target

---

## A2. Kernel Unification Attempt

### The claim tested

"One CTP kernel gives BOTH Lambda_grav (decoherence) AND tau (cosmological relaxation)."

### What was found

The Diósi gravitational noise kernel N = G/(hbar|x-x'|) gives:

**Output (a):** Lambda_grav = G m^2 S(l/R) / (hbar l) — CORRECT, DERIVED

**Output (b):** tau_dissipation = 2 k_B T / N_eff(Hubble) — gives tau ~ 10^-85 s at BBN

The gravitational kernel at the Hubble scale gives an unreasonably small tau.
The cosmological tau_0 = 41.9 Myr does NOT come from the Diósi kernel integrated
at the Hubble scale. It comes from the 3-loop anomaly structure (C_FINAL, S).

### The honest picture

- Lambda_grav comes from the noise kernel (imaginary part of influence functional)
- H_inf comes from the 3-loop anomaly structure (nonlocal operator R ln(Box) R)
- tau_0 connects them through the decoherence surface tau(m, l) = hbar l/(G m^2)
- Both use C_FINAL, but through different routes (normalization vs anomaly)

The unification is at the level of S_CTP (one action, multiple outputs),
not at the level of a single kernel integration.

---

## A3. The Bridge Parameter

### The central finding

    tau_0 = hbar l / (G m^2)

The FORMULA is derived from the noise kernel.
The VALUE (41.9 Myr) depends on the evaluation point: m = 20,818 amu, l = 1 um.

### What determines the evaluation point?

**Attempted:** Self-referential condition l = R gives m ~ 500 amu at water density.
Does NOT match the 20,818 amu. The relevant separation l = 1 um is far-field
(500× larger than the object at any condensed-matter density).

**Conclusion:** No GRUT-native scale selection principle currently determines
the evaluation point. The specific (m, l) is characteristic of the decoherence
crossover regime but is not uniquely selected by the CTP structure.

### The experimental resolution

The decoherence experiment would fix tau_0 independently:
- Measure Lambda_grav at ANY (m, l)
- Infer tau_0 = hbar l / (G m^2 Lambda_grav)
- Then H_inf = (2-R)/(S tau_0) becomes a PREDICTION

This flips the framework from "fitted" to "predictive."

### Status

tau_0 is the one bridge parameter connecting the decoherence sector to cosmology.
It is experimentally determinable. The scale selection problem is the deepest
open question remaining in GRUT.

---

## A4. The GRUT Interpretation of Cosmic Origins

The constitutive equation suggests a specific picture of the origin:

- **The "beginning"** is not a singular creation event but a highly non-equilibrium
  state far from the fixed point z = z_target[z]
- **Time** is the process of convergence toward self-consistency
- **The arrow of time** is structural (Axiom A1: retarded, not advanced)
- **Dissipation and noise** are fundamental, not added — both come from S_CTP
- **Classical physics** emerges as the fixed-point regime where relaxation is complete

This is an INTERPRETATION of the framework's mathematics, not a new computation.
It is consistent with the computed expansion history (Appendix A1) but does not
add predictive content.

---

*D. Ryan Grover, April 2026.*
*GRUT v7 Appendix A: Exploratory Results.*
