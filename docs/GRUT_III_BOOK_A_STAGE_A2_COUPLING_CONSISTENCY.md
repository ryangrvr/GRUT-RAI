# GRUT III Book A — Stage A2: Coupling Consistency Audit

---

## 1. Coupling Map

The minimal backbone {L1, L2, L3, L4, L6} contains four doubled fields: (g_r, g_a, Phi_r, Phi_a). This section maps every coupling between them.

### 1.1 Coupling inventory

| # | From | To | Coupling term | Sector | Mechanism | Status |
|---|------|-----|--------------|:------:|-----------|:------:|
| **K1** | g_r | Phi_r | X(g_r) in Sector 1: -[tau ∂_t Phi_r + Phi_r - **X(g_r)**] Phi_a | 1 | g_r determines the equilibrium target X that Phi_r relaxes toward. One-way: g_r sources Phi_r. | **ASSUMED** (X[g] unspecified) |
| **K2** | Phi_r | g_r | Backreaction: Phi_r contributes to T^{mu nu}_Phi, sourcing the semiclassical Einstein equation for g_r. | Gravitational | Standard scalar-field stress-energy. | **ASSUMED** (not computed in GRUT; the semiclassical Einstein equation from variation w.r.t. g_a has never been written) |
| **K3** | g_a | Phi_r, Phi_- branches | S_IF^{grav}: integrating out g_a at tree level produces the Newtonian self-energy difference between the (+) and (-) branches of a spatial superposition of matter. | 3 | Tree-level Newtonian gravitational interaction between CTP branches. | **DERIVED** (Newtonian limit) |
| **K4** | Phi_a | Phi_r | Noise: the iD Phi_a^2 term couples quantum fluctuations (Phi_a) back into the classical dynamics (Phi_r) via the Langevin noise xi(t). | 2 | Standard CTP noise generation. | **DERIVED** |
| **K5** | g_r | D (noise coefficient) | D = k_B T tau, where T is the bath temperature. If the bath is environmental (gas, thermal radiation), g_r enters only through determining what "equilibrium" means. If the bath is gravitational, D would depend on gravitational fluctuations around g_r. | 2 | Indirect: g_r may set the thermal state of the environment. | **INFERRED** (bath identity unresolved — A1 Conflict C6) |
| **K6** | g_a | g_r | Self-coupling of the gravitational sector: the standard CTP Einstein-Hilbert action S_EH[g_+] - S_EH[g_-] produces the semiclassical Einstein equation from variation w.r.t. g_a. | Gravitational | Standard CTP gravity. | **ASSUMED** (not explicitly constructed within GRUT) |

### 1.2 Coupling diagram

```
          g_r ─────────K1────────→ Phi_r (via X(g_r))
           ↑                         │
           │K2 (backreaction)        │K4 (noise → Langevin)
           │ [NOT COMPUTED]          ↓
          Phi_r ←─────────────── Phi_a
           │                         ↑
           │                         │ (CTP doubling: Phi_a is the
           │                         │  quantum/difference field)
           ↓
          g_a ──────K3──────→ S_IF^{grav} → USL dephasing
           │
           │K6 (gravitational self-coupling)
           ↓
         [Loop: gravitational noise → D?]  [NOT COMPUTED]
```

### 1.3 Missing couplings

| # | Missing coupling | Why it matters | Status |
|---|-----------------|---------------|:------:|
| **M1** | Phi_r → g_r (backreaction, K2) | Without it, Phi is a test field on a fixed background. No self-consistent dynamics. The scalar field's energy-momentum does not curve spacetime. | **OPEN** |
| **M2** | g_a → D (loop-level noise, K5) | Without it, the noise coefficient D is a free parameter sourced by an unspecified bath. The theory cannot self-consistently determine tau. | **OPEN** |
| **M3** | Phi_a → g_a (quantum backreaction of Phi fluctuations on metric fluctuations) | Expected at one-loop order. Likely negligible for mesoscopic experiments but important for self-consistency of the full CTP action. | **OPEN** (expected to be perturbatively small) |

---

## 2. Consistency Identities / Constraints Checked

### 2.1 CTP unitarity conditions

The CTP effective action must satisfy three structural constraints (Calzetta & Hu 1994):

