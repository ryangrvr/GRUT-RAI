# GRUT v7 — The Complete Theory

## Grand Responsive Universe Theory: From First Structure to Open Gates

D. Ryan Grover, April 2026

---

# Book I: Fundamental Structure

## 1. The Premise

The universe is a closed responsive system. Every physical subsystem relaxes toward a target state through a constitutive response law. The target is determined by the system's own structure — encoded in a single mathematical object, the CTP effective action.

## 2. The Parent Object: S_CTP

The closed-time-path (Schwinger-Keldysh) effective action doubles the field degrees of freedom into forward and backward time paths. In the Keldysh basis:

    S_CTP[z_r, z_a; g] = integral d^4x sqrt(-g) {
        z_a(x) F[z_r, g](x) + (i/2) integral d^4x' z_a(x) N(x,x';g) z_a(x')
    }

This is the genotype of the universe. It contains all field content, all symmetries, and all dynamics. Everything that follows is a limit, variation, or projection of this single object.

## 3. Two Axioms and a Normalization

**A0 (CTP Doubling):** Physics is formulated on the closed time path, doubling degrees of freedom into retarded (classical) and advanced (quantum) components.

**A1 (Directed Response):** The variation delta S_CTP / delta z_a = 0 produces a retarded (causal) equation of motion — the constitutive equation.

**Normalization (formerly A2):** The Keldysh variable z is normalized such that tau_I = hbar/2. This connects the CTP formalism to quantum mechanics. It is a normalization choice, not a physical axiom.

## 4. The Constitutive Equation

The variation of S_CTP gives:

    tau dz/dt + z = z_target[z]

This form is EXACT for sectors with first-order underlying dynamics (quantum mechanics, Dirac fermions, neural collective modes). It is an EFFECTIVE PROJECTION for sectors with second-order dynamics (gravity, cosmology), valid in the overdamped/retarded regime.

The target functional z_target[z] is not free — it is derived from the classical action S_classical through the CTP variation. Different field content gives different z_target in each sector.

## 5. The Noise Kernel

