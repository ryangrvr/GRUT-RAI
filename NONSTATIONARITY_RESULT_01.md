# NON-STATIONARITY MEASUREMENT — REPORT

**Date:** 2026-09-25 · **Charter:** `NONSTATIONARITY_CHARTER_01.md`,
pre-registration frozen at commit `eb3fc07` before the run · **Instrument:**
`calc/kernel_nonstationarity.py` (reuses the transport instrument's validated
integrator unchanged) · **Artifact:** `KERNEL_NONSTATIONARITY_RESULT.json`
(sha `19fa44a18990e0f8…`) · **Battery: 7/7** (flat exact-zero control 1.7e-14;
dS comparator spot-check 1.5e-16; Wronskian 5.5e-13; zero cells dropped).
**Measurement only** — no transport rule proposed, no discriminator
evaluated, no register change; fenced routes untouched.

## THE MEASURED ANSWER TO THE BOXED QUESTION

**How large is K(t,t′) − K(t−t′) on the stored exact FRW solutions?
Order unity.**

- **M1 (same-lag drift, headline):** the maximum relative same-lag drift
  over the reportable cells is **1.531** (at k = 0.5, lag 0.4/H₀); every
  reportable cell sits between **1.17 and 1.53** — the kernel's value at
  fixed lag changes by more than its own mean magnitude as the anchor time
  moves across z_a ∈ {0, 0.25, 0.5}.
- **M2 (best-stationary residual):** pooled **R = 0.516**
  (R = 0.535 / 0.522 / 0.457 at k = 0.5 / 1 / 2): **no Δt-only function can
  carry even half of the kernel's sampled variation.** This is the D3b
  obstruction as a measured quantity.
- **M3 (excess over the dS comparator):** the dS(H₀) comparator itself
  drifts at n2 ≈ 0.99 across the grid — the fixed-comoving-k redshifting-
  label effect disclosed at pre-registration — and FRW **exceeds** it by
  **0.17 at lag 0.1/H₀, 0.24 at 0.2/H₀, 0.54 at 0.4/H₀** (max 0.540). The
  FRW-specific, background-evolution part of the non-stationarity is a
  17–54% effect over the measured lags, growing with lag — consistent with
  the transport instrument's validity domain (licensed at 0.24/H₀,
  degrading beyond).

Observed pattern, reported without interpretation: the drifts are nearly
k-independent at the two shorter lags (columns for k = 0.5, 1, 2 agree to a
few percent) and mildly smaller at k = 2 for the longest lag. Three of nine
cells (all at lag 0.1/H₀) fall below the frozen 0.1 reporting floor and are
printed but excluded from the headline per the pre-registered rule.

## WHAT THIS FIXES IN THE RECORD (measurement report language only)

- **Stationarity, previously "not established," now carries a magnitude:**
  at cosmological lags the exact free kernel is a genuinely two-time object
  at order unity, with the FRW-specific share measured against the declared
  maximally-symmetric comparator.
- The D3b obstruction and the "proved stationary reduction" prerequisite
  (Decision C item 3; transport verdict T-III item iii) are now quantified
  obstacles, not qualitative ones: any future stationary-reduction claim
  must explain away a measured R ≈ 0.5.
- The scope caveat travels with the number: this is the fixed-comoving-k
  mode kernel. The worldline position-space object (the one D3a makes
  stationary on dS) requires a smearing choice — named at pre-registration,
  not taken; its measurement would be a separate, equally bounded
  instrument if the owner ever wants it.

## DEFECT HISTORY (disclosed)

Run 1 halted in the flat control: on a flat background the scale factor
never grows, so the integrator's `a_end` termination guard exited before a
single step; the control now runs on the step-count guard. No other defects;
no post-run edits to any reported quantity.

## HARD STOP

The measurement is recorded. The record state of
`KERNEL_TRANSPORT_OWNER_RULING_01.md` §4 updates one line:
**"Magnitude of nonstationarity: next bounded measurement" → measured
(headline 1.53 relative; excess over dS up to 0.54; R = 0.516).**
The decision this stop waits on: the owner reads the magnitude and decides
what, if anything, it changes about the fenced queue
(Λ_R, Matsubara, Π₀, U5 — all still fenced).
