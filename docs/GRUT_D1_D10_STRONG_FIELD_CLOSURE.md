# GRUT Strong-Field Closure: Phases D1–D10

**Technical Source Package — Zenodo Archive Draft**

---

## Abstract

This document archives the strong-field sector of the GRUT interior program as assessed through ten successive analytical and numerical phases (D1–D10). The classical GRUT scalar-memory sector, locked through Phase 6C, produces a two-component energy-density deficit decomposition ε(r) = Component A (∝ 1/r⁴) + Component B (∝ 1/r²). Prior exhaustion of classical routes (Route B, Route C, Source-Law Program I) established that no GRUT-native classical mechanism generates Component B. Phases D1–D10 introduce, test, couple, and assess an O(3) topological defect extension under progressively relaxed approximations. The leading surviving architecture is a dual-sector Companion model — scalar-memory (Component A) plus curvature-triggered hedgehog defect (Component B) — with a portal interaction Φ²|Φ⃗|² providing the structural inter-sector coupling. Metric positivity on the tested radial interval [R_eq, R_ext] = [1/3, 2.0] is restored across the tested λ set {5, 10, 25, 50, 100, 200} under self-consistent Picard iteration at the D9 macro-field proxy-closure level. The Kretschmann-family curvature trigger is the best-supported trigger within the tested D8/D9 framework (D10), though it remains degenerate with the Weyl invariant in vacuum Schwarzschild. All results are conditional on the macro-field proxy closure used in D9, on the tested parameter ranges, and on the Schwarzschild background geometry. No claim of final unified field theory closure is made.

---

## 1. Classical Exhaustion and the Missing Component B Support

### 1.1 The locked deficit decomposition

The GRUT strong-field interior program, locked through Phase 6C, establishes that the metric function in the interior domain [R_eq, R_ext] = [1/3, 2.0] takes the form

    f(r) = −2(δ(r) − Σ(r))/r

where δ(r) = m(r) − r/2 is the mass deficit and Σ(r) is the integrated energy support. The minimum energy density required to restore metric positivity (f ≥ 0) decomposes as

    ε_min(r) = Component A · (1/r⁴) + Component B · (1/r²)

with the scalar-memory sector providing Component A at amplitude A² and Component B requiring a coefficient η² = 1/(8π) ≈ 0.03979.

### 1.2 Locked classical results

| Phase | Result | Status |
|---|---|---|
| Phase 6 | f(R_eq) = −17.71 (uncorrected metric) | LOCKED |
| Phase 6B | A_crit = 1.062 (critical scalar overshoot) | LOCKED |
| Phase 6C | ε_min = Component A + Component B | LOCKED |
| Route B | All CTP channels closed | LOCKED |
| Route C (Markov) | ε ~ 1/r⁴ only (insufficient) | LOCKED |
| Route C (non-Markov) | Source profile locking: 1/r⁴ for any kernel | LOCKED |
| Source-Law Program I | Partially viable, no GRUT-native mechanism | LOCKED |

### 1.3 The Component B gap

Route C demonstrated that Markov and non-Markov kernel structures produce only 1/r⁴ tails, regardless of kernel choice. Route B closed all Galley CTP channels. The Source-Law Program I identified defect/topological sources as the cleanest shape-compatible class for generating Component B, but found no GRUT-native mechanism. This gap motivated the D-phase program.

---

## 2. Defect-Sector Admissibility and Viability (D1–D2)

### 2.1 Topological admissibility (D1)

The criterion for monopole-type defects in three spatial dimensions is π₂(M) ≠ 0 for the vacuum manifold M. Among minimal field contents:

| Field | Vacuum manifold | π₂ | Monopole? |
|---|---|---|---|
| Real scalar | {±η} (discrete) | 0 | NO |
| Complex scalar | S¹ | 0 | NO |
| **O(3) triplet** | **S²** | **ℤ** | **YES** |

The O(3) triplet with Mexican-hat SSB, V(Φ⃗) = −(1/2)μ²|Φ⃗|² + (1/4)λ|Φ⃗|⁴, is the minimal admissible field content. The hedgehog ansatz Φₐ(r) = η f(r) x̂ₐ yields the ODE

    f″ + (2/r)f′ − (2/r²)f − λη²f(f² − 1) = 0

with f(0) = 0, f(∞) = 1. The asymptotic energy density is ε(r) → η²/r² as r → ∞, matching the Component B shape. The coefficient-matching condition is η² = 1/(8π).

**D1 Classification**: `provisional_candidate_extension_formulated`

### 2.2 Numerical BVP integration (D2)

The hedgehog BVP was solved via scipy.solve_bvp for six λ values {5, 10, 25, 50, 100, 200} at fixed η² = 1/(8π). All BVPs converge. The tail exponent approaches −2.0 monotonically as λ increases (−0.83 at λ = 5, −1.97 at λ = 200).

