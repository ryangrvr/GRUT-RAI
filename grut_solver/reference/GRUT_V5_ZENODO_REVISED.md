# GRUT v5 — The Self-Referential Universe (Revised)

**From Neural Resonance to Cosmic Acceleration via the Constitutive Fixed Point**

D. Ryan Grover, April 2026

Correspondence: dryangrover@gmail.com
Full research: www.zenodo.org/communities/grut
Software: github.com/ryangrvr/GRUT-RAI-v1.0
DOI: 10.5281/zenodo.18993690

Status tiers: LOCKED — RECOVERED — PREDICTIVE — CANDIDATE — MAPPED — SIGNATURE — COMPUTED — PARTIAL — NONCLAIM

---

## Abstract

The Grand Responsive Universe Theory (GRUT) is built on a single constitutive equation — tau dz/dt + z = z_target[z] — derived from three axioms (CTP doubling, directed response, complex relaxation). The target functional z_target[z] is specified explicitly in each sector from the CTP influence functional. v5 demonstrates that the self-referential fixed point z = z_target[z] organizes all of physics as one mechanism viewed at different scales.

**Locked results**: Quantum mechanics recovery (12/12 tests), electroweak structure (13/13 tests), gravitational decoherence at zero free parameters (Lambda_grav = 689 Hz for a gold microsphere of radius 1 um and mass 80.8 pg at superposition separation l = 1 um, 14/14 tests).

