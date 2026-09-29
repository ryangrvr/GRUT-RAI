# L0-1g (O-6) — PRE-FREEZE REVIEW 01 + OWNER DECISION MEMO (freeze held)

**Date:** 2026-09-29 · **Object:** `L0_1G_CHARTER_01.md` draft
(`940964e`) · **Method:** two analytic reviewers (method and outcome
rules; mathematics and numerics), then one operator check on a
**non-member** chain. **Nothing was computed on the declared pin-0.3
chain.**

**Disclosed non-member computations:**
- reviewer toy chains: pin 0.45 and 1.7, N ≤ 5, plus a symbolic
  N = 5 chain;
- the operator's D-1 check: pin 0.45, N = 800, archived in
  `calc/feasibility/l01g_d1_latetime_nonmember.py`.

**Status: FREEZE HELD.** The review found that the charter's gated
question is, generically, decided in advance at late times. Choosing
the operationalization is the owner's call.

## 1. The finding that changes the fork (D-1): band-edge memory forces pointwise sign alternation

**The argument (method reviewer):**
- The pinned chain's local density of states at site 1 vanishes like a
  square root at both band edges, ω₋ = √0.3 and ω₊ = √4.3.
- So the retained propagators decay like t^{−3/2}, with persistent
  oscillation at ω±.
- Every deviation of the reduced covariance from its asymptote is a
  product of two such factors: δ(t) = t⁻³[A + Σ_j B_j cos(Ω_j t + φ_j)],
  with Ω_j ∈ {2ω₋, 2ω₊, ω₊ ± ω₋}.
- **Differentiating gives oscillating terms at order t⁻³, which
  dominate the non-oscillating part at order t⁻⁴.** So the heat current
  J, and likewise Ḋ, **change sign infinitely often at late times,
  generically. This holds on the infinite chain as well.** It is
  non-Markovian memory, and it is not recurrence.

**Operator confirmation on a non-member chain** (pin 0.45, N = 800,
T_s = 2, T_b = 1; t ∈ [150, 700], well before recurrence):
- **J < 0 at 49.6% of the grid, with 739 sign changes;**
- |J| falls from 1.1×10⁻⁶ (t ≈ 150) to 8.3×10⁻⁸ (t ≈ 400) to
  2.5×10⁻⁸ (t ≈ 700), consistent with t⁻³ ripples.

**Consequence.** Strict pointwise monotonicity of J or of D on a long
window (G-1 and G-2 as drafted) **fails generically by asymptotic
identity.** Under the draft, the "live alternative" (memory backflow)
was really the expected outcome. This is the floor's third instance of
the pattern: attackable content collapsing into an identity under
review.

## 2. Other confirmed defects (both reviewers; applied in whichever form the owner chooses)

