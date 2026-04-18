# GRUT Cosmological Sector — Specialist Verification Brief

**Prepared by:** D. Ryan Grover, April 2026
**For:** Curved-space CTP specialists (Bei-Lok Hu, Enric Verdaguer, Albert Roura, or equivalent)
**Estimated effort:** 2–4 weeks
**Deliverable:** One dimensionless number per SM gauge group (K_SU3, K_SU2, K_U1)

---

## 1. What We Need

Compute the noise-kernel projection of the coupling-source self-energy on
Euclidean S⁴ with Standard Model matter, and verify that the result uses
SM couplings at the matter-mass scale (M_Z) rather than the curvature
scale (H_inf).

Specifically: extract the O(1) coefficient K_i such that the CTP
forward/backward coupling asymmetry for gauge group i is:

    (g_+ − g_-)_i = K_i × g_i³/(16π²) × f(T_GH/m)

where f → 1 in the limit T_GH >> m (all SM matter thermally excited).

If K_SU3 = 17 × (1 + corrections of order α_s/(4π)), the identification
R_GRUT = ε_combined(SM, M_Z) is verified.

---

## 2. Why This Calculation — Context

GRUT's cosmological formula is H_inf = (2 − R)/(S × τ₀), where f(R) = 2 − R
is derived from 3-loop CTP on S⁴ (verified numerically, quadratic
alternative excluded by 70× in RMS). The value R = 1.15428 was originally
hand-constructed.

A candidate SM-derivable expression was identified:

    R = ε_combined(SM, M_Z) = 1.1537

from Osborn (2003) eq (36), arXiv:hep-th/0302119. This matches the
hand-constructed value to 0.05% and gives Ω_Λ = 0.6886 (Planck:
0.6889, deviation 0.04%).

A 14-step derivation attempt established:
- Steps 1-2: On S⁴, Weyl² = 0 → only Euler coefficient b contributes,
  and b lives in Im(Γ_CTP) (DERIVED)
- Step 3: ε from Osborn 2003 eq (36) is the R·(∂g)² operator coefficient,
  not a multiplicative correction to b (DERIVED from paper)
- Steps 4-6: CTP source doubling with thermal KMS structure produces the
  ε-weighted asymmetry (STRUCTURAL)
- Spectral test: The noise kernel (Γ_I) is IR-dominated at n ≈ 12
  (effective λ ~ 180 H²), while the effective action (Γ_R) is UV-dominated
  at n ≈ 170 (effective λ ~ 29000 H²). 100× separation. (COMPUTED)

The single remaining question is R3: does the noise kernel on S⁴ with
interacting SM matter evaluate its couplings at the matter-mass scale
(giving ε(M_Z) = 1.155, Ω_Λ = 0.69) or the curvature scale (giving
ε(H_inf) = 1.012, Ω_Λ = 0.91)?

Our spectral analysis shows the noise kernel is IR-dominated, which
physically favors the matter scale. The specialist calculation makes
this precise.

---

## 3. The Object to Compute

The coupling-source self-energy on Euclidean S⁴:

    Π(x, y) = ⟨[F_μν F^μν](x) · [F_αβ F^αβ](y)⟩_connected

evaluated on S⁴ of radius 1/H_inf, with SM matter loops running inside.

From Im(Π) (the noise-kernel projection), extract the finite part and
determine the effective renormalization scale at which the coupling
enters.

---

## 4. What Has Already Been Established (Do Not Re-derive)

The specialist can take these as given (all verified, references provided):

**4.1 Geometric facts on S⁴**
- Weyl tensor: C_μνρσ = 0 (maximal symmetry, conformally flat)
- Euler density: ∫E₄ √g d⁴x = 64π² (Gauss-Bonnet, χ(S⁴) = 2)
- Ricci scalar: R = 12H² (constant on S⁴)
- Laplacian eigenvalues: λ_n = n(n+3)H² with degeneracies
  d_n = (n+1)(n+2)(2n+3)/6

**4.2 Anomaly coefficients**
- SM free-field: a_SM = 283/120, b_SM = −3487/1440
- Free-field ratio: |b/a| = 1.0268 (not the target — see §4.3)
- C_FINAL = 1.14021 × 10⁻⁴ (3-loop, from SM field content)

**4.3 Why R ≠ |b/a|**
Three independent arguments (see companion document
ZENODO_EPSILON_IDENTIFICATION.md §1.1):
1. Gradient flow theorem (Jack-Osborn 2014, arXiv:1312.0428): |b/a|
   structurally invariant at all perturbative orders
2. C² = 0 on S⁴: coefficient a doesn't contribute
3. CTP Im(Γ) structure: decoherence couples to b × ε, not b/a

**4.4 The ε formula**
Osborn (2003) eq (36), arXiv:hep-th/0302119:

    ε = 1 + (1/3)(29C − 12R_ψ − (5/2)R_φ) × g²/(16π²)

