# Phase D8 — Coupled Action Closure

This is a derivational and taxonomic assessment, not locked canon.

---

## A. Mission & Context

D7 locked as `fully_coupled_viable`. Two effective phenomenological channels (gravitational back-reaction alpha_BR, source amplification beta_XR) survive a 25-point coupling scan and expand the viable lambda window from [25, 50, 100, 200] to all 6 scanned values. However, these channels remain effective ansätze — structurally motivated proxies, not derived from a unified action.

D8 addresses this derivational gap: can the D7 cross-coupling structure be obtained from a single explicit effective action?

| Prior Phase | Status |
|-------------|--------|
| Phase 6: f(R_eq) | LOCKED (-17.71) |
| Phase 6B: A_crit | LOCKED (1.062) |
| Phase 6C: deficit | LOCKED (Component A + Component B) |
| Route C (all kernels) | LOCKED (insufficient) |
| Route B (all channels) | LOCKED (closed) |
| Source-Law Program I | LOCKED (partially viable, no GRUT-native) |
| Defect D1 | LOCKED (provisional candidate formulated) |
| Defect D2 | LOCKED (defect_candidate_numerically_viable) |
| Unification D3 | LOCKED (scalar_triplet_embedding_most_promising) |
| Unification D4 | LOCKED (component_a_shape_recovered_but_interpretation_not_yet_verified) |
| Source-Coupled D5 | LOCKED (source_coupling_insufficient) |
| Companion D6 | LOCKED (companion_architecture_viable) |
| Cross-Coupling D7 | LOCKED (fully_coupled_viable) |

**Goal**: Determine whether the D7 effective channels can be derived from one explicit effective action, or identify what remains as closure.

---

## B. Candidate Coupled Action

The minimal candidate action has four sectors plus one interaction term:

    S_total = S_grav[g] + S_macro[Phi, g] + S_defect[vec_Phi, g]
            + S_trigger[K, vec_Phi] + S_portal[Phi, vec_Phi, g]

| Sector | Field Content | Lagrangian | Symmetry |
|--------|---------------|------------|----------|
| Gravitational | g_{ab} | (1/16piG) sqrt(-g) R | Diffeomorphism |
| Macro scalar-memory | Phi (real scalar) | sqrt(-g) [-1/2 (nabla Phi)^2 - V_macro + J_eff Phi] | Z_2 broken by source |
| Defect triplet | vec_Phi^a (O(3)) | sqrt(-g) [-1/2 (D vec_Phi)^2 - lambda(|vec_Phi|^2 - eta^2)^2] | O(3) -> U(1) |
| Curvature trigger | K coupled to vec_Phi | sqrt(-g) [-xi K |vec_Phi|^2] | Scalar |
| Portal interaction | Phi^2 |vec_Phi|^2 | sqrt(-g) g_p Phi^2 |vec_Phi|^2 | Z_2 x O(3) |

**Free parameters**: 6 total (5 inherited: G, eta, lambda, xi, A_0; 1 new: g_p portal coupling).

**Minimality**: The portal term Phi^2 |vec_Phi|^2 is the unique minimal renormalizable interaction between a real scalar and an O(3) triplet. One new coupling constant is added.

---

## C. Interaction Term Candidates

Four interaction structures were assessed:

| # | Name | Formula | Target Channel | Selected |
|---|------|---------|----------------|----------|
| 1 | Stress-energy gravitational coupling | T^{defect}_{ab} in G_{ab} = 8piG T_{ab} | Gravitational penalty | YES (automatic in GR) |
| 2 | Scalar-triplet portal | g_p Phi^2 |vec_Phi|^2 | Source amplification | YES (1 new constant) |
| 3 | Derivative portal | g_d (nabla Phi)^2 |vec_Phi|^2 | Source amplification | NO (subleading) |
| 4 | Defect-source modulation | g_s J_eff |vec_Phi|^2 | Source amplification | NO (potential circularity) |

The minimal action uses terms 1 and 2 only. Term 1 is automatic in GR (no new coupling). Term 2 adds one new parameter g_p.

---

## D. Euler-Lagrange Equations

Three field equations derived structurally:

### Metric equation (g_{ab})

    G_{ab} = 8piG (T^{macro}_{ab} + T^{defect}_{ab} + T^{trigger}_{ab} + T^{portal}_{ab})

The defect stress-energy T^{defect}_{ab} enters the enclosed mass m(r) through the Einstein equations. This is the **gravitational penalty** — it requires no new interaction term.