| # | Defect | Fix |
|---|---|---|
| Echo guard (both reviewers; blocker) | T_rec marks the *centre* of the returning front, not its onset. The Airy front has a width of about 3.7 / 4.7 / 6.0 time units at N = 23 / 47 / 95, so the echo is at about 66% of its peak by T_rec. The observables at sites 1 and 2 also arrive about 1.3 units early. A violation near the window's end would be recurrence misread as "memory". | Gate on [t_s, T_rec − 4σ_t(N) − 2/v_max), with σ_t = (v_max·T_rec/2)^{1/3}/v_max frozen. A halt-grade cross-N control: on each smaller N's guarded window, J and Ḋ must match N = 95. |
| Label logic (blocker) | H-ORD is a conjunction, so one failed gate is FALSIFIED under T2. The draft routed it to CLASS-SPLIT with no declared subclasses, and it was also confounded: heat was tested only with a hot system, entropy only with a cold one. I-5 excludes the other two directions only at t = 0⁺; on the post-slip window they are open too. | Either declare the subclasses before evaluation, or map one-fail to FALSIFIED. Map all four directions on the window, ungated. |
| J is not purely "heat" (D-5) | By linearity J = T_s·a(t) + T_b·b(t), and J ≠ 0 even at T_s = T_b: correlation-building moves the interaction energy from 0 toward −g·T(K⁻¹)₁₂. | Name the line "bath self-energy non-decreasing". Map the equal-temperature baseline and the (T_s − T_b) decomposition. |
| "Robustly" read as strictest | One grid point at 10⁻¹⁰ relative scores FALSIFIED. Ripples are indistinguishable from gross reversal. | Magnitude maps: the worst drawdown of ⟨E_B⟩ normalized by its net rise; the backflow fraction ∫J⁻/∫\|J\|; and the analogues for D. |
| Slip end t_s | Arbitrary but defensible: substrate data, the uncoupled retained period; not a clock under O-5. | Map the outcomes at t_s/2 and 2t_s, and the "last violation time" t*_N. Label any violation in [0, t_s) as "early backflow (not I-5)". |
| Numerics | RC-2 is tautological in modal form. RC-4's points were not listed and used a pure-relative tolerance. There is no noise-floor control. The efficient decomposition was not frozen. v_max was not in closed form. | Site-basis ⟨H⟩ at 20 listed points; a mixed tolerance; `fsum` with per-point error bounds (points below 100·err count as undecided); the O(N) Schur/modal decomposition; closed-form v_max = √cos k*, cos k* = (2.3 − √1.29)/2 (v_max = 0.762961). |
| Minor | L-1 dropped the identities' scope qualifiers; RC-5 used global vs bath indexing and an O(t³) remainder (the correct remainder is O(t⁴), because D is even); grid alignment; normalization 2/√(2N+1); window-ratio wording (4.53×, not 4.2×). | All applied. |

**Confirmed correct by the mathematics reviewer:**
- the closed-form spectrum at general N;
- K_BB = K_{N−1};
- the initial state;
- the evolution;
- J = g⟨p₂q₁⟩;
- S_ref and Ḋ;
- all moment derivatives;
- the RC-5 and RC-6 coefficients and margins;
- feasibility (under 10 s with the O(N) decomposition).

## 3. The owner's decision (with the operator's recommendation)

With pointwise strict ordering generically dead at late times, O-6 has
three honest forms:

- **(a) A theorem document with an exact appendix (the O-4 precedent).**
  *Recommended.*
  - **The theorem:** in the conservative pinned harmonic class, the
    ensemble heat current and the reduced relative entropy **cannot be
    strictly monotone on long windows.** Band-edge memory forces t⁻³
    sign-alternating ripples, even at N = ∞.
  - **The non-degeneracy condition** (some B_j ≠ 0) is evaluated
    exactly in the appendix from the closed-form spectral weights.
  - **The appendix list, frozen before evaluation:** on the declared
    chain, with the guard band, all four directions, the
    equal-temperature baseline, and the **magnitude measures**
    (drawdown, backflow fraction). These measure *how big* the backflow
    is, answering "ripples or reversal?" as evaluated quantities, not
    gates.
  - **Proposed terminal label:** **FALSIFIED** for H-ORD's strict
    pointwise ensemble form. The magnitude findings would say whether a
    *coarse* arrow survives.
- **(b) Re-operationalize "robustly" as a magnitude criterion** with
  thresholds the owner sets *now*, e.g. "backflow fraction below x" or
  "drawdown below y%", and run a gated fork. It is honest only if the
  thresholds come from a principle rather than from tuning, and none is
  currently derived.
- **(c) Keep the strict gates and run anyway.** Not recommended. It
  would present a predicted failure as a finding.

**Why (a):** it is the same honest move as O-4. Most of the content is
identity- or asymptotics-grade, and the genuinely unknown part (how
large the backflow is on the declared chain's window) is an evaluation
rather than a prediction. **The O-7 input either way:** in this class,
*emergent dissipation does not imply strict emergent ordering. After
the switch-on slip (I-5), the ensemble arrow is interrupted forever by
band-edge memory ripples.* Whether a coarse arrow survives is exactly
what the magnitude maps would show.

## 4. Standing

No channel moves. L0-1g is not frozen, not run, and banks nothing.
O-1, O-3, O-4 and O-5 are terminal. O-2 is open.
