# tt_worldline_spectrum — result

**Date:** 2026-08-21 · **Code:** `calc/tt_worldline_spectrum.py` (stdlib only, ~3 s)
**Status:** computed; bears on the **POSEDNESS** of rung 3's spectral question in the
gravitational channel; **NOTHING BANKED — overseer relay required (CHARTER §5.3).**

> **SCOPE FENCE.** Class-A gravitational channel only (free TT-graviton BD two-point function
> along a comoving geodesic). Class C — the assembled interacting G_R^TT — is untouched
> (walls A–C stand). At free level the field is pure P^(2); P^(0,s) is nondynamical
> (constraints), so no feature can hide there — and nothing here constrains the P^(0,s)
> content of the assembled class-C response.

## What was computed

The exact BD mode-function pair (two polarizations, H = 1) integrated over the regulated band
[k_min, W_c] = [0.5, 50], giving G(Δ; t̄) — the worldline kernel at epoch t̄ and separation Δ.
Pipeline validated: the subhorizon band reproduces the flat-vacuum variance (1/π²)∫k dk
exactly (<5%).

## Finding 1 — the coincidence variance is strongly time-dependent

⟨h²⟩(t) decays ~e^{−2t}·(log) under the fixed comoving IR regulator (127 → 0.002 over three
e-folds in the printed window): canonical strain redshifts while frozen superhorizon modes
dilute. First direct evidence of non-stationarity in the gravitational channel.

## Finding 2 — the worldline kernel is NON-STATIONARY (the decisive result)

Normalized shapes of G(Δ; t̄) at three epochs differ by up to **134%**, including a change of
character (oscillatory-sign vs monotone-decay). Contrast: the conformal-scalar PROXY was
exactly stationary along the same geodesic (keystone map D3a). So:

- D3a's licensed cosmic-time clock exists for invariant fields, but **the graviton channel
  does not inherit it**: the minimally-coupled-like sector has no dS-invariant state, and its
  worldline kernel acquires epoch dependence (the known secular/IR structure of massless
  spin-2 in dS, here exhibited numerically from the mode functions rather than cited).

**Consequence: the registered class-A-style spectral analysis (ω-spectrum, pole-vs-cut,
single-pole) cannot be POSED for the gravitational channel without an epoch-window
approximation whose validity must itself be priced.** This answers the spec's central
question at the posedness level: the adverse proxy floor neither transfers nor is refuted —
it is **surpassed**: the gravitational channel lacks a stationary reduced object to compare.

## Finding 3 — no parameter-free memory time

Effective decorrelation times are non-monotonic across epochs (≈0.40 / 0.33 / 2.40 at
t̄ = 0.5 / 2.0 / 3.5): any extracted "memory time" is epoch- and regulator-controlled.
No derived τ_eff exists at class A for the graviton.

## Finding 4 — the epoch-window price, measured (spec hard gate executed)

Stationarity holds only for epoch windows **W < 0.25 e-folds** (10% shape tolerance) at every
epoch tested (t̄ = 1, 2, 3). The PRICE of the epoch-window approximation is therefore severe
and quantified:

- class-A spectral claims are restricted to **ω ≳ 1/W\* ≈ 4** and separations **Δ ≲ 0.25**;
- outside that window the registered analysis has no object.

## Finding 5 — the regulated class-A spectrum exists but is regulator-priced

With Hann-windowed Fourier transforms of G(Δ; t̄ = 2) per regulator:

| k_min | mean low-w band S (0.2 ≤ w ≤ 0.5) | sign-flips |
|---|---|---|
| 0.25 | 0.00074 | 0 |
| 0.50 | 0.00060 | 0 |
| 1.00 | 0.00046 | 0 |

- The regulated spectrum EXISTS, is positive, and is **amplitude-regulator-controlled**
  (2.3× across a 4× change in k_min).
- **Selftest correction (recorded, not hidden):** the draft claim "τ_eff tracks k_min" was
  FALSIFIED — τ_eff ≈ 0.33 with only ~3% spread across regulators. The regulator prices the
  NOISE LEVEL, not the decorrelation time; the EPOCH prices the decorrelation time
  (non-monotonic across epochs, Finding 3). Two different priced dependencies, previously
  conflated in one sentence — the exact laundering shape the process exists to catch.

## Net statement for rung 3 (class A, gravitational channel)

A regulated spectrum CAN be produced, but every number it contains — the floor amplitude
(k_min-controlled) and the decorrelation time (epoch-controlled) — carries a named, measured
dependence on a choice, not a derivation. **No parameter-free memory time or noise level
exists at class A for the graviton.** The registered J ∼ ω³ → single-pole chain therefore
cannot be executed in the gravitational channel at class A at any parameter-free strength.

## Limit-order disclosure (hard gate)

Order executed: IR regulator k_min FIRST (physical: horizon freezing), THEN worldline
restriction, THEN epoch window. The alternate order requires the massive-griton mode calculus
and was NOT executed — disclosed per the spec's firewall. k_min was fixed by the
epoch-freezing scale; no memory behavior entered its selection.

## Relation to the owner's outcome classes

Class **(e)**, with (c) as the fallback: the epoch-window approximation and the IR regulator
are the named, measured additional inputs; the memory behavior is not derived but
regulator/epoch-priced. It does NOT establish "GRUT's mechanism disproven" — it establishes
that **no parameter-free class-A gravitational spectrum exists**, and any rung-3 claim must
now either price these dependencies explicitly or move to class C (the dispatch re-pose, with
the keystone-map C7 clock disclosure upgraded).

## Draft ledger language (DRAFT — NOT APPLIED)

Candidate `tier_note` addition to `rung3_single_pole` (owner adjudication required):

> 2026-08-21 TT-WORLDLINE + EPOCH-WINDOW FINDINGS (calc/tt_worldline_spectrum.py, class-A
> scope): (i) the free TT-graviton geodesic kernel is non-stationary (shapes vary >130%
> across epochs; coincidence variance redshifts ~e^-2t under fixed comoving IR regulator);
> (ii) stationarity holds only for epoch windows W < 0.25 e-folds (10% tolerance), restricting
> class-A spectral claims to w >~ 4 and Delta <~ 0.25; (iii) the regulated spectrum's
> low-w amplitude is regulator-controlled (2.3x across k_min in [0.25, 1.0]) while the
> decorrelation time is epoch-controlled (non-monotonic 0.40/0.33/2.40). Conditional on
> screening: the pole-vs-cut question is NOT WELL-POSED in the gravitational channel at
> class A; any rung-3 export requires pricing the epoch window and the IR regulator as named
> inputs, or moving to class C. No ledger delta proposed here.

## Owner adjudication recorded (2026-08-21)

**Class A — CLOSED/EXHAUSTED for parameter-free rung-3 discharge. Class C — OPEN, DECISIVE.**
Ruling verbatim in `CLASS_C_DISPATCH_SPEC.md` §0; draft register language (i)/(ii) there.
No further class-A variations authorized unless answering a specific unresolved mathematical
objection. The keystone is routed to class C via `CLASS_C_DISPATCH_SPEC.md` (the re-posed,
clock-named dispatch); its HELD status transfers until pre-screen + owner authorization.
