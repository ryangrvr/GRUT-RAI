# C1-a2 — THE PACKAGING BOUNDARY, RE-TESTED: CHARTER + PRE-REGISTRATION (frozen before evaluation)

**Date:** 2026-09-25 · **Authority:** owner ruling on C1-a (recorded on
Issue #2, 2026-09-25): C1-a accepted at recorded strength — map,
continuity, structure — with the packaging boundary **not certified**;
*"C1-a2 authorized as a separate, freshly chartered attack. Its purpose
is narrowly to re-test the packaging boundary with a defensible
normalization and freshly frozen thresholds. It must not rewrite
C1-a."*

**Binding relations to C1-a:**
- C1-a's record is immutable: its two L-B gates (D = 0.0498 vs 0.1;
  midpoint anchor 0.0494 vs 0.05) **stay red forever**. Nothing here
  re-adjudicates them.
- This charter is a **new** pre-registration for a **new** instrument
  with its own gates. Passing here certifies the packaging boundary
  going forward; it does not turn any C1-a red green.

**Calibration disclosure (stated openly, per house discipline):** the
statistics and working points below are informed by C1-a's *labeled
post-hoc diagnostics* (lagwise relative drift 0.118 at ε_m = 0.5;
at ε_m = 1.0: peak-normalized D = 0.0887, anchor-family worst errors
0.1095 / 0.1484 / 0.0968). Gates are frozen with roughly 2× margin
below those measured diagnostic values. This is calibration by prior
measurement, disclosed — not blind prediction; the certification's
strength is "freshly frozen, mechanically evaluated," not "surprising."

**The defensible normalization (the charter's core justification):**
k(0) = vᵀv is modulation-independent, so any statistic normalized by
the τ = 0 peak structurally suppresses the two-time effect (the C1-a
L-B(a) defect). The defensible scale is the kernel's **own local scale
at the same lag**, over the window τ ∈ [0.5, 3] that excludes the
universal peak and covers the lags where memory acts.

**The question:** does the stationary spectral packaging — a single
ρ(τ) / a single Δt-only kernel — extend across the stationarity seam?
Certification target: **NO**, mechanically, at the frozen thresholds.

## 1. THE MODEL (frozen; machinery reused from `calc/c1_seam.py` unchanged)

The C1-a world: N = 24 chain, springs 1.0, pins 0.3, epochs
[0,4) A / [4,8) B / [8,12] A, bath springs (1,2)…(4,5) × (1 + ε_m),
coupling row never modulated, exact per-epoch eigenmachinery.
Working points: ε_m = 0.5 (P-1), ε_m = 1.0 (P-2…P-4; diagnostic-
informed, disclosed above), ε_m = 0 (control). Anchors:
A-epoch {1.5, 2.0, 2.5}, B-epoch {5.5, 6.0, 6.5}. Window
τ ∈ [0.5, 3.0], step 0.1.

## 2. THE GATES (frozen, predictions written before any number of THIS instrument)

- **P-1 (two-time magnitude, local scale, ε_m = 0.5).**
  r(τ; a, b) = |k(a+τ, a) − k(b+τ, b)| / max(|k(a+τ, a)|, |k(b+τ, b)|)
  over cross-epoch anchor pairs (a, b) ∈ A×B and τ in the window.
  **Prediction: max r > 0.05.**
- **P-2 (amplitude scaling).** The same statistic at ε_m = 1.0 versus
  ε_m = 0.5: **ratio ∈ [1.5, 2.5]** (the two-time effect scales with
  the TTI-breaking amplitude, as C1-a's continuity leg measured).
- **P-3 (the local-anchor family fails, every member, ε_m = 1.0).**
  Frozen rules k_frozen(a)(t−s), a ∈ {s, t, (t+s)/2}, on the C1-a
  cross-boundary pair set (t−s ∈ [0.5, 3]). **Prediction: worst
  relative error > 0.05 for each of the three members.** (ε_m = 0.5
  values reported, not gated.)
- **P-4 (the whole Δt-only class is excluded — the certifying gate).**
  For fixed lag τ, the L²-optimal Δt-only approximation over the
  anchor set is the per-lag mean (a theorem, not a choice). Statistic:
  s(τ) = std over the six anchors of k(a+τ, a), divided by the mean of
  |k(a+τ, a)|. **Prediction: max over the window s(τ) > 0.05 at
  ε_m = 1.0.** This excludes not just the frozen-epoch family but
  every Δt-only function, at the stated scope.
- **P-5 (stationary control, halt-grade).** At ε_m = 0, the P-1 and
  P-4 statistics are both **< 1e-10**.
- **P-6 (specificity control, halt-grade).** A matched **stationary**
  world with all springs × 1.25 (constant in time): its P-1 drift
  statistic is **< 1e-10**, while its kernel differs from the base
  stationary kernel by **> 0.05** relative at some window lag — the
  statistic detects *nonstationarity*, never mere kernel difference.

## 3. OUTCOME RULE (frozen, mechanical)

- **PACKAGING BOUNDARY CERTIFIED** iff P-1, P-2, P-3, P-4 all hold
  with P-5 and P-6 green. Consequence: the third item of S1's
  partition (the packaging certification) **closes at finite stepped
  level in-class**: no single spectral measure and no Δt-only kernel
  packages the generated K(t,s); the priced datum is the two-time
  spectral datum C1-a exhibited ({λ_e, u_e} + the mixing matrices).
  C1-b and C1-c remain open and are untouched.
- **NOT CERTIFIED** if any P-gate fails — kept red, labeled
  diagnostics permitted, no re-run tuning.
- Either way, **C1-a's record is unchanged.**

## 4. CONTROLS AND FENCES

- Halt-grade: P-5, P-6, and the reused composition identity of the
  eigenmachinery.
- Deterministic; single run; no FRW/cosmological object anywhere.
- No C2 content; ω⁷ / Class-4 / GR-1 / closed forks untouched; no
  absolute exponent; ℏ located; operator ordering fenced.

## 5. DELIVERABLES AND STOP

1. `calc/c1a2_packaging.py` (pure stdlib; reuses `c1_seam` machinery;
   emits `C1A2_PACKAGING_RESULT.json`, sha-hashed).
2. `C1A2_PACKAGING_VERDICT_01.md` and a closing comment on Issue #2.
3. **HARD STOP after the C1-a2 verdict.** C1-b and C1-c named, not
   opened.
