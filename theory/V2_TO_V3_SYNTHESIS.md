# GRUT V2 → V3 Synthesis — how we derived the V3 foundation

**Date:** June 2026 (2026-06-16)
**Scope:** everything since the last book update (v2.6). The output is a single conclusion —
*a foundation V3 can be built on* — plus the full record of how each step was earned and
adversarially survived. This document is the bridge; it does **not** build V3.

**Status of this document:** report. The foundation it describes is recorded on the backend
(`grut/foundation/organizing_structure.py`, registry claims `organizing_structure_v3` and
`adiabatic_dilatation_redundancy_nogo`, tests green) but **not yet built upon.**

---

## 0. The one-line result

> **GRUT is a theory of permissible vacuum response. Concretely: it is the
> adiabatic-dilatation-redundant (general-relativistic) limit, plus the controlled breaking of
> that redundancy by exactly one scale `L₀ = cτ₀ ≈ 12.85 Mpc`** — the same shape by which a mass
> breaks scale invariance.

Two pillars carry it — **Q** = CTP/in-in unitarity (*proven*), **F** = finite single-pole memory
(*postulated*). The adiabatic spatial-dilatation redundancy **D** is a *conjectured bridge whose
breaking term is established*: **F is the controlled breaking of D.** Everything else is either a
theorem these force, a named open frontier, or — for flavor — outside the scheme.

This is a foundation in the thermodynamics / GR sense: the organizing principle is **stable** and
the open questions are **precisely located**, not closed. That is what makes it buildable.

---

## 1. The method that produced it (why this is trustworthy)

The whole phase ran one discipline: **a result counts only if it survives adversarial attack, and
demoting our own claims is a feature, not a failure.** Four "clean" foundational claims were
*caught and corrected* by independent skeptic passes before anything was banked:

1. "general covariance forces the selection principle P" — **refuted** (`w8psedyng`).
2. the source-channel "high-pass rescue" reconciliation — **refuted** (`ww3jtq2t9`).
3. the §3.7 "high-pass operative theorem" — **false-positive, retracted**.
4. the first-pass dilatation arithmetic (`e^{-2λ}` on `k_phys`) — **corrected** (`w3g2yu2wc`).

The result that finally **survived** full verification (the dilatation theorem, §6 below) is a
*partly-negative* one. That is the signal: across cosmology, flavor, decoherence, and
source-coupling, **the claims that survive are constraints and honest no-gos, never rescues.**

---

## 2. What died, what survived (the boundary operator)

| Candidate | Verdict | Where |
|---|---|---|
| Linear dark-sector (μ→4/3) enhancement | **RULED OUT** (data 2.79×/32σ + consistency) | `CMB_ISW_EQUALITY_FILTER.md §0.1`, `PROJECTOR_CONSISTENCY_NOGO.md §5` |
| Horizon-filter (`k_eq`) cosmology | **RULED OUT** ("no physical basis") | `CMB_ISW_EQUALITY_FILTER.md §0.1` |
| Bare-density coupling | **NO-GO** (not separate-universe invariant) | `PROJECTOR_CONSISTENCY_NOGO.md §5` |
| Koide amplitude closure | **NO-GO** (impedance gives 4/9, not 2/3; Yukawa-input) | `KOIDE_AMPLITUDE_UNIFICATION.md` |
| "distinguishability" as DNA | **RELABELING** (a name for Q∩F∩D, not an axiom) | `GRUT_SELECTION_PRINCIPLE.md §3.6` |
| "covariance forces P" / high-pass rescue | **REFUTED / RETRACTED** | `GRUT_SELECTION_PRINCIPLE.md §3.7` |
| **CTP difference principle (Q)** | **SURVIVED** (proven leg) | `ctp_action_structure` |
| **Constitutive / finite-memory response (F)** | **SURVIVED** (postulated) | `memory_kernel_form` |
| **Separate-universe consistency / one conformal mode** | **SURVIVED** | `PROJECTOR_CONSISTENCY_NOGO.md`, `conformal_mode_scalar.py` |
| **`μ_linear = 1` (linear cosmology = ΛCDM)** | **DERIVED REQUIREMENT** | `PROJECTOR_CONSISTENCY_NOGO.md §5-§6` |

