# L0 LIFT SELECTION — INDEPENDENT VERIFICATION 01

- **Status:** VERIFICATION REPORT. No selector evaluated here, no terminal assigned.
- **Authority:** owner ruling `5899215672` (`L0_LIFT_SELECTION_OWNER_RULING_01.md`), items V-1 … V-7.
- **Verifier:** an independent adversarial subagent, read-only on the repo. Abstract mathematics on
  1–3 modes only; no repo data imported.
- **Operator re-run:** s1 (Koopman vs Mehler) reproduced.
- **Scripts:** `calc/feasibility/lift_verify/` (s1–s4).
- **Frozen target:** `L0_LIFT_SELECTION_01.md` at `a14c722`.

## §0 Summary

| Item | Verdict |
|---|---|
| V-1 / I-1 (collective) | **COUNTEREXAMPLE.** Quasi-free lifts cannot reproduce the earned nonlinear L0-1c responses. |
| V-1 / I-1 (lift by lift) | mixed (§1). Each lift yields k(τ) only through its own declared readout identification. |
| V-2 / I-2 spectra | IMPORTED-STANDARD, **on polynomial observables only** |
| V-2 "first discriminator is −2λ_k" | **COUNTEREXAMPLE** without a non-resonance condition |
| V-2 permanent vs determinant | IMPORTED-STANDARD at gauge-invariant quasi-free scope |
| **V-3 Koopman vs real Λ-B** | **NO MERGE** |
| V-4 / I-3 "every dilation exact" | **COUNTEREXAMPLE.** Finite positive-energy baths are not exact (Bohr). The second-order Bateman is not the earned model. |
| V-4 interface-relative wording | VERIFIED-WITH-NARROWER-SCOPE (the bath preparation must be declared) |
| V-5 / I-4 | VERIFIED-WITH-NARROWER-SCOPE. The exclusion part is a theorem. "Not quasi-free" ≠ "no lift". |
| V-6 graded CAR locality | IMPORTED-STANDARD, checked. **The D-6 fermion exclusion is withdrawn.** |
| V-7 bosonic complex structure | VERIFIED, with a sharper price, including the odd-N obstruction. §1's "fermions need no complex structure" is narrowed. |

## §1 V-1: what each lift reproduces

**The earned model.** ẋ = −K_bx − 4βx³ (β = 0 is the linear core; K_b is symmetric positive
definite, N = 23), with identity readout x₁, probe x(0) = a·e₁ and kernel
k(τ) = e₁ᵀe^{−K_bτ}e₁.

| Lift | (a) one-particle map | (b) k(τ), and through which readout | (c) reduced semigroup? | Verdict |
|---|---|---|---|---|
| Λ-K (composition) | ℓ_c ↦ ℓ_{e^{−Kᵀt}c} | x₁ in the δ-state δ_{ae₁}: **exact, all β** | the full semigroup; the earned model rewritten | VERIFIED |
| Λ-KvN | via U\*M_gU = M_{g∘φ_t} | ∫\|ψ\|²x₁∘φ_τ. **At β = 0** it equals k for any ψ with mean e₁. **At β > 0** it matches only in the δ-limit, which is not a vector state | — | VERIFIED-WITH-NARROWER-SCOPE. Also: KvN is exactly the Weyl quantization of the cotangent lift on the subalgebra at most linear in p, where Groenewold–van Hove does not obstruct (this narrows BC-9). |
| Λ-H cotangent (H = pᵀf) | the x-projection commutes with the flow | x₁(τ) from (ae₁, any p₀): **exact, all β** | — | VERIFIED. H is indefinite, and the p-sector grows as e^{Kᵀt}. |
| Bateman | the first-order version = the cotangent lift. The second-order original is not the earned model | — | — | **merge into the cotangent row / strike** |
| FKM / Caldeira–Leggett | a second-order Langevin equation; e^{−Kt} only as the mean response in an infinite Ohmic overdamped limit with the bath unexcited | a finite positive-definite bath **cannot** reproduce k exactly (x₁ is almost periodic; Bohr) | — | **NOT-ESTABLISHED** as exact |
| Sz.-Nagy minimal unitary dilation | P_HU(t)\|_H = e^{−Kt} (needs K accretive: R-4) | ⟨e₁,U(τ)e₁⟩, a one-particle **amplitude**. It needs a zero bath initial component | yes, linear only | VERIFIED-WITH-NARROWER-SCOPE |
| Λ-B (Γ_B) | exact on the one-particle sector | the amplitude; the coherent-state field mean (linear in a); **over the real space**, the Mehler/OU conditional mean, which is **P^resp only**. The covariance is **T C₀ T†**, not e^{−Kt}C₀e^{−Kt} unless K is symmetric | linear only | VERIFIED-WITH-NARROWER-SCOPE |
| Λ-F (Γ_F) | exact on the one-particle sector | the amplitude; the two-time ⟨{a₁(τ),a₁†}⟩ (quantum regression); ⟨n₁⟩ = k². **The linear readout image is odd:** under parity superselection ⟨γ₁⟩ = 0 in every physical state | linear only | VERIFIED-WITH-NARROWER-SCOPE |

