# Route B Mixed g_+ * g_- Cross-Coupling Channel — Final Classical Pass

## Status

**MIXED CHANNEL INSUFFICIENT WITHIN TESTED GALLEY FRAMEWORK**

Classification: **mixed_channel_insufficient_within_tested_galley_framework**

This phase closes the final tested classical Route B residue within the
perturbative Galley CTP framework.  The mixed g_+ * g_- cross-coupling
channel is insufficient for Component B: the four pathologies (ghost-sourced,
IC-dependent, CTP-killed, projection-killed) jointly render it non-promotable
to a clean physical geometric support mechanism.  All tested classical Route B
channels are now classified.

---

## A. Mission and Context

Phase 6C (FROZEN) identified the minimal additive source for metric closure:

    epsilon_min(r) = |rho_eq(r)| + 1/(8*pi*r^2)

with two components:
- **Component A ~ 1/r^4**: cancels the equilibrium negative density rho_eq
- **Component B ~ 1/r^2**: intermediate-radius geometric support

The classical frontier was narrowed step by step:

| Phase | Result |
|:---|:---|
| Route C | Insufficient within Markov reduction (pure 1/r^4, wrong shape) |
| Route B post-projection | Insufficient (same standard scalar T^Phi as Route C) |
| Route B Phi_- sector | Pathological (ghost, IC-dependent, CTP-killed) |
| Route B S_diss | Vanishes in physical limit |
| Route B g_- diagonal | Absent (CTP antisymmetry kills quadratic action) |
| **Route B g_- mixed** | **This phase** |

**This module asks:** Can the surviving mixed g_+ * g_- cross-coupling
channel induce an effective support term shape-compatible with the missing
1/r^2-type Component B?

**The answer:** No, within the tested framework.  The mixed channel is
insufficient for Component B.

---

## B. Mixed Channel Definition

**The mixed object:**

The doubled-metric action expanded around background g_bar:
- g_1 = g_bar + h_+ + h_-/2
- g_2 = g_bar + h_+ - h_-/2

where h_+ is the physical metric perturbation and h_- is the metric
difference (g_- = g_1 - g_2).

At second order in S_1 - S_2:

    S_1 - S_2 = delta^1 S * h_- + delta^2 S_EH(h_+, h_-) + O(3)

The **mixed term** delta^2 S_EH(h_+, h_-) is:

| Property | Value |
|:---|:---|
| Type | Lichnerowicz bilinear form |
| Bilinear | Yes (linear in h_+ AND linear in h_-) |
| Self-adjoint | Yes |
| Only surviving quadratic | Yes |
| Diagonal h_-^2 | Absent (CTP antisymmetry, g_- energy phase) |
| Diagonal h_+^2 | Cancelled (between the two copies) |
| Perturbative order | 2 |

---

## C. Surviving Mixed Structure

**Taylor expansion derivation:**

Setting eta_1 = h_+ + h_-/2 and eta_2 = h_+ - h_-/2:

    delta^2 S(eta_1, eta_1) = delta^2 S(h_+, h_+) + delta^2 S(h_+, h_-) + (1/4)*delta^2 S(h_-, h_-)
    delta^2 S(eta_2, eta_2) = delta^2 S(h_+, h_+) - delta^2 S(h_+, h_-) + (1/4)*delta^2 S(h_-, h_-)

Subtracting:

    delta^2 S(eta_1, eta_1) - delta^2 S(eta_2, eta_2) = 2 * delta^2 S(h_+, h_-)

The coefficient 2 is exact (from bilinearity).

**Numerical verification:**

Using scalar model f(x) = x^4, the mixed term coefficient (proportional to
delta * epsilon) is 12*a^2.  Numerical verification passes with residual
~ 5e-05.

---

## D. Source Chain

The complete source chain for the mixed channel:

    ICs --> Phi_- spatial profile f(r) [IC-dependent]
         --> Phi_-(t,r) = A * exp(phi*t/tau) * f(r) [growing ghost mode]
         --> T_tilde_mu_nu[Phi_-] = bilinear(Phi_eq, Phi_-) [depends on f(r)]
         --> h_- = G_hat^{-1} * T_tilde [linearized Einstein, depends on f(r)]
         --> delta^2 S_EH(h_+, h_-) feeds h_- back into h_+ equation

At every step, the IC-dependent spatial profile f(r) propagates.

**The h_- equation of motion:**

    G_hat(h_-) = -16*pi*G * T_tilde_mu_nu[Phi_-]

where T_tilde is the scalar difference stress-energy:

    T_tilde_mu_nu = partial_mu Phi_eq * partial_nu Phi_-
                  + partial_mu Phi_- * partial_nu Phi_eq
                  - g_mu_nu [partial^a Phi_eq * partial_a Phi_- + m^2 * Phi_eq * Phi_-]

