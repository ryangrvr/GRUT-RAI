# GRUT III, Book A: Effective Action Closure

---

## 1. Stage Summary

Book A audits the CTP / influence-functional backbone established in GRUT-II (Theta/Iota-Prime) for internal consistency, coupling coherence, and domain-of-validity rigor. It does not add new derivations. It classifies every claim, identifies every conflict, and draws the boundary around what the minimal irreversible EFT actually controls.

**What was done this run:**

1. Re-read and cross-referenced the three foundational GRUT-II documents: Theta-Prime (formalism selection), Iota-Prime (explicit construction), Nu-Prime (terminal closure).
2. Audited the CTP backbone for structural completeness against four hard gates.
3. Identified six conflicts that were silently harmonized or left ambiguous in GRUT-II.
4. Constructed the explicit domain-of-validity map with controlled and unsafe zones.
5. Produced the tagged claim ledger below.

---

## 2. Claim Ledger

### 2.1 Structural Claims

| # | Claim | Tag | Regime | Source | Notes |
|---|-------|-----|--------|--------|-------|
| S1 | A local real action cannot generate the first-order dissipative constitutive law tau dPhi/dt + Phi = X. | **DERIVED** (Bauer 1931) | All regimes | Theta-Prime II.1 | Theorem. No approximation. |
| S2 | The CTP / Schwinger-Keldysh doubled-field formalism is necessary and sufficient for the constitutive sector. | **DERIVED** | All regimes where dissipation is present | Theta-Prime II.3 | "Necessary" follows from S1. "Sufficient" demonstrated in Iota-Prime. |
| S3 | The minimal variable set is (g_r, g_a, Phi_r, Phi_a). | **ASSUMED** → partially **DERIVED** | Newtonian, Markovian, overdamped | Iota-Prime VI | Sufficient shown by construction. Minimality not proven — could an auxiliary field reduce to fewer effective DOF? No proof of irreducibility exists. Tag downgraded from "derived" to "assumed + partially derived." |
| S4 | No additional bath field beyond (g, Phi) is needed in principle. | **INFERRED** | Newtonian, overdamped | Iota-Prime VI | See Conflict C3 below. The claim is that g_a provides both USL (tree) and noise (loop). The loop-level computation has NOT been performed. |

### 2.2 Constitutive Sector Claims

| # | Claim | Tag | Regime | Source | Notes |
|---|-------|-----|--------|--------|-------|
| C1 | Variation of iS_eff w.r.t. Phi_a in the classical limit (Phi_a → 0) gives tau dPhi_r/dt + Phi_r = X. | **DERIVED** (exact) | Markovian, overdamped, flat or slowly-varying background | Iota-Prime II | Exact within stated regime. |
| C2 | The noise term iD Phi_a^2 generates Gaussian white noise with variance 2D in the Langevin equation. | **DERIVED** | Markovian, overdamped, thermal equilibrium | Iota-Prime II | Numerically verified (FDT to 1.2%). |
| C3 | D = k_B T × tau (FDT, Ohmic high-T limit). | **DERIVED** | Ohmic spectral density, k_B T >> hbar/tau | Iota-Prime V | The high-T condition k_B T >> hbar/tau is satisfied at T = 4K for tau > 10^-12 s. |
| C4 | The forward semigroup S(t) = exp(-t/tau) and unique attractor Phi* = X follow from the CTP structure. | **DERIVED** | Linear regime (no nonlinear self-interaction of Phi) | Iota-Prime II | Exact for the linear action. Nonlinear extensions (cubic saturation, delay from GRUT-II Nu) are NOT covered by this derivation. |
| C5 | The Markovian constitutive law is the leading-order truncation of the full retarded response when bath correlation time << tau. | **DERIVED** (controlled approximation) | omega_D >> 1/tau (Markovian limit) | Iota-Prime III | Verified numerically for Drude spectral density. |
| C6 | The value of tau is not determined by the minimal CTP action. | **OPEN** | All regimes | Iota-Prime, Nu-Prime | tau enters as a free parameter of the effective theory. Its determination requires specifying the bath spectral density J(omega), which is not computed in GRUT-II. This is the primary GRUT-III foundational issue. |

### 2.3 Quantum / USL Claims