### Macro scalar equation (Phi)

    Box Phi - V'_macro(Phi) + J_eff + 2 g_p Phi |vec_Phi|^2 = 0

The portal term produces a radius-dependent effective mass: m_Phi_eff^2(r) = m_Phi^2 + 2 g_p eta^2 h(r)^2. This modifies the source-driven amplitude, creating the **source amplification** pathway.

### Defect triplet equation (vec_Phi^a)

    D^2 vec_Phi^a - 4 lambda(|vec_Phi|^2 - eta^2) vec_Phi^a - 2 xi K vec_Phi^a + 2 g_p Phi^2 vec_Phi^a = 0

The portal backreaction on the defect (2 g_p Phi^2 vec_Phi) is subdominant to the trigger and symmetry-breaking terms. This justifies D7's defect-shape freezing approximation at leading order.

---

## E. D7 Channel Recovery Map

This is the key output of D8.

### Channel 1: Gravitational penalty (alpha_BR) — ACTION-DERIVED

| Property | Value |
|----------|-------|
| Recovery status | **action_derived** |
| Recovery quality | **exact** |
| Source in action | S_grav[g] + S_defect[vec_Phi, g] |
| Approximations required | None |

**Derivation path**: T_defect gravitates through the Einstein equations. The enclosed mass m(r) includes the integral of T^{defect}_{00}. The deficit delta_coupled = delta_static + Sigma_defect is exactly the D7 formula with alpha_BR = 1.

alpha_BR = 1 is the unique GR-consistent value. The D7 scan over alpha_BR < 1 tested equivalence-principle-violating scenarios.

### Channel 2: Source amplification (beta_XR) — DERIVED AFTER APPROXIMATION

| Property | Value |
|----------|-------|
| Recovery status | **derived_after_approximation** |
| Recovery quality | **structural** |
| Source in action | S_portal = g_p Phi^2 |vec_Phi|^2 |
| Approximations required | 3 (see below) |

**Derivation path**:
1. Portal term enters Phi EL as effective mass: m_Phi_eff^2(r) = m_Phi^2 + 2 g_p eta^2 h(r)^2
2. **Approximation 1** (frozen profile): h(r) from D2 BVP, not re-solved
3. **Approximation 2** (adiabatic envelope): macro amplitude adjusts slowly to local defect background
4. **Approximation 3** (linear identification): portal mass shift identified with enclosed-mass parametrization M + beta_XR * Sigma_defect

The portal term provides the structural mechanism. D7's linear form A_eff = A_0 * m_eff/M is an approximation of the full portal-modified dynamics.

### Recovery summary

| Channel | Parameter | Status | Quality | New Constants |
|---------|-----------|--------|---------|---------------|
| Gravitational penalty | alpha_BR | action_derived | exact | 0 |
| Source amplification | beta_XR | derived_after_approximation | structural | 1 (g_p) |

**Recovery fraction**: 0.75 (1 exact + 0.5 × 1 approximate out of 2 channels).

---

## F. Closure Inventory

| # | Item | Status | Source |
|---|------|--------|--------|
| 1 | Macro source driving | action_derived | S_macro: J_eff * Phi |
| 2 | Defect curvature triggering | action_derived | S_trigger: xi K |vec_Phi|^2 |
| 3 | Defect hedgehog profile | action_derived | S_defect: O(3) potential |
| 4 | Gravitational penalty channel | action_derived | S_grav + S_defect: Einstein eqs |
| 5 | Source amplification mechanism | effective_but_disciplined | S_portal + 3 approximations |
| 6 | Linear amplitude model | effective_but_disciplined | Linearization of portal EL |
| 7 | Defect-shape freezing | effective_but_disciplined | Portal backreaction neglected |
| 8 | Coupling constant beta_XR value | still_open | Requires full coupled solution |
| 9 | Nonlinear amplitude corrections | still_open | Higher-order portal terms |
| 10 | Self-consistent coupled profile | still_open | Full coupled BVP system |

**Summary**: 4/10 action-derived, 3/10 effective-but-disciplined, 3/10 still open.

The core structural elements (macro driving, defect profile, trigger, gravitational penalty) are all action-derived. The source amplification is structurally motivated but parametrically approximate. Three items remain open and would require a self-consistent coupled computation.

---

## G. Classification

**Classification**: `d7_channels_largely_action_derived`

