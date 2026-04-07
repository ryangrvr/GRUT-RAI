# Program F — Stage F4: NP5 Final Novelty Audit (Gravitational Phase-Transition Claim)

**Predecessor:** F3 (h4_repackaging). Sole remaining novelty candidate: NP5.

---

## 1. NP5 Formalization

### Claim (theorem-like form)

```
ASSUMPTIONS:
  NP5-A1. A scalar entropy-density field s with first-order dissipative dynamics
           on a curved background: τ₁ u^μ ∇_μ s = h(s_eq(g) − s) − κψ
  NP5-A2. An auxiliary constitutive mode ψ with cubic-saturating dynamics:
           τ₂ u^μ ∇_μ ψ = εs + (σ−1)ψ − νψ³
  NP5-A3. Parameters in a bistable regime (σ > 1, appropriate κ, ε, ν).
  NP5-A4. The equilibrium target s_eq(g) depends on the local Ricci scalar:
           s_eq = β + αR.

OBSERVABLE CONSEQUENCE:
  For a range of curvature values R, the system admits TWO stable equilibrium
  entropy densities s*_A(R) ≠ s*_B(R), separated by an unstable saddle point.
  A spatial or temporal transition in R can drive the system from one
  entropy-density phase to the other, producing a FIRST-ORDER PHASE
  TRANSITION in the local entropy density as a function of curvature.

FALSIFIER:
  If the two attractors merge (become degenerate) for all curvature values
  in the physical range, or if the bistability requires parameter tuning
  that has no physical basis, NP5 is not a robust prediction.
```

### Minimal model realizing NP5

The coupled system from C1/C2:

```
τ₁ ṡ = a(s_eq(R) − s) − κψ
τ₂ ψ̇ = εs + (σ−1)ψ − νψ³
```

At the C2 bistable parameters (σ = 2.0, κ = 0.3, ε = 0.2, ν = 1.0): two stable fixed points confirmed numerically (basin fractions 46%/54%).

As R varies: s_eq(R) = β + αR changes. The fixed-point positions s*_A(R) and s*_B(R) shift. At some critical R = R_c, the two attractors may merge (saddle-node bifurcation), producing a curvature-driven phase transition.

---

## 2. Genericity Test

### Question: Does the NP5 bistability require GRUT-specific structure, or does it appear in any two-field dissipative system?

**Test:** Compare NP5 to the generic two-field dissipative system (D1 class):

```
Generic:
  τ₁ ẋ = F(x, y, λ)
  τ₂ ẏ = G(x, y, λ)

where λ is an external control parameter.
```

**Standard theory of bifurcations:** For a generic two-dimensional ODE system with a control parameter λ:

- **Saddle-node bifurcation** (two fixed points merge and annihilate) is GENERIC — it occurs in codimension-1 (a single parameter must be tuned to reach the bifurcation point). This is a standard result (Guckenheimer & Holmes 1983).

- **Pitchfork bifurcation** (one fixed point splits into three) is GENERIC for systems with a Z₂ symmetry. Without symmetry, it unfolds into a saddle-node. Also codimension-1.

- **Cusp catastrophe** (the boundary between bistable and monostable regions in a two-parameter family) is GENERIC for any system with two control parameters and a cubic nonlinearity. This is a standard catastrophe-theory result (Thom 1972).

**Comparison to NP5:** The NP5 system has:
- Two fields (s, ψ)
- One control parameter (R, which enters through s_eq = β + αR)
- Cubic nonlinearity (νψ³)
- No special symmetry (ε ≠ 0 breaks s → −s symmetry)

This is EXACTLY the setting of the generic cusp catastrophe. The bistability and its curvature-driven phase transition are:
- Codimension-1 in R (a single curvature value R_c separates monostable from bistable regions)
- Generic for any two-field system with cubic saturation and external control

**Countermodel (generic, non-GRUT):**

Take any two-variable Langevin system with cubic nonlinearity and an external driving parameter λ:

```
τ₁ ẋ = (λ − x) − κy
τ₂ ẏ = εx + (σ−1)y − νy³
```

This is IDENTICAL to NP5 with the substitution λ = s_eq(R). The bistability, the phase transition at λ_c, and the basin structure are ALL properties of the generic system, not of the curvature coupling. The curvature merely provides the control parameter λ. Any other external parameter (temperature, pressure, chemical potential, electric field, ...) would produce the same phase structure.

**Result: NP5 bistability is GENERIC.** It is a standard cusp catastrophe in a two-field dissipative system with cubic nonlinearity. The curvature-driven aspect is cosmetic: R enters only as an external control parameter, identical in function to any other external parameter.

---

