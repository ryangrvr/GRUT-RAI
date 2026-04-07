# GRUT III Book B — Stage B0 (MC1): Source Coupling Specification

**Inherited:** BA1-BA7, X1-X10 (Book A). Environmental bath confirmed (A3).

**Task:** Evaluate three candidates for X[g_{mu nu}] with minimal-complexity discipline and select the minimum passing option.

---

## Candidate A: X = alpha R + beta

### Definition

```
X_A = beta + alpha R(g_r)
```

- beta: constant background equilibrium. [Phi]. **EFT parameter.**
- alpha: dimensionful curvature coupling. [Phi] × [length]^2. **EFT parameter.**
- R: Ricci scalar of g_r.

Parameter count: **2** (beta, alpha).

### 1. Regime tags

| Regime | Status | Condition |
|--------|:------:|-----------|
| Flat space (R = 0) | CONTROLLED | X = beta. Constitutive law reduces to tau dPhi/dt + Phi = beta. |
| Weak field, matter present | CONTROLLED | R = -8 pi G T^{matter} / c^4 (trace of Einstein equation). X = beta + alpha × (-8 pi G T^m / c^4). Perturbatively small correction. |
| Vacuum Schwarzschild/Kerr | **BLIND** | R = 0 in Ricci-flat spacetimes. X = beta. Phi does not respond to vacuum curvature. |
| Moderate curvature (NS surface) | CAUTION | alpha R ~ beta possible. Nonlinear in the effective X. |
| Strong curvature (near horizon) | UNSAFE | Untested. R may diverge at matter-filled interiors. |
| Cosmological (FRW) | CONTROLLED | R = 6(a-double-dot/a + (a-dot/a)^2 + k/a^2). X varies on Hubble timescale. |

### 2. Phi role classification

**Auxiliary in flat space.** When X = beta (constant), the constitutive equation tau dPhi/dt + Phi = beta has a single trivial attractor Phi* = beta. Phi carries no independent dynamics — it is slaved to the constant X.

**Dynamical when X varies.** When R changes in time (e.g., near a collapsing star, or on cosmological timescales), X_t varies and Phi tracks it with lag tau. Phi is then a dynamical degree of freedom encoding the history of the curvature through its approach to the moving target.

**Classification: auxiliary at equilibrium, dynamical during transients.** Status: **DERIVED** from the constitutive law structure.

### 3. Semiclassical consistency impact

The semiclassical Einstein equation (from variation of the CTP action w.r.t. g_a) would read:

```
G_{mu nu} = 8 pi G (T^{matter}_{mu nu} + T^{Phi}_{mu nu})
```

For Candidate A, T^{Phi}_{mu nu} receives contributions from:
- The kinetic-like sector: zero in the overdamped limit (no (dPhi)^2 term)
- The potential sector: X depends on R, creating an implicit R-R coupling through the Einstein equation

