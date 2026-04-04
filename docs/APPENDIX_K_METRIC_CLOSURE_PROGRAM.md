# APPENDIX K — INTERIOR METRIC CLOSURE PROGRAM

**Classification:** `metric_closure_requires_supercritical_kinetic_or_nonnative_component_b__no_static_grut_native_closure_in_tested_catalog`
**Date:** 2026-03-28
**Depends on:** interior_metric_closure.py (Appendix J), metric_deficit.py (Phase 6C), dynamical_interior.py (Phase 6B), tov_interior.py (Phase 6), covariant_interior.py (Phase V), route_b_component_b.py, barrier_action_sector.py
**Implementation:** `grut/metric_closure_program.py`
**Tests:** `tests/test_metric_closure_program.py`

---

## 1. EXECUTIVE DETERMINATION

> **`metric_closure_requires_supercritical_kinetic_or_nonnative_component_b__no_static_grut_native_closure_in_tested_catalog`**

This determination is **computed**, not predetermined.  The module builds a catalog of every GRUT-native energy-density source that could in principle contribute to the interior metric, integrates the mass equation for each, and applies three Boolean tests.  The verdict strings are assigned from the Boolean outcomes inside the test functions.

Three focal questions are answered:

| Question | Verdict |
|----------|---------|
| Q1. What covariant structure supplies the missing Component B (1/r² source)? | `no_grut_native_static_source_provides_component_b__kinetic_1r4_only` |
| Q2. Can the barrier-supported region admit a true timelike lapse at R_eq in a static configuration? | `static_timelike_lapse_not_achievable_from_grut_native_sources__requires_supercritical_kinetic_or_nonnative_1r2_support` |
| Q3. What field equation closure condition turns the constitutive ansatz into a real interior metric? | `killing_condition_requires_supercritical_kinetic_A_crit_or_nonnative_component_b__no_static_grut_native_closure_exists` |

---

## 2. CONTEXT AND MOTIVATION

Appendices I and J established two hard boundary results:

- **Appendix I:** The first-law gap is structural — the ratio R = 1.209 is fixed by Q = β_Q/α_vac alone and cannot be closed by any single temperature candidate from the current set.
- **Appendix J:** A transient Killing horizon exists at R_eq when A ≥ A_crit ≈ 1.062; T_Killing = (3/5)T_Hawking; the static equilibrium gives f(R_eq) = −17.71.

Appendix K asks the complementary covariant question: **what static or stationary structure would need to be present to achieve f(R_eq) ≥ 0?**  This is not a new simulation but a structural audit of every source in the T^Φ catalog.

Phase 6C (metric_deficit.py) established that the minimal energy-density source for a Killing horizon requires two components:

- **Component A:** ε_A ~ 1/r⁴ (kinetic energy density or equilibrium density)
- **Component B:** ε_B ~ 1/r² (spatial topology / hedgehog defect energy)

The deficit that Component B must supply (after Component A kinetic cancellation at A = 1) is:

```
Δ = M_EXT - R_eq/2 = 1/2 - 1/6 = 1/3   (canonical units)
```

This appendix asks whether any GRUT-native source provides Component B, or whether alternative closure paths exist.

---

## 3. CANDIDATE SOURCE CATALOG

Canonical parameters: r_s = 1, M = 1/2, R_eq = 1/3, τ² = 3/2, R_ext = 2.

### Mass integral formula

For a source ε(r) = coeff/r^n the enclosed mass contribution is:

```
Σ = ∫_{R_eq}^{R_ext} 4π r² ε(r) dr

  n ≠ 3:  Σ = 4π·coeff / (3-n) · [R_ext^{3-n} − R_eq^{3-n}]
  n = 3:  Σ = 4π·coeff · ln(R_ext/R_eq)
```

A **positive Σ** means the source reduces m(R_eq) toward R_eq/2 (helping toward f = 0).

### Six tested candidates

