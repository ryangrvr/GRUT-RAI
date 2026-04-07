# GRUT III Book A — Stage A1: Minimal CTP Backbone Freeze

---

## A1 Action Status Ledger

Each term or structural element of the CTP backbone is classified below. Columns:

- **Term / Structure**: the object under audit
- **Role**: what it does in the theory
- **Status**: derived / assumed / inferred / open / falsified / retracted
- **Evidence basis**: where the status claim comes from
- **Regime scope**: where it is valid (with explicit boundaries)
- **Failure mode if removed**: what breaks if this element is dropped
- **Confidence**: 0 (no basis) to 1 (theorem)

---

### L1: CTP contour doubling

| Field | Value |
|---|---|
| **Term** | Fields doubled on the Schwinger-Keldysh closed-time-path contour: Phi → (Phi_+, Phi_-) and g → (g_+, g_-), equivalently (Phi_r, Phi_a) and (g_r, g_a) in Keldysh rotation. |
| **Role** | Framework. Enables variational derivation of dissipative equations of motion from an action principle. Required by Bauer's theorem (1931): no single-variable real Lagrangian produces first-order dissipative dynamics. |
| **Status** | **DERIVED** (necessity). The CTP structure is necessary for any action-based formulation of the constitutive sector. Sufficiency demonstrated by construction (Iota-Prime). |
| **Evidence** | Bauer (1931) — theorem. Galley (2013) — explicit construction. Iota-Prime — GRUT-specific verification. |
| **Regime** | All regimes where the constitutive field dissipates. Not regime-restricted. |
| **Failure mode** | Without CTP doubling, no action principle for the constitutive law exists. The entire variational backbone collapses. One must revert to postulating the EOM directly. |
| **Confidence** | **1.0** |

---

### L2: Sector 1 — Constitutive dissipation term

| Field | Value |
|---|---|
| **Term** | -[tau ∂_t Phi_r + Phi_r - X(g_r)] Phi_a, appearing as a real term linear in Phi_a in the CTP action. |
| **Role** | Generates the classical constitutive equation of motion tau dPhi_r/dt + Phi_r = X upon variation w.r.t. Phi_a in the classical limit (Phi_a → 0). |
| **Status** | **DERIVED** (exact within stated regime). |
| **Evidence** | Iota-Prime II. Variation performed explicitly. Forward semigroup S(t) = exp(-t/tau) and unique attractor Phi* = X follow from the linear structure. Numerically verified. |
| **Regime** | Markovian (bath correlation time << tau). Overdamped (no inertial/kinetic term for Phi). Flat or slowly-varying background (X approximately constant or slowly varying on timescale tau). Linear Phi dynamics (no cubic saturation, no delay). |
| **Failure mode** | Without this term, no constitutive relaxation. The scalar field Phi has no dissipative dynamics. The entire GRUT constitutive framework is lost. |
| **Confidence** | **0.95** (exact derivation, but regime conditions are assumed not derived — see L8, L9 below). |

---

### L3: Sector 2 — Noise term

| Field | Value |
|---|---|
| **Term** | +iD Phi_a^2, appearing as an imaginary, positive-definite term quadratic in Phi_a. |
| **Role** | Generates Gaussian white noise xi(t) in the stochastic constitutive equation. Ensures positivity of the density matrix (Im S_eff ≥ 0). Linked to dissipation via the fluctuation-dissipation theorem: D = k_B T × tau (Ohmic, high-T limit). |
| **Status** | **DERIVED** (exact within stated regime). |
| **Evidence** | Iota-Prime II, V. Langevin simulation verifies FDT to 1.2% (statistical). Standard CTP construction (Calzetta & Hu 1994). |
| **Regime** | Same as L2, plus: thermal equilibrium, Ohmic spectral density, high-temperature limit k_B T >> hbar/tau. |
| **Failure mode** | Without this term, the CTP action violates the positivity condition (Im S_eff ≥ 0 required for probability conservation). The theory produces negative probabilities. Also: the constitutive field has no equilibrium fluctuations, breaking thermodynamic consistency. |
| **Confidence** | **0.90** (derivation exact; confidence reduced because the bath identity and the temperature T are NOT specified within the minimal action — see Conflict C6 from Book A). |

