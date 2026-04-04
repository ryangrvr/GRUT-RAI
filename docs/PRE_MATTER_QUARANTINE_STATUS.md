# PRE-MATTER QUARANTINE STATUS

**Date:** 2026-03-28
**Scope:** Structural constraints on all subsequent matter-sector work.
**Implementation:** `grut/phi_sector_bifurcation.py`, `grut/tau_eff_domain_declaration.py`, `grut/beta_q_sensitivity.py`
**Tests:** 208 passing, 0 failures.

This document records the quarantine perimeter established before matter claims
are introduced. It is not an analysis. It is doctrine.

---

## 1. Φ Object Separation

GRUT uses the symbol Φ across two structurally distinct regimes:

**Φ_trajectory** (collapse sector): the memory field M_drive(t), evaluated at the
moving shell position R(t). A single degree of freedom. Units: acceleration.

**Φ_field** (constitutive sector): the relaxation field Φ(r, t), distributed across
all r. Equilibrium profile: Φ_eq(r) = M/r². Produces energy density
ρ_eq = −M²/(2τ²r⁴).

Both satisfy the same governing ODE:
```
τ_eff · dΦ/dt + Φ = X
```
**Shared ODE form does not imply shared ontology.** The trajectory sector evaluates
this at a point; the field sector evaluates it everywhere. At static equilibrium
both converge to the same fixed point X(R_eq) = M/R_eq² — a coincidence of fixed
points, not an identity of objects.

A third object, Ψ_proxy = 1/(1+β_Q) = α_vac = 1/3, is the barrier-to-gravity lapse
ratio (effective_lapse.py). It equals α_vac numerically but is neither M_drive nor
Φ_field.

**What this means for matter:** Any matter claim using Φ for localization, spatial
extent, or response structure must declare which regime is intended. The field regime
gives matter with profile 1/r²; the trajectory regime gives a point value. These are
different objects even at R_eq where they agree numerically.

No unified governing equation exists in the current architecture. Its construction
would require a covariant field equation that reduces to the trajectory ODE in the
point-particle limit, with a covariant source X[g, T] and a covariant τ_eff — neither
of which is yet built.

---

## 2. τ_eff Domain Declaration

τ_eff = τ₀ / (1 + (ω · τ₀)²) appears in three GRUT sectors with three distinct
definitions of ω:

| Sector | ω | Reference |
|--------|---|-----------|
| Cosmological | H (Hubble rate) | field_equations.py |
| Collapse | \|V\|/R (collapse rate) | collapse.py |
| Interior PDE | ω₀ (mode frequency) | interior_pde.py |

No 4-covariant expression produces all three as components or limits of a single
geometric object. The functional form is preserved; the function is not.

**Effective domain:** All τ_eff-based reasoning in the current architecture is valid
within the *spherically symmetric, quasi-static, preferred-frame regime*. τ_eff is
evaluated in the local rest frame of the shell or fluid element. Results are internally
consistent within each sector's stated domain and are not manifestly frame-independent.

**Structural anchor:** The identity ω₀ · τ_eff = 1 holds at static equilibrium across
all three sectors and is preserved as a frame-safe constraint. It does not resolve the
non-covariance; it survives it.

**What this means for matter:** Matter persistence, local dynamics, transport, and
any claim about moving localized configurations must carry the effective-domain caveat
explicitly. Microscopic and macroscopic claims do not automatically sit under one law
until covariant τ_eff unification is built. An acceptable statement is:

> *"This result is produced in the spherically symmetric quasi-static preferred-frame
> regime. Full covariant unification of τ_eff remains an open structural item."*

That is survivable. Leaving it implicit is not.

---

## 3. β_Q Status

β_Q = 2 is a **working canon hypothesis**. It is not derived from first principles.

**What selects β_Q = 2:** The coincidence Ψ_proxy = 1/(1+β_Q) = α_vac = 1/3.
If this equality is imposed as a constraint, it selects β_Q = 2 given α_vac = 1/3.
But the equality itself — that the barrier-to-gravity lapse ratio equals the vacuum
fraction — is observed in effective_lapse.py output and has not been independently
derived. The coincidence route is real; the justification for the coincidence is absent.

**Blast radius:** Under self-consistent encoding (ε_Q = α_vac^β_Q), R_eq/r_s = α_vac
is β_Q-invariant. The following are β_Q-sensitive through ω₀ and τ_eff:

- ω₀ = √(β_Q · GM/R_eq³) scales as √β_Q
- τ_eff_canon = 1/ω₀ scales inversely
- All quantities depending on τ_eff: A_crit, κ_GRUT, T_Killing, first-law gap R

The locked exact ratios (κ_GRUT/κ_Schw = 3/5, T_Killing/T_Hawking = 3/5) are exact
at β_Q = 2. Whether they hold for other β_Q requires τ²(β_Q), which has not been
derived. They are conditionally locked, not universally locked.

**Required treatment:** β_Q = 2 must not be treated as a fixed constant whose value
is beyond question. It must be treated as a canon assumption whose downstream
consequences are precisely those listed above, and which would require reopening the
deficit chain analysis if it moves.

---

## 4. Claim Firewall

The following claims may be made in later sectors **without reopening these audits**:

✓ R_eq/r_s = 1/3 (β_Q-invariant under self-consistent encoding)
✓ The self-healing condition X − Φ = 0 at equilibrium (ODE-form result, both regimes)
✓ ω₀ · τ_eff = 1 at equilibrium (structural identity, preserved across sectors)
✓ The field regime equilibrium profile Φ_eq(r) = M/r² (constitutive sector)
✓ ρ_eq = −M²/(2τ²r⁴) < 0 (constitutive field sector energy density)
✓ κ_GRUT/κ_Schw = 3/5, T_Killing/T_Hawking = 3/5 (locked at β_Q = 2, stated as such)
✓ A_crit = √(1 + 2/(5π)) ≈ 1.062 (locked at β_Q = 2, stated as such)
✓ τ_eff results within the declared preferred-frame quasi-static domain

The following claims **require reopening the relevant audit** before they may be made:

✗ "Φ localizes matter" — without declaring which Φ regime (field or trajectory)
✗ Any spatial profile claim for matter derived from Φ that does not specify Φ_field
✗ Any matter claim depending on τ_eff in a moving frame or anisotropic background
✗ Any claim that β_Q = 2 is derived (it is observed coincidence, not derivation)
✗ Any claim that κ_GRUT = 3/5 or A_crit is β_Q-universal (they are conditional)
✗ Any claim about Φ unification across sectors without a formal projection map
✗ "The GRUT equilibrium is unique" — the β_Q coincidence route leaves this open

**Reopen condition:** Any of the above claims requires either (a) the relevant
open item is closed by a new derivation with tests, or (b) the claim is explicitly
scoped to the canon β_Q = 2 / preferred-frame / field-sector regime and labelled
as such.
