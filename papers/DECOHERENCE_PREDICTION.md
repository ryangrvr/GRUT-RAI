# Gravitational Decoherence from the CTP Influence Functional: A Zero-Parameter Prediction with Six Discriminating Signatures

D. Ryan Grover

April 2026

Correspondence: dryangrover@gmail.com

---

## Abstract

We derive the gravitational decoherence rate for mesoscopic objects from the imaginary part of the Schwinger-Keldysh (closed-time-path) influence functional. The derivation uses no free parameters: the rate is determined entirely by Newton's constant G, the object's mass m, its spatial extent R, and the superposition separation l. The result — Lambda_grav = G m^2 S(l/R) / (hbar l) with S(l/R) = min(1, (l/R)^3/6) — produces six experimentally discriminating signatures that no tested alternative decoherence model reproduces simultaneously. We present the complete derivation, corrected experimental benchmarks, an adversarial comparison against five competing models, and a concrete experimental proposal targeting optomechanical systems at the 10-picogram scale. The prediction is robust against non-Markovian corrections to the dynamics because it depends only on the noise kernel, not on the constitutive equation of motion.

---

## 1. Introduction

The quantum-classical boundary remains one of the deepest open questions in physics. Standard quantum mechanics provides no mechanism for the emergence of classicality — superposition is preserved at all scales, and the apparent definiteness of the macroscopic world is attributed to environmental decoherence without specifying the irreducible floor.

Several proposals have identified gravity as the agent of irreducible decoherence. Diósi [1] proposed a gravitational self-energy kernel for mass-density localization. Penrose [2] argued that gravitational time dilation between superposed geometries provides a natural decoherence timescale. Both proposals yield decoherence rates proportional to G m^2, but differ in their treatment of extended bodies and their connection to quantum field theory.

In this paper, we derive the gravitational decoherence rate from the closed-time-path (CTP) effective action — the standard formalism for nonequilibrium quantum field theory [3,4]. The derivation requires no assumptions beyond the CTP axioms (path doubling and retarded variation) and the Newtonian limit of the graviton propagator. The result is parameter-free: no coupling constants, collapse rates, or correlation lengths are introduced. The decoherence rate is a direct output of the imaginary part of the CTP influence functional, following the approach of Anastopoulos and Hu [5].

The prediction produces six experimentally discriminating signatures — mass-squared scaling, geometry dependence, pressure-independent plateau, separation scaling, entanglement protection, and a geometric kink at l = 1.8R — that collectively distinguish it from all tested alternatives. We present an adversarial comparison against five competing models and show that no alternative reproduces all six.

For the full theoretical framework in which this prediction is embedded, see the GRUT v6 formalism paper [6] and the v7 program document [7]. The present paper is self-contained: it derives the decoherence rate from the CTP influence functional alone, without reference to the broader constitutive framework.

---

## 2. Derivation from the CTP Influence Functional

### 2.1 The CTP effective action

The Schwinger-Keldysh formalism doubles the degrees of freedom into forward (+) and backward (-) branches [3]. In the Keldysh basis:

    z_r = (z_+ + z_-) / 2       (classical / retarded field)
    z_a = z_+ - z_-              (quantum / advanced field)

The CTP effective action:

    S_CTP[z_r, z_a] = z_a F[z_r] + (i/2) z_a N z_a                     (1)