Two coupling modes were tested:
- **Case A** (additive, A = A_crit = 1.062): metric positive for ALL λ
- **Case B** (hybrid, A = 1.0): metric positive for λ ≥ 25

The defect provides 6–22% of total Σ at R_eq depending on λ.

**D2 Classification**: `defect_candidate_numerically_viable`

---

## 3. Embedding Route: Partial Recovery and Failure of Coefficient/Mechanism Closure (D3–D5)

### 3.1 Architecture and trigger narrowing (D3)

Four scalar-triplet relation architectures and five trigger mechanisms were assessed. Embedding (Φ = |Φ⃗|) with curvature-triggered SSB scored highest (0.8215) and passed all canon-preservation checks. Companion architecture ranked fourth (0.6807) but also passed canon preservation. Replacement and emergent architectures failed canon preservation.

**D3 Classification**: `scalar_triplet_embedding_most_promising`

### 3.2 Component A recovery test (D4)

The curvature-coupled embedded-triplet Lagrangian decomposes into four energy sectors: radial kinetic (∝ 1/r⁴), angular gradient (∝ 1/r²), potential (exponential), and curvature coupling (∝ 1/r³). The three-part Component A recovery test yielded:

| Test | Result | Detail |
|---|---|---|
| Shape | SUGGESTIVE | Fitted exponent −2.89 at default λ = 8π on finite domain [0.01, 5.0]; target is −4.0. The exponent trends toward −4.0 at higher λ (finite-domain BVP convergence effect), indicating the radial kinetic sector belongs to the correct power-law family but has not yet reached the asymptotic regime at the tested λ. This is not a clean pass: a 1.11-unit gap from the target remains at default parameters. |
| Coefficient | FAIL | Ratio ≈ 0.0035; the radial kinetic amplitude is 286× too weak to match the Component A energy budget. |
| Interpretation | DIFFERENT | The radial kinetic energy is topology-driven (hedgehog boundary conditions + self-interaction); the scalar-memory Component A is source-driven (τ dΦ/dt + Φ = X(r)). These are structurally different mechanisms. |

The radial kinetic sector suggests membership in the correct 1/r⁴ power-law family, but the coefficient is orders of magnitude below the Component A budget, and the driving mechanism is structurally different from the source-driven scalar-memory equation. All three tests must pass for full Component A recovery; only the shape test is suggestive, while coefficient and mechanism both fail. Component B is preserved (angular gradient retains η²/r²).

Among curvature trigger candidates, Kretschmann √K scored 0.85 (nonzero in vacuum), Ricci scalar R scored 0.50 (zero in vacuum Schwarzschild), and Ricci-squared scored 0.70.

**D4 Classification**: `component_a_shape_recovered_but_interpretation_not_yet_verified`

### 3.3 Source coupling insufficiency (D5)

Coupling the GRUT source X(r) = M/r² into the triplet ODE via the minimal quadratic interaction L_int = −(1/2)γX|Φ⃗|² was tested across nine γ values [0, 0.1, 0.5, 1, 2, 5, 10, 20, 50]. The EL-derived sign is negative for γ > 0, acting as an effective mass increase rather than a driving force. The peak coefficient ratio is 0.0049 at γ ≈ 5, still ∼200× too weak. The ratio decreases at high γ (counterproductive). Component B is preserved only for γ ≤ 2. No viable window exists.

**D5 Classification**: `source_coupling_insufficient`

### 3.4 Route summary

The embedding architecture is informative: it confirms the defect sector's 1/r⁴ shape in the radial kinetic channel and preserves Component B. However, it does not close the Component A amplitude or mechanism gap. The embedding route is not the winning closure route for the full two-component deficit.

---

## 4. Companion Architecture: Additive Viability and Fully Coupled Viability (D6–D7)

### 4.1 Dual-sector additive model (D6)

Rather than embedding the scalar as the radial mode of the triplet, D6 treats macro (scalar-memory, Component A) and defect (hedgehog, Component B) as independent additive sectors: T_total = T_macro + T_defect.

At A = 1.0 (the scientifically stronger baseline), metric positivity on [R_eq, R_ext] is restored for λ ≥ 25. At A = A_crit = 1.062, all tested λ values yield positive metrics on [R_eq, R_ext]. The defect provides 6–22% of total Σ at R_eq, with macro dominating at small r (∼279× at R_eq) and defect dominating at large r. The crossover radius is ∼1.67.

Four neglected cross-terms were inventoried: gravitational back-reaction (moderate), scalar-defect coupling (moderate), trigger self-consistency (minor), defect feedback on macro driver (significant).

**D6 Classification**: `companion_architecture_viable`

### 4.2 Cross-coupling stress test (D7)

D7 introduced two effective phenomenological response channels:

1. **Gravitational back-reaction** (α_BR): defect energy gravitates, increasing enclosed mass. DESTRUCTIVE.
2. **Source amplification** (β_XR): defect modifies effective gravitational source, amplifying macro amplitude via A_eff(r) = A₀ · m_eff(r)/M. CONSTRUCTIVE.

A 5×5 coupling-strength grid (25 configurations) was scanned. Key results at the unit benchmark (α_BR = 1, β_XR = 1):

- A_eff(R_eq) amplification: 3.36×
- Source amplification overwhelms gravitational penalty by ∼12.7×
- Net result: constructive
- D6 additive approximation was pessimistic

The viable λ window expanded from {25, 50, 100, 200} (D6) to all six scanned values {5, 10, 25, 50, 100, 200}. Of 25 grid configurations, 21 (84%) yield positive metrics; the 4 failures all have α_BR ≥ 0.75 with β_XR = 0.

Three leading approximations were explicitly flagged: defect-shape freezing (significant), effective phenomenological channels (moderate), and linear amplitude model (moderate).

**D7 Classification**: `fully_coupled_viable`

---

## 5. Action-Level Recovery and Portal Coupling Interpretation (D8)

### 5.1 Candidate coupled action

The minimal candidate action has four sectors plus one interaction:

    S_total = S_grav[g] + S_macro[Φ, g] + S_defect[Φ⃗, g] + S_trigger[K, Φ⃗] + S_portal[Φ, Φ⃗, g]

| Sector | Content | Free parameters |
|---|---|---|
| Gravitational | Einstein-Hilbert | G (inherited) |
| Macro scalar-memory | Real scalar Φ with source J_eff | A₀ (inherited) |
| Defect triplet | O(3) with Mexican-hat SSB | η, λ (inherited) |
| Curvature trigger | ξ√K|Φ⃗|² | ξ (inherited) |
| Portal interaction | g_p Φ²|Φ⃗|² | g_p (**1 new**) |

The portal term Φ²|Φ⃗|² is the unique non-derivative polynomial renormalizable (dimension ≤ 4) interaction between a real scalar and an O(3) triplet under the assumed Z₂ × O(3) symmetry. Total: 6 parameters (5 inherited, 1 new).

### 5.2 Channel recovery map

| D7 Channel | D8 Recovery | Quality | Source in action | Approximations |
|---|---|---|---|---|
| Gravitational penalty (α_BR) | **action_derived** | exact | S_grav + S_defect: Einstein equations | 0 |
| Source amplification (β_XR) | **derived_after_approximation** | structural | S_portal: g_p Φ²|Φ⃗|² | 3 (frozen profile, adiabatic envelope, linear identification) |

Recovery fraction: 0.75 (1 exact + 0.5 × 1 approximate, out of 2 channels).

### 5.3 Closure inventory

| Status | Count | Items |
|---|---|---|
| action_derived | 4/10 | Macro source driving, defect curvature triggering, defect hedgehog profile, gravitational penalty |
| effective_but_disciplined | 3/10 | Source amplification mechanism, linear amplitude model, defect-shape freezing |
| still_open | 3/10 | β_XR numerical value, nonlinear amplitude corrections, self-consistent coupled profile |

**D8 Classification**: `d7_channels_largely_action_derived`

---

## 6. Self-Consistent Back-Reaction and D9 Stability

### 6.1 Modified defect ODE

D9 relaxes the defect-shape freezing approximation from D7. The portal feedback enters the hedgehog ODE as an additional effective mass term:

    f″ + (2/r)f′ − (2/r²)f − λη²f(f² − 1) + g_portal · V_proxy(r) · f = 0

where V_proxy(r) = A_eff(r)² · RHO_EQ_COEFF / (η² · r⁴).

**Portal sign (from D8)**: POSITIVE (stabilizing). The portal acts as an additional effective mass, tightening the defect core by pushing f toward vacuum faster.

### 6.2 Macro-field proxy closure

**Critical caveat**: D9 uses a macro-amplitude proxy, not a full two-field Euler–Lagrange solution. The portal feedback uses A_eff(r) from the D7/D8 source-amplification model as a proxy for the macro field Φ²(r). This is a significant approximation. D9 tests self-consistency under a reduced closure, not the fully exact coupled system.

### 6.3 Self-consistent solution

Under-relaxed Picard iteration (ω = 0.5, with fallback to 0.3/0.2 on oscillation detection) converges at default parameters (g_portal = 1.0, λ = 8π):

| Quantity | Value |
|---|---|
| Converged | YES |
| Iterations | 13 |
| Final residual | 7.4 × 10⁻⁵ |
| Max profile deformation | 0.296 (29.6%) |
| Deformation classification | large |
| f_min (self-consistent) | +0.448 |
| f_min (D7 frozen) | +0.437 |
| Shift | +0.011 (constructive) |