**Conflict note (CN-L3):** The noise coefficient D = k_B T tau requires specifying T and the bath. In the GRUT-II experimental roadmap (Delta-Prime onward), T = 4 K and the noise source is gas collisions (environmental, not gravitational). This means Sector 2 noise is de facto environmental, not sourced by g_a. This is in tension with claim S4 ("no additional bath beyond g, Phi needed"). If the environmental bath is required for Sector 2, the minimal variable set is (g_r, g_a, Phi_r, Phi_a) PLUS an environmental sector. The tension is flagged, not resolved.

---

### L4: Sector 3 — Gravitational dephasing (USL)

| Field | Value |
|---|---|
| **Term** | S_IF^{grav}: the influence functional contribution from integrating out the Newtonian gravitational field on the CTP contour. Produces a real phase: Delta_E × t / hbar, where Delta_E is the Diosi self-energy difference for the superposed mass distribution. |
| **Role** | Generates gravitational decoherence of spatial superpositions at rate Lambda = Delta_E / hbar. In the point-mass limit (l > 2R): Lambda = Gm^2/(hbar l). |
| **Status** | **DERIVED** (exact in the Newtonian limit for the point-mass case; exact numerical for the extended-body case). |
| **Evidence** | Iota-Prime IV (point-mass derivation). Kappa-Prime (extended-body Diosi integral, numerical). Standard result equivalent to Diosi (1987) and Penrose (1996). GRUT contribution: placement within the three-sector CTP framework. |
| **Regime** | Newtonian gravity (v << c, weak field, l << c^2/(Gm)). Instantaneous potential (no gravitational retardation). Point-mass regime requires l > 2R; extended-body regime uses the full 6D Diosi integral. |
| **Failure mode** | Without this term, no gravitational decoherence prediction. The USL is lost. The quantum sector has no testable content. The three-sector structure collapses to two sectors (dissipation + noise only). |
| **Confidence** | **0.85** (the Newtonian self-energy integral is exact. Confidence reduced because: (a) the passage from a pure oscillating phase exp(-i Delta_E t/hbar) to irreversible decoherence requires an additional step — averaging, environment-induced dephasing, or decoherence of the gravitational field itself — that is standard in the DP literature but was not explicitly derived within the GRUT CTP action; (b) the "no FDT partner" claim is tree-level only — see L5). |

**Conflict note (CN-L4):** The mechanism by which a purely real oscillating phase produces IRREVERSIBLE decoherence deserves scrutiny. A coherent oscillation exp(-i omega t) does not by itself decohere — it produces a phase that can in principle be reversed. Decoherence requires either: (i) coupling to many modes that produce effective phase randomization, or (ii) an external tracing operation (the environment "observes" the phase). In the Diosi-Penrose framework, the argument is that the gravitational field itself decoheres the superposition because gravity cannot maintain superpositions (the Penrose argument from the absence of a well-defined time-translation operator for superposed geometries). In the CTP framework, this role is played by the tracing out of g_a, which produces the influence functional. The irreversibility is thus tied to the CHOICE of tracing out the gravitational sector. This is a standard operation in the influence-functional formalism, but it is an ASSUMPTION about what constitutes the "system" vs the "environment," not a derived consequence of the action.

---

### L5: FDT structure and Sector 3 independence

| Field | Value |
|---|---|
| **Term** | The fluctuation-dissipation relation D = k_B T tau linking Sectors 1 and 2. The independence of Sector 3 (USL) from this relation. |
| **Role** | Ensures thermodynamic consistency of the constitutive sector (Sectors 1-2). Identifies the USL as a structurally distinct mechanism (dephasing, not diffusion). Explains the Alpha-Prime separation of USL and Level-1 as separate predictions. |
| **Status** | Sectors 1-2 FDT: **DERIVED**. Sector 3 independence: **INFERRED** (tree-level only). |
| **Evidence** | Iota-Prime V. Langevin simulation FDT check. The independence of Sector 3 follows from the tree-level truncation: at tree level, the gravitational self-energy is deterministic and has no noise partner. |
| **Regime** | FDT: Ohmic, high-T, Markovian, thermal equilibrium. Sector 3 independence: tree-level Newtonian gravity only. At loop level, gravitational fluctuations would introduce a noise partner for the USL, and the independence would be partially broken. |
| **Failure mode** | If FDT fails: thermodynamic inconsistency, negative-entropy production possible. If Sector 3 independence fails (i.e., at loop level): the USL acquires a noise partner, the three-sector structure merges into a two-sector structure (dissipation + noise, with both environmental and gravitational contributions to each), and the Alpha-Prime separation is softened. |
| **Confidence** | FDT: **0.95**. Sector 3 independence: **0.70** (tree-level only; loop corrections expected but unknown in magnitude). |

---

