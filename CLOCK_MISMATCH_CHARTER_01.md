# CLOCK-MISMATCH INSTRUMENT — CHARTER + PRE-REGISTRATION (frozen before evaluation)

**Date:** 2026-09-25 · **Chartered by:** owner, verbatim scope: *"Charter only the
clock-mismatch instrument from PREDICTION_UNIQUENESS_MAP_01. Recompute the rung3
ladder rate and rung7 τ₂ comparison using one common time coordinate. Preserve
the original calculations unchanged as the control. Pre-register the
transformation and comparison rule before evaluating the result. Do not use any
downstream GRUT conclusion to choose the coordinate or normalization. Return
exactly one of (A)/(B)/(C). Do not proceed to Λ_R, Matsubara, Π₀, or U5 until
this verdict is recorded."*

**This file is the pre-registration. It is committed and pushed BEFORE the
instrument runs**; the verdict document will cite this file's commit hash.
Register untouched; ledger 0; banks nothing.

---

## 1. THE OBJECT

The stage-close addendum's finding (2026-08-19/20): every *"Ht ≈ 1 versus
Ht ≳ 4.3"* comparison filed into `rung3` compares two clocks without checking
they are the same one; the recomputation "outranks everything queued."
`RUNG3_KEYSTONE_MAP.md` (screened 2026-08-21, AMBER) derived the clock maps
(D1–D6) and ordered, but did not perform, "the one-clock recomputation (C1/C2)"
(its §9.1). This instrument performs it.

**The two filed quantities (verbatim, sources pinned):**

- **Q-rung3:** the finite-T ladder-kernel dominance requirement
  (`calc/finite_T_pole_structure.py`, part 4b): with residue weights n³, the
  leading rung's share is share(Ht) = (1−x)⁴/(1+4x+x²), x = e^{−Ht}; 6.1% at
  Ht = 1; 90% at Ht = 4.33; 99% at Ht = 6.68. Filed comparison (line 262):
  *"rung7 carries tau_2 ~ 1/H_0, i.e. H t ~ 1. Single-pole dominance needs
  H t > 4.3."* The tower rates (l+1)H (`calc/static_patch_tt_response.py`) are
  per static-patch Killing time.
- **Q-rung7:** τ₂ ~ 1/H₀, the inserted IR relaxation constant
  (`rung7_wz.statement`: "+2 of the +3 total"), an FRW **cosmic-time**
  quantity.

## 2. THE NAMED CLOCK — and why its selection satisfies the owner's fence

**The common coordinate is comoving proper time on the shared axis worldline**
(the r = 0 / x = 0 comoving geodesic). Selection is forced by derivations that
predate this charter and are independent of every downstream GRUT conclusion —
the 2026-08-21 screened keystone map:

- **D1 (derived, exact):** static-patch Killing time T equals flat-slicing
  cosmic time t on the axis; both are that geodesic's proper time.
- **D3a (derived, screened):** along a single comoving geodesic the restricted
  correlator is stationary in cosmic proper time; the QBM toy's silent clock is
  licensed at that scope only.
- rung7's "cosmic time" is by definition comoving proper time.

So the named clock is **the only clock in which all three filed usages already
have a screened, licensed meaning**. No alternative is selected; no
normalization is chosen (all comparisons are dimensionless ratios). The
conformal-time re-expression is computed only as a control exhibiting
clock-form dependence, never as a candidate reading.

## 3. THE TRANSFORMATION RULE (pre-registered)

The screened maps D1–D6 of `RUNG3_KEYSTONE_MAP.md` §1.2 are the transformation
rule. The instrument does not assume them: it **re-verifies each numerically**
from the hyperboloid embedding before use —

1. both patch embeddings satisfy −X₀²+X⃗²+X₄² = H⁻² (sampled);
2. **axis identity** T = t (D1) — the two filed clocks are the same clock on
   the shared worldline;
3. off-axis: dτ_static = √(1−H²r²)·dT ≠ dt (D2);
4. stationarity split: equal-space invariant z depends on Δt only
   (worldline-stationary, D3a); separated pairs depend jointly on t₁+t₂ and Δt
   (D3b) — both verified numerically;
5. the exponential↔power-law mismatch attaches to the cosmic↔**conformal**
   pair (e^{−ΓΔt} = (η′/η)^{Γ/H}), not to the Killing↔cosmic axis pair, which
   is the identity — computed explicitly, resolving the apparent D1/D4 tension
   on the keystone map's face.

## 4. CONTROLS (owner: "preserve the original calculations unchanged")

- **No frozen file is edited.** `finite_T_pole_structure.py`,
  `two_scale_desitter.py`, `wz_dark_energy.py`, `static_patch_tt_response.py`,
  `RUNG3_KEYSTONE_MAP.md` are read-only citations.
- **Control reproduction gate:** the instrument independently re-derives
  share(Ht) (closed form AND direct summation) and must reproduce the frozen
  numbers — share(1) = 6.1% (±0.1 pp), t₉₀ = 4.33 (±0.02), t₉₉ = 6.68 (±0.02)
  — or it HALTS with no verdict.
