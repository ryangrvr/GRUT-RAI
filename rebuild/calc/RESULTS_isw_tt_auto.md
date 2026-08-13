# The TT-auto gate: computed, voided by its own firewall, rebuilt, re-frozen

*Code: `calc/isw_tt_auto.py` (pure stdlib; exact line-of-sight SW+ISW transfer, per-mode filtered growth, spherical Bessel; self-tested with large-argument Bessel validation). Pipeline P1–P5 pre-registered and frozen 2026-08-03; **first-freeze constants VOIDED by the firewall same-day** (numerical noise); re-frozen under amendment record A1–A7 with the fix verified against the firewall adjudicator's independent harness (mpmath ground truth; κ=1 LR edge agrees to 4 decimals). The re-freeze is legal: verified pre-candidate — no R1/rung3 x\* computation exists in the repo.*

---

## The gate (re-frozen record, exact-CV-likelihood metric)

| quantity | value |
|---|---|
| **Unconditional bound** (most conservative corner: sharp θ-filter, κ=3) | **x < 0.358** — any computed x\* above this is dead at every declared pipeline member |
| κ=1 member (2σ edge) | **0.037** (band 0.037–0.041 over all KC corners) |
| κ=3 member (top-crossing 2σ edge) | **0.358** sharp-θ; **0.149** smoothed (W=0.5 in ln k) — band [0.149, 0.358]; **N(x) non-monotone** there (dip ≈0.34σ near x≈0.25): the full curve, not the edge, is the quotable object |
| unfiltered diagnostic (κ=0; not quotable — contradicts the banked separate-universe result) | 0.018 |
| pipeline validation | ΛCDM ISW share of low-ℓ TT: 0.23 at ℓ=2 (in the literature range; the ℓ=10 value 0.08 sits *below* the ~0.10 floor — fenced under A6, selftest gates on ℓ=2) |

**Named-point adjudications — all κ-conditional below the unconditional bound:**

| point | κ=1 | κ=3 (sharp) | κ=3 (smoothed) | verdict |
|---|---|---|---|---|
| the retired 1/16 (0.0625) | 3.4σ | 0.63σ | — | κ-conditional |
| **x = α² (0.111)** | **6.2σ** | **0.86σ** | 1.37σ | **κ-conditional** |
| x = α (0.333) | 18.5σ | 1.45σ | — | κ-conditional |

**KC-band:** n_s ∈ {0.95, 0.97} and Ω_m ∈ {0.28, 0.35} move the edges by <1% — normalization is not a lever. **The filter is the entire systematic**: κ (activation threshold) and the crossover sharpness together span the ~10× spread. 

## The amendment record (what the firewall caught — all three lenses + adjudicator, RED → rebuilt)

**A1 (the void):** the Bessel Miller-recurrence start ignored the argument; the LOS reaches x = kχ ≈ 124 where the routine failed by factors up to ~250×. Every first-freeze constant (0.035 edge, "21σ/212σ dead on arrival", the 0.23/0.10 validation split) was noise — the adjudicator showed the "edge" moved 0.035 → 0.27 on one resolution doubling, and the hoped-for model/baseline error cancellation was refuted by direct computation. The one-line fix is verified to 4e-11 against mpmath to x=128; the frozen resolutions are converged (~0.03%) post-fix. The selftest hole (only x=7.3 tested) is closed with x ∈ {0.1, 7.3, 60, 128} closed-form checks. **A2:** the original P1 claim "a likelihood-ratio treatment is stronger → conservative" was inverted — the exact CV likelihood N²_LR = Σ(2ℓ+1)[1/R + ln R − 1] is strictly *weaker* than the Gaussian for any R ≠ 1; it is therefore the conservative, quotable metric and is now primary. **A3:** modes filter-active at recombination now start on the μ-consistent growing mode. **A4:** non-monotonicity at κ=3 recorded; the accidental monotonicity selftest replaced. **A5:** the κ-lever *is* the verdict — pre-adjudications flipped from "all dead" (corrupted numbers) to "all κ-conditional" (corrected). **A6:** the "common terms cancel in the difference" fence is **load-bearing** at κ=3 (omitted early-ISW/Doppler power deflates C_obs by tens of percent at the dominant ℓ; the pipeline's D30/D2 = 0.62 vs ~0.82–0.84 Boltzmann, memory-grade) — a **Boltzmann-grade differential check is OWED before any κ=3 kill-grade use**. **A7:** the KC-band run and recorded (above).

## What the gate can and cannot do (the honest statement for the X_FLOOR decision tree)

- **Can, unconditionally:** kill any computed x\* > 0.358. Bound the family: μ−1 < ~0.12 at every declared member — which already **supersedes the lensing 0.59 loose-upper as the binding computed channel** (a second binding inversion, pending overseer-verified propagation).
- **Can, κ-conditionally:** kill x=α² (6.2σ) and everything above ~0.04 *if* the activation scale is κ≈1-class; nothing below 0.36 *if* it is κ≈3-class with a sharp crossover.
- **Cannot, yet:** deliver an unconditional verdict on the natural points. The residue is one named physics question — **where does the quasi-static P⁰ˢ response activate?** — plus the A6 common-mode check. Constructive note (for the overseer): the activation scale may be GRUT-derivable rather than a generic-validity guess — the response kernel carries its own banked memory structure; if the kernel fixes the crossover, every κ-conditional verdict becomes unconditional. That question is proposed as a named owed item of the x-floor front.
- **Never:** vote for x=0. A bound with no floor selects nothing (the window-shrink fence stands).

## Banking status

**HELD — nothing from this calc propagates** into `mu_slip_interior.py`, the harness, or claims.json until: the overseer verifies the re-frozen record, the A6 common-mode check is scheduled or fenced at consumer level, and the propagation plan (the second binding inversion; the window ceiling μ−1 ≲ 0.12 unconditional / ≲ 0.013 κ=1-conditional) is blessed. The retraction of the first-freeze numbers (0.035 / 21σ / 212σ) is on record in the overseer relay.

---

## A8 DEMOTION (2026-08-09) — appended, per the κ wave

**The headline "UNCONDITIONAL x < 0.358" is superseded.** Three independent defects (full record: `provenance/prereg/RESULT_KAPPA_2026-08-08.txt`; amendment A8 in the calc header):

1. **Range unbounded** — no upper bound on κ exists in banked physics; the edge loosens without limit (0.55 / 0.90 at κ = 10 / 30, triple-replicated). "Unconditional" was scan-relative (κ ≲ 6).
2. **Form excluded** — the sharp θ-step is not the k-dependence of any causal finite-memory kernel (Paley–Wiener-grade); banked structure is low-pass and cannot produce horizon-tracking activation. **No replacement licensed** (not W≈0.5, not F = C·u²; both need in-house bath choices — the CHARTER §3 automatic fail).
3. **Insertion, not scheme** — P2 is exact line-of-sight; `act()` edits the prediction; there is no quasi-static approximation in this pipeline to guard. The filter is an **unbanked world-model insertion**, and the ISW signal's central 68% (k/aH ∈ [1.7, 15.7]) sits exactly where the register is silent.

**Quotable object now:** *x < 0.358 conditional on the declared filter family (sharp θ, κ ≤ 3); no unconditional x-bound exists from this gate pending the activation-scale frontier.* Every number this gate emits is **insertion-contaminated** — a property of GRUT-plus-filter, to be declared by any consumer, never inherited. Surviving floors: κ ≥ 1 (a floor, never a value); A6's Boltzmann-grade check still precedes any κ=3 kill-grade use.
