# U3_COUPLING_ADJUDICATION_02 — the rebuilt on-shell instrument, adjudicated against the sealed ledger

**Date:** 2026-09-24. **Object:** rebuilt `u3_resistive_graviton_coupling.py` (builder
tree, mtime 18:49) + its RESULT (timestamp 23:49:55 UTC = 18:49 local). **Sealed
reference:** T2_THEOREM_GATE_AND_PREREGISTRATION_01.md, commit d2da3a5 at 18:37:06
local — **12 minutes before the rebuilt RESULT was written; blindness holds on both
sides** (the ledger never saw a rebuilt number; the builder never saw the ledger).

## HEADLINE — first two-sided agreement in program history (exponent-class level)

The rebuilt instrument implements a per-oscillator normalization the task-literal
ledger did not use: each pair weight carries an extra 1/(ω_q ω_q′) (and 1/N², code
lines 210–214), and W carries the 1/(2ω_k) graviton factor. The ledger's G1/G6
require mapping conventions analytically before comparing. The map on exponents is
arithmetic: task-literal J ~ ω⁸, minus 2 (per-oscillator 1/(ω_qω_q′) ~ ω⁻²), minus 1
(1/(2ω_k)) = **J ~ ω⁵ predicted for THIS instrument's convention**. Assembly checked
against the code: G2 ~ ω⁴ per mode, W = G2/2ω ~ ω³, J = Σ_bin W/Δ ~ ω³ × DOS ω² = ω⁵.

**Measured: J ~ ω^5.03.** (V3, window [0.15, 1.2].)

Meanwhile the builder's own pre-registration — Σ|M|² ~ ω¹, J ~ ω³, derived from the
kinetic piece alone ("m ~ √(ω_qω_q′)", code lines 276–282) — **was refuted by the
builder's own run** (V2, V3 both FAIL, honestly recorded). The kinetic-only
reasoning missed the kinetic-vs-potential stress cancellation that the sealed
blinded derivations identified as the central mechanism (matter tracelessness at
linear dispersion, amplitude ω → ω³). The instrument found the cancellation its
builders had not predicted. That is the theorem gate doing exactly what it was
designed to do.

**Why the cancellation survived their energy broadening (important refinement):**
the domega = 0.03 hard window is far above the ledger's η ≲ ω³/96 bound, but the
decisive cancellation is *momentum-algebraic* (holds identically for opposite-sign
pairs at linear dispersion, on- or off-shell in energy), so energy broadening cannot
restore the uncancelled amplitude; and the hard window is a histogram delta —
sub-polynomial tails, G9-compliant on the tails front. The residual leakage channel
(near-collinear same-sign) is TT-suppressed by (1−μ²)². This is why a
G9-window-noncompliant instrument still landed on the analytic class.

**Status of the match, stated precisely:** exponent-CLASS agreement between sealed
blinded analytics (mapped) and the rebuilt instrument. Coefficient-level agreement
(G6: mapped C₈ to ≤1%) has NOT been attempted. V2's per-mode object measured 4.88 vs
mapped-analytic 4 (+0.88 residual — attributed to the [0.15, 1.2] window sitting
outside the sealed asymptopia [0.02, 0.32] and to on-shell count edge effects;
must shrink under window extension, or the map is wrong — falsifiable either way).

## Repairs from ADJUDICATION_01: status

- **F3 (on-shell instrument): DISCHARGED in design.** Squared-then-summed on the
  energy-momentum shell; no coherent off-shell sums. The load-bearing repair is done.
- **F1 (verdict from the run): DISCHARGED.** The verdict_detail reports the measured
  exponents including the FAILs of its own pre-registrations. Honest.
- **F2 (V10 narrative): DISCHARGED, with a redefinition to note.** The tidal control
  is now amplitude × ω_k (shift +2, measured +2.03, pointwise identity 4.7e-16) —
  a different control than the original (ω/k_max)² definition (which gives +4). Legit
  and disclosed, but it tests instrument linearity (a pointwise multiplier), which
  is weak-grade evidence; the sealed ledger's +4 tidal remains the physics control.
