# Route C Non-Markov Kernel Test — Spectral Kernels vs Missing 1/r^2

## Status

**NONMARKOV ROUTE C INSUFFICIENT FOR COMPONENT B**

Classification: **nonmarkov_route_c_insufficient_for_component_b**

This phase closes the non-Markov kernel loophole (Loophole 1 from
route_c_deficit.py, rated high severity) within the tested spectral-representable
kernel framework.  The 1/r^4 spatial scaling of the kinetic energy density is
locked by the source profile X = M/r^2, not by the kernel.  Spectral richness
changes the temporal envelope but cannot redistribute support radially from
1/r^4 toward 1/r^2.  No tested non-Markov kernel class produces the missing
Component B support.

---

## A. Mission and Context

Phase 6C (FROZEN) identified the minimal additive source for metric closure:

    epsilon_min(r) = |rho_eq(r)| + 1/(8*pi*r^2)

with two components:
- **Component A ~ 1/r^4**: cancels the equilibrium negative density rho_eq
- **Component B ~ 1/r^2**: intermediate-radius geometric support

The Route C deficit assessment classified the Markov-reduced exponential kernel
as `route_c_insufficient_within_markov_reduction` — it produces only 1/r^4
support.  Five loopholes were documented.  **Loophole 1** (non-exponential
kernel, high severity) was the most fundamental: non-Markov kernels break the
Markov property, and T^Phi_history could potentially generate different radial
structure.

**This module asks:** Can non-Markov kernels — multi-pole, power-law, or any
kernel with a spectral representation — generate 1/r^2 support?

**The answer:** No.  The spatial scaling is locked at 1/r^4 by the source
profile X = M/r^2, not by the kernel.

---

## B. Markov Reduction — What It Discards

The Markov-reduced exponential kernel K(s) = (1/tau) exp(-s/tau) has the unique
property that the nonlocal retarded integral reduces to a first-order ODE:

    tau dPhi/dt + Phi = X(t)

This absorbs all history into the current field value Phi.  Non-Markov kernels
discard this reduction, retaining:

| Property | Markov (exponential) | Non-Markov |
|:---|:---|:---|
| T^Phi_history | = 0 (absorbed) | != 0 (genuinely nonlocal in time) |
| Relaxation timescales | Single (tau) | Multiple or continuous |
| Spectral density | Single pole at 1/tau | Multi-pole or continuous rho(w) |
| Temporal decay | Pure exponential | Stretched, power-law, or multi-exponential |
| Spatial profile of Phi | M/r^2 | **Still M/r^2** |

The last row is the key: the spatial profile is determined by the source, not
the kernel.

---

## C. Kernel Classes Tested

| # | Kernel | Formula | Spectral Rep. |
|:---|:---|:---|:---|
| 1 | Single exponential | K(s) = (1/tau) exp(-s/tau) | Yes (single pole) |
| 2 | Two-pole | K(s) = w1/tau1 exp(-s/tau1) + w2/tau2 exp(-s/tau2) | Yes (two poles) |
| 3 | Power-law | K(s) ~ s^{-alpha}, alpha=0.5 (spectral approximation) | Yes (continuous) |
| 4 | Generic spectral | K(s) = integral dw rho(w) exp(-w*s) | Yes (by definition) |

Parameters for testing:
- Two-pole: tau_1 = 1.2247, tau_2 = 3.6742, weights (0.6, 0.4)
- Power-law: alpha = 0.5, 20-term spectral sum approximation

---

## D. Source Profile Locking Theorem — THE KEY RESULT

**Theorem:** For any kernel K(s) with spectral/Laplace representation
K(s) = integral dw rho(w) exp(-w*s), if the source X(t,r) = A(t) * M/r^2 is
separable in time and radius, then the kinetic energy density scales as 1/r^4
at ALL time slices.

**Proof:**

1. The source X(t,r) = A(t) * M/r^2 is separable: X = A(t) * g(r) where
   g(r) = M/r^2.

2. Each spectral component Phi_w satisfies (1/w) dPhi_w/dt + Phi_w = X(t,r).
   Since the ODE is linear and X is separable, the solution is:
   Phi_w(t,r) = h_w(t) * M/r^2 (separable).

3. Therefore dPhi_w/dt = dh_w/dt * M/r^2.

4. The effective time derivative is:
   dPhi_eff/dt = integral dw rho(w) dh_w/dt * M/r^2 = F(t) * M/r^2
   where F(t) = integral dw rho(w) dh_w/dt is a pure function of time.

