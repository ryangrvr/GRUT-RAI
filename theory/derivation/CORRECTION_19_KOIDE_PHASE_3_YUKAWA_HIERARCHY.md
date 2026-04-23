# Correction #19 — Track II Phase 3: CTP fixed point does not constrain charged-lepton Yukawas

**Date:** April 22, 2026
**Status:** Honest negative. V7 §29 stays MAPPED; Conjecture F1 stays HYPOTHESIS.
Phase 1 CANDIDATE IDENTITY (θ = K·α_vac = 2/9) and Phase 2 HYPOTHESIS
(v_EW as sole viable anchor) both preserved. Phase 4 is identified
as the charged-lepton half of the Yukawa hierarchy problem.

## What was attempted

Phase 1 closed with θ = K·α_vac = 2/9 as CANDIDATE IDENTITY (at 4.6 ppm, 56×
inside the PDG m_τ window). Phase 2 identified v_EW as the sole viable
dimensional anchor, with Λ_QCD and v_dark both FAILED on Lagrangian-operator
grounds. Phase 3 target: with v_EW as SM input and θ = 2π/3 + 2/9 = 2.316 rad
as the Z₃ phase, derive the three charged-lepton Yukawa couplings
(y_e, y_μ, y_τ) = (2.94×10⁻⁶, 6.07×10⁻⁴, 1.02×10⁻²) or at least their
trace-level scale ⟨y⟩ = Σy_i/3 = 3.605×10⁻³ from the multi-generation
CTP fixed-point condition z* = z_target[z*].

Module: `grut/derived/flavor/koide_operator.py:phase_3_yukawa_derivation_attempt()`
Tests: `tests/flavor/test_koide_operator.py::TestPhase3YukawaDerivation` (14 tests, all pass)

## What was found

**The CTP fixed point does not constrain the Yukawa couplings.**
The SM Lagrangian at the EW scale contains V(H) = −μ²|H|² + λ|H|⁴ and
L_Yuk = −y_i Ψ̄_L^i H ℓ_R^i + h.c. The CTP fixed-point condition
z* = z_target[z*] applied to this system fixes ⟨H⟩ = v_EW/√2 as the
Mexican-hat minimum, and after EWSB delivers m_i = y_i · v_EW/√2.
The Jacobian M_ij in mass basis is diagonal with eigenvalues m_i.

But the three y_i are independent Lagrangian inputs; the fixed-point
condition is satisfied for any choice. Conjecture F1's claim that M_ij
is Z₃-circulant in flavor basis is a RESTRICTION on the Lagrangian
input, not a derivation from the fixed-point condition. V7 §29's
action-specification gap (Phase 1 blocker i) does not close by
supplying the SM Yukawa operator — the operator is present, but it
takes the y_i as free parameters.

**No mechanism-free numerical survey rescues the derivation.**
Dimensionless combinations of (R, α_vac, S, α_s(M_Z), α_em(M_Z))
against ⟨y⟩ = 3.605×10⁻³, ranked by deviation:

| Expression | Value | Ratio | Dev % |
|:---|:---|:---|:---|
| α_vac · α_s/(4π) | 3.13×10⁻³ | 0.87 | 13% |
| √α_vac · α_em | 4.51×10⁻³ | 1.25 | 25% |
| (2−R)/S = H_inf·τ₀ | 2.49×10⁻³ | 0.69 | 31% |
| (2−R)/(S·R) | 2.16×10⁻³ | 0.60 | 40% |
| (2−R)²/S | 2.11×10⁻³ | 0.59 | 42% |
| α_em/(4π) | 6.22×10⁻⁴ | 0.17 | 83% |
| α_s/(4π) | 9.40×10⁻³ | 2.61 | 161% |

Nothing at derivation-level precision (< 5%). The closest candidate,
α_vac · α_s/(4π) at 13% off, is rejected on mechanism grounds:
charged leptons are color singlets and have no tree-level coupling to
α_s. Any y_lepton ∝ α_s expression without a mediating operator is
the exact curve-fitting pattern the honesty protocol prohibits.

## Why this is Phase 4 = Yukawa hierarchy problem (mainstream-unsolved)

The SM has no uniform loop-suppression mechanism across the fermion
content. Empirically:

