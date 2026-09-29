# EA-0 — CORRECTIONS 01 (additive; the verifier's eight corrections, accepted by owner ruling 02)

**Applies to:** `EA0_ENDOGENOUS_ACCESS_FORMULATION_01.md` (commit `1748ccd` plus its in-document
L7 caveat). That document is **preserved as written.** Where it conflicts with this file, **this
file governs.**
- **Source:** `EA0_INDEPENDENT_VERIFICATION_01.md` §5 (commit `41895a4`).
- **Authority:** `EA0_OWNER_RULING_02.md` §2.
- **Terminal (owner):** EA-0 = **UNFORMULABLE at earned Level-0 scope.** The auxiliary quantum
  findings are subordinate and do not upgrade it.

## C-1 · L2 (the category error)

**Replace** the sentence about "the declared L0 substrate" in L2 with:

> The earned L0-1a/b/c substrate is **classical deterministic dynamics** (ẋ = −Kx; L0-1c also the
> gradient flow ẋ = −∇V). Its asymptotic state under ẋ = −Kx is the **point mass δ₀**, not a
> full-support state. The quantum reach projector P_ρ, the compression P_ρ𝒜_xP_ρ and Γ(ρ) are
> **not defined** on that substrate without an additional lift (Koopman, Liouville, stochastic,
> quantization) that is not currently earned. For the L0-1e stochastic members, the Gaussian
> stationary law has full support iff (K,B) is controllable (Kalman; standard). That holds when
> Q ≻ 0 and is **unverified** for the rank-deficient members, which include zero-temperature and
> rank-one-noise members.

The primitive-semigroup analogue is **VERIFIED-WITH-NARROWER-SCOPE**: the imported standard
result applies to the stationary state, and no semigroup notion of reach is defined.

## C-2 · L3 (define "generic"; L3′ only where established)

**Add:**

> "Generic" means outside a closed, Lebesgue-null real-algebraic subset of Herm(ℋ) × ℋ
> (degenerate H, or E_λψ = 0 for some λ). Within a parametrized local family it requires at least
> one non-degenerate witness. **It is false in families that carry a symmetry**, since sectors are
> then forced.
>
> **L3′ (at d = 4 and d = 8 only; witnessed).** For generic H, Γ(ρ) = Γ for **every** ρ,
> including ρ that miss eigenvectors. **L3′ is not a theorem for arbitrary dimension.**

## C-3 · L4 (the exact identity only; the physical reading retired)

**Keep:** Γ(ρ) ⊆ Γ **for the particular definition of Γ(ρ) used.** Add: "the compression
A ↦ PAP is multiplicative iff P ∈ 𝒜_x′" (commuting with 𝒜_x is not the condition for the image to
be an algebra).

**Retire** "exclusion, never inclusion" as a physical prediction. Replace it with:

> Γ is monotone in P_ρ for this definition. This is a property of the chosen definition. It is
> **not** a physical prediction and **not** state-to-state monotone. An equally seedless,
> covariant, localized compressed definition, Γ′ (x ~′ z iff [PAP,[PHP,PBP]] ≠ 0), **can add an
> edge absent from Γ.**

## C-4 · L5 (commutant corrections)

- {ρ}′ for non-degenerate ρ: full rank is **not** needed.
- **{e^{−βH}}′ = {H}′ for all Hermitian H and all real β ≠ 0.** Non-degeneracy is not needed.
  Hence 𝒜_x ∩ {ρ_β}′ = the local conserved quantities of H, for any H.
- **C-5 row:** replace "entangled faithful ρ" with "**generic** faithful ρ". Counterexample:
  ρ = ρ_xs ⊗ 𝟙_y/2 is full rank and entangled, yet {ρ}′ ⊇ 𝒜_y.

## C-5 · L6 (linear-field response only)

> L6 holds for **linear-field** response in the quadratic class and bears only on (a)-type response
> data. Nonlinear probes are state-dependent (e.g. [q(t)², q²] is operator-valued). **L6 does not
> establish triviality of C-6.** C-6 uses all of 𝒜_x, and the bosonic quadratic class is
> infinite-dimensional, outside L1's scope.

