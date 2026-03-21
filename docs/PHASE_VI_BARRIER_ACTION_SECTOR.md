# Phase VI — Covariant Barrier Action Sector

## A. Mission and Context

Phase V proved the Constitutive Lapse Insufficiency Theorem: A_eff < 0 for
every finite beta_Q > 0, establishing that the naive constitutive
post-Newtonian lapse identification fails universally.  Phase V also
identified the structural blocker: T^Phi is schematic/effective (not
Lagrangian-derived), making the interior metric underdetermined.

Phase VI attempts the next honest escalation: determine whether current GRUT
primitives can support a minimal covariant barrier action.

## B. Admissibility Conditions

Any barrier-sector action must satisfy six conditions:

| # | Condition | Required By |
|---|-----------|-------------|
| 1 | General covariance (diffeomorphism invariance) | General relativity |
| 2 | Stress-energy derivability: T^Phi = (-2/sqrt(g)) delta(S)/delta(g^{mu nu}) | Variational principle |
| 3 | Combined conservation: nabla_mu(T^{mu nu} + T^{Phi mu nu}) = 0 | Bianchi identity |
| 4 | Spherical symmetry compatibility | GRUT endpoint geometry |
| 5 | Equilibrium compatibility: admits R_eq/r_s = epsilon_Q^{1/beta_Q} | GRUT endpoint law |
| 6 | Constitutive limit: recovers tau dPhi/dt + Phi = X | GRUT memory equation |

## C. Route Assessment

Four action routes assessed against six criteria:

| Criterion | Route A (KG) | Route B (Galley) | Route C (Nonlocal) | Route D (Auxiliary) |
|-----------|-------------|-----------------|-------------------|-------------------|
| Action-based | Yes | Yes | Yes | **No** (non-action closure) |
| Covariant | Yes | Yes | Yes | Yes (by construction) |
| Reproduces constitutive limit | Approximate (overdamped) | Exact (physical limit) | Exact (exponential kernel) | Exact (by construction) |
| Gravity coupling resolved | Formal minimal coupling | **Not resolved** | Formal (retarded kernel) | By construction |
| Uniquely determined by GRUT | **No** | **No** | **No** | N/A |
| Requires extra postulate | V(Phi) + J | K_diss + L_nondiss | Full kernel beyond exponential | N/A |

Route B (Galley doubled-field) is formally the strongest action-based
candidate: it produces the first-order dissipative ODE exactly.  However, its
gravity coupling has not been implemented, and K_diss and L are free.

Route D is a non-action closure route, outside the present phase target.
It is NOT "inadmissible" in the sense of physically failing; it simply does
not answer the action question.

No action-based route is fully determined by current GRUT primitives.

## D. Equilibrium Source Degeneracy Theorem

**Theorem.** For any admissible barrier-sector action that reproduces the
constitutive memory equation in the appropriate limit and admits the GRUT
equilibrium endpoint, the self-healing equilibrium condition X - Phi = 0
removes source-level dynamical sensitivity to the action's free functions
in the first-order memory equation.  Therefore the equilibrium constitutive
primitives alone do not identify a unique barrier action.

**Proof** (6 steps).

1. At GRUT equilibrium: Phi_eq = X_eq (memory fully relaxed to source,
   force balance).
2. Source functional: X - Phi = 0 at equilibrium (self-healing, established
   in Phase IV).
3. All admissible actions reproduce the constitutive memory ODE
   tau dPhi/dt + Phi = X; at equilibrium, this reduces to 0 = 0 regardless
   of the action's free functions (V(Phi), K, K_diss).
4. Therefore the equilibrium source equation does not dynamically
   discriminate among different choices of free functions.
5. Within the current GRUT equilibrium primitive set, the source equation
   is the only direct dynamical constraint on the barrier-sector relaxation
   variable at equilibrium; therefore equilibrium constitutive primitives
   alone cannot identify a unique action.
6. Therefore additional closure input is required.  QED.

**Scope.** This theorem establishes equilibrium dynamical non-identifiability.
It does NOT claim that all admissible actions produce identical stress-energy,
pressure profiles, action values, or derivative couplings at equilibrium.

**What is genuinely new.** Phase IV identified four action routes and the
first-order ODE obstruction.  Phase V proved the constitutive lapse fails
universally.  Phase VI explains WHY equilibrium data cannot identify the
action: self-healing removes source-level dynamical sensitivity to free
functions.

## E. Two Levels of Underdetermination

### Level A — Dynamical: Equilibrium Source Degeneracy (theorem-grade)

The equilibrium source equation does not constrain free functions.  This is
what the theorem proves.

### Level B — Structural: T^Phi Requires Additional Closure (classification-grade)