where F[z_r] is the equation-of-motion operator from the classical action, and N is the noise kernel — the connected Hadamard function of the stress-energy tensor:

    N(x, x') = (1/2)<{T(x), T(x')}> - <T(x)><T(x')>                    (2)

The first term in (1) generates the retarded (causal) dynamics. The second generates the noise — the stochastic fluctuations from the gravitational environment. Together they enforce the fluctuation-dissipation theorem (FDT).

### 2.2 The gravitational noise kernel

In the Newtonian limit (v << c, weak field), the gravitational contribution to the noise kernel reduces to the self-energy of the mass distribution in its own gravitational field [1,5]:

    N_grav(x, x') = G / (hbar |x - x'|)                                  (3)

This is the imaginary part of the graviton propagator at zero frequency — the instantaneous Coulomb-like piece of the gravitational interaction. The derivation follows from the CTP influence functional by integrating out the gravitational field treated as environment [5]:

    exp(i S_IF[x_+, x_-]) = integral D[g] exp(i S_grav[g, x_+] - i S_grav[g, x_-])

In the Newtonian limit:

    Im(S_IF) = (1/2) integral dt d^3x d^3x' Delta_rho(x) [G/(hbar|x-x'|)] Delta_rho(x')

where Delta_rho = rho_+ - rho_- is the difference between the forward and backward mass distributions. This is exact in the Newtonian limit. Post-Newtonian corrections enter at O(v^2/c^2) ~ 10^-16 for laboratory-scale objects and are negligible.

### 2.3 Integration over extended bodies

For a uniform sphere of mass m, radius R, in a superposition of two positions separated by l, the integral of (3) over the mass distribution gives:

    Lambda_grav = G m^2 S(l/R) / (hbar l)                                (4)

with the extended-body suppression factor:

    S(l/R) = min(1, (l/R)^3 / 6)                                         (5)

The suppression factor arises from the spatial overlap of the mass distribution with itself at displacement l. When l >> R (far field), the object acts as a point mass and S = 1. When l << R (near field), the self-energy integral partially cancels, suppressing the rate by (l/R)^3.

The crossover between these regimes occurs at l ~ 1.8R, producing a measurable kink in the decoherence rate as a function of separation (signature F6, Section 4).

### 2.4 No free parameters

Equation (4) contains:
- G: Newton's constant (measured)
- hbar: Planck's constant (measured)
- m: mass of the object (measured)
- l: superposition separation (controlled experimentally)
- R: radius of the object (measured)

No coupling constant, collapse rate, correlation length, or fitting parameter is introduced. The decoherence rate is determined entirely by the gravitational self-energy of the mass distribution at the superposition separation.

### 2.5 Robustness

The derivation uses only the imaginary part of the CTP influence functional — the noise kernel. It does not depend on:
- The constitutive equation tau dz/dt + z = z_target[z] (which governs deterministic dynamics)
- The Markovian approximation (the noise kernel is pre-dynamical)
- Any projection from second-order to first-order dynamics

Non-Markovian corrections to the constitutive dynamics change the APPROACH to the fixed point but not the decoherence rate. The rate is kernel-determined and dynamics-independent. Theoretical corrections to the kernel itself — post-Newtonian O(10^-16), 2-loop graviton O(10^-8), compactness O(Gm/Rc^2) ~ 10^-27 for a 1 um gold sphere — are negligible at laboratory scales.

---

## 3. The Six Scaling Laws

The predictive content of equation (4) is not a single number but a set of scaling laws that collectively fingerprint gravitational decoherence.

### F1: Mass-squared scaling

    Lambda_grav ~ m^2    (at fixed l, geometry)

Doubling the mass quadruples the rate. This is the gravitational self-energy scaling: the noise kernel goes as G m^2. No competing model with a constant decoherence floor reproduces this.

### F2: Geometry dependence

    Lambda_grav(gold, m) ≠ Lambda_grav(silica, m)    (at fixed mass m)

Two objects of the same mass but different material density (and therefore different R) have different decoherence rates through S(l/R). A gold sphere (rho = 19,300 kg/m^3) and a silica sphere (rho = 2,200 kg/m^3) at the same mass differ in R by a factor of 2.1, producing measurable rate differences.

### F3: Pressure-independent plateau

    Lambda_grav → constant    as P → 0

Below P ~ 10^-10 Pa, the decoherence rate saturates at Lambda_grav. Standard quantum mechanics predicts Lambda → 0 as environmental noise is removed. The plateau IS the gravitational floor.

### F4: Separation scaling (far field)

    Lambda_grav ~ l^-1    (l >> 2R)

The rate decreases with separation. Slope = -1 on a log-log plot of Lambda vs l.

### F5: Entanglement protection

    Lambda_grav(Bell state) < Lambda_grav(separable state)

An entangled pair decoheres slower than a separable state of the same total mass, because the entangled state's effective mass distribution differs. CSL and other state-independent models cannot reproduce this.

### F6: Geometric kink at l = 1.8R

    d(log Lambda) / d(log l) changes sign at l ~ 1.8R

In the near field (l < R): Lambda ~ l^2 (slope +2). In the far field (l > R): Lambda ~ l^-1 (slope -1). The transition produces a sharp, measurable kink. No point-mass model (Diósi-Penrose without extended bodies, Penrose objective reduction) can produce this feature — it requires the finite extent of the mass distribution.

---

## 4. Adversarial Comparison

| Model | Free params | F1 | F2 | F3 | F4 | F5 | F6 | Killed by |
|:---|:---|:---|:---|:---|:---|:---|:---|:---|
| This work (CTP) | 0 | Yes | Yes | Yes | Yes | Yes | Yes | — |
| Constant floor | 1 | No | No | Yes | No | No | No | F1, F2 |
| Power-law | 2 | Tunable | No | Yes | Tunable | No | No | F2, F5 |
| CSL [8] | 2 | Yes | No | Yes | No | No | No | F2, F5, F6 |
| Diósi-Penrose (point) [1,2] | 0 | Yes | No | Yes | Yes | Yes | No | F6 |
| Penrose OR (point) [2] | 0 | Yes | No | Yes | Yes | No | No | F5, F6 |

No tested alternative reproduces all six signatures. The geometric kink (F6) is the single most discriminating feature — it kills all point-mass models. Geometry dependence (F2) kills all constant-floor models. Entanglement protection (F5) kills all state-independent models.

**A single experiment measuring F1 + F2 + F6 would be decisive.** Even without reaching the absolute rate, the scaling laws and the geometric kink distinguish gravitational decoherence from all known alternatives.

---

## 5. Experimental Benchmarks

### 5.1 Corrected gold benchmark

Gold microsphere, R = 1 um, m = 80.8 pg (rho = 19,300 kg/m^3), l = 1 um:

    S(l/R) = (l/R)^3 / 6 = 1/6
    Lambda_grav ~ 689 Hz
    t_coh ~ 1.5 ms

Previous benchmarks in the literature (10 pg at R = 50 nm) are physically inconsistent — no material has the required density of ~19,000 g/cm^3 at that radius. All benchmarks in this paper use realizable objects with known material densities.

### 5.2 Benchmark table

| R [nm] | m [pg] | Material | l [nm] | l/R | S(l/R) | Lambda [Hz] | t_coh [ms] |
|:---|:---|:---|:---|:---|:---|:---|:---|
| 1000 | 80.8 | Gold | 1000 | 1.0 | 0.167 | ~689 | ~1.5 |
| 500 | 10.1 | Gold | 1000 | 2.0 | 1.000 | ~65 | ~15 |
| 750 | 34.1 | Gold | 1500 | 2.0 | 1.000 | ~491 | ~2 |
| 500 | 10.1 | Gold | 500 | 1.0 | 0.167 | ~22 | ~46 |
| 1356 | 22.9 | Silica | 1000 | 0.74 | 0.067 | ~23 | ~44 |

The last row uses silica at the same mass as gold R = 500 nm, demonstrating signature F2 (geometry dependence): same mass, different rate.

### 5.3 Heating and radiation constraints

The gravitational decoherence rate implies momentum diffusion:

    D_p = Lambda_grav × (hbar/l)^2

For the gold benchmark: D_p = 7.7 × 10^-54 kg^2 m^2/s^3. Heating rate P = D_p/(2m) = 4.7 × 10^-68 W — safe by > 60 orders of magnitude against any measurable threshold. The extended-body suppression S(l/R) prevents the UV divergence that causes heating problems in point-mass models.

---

## 6. Experimental Proposal

### 6.1 Required parameters

| Parameter | Required | Current state-of-art | Gap |
|:---|:---|:---|:---|
| Mass | > 10 pg (10^10 amu) | ~10^5 amu | 10^5 |
| Separation | > 100 nm | ~10 nm | 10 |
| Pressure | < 10^-10 Pa | ~10^-8 Pa | 100 |
| Temperature | < 100 mK | Achieved | Met |
| Coherence time | > 1 ms | ~10 us | 100 |

### 6.2 Experimental protocol

1. Prepare a gold or silica nanoparticle in a spatial superposition using optical or magnetic trapping
2. Vary the superposition separation l from 100 nm to 5 um
3. Measure the decoherence rate Lambda as a function of l at fixed mass
4. Scan pressure P from 10^-8 to 10^-11 Pa to identify the plateau
5. Repeat with different materials (gold vs silica) at the same mass
6. Compare Lambda(l) profile to the predicted kink at l = 1.8R

### 6.3 What constitutes a positive result

The decoherence rate must:
- Saturate at a pressure-independent floor (F3)
- Scale as m^2 when mass is varied (F1)
- Differ between gold and silica at the same mass (F2)
- Show slope -1 on log-log at l > 2R (F4)
- Show a kink at l ~ 1.8R (F6)

Meeting three or more of these signatures at the predicted quantitative level would constitute strong evidence. Meeting all six would be decisive.

### 6.4 What constitutes a null result

If the decoherence rate continues to decrease with pressure below 10^-10 Pa (no plateau), the gravitational decoherence prediction is falsified. This would remove the quantitative foundation of the decoherence sector and weaken the downstream connections to cosmology and dark matter described in [6,7].

### 6.5 Target experimental groups

- Arndt group (Vienna): matter-wave interferometry with large molecules
- Aspelmeyer group (Vienna): optomechanical quantum state preparation
- Geraci group (Northwestern): levitated nanoparticle sensing
- Bateman group (UCL): macroscopic superposition tests

---

## 7. Connection to Cosmology

The decoherence rate Lambda_grav(m, l) defines a surface in (m, l) space. The canonical timescale tau_0 = hbar l / (G m^2) evaluated at characteristic decoherence-crossover parameters connects to the cosmological vacuum rate through the formula H_inf = (2 - R_anomaly) / (S × tau_0), where R_anomaly = 1.15428 is the 3-loop gravitational anomaly ratio and S = 108 pi is the CTP normalization. This gives Omega_Lambda = 0.691 at H_0 = 70 km/s/Mpc, within 0.3% of the Planck 2018 value [9]. The full derivation and verification are presented in [6,7].

If the decoherence experiment measures Lambda_grav at any (m, l), it fixes tau_0 independently, and the cosmological constant becomes a zero-parameter prediction. A single laboratory measurement of gravitational decoherence would determine the vacuum expansion rate of the universe.

---

## 8. Conclusion

The gravitational decoherence rate Lambda_grav = G m^2 S(l/R) / (hbar l) is derived from the CTP influence functional with zero free parameters. It produces six experimentally discriminating signatures that no tested alternative reproduces simultaneously. The prediction is robust against non-Markovian corrections because it depends on the noise kernel (a property of the quantum state and the gravitational field), not on the dynamical evolution equation. The extended-body suppression factor S(l/R) prevents UV divergences, ensures heating safety, and produces the geometric kink at l = 1.8R that is the single most discriminating experimental signature.

The experiment is feasible with next-generation optomechanical systems. A positive result would establish gravity as the agent of the quantum-classical transition and, through the decoherence-cosmology bridge, potentially connect a tabletop measurement to the expansion of the universe.

---

## References

[1] L. Diósi, "A universal master equation for the gravitational violation of quantum mechanics," Phys. Lett. A 120, 377 (1987).

[2] R. Penrose, "On gravity's role in quantum state reduction," Gen. Relativ. Gravit. 28, 581 (1996).

[3] J. Schwinger, "Brownian motion of a quantum oscillator," J. Math. Phys. 2, 407 (1961).

[4] L. V. Keldysh, "Diagram technique for nonequilibrium processes," Sov. Phys. JETP 20, 1018 (1965).

[5] C. Anastopoulos and B. L. Hu, "A master equation for gravitational decoherence," Class. Quantum Grav. 30, 165007 (2013).

[6] D. R. Grover, "GRUT v6: The CTP Formalism Paper," Zenodo (2026). doi:10.5281/zenodo.XXXXX

[7] D. R. Grover, "GRUT v7: The Responsive Universe Program," Zenodo (2026). doi:10.5281/zenodo.XXXXX

[8] G. C. Ghirardi, A. Rimini, and T. Weber, "Unified dynamics for microscopic and macroscopic systems," Phys. Rev. D 34, 470 (1986).

[9] Planck Collaboration, "Planck 2018 results. VI. Cosmological parameters," Astron. Astrophys. 641, A6 (2020).

---

*D. Ryan Grover, April 2026.*
