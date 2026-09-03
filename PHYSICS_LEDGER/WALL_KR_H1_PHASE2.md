# H¹ CLOSURE — PHASE 2: α-VACUUM-LIKE O(H) STATE DEFORMATION CONTROL

**Date:** 2026-09-03 · **Instrument:** `wall_kr_h1_phase2_alpha_control.py` ·
**Artifacts:** `WALL_KR_H1_PHASE2_RESULT.json`, `WALL_KR_H1_PHASE2_POSTANG_NOTE.json`
(gated addendum `wall_kr_h1_phase2_postang_note.py`).
**Battery: 40/40 testable gates, zero failures (369 s); post-angular addendum 1/1.**
**VERDICT: `PHASE2-BREAKS`** — a CONTROL classification only; no
H1-THEOREM-A/B/C, no Phase 3, Phase 1 NOT reopened. Read-only on frozen artifacts; register
sha256 identical pre/post; A–F unselected; nothing banked. W-0.

## A · EXACT DEFORMATION DEFINITION (defined before computing; every line gated)

- Native BD mode: h(u) = e^{−iqu}[(1−Hu) + iH/q].
- **Native O(H) state term in the pair kernel = 0** (GATED): in h(u)h*(u′) the ±iH/q state
  pieces cancel at O(H) — the native O(H) content is PURELY CONFORMAL, −(u+u′)W_flat.
- Deformed mode: **h_α(u) = h(u) + α·(H/q)·h̄(u)** — a Bogoliubov-like mixing whose
  coefficient is EXPLICITLY O(H). Deformation parameter α: real, dimensionless, SYMBOLIC
  throughout; α₀ = 1 registered for the explicit-point checks.
- **Deformed O(H) state term** (DERIVED in-run from the mode product rule, GATED): the pair
  acquires exactly α(H/q)(e^{+iq(u+u′)} + e^{−iq(u+u′)}) at O(H) and nothing else; at kernel
  level W_α = W_flat(1−H(u+u′)) + αH(κ²/q²)(e^{+iq(u+u′)} + e^{−iq(u+u′)}) + O(H²).
- Products changed: **both internal line kernels** (the state feeds every line). Unchanged:
  flat kernel, conformal dressing, vertex, projector, routing, derivative algebra,
  compensator, angular machinery, symbolic d/q/n̂, pre-angular evaluation.
- GATED: reversible (α→0 recovers the native pair identically); O(H)-pure (the flat O(H⁰)
  pair untouched); exactly linear (the α² pair term is O(H²), outside the tested order —
  normalization correction likewise O(α²H²)), so **M(α) = M(0) + α·M₁ exactly**.
- **Naming discipline:** this is an *α-vacuum-LIKE O(H) state deformation control*. A true
  dS α-vacuum carries a CONSTANT Bogoliubov angle; **NOT CLAIMED:** anything about that
  family.

## B · NATIVE-LIMIT RECONSTRUCTION (section 4 — passed before any deformed evaluation)

The control was built independently, Route-B style: V_k from the frozen flat C⁰ vertex,
line residuals from the mode-function product rule, compensator once at pair level.
**B_mixed was not read; the Phase-1 swap relation was not used as an input.**
**VERIFIED on all three configurations: M(α=0) ≡ 0 pointwise pre-angular** (plus_z 38s,
cross_z 319s, plus_x 560s).

## C · M(α) RESULT

$$ M(\alpha) = \alpha\,M_1, \qquad \boxed{M_1 \not\equiv 0 \ \text{on ALL THREE
configurations}} $$

GATED: M(0) = 0 explicitly; M(±α₀) ≠ 0, consistent with the symbolic M₁ verdict. Closed
form of the breaking term (representation GATED per config):

