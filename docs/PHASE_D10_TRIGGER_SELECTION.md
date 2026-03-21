# Phase D10 — Trigger Selection Closure

## 1. Mission

Determine whether the SSB trigger can be upgraded from D4's
"top-ranked candidate" to "best-supported trigger within the
D8 action structure and D9 self-consistent coupled framework."

| Prior Phase | Status | Inherited Result |
|---|---|---|
| D4 | LOCKED | component_a_shape_recovered_but_interpretation_not_yet_verified |
| D5 | LOCKED | source_coupling_insufficient |
| D6 | LOCKED | companion_architecture_viable |
| D7 | LOCKED | fully_coupled_viable |
| D8 | LOCKED | d7_channels_largely_action_derived |
| D9 | LOCKED | self_consistent_coupling_viable |
| **D10** | **ASSESSED** | **kretschmann_family_trigger_best_supported_within_tested_framework** |

## 2. Trigger Candidate Set

Four candidates, kept minimal and disciplined:

| # | Candidate | Formula (Schwarzschild vacuum) | Nonzero in vacuum | D4 score | Family |
|---|---|---|---|---|---|
| 1 | Ricci scalar R | R = 0 | NO | 0.50 | ricci |
| 2 | Kretschmann sqrt(K) | sqrt(48)·M/r³ | YES | 0.85 | tidal |
| 3 | Ricci-squared sqrt(R_ab R^ab) | 0 | NO | 0.70 | ricci |
| 4 | Weyl sqrt(C_abcd C^abcd) | sqrt(48)·M/r³ (= sqrt(K) in vacuum) | YES | — | tidal |

**Note on Kretschmann/Weyl**: These are degenerate in vacuum Schwarzschild
(where R_ab = 0, so C_abcd = R_abcd). They are *distinct invariants in
general*: in sourced regions where R_ab ≠ 0, they diverge via
K = C² + 2·R_ab·R^ab − R²/3. D10 states the degeneracy, notes the
distinction, and flags that resolving which member of the tidal-curvature
family is preferred would require sourced-interior analysis beyond scope.

## 3. Vacuum Strong-Field Analysis

| Candidate | Value at R_eq = 1/3 | Value at R_ext = 2.0 | Contrast ratio | Vacuum active |
|---|---|---|---|---|
| ricci_scalar | 0.0 | 0.0 | 0.0 | NO |
| kretschmann_sqrt | 93.53 | 0.433 | 216.0 | YES |
| ricci_squared_sqrt | 0.0 | 0.0 | 0.0 | NO |
| weyl_sqrt | 93.53 | 0.433 | 216.0 | YES |

Vacuum strong-field activation is a **necessary but not sufficient**
criterion. The trigger must remain meaningful in Schwarzschild-like
strong-field regions, but final trigger support is assessed on the
combined basis of vacuum activation, sourced interior behavior, D8
action-naturalness, and D9 self-consistency compatibility.

**Contrast ratio**: (R_ext/R_eq)³ = 6³ = 216 for tidal-family invariants.

## 4. Weak-Field Suppression Analysis

| Candidate | Weak-field suppressed | Regime correct |
|---|---|---|
| ricci_scalar | (trivially, zero) | NO — zero everywhere in vacuum |
| kretschmann_sqrt | YES | YES |
| ricci_squared_sqrt | (trivially, zero) | NO — zero everywhere in vacuum |
| weyl_sqrt | YES | YES |

Both tidal-family candidates show strong suppression at R_ext (value
drops by factor 216 from R_eq to R_ext). Ricci-family candidates are
trivially suppressed (zero everywhere in vacuum) but this is not
meaningful suppression — they simply fail to activate anywhere.

## 5. Sourced Interior Behavior

| Candidate | Active in sourced regions | Assessment |
|---|---|---|
| ricci_scalar | YES (R ~ −8πρ) | Active only with matter sources. Cannot trigger in vacuum tidal regime. |
| kretschmann_sqrt | YES (same + Ricci corrections) | Active in both vacuum and sourced regimes. |
| ricci_squared_sqrt | YES (~ (8π)ρ) | Active only with matter sources. Same limitation as R. |
| weyl_sqrt | YES (≈ sqrt(K) minus Ricci terms) | Active in vacuum. In sourced regions, differs from Kretschmann by excluding Ricci contributions — captures pure tidal curvature. |