### L6: Source coupling X(g_r)

| Field | Value |
|---|---|
| **Term** | The source function X(g_r) that determines the equilibrium value of Phi for a given background geometry. |
| **Role** | Couples the constitutive sector to gravity. Determines what Phi relaxes TOWARD. Without X, the constitutive law tau dPhi_r/dt + Phi_r = 0 has no interesting dynamics (Phi → 0 always). |
| **Status** | **ASSUMED** (functional form not specified). |
| **Evidence** | Inherited from GRUT-I where X was defined operationally as the curvature-determined equilibrium. In the CTP action (Iota-Prime), X(g_r) appears as an input, not a derived quantity. No specific functional form X[g_{mu nu}] has been written. |
| **Regime** | All regimes where Phi couples to gravity. The functional form determines the regime of validity of the coupling. |
| **Failure mode** | Without X: no Phi-gravity coupling, no physical content to the constitutive sector beyond free relaxation. With an incorrect X: the constitutive law relaxes to the wrong target, producing wrong predictions near gravitating sources. |
| **Confidence** | **0.30** (the existence of X is structurally required; its functional form is entirely unspecified). |

**Conflict note (CN-L6):** This is the single most underspecified element of the minimal backbone. Every other term has a known form; X does not. The choice of X determines: (a) the near-horizon behavior of Phi, (b) the Level-1 formula 1/tau_local = 1/tau_0 + 1/t_dyn, (c) the strong-field phenomenology. Without an explicit X, the theory is a framework, not a complete EFT.

---

### L7: Gravitational CTP sector

| Field | Value |
|---|---|
| **Term** | The Einstein-Hilbert action doubled on the CTP contour: S_EH[g_+] - S_EH[g_-], or equivalently in Keldysh basis: the gravitational (g_r, g_a) action. |
| **Role** | Provides the dynamical gravitational sector. At tree level: generates the Newtonian potential that produces the USL. At loop level: would provide the gravitational noise kernel. |
| **Status** | **ASSUMED** (not explicitly written in GRUT). |
| **Evidence** | Standard CTP gravity exists in the literature (Calzetta & Hu 1994, Salcedo et al. 2025). GRUT-II bypassed the explicit gravitational CTP action by working directly in the Newtonian limit for the USL. The full gravitational CTP action within the GRUT coupling structure has NOT been written. |
| **Regime** | The Newtonian limit (used for USL) is controlled. The full action is needed for strong-field extensions, backreaction, and loop-level noise. |
| **Failure mode** | Without an explicit gravitational CTP action: Gate 2 (coupled consistency) cannot be passed. Backreaction of Phi on g is uncontrolled. The gravitational noise kernel (needed for tau determination) cannot be computed. |
| **Confidence** | **0.50** (the Newtonian limit is standard and correct; the full coupled action is assumed to exist but has not been constructed within GRUT-specific coupling). |

---

### L8: Overdamped limit

| Field | Value |
|---|---|
| **Term** | The absence of a kinetic term (1/2)(∂_t Phi)^2 in the CTP action. The constitutive equation is first-order, not second-order. |
| **Role** | Ensures the constitutive dynamics is purely relaxational (no propagating wave modes for Phi). Equivalent to the strong-damping limit of the Caldeira-Leggett model. |
| **Status** | **ASSUMED** (not derived from a scale comparison). |
| **Evidence** | Theta-Prime/Iota-Prime assume the overdamped regime without computing the Phi inertial mass M or comparing M omega_0 to eta. The assumption is physically plausible for a constitutive field that represents slow equilibration toward a geometric target, but it is not checked. |
| **Regime** | Valid when M omega_0 << eta, i.e., when the inertial timescale (sqrt(M/k)) is much shorter than the dissipative timescale (tau = eta/k). |
| **Failure mode** | If the overdamped limit fails, Phi acquires propagating wave modes. The EOM becomes a damped wave equation, not a relaxation equation. The constitutive field could oscillate rather than relax, and the unique-attractor structure of GRUT-I is modified. |
| **Confidence** | **0.60** (physically plausible but not derived; could be checked once M and eta are known). |

---

### L9: Markovian limit