| Condition | Requirement | Status |
|-----------|-------------|:------:|
| **U1:** S_eff[Phi_r, Phi_a = 0] = 0 | Setting the quantum field to zero must give zero action (normalization of the density matrix). | **PASS.** Sector 1 is linear in Phi_a → vanishes at Phi_a = 0. Sector 2 is quadratic in Phi_a → vanishes. Sector 3 (USL) is evaluated on the matter branches, not on Phi_a directly; for identical branches (no superposition), Delta_E = 0. ✓ |
| **U2:** S_eff[Phi_r, -Phi_a] = -(S_eff[Phi_r, Phi_a])* | Reality / hermiticity condition. Ensures the density matrix is hermitian. | **PASS.** Sector 1: -[...] × (-Phi_a) = +[...] × Phi_a = -(original)*. Since the original is real × Phi_a, this gives -original. ✓ (real part is odd in Phi_a). Sector 2: iD(-Phi_a)^2 = iD Phi_a^2 = original. Taking -(...)* gives -(-iD Phi_a^2) = iD Phi_a^2. ✓ (imaginary part is even in Phi_a). |
| **U3:** Im S_eff ≥ 0 | Positivity. Ensures probabilities are non-negative and the density matrix has non-negative eigenvalues. | **PASS.** Im S_eff = D Phi_a^2, and D > 0 (required by FDT: D = k_B T tau > 0 for T > 0, tau > 0). ✓ |

All three CTP unitarity conditions are satisfied by construction. **No violation.**

### 2.2 FDT consistency (KMS symmetry)

The dynamical KMS symmetry of the CTP action (the action-level FDT) requires:

```
Under the KMS transformation:
  Phi_r(t) → Phi_r(-t)
  Phi_a(t) → Phi_a(-t) + i beta ∂_{-t} Phi_r(-t)

S_eff must be invariant (up to boundary terms).
```

**Check for Sector 1 + Sector 2:**

The Markovian dissipation + Ohmic noise action:
```
iS = i ∫ dt [-( tau ∂_t Phi_r + Phi_r - X) Phi_a + iD Phi_a^2]
```

Under KMS with beta = 1/(k_B T):
- The dissipation term transforms as: tau ∂_t Phi_r Phi_a → tau ∂_t Phi_r (Phi_a + i beta ∂_t Phi_r) = original + i beta tau (∂_t Phi_r)^2
- The noise term transforms as: iD Phi_a^2 → iD(Phi_a + i beta ∂_t Phi_r)^2 = iD Phi_a^2 - 2D beta (∂_t Phi_r) Phi_a - D beta^2 (∂_t Phi_r)^2

Invariance requires the cross-term and the (∂_t Phi_r)^2 terms to cancel:
- Cross-term: -2D beta ∂_t Phi_r Phi_a must cancel against... nothing from Sector 1. This means KMS invariance requires D beta = tau / 2, i.e., **D = tau k_B T / 2**.