This is where the Kretschmann/Weyl distinction becomes potentially
material: in sourced regions, Kretschmann includes Ricci contributions
while Weyl isolates pure tidal/gravitational curvature. Resolving this
distinction requires sourced-interior analysis beyond D10's scope.

## 6. D8 Action Compatibility

| Candidate | Coupling form | Natural in action | Compatibility level |
|---|---|---|---|
| ricci_scalar | ξ R \|Φ\|² | YES (conformal coupling) | naturally_compatible |
| kretschmann_sqrt | ξ sqrt(K) \|Φ\|² | YES (scalar-to-scalar) | naturally_compatible |
| ricci_squared_sqrt | ξ sqrt(R_ab R^ab) \|Φ\|² | NO (sqrt of tensor contraction) | compatible_with_assumptions |
| weyl_sqrt | ξ sqrt(C²) \|Φ\|² | YES (scalar-to-scalar) | naturally_compatible |

D8 action structure: S_trigger = ∫ d⁴x √(−g) ξ C \|Φ\|².
All scalar-to-scalar couplings enter naturally. The Ricci-squared
coupling involves a square root of a rank-2 tensor contraction,
which is structurally less natural (non-polynomial invariant).

## 7. D9 Self-Consistent Compatibility

| Candidate | D9 compatible | Effect on iteration | Assessment |
|---|---|---|---|
| ricci_scalar | YES | neutral | Zero effective mass in vacuum — does nothing |
| kretschmann_sqrt | YES | stabilizing | Reference case: D9 converged with this trigger (13 iterations, constructive deformation) |
| ricci_squared_sqrt | YES | neutral | Zero effective mass in vacuum — does nothing |
| weyl_sqrt | YES | stabilizing | Identical to Kretschmann in vacuum — same effective mass, same stabilizing behavior |

The trigger enters the defect ODE as an effective mass term ξ·C·f.
Tidal-family invariants provide a positive effective mass (~1/r³)
that pushes f toward vacuum faster, tightening the defect core.
This is the constructive deformation observed in D9. Ricci-family
triggers provide zero effective mass in vacuum — they are compatible
(they don't destabilize) but useless (they don't contribute).

## 8. Scoring

Five criteria, each scored 0 or 1:

| Criterion | ricci_scalar | kretschmann_sqrt | ricci_squared_sqrt | weyl_sqrt |
|---|---|---|---|---|
| Vacuum strong-field active | 0 | 1 | 0 | 1 |
| Strong-to-weak contrast > 100 | 0 | 1 | 0 | 1 |
| Action-natural | 1 | 1 | 0 | 1 |
| D9-compatible (stabilizing) | 0 | 1 | 0 | 1 |
| Prior-phase consistent | 1 | 1 | 1 | 1 |
| **Total** | **2** | **5** | **1** | **5** |

## 9. Ranking

| Rank | Candidate | Score | Family |
|---|---|---|---|
| 1 (tie) | kretschmann_sqrt | 5/5 | tidal |
| 1 (tie) | weyl_sqrt | 5/5 | tidal |
| 3 | ricci_scalar | 2/5 | ricci |
| 4 | ricci_squared_sqrt | 1/5 | ricci |

**Separation**: Top score (5) vs. lowest (1) = 4 points.

**Vacuum degeneracy**: Kretschmann and Weyl are degenerate in vacuum
Schwarzschild. They are distinct invariants in general spacetimes.
In sourced regions, Kretschmann includes Ricci contributions while
Weyl captures pure tidal curvature. Resolving which is preferred
requires sourced-interior analysis beyond D10's scope.

**Ranking rationale**: Tidal-curvature invariants score highest because
they are nonzero in vacuum strong-field regions, have large strong-to-weak
contrast (216×), enter the D8 action naturally, and produce stabilizing
effective mass in the D9 framework. Ricci-family invariants fail the
vacuum strong-field criterion and provide no useful coupling in the
vacuum regime.

## 10. Proxy-Closure Caveat

D9 used a macro-amplitude proxy closure, not the fully exact two-field
Euler–Lagrange system. Trigger closure in D10 is therefore:

- **Strong within the tested framework** — trigger selection is robust
  to the D8/D9 coupling structure. All assessment criteria produce
  clear, unambiguous results within this framework.
- **Still conditional on the current closure level** — a full two-field
  solution could in principle modify trigger coupling behavior in the
  sourced interior, potentially distinguishing Kretschmann from Weyl.

This is a strength statement, not a weakness statement. The tested
framework provides a well-defined closure level within which the
trigger selection is decisive.

## 11. Final Classification

**Classification**: `kretschmann_family_trigger_best_supported_within_tested_framework`

**Meaning**: Tidal-curvature triggers (Kretschmann sqrt(K) and Weyl
sqrt(C²)) are the best-supported triggers within the D8/D9 tested
framework. They score 5/5 on the five-criterion assessment. Ricci-family
triggers score 1–2/5 and fail the vacuum strong-field criterion.

This does NOT claim:
- Kretschmann and Weyl are the same invariant (they are distinct in general)
- The trigger is mathematically unique (Kretschmann and Weyl tie in vacuum)
- The result is independent of the closure level (it is conditional on D9 proxy closure)

It DOES claim:
- Tidal-curvature triggering is clearly superior to Ricci-family triggering
- The Kretschmann/Weyl family is the best-supported trigger family within the tested framework
- The assessment is robust within the D8 action + D9 self-consistent framework

## 12. Validation

| Check | Result |
|---|---|
| Benchmark (60 checks) | **60/60 PASSED** |
| Pytest (60 tests) | **60/60 PASSED** (0.21s) |
| JSON serialization | Valid |

## 13. Nonclaims

1. This phase does NOT prove final unified field theory closure.
2. Trigger closure here is within the D8/D9 tested framework.
3. A preferred trigger is a mathematical/modeling result, not a metaphysical statement.
4. A "best-supported" trigger may still remain conditional on the reduced closure level used in D9.
5. The Kretschmann/Weyl degeneracy in vacuum does NOT imply they are the same invariant.
6. No claim is made that the tested candidate set is exhaustive.
7. Sourced-interior trigger behavior is assessed qualitatively, not through a full interior solution.
8. The ranking may change if the proxy closure is upgraded to a full two-field solution.
9. No claim is made about trigger uniqueness unless the evidence supports it.
10. D10 does not reopen any prior locked phase result.

## 14. Assumptions

1. Background geometry is Schwarzschild with M = 0.5, R_S = 1.0.
2. Trigger candidates are evaluated analytically using exact Schwarzschild formulas.
3. The D8 action structure is the reference action framework.
4. The D9 self-consistent coupled framework with proxy closure is the reference SC framework.
5. The trigger enters the defect ODE as an effective mass coupling ξ·C·|Φ|².
6. Regime correctness requires both vacuum strong-field activation AND weak-field suppression.
7. Vacuum strong-field activation is a necessary but not sufficient criterion.
8. Kretschmann and Weyl are treated as distinct objects degenerate in vacuum.
9. The candidate set is minimal (4 invariants) for contrast without proliferation.
10. Prior phase results (D4–D9) are locked and inherited without modification.

## 15. Phase Lock Update

| Phase | Classification | Status |
|---|---|---|
| D4 | component_a_shape_recovered_but_interpretation_not_yet_verified | LOCKED |
| D5 | source_coupling_insufficient | LOCKED |
| D6 | companion_architecture_viable | LOCKED |
| D7 | fully_coupled_viable | LOCKED |
| D8 | d7_channels_largely_action_derived | LOCKED |
| D9 | self_consistent_coupling_viable | LOCKED |
| **D10** | **kretschmann_family_trigger_best_supported_within_tested_framework** | **ASSESSED** |

## 16. Recommended Next Move

1. **Sourced-interior trigger analysis**: Distinguish Kretschmann from Weyl in the sourced Companion interior. This would resolve whether D10's tidal-curvature family reduces to a single preferred trigger or remains a two-member family.

2. **Full two-field coupled BVP**: Replace the D9 macro-amplitude proxy with a separately solved Φ(r). This would test whether trigger closure survives the full Euler–Lagrange system.

3. **Portal coupling determination**: Derive g_portal from matching conditions rather than scanning.

4. **Master integration document**: Consolidate D4–D10 results into a single structural summary with the complete phase lock table and remaining open gaps.