| # | Claim | Tag | Regime | Source | Notes |
|---|-------|-----|--------|--------|-------|
| Q1 | Integrating out the Newtonian gravitational field on the CTP contour gives the Diosi self-energy difference Delta_E as a real phase contribution to the influence functional. | **DERIVED** | Newtonian (v << c, weak field), instantaneous potential (no retardation) | Iota-Prime IV | Standard result. Equivalent to Diosi (1987), Penrose (1996). The GRUT contribution is placing this in the CTP three-sector framework, not the integral itself. |
| Q2 | For a point mass in superposition with separation l: Lambda_USL = Gm^2/(hbar l). | **DERIVED** | l >> R_body (point-mass regime) | Iota-Prime IV | Exact for point masses. Valid for extended bodies only when l > 2R (Kappa-Prime). |
| Q3 | For an extended body with l < 2R: Lambda is suppressed by ~C × (l/R)^3 with C ≈ 0.5. | **DERIVED** (numerical, exact integral) | l < 2R, uniform-density sphere | Kappa-Prime III | Computed by direct numerical integration of the 6D Diosi integral (reduced to 2D by symmetry). |
| Q4 | The USL is a dephasing (real phase) mechanism, structurally distinct from Caldeira-Leggett noise diffusion (imaginary, l^2 scaling). | **DERIVED** | All Newtonian regimes | Iota-Prime IV | The 1/l vs l^2 distinction is exact. |
| Q5 | The USL has no FDT partner (no corresponding noise term). | **INFERRED** | Newtonian, tree-level | Iota-Prime V | See Conflict C2 below. This inference assumes the gravitational self-energy is purely deterministic. At loop level, gravitational fluctuations would introduce a noise partner. The tree-level truncation suppresses this. |
| Q6 | The USL and Level-1 constitutive relaxation are separate predictions for separate observables. | **DERIVED** | Within the three-sector CTP structure | Alpha-Prime, Iota-Prime V | Sector 3 (dephasing) vs Sectors 1-2 (dissipation/noise). Structurally clean separation. |

### 2.4 Coupling Claims

| # | Claim | Tag | Regime | Source | Notes |
|---|-------|-----|--------|--------|-------|
| K1 | Phi couples to gravity only through the source X(g_r), which is determined by local curvature. | **ASSUMED** | All regimes | Iota-Prime I | The form of X(g) is not derived from the CTP action — it is an INPUT. The constitutive framework assumes X is the local curvature-determined equilibrium, but the functional form X[g_{mu nu}] is not specified. |
| K2 | The gravitational sector enters the CTP action through the standard Einstein-Hilbert term doubled on the CTP contour. | **ASSUMED** | All regimes | Iota-Prime I, Theta-Prime | No explicit gravitational CTP action has been written in GRUT-II. The USL derivation uses the Newtonian limit directly, bypassing the need for the full gravitational CTP action. |
| K3 | g_a plays a double role: tree-level USL and loop-level noise/memory. | **INFERRED** | Newtonian | Iota-Prime VI | See Conflict C3. The loop-level role is asserted but not computed. |

### 2.5 Voided / Retracted Claims

| # | Claim | Tag | Source | Reason |
|---|-------|-----|--------|--------|
| V1 | USL/gas = 13 at m = 25 fg, l = 5 nm. | **RETRACTED** | Gamma-Prime through Zeta-Prime | Point-mass formula used at l/R = 0.036. Kappa-Prime correction: suppression 2×10^-5. |
| V2 | Optimal operating point: 25 fg / 5 nm / expansion ratio 2700. | **RETRACTED** | Epsilon-Prime, Eta-Prime | Voided by Kappa-Prime. |
| V3 | USL testable in 2-5 years. | **RETRACTED** | Eta-Prime | Corrected to 5-15 years (Mu-Prime). |
| V4 | SG nanodiamond at 1000 fg / 930 nm / USL/gas = 13 with 10 ms protocol. | **RETRACTED** | Lambda-Prime | Used dB/dz = 10^6 T/m (atom-chip scale, not demonstrated for nanodiamonds). Corrected in Mu-Prime. |

---

## 3. Hard-Gate Status

### Gate 1: Minimal CTP backbone coherence

**Status: PASS (conditional)**

The CTP action in Keldysh basis with three sectors (dissipation, noise, dephasing) is structurally coherent. The constitutive law is derived exactly. The FDT is satisfied. The noise is properly positive (Im S_eff > 0). The CTP unitarity conditions (S_eff[Phi_r, 0] = 0, reality condition, positivity) are satisfied by construction.

**Condition:** Only verified in the Markovian/overdamped/Newtonian regime. Non-Markovian, relativistic, and strong-field extensions are not tested.

