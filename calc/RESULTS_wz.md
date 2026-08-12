# Rung 7 — evolving w(z) from a finite-memory vacuum: result

**Date:** 2026-06-25 · **Code:** `calc/wz_dark_energy.py` (stdlib, <1 s)
**Status:** lead; structural result robust, DESI-matching shape **to-derive**. Independent of
the rung-8 falsifier's magnitude (the point — diversifies off single-point-of-failure).

## Goal
A second differentiator that does **not** depend on rung 8. A finite-memory vacuum has a
frequency-dependent χ(ω); out of equilibrium its effective w(z) can leave −1, which a
static-Λ time-symmetric family cannot do.

## What the calc shows

**(A) Which scale? — the decisive question.** w(z) deviates from −1 only if the vacuum has
response power at ω ∼ H(z).
- **UV-cutoff memory** (τ_c ∼ 1/ω_c, the confirmed single-pole scale): H₀τ_c ∼ 10⁻⁴⁰ →
  **w = −1 flat to ~80 decimals.** No evolution → **FAILS-DIFFERENTIATION** (reproduces Λ,
  inherits the cosmological-constant problem).
- Observable w(z) evolution **requires a second, slow scale τ₂ ∼ 1/H₀.**

**(B) The coupling to rung 3 — the main result.** That second scale is *exactly* the "second
internal bath scale" that the expert's single-pole confirmation forbids. They are not in
contradiction — **they coexist by scale separation:**
- τ₂/τ_c ∼ ω_c/H₀ ∼ 10⁴⁰. The IR pole is ~40 orders of magnitude slower.
- At **tabletop** frequencies (ω ≫ H₀) the IR pole is invisibly slow → kernel stays
  single-pole/cutoff-dominated → the expert's "no second scale" holds *where the tabletop lives.*
- At **cosmological** frequencies (ω ∼ H) the IR pole is active → w(z) evolves.

So GRUT can have **both single-pole (tabletop) and evolving w(z) (cosmology)** — but only by
committing to a **two-scale vacuum**: UV cutoff ω_c + IR horizon scale ∼H. A concrete, named,
falsifiable structural input. It ties rung 3, rung 7, and the kill-shot-#1 de Sitter crossover
(cosmology sits at ω ∼ ω* ∼ H) into one coherent picture. The IR scale ∼H is
horizon-motivated (de Sitter/Gibbons-Hawking), possibly natural rather than tuned — but
"why τ₂ ∼ 1/H *now*" is the cosmic-coincidence question to address.

**(C) Parameter economy — candidate win.** With τ₂ = 1/H₀ pinned by the horizon, w(z) is a
**one-parameter (ε) family**, so w₀ and w_a are **correlated** (w₀ = −1 + ε/2, w_a ≈ +0.23ε) —
a pre-registerable locus with fewer parameters than CPL's free (w₀, w_a).

**(D) DESI match — the embarrassing-direction check, reported straight.** DESI 2024-25 hints
w₀ ≈ −0.8 (>−1) **with w_a ≈ −0.6 (<0)** — w more negative in the past, a quintom crossing of
−1. **The simplest one-parameter relaxor does not match DESI** — because a single passive channel
cannot produce the **crossing** (needs ≥2 modes / a sign-changing response). *(Superseded
2026-06-29 by `rung7_w2`, `calc/RESULTS_wz_sign.md`:* the earlier "**w_a > 0, wrong sign**" reading
in this toy is **retracted** — the w_a **sign is frontier-indeterminate**; the second law fixes the
dissipative branch on the phantom *side* (w≤−1, which forbids the crossing) but **not** the w_a
*slope* (the toy's sign is a ζ=const artifact). The sourced prediction is w=−1 **flat**; the
no-crossing is the robust content, the sign is open.*) Not fitted around — flagged. A −1 crossing
likely needs two modes (adds a parameter, erodes the economy win) or a sign-changing in-in response.

## Status
Rung 7 stays **to-derive**. Structural second differentiator (w(z) evolution impossible for
the Λ family) ✓, but the DESI-matching shape is **not yet earned** and the simplest version
mismatches. Ledger **+2** (ε + the two-scale commitment). The two-scale vacuum is a new named
structural input.

## One-line question for the specialist
> Does the in-in (Calzetta-Hu) effective stress tensor of a relaxing vacuum with an IR
> horizon-scale relaxation give w(z) with w_a < 0 (quintom, DESI-like) or w_a > 0, for a
> single passive relaxor — i.e. can one slow pole cross w = −1, or does crossing require two
> modes?
