# S5-1 — CONSERVATIVE-ORIGIN / MARKOVIAN-LIMIT GATE (charter)

**STATUS: FROZEN FOR EXECUTION** (amended per `S5_OWNER_RULING_02.md`, Issue #2 comment
`5904251680`).
- **The frozen commit is the commit that introduces this revision.** CURRENT_STATE records its hash
  as the **frozen S5-1 charter.**
- **ONE S5-1 analytic physics execution is authorized**, with a campaign-specific post-v4 exception
  for S5-1 only.
- **Draft history:** the draft is at `4761f6c`, and the amendment log is §12.
- **Date:** 2026-09-30 · **Branch:** `master-w25bu9`.

**Disclosures:**
- *Prior expectation (draft, carried).* A weak-coupling limit may give a damped-oscillator Markov law
  rather than the Level-0 G-D law.
- *Planning note (new, honest).* In preparing this freeze, the auditor sketched the standard
  structure of the problem mentally, **without computing any member**:
  - the retained resolvent is a Schur complement;
  - the uniform semi-infinite tridiagonal has a semicircle-type spectral measure;
  - weak coupling gives a resonance.

  This sketch is not the derivation, and **no gate or window below was tuned to it.** The
  cross-check g-values and windows are fixed by rule (§7), not by a computed rate.

## §0 Question (ruling S5-01 §9, verbatim)

> Can the already-declared O-6 / pinned-chain conservative parent produce the Level-0 first-order
> Markov generator, or its retained kernel class, as a controlled reduction/scaling limit without
> inserting friction, white noise, or a Markov law by hand?

## §1 Parent (fixed; record definitions)

- **𝒦_N:** q̈ = −K_N q (`L0_1G_CHARTER_01.md` §1).
  - K_N is N × N tridiagonal, with diagonal 2.3 (sites 1 … N−1), 1.3 (site N), and off-diagonal −1.
  - K₂₃ = K_b.
  - λ_k = 2.3 − 2cos((2k−1)π/(2N+1)) and v_k(i) ∝ sin((2k−1)iπ/(2N+1)).
  - z = (q, p), ż = Az, A = [[0, I], [−K_N, 0]], with H = ½|p|² + ½qᵀK_N q conserved.
- **Split:**
  - retained system: site 1, with K₁₁ = 2.3;
  - coupling: g = −K₁₂;
  - bath: sites 2 … N.
- **The isolated system generator:** A₀ = [[0, 1], [−K₁₁, 0]].
- **N:** {23, 47, 95} and N → ∞.
- **Initial class C₀:** the bath at rest. The Gibbs product is report-only.
- **Nothing added** (NI, §9).

## §2 Admitted limits (OR-A ruled)

| Tag | Definition | Status |
|---|---|---|
| **L-N** | N → ∞ at fixed declared local parameters (g = 1) | **ADMITTED** (primary; parent-preserving) |
| **L-vH** | **The K(g) family:** K₁₁ = 2.3 fixed; K_BB fixed; only K₁₂ = K₂₁ = −g varies, 0 < g ≤ 1; every other entry fixed. Take N → ∞ first, then g → 0 with τ = g²t fixed. | **ADMITTED as a controlled deformation of the declared parent class, not an already-evaluated O-6 member.** Results are labelled **conditional on the weak-coupling deformation.** **Positive definiteness of the whole family must be proved before use.** |
| L-WB | wide-band / flat spectral density | **NOT ADMITTED**: a named missing ingredient only |
| L-OD | overdamped / Smoluchowski | **NOT ADMITTED**: a named missing ingredient only |

## §3 Retained objects

- **R1 (primary):** Φ_N(t) := the (z₁, z₁) 2 × 2 block of e^{At} on C₀, in the physical variables
  (q₁, p₁).