### 6.4 Lambda scan under self-consistency

| λ | f_min (D7) | f_min (SC) | Shift | Max deformation | Iterations |
|---|---|---|---|---|---|
| 5 | +0.371 | +0.376 | +0.004 | 0.132 | 11 |
| 10 | +0.410 | +0.417 | +0.007 | 0.178 | 11 |
| 25 | +0.437 | +0.448 | +0.011 | 0.295 | 13 |
| 50 | +0.444 | +0.457 | +0.013 | 0.424 | 15 |
| 100 | +0.446 | +0.457 | +0.011 | 0.565 | 18 |
| 200 | +0.448 | +0.452 | +0.005 | 0.694 | 20 |

All six λ values remain positive. All shifts are constructive (positive). The viable window is unchanged from D7. Deformation increases with λ (up to 69% at λ = 200), but convergence is maintained.

### 6.5 Portal sensitivity

| g_portal | f_min | Positive | Max deformation |
|---|---|---|---|
| 0.00 | +0.437 | YES | 0.000 |
| 0.10 | +0.439 | YES | 0.117 |
| 0.50 | +0.444 | YES | 0.233 |
| 1.00 | +0.448 | YES | 0.296 |

Sensitivity is mild. At g_portal = 0, the D7 frozen result is exactly recovered (0 iterations, 0 deformation), confirming D9 as a strict generalization.

**D9 Classification**: `self_consistent_coupling_viable`

---

## 7. Trigger Selection and D10 Conclusion

### 7.1 Trigger candidate set

Four candidates, minimal and disciplined:

| Candidate | Value at R_eq (vacuum) | Value at R_ext | Contrast ratio | Nonzero in vacuum |
|---|---|---|---|---|
| Ricci scalar R | 0.0 | 0.0 | — | NO |
| Kretschmann √K | 93.53 | 0.433 | 216× | YES |
| Ricci-squared √(R_ab R^ab) | 0.0 | 0.0 | — | NO |
| Weyl √(C²) | 93.53 | 0.433 | 216× | YES |

### 7.2 Five-criterion scoring

| Criterion | Ricci R | Kretschmann √K | Ricci² √(R_ab R^ab) | Weyl √(C²) |
|---|---|---|---|---|
| Vacuum strong-field active | 0 | 1 | 0 | 1 |
| Strong-to-weak contrast > 100 | 0 | 1 | 0 | 1 |
| D8 action-natural | 1 | 1 | 0 | 1 |
| D9-compatible (stabilizing) | 0 | 1 | 0 | 1 |
| Prior-phase consistent | 1 | 1 | 1 | 1 |
| **Total** | **2** | **5** | **1** | **5** |

### 7.3 Vacuum Kretschmann/Weyl degeneracy

In Schwarzschild vacuum (R_ab = 0), the Riemann tensor equals the Weyl tensor, so K = C_abcd C^abcd exactly. The Kretschmann and Weyl invariants are numerically identical in the tested vacuum geometry. They are distinct invariants in general: in sourced regions, K = C² + 2R_ab R^ab − R²/3. Resolving which member of the tidal-curvature family is preferred requires sourced-interior analysis beyond the scope of D10.

### 7.4 Proxy-closure caveat on trigger selection

D9 used a macro-amplitude proxy closure, not the fully exact two-field Euler–Lagrange system. Trigger closure in D10 is:

- **Strong within the tested framework**: trigger selection is robust to the D8/D9 coupling structure. All assessment criteria produce clear, unambiguous results.
- **Still conditional on the current closure level**: a full two-field solution could in principle modify trigger coupling behavior in the sourced interior, potentially distinguishing Kretschmann from Weyl.

**D10 Classification**: `kretschmann_family_trigger_best_supported_within_tested_framework`

---

## 8. Phase Closure Statement

### 8.1 Phase outcome table (D1–D10)

The status column uses a six-level distinction reflecting the actual evidential weight of each phase result. Not all D-phase outcomes carry the same epistemic standing.

| Level | Meaning |
|---|---|
| LOCKED | Result is mathematically established or follows from standard theory; not subject to revision by later D-phases. |
| STRONGLY SUPPORTED | Result is numerically robust across tested parameter ranges but depends on identified approximations that have not yet been relaxed. |
| PROVISIONAL | Result is a working hypothesis or candidate that has not been falsified but also has not been independently confirmed or derived. |
| REJECTED IN TESTED FORM | The specific mechanism tested was found insufficient; the broader question may remain open under different assumptions. |
| PROXY-DEPENDENT | Result holds within the tested closure level (D9 macro-field proxy) and may change under a more exact treatment. |
| FRAMEWORK-CONDITIONAL | Result is valid within the D8/D9 tested framework but is conditional on that framework's approximations and scope. |

