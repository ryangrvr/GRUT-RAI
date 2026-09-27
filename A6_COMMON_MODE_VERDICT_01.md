# A6 — VERDICT (the owed common-mode check, discharged at Boltzmann grade)

**Date:** 2026-09-27 · **Charter:** `A6_COMMON_MODE_CHARTER_01.md`,
frozen at `59ab1ec` **before** implementation and run; Amendment 01
(pre-run, disclosed) at `0c9e9e3` · **Authority:** the owner's standing
delegation of 2026-09-27; the owed item is amendment A6 of the frozen
TT-auto gate (`calc/isw_tt_auto.py`, `calc/RESULTS_isw_tt_auto.md`) ·
**Instrument:** `calc/a6_common_mode.py` (`3cd2a73`; the frozen
pipeline imported unchanged; CAMB 2.0.4 + `camb.symbolic` as the
declared external ground-truth harness, A1/mpmath precedent) ·
**Artifact:** `A6_COMMON_MODE_RESULT.json` (sha `49e9f987587b2850…`) ·
**Battery: 5/5 gated checks, zero failures, zero halts, in the
recorded run.**

## THE VERDICT — A6-DISCHARGED

> **The owed Boltzmann-grade common-mode differential check is
> computed. Under the exact CAMB source decomposition, with the missing
> common power (Doppler, quadrupole, early-ISW) attached through the
> normalization-free correction $R^{\rm corr} = (R + f_\ell)/(1 +
> f_\ell)$: every κ=1 named-point kill SURVIVES the correction
> (KILL-CONFIRMED-AT-MEMBER at all three points), the κ=3 survivals
> strengthen, and the edges loosen moderately (κ=1: 0.0372 → 0.0489;
> κ=3 sharp: 0.358 → 0.388). The κ=3 member's kill-grade gating
> condition is discharged. A8's insertion marking stands whole: every
> number remains a property of GRUT-plus-the-declared-filter.**

## The corrected table (uncorrected beside every entry; B/C = the quotable window members)

| point | κ=1 uncorr → corr (B, C) | κ=3 uncorr → corr (B, C) |
|---|---|---|
| x = 1/16 (0.0625) | 3.43 → **2.60, 2.62** (kill confirmed) | 0.63 → 0.48, 0.48 |
| x = α² (0.111) | 6.24 → **4.87, 4.89** (kill confirmed) | 0.86 → **0.67, 0.67** (survival robust, gated) |
| x = α (0.333) | 18.51 → **15.83, 15.89** (kill confirmed) | 1.45 → 1.02, 1.03 |
| 2σ edge | 0.0372 → **0.0489** | 0.358 → **0.388** |

The diagnostic bracket (f^A, early-ISW left in the baseline) is looser
throughout (e.g. 1.74 at the 1/16 point) — reported, not quotable, as
chartered. The two quotable members agree everywhere to ≤ 0.016 in f:
the window-scale insertion is weak, as calibrated.

## The findings

1. **The net direction was a genuine measurement, and it resolved
   moderate-weakening.** The pre-freeze calibration had killed the
   naive "corrections only weaken exclusions" shortcut (the early-ISW
   cross-term *anticorrelates* at low ℓ, so f^B is negative there);
   the recorded run shows the high-ℓ suppression dominates the metric,
   so exclusions weaken by ~20–25% in σ and no verdict flips.
2. **The named finding (Amendment 01):** the record's memory-grade
   "~0.82–0.84 Boltzmann" D30/D2 reproduces under **no** tested
   convention or member (full TT 0.976; mono+full-ISW 0.377;
   mono+late-ISW 0.493). The A6 fence's *direction* and *O(signal)
   magnitude* were right (f^A reaches +1.93 at ℓ=30); its cited shape
   number was itself memory-grade and wrong — precisely the defect
   class this fork exists to close.
3. **Controls:** the frozen pipeline replicated in-run to its recorded
   constants; the harness validated per the amended window; the
   identities held exactly (f^A > 0 everywhere; the corrected metric is
   identically zero at x = 0).

## What this does and does not do

- It **discharges** the A6 owed item: the κ=3 member's kill-grade use
  is no longer blocked by the common-mode fence, and every consumer
  statement can now cite the corrected table.
- It does **not** repair the κ-filter insertion: the A8 demotion stands
  whole; every number here is GRUT-plus-an-unbanked-filter, and the
  activation-scale frontier (A8's two blocked inputs) is untouched.
- It moves **no register field** (v4 R2: consumption at the named
  nodes is the owner's adjudication).
- Run 1 is the recorded run; `defect_history` is empty; the only
  provenance event is the pre-run Amendment 01, disclosed.

## Proposed C3 channel line (for the owner's adjudication under v4 R2 — nothing executes here)

With A6 discharged, the first Part-7 front's channel (v4 C3) has, on
its own sealed text, two candidate readings — presented mechanically,
neither forced (R1):

- **Reading 1 — RESOLVED (a):** *"a register-grade window SURVIVES at
  one or more declared kappa-members"* — satisfied at both members
  (κ=3: everything below the corrected 0.388; κ=1: the window below
  the corrected 0.0489), with every insertion declared (the A8 record;
  this fork's declarations); ships as an **ALLOWANCE, never a
  prediction** (Q2: "The family ALLOWS up to the edge; it predicts
  nothing"); **no frozen reach threshold exists**, stated as C3(a)
  requires. Proposed deposit-form line: `C3 RESOLVED (a): register-
  grade window survives at the declared members (corrected edges
  0.0489 / 0.388, kappa = 1 / 3, sharp theta); ALLOWANCE per Q2;
  insertions declared per A8; A6 discharged at Boltzmann grade
  (A6_COMMON_MODE_RESULT.json); no frozen reach threshold exists.`
- **Reading 2 — STILL OPEN (mixed members):** C3's still-open causes
  include *"mixed members"*; the named-point verdicts are
  κ-conditional (killed at κ=1, surviving at κ=3), and the owner may
  judge that structure to be exactly what "mixed members" names —
  in which case the line is `C3 STILL OPEN: mixed members (named
  points kappa-conditional; window statement clean at each member;
  A6 discharged).`

The mechanical difference: Reading 1 treats the *window* (which is
clean at every member) as the resolving object; Reading 2 treats the
*named points* (which are member-dependent) as blocking. The sealed
text supports either; per R1 no resolved outcome is forced, and per R2
only the owner's adjudication, recorded in the canonical event log,
makes either operative.

**HARD STOP.** Verdict recorded pending owner ruling. (The second
Part-7 front, C5 — the ξ_ij/Γ_T calc — remains owed-or-retired and is
the natural next in-house work either way.)