| Field | Value |
|---|---|
| **Term** | The assumption that the bath correlation time tau_bath << tau (the constitutive relaxation time), so that the retarded kernel collapses to a delta function and the constitutive equation is local in time. |
| **Role** | Justifies the simple first-order ODE form of the constitutive law. Without it, the EOM is an integro-differential equation with memory. |
| **Status** | **ASSUMED** (plausible but the bath spectral density J(omega) is not specified). |
| **Evidence** | Iota-Prime III verifies the Markovian limit for a Drude spectral density with omega_D >> 1/tau. But the actual spectral density of the GRUT environment is unknown. |
| **Regime** | Valid when tau_bath << tau. Fails in the non-Markovian regime (omega_D ~ 1/tau). |
| **Failure mode** | If Markovian limit fails, the constitutive law acquires memory corrections. The simple exponential semigroup is modified. The kernel structure from GRUT-I Kappa becomes the leading correction. |
| **Confidence** | **0.65** (plausible for a gravitational/thermal bath, but J(omega) unknown). |

---

### L10: Point-mass USL regime condition

| Field | Value |
|---|---|
| **Term** | The condition l > 2R for the point-mass formula Lambda = Gm^2/(hbar l) to apply. |
| **Role** | Defines the boundary of validity for the simple USL formula. Below this, the extended-body Diosi integral must be used. |
| **Status** | **DERIVED** (exact for uniform-density spheres). |
| **Evidence** | Kappa-Prime. Numerical integration of the Diosi 6D integral confirms (l/R)^3 suppression with C ≈ 0.5. |
| **Regime** | Geometric: applies to any uniform-density spherical body. Non-spherical bodies have different crossover conditions. |
| **Failure mode** | If this condition is ignored: the point-mass USL overestimates the decoherence rate catastrophically (factor 44,000 at l/R = 0.036, as discovered in Kappa-Prime). |
| **Confidence** | **0.98** (numerically computed, crosschecked against known analytical limits). |

---

## A) Minimal Backbone Proposal

### The smallest coherent term set

The minimal CTP backbone that retains constitutive relaxation, memory placement, and quantum-sector (USL) placement consists of **five irreducible elements:**

| # | Element | Why irreducible |
|---|---------|----------------|
| **L1** | CTP contour doubling | Required by Bauer's theorem. Without it, no action for dissipation. |
| **L2** | Sector 1 (constitutive dissipation) | Without it, no relaxation equation. |
| **L3** | Sector 2 (noise) | Without it, CTP positivity violated. Thermodynamic inconsistency. |
| **L4** | Sector 3 (gravitational dephasing) | Without it, no quantum prediction. USL lost. |
| **L6** | Source coupling X(g_r) | Without it, Phi relaxes to zero, not to a geometry-dependent equilibrium. |

### What is excluded and why

| Excluded element | Why excluded from MINIMAL backbone |
|---|---|
| **L7** (full gravitational CTP action) | Not needed for the Newtonian-limit USL. Needed for strong-field extension and loop-level computation. Excluded from MINIMAL; required for EXTENDED backbone. |
| **L8** (overdamped limit justification) | An assumption about the regime, not a term in the action. It constrains the validity of L2 but is not itself a structural element. |
| **L9** (Markovian limit justification) | Same as L8: a regime assumption, not a term. |
| **L10** (point-mass regime condition) | A validity boundary on L4, not a separate term. Encoded in the Diosi integral. |

### Minimal backbone = {L1, L2, L3, L4, L6}

The action is:

```
iS_min[Phi_r, Phi_a] = i ∫ dt { -[tau ∂_t Phi_r + Phi_r - X] Phi_a + iD Phi_a^2 }
                      + S_IF^{grav,Newtonian}[superposition branches]
```

with five free inputs: tau, D (or equivalently T), X(g_r), the body mass m, and the body geometry (radius R, density rho).

---

## B) Hidden-Assumption Audit

Assumptions that were previously implicit in GRUT-II, now made explicit:

| # | Previously implicit assumption | Now explicit as | Status |
|---|-------------------------------|----------------|:------:|
| **H1** | The constitutive field Phi has no inertial mass (no kinetic term). | L8: overdamped limit. Requires M omega_0 << eta. Not checked. | **ASSUMED** |
| **H2** | The bath producing dissipation is memoryless on the timescale tau. | L9: Markovian limit. Requires tau_bath << tau. Not checked. | **ASSUMED** |
| **H3** | The noise in Sector 2 comes from the same bath as the dissipation. | FDT relation D = k_B T tau. Requires a single-bath thermal equilibrium. | **ASSUMED** |
| **H4** | The gravitational self-energy oscillation produces irreversible decoherence. | CN-L4: requires tracing out g_a or equivalent environment-induced dephasing. | **ASSUMED** (standard in DP literature but not derived within GRUT) |
| **H5** | The temperature T in the FDT is the environmental temperature. | CN-L3: this means Sector 2 is sourced by an environmental bath, not gravitational. If so, S4 ("no extra bath") is wrong. | **ASSUMED** (in tension with S4) |
| **H6** | X(g_r) exists and is a well-defined functional of the metric. | CN-L6: functional form not specified. | **ASSUMED** |
| **H7** | The CTP action is evaluated on a fixed background metric (no backreaction of Phi on g). | Iota-Prime treats g_r as a background; g_a is integrated out for the USL but the backreaction equation (variation w.r.t. g_a giving the semiclassical Einstein equation) is not checked. | **ASSUMED** |
| **H8** | The Keldysh rotation (r, a basis) introduces no physics. | Standard. But: the physical limit Phi_a → 0 is a CHOICE of saddle point, not a derived consequence. At strong quantum fluctuations (large Phi_a), the saddle-point approximation fails. | **ASSUMED** (valid in the classical regime) |
| **H9** | The bath spectral density J(omega) is Ohmic. | Required for D = k_B T tau (high-T Ohmic FDT). Non-Ohmic baths give different FDT relations. | **ASSUMED** |

All nine hidden assumptions are now explicit. Each carries a regime tag (from the Ledger) and a confidence score (from the L-entries above).

---

## C) Hard Gates for A1

### Gate A1-G1: All core terms classified

**Status: PASS.**

All ten structural elements (L1-L10) are classified with status, evidence, regime, failure mode, and confidence. No unclassified terms remain.

### Gate A1-G2: No hidden unclassified assumptions

**Status: PASS.**

Nine previously implicit assumptions (H1-H9) have been identified and made explicit. Each is tagged. No further hidden assumptions have been detected at this stage.

**Caveat:** This does not guarantee zero remaining hidden assumptions. It means: a systematic pass through every term and claim in the Iota-Prime action has been performed, and all assumptions found have been surfaced. A second-pass audit (e.g., by an independent reviewer) could surface additional ones.

### Gate A1-G3: Regime tags attached to every surviving claim

**Status: PASS.**

Every L-entry and every claim in the Book A claim ledger carries explicit regime tags:
- Scale (Newtonian vs strong-field)
- Curvature (weak vs strong)
- Timescale (Markovian vs non-Markovian)
- Coupling (linear vs nonlinear)
- UV/IR (point-mass vs extended-body, l > 2R vs l < 2R)
- Quantum/classical (Phi_a → 0 vs large Phi_a)

---

## D) Decision

**Decision: FREEZE (conditional).**

**Rationale:**

The minimal CTP backbone {L1, L2, L3, L4, L6} is coherent, classified, and regime-tagged. All three A1 gates pass. The backbone is frozen at this level.

**Conditions on the freeze:**

1. The freeze applies ONLY within the controlled domain: Newtonian, Markovian, overdamped, linear Phi, flat/slowly-varying background, l > 2R for point-mass USL, Ohmic bath in thermal equilibrium.

2. The following elements are NOT frozen and remain open for GRUT-III resolution:
   - L6 (X functional form) — must be specified (Book A Action 1)
   - L7 (full gravitational CTP action) — must be constructed (Book A Action 2)
   - The bath identity question (is Sector 2 noise gravitational or environmental?) — must be computed (Book A Action 3)
   - The overdamped and Markovian limits — must be checked (Book A Action 4)

3. No claim of full covariance. The backbone is explicitly non-covariant (Newtonian limit, no retardation, no post-Newtonian corrections).

4. No claim of universal validity. The backbone is an EFT with a defined domain of validity and seven identified unsafe zones (U1-U7 from Book A Section 5).

5. The four retracted claims (V1-V4) remain retracted. The corrected operating point (196 fg / 474 nm / USL/gas = 2.9) from Mu-Prime stands as the current best hardware-audited target.

**Next stage:** A2 — Source Coupling Specification: write X[g_{mu nu}] explicitly and test against Level-1 near-horizon behavior.

---

*GRUT III Book A Stage A1 complete. Gates: A1-G1 PASS, A1-G2 PASS, A1-G3 PASS. Decision: FREEZE (conditional). Backbone: {L1, L2, L3, L4, L6} = CTP doubling + constitutive dissipation + noise + gravitational dephasing + source coupling. Five irreducible elements. Nine hidden assumptions now explicit. Ten structural elements classified. Confidence range: 0.30 (L6, X unspecified) to 1.0 (L1, Bauer's theorem). Four open issues handed to subsequent A-stages.*