For SU(3) QCD (C=3, R_ψ=3, R_φ=0): ε = 1 + 17 α_s/(4π)

IMPORTANT: ε multiplies the operator −(1/3) n_V (1/g²) R (∂_μ g)²
(Osborn 2003 eq 35). It is the curvature × coupling-gradient coefficient,
NOT a multiplicative correction to the Euler density. It contributes
only when couplings vary — which the CTP doubling (g₊ ≠ g₋) provides.

**4.5 Spectral dominance (computed)**

| Observable | 50% mode | Effective λ | Character |
|:---|:---|:---|:---|
| Effective action Γ_R | n ≈ 170 | ~29000 H² | UV-dominated |
| Noise kernel Γ_I | n ≈ 12 | ~180 H² | IR-dominated (100×) |

With Hartle-Hawking zero mode: noise kernel is 100% dominated by n=0
for m/H < 0.1 (Starobinsky H⁴/m² enhancement confirmed numerically).

**4.6 HV framework note**
Hu-Verdaguer (2008) state µ̄ is an arbitrary mass scale — but this
applies to their free-field / conformally-coupled treatment. The SM
with running couplings and mass thresholds is beyond their primary
scope. The "µ is arbitrary" statement does not apply to the interacting
SM case without additional analysis.

---

## 5. Calculation Workflow

### Phase A: Setup (3–5 days)

**A1. Background-field method on S⁴.**
Gauge field A_μ = Ā_μ + a_μ (Ā = 0 for vacuum). Quadratic fluctuation
operator has known spectrum on S⁴.

**A2. SM matter propagators on S⁴.**
For each species running in the loop:
- Scalars (Higgs): Allen (1985) massive propagator —
  hypergeometric of geodesic distance
- Fermions (quarks, leptons): spinor spherical harmonics on S⁴,
  eigenvalues (n + 3/2)²/R² + m²
- Gauge bosons: transverse vector propagator on S⁴

**A3. Ghost sector + gauge fixing.**
Standard background-field gauge + BRST. Textbook on S⁴.

Tools: xAct/xTensor (Mathematica) for curved-space tensor algebra.
Alternatively FORM with custom curved-space modules.

### Phase B: 1-Loop Self-Energy (5–8 days)

**B1. Diagrams for ⟨[F²][F²]⟩ at 1-loop.**
Two-vertex topology, matter loops contribute through
g² tr(t_a t_b) = −g² R_ψ δ_{ab}. Self-interaction loops from
gauge-boson couplings. Roughly 8–15 diagrams per gauge group.

**B2. Evaluate each diagram on S⁴.**

    D_i = ∫d⁴x d⁴y (√g_x √g_y) · (tensor structure) · G(x,y;m²)²

using Allen-Jacobson propagators. IBP reduction on S⁴ (more subtle
than flat space due to curvature but tractable).

**B3. Separate Re(Π) and Im(Π).**
The noise-kernel projection is Im(Π). This is the physical deliverable.
Re(Π) gives the vacuum-energy contribution — we already know that uses
µ = H. The specialist should compute both and confirm the different
scale dependence.

### Phase C: Thermal/CTP Structure (2–4 days)

**C1. KMS periodicity.**
On Euclidean S⁴, angular periodicity → thermal periodicity with
β_GH = 2π/H. The Wightman function has KMS structure.

**C2. CTP branch difference.**
⟨[F²]₊ [F²]₋⟩_thermal ≠ ⟨[F²]₊ [F²]₊⟩_vacuum

The difference gives (g₊ − g₋) — the CTP forward/backward asymmetry.

**C3. Extract scale dependence of Im(Π).**
This is the KEY deliverable for R3. Does the finite part of Im(Π)
have its dominant contribution from momenta near matter masses
(confirming IR dominance and M_Z) or from momenta near H
(standard dS practice)?

The spectral test (§4.5) predicts IR dominance. The specialist
calculation either confirms this for the specific tensor projection
or finds UV dominance (which would refute the M_Z identification).

### Phase D: Renormalization + Extraction (2–3 days)

**D1. MS-bar renormalization.** Subtract 1/ε poles.

**D2. Extract K_i per gauge group.**

    (g₊ − g₋)_i = K_i × g_i³/(16π²) × f(T_GH/m_i)

K_i is the dimensionless O(1) coefficient — the primary deliverable.

**D3. Determine effective scale.**
From the finite part of Im(Π), identify whether the coupling g_i
entering K_i is naturally evaluated at the matter-mass scale, the
curvature scale, or some intermediate scale.

### Phase E: Cross-Checks (2–3 days)

**E1. Flat-space limit.** H → 0 should recover standard results.
Specifically, the 1-loop β-function coefficient
β₀ = 11C/3 − 4R_ψ/3 − R_φ/6 = 7 for SU(3) with 6 Dirac quarks.

**E2. Osborn 2003 consistency.** The coefficient structure
(29C − 12R_ψ), (51 for SU(3)), should be reproducible by taking
appropriate projections of the S⁴ self-energy. This is the most
important sanity check.

