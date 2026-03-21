# Source-Law Program I — Exploit Loophole 5 (X != M/r^2)

## A. Mission & Context

All kernel-based classical routes to Component B have been exhausted:

| Phase | Result | Status |
|-------|--------|--------|
| Phase 6 | f(R_eq) = -17.71 | LOCKED |
| Phase 6B | A_crit = 1.062 | LOCKED |
| Phase 6C | epsilon_min = Component A (1/r^4) + Component B (1/r^2) | LOCKED |
| Route C (Markov) | epsilon_RC ~ 1/r^4 only | LOCKED (insufficient) |
| Route B (all channels) | Closed within Galley CTP | LOCKED |
| Route C (non-Markov) | Source profile locking: 1/r^4 for ANY kernel | LOCKED |

**Loophole 5** from `route_c_deficit.py` — modified source law X != M/r^2 — is the **only remaining classical loophole** (severity: HIGH).

**Mission**: Test whether any GRUT-native source-law modification can generate the missing 1/r^2 Component B support.

---

## B. Target Definition

The memory equation locks the energy density spatial profile to the source:

    tau * dPhi/dt + Phi = X(r)

For step turn-on A(t) = A_crit * theta(t):

    Phi_dot(t,r) = (A_crit / tau) * S(r) * exp(-t/tau)
    epsilon(t,r) = (1/2) * Phi_dot^2 = (A_crit^2 / (2*tau^2)) * S(r)^2 * exp(-2t/tau)

where S(r) is the spatial profile of the source X.

**Standard source**: X = M/r^2 gives S(r) = M/r^2 and epsilon ~ 1/r^4.

**Target**: Need S(r) ~ 1/r to get epsilon ~ 1/r^2 (Component B).

Component B coefficient: 1/(8*pi) ~ 0.03979.

---

## C. Diagnostic Toy Probe

**Probe**: X = M/r^2 + B/r with B = 0.1 (NOT canon, diagnostic only).

**Result**: epsilon = (A^2/(2*tau^2)) * (M/r^2 + B/r)^2

Expanding:
- M^2/r^4 term (Component A)
- 2*M*B/r^3 term (cross-coupling, intermediate)
- B^2/r^2 term (Component B)

Fitted exponents:
- Inner region: ~ -3.74 (1/r^4 dominated)
- Outer region: ~ -3.19 (approaching 1/r^2)
- Full range: ~ -3.50 (mixed)

**Conclusion**: The mechanism works. A 1/r source term produces a 1/r^2 contribution to epsilon. The probe confirms the computational framework.

**Caveat**: The B/r term is inserted by hand. The question is whether any GRUT-native mechanism provides it.

---

## D. Family 1: Local Algebraic Correction

**Formula**: X = (M/r^2)^p with F(Phi) = Phi^{p-1}

The equilibrium field Phi_eq = M/r^2 maps to X = (M/r^2)^p = M^p / r^{2p}.

| Power p | Source exponent | Epsilon exponent | Status |
|---------|----------------|------------------|--------|
| 1.00 | -2.00 | -4.00 | Standard (locked) |
| 0.75 | -1.50 | -3.00 | Intermediate |
| 0.50 | -1.00 | -2.00 | TARGET |
| 0.25 | -0.50 | -1.00 | Too shallow |

**p = 1/2 achieves the target exactly**: X = sqrt(M)/r gives epsilon ~ 1/r^2.

**Obstruction**: F(Phi) = Phi^{-1/2} is singular at Phi = 0. This self-coupling has no derivation from the canonical GRUT Lagrangian.

**Verdict**: Mathematically viable. Not GRUT-native.

---

## E. Family 2: Gradient/Derivative Correction

**Formula**: X = M/r^2 + alpha * d/dr(M/r^2) + beta * d^2/dr^2(M/r^2)

Derivatives of M/r^2:
- d/dr(M/r^2) = -2M/r^3 (exponent -3, STEEPER)
- d^2/dr^2(M/r^2) = 6M/r^4 (exponent -4, STEEPER STILL)