The dying entries are **mechanisms**; the surviving entries are **constraints**. Mature theories
(thermodynamics, GR, QM) all began as constraints. The no-gos are not roadblocks — they map the
shape of the allowed solution space.

---

## 3. The narrative arc (how we got here, since v2.6)

**A — The CMB-ISW reckoning (→ manuscript v2.7).** GRUT's linear refractive enhancement
over-produces the low-ℓ ISW: the quasi-static law gives 2.6× (~29σ); the *full* derived memory
kernel (run in MGCAMB) gives **2.79× (~32σ) — worse, not better**. The `k_eq` filter that seemed
to rescue it has no physical basis. Manuscript demoted σ₈/fσ₈/S₈/CMB-ISW from "certified," ruled
out falsifiers F5/F7, logged Correction #38.

**B — V7 self-containment.** Audited that v2 ("the phoenix") relies on no legacy V7 result; the one
real mislabel (rotation curves are *imported* MOND `ν(y)`, not GRUT-derived) was corrected.
(`V2_SELF_CONTAINMENT_AUDIT.md`.)

**C — Koide frontier.** Unified `K=2/3` and `θ=2/9` into one posit `A²=N−1`; then a fixed-point
**no-go**: GRUT's impedance gives `4/9`, the amplitude is Yukawa-input. Flavor is hosted.
(`KOIDE_AMPLITUDE_UNIFICATION.md`.)

**D — Terrain + origin reframe.** Built the selected/permitted/hosted/anchored map; established
GRUT = *one dimensionless axiom (α=1/3) + one scale (τ₀)*. Recognized the real target was not a
better Big-Bang story but a **selection principle**: why one conformal mode, why α=1/3, why the
conformal mode is the IR carrier. (`GRUT_TERRAIN.md`, `GRUT_ORIGIN_POINT.md`.)

**E — The selection principle and its load-bearing question.** Convergence audit (§3.6): of five
proposed routes to P, only CTP is independent; the rest are "the same idea wearing N hats," and
"distinguishability" is a re-description, not a derived quantity. This isolated the one question
worth attacking: *is the adiabatic rescaling a genuine redundancy of GRUT's bare action?*

**F — What GRUT actually derives.** Attacking that question forced the dual-front result: the
linear refractive enhancement is **ruled out** (data + consistency), and **`μ_linear = 1` is a
derived requirement** (the tracefree `P^TT` kernel annihilates linear scalars; conformal ⊥
separate-universe at k→0). The §3.7 "high-pass rescue" was a false-positive and was retracted.

**G — The organizing-structure audit.** With mechanisms dead and constraints standing, the
structure resolved into **two pillars (Q proven, F postulated) + one conjectured bridge (D)**, with
Koide outside the scheme. (`GRUT_V3_ORGANIZING_STRUCTURE.md`.)

**H — The catalyst: the dilatation theorem (§6).** The load-bearing question, answered and
independently verified.

---

## 4. The robust theorem (the thing V3 is anchored to)

**`μ_linear = 1` — linear cosmology IS ΛCDM, by derivation.** Forced two independent ways
(tracefree `P^TT` annihilates linear scalars; conformal response ⊥ separate-universe invariance at
k→0) *and* over-determined by data (the full kernel gives 2.79×/32σ, so any nonzero linear
enhancement is excluded). GRUT's dark sector therefore **cannot** live in the linear-scalar
channel; it must be nonlinear/tensor (C5a–c). This is the one place the framework makes a sharp,
non-negotiable, already-confirmed prediction — the right thing to build on.

---

## 5. Corrections logged this phase

- **#38** — linear modified-gravity enhancement ruled out by the low-ℓ ISW (2.6× / ~29σ; full
  kernel 2.79× / ~32σ).
- **#39** — the §3.7 "high-pass / covariance-forces-P" rescue retracted as a false-positive;
  replaced by the dual-front ruling-out and `μ_linear=1`.
- Provenance corrections: rotation-curve engine relabeled (imported MOND `ν(y)`); the
  `(H_eq τ₀)²` arithmetic error in the QS-validity domain; the `k_phys` exponent
  (`e^{-λ}`, with `e^{-2λ}` on its square).

---

## 6. The catalyst theorem — adiabatic dilatation in the full CTP action

