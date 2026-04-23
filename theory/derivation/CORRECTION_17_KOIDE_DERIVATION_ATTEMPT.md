# Correction #17 — Track II Phase 1 Koide (M₀, θ) derivation attempt: HONEST NEGATIVE with one CANDIDATE IDENTITY

**Date:** April 22, 2026
**Status:** Honest negative. V7 §29 stays MAPPED; Conjecture F1 stays HYPOTHESIS.
One CANDIDATE IDENTITY flagged for future falsification: θ = K · α_vac = 2/9.

## What was attempted

V8 Track II Phase 1: derive the two free parameters (M₀ ≈ 0.560 GeV^(1/2),
θ ≈ 2.317 rad) of the Z₃ circulant Koide mass operator from GRUT's canonical
constants (R_anomaly = 1.15428, S = 108π, α_vac = 1/3, τ₀ = 41.9 Myr) via
the multi-generation CTP fixed-point condition z* = z_target[z*] with
z_target[z] = z − F_spatial[z] / F_temporal (V7 §29).

Module: `grut/derived/flavor/koide_operator.py`.
Tests: `tests/flavor/test_koide_operator.py` (26 tests, all pass).

## What was found

### (A) Derivation fails — underdetermined

Two independent blockers:

1. **Multi-flavor action specification gap.** V7 §29 asserts the Jacobian
   dz_target_i/dz_j at z* is Z₃-circulant with eigenvalues equal to the
   three lepton masses (Conjecture F1), but does NOT specify F_spatial
   and F_temporal for the three-flavor sector. Without the flavor-space
   classical action F[z] = 0 we cannot compute the Jacobian from first
   principles — the Z₃-circulant shape remains a claim about the fixed
   point, not a theorem derived from it.

2. **M₀ dimensional anchor gap.** M₀ has units GeV^(1/2). GRUT's canonical
   foundation (R, S, α_vac, τ₀) contains no GeV-scale mass. The only
   mass scale derivable from the foundation is μ_0 = ℏ/τ₀ ≈ 1.57 × 10⁻³¹ eV,
   giving √μ_0 ≈ 10⁻²⁰ GeV^(1/2) — ~20 orders of magnitude smaller than
   the required 0.56 GeV^(1/2). Without importing an external mass anchor
   (Λ_QCD, v_EW, or v_dark from §11), M₀ cannot be derived from the
   foundation alone.

### (B) One CANDIDATE IDENTITY worth flagging

A numerical survey of simple dimensionless combinations of (R, S, α_vac)
against the fitted θ (mod 2π/3) surfaces exactly one match below the
0.1% threshold:

    θ_candidate = K · α_vac = (2/3) · (1/3) = 2/9 = 0.22222222…
    θ_fit       = θ_FIT mod 2π/3            = 0.22222120…
    deviation   = 4.6 ppm

Experimental-uncertainty propagation from the PDG m_τ error gives
~258 ppm window on θ, so this candidate sits **56× inside the current
experimental window** — well below detection threshold but
consistent with data.

This is labeled **CANDIDATE IDENTITY** (a status tier below DERIVED /
COMPUTED and above HYPOTHESIS): a tight numerical observation without
a derivation. Upgrading to DERIVED requires a proof from S_CTP that
the multi-generation CTP fixed point selects θ = K · α_vac for the
three-flavor Z₃ circulant.

**Falsifier (Track II-F1):** a CEPC / FCC-ee m_τ measurement at
≤10 ppm precision that excludes θ = 2/9 at > 5σ kills the candidate.
Confirmation restores leverage for a proper derivation.

## Why the negative result survives the honesty protocol

Per V7 status tiers: a status upgrade to COMPUTED or DERIVED requires
strict derivation from S_CTP with no free parameters. The attempt
produces neither — (A) blocks any derivation attempt, and (B) prevents
the candidate identity in θ from constraining M₀. No upgrade is made.

V7 §29 therefore remains **MAPPED** (unchanged).
V7 Conjecture F1 remains **HYPOTHESIS** (unchanged).

The Z₃ identity K = 2/3 and N = 3 uniqueness (both PROVEN algebraically)
are independent of this attempt and are **unaffected**. The failure is
confined strictly to the two free parameters (M₀, θ) that the identity
does not determine.

## Cross-sector consistency

- Canonical constants (R, S, α_vac, τ₀) are not modified.
- No structural claim of the foundation is altered.
- The attempt is contained within V7's canonical framework and the
  framework survives intact.

## What would close it

1. Derive F_spatial[z] and F_temporal for the three-flavor sector from
   S_CTP, with the Z₃-circulant Jacobian at z* emerging by construction.
2. Either (a) derive v_EW from the EW fixed point, (b) derive Λ_QCD
   from the confinement fixed point, or (c) connect M₀² to v_dark via
   a multi-generation coupling relation — supplying the missing GeV
   mass anchor.
3. Sub-10-ppm experimental determination of m_τ that falsifies or
   confirms θ = 2/9.

## Deliverables

| Artifact | Path | Status |
|:---|:---|:---|
| Module | `grut/derived/flavor/koide_operator.py` | New, 26 tests pass |
| Tests | `tests/flavor/test_koide_operator.py` | 26/26 pass |
| V8 §Track II summary paragraph | `derivation_attempt()['V8_track_II_summary_paragraph']` | Embedded |
| Correction-log entry | This file | — |

Full test suite: **418 passed** (392 baseline + 26 Track II).
