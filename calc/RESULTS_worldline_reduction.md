# worldline_reduction — result

**Date:** 2026-08-21 · **Code:** `calc/worldline_reduction.py` (stdlib only, ~1 s)
**Status:** computed; **adverse to `rung3_single_pole`'s super-Ohmic premise at class-A scope;
NOTHING BANKED — overseer relay required (CHARTER §5.3) before any register edit.**

> **SCOPE FENCE (read first).** Class C — the assembled graviton Σ(x;x′) — is UNCOMPUTED
> (wall A of `RUNG3_KEYSTONE_MAP.md` stands untouched by this file). What was reduced is the
> FREE dS two-point function along a comoving geodesic — the massless conformal-proxy BD
> kernel, exactly stationary in cosmic proper time per keystone-map D3a — through the same
> operation the booked family would undergo. Every statement below is about that PROXY at
> class-A scope.

## What was asked

The owner authorized one calculation: perform the C→A worldline reduction on the booked
(K_R, N) family, track what survives, and treat the point-particle-vs-IR limit order as a
first-class kill condition (`[R_wl, R_IR]` test).

## Result 1 — where ρ ∼ ω³ actually comes from (machinery validated)

The flat-space, T = 0 bilinear fold has the EXACT truncated form

    N(w; Lam) = (1/4 pi^2) [ Lam^3/3 - Lam^2 w/2 + w^3/6 ],

verified numerically to rel.err ~ 1e-11 at three w. The memory-carrying NONANALYTIC piece is
w³/6: rung3's s = 3 premise is real, but it is a **zero-temperature flat-space artifact** —
both fold factors vanish linearly at w = 0 only because T = 0 empties the thermal occupation.
The analytic pieces are local/contact content.

## Result 2 — the dS worldline-reduced kernel has a horizon-forced white floor
### (the adverse finding) — and both simple closed forms for it are FALSIFIED

Along the geodesic, the BD kernel is
g(τ) = −(H²/16π²) csch²(H(τ−iε)/2) (flat limit recovered; KMS period 2πi/H by construction).
Its symmetrised worldline spectrum was computed by direct quadrature of the exact kernel on an
ε-resolved grid (pipeline validated: same code path reproduces the EXACT flat-kernel half-line
result (ω/2π)e^{−εω} to <3%), with ε-extrapolation as the result of record:

    w:      0.10     0.20     0.50     1.00     2.00     4.00     8.00
    S(w): 0.03393  0.04443  0.08306  0.15905  0.31671  0.63019  1.24730   (H = 1)

Gates passed: strictly positive floor at w→0 (S(0.1)=0.034 > 0; T = T_dS is rung2-fixed, not
optional); approach to the flat-vacuum line w/2π at high w (ratios 0.99, 0.98); **both simple
closed-form candidates FALSIFIED at w=0.1** — candidate A (w coth πw/2π − 1/4π², the shipped
draft's own formula) misses by 20%, candidate B (pure thermal line, no contact) by 54%. The
low-w shape is neither: it is a distinct floored spectrum whose exact analytic form is
UNRESOLVED and flagged for independent verification against the published geodesic-detector
response literature before any export.

What survives every candidate AND the numerics (the robust core):
- **finite horizon-forced floor**: the temperature is rung2-fixed (T = T_dS), not optional,
  so the floor cannot be switched off within class A;
- **folded bilinear noise**: s_eff(low-w) → ~0, against the registered 3;
- therefore the registered premise J(ω) ∼ ω³ does not survive the only reduction whose clock
  is licensed. This EXTENDS the banked 2026-06-25 finite-T softening (s_eff 3 → 2 from the
  STAKED flat-space J): the reduction removes the super-Ohmic leg itself.

Equally fenced, both directions: this is **not** pro-GRUT either. A white floor is zero-memory,
contradicting the FINITE-memory claim as much as it contradicts s = 3; and it is NOT a verdict
on class C, where the graviton TT channel's own spectral measure is uncomputed. The honest
statement: **the registered kernel and the reduced proxy kernel are different objects; any
memory claim must be re-derived from the reduced object or from class C directly.**


## Result 3 — [R_wl, R_IR] ≠ 0 (exact)

int₀^∞ cos(kL)/(k²+m²) dk = (π/2m)e^{−mL} gives
lim_{m→0} lim_{L→∞} = 0 but lim_{L→∞} lim_{m→0} = ∞. The worldline/point-particle operation
and the IR operation do not commute on exactly the integral structure the reduction contains.
Any C→A map must SPECIFY ITS ORDER and price it; particle-first silently deletes dS IR content
— precisely where rung3's candidate memory scales live (τ₂ ~ 1/H₀, ladder spacing H).

## Draft ledger language (DRAFT — NOT APPLIED — for the bank gate)

Candidate `tier_note` addition to `rung3_single_pole` (owner adjudication required):

> 2026-08-21 WORLDLINE-REDUCTION FINDING (calc/worldline_reduction.py, proxy scope): the
> super-Ohmic input J ~ omega^3 is recovered only as the zero-temperature flat-space
> nonanalytic fold; the D3a-licensed dS worldline reduction of a free proxy is Ohmic-thermal
> with a horizon-forced floor S(0) = 1/(4 pi^2), folded s_eff -> 0. Conditional on screening:
> the DOS step of this node's justification chain does not transfer to de Sitter at class-A
> scope, and [R_wl, R_IR] != 0 makes reduction order load-bearing. Does NOT touch class C
> (wall A). Candidate re-tier: derived-pending -> pending on TWO named inputs (bath regime
> AND dS DOS step); no ledger delta proposed here.

## What this does NOT do

- Does not touch class C; wall (A)–(C) of the dispatch stand.
- Does not validate or refute the single-pole ANSATZ itself at class C.
- Does not bank anything; requires adversarial pre-screen (CHARTER §1.3) and overseer relay
  (§5.3); register untouched by this file.
