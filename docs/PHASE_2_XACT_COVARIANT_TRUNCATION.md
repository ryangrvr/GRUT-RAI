# Phase 2 xAct Symbolic Offensive — Covariant Truncation / Attractor Analysis

## Status

**CONSISTENT TRUNCATION VERIFIED — IR-DOMINATED INSTABILITY — NOT ATTRACTOR**

Classification: **PHYSICAL-LIMIT CONSISTENT, NOT DYNAMICALLY SELECTED**

Phase 2 extends the Phase 1 result (Delta T = 0, dissipative kernel gravitationally
silent) to the covariant truncation and stability analysis of the Galley doubled-field
system. The principal new result is the dispersion relation for the difference mode
Phi_- = Phi_1 - Phi_2 at arbitrary spatial wavenumber k, establishing that the
instability is IR-dominated: growth rate decreases from phi/tau at k=0 to 1/(2tau) at
k -> infinity. No UV catastrophe. The physical-limit projection Phi_- = 0 is an exact
consistent truncation but is NOT a dynamical attractor — it requires the CTP boundary
condition for enforcement.

This computation was performed using xAct/xPert on Wolfram Engine 14.x. All k=0
results verified against the independent Python analysis in galley_truncation.py.

---

## A. Mission and Context

Phase 1 (grut_tphi_variation.wl) established that the Galley dissipative kernel
L_diss does not contribute to the stress-energy tensor T^Phi_{ab} in the physical
limit. The Factorization Theorem proves this: any Lagrangian of the form
L = (Phi_1 - Phi_2) * F has metric variation proportional to (Phi_1 - Phi_2),
which vanishes at Phi_1 = Phi_2.

The existing Python analysis (galley_truncation.py, 1193 lines) comprehensively
addresses the homogeneous (k=0) case:

- Plus/minus decomposition: Phi_+ = (Phi_1 + Phi_2)/2, Phi_- = Phi_1 - Phi_2
- Consistent truncation: YES (Phi_- = 0 is exact solution, preserved by linearity)
- Attractor: NO (growth rate 1/tau first-order, phi/tau full KG, where phi = golden ratio)
- Classification: IMPOSED (CTP boundary condition, not dynamics)

**What Phase 2 adds**: the fully covariant analysis including spatial gradients (k > 0).
The critical question: does the growing eigenvalue lambda_+(k) increase or decrease
with |k|? If it increases, the instability is UV-catastrophic; if it decreases, the
instability is IR-dominated and potentially regulable.

---

## B. Cross-Coupled First-Order Galley EOMs

From the Galley CTP action S = S_1 - S_2 + S_diss, the first-order cross-coupled
equations of motion are:

    tau u^a nabla_a Phi_1 + Phi_2 = X     (EOM from delta S / delta Phi_-)
    tau u^a nabla_a Phi_2 + Phi_1 = X     (EOM from delta S / delta Phi_+)

Note the cross-coupling: EOM_1 contains Phi_2, EOM_2 contains Phi_1.

Adding the equations:

    tau u^a nabla_a (Phi_1 + Phi_2) + (Phi_1 + Phi_2) = 2X
    => tau u^a nabla_a Phi_+ + Phi_+ = X     (GRUT relaxation law)

Subtracting the equations:

    tau u^a nabla_a (Phi_1 - Phi_2) - (Phi_1 - Phi_2) = 0
    => tau u^a nabla_a Phi_- = Phi_-          (exponential growth)

The plus/minus decomposition completely diagonalizes the first-order system.

---

## C. First-Order Phi_- Equation (Covariant)

**Equation:**

    tau u^a nabla_a Phi_- = Phi_-

**Structure:** This is a transport equation along the flow lines of u^a.
There is no spatial Laplacian. For a scalar field, nabla_a Phi = partial_a Phi
(no Christoffel correction), so u^a nabla_a Phi = dPhi/ds where s is proper
time along u^a.

**Solution:** Phi_-(s) = Phi_-(0) exp(s / tau)

**Growth rate:** 1/tau, along every flow line.

**Spatial modes:** For Phi_-(t, x) = f(x) exp(t/tau), the spatial profile
f(x) is preserved unchanged. The growth rate is universal — independent of the
spatial structure of the perturbation.

**Consistent truncation:** Phi_- = 0 is an exact solution (the equation is
linear homogeneous). VERIFIED by xAct: EOM|_{Phi_-=0} = 0 identically.

