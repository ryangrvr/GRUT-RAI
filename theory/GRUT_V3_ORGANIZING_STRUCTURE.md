# GRUT's Organizing Structure — the V3 boundary

**Date:** June 2026 (2026-06-16)
**Purpose:** the artifact the whole audit phase was for. Not "add more sectors" — *rebuild
around the constraints that survived every adversarial attack.* This is what GRUT actually is
once the mechanisms that died are stripped away. Grounded in, and adversarially verified against,
the primary corpus (`GRUT_SELECTION_PRINCIPLE.md §3.6–3.7`, `PROJECTOR_CONSISTENCY_NOGO.md §5–§6`,
`linearized_ctp_action.py`, `closure_protocol.py`, `CMB_ISW_EQUALITY_FILTER.md §0.1/§0.25`,
`KOIDE_AMPLITUDE_UNIFICATION.md`). Workflow audits: `ww3jtq2t9`, `wqr4a0cuq`, `w1up736t0`, `w3g2yu2wc`.

---

## The verified verdict — one paragraph for the top of V3

> **What the adiabatic dilatation is to GRUT.** The long-wavelength adiabatic spatial dilatation
> `T_λ: a → a e^λ` (comoving `k` fixed) is GRUT's organizing redundancy — but an *exact* one only in
> the memoryless GR limit `L₀ → 0`, or at the strict `k = 0` point. It is the gauge freedom of a
> vacuum that responds to nothing absolute. GRUT's single physical scale `L₀ = cτ₀ ≈ 12.85 Mpc` — a
> fixed *proper* length — breaks it for every `k ≠ 0`: under `T_λ` the physical wavenumber transforms
> `k_phys = k/a → e^{-λ}k_phys`, so the memory argument `(L₀k_phys)² → e^{-2λ}(L₀k_phys)²` and the
> static susceptibility `χ_eq = 1/(1+(L₀k_phys)²)` is not invariant. The breaking is *controlled*
> (enters at `O((L₀k_phys)²)`) and *non-anomalous*: `T_λ` is a diffeomorphism, not a Weyl rescaling,
> so the path-integral measure is invariant (Jacobian ≡ 1) and the trace-anomaly coefficient α does
> **not** enter — outcome (B), anomaly route (C) ruled out. The spine of V3 follows: **GRUT is the
> adiabatic-dilatation-redundant (GR) limit, plus the controlled breaking of that redundancy by
> exactly one scale `L₀`** — the shape by which a mass breaks scale invariance. The CTP-unitarity
> pillar (Q) stands as an independent theorem; finite memory (F) is revealed not as a third axiom but
> as *the breaking term of the dilatation redundancy D*. Consistently, in the linear scalar sector
> where `T_λ` would otherwise be obstructed, the tracefree `P^TT` kernel annihilates the response
> (`μ_linear = 1`, linear cosmology = ΛCDM), so the `k ≠ 0` breaking lives only in the physical
> tensor sector — not as a pathology.

---

## 0. The reframe (what survived teaches the shape)

The casualties of this phase were **mechanisms** (Koide-amplitude closure, linear dark-sector
enhancement, bare-density coupling, horizon-filter cosmology). The survivors were **constraints**.
And every dead mechanism died the same death: it tried to make the vacuum *respond to something
it must not*. So:

> **GRUT is a theory of permissible vacuum response.** Its no-gos are not roadblocks — they are a
> **boundary operator** that deletes forbidden responses and leaves the allowed solution space.

---

## 1. The generator count: TWO proven pillars + ONE conjectured bridge

