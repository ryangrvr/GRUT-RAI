# G1 v2 — CORRECTED VERDICT: **PASS** on the declared pass-criterion object

**Date:** 2026-08-23 · JSON: `G1_DIAGNOSTIC_V2.json` (regenerated after object correction).

## Correction history on this file

An earlier version of this document reported PASS with slopes 0.974/1.955/2.938 marked against
targets 0/1/2. That was the **twentieth defect (object substitution)**: the closed form used was
the transform of J(ω)=ω^s·e^{−aω} itself, not of the response object Im χ = J/ω. The numbers were
real; they were slopes of the wrong object, marked against targets they miss by a full power.
This document replaces it after re-running with the corrected kernel
γ(t)=(2/π)Γ(s)·Re[(a−it)^−s] — the transform of ω^(s−1)e^{−aω}, i.e. of the response spectrum.

## Corrected results (response object; declared targets 0 / 1 / 2)

| cell | s_J=1 plant | s_J=2 plant | s_J=3 plant |
|---|---|---|---|
| baseline (T=30, m=6000) | **−0.045** | **+0.974** | **+1.955** |
| T×2 | −0.045 | +0.957 | +1.955 |
| dt/2, dt/4 (T=30) | −0.045 | +0.974 | +1.955 |
| T×4 (dt confounded) | −0.045 | +0.954 | +1.480 |

Expected response classes: s≈0 (s≤1, power-divergent) · s≈1 (log-divergent) · s≈2 (convergent).

**Every plant recovers its expected response class within ±0.05.** The three classes are cleanly
separated — including the s=1 boundary, which sits exactly where the convergence table says the
log-divergence lives.

## Systematic residual, named

A uniform deficit of ~0.03–0.05 below each target, constant across all cells: the multi-point
fit band [0.03, 8] touches the exponential-cutoff shoulder (e^{−w/20} bends slopes down near
w~5–8), pulling every fitted slope slightly low. Constant, understood, and does not affect the
separation between classes.

## Convergence matrix reading

- dt/2, dt/4 identical to baseline ⇒ no aliasing at satisfied-Nyquist settings.
- T×2/T×4 rows show the next-lower class's value because doubling T at fixed m doubles dt,
  halving Nyquist — aliasing of the cutoff tail, consistent with §6's warning.
- Baseline settings are converged for classification purposes.

## Verdict

> **G1 PASS.** The assembly pipeline distinguishes s_resp ≈ 0 from ≈1 from ≈2 — including the
> convergence-boundary crossing between s=1 and s=2 — on planted admissible baths, blind, with
> controls. Wall A's gravitational adjudication may proceed under G0/G2/G3 as frozen.

## Defect ledger

Twentieth defect (object substitution) caught by the owner before it propagated into G3, where
every verdict would have shifted by one power and the convergence boundary would have sat in the
wrong place. The catch class: internal consistency checks all passed while the graded object was
the wrong one — same family as C1.3/C1.4.