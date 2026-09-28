# L0-1a — GAP AND PASSIVITY: CHARTER + PRE-REGISTRATION (frozen before evaluation)

**Fork:** L0-1a, the first fork of the Level-0 necessity sweep and the
first instrument of the successor program.
**Authority:** `GRUT_PROGRAM_REOPEN_02.md` (owner decision, 2026-09-28,
post-deposit; the four prohibitions and attack posture recorded there
bind this charter); design basis `L0_1_NECESSITY_SWEEP_DESIGN_01.md`
§§2–4 (D-GAP, D-PASS).
**Source machinery:** the C1-a substrate exactly as committed
(`calc/c1_seam.py`: `build_K`, `World`, PIN = 0.3, N = 24; replication
targets = the owner-verified sealed kernels of
`REPRODUCTION_NOTE_C1A_KERNELS_01.md`).

## 0. The two frozen questions (the owner's architecture: two deletions, two properties, never conflated)

> **gap deletion → P_memory** — is the spectral gap load-bearing for
> finite-memory-grade decay of the retained-site kernel?
> **passivity deletion → P_positivity** — is passivity load-bearing
> for the kernel's positivity/complete-monotonicity structure?

Frozen hypotheses to **attack, not protect** (the owner's wording:
"that is a prediction to attack, not a result"; either outcome is
informative):

- **H-GAP:** within the declared emergence class, removal of the
  spectral gap destroys finite-memory-grade decay.
- **H-PASS:** removal of passivity destroys the earned positivity
  structure.

The separation is itself a frozen rule: **P_memory is adjudicated only
from D-GAP members; P_positivity only from D-PASS members.**
Cross-appearances are labeled diagnostics and adjudicate nothing. A
failed memory kernel is never read as evidence against passivity; a
negative-residue instability is never read as evidence against a gap.

## 1. The substrate, the members, and the object (frozen)

The C1-a construction: chain of N sites, springs 1.0, retained site 0,
bath = sites 1..N−1 (the coupling spring's diagonal contribution
included, exactly as `build_K` builds it), memory kernel
$k(\tau) = \sum_k u_k^2 e^{-\lambda_k \tau}$ with $(λ_k, u_k)$ the bath
block's eigensystem and $u$ its site-1 row. τ-grid: 1.0 to 40.0, step
0.5.

- **D-GAP members** (pin varied, all springs +1, N = 24):
  pin ∈ {0.3 (anchor), 0.1, 0.03, 0.01, 0.003, 0}. The intermediate
  members MAP the crossover (the L-g precedent: watch the property
  degrade and say where); certification is keyed to the two ENDS.
  **N-scan** (pin = 0 only): N ∈ {24, 48, 96} — establishes that the
  deleted member's residual λ_min is a finite-size artifact vanishing
  ∝ 1/N², so the deletion is real in the large-N sense.
- **D-PASS members** (pin = 0.3 held fixed, one interior spring — the
  chain spring (2,3) — set to w): w ∈ {+1 (anchor), −0.3 (marginal,
  maps the boundary, ungated), −1.0 (deep, gated)}.

## 2. The gates (frozen, mechanical; analytic-backed where gated, reported where not)

**Controls (halt-grade):**
- RC-1 the sealed C1-a kernels replicate:
  `World(24, 1.0).frozen(e, τ)` reproduces (0.1594754, 0.1328810,
  0.3579003, 0.2874716) at (A/B × τ = 1.0/0.5), each |Δ| < 5e-8; and
  this instrument's parametric builder at pin = 0.3 equals
  `build_K(24, 0)` entrywise (< 1e-15).
- RC-2 identities, per member: k(0) = 1 exactly (orthonormality;
  |Δ| < 1e-12); **λ_min ≥ pin** for every D-GAP member (K = pin·I + L
  with L PSD; |breach| < 1e-12 tolerance — halt-grade: a violation is
  an eigensolver bug, never physics).

