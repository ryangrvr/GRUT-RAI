# APPENDIX J — INTERIOR METRIC CLOSURE ANALYSIS

**Classification:** `interior_metric_positivity_achievable_transient_supercritical_processing`
**Date:** 2026-03-27
**Depends on:** tov_interior.py, dynamical_interior.py, covariant_interior.py, Appendix I
**Implementation:** `grut/interior_metric_closure.py`
**Tests:** `tests/test_interior_metric_closure.py`

---

## 1. EXECUTIVE DETERMINATION

> **`interior_metric_positivity_achievable_transient_supercritical_processing`**

The interior metric f(R_eq) can be driven to zero — a Killing horizon at the equilibrium radius — but only transiently, and only when the scalar field processing amplitude exceeds the natural rate by ~6.2% (A = A_crit ≈ 1.062). At this threshold the surface gravity κ_GRUT = 3/10 (in canonical units), which is exactly 3/5 of the Schwarzschild value. The implied Killing temperature T_Killing = (3/5) T_Hawking is a new, GRUT-covariant temperature candidate not previously enumerated.

---

## 2. PROBLEM STATEMENT

The target for this appendix is to determine whether the interior metric f(r) can achieve positivity at r = R_eq, the GRUT equilibrium radius, and if so under what conditions. Three prior analyses constrain the answer from different directions:

1. **Covariant interior (Appendix E / covariant_interior.py):** The naive constitutive lapse gives A_eff = -1 < 0 for all finite β_Q. A +1 correction over Schwarzschild (A_Schw = -2) is insufficient.

2. **Static TOV (tov_interior.py):** Full self-consistent equilibrium with ρ_eq < 0 gives f(R_eq) = -17.71 — far worse than Schwarzschild. The equilibrium develops a singularity at r_★ ≈ 1.023 r_s.

3. **Dynamical interior (dynamical_interior.py):** Scalar field kinetic energy (Φ̇ ≠ 0) can partially cancel the equilibrium deficit. The question is how much.

This appendix synthesises these into a three-layer deficit chain, derives the critical amplitude A_crit analytically, computes the surface gravity at the transient Killing horizon, and identifies a new temperature candidate.

---

## 3. THREE-LAYER METRIC DEFICIT CHAIN

Canonical parameters throughout: r_s = 1, M = 1/2, R_eq = 1/3, τ² = 3/2.

| Layer | Physical content | f(R_eq) | m(R_eq) | Source |
|-------|-----------------|---------|---------|--------|
| 0 | Schwarzschild reference (GR baseline) | −2 | 1/2 | Analytic |
| 1 | Constitutive lapse correction (+1) | −1 | — | covariant_interior.py |
| 2 | Static TOV equilibrium (full ρ_eq < 0) | **−17.71** | **3.118** | tov_interior.py (**locked**) |
| 3a | Dynamic, natural rate A = 1 | −2 | 1/2 | dynamical_interior.py (**locked**) |
| 3b | Dynamic, supercritical A = A_crit | **0** | **1/6** | This appendix |

### Layer 0 — Schwarzschild Reference

The vacuum Schwarzschild metric at r = R_eq:

```
f_Schw(R_eq) = 1 - 2M/R_eq = 1 - r_s/R_eq = 1 - C = -2
```

The compactness C = r_s/R_eq = 3 places R_eq deep inside the Schwarzschild radius. This is not a GRUT result; it is the baseline.

### Layer 1 — Constitutive Lapse Correction

The post-Newtonian constitutive ansatz contributes a +1 correction:

```
A_eff = A_Schw + δA = -2 + 1 = -1
δA = +1  (from β_Q/(1+β_Q) = 2/3 at C = 3)
```

This is the maximum the constitutive correction can achieve. The **Constitutive Lapse Insufficiency Theorem** (covariant_interior.py) proves that A_eff < 0 for all finite β_Q when α_vac ≤ e^{−1/2}. The +1 is real but insufficient.

