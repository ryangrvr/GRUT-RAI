# Route B g_- Energy Density — CTP Antisymmetry Analysis

## Status

**STANDALONE DIAGONAL g_- ENERGY: ABSENT — MIXED CHANNEL UNRESOLVED**

Classification: **gminus_diagonal_quadratic_energy_absent__mixed_channel_unresolved**

This phase closes the standalone diagonal g_- energy question, but not the
full doubled-metric Route B question.  The Route B residue is reduced from
"full g_- sector uncomputed" to "only the mixed g_+ * g_- cross-coupling
channel remains."

---

## A. Mission and Context

Phase 6C (FROZEN) identified the minimal additive source for metric closure:

    epsilon_min(r) = |rho_eq(r)| + 1/(8*pi*r^2)

with two components:
- **Component A ~ 1/r^4**: cancels the equilibrium negative density rho_eq
- **Component B ~ 1/r^2**: intermediate-radius geometric support

Route C was classified as `route_c_insufficient_within_markov_reduction` —
pure 1/r^4 from Markov-reduced kinetics, no 1/r^2.

Route B Component B test was classified as
`route_b_post_projection_insufficient__preprojection_unresolved` — the
only remaining unresolved classical residue was the g_- / doubled-metric
energy channel.

**This module asks:** Can the closed-form energy density of the g_-
metric superposition generate the missing 1/r^2-type support?

**Revised mission:** Determine whether a standalone diagonal quadratic g_-
energy sector exists, and if not, localize the remaining Route B residue
to the mixed g_+ * g_- channel.

**The answer (three-part):**

A. The standalone diagonal quadratic g_- action is ABSENT — CTP
   antisymmetry of S_1 - S_2 kills all even powers of g_-, including
   the quadratic.

B. Four standard energy definitions all give null for the standalone
   diagonal sector.

C. The mixed g_+ * g_- cross-coupling survives at quadratic order and
   remains the sole unresolved Route B residue.

---

## B. Object Definition

**What g_- means in this phase:**

The Galley doubled-metric gravitational action is:

    S_grav = (1/16*pi*G) * integral [sqrt(-g_1)*R_1 - sqrt(-g_2)*R_2] d^4x

The +/- decomposition:
- g_+ = (g_1 + g_2) / 2  (physical metric)
- g_- = g_1 - g_2          (difference metric)
- g_1 = g_+ + g_-/2,  g_2 = g_+ - g_-/2

**What energy definitions are tested:**

Four standard definitions, all for the standalone diagonal sector only:

| # | Definition | Requires |
|:---|:---|:---|
| 1 | Quadratic EH expansion | Nonzero diagonal S_2[g_-] |
| 2 | Canonical Hamiltonian | Diagonal kinetic term |
| 3 | Isaacson tensor | Diagonal quadratic perturbation |
| 4 | Second-order perturbation theory | Diagonal propagator |

All four require a nonzero diagonal quadratic action.

---

## C. CTP Antisymmetry Derivation

For ANY smooth functional F:

    F(a + eps) - F(a - eps) = 2*eps*F'(a) + (2/3!)*eps^3*F'''(a) + ...

Only ODD powers of eps survive.  ALL even powers cancel.

Apply to S_grav with a = g_+ and eps = g_-/2:

    S_EH[g_+ + g_-/2] - S_EH[g_+ - g_-/2]

Taylor expansion of each term around g_+:

    S_EH[g_+ + g_-/2] = S_EH[g_+] + (1/2)*d^1S*g_- + (1/8)*d^2S*g_-^2 + ...
    S_EH[g_+ - g_-/2] = S_EH[g_+] - (1/2)*d^1S*g_- + (1/8)*d^2S*g_-^2 - ...

Subtraction:

| Order | Copy 1 coeff | Copy 2 coeff | S_1 - S_2 | Status |
|:---|:---|:---|:---|:---|
| 0th | +S_EH | +S_EH | 0 | Killed (even) |
| 1st | +(1/2)*d^1S | -(1/2)*d^1S | d^1S*g_- | Survives (EOM) |
| **2nd** | **+(1/8)*d^2S** | **+(1/8)*d^2S** | **0** | **Killed (even)** |
| 3rd | +(1/48)*d^3S | -(1/48)*d^3S | (1/24)*d^3S*g_-^3 | Survives (cubic) |

**The diagonal quadratic action for g_- is IDENTICALLY ZERO.**

This is a purely algebraic result.  It holds for ANY smooth functional.

---

## D. Quadratic Action Analysis

### Diagonal sector: ABSENT

