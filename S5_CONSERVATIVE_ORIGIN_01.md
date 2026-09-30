# S5-1 — CONSERVATIVE-ORIGIN / MARKOVIAN-LIMIT GATE (charter draft; formulation only)

**STATUS: DRAFT FOR OWNER REVIEW. NOT FROZEN. NOTHING DERIVED OR COMPUTED.**
- **Authority:** `S5_OWNER_RULING_01.md` §9 (Issue #2 comment `5904042956`): "charter/formulation
  gate first … No physics run yet; no v4 exception in this ruling … HARD STOP for owner review before
  any new derivation/run."
- **Date:** 2026-09-30 · **Branch:** `master-w25bu9`.

**Disclosure of prior expectations (not results, not assumed).** From the O-6 record and standard
open-system theory, the auditor expects:
- finite N: recurrence blocks any strictly dissipative exact generator;
- N = ∞: band-edge algebraic tails;
- a weak-coupling (van Hove) limit may give a Markov semigroup of **damped-oscillator
  (phase-space) type rather than the Level-0 first-order G-D type**.

The grades and outcomes below are written so that none of these expectations decides the result by
wording. §8 carries an outcome specifically for the last case.

## §0 Question (ruling §9, verbatim)

> Can the already-declared O-6 / pinned-chain conservative parent produce the Level-0 first-order
> Markov generator, or its retained kernel class, as a controlled reduction/scaling limit without
> inserting friction, white noise, or a Markov law by hand?

## §1 Parent (fixed; record definitions only)

- **𝒦_N:** q̈ = −K_N q, the O-6 pinned chain (`L0_1G_CHARTER_01.md` §1).
  - K_N is N × N tridiagonal, with diagonal 2.3 (sites 1 … N−1), 1.3 (site N), and off-diagonal −1.
  - **K₂₃ = K_b**, the sealed Level-0 bath block.
  - Closed form: λ_k = 2.3 − 2cos((2k−1)π/(2N+1)), v_k(i) ∝ sin((2k−1)iπ/(2N+1)).
  - Phase space z = (q, p) ∈ ℝ^{2N}, with ż = Az, A = [[0, I], [−K_N, 0]], and
    H = ½|p|² + ½qᵀK_N q conserved.
- **Split (O-6):**
  - retained system: site 1, with K₁₁ = 2.3;
  - coupling: g = −K₁₂ = 1;
  - bath: sites 2 … N, with K_BB of the same structure at size N − 1.
- **N sequence:** the declared {23, 47, 95} and the N → ∞ limit.
- **Initial classes (O-6, record):**
  - **C₀:** bath at rest, z₁(0) arbitrary. This gives the deterministic reduced map.
  - **Gibbs product:** the declared "past hypothesis". Fluctuations are report-only, §7.
- **Nothing added (NI checklist, audited in §9):** no friction coefficient, Langevin noise, external
  reservoir, Lindblad operator, chemical potential, or phenomenological exponential kernel.

## §2 The Level-0 target (fixed; record definitions only)

- **Generator:** ẋ = −Kx, the first-order dissipative convention (`L0_1C_CHARTER_01.md:70-75`),
  on the same K.
- **Retained kernel:** k_D(τ) = e₁ᵀe^{−K_bτ}e₁ (`L0_1C_CHARTER_01.md:70-72`;
  `L0_1F_DORD_THEOREM_01.md` §1), with K_b = K₂₃.

**Target membership levels (frozen):**

| Level | Name | Definition |
|---|---|---|
| **M-1** | MARKOV | The reduced map is a semigroup, Φ(t+s) = Φ(t)Φ(s) for all t, s ≥ 0 (equivalently Φ(t) = e^{−Mt} with M fixed), **and strictly dissipative**: every eigenvalue of M has Re > 0. |
| **M-2** | G-D-PROPER | M-1, **and** the retained law is of Level-0 first-order type: M has real non-negative spectrum and the retained response is completely monotone (the G-D reading; Bernstein). Equivalently, a first-order law on the retained position alone. |
| **K-L0** | Kernel class | The parent's retained **memory kernel** (from eliminating the bath) is in the Level-0 kernel class: pole-only / exponential-grade and CM, like k_D. |

**Equivalence:** SC5-1 applies. A positive clock rescaling c𝒜 (c > 0) is quotiented. Sign flips,
f(K), noise and phase-space doubling are not.

## §3 Retained variables and reduced objects (frozen)

**Retained variable sets:**
- **R1 (primary):** z₁ = (q₁, p₁), the O-6 split.
  - The reduced map on C₀ is Φ_N(t) := the (z₁, z₁) 2 × 2 block of e^{At}.
- **R2 (Level-0-like scalar):** q₁ alone, on the class C₀′ = C₀ ∩ {p₁(0) = 0}.
  - The reduced map is φ_N(t) := e₁ᵀcos(√K_N t)e₁.

**Memory kernel (bath elimination; record-form GLE):**
- Γ_N(t) := g²·e₁ᵀcos(√K_BB t)K_BB⁻¹e₁, the friction-kernel form for site 1.
- It is to be **compared with the Level-0 k_D on the same bath block structure.**
- Whether the derivation instead produces the propagator form g²·e₁ᵀK_BB^{−1/2}sin(√K_BB t)e₁ must be
  stated in the derivation. Both are functionals of the one bath spectral measure μ_B at e₁.

## §4 Grades (ruling §9.2)

- **T-A, exact generator.**
  - At a declared N (finite, or N = ∞ as a defined limit object): does Φ_N (R1) or φ_N (R2) equal
    e^{−Mt} for all t ≥ 0, with M determined by the parent, at level M-1 / M-2?
  - Does Γ_N meet K-L0?
- **T-B, controlled Markov limit.** In an **admitted** limit (§5), does the reduced map converge
  under the frozen norm/window (§6) to e^{−Mt}, with M **determined by the limit** (not fitted), at
  level M-1 / M-2?
- **T-C, non-Markovian-only.** The parent produces retained decay (Φ → 0 in some admitted limit),
  but with an irreducible memory kernel, branch cut or algebraic tail. Record it as:

  > **effective dissipation emerges, but the Level-0 Markov generator does not.**

## §5 Scaling limits (frozen before evaluation; from existing parent parameters only)

| Tag | Limit | Parent parameters used | Status |
|---|---|---|---|
| **L-N** | N → ∞ at fixed (K₁₁, g, pin, springs) | N (declared sequence) | **ADMITTED** (native; O-6) |
| **L-vH** | Weak coupling (van Hove): g = −K₁₂ → 0 with **K₁₁ held at 2.3** (the O-6 split lists K₁₁ and g as separate entries) and **N = ∞ taken first**; rescaled time τ = g²t fixed; interaction frame with respect to the isolated system flow e^{A₀t}, A₀ = [[0, 1], [−K₁₁, 0]] (an exact frame change, not an added term) | g | **ADMITTED, subject to OR-A.** K_N stays positive definite for 0 < g ≤ 1 by diagonal dominance, which must be checked. Whether the system frequency √K₁₁ lies inside the bath band is **derived, not assumed.** |
| L-WB | Wide-band / flat spectral density (bath band → ∞ with the coupled rate fixed) | would scale the bath spring stiffness (unit springs) and g jointly | **NAMED, NOT ADMITTED.** It is singular; its parent-consistency needs an owner ruling (OR-A). |
| L-OD | Overdamped / Smoluchowski (friction ≫ system frequency, then adiabatic elimination of p₁) | would need a mass or stiffness scale not present (unit masses) | **NAMED, NOT ADMITTED** (OR-A) |

A limit not in the ADMITTED rows can be reported as the **required ingredient** (§8). It cannot be
consumed to claim a derivation.

## §6 Frozen norm and window for T-B

- **Norm:** the operator 2-norm on R1 (|·| on R2).
- **L-vH criterion:**

  lim_{g→0} sup_{τ∈[0,τ_max]} ‖e^{−A₀τ/g²}Φ_{∞,g}(τ/g²) − e^{−Γτ}‖ = 0 for **every** fixed τ_max,

  with Γ obtained from the limit (a Fermi-golden-rule-type expression in the parent's bath spectral
  measure). This is compact-uniform convergence in rescaled time.
  - The **lab-frame limit generator** is M = −A₀ + Γ.
  - Its membership level (M-1 / M-2) is read **in the lab frame.** The frame change is not allowed
    to hide the system oscillation.
- **L-N:** T-A at N = ∞, meaning exact equality for all t ≥ 0. No window is involved.
- **A good exponential fit on a finite window is NOT a T-B result** (ruling §9.5).

## §7 Mandatory analytic no-go attack (before any numerics; ruling §9.3)

The following statements are to be **proved or killed at the exact scope of 𝒦_N.** None is assumed.
Each needs a written proof, or a counterexample within the parent.

- **NG-A1 (finite N).** Φ_N(t) and φ_N(t) are almost-periodic (finite sums of cos/sin(ω_k t)) and do
  not tend to 0. No M-1 semigroup (which decays strictly) can equal them.
  - Also to settle: the only exact first-order generator of the full parent on the full phase space
    is the conservative A itself, which is G-W in first-order form and is not dissipative.
  - **Consume:** O-6 I-1 (orbit recurrence) and T_rec(N).
- **NG-A2 (N = ∞).** Four parts:
  1. Determine the retained spectral measure μ₁ of K_∞ at e₁: its absolutely continuous part on
     [0.3, 4.3], its band-edge exponents, and **whether any bound state lies outside the band**. A
     bound state would give an undamped component, so Φ_∞ would not tend to 0.
  2. If μ₁ is purely a.c. with power-law edges, show that Φ_∞ decays **algebraically** and that its
     Laplace transform has **branch points** at the band edges. It is then not rational and cannot
     equal e₁ᵀe^{−Mt}e₁ for any finite M.
  3. **Consume** O-6 D-1 (band-edge t⁻³ sign-alternating ripples in current and entropy derivative
     at N = ∞) and the O-6 infinite-chain algebraic memory. Do not rediscover them.
  4. **Scope fence:** do not generalize to all unitary dilations. The lift work shows abstract
     unitary dilations of contraction semigroups exist (Sz.-Nagy). The claim is only about **the
     declared local 𝒦_N.**
- **NG-A3 (kernel class).** Decide whether Γ_N (and Γ_∞) can be CM / pole-only at any declared N.
  The oscillatory cos(√λ t) structure versus the Level-0 CM e^{−λτ} reading of the same kind of
  spectral measure is the point at issue.
- **NG-A4 (van Hove, if L-vH is admitted).** Derive the limit generator and its membership level.
  In particular, decide whether the lab-frame M has complex spectrum (damped oscillation, which is
  M-1 but not M-2) or real spectrum (M-2).
- **Numerics** (only after an owner authorization naming them): finite-N closed-form checks of the
  analytic statements. Never a replacement for them.

## §8 Outcomes and determination rule (frozen at freeze; proposed here)

The ruling §9.5 minimum set, plus one auditor-proposed outcome (marked †) for owner acceptance.

The first matching item decides:

1. **UNFORMULABLE:** the reduced objects of §3 cannot be defined on the declared classes without
   adding structure.
2. **EXACT-GENERATOR-DERIVED:** T-A holds at level **M-2** (R1 or R2) at a declared N or at N = ∞.
   K-L0 is reported alongside.
3. **MARKOV-LIMIT-DERIVED:** T-B holds at level **M-2** in an ADMITTED limit.
4. **† MARKOV-LIMIT-OTHER-CLASS:** T-B holds at level **M-1 but not M-2** in an ADMITTED limit.
   - Meaning: the parent derives *a* Markov generator, but **not the Level-0 G-D kind** (for
     example an underdamped phase-space semigroup).
   - The required further ingredient for G-D must be named.
5. **REQUIRES-SINGULAR/NEW-PARENT:** items 2–4 fail, **and** the analysis shows that level M-2 is
   reachable only through a **NOT-ADMITTED** limit (L-WB, L-OD) or through bath structure absent from
   𝒦_N. The ingredient must be named.
6. **NONMARKOVIAN-DISSIPATION-ONLY:** items 2–5 fail, **and** retained decay is proven in an
   ADMITTED limit with irreducible memory (T-C). The field "required ingredient" is filled if it is
   identified, else "unidentified".
7. **UNDERDETERMINED:** the analysis cannot settle the grade at the declared scope, or R1 and R2
   give conflicting answers that the rules above do not order.

**Fences:**
- A finite-window exponential fit never counts.
- An abstract dilation outside 𝒦_N never counts.
- No imported selector (least action, maximum entropy, …).

## §9 No-insertion audit (NI; applied to every derivation step)

**Each step must declare that it introduces none of the following:**
- a friction coefficient not computed from the parent;
- a noise term not generated by the parent's declared initial ensemble;
- a Markov assumption (for example a Born–Markov truncation without the limit that justifies it);
- a reservoir or Lindblad operator;
- a chemical potential;
- an exponential kernel ansatz;
- a change of K entries other than the admitted limit parameter.

**A violation voids the step.**

## §10 Scope limits (carried into any result)

- **SL-1.** The O-6 split retains **one site.** A positive result derives a first-order Markov law
  **for the retained site's reduced dynamics.** It does **not** by itself derive the Level-0
  multi-site generator ẋ = −Kx on the whole net. Each Level-0 site would need its own reduction, and
  the parent's "bath" of site i is the rest of the same chain. Any full-net claim needs a separate
  argument.
- **SL-2.** Fluctuations: whether the Gibbs-bath force becomes white in the admitted limit is
  **report-only.** It bears on G-OU, not on the deterministic G-D target.
- **SL-3.** Even a positive result is **conditional on the conservative parent and the admitted
  limit** (ruling §9.6). It does not make the generator unconditionally derived.

## §11 Open items for owner review (before freezing)

- **OR-A. Admitted limits.**
  - Is L-vH admitted as defined: g → 0 at fixed K₁₁ = 2.3, N = ∞ first, in the interaction frame
    with a lab-frame membership reading?
  - Should L-WB or L-OD be admitted, or left as named "required ingredients" only?
- **OR-B. Execution mode.**
  - S5-1 is primarily an **analytic derivation** (§7).
  - Does its execution need the campaign-specific v4 exception, as a physics run would?
  - Are numerical cross-checks allowed, and on which members?
- **OR-C. Outcome †.** Accept MARKOV-LIMIT-OTHER-CLASS as a frozen outcome, or fold it into
  REQUIRES-SINGULAR/NEW-PARENT.
- **OR-D. R2 class.** Accept C₀′ (p₁(0) = 0) as the admissible class for the scalar reading.
- **OR-E. Kernel form.** Friction-kernel versus propagator form for Γ (§3). Both are to be reported;
  confirm which one K-L0 is read on.

**HARD STOP.** No derivation or computation until the owner reviews and freezes this charter.
