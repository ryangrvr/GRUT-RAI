# L0-1a — VERDICT (two lines, never composed)

**Date:** 2026-09-28 · **Charter:** `L0_1A_CHARTER_01.md`, frozen at
`bb77df9` **before** implementation and run · **Authority:**
`GRUT_PROGRAM_REOPEN_02.md` (the successor program's first instrument;
the owner's four prohibitions in force) · **Instrument:**
`calc/l01a_gap_passivity.py` (pure stdlib; no RNG; the committed C1-a
machinery imported unchanged) · **Artifact:** `L0_1A_RESULT.json` (sha
`ff7465aeb8ff3525…`) · **Battery: 8/8 gated checks, zero failures,
zero halts, in the recorded run.**

## VERDICT LINE 1 — GAP: NECESSITY-CERTIFIED for P_memory

> **Within the declared background mathematics and the tested
> construction class, on the declared window: removal of the spectral
> gap destroys finite-memory-grade decay.** The anchor (pin = 0.3)
> holds k(40) = 6.8e-9 (under its analytic bound e^{−12}) and
> classifies EXPONENTIAL-GRADE; the deleted member (pin = 0) holds
> k(40) = 1.1e-3 — a contrast ratio of 1.6×10⁵ — and classifies
> ALGEBRAIC-GRADE; and the deleted member's residual λ_min is a pure
> finite-size artifact (1/N² ratios 4.084, 4.042). **H-GAP survived
> the attack.** Consequence, at recorded strength: *in this family,
> finite memory need not be inserted as an axiom — it emerges
> conditionally from a spectral gap in the substrate.*

## VERDICT LINE 2 — PASSIVITY: NECESSITY-CERTIFIED for P_positivity

> **Removal of passivity destroys the earned positivity structure.**
> The anchor is passive (λ_min = 0.304) and completely monotone on the
> grid; the deep member (spring(2,3) = −1.0) breaches the spectrum
> exactly as Cauchy interlacing requires (λ_min = −1.018 < −0.7) and
> the kernel's positivity structure breaks with it (k(40) = 2.0×10¹⁶ >
> k(0) = 1 — growth, monotonicity gone). **H-PASS survived the
> attack.** The marginal member (−0.3) is the mapped boundary: the
> pins protect passivity against mild negative couplings (λ_min =
> +0.124, kernel still monotone) — reported, adjudicating nothing.

The separation rule held throughout: P_memory was adjudicated only from
D-GAP members, P_positivity only from D-PASS members.

## The structural finding the run exposed (post-run analytic note, labeled; it changes no gate and no verdict — it explains them)

The run's own numbers reveal that the D-GAP deletion in this family is
an **exact factorization**: the pin enters the bath as pin·I, so the
eigenvectors are pin-independent and every eigenvalue shifts uniformly —
visible in the artifact as λ_min(pin) = λ_min(0) + pin to machine
precision and as the *identical* R_exp = 1.9810 across all six members.
Therefore, exactly:

> **k_pin(τ) = e^{−pin·τ} · k_0(τ)** — the gap contributes precisely an
> exponential envelope over the ungapped substrate's algebraic memory
> (fitted power ≈ τ^{−3/2}-class, in the artifact).

Two honest consequences: (i) the certification is *stronger* than a
numerical trend — it is a structural identity of the construction
class, and the end-member gates passed because the identity forces
them; (ii) the intermediate members' grades are **window-relative**, as
the charter scoped — the comparator reads the algebraic envelope until
e^{−pin·τ} dominates the window's residuals (all four intermediates
classify ALGEBRAIC-GRADE on τ ∈ [1, 40], with the crossover set by the
envelope's curvature against pin × window). The crossover map is in the
artifact, ungated, adjudicating nothing.

## What this does and does not establish

- It does **not** say "the axioms of reality include a gap." Scope,
  on the face: real symmetric matrices, exact eigendecomposition, the
  C1-a chain family, window τ ∈ [1, 40].
- It **does** deliver the Level-0 program's first two necessity
  certificates, in the exact sense the direction demanded: two members
  of 𝒮₀ that were implicit premises are now *conditional theorems of
  the substrate* — finite memory rides on the gap; positivity rides on
  passivity — each certified by a controlled deletion that could have
  failed and was given every chance to.
- No v4 channel moves (the deposit stands as filed); no red gate is
  touched; the public paper is untouched; GR2's adjudications are
  unmodified.

**HARD STOP.** Verdicts recorded pending owner ruling — which also
decides whether **L0-1b (D-LOC, the response/space split)** is
chartered next, per the frozen priority order.