### Gate 2: Coupled consistency under (g_r, g_a, Phi_r, Phi_a)

**Status: PENDING**

**Reason:** The full coupled CTP action for (g, Phi) has never been written explicitly. Iota-Prime wrote the Phi sector and used the Newtonian limit for the g sector. The following are unverified:

- Does variation w.r.t. g_a produce a consistent semiclassical Einstein equation?
- Is the backreaction of Phi on g handled correctly in the CTP framework?
- Is there a ghost or instability in the doubled gravitational sector?

These are standard questions in CTP gravity (Calzetta & Hu 1994, Salcedo et al. 2025) but have not been addressed within the GRUT-specific coupling structure.

**What would PASS this gate:** Explicit construction of the full (g, Phi) CTP action, verification of the semiclassical limit, and absence of pathologies in the linearized spectrum.

### Gate 3: Gravitational dephasing and bath/noise sourcing

**Status: FAIL (partial)**

**Reason:** Two distinct sub-questions, with different outcomes:

**(a) Gravitational dephasing (USL):** PASS. The tree-level Newtonian gravitational self-energy integral is computed exactly (Kappa-Prime) and reproduces the Diosi-Penrose result in the valid regime. The CTP placement (Sector 3, real dephasing term) is clean.

**(b) Bath/noise sourcing:** FAIL. The claim that g_a provides the noise kernel D (and hence the dissipation tau) at loop level is ASSERTED but NOT COMPUTED. No one-loop gravitational calculation has been performed. The value of D (and therefore tau) remains a free parameter. The statement "no additional bath needed in principle" (Iota-Prime VI, claim S4) is an inference without a supporting computation. It may be correct, but it is not derived.

**What would PASS this gate:** Explicit one-loop computation of the gravitational contribution to D and tau, or a proof that gravity alone is insufficient and additional matter content is required.

### Gate 4: Domain of validity

**Status: PASS**

The domain-of-validity map is now well-defined (see Section 5). The Kappa-Prime correction and Mu-Prime hardware audit established the regime boundaries through calculation, not assertion.

---

## 4. Conflict Log

### C1: Iota-Prime lines 224-227 vs Kappa-Prime

**Conflict:** Iota-Prime states the USL is "exact for point masses (valid when l >> R_body — 5 nm vs 140 nm radius is marginal; for extended bodies, the DP integral gives a correction factor of order unity)." This characterizes the extended-body correction as "order unity." Kappa-Prime finds the correction is a factor of 44,000 at the stated parameters.

**Resolution:** "Order unity" was wrong. The correction is (l/R)^3, which is 2×10^-5 at l/R = 0.036. Iota-Prime's parenthetical underestimated the correction by ~4.4 orders of magnitude. Kappa-Prime supersedes.

**Status:** RESOLVED. Iota-Prime parenthetical is retracted. The claim now reads: "exact for point masses; for extended bodies, the full Diosi integral must be used. The point-mass formula is valid ONLY for l > 2R."

### C2: USL "has no FDT partner" (Iota-Prime V, claim Q5) — is this exact?

**Conflict:** At tree level, the gravitational self-energy is a deterministic phase with no noise partner, and the FDT does not apply. But at loop level, gravitational fluctuations (metric perturbations from the quantum gravitational field) would produce a noise term that IS the FDT partner of any gravitationally-sourced dissipation. The claim "no FDT partner" is tree-level only.

**Resolution:** The claim should read: "At tree level, the USL has no FDT partner. At loop level, a gravitational noise partner is expected but has not been computed." This is not a contradiction — it is a loop-order truncation. The tree-level USL and the loop-level noise live at different orders in the perturbative expansion of the CTP effective action.

**Status:** RESOLVED by tagging. Claim Q5 updated to: **INFERRED (tree-level only)**.

### C3: "No additional bath needed" (S4) vs "tau not determined" (C6)