The pure g_-^2 term in S_1 - S_2 cancels exactly:

    (+1/8)*d^2S*g_-^2 - (+1/8)*d^2S*g_-^2 = 0

This is the key result.  The standalone diagonal quadratic action is zero.

### Cross-coupling: SURVIVES

The mixed g_+ * g_- cross-coupling exists at second order:
- It is bilinear: linear in g_- and linear in perturbations of g_+
- It vanishes in the physical limit g_- -> 0
- It cannot define a standalone energy density for g_-

### Individual-copy analysis

| Copy | EH sign | g_-^2 coefficient |
|:---|:---|:---|
| Copy 1 (S_EH[g_1]) | right-sign (+1) | +(1/8)*d^2S |
| Copy 2 (S_EH[g_2]) | wrong-sign (-1 in S_1 - S_2) | +(1/8)*d^2S |
| **Net diagonal** | | **0 (absent)** |

### Upgrade of existing characterization

The existing `galley_truncation.py` (line 893-896) claims "WRONG-SIGN
kinetic energy" for g_- in the individual-copy basis.  In the +/- basis:

- Individual-copy basis: copy 2 has wrong-sign EH (true)
- +/- basis: the wrong-sign and right-sign diagonal contributions cancel
  EXACTLY to zero

The correct characterization of the **standalone diagonal sector** is:
**diagonal quadratic action ABSENT** (not wrong-sign).

This is a strictly sharper result.  The mixed sector is not captured
by this refinement.

---

## E. Four Energy Definitions — Standalone Diagonal Sector Only

All tested for the standalone diagonal sector ONLY, not the mixed channel.

| # | Definition | Result | Reason |
|:---|:---|:---|:---|
| 1 | Quadratic EH expansion | **zero** | S_2_diag[g_-] = 0 |
| 2 | Canonical Hamiltonian | **zero** | No diagonal kinetic term |
| 3 | Isaacson tensor | **zero** | No diagonal quadratic perturbation |
| 4 | Second-order perturbation | **N/A** | No diagonal propagator |

Consensus: **energy structurally absent** in the standalone diagonal sector.

---

## F. Mixed Channel Residue

The mixed g_+ * g_- cross-coupling survives at quadratic order:

| Property | Value |
|:---|:---|
| Cross-coupling exists | Yes |
| Linear in g_- | Yes (vanishes as g_- -> 0) |
| Vanishes in physical limit | Yes |
| Can induce effective support | **Undetermined** |
| Is remaining Route B residue | **Yes** |
| Effective energy computed | No |

The residue has been REDUCED from "full g_- sector uncomputed" to "only
the mixed g_+ * g_- cross-coupling channel remains."

Whether the mixed channel can induce effective support after sourcing,
constraint handling, or field integration is NOT determined by this phase.

---

## G. Component B Compatibility

| Channel | Compatible with Component B | Reason |
|:---|:---|:---|
| Standalone diagonal | **No** | Energy density absent |
| Mixed g_+ * g_- | **Undetermined** | Not computed |
| All computed channels | **No** | No computed channel provides Component B |

Overall status: **unresolved but narrowed**.

---

## H. Projection Sensitivity

| Channel | Projection | Notes |
|:---|:---|:---|
| Standalone diagonal | **Moot** | Object does not exist |
| Mixed g_+ * g_- | **Pre-projection only** | Vanishes at g_- -> 0 |

The mixed channel may also be boundary-sensitive through the full
doubled system — this is not determined.

---

## I. Physical Admissibility

| Channel | Admissibility | Notes |
|:---|:---|:---|
| Standalone diagonal | **Not applicable** | No object to admit |
| Mixed g_+ * g_- | **Undetermined** | Could be gauge/source/boundary-sensitive |

---

## J. Upgrade of Existing Characterization

| Aspect | Previous (galley_truncation.py) | Current (this phase) |
|:---|:---|:---|
| Basis | Individual-copy | +/- decomposition |
| g_- kinetic | "Wrong-sign" | **Absent** (diagonal sector) |
| Scope | Full g_- sector | Standalone diagonal only |
| Mixed channel | Not analyzed | Survives, unresolved |

The upgrade is scoped to the standalone diagonal sector.  The mixed
sector is not captured by this refinement.

---

## K. Final Classification & Phase Lock Update

Classification: **gminus_diagonal_quadratic_energy_absent__mixed_channel_unresolved**

| Channel | Status |
|:---|:---|
| Post-projection T^Phi | **Insufficient** (pure 1/r^4, identical to Route C) |
| Phi_- sector | **Pathological** (ghost, IC-dependent, CTP-killed) |
| S_diss | **Vanishes** in physical limit |
| g_- standalone diagonal | **Absent** (CTP antisymmetry kills quadratic action) |
| g_- mixed g_+ * g_- | **Unresolved** (surviving cross-coupling, not computed) |

