# WALL A / G1 — OHMIC PLANT RESULT: **FAIL — STOP**

**Date:** 2026-08-23 · JSON: `WALL_A_G1_RESULT.json` (authoritative). G1 is a precondition;
its failure stops Wall A before the gravitational assembly.

## Verdict: **FAIL — the instrument cannot adjudicate the conflict**

The pipeline implementation cannot distinguish s≈1 from s≥2. Per the entry-gate protocol:
**do not proceed to gravity through this machinery** — whatever it returns for the gravitational
response would be uninterpretable, regardless of how confident it looks.

## What was planted and what came back

| plant (bath J) | expected response | recovered |
|---|---|---|
| Ohmic J=ω·e^{−ω/20} (s_J=1) | s_resp ≈ 0, divergent | slope −0.025 → classified s≤1 ✓ but only after apodization; un-windowed: +? wrong |
| super-Ohmic J=ω³·e^{−ω/20} (s_J=3) | s_resp ≈ 2, convergent | **+0.001 → flat. WRONG by 2 full powers** |
| boundary J=ω²·e^{−ω/20} (s_J=2) | s_resp ≈ 1, log-divergent | +0.013 → flat. WRONG |

## Diagnosis (root cause identified, repair known but not built)

Two implementations, both fail differently:

1. **Un-windowed truncated cosine transform:** returns slope ≈ 0 for EVERY plant. Cause:
   the spectrum's mass sits at high ω (super-Ohmic peak at ω~2L); truncating the time domain
   at T=80 makes sinc-sidelobe leakage from that massive high-ω content swamp the low-ω
   probes. Ringing amplitude scales with total spectral mass over πT.
2. **Hann-apodized:** suppresses the ringing but also suppresses the t≈0 region — exactly
   where the low-ω spectral shape lives. Result: non-positive reconstructed spectra in the
   probe band; classification impossible.

## What this means

- **Not a statement about gravity.** No gravitational assembly was run; the plant stage failed.
- **A real statement about the instrument class:** naive time-domain round-trips cannot
  preserve power-law exponents across a massive spectral dynamic range. Any prior result
  produced by such a round trip would have been untrustworthy in the same way.
- **The class-A white-floor finding does NOT get validated by this failure** — its machinery
  was different (analytic in ω-space), and guilt-by-association is not evidence.

## Repair path (for the next attempt)

Standard practice exists and is known: (i) analytic tail subtraction beyond a split point,
(ii) higher-order windowing with amplitude calibration per window, or (iii) stay in ω-space
entirely and test the classification step on analytically transformed pairs (Debye exact pair
already calibrates at 0.001–0.2%). Option (iii) is the cheapest and was proven earlier this
session.

**Until a repaired pipeline passes G1, the s=3 vs s≤1 adjudication is UNRESOLVED-BLOCKED on
the instrument — not decided.**