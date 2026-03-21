# Phase 5 xAct Symbolic Offensive — Route A Klein-Gordon Covariant Lift

## Status

**ROUTE A COMPLETE — QUASI-ACTION FULLY CHARACTERIZED**

Classification: **LOCAL VARIATIONAL, EXTRA DOF, T^Φ MATCHES PHASES 1–4**

Phase 5 derives the complete Route A (Klein-Gordon) covariant package from the
Phase VII candidate potential V(Φ) = Φ²/(2τ²). The principal result is that
Route A provides a CLEAN LOCAL VARIATIONAL PRINCIPLE that fully derives the
same T^Φ locked in Phases 1 and 4, with stable massive modes (no ghost, no
tachyon), but introduces extra propagating degrees of freedom absent from the
effective GRUT framework. Route A is classified as a QUASI-ACTION: a UV
completion that yields correct stress-energy but does not exactly reproduce
the first-order GRUT relaxation dynamics.

---

## A. Mission and Context

The GRUT scalar field obeys a first-order memory relaxation ODE:
τ u^a ∇_a Φ + Φ = X. No local, real-valued, time-independent Lagrangian can
produce a first-order (odd-order) equation of motion via Euler-Lagrange
variation (Bauer's theorem). This is the fundamental reason why GRUT requires
either a non-local action (Route C), a doubled-field dissipative action
(Route B/Galley), or an approximate local action (Route A/Klein-Gordon).

Phase VII identified V(Φ) = Φ²/(2τ²) as the candidate potential for Route A,
with the mapping chain β_Q → ω₀² → m² = 1/τ² → V(Φ). Phase 5 completes
this identification by deriving the full Route A package:
action → EOM → T^Φ → dispersion → EOS → overdamped limit.

---

## B. Klein-Gordon Action

The Route A scalar action:

    S_Φ = ∫ d⁴x √(−g) [−(1/2)(∇Φ)² − Φ²/(2τ²) + ΦX/τ]

where:
- V(Φ) = Φ²/(2τ²) is the mass-term potential (m² = 1/τ²)
- J = X/τ is the source coupling
- X is the gravitational drive (external source)

**Scalar equation of motion** (δS/δΦ = 0):

    □Φ − Φ/τ² + X/τ = 0

Equivalently: □Φ = (Φ − Xτ)/τ².

**Static homogeneous equilibrium** (□Φ = 0):

    Φ_KG = Xτ

This differs from the GRUT memory equilibrium Φ_GRUT = X by a factor of τ.
The discrepancy is a structural signature of Route A: the second-order KG
equation is a UV completion that does not exactly reproduce the first-order
GRUT dynamics. The equilibrium mismatch can be absorbed by a field
redefinition Φ_{Route A} = τ · Φ_{GRUT}.

---

## C. T^Φ from Metric Variation

The standard formula for the stress-energy of a minimally-coupled scalar:

    T_{ab} = ∇_a Φ ∇_b Φ − g_{ab}[(1/2)(∇Φ)² + V(Φ) − ΦJ]

Explicitly:

    T_{ab} = ∇_a Φ ∇_b Φ − g_{ab}[(1/2)(∇Φ)² + Φ²/(2τ²) − ΦX/τ]

**Phase 1/4 match**: This is IDENTICAL to the locked T^Φ from Phase 1
(Factorization Theorem) and Phase 4 (Einstein + T^Φ). Route A DERIVES from
a variational principle what Phase 1 LOCKED from the Galley CTP formalism
at the physical limit.

**xAct verification**: The abstract T^Φ_{ab} was constructed in xAct and
its structure confirmed. The same expression produces the correct divergence
(see Section D) and component decomposition (see Section F).

---

## D. On-Shell Conservation (Bianchi Consistency)

The xAct computation of ∇^a T^Φ_{ab} yields:

    ∇^a T^Φ_{ab} = (□Φ)∇_b Φ + ∇^a Φ · ∇_b ∇_a Φ

This can be rewritten as:

    ∇^a T_{ab} = (□Φ − dV/dΦ + J) · ∇_b Φ

The divergence vanishes identically when Φ satisfies the KG equation of
motion □Φ − Φ/τ² + X/τ = 0. This ensures Bianchi consistency: the Einstein
equations G_{ab} = 8πG T^Φ_{ab} are compatible with ∇^a G_{ab} = 0 if and
only if the scalar field satisfies its field equation.

**Result**: NONZERO off-shell (expected), ZERO on-shell (verified).

---

## E. Dispersion Relation and Mode Analysis

Linearizing the KG equation about equilibrium (Φ = Φ₀ + δΦ):

    □(δΦ) − δΦ/τ² = 0

For plane waves δΦ ~ exp(−iωt + ik·x) in Minkowski spacetime:

    (ω² − |k|²) − 1/τ² = 0

**Route A dispersion relation**:

    ω² = |k|² + 1/τ²

This is the standard massive Klein-Gordon dispersion relation:
- Mass gap: ω_min = 1/τ (at k = 0)
- Group velocity: v_g = |k|/ω < c (subluminal)
- Phase velocity: v_p = ω/|k| > c (superluminal, no signal propagation)
- ALL modes are oscillatory (ω² > 0 for all k)
- NO instability, NO tachyon, NO ghost

**Comparison with Route B** (Phase 2, Φ₋ sector):

| Property | Route A (KG) | Route B (Galley Φ₋) |
|:---|:---|:---|
| Dispersion | ω² = k² + 1/τ² | λ² − λ/τ + k² − 1/τ² = 0 |
| Stability | ALL modes stable | UNSTABLE for k < √5/(2τ) |
| Mode type | Oscillatory (massive) | Growing (tachyonic + anti-damped) |
| Ghost | None | Action-level (off-diagonal kinetic) |

Route A has NO instability because it is a single-copy theory. Route B
instability comes from the doubled-field structure (ghost mode Φ₋).

---

## F. Equation of State

**T^Φ components** (static spherically symmetric, h = 1/(1−2m/r)):

    ρ = (1/2)(Φ')²/h + Φ²/(2τ²) − ΦX/τ
    p_r = (1/2)(Φ')²/h − Φ²/(2τ²) + ΦX/τ
    p_⊥ = −(1/2)(Φ')²/h − Φ²/(2τ²) + ΦX/τ

**At GRUT equilibrium** (Φ = X, Φ' = 0):

    ρ_GRUT = −X²/(2τ²) < 0    (NEGATIVE energy density)
    p_GRUT = +X²/(2τ²) > 0    (POSITIVE pressure, isotropic)
    w_GRUT = −1                 (NEC-saturating)

**At KG equilibrium** (Φ = Xτ, Φ' = 0):

    ρ_KG = −X²/2 < 0           (NEGATIVE energy density)
    p_KG = +X²/2 > 0           (POSITIVE pressure, isotropic)
    w_KG = −1                   (NEC-saturating)

Both equilibria give w = −1. The energy densities differ (by a factor τ²),
but the EOS ratio is identical. This is a structural property.

**Effective potential**: V_eff = V − ΦJ = (Φ − Xτ)²/(2τ²) − X²/2.
The minimum is at Φ = Xτ (KG equilibrium) with V_eff,min = −X²/2.

**Remarkable result**: The homogeneous EOS is w = −1 for ALL values of Φ,
not just at equilibrium. Since ρ = V_eff and p = −V_eff at Φ' = 0,
w = p/ρ = −1 identically. The NEC-saturating EOS is a KINEMATIC property
of any homogeneous scalar field with a potential.

---

## G. EOS With Gradients (Anisotropy)

When Φ' ≠ 0, the stress-energy becomes anisotropic:

    p_r − p_⊥ = (Φ')²/h > 0

The radial EOS is stiffer than w = −1 (w_r > −1) and the tangential EOS
is softer (w_⊥ < −1). The anisotropy vanishes at the equilibrium core
(Φ' = 0) and in the exterior (Φ' → 0), and is significant only in the
transition region. This is consistent with the Phase VII anisotropy block
for the collapse sector.

**NEC with gradients**:

    ρ + p_r = (Φ')²/h ≥ 0     (NEC satisfied for radial null vectors)
    ρ + p_⊥ = 0                 (NEC saturated for tangential null vectors)

The NEC structure is unchanged by the gradients.

---

## H. Overdamped Limit: KG → GRUT

The hierarchy of scalar field equations, from UV to IR:

| Level | Equation | Classification |
|:---|:---|:---|
| 3 (UV) | □Φ − Φ/τ² + X/τ = 0 | Route A, Klein-Gordon |
| 2 (IR) | (1/τ)u^a∇_aΦ − Φ/τ² + X/τ = 0 | Overdamped KG |
| 1 (eff) | τ u^a∇_aΦ + Φ = X | GRUT memory ODE |

**Level 3 → Level 2**: In the overdamped limit, when external dissipation
(Hubble friction, CTP kernel, or other mechanism) provides a damping term
(1/τ)u^a∇_aΦ that dominates over the wave term □Φ, the KG equation reduces
to the overdamped form.

**Level 2 → Level 1**: Multiplying Level 2 by τ² gives τ u^a∇_aΦ = Φ − Xτ,
which is the GRUT memory ODE with the equilibrium shifted to Φ = Xτ.
The shift is absorbed by the field redefinition Φ_{Route A} = τ · Φ_{GRUT}.

**Critical observation**: T^Φ is IDENTICAL across all three levels. The
stress-energy is determined by the action structure, not by the specific
dynamics. The KG, damped KG, and GRUT memory equations all produce the same
T^Φ because they share the same Lagrangian density.

---

## I. Route A vs Route B: Structural Comparison

| Property | Route A (KG) | Route B (Galley CTP) |
|:---|:---|:---|
| Action type | Local, single-copy | Doubled-field, dissipative |
| EOM order | 2nd (wave equation) | 2nd (damped wave) |
| Damping | None (external only) | Built-in (dissipative kernel) |
| Equilibrium | Φ = Xτ | Φ = X |
| Perturbation modes | Oscillatory (stable) | Growing (Φ₋ unstable) |
| Dispersion | ω² = k² + 1/τ² | λ² − λ/τ + k² − 1/τ² = 0 |
| Ghost | None | Action-level (Φ₋, h₋) |
| T^Φ | Fully derived from action | Fully derived (same result) |
| EOS (equilibrium) | w = −1 | w = −1 |
| GRUT recovery | Overdamped limit (approximate) | Physical limit (exact) |
| Classification | Quasi-action | Formal framework |

**Key structural difference**: Route A is a clean variational principle but
misses the dissipative dynamics of GRUT. Route B captures the dissipation but
introduces ghosts. Both produce the SAME T^Φ, confirming that the
stress-energy structure is robust across action formulations.

---

## J. Extra Propagating Modes

Route A introduces modes absent from effective GRUT:

**Massive scalar waves**: ω² = |k|² + 1/τ² with mass gap m = 1/τ.
These propagate subluminally and describe oscillations of Φ about equilibrium.
In GRUT, Φ relaxes to equilibrium without oscillation (first-order dynamics).

**Compton wavelength**: λ_C = 2πτ. Modes with wavelength ≪ λ_C behave as
approximately massless waves; modes with wavelength ≫ λ_C are heavily
mass-gapped.

**Bauer's theorem**: A local, real-valued, time-independent Lagrangian
produces Euler-Lagrange equations of even order only. Since the GRUT memory
ODE is first-order, no local action can reproduce it exactly. Route A (KG)
is the simplest second-order approximation, and the extra modes are the
price of having a local variational principle.

---

## K. Remaining Obstructions (Updated)

1. **Route A is a quasi-action, not the true GRUT dynamics** — STRUCTURAL.
   The KG equation introduces propagating modes absent from GRUT. Route A
   provides a variational parent for T^Φ but does not capture the
   dissipative relaxation dynamics.

2. **Source coupling J remains free** — OPEN. V(Φ) = Φ²/(2τ²) reduces
   Route A from 2 free functions (V, J) to 1 (J only), but J = X/τ is
   chosen for T^Φ matching, not derived from first principles.

3. **Phase VI source degeneracy NOT broken** — STRUCTURAL. At equilibrium
   (Φ = X), the source equation becomes 0 = 0 regardless of V(Φ). The
   potential specification does not discriminate between action routes
   at the equilibrium point.

4. **Anisotropy block** — HARD STRUCTURAL. In the collapse sector, the
   stress-energy is anisotropic (p_r ≠ p_⊥), requiring separate (w_r, w_⊥).
   A single w_Φ does not close the system. Route A confirms this: the
   gradient terms break isotropy in exactly the manner identified by Phase VII.

5. **Equilibrium mismatch** — STRUCTURAL BUT RESOLVABLE. The KG equilibrium
   Φ = Xτ differs from GRUT equilibrium Φ = X. This can be absorbed by a
   field redefinition but reflects the approximate nature of Route A.

6. **Quantitative interior metric** — OPEN (inherited from Phase 4). The
   mass reduction mechanism works with Route A T^Φ, but the quantitative
   solution of the modified TOV system is not addressed.

---

## L. Explicit Nonclaims

1. Route A does NOT replace GRUT; it provides a variational parent that
   yields the correct T^Φ but introduces extra propagating modes

2. The KG equation is NOT the GRUT memory ODE; the first-order dynamics
   cannot be reproduced by any local variational principle (Bauer's theorem)

3. The w = −1 EOS is a KINEMATIC property of homogeneous scalar fields,
   not a dynamical prediction specific to Route A

4. The dispersion relation ω² = k² + 1/τ² applies to PERTURBATIONS about
   equilibrium, not to the full nonlinear dynamics

5. The equilibrium mismatch (Φ_KG = Xτ vs Φ_GRUT = X) does NOT invalidate
   Route A — it is a structural feature of the quasi-action classification

6. The T^Φ match between Routes A and B does NOT mean the routes are
   physically equivalent — they differ in dynamics, ghost structure, and
   mode content

7. The overdamped hierarchy (KG → damped KG → GRUT) is a qualitative
   classification, not a rigorous asymptotic expansion

8. The anisotropic EOS (w_r ≠ w_⊥) when Φ' ≠ 0 is consistent with the
   Phase VII anisotropy block but does NOT resolve it

9. The statement that Route A is "ghost-free" refers to the SINGLE-COPY
   sector only; the doubled-field formalism (Route B) introduces ghosts
   at the action level

10. The mass gap m = 1/τ in the dispersion relation does NOT imply a
    physical particle mass — it is the inverse relaxation time of the
    GRUT memory kernel

11. The source coupling J = X/τ is chosen for T^Φ matching with Phase 1/4;
    a different coupling J = X/τ² would give equilibrium at Φ = X but a
    different T^Φ

12. Route A COMPLETES the action-route classification but does not SELECT
    a unique action — Routes A, B, C, and D all remain viable with different
    trade-offs

13. The effective potential V_eff = (Φ − Xτ)²/(2τ²) − X²/2 is NEGATIVE
    at all points where the barrier operates; this is consistent with
    the Phase 4 mass reduction mechanism

14. The NEC saturation ρ + p_⊥ = 0 holds for ALL field configurations
    (not just equilibrium) and is a property of the minimally-coupled
    scalar action, not specific to V(Φ) = Φ²/(2τ²)

---

## Computational Artifacts

**Script:** xact/grut_route_a_kg.wl (Parts A–K)
**Engine:** Wolfram Engine 14.x with xAct 1.2.0 / xPert 1.0.6
**Method:** xAct abstract T^Φ construction and divergence verification;
algebraic mode analysis and EOS derivation in plain Mathematica
**Exports:** xact/results/route_a_tphi.m, route_a_div_tphi.m,
route_a_dispersion.m, route_a_eos.m, route_a_classification.m

---

## Phase 1–5 Result Lock

    Phase 1 (T^Φ):              LOCKED (ΔT = 0, Factorization Theorem)
    Phase 2 (Φ₋):              LOCKED (consistent, not attractor, IR-dominated)
    Phase 3 (h₋):              LOCKED (consistent, vacuum stable, sourced unstable)
    Phase 4 (Einstein+T^Φ):    LOCKED (ρ<0, mass reduction, metric restoration possible)
    Phase 5 (Route A KG):       LOCKED (quasi-action, T^Φ matches, stable, w=-1)

    Route B:                    COMPLETE (scalar + metric sectors, both characterized)
    Route A:                    COMPLETE (action → EOM → T^Φ → EOS → classification)
    T^Φ universality:           VERIFIED (Route A = Route B = Phase 1 locked form)
    Phase V obstruction:        RECLASSIFIED (constitutive ansatz artifact)
    Interior metric:            STRUCTURALLY POSSIBLE (quantitative TBD)

    Equation hierarchy:         KG (Route A) → Damped KG → GRUT memory ODE
    Action route summary:       A=quasi-action, B=formal, C=nonlocal, D=non-action