**Every use of L6 in §0.2, §7 and §8 to support C-6's triviality is withdrawn.**

## C-6 · L7 (mechanism retired; the exact content kept)

**Keep (exact):**

> x ≁_ρ y ⟺ P_ρ[A,[H,B]]P_ρ = 0 for all declared local A ∈ 𝒜_x, B ∈ 𝒜_y,

together with its equivalents:
- **(2a)** ⟨φ|[A,[H,B]]|φ⟩ = 0 for all φ ∈ 𝒦(ρ). Γ(ρ) is the union, over pure states in the
  sector, of their short-time x–y response graphs.
- **(2b)** Tr_{ȳ}[H,[A,M]] = 0 for all A ∈ 𝒜_x and M ∈ P𝔅(ℋ)P.

**Record explicitly:**
- "the coupling acts trivially in the sector" is **neither necessary nor sufficient** (examples A,
  F; B, D);
- "aligned with a local configuration" is **not necessary** (158 of 206 removable 3-qubit
  configuration sectors fix neither x nor y; removal also occurs with no frozen site, at ranks 2–6
  of 8, and at rank 1);
- "extensive, configuration-dependent sectors" is **not a proved requirement**. It is an
  interpretive restriction. The rank-based "degenerate regime" line is a matter of degree, not a
  proved dichotomy;
- **edge removal can depend on H outside the reachable sector** (through virtual excursions);
- **no structural necessary-and-sufficient mechanism was found**;
- "exact invariant structure in the generator" is **vacuous** as a condition on H, since every H
  has proper invariant subspaces.

**Retire** L7's mechanism sentence and the (3)–(5) language in full.

## C-7 · Theorem S (kept, as a sufficient condition only)

> **Theorem S.** Let Q_x be a local projector with [H, Q_x⊗𝟙] = 0, supp ρ ⊆ Q_x⊗𝟙, and
> P = Q_x⊗𝟙. Then P[A,[H,B]]P = [PAP, P[H,B]P] for all A ∈ 𝒜_x, B ∈ 𝒜_y. If rank Q_x = 1, every
> x–y edge is removed.

It is a genuine positive theorem, proved by the verifier and checked by the operator. **It is
sufficient only;** it does not characterize the branch.

## C-8 · §0 / §8 / §9

- **§0.1:** delete "**canonical**".
- **§0.3 and §8:** replace "non-trivial exactly when / iff the generator carries exact local
  invariant structure …" with:

  > "C-6 **can** be non-trivial when H has exact local invariant structure (Theorem S gives a
  > sufficient case); no characterization is proved."

- **§8, EA-1 paragraph:** replace "EA-0 already settles EA-1's original question structurally"
  with:

  > "EA-0 settles the declared reach-based Γ(ρ) construction largely by construction; it does
  > **not** settle endogenous access generally."

- **§9.1:** "only through support relative to invariant subspaces, or {ρ}′" is **heuristic**.
  Unexamined competitors: ρ's eigenspaces and modular flow, and the supports of local marginals.
- **§9.3–4:** replace the general "endogenous access, where non-trivial, is generator-carried"
  with:

  > "**Reach-based** access is generator-carried **by identity**, because its reachable sector is
  > defined through generator-invariant structure. That is **not** evidence that all
  > state-derived access mechanisms are generator-carried."

- **§0.2 and the §7 row "C-6 on every earned class":** replace with:

  > "TRIVIAL/IDENTITY for faithful states (any finite-dimensional quantum class) and for generic
  > quantum H (L3′ at d = 4, 8); **UNFORMULABLE on the earned classical L0 substrate**."

- **§7 "EA-0 overall" and the §10 proposal:** superseded by the owner's terminal, **UNFORMULABLE
  at earned Level-0 scope**, with the subordinate auxiliary findings of `EA0_OWNER_RULING_02.md` §1.