5. The kinetic energy density is:
   epsilon = (1/2)(F(t) * M/r^2)^2 = (1/2) F(t)^2 * M^2/r^4.

6. The spatial scaling is 1/r^4, independent of the kernel K(s).

**What spectral richness changes:** F(t), the temporal envelope (peak time,
width, decay shape, effective amplitude).

**What spectral richness cannot change:** M/r^2, the spatial profile.

---

## E. Per-Kernel Support Profiles

| Kernel | Spatial Exponent | Temporal Differs | Matches Component B |
|:---|:---|:---|:---|
| Single exponential | -4.0 (exact) | No (baseline) | No |
| Two-pole | -4.0 (to 1e-14) | Yes | No |
| Power-law | -4.0 (to 1e-14) | Yes | No |
| Generic spectral | -4.0 (structural) | — | No |

The exponent standard deviation across all time slices is < 1e-14 for all
numerical kernels.  The spatial scaling is perfectly stable.

---

## F. Spectral Richness — What It Can and Cannot Change

| Property | Can Change? | Mechanism |
|:---|:---|:---|
| Temporal profile F(t) | **Yes** | Different spectral weights change the envelope |
| Peak amplitude | **Yes** | Different effective A_crit equivalent |
| Peak timing | **Yes** | Slow modes shift the peak later |
| Spatial scaling | **No** | Locked by X = M/r^2 |
| Radial redistribution | **No** | Cannot broaden from 1/r^4 toward 1/r^2 |
| History stress T^K_history | **Exists** | But carries same 1/r^4 spatial dependence |

---

## G. Component B Compatibility

| Kernel | Spatial Exponent | Target (Component B) | Gap |
|:---|:---|:---|:---|
| Single exponential | -4.0 | -2.0 | 2.0 |
| Two-pole | -4.0 | -2.0 | 2.0 |
| Power-law | -4.0 | -2.0 | 2.0 |
| Generic spectral | -4.0 | -2.0 | 2.0 |

No kernel class produces 1/r^2 support.  The gap of 2.0 in the exponent is
structural, not a numerical artifact.

---

## H. Localizability Assessment

| Property | Value |
|:---|:---|
| Nonlocal in time | Yes (for non-Markov kernels) |
| Local in space | Yes (field profile ~ M/r^2 at every instant) |
| Energy density localizable | Yes (epsilon ~ M^2/r^4 at every instant) |
| History term T^K_history | Formal, nonlocal in time, but 1/r^4 in space |

The nonlocality is temporal (memory of past states), not spatial.  The energy
density has a well-defined local spatial profile at every instant.

---

## I. Physical Promotability

No kernel can be promoted to physical 1/r^2 support.

**Obstruction:** Source profile locking — the 1/r^4 scaling is a structural
consequence of X = M/r^2, not of the kernel choice.

**Remaining loophole:** Modified source law X != M/r^2.  If X ~ M/r instead
of M/r^2, then Phi_dot ~ 1/r and epsilon ~ 1/r^2.  This could arise from
curvature-scalar coupling (R*Phi), modified interior metric, or non-standard
sourcing.  This is a SOURCE question, not a KERNEL question (Loophole 5 from
route_c_deficit.py).

---

## J. Final Classification & Phase Lock Update

Classification: **nonmarkov_route_c_insufficient_for_component_b**

    Phase 6 (Static Interior):              LOCKED (f(R_eq) = -17.71)
    Phase 6B (Dynamical Interior):          LOCKED (A_crit = 1.062, global_robust)
    Phase 6C (Metric Deficit):              LOCKED (epsilon_min two-component)
    Route C Deficit Assessment:             LOCKED (route_c_insufficient_within_markov_reduction)
    Route B Component B Test:               LOCKED (route_b_post_projection_insufficient__preprojection_unresolved)
    Route B g_- Energy Density:             LOCKED (gminus_diagonal_quadratic_energy_absent__mixed_channel_unresolved)
    Route B Mixed Channel:                  LOCKED (mixed_channel_insufficient_within_tested_galley_framework)
    Route C Non-Markov Kernel Test:         LOCKED (nonmarkov_route_c_insufficient_for_component_b)

    source_profile_locking_proven: TRUE
    all_tested_kernel_classes_insufficient: TRUE
    framework_scope: spectral_representable_kernels_with_standard_source
    loophole_1_status: CLOSED (within tested framework)
    remaining_classical_loophole: modified_source_law (Loophole 5)

---

## K. Numerical Validation

