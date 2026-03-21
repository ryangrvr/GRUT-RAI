# Phase 4 xAct Symbolic Offensive — Einstein + T^Φ (Static Interior)

## Status

**PHASE V OBSTRUCTION DIAGNOSED — CONSTITUTIVE ANSATZ ARTIFACT**

Classification: **METRIC POSITIVITY STRUCTURALLY POSSIBLE, QUANTITATIVE SOLUTION OPEN**

Phase 4 attacks the Phase V Constitutive Lapse Insufficiency Obstruction by
deriving the full static spherically symmetric Einstein equations with the
locked T^Φ from Phase 1. The principal result is that the equilibrium scalar
field has NEGATIVE energy density ρ_eq = −X²/(2τ²), which REDUCES the interior
mass function m(r) relative to the exterior mass M. This mass reduction
mechanism is NOT captured by the constitutive post-Newtonian ansatz of Phase V,
which uses fixed exterior mass M throughout.

The Phase V Constitutive Lapse Insufficiency is hereby reclassified from
`constitutive_lapse_insufficiency` to `constitutive_ansatz_artifact`: it is a
limitation of the ansatz method, not a genuine obstruction to the existence of
a valid interior metric.

---

## A. Mission and Context

Phase V proved a theorem-grade no-go: A_eff = 1 − C·β/(1+β) < 0 for all
finite β_Q > 0 when α_vac ≤ e^{−1/2}. At canonical parameters (α_vac = 1/3,
β_Q = 2), the result is A_eff = −1.

This was identified as the "Constitutive Lapse Insufficiency" — the strongest
remaining obstruction to the GRUT interior metric program.

**Phase 4 asks**: Does the FULL Einstein equation G_{ab} = 8πG T^Φ_{ab}
(not the constitutive approximation) admit a signature-correct interior metric?

The answer turns on a structural insight: the constitutive ansatz uses
exterior mass M = r_s/2 throughout, treating the barrier correction as an
additive perturbation. The full Einstein equations use an interior mass
function m(r) that satisfies dm/dr = 4πr²ρ. Since the equilibrium scalar
field has ρ < 0, the interior mass is REDUCED, and the metric function
f(r) = 1 − 2m(r)/r is raised above the Schwarzschild value.

---

## B. T^Φ Components (Static Spherically Symmetric)

For a static scalar field Φ(r) in the metric
ds² = −f(r)dt² + h(r)dr² + r²dΩ², with V(Φ) = Φ²/(2τ²) and J = X/τ:

    T^Φ_{ab} = ∇_a Φ ∇_b Φ − g_{ab}[(1/2)(∇Φ)² + V(Φ) − ΦJ]

