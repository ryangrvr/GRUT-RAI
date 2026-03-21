# Route B Component B Test — Pre-Projection Doubled-Field Assessment

## Status

**ROUTE B POST-PROJECTION INSUFFICIENT — PRE-PROJECTION UNRESOLVED**

Classification: **route_b_post_projection_insufficient__preprojection_unresolved**

This module tests whether pre-projection Route B (Galley doubled-field /
doubled-metric sector BEFORE the physical-limit projection) can generate
the missing 1/r^2 support identified in Phase 6C.

Three-part answer:

A. Post-projection Route B cannot solve Component B — it collapses to
   Route C-like 1/r^4 support (identical standard scalar T^Phi).

B. The already-computed pre-projection sectors do not supply a clean
   physical 1/r^2 support — they are ghost-driven, IC-dependent, or
   projection-sensitive.

C. The remaining g_- / doubled-metric sector is still the unresolved
   residue — its energy density has not been computed in closed form.

---

## A. Mission and Context

Phase 6C (FROZEN) identified the minimal additive source for metric closure:

    epsilon_min(r) = |rho_eq(r)| + 1/(8*pi*r^2)

with two components:
- **Component A ~ 1/r^4**: cancels the equilibrium negative density rho_eq
- **Component B ~ 1/r^2**: intermediate-radius geometric support

Route C was classified as `route_c_insufficient_within_markov_reduction` —
pure 1/r^4 from Markov-reduced kinetics, no 1/r^2.  Route B (Galley
doubled-field) was the highest-ranking untested candidate.

**This module asks:** Can full pre-projection Route B generate the missing
1/r^2-type support?

**The answer:** Post-projection Route B is identical to Route C (insufficient).
Computed pre-projection sectors are pathological or projection-killed.  The
g_- / doubled-metric sector remains uncomputed and is the key open channel.

---

## B. Post-Projection Equivalence

In the physical limit (Phi_1 = Phi_2 = Phi, g^(1) = g^(2) = g):
- The doubled action S_1 - S_2 -> 0 (copies cancel)
- The dissipative kernel S_diss -> 0 (Phi_1 - Phi_2 = 0)
- The EOM, derived from variation before projection, reduces to the GRUT law
- T^Phi from metric variation = standard minimally-coupled scalar
- epsilon = A_crit^2 * M^2 / (2 * tau^2 * r^4) — pure 1/r^4

This is IDENTICAL to Route C.  The same shape mismatch applies.

| Quantity | At R_eq = 1/3 | At r = 1 |
|:---|:---|:---|
| epsilon_post_proj | 7.614 | 0.0940 |
| epsilon_min | 7.108 | 0.1231 |
| deficit_ratio | 1.071 | 0.763 |
| Interpretation | Overcovering | Undercovering |

**Post-projection channel: CLOSED.  Insufficient for Component B.**

---

## C. Pre-Projection Sector Analysis

### C1. Phi_- Sector (Ghost / Difference Mode)

The Galley cross-coupled EOMs give:

    dPhi_+/dt = (X - Phi_+) / tau    [GRUT relaxation]
    dPhi_-/dt = Phi_- / tau           [exponential GROWTH]

Full KG+Galley: d^2 Phi_-/dt^2 - (1/tau) dPhi_-/dt - (1/tau^2) Phi_- = 0

| Property | Value |
|:---|:---|
| Growth rate (simple) | 1/tau ~ 0.817 |
| Growth rate (full KG+Galley) | phi/tau ~ 1.321 |
| Kinetic sign | -1 (wrong-sign, ghost) |
| Spatial profile | IC-dependent (NOT geometric) |
| CTP boundary | Phi_-(t_final) = 0 (kills at final time) |

Because the Phi_- spatial profile is initial-condition dependent rather than
sourced by the geometric X = M/r^2 profile, it cannot be treated as an
independently derived geometric Component B carrier.

**Phi_- sector: PATHOLOGICAL.  Ghost, non-geometric, CTP-killed.**

