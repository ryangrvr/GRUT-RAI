# Correction #18 — Track II Phase 2: Mass-anchor mechanism evaluation

**Date:** April 22, 2026
**Status:** Honest negative on Λ_QCD and v_dark; v_EW Yukawa identified
as the sole viable anchor. V7 §29 stays MAPPED; Conjecture F1 stays
HYPOTHESIS. Phase 3 is redirected to deriving the three Yukawa
eigenvalues (not M₀ directly).

## What was attempted

Phase 1 left M₀ with a 20-order-of-magnitude dimensional gap to the
only mass scale native to GRUT's canonical foundation. Phase 2
evaluates three candidate mechanisms for supplying a GeV-scale
anchor, on mechanism grounds — is there a Lagrangian operator that
couples the anchor to the charged-lepton sector? — not on numerical
fit grounds.

Module: `grut/derived/flavor/koide_operator.py:evaluate_mass_anchor_mechanisms()`
Tests: `tests/flavor/test_koide_operator.py::TestPhase2MassAnchorMechanisms` (11 tests, all pass)

The rejection criterion is explicit: **numerical proximity between
M₀² and any combination of (R, α_vac, S, anchor) is NOT evidence
of a derivation**. A near-miss without a Lagrangian operator is the
exact failure mode V7's architecture rejects.

## What was found

### Mechanism 1 — v_EW Yukawa (SM-native) → HYPOTHESIS

- Lagrangian operator: `L_Yuk = −y_i Ψ̄_L^i H ℓ_R^i + h.c.` — present in
  V7 §8 (SM-emergence sector).
- Anchor relation: `m_i = y_i · v_EW/√2` ⇒ `M₀² = (v_EW/√2) · Σy_i / 6`
- Numerical: `M₀²` from (Y_E, Y_MU, Y_TAU) reproduces the fit at
  9.2 ppm — the residual is purely the rounding of the PDG Yukawa
  values, not a mechanism failure.
- The operator exists and is SM-canonical; the three eigenvalues
  (2.94×10⁻⁶, 6.07×10⁻⁴, 1.02×10⁻²) are SM INPUTS in V7 §8, not yet
  derived from S_CTP. **Status: HYPOTHESIS** (mechanism present,
  eigenvalues pending). This is the viable path.

### Mechanism 2 — Λ_QCD (non-SM coupling) → FAILED

- Lagrangian operator: **NONE**. Charged leptons are color singlets;
  SM-level Λ_QCD enters lepton masses only through two-loop gluon
  corrections at O(α_s²/π²)·(m_q/m_lepton)² — numerically negligible.
- V7 §16 (noise kernel, constitutive) introduces no lepton-quark
  operator beyond the SM.
- Numerical proximity `M₀²/Λ_QCD ≈ 1.26` is a coincidence rejected by
  the no-curve-fitting rule.
- **Status: FAILED.** Inventing a new lepton-quark operator to
  anchor M₀ would be ad hoc machinery — the failure mode the
  protocol rejects.

### Mechanism 3 — v_dark (V7 §28) → FAILED

- Lagrangian operators present in V7 §28: U(1)_dark kinetic term,
  dark scalar potential `V(φ_dark) = (λ/4)(|φ_dark|² − v_dark²)²`, and
  kinetic mixing `L_mix = −(ε/2) F^{μν} F_{μν,dark}`.
- The only portal between sectors is the gauge-boson kinetic mixing
  (dark-photon ↔ SM photon). It couples gauge fields, not fermion
  masses. No `H†_dark · L̄ · ℓ_R` Yukawa exists in V7 §28.
- The anomaly coupling `C_FINAL ↔ C_dark` is a relation between
  gauge anomaly coefficients, not a fermion mass operator.
- Numerical proximity `v_dark ≈ R² · M₀²` within 1.1% is a
  coincidence — the exact curve-fitting pattern Phase 2 rejects.
- **Status: FAILED.** V7 §28 provides no Lagrangian operator
  coupling v_dark to the charged-lepton sector. Adding one requires
  its own derivation.

## Phase 3 redirect

With v_EW identified as the sole viable anchor, the Phase 3 problem is
no longer "derive M₀ from the foundation" but rather:

> Derive the three charged-lepton Yukawa eigenvalues
> `(y_e, y_μ, y_τ) = (m_i √2 / v_EW)` from the multi-generation CTP
> fixed-point condition `z* = z_target[z*]`, with `v_EW` as an input
> (not derived) and `θ = K · α_vac` from the Phase 1 CANDIDATE IDENTITY
> as the Z₃ phase.

**Well-posedness:** v_EW is an SM input accepted by all of mainstream
flavor physics; reducing M₀ to Σy_i and the Z₃ phase means Phase 3
faces one equation — `Σy_i/6 = ⟨y⟩` as a function of (R_anomaly,
α_vac, S) — plus the Z₃ eigenvalue distribution set by θ. No
dimensional-anchor gap remains.

**What Phase 3 MUST NOT do:** construct a closed-form operator
combination of (R, α_vac, S, v_dark, Λ_QCD, μ_0) that fits
M₀² = 0.3138 GeV. That is numerology without falsifiable content
and is rejected by V7's honesty protocol. Any apparent "derivation"
produced that way carries no physical content.

## Status

| Item | Before | After |
|:---|:---|:---|
| V7 §29 | MAPPED | MAPPED (unchanged) |
| V7 Conjecture F1 | HYPOTHESIS | HYPOTHESIS (unchanged) |
| M₀ anchor problem | 3 candidates | 1 viable (v_EW) |
| Phase 3 goal | "derive M₀" | "derive (y_e, y_μ, y_τ) from Z₃ fixed-point with v_EW input" |

No status upgrades. No modifications to canonical constants.
The Phase 1 CANDIDATE IDENTITY `θ = K · α_vac = 2/9` survives intact
and supplies the Z₃ phase for the Phase 3 Yukawa derivation.

## Deliverables

| Artifact | Path |
|:---|:---|
| Phase 2 evaluator | `grut/derived/flavor/koide_operator.py:evaluate_mass_anchor_mechanisms()` |
| Tests | `tests/flavor/test_koide_operator.py::TestPhase2MassAnchorMechanisms` |
| Log | This file |

**Test suite: 429 passed** (418 baseline + 11 Phase 2 tests).