This is bilinear in Phi_eq and Phi_-.

---

## E. Effective Support Analysis

**Note:** This is a structural EOM-level argument, not a path-integral
integration.  We use the h_- EOM to express h_- in terms of sources,
then substitute into the h_+ equation.

Substituting h_- = G_hat^{-1} * T_tilde[Phi_-] into the h_+ equation:

    G_hat(h_+) = -8*pi*G * T_phys[Phi_+] + effective_correction(G_hat^{-1} * T_tilde[Phi_-])

The effective correction:
- Depends on Phi_-(r) = A * exp(phi*t/tau) * f(r) -> IC-dependent
- Grows as exp(2*phi*t/tau) -> time-dependent, not static
- Ghost-sourced: Phi_- has wrong-sign kinetic energy
- CTP-killed: Phi_-(t_final) = 0 -> correction vanishes at final time
- Projection-killed: in physical limit Phi_- -> 0 -> correction vanishes

---

## F. Shape / Scaling Analysis

**Radial proxy for T_tilde:**

    T_tilde(r) ~ Phi'_eq(r) * f'(r) + m^2 * Phi_eq(r) * f(r)

With Phi_eq = M/r^2, Phi'_eq = -2M/r^3, m^2 = 1/tau^2:

    T_tilde(r) ~ -(2M/r^3) * f'(r) + (M/tau^2 r^2) * f(r)

**Two test IC profiles:**

| Profile | f(r) | T_tilde scaling (large r) | T_tilde scaling (small r) | Best-fit exponent |
|:---|:---|:---|:---|:---|
| Profile 1 | 1/r | ~1/r^3 to 1/r^5 | ~1/r^5 | ~ -4.6 |
| Profile 2 | 1/r^2 | ~1/r^4 to 1/r^6 | ~1/r^6 | ~ -5.8 |
| Component B | N/A | 1/r^2 | 1/r^2 | -2.0 |

**Different ICs give different radial profiles.**  Neither matches 1/r^2.

**General structural argument (not resting on two examples alone):**

Because T_tilde is bilinear in Phi_eq and Phi_-, and Phi_- carries an
arbitrary IC-dependent spatial profile f(r), the induced mixed-channel
support cannot define a unique geometric 1/r^2-type Component B term
independently of initial data.  The formula T_tilde(r) shows that different
f(r) produce different T_tilde(r) — this is a structural consequence of
the bilinear dependence on f(r), not an artifact of the two test profiles.

---

## G. Projection & CTP Boundary Sensitivity

| Mechanism | Result | Argument |
|:---|:---|:---|
| Physical limit | **Killed** | Phi_- -> 0 implies T_tilde -> 0 implies h_- -> 0 implies mixed contribution = 0 |
| CTP boundary | **Killed** | Phi_-(t_final) = 0 implies h_-(t_final) = 0 |
| Pre-projection only | **Yes** | Entire mixed structure exists only away from the physical limit |

Both killing mechanisms are structural (follow from the formalism itself).

---

## H. Physical Admissibility

| Pathology | Mechanism | Consequence |
|:---|:---|:---|
| IC-dependent | Phi_- spatial profile f(r) set by ICs | NOT geometric 1/r^2 |
| Ghost-sourced | Phi_- has wrong-sign kinetic | Ghost-mediated effective source |
| CTP-killed | Phi_-(t_final) = 0 | Vanishes at final time |
| Projection-killed | Phi_- -> 0 in physical limit | Vanishes in physical metric |

These four pathologies jointly render the mixed channel non-promotable to a
clean physical Component B mechanism within the tested perturbative Galley
framework.

---

## I. Final Classification & Full Route B Status

Classification: **mixed_channel_insufficient_within_tested_galley_framework**

Residue progression:
- "full g_- sector uncomputed" -> (g_- energy phase) -> "mixed channel only"
- "mixed channel unresolved" -> (this phase) -> "mixed channel insufficient"

**Full Route B status (within tested perturbative Galley CTP framework):**

| Channel | Status |
|:---|:---|
| Post-projection T^Phi | Insufficient (pure 1/r^4, identical to Route C) |
| Phi_- sector | Pathological (ghost, IC-dependent, CTP-killed) |
| S_diss | Vanishes in physical limit |
| g_- standalone diagonal | Absent (CTP antisymmetry kills quadratic action) |
| g_- mixed g_+ * g_- | Insufficient within tested framework |

All tested classical Route B channels are now classified.

---