**Attractor:** NO. Any nonzero perturbation, no matter how small, grows
exponentially at rate 1/tau.

---

## D. Full KG+Galley Phi_- Equation (Second-Order Covariant)

When the kinetic term -(1/2)(nabla Phi_i)^2 is included in each copy of the
action (with sign flip for copy 2 from the S_1 - S_2 structure), the covariant
second-order equation for Phi_- is:

    Box Phi_- + (1/tau) u^a nabla_a Phi_- + (1/tau^2) Phi_- = 0

where Box = g^{ab} nabla_a nabla_b is the covariant d'Alembertian.

### Sign analysis

| Term | Standard damped KG | Our equation | Interpretation |
|:---:|:---:|:---:|:---:|
| Box Phi | +1 | +1 | Same |
| u^a nabla_a Phi | -1/tau (friction) | +1/tau (anti-friction) | Energy INTO Phi_- |
| mass term | +m^2 | +1/tau^2 | m_eff^2 = -1/tau^2 < 0 (tachyonic) |

**Sign subtlety:** The action S = S_1 - S_2 flips the kinetic sign for copy 2.
In the EOM for Phi_2, the d'Alembertian appears with a minus sign:
-Box Phi_2 + V'(Phi_2) - ... = 0. When we subtract EOMs to get the Phi_-
equation, this sign flip converts the damping term into anti-damping and
changes the sign of the effective mass squared.

### Verification

In the rest frame of u^a with homogeneous field (k=0), Box -> -d^2/dt^2 and
u^a nabla_a -> d/dt, giving:

    -d^2Phi_-/dt^2 + (1/tau) dPhi_-/dt + (1/tau^2) Phi_- = 0

Multiply by -1:

    d^2Phi_-/dt^2 - (1/tau) dPhi_-/dt - (1/tau^2) Phi_- = 0

This matches the Python result in galley_truncation.py exactly.

**Consistent truncation:** EOM|_{Phi_-=0} = 0 identically (VERIFIED by xAct).

---

## E. Dispersion Relation — THE KEY NEW RESULT

Plane-wave ansatz in the rest frame of u^a:

    Phi_- ~ exp(lambda t + i k . x)

In the rest frame (u^a = (1,0,0,0), Minkowski background):

    Box Phi_- = (-lambda^2 - |k|^2) Phi_-
    u^a nabla_a Phi_- = lambda Phi_-

Substituting into the covariant equation:

    (-lambda^2 - |k|^2) + lambda/tau + 1/tau^2 = 0

**Dispersion relation:**

    lambda^2 - lambda/tau + (|k|^2 - 1/tau^2) = 0

**Roots:**

    lambda_+/- = (1/tau +/- sqrt(5/tau^2 - 4|k|^2)) / 2

**Discriminant:**

    Delta = 5/tau^2 - 4|k|^2

### k = 0 verification (golden ratio)

At k = 0: lambda^2 - lambda/tau - 1/tau^2 = 0

Substituting mu = lambda * tau: mu^2 - mu - 1 = 0

Roots: mu = (1 +/- sqrt(5)) / 2

    lambda_+(0) = phi / tau     where phi = (1 + sqrt(5))/2 = 1.618...
    lambda_-(0) = -1 / (phi * tau)

VERIFIED by Mathematica: exact symbolic match. The growing eigenvalue at k=0
is phi/tau (golden ratio divided by tau), matching the Python result.

### Critical wavenumber

    k_c = sqrt(5) / (2 tau) = 1.118... / tau

At k = k_c, the discriminant vanishes: degenerate eigenvalue lambda = 1/(2tau).

### Three regimes

**Regime I: |k| < k_c (long wavelengths)**

Two real eigenvalues. The growing mode:

    lambda_+(k) = (1/tau + sqrt(5/tau^2 - 4|k|^2)) / 2

Growth rate decreases monotonically with |k|:

| k * tau | lambda_+ * tau |
|:---:|:---:|
| 0 | 1.618 (golden ratio) |
| 0.25 | 1.590 |
| 0.50 | 1.500 |
| 0.75 | 1.329 |
| 1.00 | 1.000 |
| k_c = 1.118 | 0.500 (degenerate) |

**Regime II: |k| = k_c (critical wavelength)**

Degenerate: lambda = 1 / (2 tau). Single repeated eigenvalue.

**Regime III: |k| > k_c (short wavelengths)**

Complex conjugate eigenvalues:

    lambda = 1/(2 tau) +/- i sqrt(4|k|^2 - 5/tau^2) / 2