- **R2 (scalar response preparation):** φ_N(t) := e₁ᵀcos(√K_N t)e₁, from q₁(0) = 1, p₁(0) = 0 and the
  bath at rest.
  - **C₀′ is not an invariant one-dimensional state space**, because the parent generates
    p₁(t) ≠ 0.
  - R2 adjudicates the **retained response/kernel class.**
  - R2 supports M-2 **only if closure/restartability is proved in the claimed limit.** That means
    either a proven slaving relation eliminating p₁, or a directly proven scalar semigroup with
    restartability that does not depend on hidden momentum or history.
- **Short-time control (to be proved formally):** φ_N(0) = 1, φ_N′(0) = 0, φ_N″(0) = −K₁₁.
- **Retained-response comparison with the Level-0 object k_D(t) = e₁ᵀe^{−K_b t}e₁:**
  - Level-0's retained response is the same-site diagonal response, a scalar function of t with
    value 1 at t = 0.
  - The parent's comparable object is **φ_N** (the same-site diagonal, value 1 at t = 0, from a
    position preparation).
  - The R1 matrix Φ_N is used for the generator levels M-1/M-2.
- **Memory diagnostic (categorically separate; never identified with k_D):** the exact GLE friction
  kernel from eliminating the bath, expected in the form Γ_fric(t) = g²e₁ᵀK_BB⁻¹cos(√K_BB t)e₁ (with
  the exact form as derived), and optionally the sine/self-energy form.

## §4 Target levels (renamed per ruling §6)

| Level | Name | Definition |
|---|---|---|
| **M-1** | PHYSICAL MARKOV | A closed retained physical-variable map that is a time-homogeneous, **strictly dissipative** semigroup, exactly or as a controlled limit. |
| **M-2** | G-D-PROPER | M-1, plus an **autonomous first-order retained law**, real non-negative decay spectrum (up to the S5 clock-rescaling quotient, SC5-1), and a **CM scalar response** where applicable. |
| **K-L0** | RETAINED-KERNEL-CLASS | The parent's **retained response** (φ, not Γ_fric) lies in the Level-0 response-kernel class: CM (scalar), pole-only / rational Laplace transform at finite-dimensional G-D scope, and exponential-grade semigroup structure. |

## §5 Grades and the van Hove statement (corrected per ruling §1)

**T-A (exact).** At a declared N, or at N = ∞: is Φ (R1) exactly e^{−Mt}? Is φ in K-L0?

**T-B (controlled limit, L-vH).** The frozen primary statement:

  Ψ_g(τ) := e^{−A₀τ/g²} Φ_{∞,g}(τ/g²) → e^{Bτ}, **compact-uniformly on every finite τ-interval**,

with B **derived** from the parent spectral measure.

- **Then, separately, reconstruct the physical retained dynamics.** An interaction-picture Markov
  envelope counts toward MARKOV-LIMIT-OTHER-CLASS **only if** the derivation also yields a controlled,
  time-homogeneous, damped-oscillator effective generator in the physical variables (equivalently
  A₀ + g²B_eff + ⋯ on kinetic times), with a stated error control.
- **The free oscillation may not be discarded** when assigning M-1 vs M-2.
- **An interaction-picture exponential by itself is not a Level-0 G-D derivation.**
- **There is no finite rescaled-time "lab-frame generator" −A₀ + Γ**; the draft §6 statement is
  withdrawn.

**T-C (non-Markovian-only).** Decay with irreducible memory, a branch cut or an algebraic tail gives:
*"effective dissipation emerges, but the Level-0 Markov generator does not."*

A good exponential fit on a finite window never counts.

## §6 Required analytic sequence (frozen order; ruling §8)

1. **Finite-N theorem.**
   - Recurrence / almost-periodicity of Φ_N and φ_N.
   - No exact strictly decaying semigroup.
   - The R2 short-time obstruction (φ_N″(0) = −K₁₁ versus e^{−γt}).
2. **Infinite-N spectral theorem.**
   - The exact or closed spectral measure of K_∞ at e₁, or a sufficient resolvent representation.
   - A **bound-state audit.**
   - Band-edge branch structure.
   - The long-time class of the retained response.
   - Consume O-6 D-1 and the infinite-chain algebraic memory.
   - Fenced from general unitary dilations.