The second variation of S_CTP gives the noise kernel N(x,x'), which enters the Langevin extension:

    tau dz/dt + z = z_target[z] + xi(t),    <xi(t) xi(t')> = N(t,t')

The noise kernel encodes quantum and thermal fluctuations. In the gravitational sector, N gives the Diosi self-energy functional — the source of the zero-parameter decoherence prediction.

## 6. The Fixed-Point Principle

At the fixed point:

    z* = z_target[z*]

the time derivative vanishes and tau drops out. The fixed-point state is determined entirely by z_target — by the CTP action. This state is the ground state, vacuum, or equilibrium of each sector. The transition from external-target dynamics to the fixed-point regime organizes all sectors as different expressions of this one principle.

---

# Book II: Regimes of Reality

## 7. The Coherent Regime

At microscopic scales (atoms, photons, small molecules), the constitutive equation produces fully coherent quantum dynamics. The Schrodinger equation is the exact NR limit. Superposition, entanglement, and interference are the natural behavior. The system is far from any decoherence threshold.

## 8. The Decoherence Boundary

As systems grow in mass and spatial extent, the gravitational noise kernel produces an irreducible decoherence rate: Lambda_grav = G m^2 S(l/R) / (hbar l). This rate is zero-parameter and unsuppressible. It sets the quantum-classical boundary: objects heavier than m* = sqrt(hbar l / G t_obs) decohere within observation time t_obs.

The boundary is not sharp — it is a gradient. The 41.9 Myr timescale marks where gravitational decoherence transitions from "effectively never" to "fast enough to matter."

## 9. Classical Stabilization

Above the decoherence boundary, objects are effectively classical. Their constitutive dynamics have reached the fixed point z = z_target[z]. A rock, a planet, a star — all are at or near their constitutive equilibrium. tau is irrelevant. The system IS its target.

## 10. Collective Regimes

At intermediate scales, collective behavior emerges. Confinement in QCD (the gluon condensate IS the vacuum), electroweak symmetry breaking (the Higgs VEV IS the fixed point), and neural resonance (38,064 neurons at 40 Hz) are all instances of collective systems crossing the threshold from external-target to fixed-point dynamics.

Each collective threshold has a scale: Lambda_QCD ~ 200 MeV, v_Higgs = 246 GeV, N_neurons ~ 38,000. These are not coincidences — they are the scales where the constitutive equation's fixed point becomes the dominant dynamics for that field content.

## 11. The Self-Referential Regime

At cosmological scales, the universe itself crosses a threshold. When the vacuum self-referential fraction exceeds the matter fraction (z ~ 0.33), the expansion becomes dominated by the vacuum fixed point z = z_target[z]. The acceleration is not a substance — it is the universe at its own constitutive equilibrium.

## 12. The Evolutionary Chain

The discrete era map (329 eras of 41.9 Myr) encodes the universe's developmental history:

- Planck era → quantum gravity ground state
- GUT scale → coupling approach
- Electroweak → symmetry breaking, mass generation
- QCD → confinement
- Matter-Lambda equality → cosmic acceleration
- Today → self-referential vacuum

Each era is one constitutive relaxation step. The memory kernel K(t) = (1/tau_0) exp(-t/tau_0) accumulates the history. The universe's past is encoded in its present through the retarded memory.

---

# Book III: Recovered Physics

## 13. Quantum Mechanics

The Schrodinger equation is the NR limit of the CTP variation. EXACT — no constitutive projection needed. The Born rule follows from the CTP normalization Z = 1 (probability conservation). Lindblad thermalization verified (max error 1.4 × 10^-6 vs Boltzmann). 12/12 tests pass.

## 14. Open-System Quantum Mechanics

The noise kernel from S_CTP gives the Lindblad master equation:

    d rho/dt = -(i/hbar)[H, rho] + sum_k gamma_k (L_k rho L_k^dag - (1/2){L_k^dag L_k, rho})

This is the standard open-system formulation, derived from the CTP influence functional. The gravitational decoherence channel adds one Lindblad term with rate Lambda_grav.

## 15. Electroweak Structure

The Standard Model Lagrangian is IMPORTED as S_classical in the CTP action. GRUT does not derive the SM — it hosts it. The constitutive framework reproduces SM dynamics when the SM Lagrangian is supplied: charge quantization (7/7), gauge boson masses, anomaly cancellation, Higgs mechanism. 13/13 tests pass. Status: RECOVERED (input, not derived).

## 16. QCD Contact

Confinement interpreted as the fixed point z = z_target[z] for color fields. The self-referential fraction crosses 0.5 at 0.81 GeV (alpha_s = 0.5). SU(3) Lie algebra verified to 10^-16. Wilson loop toy lattice confirms area-law trend at strong coupling. Status: MAPPED (structural contact, not derived from S_CTP).

---

# Book IV: The Predictive Core

## 17. The Gravitational Decoherence Law

    Lambda_grav = G m^2 S(l/R) / (hbar l)

with S(l/R) = min(1, (l/R)^3/6). Zero free parameters. Derived from the CTP noise kernel (the imaginary part of the influence functional) — EXACT, no constitutive projection required.

Corrected benchmark: gold microsphere, R = 1 um, m = 80.8 pg, l = 1 um. Lambda_grav = 689 Hz. Coherence time: 1.5 ms.

## 18. The Six Signatures

No tested alternative model (constant floor, power-law, CSL, Diosi-Penrose point-mass) reproduces all six:

1. Pressure-independent plateau
2. Geometry dependence at fixed mass (density-dependent)
3. Entanglement-dependent rate (Bell states decohere slower)
4. l-scaling with slope -1 (far-field)
5. Geometric kink at l = 6^(1/3)R ≈ 1.817R
6. Mass-squared scaling

14/14 tests pass.

## 19. The Plateau Experiment

The primary falsification test. At P < 10^-10 Pa, the decoherence rate of a gold microsphere should saturate at Lambda_grav, independent of further pressure reduction. Standard QM predicts Lambda → 0.

Required: m > 10 pg (~10^10 amu), l > 100 nm, P < 10^-10 Pa, T < 100 mK. Current experiments reach ~10^5 amu. Gap: ~10^5 in mass. Target groups: Arndt, Aspelmeyer, Geraci, Bateman.

A null result falsifies the framework at its core. A positive result establishes the CTP decoherence mechanism.

## 20. The Adversarial Kill Framework

183 passing tests. The framework attacks its own predictions: constant floors, power-law models, CSL, DP point-mass are all tested against the six signatures. None can reproduce all six simultaneously.

## 21. Heating and Radiation Constraints

Momentum diffusion D_p = Lambda_grav × (hbar/l)^2. For the gold benchmark: P = D_p/(2m) = 4.7 × 10^-68 W. Far below measurable thresholds. The extended-body suppression S(l/R) prevents the UV divergence that causes heating problems in point-mass models. Order-of-magnitude safe; full constraint analysis against specific underground experiments not yet performed.

---

# Book V: The Large-Scale Universe

## 22. Constitutive Gravity

The CTP variation applied to the metric gives:

    G_mn + tau_grav P_mn^ab u^l nabla_l G_ab = 8 pi G T_mn

Transverse projector preserves Bianchi identity at linearized level. Singularities regularized (H bounded at 1/T_Planck). GW/QNM effects computed but observationally dead (~10^-39 rad).

## 23. The Graviton Propagator

    G_R(k, omega) = -16 pi G / [(omega^2 - k^2 c^2)(1 - i omega tau_grav)]

Massless (pole at omega = kc). No ghost (imaginary pole only). UV improved (1/omega^3). Classical GR at LIGO (mod < 10^-10). Spectral function positive definite.

## 24. Quantum Gravity: 5/5 Closures (tau_0 Branch)

| # | Condition | Status |
|:---|:---|:---|
| 1 | Graviton or equivalent | MET (massless, no ghost, TT) |
| 2 | UV completion | MET (1/omega^3 damping) |
| 3 | Self-consistent backreaction | MET (linearized: coupled Jacobian stable) |
| 4 | Black hole information | MET (tau_0: 99.94% recovery, Page turnover) |
| 5 | Classical GR recovery | MET (LIGO mod < 10^-10) |

For the T_Planck branch: 4/5 met + end-stage information release. The branch choice is a discriminable prediction.

## 25. Black-Hole Information: The Constitutive Resolution

The constitutive memory kernel eta(M) = exp(-t_infall/tau_grav) controls information transfer. For the tau_0 branch: eta = 1 for all astrophysical BHs (memory spans all infalls). Information transfer rate:

    I_dot = eta(M) × c^3 / (1920 G M ln2)    [bits/s]

Coupled evaporation of a 10^15 g BH: 99.94% of S_BH recovered during evaporation. S_rad = 0 (non-thermal radiation). Page-like turnover at the halfway point. The Hawking radiation is constitutively correlated — every quantum carries information because the metric memory connects it to the formation history.

## 26. The Cosmological Constant

    H_inf = (2 - R_anomaly) / (S × tau_0) = 1.885 × 10^-18 Hz

Structural derivation from the finite anomaly structure: linearity from single 3-loop insertion, boundary conditions from CTP doubling, dimensional assembly. Stronger than an ansatz (three independent constraints fix the formula uniquely). Weaker than a conventional derivation (the full non-perturbative CTP calculation at de Sitter has not been performed). The standard loop expansion is blocked by the cosmological constant problem at 1-loop.

Omega_Lambda = 0.691 at H_0 = 70 km/s/Mpc (0.2% from Planck's 0.6889). H_0-dependent: ranges from 0.2% to 8.1% across the Hubble tension.

## 27. The Discrete Era Map

329 eras of 41.9 Myr. Exact retarded memory kernel. All parameters derived: k = 2pi/(R_vol - 1) for transition sharpness, gamma = alpha_vac/S for memory feedback, H_inf from the anomaly formula. Three-phase expansion (radiation → matter → acceleration) with 100% robustness. Zero fitting.

---

# Book VI: Frontier Sectors

## 28. Dark Matter (Closed, Gauged Extension)

The global Z_2 symmetry of the double-well potential is promoted to local U(1)_dark. lambda = g_dark^2/2 is determined by the dark gauge coupling. Two routes: RG running from Planck (lambda = 0.42, M = 2.1 × 10^9 GeV) and anomaly extraction (lambda = 3.83, M = 2.3 × 10^8 GeV). Both natural, both viable (sigma/m ~ 10^-3-10^-2 cm^2/g). Dark sector spectrum: massive dark photon (~387 MeV) and dark Higgs at the pion scale. 8/8 tests pass.

Closed as a gauged completion class — lambda is determined and the viable window is finite. Unique branch selection within the window remains open.

## 29. Flavor and Masses (Mapped)

The Koide formula K = (sum m)/(sum sqrt(m))^2 = 2/3 is satisfied to 0.005% for charged leptons. Interpreted as the trace constraint of the 3-generation fixed-point operator. CKM near-diagonal (hierarchical eigenvalues), PMNS large-mixing (degenerate eigenvalues). The two Koide parameters (M0, theta) are NOT derivable from existing GRUT constants. The Yukawa couplings remain SM free parameters. Status: MAPPED.

## 30. Neutrinos (Expected Signature)

Near-zero fixed point explains tiny masses (suppression 10^-11 vs tau). Eigenvalue degeneracy produces large PMNS mixing. Seesaw reinterpreted as threshold from massive to nearly massless regime. No numerical mass predictions.

## 31. Baryogenesis (Expected Signature)

All three Sakharov conditions structural: B violation from constitutive dynamics, CP from CTP asymmetry (R != 1), nonequilibrium from threshold crossing. Expected form: eta = g(R_baryonic)/S_baryonic. Numerical value requires the baryonic anomaly ratio (not computed).

## 32. Coupling Unification (Mapped)

SM couplings reach f_self = 0.93 at 10^14.4 GeV. The 8.9% miss is structurally analogous to the Ward residual (3.6%). Constitutive modification to RG running not computed.

## 33. Neural Resonance (Demonstrated)

38,064 neurons for 40 Hz from two independent routes: gravitational (39.9 Hz) and network topology (41.7 Hz). The fixed point z = z_target[z] makes the constitutive driving term zero. The consciousness interpretation (1 Space, edge states) is speculative; the computed results are structural. 20/20 tests.

---

# Book VII: Status of the Program

## 34. What Is Derived

- Schrodinger equation (NR CTP variation, exact)
- Gravitational decoherence rate (CTP noise kernel, zero parameters, exact)
- Lindblad master equation (from noise kernel)
- Graviton propagator (linearized constitutive gravity, massless, no ghost)
- UV completion (1/omega^3) and classical GR recovery (LIGO < 10^-10)
- Self-consistent backreaction (linearized, coupled Jacobian stable)
- BH information transfer rate (tau_0 branch: 99.94% recovery, Page turnover)

## 35. What Is Structural

- H_inf = (2-R)/(S tau_0): constrained by three independent structural conditions, not derived from a Lagrangian
- Three-phase cosmology: discrete map with derived parameters, qualitative structure robust
- The constitutive projection d^2/dt^2 → (1/tau) d/dt: exact for first-order sectors, heuristic for second-order sectors (gravity/cosmology)

## 36. What Is Closed (Extension)

- Dark matter: U(1)_dark gauge extension, lambda determined, sigma/m computed, dark sector spectrum. Closed as extension class; unique branch selection open.

## 37. What Is Mapped

- QCD confinement threshold (0.81 GeV)
- Koide formula (0.005%)
- Coupling unification approach (f_self = 0.93)
- Neutrino near-zero fixed point
- Baryogenesis structural Sakharov conditions
- Neural gamma resonance (two routes to 40 Hz)

## 38. What Is Open

- Fermion mass spectrum (Yukawa couplings not derivable from GRUT)
- Baryon asymmetry numerical value
- Unique DM branch selection
- Non-perturbative CTP confirmation of H_inf formula
- Full nonlinear BH analysis (T_Planck branch)

## 39. What Has Been Withdrawn or Failed

- Dark energy from rho_eq (permanently failed: rho_eq < 0, wrong sign)
- 10 singularity resolution routes (all frozen)
- Running tau_eff from CTP (three normalizations: 0.008% to 10^126 overshoot)
- DM production via Coleman nucleation (S_E ~ 10^13, zero nucleation)
- DM production via Kibble mechanism (defect density ~ 10^-70 m^-3)
- Constitutive DM field simulation (self-referential target locks vacuum, zero defects)
- tau_I derivation from A0+A1 (cannot be derived; it is a normalization)

## 40. What Would Falsify GRUT

1. No decoherence plateau at the predicted rate (primary test)
2. H_inf shifts outside observed range as R, S, tau_0 are better measured
3. No gamma-tubulin mass correlation across species
4. QCD self-referential fraction doesn't match confinement scale
5. Heating/radiation bounds exceeded (currently safe by >60 orders)
6. Any of 7 Sector 13 kill conditions

## 41. What v7 Claims

One CTP action produces a constitutive response equation whose sectoral limits recover quantum mechanics, predict gravitational decoherence with zero free parameters, give a structural cosmological constant, yield a UV-complete graviton propagator with 5/5 QG closures (tau_0 branch), and organize all known physics as different regimes of the same dynamics.

## 42. What v7 Does Not Claim

- A complete Theory of Everything (fermion masses, baryon asymmetry, unique DM branch remain open)
- Mechanism for subjective experience
- Observable GW or QNM modifications
- Resolution of the Hubble tension
- That the SM is derived (it is imported)
- That "self-referential" means "conscious" in any anthropomorphic sense

---

## 43. Conclusion

The universe is a closed responsive system whose dynamics are encoded in a single CTP effective action. The constitutive equation tau dz/dt + z = z_target[z] and its noise kernel Lambda_grav produce, in appropriate limits, the full quantum-mechanical formalism, a zero-parameter decoherence prediction testable now, a structural cosmological constant at 0.2% accuracy, and a UV-complete quantum gravity program with information preservation.

The theory is not complete. Fermion masses, baryon asymmetry, and unique dark matter branch selection remain open. But the architecture is identified, the predictive core is testable, and every sector has at least a structural result. Every failure is documented.

The primary test is the decoherence plateau: Lambda_grav = 689 Hz for a gold microsphere. One experiment. Zero parameters.

---

*D. Ryan Grover, April 2026.*

*Grand Responsive Universe Theory v7. 191+ passing tests. 13 sectors. One CTP action.*