**New in v5**: (1) The 25-order thermal wall separating gravitational decoherence from biology is bypassed (not breached) by the self-referential fixed point. Two independent routes produce the gamma frequency: gravitational (39.9 Hz) and network topology (41.7 Hz). (2) Cosmic acceleration is the universe crossing matter-Lambda equality at z ~ 0.33 (acceleration onset at z ~ 0.67). A structurally derived formula H_inf = (2 - R_anomaly)/(S x tau_0) predicts an absolute vacuum expansion rate H_inf = 1.885 x 10^-18 Hz. The implied Omega_Lambda depends on the measured H_0: 0.691 at H_0 = 70 km/s/Mpc (0.2% from Planck's 0.6889), ranging to 0.745 at H_0 = 67.4 (8.1%). (3) The same fixed-point condition connects the 40 Hz neural resonance to the cosmological constant through the CTP effective action, bridging Sectors 13 and 5 at a scale ratio of 10^{-19.3}.

**Computed sectors**: Dark matter (solitonic, BPS exact, 10^6-10^13 GeV). **Partial**: Quantum gravity (2/5 closure conditions met: UV completion + classical GR). **Mapped**: QCD confinement (0.81 GeV), flavor (Koide 0.005%), unification (f_self = 0.93). **Signatures**: neutrinos, baryogenesis.

13 sectors, 183 passing tests, one equation, one fixed point. 70-75% of a complete Theory of Everything, honest about the 25-30% it hasn't closed.

---

## 1. The Equation and the Principle

### 1.1 Three Axioms

**A0 (CTP Doubling)**: The closed-time-path (Schwinger-Keldysh) formalism doubles the degrees of freedom into forward (+) and backward (-) paths.

**A1 (Directed Response)**: Variation of the CTP effective action gives the constitutive equation:

    tau dz/dt + z = z_target[z]                    (1)

**A2 (Complex Relaxation)**: tau = tau_R + i tau_I with tau_I = hbar/2 (identified by matching to the Schrodinger equation).

**On the nature of tau_I**: hbar/2 has units of action (J s), not time. The constitutive equation (1) is therefore not a standard relaxation equation in every sector — it recovers the form of a relaxation equation only after sector-specific reinterpretation. In the QM sector, the combination tau_I (dz/dt) with z as a wavefunction and z_target encoding the Hamiltonian yields the Schrodinger equation exactly. The conversion c_2 = tau_I^2/m = hbar^2/(4m) translates to SI units per particle species. In the gravitational sector, tau_0 = 41.9 Myr is a derived timescale (from C_FINAL and cosmological parameters), not tau_I directly.

The "one equation everywhere" claim is structural: the same FORM tau dz/dt + z = z_target[z] appears in each sector, but the physical meaning of tau, z, and z_target shifts between sectors. This is analogous to how the action principle S = integral L dt applies everywhere but the Lagrangian L is sector-specific. The content lives in z_target[z], not in the equation's form alone.

### 1.2 The Fixed Point

The equation has two qualitative regimes:

- **External-target**: z approaches a target set by external forces. Dynamics are fast, driven, subject to decoherence.
- **Self-referential**: z = z_target[z]. The system IS its own target. tau becomes irrelevant. Stable, self-sustaining.

The transition between regimes — the self-referential threshold — is the organizing principle.

### 1.3 Explicit Target Functionals

The constitutive equation has predictive power only when z_target[z] is specified. The target functional is derived from the CTP influence functional in each sector:

**Sector 1 (QM):** z_target[z] = c_0(x) z - c_2 nabla^2 z, where c_0(x) = 1 + V(x)/(hbar omega) and c_2 = hbar^2/(4m). Substitution recovers the Schrodinger equation exactly.

**Sector 3 (Decoherence):** The constitutive equation governs the coherent evolution of z (the center-of-mass wavefunction). z_target is the same as in Sector 1 (potential + kinetic). The decoherence rate Lambda_grav comes from a SEPARATE output of the same CTP action: the imaginary part of the influence functional, Im[S_IF] = (G/hbar) integral of the Diosi self-energy kernel. This noise term drives the system AWAY from z_target, causing loss of coherence. The constitutive equation and the noise kernel are two outputs of one formalism (the CTP action), not one equation doing two things. The decoherence rate is not z_target; it is the strength of the stochastic force in the Langevin extension of the constitutive equation.

**Sector 5 (Cosmology):** z_target(H) = H_inf + (1 - f_self) x (H_Friedmann - H_inf), where H_Friedmann is the standard matter/radiation Hubble rate and f_self is the sigmoid self-referential fraction.

All forms are implemented and tested in the grut_solver codebase.

---

## 2. The 13-Sector Map

| # | Sector | Status | Fixed Point | Key Result |
|---|--------|--------|-------------|------------|
| 1 | Quantum Mechanics | Recovered | Ground state | 12/12 tests |
| 2 | Electroweak/SM | Recovered | EWSB vacuum | 13/13 tests |
| 3 | Decoherence | Predictive | Grav plateau | 689 Hz (gold, 0 params) |
| 4 | Gravity | Partial+ | Singularity cap | H = 1/T_Planck |
| 5 | Cosmology | Candidate | Vacuum H_inf | 1.885e-18 Hz (absolute) |
| 6 | QCD | Mapped | Confinement | 0.81 GeV threshold |
| 7 | Flavor | Mapped | Eigenvalues | Koide 0.005% |
| 8 | Neutrinos | Signature | Near-zero FP | 10^-11 suppression |
| 9 | Dark Matter | Computed (toy) | Solitonic DM | 10^6-10^13 GeV, BPS exact |
| 10 | Baryogenesis | Signature | Asymmetric FP | 3/3 Sakharov |
| 11 | Unification | Mapped | Unified FP | f_self = 0.93 |
| 12 | Quantum Gravity | Partial (2/5) | Spacetime GS | UV complete + classical GR |
| 13 | Neural Resonance | Demonstrated | 40 Hz fixed point | 2 routes match |

---

## 3. The Predictive Core (Sector 3)

    Lambda_grav = G m^2 S(l/R) / (hbar l)          (2)

Zero free parameters. S(l/R) = min(1, (l/R)^3/6) is the extended-body suppression from the Diosi self-energy integral.

**Benchmark (physically consistent):** A gold microsphere of radius R = 1 um has mass m = 80.8 pg at gold density (19,300 kg/m^3). At superposition separation l = 1 um: S(l/R) = (l/R)^3/6 = 1/6. Lambda_grav = 689 Hz. Coherence time: 1.5 ms.

Note: Earlier versions used m = 10 pg with R = 50 nm. These parameters are not mutually consistent for any known material (would require density ~19,000 g/cm^3). The corrected benchmark uses a single physically realizable object. The formula itself is unchanged.

**Alternative benchmark:** Gold microsphere R = 500 nm, m = 10.1 pg, l = 1 um. In the far-field (l = 2R): S = 1, Lambda_grav = 64.6 Hz, t_coh = 15.5 ms.

Six discriminating signatures. Adversarial kill framework. 14/14 tests pass.

### 3.1 The Lindblad Master Equation

The gravitational decoherence channel contributes to the density matrix evolution:

    d rho/dt = -(i/hbar)[H, rho] + Lambda_grav (L rho L^dag - (1/2){L^dag L, rho})     (3)

where L is the position-basis localization operator. This is the standard Lindblad form with the GRUT rate Lambda_grav. Verified to thermalize correctly (max population error 1.4 x 10^-6 vs Boltzmann distribution).

### 3.2 Heating and Radiation Constraints

The gravitational decoherence rate implies momentum diffusion:

    D_p = Lambda_grav x (hbar/l)^2

For the gold benchmark (m = 80.8 pg, l = 1 um): D_p = 7.7 x 10^-54 kg^2 m^2/s^3. The associated heating rate P = D_p/(2m) = 4.7 x 10^-68 W. This is far below any measurable threshold. The extended-body suppression S(l/R) prevents the UV divergence that causes heating problems in point-mass Diosi-Penrose models. This order-of-magnitude estimate suggests no conflict with existing heating or radiation bounds. A complete constraint analysis would require propagating the extended-body regularization through the full noise kernel and comparing to specific experimental bounds (underground radiation limits, precision oscillator heating, cryogenic system constraints). This has not been done.

---

## 4. The Self-Referential Bypass (Sector 13)

The 25-order thermal wall: water at 310 K destroys tubulin coherence 10^25 times faster than gravity. Every known mechanism tested (ordered water, topology, GHZ entanglement) — all fail to close the gap.

The bypass: at the fixed point z = z_target[z], the constitutive equation's driving term (z_target - z) is identically zero. In the constitutive framework, dissipation is driven by the distance |z - z_target(z)|. When this distance is zero, the constitutive dissipation channel is inactive. This does not mean decoherence is "undefined" in the standard Lindblad sense — standard environmental decoherence still operates on the reduced density matrix. The claim is narrower: the constitutive response channel, which is the channel that connects to gravitational decoherence, has zero driving force at the fixed point.

Two routes to 40 Hz: gravitational (N x Lambda_grav x dimers/neuron = 39.9 Hz) and network topology (1/(6 hops x 4 ms) = 41.7 Hz). No common parameters. Not by construction.

Note: The consciousness interpretation (1 Space, edge states, antenna coupling) is speculative. No mechanism for subjective experience is proposed. The computed results — the 40 Hz coincidence, the self-referential fixed point mathematics — are structural, not phenomenological.

---

## 5. The Cosmological Constant (Sector 5)

### 5.1 The 10-Step Derivation Chain

| Step | Name | Status | Output |
|------|------|--------|--------|
| 1 | CTP Doubling (A0) | Derived | Influence functional |
| 2 | Constitutive Equation (A1) | Derived | tau dz/dt + z = z_target[z] |
| 3 | Complex Relaxation (A2) | Derived (id.) | tau_I = hbar/2 |
| 4 | Gravitational Decoherence | Derived | Lambda_grav (0 params) |
| 5 | 3-Loop Anomaly | Derived | C_FINAL, R_anomaly = 1.15428 |
| 6 | Canonical tau | Derived | tau_0 = 41.9 Myr, S = 108 pi |
| 7 | Self-Referential FP | Derived | z = z_target[z] |
| 8 | Linearity (structural) | Structural | f(R) linear at 3-loop |
| 9 | Boundary Conditions | Structural | f(R) = 2 - R (unique) |
| 10 | Assembly | Structural | H_inf = (2-R)/(S x tau_0) |

10 steps: 7 computed from prior steps, 3 structural (constrained by symmetry and boundary conditions rather than explicit calculation). The structural steps narrow the formula to a unique form but do not constitute a conventional derivation from a Lagrangian. A full non-perturbative CTP calculation would elevate the structural steps to computed ones.

**R disambiguation:** R_anomaly = 1.15428 is the 3-loop anomaly ratio |C_Cosmo/C_Final|, used in the vacuum formula. R_particle (e.g., R = 1 um for the gold benchmark) is the object radius in the decoherence formula S(l/R). These are different quantities.

### 5.2 The Prediction

    H_inf = (2 - 1.15428) / (108 pi x 1.322 x 10^15 s) = 1.885 x 10^-18 Hz     (4)

This is an absolute prediction, independent of H_0.

| H_0 [km/s/Mpc] | Implied Omega_Lambda | vs Planck 0.6889 |
|-----------------|---------------------|-----------------|
| 67.4 (Planck) | 0.745 | +8.1% |
| 69.9 | 0.693 | +0.6% |
| 70.0 | 0.691 | +0.2% |
| 73.0 (SH0ES) | 0.635 | -7.8% |

GRUT predicts H_inf, not Omega_Lambda. The Hubble tension determines which Omega_Lambda we observe. The accuracy ranges from 0.2% (H_0 = 70) to 8.1% (Planck H_0 = 67.4) across the tension range. GRUT does not resolve the Hubble tension.

### 5.3 Why (2-R)?

Linearity: The 3-loop anomaly is a single insertion. Higher powers require 6-loop, 9-loop. At 3-loop: f(R) is forced linear.

Boundaries: f(1) = 1 (CTP paths identical, max rate). f(2) = 0 (paths cancel, destructive interference). With linearity: f(R) = 2 - R. Unique.

Verification: 10 candidate functions tested. Linear: 0.7% error. Next-best (tanh): 6.2%.

### 5.4 The Self-Referential Threshold

The self-referential fraction f_self = Omega_Lambda/(Omega_m + Omega_Lambda) crosses 0.5 at z ~ 0.33 (matter-Lambda equality). The deceleration-to-acceleration transition (q = 0) occurs at z ~ 0.67 in LCDM. These are different epochs. GRUT's threshold crossing corresponds to the equality epoch.

The non-perturbative discrete map with exact retarded memory kernel produces three-phase expansion (radiation, matter, acceleration) with all parameters derived from first principles. Zero fitting. Robustness: 100%.

---

## 6. The Bridge

The same z = z_target[z], from the same CTP action, determines:

- **40 Hz** (neural): Diosi kernel at tree level
- **H_inf = 1.885 x 10^-18 Hz** (vacuum): anomaly structure at 3-loop

Scale ratio: 10^{-19.3}. Both from R_anomaly, S, tau_0.

---

## 7. The Remaining Sectors

### 7.1 QCD (Mapped)

Confinement as z = z_target[z] for color fields. Self-referential fraction f_self crosses 0.5 at 0.81 GeV (alpha_s = 0.5). SU(3) algebra exact to 10^-16.

### 7.2 Flavor (Mapped)

Mass hierarchy as eigenvalue spectrum. Koide formula K = 0.666632 for leptons (2/3 to 0.005%). CKM near-diagonal, PMNS large-mixing.

### 7.3 Neutrinos (Signature) / Baryogenesis (Signature)

Neutrinos: near-zero fixed point. Baryogenesis: 3/3 Sakharov conditions structural.

### 7.4 Dark Matter (Computed, toy)

Solitonic DM from double-well fixed-point landscape. BPS exact. Mass 10^6-10^13 GeV (superheavy). Self-interaction: at superheavy masses with femtometer-scale soliton radii, the geometric cross-section sigma ~ pi R_soliton^2 is extremely small relative to the mass, giving sigma/m << 1 cm^2/g. This is consistent with Bullet Cluster bounds but a full microphysical cross-section calculation (beyond the geometric estimate) has not been performed.

### 7.5 Quantum Gravity (Partial, 2/5)

Minisuperspace fluctuation spectrum: Jacobian J = Omega_Lambda = 0.691. UV completion: 1/omega^2 damping (closure condition #2 MET). Classical GR: |H| = 1.000000 at LIGO frequencies (condition #5 MET). Stable fixed point. Full tensor-sector computation remains open.

---

## 8. Honest Status

| Claim | Status |
|-------|--------|
| QM recovery (Schrodinger, Born, Lindblad) | VERIFIED (12/12 tests) |
| Electroweak structure (charges, masses) | VERIFIED (13/13 tests) |
| USL decoherence rate (zero parameters) | VERIFIED (14/14 tests, untested experimentally) |
| Lindblad master equation | DOCUMENTED (verified, max error 1.4e-6) |
| Heating/radiation constraints | NOT VIOLATED (P = 4.7e-68 W) |
| Self-referential fixed point mathematics | COMPUTED (numerical verification) |
| Two routes to 40 Hz (39.9 + 41.7) | DEMONSTRATED |
| Three-phase cosmology from threshold | DEMONSTRATED (100% robust) |
| H_inf = 1.885e-18 Hz from (2-R)/(S tau_0) | STRUCTURAL ANSATZ (constrained, not derived from Lagrangian) |
| Omega_Lambda: 0.2% at H0=70, 8.1% at Planck | H_0 DEPENDENT (not an independent prediction of Omega_Lambda) |
| 10-step derivation chain | 7 COMPUTED + 3 STRUCTURAL |
| Bridge: 40 Hz + H_inf | COMPUTED |
| QCD confinement mapping | MAPPED (0.81 GeV) |
| Koide formula as eigenvalue constraint | MAPPED (0.005%) |
| Unification approach | MAPPED (f_self = 0.93) |
| Neutrino masses from near-zero FP | EXPECTED SIGNATURE |
| Baryogenesis from asymmetric FP | EXPECTED SIGNATURE |
| Singularity regularization | STRUCTURAL POSITIVE |
| Solitonic DM from FP landscape | COMPUTED (BPS exact, 10^6-10^13 GeV) |
| QG: UV completion + classical GR | MET (2/5, minisuperspace) |
| Consciousness (subjective experience) | NONCLAIM |
| Thermal wall "bypass" | CONSTITUTIVE CHANNEL ONLY (Lindblad decoherence still operates) |

---

## 9. What Is Not Claimed

- Mechanism for subjective experience
- Dark matter at WIMP mass scale (computed solitons are superheavy)
- Quantum gravity completion beyond minisuperspace (0/3 on graviton, backreaction, BH info)
- Observable GW/QNM effects (computed, dead at ~10^-39 rad)
- Dark energy as a substance (Lambda is the vacuum fixed-point value)
- Exact fermion masses from first principles
- Resolution of the Hubble tension
- "Decoherence is undefined" in the Lindblad sense (only the constitutive driving term is zero at the fixed point)

---

## 10. How To Kill It

1. No decoherence plateau in mesoscopic superposition experiments at ultra-high vacuum
2. H_inf shifts outside observed range as R_anomaly, S, tau_0 are better measured
3. No gamma-tubulin mass correlation across species
4. QCD self-referential fraction doesn't match confinement scale
5. Any of 7 Sector 13 kill conditions
6. Heating/radiation bounds exceed the computed D_p (currently safe by >60 orders)

The decoherence plateau is the primary falsification target. Its failure would remove the quantitative grounding for the cosmological formula (which uses tau_0, R_anomaly, and S derived from the same decoherence sector) and weaken the 40 Hz coincidence (which uses Lambda_grav). However, the structural mappings in other sectors (QCD confinement threshold, Koide formula, unification approach) are independently testable and do not logically depend on the plateau measurement.

The plateau measurement requires a mesoscopic object in spatial superposition at P < 10^-10 Pa. Current experiments reach ~10^5 amu; the gold benchmark (R = 500 nm, m ~ 10 pg) requires ~10^10 amu. This is not "within reach" of current technology but is a target for next-generation levitated optomechanics experiments.

---

## 11. Software

183 tests, all passing. 13 sectors (0 fully open). 70+ modules, 23+ API endpoints, 110+ GRUTipedia topics, 9 applications, 7 Zenodo briefs.

Code: github.com/ryangrvr/GRUT-RAI-v1.0

---

## 12. Conclusion

The constitutive equation tau dz/dt + z = z_target[z] produces a qualitative transition at every scale: the shift from external-target dynamics to the self-referential fixed point z = z_target[z]. The target functional is specified from the CTP influence functional in each sector. This transition:

- Recovers quantum mechanics (ground state as fixed point)
- Predicts gravitational decoherence with zero free parameters
- Produces cosmic acceleration (vacuum fixed point, H_inf = 1.885e-18 Hz)
- Maps onto confinement, flavor hierarchy, neutrino masses, baryogenesis, unification
- Generates stable solitonic dark matter (BPS exact, topologically protected)
- Provides UV completion and classical GR recovery for quantum gravity (2/5 closures)

The self-referential bypass of the thermal wall and the bridge between 40 Hz and H_inf are structural results from the same CTP action. Their interpretation as "consciousness" and "cosmic acceleration sharing a mechanism" is striking but should be evaluated on the mathematics, not the language.

13 sectors. 183 tests. One equation. One fixed point.

---

*D. Ryan Grover, April 2026. Grand Responsive Universe Theory v5 (Revised).*

*All computations reproducible via the grut_solver package. Candidate results separated from demonstrated results throughout. 70-75% of a complete Theory of Everything — honest about the 25-30% it hasn't closed.*