**Consequence for I-1.** "All lifts agree at earned access" holds **only on linear members**, and
only under a **lift-specific declared readout identification**, which is itself a supplied datum per
lift.
- On β > 0 members the quasi-free lifts **cannot** agree. Their Heisenberg maps are linear in the
  fields, so any readout is linear in the probe amplitude a, while r(τ; a, β) is not. This is a
  theorem.
- **Verifier's flag:** evaluating D-1 on the nonlinear predicates would re-import D-2 (ruled
  CRITERION) through an EARNED row.

## §2 V-2: spectra and statistics

- **Koopman.** On polynomials of degree ≤ d the spectrum is {−Σnₖλₖ}, for any K. Monomials in
  normal coordinates additionally need K diagonalizable.
  - **Off polynomials it changes:** on L²(γ), |x|^s is an eigenfunction with eigenvalue T^s, so the
    point spectrum is a punctured disk.
  - "Koopman spectrum = boson number spectrum" is therefore a statement about the symmetric algebra
    only.
- **Fermionic eigenvalues** are subset sums.
- **Counterexamples** (eigenvalues 1, 2, 3):
  - 2λ₂ = 4 = λ₁ + λ₃ lies in Λ²;
  - ungraded, 2λ₁ = λ₂;
  - with the repeated spectrum (1, 1, 3), 2 = 2λ₁ lies in Λ² with every nₖ ≤ 1.
- **Non-resonance condition.** −2λ_k separates the two spectra iff 2λ_k ∉ {Σ_{j∈S}λ_j}.
  - Within the graded n = 2 sector: λ_k simple and 2λ_k ≠ λ_i + λ_j.
  - For a Jacobi K_b, k = argmin λ satisfies the graded condition.
  - The ungraded condition (2λ_min ∉ spec K) is **unchecked on K_b.**
- **The invariant discriminator.** **Sym² vs Λ²** (dimensions N(N+1)/2 vs N(N−1)/2). Equivalently,
  nilpotency a(f)² = 0 in CAR, or :B(f)B(f): = 0 in real Clifford. Higher correlations follow.
- **Wick.** Permanent vs determinant for normally ordered correlators in **gauge-invariant
  quasi-free states** (checked on 2 modes; ⟨n₁n₂⟩ differs by 2|C₁₂|²). Otherwise hafnian (bosons)
  or Pfaffian (fermions).

## §3 V-3 (priority): Koopman vs the real bosonic lift — NO MERGE

1. **Not the same semigroup** (operator re-run reproduced):
   - U_T x² = T²x², while P_T x² = T²x² + (1 − T²);
   - Hermite polynomials are eigenfunctions of P_T but not of U_T;
   - on L²(γ), U_T does not preserve γ, has norm |det T|^{−1/2} > 1, and has disk spectrum;
   - P_T is a γ-invariant Markov contraction.

   **They are not unitarily equivalent, nor similar, on L²(γ).**
2. **What is true.** On polynomials, P_T = W U_T W⁻¹ with W = e^{−Δ/2} (Wick ordering; verified to
   degree 4 for a non-symmetric 2-mode T). Under the transported (Fischer/Fock) inner product,
   U_T|_poly = Γ_s(Tᵀ). **So they are unitarily equivalent only as abstract contraction semigroups on
   the symmetric algebra.**
3. **The observable content is not intertwined:**
   - W M_x W⁻¹ = x − ∂ = a†, not the Segal field;
   - U_T is multiplicative, but P_T is not (P_T(x₁²) − P_T(x₁)² = (I − TTᵀ)₁₁ = 0.71);
   - a theorem: no algebra isomorphism Φ satisfies ΦU = PΦ.

   The readouts differ as well: a deterministic x₁(τ) vs a random X₁(τ) with variance
   1 − (e^{−Kτ}e^{−Kᵀτ})₁₁.
