# GRUT v7 — Appendix N: Toward v8 — A Surgical Roadmap

## Transitioning from Coherent Framework to Falsifiable Physical Theory

*D. Ryan Grover, April 2026*

---

## N.0 — Purpose and Invitation

This appendix is not a v8 document. It is a roadmap — a structured
proposal for how GRUT should evolve from its current state (a coherent
CTP-based framework with computed predictions) into a falsifiable
physical theory with community-verified formalism.

**v8 will not be built alone.** This appendix opens the conversation
by defining the phases, decision points, and deliverables required.
Contributions, critiques, and collaboration are explicitly invited.

---

## N.1 — Hard Constraint (Anchor for v8)

Before any v8 work proceeds, one enforced rule:

> **If it cannot produce a measurable deviation from LCDM, GR, or
> standard QFT, it is not part of v8.**

This cuts abstraction drift. Every section of v8 must connect to a
number that can be compared against data. Philosophy and interpretation
are permitted only after the equations and predictions are established.

---

## N.2 — Where v7 Stands

### What v7 has achieved

| Achievement | Status | Evidence |
|:---|:---|:---|
| Internal consistency across 13 sectors | Verified | 22 foundation tests pass |
| Gravitational decoherence with 6 scaling laws | DERIVED (0 params) | Lambda_grav = G m^2 S(l/R) / (hbar l) |
| Cosmological constant | COMPUTED (1 param) | Omega_Lambda = 0.6904 vs Planck 0.6889 |
| Baryon asymmetry | COMPUTED (0 params) | eta_B = 6.57e-10 vs observed 6.1e-10 |
| Dark matter sector | CLOSED | Route 1 selected 5/5, m_A = 387.4 MeV |
| Koide identity | PROVEN | K = 2/3 exact, N = 3 unique |
| 9 computed experiments | COMPUTED | Decisive discriminators identified |

### What v7 lacks

| Gap | Severity | Why it matters |
|:---|:---|:---|
| No modified field equation | Critical | Cannot couple to existing GR/QFT toolchain |
| "Responsiveness" is conceptual | Critical | Must become a quantitative field or operator |
| Perturbation growth fails | Fundamental | Cannot do structure formation at first order |
| No direct confrontation with data | Significant | Predictions exist but have not been tested against datasets |
| Hierarchy problem unsolved | Fundamental | UV softening insufficient |

### The gap between v7 and a publishable theory

v7 is **post-Phase 0** (conceptual consistency, directional clarity) but
**pre-Phase 1** (mathematical formalization as a field theory). The
constitutive equation tau dz/dt + z = z_target[z] is well-defined and
computable, but it has not been cast in the language of modified gravity
or quantum field theory that would allow direct comparison with existing
frameworks.

---

## N.3 — Phase 1: Formalization Layer

### N.3.1 — Define the Core Operator

v7 implies three dynamical features: responsiveness, decoherence coupling,
and gravitational feedback. v8 must encode these in a single governing object.

**The GRUT Response Functional:**

    R[g, psi, phi] -> modified evolution

where:
- g_mu_nu: spacetime metric
- psi: quantum state (matter sector)
- phi: GRUT scalar field (encodes decoherence/response)

**Deliverable:** One equation modifying either Einstein's field equations
OR Schrodinger evolution. Not both initially.

### N.3.2 — Choose Entry Point

This is a critical decision that must be made early.

**Option A (recommended): Modify Einstein Field Equations**

    G_mu_nu + Phi_mu_nu(phi) = 8 pi G T_mu_nu

where Phi_mu_nu encodes the GRUT response through a scalar field phi
with stress-energy:

    T_mu_nu^(phi) = nabla_mu phi nabla_nu phi
                    - (1/2) g_mu_nu (nabla phi)^2
                    - g_mu_nu V(phi)

This provides a cleaner path to cosmology and decoherence simultaneously.
The constitutive equation governs phi's dynamics.

**Option B: Modify Schrodinger**

    i hbar d psi/dt = (H + H_GRUT) psi

This is harder to scale to cosmology and does not naturally produce
metric modifications. Not recommended as the primary entry point.

**Decision required:** v8 should commit to one entry point. Dual-track
formalization dilutes effort and delays falsifiable predictions.

### N.3.3 — Define "Responsiveness" Quantitatively

The GRUT field phi must have a concrete definition with units.

**Candidate definitions:**