| Quantity | Value |
|:---|:---|
| Markov baseline epsilon_RC_coeff | 0.09399 |
| Markov baseline exponent | -4.0 (exact) |
| Markov matches locked result | True |
| Single exponential spatial exponent | -4.0 (to 1e-14) |
| Two-pole spatial exponent | -4.0 (to 1e-14) |
| Power-law spatial exponent | -4.0 (to 1e-14) |
| Max deviation from -4.0 | ~ 1.7e-14 |
| Exponent std across time (two-pole) | ~ 2.1e-15 |
| Exponent std across time (power-law) | ~ 2.0e-15 |
| Component B target exponent | -2.0 |
| Gap to target | 2.0 |
| Any matches Component B | False |
| Source profile locking proven | True |
| Can change spatial scaling | False |
| Can change temporal profile | True |
| Any kernel promotable | False |

Benchmark: 57/57 ALL CHECKS PASSED.
Pytest: 57/57 ALL TESTS PASSED in 0.64s.

---

## L. Nonclaims (10)

1. This phase does NOT prove Route C physically incorrect in full generality.
   It closes the non-Markov kernel loophole within the tested
   spectral-representable kernel framework.

2. A broader temporal response is not automatically a broader spatial response.
   The spatial profile is locked by the source, not the kernel.

3. The source-profile locking result assumes X = M/r^2.  Modified source laws
   (Loophole 5 from route_c_deficit.py) are outside scope.

4. Non-spectral-representable kernels (if they exist for causal retarded
   systems) are not tested.  All standard physical kernels have spectral
   representations.

5. Self-consistent back-reaction (where the kernel modifies the metric which
   modifies the source) is not included.  This would require a full nonlinear
   coupled evolution.

6. The history stress-energy T^K_history for non-Markov kernels is classified
   as carrying 1/r^4 spatial dependence, but its full covariant form has not
   been computed in closed form.

7. The power-law kernel is approximated via spectral sum.  The exact
   Mittag-Leffler function is used structurally but the numerical verification
   uses the spectral approximation.

8. The temporal profile analysis (what spectral richness CAN change) is
   illustrative, not exhaustive.  Other temporal effects exist but are not
   relevant to the spatial shape question.

9. The remaining loophole (modified source law) is a source question, not a
   kernel question.  It is outside the scope of this kernel test.

10. Failure for the tested kernel classes closes only the tested non-Markov
    Route C families within the standard-source framework, not every
    conceivable nonlocal theory.

---

## M. Assumptions (10)

1. The Route C kernel K(s) has a spectral/Laplace representation:
   K(s) = integral dw rho(w) exp(-w*s).  This includes all completely monotone
   kernels, sums of exponentials, and power-law kernels.

2. The gravitational source has the standard profile X(t,r) = A(t) * M/r^2
   (from the equilibrium mass profile).

3. Each spectral component w drives an independent auxiliary field via linear
   response: (1/w) dPhi_w/dt + Phi_w = X(t,r).

4. The effective field is the spectral integral:
   Phi_eff = integral dw rho(w) Phi_w.

5. The effective kinetic energy density is epsilon = (1/2)(dPhi_eff/dt)^2
   (standard minimally-coupled form).

6. The deficit target is Component B: 1/(8*pi*r^2) — an independent 1/r^2
   geometric support term (from Phase 6C).

7. The Markov baseline is the locked result from route_c_deficit.py:
   epsilon_RC = EPSILON_RC_COEFF / r^4 with the exponential kernel.

8. The two-pole kernel tested uses tau_1 = TAU_CANONICAL, tau_2 = 3*TAU_CANONICAL
   with spectral weights (0.6, 0.4).

9. The power-law kernel K(s) ~ s^{-alpha} is approximated by its spectral
   representation with alpha = 0.5 (half-order fractional memory).

10. The background metric and source profile are held fixed (no self-consistent
    back-reaction from the kernel change).

---

## N. Recommended Next Move

The non-Markov kernel loophole (Loophole 1) is now closed within the tested
spectral-representable kernel framework with standard source X = M/r^2.

The only remaining classical loophole for Route C is **Loophole 5: modified
source law**.  If X had a different radial profile (e.g. X ~ M/r instead of
M/r^2), then Phi_dot ~ 1/r and epsilon ~ 1/r^2, which would match Component B.

This is a SOURCE question, not a KERNEL question.  It could arise from:
- Curvature-scalar coupling (R*Phi terms)
- Modified interior metric ansatz
- Non-standard gravitational sourcing

Whether to pursue this avenue or accept the deficit as structural is a
framework-level decision that depends on the physical content of the GRUT
theory beyond the currently tested modules.
