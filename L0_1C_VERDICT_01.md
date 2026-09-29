# L0-1c — VERDICT (three lines, never composed)

**Date:** 2026-09-29 · **Charter:** `L0_1C_CHARTER_01.md`, FROZEN at
`2da022d` **before** implementation and run, after the adversarially
verified pre-freeze review (`L0_1C_PREFREEZE_REVIEW_01.md`; 29
findings, 23 confirmed and incorporated; the panel's measured preview
values are quarantined there and adjudicated nothing) · **Authority:**
`L0_1B_OWNER_RULING_01.md` (D-LIN per the frozen descent order) ·
**Instrument:** `calc/l01c_linearity.py` (commit `36a08f9`; pure
stdlib; no RNG; the committed machinery imported unchanged; the
comparator carried as an RC-6-certified textual copy) · **Artifact:**
`L0_1C_RESULT.json` (sha `6447ff3748232a48…`) · **Battery: 11/11
gated checks, zero failures, zero halts, in the recorded single run
(38 trajectories, 83 s).**

## RUN LABEL: OUTCOME-B-CERTIFIED — the instrument split

## VERDICT LINE 1 — LINEARITY: NECESSITY-CERTIFIED for P_exact-reduction

> **Definitional status on the face (charter §3.1): this line
> instantiates, it does not discover.** Superposition — the
> eigen-reduction's defining premise — holds at β = 0 to 7.5×10⁻¹⁵
> (RC-4) and fails at the deleted members exactly as the deletion
> demands: amplitude-collapse deficits 0.7422 (β = 1, a = 3) and
> 0.8460 (β = 3, a = 3) against the frozen 0.1 margin (X-1,
> certification-grade — the magnitudes sat in the charter's
> pre-declared analytic band 0.6–0.85).

## VERDICT LINE 2 — LINEARITY: NOT-LOAD-BEARING for P_memory

> **At the declared amplitudes, under a deletion whose in-window
> action is recorded at D_act ≈ 0.026–0.029:** the certified
> comparator classifies the normalized response EXPONENTIAL-GRADE at
> **all 18 legs**, including the strongest (β = 3, a = 3: R_exp =
> 1.874 < R_alg = 4.845). The window-tail slope is deletion-blind to
> four decimals across the entire lattice (0.3507–0.3510, against the
> anchor's own 0.3510) — the held fixed-point Hessian doing exactly
> what §3's identity said it must.

## VERDICT LINE 3 — LINEARITY: NOT-LOAD-BEARING for P_positivity (as operationalized)

> **Nonnegativity identity-held (the §3.2 cooperativity theorem;
> RC-5 clean); monotone decrease and the trajectory-Gram PSD reading
> tested:** every leg is strictly monotone on the gated window (worst
> step −2.26×10⁻¹⁰, sign-definite), and — **the fork's one genuinely
> unpreviewed gate, M-3** — the 39×39 trajectory Gram
> G_ij = r(τ_i + τ_j) is positive semidefinite at every leg with
> minimum eigenvalues in the −10⁻¹⁹ to −10⁻²⁰ range: **nine orders of
> magnitude inside the −10⁻¹⁰ tolerance.** The nonlinear response is
> completely monotone on the declared grid to machine precision. No
> identity forced this; no preview touched it; it could have failed
> and did not.

## THE SPLIT (Outcome B): CERTIFIED, transient-limited, at recorded scope

All three lines landed as the frozen outcome rule requires:

> **Linearity belongs to the instrument, not to the tested response
> phenomena (P_memory; P_positivity as operationalized)** — within
> the declared background mathematics (real symmetric matrices, exact
> eigendecomposition, the frozen RK4 schedule), the convex quartic
> on-site class on the C1-a bath (N = 24), the declared amplitudes
> a ∈ {0.001, 1.0, 3.0}, window, grids, and comparator — **under the
> §3.4 qualifier on the face: the tested deletion is transient-limited
> on the declared window** (the max-principle envelope x₁² ≤ 1/(8βt)
> caps in-window nonlinearity uniformly in β and a; a stronger
> deletion sense requires a structurally different deletion, named in
> the charter). P_continuum and P_geometry are visibly unclaimed.

## The maps (ungated; the exploratory payload)

- **Collapse-defect map** (sup |r(τ; a)/r(τ; 0.001) − 1|), monotone
  in βa²: at a = 3 — 0.171 (β = 0.03), 0.366 (0.1), 0.568 (0.3),
  0.742 (1), 0.846 (3); at a = 1 — 0.025 up to 0.585. The deletion's
  bite is amplitude-borne, pre-window, and saturating toward 1.
- **Linear-regime hug:** the a = 0.001 legs track the eigen kernel to
  2.6×10⁻⁸ … 2.6×10⁻⁶ (∝ β) — the small-amplitude limit of every
  deleted member is the sealed linear theory, on the face.
- **D_act** ≈ 2.6–2.9%: X-1's huge deficits are pre-window amplitude
  burn; the in-window deletion activity is a few percent — recorded
  on both NOT-LOAD-BEARING faces, per the charter.
- The early-early grid resolved the actual collapse (the strongest
  leg's collapse time ≈ 0.005), and r(40) falls with βa² (6.8×10⁻⁹ →
  1.2×10⁻⁹) — the frozen amplitude-loss offset, not a rate change.

## Grading, per the charter's preview-disclosure provenance

X-1, RC feasibility, the hardest leg's grade, and D_act were
previewed or analytically banded before freeze and are recorded here
as **disclosed-foreknowledge certifications**. The fork's **earned,
unpreviewed content** is: M-3's machine-precision Gram positivity at
every leg, the full 18-leg maps, and the deletion-blind tail-slope
identity landing at four decimals.

## What this does and does not establish

- It does **not** say "reality is linear" or "nonlinearity never
  matters" — the class is convex, on-site, self-limiting, and the
  charter says so on its face.
- It **does** deliver the sweep's fourth certificate set and its
  cleanest structural sentence so far: **linearity is the first
  tested axiom that is load-bearing for NO tested phenomenon — only
  for the instrument that reads them.** The Level-0 ledger now reads:
  gap → P_memory; passivity → P_positivity; locality → P_geometry;
  linearity → P_exact-reduction only.
- H3 survived the attack at recorded strength, through the one gate
  that was genuinely free to kill it.
- No v4 channel moves (the deposit stands as filed); no red gate is
  touched; GR2, L0-1a, L0-1b, and the public paper unmodified.

**HARD STOP.** Verdicts recorded pending owner ruling — which decides
the formulability floor (D-ORD / D-HERM / D-DET, per the frozen
descent order) and the disposition of the queued pin-free locality
fork.
