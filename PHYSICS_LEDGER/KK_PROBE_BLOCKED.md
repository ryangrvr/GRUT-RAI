# KK/DOS Re χ sign-change probe — BLOCKED at calibration

**Date:** 2026-08-23. The bounded question (can GRUT's super-Ohmic Im χ shape support a Re χ sign
change, per Kramers–Kronig?) remains OPEN. The numerical principal-value integrator **failed its
own calibration** (Debye exact pair: errors 225–1011%) and was stopped before any physics reading,
per the discipline that no number ships from an unvalidated instrument.

## What is NOT blocked

The reframing itself is recorded and correct: Re χ is fixed by Im χ through KK, so "does GRUT's
spectral density support a Re χ sign change?" is a property of Im χ's shape alone — spectral
concentration vs smooth monotone decay. GRUT's DOS/super-Ohmic argument (J~ω³) is already such a
statement, so a validated integrator may answer it without the full Σ(x,x′) calculation.

## Unblock requirements

1. A PV integrator passing the Debye calibration to <2% at ω₀ ∈ {0.5,1,2,3}
   (subtraction scheme drafted in `kk_dos_signchange_probe.py`; error source not yet diagnosed).
2. Then: probe shapes — smooth super-Ohmic w³/(1+w)⁶ · super-Ohmic + narrow bump.
3. Outcomes: (i) no admissible shape flips Re χ ⇒ derived no-resonance constraint; no-crossing
   becomes physics. (ii) some shape flips ⇒ microscopic rung3 calculation genuinely required.

## Verdict

`NUMERICALLY UNVERIFIED-BLOCKED` on the integrator. No physics conclusion drawn either way.