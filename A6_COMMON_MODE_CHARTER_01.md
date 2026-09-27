# A6 — THE COMMON-MODE DIFFERENTIAL CHECK: CHARTER + PRE-REGISTRATION (frozen before evaluation)

**Fork:** A6-1, the owed Boltzmann-grade common-mode check of the frozen
TT-auto gate — the named blocking item of the **first Part-7 front**
(v4 channel C3).
**Authority:** the owner's standing delegation of 2026-09-27 ("do what
you see fit with it … keep the record up to date as we go"); the owed
item itself is pre-existing: amendment **A6** of the frozen
`calc/isw_tt_auto.py` record ("a Boltzmann-grade differential check is
OWED before any κ=3 kill-grade use") and `STAGE_CLOSE_2026-08-09.md`
("the Boltzmann-grade TT-auto channel (with A6's common-mode check)").
**Source records:** `calc/isw_tt_auto.py` (pipeline P1–P5, re-frozen
2026-08-03, amendments A1–A8), `calc/RESULTS_isw_tt_auto.md`,
`X_FLOOR_MAP.md`, the A8 demotion
(`provenance/prereg/RESULT_KAPPA_2026-08-08.txt`).
**Standing constraint (A8, carried whole):** every number the TT-auto
gate emits is **insertion-contaminated** (GRUT-plus-an-unbanked-filter).
This fork repairs the **common-mode defect only**; it removes no
insertion, and every consumer statement keeps the A8 marking.

## 0. The question (the owed item's own wording)

> At κ=3 the omitted common power (Doppler / early-ISW / radiation) is
> O(signal) — **a Boltzmann-grade differential check is OWED before any
> κ=3 kill-grade use**; the in-pipeline baseline shape (D30/D2 ~ 0.62
> vs ~0.82–0.84 Boltzmann, memory-grade) understates C_obs at the
> dominant ells.

Delta over the record: the fence was **memory-grade** (a remembered
literature ratio). This fork computes it — the common-mode content is
obtained from an actual Boltzmann code by exact source decomposition,
and its effect on every declared verdict is recomputed mechanically.

## 1. The scheme (frozen; normalization-free)

The pipeline's exclusion metric depends only on the per-ℓ ratios
$R_\ell(x) = C^{\rm pipe}_\ell(x)/C^{\rm pipe}_\ell(0)$
($N^2_{LR} = \sum_\ell (2\ell{+}1)[1/R + \ln R - 1]$, A2). The omitted
terms are **common** to model and baseline (the modification is
post-recombination — P2's fence), so they enter as additive common
power $\Delta_\ell$ on both sides:

> $R^{\rm corr}_\ell(x) = \dfrac{R^{\rm pipe}_\ell(x) + f_\ell}{1 + f_\ell},
> \qquad f_\ell = \Delta_\ell / C^{\rm pipe}_\ell(0).$

$f_\ell$ is measured **entirely inside CAMB** as a ratio (all absolute
normalization cancels):

- **matched baseline** = the pipeline's source content, at Boltzmann
  grade: monopole (Sachs–Wolfe) + **late** ISW, via CAMB's exact
  scalar-source decomposition (`camb.symbolic`), with the late-ISW
  window $W(a) = 1/(1 + (a_s/a)^8)$ — the pipeline's ISW starts at
  recombination in a matter+Λ background, so early (radiation-era) ISW
  is part of what it *misses*;
- **quotable members** (the declared family): $f^B_\ell$ with
  $a_s = 1/50$ and $f^C_\ell$ with $a_s = 1/20$ — the window scale is
  an insertion, scanned not chosen, and the calibration shows it is
  weak (members agree to ~0.02);
- **diagnostic bracket** $f^A_\ell$: baseline = monopole + full ISW
  (early-ISW kept in the baseline) — undercounts the pipeline's missing
  set; reported, not quotable.

**Declared insertions (A8 discipline):** (i) the missing common power
is attached proportionally to the pipeline's own baseline through
$f_\ell$; (ii) the window form and scale (scanned pair); (iii) the CAMB
cosmology: H0 = 67.36, ωb = 0.02237, ωc = 0.1200, A_s = 2.1e-9,
n_s = 0.96 (matching the pipeline's frozen n_s; implied Ω_m = 0.314 vs
the pipeline's 0.315 — inside the pipeline's own recorded KC-band where
normalization moves edges < 1%); unlensed scalar spectra throughout.

## 2. Pre-freeze calibration (disclosed; ΛCDM only — no model-x quantity was computed before this freeze)

1. **The frozen pipeline replicates digit-exact in this container**
   (run of 2026-09-27): ISW shares 0.23 / 0.08 (ℓ=2 / 10); edges
   κ=1: 0.0372, κ=3: 0.358; N(0.111) = 6.24 (κ=1), 0.86 (κ=3);
   selftest PASS.
2. **The measured common-mode fractions** (CAMB 2.0.4, decomposition
   exact): $f^A_\ell$ = +0.13 (ℓ=2), +0.17 (5), +0.30 (10), +0.92
   (20), +1.93 (30) — one-signed positive, growing exactly as A6
   flagged. **Pipeline-matched members are NOT one-signed:**
   $f^B_\ell$ = −0.10 (ℓ=2), −0.12 (5), −0.07 (10), +0.25 (20), +0.79
   (30); $f^C$ within ~0.02 of $f^B$ throughout.
3. **The sign discovery (disclosed because it kills a shortcut):** the
   naive argument "common-mode correction can only weaken exclusions"
   is **wrong** once early-ISW is correctly counted as missing — the
   early-ISW cross-term *anticorrelates* at low ℓ, so the full sky has
   *less* power there than the matched baseline, and the correction
   **amplifies** low-ℓ deviations (÷(1+f), f<0) while suppressing
   high-ℓ ones. The net effect on each verdict is therefore a genuine
   measured question — which is exactly why A6 was owed rather than
   waved through. No corrected $N(x)$ value was computed before this
   freeze.

## 3. The gates (frozen, mechanical)

**Controls (halt-grade):**
- RC-1 the frozen pipeline replicates in-run: ISW shares within ±0.005
  of (0.23, 0.08); edges within ±0.0005 / ±0.001 of (0.0372, 0.358);
  N(0.111) within ±0.01 of (6.24, 0.86).
- RC-2 the Boltzmann harness validates: full-TT D30/D2 ∈ [0.75, 0.90]
  (the A6-cited ~0.82–0.84 with margin); the quotable members agree,
  $\max_\ell |f^B_\ell - f^C_\ell| < 0.05$.
- RC-3 identities: $f^A_\ell > 0$ for every ℓ ∈ [2, 30] (Doppler +
  quadrupole add positive power against the full-ISW baseline; a
  violation is a decomposition bug); and $R^{\rm corr}_\ell(0) \equiv 1$
  (the corrected metric is exactly zero at x = 0).

**The corrected table (the deliverable):**
- M-1 $N^{\rm corr}(x, \kappa, f)$ for x ∈ {0.0625, 0.111, 0.333} ×
  κ ∈ {1, 3} × f ∈ {B, C}, plus corrected top-crossing 2σ edges per
  (κ, f), computed from the frozen pipeline's own $C_\ell(x)$ (reused
  unchanged) with the frozen correction formula. The uncorrected values
  are printed beside every corrected one.
- M-2 (gate) the κ=3 survival at the natural point is
  Boltzmann-robust: $N^{\rm corr}(0.111, \kappa{=}3) < 2$ under both
  quotable members.
- M-3 (classification, not pass/fail — either way is a finding): each
  κ=1 named point is **KILL-CONFIRMED-AT-MEMBER** (≥ 2σ under both
  quotable members) or **KILL-WEAKENED** (< 2σ under either).
- D-1 (ungated diagnostics): the pipeline ΛCDM shape D30/D2 vs the
  CAMB matched-source shape; the $f^A$ bracket table; the Gaussian
  metric beside the LR metric.

## 4. Outcome rule (frozen, mechanical)

- **A6-DISCHARGED** iff RC-1..3 and M-2 hold and M-1 is complete: the
  owed common-mode check is computed at Boltzmann grade; the κ=3
  member's kill-grade gating condition is discharged-or-quantified;
  every consumer statement updates to the corrected table (with A8's
  insertion marking intact).
- **A6-BREAKS-THE-GATE** iff M-2 fails: the κ=3 survival itself does
  not survive correction — the gate record gains a defect entry and no
  consumer use is licensed pending owner ruling.
- **A6-PARTIAL** for any other gate failure; **HALT** (instrument bug,
  never physics; no verdict) on any RC breach.

Under every outcome: **no register field moves here** — per v4's R2,
consumption at the named nodes (zeta_interior_family, mu_linear) is the
owner's adjudication; the verdict document carries a **proposed C3
channel line** for that adjudication, and nothing executes until the
owner rules. The A8 demotion stands whole. **HARD STOP** after the
verdict.

## 5. Instrument contract

`calc/a6_common_mode.py`: imports the frozen pipeline
(`isw_tt_auto`: `cls`, `ELLS`, `KAPPAS`, and its validation machinery)
**unchanged**; the Boltzmann ground-truth harness is **declared
external tooling** — CAMB 2.0.4 with `camb.symbolic` custom compiled
sources (sympy, gfortran) — under the A1 precedent (mpmath as the
Bessel ground truth); deterministic; single run; no post-hoc tuning;
writes `A6_COMMON_MODE_RESULT.json` (sha-hashed) at the repository root
with a `defect_history` field; runtime minutes (the pipeline's own
$C_\ell(x)$ evaluations dominate). Scope: exactly the frozen pipeline's
band ℓ ∈ [2, 30], its declared κ members, its named points; the
activation-scale frontier (A8's two blocked inputs) is out of scope and
untouched.