## 3. Gravity-Specificity Test

### Question: Does curvature coupling change the phase structure in a way not reproducible by non-gravitational parameter rescaling?

**Test:** In NP5, the curvature R enters through s_eq = β + αR. The fixed-point equations are:

```
a(β + αR − s*) − κψ* = 0
εs* + (σ−1)ψ* − νψ*³ = 0
```

Eliminating s*: s* = (β + αR) − κψ*/a. Substituting into the second equation yields a cubic in ψ* with coefficients that depend on (β + αR).

**The variable u ≡ β + αR enters as a single scalar control parameter.** Any external field that provides the same scalar control u produces identical phase structure. The cubic in ψ* depends on u, not on R separately.

**Invariant signature test:** Is there any observable that depends on R in a way that CANNOT be reproduced by a non-gravitational u?

- **Phase boundary R_c:** The critical curvature at which the saddle-node occurs. R_c = (u_c − β)/α, where u_c is the generic critical value of u. R_c is just u_c expressed in curvature units. No gravity-specific content.

- **Hysteresis width ΔR:** The curvature range over which bistability exists. ΔR = Δu/α. Again, just the generic width rescaled. No gravity-specific content.

- **Basin fractions:** Depend on initial conditions, not on whether the control parameter is R or something else. No gravity-specific content.

- **One-loop selection (Model W):** |det(J)| at each attractor depends on the Jacobian, which depends on the local parameters (a, κ, ε, σ, ν) and on u = β + αR. The determinant varies with u, hence with R. But the VARIATION is smooth and generic — it is the same as any system with a smoothly varying control parameter.

**Result: NO gravity-specific invariant found.** The curvature R enters as an external control parameter with no structural distinction from any other external scalar. The phase transition is curvature-PARAMETRIZED but not curvature-SPECIFIC.

**The one scenario where gravity IS specific:**

If the phase transition occurs near a BLACK HOLE HORIZON, where R changes rapidly over short distances, the spatial gradient in R could produce a DOMAIN WALL between the two entropy-density phases. This domain wall would be a surface where the entropy density jumps between s*_A and s*_B, located at the critical curvature R_c. Such a gravitational entropy domain wall has no direct analogue in non-gravitational systems because it is sourced by spacetime curvature gradients, not by externally imposed field gradients.

**Status: POTENTIALLY NOVEL (domain wall near horizons) but in the UNSAFE regime** (strong curvature, near horizon = Book A UNSAFE zone). The domain wall prediction cannot be made within the declared controlled regime. It would require extending the theory to moderate/strong curvature — which is outside Program F's scope.

---

## 4. Observable Novelty Test

| # | Observable | Novel? | Measurability | Discriminating power |
|---|-----------|:------:|:-------------:|:-------------------:|
| OB1 | Entropy bistability at fixed curvature (two stable s* values) | **NON-NOVEL.** Generic cusp catastrophe. Any two-field system with cubic saturation has this. | LOW (requires identifying s with a measurable entropy density AND observing the two states) | ZERO (generic) |
| OB2 | Curvature-driven entropy phase transition (s jumps as R crosses R_c) | **NON-NOVEL as a phenomenon.** Standard first-order transition with curvature as control parameter. Equivalent to any externally driven transition. | LOW (requires varying R while measuring s — practically: observing different gravitational environments) | ZERO (R is just a control parameter) |
| OB3 | Entropy domain wall near BH horizon | **POTENTIALLY NOVEL.** A surface of entropy-density discontinuity at R = R_c, located at a specific radius from the BH. No standard EIT counterpart. | VERY LOW (requires near-horizon observations; outside controlled regime) | MEDIUM (if observable, unique to curvature-sourced bistability) |
| OB4 | Hysteresis in cosmological entropy as universe expands (R decreases over cosmic time) | **NON-NOVEL.** Standard hysteresis in a bistable system with slowly varying control parameter. Equivalent to any cosmological phase transition (QCD, electroweak). | LOW (requires cosmological model + entropy-density measurement) | ZERO (generic) |
| OB5 | One-loop attractor preference depends on R | **NON-NOVEL.** Generic: one-loop free energy depends on all parameters, including the control parameter. | LOW | ZERO |

### Summary

| Novelty status | Count | Items |
|:---:|:---:|---|
| NON-NOVEL | 4 | OB1, OB2, OB4, OB5 |
| POTENTIALLY NOVEL (but unsafe regime) | 1 | OB3 (entropy domain wall near horizons) |
| CONFIRMED NOVEL | 0 | — |

---

## 5. Final NP5 Classification

### **np5_generic_effect**

**Confidence: 0.80**

**Evidence:**