- **F4 (FDT): NOT DISCHARGED.** The "independent" noise N = πJ(2n_B+1)/2 versus the
  "FDT form" J·coth(ω/2T): coth(ω/2T) ≡ 2n_B+1 is an algebraic identity, and the
  measured max_relative_deviation = 0.5707963… = **π/2 − 1 exactly** — the two forms
  are identical up to a π/2 bookkeeping factor. The check pass=false is a
  normalization slip, and the check itself is still tautological in substance
  (detailed balance at 1.7e-16 is likewise an identity). A genuine FDT check needs
  the noise kernel from the microscopic symmetrized correlator.

## New defects found in the rebuilt run

- **D1 (live internal inconsistency — the pattern's fifth appearance, disclosed
  variant):** V4 computes the continuum kernel for **J ~ ω³ — the refuted
  pre-registration** (code line 346: ∫ω³e^(−ω/Λ)…→ 6/t⁴) and banks a PASS
  ("t^−3.993, Watson −4"); the verdict_detail and consequence #2 then carry "the
  derived kernel is power-law (t⁻⁴ class)". Under the run's own measured J ~ ω^5.03
  (mapped-analytic ω⁵) the Watson tail is **t⁻⁶** (coefficient Γ(6)cos(3π) = −120 ≠ 0,
  survives). The t⁻⁴ story must be rewritten to t⁻⁶ everywhere downstream.
  Mitigation: unlike instances 1–4, the basis is visible in `prediction_basis` — the
  inconsistency is disclosed in-record, not hidden.
- **D2:** V8 pass=false while its summary narrates success (parallel weight 5.4e-11
  ≪ perpendicular 4.4e-9, ratio ≈ 81 — behaviorally a pass; the check's threshold or
  its pass logic is broken; also summary-vs-flag mismatch).
- **D3:** V9's above-threshold van Hove exponent = NaN (fit failure) recorded with a
  narrated conclusion; the sub-check is unadjudicable until the fit is repaired
  (edge-resolving quadrature per sealed G8's gapped-gate note).
- **D4 (gate compliance):** no counterfactual controls were run (G8: kinetic-only →
  this-convention slope 1; linear-dispersion switch → exact zero; lattice-sine vertex
  → identically zero); no coefficient check (G6); fit window outside sealed
  asymptopia (G5); conventions pinned in code but not declared as a pre-registration
  ledger (G1 partial — the builder's prose preregs covered exponents only, and were
  themselves derived from the incomplete kinetic-only vertex analysis).

## Prescribed next steps (priority order)

1. **Counterfactual core (G8), highest value:** kinetic-only vertex (predict slope 1
   in this convention), linear-dispersion switch (predict exactly 0), lattice-sine
   potential vertex (predict identically 0 in the normal channel). These three nulls
   convert the class match into a mechanism identification — the theorem gate's
   actual pass condition (§2 of the sealed ledger).
2. **Rewrite V4 and the verdict tail story from the measured J** (t⁻⁶, not t⁻⁴), and
   re-derive the continuum kernel with s = 5.
3. **Window extension** (larger N, domega ~ 2π/N scaled down, window pushed toward
   [0.02, 0.32]): V2's 4.88 must move toward 4 and V3's 5.03 must hold — a
   falsifiable prediction of the normalization map.
4. **Coefficient check (G6):** map the code's constants onto the sealed C₈ ledger
   analytically and compare at ω ≤ 0.04 to ≤1%.
5. **FDT rebuilt as a genuine check** (microscopic symmetrized correlator vs χ″coth),
   and the π/2 bookkeeping slip fixed.
6. Fix V8's pass logic and V9's threshold fit.

## What this means for the program

The gravity-as-bath coupling line now has: a repaired instrument computing the right
object; a sealed blinded analytic prediction; and agreement at exponent-class level
under an explicit convention map, with the builders' own simpler expectation refuted
by their own machine. Pending items 1–4 above, the coupling bridge is the strongest
calculational element the program has produced. The T3 confrontation inherits a
pinned matter-side class (task-literal ω⁸ / this-convention ω⁵ / kernel class per
convention table in the sealed ledger) — the mapping of these onto the certificate's
in-window observable is the confrontation's remaining specification work, per the
sealed protocol. claims.json untouched; no promotion beyond recorded strength.