**E3. Scheme dependence.** Check K_i variation between MS-bar and
momentum subtraction. Physical predictions (Ω_Λ) should be
scheme-independent to the order computed.

**E4. Transcendental check.** Does ln(2)·ζ(3) appear at 3-loop
with a coefficient consistent with the 576 in GRUT's C_FINAL?
This is a bonus check, not a requirement.

### Phase F: Write-Up (2–3 days)

Report containing:
- K_i values for SU(3), SU(2), U(1) gauge sectors
- Scale dependence of Im(Π): confirms M_Z or H or other
- Comparison to target: does ε_combined(K_i) = 1.1554 ± O(10⁻²)?
- Cross-check results (flat-space limit, Osborn consistency)

---

## 6. Expected Output

The specialist's result should look like:

    K_SU3 = 17 × (1 + corrections of order α_s/(4π))
    K_SU2 = [group theory prediction, expected ~6.5]
    K_U1  = [hypercharge weighting, expected negative, ~-40]

    Effective scale of Im(Π): µ_eff = [M_Z / H / other]

If K_SU3 ≈ 17 and µ_eff ≈ M_Z:
→ R_GRUT = ε_combined(SM, M_Z) = 1.155, Ω_Λ = 0.689 (0.04% Planck)
→ Cosmological sector is SM-derived.

If K_SU3 ≈ 17 but µ_eff ≈ H_inf:
→ R_GRUT = ε(H_inf) = 1.012, Ω_Λ = 0.91 (30% miss)
→ ε identification fails; cosmological sector remains conditional.

If K_SU3 ≠ 17:
→ ε identification is wrong at the coefficient level.
→ Check whether the actual K_i give a different ε_combined in
   the viable range [1.08, 1.16].

All three outcomes are clean and publishable.

---

## 7. Success Criteria

1. K_i computed to ≤ 1% precision for all three SM gauge groups
2. Scale dependence of Im(Π) determined (M_Z vs H vs other)
3. Flat-space limit reproduces β₀ = 7 for SU(3) with 6 Dirac quarks
4. Osborn 2003 eq (36) coefficient structure reproduced
5. Scheme dependence quantified (should be sub-percent for physical
   observables)
6. [Bonus] ln(2)·ζ(3) coefficient extracted if 3-loop terms computed

---

## 8. What Could Change the Expected Outcome

1. **Nontrivial scheme dependence.** If K_i depends strongly on
   subtraction scheme, the "match" becomes scheme-dependent. Weakens
   but doesn't kill the claim.

2. **Thermal suppression.** If decoupling of heavy SM particles
   (top quark) suppresses their noise-kernel contribution more than
   assumed, the weighting shifts.

3. **Operator mixing.** F² can mix with F·F̃ under renormalization
   on S⁴. However, at θ = 0 (which SM satisfies to < 10⁻¹⁰),
   this mixing is absent. Confirmed in our pre-analysis (Task 05).

4. **IR dominance invalidated.** If the specific tensor projection
   Im(⟨F²F²⟩) is UV-dominated despite the scalar noise kernel being
   IR-dominated, the M_Z argument fails for this observable.

---

## 9. Papers and Tools

### Essential references
- Osborn (2003), arXiv:hep-th/0302119 — eq (35), (36) for ε
- Jack & Osborn (1990), Nucl. Phys. B 343, 647 — 2-loop anomaly
  coefficients, eq (5.8), (5.12), (5.15)
- Jack & Osborn (2014), arXiv:1312.0428 — 3-loop Yukawa β-functions,
  gradient flow theorem (§6)
- Hu & Verdaguer (2008), Living Rev. Rel. 11, 3 — CTP noise kernel
  on de Sitter, stochastic gravity
- Allen (1985), Phys. Rev. D 32, 3136 — massive propagator on S⁴
- Chetyrkin & Zoller (2012), arXiv:1205.2892 — 3-loop SM β-functions

### Computational tools
- xAct/xTensor (Mathematica) — curved-space tensor algebra
- FORM — large-scale algebraic manipulation
- Allen-Jacobson propagators — hypergeometric of geodesic distance
- Standard MS-bar dimensional regularization

### GRUT-specific references
- GRUT V7 §26–26.1: cosmological formula and ε identification
- ZENODO_EPSILON_IDENTIFICATION.md: full analysis with robustness scan
- COSMOLOGICAL_SECTOR_STATUS.md: current status document
- Derivation Steps 1–6 + Tasks 01–05 + R3 analysis: full logs in
  repository at github.com/ryangrvr/GRUT-RAI

---

## 10. Contact

D. Ryan Grover — dryangrover@gmail.com
Full research: zenodo.org/communities/grut
Software: github.com/ryangrvr/GRUT-RAI

The complete derivation attempt (14 pieces of work, 7 corrections
caught, spectral test results, honest status labels) is available
in the repository for review.