| Fermion | Yukawa | Order |
|:---|:---|:---|
| t (top quark) | y_t ≈ 1.00 | 10⁰ |
| b (bottom) | y_b ≈ 2.4×10⁻² | 10⁻² |
| τ | y_τ ≈ 1.02×10⁻² | 10⁻² |
| c (charm) | y_c ≈ 7.3×10⁻³ | 10⁻² |
| μ | y_μ ≈ 6.07×10⁻⁴ | 10⁻⁴ |
| s (strange) | y_s ≈ 5.5×10⁻⁴ | 10⁻⁴ |
| u, d | y_{u,d} ≈ 10⁻⁵ | 10⁻⁵ |
| e | y_e ≈ 2.94×10⁻⁶ | 10⁻⁶ |

The span is six orders of magnitude. No single-power-of-(α/4π) Ansatz
covers y_t ≈ 1 and y_e ≈ 10⁻⁶ simultaneously. The Froggatt-Nielsen
framework explains the hierarchy by assigning integer U(1)_FN charges
to each fermion and recovering y_ij ∝ (v_FN/Λ)^(q_i + q_j + q_H) —
but the charges themselves are inputs. No mechanism is currently
accepted that DERIVES the three charged-lepton Yukawas (or, more
generally, the full Yukawa matrix pattern) from first principles.

Phase 3's honest-negative outcome is therefore not a GRUT-specific
failure. It is a restatement, from inside the CTP framework, of a
well-known mainstream open problem. Phase 4 is correspondingly:

> Identify a GRUT-native flavor-selection mechanism BEYOND the SM
> Yukawa operator that forces charged-lepton Yukawas specifically
> to the 10⁻³ trace stratum — i.e., derive the charged-lepton half
> of the Yukawa hierarchy from first principles.

This is a genuinely open research direction. It is narrower than the
full hierarchy problem (it asks only for the charged-lepton trace,
not for the full 3×3×3 Yukawa matrix), and it sits in the smallest
possible working space: ⟨y⟩ as a function of (R, α_vac, S, v_EW, Λ_UV?).
If θ = 2/9 is directly confirmed by a sub-10-ppm m_τ measurement
(Phase 1 falsifier), Phase 4 reduces further to the single trace
equation ⟨y⟩ = f(GRUT constants).

## What Phase 3 does NOT falsify

The Phase 1 CANDIDATE IDENTITY θ = K·α_vac = 2/9 is untouched.
Given the trace scale ⟨y⟩ as input, θ determines how the three
eigenvalues are distributed across the Z₃ circulant. Phase 3's
failure to derive ⟨y⟩ does not disturb the distribution's structure.
Test `test_phase_3_does_NOT_falsify_phase_1_candidate` pins this
architecturally.

The Phase 2 HYPOTHESIS (v_EW as sole viable anchor) is also
untouched. The reduction M₀² = (v_EW/√2) · Σy_i / 6 still holds;
what remains open is Σy_i itself.

## Cross-sector consistency

- Canonical constants (R, S, α_vac, τ_0) are not modified.
- SM inputs (v_EW, α_s, α_em) are not modified.
- No structural claim of V7's foundation is altered.
- Phase 1 and Phase 2 results survive intact.

## Status ledger

| Item | Before | After |
|:---|:---|:---|
| V7 §29 | MAPPED | MAPPED (unchanged) |
| V7 Conjecture F1 | HYPOTHESIS | HYPOTHESIS (unchanged) |
| Phase 1 θ = 2/9 candidate | CANDIDATE IDENTITY | CANDIDATE IDENTITY (unchanged) |
| Phase 2 v_EW anchor | HYPOTHESIS | HYPOTHESIS (unchanged) |
| Phase 3 ⟨y⟩ derivation | (pending) | HONEST NEGATIVE |
| Phase 4 problem | (pending) | "Yukawa hierarchy at the charged-lepton trace" — a well-posed Phase 4 |

## Deliverables

| Artifact | Path |
|:---|:---|
| Phase 3 module functions | `grut/derived/flavor/koide_operator.py:phase_3_yukawa_derivation_attempt()` (+ helpers) |
| Tests | `tests/flavor/test_koide_operator.py::TestPhase3YukawaDerivation` |
| V8 paragraph | `phase_3_yukawa_derivation_attempt()['V8_track_II_phase_3_paragraph']` |
| Log | This file |

**Test suite: 444 passed** (430 baseline + 14 Phase 3 tests).