### Layer 2 — Static TOV Equilibrium

Full integration of the TOV equations with equilibrium density:

```
ρ_eq(r) = -M² / (2τ²r⁴)  < 0
dm/dr = 4πr²ρ_eq < 0  (inward, mass ACCUMULATION)
```

The negative density causes mass to increase toward the centre. Integrating from R_ext = 2 inward to R_eq:

```
m(R_eq, A=0) = M + 2πM²/τ² × (1/R_eq - 1/R_ext)
             = 0.5 + 5π/6 ≈ 3.118        [locked]
f(R_eq, A=0) = 1 - 6m = 1 - 18.71 = -17.71  [locked]
```

The self-consistent static equilibrium has a singularity at r_★ ≈ 1.023 r_s; the field cannot reach R_eq in the static purely-equilibrium picture.

### Layer 3a — Dynamic at Natural Rate (A = 1)

The natural profile Φ̇(r) = A · M/(τr²) at A = 1 adds kinetic energy density:

```
ε(r) = ½Φ̇² = M²/(2τ²r⁴) = -ρ_eq(r)
```

Exact cancellation: ρ_total = ρ_eq + ε = 0 at every r. Therefore:

```
dm/dr = 0  →  m(R_eq, A=1) = M = 1/2  [locked]
f(R_eq, A=1) = 1 - 2M/R_eq = A_Schw = -2  [locked]
```

The natural kinetic rate exactly heals the mass accumulation and recovers the Schwarzschild metric — but f = -2 still corresponds to being inside the Schwarzschild radius.

### Layer 3b — Supercritical at A = A_crit

For A > 1 the kinetic term over-compensates, reducing m(R_eq) below M:

```
m(R_eq, A) = M + 2πM²(A²-1)/τ² × (1/R_ext - 1/R_eq)
           = M - (5π/6)(A²-1)
```

The Killing horizon condition f(R_eq) = 0 requires m(R_eq) = R_eq/2 = 1/6:

```
M - (5π/6)(A_crit²-1) = 1/6
(5π/6)(A_crit²-1) = 1/3
A_crit² = 1 + 2/(5π)
A_crit = √(1 + 2/(5π)) ≈ 1.062
```

This is consistent with the locked numerical value A_crit ≈ 1.06 from dynamical_interior.py tests (6.2% above natural rate).

---

## 4. SURFACE GRAVITY AT THE TRANSIENT KILLING HORIZON

### Derivation

At A = A_crit, f(R_eq) = 0 with m(R_eq) = R_eq/2. The radial derivative of f at this point:

```
df/dr|_{R_eq} = -2(dm/dr)/R_eq + 2m/R_eq²

dm/dr|_{R_eq} = 2πM²(A_crit²-1)/(τ²R_eq²)
              = 2π·(1/4)·(2/(5π)) / ((3/2)·(1/9))
              = 6/5

df/dr|_{R_eq} = [1 - 2R_eq·(6/5)] / R_eq
              = [1 - 4/5] / (1/3)
              = (1/5)·3 = 3/5
```

Surface gravity:

```
κ_GRUT = ½|f'(R_eq)| = 3/10
```

### Schwarzschild Reference

```
κ_Schw = 1/(4M) = 1/(4·½) = 1/2
```

### Ratio

```
κ_GRUT / κ_Schw = (3/10) / (1/2) = 3/5  (exact)
```

The intermediate factor that fixes this ratio is:

```
4πM²(A_crit²-1)/(τ²R_eq) = 4π·(1/4)·(2/(5π)) / ((3/2)·(1/3)) = 4/5
```

giving f'(R_eq) = (1 - 4/5)/(1/3) = 3/5, κ_GRUT = 3/10.

---

## 5. KILLING TEMPERATURE — NEW CANDIDATE

Via the standard Wald–Unruh formula T = ℏκ/(2πk_B):

```
T_Killing / T_Hawking = κ_GRUT / κ_Schw = 3/5  (exact)
```

