# GR2-L6 — THE 3D RED GATE'S FINITE-SIZE LAW: CHARTER + PRE-REGISTRATION (frozen before evaluation)

**Fork:** GR2-L6, the first fork of the GR-2 campaign (Layer 6 of
`GR2_CAMPAIGN_DIRECTIVE_01.md`).
**Authority:** owner campaign directive, given in-session 2026-09-27.
**Chartered by:** the session agent under that directive; this charter
freezes the implementation.
**Source commits:** publication branch `master-w25bu9`; the object under
study is the L-D leg of `calc/gr1_gravity.py` exactly as committed at
`d827a32` (unchanged since). The GR-1 3D gate (5.362 against a frozen
$6\pm0.6$) is **RED and stays RED whatever this fork finds.** This fork
re-adjudicates nothing; it asks what the deficit *is*.

## 0. The question (one sentence)

Does the GR-1 3D pair-count deficit have a derivable mathematical source —
and what is the true infinite-size value of the frozen-window exponent?

## 1. The object (frozen, replicated from the GR-1 instrument)

- Per-axis spectrum of the open $s$-site chain: $c_k=2-2\cos(\pi k/s)$,
  $k=0,\dots,s-1$; 3D modes $\omega=\sqrt{c_a+c_b+c_c}$ over the cube of
  that list, excluding only the all-zero mode.
- Pair count $P_s(W)$: unordered pairs $i\le j$ (self-pairs included) with
  $\omega_i+\omega_j\le W$.
- Exponent: the two-point ratio $S(s)=\log_2[P_s(1.8)/P_s(0.9)]$.
- Recorded public values (the calibration set; already on the record):
  $S(13)=5.361664$, $S(21)=5.492996$, $S(31)=5.662049$.

## 2. The analytic model (derived before this charter was frozen)

**Counting measure.** By Euler–Maclaurin, the open chain's per-axis mode
sum obeys $\sum_{k=0}^{s-1}f(\pi k/s)=(s/\pi)\int_0^\pi f
+\tfrac12 f(0)-\tfrac12 f(\pi)+O(1/s)$: the open (free-end) grid carries a
half-weight **surplus at $\theta=0$** and deficit at $\theta=\pi$. In the
3D tensor cube this puts an $O(s^2)$ surplus of modes on the three
$\theta_i=0$ coordinate planes — low-frequency *surface* modes — while the
$\theta_i=\pi$ planes have $\omega\ge2$ and are silent below the window.
Hence the mode-count CDF is
$C_s(x)=s^3F_3(x)+\tfrac32 s^2F_2^0(x)+O(s)$, with $F_3$ the bulk CDF and
$F_2^0$ the CDF of the $\theta_3=0$ plane spectrum
$\omega=2\sqrt{\sin^2(\theta_1/2)+\sin^2(\theta_2/2)}$.

**Consequences, in order:**

1. **The infinite-size window slope is not 6.** With the lattice
   dispersion, $F_3(x)=Ax^3(1+\beta x^2+\dots)$ with $\beta>0$, so the
   two-point slope on the frozen window $[0.9,1.8]$ exceeds the
   dimensional value $2d=6$ by a curvature offset. Sealed continuum
   computation (midpoint quadrature, $M=101$; Richardson-corroborated):
   $$S_\infty = 6.2147 .$$
2. **The finite-size deficit is the surface-mode surplus.** Since
   $F_2^0\sim x^2$ against $F_3\sim x^3$, the plane surplus inflates
   $P(0.9)$ relatively more than $P(1.8)$, biasing the slope **down** by
   $b_1/s$ with
   $$b_1=\frac{3\,[\hat q(0.9)-\hat q(1.8)]}{\ln 2},\qquad
     \hat q(W)=\frac{\int_0^W f_2^0(x)\,F_3(W-x)\,dx}{\int_0^W f_3(x)\,F_3(W-x)\,dx}.$$
   Sealed quadrature value ($M=101$ bulk, $M_2=1001$ plane):
   $\hat q(0.9)=10.477$, $\hat q(1.8)=5.262$, so
   $$b_1 = 22.571\ \text{(analytic; no fit)} .$$
3. **Model.** $S(s)=S_\infty-b_1/s+c_2/s^2$, with one fitted constant.
   **Calibration disclosure (per house discipline):** $c_2$ is
   least-squares fitted on the three already-public sizes only:
   $c_2=150.58$. Residuals there are $-0.008,\ +0.012,\ +0.019$; nothing
   below is calibrated on any new size. Small sizes also carry staircase
   granularity (at $s=13$, $P(0.9)=94$ counts), which the tolerances cover.

## 3. The gates (frozen, mechanical; predictions written before any new number exists)