3. **Kernel-class theorem.**
   - **Local CM tests**, not late tails alone: φ″(0), and Γ_fric″(0) with its exact normalization.
   - The pole/branch-cut distinction.
   - The exact GLE friction-kernel derivation, kept separate from k_D.
4. **Weak-coupling theorem.**
   - Prove the K(g) family is valid (positive definite for all 0 < g ≤ 1, and the N → ∞ object
     well defined).
   - Locate √K₁₁ relative to the bath spectrum.
   - Derive, or fail, the Ψ_g → e^{Bτ} semigroup.
   - Reconstruct the physical-variable effective dynamics.
   - Assign M-1/M-2 only in that sense, together with R2 closure.
5. **NI audit** (§9).
6. **Mechanical terminal** (§8).

The optional cross-checks (§7) run **only after steps 1–4.**

## §7 Numerical cross-checks (pre-frozen; non-adjudicating)

**Members:**
- N ∈ {23, 47, 95};
- K(g) at **g ∈ {1, 0.5, 0.25}** with N = 95.

The g-values are chosen by rule (halving from the O-6 value). No rate estimate was used.

**Window rule:** t ∈ [0, 0.9·T_rec(95)], with T_rec from the O-6 frozen formula
(T_rec(N) = 2(N−1)/v_max, where v_max is the maximum over k ∈ (0, π) of sin k/√(2.3 − 2cos k)). The
grid is t = 0.05·j.

**Norm:** the max-abs entry of Φ in the coordinates (q₁, p₁/√K₁₁).

| # | Check | Kind |
|---|---|---|
| X-1 | The closed-form spectra of K_N (g = 1) match `numpy.linalg.eigvalsh` (max \|Δλ\| < 10⁻¹²). The K(g) spectra are listed. | verify |
| X-2 | The derived bound-state statement, shadowed at finite N: every eigenvalue of K_95(g) (g ∈ {1, 0.5, 0.25}) lies in the derived band closure. The minimum eigenvalue is > 0. | report |
| X-3 | The short-time identities φ_N(0) = 1, φ_N′(0) = 0, φ_N″(0) = −K₁₁, evaluated as spectral moments Σ w_k λ_k^m (N ∈ {23, 47, 95}). | verify |
| X-4 | The derived N = ∞ asymptotic formula for φ_∞, compared with φ_95 on t ∈ [T_rec(95)/3, 0.9·T_rec(95)]. The maximum deviation is reported. | report |
| X-5 | The derived weak-coupling approximant, compared with Φ_{95,g} over the window, for g ∈ {0.5, 0.25}. The sup-deviation is reported for each g. | report |

**Not allowed:**
- fitting;
- choosing windows after seeing data;
- searching g;
- using numerics to settle a theorem claim.

A defect in a cross-check is preserved and stops the run before any re-run, unless the analytic
terminal is wholly independent of it (ruling §2).

## §8 Outcomes and determination rule (frozen; ruling §§3, 7)

The first matching item decides:

1. **UNFORMULABLE:** the §3 objects cannot be defined on the declared classes without adding
   structure.
2. **EXACT-GENERATOR-DERIVED:** T-A at **M-2** at a declared N or at N = ∞.
3. **MARKOV-LIMIT-DERIVED:** T-B in an ADMITTED limit at **M-2**, with a physical-variable
   reconstruction; R2 closure is required for a scalar claim.
4. **MARKOV-LIMIT-OTHER-CLASS:** an admitted limit derives a genuine **time-homogeneous Markov
   semigroup / effective generator for the retained physical variables** (M-1), with a controlled
   physical-variable reconstruction, **but its structural type is not the Level-0 first-order
   CM/real-spectrum G-D class** (not M-2). A rotating-frame envelope alone is not enough.