For a reference mass M = 30 M_☉:

```
T_Hawking ≈ 2.05 × 10⁻⁹ K
T_Killing ≈ 1.23 × 10⁻⁹ K
```

### Status of T_Killing as a Temperature Candidate

This is the **sixth** temperature candidate in the GRUT program, supplementing the five identified in the thermodynamic sector:

| # | Candidate | T/T_Hawking | Origin |
|---|-----------|------------|--------|
| 1 | T_Hawking (standard) | 1 | Standard BH thermodynamics (imported) |
| 2 | T_kin ~ ω₀/(2Q) | ~Q-dependent | PDE damping analogy |
| 3 | T_bath from Drude cutoff | ~ℏ/(k_B τ₀) scale | Q2 structural match |
| 4 | T_1stlaw option (b) | 9 | Appendix I thermostatic requirement |
| 5 | T_Unruh_barrier | (TBD) | Barrier dynamics |
| **6** | **T_Killing (this appendix)** | **3/5** | **Dynamical interior metric** |

### GRUT-covariance of T_Killing

T_Killing satisfies three GRUT-covariance criteria:

1. **Derived from GRUT objects:** κ_GRUT comes from f'(R_eq) of the dynamical interior metric with locked parameters (M, R_eq, τ, A_crit).
2. **Mass-independent ratio:** T_Killing/T_Hawking = 3/5 is a pure number, independent of the black hole mass.
3. **No Hawking machinery imported:** the Wald–Unruh formula requires only the surface gravity of a metric horizon; no Hawking radiation derivation is needed.

---

## 6. TRANSIENT CAVEAT

The Killing horizon is **not permanent**. The critical processing amplitude A_crit requires Φ̇ ~ A_crit·M/(τr²), which decays as exp(−t/τ) during dynamical relaxation. The timeline:

| Time | State | f(R_eq) |
|------|-------|---------|
| t = 0 (active collapse) | Peak Φ̇, A ~ A_crit | ≈ 0 |
| 0 < t < τ | Exponential Φ̇ decay | Decreasing from 0 |
| t ≫ τ | Static equilibrium | −17.71 |

**Classification:** `metric_positivity_achievable_transient_supercritical_processing`

**Physical interpretation:** The Killing temperature T_Killing is associated with the active scalar-processing phase during and shortly after collapse infall, not with the long-time static interior. Whether this active phase persists long enough to emit radiation is a dynamical question outside the scope of this appendix.

---

## 7. SPECIAL CASE: EXTREMAL HORIZON

When the exterior matching radius R_ext → r_s = 1 (matching at the Schwarzschild surface):

```
A_crit²|_{extremal} = 1 + 1/(2π)
dm/dr|_{R_eq} → κ = 0
T_Killing → 0 (zero-temperature extremal horizon)
```

This is a self-consistency marker: when no exterior domain exists for the mass integral correction, the critical amplitude is larger (A_crit ≈ 1.077) but the resulting horizon is extremal with vanishing temperature.

---

## 8. FIRST-LAW CROSS-CHECK

From Appendix I, the first-law gap closes if the physical temperature satisfies:

```
T_1stlaw = 9 × T_Hawking  [option (b), viable]
```

The Killing temperature T_Killing = 3/5 × T_Hawking is:

```
T_Killing / T_1stlaw = (3/5) / 9 = 1/15 ≈ 0.067
```

**T_Killing does NOT close the first-law gap.** They are independent constraints:

- T_1stlaw = 9 T_Hawking is a thermostatic requirement from energy-entropy balance.
- T_Killing = 3/5 T_Hawking is a kinematic temperature from the interior metric's surface gravity.

Their coexistence as distinct candidates is not a contradiction; it reflects the temperature non-uniqueness identified in Appendix E (PASS 1, Section 3.C) and reinforces the `temperature_multiple_candidates_no_convergence` status.

---

## 9. NONCLAIMS

