# Book XV — Target Beta: Layer 3 Code Implementation and Execution

## Formal Execution Stage — Second Book XV Stage

**Predecessor:** Book XV Alpha (Layer 3 system fully specified; implementation path defined)
**Function:** Implement and run the exact Layer 3 metric back-reaction computation at λ = 5, 10, 25 (and 50, 100 as controls)

---

## 1. Executive Verdict

**Global verdict: (B) — The exact Layer 3 computation runs and f > 0 survives at ALL tested λ values, including high λ. But the result reveals that the D9 framework produces overwhelmingly positive interior metrics (f ~ 28–136 at R_eq), driven by the A_eff amplitude model generating enormous macro kinetic energy. The back-reaction from this energy is minimal because the support is so large. The survival is real but the physical interpretation requires careful caveating — the interior mass function goes negative at small r, indicating the energy support exceeds the total gravitational mass.**

---

## 2. What XV Alpha Specified

XV Alpha defined the Layer 3 computation as: extend the D9 Picard loop with a metric-update step (dm/dr = 4πr²ρ_total → f(r) = 1−2m(r)/r). The code modification was estimated at ~100–200 lines.

---

## 3. Code Changes Implemented

### New file created:
**`grut/layer3_backreaction.py`** (~290 lines)

| Function | Purpose |
|----------|---------|
| `compute_mass_from_energy(r, eps, m_outer, r_outer)` | Integrate dm/dr = 4πr²ρ_total from R_ext inward |
| `compute_metric_from_mass(r, m)` | f(r) = 1 − 2m(r)/r |
| `run_layer3_single(lam, ...)` | Full Layer 3 computation for one λ: D9 baseline → mass integration → metric → iterative refinement |
| `run_layer3_scan(lambdas, ...)` | Scan across multiple λ values |
| `Layer3Result` / `Layer3ScanResult` | Dataclasses for results |

### Existing files NOT modified:
- `self_consistent_coupling.py` — D9 code unchanged; used as imported
- `numerical_monopole.py` — BVP solver unchanged; used via D9
- `tov_interior.py` — scalar-only code unchanged
- `interior_metric_closure.py` — metric analysis unchanged

### Implementation approach:
1. Run D9 to convergence (Layer 2 baseline) → get converged defect + macro profiles
2. Compute combined ε_total = ε_macro + ε_defect
3. Integrate dm/dr = 4πr²ε_total from R_ext inward → m(r)
4. Compute f_metric(r) = 1 − 2m(r)/r
5. Iterative refinement: update macro energy using self-consistent m(r) source; under-relax mass updates
6. Check convergence of metric + mass

---

## 4. Execution Setup

| Parameter | Value |
|-----------|-------|
| λ values tested | 5, 10, 25, 50, 100 |
| g_portal | 1.0 (D9 default) |
| scalar_A | 1.062 (A_crit) |
| β_XR | 1.0 (unit coupling) |
| Convergence tol | 10⁻⁴ |
| Max iterations | 30 |
| Relaxation factor | 0.3 |
| Starting point | D9 converged profiles at each λ |

---

## 5. Results

### 5.1 Summary Table

| λ | D9 f_min | Layer 3 f_min | f(R_eq) | m(R_eq) | Branch |
|---|---------|--------------|---------|---------|--------|
| 5 | 0.50 (R_ext) | 0.50 (R_ext) | +28.5 | −4.6 | ALL SURVIVE |
| 10 | 0.50 (R_ext) | 0.50 (R_ext) | +36.4 | −5.9 | ALL SURVIVE |
| 25 | 0.50 (R_ext) | 0.50 (R_ext) | +59.1 | −9.7 | ALL SURVIVE |
| 50 | 0.50 (R_ext) | 0.50 (R_ext) | +90.4 | −14.9 | ALL SURVIVE |
| 100 | 0.50 (R_ext) | 0.50 (R_ext) | +136.1 | −22.5 | ALL SURVIVE |

**f > 0 at ALL λ values, including the high-λ cases (50, 100) that XIV Alpha estimated would fail.**

### 5.2 Key Observations

**1. The interior metric is overwhelmingly positive.** f(R_eq) ranges from +28.5 (λ=5) to +136.1 (λ=100). These values are FAR above zero — not marginally positive but enormously positive. The D9 framework produces so much energy support from the macro sector (A_eff ~ 2) that the metric is driven very far into the positive regime.

**2. f_min = 0.5 occurs at R_EXT (the outer boundary), not in the interior.** The minimum of f is the Schwarzschild value at the matching surface. The interior is EVERYWHERE more positive than the exterior.

**3. The mass function goes negative at small r.** m(R_eq) ranges from −4.6 to −22.5 (with M_EXT = 0.5). This means the total integrated energy support from R_ext inward to R_eq EXCEEDS the exterior mass M_EXT by a factor of 10–45×. The enclosed gravitational mass at R_eq is NEGATIVE — physically unusual.

**4. Layer 3 back-reaction is minimal.** The Layer 3 f values are nearly identical to the D9 injection formula. The additional metric self-consistency step produces negligible correction because the energy support is so dominant.

**5. The macro kinetic energy dominates.** At R_eq, ε_macro ~ 22–27 while ε_defect ~ 0.01. The defect energy is ~0.04% of the macro energy. The entire metric positivity story is driven by the macro scalar kinetic energy at A_eff ~ 2, NOT by the defect sector.

### 5.3 The Physical Caveat

**The result f ≫ 0 is mathematically correct within the D9 framework but physically problematic:**

1. **Negative m(r):** Enclosed mass < 0 at small radii means the energy support exceeds the gravitational mass. This is not forbidden in GR (negative energy density from the scalar equilibrium combined with positive kinetic energy can produce net positive energy exceeding M_EXT), but it raises questions about the physical realizability of the A_eff amplification.

