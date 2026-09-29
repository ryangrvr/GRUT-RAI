# L0 LIFT SELECTION — CORRECTIONS 01 (additive; governs `L0_LIFT_SELECTION_01.md` where they conflict)

- **Authority:** owner ruling `5899215672`, evaluation step 1 ("If any I-1…I-4 claim fails, apply an
  additive correction and strike every dependent prediction **before** selector evaluation").
- **Source:** `L0_LIFT_SELECTION_VERIFICATION_01.md`.
- The frozen pre-registration (`a14c722`) is preserved. **No discriminator is added, and no R-0
  ruling is changed.**

| # | Target | Correction |
|---|---|---|
| **LS-1** | I-1 and its consequence | Replaced by the lift-by-lift table (verification §1). "All lifts agree at the earned interface" holds **only on linear members, under a declared per-lift readout identification** (itself a price). On β > 0 members the quasi-free lifts provably cannot agree. **Struck:** the §3 prediction "D-1 non-discriminating (I-1)". **Flag carried to evaluation:** the D-1/D-2 reconciliation. |
| **LS-2** | the Λ-B/Λ-F covariance | C(t) = T C₀ T† (= e^{−Kt}C₀e^{−Kt} only for symmetric K). |
| **LS-3** | the §1 Λ-H row | The first-order Bateman doubling **is** the cotangent lift (merged). The second-order Bateman is not the earned model (struck). FKM: exact **only** as the mean response in an infinite Ohmic overdamped limit with a declared unexcited bath; a finite positive-definite bath cannot reproduce k. |
| **LS-4** | I-2 | Scoped to **polynomial observables.** "First spectral discriminator −2λ_k" holds only under the non-resonance condition 2λ_k ∉ {Σ_{j∈S}λ_j} (graded: λ_k simple and 2λ_k ≠ λ_i + λ_j). **The invariant discriminator is Sym² vs Λ²** (repeated-mode occupation; nilpotency a(f)² = 0). Wick permanent vs determinant is scoped to gauge-invariant quasi-free states; otherwise hafnian or Pfaffian. |
| **LS-5** | §4, row 3 (Λ-K vs real Λ-B) | **NOT merged** (V-3). Equivalent only as abstract contraction semigroups on the symmetric algebra (Wick map W = e^{−Δ/2}). The observable algebras are not intertwined (P_T is non-multiplicative). Real Λ-B = the OU semigroup with Q = K + Kᵀ; Koopman is its singular ε → 0 limit. |
| **LS-6** | I-3 | Replaced by: "Dilations realizing the same reduced retained-site map **under a declared bath preparation** are indistinguishable at that earned interface." "Differ only in bath observables" is withdrawn outside unitary dilations (Sz.-Nagy–Foiaș decomposition). |
| **LS-7** | I-4 | The exclusion part is a theorem (linear Heisenberg maps vs the a-dependent r(τ; a, β)). Non-quasi-free lifts: KvN (= the Weyl quantization of the cotangent lift on the ≤1-in-p subalgebra, which also narrows BC-9's Groenewold–van Hove remark), the cotangent lift, and the Carleman/Doi–Peliti Fock form (representational; semigroup NOT-ESTABLISHED). Interacting quantization is non-unique (x³ vs :x³:). **Scope/price only (D-2 is CRITERION).** |
| **LS-8** | D-6 | The predicted fermion exclusion is **withdrawn** (graded locality; commuting even net). A priced residue is added to Λ-F: the site coordinate's natural image is **odd**, so linear one-time readouts vanish under superselection, and k appears via the amplitude, ⟨{a₁(τ),a₁†}⟩, or k² via ⟨n₁⟩. |
| **LS-9** | the §1 Λ-F row, "no complex structure needed" | Restricted to Cl(ℝᴺ)/ΛT. **Fock vacuum, occupation numbers, particle number and determinants need complexification.** ℝ²³ admits no J or σ, so the doubling price is the same as for bosons. |
| **LS-10** | new | The D-4/D-5 readiness table (verification §5) is added, with the ill-definedness flags (FKM, real Λ-B, real Clifford Λ-F) and the requirement that "source-descended observable" be fixed uniformly and in advance. |

**The lifts as they stand for evaluation** (after LS-3 and LS-5; no mergers beyond LS-3's
Bateman → cotangent):

| Lift | Status |
|---|---|
| Λ-K | representational (R-3) |
| Λ-KvN | representational (R-3) |
| Λ-H cotangent (incl. first-order Bateman) | — |
| Λ-H Sz.-Nagy | — |
| Λ-H FKM | exactness NOT-ESTABLISHED |
| Λ-B complex (priced, V-7) | — |
| Λ-B real / OU | not merged. Representational status under R-3 **not ruled**; it adds fluctuation content |
| Λ-F complex Fock (priced, V-7/LS-9) | — |
| Λ-F real Clifford | — |