All spatial derivatives of M/r^2 produce terms with exponents <= -3. No combination of derivatives can produce a 1/r term.

**Structural result**: Gradient corrections can only make the source profile steeper, not shallower.

**Verdict**: STRUCTURALLY CLOSED. No parameter choice can produce 1/r.

---

## F. Family 3: Cumulative/Integral Source

**Formula**: X = M/r^2 + lambda * integral_{r_min}^r dr' (M/r'^2)

The integral evaluates to:

    integral_{r_min}^r dr' (M/r'^2) = M * (1/r_min - 1/r)

This contains two terms:
- **-M/r**: a 1/r contribution (desirable)
- **M/r_min**: a constant offset (contaminant)

With lambda = 0.3 and r_min = 0.1:
- 1/r coefficient: lambda * M = 0.15
- Constant offset: lambda * M / r_min = 1.5

The constant offset overwhelms the 1/r term at all radii, driving the effective epsilon exponent to ~ -0.56 (far shallower than -2.0).

**Verdict**: Contains the needed 1/r contribution but is fatally contaminated by a constant offset. Not GRUT-native in the source coupling.

---

## G. Family 4: Defect/Topological Source

**Formula**: X = M/r^2 + Q/r

A charge-like 1/r source from a topological defect. The epsilon profile:

    epsilon = (A^2/(2*tau^2)) * (M/r^2 + Q/r)^2
            = (A^2/(2*tau^2)) * [M^2/r^4 + 2MQ/r^3 + Q^2/r^2]

The Q^2/r^2 term is exactly Component B with coefficient:

    (A_crit^2 / (2*tau^2)) * Q^2

For Q = 0.1: Component B coefficient = 0.003759 (target: 0.03979). Would need Q ~ 0.325 to match.

**Pure Q/r epsilon exponent**: -2.0000 (exact target).

**Full profile**: mixed 1/r^4 + 1/r^3 + 1/r^2, with effective exponent ~ -3.50 across the full radial range.

**Obstruction**: No topological charge Q is currently defined in the canonical GRUT framework. Such a charge might arise from boundary conditions, winding numbers, or a conserved Noether current.

**Verdict**: Mathematically cleanest route to Component B. Not GRUT-native (no known Q).

---

## H. Family 5: Processing/Lag-Invariant Source

**Formula**: X = G(Phi_eq, Phi_dot_eq, memory_integrals)

At equilibrium:
- Phi_dot = 0
- Memory integrals reduce to functions of Phi_eq = M/r^2

Therefore G(M/r^2, 0, f(M/r^2)) = g(M/r^2), which is a local algebraic function of M/r^2 — identical to Family 1.

**Source exponent**: -2.00 (standard, p=1 collapse)
**Epsilon exponent**: -4.00 (standard)

**Verdict**: Collapses to Family 1 at equilibrium. No independent spatial structure.

---

## I. Source Family Taxonomy & Ranking

| Rank | Family | Epsilon exp. | Deviation | Viable? | GRUT-native? |
|------|--------|-------------|-----------|---------|-------------|
| 1 | Local algebraic (p=0.5) | -2.00 | 0.00 | YES | NO |
| 2 | Cumulative/integral | -0.56 | 1.44 | NO (contaminated) | NO |
| 3 | Defect/topological | -3.50 (full); -2.00 (pure Q/r) | 1.50 (full) | YES | NO |
| 4 | Gradient/derivative | -3.85 | 1.85 | NO (closed) | YES |
| 5 | Processing-invariant | -4.00 | 2.00 | NO (collapses) | YES |

Two families are viable (can produce 1/r^2 epsilon): Family 1 (algebraic, p=1/2) and Family 4 (defect, Q/r). Neither is GRUT-native.

---

## J. GRUT-Nativeness Assessment

