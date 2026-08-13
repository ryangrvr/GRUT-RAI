# Kill-shot #1 — finite-T spectral exponent: result

**Date:** 2026-06-25 · **Code:** `calc/finite_T_exponent.py` (stdlib only, runs in <1 s)
**Status:** lead computed; **awaiting specialist sign-off** — not a settled result.

## Question
Single-pole was graduated from "assumed" to "derived-at-DOS-level" via ω=c|k| → DOS∼ω² →
J(ω)∼ω³ (s=3 super-Ohmic → short memory). Does the finite-T FDT/KMS factor
coth(ħω/2kT) ∼ 2kT/ħω at low ω soften the effective exponent enough to restore **long
memory** and break single-pole in the regime where the observables (689 Hz, w(z)) live?

## Result — soften, not break
The standard QBM / Caldeira-Leggett calculation with a smooth UV cutoff, S(ω,T)=J(ω)coth(ω/2T):

| Diagnostic | Finding |
|---|---|
| Effective IR exponent s_eff | runs **3 → 2** across the crossover ω*=2T; lands at **exactly 2.000** for ω≪2T |
| Class | **still super-Ohmic** (s_eff=2 > 1, one notch above the Ohmic boundary); a single coth power cannot reach s_eff<1 |
| DC noise floor S(ω→0) | **→ 0 as ω²** at every T>0 — no white floor, no long-memory signature; amplitude grows ∝T |
| Noise memory time τ_ν | **flat: 1.60–1.72** over T ∈ [10⁻³, 10²] (ratio 1.07×) — set by the cutoff 1/ω_c, not by T |

**Scale map (which T, ω apply per rung):**
- **Rung 8 (689 Hz tabletop):** T = lab/environment temperature → ω/ω* ≈ 1.7×10⁻⁸ (at 1 K). **Deep thermal, s_eff=2.**
- **Rung 7 (cosmology):** T = de Sitter (T_dS = ħH/2πk_B) → ω/ω* ≈ 3. **At the crossover; s_eff drifts 2↔3**, so the w(z) shape is crossover-sensitive.

## What this does NOT settle (for the specialist)
1. Assumes the **standard bilinear QBM coupling** and the friction/noise split. A different GRUT coupling, or an observable governed by a different kernel combination, could make s_eff=2 vs 3 matter more.
2. s_eff=2 sits closer to Ohmic than s=3 — need the **explicit pole structure** of the s_eff=2 kernel (one dominant pole vs a slow+fast pair), not just the exponent, to confirm "single-pole."
3. The cosmological **crossover** is genuinely ambiguous; w(z) inherits that.

## One-line question for the specialist (same shape as the DOS question)
> For an s=3 super-Ohmic bath with a smooth UV cutoff, does the finite-T coth factor
> (S∼ω² in the thermal IR, S(0)=0) keep the noise kernel single-pole/short-memory, or
> does the s_eff=2 spectrum carry a slow second pole that the cutoff-set memory time hides?

## Consequence for the ladder
Rung 3 stays **derived-pending** (not promoted to shown). Rungs 7–8 may proceed on the
working assumption that memory stays cutoff-set (short), **pending** the pole-structure
sign-off. The falsifier recompute (kill-shot #2, energy basis) inherits the bandwidth from
here, so it is the correct next step.