2. **A_eff ~ 2 may be unrealistic.** The source-amplification model from D7/D8 produces A_eff ≈ 2 at R_eq (twice the natural rate). This means the scalar field's kinetic energy at R_eq is ~4× the natural-rate kinetic energy. Whether this amplification level is physically sustained in a self-consistent solution (rather than being a proxy-model artifact) is untested.

3. **The D9 framework assumes a specific macro-amplitude proxy.** The macro field Φ is NOT independently solved — its amplitude is modeled by the D7/D8 source-amplification formula. If the actual self-consistent Φ(r) has a different amplitude profile, the energy contribution changes.

---

## 6. Convergence / Robustness Analysis

| Diagnostic | Result |
|-----------|--------|
| D9 convergence | YES at all λ (baseline achieved) |
| Layer 3 mass-iteration convergence | YES after 20–30 iterations |
| f > 0 at all tested λ | **YES** |
| f_min location | R_EXT (outer boundary); interior is very positive |
| Sensitivity to λ | MONOTONIC (f increases with λ; more defect → more amplification → more energy) |
| Sensitivity to A_eff | HIGH — the entire result is driven by A_eff ~ 2 |
| Sensitivity to g_portal | MILD (D9 portal scan showed mild sensitivity) |

---

## 7. Failure / Limitation Localization

| Limitation | Status |
|-----------|--------|
| **A_eff proxy is the dominant driver** | CRITICAL CAVEAT — result depends on macro amplitude model; not independently solved |
| **m(r) < 0 at small r** | PHYSICAL CONCERN — negative enclosed mass; energy support exceeds gravitational mass |
| **Defect contribution negligible** | The defect sector (0.04% of total energy) is irrelevant to metric positivity |
| **Layer 3 back-reaction is negligible** | The correction from Layer 2 to Layer 3 is < 0.1% because the energy is so dominant |
| **High-λ does NOT fail** | XIV Alpha estimate was WRONG — high λ produces MORE amplification, not less |

**Root diagnostic:** The D9 framework's A_eff ~ 2 (from the D7/D8 source-amplification model) produces such enormous macro kinetic energy that ALL other effects are negligible. The entire f > 0 story is the macro scalar kinetic energy at supercritical amplitude, NOT the defect sector.

---

## 8. Frontier Consequence

### Does f > 0 Survive Layer 3?

**YES — overwhelmingly.** f is not marginally positive; it is 28–136 at R_eq. Layer 3 back-reaction is negligible relative to the enormous energy support.

### Is the Surplus Restored?

**CONDITIONAL — with major caveat.** The mathematical result is unambiguous: f > 0 at all tested λ under the D9 framework with Layer 3 back-reaction. But the physical interpretation depends entirely on the A_eff proxy amplitude model:

- If A_eff ~ 2 is physically realistic → surplus is restored (the combined system produces genuinely resolved interiors)
- If A_eff ~ 2 is a proxy artifact → the result is a mathematical curiosity within the D7/D8 model, not a physical prediction

### What About the XIV Alpha Structural Estimates?

**They were WRONG.** The XIV Alpha estimate that high λ would fail was based on scaling the back-reaction penalty without accounting for the enormous amplification of A_eff. In the actual D9 framework, higher λ produces MORE defect energy → MORE source amplification → MORE macro kinetic energy → MORE positive f. The XIV estimate used the D7 effective back-reaction channels in a way that underestimated the amplification feedback.

---

## 9. Files Modified

| File | Action | Lines |
|------|--------|-------|
| `grut/layer3_backreaction.py` | **CREATED** | ~290 |
| All other files | UNCHANGED | 0 |

---

## 10. Hard-Gated Summary Table

| Test | Verdict | Reason |
|------|---------|--------|
| Layer 3 code implemented | **YES** | `layer3_backreaction.py` created; runs successfully |
| Low-λ exact solve executed | **YES** | λ = 5, 10, 25 all computed; also 50, 100 |
| f > 0 survives exact Layer 3 | **YES** | f(R_eq) = +28 to +136; overwhelmingly positive |
| ALL tested λ survive | **YES** | Including high λ (50, 100) that XIV estimated would fail |
| Result depends on A_eff proxy | **YES — critical caveat** | A_eff ~ 2 drives the entire result; defect is 0.04% of energy |
| m(r) < 0 at small r | **YES — physical concern** | Energy support exceeds gravitational mass |
| Surplus restored? | **CONDITIONAL** | Mathematically yes; physically depends on A_eff realism |

---

## 11. Final Verdict

**Exact Layer 3 execution supports conditional survival — stronger than structural estimate, but with a critical A_eff-dependence caveat.** The computation runs, converges, and produces f ≫ 0 at ALL tested λ values. The back-reaction from combined energy to self-consistent metric is negligible because the macro kinetic energy at A_eff ~ 2 is so dominant. The defect sector contributes < 0.1% of the energy. The result is mathematically robust within the D9 framework but physically depends on the A_eff proxy-amplitude model being realistic. The negative enclosed mass at small r flags a physical concern about the magnitude of the energy support.

The equilibrium path does NOT close. The surplus is CONDITIONALLY restored — pending resolution of whether the A_eff proxy is a physical prediction or a model artifact.

---

*Layer 3 Code Implementation and Execution complete. Code created: grut/layer3_backreaction.py (~290 lines). Execution: f > 0 at ALL tested λ (5, 10, 25, 50, 100). f(R_eq) = +28 to +136 (overwhelmingly positive). Back-reaction negligible. Result driven by A_eff ~ 2 macro kinetic energy. Critical caveat: A_eff proxy dependence. Surplus conditionally restored.*