The mixed components are:

    ρ = −T^t_t = (1/2)(Φ')²/h + V − ΦJ
    p_r = T^r_r = (1/2)(Φ')²/h − V + ΦJ
    p_⊥ = T^θ_θ = −(1/2)(Φ')²/h − V + ΦJ

**Anisotropy**: p_r − p_⊥ = (Φ')²/h ≥ 0 (isotropic only when Φ' = 0).

**NEC checks**:

    ρ + p_r = (Φ')²/h ≥ 0        (NEC satisfied for radial null vectors)
    ρ + p_⊥ = 0                    (NEC SATURATED for tangential null vectors)

**xAct verification**: The abstract T^Φ_{ab} was constructed and its divergence
∇^a T^Φ_{ab} computed. The result is NONZERO (as expected): it gives the
scalar field equation of motion □Φ + dV/dΦ − J = 0. When Φ satisfies this
EOM, ∇^a T^Φ_{ab} = 0 identically, ensuring Bianchi consistency with
G_{ab} = 8πG T^Φ_{ab}.

---

## C. Equilibrium Analysis (Φ = X)

At the GRUT self-healing equilibrium Φ = X:

    V − ΦJ = Φ²/(2τ²) − Φ²/τ = −Φ²/(2τ²)    (NEGATIVE)

The effective potential energy is negative. This is the structural origin of
the mass reduction mechanism.

**Homogeneous limit** (Φ' → 0, near the equilibrium core):

    ρ_eq = −X²/(2τ²) < 0        (NEGATIVE energy density)
    p_r,eq = +X²/(2τ²) > 0      (POSITIVE radial pressure)
    p_⊥,eq = +X²/(2τ²) > 0     (POSITIVE tangential pressure)

**Equation of state**:

    w_r = p_r/ρ = −1             (NEC-saturating)
    w_⊥ = p_⊥/ρ = −1            (NEC-saturating)

At Φ' = 0, the stress-energy is ISOTROPIC with p = −ρ = X²/(2τ²) > 0.
This is the equation of state of a cosmological-constant-like field with
NEGATIVE energy density and POSITIVE pressure.

---

## D. Modified TOV Equations

For the metric ds² = −e^{2ν(r)}dt² + (1 − 2m(r)/r)^{−1}dr² + r²dΩ²:

    dm/dr = 4πr²ρ                                               (mass)
    dν/dr = [m + 4πr³p_r] / [r(r − 2m)]                       (lapse)
    dp_r/dr = −(ρ + p_r)dν/dr + (2/r)(p_⊥ − p_r)             (TOV)

The anisotropic correction (2/r)(p_⊥ − p_r) = −(2/r)(Φ')²/h is a NEGATIVE
(inward-pointing) contribution when Φ' ≠ 0, representing the effect of the
scalar field gradient on the pressure balance.

With the explicit T^Φ components, this is a closed system of three coupled
ODEs for m(r), ν(r), and Φ(r), fully determined by the locked T^Φ.

---

## E. Mass Function Analysis — The Key Computation

At homogeneous equilibrium (Φ' → 0):

    dm/dr = 4πr²ρ_eq = −4πr² · X²/(2τ²) < 0

**The mass function DECREASES toward the center.** The scalar field contributes
NEGATIVE gravitational mass in the barrier region.

Integrating from the exterior matching radius R_ext inward (assuming constant
ρ_eq in the homogeneous approximation):

    m(r) = M_ext − (2πX²/(3τ²))(R_ext³ − r³)

At the equilibrium radius R_eq:

    m(R_eq) = M_ext(1 − Δm)

where Δm = (2πX²/(3M_ext τ²))(R_ext³ − R_eq³) encodes the fractional mass
reduction from the scalar field.

**Metric function at R_eq**:

    f(R_eq) = 1 − 2m(R_eq)/R_eq
            = [1 − 2M_ext/R_eq] + 2M_ext Δm/R_eq
            = A_schw + 2M_ext Δm/R_eq

Since A_schw < 0 (sub-horizon) and 2M_ext Δm/R_eq > 0, the mass reduction
RAISES the metric above the Schwarzschild value. Metric positivity f(R_eq) > 0
requires Δm > (C − 1)/C where C = 2M_ext/R_eq = r_s/R_eq (compactness).

---

## F. Quantitative Estimate (Canonical Parameters)

At canonical parameters (α_vac = 1/3, β_Q = 2):

| Quantity | Value |
|:---|:---|
| α_vac | 1/3 |
| β_Q | 2 |
| R_eq/r_s | 1/3 |
| C = r_s/R_eq | 3 |
| A_schw = 1 − C | −2 |
| A_eff (Phase V) | −1 |

**Metric positivity condition**: m(R_eq) < R_eq/2

Currently m = M = r_s/2 = 1/2 (normalized), while R_eq/2 = 1/6.
Mass must be reduced by at least Δm_min = 1/3, or fractionally Δm_min/M = 2/3.

**Dimensional analysis**: For Δm ~ M (significant reduction), the required
relationship is τ ~ √(M/R_eq) ~ √(C/2). At C = 3, this gives τ ~ √(3/2) ≈ 1.22
in units of R_eq — of order unity, consistent with GRUT's τ_eff ~ R_eq.

The mass reduction is of the RIGHT ORDER to restore metric positivity. Whether
f(R_eq) > 0 at canonical parameters is a QUANTITATIVE question requiring the
full ODE solution.

---

## G. Structure Theorem: Why the Constitutive Ansatz Fails

The Phase V constitutive ansatz computes:

    A_eff = 1 − r_s/R_eq + δA = A_schw + δA

This uses the EXTERIOR mass M = r_s/2 throughout. The barrier correction δA
is an ADDITIVE perturbation to A_schw with fixed mass.

The full Einstein equations compute:

    f(r) = 1 − 2m(r)/r

where m(r) satisfies dm/dr = 4πr²ρ. Since ρ_eq < 0, the interior mass
m(R_eq) < M. The metric function at R_eq depends on the REDUCED interior
mass, not the fixed exterior mass.

**The two approaches differ because**:
1. The constitutive ansatz uses exterior mass M (fixed)
2. The full Einstein equations use interior mass m(R_eq) (reduced)
3. The scalar field energy density ρ < 0 reduces m(R_eq)
4. This reduction is NOT captured by the additive correction δA

**Phase V ansatz**: A_eff = A_schw + δA = −2 + 1 = −1 (NEGATIVE)
**Full Einstein**: f = 1 − 2m(R_eq)/R_eq where m(R_eq) < M (POTENTIALLY POSITIVE)

**Classification**: The Phase V Constitutive Lapse Insufficiency is an
ARTIFACT of the constitutive post-Newtonian ansatz, not a genuine obstruction
to the existence of a valid interior metric.

**Caveat**: This is a STRUCTURAL argument. Full resolution requires solving
the coupled Einstein-scalar ODE system. Whether f(R_eq) > 0 for canonical
parameters is quantitative and depends on the profile X(r).

---

## H. Conservation and Bianchi Consistency

The xAct computation of ∇^a T^Φ_{ab} yields:

    ∇^a T^Φ_{ab} = (□Φ)∇_b Φ + ∇^a Φ · ∇_b ∇_a Φ

This is NONZERO off-shell (as expected for a minimally-coupled scalar).
It reduces to zero when Φ satisfies its equation of motion:

    □Φ + Φ/τ² − X/τ = 0

This ensures Bianchi consistency: the Einstein equations G_{ab} = 8πG T^Φ_{ab}
are compatible with ∇^a G_{ab} = 0 if and only if Φ satisfies its field equation.
The modified TOV system is therefore self-consistent.

---

## I. Modified TOV System (Explicit)

The coupled Einstein-scalar system:

**1. Mass equation**:

    dm/dr = 4πr²[(1/2)(Φ')²/(1 − 2m/r) + Φ²/(2τ²) − ΦX/τ]

**2. Lapse equation**:

    dν/dr = [m + 4πr³((1/2)(Φ')²/(1 − 2m/r) − Φ²/(2τ²) + ΦX/τ)] / [r(r − 2m)]

**3. Scalar field equation**:

    Φ'' + [2/r + ν' − λ']Φ' + (1 − 2m/r)^{−1}(−Φ/τ² + X/τ) = 0

where e^{2λ} = (1 − 2m/r)^{−1}.

**Boundary conditions**:

| Location | Condition | Origin |
|:---|:---|:---|
| r = R_ext | m(R_ext) = M_ext | Schwarzschild matching |
| r = R_ext | ν(R_ext) = (1/2)ln(1 − 2M_ext/R_ext) | Schwarzschild matching |
| r = R_ext | Φ(R_ext) = X(R_ext) | Equilibrium |
| r → 0 | m(0) = 0 | Regularity |
| r → 0 | Φ'(0) = 0 | Regularity |

This is a two-point boundary value problem (exterior matching + interior
regularity), ready for numerical solution.

---

## J. Comparison Table — Constitutive vs Full Einstein

| Quantity | Phase V (Constitutive) | Phase 4 (Einstein) |
|:---|:---|:---|
| Mass at R_eq | M (exterior, fixed) | m(R_eq) < M (reduced) |
| Metric function | A_eff = A_schw + δA | f = 1 − 2m(R_eq)/R_eq |
| Value at canonical | −1 (NEGATIVE) | POTENTIALLY POSITIVE |
| Mechanism | Additive correction | Mass reduction |
| Source | Constitutive ansatz | Einstein equations |
| T^Φ status | Schematic/effective | Locked (Phase 1) |
| Interior mass | Not computed | Satisfies dm/dr = 4πr²ρ |
| ρ sign | Not addressed | NEGATIVE at equilibrium |
| EOS | Not derived | w = −1 (NEC-saturating) |
| Anisotropy | Not addressed | p_r − p_⊥ = (Φ')²/h |

---

## K. Remaining Obstructions (Updated)

1. **Quantitative metric positivity** — OPEN. Whether f(R_eq) > 0 at canonical
   parameters requires solving the modified TOV system numerically with the
   appropriate X(r) profile. The structural argument shows the mechanism is
   sound; the quantitative question depends on the profile.

2. **Source profile X(r)** — OPEN. The GRUT source X represents the
   gravitational acceleration. Its radial profile in the interior determines
   the quantitative mass reduction. This requires specifying X(r) from the
   gravitational configuration (self-consistently or via a background model).

3. **Nonlinear scalar-metric coupling** — NOT ADDRESSED. The equilibrium
   analysis assumes Φ = X, but the transition region (where Φ adjusts from
   exterior to interior equilibrium) involves nonlinear coupling between the
   scalar field profile and the metric.

4. **CTP consistency** — OPEN. The analysis uses the single-copy (physical-limit)
   T^Φ from Phase 1. The relationship between the Einstein solution and the
   Galley doubled-field formalism (Route B) is not addressed here.

5. **Stability of the static solution** — NOT ADDRESSED. Even if a static
   solution with f > 0 exists, its stability under perturbations must be verified.

---

## L. Explicit Nonclaims

1. The mass reduction mechanism is STRUCTURAL, not a quantitative proof that
   f(R_eq) > 0; the latter requires solving the full ODE system

2. The reclassification of the Phase V obstruction does NOT invalidate the
   Phase V theorem; the theorem is CORRECT for the constitutive ansatz

3. The Phase V theorem remains valid as a no-go for the specific constitutive
   post-Newtonian mapping; Phase 4 shows this mapping is not the full story

4. The NEC saturation ρ + p_⊥ = 0 is a property of the minimally-coupled
   scalar with this specific potential, not a general GRUT feature

5. The negative energy density ρ < 0 does NOT violate any energy condition
   that would invalidate the Penrose singularity theorem — the NEC is
   saturated (not violated) for tangential null vectors, and satisfied for
   radial null vectors

6. The modified TOV system is derived for the STATIC case only; dynamical
   collapse requires time-dependent analysis

7. The dimensional estimate τ ~ √(C/2) is ORDER-OF-MAGNITUDE only; the
   actual mass reduction depends on the full profile integration

8. The anisotropy p_r − p_⊥ = (Φ')²/h vanishes at the equilibrium core
   (Φ' = 0) and in the exterior (Φ' → 0); it is significant only in the
   transition region

9. The Bianchi consistency check confirms the MATHEMATICAL structure of the
   equations, not the physical realizability of the solution

10. The equation of state w = −1 at homogeneous equilibrium does NOT make
    the scalar field a cosmological constant — it has spatial dependence
    and dynamics away from equilibrium

11. The constitutive ansatz artifact diagnosis applies to the SPECIFIC
    post-Newtonian mapping used in Phase V; other constitutive approaches
    might or might not suffer the same limitation

12. This analysis does NOT claim that the GRUT barrier prevents horizon
    formation in general; it shows the STRUCTURAL POSSIBILITY of a
    horizon-free interior for the locked T^Φ

13. The mass reduction integrand dm/dr = 4πr²ρ_eq = −2πr²X²/τ² depends
    on X(r), which is itself determined by the gravitational configuration;
    self-consistency requires solving the coupled system

14. The boundary conditions are stated for a two-point BVP; the actual
    numerical solution may require shooting or relaxation methods

---

## Computational Artifacts

**Script:** xact/grut_einstein_tphi.wl (Parts A–J)
**Engine:** Wolfram Engine 14.x with xAct 1.2.0 / xPert 1.0.6
**Method:** xAct abstract T^Φ construction + divergence verification;
explicit component analysis and ODE derivation in plain Mathematica
**Exports:** xact/results/tphi_abstract.m, div_tphi.m,
equilibrium_eos.m, phase4_classification.m

---

## Phase 1–4 Result Lock

    Phase 1 (T^Φ):              LOCKED (ΔT = 0, Factorization Theorem)
    Phase 2 (Φ₋):              LOCKED (consistent, not attractor, IR-dominated)
    Phase 3 (h₋):              LOCKED (consistent, vacuum stable, sourced unstable)
    Phase 4 (Einstein+T^Φ):    LOCKED (ρ<0, mass reduction, metric restoration possible)
    Metric Factorization:       LOCKED (diss kernel silent in metric sector)
    Route B overall:            COMPLETE (physical-limit derived, NOT fully derived)
    Phase V obstruction:        RECLASSIFIED (constitutive ansatz artifact)
    Interior metric:            STRUCTURALLY POSSIBLE (quantitative TBD)
    Modified TOV:               DERIVED (ready for numerical solution)