1. The bistability is a standard cusp catastrophe in a two-field system with cubic nonlinearity (genericity test: countermodel exists, identical structure without gravity).

2. The curvature R enters as a generic external control parameter with no structural distinction from temperature, pressure, or any other scalar (gravity-specificity test: no invariant found).

3. All observables in the controlled regime (OB1, OB2, OB4, OB5) are non-novel — they are standard properties of generic bistable open systems.

4. The one potentially novel observable (OB3: entropy domain wall near horizons) is in the UNSAFE regime (strong curvature) and cannot be predicted within the declared scope.

**What NP5 IS:** A specific instance of a generic cusp catastrophe, parametrized by spacetime curvature instead of by temperature or pressure. The curvature parametrization is PHYSICALLY INTERESTING (it connects thermodynamic phase transitions to gravitational environments) but MATHEMATICALLY GENERIC (the same phase structure occurs for any control parameter).

**What NP5 is NOT:** A novel gravitational effect, a GRUT-specific prediction, or a signature that distinguishes GRUT from the generic D1 class. It is one more confirmation that GRUT's constitutive sector is a specific instance of known dissipative dynamics.

---

## 6. Program-Level Closure Impact

### Since np5_generic_effect:

NP5 does not provide novelty sufficient to keep Program F open. The last remaining potential novelty candidate has been classified as generic.

### Recommend: **CLOSE PROGRAM F.**

**What Program F accomplished:**

| Stage | Result |
|:-----:|--------|
| F0/F1 | USL is robust (Sector 3 decoupled from Sectors 1-2). USL cannot discriminate class members. |
| F2-A | Class-level experimental protocol: 900 runs, 9 configurations, 3 kill signals, decision engine. |
| F2-B | Φ identification narrowed: H4 (entropy density) > H1 (geometric relaxation) > H3 (fundamental scalar) >> H2 (excluded). |
| F3 | H4 is EIT in curved spacetime. Repackaging of known thermodynamics. Two qualifications: CTP derivation (formal), NP5 (ambiguous). |
| F4 | NP5 is generic cusp catastrophe. Not GRUT-specific. One potentially novel observable (domain wall) is in unsafe regime. |

**Program F's permanent output:**

1. The USL experimental protocol (F2-A) — operational, class-level, ready for hardware maturity.
2. The Φ identification ranking (F2-B) — H4 as the physically motivated identification.
3. The honest equivalence finding (F3/F4) — GRUT's constitutive sector IS extended irreversible thermodynamics in a gravitational field.

**What is NOT a Program F output:**

- Novel physics beyond standard EIT + Newtonian gravity.
- Class-member selection.
- ToE-level closure.

---

## Gate Table

| Gate | Criterion | Status | Evidence |
|:----:|-----------|:------:|---------|
| **F4-G1** | NP5 formalized with falsifier | **PASS** | Section 1: assumptions, observable consequence, falsifier. Minimal model specified (C1/C2 coupled system). |
| **F4-G2** | Genericity test completed | **PASS** | Section 2: generic cusp catastrophe. Countermodel: any two-field cubic system with external control. |
| **F4-G3** | Gravity-specificity assessed | **PASS** | Section 3: R enters as generic control parameter u = β + αR. No invariant gravity-specific signature in controlled regime. Domain wall (OB3) is potentially novel but in unsafe regime. |
| **F4-G4** | Observable novelty table complete | **PASS** | Section 4: five observables tested. 4 non-novel, 1 potentially novel (unsafe regime). 0 confirmed novel. |
| **F4-G5** | Classification + closure recommendation | **PASS** | np5_generic_effect (confidence 0.80). Recommend close Program F. |

## Decision Token

### **close_ProgramF**

**Rationale:**

1. The sole remaining novelty candidate (NP5) is classified as a generic effect (cusp catastrophe with curvature as control parameter).
2. No confirmed novel observable exists in the controlled regime.
3. The one potentially novel observable (entropy domain wall near horizons) is in the unsafe regime and outside Program F's scope.
4. All Program F objectives have been met: robustness assessed, protocol designed, Φ identified, novelty tested.
5. Continuing would be diminishing returns — no untested novelty candidate remains.

**Program F is closed.**

---

*Program F Stage F4 complete. Decision: close_ProgramF. NP5 classification: np5_generic_effect (confidence 0.80). Bistability is standard cusp catastrophe; curvature is a generic control parameter. One potentially novel observable (domain wall) in unsafe regime. Zero confirmed novel physics in controlled regime. Program F permanent outputs: USL experimental protocol, Φ identification ranking, EIT equivalence finding. All gates pass (5/5). Program F is closed.*
