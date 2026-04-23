# Correction #20 — Track II Phase 4: flavor-selection mechanism evaluation

**Date:** April 22, 2026
**Status:** Honest negative on full closure. V7 §29 stays MAPPED;
Conjecture F1 stays HYPOTHESIS. Phase 4.0 scope document produced;
Phase 4.1 (attempted mechanisms) deferred to Phase 5.

## What was attempted

Phase 3 proved the CTP fixed-point at the EW scale is underdetermined
at the three-flavor level. Phase 4 evaluated three candidate GRUT-
native flavor-selection mechanisms against four mechanism requirements:

- **C1** — Flavor distinction (charged leptons vs. quarks vs. neutrinos)
- **C2** — Trace scale ⟨y⟩ = 3.605×10⁻³ at < 5% derivation precision
- **C3** — Z₃ compatibility with Phase 1 candidate θ = K·α_vac = 2/9
- **C4** — Lagrangian-grade mechanism (not numerical curve-fit)

Module: `grut/derived/flavor/koide_operator.py` — `direction_A_…`, `direction_B_…`, `direction_C_…`, `phase_4_mechanism_evaluation`, `phase_4_scope_document`.
Tests: `tests/flavor/test_koide_operator.py::TestPhase4FlavorMechanism` (14 tests, all pass).

## What was found

### Direction A — Anomaly-weighted CTP path counting at flavor level

Use the charged-lepton hypercharge content (Y²_cl = 5/4 per generation,
versus Y²_total = 10/3) in a CTP path-counting normalization analogous
to V7 §26.2.6.

| Candidate | Value | Dev % |
|:---|:---|:---|
| R · Y²_cl_per_gen / (108π) | 4.25×10⁻³ | 18% |
| (2−R)/S_B_baryogenesis | 1.50×10⁻³ | 58% |
| α_vac · (Y²_cl/Y²_total)² · (2−R) | 3.96×10⁻² | 999% |

**Verdict: PARTIAL.** C1 (flavor distinction via hypercharge content)
and C4 (SM-native group theory) both satisfied. C2 fails — best
candidate at 18% deviation, far from 5% threshold. C3 is orthogonal
(Direction A targets the trace scale; θ lives in the Z₃ eigenvalue
distribution).

The hypercharge ratios give O(1) distinctions among fermion classes
but cannot supply the O(10⁻³) loop-suppression regime the Yukawa
scale sits in.

### Direction B — Dielectric coupling with flavor-dependent kinetic mixing

Evaluate α_eff(ω) = α_vac/(1 + (ωτ_0)²) at charged-lepton Compton
frequencies and the EW scale:

| Scale | ω_Compton [Hz] | ωτ_0 | α_eff |
|:---|:---|:---|:---|
| electron | 7.8×10²⁰ | 10³⁶ | 3×10⁻⁷³ |
| muon | 1.6×10²³ | 10³⁸ | 7×10⁻⁷⁸ |
| tau | 2.7×10²⁴ | 10³⁹ | 3×10⁻⁸⁰ |
| top | 2.6×10²⁶ | 10⁴¹ | 3×10⁻⁸⁴ |
| v_EW | 3.7×10²⁶ | 10⁴¹ | 1×10⁻⁸⁴ |

**Verdict: FAILED.** C1, C2, C4 all fail. α_eff is ~70 decades below
the required 10⁻³ scale. V7 §28 has only gauge kinetic mixing; no
lepton-dark Yukawa operator exists. Adding one would be the Phase 2
curve-fit failure mode. Direction B is structurally incompatible
with the flavor sector as V7 currently formulates it.

### Direction C — Flavor-sector anomaly-matching analog to C_Cosmo

Construct R_flavor by restricting the 3-loop CTP machinery to charged-
lepton field content, then assemble ⟨y⟩ ~ (2−R_flavor)/S_flavor.

| Candidate | Value | Dev % |
|:---|:---|:---|
| (2 − R·N_cl/N_total) / S_B | 3.29×10⁻³ | 9.5% |
| (2 − R·(Y²_cl/Y²_total)²) / (108π) | 5.42×10⁻³ | 50% |
| (2 − R) / S_cl_Weyl | 1.12×10⁻² | 211% |
| (2 − R·(Y²_cl/Y²_total)) / (108π) | 3.93×10⁻³ | 9.0% |

**Verdict: FAILED on C2.** Best candidate at 9.0% deviation — in the
right regime but not derivation-grade (< 5% threshold). C1 is
inherited partially from Direction A. C4 is partial: flavor-subset R
inherits Lagrangian grade from V7 §26.2, but the specific weighting
(Y²-squared, linear, Weyl) requires its own derivation from the
3-loop machinery — not supplied here.

More importantly, Direction C inherits Phase 3's underdetermination
theorem: one trace-level equation does not determine three Yukawa
eigenvalues. Even if the trace formula closed at 5%, the three
eigenvalues would still require the Phase 1 candidate θ = 2/9 as an
auxiliary input. The V7 §31 baryogenesis formula's K_neq has no
charged-lepton analog derived in V7.