**D-GAP measurements and gates:**
- G-1 (gate; analytic-backed) **the deletion contrast:**
  k(40 | pin = 0.3) < 1e-5 (analytic bound: k(40) ≤ e^{−pin·40} =
  6.1e-6) AND k(40 | pin = 0)/k(40 | pin = 0.3) > 100.
- G-2 (gate) **grade classification at the ends**, by the frozen
  comparator — on the τ-window, least-squares linear fits of ln k vs τ
  (exponential model) and ln k vs ln τ (algebraic model), compared by
  maximum absolute residual: the anchor classifies EXPONENTIAL-GRADE
  (R_exp < R_alg) and the deleted member classifies ALGEBRAIC-GRADE
  (R_alg < R_exp). Intermediate members: classified and REPORTED,
  ungated (the crossover map).
- G-3 (gate) **the deletion is real:** λ_min(pin = 0, N) scales as
  1/N² — both successive ratios λ_min(N)/λ_min(2N) ∈ [3.5, 4.5].
- G-diag (ungated): per-member λ_min, fitted rates, residual pairs,
  the crossover location in pin.

**D-PASS measurements and gates:**
- P-1 (gate; analytic) the anchor is passive and completely monotone:
  min λ_bath ≥ 0.3 − 1e-12, and k strictly decreasing on the τ-grid
  (each step ≤ +1e-12).
- P-2 (gate; analytic-backed) **the deep member breaches passivity:**
  min λ_bath < 0 — guaranteed direction by Cauchy interlacing (the
  (2,3)-spring block at w = −1 has a principal 2×2 eigenvalue −0.7,
  and λ_min of the full matrix lies at or below it) — the gate
  confirms the instrument sees what the algebra requires.
- P-3 (gate) **the positivity phenomenon breaks with it:** on the deep
  member, k(40) > k(0) (the negative mode's weight grows as
  e^{|λ|τ}; any nonzero site-1 component suffices).
- P-diag (ungated): the marginal member's full spectrum and kernel —
  the boundary map; no adjudication from it.

## 3. Outcome rule (frozen, mechanical; per-property verdicts, never composed)

Two verdict lines, reported separately:

- **GAP: NECESSITY-CERTIFIED for P_memory** (at the declared class,
  window, and background mathematics) iff RC-1/2 and G-1/2/3 all hold.
  **GAP: NOT-LOAD-BEARING-ON-WINDOW** iff the deleted member classifies
  EXPONENTIAL-GRADE or the contrast fails in the informative direction
  (recorded as the finding it would be: the apparent pin–memory
  relationship was not fundamental as thought). **L01A-GAP-PARTIAL**
  otherwise.
- **PASSIVITY: NECESSITY-CERTIFIED for P_positivity** iff RC-1/2 and
  P-1/2/3 all hold. **PASSIVITY: NOT-LOAD-BEARING** iff the deep
  member breaches spectrum without breaking the kernel's monotone
  structure (P-2 passes, P-3 fails — recorded as the finding).
  **L01A-PASS-PARTIAL** otherwise.

**HALT** (instrument bug, never physics; no verdict on the affected
property) on any RC breach. Scope declaration on the face of every
statement: *within the declared background mathematics (real symmetric
matrices, exact eigendecomposition) and the tested construction class
(the C1-a chain family), on the declared window.* No claim is made
about "the axioms of reality." Under every outcome: no v4 channel
moves; no red gate is touched; the public paper is untouched; the
prior adjudications stand. **HARD STOP** after the verdict, pending
owner ruling (which also decides whether L0-1b, D-LOC, is chartered
next).

## 4. Instrument contract

`calc/l01a_gap_passivity.py`: pure Python 3 standard library; imports
`World`, `build_K` from the committed `c1_seam` and `jacobi_eig` from
`partition_selection_p1`, unchanged; deterministic (no RNG); single
run; no post-hoc tuning; writes `L0_1A_RESULT.json` (sha-hashed) at the
repository root with a `defect_history` field; runtime seconds
(the largest eigenproblem is the 95-dim bath of the N = 96 scan).
Out of scope: locality (L0-1b), linearity (L0-1c), the formulability
floor, and every Level-II question.