**Consistency check:** If X = beta + alpha R, then T^{Phi}_{mu nu} depends on R (through Phi's approach to X = beta + alpha R). Substituting back into the Einstein equation creates a self-consistency condition:

```
G_{mu nu} = 8 pi G T^{matter}_{mu nu} + f(R, Phi)
```

This is structurally similar to f(R) gravity, where the gravitational equation is modified by a function of R. In f(R) gravity, the additional terms can be rewritten as a scalar degree of freedom (the scalaron).

**Risk:** The alpha R coupling in X may introduce a scalaron-like degree of freedom at the level of the Einstein equation, even if Phi itself is overdamped. This would be an implicit modification of GR beyond what the constitutive sector intends.

**Assessment:** In the weak-field regime (alpha R << beta), the correction to the Einstein equation is perturbatively small: delta G_{mu nu} / G_{mu nu} ~ alpha R T^{Phi} / T^{matter} << 1 provided T^{Phi} << T^{matter}. From GRUT-II Phase 4: T^{Phi}_{00} = rho_eq = -X^2/(2 tau^2). For X ~ 1, tau ~ 1 s: rho_Phi ~ 0.5 kg/m^3 — potentially significant near ordinary matter densities. This requires alpha to be small enough that the backreaction is subdominant.

**Status: CAUTION.** No inconsistency at small alpha. Potential f(R)-like modification at large alpha. Must constrain alpha from backreaction bounds.

### 4. Linear stability / ghost screen

In the linearized theory (Phi = beta + delta_Phi, g = eta + h), the constitutive equation is:

```
tau d(delta_Phi)/dt + delta_Phi = alpha delta_R
```

where delta_R is the linearized Ricci scalar perturbation.

**Stability:** delta_Phi relaxes exponentially to alpha delta_R with timescale tau. The eigenvalue is -1/tau < 0. **Stable.** No growing mode. No ghost.

**Ghost screen:** Phi enters the CTP action linearly in Phi_a (dissipation) and quadratically in Phi_a (noise). The noise coefficient D > 0 ensures positivity. No negative-norm states arise from the Phi sector. The gravitational sector is standard CTP (ghost-free by the standard argument). The coupling alpha R in X is linear in the curvature perturbation, which does not introduce new propagating DOF in the linearized theory.

**Status: PASS.** No instability or ghost in the weak-field linearized regime.

### 5. Parameter cost and complexity score

| Metric | Score |
|--------|:-----:|
| Free parameters | 2 (beta, alpha) |
| Nonlinearity of X in g | Linear (R is linear in second derivatives of g) |
| Additional DOF introduced | 0 (Phi is slaved, not propagating) |
| Analytic tractability | High (linear ODE with linear source) |
| **Complexity score** | **2/10** (minimal) |

### 6. Failure modes and nonclaims

| # | Item | Type |
|---|------|:----:|
| FA1 | X = beta in vacuum Schwarzschild. Phi is blind to BH exterior. | **Failure mode** |
| FA2 | At large alpha: f(R)-like backreaction on Einstein equation. | **Failure mode** |
| FA3 | alpha is not determined from the CTP action. It is an EFT input. | **Nonclaim** |
| FA4 | Candidate A does NOT make the CTP action covariant. It specifies X, not the full action. | **Nonclaim** |
| FA5 | The strong-field regime is not controlled by Candidate A. | **Nonclaim** |

---

## Candidate B: X = alpha R + gamma T + beta

### Definition

```
X_B = beta + alpha R + gamma T^{matter}
```

where T^{matter} = g^{mu nu} T^{matter}_{mu nu} is the trace of the matter stress-energy tensor.

- beta, alpha: same as Candidate A. **EFT parameters.**
- gamma: matter coupling. [Phi] × [length]^2 × [energy]^{-1} × [volume]. **EFT parameter.**

Parameter count: **3** (beta, alpha, gamma).

### 1. Regime tags

| Regime | Status | Notes |
|--------|:------:|-------|
| Flat space | CONTROLLED | X = beta (T = 0 in vacuum). |
| Weak field, matter | CONTROLLED | Both R and T contribute. In GR: R = -8 pi G T / c^4, so alpha R + gamma T = (-8 pi G alpha / c^4 + gamma) T + beta. If alpha and gamma are independent, this is a single effective coupling to T. If they are related (gamma = 8 pi G alpha / c^4), the T terms cancel and X = beta again. |
| Vacuum Schwarzschild | **BLIND** | R = 0 and T = 0 in vacuum. X = beta. Same as A. |
| Moderate curvature | CAUTION | Both terms potentially order-unity. |
| Cosmological | CONTROLLED | T includes dark energy/matter components if present. |

### Key observation

**In GR, R and T are not independent:** the Einstein equation gives R = -8 pi G T / c^4 (in 4D, trace-reversed). Therefore:

```
alpha R + gamma T = (-8 pi G alpha / c^4 + gamma) T
```

Unless gamma is fine-tuned to exactly cancel the alpha contribution (gamma = 8 pi G alpha / c^4), Candidate B is equivalent to:

```
X_B = beta + gamma_eff T
```

where gamma_eff = -8 pi G alpha / c^4 + gamma. This is a SINGLE effective coupling to T, not two independent couplings.

**This means:** Either (a) Candidate B reduces to a single coupling to T (making it equivalent to a matter-coupled scalar with one parameter), or (b) alpha and gamma are both needed because the on-shell relation R = -8 pi G T / c^4 is modified by Phi backreaction (making the two terms genuinely independent). Option (b) requires the full coupled (g, Phi) system, which is not yet constructed.

### 2. Phi role classification

Same as Candidate A: auxiliary at equilibrium, dynamical during transients. The additional T coupling does not change the classification.

### 3. Semiclassical consistency impact

Worse than A. The gamma T coupling means T^{Phi}_{mu nu} depends on T^{matter}_{mu nu} through X. This creates a circular dependence in the Einstein equation:

```
G_{mu nu} = 8 pi G [T^{matter}_{mu nu} + T^{Phi}_{mu nu}(Phi(X(T^{matter})))]
```

Self-consistency requires solving for T^{matter} and Phi simultaneously. This is tractable perturbatively but adds complexity.

### 4. Linear stability / ghost screen

Same as A in the linearized regime. The additional gamma T coupling is linear in the matter perturbation, which does not introduce new DOF or instabilities. **PASS.**

### 5. Parameter cost and complexity score

| Metric | Score |
|--------|:-----:|
| Free parameters | 3 (beta, alpha, gamma) — but effectively 2 on-shell (beta, gamma_eff) |
| Nonlinearity of X in g | Same as A (R is linear; T is linear in matter fields) |
| Additional DOF | 0 |
| Analytic tractability | Moderate (requires matter EOS for T) |
| Redundancy | alpha and gamma are degenerate on-shell unless backreaction is included |
| **Complexity score** | **4/10** |

### 6. Failure modes and nonclaims

| # | Item | Type |
|---|------|:----:|
| FB1 | Same vacuum-blindness as A: R = 0, T = 0 in vacuum. | **Failure mode** |
| FB2 | Parameter degeneracy: alpha and gamma are not independently measurable on-shell in GR. | **Failure mode** |
| FB3 | Circular dependence in semiclassical Einstein equation. | **Failure mode** (tractable perturbatively) |
| FB4 | gamma is not determined. | **Nonclaim** |

---

## Candidate C: X = alpha R + beta + epsilon □R

### Definition

```
X_C = beta + alpha R + epsilon □R
```

where □R = g^{mu nu} nabla_mu nabla_nu R is the d'Alembertian of the Ricci scalar.

Parameter count: **3** (beta, alpha, epsilon).

### Evaluation (abbreviated — only if A/B fail)

**When is C needed?** Only if the constitutive field must respond to the RATE OF CHANGE of curvature, not just its value. The □R term introduces second derivatives of R (fourth derivatives of the metric) into X. This is the signature of Starobinsky-type R^2 gravity.

### 1. Regime tags

| Regime | Status |
|--------|:------:|
| Static weak field | CONTROLLED (□R = 0 for static spacetimes, so C = A) |
| Dynamic weak field | CAUTION (□R ≠ 0 during dynamical evolution; epsilon □R is a correction to the transient response) |
| Strong field | UNSAFE (fourth-derivative terms in the Einstein equation — Ostrogradsky instability risk) |

### 4. Stability / ghost screen

**CRITICAL RISK.** Fourth-derivative terms in the metric equation of motion generically introduce Ostrogradsky ghosts. In pure R + alpha R^2 gravity (Starobinsky), the ghost is absent because the R^2 term can be rewritten as a healthy scalar (the scalaron). But the epsilon □R coupling to Phi is a different structure — it couples the scalaron dynamics to the constitutive field. Whether this is ghost-free depends on the detailed coupled (g, Phi) action, which has not been constructed.

**Status: BLOCKED** until ghost-freedom is demonstrated.

### 5. Parameter cost and complexity

| Metric | Score |
|--------|:-----:|
| Parameters | 3 (beta, alpha, epsilon) |
| Derivative order | 4th (in the metric, through □R) |
| Ghost risk | Elevated (Ostrogradsky) |
| Tractability | Low |
| **Complexity score** | **7/10** |

### 6. Failure modes

| # | Item | Type |
|---|------|:----:|
| FC1 | Ostrogradsky ghost risk from □R coupling. | **Failure mode (potentially fatal)** |
| FC2 | Equivalent to static A in static spacetimes. Adds nothing there. | **Redundancy** |
| FC3 | Three parameters, none determined. | **Nonclaim** |

---

## Decision Matrix

| Property | A: αR + β | B: αR + γT + β | C: αR + β + ε□R |
|----------|:---------:|:---------------:|:----------------:|
| Parameters | **2** | 3 (effectively 2 on-shell) | 3 |
| Vacuum response | Blind (R=0) | Blind (R=0, T=0) | Blind (static vacuum) |
| Weak-field consistency | **PASS** | PASS (with degeneracy) | PASS (static) |
| Stability/ghosts | **PASS** | PASS | **BLOCKED** |
| Semiclassical backreaction | Manageable (small alpha) | Circular (tractable perturbatively) | Unstudied |
| Level-1 compatibility | Direct (R ~ Grho ~ 1/t_dyn^2) | Direct (T ~ rho directly) | Overkill |
| Complexity | **2/10** | 4/10 | 7/10 |
| Redundancy | None | alpha/gamma degenerate on-shell | Reduces to A in static case |

---

## Decision: **adopt_A**

### Rationale

1. **Candidate A passes all gates in the controlled regime.** Linear stability: PASS. Ghost screen: PASS. Weak-field consistency: PASS. CTP unitarity: unaffected (X enters linearly in Sector 1). Complexity: minimal (2 parameters).

2. **Candidate B adds a parameter (gamma) that is degenerate with alpha on-shell in GR.** The trace relation R = -8 pi G T / c^4 makes alpha R and gamma T linearly dependent. Candidate B reduces to a relabeled version of A with a different effective coupling to the matter trace. It adds complexity without new physics in the controlled regime. **Not needed.**

3. **Candidate C is blocked** by Ostrogradsky ghost risk from the □R term. It reduces to A in static spacetimes and adds nothing in the controlled regime. It should not be adopted until ghost-freedom is explicitly demonstrated. **Not needed and potentially dangerous.**

4. **The vacuum-blindness of A (FA1) is a known limitation, not a failure in the controlled regime.** The controlled regime is weak-field with matter present (where R ≠ 0). Vacuum Schwarzschild exterior is UNSAFE per Book A. Extending to vacuum spacetimes is a Book C issue.

5. **The minimal passing candidate is A.** Consistent with the complexity-minimization mandate.

### Adopted interface

```
X[g_r] = beta + alpha R(g_r)

EFT parameters: beta (background equilibrium), alpha (curvature coupling)
Status: ASSUMED (provisional — not derived from CTP action)
Confidence: 0.55
Regime: weak field (alpha R << beta), matter present (R ≠ 0)
```

### Book B carry-forward contract

**From B0 into B1 and beyond, the following are established:**

| # | Item | Status |
|---|------|:------:|
| BF1 | X = beta + alpha R is the provisional source coupling. | ASSUMED |
| BF2 | beta and alpha are EFT parameters (not derived). | ASSUMED |
| BF3 | X vanishes in vacuum Schwarzschild (R = 0 → X = beta only). | KNOWN LIMITATION |
| BF4 | At small alpha, semiclassical backreaction is perturbatively controlled. | DERIVED (linearized) |
| BF5 | No ghost or instability from the X coupling in the linearized regime. | DERIVED |
| BF6 | Candidate B is available if on-shell degeneracy is broken by backreaction. | RESERVED |
| BF7 | Candidate C is BLOCKED until ghost-freedom is demonstrated. | BLOCKED |

**Nonclaims:**
- No claim that alpha is known or constrained.
- No claim that A is unique or correct — it is the minimum passing candidate.
- No strong-field claim.
- No covariance claim beyond scalar X depending on scalar R.

---

*B0 (MC1) complete. Decision: adopt_A. X = beta + alpha R. Two parameters. Weak-field controlled. Vacuum-blind (flagged). Ghost-free (linearized). Candidate B redundant on-shell. Candidate C blocked (Ostrogradsky). Carry-forward contract: BF1-BF7.*