| Phase | Classification | Status | Type |
|---|---|---|---|
| D1 | `provisional_candidate_extension_formulated` | PROVISIONAL | Formulation |
| D2 | `defect_candidate_numerically_viable` | STRONGLY SUPPORTED | Numerical test |
| D3 | `scalar_triplet_embedding_most_promising` | LOCKED | Taxonomy (structural ranking) |
| D4 | `component_a_shape_recovered_but_interpretation_not_yet_verified` | PROVISIONAL | Analytical test (shape suggestive, coefficient/mechanism fail) |
| D5 | `source_coupling_insufficient` | REJECTED IN TESTED FORM | Negative result (quadratic coupling only) |
| D6 | `companion_architecture_viable` | STRONGLY SUPPORTED | Numerical test (additive approximation, cross-terms neglected) |
| D7 | `fully_coupled_viable` | STRONGLY SUPPORTED | Stress test (phenomenological channels, defect-shape frozen) |
| D8 | `d7_channels_largely_action_derived` | LOCKED | Derivational (structural, not numerical) |
| D9 | `self_consistent_coupling_viable` | PROXY-DEPENDENT | Self-consistency (macro-field proxy closure, not full two-field EL) |
| D10 | `kretschmann_family_trigger_best_supported_within_tested_framework` | FRAMEWORK-CONDITIONAL | Trigger closure (conditional on D8/D9 framework and vacuum geometry) |

**Reading guide**: LOCKED results (D3, D8) rest on structural/mathematical arguments that do not depend on numerical approximations. STRONGLY SUPPORTED results (D2, D6, D7) are numerically robust across tested ranges but carry identified approximations. PROVISIONAL results (D1, D4) are candidate formulations or partial recoveries not yet independently confirmed. REJECTED IN TESTED FORM (D5) means the specific tested mechanism failed but does not foreclose all alternatives. PROXY-DEPENDENT (D9) means the result holds under the D9 macro-field proxy but may shift under a more exact closure. FRAMEWORK-CONDITIONAL (D10) means the result is valid within the D8/D9 framework and vacuum Schwarzschild geometry but is conditional on both.

### 8.2 Architecture conclusion

The dual-sector Companion architecture is the leading surviving route in the tested framework:
- Macro scalar-memory sector → Component A (∝ 1/r⁴)
- Curvature-triggered O(3) hedgehog defect → Component B (∝ 1/r²)
- Portal interaction Φ²|Φ⃗|² → inter-sector coupling (1 new constant g_p)
- Kretschmann-family curvature trigger → SSB activation mechanism

The embedding route (D3–D5) was informative but is not the winning closure route: it preserves Component B and shows a suggestive 1/r⁴ power-law family membership in the radial kinetic sector, but fails both the coefficient test (286× too weak) and the mechanism test (topology-driven vs. source-driven) for Component A.

### 8.3 Formal phase-closure statement

The D-phase program (D1–D10) establishes that the O(3) topological defect sector, coupled to the classical GRUT scalar-memory sector through a dual-sector Companion architecture with portal interaction, restores metric positivity on the tested radial interval [R_eq, R_ext] = [1/3, 2.0] across the tested λ set {5, 10, 25, 50, 100, 200} under self-consistent Picard iteration at the D9 macro-field proxy-closure level. The gravitational back-reaction and source-amplification channels are largely action-derived from a minimal five-sector effective action with one genuinely new coupling constant. Kretschmann-family curvature triggering is the best-supported trigger within the tested D8/D9 framework, though it remains degenerate with the Weyl invariant in vacuum Schwarzschild. These results are proxy-dependent (D9 uses a macro-amplitude proxy, not the full two-field Euler–Lagrange system), framework-conditional (D10 trigger assessment is valid within the D8/D9 coupling structure and vacuum geometry), and bounded by the tested parameter ranges and approximation inventories documented in each phase. No claim of final unified field theory closure, trigger uniqueness, or metaphysical interpretation is made.

---

## 9. Explicit Open Caveats

### 9.1 Macro-field proxy closure (D9)

D9 uses A_eff(r) as a proxy for the macro field Φ²(r) in the portal feedback term. The fully exact two-field Euler–Lagrange system (simultaneously solving the macro Φ equation and the defect BVP) has not been computed. All D9 and D10 results are conditional on this reduced closure.

### 9.2 Portal coupling not predicted

The portal coupling g_p (and hence the effective β_XR) is introduced as a free parameter and scanned, not derived from matching conditions or renormalization constraints. Its numerical value is open.

### 9.3 Kretschmann/Weyl vacuum degeneracy

In the vacuum Schwarzschild geometry used throughout D1–D10, the Kretschmann and Weyl invariants are identical. D10 classifies the tidal-curvature family as best-supported but cannot distinguish between its members without sourced-interior analysis.