$$ M_1 = \mathrm{pref}\,\frac{\kappa^4}{q^3} \sum_{N=0}^{4} q^N \left[ A^+_N\,
e^{2iqu'} + A^-_N\, e^{-2iqu} \right], $$

with A⁺_N = Σ_k V_k[(−1)^e + (−1)^f], A⁻_N = Σ_k V_k(−1)^{e+f}[(−1)^g + (−1)^h] —
**every A±_N nonzero, every sector N = 0..4, every configuration.**

Because the vertex and projector carry no state input (GATED: α never enters V_k) and the
state enters the O(H) loop only through the two line kernels, α·M₁ is the COMPLETE O(H)
response of the pre-angular integrand to this deformation (DERIVED from those gated facts).

## D · SWAP-RELATION RESULT (section 6 — computed independently of the M sum)

- The vertex S-array is **STATE-INDEPENDENT by construction** (GATED: V_k carries no α).
  The deformation **cannot** break F1 itself: S_{m,j}(ω;α) = (−1)^{j+m}S_{j,m}(ω;α) holds
  trivially because α never reaches S.
- The meaningful deformed observable: the (j,m)-resolved aggregate A_{j,m}(α). Its native
  part is transposition-ANTISYMMETRIC (GATED — the Phase-1 pairing operates in the native
  object); its **α-part is NOT transposition-antisymmetric** (GATED, all three configs).
- **The precise reason, localized** (this is the section-6 branch "swap relation survives
  yet M ≠ 0"): the deformed state term is a PURE PHASE e^{±iq(u+u′)} — the ν-derivatives
  never demote on it, so the antisymmetric ladder weight (g+h−e−f)(−1)^{e+f} **never
  forms**. Phase 1's mechanism is a symmetry CONTRACTED WITH an antisymmetric weight; the
  deformation removes the weight, not the symmetry. Without it, the sector sums are the
  parity sums A±_N above, and they do not vanish. **Structural correlation recorded:** F1
  intact + weight structure lost ⇒ cancellation lost. *(Reading, per Leg B: the
  "derivatives never demote ⇒ weight never forms" account is an accurate reading of the
  GATED positive parity representation M₁ = pref(κ⁴/q³)Σ q^N[A⁺_N e^{2iqu′}+A⁻_N e^{−2iqu}] —
  the gate proves that form and A±_N ≠ 0 directly; the demotion story explains WHY, and is
  not a separately-gated claim. The verdict rests on the direct M₁ ≠ 0, not on the reading.)*

## E · ALL THREE CONFIGURATIONS

| config | native M(0)=0 | M₁ | A₁ antisym | A⁺_N=0 (N=0..4) | A⁻_N=0 (N=0..4) |
|---|---|---|---|---|---|
| plus_z | VERIFIED | **NONZERO** | no | none | none |
| cross_z | VERIFIED | **NONZERO** | no | none | none |
| plus_x | VERIFIED | **NONZERO** | no | none | none |

**Post-angular note (gated addendum):** the breaking SURVIVES the exact angular average —
⟨A±_N⟩ ≠ 0 for every sector and every configuration, uniformly. The nonzero result is not a
pre-angular artifact.

## F · NEGATIVE CONTROL

**The instrument can see a break.** Deliberately broken construction: W_neg = W_flat(1−2Hu)
— ALL the O(H) dressing loaded onto the u endpoint, which NO single-mode deformation can
produce (a mode deformation always dresses the pair symmetrically through h(u)h*(u′)). The
detectability precondition is gated first (Σ₀ = Σ_k V_k·pref·flatA·flatB ≠ 0, so the
u′-content cannot vanish), then **M_neg ≠ 0 is confirmed by numeric witness** (|M_neg| ≈
3.2, 1.9, 1.3 at three independent rational points; a symbolic expression nonzero at a point
is not identically zero). The gate that passes when the cancellation HOLDS therefore fails
when it is broken — the control is not vacuous.

*Instrument note (disclosed):* the negative control's exact symbolic zero-test on the broken
kernel's large rational coefficients did not converge within the 20-minute budget across
several attempts; per the standing 20-minute rule it was re-represented as a **numeric
witness**, which is the correct tool for a "confirm nonzero" gate (microseconds, no symbolic
cancellation) and is used ONLY to confirm nonzero, never to certify a zero. All zero-valued
gates (native limit, M(0)) remain exact-symbolic. A separate reported diagnostic: the
hermiticity-sign-broken Bogoliubov pair also gives M_sign ≠ 0 (numeric witness) — reported
only, not used as the negative control, since it probes the same A± sums.

## G · INDEPENDENT ADVERSARIAL VERDICTS (workflow wd2hzdhto, 2 legs, 0 errors)

**Leg A — CONSTRUCTION: `CONFIRMED`.** Independently reproduced the load-bearing results:
the flat kernel equals frozen WPLUS|_{H=0}; the dressing reproduces frozen WPLUS at O(H⁰)
AND O(H¹) exactly; V_k is alpha-free on all 36 keys; the local wop equals frozen wops for
all a,c≤2; the compensator matches Route B byte-for-byte; **both M0 and M1 are themselves
alpha-free**, and Ma = M0 + α·M1 reattaches α explicitly. **Only the state ingredient
changed** — α enters solely the two line kernels via sdef, symmetrically. The native
limit is REAL-independent: B_mixed never read as a variable; the swap relation never a
computational input (only a gate label); iszero(M0)=0 recomputed from the flat vertex alone.
Order purity CLEAN (α² pair term pure O(H²)); the M1_zero verdict rests on exact-symbolic
iszero(M1)=False, NOT on any numeric witness; the witness is confined to the two
confirm-nonzero sites. No errors.

**Leg B — INTERPRETATION: `CONFIRMED_WITH_CAVEATS`.** The conclusion is justified exactly;
the swap relation is treated as an OBSERVABLE, not smuggled in (V_k literally carries no α,
verified not assumed; the deformed aggregate A_{j,m}(α) transposition behavior is computed
directly on the deformed object); no theorem creep; the α-vacuum-LIKE naming discipline and
the DERIVED/GATED/VERIFIED/CONTROL/NOT-CLAIMED status verbs are honored. Three caveats,
**all adopted, none affecting the verdict**:

1. **"REQUIRED" scoped** (§ verdict line, corrected below): what is proven is that the
   native property "the O(H) state term in the pair kernel vanishes" is LOAD-BEARING —
   this explicit deformation and the negative control both break the cancellation. It is
   NOT shown that *every* O(H) state deformation breaks it. The verdict line is rephrased
   so "REQUIRED" cannot be misread as that universal.
2. **§D narrative vs gated form:** the "ν-derivatives never demote, so the ladder weight
   never forms" account is CORRECT (Leg B re-verified it on generic keys) but is an
   accurate *reading* layered on the gated parity representation of M₁ — the code gates the
   positive form M₁ = pref(κ⁴/q³)Σ q^N[A⁺_N e^{2iqu′}+A⁻_N e^{−2iqu}], not a direct
   "weight-absent" comparison. The reading is not load-bearing for the verdict (which rests
   on direct M₁≠0). Flagged as a reading, not a separately-gated claim.
3. **Frozen-file language (not a Phase-2 defect):** the reproduction-target
   `wall_kr_h1_stage2b425_routeB.py` (frozen, base 4563b4d) still uses the pre-rename
   "vertex/frequency exchange" wording; the Phase-2 record itself honors the Phase-1 rename
   to "transposition" throughout. The frozen file predates the rename and is NOT edited
   (append-only; frozen artifacts untouched).

## H · EXACT SCOPE

Frozen flat EH cubic vertex, declared TT contraction and routing, the three frozen TT
configurations (the non-TT `ward` probe untested, as in Phase 1), O(H), pre-angular
(post-angular fate reported in the addendum), THIS deformation (explicitly-O(H) Bogoliubov
mixing) only. Status verbs: linearity GATED; native limit VERIFIED; M₁ GATED per config;
swap-relation state-independence GATED; A₁ transposition behavior GATED observable; the
completeness of α·M₁ as the O(H) response DERIVED from gated facts. This is a CONTROL.

## I · WHAT THE CONTROL DOES NOT ESTABLISH

- **NOT new physics.** A nonzero M₁ is a control result: it says the H¹ cancellation is
  NOT state-blind — it depends on the native property that the O(H) state term in the pair
  kernel vanishes (a BD property at this order). It does not say the deformed state is
  physical, preferred, or excluded.
- **NOT CLAIMED:** anything about the constant-angle dS α-vacuum family; any GRUT-specific
  content; any H1-THEOREM-A/B/C adjudication; any statement beyond the frozen construction.
- **Phase 1 is NOT contradicted and NOT reopened:** its theorem is about the native object;
  the control confirms the boundary of its mechanism's applicability (the mechanism needs
  the demotion-generated antisymmetric weight, which only the conformal dressing produces).

## VERDICT: `PHASE2-BREAKS`

**For Phase 6's truth table:** the native O(H) state property is **LOAD-BEARING** — the
cancellation depends on the O(H) state term in the pair kernel *vanishing* (a BD property at
this order). THIS explicit α-vacuum-like deformation breaks the cancellation on all three TT
configs, pre- and post-angular, and the negative control confirms the instrument's
sensitivity. Scope (per Leg B caveat 1): this establishes that the vanishing-O(H)-state
property is load-bearing; it does NOT establish that *every* O(H) state deformation breaks
the cancellation.

## W-0 STATUS — control computed and reported; no frozen input modified; A–F unchanged; nothing banked.