**Conflict:** Iota-Prime claims no extra bath beyond (g, Phi) is needed (S4), but also admits tau is not determined by the minimal action (C6). If g_a at loop level provides D and tau, then S4 is consistent with C6 (tau is determined but the computation hasn't been done). But if the loop-level gravitational contribution to D is too small to explain the observed/assumed tau, then S4 is wrong and an additional bath IS needed.

**Resolution:** This is genuinely OPEN. The claim S4 should be downgraded from "inferred" to "open — depends on one-loop gravitational D." It cannot be resolved without the computation.

**Status:** OPEN. This is the first GRUT-III issue.

### C4: Overdamped limit — is it justified?

**Conflict:** The CTP action drops the kinetic term (1/2)(dPhi/dt)^2, retaining only the first-order constitutive equation. This is the overdamped Caldeira-Leggett limit, valid when eta >> M omega_0. But: what IS the inertial mass M of the constitutive field Phi? And what is its natural frequency omega_0? These are never specified in GRUT-II. The overdamped limit is assumed, not derived from a comparison of scales.

**Resolution:** The overdamped limit is an ASSUMPTION of the effective theory, not a derived consequence. Its validity requires that Phi has no propagating wave-like modes at the frequencies of interest. For a cosmological scalar with tau >> H^{-1} (Hubble time), this is plausible. For near-horizon physics where tau ~ t_dyn ~ 10^-5 s, it requires M << eta/omega_0 at these timescales.

**Status:** OPEN. The overdamped limit should be checked when the full (underdamped) action is available.

### C5: X(g_r) — functional form not specified

**Conflict:** The constitutive law tau dPhi/dt + Phi = X requires a source term X that is "determined by local curvature." But the functional form X[g_{mu nu}] is never specified in the CTP action. Is X a scalar invariant of the Ricci tensor? The Kretschner scalar? A contraction with the Phi field? Without specifying X, the coupling between the gravitational sector and the constitutive sector is incomplete.

**Resolution:** This is inherited from GRUT-I, where X was defined operationally (the local equilibrium of the constitutive field for a given background geometry). In the CTP action, X(g_r) must be promoted to an explicit functional. The simplest choice is X = f(R) for some function of the Ricci scalar, but this is not unique.

**Status:** OPEN. Must be resolved for the coupled action (Gate 2) to pass.

### C6: Sector 2 noise coefficient D — what bath?

**Conflict:** The noise coefficient D appears in Sector 2 of the CTP action as D = k_B T × tau (FDT). But what is the temperature T? And what is the bath? If the bath is the gravitational sector (g_a at loop level), then T should be the gravitational vacuum temperature (which is zero in flat space, or the Unruh temperature in accelerated frames, or the Hawking temperature near a horizon). If the bath is a matter/thermal sector, then T is the environmental temperature. GRUT-II never specifies.

**Resolution:** In the experimental roadmap (Delta-Prime onward), T = 4 K is the environmental temperature, and the noise is from gas collisions, not gravitational fluctuations. The Sector 2 noise is effectively an ENVIRONMENTAL noise, not a gravitational one. This means the FDT links the constitutive dissipation (1/tau) to an environmental bath, NOT to the gravitational sector. This is consistent with claim C6 (tau not determined by gravity alone) but contradicts claim S4 (no extra bath needed).

**Status:** OPEN. This sharpens Conflict C3: the noise D likely requires an environmental (non-gravitational) bath. If so, S4 is wrong, and the minimal variable set requires an additional environmental sector.

---

## 5. Domain-of-Validity Map

### Controlled zones (EFT valid)

| Zone | Scale | Curvature | Timescale | Coupling | UV/IR | Quantum/Classical | Status |
|------|-------|-----------|-----------|----------|-------|:-:|:---:|
| **Z1: Constitutive (Markovian)** | l >> lambda_bath | Weak (R << 1/tau^2) | t >> tau_bath | Linear Phi coupling | IR (omega << omega_D) | Classical (Phi_a → 0) | **CONTROLLED** |
| **Z2: USL (point-mass)** | l > 2R | Weak (Newtonian) | t >> hbar/Delta_E | Gravitational tree-level | IR (l >> l_Planck) | Quantum (superposition) | **CONTROLLED** |
| **Z3: USL (extended-body)** | l < 2R | Weak (Newtonian) | Same | Same | Same | Same | **CONTROLLED** (use Diosi integral, not point-mass formula) |
| **Z4: FDT-consistent noise** | Same as Z1 | Same | Thermal equilibrium | Ohmic bath | k_B T >> hbar/tau | Classical-stochastic | **CONTROLLED** |

### Unsafe zones (EFT not validated)

| Zone | Why unsafe | What breaks | Resolution needed |
|------|-----------|-------------|-------------------|
| **U1: Strong curvature** (r ~ R_S) | X(g) unspecified. Overdamped limit unverified. Newtonian USL invalid. | Constitutive law form, USL scaling, and coupling all change. | Full covariant CTP action with explicit X[g]. |
| **U2: Non-Markovian** (omega ~ omega_D) | Markovian truncation fails. Full retarded kernel needed. | Constitutive law acquires memory terms. Simple exponential semigroup breaks. | Specify bath spectral density J(omega). |
| **U3: Underdamped** (M omega_0 >> eta) | Overdamped assumption fails. Inertial term dominates. | EOM becomes second-order wave equation, not first-order relaxation. | Derive or bound M and eta for the Phi sector. |
| **U4: Quantum Phi** (Phi_a not small) | Classical limit (Phi_a → 0) invalid. Full quantum dynamics needed. | Constitutive law is only the mean-field equation. Quantum corrections to Phi dynamics unknown. | Full quantum CTP path integral for Phi (not just the saddle point). |
| **U5: Relativistic separation** (l ~ c^2/(Gm)) | Newtonian approximation for gravitational self-energy breaks. | USL formula receives post-Newtonian corrections. | Compute PN corrections to the Diosi integral. |
| **U6: UV (l ~ l_Planck or l ~ R for extended body)** | Diosi integral has UV sensitivity through 1/|x-x'|. Regularized by R for extended bodies. For point masses, requires cutoff. | USL rate diverges for point masses. Extended-body Diosi integral provides physical regularization. | The natural UV cutoff is the body radius R. No Planck-scale physics enters for mesoscopic tests. |
| **U7: Loop-level gravitational noise** | Not computed. Needed for tau determination and FDT completion. | S4 and C6 unresolved. Bath identity unknown. | One-loop gravitational self-energy on CTP contour. |

### Boundary summary

```
CONTROLLED:                    UNSAFE:
  Newtonian gravity              Strong curvature (U1)
  Markovian dissipation          Non-Markovian (U2)
  Overdamped Phi                 Underdamped Phi (U3)
  Classical Phi_a → 0            Quantum Phi (U4)
  l > 2R (point-mass USL)        l < 2R (use Diosi, not Gm^2/l) (Z3)
  Tree-level dephasing           Loop-level noise (U7)
  Ohmic FDT at k_B T >> hbar/tau   Low-T quantum noise (U4)
```

---

## 6. Next Actions

Ordered by logical dependency. Each action has a gate it addresses.

| Priority | Action | Gate | Deliverable | Dependency |
|:--------:|--------|:----:|-------------|------------|
| **1** | **Specify X[g_{mu nu}] explicitly.** Write the functional form of the curvature source in the CTP action. Minimal choice: X = alpha R + beta (Ricci scalar + constant). Test whether this reproduces the Level-1 near-horizon behavior. | Gate 2, C5 | Explicit X functional with regime tags | None |
| **2** | **Write the full linearized (g, Phi) CTP action.** Include: Einstein-Hilbert on CTP contour, Phi kinetic + dissipative sector, Phi-g coupling through X. Verify: semiclassical Einstein equation from g_a variation, absence of ghosts in linearized spectrum. | Gate 2 | Full coupled CTP action; linearized stability check | Action 1 |
| **3** | **Compute one-loop gravitational contribution to D and tau.** Integrate out g_a at one loop for Phi on a flat background. Extract: noise kernel D_grav, dissipation kernel eta_grav. Compare: D_grav to the environmental D used in the roadmap. Determine: is gravity sufficient to source tau, or is an external bath mandatory? | Gate 3, C3, C6 | D_grav, eta_grav, verdict on bath identity | Action 2 |
| **4** | **Check the overdamped limit.** From the full (underdamped) CTP action (Action 2), identify the Phi inertial mass M and compare M omega_0 to eta. If M omega_0 << eta at the scales of interest, the overdamped limit is justified. If not, the constitutive law receives second-order corrections. | C4 | M, eta, overdamped criterion | Action 2 |
| **5** | **Domain-of-validity freeze.** After Actions 1-4, update the domain map to remove "pending" entries. Convert unsafe zones to either "controlled" (if the computation succeeds) or "excluded" (if it fails). | Gate 4 | Final domain map | Actions 1-4 |

---

*GRUT III Book A complete. Four gates assessed: 1 PASS (conditional), 1 PENDING, 1 PARTIAL FAIL, 1 PASS. Six conflicts identified: 2 resolved, 4 open. Claim ledger: 16 active claims (6 derived, 4 assumed/inferred, 2 open, 4 retracted). Domain map: 4 controlled zones, 7 unsafe zones. Next forced action: specify X[g_{mu nu}] (Action 1), then write the full coupled CTP action (Action 2).*
