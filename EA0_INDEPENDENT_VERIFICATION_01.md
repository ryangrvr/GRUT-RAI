# EA-0 — INDEPENDENT VERIFICATION 01

**Status: VERIFICATION REPORT. No terminal assigned** (the owner assigns it). Ordered by
`EA0_OWNER_RULING_01.md` §1.

**Who did it:**
- An independent adversarial verifier (subagent). It was given the owner's attack targets, not
  the operator's reasoning, and instructed that "no result is to be protected".
- It was read-only on the repository.
- Its lemma checks used **abstract 2–3 qubit toy operators only**. No declared substrate was
  evaluated, and no physics model was built.
- The operator re-ran the key scripts, and the numbers reproduced (§6). The operator also checked
  Example B and Theorem S by hand.

`EA0_ENDOGENOUS_ACCESS_FORMULATION_01.md` is **unmodified.** The corrections are *proposed* in
§5, additively, for the owner to accept.

## §0 Headline

1. **Recommended terminal (verifier; matches the owner's provisional reading):**
   **TRIVIAL/IDENTITY ON EARNED SCOPE + CONDITIONAL FORMULABLE BRANCH**, with one scope amendment.
   - On the *classical* earned L0 substrate, C-6 is **UNFORMULABLE-YET** (not defined), not
     TRIVIAL.
   - **CLASS-SPLIT is not earned as written.**
2. **L7's mechanism language is retired by counterexample.**
   - "Coupling acts trivially in the sector" is **neither necessary nor sufficient**.
   - "Aligned with a local configuration" is **not necessary**.
   - "Extensive sectors" is an **interpretive restriction, not a proved condition**.
   - The only exact necessary-and-sufficient condition is the definitional one (in expectation or
     dual form).
   - Edge removal **depends on H outside the reachable sector** (virtual excursions), so no
     condition on the sector-restricted coupling alone can characterize it.
3. **L2's claim about the declared L0 substrate is NOT ESTABLISHED, and is a category error.**
   - The earned L0-1a/b/c substrate is **classical and deterministic** (ẋ = −Kx). Its invariant
     measure is the **point mass δ₀**, not a full-support state.
   - Reach, compression and Γ are **undefined** there without a lift (Koopman, Liouville or
     quantization) that is not on the record.
   - The "non-degenerate noise Q ≻ 0" premise was imported from a different layer. L0-1e even
     includes zero-temperature and rank-one-noise members.
4. **"Canonical" fails.** A second seedless, covariant, localized definition (compressing the
   operator systems themselves, Γ′) disagrees with Γ and can *add* edges. So "exclusion, never
   inclusion" is a property of the chosen definition, **not a physical prediction.**
5. **What is new and proved:**
   - **Theorem S** gives a sufficient condition for edge removal.
   - **L3′:** for generic H, Γ(ρ) = Γ for **every** ρ, including states that miss eigenvectors.
     This is theorem-grade at d = 4 and 8 (analytic zero-set argument plus witnesses) and only
     plausible for general d.

   L3′ is the actual content behind "non-triviality needs non-generic H".

## §1 Per-lemma verdicts

| Lemma | Verdict | Grade | Key reason |
|---|---|---|---|
| **L1** reach projector | **VERIFIED** | theorem (spectral theorem; Krylov/cyclic subspace, IMPORTED-STANDARD) | Holds with degenerate H (spectral form vs Krylov 2.6e-15). P_ρ depends only on supp ρ. C-6's covariance also needs the net to transform. |
| **L2** full rank ⇒ P_ρ = 𝟙; Gibbs states are full rank | **VERIFIED** | identity | — |
| **L2** primitive dissipative analogue | **VERIFIED-WITH-NARROWER-SCOPE** | IMPORTED-STANDARD (primitive quantum Markov semigroups) | L1 defines reach only for unitary dynamics. A semigroup reach is never defined. |
| **L2** "the declared L0 substrate … has a unique full-support stationary state" | **NOT ESTABLISHED; category error** | unsupported strengthening (imported assumption) | §0 item 3. For L0-1e members, full support holds iff (K,B) is controllable (Kalman, standard). Q ≻ 0 suffices; rank-deficient members were not checked (that would be a member evaluation). |
| **L3** generic pure collapse | **VERIFIED as stated**; "generic" undefined | theorem | "Generic" = outside a closed, Lebesgue-null real-algebraic set in Herm(ℋ) × ℋ. It needs one non-degenerate witness in a local family, and it **fails in symmetric families**. |
| **L3′** (new) Γ(ρ) = Γ for all ρ, for generic H | **VERIFIED at d = 4, 8 (witnessed); NOT ESTABLISHED for general d** | theorem at fixed d | The edge survives over all 2^d − 2 eigen-subsets, for random Herm(4), Herm(8) and 2-local 3-qubit chains (minimum strengths 0.65 / 1.17 / 0.99). |
| **L4** Γ(ρ) ⊆ Γ | **VERIFIED** | identity | A zero commutator compresses to zero. |
| **L4** compression is CP; the image is an operator system | **VERIFIED**, one imprecision | identity | Commuting with 𝒜_x is the condition for the compression to be *multiplicative*, not for the image to be an algebra (at rank 1, P𝒜_xP = ℂP is an algebra). |
| **L4** "exclusion, never inclusion" as an inherited prediction | **COUNTEREXAMPLE** | unsupported strengthening | (i) The alternative seedless definition Γ′ adds an x–z edge (strength 3.25) absent from Γ. (ii) State-to-state it is not monotone: moving from a frozen sector to a faithful state *adds* an edge (0 → 11.3). |
| **L5** {ρ}′ for non-degenerate ρ | **VERIFIED** (full rank not needed) | theorem | — |
| **L5** {e^{−βH}}′ = {H}′ | **VERIFIED, broader than stated** | theorem | Holds for **all** H and β ≠ 0 (injectivity of e^{−βλ}). The non-degeneracy qualifier is unnecessary (degenerate check: dim 16 = 16). |
| **C-5 row:** "{ρ}′ ∩ 𝒜_x = ℂ𝟙 for entangled faithful ρ" | **COUNTEREXAMPLE** | unsupported strengthening | ρ = ρ_xs ⊗ 𝟙_y/2 is full rank (min eigenvalue 0.025) and entangled (PT min eigenvalue −0.35), yet {ρ}′ ⊇ 𝒜_y. It needs "generic". |
| **L6** quadratic response | **IMPORTED-STANDARD; VERIFIED for linear fields only** | standard | Nonlinear probes are state-dependent (e.g. [q(t)², q²] is operator-valued). **Misapplied:** §0.2, §7 and §8 cite L6 for **C-6's** triviality, but C-6 uses all of 𝒜_x, and the bosonic class is infinite-dimensional, outside L1. |
| **L7** | split; see §2 | mixed | — |
| **L8** P-1 criteria are functions of V | **VERIFIED** | reading of frozen definitions | C1 via V_SE and Ω_E; C2 via the model's ground state (fixed, not free); C3 via G(t) at the declared t* = 2.0 (exact). Side note: §5(2)'s "all three single out a decoupled block" needs a convention, since C1 = 0/0 and C3 divides by zero. |

## §2 L7, taken apart (the owner's highest priority)

| # | Statement | Verdict |
|---|---|---|
| (1) | P_ρ ≠ 𝟙 requires support in a proper invariant subspace | **VERIFIED** (tautology: P_ρ *is* the smallest one). **Not sufficient** for Γ(ρ) ≠ Γ (L3′). |
| (2) | The edge is removed iff every compressed double commutator vanishes | **VERIFIED (the definition).** Two exact reformulations, both theorems below. |
| (3) | This implies exact invariant structure in the generator | **Vacuous as a condition on H.** Every H in dimension ≥ 2 has proper invariant subspaces. Non-vacuous replacement: H lies in the exceptional null set of L3′, proved only at d = 4, 8. |
| (4) | That structure is "aligned with a local configuration" | **NOT ESTABLISHED as necessary.** See below. |
| (5) | The x–y coupling "acts trivially" in the sector | **FALSE in both directions.** See below. |

**The two exact reformulations of (2):**
- **(2a) Expectation form.** x ≁_ρ y ⟺ ⟨φ|[A,[H,B]]|φ⟩ = 0 for all φ ∈ 𝒦(ρ), A ∈ 𝒜_x,
  B ∈ 𝒜_y. So **Γ(ρ) is the union, over pure states in the sector, of their short-time x–y
  response graphs** (i⟨[A,[H,B]]⟩ = d/dt ⟨[A,B(t)]⟩ at t = 0).
- **(2b) Dual form.** x ≁_ρ y ⟺ Tr_{ȳ}[H,[A,M]] = 0 for all A ∈ 𝒜_x and M ∈ P𝔅(ℋ)P.

**Why (4) is not necessary:**
- 3-qubit configuration sectors (exhaustive): of the 206 sectors that admit edge removal with a
  non-zero x–y coupling, **158 fix neither x nor y.**
- Removal occurs with **no site frozen** at ranks 2–6 of 8. Example: a rank-6 blockade-type
  sector (excluding x = 1 ∧ s = 1). There the admissible H form a 19-dimensional space, the
  sector dynamics is connected, the compressed coupling is non-scalar (norm 4.6), and the edge is
  removed to 1e-14.
- Removal also occurs at rank 1 for an entangled eigenvector.
- What remains is evidence, not proof: for *random* subspaces of rank ≥ 2, only h_xy = 0 is
  admissible. So *some* special structure is needed, but "local configuration of x or y" is not
  the right characterization.

**Why (5) fails in both directions:**
- **Not necessary.**
  - Example A: H = Z_xZ_y + 0.7X_y + 0.4X_yX_s + 0.3Z_s in the sector Z_x = +1 (rank 4 of 8).
    The edge is removed (0.0), yet P h_xy P = P Z_y P is **non-scalar**.
  - Example F: H = Z_x(Z_y + X_y) + Z_xX_s + Y_yY_s. The edge is removed, and the compressed
    coupling is non-scalar with non-commuting parts.
- **Not sufficient.**
  - Example B: H = Z_xZ_y with the sector span{|00⟩,|11⟩}. The coupling is the scalar +1 on the
    sector, yet the **edge survives** (5.66; hand check: [X_x,[H,X_y]] = 4Y_xY_y and
    ⟨11|YY|00⟩ = −1).
  - Example D: hopping in the N = 0 sector. P h_xy P = 0, yet the edge survives (4.0).
- **Mechanism:** P[A,[H,B]]P contains terms of the form PAP⊥HP⊥BP. Γ(ρ) depends on H
  **outside** 𝒦(ρ).

**Theorem S (new; proved by the verifier, checked by the operator).**
- **Hypotheses:** Q_x is a local projector with [H, Q_x⊗𝟙] = 0, and supp ρ ⊆ Q_x⊗𝟙. Let
  P = Q_x⊗𝟙.
- **Then:** P commutes with H and with every B ∈ 𝒜_y, so
  P[A,[H,B]]P = [PAP, P[H,B]P].
- **Consequence:** if rank Q_x = 1, then PAP = aP and **the x–y edge is removed for every y.**
  More generally, when P = Q_x⊗𝟙 exactly, removal holds iff Q_xHQ_x has no joint (Q_x-block)–y
  part.

**Degenerate-regime caveat (the document's L7 caveat).**
- "Small rank ⇒ numbers" is imprecise. The operator content at x is dim P𝒜_xP, which is set by
  *alignment*, not by rank. Example A has rank 4, yet P𝒜_xP = ℂP.
- By (2a), Γ(ρ) is a family of expectation-value readouts **at every rank**. The line between
  "(a)-type at rank 1" and "(c)-type for extensive sectors" is **a matter of degree, not a proved
  dichotomy.**

**Tightest proved statements:**
- **Necessary:** P_ρ ≠ 𝟙, and (at d = 4, 8) H non-generic.
- **Sufficient:** Theorem S.
- **Exact:** only (2a)/(2b). No structural iff is proved.

## §3 The conclusions of EA-0, audited

| Claim | Verdict |
|---|---|
| §0.1: C-6 exists, seedless (given the net), parameter-free | **VERIFIED** |
| §0.1: "canonical" | **COUNTEREXAMPLE** (Γ vs Γ′) |
| §0.2: trivial for faithful and Gibbs states | **VERIFIED** |
| §0.2: trivial on the "declared L0 substrate" | **NOT ESTABLISHED.** C-6 is undefined on the classical earned substrate, whose deterministic asymptotic state is δ₀. |
| §0.2: trivial for generic pure states | **VERIFIED-WITH-NARROWER-SCOPE** (define "generic"); strengthened by L3′ |
| §0.2: trivial for quadratic-class response | **VERIFIED for linear response only; not a statement about C-6** |
| §0.3 / §8: "non-trivial exactly when/iff exact local invariant structure with extensive, configuration-dependent sectors" | **NOT ESTABLISHED.** Sufficiency fails (B, D). Necessity of alignment and of extensivity fails (S4, S6, S7, rank 1). |
| §7: C-6 TRIVIAL/IDENTITY on earned classes | **VERIFIED-WITH-NARROWER-SCOPE:** faithful states (any quantum class) and generic quantum H. **UNFORMULABLE-YET on the classical L0 substrate.** |
| §7: C-6 FORMULABLE on constrained classes | **VERIFIED as existence** (Theorem S; examples A, F, S7). The characterization is not proved. |
| §8: "EA-0 already settles EA-1's question structurally" | **NOT ESTABLISHED.** "Only if supp ρ moves between invariant subspaces" is a tautology, since Γ(ρ) depends only on 𝒦(ρ). "If" is false: moving between number sectors keeps hopping edges. It also says nothing about other (c)-type definitions (Γ′). |
| §9.1: "only through support relative to invariant subspaces, or {ρ}′" | **NOT ESTABLISHED (heuristic).** Competitors: ρ's eigenspaces and modular flow; supports of local marginals. |
| §9.3–4: "non-trivial ⇒ generator-carried" | **VERIFIED only as an identity for reach-based constructions** (𝒦(ρ) is H-invariant by construction). Not a finding about endogenous access in general. |

## §4 Terminal recommendation (verifier)

> **TRIVIAL/IDENTITY ON EARNED SCOPE + CONDITIONAL FORMULABLE BRANCH**, where:
> - TRIVIAL/IDENTITY rests on (i) faithful states in any finite-dimensional quantum class and
>   (ii) generic quantum generators (L3′: proved at d = 4, 8, asserted beyond);
> - **on the classical earned L0 substrate, C-6 is UNFORMULABLE-YET**, not TRIVIAL;
> - the conditional FORMULABLE branch exists (Theorem S), is generator-carried by identity, and
>   has no proved characterization.

**Why not CLASS-SPLIT:**
- the non-trivial branch was asserted through an "iff" that is false in both directions;
- it is not stated within a declared class at theorem strength;
- "canonical" fails.

**What would earn CLASS-SPLIT:** an additive theorem that declares the class "H with a local
conserved projector Q_x⊗𝟙" and adopts Theorem S. Even then, the branch would remain
generator-carried by identity.

## §5 Proposed additive corrections to EA-0 (NOT applied; for owner acceptance)

1. **L2.** Replace the L0 sentence with:

   > "The earned L0-1a/b/c substrate is classical and deterministic (ẋ = −Kx; its asymptotic
   > state is δ₀). C-6, P_ρ and Γ are undefined on it without a lift not on the record. For
   > L0-1e members, the Gaussian stationary law has full support iff (K,B) is controllable
   > (Kalman; standard); this holds for Q ≻ 0 and is unverified for rank-deficient members."

2. **L3.** Define "generic" (the null-set formulation; the local-family witness condition; false
   in symmetric families). Add **L3′** at d = 4, 8 (witnessed).
3. **L4.** Add: "the compression is multiplicative iff P ∈ 𝒜_x′". Replace "exclusion, never
   inclusion" with:

   > "Γ(ρ) ⊆ Γ, and Γ is monotone in P_ρ. This is a property of this definition. It is not a
   > physical prediction and not state-to-state monotone; alternative compressed definitions can
   > add edges."

4. **L5.** "{e^{−βH}}′ = {H}′ for all H and all β ≠ 0". In the C-5 row, replace "entangled
   faithful ρ" with "generic faithful ρ".
5. **L6 and its uses.**

   > "L6 bears on (a)-type response data only. It does not establish triviality of C-6 in the
   > quadratic class, which lies outside L1's finite-dimensional scope."

6. **L7.** Replace the mechanism sentence with:

   > "Edge removal ⟺ ⟨φ|[A,[H,B]]|φ⟩ = 0 for all φ ∈ 𝒦(ρ), A, B. This depends on H outside
   > 𝒦(ρ). Sufficient: Theorem S. Coupling-triviality on the sector is neither necessary nor
   > sufficient. Local alignment is not necessary. 'Extensive sectors' is an interpretive
   > restriction."

   Retire the (3)–(5) mechanism language.
7. **§0.1:** delete "canonical". **§0.3 and §8:** replace "iff" with:

   > "can be non-trivial when H has exact local invariant structure (Theorem S); no
   > characterization is proved".

   **§8, the EA-1 paragraph:** replace "settles … structurally" with:

   > "settles it for Γ(ρ) as defined, largely by construction".

8. **§9.4.**

   > "generator-carried *for every reach-based construction, by identity*; not shown for
   > (c)-type constructions in general."

**Operator comment on what survives.** The owner's reading, "the state can select among
structural sectors, but the generator has to provide those sectors first", survives, **but only
as an identity for reach-based constructions.** It is not a theorem about endogenous access in
general: Γ′ and §9.1's competitors are unexamined routes. So the migration to S-5 is
**motivated, not forced**, by EA-0 as verified.

## §6 Reproducibility

- **Scripts:** archived as `calc/feasibility/ea0_verify/` (common.py and s1–s9; abstract qubit
  toys; each file headed as such).
- **Operator re-run** of s2, s8 and s9. The values reproduced:
  - A: edge 0.0, ‖P h_xy P − scalar‖ = 2.0;
  - B: 5.657;
  - D (N = 0): 4.0;
  - F: 0.0;
  - Γ′ x–z edge: 3.2507;
  - faithful-state edge: 11.314;
  - {H}′ = {e^{−βH}}′ at dimension 16;
  - entangled faithful counterexample: min eigenvalue 0.025, PT −0.35.
- s1 and s3–s7 were archived as run by the verifier and were not re-run by the operator.

**HARD STOP.** EA-0's terminal is the owner's to assign. EA-1 remains **NOT AUTHORIZED.**