The honest decomposition, ranked by epistemic standing (this corrects the earlier "three
independent constraints D/Q/F" framing — D is *not* established):

### Pillar Q — in-in / CTP unitarity. **THEOREM of the formalism (proven, independent).**
`S_IF[φ₊=φ₋] = 0`; physical response `= δS_IF/δφ_q|_{q=0}`; the cc-propagator is identically zero.
The vacuum responds only to *realized differences* (deviations from the classical diagonal).
`§3.6` names this the **one genuinely independent leg** of the former "five-route convergence."
Invariance group: the q-axis (forward = backward).

### Pillar F — finiteness / single-pole susceptibility. **INDEPENDENT, but POSTULATED (anchored, not derived).**
`χ(ω) = 1/(1−iωτ₀)` from `τ₀ż + z = z_target`. Makes the response causal, bounded, GR-recovering
(`n_g→1` at high ω). Consistent with Q via FDT — **but FDT consistency is not derivation**; F does
not reduce to Q. It is a constitutive input with `τ₀` observationally anchored.

### Bridge D — separate-universe / spatial-dilatation redundancy. **ATTACKED & INDEPENDENTLY VERIFIED (June 2026). RESULT: not a clean redundancy — broken by F.**
The adiabatic rescaling `x → (1+λ)x`. The load-bearing theorem — *is `T_λ` a genuine gauge
redundancy of the FULL CTP action `S_IF[φ_c,φ_q]`?* — was worked piece-by-piece (workflow
`w1up736t0`) and then **independently adjudicated** by a three-skeptic verification (`w3g2yu2wc`),
all three returning **confirmed, outcome (B), high confidence**.

**Verdict: outcome (D)→(B). NOT a clean (A); the anomaly outcome (C) is RULED OUT.**

- **Invariant (high confidence):** the local branch action, the retarded kernel `αχP^TT`, minimal
  coupling `½h_aT`, and — decisively — **the path-integral measure**. `T_λ` is a *diffeomorphism*,
  not a local Weyl rescaling, so the Fujikawa/trace-anomaly Jacobian (the only object carrying
  `a,c`, hence α) is identically 1. **α does not enter; there is no anomalous breaking.** The hoped
  "broken by exactly α" is wrong — α lives in the conformal/trace sector, the opposite side of the
  conformal⊥separate-universe exclusion from `T_λ`.
- **The obstruction is the finite memory scale `L₀=cτ₀ ≈ 12.85 Mpc` (i.e. pillar F):** the response
  depends on the dimensionless `L₀k_phys = L₀k/a`, and under the separate-universe shift `a→a e^λ`
  (comoving `k` fixed) a mode changes physical size: `k_phys = k/a → e^{-λ}k_phys`, hence the
  *squared* memory argument in `χ_eq` scales `(L₀k_phys)² → e^{-2λ}(L₀k_phys)²` — **not invariant**,
  because `L₀` is a fixed proper scale the dilatation cannot absorb. *(Arithmetic note: the breaking
  factor is `e^{-λ}` on `k_phys` itself and `e^{-2λ}` on its square — verified `w3g2yu2wc`; an
  earlier draft mislabeled it `e^{-2λ}` on `L₀k_phys` linearly.)* A medium with an absolute length cannot
  be separate-universe invariant for any `k≠0`.
- **Survives only at strict k=0** (infinite wavelength, always ≫`L₀`) and **trivially in the scalar
  sector** (where `P^TT` annihilates the response → `μ_linear=1`, ΛCDM, consistent with the No-Go;
  the trace-only shortcut breaks `T_λ` and is the retracted/ruled-out path). The `k≠0` breaking
  lives in the *tensor* sector, where the modes are physical anyway — not a pathology.

> **The "one symmetry" question, resolved.** The stronger instinct — that GRUT is one symmetry — is
> **not realized**, and the reason is structural, not technical: **D is the redundancy that F
> breaks.** At `L₀→0` (memoryless/GR limit) the adiabatic dilatation is an exact redundancy; turning
> on finite memory `L₀` breaks it at `O((L₀k_phys)²)`. So GRUT is **the adiabatic-dilatation-
> redundant (GR) limit, plus the controlled breaking of that redundancy by exactly one scale `L₀`** —
> the same shape by which a mass breaks scale invariance. Q (CTP unitarity) stands independent; F is
> now revealed as *the breaking term of D*, linking two of the three structures rather than leaving
> them merely independent. The unification is **PARTIAL by theorem, not by ignorance.**

**Residual standing (honest flag).** The verification establishes the *breaking* — that finite `L₀`
obstructs `T_λ` at the kernel and the measure — and rules out the anomaly route. It does **not**
independently re-derive that `T_λ` is a redundancy of the bare action in the `L₀→0` limit; that
underlying redundancy is presupposed (the standard Weinberg adiabatic mode), not proven from GRUT's
CTP action from scratch. So D's correct label is **"conjectured bridge whose *breaking term* is
established,"** not a proven pillar. And F itself is *postulated* (single-pole `χ`, `τ₀` anchored),
so "F breaks D" links a postulated structure to a conjectured one — sound, but inheriting the weaker
standing of its two ends.

---

## 2. What the pillars FORCE (the robust theorems)

- **Minimal matter coupling** `½ h_a T` (no non-minimal vacuum–matter term). — from Q (Fact 1).
- **Tracefree `P^TT` kernel**, which annihilates linear scalars. — from Q + the kernel structure.
- **`μ_linear = 1` — linear cosmology IS ΛCDM.** Forced *two ways* (tracefree `P^TT` annihilates
  linear scalars; and conformal ⊥ separate-universe at k→0), and *over-determined by data* (the
  full retarded kernel gives 2.79× / ~32σ — worse, not better; `CMB_ISW §0.1`). **This is the
  genuinely robust result of the entire framework.** GRUT's dark sector therefore *cannot* live in
  the linear-scalar channel — it must be **nonlinear / tensor / bound-system** (C5a–C5c, all OPEN).

---

## 3. "Distinguishability" — a NAME, not an axiom (and it spans two mechanisms)

"The vacuum responds only to physically distinguishable information" is **not a fourth axiom.** Per
`§3.6`: *"the information/distinguishability framing is a re-description, not a derived quantity."*
It is the apt *name* for what Q (and, if proven, D) enforce — a **relabeling**, not a foundation.

Sharper finding: the principle as previously written (**P**) silently fused **two distinct
mechanisms**, which must not be conflated:
- **Invariance clause** ("couple only to what survives separate-universe subtraction") — geometric / Q+D.
- **Realization clause** ("unrealized configurations elicit no response") — the **Keldysh-noise
  sector** (`ρ_cl = φ_c²`, `G^K = ⟨δρ²⟩`), a *different* CTP structure than the retarded q-axis
  nullity (`CMB_ISW §0.25`).
"Distinguishability" is a label bolted across both — which *weakens* the unification claim, not
strengthens it.

---

## 4. Hosted / outside the vacuum-response scheme

| Quantity | Status |
|---|---|
| `α = 1/3` **value** | OPEN — needs the 4th-order Riegert a/c (`SELECTION_PRINCIPLE §6`). Mode-count is selected; value is not. |
| `τ₀` **value** (41.9 Myr) | POSITED / anchored (`1/(108π H₀)` + Bullet Cluster). |
| `N = 3`, the Yukawas, **Koide `K=2/3`** | **OUTSIDE the scheme.** Yukawa-input, hosted not generated; the fixed-point derivation **FAILED** (GRUT impedance gives 4/9, not 2/3). Flavor amplitude is not a vacuum-response redundancy. |

**Implication for V3 scope:** the organizing principle governs **gravity / cosmology** and *hosts*
flavor rather than generating it. That is a boundary, not a gap.

---

## 5. The honest V3 architecture

Not "universe begins → S⁴ → snap." Instead, built on what survived:

1. **What a responsive vacuum is (Q):** in-in/CTP structure; physics is the response to realized
   differences; `S_IF[diagonal]=0`.
2. **What keeps it finite (F):** single-pole memory `χ(ω)=1/(1−iωτ₀)`; causal, bounded, GR-recovering.
3. **What it is forbidden to respond to (the boundary operator):** the no-gos, presented as the
   *shape* of the allowed space — minimal coupling, tracefree kernel, `μ_linear=1`.
4. **The conjectured collapse (D):** *if* `x→(1+λ)x` is a bare-action redundancy, 1–3 become facets
   of one symmetry. State it as the open theorem it is.
5. **What is hosted, not generated:** α-value, τ₀, flavor/Koide — named honestly.
6. **Only then:** what universe emerges, and where the dark sector must live (nonlinear/tensor, open).

---

## 6. The single next move (not α, not τ₀, not Riegert)

**Prove or refute: is the long-wavelength adiabatic spatial dilatation `x→(1+λ)x` a genuine gauge
redundancy of GRUT's FULL CTP action `S_IF[φ₊,φ₋]` — not merely of the classical geometry?**

This is the one theorem that converts GRUT's structure from "two pillars + a bridge" into "one
organizing symmetry." Prior work (`§3.7`, June 2026) established the *demotion* (the invariance
clause is locality + a residual spatial-dilatation redundancy, not new DNA, not general covariance)
and *refuted* the high-pass-rescue corollary — but the **gauge status of the full CTP action**
remains the open, load-bearing question. It is bigger than deriving α: α gives a number; this gives
the organizing principle.
