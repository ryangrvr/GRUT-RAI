# Phase V — Constitutive-to-Metric Lapse Obstruction Analysis

## A. Mission and Context

Phase IV established the three-level lapse hierarchy:

| Level | Status | Content |
|-------|--------|---------|
| 1 | EXACT | Phi_barrier / Phi_grav = 1/(1 + beta_Q) |
| 2 | CONSTITUTIVE_DERIVED | Psi_proxy = 1/(1 + beta_Q) as lapse scale |
| 3 | UNRESOLVED | True interior metric lapse |

Phase IV also identified the central obstruction: A_eff = -1 at canonical
beta_Q = 2, meaning the constitutive post-Newtonian ansatz cannot resolve the
true interior metric lapse at the canonical parameters.

Phase V sharpens this obstruction into a theorem-grade no-go for the naive
constitutive post-Newtonian lapse identification, classifies Psi_proxy with
mathematical precision, and determines what can presently be established at
the constitutive-to-covariant obstruction level.

## B. Constitutive Lapse Insufficiency Theorem

**Theorem.** For the canonical GRUT parameter regime alpha_vac <= e^{-1/2}
(which covers the canonical value alpha_vac = 1/3 and any regime satisfying
this bound), the naive constitutive post-Newtonian mapping yields
A_eff(beta_Q) < 0 for every finite beta_Q > 0.

**Proof** (clean inequality route).

Define:

    A_eff = 1 - C * beta / (1 + beta),  where  C = alpha^{-2/beta}

A_eff < 0 if and only if g(beta) = ln(C * beta / (1 + beta)) > 0.

Substitute x = 1/beta > 0:

    g = 2Lx - ln(1 + x),  where  L = |ln alpha|

For L >= 1/2 (i.e., alpha <= e^{-1/2}), we have 2L >= 1, so:

    g >= x - ln(1 + x) = h(x)

The function h(x) = x - ln(1 + x) satisfies h(0) = 0 and
h'(x) = x/(1 + x) > 0 for all x > 0, hence h(x) > 0 for all x > 0.

Therefore g(beta) > 0 for every finite beta > 0.

Therefore A_eff < 0 for every finite beta > 0.  QED.

**Scope.** This theorem rules out only the naive constitutive post-Newtonian
lapse identification.  It does not rule out a different covariant interior
metric construction or a non-Schwarzschild-like observer-adapted lapse notion.

**What is genuinely new.** Phase IV showed A_eff = -1 at canonical beta_Q = 2
only.  Phase V proves A_eff < 0 for every finite beta_Q > 0, establishing
that the failure is structural (not a parameter-tuning artifact).

**Limiting behavior.** As beta_Q -> infinity, A_eff -> 0^- but never reaches
zero.  The theorem covers every finite beta_Q > 0.

## C. Effective NEC-Violating Support (Secondary, Constitutive-Level)

Under Einstein-like covariant closure assumptions, the provisional
constitutive-to-covariant translation indicates that NEC-violating effective
stress-energy (rho_eff + P_eff < 0) appears necessary for sub-horizon barrier
support.

**Qualification.** This is a constitutive-level observation, NOT a covariant
theorem.  The effective stress-energy decomposition is provisional because
T^Phi is schematic/effective (not derived from a covariant action).

The mechanism is analogous to the NEC-violating support in gravastar-type
constructions, but is not derived from a covariant action in the GRUT
framework.

## D. Lapse Direction Failure

At the GRUT equilibrium endpoint (C = 3 at canonical parameters):

- In Schwarzschild coordinates: A_schw = 1 - C = -2, so g_tt = -A_schw = 2 > 0
  (spacelike) and the coordinate t becomes spacelike inside the horizon.
- The constitutive barrier correction adds delta_A = C/(1 + beta_Q) = 1, giving
  A_eff = A_schw + delta_A = -2 + 1 = -1.
- Since A_eff < 0, the constitutive barrier correction does NOT restore a
  timelike Schwarzschild-like lapse direction at the endpoint.
- The naive static redshift formula Psi = 1/sqrt(A_eff) - 1 does not apply
  when A_eff < 0.

Further metric interpretation requires an observer-adapted interior chart or
a fuller covariant construction.

## E. T^Phi Status

T^Phi_mu_nu is SCHEMATIC/EFFECTIVE in the current GRUT framework:

- Not derived from a Lagrangian.
- Not uniquely specified.
- The mapping from the barrier energy ratio to the metric lapse is
  structurally undetermined.

What is missing for a metric determination:

1. A covariant action S[Phi] for the memory/barrier field.
2. The stress-energy T^Phi_mu_nu derived from that action via variation.
3. An equation of state relating barrier pressure to energy density.
4. Covariant conservation constraints on T^Phi in the sub-horizon regime.

