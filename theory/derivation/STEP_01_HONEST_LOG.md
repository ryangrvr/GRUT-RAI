# STEP 01 — Honest Log: What happened and what it means

**Date:** April 2026
**Outcome:** Caught my own error before it contaminated the derivation.

## What I did

I wrote `grut/derivation/step01_heat_kernel_s4.py` to derive the free-field
|b/a| ratio on S⁴ for SM content. The script used per-species Birrell-Davies
coefficients:

- `b_scalar = 1/360`
- `b_fermion = 11/360`  ← WRONG
- `b_vector = 31/180`

The result was `R = b_SM / a_SM = 253/219 = 1.155251` for Convention A
(n_S = 4, n_F = 24 Dirac, n_V = 12).

This number matches the target ε_combined = 1.1537 to 0.2%. Had I stopped
here, I would have concluded: "The free-field Birrell-Davies ratio for SM
content with Dirac neutrinos is 1.155, matching the cosmological constant
observation — the 12.5% gap was an error in earlier analysis."

## What actually happened

I cross-checked against `grut/foundation/anomaly_derived.py`, which has
been in the repository since the project's early days:

```
COEFF_DIRAC['b'] = Fraction(-11, 720)
```

Note: **11/720**, not 11/360. The correct per-Dirac-fermion Euler-density
coefficient is half what I wrote.

This is a standard result from Birrell-Davies Table 6.1 / Duff 1994 Table 1:
the Euler coefficient for a Dirac fermion is 11/720 (or equivalently,
22/720 = 11/360 for a Weyl fermion).

Different sources use different conventions:
- Per Weyl fermion: b = 11/360
- Per Dirac fermion: b = 11/720 (two Weyl species)

I mixed conventions: used the "Weyl" b-coefficient while counting Dirac
species. That inflated b by exactly a factor of 2, which gave R = 1.155
instead of the correct value near 1.00-1.03.

With the correct coefficients, the actual SM free-field values are:

- **Weyl neutrinos** (3 left-handed, N_f = 45/2): R = 3487/3396 ≈ 1.0268
- **Dirac neutrinos** (3 right-handed added, N_f = 24): R = 220/219 ≈ 1.0046

Both are in the ~1.00-1.03 range. The "12.5% gap" is real. The "1.155 match"
from my Step 01 was a coefficient-transcription error.

## Why this matters

This is exactly the kind of hallucination the GRUT-RAI honesty protocol
is designed to catch. A number that matches the target to 0.2% is the
most dangerous kind of output because the reviewer wants to believe it.

**I caught this one.** The cross-check against `anomaly_derived.py` was
automatic because that module was in the repository. If the audit had been
entirely within my own script, I might have shipped the wrong answer.

The lesson: **every step in this derivation must be cross-checked against
a source that is NOT under my own control.** Wolfram Engine output can be
wrong if I set up the problem wrong. Sympy output can be wrong if I type
the wrong coefficient. The safety net is:

1. Published literature (Birrell-Davies Table 6.1 explicitly)
2. Independent implementations (GRUT's own `anomaly_derived.py`)
3. Physical sanity checks (R within observational window before Osborn
   corrections? Expected to be ~1.00-1.05 for free fields, not 1.15)

## The real Step 01 result

The correct free-field |b/a| for SM content is:

- **R = 3487/3396 ≈ 1.0268** (using 3 Weyl neutrinos, N_f = 45/2, which is
  the convention matching GRUT's a = 283/120, b = 3487/1440)

This is the BASELINE. It is the starting point for the full derivation.
The observed value Ω_Λ = 0.69 requires R closer to 1.15, which is a
12.5% gap relative to the free-field baseline.

That gap is what the epsilon identification is supposed to close through
the Osborn coupling-dependent correction. The observation of Step 01 —
the Weyl tensor vanishes on S⁴, so only b (Euler) contributes to the
bulk anomaly, possibly with coupling corrections — remains valid and is
the right framing for Steps 02 onward.

## Status of Step 01

**RE-STARTED under corrected conventions.** The result:

- Baseline free-field R = 1.0268 (for SM with Weyl neutrinos) — DERIVED
- Only b contributes on S⁴, not |b/a| ratio — STRUCTURAL (geometric)
- Coupling corrections (Osborn ε) are the mechanism that could shift b
  upward by the required 12.5% — STRUCTURAL claim, to be checked in
  Steps 03-06

## Takeaway

The honesty protocol worked. I generated a spurious "match," caught it
within one turn, and now have a cleaner starting point for Step 02. The
alternative — celebrating a 0.2% match and building the next five steps
on top of it — would have been catastrophic.

Every subsequent step will include this kind of external cross-check
before proceeding.
