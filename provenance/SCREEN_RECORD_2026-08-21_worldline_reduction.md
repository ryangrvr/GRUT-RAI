# Screen record — `calc/worldline_reduction.py` (2026-08-21)

> **Hostile pre-screen per CHARTER §1.3**, charged against the nine surfaces the owner named,
> defaulting to broken. The screen's own verification pass **falsified the shipped closed-form
> spectrum before it could be cited** — recorded below as the headline catch.

## Verdict summary

| # | attack surface | verdict |
|---|---|---|
| 1 | proxy choice (conformal scalar) | **FENCED, not resolved** — see A1 |
| 2 | BD-state choice | PASS at proxy scope; α-vacua excluded by the booked state |
| 3 | Gaussian truncation | consistent with the banked family (K = c2·P^TT + c0·P^(0s)) |
| 4 | normalization | one factor-2 error caught and fixed during development (half-line vs full-line transform); final pipeline validated against the exact half-line result to <3% |
| 5 | tensor-to-scalar correspondence | **NOT ESTABLISHED — the decisive fence**: nothing proves the conformal-scalar floor transfers to the TT channel |
| 6 | definition of the folded spectrum | validated against the register's own premise origin (ω³ reproduced exactly); both simple closed forms for the dS spectrum FALSIFIED by numerics |
| 7 | interpretation of S(0) | floor is real noise (FDT-locked), not a contact artifact: it survives every candidate form AND the ε→0 convergence study |
| 8 | s_eff → 0 inference | ROBUST — follows from any bounded-at-origin spectrum under the fold, independent of shape details |
| 9 | does the proxy represent the rung-3 gravitational channel? | **NO — unproven and doubted**: see A1/A5; this is the map's own wall-A fence restated |

## Headline catch (surface 6/4)

The draft's closed-form spectrum S = ω·coth(πω)/(2π) − 1/(4π²) was derived twice by hand with
conflicting signs. An independent ε→0 convergence study of the exact kernel (four ε values,
Richardson-extrapolated) falsified it at ω = 0.1 by 20% — and falsified the alternative pure
thermal line by 54%. The calc now presents the **converged numeric spectrum as the result of
record**, with both candidates' falsification printed on its face. Lesson recorded: a closed
form derived through sign-heavy residue manipulation is not "exact" until an independent
numerical path agrees with it.

## Robust core that survived every attack

- Positive horizon-forced floor S(0.1) ≈ 0.034 > 0 (T = T_dS fixed by rung2; not optional).
- Folded bilinear noise exponent → ~0 ≠ 3, on ANY candidate spectrum including the falsified
  ones (all are bounded at the origin; the fold result is shape-robust).
- [R_wl, R_IR] ≠ 0 in closed form; reduction order is load-bearing and must be priced.
- Pipeline validation against the exact flat half-line transform (<3%).

## Firewalls imposed (owner directive, 2026-08-21)

1. Forbidden phrasing: "GRUT's s=3 bath is disproven" / "memory mechanism disproven" / "the
   Ohmic floor solves the problem" / "the worldline kernel is the cosmological kernel".
2. Correct statement: *the registered J ∼ ω³ premise does not survive the D3a-licensed dS
   geodesic reduction in the stated BD conformal Gaussian proxy; class C is uncomputed.*
3. No exponent search may be conducted to find an s that produces a desired τ₀ — derive the
   spectrum first, its response second, accept the dynamics third.
4. Any C→A reduction claim must state whether IR regulation, worldline restriction, and
   point-particle limiting commute; if not, the chosen order needs physical justification
   selected independently of the desired memory behavior.

## Conditions for re-verdict

1. Independent check of the converged low-w spectral shape against published geodesic-detector
   response rates (source-verified into `sources.json` before citation).
2. Channel-tracking calculation: P^(2) vs P^(0,s) worldline reductions computed separately —
   the scalar proxy must not silently stand in for TT (owner surface 9).
3. The class-C spectral-measure specification (`RUNG3_SPECTRAL_MEASURE_SPEC.md`) executed or
   dispatched; until then the proxy result stays class-A-scoped.