1. **T_Killing is NOT the physical temperature** of the GRUT interior. It is a new candidate derived from the interior metric.
2. **The transient Killing horizon is NOT permanent.** It exists only during active scalar processing.
3. **A_crit > 1 is NOT shown to be physically realised.** It defines a threshold condition.
4. **The first-law gap is NOT closed** by T_Killing. T_Killing and T_1stlaw are independent.
5. **Ghost-free status of the Galley route is NOT resolved here.** T_Killing is independent of the Galley sector.
6. **All Appendix C quantum blockers remain in force.**
7. **Hawking radiation is NOT derived.** The Wald–Unruh formula is invoked to translate κ to T; this does not constitute a Hawking radiation derivation.
8. **The information paradox is NOT addressed.**

---

## 10. SUMMARY TABLE

| Quantity | Symbol | Value | Status |
|----------|--------|-------|--------|
| Static TOV f(R_eq) | f_static | −17.71 | Locked |
| Static TOV m(R_eq) | m_static | 3.118 | Locked |
| Schwarzschild f | A_Schw | −2 | Locked |
| Constitutive lapse | A_eff | −1 | Locked |
| Natural rate f (A=1) | f(A=1) | −2 | Locked |
| A_crit (analytic) | √(1+2/(5π)) | ≈1.062 | Derived |
| A_crit (numerical) | — | ~1.06 | Locked (dynamical_interior.py) |
| f'(R_eq) at A_crit | — | 3/5 | Derived |
| κ_GRUT | — | 3/10 | Derived |
| κ_GRUT / κ_Schw | — | **3/5** (exact) | Derived |
| T_Killing / T_Hawking | — | **3/5** (exact) | Derived |
| Horizon type | — | Transient Killing | Classification |
| First-law gap closed? | — | NO (T_Killing/T_1stlaw = 1/15) | Boundary result |

---

## 11. SAFE AND UNSAFE CLAIMS

### Claims this appendix MAY safely make:

1. The dynamical interior can achieve a transient Killing horizon at R_eq with amplitude A_crit = √(1 + 2/(5π)) ≈ 1.062.
2. The surface gravity at this horizon is κ_GRUT = 3/10 in canonical units, giving κ_GRUT/κ_Schw = 3/5 exactly.
3. The Killing temperature T_Killing = (3/5) T_Hawking is a new GRUT-covariant temperature candidate.
4. T_Killing does not close the first-law gap identified in Appendix I.
5. The Killing horizon is transient; the late-time static equilibrium has f(R_eq) = −17.71.

### Claims this appendix MUST NOT make:

1. That T_Killing is the physical temperature of the GRUT interior (unproven).
2. That A_crit > 1 is dynamically realised in any specific collapse scenario (threshold, not result).
3. That the Killing horizon is permanent or stationary.
4. That the first-law gap is closed (T_Killing/T_1stlaw = 1/15 ≪ 1).
5. That Hawking radiation is derived or modified by GRUT (Wald–Unruh formula is used, not Hawking's derivation).
6. That the constitutive lapse insufficiency theorem is circumvented (it is: A_crit achieves f = 0 through dynamic kinetics, not static constitutive lapse).

---

## 12. RELATION TO APPENDIX E WARNINGS

This appendix resolves or sharpens several warnings from the PASS 1 stability audit:

| Warning | Status after Appendix J |
|---------|------------------------|
| W7: ρ_Φ < 0 with positive entropy | Sharpened: static TOV confirms ρ_eq < 0 causes mass accumulation; the transient positive-f window has ρ_total ≈ 0 at threshold |
| W5: Φ dual-use | Unresolved (out of scope for Appendix J) |
| W3: Ghost route T^Φ | T_Killing is independent of Route B/Galley; derived from metric, not Lagrangian |
| W1: τ_eff non-covariance | Not addressed (out of scope) |

The temperature non-uniqueness identified in Section 3.C of the PASS 1 audit is confirmed and deepened: T_Killing is a sixth independent candidate, and no convergence with the other five has been demonstrated.
