# Rung 4 — GW dissipation from Im[χ]: result

**Date:** 2026-06-25 · **Code:** `calc/gw_dissipation_bounds.py` (stdlib, <1 s)
**Outcome: (B) — real-but-unobservable.** Independent of rungs 7 and 8.

## The honest question
Not "extract a bound" but "is there anything to bound?" A finite-memory vacuum has a
dissipative Im[χ] (KK partner of the elastic Re[χ]); a GW through it would pick up
frequency-dependent attenuation and v_g(ω) ≠ c — absent in lossless GR. But the
Planck-suppressed vacuum that keeps GRUT solar-system-safe likely makes this tiny.

## GW170817 speed bound — checked first (it is not binding)
Predicted |v_g − c|/c ∼ |Re[χ]|/2 = **1.7×10⁻⁴¹** (q=1) / **5.7×10⁻⁸²** (q=2) at 100 Hz.
Observed bound |c_gw − c|/c < 10⁻¹⁵. **Consistent with 26–66 orders to spare** — the model is
nowhere near the GW170817 bound; the bound does not falsify it and is not the binding constraint
(the effect is far beneath it).

## The ratio — the answer
Predicted accumulated dephasing over D_L = 40 Mpc vs the ~0.1 rad detectability threshold:

| q | Im[χ]∼(ω/ω_c)^q | Δφ at 100 Hz | Δφ/threshold | orders too small |
|---|---|---|---|---|
| 1 (thermal s_eff=2) | (ω/ω_P)¹ | 4.4×10⁻²³ rad | 4.4×10⁻²² | **~10²²** |
| 2 (bare s=3) | (ω/ω_P)² | 1.5×10⁻⁶³ rad | 1.5×10⁻⁶² | **~10⁶²** |

Across the whole 10–1024 Hz band the effect stays 21–62 orders below threshold (it grows with
ω but never approaches detectability).

## The live window, and why tuning can't reach it
For GW dissipation to be a real differentiator, |χ| would need to sit in **[8×10⁻²⁰, 2×10⁻¹⁵]**
(above the 0.1-rad detectability floor, below the speed-bound ceiling). GRUT predicts |χ| ∼
10⁻⁴¹ (q=1), **21 orders below the window**. To reach it, the vacuum cutoff would have to drop to
ω_c ∼ MeV (q=1) or meV (q=2) — which would give the vacuum dynamical structure at those energies,
grossly excluded by particle-physics and equivalence-principle tests. **You cannot tune into
detectability without breaking everything else** — the anti-laundering guard holds.

## Consistency
The effect grows with ω, so solar-system tests (orbital μHz–mHz) are even more suppressed than
LIGO. "GW effect tiny" and "solar-system safe" are consistent — both Planck-suppressed, GW less
so. No regime where the GW effect is large while solar-system is safe → no tell of an error. The
smallness is **structural**.

## Verdict
**GW dissipation is ruled out as the second differentiator** — real but ~22–62 orders too small
for current or any foreseeable detector. This does **not** weaken GRUT: the same Planck
suppression underwrites solar-system safety. Reported straight, with the number; no manufactured
bound. Rung 4 stays tier `shown` (KK structure), differentiator stamped **FAILS-DIFFERENTIATION
(real-but-invisible)**, ledger 0 (no new input, no working observable).

**Consequence for diversification:** the search for a second observable independent of rung 8 is
**not yet successful**. GW dissipation is out; the remaining lever is an FDT-violation noise
excess out of equilibrium (longer shot), or accepting that GRUT's empirical distinctness rests on
the energy-basis falsifier (rung 8, magnitude-uncertain) plus the structural rung-7 w(z)
(DESI-shape to-derive).

## One-line question for the specialist
> For a Planck-cutoff super-Ohmic vacuum, is the GW dissipative response Im[χ(ω)] genuinely
> suppressed by (ω/ω_P)^q with q ≥ 1 (unobservable by ~22+ orders), or is there an enhancement
> (resonant bath mode, coherent build-up over D_L, lower effective cutoff) that lifts it toward
> the [10⁻¹⁹, 10⁻¹⁵] live window?