**Question:** is the rigid spatial dilatation `T_λ` (`a→a e^λ`, comoving `k` fixed) a genuine gauge
redundancy of the full CTP action `S_IF[φ_c,φ_q]`?

**Answer (outcome B; piecewise `w1up736t0`, 3-skeptic verified `w3g2yu2wc`):**
- **Invariant:** the local action, the retarded kernel `αχP^TT`, minimal coupling `½h_aT`, and the
  **measure** (`T_λ` is a diffeomorphism, not a Weyl rescaling → Jacobian ≡ 1 → **α does not
  enter; the anomaly route C is ruled out**).
- **Broken by F:** `χ_eq = 1/(1+(L₀k_phys)²)` is not invariant for `k≠0`. Under `T_λ`,
  `k_phys=k/a → e^{-λ}k_phys`, so `(L₀k_phys)² → e^{-2λ}(L₀k_phys)²`. A fixed *proper* length `L₀`
  cannot be separate-universe invariant.
- **Survives only** at strict `k=0` / in the memoryless `L₀→0` limit, and trivially in the scalar
  sector (`P^TT` annihilates it → `μ_linear=1`). The `k≠0` breaking lives in the *physical* tensor
  sector — not a pathology.

**Structural reading:** **D does not collapse into Q; F is the controlled breaking of D.** The
"one symmetry" hope is not realized — and the replacement is cleaner: GRUT is *defined* by which
redundancy it breaks and by how much (one scale `L₀`).

**Honest residual:** this establishes the *breaking* and rules out the anomaly. It does **not**
re-derive the underlying `L₀→0` redundancy from the CTP action (that is the presupposed Weinberg
adiabatic mode). D's correct label: "conjectured bridge whose *breaking term* is established."

---

## 7. The V3 foundation (declared as structure, not completeness)

| Element | Standing |
|---|---|
| Organizing principle (dilatation-redundant limit + L₀-breaking) | **verified** |
| Q — CTP/in-in unitarity | **proven pillar** |
| F — finite single-pole memory (τ₀ anchored) | **postulated pillar** (one input, like GR's metric) |
| D — adiabatic dilatation redundancy | **conjectured bridge; breaking established** |
| `μ_linear=1` (linear cosmology = ΛCDM) | **derived requirement** |
| α = 1/3 (the value) | **open** — 4th-order Riegert a/c |
| Dark sector | **open** — nonlinear/tensor (C5a W², C5b orbital-ω, C5c TT) |
| Flavor / Koide | **outside the scheme** (hosted Yukawa input) |
| "distinguishability" | a **name** for Q∩F∩D, not an axiom |

**What V3 is NOT:** a completed derivation of everything. It names its frontiers honestly — as
thermodynamics, GR, and QM all did at their founding.

---

## 8. Where it is recorded on the backend

- `grut/foundation/organizing_structure.py` — the verified result as structured, testable data
  (the dilatation theorem computed symbolically; pillars, outcome, terrain).
- `tests/foundation/test_organizing_structure.py` — 7 tests, green.
- Registry: `organizing_structure_v3` (foundational), `adiabatic_dilatation_redundancy_nogo`
  (computed). Registry completeness suite green (34/34).
- Theory: `GRUT_V3_ORGANIZING_STRUCTURE.md` (the foundation artifact), this synthesis, and the
  corrected `GRUT_SELECTION_PRINCIPLE.md §3.7`, `CMB_ISW_EQUALITY_FILTER.md §0`, `frw_explicit.py`.

---

## 9. When we build V3 (not now) — the spine it would follow

1. What a responsive vacuum is (**Q**): physics is the response to realized differences;
   `S_IF[diagonal]=0`.
2. What keeps it finite (**F**): single-pole memory; causal, bounded, GR-recovering.
3. What it is forbidden to respond to (the **boundary operator**): the no-gos as the shape of the
   allowed space — minimal coupling, tracefree kernel, `μ_linear=1`.
4. The organizing principle (**D broken by F**): GRUT = the dilatation-redundant GR limit + one
   scale of controlled breaking.
5. What is hosted, not generated: α's value, τ₀, flavor/Koide.
6. Only then: what universe emerges, and where the dark sector must live (nonlinear/tensor — open).