Even if equilibrium observables are fully specified, T^Phi_mu_nu still
requires additional input: action normalization, a specific potential V(Phi),
an equation of state, propagation structure, auxiliary-field or nonlocal
closure specifics, and coupling to gravity beyond formal minimal coupling.

Level A supports Level B (by removing the strongest available constraint),
but Level A alone does not prove Level B.  Level B is an independent
structural observation about what a variational T^Phi requires.

## F. Admissible T^Phi Constraints

Even without a unique action, structural constraints hold:

1. Combined conservation: nabla_mu(T^{mu nu} + T^{Phi mu nu}) = 0
2. Spherical symmetry: T^Phi diagonal in adapted coordinates
3. At most 3 independent components (rho_Phi, P_r, P_perp)
4. NEC violation indicated at the constitutive level (from Phase V)
5. Equilibrium energy consistent with barrier energy Phi_barrier — as a
   **matching condition**, not a derived unique stress-energy result

## G. Minimal Missing Input

The irreducible inputs that would break the equilibrium source degeneracy
and/or provide structural closure for T^Phi:

1. A potential V(Phi) — not constrained by existing GRUT
2. A covariant propagation equation for Phi — currently no wave equation
3. An equation of state p_Phi(rho_Phi) — not specified
4. Off-equilibrium dynamical data (e.g., quasi-normal mode observation)

At least one additional closure input is required.  A single such input may
be sufficient to break source degeneracy (Level A) in favorable cases, but
sufficiency is not guaranteed generically.  A complete determination of
T^Phi (Level B) likely requires multiple inputs.

None of these is available from existing GRUT primitives.

## H. Status Ladder Update

| Level | Phase V | Phase VI | Changed? |
|-------|---------|----------|----------|
| 1 | exact | exact | No |
| 2 | constitutive_derived | constitutive_derived | No |
| 3 | constitutive_lapse_promotion_obstructed | constitutive_lapse_promotion_obstructed | No |
| T^Phi | schematic_effective | schematic_effective_equilibrium_degenerate | **Sharpened** |

No level is weakened by Phase VI.  No level changed.  The T^Phi
sub-classification is sharpened with a structural explanation (equilibrium
source degeneracy removes dynamical discrimination).

## I. Phase V Reconfirmation

All Phase V results survive Phase VI:

- Insufficiency Theorem: PRESERVED.
- Effective NEC: PRESERVED.
- Lapse Direction Failure: PRESERVED.
- Proxy Classification: PRESERVED.
- Self-Healing: PRESERVED (used as INPUT to degeneracy theorem).
- Phase IV Results: PRESERVED.

Phase VI adds new results but does NOT invalidate any Phase V result.

## J. Nonclaims

1. Phase VI does NOT derive a covariant action for the barrier sector.

2. The Source Degeneracy Theorem proves equilibrium dynamical
   non-identifiability; it does NOT claim all admissible actions produce
   identical stress-energy, pressure, or action values at equilibrium.

3. T^Phi underdetermination (Level B) is a classification-grade structural
   observation supported by, but not solely proven by, the Source Degeneracy
   Theorem (Level A).

4. Route A (KG overdamped) has formal minimal coupling, but V(Phi) is not
   determined — fully determined gravitational closure not achieved.

5. Route B (Galley) gravity coupling is NOT worked out.

6. Route D is a non-action closure route, outside present phase target —
   not "inadmissible" but simply does not answer the action question.

7. NEC violation remains constitutive-level (from Phase V).

8. No new GRUT primitives introduced.

9. No existing result weakened; all Phase V results preserved.

10. Equilibrium source degeneracy does NOT invalidate self-healing (it uses
    self-healing as an established input).

11. Equilibrium energy consistency with barrier energy is a matching
    condition, NOT a derived unique stress-energy result.

12. No observational predictions changed.

## K. What Would Resolve the Barrier Action

To determine a unique covariant barrier action and its T^Phi:

1. A specific potential V(Phi) or equivalent closure for the barrier scalar,
   derived from first principles or constrained by observation.

2. A covariant propagation equation for Phi (wave equation or equivalent),
   which would lift the first-order ODE to a second-order covariant field
   equation.

3. An equation of state p_Phi(rho_Phi) relating barrier pressure to energy
   density.

4. Off-equilibrium dynamical data (e.g., quasi-normal mode observations)
   that would probe away from the degenerate equilibrium point where the
   source equation trivializes.

At least one such input is required; sufficiency is not guaranteed
generically.  A complete T^Phi determination likely requires multiple inputs.
Until these are provided, the barrier action remains underdetermined and
T^Phi remains schematic/effective.