4. **Identification.**
   - Real Λ-B is the transition semigroup of the **OU process with noise Q = K + Kᵀ**. It is an
     FDT-held, L0-1e-type declared extension, which exists iff K is accretive.
   - Koopman is its ε → 0 limit, a singular limit (ε supplied), not an equivalence.

**Under R-2, Λ-K and real Λ-B stay separate.** Whether real Λ-B counts as "representational" under
R-3 is left open by the verifier. It adds fluctuation content.

## §4 V-4 … V-7

- **V-4.** Corrected I-3:

  > Dilations that realize the same reduced retained-site map **under a declared bath
  > preparation** are indistinguishable at that earned interface.

  - Imported (Sz.-Nagy–Foiaș): the minimal unitary dilation is unique up to a unitary equivalence
    fixing H, and every unitary dilation is the minimal one plus an invisible reducing summand.
  - Beyond unitary dilations nothing is proved. Classical and quantum dilations differ in algebra
    type, energy boundedness and statistics.
  - Exact reproduction of k needs an infinite-dimensional dilation or an indefinite H.
- **V-5.**
  - I-4's exclusion is a theorem (§1).
  - KvN, the cotangent lift and the Carleman/Doi–Peliti Fock form of Koopman are non-quasi-free
    lifts. The last is representational and not self-adjoint; whether it generates a semigroup is
    NOT-ESTABLISHED.
  - Interacting quantization is non-unique by example (x³ vs :x³:).
- **V-6.** Under CAR over site-orthogonal modes, odd generators at disjoint sites anticommute, and
  even parts of disjoint regions commute ([AB, C] = A{B,C} − {A,C}B; Jordan–Wigner; checked on 3
  sites). The observable net under parity superselection is the even, commuting net. **The predicted
  D-6 fermion exclusion is WITHDRAWN.** What remains is a price: the site coordinate's natural image
  is odd (§1, Λ-F row).
- **V-7.**
  - CCR needs a real symplectic space. **ℝ²³ carries no symplectic form and no complex structure**
    (both need even dimension).
  - On even N, e^{−Kt} is never σ-symplectic (det < 1), so it acts only through quasi-free CP maps
    with noise.
  - **The canonical route is doubling** (ℂᴺ, or T\*ℝᴺ). **Its price:**
    - N extra real directions (π fields, like KvN's λ);
    - a σ normalization;
    - the J-linear extension.
  - The commutative Mehler construction needs only (ℝᴺ, metric, γ-scale ε, accretive K).
  - **Narrowing of §1:** Cl(ℝᴺ) and ΛT need no complex structure. But Fock vacuum, occupation
    numbers, particle number, ⟨n₁n₂⟩ and determinants **do** need complexification, which for
    N = 23 is the same doubling price as for bosons.

## §5 D-4 / D-5 readiness (verifier; no evaluation)

| Lift | Descended sector | Source-descended observables | Flags |
|---|---|---|---|
| Λ-K | ℝᴺ, δ-states | V∘φ_t | for β > 0, "accretive" needs a nonlinear notion that the record does not state |
| Λ-KvN | multiplication subalgebra | M_V | the λ-sector expands; vector states are not orbits |
| cotangent | base x | V∘π | H is indefinite; Hamiltonian passivity ≠ R-4 accretivity |
| FKM | system coordinates, in the limit | V(mean) | **ill-defined** until the bath limit and preparation are fixed |
| Sz.-Nagy | compression to H | ⟨v, Pv⟩ | only for accretive K |
| Λ-B complex | one-particle sector | dΓ(P) or tr(PC) | ordering choice |
| Λ-B real (OU) | first Wiener chaos | P_tV = V∘Tx + ½tr(P(I − TTᵀ)) ≠ V∘φ_t | **ill-defined between V(mean) and E[V]**; O-5's 𝒞₃ (law-level) clause may be the applicable one |
| Λ-F real Clifford | degree-1 elements | Σ P_ij γ_iγ_j = tr P, a scalar | **ill-defined:** O-5's quadratic Lyapunov functions have trivial image |

**The verifier's instruction:** whether "source-descended observable" means (R-a) V evaluated on
the descended one-particle data or (R-b) the operator image of V must be declared **uniformly and in
advance.** Choosing after evaluation would add a discriminator. This is addressed in
`L0_LIFT_SELECTION_EVALUATION_01.md` §0.

## §6 Additive corrections

LS-1 … LS-10 are applied in `L0_LIFT_SELECTION_CORRECTIONS_01.md` (ruling step 3: "apply additive
corrections … and strike every dependent prediction before selector evaluation").