The modes oscillate, but the envelope STILL GROWS. The real part is:

    Re(lambda) = 1 / (2 tau) > 0     for all k

The oscillation frequency increases without bound as k -> infinity, but the
growth rate is locked at 1/(2 tau).

### Summary of dispersion

    Max growth rate:   phi/tau  = 1.618/tau     (at k = 0)
    Min growth rate:   1/(2tau) = 0.500/tau     (at k -> infinity)
    All modes grow:    Re(lambda) > 0 for ALL k
    IR-dominated:      growth rate DECREASES with |k|
    NOT UV-catastrophic: no gradient instability

---

## F. Instability Classification

| Property | Status | Evidence |
|:---:|:---:|:---:|
| Tachyon | YES | m_eff^2 = -1/tau^2 < 0 |
| Ghost | YES | Wrong-sign kinetic from S_1 - S_2 |
| Anti-damped | YES | +1/tau coefficient on u.nabla (energy inflow) |
| UV-catastrophic | NO | Growth rate decreases with k (IR-dominated) |
| CTP artifact | YES | All pathologies from doubled-field construction |
| Removed by physical limit | YES | Phi_- = 0 boundary condition eliminates sector |

**Combined classification:** Ghost-tachyon CTP artifact, IR-dominated, removed
by physical-limit boundary projection.

The ghost-tachyon pathology of the Phi_- sector is a construction artifact of
the Galley CTP formalism. It encodes the time-asymmetry (arrow of time)
needed for the dissipative EOM. The doubled fields carry this information, and
the physical-limit projection Phi_1 = Phi_2 discards it after the variational
principle has done its work.

---

## G. Consistent Truncation Verification

The Phi_- equation L[Phi_-] = 0 is linear homogeneous, where:

    L = Box + (1/tau) u^a nabla_a + 1/tau^2

Since L is a linear operator with no source term:

1. Phi_- = 0 is an exact solution (L[0] = 0 identically)
2. The truncation is EXACT, not approximate
3. The Phi_+ equation decouples completely from Phi_-
4. The GRUT relaxation law tau u^a nabla_a Phi + Phi = X is recovered exactly

Verified by xAct substitution: both first-order and full KG equations vanish
identically at Phi_- = 0.

**Attractor status:** The linearized equation has Re(lambda) > 0 for ALL spatial
modes. Phi_- = 0 is an UNSTABLE fixed point. Any perturbation grows.

- First-order growth rate: 1/tau (universal)
- Full KG maximum rate: phi/tau (at k = 0)
- Full KG minimum rate: 1/(2tau) (at k -> infinity)

**Classification:** Consistent truncation, NOT an attractor. The physical limit
Phi_1 = Phi_2 is maintained by the CTP BOUNDARY CONDITION, not by attractive
dynamics.

---

## H. Phi_+ Equation (GRUT Relaxation Law Recovery)

For completeness, the physical-mode equation:

**First-order:**

    tau u^a nabla_a Phi_+ + Phi_+ = X

This IS the GRUT relaxation law, recovered exactly in the physical limit.

**Full KG (second-order):**

    Box Phi_+ + (1/tau) u^a nabla_a Phi_+ - Phi_+/tau^2 + X/tau = 0

Note the OPPOSITE signs compared to Phi_-: the u^a nabla_a term provides
DAMPING (standard sign), and the mass term has the correct physical sign.
The physical mode relaxes to the equilibrium X with damping rate 1/tau.

This asymmetry between Phi_+ (damped) and Phi_- (anti-damped) is the core
mechanism of the Galley formalism: dissipation is encoded as energy flow from
Phi_+ into Phi_-, with the CTP boundary condition preventing Phi_- from
accumulating the leaked energy.

---

## I. Phase 1 Result Lock

Phase 1 results are hereby LOCKED within the stated scope:

1. **Delta T = 0**: The metric variation and physical-limit projection commute.
   The dissipative kernel L_diss does NOT contribute to T^Phi_{ab} in the
   physical limit. VERIFIED by xPert computation (Route 1 = Route 2).

2. **Factorization Theorem**: Any Lagrangian L = (Phi_1 - Phi_2) * F has metric
   variation delta L / delta g^{ab} proportional to (Phi_1 - Phi_2), which
   vanishes at Phi_1 = Phi_2. VERIFIED analytically and computationally.