### 9.4 Lambda not predicted

The self-coupling λ controls the defect core width and the viable window threshold. It is scanned, not derived from GRUT parameters or matching conditions.

### 9.5 η identification

The coefficient-matching condition η² = 1/(8π) is a shape-and-normalization requirement. It has not been derived from a physical identification (e.g., with a gauge charge or fundamental constant).

### 9.6 Component A mechanism gap

The embedding route (D3–D5) showed that the radial kinetic sector of the embedded triplet has the correct 1/r⁴ shape but the wrong coefficient (286× too weak) and a different driving mechanism (topology-driven vs. source-driven). The Companion architecture treats Component A and Component B as originating from separate sectors. Whether a deeper unification of these two mechanisms exists is open.

### 9.7 Linear amplitude model

The source amplification channel uses A_eff(r) = A₀ · m_eff(r)/M (linear response). Higher-order and nonlinear corrections have not been computed.

### 9.8 Picard iteration uniqueness

D9's Picard iteration converges to one fixed point from the D7 frozen initial guess. Whether other initial conditions converge to the same or a different solution has not been tested.

### 9.9 High-λ convergence

At λ = 200, the D9 iteration takes 20 steps with 69% maximum deformation. Whether this trend saturates or eventually breaks convergence at higher λ is untested.

### 9.10 Background geometry

All phases use Schwarzschild geometry (M = 0.5, R_S = 1.0). Extension to non-Schwarzschild backgrounds (e.g., Reissner–Nordström, Kerr) is not addressed.

---

## Appendix A: Claims Audit Table

| # | Claim | Status | Evidence | Dependency | Caveat |
|---|---|---|---|---|---|
| 1 | O(3) triplet is minimal field admitting monopole defects | Locked result | π₂(S²) = ℤ (D1) | None | Standard topology result; no GRUT-specific content |
| 2 | Hedgehog tail ε → η²/r² matches Component B shape | Locked result | Asymptotic analysis + numerical verification (D1, D2) | η² = 1/(8π) | Coefficient-matching condition, not derived identification |
| 3 | BVP converges for all 6 tested λ values | Locked result | scipy.solve_bvp convergence (D2) | Finite domain [0.01, 5.0] | Domain truncation; max residual < 10⁻⁴ |
| 4 | Embedding architecture top-ranked | Locked result | Structural scoring 0.8215 (D3) | Scoring weights | Rankings are structural assessments, not proofs |
| 5 | Radial kinetic sector suggests 1/r⁴ power-law family membership | Provisional | Fitted exponent −2.89 at default λ; trends toward −4.0 at higher λ (D4) | Finite-λ BVP convergence; finite domain [0.01, 5.0] | 1.11-unit gap from target at default λ; coefficient 286× too weak; mechanism different. Shape is suggestive, not a clean recovery. |
| 6 | Source coupling insufficient for Component A recovery | Locked result | Peak ratio 0.0049 at γ = 5 (D5) | Quadratic coupling only | Other coupling forms not exhaustively tested |
| 7 | Companion architecture restores metric positivity on [R_eq, R_ext] at A = 1 for λ ≥ 25 | Strongly supported | f_min > 0 on [R_eq, R_ext] (D6) | Additive approximation; Schwarzschild background | Cross-terms neglected; 4 inventoried; tested λ range only |
| 8 | Cross-coupling is net constructive; source amplification dominates by ∼12.7× | Strongly supported | 5×5 grid scan (D7) | Defect-shape freezing; linear amplitude model | Phenomenological channels, not derived strengths |
| 9 | Viable λ window expands from {25–200} to {5–200} under coupling | Strongly supported | Lambda scan (D7) | Unit benchmark (1,1) | Coupling strengths scanned, not predicted |
| 10 | α_BR is action-derived (exact, from GR) | Locked result | Einstein equations: T_defect gravitates (D8) | None | GR-consistent; α_BR = 1 is unique value |
| 11 | β_XR is structurally derived from portal term after 3 approximations | Strongly supported | Portal EL derivation (D8) | Frozen profile, adiabatic envelope, linear identification | Recovery quality = structural, not exact |
| 12 | Portal term Φ²|Φ⃗|² is unique among non-derivative polynomial renormalizable Z₂ × O(3)-invariant scalar-triplet interactions | Locked result | Field-theory classification (D8) | Non-derivative, polynomial, dimension ≤ 4 assumptions | Derivative portals and higher-dimension operators excluded by assumption |
| 13 | D7 viability survives self-consistent iteration | Strongly supported | Picard convergence, all 6 λ positive (D9) | Macro-field proxy closure | Proxy uses A_eff, not full Φ(r) |
| 14 | Profile deformation is constructive (positive f_min shifts) | Strongly supported | All 6 λ shifts positive (D9) | g_portal = 1.0 default | Sensitivity mild but untested beyond g_portal = 1 |
| 15 | D9 is strict generalization of D7 | Locked result | D7 recovered exactly at g_portal = 0 (D9) | None | Mathematical identity |
| 16 | Kretschmann-family trigger scores 5/5; Ricci-family scores 1–2/5 | Locked result | Five-criterion assessment (D10) | Vacuum Schwarzschild geometry | Kretschmann/Weyl degenerate in vacuum |
| 17 | Tidal-curvature family is best-supported trigger | Strongly supported | 4-point separation in scoring (D10) | D8/D9 tested framework | Conditional on proxy closure level |
| 18 | Ricci scalar R = 0 in vacuum Schwarzschild | Locked result | Analytic (D4, D10) | None | Standard GR result |
| 19 | Kretschmann/Weyl degeneracy in vacuum | Locked result | K = C² when R_ab = 0 (D10) | Schwarzschild geometry | Distinct in sourced regions |
| 20 | Embedding route is not the winning closure route | Locked result | Coefficient fail (D4), source coupling insufficient (D5) | Within tested coupling forms | Other mechanisms not exhaustively tested |

