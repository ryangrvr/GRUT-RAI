# Phase VII — Testing EOS / Potential Closure from beta_Q

## A. Mission and Context

Phase VI established the Equilibrium Source Degeneracy Theorem: self-healing
(X - Phi = 0) removes source-level dynamical sensitivity to the action's free
functions at equilibrium.  At least one additional closure input is required
(V(Phi), EOS, propagation equation, or off-equilibrium data), but Phase VI
did NOT determine whether any single proposed input is generically sufficient.

Phase VII tests one specific closure hypothesis: can the GRUT stiffness
exponent beta_Q be consistently mapped to an effective barrier equation of
state w_Phi and then to a scalar potential V(Phi)?

Phase VII does NOT derive an equation of state.  It classifies the conditional
mapping and identifies structural obstructions.

## B. What beta_Q Actually Is

beta_Q is a compactness-dependent barrier steepness exponent.  It is NOT an
EOS exponent.  It enters the barrier dynamics through four exact relations:

| Relation | Formula | Status |
|----------|---------|--------|
| Endpoint law | R_eq/r_s = epsilon_Q^{1/beta_Q} | EXACT |
| Barrier acceleration | a_Q = a_grav x epsilon_Q x (r_s/R)^{beta_Q} | EXACT |
| Natural frequency | omega_0^2 = beta_Q * omega_g^2 | EXACT |
| Barrier-to-gravity ratio | Phi_barrier/Phi_grav = 1/(1 + beta_Q) | EXACT |

All four are barrier-geometry relations, not fluid EOS relations.  The
identification of beta_Q with an EOS parameter requires additional
assumptions that are not part of the core GRUT framework.

## C. Conditional Mapping Sequence

The mapping from beta_Q to w_Phi is a 5-step mapping-and-block structure,
NOT a fully forward derivation chain.  Steps 2-4 are conditional; step 5
is a terminal anisotropy block.

| Step | Input | Output | Exact? | Route-Specific? | Type |
|------|-------|--------|--------|-----------------|------|
| 1 | beta_Q | omega_0^2 = beta_Q * omega_g^2 | **Yes** | No | Forward (exact) |
| 2 | omega_0^2 | m^2 = 1/tau^2 | **No** | Yes (Route A) | Forward (conditional) |
| 3 | m^2 | V(Phi) = Phi^2/(2 tau^2) | **No** | Yes (Route A) | Forward (conditional) |
| 4 | V(Phi) + canonical kinetic | w_Phi = -1 at equilibrium | **No** | Yes (Route A) | Forward (conditional) |
| 5 | single w_Phi | BLOCKED for collapse sector | **Yes** | No | Terminal block |

Step 1 is exact and route-independent.  Steps 2-4 each introduce additional
assumptions (KG mass identification, canonical quadratic potential, isotropy
at equilibrium).  Step 5 is an exact structural observation: the collapse
sector is anisotropic, so a single w_Phi cannot close it.

The sequence carries explicit conditionality flags: is_conditional=True,
requires_route_a=True, requires_isotropy=True, valid_for_collapse=False,
unique=False.

## D. Anisotropy Block

The barrier stress-energy tensor has different symmetry in the two sectors:

- **Cosmological (FRW) sector**: isotropic.  T^Phi takes perfect-fluid form
  T^Phi_mu_nu = (rho + p) u_mu u_nu + p g_mu_nu.  A single w_Phi is
  sufficient.

- **Collapse (spherical) sector**: anisotropic.  T^Phi_mu_nu =
  diag(-rho_Phi, p_r, p_t, p_t) with p_r != p_t in general.  A single
  w_Phi is NOT sufficient; one needs (w_r, w_perp).

This anisotropy is a hard structural block on any single-w_Phi EOS closure
for the collapse sector.  Sources: memory_tensor.py lines 56-58, 264,
320-330, 349.

## E. Candidate V(Phi) and Degeneracy Reduction

V(Phi) = Phi^2/(2 tau^2) is the KG Route A candidate.  It is NOT derived
from beta_Q alone.  It requires three additional identifications:

1. Route A / Klein-Gordon overdamped identification
2. Canonical kinetic structure: -(1/2) g^ab nabla_a Phi nabla_b Phi
3. Mass-term identification: m^2 = 1/tau_eff^2

This potential is NOT unique: other forms (quartic, polynomial,
non-polynomial, hyperbolic) are equally compatible with existing GRUT
constraints.

Specifying V(Phi) reduces Route A from 2 free functions (V, J) to 1 (J
still free).  Routes B (K_diss, L) and C (kernel K) are NOT affected.

The Phase VI equilibrium source degeneracy is NOT broken: the source
equation 0 = 0 at equilibrium holds regardless of V because self-healing
(X - Phi = 0) makes the source term vanish independent of V.

Classification: partially_closing.

## F. NEC Compatibility

w_Phi = -1 at equilibrium implies rho + p = 0 (NEC-saturating).  This is
marginally on the NEC boundary, neither violating nor satisfying with a
definite sign.

Phase V indicated NEC violation at the constitutive level for sub-horizon
barrier support.  The candidate w = -1 at equilibrium does not conflict
with this: the violation can occur off-equilibrium or through anisotropic
components.

**Explicit scope:** This NEC check applies ONLY to the isotropic Route A
candidate closure.  It does NOT constitute a full anisotropic collapse-sector
NEC analysis, which would require separate rho + p_r and rho + p_perp
conditions.

## G. Lapse Impact