3. **T^Phi = standard minimally-coupled scalar**: nabla_a Phi nabla_b Phi
   - g_{ab}[(1/2)(nabla Phi)^2 + V - Phi J]. No dissipative correction.

These results hold for the scalar sector in the physical limit. They do NOT
address the metric perturbation sector (g_-), which remains OPEN.

---

## J. Remaining Obstructions (Ranked)

1. **Physical-limit projection is imposed, not emergent** — PRECISELY LOCALIZED.
   The CTP boundary condition Phi_- = 0 is mathematically consistent but not
   dynamically selected. This is the core Route B obstruction.

2. **Metric sector (g_-) unanalyzed** — OPEN. The doubled metric perturbation
   h_- = h_1 - h_2 has not been studied. The ghost/truncation analysis applies
   only to the scalar sector.

3. **CTP sufficiency as a derivation** — OPEN (mathematical physics question).
   Whether the CTP boundary condition constitutes a "derivation" of the physical
   limit is definitional, not computational.

4. **Nonlinear stability** — NOT ADDRESSED. The truncation and attractor analysis
   is linear. Nonlinear coupling between Phi_+ and Phi_- at higher order is not
   examined.

5. **Curved-background corrections** — EXPECTED SMALL. The dispersion analysis
   uses a Minkowski rest frame. Curvature corrections to the dispersion relation
   enter at order R * tau^2 and are suppressed when tau << L_curvature.

---

## K. Explicit Nonclaims

1. The physical limit Phi_1 = Phi_2 is a consistent truncation but NOT a
   dynamical attractor of the doubled system

2. The ghost-tachyon instability of Phi_- is a FEATURE of the CTP construction,
   not a pathology requiring resolution within the physical theory

3. The dispersion relation lambda^2 - lambda/tau + (k^2 - 1/tau^2) = 0 is
   derived in the rest frame of u^a on a Minkowski background; curved-background
   corrections are NOT computed

4. Route B does NOT upgrade from "physical-limit derived" to "derived" as a
   result of this analysis

5. The IR-dominated character of the instability does NOT make it "safe" — it
   means short-wavelength modes do not grow faster than long-wavelength modes,
   which is a structural property, not a stability guarantee

6. The Phi_+ (physical mode) damping and Phi_- (ghost mode) anti-damping are
   NOT independent phenomena; they are the same energy flow seen from opposite
   sides of the CTP construction

7. The golden ratio eigenvalue phi/tau at k=0 is NOT a deep physical result;
   it is an algebraic consequence of the specific cross-coupling structure
   tau u.nabla Phi_1 + Phi_2 = X with equal coefficients

8. The metric perturbation sector (g_-) is UNDETERMINED — the scalar-sector
   results do NOT extend automatically to the metric sector

9. The xAct computation verifies consistency of the analytical derivation but
   does NOT independently derive the covariant equation from the doubled action
   (the equation is constructed, then verified for truncation properties)

10. The "anti-damping" interpretation assumes a definite arrow of time aligned
    with u^a; in the full CTP formalism, both time directions are present
    until the physical-limit projection selects one

11. Nonlinear Phi_+ / Phi_- coupling is NOT analyzed; the truncation analysis
    is strictly linear

12. This analysis LOCALIZES but does not RESOLVE the Route B obstruction: the
    physical limit is consistent but externally imposed

---

## Computational Artifacts

**Script:** xact/grut_truncation_covariant.wl (Parts A-H)
**Engine:** Wolfram Engine 14.x with xAct 1.2.0 / xPert 1.0.6
**Method:** xPert Perturbation (VarD broken on Wolfram Engine 14.x, see vard_diagnostic.wl)
**Exports:** xact/results/dispersion_relation.m, instability_classification.m,
phi_minus_first_order.m, phi_minus_kg.m
**Python cross-check:** galley_truncation.py (k=0 eigenvalues, characteristic equation)

---

## Status Implications

    Phase 1 (T^Phi):           LOCKED (Delta T = 0)
    Consistent truncation:     LOCKED (exact, by linearity)
    Attractor:                 LOCKED (NO, all modes grow)
    UV behavior:               LOCKED (IR-dominated, NOT catastrophic)
    Dispersion relation:       LOCKED (new result, verified at k=0)
    CTP sufficiency:           OPEN (mathematical physics question)
    Metric sector (g_-):       OPEN (not addressed)

    Route B overall:           physical-limit derived, NOT fully derived
    Obstruction #5:            PRECISELY LOCALIZED
      (physical limit is consistent but not dynamically selected)
