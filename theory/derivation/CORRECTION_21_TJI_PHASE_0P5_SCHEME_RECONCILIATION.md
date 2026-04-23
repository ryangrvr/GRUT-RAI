# Correction #21 — TJI Phase-0.5: MS-bar scheme reconciliation

**Date:** April 23, 2026
**Status:** HONEST NEGATIVE on FeynCalc 7/4 match.
Phase-0.5 delivers canonical MS-bar pipeline with full transparency; no standard variant reproduces V7 §26.2.3's reported 7/4 from the raw Laurent.

---

## What Phase-0.5 attempted

Phase-0 established the flat-space SymPy pipeline with the raw gamma-function Laurent:

| Coefficient | Exact Fraction |
|:---|:---|
| 1/ε² | `Fraction(-1, 64)` |
| 1/ε rational part (γ_E → 0) | `Fraction(-25, 384)` |
| ε⁰ rational (γ_E → 0, π² → 0, ζ(3) → 0) | `Fraction(-541, 2304)` |

V7 §26.2.3's FeynCalc verification log reported `Fraction(7, 4)` as the ε⁰ pure rational. Phase-0.5's mission: implement standard MS-bar absorption in SymPy and verify the reconciled ε⁰ equals `Fraction(7, 4)` exactly, with transcendental cancellation explicitly verified.

The arithmetic shift this would require:

    Δ = 7/4 − (−541/2304) = 4032/2304 + 541/2304 = 4573/2304

The three cross-term contributions T₁ + T₂ + T₃ (pole × absorption expansion) must sum to exactly `+4573/2304` for the reconciliation to close.

---

## Convention declaration (mandatory per NIS discipline)

Every Fraction equality in this work is asserted under the conventions in `grut.derivation.tji.flat_space.convention_declaration()`:

| Item | Convention |
|:---|:---|
| **C1** Dimensional regularization | `d = 4 − 2ε` (standard MS-bar input form) |
| **C2** Raw Laurent form | Prefactor `−3(D−2)³/(64(D−4)(D−1))` × `Γ(2ε−1)·Γ(1−ε)³/Γ(3−3ε)`; full TJI factors of π^D, (−k²)^(1−2ε), 1/k² absorbed into per-unit `e⁴/(16π⁴)` normalization |
| **C3** Raw sign pattern | 1/ε² = −1/64 (invariant), 1/ε rational = −25/384 (odd; flips under ε → −ε), ε⁰ rational = −541/2304 (invariant). If a reader sees 1/ε rational = +25/384 the convention has been flipped to d = 4+2ε |
| **C4** MS-bar absorption | `F_loop(ε) = (4π)^ε · Γ(1+ε)⁻¹` per loop, squared at 2 loops. Matches C1. Reference: Collins, *Renormalization* (1984) §3 |
| **C5** Transcendentals | Absorbed: γ_E, log(2), log(π), log(4π). Physical: π² (ζ(2)), ζ(3), higher |
| **C6** FeynCalc 7/4 session | Internal TarcerRecurse/ApartFF convention **not documented** in FEYNCALC_VERIFICATION_LOG.md; session **not archived** among the V7 notebooks reviewed |

Conventions C1 and C4 are mutually consistent. C3 was sanity-checked against the raw Laurent output. C6's unavailability is the architectural reason Phase-0.5 cannot close against 7/4 by reverse-engineering — we can't see the target convention.

---

## What was found

### Standard MS-bar applied to the raw Laurent

Multiplication by `[(4π)^ε · Γ(1+ε)⁻¹]^2` cross-multiplies against the raw's 1/ε² and 1/ε poles. After `expand → simplify → nsimplify`:

    ε⁰ reconciled = −541/2304 + π²/192                (standard MS-bar)
                    − 25·log(2)/96 − 25·log(π)/192    (linear in log(2), log(π))
                    − log²(2)/8 − log(2)·log(π)/8 − log²(π)/32   (quadratic)