Controls (halt-grade — a miss is an instrument bug, never physics):
- **R-1a/b/c.** Replicate the public values at $s=13,21,31$ to
  $|\Delta|<10^{-9}$ (same algorithm).

Continuum (the analytic side, re-computed by the instrument):
- **C-1a.** Midpoint continuum slope at $M=121$: $|S_\infty^{(121)}-6.2147|<0.002$.
- **C-1b.** Convergence: $|S_\infty^{(121)}-S_\infty^{(101)}|<0.002$.
- **C-2.** Curvature law: on the halved window $[0.45,0.9]$ the quadratic
  law predicts a continuum slope of $6.054$; gate $6.054\pm0.04$ at $M=121$.
- **C-3.** Recompute $b_1$ from quadrature: $|b_1-22.571|<0.1$.

Blind sizes (never before computed; tolerance $\pm0.05$ = 2.5× the worst
calibration residual):
- **B-1.** $S(45)=5.7874\pm0.05$.
- **B-2.** $S(63)=5.8943\pm0.05$.
- **B-3.** $S(91)=5.9848\pm0.05$.
- **B-4.** $S(121)=6.0384\pm0.05$.
- **B-5.** $S(131)=6.0511\pm0.05$.
- **B-6 (the crossing gate).** $S(131)>6.000$: the slope passes *through*
  6 and keeps rising, so the sequence does not converge to $2d=6$.

Mechanism counterfactual (sign flip; never before computed): dropping the
$k=0$ plane per axis flips the surplus $+\tfrac12\delta_0$ to a deficit
$-\tfrac12\delta_0$, so the bias must change sign:
- **N-1.** No-plane variant at $s=13$: slope $>S_\infty^{(121)}$.
- **N-2.** No-plane variant at $s=31$: slope in
  $(S_\infty^{(121)},\ S_\infty^{(121)}+2b_1/31]=(6.21,\ 7.67]$.

Ungated notes (reported, not gated): the surface/curvature decomposition
at each size; $S(121)$ versus 6; the observation that the old diagnostic's
"the lowest mode sits at 24% of the window edge" refers to the absolute
value $\omega_{\min}(13)=2\sin(\pi/26)=0.241$ (27% of the 0.9 edge, 13% of
the 1.8 edge).

## 4. Outcome rule (frozen, mechanical)

- **L6-MECHANISM-DERIVED** iff every gate above holds: the deficit is the
  open-boundary surface-mode surplus, $O(1/s)$ with an analytically
  derived coefficient, and the frozen window's true infinite-size slope is
  $S_\infty=6.21$ (the dimensional 6 plus a lattice-curvature window
  offset), **not** 6. The GR-1 diagnostic's phrase "converging
  monotonically toward 2d = 6" is then corrected by a correction artifact
  (`GR1_LD_DIAGNOSTIC_CORRECTION_01.md`, per the directive's provenance
  rules); the gate itself and every recorded number stay untouched.
- **L6-MECHANISM-PARTIAL** iff all B-gates hold but any C- or N-gate
  fails.
- **L6-MODEL-REFUTED** iff any B-gate fails: the analytic model does not
  explain the deficit, and that is the recorded result.

Under every outcome: the GR-1 3D gate stays **RED**; nothing here is a
re-adjudication, and no status of the public record moves.

## 5. Deliverable beyond the verdict: the frozen refinement rule

Any future re-test of the 3D dimension-consistency question (completion
problem C6) must be separately chartered and must, at minimum, freeze in
advance: (i) sizes $s\ge63$; (ii) the extrapolation form
$S(s)=S_\infty-b_1/s+c_2/s^2$ with this charter's sealed constants cited;
(iii) a gate on the *dimensional part* $S_\infty-\Delta_{\rm curv}(W)$
with the curvature offset computed from the sealed quadrature at the
chosen window, not assumed zero. This fork does not execute that re-test.

## 6. Instrument contract

`calc/gr2_l6_finite_size.py`: pure Python 3 standard library,
deterministic (no randomness), single run, no post-hoc tuning; writes
`GR2_L6_RESULT.json` (sha-hashed) at the repository root; assembles its
verdict string from measured variables; halts (no verdict) on any R-gate
miss. Expected runtime: minutes (the $131^3$ lattice has 2.25M modes).

---

## AMENDMENT 01 (pre-run, disclosed control repair)

Recorded 2026-09-27, before the instrument was implemented or run
(precedent: GR-1's disclosed pre-run control repair). The R-gates as
frozen compare a full-precision recomputation against constants recorded
to six decimals, so $|\Delta|<10^{-9}$ is unsatisfiable by construction —
a threshold-definition defect, not physics. Repair: the R-1a/b/c tolerance
becomes $|\Delta|<5\times10^{-7}$ (the rounding radius of the recorded
constants). No prediction, gate value, or tolerance elsewhere changes.
