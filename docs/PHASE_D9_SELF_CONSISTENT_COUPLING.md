# Phase D9 — Self-Consistent Coupled Profile Integration

This is an analytical assessment phase, not locked canon.

---

## A. Mission & Context

D7 locked as `fully_coupled_viable` with the defect profile frozen on Schwarzschild. D8 derived the coupled action (`d7_channels_largely_action_derived`), identifying the portal term `g_p Phi^2 |vec_Phi|^2` as the structural source of the beta_XR channel.

D9 relaxes the defect-shape freezing approximation by iterating the coupled system toward self-consistency under a reduced closure. The primary question: does D7 viability survive when the defect profile is allowed to deform?

**Critical scope limitation**: D9 uses a **macro-amplitude proxy** for the portal feedback — the effective amplitude A_eff(r) from the D7/D8 Component A profile, not a separately solved macro field variable Phi(r). D9 tests self-consistency under a field-amplitude proxy closure, NOT the fully exact two-field Euler–Lagrange system.

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
| Coupled Action D8 | LOCKED (d7_channels_largely_action_derived) |

---

## B. Modified Defect ODE and Portal Sign

### Standard D2 hedgehog equation (frozen):
    f'' + (2/r)f' - (2/r^2)f - lambda*eta^2*f*(f^2 - 1) = 0

### Self-consistent modification (from D8 portal term, macro-amplitude proxy):
    f'' + (2/r)f' - (2/r^2)f - lambda*eta^2*f*(f^2 - 1) + g_portal * V_proxy(r) * f = 0

where:
    V_proxy(r) = A_eff(r)^2 * RHO_EQ_COEFF / (eta^2 * r^4)

**Sign (from D8)**: The D8 portal term `g_p Phi^2 |vec_Phi|^2` enters the defect EL equation as `+2 g_p Phi_bg^2 f`. The sign is **POSITIVE (stabilizing)**: the portal acts as an additional effective mass for the defect, pushing f(r) toward vacuum (f→1) faster. This tightens the defect core.

**Normalization**: V_proxy absorbs the factor 2*g_p and uses the macro-amplitude proxy A_eff(r)^2 for Phi_bg^2. The parameter `g_portal` controls the overall portal feedback strength.

---

## C. Macro-Field Proxy Closure

The portal feedback uses an inferred macro amplitude from the D7/D8 effective Component A profile rather than a separately solved macro field variable. Specifically:

- **What D9 uses**: V_proxy(r) = A_eff(r)^2 * RHO_EQ_COEFF / (eta^2 * r^4), where A_eff comes from the D7 source-amplification model
- **What the exact system would require**: solving a separate Phi field equation simultaneously with the defect BVP
- **Gap**: The proxy assumes the macro amplitude responds to the defect as in D7, rather than being self-consistently determined

This is an additional approximation beyond D7/D8. D9 reports results under this proxy closure explicitly.

---

## D. Under-Relaxed Picard Iteration

The self-consistent solver uses under-relaxed Picard iteration:

    f_next = (1 - omega) * f_old + omega * f_new,  0 < omega <= 1

Default omega = 0.5, with automatic fallback to 0.3 or 0.2 if oscillation is detected (residual increasing for 3 consecutive steps). This prevents false convergence failure from Picard stiffness.

Convergence criterion: ||f_next - f_old||_inf < 1e-4.

---

## E. Self-Consistent Solution at Default Parameters

At g_portal=1.0, lambda=8*pi, alpha_BR=1, beta_XR=1:

| Quantity | Value |
|----------|-------|
| Converged | YES |
| Iterations | 13 |
| Final residual | 7.4e-05 |
| Relaxation used | 0.5 |

---

## F. Profile Deformation

| Quantity | Value |
|----------|-------|
| Max |delta_f| | 0.296 |
| RMS delta_f | ~0.12 |
| Crossover shift | -0.089 |
| Core f' change | nonzero |
| Sigma_defect shift | measurable |
| Deformation classification | **large** |

The portal feedback produces significant profile deformation: the defect core tightens (f approaches vacuum faster), consistent with the stabilizing portal sign. The maximum shift of ~30% occurs in the transition region where the hedgehog profile goes from 0 to 1.

Despite this large deformation, the metric viability is preserved (see below).

---

## G. Metric Reinjection

| Quantity | Self-Consistent | D7 Frozen | Shift |
|----------|----------------|-----------|-------|
| f_min | +0.448 | +0.437 | +0.011 |
| Metric positive | YES | YES | — |

The self-consistent profile actually produces a **slightly better** metric than the D7 frozen profile. The portal-induced core tightening increases Sigma_defect slightly, which adds to the Sigma budget. The shift is small (+0.011) but consistently positive.

---

## H. Lambda Scan

| lambda | f_min (D7) | f_min (SC) | Shift | Max Deformation | Iterations |
|--------|-----------|-----------|-------|-----------------|------------|
| 5 | +0.371 | +0.376 | +0.004 | 0.132 | 11 |
| 10 | +0.410 | +0.417 | +0.007 | 0.178 | 11 |
| 25 | +0.437 | +0.448 | +0.011 | 0.295 | 13 |
| 50 | +0.444 | +0.457 | +0.013 | 0.424 | 15 |
| 100 | +0.446 | +0.457 | +0.011 | 0.565 | 18 |
| 200 | +0.448 | +0.452 | +0.005 | 0.694 | 20 |