Structure analysis:
- **γ_E fully canceled.** Algebraic check passes: `EulerGamma not in free_symbols`.
- **Logs group as pure `log(4π)`.** Linear coefficient of `log(2)` is `−25/96`, linear coefficient of `log(π)` is `−25/192`; the ratio is exactly 2:1 (structural check `log2_coeff == 2·logpi_coeff` passes), confirming they combine as `log(4π) = 2·log(2) + log(π)`. The residual expression is `−541/2304 − 25·log(4π)/192 − log²(4π)/32 + π²/192`.
- **log(4π) itself NOT absorbed to zero.** Setting log(4π) → 0 is the final MS-bar *convention* choice (choice of renormalization scale μ² = μ_MS̄²), not an absorption the factor delivers on its own.
- **After setting log(4π) → 0**: ε⁰ = `−541/2304 + π²/192`.

### Match against FeynCalc 7/4

No match. The rational part after log(4π) → 0 and all transcendentals cleared is `−541/2304`, unchanged from the raw Laurent. MS-bar shifts the π² coefficient (`1/384` → `1/192`) but not the pure rational. The 7/4 target differs from both raw and MS-bar results:

    Raw pure rational:       −541/2304  ≈ −0.2349
    MS-bar pure rational:    −541/2304  ≈ −0.2349  (unchanged)
    MS-bar rational + π²:    −541/2304 + π²/192  ≈ 0.2793
    FeynCalc claim:           7/4 = 1.75

None matches.

### Systematic enumeration of 24 MS-bar-family variants

`scheme_enumeration()` tests 6 per-loop absorption factors × {include/exclude π^D from the full TJI} × {±1 overall sign} = 24 configurations:

| # | Per-loop factor | Interpretation |
|:---|:---|:---|
| F1 | `1` | No absorption |
| F2 | `(4π)^ε · Γ(1+ε)⁻¹` | Standard MS-bar |
| F3 | `(4π)^ε · Γ(1−ε)` | Alternative MS-bar |
| F4 | `(4π)^(−ε) · Γ(1+ε)` | Reverse MS-bar |
| F5 | `exp(ε(γ_E − log(4π)))` | Direct shift |
| F6 | `exp(−ε(γ_E − log(4π)))` | Inverse shift |

All 24 configurations cluster around `±541/2304 + {0, ±π²/384, ±π²/192}`. **Zero configurations match `Fraction(7, 4)`.**

### Notebook audit (user's original V7 Mathematica notebooks)

Reviewed `/Users/mpg/Desktop/GRUT ToE/Notebooks/`:

| Notebook | Content | Relevance to 7/4 |
|:---|:---|:---|
| `1.15428.nb` | Symbolic ratio `|C_Cosmo/C_FINAL| = 1.15428` from pre-assembled constants | None; doesn't compute TJI |
| `A-ICM_3Loop_Anomaly_Coefficients.nb` | Pre-assembled 3-loop A-ICM expression `A = (3/(16π²))³ × [...]` with `Γ(1-x)` for CONSTANTS, not poles. `x = ε` (d = 4-2x consistent with C1). | None; different calculation |
| `A-ICM_Pheno_Lambda_Prediction.nb` | Similar structure for `B` (phenomenological) | None |
| `A-ICM_QFT_Input_SM_Fields.nb` | Just verifies `Γ(1-x) = 1 + γ_E·x + O(x²)` | None; just a sanity notebook |

None of these notebooks contains the 2-loop TJI `TarcerRecurse` session that produced 7/4. The A-ICM structural pattern (Γ(1-x) multiplying constants, γ_E cancels on `Series[..., 0, 0] // Normal` because it sits beside constants not poles) is **different** from the Phase-0.5 regime (Γ factors in the raw Laurent's poles, γ_E cancels via cross-multiplication with the absorption factor's ε¹ term).

**Convention audit result:** the A-ICM notebooks confirm `d = 4 - 2ε` (consistent with my C1). The FeynCalc session that produced 7/4 is a separate, unarchived artifact. Phase-0.5 cannot close reconciliation to 7/4 without recovering that session's exact convention.