## What Phase 4 does NOT falsify

- Phase 1 CANDIDATE IDENTITY θ = K·α_vac = 2/9 at 4.6 ppm — untouched.
- Phase 2 HYPOTHESIS v_EW as sole viable anchor — untouched.
- Phase 3 HONEST NEGATIVE on direct Yukawa derivation — consistent.

All prior results survive intact. Phase 4's negative is at the
"propose a new mechanism" level, not at the "check existing claims"
level.

## What the three failures reveal

1. **Structural, not numerical.** The obstruction is not that a
   nearby expression is 10% off — it is that the CTP machinery at
   the three-flavor level is one-equation-in-three-unknowns, and
   restricting to charged-lepton field content does not supply the
   extra constraint. Directions A and C reach the right regime for
   ⟨y⟩ (10⁻³) but cannot close without an additional principle.

2. **Regime gap.** Yukawa hierarchy sits in the loop-suppression
   regime (y ~ (α/4π)^n · O(1)). GRUT's canonical dimensionless
   constants (α_vac = 1/3, S = 108π, R ≈ 1.15) produce O(1) and
   O(1/100) ratios rather than the O(10⁻³)–O(10⁻⁶) span the charged
   leptons actually occupy. Without an additional mass hierarchy or
   a loop-expansion parameter, the GRUT foundation cannot reach this
   regime by dimensional analysis.

3. **Mainstream-unsolved, not GRUT-specific.** Phase 4's verdict
   restates, from inside the CTP framework, a fifty-year-old open
   problem in SM extensions. Froggatt–Nielsen, extra dimensions,
   string landscape, asymptotic safety flavor — none has a complete
   derivation either. Expecting GRUT to solve this in-session was
   the low-probability branch the user acknowledged at the outset.

## Candidate Phase 5 directions (surfaced, not attempted)

- **P5-A — 3-loop CTP flavor-sector specialist calculation.** Redo
  the V7 §26.2.6 Correction #16 derivation with charged-lepton field
  content only, producing a genuine R_flavor_cl from first principles
  rather than by weighting R_anomaly. Estimated: ~2–4 weeks specialist
  work, similar to the TJI on S⁴ item (V7 §26.2.5).

- **P5-B — Froggatt–Nielsen style GRUT extension.** Introduce a
  GRUT-native U(1)_F flavor symmetry broken at Λ_F intermediate
  between v_EW and Λ_UV, with charges from Z₃-compatible CTP
  structure. Hierarchy emerges as (v_F/Λ_UV)^(q_i). Requires deriving
  the charges from CTP — which is what mainstream Froggatt–Nielsen
  also leaves unanswered.

- **P5-C — Wait for experimental input.** A sub-10-ppm m_τ
  measurement at CEPC/FCC-ee that confirms or falsifies θ = 2/9
  would narrow Phase 5 significantly. Confirmation reduces Phase 5
  to a single trace equation ⟨y⟩ = f(R, α_vac, S, v_EW).
  Falsification kills the Phase 1 candidate but leaves Direction A's
  C1 finding intact.

## Recommended posture

Phase 4.0 (this scope document) is the Track II deliverable. Phase
4.1 (attempted mechanisms) is DEFERRED to whichever of P5-A, P5-B,
or P5-C materializes first. Per the user's pipeline protocol, the
session moves to other Track II-adjacent work or to higher-leverage
tracks (TJI specialist calc, DESI/Euclid χ², Track VII dielectric
resolution) rather than spending more attention on a mainstream-
unsolved problem inside this session.

## Status ledger

| Item | Before | After |
|:---|:---|:---|
| V7 §29 | MAPPED | MAPPED (unchanged) |
| V7 Conjecture F1 | HYPOTHESIS | HYPOTHESIS (unchanged) |
| Phase 1 θ = 2/9 | CANDIDATE IDENTITY | CANDIDATE IDENTITY (unchanged) |
| Phase 2 v_EW anchor | HYPOTHESIS | HYPOTHESIS (unchanged) |
| Phase 3 derivation | HONEST NEGATIVE | HONEST NEGATIVE (unchanged) |
| Phase 4 directions | (pending) | A PARTIAL (C1+C4 only); B FAILED; C FAILED (C2) |
| Phase 4.0 scope | (pending) | DELIVERED (see `phase_4_scope_document`) |
| Phase 4.1 attempts | (pending) | DEFERRED to Phase 5 |

## Deliverables

| Artifact | Path |
|:---|:---|
| Phase 4 module | `grut/derived/flavor/koide_operator.py` (+ 3 direction evaluators + phase_4_mechanism_evaluation + phase_4_scope_document) |
| Tests | `tests/flavor/test_koide_operator.py::TestPhase4FlavorMechanism` (14 tests) |
| Log | This file |
| V8 §9.1 update | Separate edit to `theory/GRUT_V8_CLEAN.md` |

**Test suite: 458 passed** (444 baseline + 14 Phase 4 tests).