**Key findings**:

1. **Viable window unchanged**: All 6 lambda values remain positive under self-consistency. Same window as D7.
2. **Self-consistency is constructive**: All shifts are positive — the self-consistent profile gives slightly better metrics.
3. **Deformation increases with lambda**: At lambda=200, max deformation reaches 69%. The portal tightens the core more when lambda is larger (stronger symmetry-breaking potential amplifies the portal effect).
4. **Convergence slows at high lambda**: 11 iterations at lambda=5 vs 20 at lambda=200. The feedback strengthens with lambda.
5. **All BVPs converge**: 6/6 converged at all lambda values.

---

## I. Portal Strength Sensitivity

| g_portal | f_min | Positive | Max Deformation | Iterations |
|----------|-------|----------|-----------------|------------|
| 0.00 | +0.437 | YES | 0.000 | 0 |
| 0.10 | +0.439 | YES | 0.117 | 11 |
| 0.50 | +0.444 | YES | 0.233 | 12 |
| 1.00 | +0.448 | YES | 0.296 | 13 |

**Sensitivity**: mild. All g_portal values produce positive metrics. The metric improves monotonically with g_portal. At g_portal=0: D7 frozen result recovered exactly (0 iterations, 0 deformation).

---

## J. D7 Recovery

At g_portal=0, the D7 frozen result is recovered exactly:
- 0 iterations
- 0 deformation
- f_min = +0.437 (matching D7)

This confirms that D9 is a strict generalization of D7: the frozen-profile approximation is the g_portal=0 limit.

---

## K. Classification

**Classification**: `self_consistent_coupling_viable`

This means:
- D7 viability is preserved under self-consistency
- The viable lambda window is unchanged (all 6 values)
- Profile deformation is large but constructive
- Self-consistency slightly improves the metric (positive shifts)
- The macro-field proxy closure was used (explicitly flagged)

### What this classification does NOT mean:
- It does NOT prove final theory closure
- The macro-field proxy closure is a significant approximation
- The fully exact two-field EL system is not solved
- Portal coupling g_portal is scanned, not predicted
- Convergence does not guarantee uniqueness
- Profile deformation diagnostics are relative to the frozen baseline
- Classification is within the D9 numerical framework only

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
| Coupled Action D8 | LOCKED (d7_channels_largely_action_derived) |
| **Self-Consistent D9** | **ASSESSED (self_consistent_coupling_viable)** |

---

## L. Approximation Inventory

| # | Approximation | Source | Severity |
|---|---------------|--------|----------|
| 1 | Macro-field proxy closure | D9 | significant — uses A_eff(r) as proxy for Phi^2 |
| 2 | Under-relaxed Picard iteration | D9 | moderate — numerical technique |
| 3 | Portal sign/normalization from D8 | D8→D9 | inherited — stabilizing (positive) |
| 4 | Frozen profile as initial guess | D7→D9 | removed by iteration |
| 5 | Defect-shape freezing | D7 | **relaxed in D9** (the main upgrade) |

---

## M. Numerical Validation Summary

- Benchmark: **60/60 checks PASSED**
- Pytest: **60/60 tests PASSED** (4.25s)
- Regression: **355/355 tests PASSED** (D4–D9, 5.51s)
- Self-consistent iteration converges in 11–20 iterations
- All 6 lambda BVPs converge
- All 4 portal strength values give positive metric
- D7 recovery verified at g_portal=0
- Proxy closure explicitly flagged throughout

---

## N. Nonclaims (10)

1. This phase does NOT prove final theory closure.
2. A surviving self-consistent solution strongly upgrades confidence but remains within the tested framework.
3. A failure would downgrade D7 from structural viability to stress-test viability, not erase its value.
4. The macro-field proxy closure is a significant approximation. The fully exact two-field solution is not computed.
5. Portal coupling g_portal is scanned, not predicted from first principles.
6. Under-relaxation is a numerical technique, not physical content.
7. Convergence of the Picard iteration does not guarantee uniqueness.
8. Profile deformation diagnostics are relative to the frozen baseline.
9. This phase does NOT justify metaphysical or observer-based interpretation.
10. Classification is within the D9 numerical framework only.

---

## O. Recommended Next Move

D9 establishes that the companion architecture survives self-consistent profile iteration under the proxy closure. Remaining gaps:

1. **Full two-field coupled BVP**: Replace the macro-amplitude proxy with a separately solved Phi(r) field equation. This is the next significant upgrade toward the exact coupled system.

2. **Portal coupling determination**: Derive g_portal from matching conditions or renormalization constraints.

3. **High-lambda convergence**: At lambda=200, the iteration takes 20 steps and deformation reaches 69%. Test whether this trend continues or saturates at higher lambda.

4. **Uniqueness test**: The Picard iteration finds one fixed point. Test whether other initial guesses converge to the same solution.
