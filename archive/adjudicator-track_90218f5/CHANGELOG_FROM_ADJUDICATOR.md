# CHANGELOG FROM ADJUDICATOR — 2026-09-24 (owner-authorized repairs)

The owner authorized the adjudicator to apply the outstanding repairs directly in
this tree so you can take over a steady ship and rerun. Everything below was first
built and validated in the adjudicator tree ("grut claude copy", commits noted),
then installed here. **Your first action: rerun the five touched calcs and confirm
the check counts.** Nothing else in this tree was modified. No commits were made in
this repo (your uncommitted work is untouched); the RESULT JSONs of the five calcs
were regenerated in place so no stale verdict lingers.

Reference documents (adjudicator tree, chronological):
U3_COUPLING_ADJUDICATION_02 (ebb3a42) · U3_COUPLING_ADJUDICATION_03 (1e09d30) ·
U3_RECORD_NOTE_02 (affdf52) · sealed ledger T2_THEOREM_GATE_AND_PREREGISTRATION_01
(d2da3a5, sealed 18:37 — before your 18:49 run reported).

## 1. calc/u3_resistive_graviton_coupling.py — rebuilt (v3), 20/20

Why: the 19:13 version's `DISDERIVED_cherenkov_no_go` verdict was refuted
(ADJUDICATION_03). Three defects repaired:

- **False kinematics.** "ω_q + ω_q′ < |q+q′| = k_par for every pair" holds only for
  SAME-SIGN pairs; counter-propagating pairs reach any ω at small k_par. Your own
  earlier insight ("oblique modes resonate via transverse momentum") was correct.
- **Inverted control (V1b).** The windowed sum had no 1/(2dω) golden-rule
  normalization, so W ∝ dω was the OPEN-channel signature, misread as emptiness.
  Repair: W is now the golden-rule DENSITY (÷ 2dω). Open channel ⇒ W converges
  (measured halving ratios 0.99/0.99/1.12). True emptiness = identical zero at
  finite dω — exactly your own gapped-chain-below-threshold result, now run as the
  control it always was.
- **Mutilated vertex.** The kinetic stress term √(ω_qω_q′) had been removed as an
  "X-field piece." It is not: T_xx = ½(u̇² + (∂ₓu)²) for the displacement field, and
  ⟨q,q′|T_xx|0⟩ = −½[√(ω_qω_q′) + qq′/√(ω_qω_q′)]/N carries both terms. Restored.
  The near-cancellation of the two terms for counter-propagating pairs at linear
  dispersion (matter tracelessness, T₊₋ = 0) is the central physics.