The EOS/potential closure does NOT improve lapse determination.

The Phase V obstruction (A_eff < 0 for every finite beta_Q > 0) is
structural: it stems from T^Phi being constitutive/effective rather than
Lagrangian-derived.  Specifying V(Phi) does not change this because:
(1) T^Phi remains constitutive in the existing framework,
(2) V(Phi) alone does not determine a complete coupled Einstein-scalar
system, and (3) the source coupling J remains free.

## H. Status Ladder Update

| Level | Phase VI | Phase VII | Changed? |
|-------|----------|-----------|----------|
| 1 | exact | exact | No |
| 2 | constitutive_derived | constitutive_derived | No |
| 3 | constitutive_lapse_promotion_obstructed | constitutive_lapse_promotion_obstructed | No |
| T^Phi | schematic_effective_equilibrium_degenerate | schematic_effective_equilibrium_degenerate | No |

No level changed.  No level weakened.  T^Phi was already sharpened in
Phase VI; Phase VII adds sub-classifications (eos_closure =
admissible_but_nonunique, degeneracy = partially_closing) but does not
change the main T^Phi characterization.

## I. Phase VI Reconfirmation

All Phase VI results survive Phase VII:

- Equilibrium Source Degeneracy Theorem: PRESERVED.
- T^Phi Underdetermination (Levels A and B): PRESERVED.
- Route Assessment (4 routes): PRESERVED.
- Admissibility Conditions: PRESERVED.
- Status Ladder: PRESERVED.
- Phase V Results: PRESERVED.

Phase VII adds new results but does NOT invalidate any Phase VI or
Phase V result.

## J. Answers to Primary Questions

**Q1.** Is beta_Q even interpretable as an EOS scaling exponent?
Conditionally, under stated assumptions, but it is fundamentally a barrier
steepness exponent, NOT an EOS exponent.

**Q2.** Does the mapping require isotropy or perfect-fluid closure?
Yes.  The single-w_Phi interpretation requires isotropy (perfect-fluid
form), which is valid only for the cosmological sector.

**Q3.** If the barrier sector is anisotropic, do we need w_r and w_perp?
Yes.  The collapse sector is anisotropic: T^Phi = diag(-rho, p_r, p_t, p_t)
with p_r != p_t.  A single w_Phi is structurally insufficient.

**Q4.** Under what field assumptions does w_Phi determine V(Phi)?
Under KG Route A identification + canonical kinetic structure + mass-term
identification m^2 = 1/tau^2 + isotropy + equilibrium evaluation.  The
candidate V(Phi) = Phi^2/(2 tau^2) is NOT derived from beta_Q alone.

**Q5.** Does V(Phi) reduce the degeneracy, or actually break it?
V(Phi) partially reduces Route A (2 free -> 1 free, J remains) but does
NOT break the full degeneracy.  Routes B and C are unaffected.  The
Phase VI source degeneracy is NOT broken.

**Q6.** Does the resulting closure conflict with Phase V NEC indication?
No.  w = -1 implies rho + p = 0 (NEC-saturating), which does not conflict
with the constitutive NEC violation.  Scope: isotropic Route A only; NOT
a full anisotropic collapse NEC analysis.

**Q7.** Does this closure improve the interior metric/lapse problem?
No.  The Phase V lapse obstruction persists unchanged.  Specifying V does
not resolve the structural issue of T^Phi being constitutive/effective.

## K. Nonclaims

1. Phase VII does NOT derive an EOS for the barrier sector from beta_Q.
2. beta_Q is a barrier steepness exponent, NOT an EOS exponent.
3. The conditional mapping beta_Q -> w_Phi exists ONLY under KG Route A
   + canonical kinetic term + isotropy.
4. The collapse sector is anisotropic: a single w_Phi is insufficient.
5. V(Phi) = Phi^2/(2 tau^2) is one admissible potential; it is NOT unique.
6. Other V(Phi) forms are equally compatible with existing constraints.
7. V(Phi) reduces Route A free functions but does NOT break full degeneracy.
8. Routes B and C are NOT affected by specifying V(Phi).
9. The equilibrium source degeneracy (Phase VI) is NOT broken by V.
10. w_Phi = -1 at equilibrium is NEC-saturating, compatible with Phase V
    NEC indication.  This check applies only to isotropic Route A, NOT a
    full anisotropic collapse-sector NEC analysis.
11. V(Phi) is NOT derived from beta_Q alone; it requires Route A/KG +
    canonical kinetic + mass-term identification m^2 = 1/tau^2.
12. The EOS/potential closure does NOT improve lapse determination.
13. No Phase VI result weakened or invalidated.
14. No observational predictions changed.
15. Classification: admissible_but_nonunique / partially_closing.

## L. What Would Further Resolve

To further constrain or determine the barrier action and its T^Phi:

1. Off-equilibrium dynamical data (quasi-normal mode observations) to probe
   away from the degenerate equilibrium point.

2. An independent derivation of V(Phi) from first principles (not assuming
   a specific route a priori).

3. A full anisotropic closure for the collapse sector, providing both
   w_r and w_perp (or equivalently, separate EOS for radial and tangential
   pressures).

4. A covariant propagation equation for Phi that lifts the first-order
   constitutive ODE to a second-order covariant field equation.

5. Gravitational coupling resolution for Route B (Galley doubled-field),
   which is the strongest action-based candidate but lacks implemented
   gravity coupling.

Until these are provided, the barrier action remains underdetermined and
T^Phi remains schematic/effective.