---

## Appendix B: Theorem/Proposition-Style Results

**Proposition 1** (Topological admissibility). *Let M = S² be the vacuum manifold of an O(3) triplet with Mexican-hat SSB. Then π₂(M) = ℤ, and the hedgehog ansatz Φₐ = η f(r) x̂ₐ defines a topologically nontrivial configuration with winding number 1.*

**Proposition 2** (Asymptotic Component B matching). *For any solution of the hedgehog ODE with f(∞) = 1, the energy density satisfies ε(r) → η²/r² as r → ∞. The coefficient matches Component B if and only if η² = 1/(8π).*

**Proposition 3** (Gravitational penalty is action-derived). *In the D8 candidate action, the gravitational back-reaction channel (α_BR = 1) follows exactly from the Einstein field equations applied to the defect stress-energy. No new coupling constant is required. The value α_BR = 1 is the unique equivalence-principle-consistent value.*

**Proposition 4** (Portal uniqueness among non-derivative polynomial interactions at dimension 4). *Among non-derivative, polynomial, renormalizable (mass dimension ≤ 4) Lorentz-scalar interactions between a real scalar Φ and an O(3) triplet Φ⃗ that are invariant under Z₂ × O(3), the term g_p Φ²|Φ⃗|² is unique. It introduces exactly one new coupling constant g_p. Derivative interactions (e.g., (∂Φ)²|Φ⃗|²) and higher-dimension operators are excluded by the renormalizability and non-derivative assumptions.*

**Proposition 5** (D7 recovery). *At g_portal = 0, the D9 self-consistent iteration reduces to the D7 frozen-profile result in zero iterations with zero deformation. D9 is a strict generalization of D7.*

**Proposition 6** (Ricci trigger exclusion in vacuum). *In Schwarzschild vacuum geometry, R = 0 and R_ab = 0 identically. Any trigger of the form ξR|Φ⃗|² or ξ√(R_ab R^ab)|Φ⃗|² vanishes throughout the vacuum domain, providing no SSB activation and no effective mass contribution to the defect ODE.*

---

## Appendix C: Canonical Constants

| Symbol | Value | Definition |
|---|---|---|
| α_vac | 1/3 | Vacuum alpha parameter |
| R_S | 1.0 | Schwarzschild radius (geometric units) |
| M_ext | 0.5 | External mass parameter |
| R_eq | 1/3 | Equilibrium radius |
| R_ext | 2.0 | External boundary |
| τ | √(3/2) ≈ 1.2247 | Canonical processing timescale |
| A_crit | 1.062 | Critical scalar overshoot amplitude |
| η² | 1/(8π) ≈ 0.03979 | Component B coefficient / defect VEV² |
| η | 1/√(8π) ≈ 0.1995 | Defect VEV |
| λ_default | 8π ≈ 25.13 | Default self-coupling |
| RHO_EQ_COEFF | M²/(2τ²) | Macro energy density prefactor |
| MASS_COEFF | π/3 | Mass integral coefficient |
| f(R_eq) [Phase 6] | −17.71 | Uncorrected metric at equilibrium |

---

## Appendix D: Regression and Validation Summary

### D.1 Per-phase validation (D-phase modules only)