---

## Honesty protocol (per Phase-0.5 plan)

This is failure mode **(b)** from the approved plan: "Transcendentals cancel but rational ≠ 7/4."

Protocol response: "Report the exact rational produced. Flag as convention mismatch with FeynCalc. Investigate whether a variant of MS-bar (MS-dagger, modified minimal subtraction, or other) produces the match, but do not force the match."

Executed:
- Reported exact rational: `−541/2304` (raw) and `−541/2304 + π²/192` (MS-bar).
- Flagged convention mismatch via `feyncalc_reference()` and `convention_declaration()`.
- Investigated 6 MS-bar-family variants × 4 sign/π^D configurations = 24 total. None matched.
- Did not force the match. No ad-hoc corrections. No constant tuning.

Per plan Path B: picked **standard MS-bar (F2)** as the canonical scheme for the V7/V8 record. Phase-1 S⁴ measurement will be against this canonical scheme's ε⁰ (`−541/2304 + π²/192`), **not** against 7/4.

---

## What Phase-0.5 leaves open

- **The 7/4 origin.** Recovery of the V7 FeynCalc session that produced 7/4 is the only way to close the reconciliation. This is a Phase-0.5-redux item, deferrable to specialist or session recovery.
- **The shift 4573/2304.** This arithmetic guardrail from the plan would have held IF reconciliation closed; it is documented in the regression test `test_expected_feyncalc_shift_would_be_4573_over_2304` as the value a successful reconciliation would have produced, pinned for any future retry.
- **Phase-1 S⁴ measurement baseline.** Now `−541/2304 + π²/192` (standard MS-bar canonical) instead of `7/4`. If the 7/4 reconciliation is ever closed, Phase-1's baseline updates to whichever MS-bar variant it turns out FeynCalc used.

---

## Strategic observation (from user's V8 Phase-0.5 framing)

> "If the 7/4 match comes out clean, that's mild evidence for the broader claim that the flat-space pieces of the 3-loop computation are reconcilable scheme-by-scheme with standard tools. Worth a line in the TJI_PHASE_1_CALCULATION_PLAN.md completion note."

The honest-negative outcome inverts this: the 7/4 NOT matching under standard MS-bar is mild evidence that the V7 §26.2 "rational shift of ~36 in the −108000 coefficient shifts R by ~1%" scheme fragility claim is more than a nuisance — reconciling specific rationals across schemes may require recovering the exact session convention, not just choosing a textbook MS-bar form. Phase-1 curved-space work should anticipate this: S⁴ results will need a documented MS-bar convention pinned alongside the numerical output.

---

## Status ledger

| Item | Before Phase-0.5 | After Phase-0.5 |
|:---|:---|:---|
| Flat-space raw Laurent | COMPUTED (Phase-0) | COMPUTED (unchanged) |
| Flat-space MS-bar reconciliation | PENDING | COMPUTED in canonical MS-bar |
| Match to FeynCalc 7/4 | UNKNOWN (deferred) | **HONEST NEGATIVE** under conventions C1-C5; session C6 unavailable |
| Phase-1 measurement baseline | 7/4 (tentative) | `−541/2304 + π²/192` (canonical MS-bar) |
| Convention declaration | Implicit | **Explicit** (6-item `convention_declaration()`) |
| Regression tests | 27 Phase-0 | 27 + 31 Phase-0.5 = 58 TJI total |
| Full suite tests | 492 | **523** |

---

## Deliverables

| Artifact | Path |
|:---|:---|
| Module | `grut/derivation/tji/flat_space.py` (+`ms_bar_absorption_factor`, `scheme_enumeration`, `finite_rational_ms_bar_scheme`, `convention_declaration`) |
| Tests | `tests/derivation/tji/test_ms_bar_reconciliation.py` (31 tests) |
| Correction log | This file |
| Phase-1 plan update | `theory/derivation/TJI_PHASE_1_CALCULATION_PLAN.md` (pending in same commit) |

523 passing tests overall. No regressions elsewhere.