5. **REQUIRES-SINGULAR/NEW-PARENT:** fires **only if** the analysis **establishes** that M-2 requires
   a **specifically identified** non-admitted ingredient (wide-band, an overdamped/slaving scale, an
   altered spectral density, or other changed parent structure). It does not fire merely because L-N
   and L-vH fail.
6. **NONMARKOVIAN-DISSIPATION-ONLY:** the admitted parent yields only decay with memory, and the
   needed ingredient is not established.
7. **UNDERDETERMINED:** the analysis cannot settle the grade at the declared scope.

The terminal also reports K-L0 (on φ) and the memory diagnostic (Γ_fric), without identifying them.

## §9 No-insertion audit (NI)

Every derivation step must declare that it adds none of the following:
- a friction coefficient not computed from the parent;
- a noise term not generated by the declared ensemble;
- a Markov assumption, such as a Born–Markov truncation without the limit theorem that justifies it;
- a reservoir or Lindblad operator;
- a chemical potential;
- an exponential ansatz;
- any K-entry change other than g in L-vH.

**A violation voids the step.**

## §10 Scope limits (carried)

- **SL-1:** a positive result concerns **the retained site's reduced law**, not the Level-0
  multi-site net ẋ = −Kx.
- **SL-2:** fluctuation whiteness is report-only.
- **SL-3:** any result is conditional on the parent, **and on the weak-coupling deformation for
  L-vH.**

## §11 Owner rulings replacing the draft's open items (`S5_OWNER_RULING_02.md`)

- **OR-A:** admit L-N and L-vH only (L-vH as the frozen K(g) deformation). L-WB and L-OD are named
  missing ingredients.
- **OR-B:** analytic derivation is physics work, and one execution is authorized with the S5-1
  exception. Numerics are non-adjudicating, run after the analytics, on pre-frozen members.
- **OR-C:** MARKOV-LIMIT-OTHER-CLASS is a distinct frozen outcome.
- **OR-D:** R2 is a response preparation only. Closure/restartability is required for M-2, and the
  short-time control is added.
- **OR-E:** K-L0 is read on the retained response. The friction kernel is a separate diagnostic.
  The local CM attack is added.

## §12 Amendment log (draft `4761f6c` → frozen)

| # | Change | Source |
|---|---|---|
| AM-1 | L-vH redefined as the explicit K(g) family, admitted as a controlled deformation, conditional; positive-definiteness proof required. L-WB and L-OD set to NOT ADMITTED. | §1 |
| AM-2 | The draft §6 "lab-frame M = −A₀ + Γ" is withdrawn. Ψ_g → e^{Bτ} is frozen, followed by a separate physical reconstruction. An interaction-picture exponential is not G-D. | §1 |
| AM-3 | Execution needs the exception (granted). Numerics are non-adjudicating and run after the analytics. The g-set {1, 0.5, 0.25} at N = 95 and the window rule are frozen. | §2 |
| AM-4 | MARKOV-LIMIT-OTHER-CLASS is frozen with its binding meaning. | §3 |
| AM-5 | R2 is a response preparation, not an invariant state space. Closure/restartability is required. The short-time control is added. | §4 |
| AM-6 | K-L0 moves to the retained response φ. Γ_fric is a separate diagnostic. The local CM attack is added. | §5 |
| AM-7 | Target levels renamed: M-1 PHYSICAL MARKOV, M-2 G-D-PROPER, K-L0 RETAINED-KERNEL-CLASS. | §6 |
| AM-8 | Outcome item 5 tightened: it requires an established, specifically identified ingredient. | §7 |
| AM-9 | The analytic sequence is frozen in order. | §8 |

**Artifacts at execution:**
- `S5_CONSERVATIVE_ORIGIN_DERIVATION_01.md`, the analytic steps 1–5;
- `calc/s5_conservative_origin.py`, containing symbolic identity checks for the derivation and the
  §7 cross-checks, which run after the analytic document is written;
- `S5_CONSERVATIVE_ORIGIN_RESULT.json`;
- `S5_CONSERVATIVE_ORIGIN_VERDICT_01.md`.

Then **HARD STOP.**