| Family | Viability | GRUT-native? | Obstruction |
|--------|-----------|-------------|-------------|
| 1 (algebraic) | Viable | NO | Requires singular F(Phi) = Phi^{-1/2} |
| 2 (gradient) | Closed | YES | Structurally steepens profile |
| 3 (integral) | Contaminated | NO | Non-local source coupling + constant offset |
| 4 (defect) | Viable | NO | No topological charge Q in canonical GRUT |
| 5 (processing) | Collapses | YES | Reduces to Family 1 at equilibrium |

**Overall**: No GRUT-native mechanism found. The two GRUT-native families (gradient, processing) are either structurally closed or redundant. The two viable families (algebraic, defect) require non-standard extensions.

**Recommended next step**: Identify whether a topological charge Q can emerge from the GRUT field equations under appropriate boundary conditions, or whether a curvature-scalar coupling R*Phi produces an effective 1/r source.

---

## K. Final Classification & Phase Lock Update

**Classification**: `source_law_loophole_5_partially_viable__no_grut_native_mechanism`

**Loophole 5 status**: PARTIALLY VIABLE

The mechanism for producing Component B through modified source laws is mathematically sound:
- X ~ 1/r produces epsilon ~ 1/r^2 (confirmed by diagnostic probe and Family 1/4 analysis)
- The missing ingredient is a GRUT-native source deformation that provides the 1/r term

**Phase lock update**:

| Phase | Status |
|-------|--------|
| Phase 6: f(R_eq) | LOCKED (-17.71) |
| Phase 6B: A_crit | LOCKED (1.062) |
| Phase 6C: deficit | LOCKED (Component A + Component B) |
| Route C (Markov) | LOCKED (insufficient, 1/r^4) |
| Route B (all channels) | LOCKED (closed within Galley CTP) |
| Route C (non-Markov) | LOCKED (source profile locking, 1/r^4) |
| **Loophole 5 (source law)** | **TESTED (partially viable, no GRUT-native mechanism)** |

---

## L. Numerical Validation Summary

- Benchmark: **58/58 checks PASSED**
- Pytest: **57/57 tests PASSED** (0.34s)
- All power-law exponents match analytical predictions to machine precision
- Diagnostic probe decomposition (Component A + cross + Component B) verified against exact coefficients
- Family 2 closure confirmed: all derivative exponents <= -3.0

---

## M. Nonclaims (10)

1. This phase does NOT prove that Loophole 5 is physically closed. It maps which source families CAN produce 1/r and assesses their GRUT-nativeness, but does not prove uniqueness of X = M/r^2.
2. The diagnostic toy probe X = M/r^2 + B/r is NOT a physical proposal. It is a computational test only.
3. The classification 'no GRUT-native mechanism' does NOT mean no mechanism exists. It means none was found within the 5 tested families.
4. Family 1 (algebraic with p=1/2) is NOT declared singular in all formulations. Alternative regularizations might exist.
5. Family 3 (integral) is NOT declared contamination-free. The constant offset might be absorbable in a proper formulation.
6. Family 4 (defect) is NOT declared non-GRUT. A topological charge might emerge from appropriate boundary conditions.
7. No family cross-coupling is tested.
8. The 'partially viable' classification does NOT constitute a construction of the missing source.
9. Exponent fits use log-log regression over a finite radial range.
10. This phase does NOT address whether the modified source law preserves the Einstein equations or TOV structure.

---

## N. Assumptions (10)

1. Memory equation tau * dPhi/dt + Phi = X(r) with spatial profile locked by S(r).
2. Energy density epsilon = (A_crit^2 / (2*tau^2)) * S(r)^2 for step turn-on.
3. Standard source X = M/r^2 giving epsilon ~ 1/r^4 (locked baseline).
4. Component B target: 1/(8*pi*r^2) requires S(r) ~ 1/r.
5. Source families tested at equilibrium field values.
6. Diagnostic probe used only for framework validation, not promoted to canon.
7. GRUT-nativeness requires derivation from canonical GRUT Lagrangian without new free parameters.
8. Background metric and mass profile held fixed (no back-reaction).
9. Each source family tested independently (no cross-family combinations).
10. Classification within tested source families only (non-classical sources outside scope).
