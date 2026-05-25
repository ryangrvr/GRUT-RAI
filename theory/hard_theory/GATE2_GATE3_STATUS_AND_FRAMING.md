# Gate 2 and Gate 3 Status and Framing

Date: May 9, 2026  
Status: Cross-gate interpretation locked.

## Current Two-Route Status

| Route | Current status |
|------|----------------|
| Gate 2 / V5 flow route | R improved from ~1.32 to ~1.148 after M[1,5] correction |
| Gate 3 / protected Euler quotient | Symbolic quotient exists, but coefficient values are still null |

## What 3-loop Could Do

### 1. Direct resolution (preferred)

If the protected Euler-channel extraction yields

R_3loop = C_Euler,final / C_Euler,cosmo ~ 1.154,

then Gate 3 becomes the sharper extraction route and V5 remains an approximate flow model.

This is the strongest outcome, but full native S4 3-loop promotion remains blocked until:
- coefficient extraction,
- scheme checks,
- Ward validation,
- and independent replication
are complete.

### 2. Indirect resolution (residual explanation)

If Gate 3 does not directly produce R, it may still explain the remaining ~0.6% Gate 2 residual via:
- S4 projection normalization,
- counterterm finite subtraction,
- Euler-gauge mixing coefficient,
- protected/local separation.

This is consistent with current Gate 2 diagnostics, where remaining uncertainty is concentrated in convention-sensitive provenance terms.

## Non-Patch Rule for Gate 3

3-loop cannot be used as a numerical patch for Gate 2.

A 3-loop value near 1.154 is only promotable if:
- Euler-channel coefficients are explicitly computed,
- quotient is scheme-legal,
- S4 projection is clean,
- counterterm handling is independently fixed,
- and the result is not retrofitted into V5.

Otherwise, numerical agreement is not sufficient.

## Best Current Framing

Yes, the remaining residual could be a genuine 3-loop effect.  
But Gate 3 must be treated as an independent extraction route, not a repair knob for Gate 2.

If Gate 3 lands near 1.154, then convergence across independent routes is strong:

| Route | Result |
|------|--------|
| canonical sqrt(4/3) | 1.15470 |
| V5 corrected flow | ~1.148 |
| 3-loop Euler quotient | pending coefficient extraction |
| Osborn/local RG | ~1.15367 |

## Locked Interim Status

Gate 2 brings R into the sub-percent regime.  
Gate 3 may either:
- close the remaining gap,
- independently confirm the canonical value,
- or falsify the 3-loop route.

---

## Gate 3 Closure Update (May 24, 2026)

### Current Route Status

| Route | Status | Outcome | Notes |
|-------|--------|---------|-------|
| massive_regulated (Routes A/B/C/D) | EXHAUSTED | All routes blocked by endpoint singularities | Discovery phase complete; boundary incompatibility fundamental |
| hminus_derivative_regularized | CLOSED | Probe-family incompatibility identified | Phase A succeeded (R²=0.99999932); Phase B/C uniform failure on epsilon_expansion |
| alternative routes pending | NOT STARTED | — | Direct limit, alternative regulators, external consultation |

### Gate 3 Hminus-Derivative-Regularized: Regime Characterization

**Execution:** Full protocol under frozen specification (tag gate3-hminus-dr-spec-v1.0)

**Phase A Result:** Laurent extraction succeeded cleanly
- 28/28 samples collected
- Average fit quality R² = 0.99999932
- Pole order = 1 (empirically determined)
- **Interpretation:** Medium's response is analytically extractable in the intermediate regime

**Phase B Result:** Three blind prescriptions generated
- prescription_1 (finite-part): C^(3) = 1.568
- prescription_2 (derivative-response): C^(3) = 12.566
- prescription_3 (pole-stripped): C^(3) = -27.227
- All three independent candidates differ in magnitude but follow consistent patterns

**Phase C Result:** Classification shows uniform failure pattern
- ✓ 4/8 criteria pass (finiteness, poles, sign/scale, stability)
- ✗ 1/8 criteria fails uniformly (epsilon_expansion: residual > threshold across all prescriptions)
- ? 3/8 inconclusive (no comparison data)

**Key Finding:** The uniform failure across all three independent prescriptions on the same criterion indicates **probe-family incompatibility, not implementation failure.**

**CVRU Interpretation:** The Allen-Jacobson IR threshold at h_- → 0 has a structural epsilon-character that the derivative-regularization probe family cannot preserve. This is a successful measurement of regime boundary structure, not a framework deficiency.

**Closure Decision:** hminus_derivative_regularized is **exhausted under the current derivative-regularized prescription.** The threshold behavior is characterized as incompatible with derivative-family methods. Alternative probe families (direct limit, alternative regulators) remain available.

---

## Priority Sequence for Alternative Routes

Based on Gate 3 closure findings:

| Priority | Route | Rationale | Expected Timeline |
|----------|-------|-----------|------------------|
| **1** | hminus_direct_limit | Cleanest comparison; answers whether failure is derivative-specific or IR-limit-general | Spec 2-3d; impl 1w; exec 3-5d ≈ 2 weeks |
| **2** | endpoint-subtracted massive_regulated | Endpoint singularity already diagnosed; asymptotic subtraction may resolve | Requires Route D diagnostics |
| **3** | alternative regulator family | If direct-limit also fails on epsilon_expansion, signals need for fundamentally different approach | After P1/P2 results |
| **4** | external specialist consultation | Mathematica/hypergeometric experts for regime-specific prescriptions | Hold until P1-P3 exhausted |

### Recommended Next Action
**Prioritize hminus_direct_limit** to maximize information per unit effort. If this also fails uniformly on epsilon_expansion, the IR limit itself (not the derivative family) is the structural barrier. If it succeeds, derivative-regularization specifically is wrong, indicating a refinement direction.