### C2. g_- Sector (Metric-Difference)

The doubled-metric action S_grav = S_EH[g_1] - S_EH[g_2] gives the
linearized g_- sector a wrong-sign Einstein-Hilbert action (gravitational
ghost).  g_- = 0 is a consistent truncation but is expected unstable.

| Property | Value |
|:---|:---|
| Wrong-sign EH | Yes |
| Consistent truncation | Yes (g_- = 0 is a solution) |
| Expected unstable | Yes |
| Energy density scaling | **NOT COMPUTED** |
| Provides 1/r^2 | **UNDETERMINED** |

The g_- energy density has NOT been computed in closed form.  1/r^2 cannot
be ruled out.  This is the key unresolved pre-projection channel.

**g_- sector: UNCOMPUTED AND PROJECTION-SENSITIVE.  Key open residue.**

### C3. S_diss (Dissipative Kernel)

S_diss ~ (Phi_1 - Phi_2) * nabla(Phi_1 + Phi_2) / (2*tau) = Phi_- * Phi_dot_+ / tau

In the physical limit: Phi_- = 0 => S_diss = 0 exactly.
Pre-projection: S_diss inherits Phi_- ghost pathology.

**S_diss: PROJECTION-KILLED.  Vanishes in physical limit.**

---

## D. Candidate Carrier Catalog

| # | Carrier | Type | Scaling | Status |
|:---|:---|:---|:---|:---|
| 1 | Post-projection T^Phi | projected_observable | 1/r^4 | INSUFFICIENT |
| 2 | Phi_- kinetic energy | computed_sector | IC-dependent | PATHOLOGICAL |
| 3 | S_diss energy density | computed_sector | 0 in phys limit | PROJECTION-KILLED |
| 4 | g_- gravitational energy | formal_variation_channel | UNCOMPUTED | UNCOMPUTED + GHOST |
| 5 | delta S / delta g_- | formal_variation_channel | UNCOMPUTED | UNCOMPUTED |

Counts: 0 physical, 1 pathological, 1 projection-killed, 2 uncomputed.
The two formal variation channels (carriers 4 and 5) are the unresolved residue.

---

## E. Obstruction Catalog

| # | Obstruction | Type | Severity |
|:---|:---|:---|:---|
| 1 | Post-projection identity with Route C | structural | **high** |
| 2 | Phi_- wrong-sign kinetic energy | ghost | **high** |
| 3 | CTP boundary kills Phi_- at t_final | projection | medium |
| 4 | g_- wrong-sign Einstein-Hilbert | ghost | **high** |
| 5 | g_- energy density uncomputed | gap | medium |

3 high severity, 2 medium severity.  Obstruction 5 (gap) is the key
barrier to a full no-go.

---

## F. Uncomputed-Sector Barrier

This phase does NOT compute the pre-projection g_- energy density or the
full doubled-metric variation delta S / delta g_-.  Therefore it cannot
return a full Route B no-go.  It can only classify the already-computed
sectors and localize the remaining unknown to the g_- / doubled-metric
channel.

A full Route B no-go would require computing the g_- energy density in
closed form and showing it cannot provide 1/r^2 support.  Until that
computation is done, the g_- sector remains the key unresolved residue.

---

## G. Provisional Classification & Ranking Update

Classification: **route_b_post_projection_insufficient__preprojection_unresolved**

| Channel | Status |
|:---|:---|
| Post-projection T^Phi | **Insufficient** (pure 1/r^4, identical to Route C) |
| Phi_- sector | **Pathological** (ghost, IC-dependent, CTP-killed) |
| S_diss | **Vanishes** in physical limit |
| g_- / doubled-metric | **Unresolved** (uncomputed, key open channel) |

This is a BOUNDED result.  Route B cannot provide Component B through any
computed channel, but the g_- sector is not fully ruled out.