- **Background inputs:** flat ΛCDM, Ω_m = 0.315, the repository's own declared
  central background (`calc/isw_exclusion.py:70`, `calc/isw_tt_auto.py:140`).
  H₀ enters only through dimensionless products. **No new numerical input is
  introduced.**

## 5. THE COMPARISON RULE AND VERDICT SEMANTICS (pre-registered, mechanical)

**Comparability test.** In the named clock, the two quantities are *directly
comparable* iff they refer to the same background solution's worldline clock
with no identification beyond the D1–D6 maps. Facts the test consults, fixed
before running: the toy kernel is derived on **constant-H de Sitter** (exact);
rung7's τ₂ lives on **FRW with Ω_m ≠ 0**; the 2026-08-19 close records that
these are **different solutions** (the X2 refusal), and the register prices the
background-flow question as the +1 omission `background_time_translation_flow`.

**Verdict rule:**

- **(A) adverse mismatch survives** iff the two quantities are directly
  comparable in the named clock (no identification beyond D1–D6 needed) and
  the shortfall (available dimensionless lag < 4.33) holds across the entire
  declared reading set of §6.
- **(B) coordinate artifact** iff the D1–D6 re-expression **alone** — no new
  physical identification — removes the shortfall.
- **(C) underdetermined** iff direct comparability fails: the comparison's
  truth value depends on an identification not banked in the register (which
  H the dimensionless lag uses; the dS→FRW transport of the constant-H kernel;
  the onset/lag specification; the D3b reduction of the assembled object). A
  (C) verdict is valid **only if** the instrument exhibits the dependence
  quantitatively — at least one declared reading on each side of the 4.33
  threshold, with the unbanked input each reading requires named. Otherwise
  (all readings on one side) the verdict defaults to (A) or (B) accordingly.

**Sub-findings recorded regardless of verdict:** whether the pure
Killing-vs-cosmic clock concern is exonerated on the axis (D1), and whether
the within-toy statement (coherent in one stationary clock, per keystone §1.4)
stands. These do not alter the A/B/C classification; they scope it.

## 6. THE DECLARED READING SET (exhaustive; all computed, none selected)

Dimensionless lag D(r) compared against t₉₀ = 4.33 (t₉₉ = 6.68 also reported):

| id | the lag probed | the H used | requires unbanked input? |
|---|---|---|---|
| R1 | Δt = τ₂ = 1/H₀ (as filed) | H₀ frozen (dS-at-today) | dS→FRW identification H_bath = H₀ |
| R2 | Δt = t₀ (all available history) | H₀ frozen | same, plus onset = big bang |
| R3 | Δt = time since Λ-domination (Ω_Λ = Ω_m) | H₀ frozen | same, plus onset = z_Λ |
| R4 | same three lags | contemporaneous: D = ΔN = ∫H dt (e-fold clock) | adiabatic promotion H → H(z) of a constant-H kernel |
| R5 | control only: conformal re-expression | — | none (demonstrates clock-form dependence; not a physical reading) |

For R4 the instrument also computes the **fixed-temperature premise check**:
the variation of T_dS = H(z)/2π across each lag span (the Matsubara ladder is
a fixed-T structure; the factor by which T varies over the span measures how
far the reading is from the state the ladder was derived in). Reported as a
factor, no tolerance chosen, no reading disqualified by it — it prices R4, it
does not select against it.

## 7. TRAP FENCES

- **DIRECTIONAL-OPTIMISM, applied hardest to (B) and to (C)-as-escape.** (B)
  deletes an adverse finding — the outcome the program wants — so it is
  granted only on the pure-coordinate criterion of §5, nothing softer. (C) can
  be a dodge; it is granted only with the quantitative flip exhibited and each
  required input named, else the verdict defaults per §5.
- **READING-SHOPPING:** every §6 reading is computed and reported; none is
  selected, weighted, or dropped.
- **NO-DOWNSTREAM-SELECTION:** the clock is fixed by §2's screened
  derivations; the instrument contains no branch that consults any GRUT
  conclusion (w(z), rung7's needs, rung3's tier) to choose anything.
- **CONTROL-PRESERVATION:** §4; a failed control reproduction halts with no
  verdict.
- **NO-BANKING:** the instrument writes a result JSON and a verdict document;
  no register field changes; the verdict doc may propose register edits for
  the bank gate but applies none.

## 8. DELIVERABLES AND STOP

1. `calc/clock_mismatch_check.py` — pure stdlib, self-checking (house
   `check()` pattern), emits `CLOCK_MISMATCH_RESULT.json` (sha-hashed) with
   the verdict computed mechanically by §5.
2. `CLOCK_MISMATCH_VERDICT_01.md` — the recorded verdict: exactly one of
   (A)/(B)/(C), the sub-findings, and what it does and does not change.
3. **HARD STOP at the verdict** (bounded instrument; the decision it waits on:
   the owner reads the verdict and selects the next instrument). Per the
   owner's charter, Λ_R, Matsubara, Π₀, and U5 are fenced until then.