Route B is NOT fully closed.  The mixed channel remains open.

    Phase 6 (Static Interior):       LOCKED (f(R_eq) = -17.71)
    Phase 6B (Dynamical Interior):   LOCKED (A_crit = 1.062, global_robust)
    Phase 6C (Metric Deficit):       LOCKED (epsilon_min two-component)
    Route C Deficit Assessment:      LOCKED (route_c_insufficient_within_markov_reduction)
    Route B Component B Test:        LOCKED (route_b_post_projection_insufficient__preprojection_unresolved)
    Route B g_- Energy Density:      LOCKED (gminus_diagonal_quadratic_energy_absent__mixed_channel_unresolved)

    Standalone diagonal g_- energy:  CLOSED (absent by CTP antisymmetry)
    Mixed g_+ * g_- channel:         OPEN (unresolved residue)
    is_full_route_b_no_go:           FALSE (mixed channel remains open)
    residue_reduced:                 TRUE (from full g_- sector to mixed channel only)

---

## L. Numerical Validation

| Quantity | Value |
|:---|:---|
| Diagonal quadratic coefficient | 0 (exact, by CTP antisymmetry) |
| (+1/8) - (1/8) | 0 (exact) |
| Copy 1 quadratic coefficient | +0.125 |
| Copy 2 quadratic coefficient | +0.125 |
| Numerical verification (f(x)=x^4) | Passed (residual ~ 4.4e-09) |
| Cross-coupling exists | True |
| Cross-coupling at physical limit | 0 (g_- -> 0) |
| Energy definitions tested | 4 |
| Definitions giving zero/absent | 3 (+ 1 N/A) |
| Definitions giving nonzero | 0 |
| is_full_route_b_no_go | False |
| standalone_diagonal_closed | True |
| mixed_channel_unresolved | True |

Benchmark: 56/56 ALL CHECKS PASSED.
Pytest: 56/56 ALL TESTS PASSED in 0.37s.

---

## M. Nonclaims (10)

1. This phase does NOT prove Route B physically correct or incorrect
   in full generality.

2. A formal g_- energy density is not automatically observable — but
   here the standalone diagonal object is entirely absent at quadratic
   level.

3. Ghost-linked support is not automatically physically admissible —
   but here the standalone diagonal sector has no support at all.

4. Pre-projection support is not automatically usable post-projection —
   but here no standalone diagonal pre-projection support exists.

5. Failure of the standalone diagonal sector closes only that specific
   sub-channel, not the full mixed g_+ * g_- structure.

6. The CTP antisymmetry argument is purely algebraic:
   f(a+eps) - f(a-eps) has no eps^2 terms.  This holds for ANY smooth
   functional, not just S_EH.

7. The existing characterization of g_- as "wrong-sign kinetic energy"
   (galley_truncation.py line 893-896) is superseded for the standalone
   diagonal sector.  The mixed sector is not captured by this refinement.

8. Cubic and higher odd-order terms in g_- survive the CTP antisymmetry
   but do not contribute to a standard quadratic energy density.

9. The mixed g_+ * g_- cross-coupling exists at second order, vanishes
   in the physical limit, but whether it can induce effective support
   through sourcing or constraint handling is NOT determined by this phase.

10. Any gauge dependence in the perturbative expansion is moot for the
    standalone diagonal sector (zero in any gauge), but the mixed channel
    may be gauge-sensitive through the full doubled system.

---

## N. Assumptions (8)

1. The doubled-metric action is S_grav = (1/16*pi*G) * integral
   [sqrt(-g_1)*R_1 - sqrt(-g_2)*R_2] d^4x.

2. The +/- decomposition is g_+ = (g_1+g_2)/2, g_- = g_1-g_2
   (standard CTP variables).

3. The Taylor expansion of S_EH around g_+ exists to all orders
   (smooth functional).

4. The standalone diagonal quadratic energy is defined from the
   diagonal second-order variation delta^2 S_EH(g_-, g_-).

5. No additional non-minimal couplings between metric copies beyond
   the S_1 - S_2 structure.

6. The equilibrium background is the same as Route C: static,
   spherically symmetric, with Phi_eq = M/r^2.

7. The Isaacson effective stress-energy requires a nonzero diagonal
   quadratic action to define.

8. The canonical Hamiltonian density for the standalone sector is
   constructed from the diagonal quadratic kinetic term via Legendre
   transform.