| Route | Previous Status | Current Status |
|:---|:---|:---|
| Route B | Provisional (highest untested) | Post-projection insufficient; pre-projection unresolved |
| Route C | Insufficient within Markov reduction | (unchanged) |
| Route A | Conditional | (unchanged) |

Route B is NOT downgraded to fully closed.  The g_- / doubled-metric channel
remains open as unresolved residue.

---

## H. Numerical Validation

| Quantity | Value |
|:---|:---|
| Post-proj epsilon_RC_coeff | 0.09399 (identical to Route C) |
| deficit_ratio at R_eq | 1.071 (overcovering) |
| deficit_ratio at r=1 | 0.763 (undercovering) |
| Phi_- growth rate (simple) | 1/tau ~ 0.8165 |
| Phi_- growth rate (full) | phi/tau ~ 1.3211 |
| Phi_- decay rate | 1/(phi*tau) ~ 0.5049 |
| Phi_- kinetic sign | -1 (wrong-sign) |
| S_diss at physical limit | 0 (exact) |
| g_- kinetic sign | -1 (wrong-sign EH) |
| g_- energy density | UNCOMPUTED |
| Carriers total | 5 |
| Physical carriers | 0 |
| Uncomputed formal channels | 2 |

Benchmark: 70/70 ALL CHECKS PASSED.
Pytest: 66/66 ALL TESTS PASSED in 0.45s.

---

## I. Nonclaims (10)

1. Post-projection equivalence with Route C applies ONLY to the standard
   minimally-coupled scalar T^Phi form.

2. The Phi_- sector analysis uses the Galley cross-coupled EOMs, NOT
   independent relaxation.

3. The CTP boundary condition Phi_-(t_final) = 0 is a FEATURE of the
   Galley formalism, not a defect.

4. The ghost-like growth in Phi_- at rate phi/tau is a structural feature
   of the Galley CTP encoding of dissipation.  Whether that feature is
   merely formal or physically admissible depends on the projected
   interpretation and is not settled here.

5. The g_- sector has NOT been evaluated for its energy density scaling;
   1/r^2 CANNOT be ruled out there.  This is the key unresolved
   pre-projection channel.

6. This assessment does NOT test whether a non-Galley doubled-field
   construction could avoid the ghost sector.

7. The classification applies to the Galley doubled-field formalism as
   implemented in galley_memory.py and galley_truncation.py.

8. S_diss analysis assumes the observer-flow-projected form.

9. The provisional ranking update is a classification tool, not a prediction.

10. "Ghost-contaminated" means wrong-sign kinetic energy.  Whether this is
    merely a formal property of the CTP encoding or a physical pathology
    depends on the interpretation and is not resolved here.

---

## J. Assumptions (6)

1. Post-projection T^Phi is the standard minimally-coupled scalar form.

2. The physical-limit projection is imposed as constraint, not emergent.

3. Phi_- dynamics follow the Galley cross-coupled EOMs.

4. The equilibrium profile is Phi_eq = X_eq = M/r^2.

5. The Phi_- spatial profile is determined by initial conditions, not by
   the geometric source X = M/r^2.

6. The g_- sector energy density has NOT been computed in closed form.

---

## K. Phase Lock Update

    Phase 6 (Static Interior):      LOCKED (f(R_eq) = -17.71)
    Phase 6B (Dynamical Interior):  LOCKED (A_crit = 1.062, global_robust)
    Phase 6C (Metric Deficit):      LOCKED (epsilon_min two-component)
    Route C Deficit Assessment:     LOCKED (route_c_insufficient_within_markov_reduction)
    Route B Component B Test:       LOCKED (route_b_post_projection_insufficient__preprojection_unresolved)

    Post-projection equivalence:    Route B T^Phi = Route C T^Phi = pure 1/r^4
    Computed pre-projection:        Phi_- pathological, S_diss vanishes
    Unresolved residue:             g_- / doubled-metric (energy density uncomputed)
    General no-go:                  FALSE (uncomputed sector prevents full no-go)
    Provisional ranking:            Route B bounded but g_- channel remains open