New structure (all pre-registrations from the sealed ledger, fixed before the run):
V1b density convergence + emptiness controls · V1c tolerance-free exact-root census
(16/16 oblique roots at machine precision) · V3b continuum exact-root instrument
(second instrument class): **J ~ ω^7.008 measured vs pre-registered ω⁷ ± 0.15, and
coefficient ratio 1.0005 vs the analytic asymptote B → −ω³√(1−μ²)(1+μ²)/192** ·
V4 kernel tail from the DERIVED ω⁷ (Watson t⁻⁸, coefficient 5040 ≠ 0; measured
−7.981) — replaces the tail computed from the refuted ω³ prereg · V6/V7 FDT now
genuine: per-mode occupations n_q (not n_B(ω) plugged into coth's own identity),
with a detuned-shell NEGATIVE CONTROL that violates coth (0.33 vs 0.031 on-shell)
— the old check could never fail; this one demonstrably can · V9 corrected prereg:
angle-integrated van Hove is a threshold STEP, not −1/2 (measured step flatness
1.95); the −1/2 applies at fixed k_par only · V11 counterfactual suite: kinetic-only
→ ω^3.003, potential-only (your v2b vertex) → ω^3.006, full bracket → ω⁷ (the
cancellation is worth ω⁴ and the instrument FINDS it); linear-dispersion and
lattice-sine vertices → exact zeros (1e-34).

Declared convention (frozen in the docstring): full bracket B, W = Σ|M|²/(2ω_k·2dω),
no extra per-oscillator factors (the bracket already carries oscillator
normalization — your 18:49 version's extra 1/(ω_qω_q′) was a double-count; under
that convention the same physics reads ω⁵, which is what that run correctly
measured as 5.03).

Verdict now: `derived_within_class_onshell_omega7_channel_open`. Validated 20/20.

## 2. calc/u3_origin_persistence.py — P3 and P4 repaired (7/7)

- **P3** recorded `dx1/kick` (closed-loop rate) as the "kernel" and failed at 0.995
  while the summary asserted success. Repaired with two constructive tests:
  direct kernel extraction (error 1.8e-5) and exact trajectory equivalence of the
  reduced kernel equation vs the full 2-site chain (1.4e-16). **The derivability
  half of the base rung now stands at check level.**
- **P4** built its Hankel signal on P3's global `t` (variable shadowing) with
  near-degenerate random taus — the {5:4} "failure" was a degeneracy artifact.
  Repaired: intended grid, distinct taus, plus a degenerate-pair control that
  correctly returns M−1. Law stated honestly: N = number of DISTINCT eliminated
  modes. Now {1:1, 2:2, 3:3, 5:5} and the N=M consequences cited downstream
  (gravitational-clock, resistive-scale) are re-banked.

## 3. calc/u3_spectrum.py — E4a repaired

The Erlang cascade converges to the delay DISTRIBUTION δ(t−1), not the boxcar the
code compared against — hence the growing errors [0.721→1.193] under a
"decreasing" narrative. Repaired at step-response (CDF) level: L1 errors
[0.486, 0.376, 0.277, 0.198] for n = 2,4,8,16, decreasing at the CLT rate n^(−1/2).
The representation statement now holds at check level.

## 4. calc/u3_gravity_bath_spectral_match.py — narrative t⁻³ → t⁻⁴ (3 sites)

Docstring B3, the B7 summary, and the B8 `graviton_class` string all said t⁻³ for
the unit class while the body's check enforces −4.0 (the naive t⁻³ coefficient
Γ(3)cos(3π/2) vanishes). Long-flagged; now corrected. No logic changed.

## 5. calc/u3_continuum_origin.py — stale docstring t^(−d) → t^(−d/2)

The C3 docstring line contradicted the body's derived −d/2 (cusp term subleading).
Corrected. No logic changed.

## What this means for the record

- The dual pre-registration protocol has now fully executed: your v2 prereg
  (kinetic-only reasoning) was refuted by your own run; the adjudicator's sealed
  blinded prediction (three independent routes, d2da3a5) is confirmed at exponent
  AND coefficient level by the repaired instrument. First two-sided agreement in
  the program.
- The 'Cherenkov no-go' consequence chain (retained-sector kinematic condition,
  "which sectors satisfy ω_pair ≥ ω_k") is retired — the acoustic sector satisfies
  it at every oblique angle. What remains true and banked: same-sign closure,
  aligned-channel TT death, gapped-sector threshold emptiness.
- Standing suggestion (from four narrative-vs-run instances now repaired):
  assemble verdict/summary strings from measured variables (f-strings), never
  hand-write them — the repaired coupling calc does this throughout and is the
  template.

## Your checklist to take the reins

1. `python3.12 calc/u3_resistive_graviton_coupling.py` → expect 20/20,
   verdict `derived_within_class_onshell_omega7_channel_open`.
2. `python3.12 calc/u3_origin_persistence.py` → expect 7/7.
3. `python3.12 calc/u3_spectrum.py` → expect E4a PASS (count as before +1).
4. Rerun spectral-match and continuum-origin (text-only changes; JSONs regenerate).
5. Re-generate GRUT_EMERGENCE_HYPOTHESIS.md from claims/register if it ingests the
   repaired verdicts (the base rung L0/L1 entries strengthen; nothing else moves).
6. Next physics per the sealed ledger: the T3 confrontation mapping (compare
   J(ω) exponent classes in the certificate window; never raw lattice K_R tails).
