# GR2-d2 — VERDICT

**Date:** 2026-09-27 · **Charter:** `GR2D2_QCONE_CHARTER_01.md`, frozen
at `75f2069` **before** implementation and run · **Authority:**
`GR2D_OWNER_RULING_01.md` (narrow authorization: a re-charter of GR2-d
gate Q-2 only) · **Instrument:** `calc/gr2d2_qcone.py` (pure stdlib; no
RNG) · **Artifact:** `GR2D2_QCONE_RESULT.json` (sha
`b512cbeef1a9eec2…`) · **Battery: 9/9 gated checks, zero failures,
zero halts, in the recorded run.**

## THE VERDICT — D2-QCONE-DISTINCT

> **Two earned-admissible quantum sectors of the record's own chain
> family, analytically separated before measurement (exact
> transverse-field velocities 1.809 vs 1.000, ratio 1.809), exhibit
> measurably distinct causal cones under thresholds frozen blind before
> the targets were ever measured. Quantum causal-cone distinction is
> demonstrable within the tested class. The irreducibility
> demonstration for the cone coordinate is strengthened: locality +
> influence + geometry + memory + quantum dynamics ⇏ c_universal.**

## The owner's three pre-run gates, as executed

1. **Parameter separation (P-1, before any front leg):** targets
   C = (1.0, 0.9045, 0) and D = (0.5, 0.9, 0) are pure transverse-field
   members of the record's chain family, where the quasiparticle
   velocity is exact; the instrument recomputed v_C = 1.809000 and
   v_D = 1.000000 from the dispersion on a k-grid before measuring any
   front. D is not a rescale of C.
2. **Procedure calibration (RQ-1..3, halt-grade):** the estimator
   replicated, digit-exact, the GR2-d recorded sector-A table (0.05,
   0.45, 0.90, 1.40, 1.90) and both disclosed non-target calibration
   tables (E2, analytic v 1.2, systematic ×1.2723; E3, analytic v 1.5,
   systematic ×1.2232). The calibration never touched the targets.
3. **Blind separation (S-1/S-2, thresholds frozen in the charter):**
   - S-1: fitted-slope ratio = **1.5111**, inside [1.5, 2.1].
   - S-2: |t\*_C(5) − t\*_D(5)| = **0.95** > 0.25·max = 0.700 — the
     GR2-d Q-2 form at 2.5× the threshold that failed there, passed
     with 36% headroom.
   - S-3: both targets earned-admissible — fronts strictly outward
     (C: 0.05, 0.45, 0.90, 1.35, 1.85; D: 0.10, 0.65, 1.35, 2.05,
     2.80), identical interaction graphs, ground-state Gram PSD for
     both. **The different-cone sector D survives the entire earned
     battery: 0 of 1 eliminated.**

## Margin disclosure (nothing hidden)

S-1 passed **thinly**: 1.5111 against a floor of 1.5. The estimator's
fast-side systematic compresses the ratio more than the calibration
drift suggested — measured v_est was 2.2222 for C (systematic ×1.228,
consistent with calibration) but 1.4706 for D (systematic ×1.471, well
above the ×1.27–1.29 extrapolation; the slow sector's precursor lag is
proportionally larger on a 7-site chain). Both frozen gates were set
before the targets were measured and are reported exactly as they came
in: S-1 thin, S-2 comfortable. Had S-1 come in at 1.49, the hard rule
would have recorded D2-QCONE-INDISTINCT with no parameter
re-selection; it did not.

## What this establishes — and what it does not (frozen consequence discipline)

- **Established:** quantum causal-cone distinction is demonstrable
  within the tested class. Together with GR2-d's accepted classical,
  exchange, relabeling, and memory legs, the different-cone
  alternatives now include an explicitly quantum pair that everything
  earned admits — the supplied status of causal structure is
  considerably harder to dispute.
- **Not established:** the universal cone is not thereby derived — no
  earned discriminator eliminating the different-cone alternatives
  exists anywhere in the record, and none was produced here.
- **Untouched:** GR2-d's D-PARTIAL and its V-2/V-3 failures stand at
  recorded strength; they are not retroactively flipped. No red gate
  moves; no public-record status moves; the public paper is not
  updated.

## Provenance

Run 1 is the recorded run; no halts; `defect_history` empty; the
classical, exchange, relabeling, and memory legs were not re-run
(adjudicated in GR2-d, per the narrow authorization). **Scope:**
exactly the GR2-d quantum-leg construction — 7-site open chains, D = 1,
the X-commutator front estimator.

**HARD STOP.** Verdict recorded pending owner ruling. The chartered
GR-2 sequence (L6, a, b, c, d, d2) is now complete pending the owner's
ruling on this record and the Layer-7 campaign synthesis.
