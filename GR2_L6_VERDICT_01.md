# GR2-L6 — VERDICT

**Date:** 2026-09-27 · **Charter:** `GR2_L6_FINITE_SIZE_CHARTER_01.md`,
frozen at `29ee4d7` **before** implementation and run (pre-run disclosed
control repair, Amendment 01, at `5d5b270`) · **Directive:**
`GR2_CAMPAIGN_DIRECTIVE_01.md`, Layer 6 · **Instrument:**
`calc/gr2_l6_finite_size.py` (pure stdlib, deterministic, no randomness) ·
**Artifact:** `GR2_L6_RESULT.json` (sha `64d20c895e5f83cb…`) ·
**Battery: 15/15 gated checks, zero failures, zero halts, single run.**

## THE VERDICT — L6-MECHANISM-DERIVED

> **The GR-1 3D red gate's deficit is derived, not mysterious — and the
> gate's own target was mis-set. On the frozen window $[0.9,1.8]$ the
> pair-count exponent's true infinite-size value is
> $S_\infty = 6.2142$, not 6: the dimensional $2d=6$ plus a
> lattice-dispersion curvature offset of $+0.2142$ that belongs to the
> window, not to the dimension. The finite-size deficit below that value
> is the open-boundary surface-mode surplus, an $O(1/s)$ effect with an
> analytically derived coefficient. The gate stays red.**

### The four findings

**1. The asymptote is 6.21, not 6.** Midpoint continuum quadrature gives
$S_\infty = 6.2142$ (M = 121; convergence $4.8\times10^{-4}$ against
M = 101). The offset follows the quadratic curvature law: on the halved
window $[0.45,0.9]$ the continuum slope drops to 6.0454, against the
sealed quadratic prediction 6.054.

**2. The deficit law is derived and predicts blindly.** The open chain's
Euler–Maclaurin half-weight at $\theta=0$ puts an $O(s^2)$ surplus of
low-frequency surface modes on the three coordinate planes, biasing the
two-point slope down by $b_1/s$ with $b_1 = 22.571$ computed by
quadrature — no fit. With one calibrated $1/s^2$ term (disclosed:
calibrated on the already-public sizes 13/21/31 only), the model
predicted five never-before-computed sizes:

| $s$ | frozen prediction | measured | miss (tolerance ±0.05) |
|---|---|---|---|
| 45 | 5.7874 | 5.7939 | 0.0065 |
| 63 | 5.8943 | 5.8929 | 0.0014 |
| 91 | 5.9848 | 5.9840 | 0.0008 |
| 121 | 6.0384 | 6.0377 | 0.0007 |
| 131 | 6.0511 | 6.0503 | 0.0008 |

**3. The sequence crosses 6 and keeps going.** $S(121)=6.0377$ and
$S(131)=6.0503$ are **above** 6 (crossing gate B-6). The recorded
13³/21³/31³ trend $5.362\to5.493\to5.662$ was therefore not "converging
monotonically toward $2d=6$": it converges to 6.2142 and passes through
6 near $s\approx100$ on the way. The correction artifact
`GR1_LD_DIAGNOSTIC_CORRECTION_01.md` records this against the old
diagnostic's prose; the gate, result file, and verdict of GR-1 are
untouched.

**4. The mechanism is confirmed by sign flip.** Dropping the $k=0$
boundary planes flips the surplus to a deficit, so the slope must
overshoot instead of undershoot — and it does: at $s=13$,
$5.3617 \to 8.5196$; at $s=31$, $5.6620 \to 7.0579$, inside the frozen
band. The source is the open-boundary surface modes, not generic
discreteness.

## What this does, and does not do

- **The GR-1 3D gate stays RED.** Frozen 5.362 against $6\pm0.6$, as
  found. Nothing here re-adjudicates it; a refined re-test remains a
  separately chartered C6 act under the refinement rule frozen in the
  charter (§5), and any such gate must target the *dimensional part*
  $S_\infty-\Delta_{\rm curv}(W)$, not a bare 6 — the old target was
  itself off by the window's $+0.21$ curvature.
- **For the campaign's Layer 7:** this removes "dimension inconsistency"
  from the candidate explanations of the red gate — the pair-count
  dimensional scaling is consistent with $2d=6$ once the derived window
  curvature and boundary corrections are separated. It establishes
  **nothing** about the gravitational identification: it is a statement
  about mode counting on class (b) open-chain lattice cubes, at the
  frozen window, for the counting object exactly as frozen in
  `calc/gr1_gravity.py`.
- **Scope travels with every number above:** class (b), open-chain tensor
  cubes, the two-point ratio on $[0.9,1.8]$, self-pairs included.

**HARD STOP.** Verdict recorded pending owner ruling. The next fork
(GR2-a, the coupling-family attack) starts only from a new frozen
charter.
