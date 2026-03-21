# Route C Deficit Assessment — Nonlocal Metric Back-Reaction vs Missing 1/r^2

## Status

**ROUTE C INSUFFICIENT WITHIN MARKOV REDUCTION**

Classification: **route_c_insufficient_within_markov_reduction**

This module tests whether Route C (nonlocal retarded action) can generate
the missing 1/r^2 support identified in Phase 6C.  Within the tested
Markov-reduced exponential-kernel pathway, Route C reproduces only the
existing 1/r^4-type support structure and fails to generate an independent
1/r^2-type component.  The failure is one of shape, not amplitude.
Five loopholes are documented; this is NOT a general no-go for Route C.

---

## A. Mission and Context

Phase 6C (FROZEN) identified the minimal additive source for metric closure:

    epsilon_min(r) = |rho_eq(r)| + 1/(8*pi*r^2)

with two components:
- **Component A ~ 1/r^4**: cancels the equilibrium negative density rho_eq
- **Component B ~ 1/r^2**: intermediate-radius geometric support

No tested GRUT profile provides Component B.  The provisional candidate-sector
survey listed Route C at "highest structural plausibility."

**This module asks:** Can the Markov-reduced Route C stress-functional
generate an independent 1/r^2 energy density component?

**The answer:** No, within the tested Markov pathway.  Route C's effective
energy density is pure 1/r^4, providing Component A but not Component B.

---

## B. Route C Effective Energy Density

Route C uses the exponential retarded kernel K(s) = (1/tau)exp(-s/tau)Theta(s).
The Markov property absorbs the full history into the current auxiliary field Phi,
making T^Phi a standard minimally-coupled scalar (from nonlocal_stress.py):

    T^Phi_{ab} = nabla_a Phi nabla_b Phi - g_{ab}[(1/2)(nabla Phi)^2 + V(Phi) - Phi X/tau]

The dominant kinetic energy density at equilibrium is:

    epsilon_RC(r) = (1/2)(Phi_dot)^2 = A_crit^2 * M^2 / (2 * tau^2 * r^4)

This is **pure 1/r^4** — no 1/r^2 component.

| Quantity | At R_eq = 1/3 | At r = 1 |
|:---|:---|:---|
| epsilon_RC | 7.614 | 0.0940 |
| epsilon_min | 7.108 | 0.1231 |
| Component A | 6.750 | 0.0833 |
| Component B | 0.358 | 0.0398 |
| deficit_ratio (RC/min) | 1.071 | 0.763 |

**Shape mismatch interpretation:** Route C's effective 1/r^4 support is too
concentrated: it oversupplies the core (ratio > 1 at R_eq) while undersupplying
intermediate radii (ratio ~ 0.76 at r=1), which is exactly the wrong shape to
replace Component B.  The failure is one of shape, not amplitude.

---

## C. The Four Insufficiency Chains

### Chain 1: Markov Kinetic Scaling (strongest)

- **Premise:** Exponential kernel => Markov property => T^Phi_history = 0
- **Mechanism:** T^Phi = standard scalar; epsilon = (1/2)(Phi_dot)^2 with
  Phi_dot ~ M/(tau*r^2) => epsilon ~ 1/r^4
- **Conclusion:** No independent 1/r^2 from kinetics.  To get epsilon ~ 1/r^2,
  one would need Phi_dot ~ 1/r, but X = M/r^2 sources Phi_dot ~ 1/r^2.

### Chain 2: Self-Healing Lapse Correction

- **Premise:** Lapse correction ODE: tau d(delta_Phi)/dt + delta_Phi = Psi(X - Phi)
- **Mechanism:** At equilibrium X = Phi => source = 0 => delta_Phi = 0
- **Conclusion:** Lapse channel adds ZERO energy density at equilibrium.
  Correction is maximal during transient, not at endpoint.

### Chain 3: Candidate Potential Sector

- **Premise:** V(Phi) = Phi^2/(2*tau^2) is a tested inherited candidate ansatz
  (from Route A / shared closure), NOT intrinsic to Route C
- **Mechanism:** V(Phi_eq) = (M/r^2)^2/(2*tau^2) = M^2/(2*tau^2*r^4) => 1/r^4
- **Conclusion:** Potential contributes only 1/r^4 within the tested ansatz

### Chain 4: Spatial Gradient

- **Premise:** Phi_eq = M/r^2 => dPhi/dr = -2M/r^3
- **Mechanism:** (dPhi/dr)^2 = 4M^2/r^6 => 1/r^6
- **Conclusion:** Spatial gradient is even steeper than 1/r^4.
  Evaluated in current reduced radial background, not full covariant.

---

## D. Deficit Ratio Profile

The deficit ratio epsilon_RC / epsilon_min varies across the barrier:

| Radius | Ratio | Interpretation |
|:---|:---|:---|
| R_eq = 1/3 | 1.071 | Overcovering (Component A dominated) |
| r = 0.5 | ~0.98 | Near parity |
| r = 1.0 | 0.763 | Undercovering (Component B growing) |
| r ~ 1.4 (deficit edge) | ~0.58 | Maximum undercovering |

The ratio drops from >1 near the core to <0.6 at the deficit boundary,
confirming that Route C's 1/r^4 profile is the wrong shape.

---

## E. Loophole Catalog

| # | Loophole | Severity | Mechanism |
|:---|:---|:---|:---|
| 1 | Non-exponential kernel | **high** | Breaks Markov => genuinely nonlocal T^Phi_history |
| 2 | Full covariant metric variation | medium | 5 contributions not computed in closed form |
| 3 | Nonlinear lapse effects | low | O(Psi^2) terms, but X=Phi is structural identity |
| 4 | Off-equilibrium transients | medium | Could change mass baseline before equilibrium |
| 5 | Modified source X != M/r^2 | **high** | X ~ M/r => Phi_dot ~ 1/r => epsilon ~ 1/r^2 |

Route C remains alive through these loopholes.  The insufficiency applies
only within the tested Markov-exponential-kernel pathway.

---

## F. Provisional Candidate Sector Ranking Update

Route C is downgraded within the tested pathway based on this assessment.
This is a classification tool, not a final determination.

| Route | Previous Status | Current Status | Obstruction |
|:---|:---|:---|:---|
| Route C | Highest structural plausibility | **Insufficient within Markov reduction** | Pure 1/r^4 from kinetics; no 1/r^2 |
| Route B | Provisional | **Provisional** (unchanged) | Ghost mode, gravity coupling |
| Route A | Conditional | Conditional (unchanged) | Overdamped limit, potential ansatz |

Route B (Galley doubled-field) is now the highest-ranking untested candidate
for Component B, but has its own obstruction class (ghost mode, underdetermined
gravity coupling in the full doubled-metric sector).

---

## G. Numerical Validation

| Quantity | Value |
|:---|:---|
| EPSILON_RC_COEFF | 0.09399 |
| COMP_B_COEFF | 0.03979 |
| deficit_ratio at R_eq | 1.071 |
| deficit_ratio at r=1 | 0.763 |
| deficit_ratio range | [0.575, 1.091] |
| Lapse correction at eq | 0 (exact) |
| V(Phi_eq) at R_eq | 6.750 |
| (nabla_r Phi)^2 at R_eq | 729.0 |
| Integrated shortfall | 0.288 |

Benchmark: 70/70 ALL CHECKS PASSED.
Pytest: 70/70 ALL TESTS PASSED in 0.36s.

---

## H. Nonclaims (10)

1. The Markov reduction applies ONLY to the exponential kernel.
   Non-exponential kernels may produce genuinely nonlocal T^Phi_history.

2. The insufficiency is evaluated at STATIC EQUILIBRIUM.
   Transient dynamical effects are not assessed.

3. The classification is NOT a general no-go for Route C.

4. The full covariant metric variation has NOT been computed in closed form.

5. Nonlinear lapse effects beyond first order are not computed.

6. A modified source X != M/r^2 could produce epsilon ~ 1/r^2.

7. V(Phi) = Phi^2/(2*tau^2) is a tested inherited candidate ansatz,
   NOT intrinsic to Route C.

8. The spatial-gradient scaling is evaluated in the current reduced radial
   background, NOT a full covariant gradient-sector derivation.

9. The provisional ranking is a classification tool, not a prediction.

10. The integrated deficit depends on grid resolution and domain boundaries.

---

## I. Assumptions (5)

1. Markov-reduced auxiliary-field representation with exponential kernel.

2. T^Phi is the standard minimally-coupled scalar form.

3. Equilibrium field profile Phi_eq = X_eq = M/r^2.

4. Deficit evaluated at static equilibrium.

5. V(Phi) = Phi^2/(2*tau^2) is a tested inherited candidate ansatz
   from Route A / shared closure, not intrinsic to Route C.

---

## J. Phase Lock Update

    Phase 6 (Static Interior):      LOCKED (f(R_eq) = -17.71)
    Phase 6B (Dynamical Interior):  LOCKED (A_crit = 1.062, global_robust)
    Phase 6C (Metric Deficit):      LOCKED (epsilon_min = |rho_eq| + 1/(8*pi*r^2), two-component)
    Route C Deficit Assessment:     LOCKED (route_c_insufficient_within_markov_reduction)

    Deficit ratio at R_eq:          1.071 (overcovering — Component A dominated)
    Deficit ratio at r=1:           0.763 (undercovering — Component B shortfall)
    Shape mismatch:                 1/r^4 too concentrated for intermediate-radius support
    Insufficiency chains:           4/4 return provides_1r2 = False
    Loopholes:                      5 documented (2 high, 2 medium, 1 low severity)
    General no-go:                  FALSE (insufficiency within tested pathway only)
    Provisional ranking:            Route C downgraded; Route B highest untested