1. phi = decoherence rate density (units: Hz/m^3)
2. phi proportional to divergence of information current: phi = nabla . I(x, t)
3. phi as a scalar condensate of the CTP noise kernel

**Minimal viable form:**

    phi(x) = integral d^3 x' G rho(x) rho(x') / (hbar |x - x'|)

This is the Diosi kernel integrated over the mass distribution —
directly connecting phi to the gravitational decoherence structure
already computed in v7.

**Deliverable:** Explicit definition of phi with units, field equation,
and boundary conditions.

---

## N.4 — Phase 2: Minimal Predictive Model

### N.4.1 — Reduce to a Toy Universe

Strip everything to the minimum:
- Homogeneous FLRW spacetime
- Single scalar GRUT term phi(t)
- Standard matter and radiation

**Modified Friedmann equation (explicit):**

    H^2 = (8 pi G / 3) [ rho + (1/2) phi_dot^2 + (1/2) m_phi^2 phi^2 ]

where:
- rho: standard matter + radiation energy density
- (1/2) phi_dot^2: kinetic energy of the GRUT field
- (1/2) m_phi^2 phi^2: potential energy V(phi) = (1/2) m_phi^2 phi^2
  (quadratic potential as the minimal viable form)

The GRUT field equation in FLRW:

    phi_ddot + 3 H phi_dot + m_phi^2 phi = beta D(t)

where D(t) is the decoherence source term and beta is the coupling constant.

### N.4.2 — The Decoherence Source

The source driving the GRUT field is the gravitational self-energy
(Diosi kernel):

    D(x) = integral d^3 x' G rho(x) rho(x') / (hbar |x - x'|)

This is the SAME kernel that produces Lambda_grav in v7. The v8
formalization promotes it from a decoherence rate calculator to a
field source term. No new physics is introduced — the existing
computation is repackaged in field-theoretic language.

### N.4.3 — Identify ONE Observable Signature

v8 needs exactly one prediction to move forward. Strong candidates:

**A. Decoherence-Gravitational Coupling (strongest)**
- Measurable deviation in matter-wave interferometry near varying
  mass distributions
- v7 already predicts Lambda_grav = G m^2 S(l/R) / (hbar l)
- v8 adds: how does Lambda_grav change in a gravitational gradient?
- Signal: delta(Lambda) / Lambda ~ (delta g / g) x (R_s / l)

**B. Cosmic Expansion Drift**
- GRUT term mimics dark energy but evolves differently
- rho_GRUT(z) has different redshift dependence than Lambda
- Signal: deviation in H(z) at z ~ 0.5-2.0

**C. Structure Formation Bias**
- Galaxy clustering deviates subtly from LCDM
- But: v7 perturbation growth FAILS — this candidate requires solving
  the second-order problem first

**Recommendation:** Start with A. It builds directly on v7's strongest
result (the decoherence prediction) and is testable with existing
optomechanics technology.

### N.4.4 — Produce First Prediction Curve

Not theory text — actual graphable output.

**Minimum deliverable:** A plot of one of:
- GRUT vs LCDM expansion history H(z)
- Decoherence rate vs mass at multiple gravitational potentials
- GRUT phi field evolution in FLRW

This must be computable from the v8 equations, not imported from v7.

### N.4.5 — The Consistent GRUT Cosmological System

The minimal consistent system couples the scalar field to expansion through
a GRUT correction term. Starting from the v8 base equations:

**Scalar field equation:**

    phi_ddot + 3 H phi_dot + V'(phi) = beta S

**Modified Friedmann (with GRUT correction):**

    H^2 = (8 pi G / 3)(rho_m + rho_r + rho_phi + rho_GRUT)

**Scalar energy density (canonical):**

    rho_phi = (1/2) phi_dot^2 + V(phi)

**GRUT correction (minimal consistent form):**

    rho_GRUT = gamma H phi_dot

This term is the lowest-order covariant scalar-expansion coupling that:
(a) modifies expansion, (b) feeds back into phi dynamics, and
(c) preserves total conservation when matched by the source term.

### N.4.6 — Late-Time Solution: Does Acceleration Emerge?

**Late-time regime (z -> 0):** rho_r -> 0, rho_m -> 0, dynamics dominated
by phi. The Friedmann equation becomes:

    H^2 ~ (8 pi G / 3) [ (1/2) phi_dot^2 + V(phi) + gamma H phi_dot ]

**Slow-roll attractor:** Assume phi_ddot << H phi_dot. The scalar equation
reduces to:

    3 H phi_dot + V'(phi) ~ beta S

Conservation consistency requires the source to match the GRUT energy
exchange: S = -gamma H^2. Therefore:

    3 H phi_dot + V'(phi) = -beta gamma H^2

**Steady-state (constant H = H_inf, constant phi_dot):**
The system flows to a de Sitter-like attractor. Even when V'(phi) != 0,
constant H is sustained because the GRUT term provides effective friction
plus energy injection.

**Acceleration condition:**

    a_ddot / a = H^2 + H_dot > 0

At the attractor: H_dot ~ 0, so a_ddot / a = H_inf^2 > 0. The model
naturally produces de Sitter-like acceleration.

**Effective equation of state:**

    w_eff = -1 + epsilon,    where epsilon ~ phi_dot^2 / (H^2 M_Pl^2)

The GRUT term suppresses kinetic dominance, so w_eff -> -1 without
requiring a finely tuned flat potential.

**Result A:** GRUT generically produces late-time acceleration without a
cosmological constant. The gamma H phi_dot term acts as self-adjusting
dark energy, and the system flows to a constant-H attractor.

### N.4.7 — Observable H(z): Testable Expansion History

Convert to redshift using d/dt = -(1+z) H d/dz and phi_dot = -(1+z) H phi':

**GRUT-modified H(z):**

                   (8piG/3) [ rho_m0 (1+z)^3 + rho_r0 (1+z)^4 + V(phi) ]
    H^2(z) = ---------------------------------------------------------------
              1 - (8piG/3) [ (1/2)(1+z)^2 (phi')^2 - gamma (1+z) phi' ]

**Interpretation:** The denominator is the key GRUT signature.

- If gamma = 0: standard quintessence (no GRUT modification)
- If gamma != 0: modified expansion history with observable consequences:
  - Shift in inferred dark energy density
  - Modified late-time slope of H(z)
  - Potential contribution to H_0 tension resolution
  - Mild deviation in w(z) from -1

### N.4.8 — Dimensionless System for Numerical Integration

The following autonomous system can be dropped directly into a numerical
integrator. All derivatives are with respect to e-fold time N = ln a.

**Dimensionless variables:**

    x = phi_dot / (sqrt(6) M_Pl H)          (kinetic fraction)
    y = sqrt(V) / (sqrt(3) M_Pl H)          (potential fraction)
    Omega_r = rho_r / (3 M_Pl^2 H^2)        (radiation)
    delta = gamma / (sqrt(6) M_Pl)           (GRUT coupling)
    lambda = -M_Pl V'/V                      (potential slope)

**Constraint (modified Friedmann):**

    Omega_m + Omega_r + x^2 + y^2 + 2 delta x = 1

Use this to eliminate Omega_m.

**Evolution equations (3 ODEs):**

    x' = -3x + (sqrt(3/2)) lambda y^2 + x epsilon_H - 3 delta

    y' = -(sqrt(3/2)) lambda x y + y epsilon_H

    Omega_r' = -4 Omega_r + 2 Omega_r epsilon_H

**Hubble flow parameter (closure):**

    epsilon_H = -H'/H = (3 x^2 + 2 Omega_r + 3 delta x) / (1 + delta x)

**Equation of state (diagnostic):**

    w_eff = -1 + (2/3) epsilon_H

Acceleration when epsilon_H < 1.

**Initial conditions (z ~ 10^3):**

    Omega_r ~ 0.999,  Omega_m ~ 10^-3,  x << 1,  y << 1
    Enforce: x^2 + y^2 + 2 delta x = 1 - Omega_m - Omega_r

**Observable output:**

    H(N) = H_0 exp(-integral_0^N epsilon_H(N') dN')
    z = e^(-N) - 1

**Potential choices:**

    Exponential (cleanest): V = V_0 exp(-lambda phi / M_Pl), lambda = const
    Quadratic (physical):   V = (1/2) m^2 phi^2, lambda = -M_Pl / phi

**Stability conditions:**

    |delta x| < 1 (denominator nonzero)
    1 + delta x != 0 (no singularity in epsilon_H)

**Minimal parameter set for v8:**

    gamma (GRUT coupling), beta (energy exchange), V(phi) potential

This system is numerically stable, preserves conservation exactly,
and produces H(z) directly comparable to supernova data and CMB constraints.

### N.4.9 — Map of Modified Equations

The GRUT coupling rho_GRUT = gamma H phi_dot introduces a geometry-scalar-
expansion feedback loop that propagates unavoidably into every sector of
gravitational physics. Below is the minimal consistent form each equation
takes under the v8 structure.

**(1) Einstein Field Equations**

    Standard:  G_mu_nu = 8 pi G T_mu_nu
    GRUT:      G_mu_nu = 8 pi G (T_mu_nu^(m,r,phi) + T_mu_nu^(GRUT))

The GRUT stress-energy is an effective non-perfect-fluid tensor: not purely
isotropic in general backgrounds, encoding dissipative energy exchange.

**(2) Conservation / Continuity Equations**

    Standard:  nabla_mu T^mu_nu = 0
    GRUT:      nabla_mu T^mu_nu_(phi) = Q_nu
               nabla_mu T^mu_nu_(GRUT) = -Q_nu

In cosmology:

    rho_dot_phi + 3H(rho_phi + p_phi) = Q
    rho_dot_GRUT + 3H(rho_GRUT + p_GRUT) = -Q

Energy is redistributed between the scalar and GRUT sectors, not lost.
Total conservation is preserved by construction.

**(3) Klein-Gordon (scalar field)**

    Standard:  Box phi - V'(phi) = 0
    GRUT:      Box phi - V'(phi) = beta S

The scalar is no longer conservative. It acts as an open system coupled
to geometry through the source S = -gamma H^2.

**(4) Raychaudhuri Equation (acceleration)**

    Standard:  H_dot = -4 pi G (rho + p)
    GRUT:      H_dot = -4 pi G (rho_tot + p_tot) + Delta_GRUT

where Delta_GRUT ~ gamma (H_dot phi_dot + H phi_ddot).

This is critical: acceleration is no longer determined purely by the
equation of state. The system can produce acceleration even when w > -1.

**(5) Poisson Equation (structure formation, Newtonian limit)**

    Standard:  nabla^2 Phi = 4 pi G rho
    GRUT:      nabla^2 Phi = 4 pi G (rho + rho_GRUT_eff)

Effective gravity is modified. Depending on the regime, this mimics dark
matter enhancement or modified gravity.

**(6) Growth of Structure Equation**

    Standard:  delta_ddot + 2H delta_dot - 4 pi G rho_m delta = 0
    GRUT:      delta_ddot + (2H + Gamma_GRUT) delta_dot - 4 pi G_eff rho_m delta = 0

New terms:
- Gamma_GRUT ~ gamma phi_dot (modified friction)
- G_eff != G (effective gravitational coupling)

Directly testable via galaxy clustering, weak lensing, and the matter
power spectrum P(k).

**(7) Geodesic Equation**

    Standard:  d^2 x^mu / d tau^2 + Gamma^mu_alpha_beta u^alpha u^beta = 0
    GRUT:      d^2 x^mu / d tau^2 + Gamma^mu_alpha_beta u^alpha u^beta = f^mu_GRUT

Test particles may experience an effective extra force depending on
whether GRUT couples universally or only through the metric.

**(8) Black Hole / Horizon Equations**

Surface gravity is modified:

    kappa -> kappa + Delta(gamma, phi_dot)

The area law acquires a non-equilibrium correction: dA/dt != 0 even in
apparently stationary configurations. Horizons become dynamical,
dissipative systems — connecting to the constitutive BH information
recovery in the main document.

**(9) Effective Equation of State**

    Standard:  w_eff = p_phi / rho_phi
    GRUT:      w_eff = (p_phi + p_GRUT) / (rho_phi + rho_GRUT)

The observationally inferred w is not fundamental. It is an emergent
parameter that conflates the scalar dynamics with the GRUT coupling.

**(10) CMB Perturbation Equations**

Metric perturbations acquire anisotropic stress:

    Phi != Psi  (gravitational slip)

This is a direct, testable signature in:
- CMB lensing
- Integrated Sachs-Wolfe (ISW) effect
- E-mode polarization

### N.4.10 — Structural Assessment

GRUT introduces a geometry <-> scalar <-> expansion feedback loop.
This is not a minor modification — it forces changes in:

| Sector | Status |
|:---|:---|
| Background cosmology | Modified (N.4.5-N.4.7) |
| Conservation laws | Fixed (energy redistribution, not loss) |
| Perturbations | Modified (anisotropic stress, Phi != Psi) |
| Gravity (Einstein eq.) | Extended (T_mu_nu^GRUT) |
| Structure growth | Altered (Gamma_GRUT friction, G_eff) |
| Horizons | Non-equilibrium (dynamical dA/dt) |
| Geodesics | Potentially modified (f^mu_GRUT) |

**Closest existing frameworks:**
- Interacting dark energy (similar energy exchange structure)
- Bulk viscous cosmology (similar dissipative stress)
- Scalar-tensor gravity (similar field-metric coupling)

GRUT is distinct from all three in that the source term D(x) is the
Diosi gravitational self-energy kernel — it connects the cosmological
modification directly to the decoherence prediction.

### N.4.11 — The Covariant Action Gap (Critical Open Problem)

The v8 base system (N.9) is defined at the equation level. What is
NOT yet established:

**The covariant GRUT action:**

    S_GRUT[g_mu_nu, phi] = ?

such that:
- Variation with respect to g_mu_nu produces the modified Einstein equation
- Variation with respect to phi produces the GRUT field equation
- Conservation emerges automatically from diffeomorphism invariance

**Why this matters:**
Without a covariant action:
- T_mu_nu^(GRUT) has residual ambiguity in non-FLRW backgrounds
- Perturbation theory risks hidden inconsistencies
- The theory cannot be systematically quantized

**Why it may exist:**
The CTP effective action S_CTP IS a covariant action. The v7 constitutive
equation is derived from it. The v8 formalization should, in principle,
be obtainable by expanding S_CTP to the appropriate order and reading off
the effective action for phi coupled to g_mu_nu.

**This is the single most important theoretical deliverable for v8.**
Community collaboration in mathematical physics and scalar-tensor gravity
is essential here. The equations work at the FLRW level. The question is
whether they descend from a consistent covariant action at the full
tensorial level.

---

## N.5 — Phase 3: Falsifiability Gate

### N.5.1 — Define Kill Conditions

Explicitly state conditions under which GRUT is false:

1. No decoherence plateau at the predicted rate (kills the core prediction)
2. No deviation in decoherence near gravitational gradients (kills the
   field coupling)
3. Cosmology data fits LCDM better than GRUT-modified model at all
   redshifts (kills the cosmological extension)
4. Lambda_grav measured but Omega_Lambda disagrees (kills the bridge)
5. The GRUT field equation has no stable solutions in FLRW (kills the
   formalization)

### N.5.2 — Identify Existing Data to Test Against

Do NOT wait for new experiments. Use:

| Dataset | What it constrains | Available now? |
|:---|:---|:---|
| Planck CMB (TT, TE, EE) | H(z) at z ~ 1100, Omega_Lambda | Yes |
| DESI BAO | H(z) at z = 0.3-2.0 | Yes (2024 release) |
| SH0ES Cepheids | H_0 at z ~ 0 | Yes |
| LIGO/Virgo noise budget | Decoherence edge cases at detector mass | Yes |
| Atomic interferometry (Stanford, MAGIS) | Decoherence vs gravitational potential | Partial |
| Optomechanics (Aspelmeyer group) | Decoherence of mesoscopic objects | In progress |

**Deliverable:** 1-2 datasets where GRUT can already be constrained,
with explicit chi-squared comparison.

---

## N.6 — Phase 4: Experimental Hook

### N.6.1 — Design a Feasible Tabletop Test

The test does not require CERN-level infrastructure:

**Concept:** Place a quantum system (nanoparticle in superposition) near
a varying mass distribution (rotating source mass). Measure decoherence
rate as a function of gravitational potential gradient.

**GRUT prediction:** Lambda_grav shifts with the local gravitational
self-energy. Standard QM predicts no shift (decoherence is purely
environmental).

**Key:** The isotope test (Appendix L.9) is already a feasible
tabletop experiment. Si-28 vs Si-30 nanoparticles with identical
surfaces but different gravitational self-energy. Predicted 12.9%
rate difference. Required precision: 2.6% for 5-sigma.

### N.6.2 — Define Signal Magnitude

Even rough:

    delta(Lambda) / Lambda ~ 10^-1 (isotope test, 12.9%)
    delta(Lambda) / Lambda ~ 10^-2 (gravitational gradient test, estimated)

Without magnitude, no experimentalist can design the measurement.

---

## N.7 — Phase 5: Compression to Publishable Form

### N.7.1 — Strip Philosophy

v7 language (appropriate for a program document):
- "responsive universe", "informational coupling", "constitutive response"

v8 requirement (appropriate for a physics paper):
- Equations, derivations, predictions, testability
- Interpretation last, after the mathematics is established

### N.7.2 — Paper Structure

1. **Problem:** The decoherence-gravity gap (standard QM has no
   gravitational decoherence; GR has no quantum back-reaction)
2. **GRUT modification term:** The scalar field phi with Diosi-kernel
   source
3. **Derived equations:** Modified Friedmann, GRUT field equation,
   decoherence rate formula
4. **Prediction:** Lambda_grav = G m^2 S(l/R) / (hbar l) with
   6 scaling laws
5. **Testability:** Isotope test, material swap, gravitational gradient,
   CMB constraints

---

## N.8 — Phase 6: Scaling Path (Post-Validation)

Only after Phase 3 success (at least one prediction confirmed or
constrained against data):

| Extension | Prerequisite | What it adds |
|:---|:---|:---|
| Black hole entropy | Stable GRUT solutions in Schwarzschild | BH information from constitutive dynamics |
| Quantum measurement | GRUT field -> collapse mechanism | Physical collapse from gravitational decoherence |
| Dark energy dynamics | GRUT cosmology vs LCDM at z = 0-2 | Time-varying dark energy from phi evolution |
| Structure formation | Second-order constitutive equation | Perturbation growth (fixes v7 failure) |

These are NOT part of v8. They are the roadmap beyond v8, conditional
on v8 surviving its falsifiability gate.

---

## N.9 — The Full v8 Base System (Proposed)

For reference, the complete set of equations that define the minimal v8
field theory:

**(1) Modified Friedmann Equation:**

    H^2 = (8 pi G / 3) [ rho + (1/2) phi_dot^2 + (1/2) m_phi^2 phi^2 ]

**(2) Modified Einstein Equation (covariant form):**

    G_mu_nu = 8 pi G (T_mu_nu + T_mu_nu^(phi))

**(3) GRUT Field Stress-Energy:**

    T_mu_nu^(phi) = nabla_mu phi nabla_nu phi
                    - (1/2) g_mu_nu (nabla phi)^2
                    - g_mu_nu V(phi)

    where V(phi) = (1/2) m_phi^2 phi^2 (minimal quadratic potential)

**(4) GRUT Field Equation:**

    Box phi + m_phi^2 phi = beta D(x)

**(5) Decoherence Source (Diosi Kernel):**

    D(x) = integral d^3 x' G rho(x) rho(x') / (hbar |x - x'|)

**(6) Constitutive Constraint (from v7):**

    tau d(phi)/dt + phi = phi_target[phi]

    where phi_target is determined by the field equation (4)
    and tau is the KMS relaxation time

**Connection to v7:** Equation (1) is the cosmological specialization.
Equation (5) is the noise kernel from v7's foundation. Equation (6) is
the constitutive equation. The v8 formalization wraps them in a scalar
field theory coupled to gravity. No new physics is introduced — the
existing structure is repackaged in language that interfaces with the
GR and QFT communities.

---

## N.10 — Status and Call for Collaboration

This roadmap is classified as:

**PROPOSAL — open for community input**

The phases are sequential but the formalization decisions (entry point,
field definition, observable signature) benefit from external expertise.

**Specific areas where collaboration is needed:**

1. **Mathematical physics:** Existence and uniqueness of solutions to
   the GRUT field equation in FLRW and Schwarzschild backgrounds
2. **Cosmology:** Chi-squared comparison of GRUT-modified expansion
   against Planck + DESI + SH0ES data
3. **Quantum optics / optomechanics:** Feasibility assessment of the
   isotope decoherence test and gravitational gradient measurement
4. **Phenomenology:** Derivation of second-order perturbation equations
   from the GRUT field to address structure formation
5. **Foundations of QM:** Connection between the GRUT decoherence
   mechanism and existing collapse models (CSL, Diosi-Penrose)

**Repository:** https://github.com/ryangrvr/GRUT-RAI
**Computation platform:** All v7 results reproducible via GRUT RAI (Appendix K)

---

*D. Ryan Grover, April 2026.*
*GRUT v7 Appendix N: Toward v8 — A Surgical Roadmap.*