This means:
- The gravitational penalty (alpha_BR) is exactly action-derived from GR
- The source amplification (beta_XR) is structurally derived from the portal interaction Phi^2 |vec_Phi|^2, after 3 identified approximations
- No D7 channel requires a purely effective closure term — both are traceable to the action
- The candidate action adds exactly 1 new coupling constant (g_p) beyond D6

### What this classification does NOT mean:
- It does NOT prove final field-theory closure
- It does NOT derive the numerical value of beta_XR from first principles
- It does NOT validate the defect-shape freezing approximation
- It does NOT prove the linear amplitude model is exact
- The candidate action is minimal, not unique
- The portal coupling g_p is introduced, not predicted
- Classification is within the D8 derivational framework only

### Phase lock update

| Phase | Status |
|-------|--------|
| Phase 6: f(R_eq) | LOCKED (-17.71) |
| Phase 6B: A_crit | LOCKED (1.062) |
| Phase 6C: deficit | LOCKED (Component A + Component B) |
| Route C (all kernels) | LOCKED (insufficient) |
| Route B (all channels) | LOCKED (closed) |
| Source-Law Program I | LOCKED (partially viable, no GRUT-native) |
| Defect D1 | LOCKED (provisional candidate formulated) |
| Defect D2 | LOCKED (defect_candidate_numerically_viable) |
| Unification D3 | LOCKED (scalar_triplet_embedding_most_promising) |
| Unification D4 | LOCKED (component_a_shape_recovered_but_interpretation_not_yet_verified) |
| Source-Coupled D5 | LOCKED (source_coupling_insufficient) |
| Companion D6 | LOCKED (companion_architecture_viable) |
| Cross-Coupling D7 | LOCKED (fully_coupled_viable) |
| **Coupled Action D8** | **ASSESSED (d7_channels_largely_action_derived)** |

---

## H. Numerical Validation Summary

- Benchmark: **60/60 checks PASSED**
- Pytest: **60/60 tests PASSED** (0.33s)
- Regression: **295/295 tests PASSED** (D4+D5+D6+D7+D8, 2.47s)
- 4 sectors defined
- 4 interaction candidates assessed
- 3 Euler-Lagrange equations derived
- 2 D7 channels mapped
- 10 closure inventory items classified
- 0 channels require purely effective closure

---

## I. Nonclaims (10)

1. This phase does NOT prove final field-theory closure.
2. A partial derivation is acceptable and is reported honestly.
3. Any remaining effective closure terms are clearly labeled.
4. This phase does NOT invalidate D7 if some channels remain effective.
5. The candidate action is a minimal effective action, not a claim of the unique or final theory.
6. Euler-Lagrange equations are derived structurally, not solved.
7. The interaction term set is minimal and disciplined, not exhaustive.
8. The recovery map does not claim uniqueness of the derivation path.
9. This phase does NOT derive coupling constants from first principles — it derives structural forms only.
10. Classification is within the D8 derivational framework only.

---

## J. Assumptions (10)

1. The candidate action is S = S_grav + S_macro + S_defect + S_trigger + S_int, with each sector clearly identified.
2. S_grav is the standard Einstein-Hilbert gravitational action.
3. S_macro represents the GRUT scalar-memory sector with source-driven amplitude.
4. S_defect represents the O(3) triplet hedgehog sector from D1-D4.
5. S_trigger represents curvature-triggered activation from D3-D4 (Kretschner threshold).
6. S_int is minimal: only structurally motivated terms from D6 cross-term inventory.
7. EL derivation is structural: equations represented as term inventories.
8. Channel recovery maps D7 parameters to action origins or closure assumptions.
9. Defect-shape freezing from D7 is inherited and tracked as required approximation.
10. Classification is conservative: 'action_derived' only if obtainable without phenomenological input.

---

## K. Recommended Next Move

D8 establishes that the D7 structure is largely action-derived. Three derivational gaps remain open:

1. **Self-consistent coupled BVP** (Gap #2 from D8 preamble): Relax defect-shape freezing by solving the hedgehog BVP on the portal-modified background simultaneously with the macro and metric equations.

2. **Portal coupling determination**: Obtain g_p (and hence beta_XR) from matching conditions, renormalization constraints, or phenomenological input rather than scanning.

3. **Nonlinear amplitude corrections**: Compute higher-order terms in the portal-modified macro EL to test whether D7's linear A_eff model is quantitatively reliable.

4. **Trigger uniqueness** (Gap #3): The Kretschner trigger is top-ranked but not yet uniquely derived. A future phase could test whether it emerges from consistency conditions rather than selection.