| # | Name | Profile | Power | GRUT-native | Static | Sign in barrier | Σ (canonical) | Component B? |
|---|------|---------|-------|-------------|--------|-----------------|---------------|-------------|
| 1 | ρ_eq | −M²/(2τ²r⁴) | 4 | Yes | Yes | Negative | −5π/6 ≈ −2.618 | No |
| 2 | ε_kin (A=1) | +M²/(2τ²r⁴) | 4 | Yes | **No** (Φ̇ ≠ 0) | Positive | +5π/6 ≈ +2.618 | No |
| 3 | V_Q effective | −M²/(2τ²r⁴) | 4 | Yes | Yes | Negative | −5π/6 ≈ −2.618 | No |
| 4 | Gradient ½f(Φ')² | 2fM²/r⁶ | 6 | Yes | Yes | Negative (f < 0) | Negative | No |
| 5 | O(3) hedgehog | η²/r² | 2 | **No** | Yes | Positive | +5/6 ≈ +0.833 | **Yes** |
| 6 | Route B g_- | Unknown | — | Partial | Unknown | Unknown | NaN | Unknown |

### Key catalog observations

**Sources 1, 3, 4** — all GRUT-native static sources in the catalog have negative signs in the barrier region. They worsen the metric deficit, not improve it.

**Source 2 (kinetic)** — the only GRUT-native positive source is not static. At A = 1 it exactly cancels ρ_eq; at A = A_crit ≈ 1.062 it over-compensates and achieves the transient Killing horizon (Appendix J). Its radial power is 4 (Component A), not 2 (Component B).

**Source 5 (hedgehog)** — provides the correct 1/r² profile and positive sign, but is **not GRUT-native**. D13 (tetrad sector), D14 (tensor completion), and D15 (Weyl curvature coupling) all close the GRUT-native derivation routes for the O(3) sector.

**Source 6 (g_-)** — the pre-projection Route B g_- sector is unresolved. Post-projection, Route B collapses to Route C (1/r⁴; insufficient). The pre-projection energy density has not been computed in closed form; the catalog cannot rule this source in or out.

---

## 4. COMPONENT B ANALYSIS

### Point closure (f(R_eq) = 0 after A=1 kinetic cancellation)

After the kinetic source at A = 1 exactly cancels ρ_eq, the remaining deficit is:

```
Δ = M - R_eq/2 = 1/3
```

A 1/r² source with coefficient η² satisfies the Killing condition if:

```
4π η²_point (R_ext − R_eq) = Δ = 1/3
η²_point = (1/3) / [4π · (5/3)] = 1/(20π) ≈ 0.01592
```

### Profile closure (f(r) = 0 globally, from static baseline)

From metric_deficit.py (Phase 6C), the global closure condition forces dm/dr = 1/2 everywhere, requiring:

```
ε_min = |ρ_eq| + η²_profile / r²
η²_profile = 1/(8π) ≈ 0.03979   [COMP_B_COEFF_GLOBAL]
```

### Comparison

```
η²_point  = 1/(20π)  ≈ 0.01592   (point closure, after A=1 kinetic)
η²_profile = 1/(8π)  ≈ 0.03979   (global closure, from static baseline)

η²_point / η²_profile = (1/(20π)) / (1/(8π)) = 8/20 = 2/5
```

Point closure requires 2/5 of the global profile closure coefficient. They differ because:
- Point closure: uses A=1 kinetic to zero Component A, then asks how much 1/r² is needed for the residual.
- Profile closure: asks for a 1/r² source that simultaneously provides Component A AND closes the global metric profile without kinetic assistance.

### Achievability

| Closure route | Achievable? | Source | GRUT-native? | Static? |
|---------------|-------------|--------|--------------|---------|
| Static 1/r² | No (from tested catalog) | O(3) hedgehog (if available) | No (D13/D14/D15) | Yes |
| Dynamic kinetic A ≥ A_crit | Yes (Appendix J) | ε_kin, A-supercritical | Yes | No (transient) |

---

## 5. LAPSE SIGN TEST

The numerical lapse sign test integrates the mass equation for every positive, GRUT-native, static source in the catalog.

**Result:** Zero positive GRUT-native static sources exist in the catalog. The numerical integration using all static GRUT sources (ρ_eq + V_Q effective) gives:

```
max_f_from_static_GRUT_sources << 0   (consistent with f ≈ -17.71 scale)
static_nonneg_achieved = False
```

The **Lapse Insufficiency Theorem** (covariant_interior.py) already proves that the naive constitutive correction gives A_eff < 0 for all finite β_Q. The lapse sign test extends this to the full tested catalog of GRUT-native static sources: none provides the positive enclosed mass needed for f(R_eq) ≥ 0.

The dynamic (kinetic) route achieves f = 0 transiently at A = A_crit, confirming the Appendix J result.

---

## 6. CLOSURE CONDITION TEST

Four scenarios are tested against the Killing horizon condition m(R_eq) = R_eq/2 = 1/6:

| Scenario | m(R_eq) | f(R_eq) | Satisfies Killing? | Notes |
|----------|---------|---------|-------------------|-------|
| A = 0 (static equilibrium) | 3.118 | −17.71 | No | Locked: tov_interior.py |
| A = 1 (natural kinetic) | 1/2 | −2 | No | Cancels ρ_eq; recovers Schwarzschild |
| A = A_crit (supercritical) | 1/6 | ≈ 0 | **Yes** | Transient Killing horizon (Appendix J) |
| Component B (η²_point) | 1/6 | ≈ 0 | **Yes** | Static; NOT GRUT-native |

### Monotonicity

```
f(A=0) < f(A=1) < f(A=A_crit):
  −17.71 < −2 < 0
```

### Closure condition formula

```
Killing horizon:  m(R_eq) = R_eq/2
                  ⟺  f(R_eq) = 0
                  ⟺  Σ_positive = M - R_eq/2 = 1/3
```

where Σ_positive is the net positive mass integral from all sources.

---

## 7. VERDICT ASSIGNMENT

Verdicts are assigned by `assign_verdicts()` from Boolean outcomes — not predetermined.

```python
# Q1: any GRUT-native static 1/r^2 positive source?
q1 = VERDICT_Q1["not_found"]   # because achievable_statically = False

# Q2: can static GRUT achieve f(R_eq) >= 0?
q2 = VERDICT_Q2["not_achievable"]  # because static_nonneg_achieved = False

# Q3: which scenario satisfies Killing condition?
q3 = VERDICT_Q3["kinetic_only"]   # because kinetic_Acrit_satisfies = True
                                   # and static_grut_satisfies = False

# Executive: from Q2 + Q3
executive = (
    "metric_closure_requires_supercritical_kinetic_or_nonnative_component_b__"
    "no_static_grut_native_closure_in_tested_catalog"
)
```

### Sensitivity to catalog changes

The verdict is **catalog-conditional**, not a universal no-go theorem. If a GRUT-native source with profile 1/r² and positive Σ were added to the catalog:
- `achievable_statically` would become True
- Q1 would switch to `"grut_native_static_1r2_source_found__component_b_provided"`
- Q2 would switch to `"static_timelike_lapse_achievable_from_grut_native_sources"`
- Executive would change accordingly

The unresolved g_- sector (Source 6) is an explicit open door: the verdict cannot be upgraded to a universal theorem until that sector is computed.

---

## 8. RELATION TO UPSTREAM RESULTS

### From Appendix J (interior_metric_closure.py)

| Quantity | Appendix J value | Appendix K usage |
|----------|-----------------|-----------------|
| A_crit = √(1 + 2/(5π)) | ≈ 1.062 | Closure condition Scenario 3; cross-checked |
| f(R_eq) at A=A_crit | = 0 | Killing horizon confirmation |
| m(R_eq) at A=A_crit | = R_eq/2 | Consistent with eta^2_point calculation |
| T_Killing/T_Hawking | = 3/5 | Independent of Appendix K closure question |

### From Phase 6C (metric_deficit.py)

| Quantity | Phase 6C value | Appendix K usage |
|----------|----------------|-----------------|
| COMP_B_COEFF = 1/(8π) | Locked | η²_profile; ratio computation |
| No GRUT profile provides Comp. B | Locked | Consistent with catalog verdict |

### From Phase V (covariant_interior.py)

| Result | Appendix K relation |
|--------|---------------------|
| Lapse Insufficiency Theorem | Extended: covers constitutive correction (static); Appendix K covers full static catalog |
| A_eff = −1 | Layer 1 baseline; below Killing threshold by 1 unit |

### From route_b_component_b.py

| Result | Appendix K relation |
|--------|---------------------|
| Post-projection Route B = Route C (1/r⁴) | Consistent with Source 2 (kinetic) verdict |
| g_- sector: UNRESOLVED | Source 6 in catalog; verdict cannot be finalized |

---

## 9. NONCLAIMS

1. **This appendix does NOT claim that any GRUT-native source achieves f(R_eq) ≥ 0 statically.** The test computes this; the verdict follows from the computation.
2. **The verdicts are catalog statements**, not universal no-go theorems. They hold for the six tested sources. A future GRUT-native 1/r² source would change Q1 and Q2.
3. **The g_- sector (Route B pre-projection) is unresolved.** No verdict can be made about it. The executive determination would need revision if this sector is computed.
4. **Component B (O(3) hedgehog) is shown to work algebraically but is not GRUT-native.** D13/D14/D15 close the derivation routes.
5. **The dynamic Killing horizon (A = A_crit) is transient.** It is not a static equilibrium. It lasts ~τ during active scalar processing.
6. **All Appendix C quantum blockers remain in force.**
7. **η²_point ≠ η²_profile.** Point closure after A=1 kinetic and global static closure have different requirements. They are both valid conditions for their respective problems.

---

## 10. FORBIDDEN CLAIMS

The following claims are explicitly prohibited and will fail the test suite if asserted:

1. `grut_native_static_source_achieves_f_nonneg_at_R_eq` — not established
2. `component_b_is_grut_native` — D13/D14/D15 close all derivation routes
3. `g_minus_sector_resolved` — unresolved per route_b_component_b.py
4. `permanent_killing_horizon_from_grut_native_sources` — transient only
5. `catalog_is_exhaustive_no_go` — catalog statement, not universal theorem
6. `appendix_c_blockers_overridden` — quantum blockers remain
7. `hawking_radiation_derived` — Wald–Unruh formula used; not Hawking's derivation

---

## 11. SUMMARY TABLE

| Quantity | Symbol | Value | Status |
|----------|--------|-------|--------|
| Deficit after A=1 kinetic | Δ | 1/3 | Analytic |
| η² for point closure | η²_point | 1/(20π) ≈ 0.01592 | Derived |
| η² for global closure | η²_profile | 1/(8π) ≈ 0.03979 | Locked (metric_deficit.py) |
| Ratio point/profile | — | 2/5 | Derived |
| GRUT-native static 1/r² source | — | **None in catalog** | Computed (Q1) |
| max f(R_eq) from static GRUT | — | **<< 0** | Computed (Q2) |
| Killing satisfied by A=0 | — | No (f = −17.71) | Computed |
| Killing satisfied by A=1 | — | No (f = −2) | Computed |
| Killing satisfied by A=A_crit | — | **Yes (f ≈ 0, transient)** | Computed (Q3) |
| Killing satisfied by Comp. B | — | Yes (not GRUT-native) | Computed (Q3) |
| g_- sector status | — | **Unresolved** | Inherited |
| Q1 verdict | — | not_found | Computed |
| Q2 verdict | — | not_achievable | Computed |
| Q3 verdict | — | kinetic_only | Computed |
| Executive | — | (see Section 1) | Computed |

---

## 12. RELATION TO APPENDIX E WARNINGS

| Warning | Status after Appendix K |
|---------|------------------------|
| W5: Φ dual-use | Unresolved (out of scope for Appendix K) |
| W3: Ghost route T^Φ | g_- sector remains unresolved; Appendix K documents this explicitly as Source 6 |
| W9: O(3) sector hand-insertion | Confirmed: hedgehog provides Component B but is not GRUT-native (D13/D14/D15) |
| W8: γ-coupling sign | Unresolved (out of scope) |
| W1: τ_eff non-covariance | Unresolved (out of scope) |

Temperature non-uniqueness is unchanged: T_Killing = (3/5)T_Hawking remains the sixth candidate, independent of the Component B verdict.