This is the structural reason why Psi_proxy cannot be promoted to the true
metric lapse within the constitutive framework.

## F. Psi_proxy Classification: Constitutive Surrogate

Psi_proxy = 1/(1 + beta_Q) is classified as a CONSTITUTIVE SURROGATE:

- **Level 1 (EXACT):** It is the exact barrier-to-gravitational energy ratio.
  This is an algebraic identity, independent of any metric ansatz.
- **Level 2 (CONSTITUTIVE_DERIVED):** It serves as the constitutive lapse
  scale in the post-Newtonian regime.
- **Level 3 (OBSTRUCTED):** It cannot be promoted to the true metric lapse
  via the naive constitutive post-Newtonian mapping (Insufficiency Theorem).
- **Not excluded:** The true lapse may coincidentally equal Psi_proxy for
  reasons beyond the constitutive framework.

The scope of the obstruction is specifically about the naive constitutive
post-Newtonian lapse identification.  It does not exclude Psi_proxy as the
true lapse under a different covariant interior construction.

## G. Status Ladder Update

| Level | Phase IV | Phase V | Changed? |
|-------|----------|---------|----------|
| 1 | exact | exact | No |
| 2 | constitutive_derived | constitutive_derived | No |
| 3 | unresolved | constitutive_lapse_promotion_obstructed | Yes |

No level is weakened by Phase V.  Level 3 is sharpened from a vague
"unresolved" to a specific, provable no-go for the naive constitutive
lapse promotion.

## H. Self-Healing Reconfirmation

Self-healing at the equilibrium endpoint depends on the source term
X - Phi = a_grav - M_drive = 0 (force balance).  Force balance is a
dynamical condition, not a metric condition.

The Insufficiency Theorem concerns A_eff (metric component).  NEC violation
concerns effective stress-energy.  Neither affects the dynamical force
balance.  Therefore self-healing is PRESERVED.

## I. Phase IV Reconfirmation

All Phase IV results survive Phase V:

- Level 1 (exact barrier ratio): PRESERVED.
- Level 2 (constitutive-derived proxy): PRESERVED.
- Sensitivity band: PRESERVED.
- Self-healing: PRESERVED.
- Shift estimates: PRESERVED.
- Coincidence explanation: PRESERVED.

Phase V adds new results but does NOT invalidate any Phase IV result.

## J. Nonclaims

1. The theorem does NOT prove that no covariant interior metric exists --
   only that the naive constitutive post-Newtonian lapse identification
   fails.  A different covariant construction or non-Schwarzschild-like
   observer-adapted lapse notion is not ruled out.

2. The Insufficiency Theorem proves A_eff < 0 for every finite beta_Q > 0
   when alpha_vac <= e^{-1/2} (covering the canonical value and any regime
   satisfying this bound); this concerns the NAIVE CONSTITUTIVE
   POST-NEWTONIAN ANSATZ, not the full covariant GRUT interior.

3. Effective NEC-violating support is indicated at the constitutive-to-
   covariant translation level; it is NOT a covariant theorem.

4. The lapse direction failure means the naive static redshift interpretation
   fails; it does NOT mean no static interior is possible under a fuller
   construction.

5. T^Phi is schematic/effective -- the metric lapse cannot be determined
   without a Lagrangian-derived T^Phi.

6. Psi_proxy = 1/(1 + beta_Q) is a CONSTITUTIVE SURROGATE: neither promoted
   to the true lapse nor excluded.

7. The obstruction in Level 3 is specifically about the constitutive-to-metric
   lapse promotion, not about the interior metric itself.

8. Self-healing is PRESERVED: it depends on force balance (X - Phi = 0),
   not on the metric.

9. No Phase IV result is weakened or invalidated.

10. The Insufficiency Theorem does NOT invalidate the equilibrium endpoint
    (force balance is dynamical, not metric).

11. The qualifier alpha_vac <= e^{-1/2} covers the canonical GRUT value and
    any regime satisfying this bound; it is not an unconditional universal
    statement.

12. No observational predictions are made or modified by Phase V.

## K. What Would Resolve Level 3

To resolve the metric lapse (and complete a covariant interior metric),
the following would be needed:

1. A covariant action S[Phi] for the memory/barrier field, from which
   T^Phi_mu_nu can be derived variationally.

2. Solution of the full Einstein equations G_mu_nu = 8*pi*G * (T^matter +
   T^Phi) in the sub-horizon regime with the derived T^Phi.

3. An observer-adapted interior chart or non-Schwarzschild-like coordinate
   construction appropriate for the static (or quasi-static) sub-horizon
   barrier-supported configuration.

Until these are provided, Level 3 remains at
constitutive_lapse_promotion_obstructed.