## J. Phase Lock Update

    Phase 6 (Static Interior):       LOCKED (f(R_eq) = -17.71)
    Phase 6B (Dynamical Interior):   LOCKED (A_crit = 1.062, global_robust)
    Phase 6C (Metric Deficit):       LOCKED (epsilon_min two-component)
    Route C Deficit Assessment:      LOCKED (route_c_insufficient_within_markov_reduction)
    Route B Component B Test:        LOCKED (route_b_post_projection_insufficient__preprojection_unresolved)
    Route B g_- Energy Density:      LOCKED (gminus_diagonal_quadratic_energy_absent__mixed_channel_unresolved)
    Route B Mixed Channel:           LOCKED (mixed_channel_insufficient_within_tested_galley_framework)

    route_b_classical_channels_closed_within_tested_galley_framework: TRUE
    all_tested_channels_classified: TRUE
    framework_scope: perturbative_galley_ctp_framework

---

## K. Numerical Validation

| Quantity | Value |
|:---|:---|
| Mixed quadratic term survival | True |
| Analytical coefficient | 2.0 (exact) |
| Numerical verification (f=x^4) | Passed (residual ~ 5e-05) |
| Profile 1 (f=1/r) best-fit exponent | ~ -4.6 |
| Profile 2 (f=1/r^2) best-fit exponent | ~ -5.8 |
| Radial profiles differ | True |
| Matches Component B (1/r^2) | False |
| Survives physical limit | False |
| Survives CTP boundary | False |
| Is pre-projection only | True |
| Ghost-sourced | True |
| IC-dependent | True |
| Pathology channels | 4 |
| Jointly disqualifying | True |
| Is physically admissible | False |

Benchmark: 55/55 ALL CHECKS PASSED.
Pytest: 57/57 ALL TESTS PASSED in 0.31s.

---

## L. Nonclaims (10)

1. This phase does NOT prove Route B physically incorrect in full generality.
   It closes the tested classical Route B residue within the Galley CTP
   framework at perturbative order.

2. A formal mixed coupling is not automatically a physical support term.
   Here the mixed channel is explicitly shown to be ghost-sourced,
   IC-dependent, CTP-killed, and projection-killed.

3. Pre-projection structure is not automatically usable post-projection.
   The mixed channel exists only pre-projection and vanishes entirely
   in the physical limit.

4. Gauge sensitivity: the linearized Einstein equation involves gauge
   choices.  The IC-dependence and projection-killing results are
   gauge-independent, but the detailed form of h_- may be gauge-dependent.

5. Failure here closes only the tested classical Route B residue, not all
   conceivable classical mechanisms (e.g., non-Galley constructions,
   higher-order effects, non-perturbative mechanisms).

6. The explicit tensor structure of h_- has NOT been solved in closed form.
   The analysis derives the source chain structurally and verifies
   IC-dependence numerically.

7. The "integration out" of h_- is a structural EOM-level argument, not a
   path-integral integration.

8. The IC-dependence result relies on Phi_- being IC-dependent, established
   in route_b_component_b.py.

9. The ghost characterization of Phi_- (wrong-sign kinetic) was established
   in galley_truncation.py.

10. Non-perturbative effects, if they exist, are outside the scope of this
    linearized analysis.

---

## M. Assumptions (10)

1. The doubled-metric action is S_grav = (1/16*pi*G) * integral
   [sqrt(-g_1)*R_1 - sqrt(-g_2)*R_2] d^4x.

2. The +/- decomposition: g_+ = (g_1+g_2)/2, g_- = g_1-g_2
   (standard CTP variables).

3. The background is the static spherically symmetric equilibrium with
   Phi_eq = M/r^2.

4. Perturbative analysis: h_+ = delta g_+ (physical perturbation),
   h_- = g_- (metric difference).

5. The surviving mixed quadratic structure is delta^2 S_EH(h_+, h_-)
   (diagonal h_-^2 absent by CTP antisymmetry).

6. The scalar difference sector: Phi_- grows at rate phi/tau with
   IC-dependent spatial profile f(r).

7. The scalar difference stress-energy T_tilde is bilinear in Phi_eq
   and Phi_- at leading order.

8. The h_- EOM is the linearized Einstein equation sourced by
   T_tilde[Phi_-].

9. The CTP boundary condition requires Phi_-(t_final) = 0 and
   h_-(t_final) = 0.

10. Component B requires a geometric (IC-independent) 1/r^2-type
    radial support profile.

---

## N. Recommended Next Move

The tested classical frontier is closed within the perturbative Galley CTP
framework.  No tested classical Route B channel provides the missing 1/r^2
Component B support.

Remaining avenues would require:
- Non-perturbative mechanisms (if they exist within the Galley framework)
- Non-Galley classical constructions (alternative doubled-field frameworks)
- Non-classical extensions (quantum effects, etc.)

These are outside the scope of the classical Route B analysis.