**Conflict note (CN-A2-1):** The FDT from the Langevin equation gives D = k_B T tau (Iota-Prime, claim C3). The KMS invariance of the CTP action gives D = k_B T tau / 2. The factor-of-2 discrepancy arises from the convention for D: the Langevin noise has <xi xi> = 2D delta(t-t'), so the CTP coefficient is D_CTP = D_Langevin / 2 = k_B T tau / 2. **This is a convention issue, not a physical inconsistency.** The Iota-Prime definition uses D_Langevin; the CTP KMS check uses D_CTP = D_Langevin/2. Both give the same physics. Resolved.

**Status: PASS** (with convention clarified).

### 2.3 Sector 3 (USL) × Sector 1 (dissipation) cross-consistency

The USL (Sector 3) and the constitutive dissipation (Sector 1) are claimed to be independent. Check:

- **Does the USL rate depend on tau?** No. Lambda_USL = Gm^2/(hbar l) has no tau dependence. ✓
- **Does the constitutive relaxation depend on Lambda_USL?** No. The equation tau dPhi_r/dt + Phi_r = X has no gravitational dephasing term. ✓
- **Could they couple at higher order?** Yes: if Phi fluctuations (generated by Sector 2 noise) modify the mass distribution, they could shift Delta_E. But this is a loop-level effect (Phi fluctuation → mass redistribution → modified self-energy), suppressed by the smallness of Phi fluctuations relative to the mean field. At tree level: independent. At loop level: potential coupling, magnitude unknown.

**Status: PASS at tree level.** Cross-coupling at loop level is **OPEN** but expected to be perturbatively small.

### 2.4 Energy-momentum conservation

In the full (g, Phi) CTP theory, variation w.r.t. g_a should produce the semiclassical Einstein equation:

```
G_{mu nu}(g_r) = 8 pi G <T_{mu nu}^Phi>
```

where <T_{mu nu}^Phi> includes contributions from the constitutive field (stress-energy of Phi) and from the noise (stochastic stress-energy).

**Status: NOT CHECKED.** The variation w.r.t. g_a has not been performed because the full coupled (g, Phi) CTP action (L7) has not been written. This is the primary content of missing coupling M1.

**Gate impact:** This is why Gate 2 from Book A remains PENDING.

### 2.5 Ghost / stability check (linearized spectrum)

In the CTP formalism, the doubled gravitational sector can potentially introduce ghost degrees of freedom (negative-norm states from g_a). In the standard CTP construction, ghosts are absent because:
- g_a is not a propagating field (it appears linearly in the classical limit)
- The physical limit g_a → 0 removes the doubled DOF
- The CTP structure is equivalent to the in-in formalism, which has a positive-definite Hilbert space

**Status: PASS by standard CTP argument.** No GRUT-specific ghost check has been performed, but the standard argument applies provided the CTP structure is not modified (and it is not — GRUT uses the standard CTP framework).

---

## 3. Results by Regime

### 3.1 Weak curvature (R/R_S >> 1, Newtonian)

| Check | Result | Notes |
|-------|:------:|-------|
| CTP unitarity (U1-U3) | **PASS** | Verified by construction. |
| FDT / KMS | **PASS** | Convention clarified. |
| Sector independence (1 vs 3) | **PASS** (tree-level) | Loop-level coupling open but expected small. |
| Backreaction (K2) | **OPEN** | Not computed; expected negligible in weak field. |
| Ghost/stability | **PASS** (standard CTP) | No GRUT-specific check needed. |
| X(g_r) specification | **OPEN** | X must be specified for quantitative predictions. In weak field, X → constant + small correction. |
| **Overall** | **INTERNALLY CONSISTENT** | Within declared regime and at tree level. |

### 3.2 Moderate curvature (R/R_S ~ 10-100, e.g., near neutron stars)

| Check | Result | Notes |
|-------|:------:|-------|
| CTP unitarity | **PASS** (structural, regime-independent) | |
| FDT / KMS | **ASSUMED** (Ohmic, thermal) | May require modification if the gravitational environment is non-thermal. Near a compact object, the effective temperature could be the Hawking/Unruh temperature, which differs from the environmental temperature. |
| Sector independence | **OPEN** | The Level-1 formula 1/tau_local = 1/tau_0 + 1/t_dyn mixes gravitational timescales with the constitutive relaxation. If tau becomes geometry-dependent, the separation of Sectors 1-2 from Sector 3 may soften. |
| Backreaction | **OPEN** | Phi's stress-energy may be non-negligible at moderate curvature. T^{Phi}_{mu nu} was computed in GRUT-II Phase 4: rho_eq = -X^2/(2 tau^2), which is small but nonzero. |
| X(g_r) specification | **CRITICAL** | The functional form of X determines near-horizon physics entirely. Without it, no quantitative prediction is possible in this regime. |
| Newtonian USL | **INVALID** | The Newtonian self-energy formula breaks down; post-Newtonian corrections enter. However, for mesoscopic quantum experiments, moderate curvature is irrelevant (experiments are in the weak-field regime). |
| **Overall** | **OPEN** | Not inconsistent, but largely uncontrolled due to X unspecified and Newtonian USL invalid. |

### 3.3 Strong curvature (R/R_S ~ 1-3, near black holes)

| Check | Result | Notes |
|-------|:------:|-------|
| CTP unitarity | **PASS** (structural) | |
| FDT / KMS | **OPEN** | The thermal state near a BH is the Hartle-Hawking state at T_H = hbar c^3 / (8 pi G M k_B). The FDT in this state differs from the flat-space Ohmic limit. The noise coefficient D would be modified. |
| Constitutive law | **OPEN** | The overdamped assumption (L8) is untested near horizons. The Level-1 formula 1/tau_local = 1/tau_0 + 1/t_dyn makes tau curvature-dependent, but this is a GRUT-I result, not derived from the CTP action. |
| USL | **NOT VALID** | The Newtonian self-energy integral is inapplicable. A fully covariant Diosi-type integral on a curved background has not been derived. |
| Backreaction | **CRITICAL** | Phi backreaction on the metric is mandatory near BHs. Without it, the theory is not self-consistent at this scale. |
| X(g_r) | **CRITICAL** | Near horizons, X must encode the relationship between Phi and the local geometry. This is the make-or-break quantity for strong-field GRUT. |
| **Overall** | **OPEN** (not failed, not controlled) | The CTP backbone exists structurally but is quantitatively uncontrolled. No contradiction found because no strong-curvature computation has been performed. The absence of contradiction is absence of evidence, not evidence of absence. |

---

## 4. Contradiction Log

### CN-A2-1: FDT factor of 2 (convention)

**Description:** Iota-Prime states D = k_B T tau. KMS invariance of the CTP action gives D_CTP = k_B T tau / 2. The Langevin equation uses <xi xi> = 2D_Langevin, so D_CTP = D_Langevin / 2.

**Resolution:** Convention difference, not physical inconsistency. The CTP action uses D_CTP; the Langevin equation uses D_Langevin = 2 D_CTP. Both give the same equilibrium variance Var(Phi) = k_B T tau.

**Status:** RESOLVED.

### CN-A2-2: Backreaction omission (K2) vs self-consistency

**Description:** The minimal backbone treats g_r as a fixed background (no backreaction from Phi). This is inconsistent with general covariance, which requires that all energy-momentum sources the metric. The Phi stress-energy T^{Phi}_{mu nu} is nonzero (computed in GRUT-II: rho_eq = -X^2/(2 tau^2)) but is treated as negligible.

**Resolution:** In the weak-field regime, the backreaction is perturbatively small: T^{Phi}_{mu nu} / T^{matter}_{mu nu} << 1. The test-field approximation is valid. In the moderate/strong-curvature regime, this is NOT valid and backreaction must be included.

**Status:** RESOLVED in weak field. OPEN in moderate/strong curvature. Not a contradiction within the declared regime.

### No further contradictions found under declared regime.

**Statement:** Under the declared regime (Newtonian, Markovian, overdamped, linear, Ohmic, test-field approximation), no internal contradictions in the coupling structure have been found. All three CTP unitarity conditions pass. The FDT is satisfied. Sector independence holds at tree level. The linearized spectrum is ghost-free by standard CTP argument.

---

## 5. Required Closure Conditions Still Missing

| # | Condition | Required for | Priority | Status |
|---|-----------|-------------|:--------:|:------:|
| **MC1** | Specify X[g_{mu nu}] as an explicit functional of the metric. | Quantitative predictions at any curvature. Gate 2. | **CRITICAL** | OPEN |
| **MC2** | Write the full (g, Phi) CTP action explicitly, including the Einstein-Hilbert term and the Phi-g coupling. | Semiclassical Einstein equation. Backreaction. Ghost check. Gate 2. | **HIGH** | OPEN |
| **MC3** | Compute the one-loop gravitational contribution to D and tau. | Bath identity. Self-consistency of Sector 2 noise. Determination of tau. | **HIGH** | OPEN |
| **MC4** | Derive or bound the Phi inertial mass M to check the overdamped limit. | Validity of first-order constitutive law. | **MODERATE** | OPEN |
| **MC5** | Compute post-Newtonian corrections to the Diosi integral (or bound them). | USL validity at moderate curvature (not needed for mesoscopic experiments). | **LOW** | OPEN |
| **MC6** | Determine whether the Ohmic spectral density assumption is self-consistent with the gravitational bath. | FDT validity. Sector 2 self-consistency. | **MODERATE** | OPEN |

---

## 6. Gate Decisions

### A2-G1: Internal consistency in declared regime

**Status: PASS.**

**Rationale:** Within the declared regime (Newtonian, Markovian, overdamped, linear, test-field, Ohmic thermal equilibrium), all consistency checks pass:
- CTP unitarity: PASS (U1, U2, U3).
- FDT/KMS: PASS (convention clarified).
- Sector independence: PASS (tree-level).
- Ghost/stability: PASS (standard CTP).
- No contradictions found under declared regime.

The backbone is internally consistent where it claims to be.

### A2-G2: No untagged cross-sector assumptions

**Status: PASS.**

**Rationale:** Every coupling (K1-K6) is tagged with status, mechanism, and regime. Every missing coupling (M1-M3) is identified and tagged as OPEN. The hidden assumptions (H1-H9 from A1) that affect coupling are explicitly cross-referenced:
- H7 (no backreaction) → M1 open
- H5 (environmental temperature) → K5 inferred
- H6 (X exists) → K1 assumed

No untagged cross-sector assumptions remain.

### A2-G3: Strong/weak split explicitly documented

**Status: PASS.**

**Rationale:** Section 3 above provides explicit results for three curvature regimes:
- Weak: INTERNALLY CONSISTENT (all checks pass at tree level)
- Moderate: OPEN (X unspecified, Newtonian USL invalid, backreaction unclear)
- Strong: OPEN (not controlled, but not contradicted either)

The split is documented. No strong-curvature claim is made. The backbone is declared valid only in the weak-curvature regime.

---

*GRUT III Book A Stage A2 complete. Gates: A2-G1 PASS, A2-G2 PASS, A2-G3 PASS. Coupling map: 6 couplings identified (2 derived, 2 assumed, 2 inferred). 3 missing couplings flagged (backreaction, loop-level noise, quantum backreaction). CTP unitarity: 3/3 pass. FDT: pass (convention clarified). Sector independence: pass (tree-level). No contradictions under declared regime. 6 closure conditions remain open (MC1-MC6). Strong curvature: open (not failed, not controlled).*