| Phase | Module | Benchmark | Pytest | Time |
|---|---|---|---|---|
| D1 | `grut/defect_admissibility.py` | 57/57 | 59/59 | 0.32s |
| D2 | `grut/numerical_monopole.py` | 58/58 | 58/58 | 0.89s |
| D3 | `grut/scalar_triplet_unification.py` | 57/57 | 57/57 | 0.22s |
| D4 | `grut/unification_dynamics.py` | 55/55 | 55/55 | 0.67s |
| D5 | `grut/source_coupled_defect.py` | 60/60 | 60/60 | 0.91s |
| D6 | `grut/companion_architecture.py` | 60/60 | 60/60 | 0.85s |
| D7 | `grut/cross_coupling_dynamics.py` | 60/60 | 60/60 | 0.82s |
| D8 | `grut/coupled_action_closure.py` | 60/60 | 60/60 | 0.33s |
| D9 | `grut/self_consistent_coupling.py` | 60/60 | 60/60 | 4.25s |
| D10 | `grut/trigger_selection.py` | 60/60 | 60/60 | 0.21s |

**D-phase pytest subtotal**: 587 tests across 10 modules, 587/587 passed.

**D-phase benchmark subtotal**: 587 checks across 10 scripts, 587/587 passed.

### D.2 Repository-wide regression

The repository contains additional test modules beyond the D-phase program (pre-D classical phases, API tests, infrastructure tests, etc.). The repository-wide regression result is:

**2834 passed, 3 skipped, 0 failed** (32 min 19s).

The 3 skipped tests are unrelated to the D-phase program. The D-phase modules contribute 587 of the 2834 passed tests. All D1–D10 tests pass with zero failures. No D-phase module introduces regressions in any pre-existing test.

### D.3 Numerical reproducibility

All benchmark scripts produce deterministic output. BVP solutions use scipy.integrate.solve_bvp with tolerance 10⁻⁶ and max_nodes = 5000. Grid resolution: 300 points. Picard convergence tolerance: 10⁻⁴. All floating-point comparisons use relative tolerance ≤ 0.15 (accounting for BVP finite-domain effects).

---

## Appendix E: Items Deferred to Omni-ToE v3

The following items are explicitly deferred and not addressed in D1–D10:

1. **Full two-field coupled BVP**: Replace the D9 macro-amplitude proxy with a simultaneously solved Φ(r) field equation.
2. **Portal coupling determination**: Derive g_p from matching conditions or renormalization constraints.
3. **Kretschmann vs. Weyl resolution**: Sourced-interior analysis to distinguish tidal-curvature family members.
4. **λ prediction**: Physical principle selecting the self-coupling constant.
5. **η identification**: Physical derivation of η² = 1/(8π) from fundamental parameters.
6. **Stability analysis**: Linear perturbation spectrum of the self-consistent hedgehog solution.
7. **Non-Schwarzschild backgrounds**: Extension to Kerr, Reissner–Nordström, or cosmological geometries.
8. **Nonlinear amplitude corrections**: Higher-order terms in the portal-modified macro EL equation.
9. **Picard uniqueness**: Alternative initial conditions and multi-solution landscape.
10. **High-λ convergence saturation**: Behavior of D9 iteration beyond λ = 200.
11. **Component A deep unification**: Whether the topology-driven and source-driven mechanisms for 1/r⁴ energy density can be unified.
12. **Particle-sector interpretation**: Physical identification of the O(3) triplet (if any) with known particles or gauge fields.

---

## Closing Statements

### A. Formal phase-closure statement

Phases D1–D10 establish that an O(3) topological defect extension, coupled to the locked GRUT scalar-memory sector through a dual-sector Companion architecture with Kretschmann-family curvature triggering and a minimal portal interaction Φ²|Φ⃗|², restores metric positivity on the tested radial interval [R_eq, R_ext] = [1/3, 2.0] across the tested λ set {5, 10, 25, 50, 100, 200} under self-consistent Picard iteration at the D9 macro-field proxy-closure level, with constructive profile deformation. The effective cross-coupling channels are largely action-derived from a five-sector effective action introducing one genuinely new coupling constant. The tidal-curvature trigger family is the best-supported trigger within the D8/D9 tested framework, though the Kretschmann/Weyl degeneracy in vacuum remains unresolved. These results are proxy-dependent (D9), framework-conditional (D10), and bounded by the tested parameter ranges and documented approximation inventories. No claim of final theory closure, trigger uniqueness, or metaphysical interpretation is made.

### B. Items deferred to Omni-ToE v3

The following remain open: (1) full two-field coupled BVP replacing the macro-amplitude proxy, (2) portal coupling g_p prediction from matching or renormalization conditions, (3) sourced-interior analysis resolving the Kretschmann/Weyl degeneracy, (4) physical derivation of λ and η, (5) linear stability analysis, (6) extension to non-Schwarzschild backgrounds, (7) nonlinear amplitude corrections and Picard uniqueness, (8) deeper unification of the Component A mechanism across the topology-driven and source-driven sectors, (9) particle-sector interpretation of the O(3) triplet, and (10) high-λ convergence saturation testing.

### C. Recommended filename

`GRUT_D1_D10_STRONG_FIELD_CLOSURE.md`
