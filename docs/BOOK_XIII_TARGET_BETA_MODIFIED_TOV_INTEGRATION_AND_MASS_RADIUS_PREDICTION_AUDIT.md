# Book XIII — Target Beta: Modified TOV Integration and Mass-Radius Prediction Audit

## Formal Quantitative Prediction Stage — Second Book XIII Stage

**Predecessor:** Book XIII Alpha (two structural signature families survive; modified TOV integration identified as highest-leverage gap)
**Function:** Determine whether the GRUT-modified TOV system generates quantitative compact-object predictions that materially differ from GR
**Entry cost:** 16/11/1/6 (committed; GGB uncommitted)

---

## 1. Executive Verdict

**Global verdict: (B) — A partial but real quantitative compact-object phenomenology program exists. The modified TOV system is closed and structurally analyzable. Three concrete predictions emerge from structural analysis without requiring full numerical M-R curves. Full quantitative M-R curves remain uncomputed.**

The audit establishes:

**The system IS closed.** Phase 4 xAct provides: three coupled ODEs (mass, lapse, anisotropic TOV) + the Φ field equation + explicit T^Φ components. The system is fully determined for any choice of boundary conditions and source function X(r). Numerical integration is a standard ODE problem — tractable with scipy or equivalent.

**Three structural predictions survive without full numerical integration:**

**Prediction 1 — Relaxed Buchdahl bound (STRUCTURAL):** The standard Buchdahl theorem (C ≤ 8/9 for perfect fluid with ρ ≥ 0, dρ/dr ≤ 0) fails when ρ_eq < 0. The GRUT interior violates the theorem's energy-condition hypothesis. Consequence: equilibrium configurations with **C > 8/9 are structurally permitted.** The exact maximum C requires numerical integration, but the existence of ultra-compact equilibria beyond the GR bound is a theorem-level structural result.

**Prediction 2 — Two-zone compact-object architecture (STRUCTURAL):** A GRUT-modified compact object has two structural zones: an outer nuclear-matter shell (standard EOS, ρ > 0) and an inner GRUT-modified core (T^Φ sector, ρ_eq < 0 near equilibrium). The transition between zones occurs where the GRUT equilibrium condition Φ ≈ X is first satisfied — i.e., where the gravitational field is strong enough to activate the constitutive equilibrium. This two-zone structure is qualitatively distinct from: standard neutron stars (single-zone nuclear), strange stars (quark matter throughout), or hybrid stars (nuclear + quark transition). It is a new architectural class.

**Prediction 3 — Mass-deficit interior with negative effective mass contribution (QUANTIFIABLE):** In the inner zone, dm/dr = 4πr²ρ_eq < 0 — the mass function DECREASES toward the center. The total enclosed mass at the zone boundary r = R_core is LESS than the mass at the surface. This produces a characteristic mass-profile signature: m(r) increases through the outer zone (standard), then DECREASES through the inner zone (GRUT-modified). The exterior observer measures a total mass M_total = m(R_surface) that is REDUCED relative to what the outer-zone mass profile alone would predict. This is quantifiable: the mass deficit Δm = (2πX²/(3τ²))(R_core³ − R_inner³) from Phase 4 §E.

**What remains uncomputed:**

Full numerical M-R curves have NOT been generated. Producing them requires: (a) choosing a nuclear EOS for the outer zone, (b) specifying X(r) self-consistently, (c) scanning central conditions, and (d) integrating the coupled system for each. This is computationally tractable (standard ODE boundary-value problem) but has not been performed. The structural predictions above are derivable from the equations without full integration; the M-R curves require it.

---

## 2. Why Book XIII Beta Is the Correct Next Stage

XIII Alpha identified two structural signature families (compactness deviations, remnant structure) and flagged modified TOV integration as the highest-leverage gap. Beta translates the structural arguments into the tightest quantitative form achievable with the current formalism — determining what predictions are available NOW vs what requires future numerical work.

---

## 3. Restatement of the Book XIII Alpha Result

**Structural families A (compactness) and D (remnant) survive** with direct links to the D1–D10 singularity-resolution surplus. **Conditional families B (maximum mass) and C (tidal deformability) require computation.** The highest-leverage gap: the modified TOV system is closed but unintegrated across central-condition space.

---

## 4. Formal Modified TOV System

### 4.1 Metric Ansatz

Static, spherically symmetric:
```
ds² = −e^{2ν(r)} dt² + (1 − 2m(r)/r)^{−1} dr² + r² dΩ²
```

where m(r) is the mass function and ν(r) is the lapse function.

### 4.2 Matter Variables

**Outer zone (r > R_core):** Standard nuclear matter with EOS p = p(ρ). Isotropic.

**Inner zone (r < R_core):** GRUT T^Φ sector. Variables: Φ(r), and the source X(r).

### 4.3 T^Φ Components (from Phase 4 §B)

```
ρ_Φ(r) = (1/2)(Φ')²·h(r) + Φ²/(2τ²) − Φ·X(r)/τ

p_r,Φ(r) = (1/2)(Φ')²·h(r) − Φ²/(2τ²) + Φ·X(r)/τ

p_⊥,Φ(r) = −(1/2)(Φ')²·h(r) − Φ²/(2τ²) + Φ·X(r)/τ
```

where h(r) = 1/(1 − 2m(r)/r) and Φ' = dΦ/dr.

### 4.4 Modified TOV Equations (from Phase 4 §D)

```
dm/dr = 4πr² ρ_total(r)                                          (mass)

dν/dr = [m + 4πr³ p_r,total] / [r(r − 2m)]                     (lapse)

dp_r/dr = −(ρ_total + p_r,total) dν/dr + (2/r)(p_⊥ − p_r)     (anisotropic TOV)
```

In the outer zone: ρ_total = ρ_nuclear, p_r = p_⊥ = p_nuclear (isotropic). Standard TOV.

In the inner zone: ρ_total = ρ_Φ, p_r = p_r,Φ, p_⊥ = p_⊥,Φ. Anisotropic TOV.

### 4.5 Φ Field Equation (Static)

From ∇^a T^Φ_{ab} = 0:
```
Φ'' + (2/r + ν' − (1/2)h'/h) Φ' + h·(Φ/τ² − X(r)/τ) = 0
```

This is a second-order ODE for Φ(r), coupled to m(r) and ν(r) through h(r).

### 4.6 Source Function X(r)

In the D1–D10 framework: X(r) = M/r² (Schwarzschild gravitational source). In the self-consistent TOV: X depends on the metric, which depends on T^Φ, creating a nonlinear feedback loop.

**Two tractable approaches:**

(a) **Fixed-background approximation:** Use X(r) = m(r)/r² as the gravitational source (computed from the outer-zone mass profile). This is the D1–D10 approach extended to TOV — a Picard-iteration strategy where the mass profile determines X, which determines Φ, which corrects the mass profile.

(b) **Fully self-consistent integration:** Solve the coupled system (m, ν, p_r, Φ) simultaneously as a four-variable ODE system. This is computationally more demanding but is a standard numerical BVP.

### 4.7 Boundary Conditions

**Center (r → 0):** m(0) = 0; Φ(0) = Φ_c (central value, a free parameter); Φ'(0) = 0 (regularity).

**Surface (r = R_surface):** p_r(R_surface) = 0 (defines the surface); match to exterior Schwarzschild: m(R_surface) = M_total, ν matches to −(1/2)ln(1 − 2M/R).

**Zone boundary (r = R_core):** Continuity of m, ν, and p_r across the nuclear-to-GRUT transition.

### 4.8 Closure Status

**The system IS closed.** Four ODEs (m, ν, p_r, Φ) with: (a) T^Φ components providing ρ, p_r, p_⊥ algebraically from Φ, Φ', m, r; (b) nuclear EOS providing p_nuclear(ρ_nuclear) in the outer zone; (c) boundary conditions at center and surface; (d) source X determined self-consistently. This is a standard nonlinear ODE boundary-value problem. Numerically tractable.

---

## 5. Parameter / EOS Strategy

### 5.1 What Is Fixed by Canon

| Parameter | Value | Source | Status |
|-----------|-------|--------|--------|
| τ | ~10⁻⁵ s (compact-interior scale) | XII Gamma; Appendix G | Structurally motivated; not observationally fixed |
| V(Φ) = Φ²/(2τ²) | From constitutive equation | Phase 4 | Canon |
| J = X/τ | Source coupling | Phase 4 | Canon |
| T^Φ components | As specified in §4.3 | Phase 4 | Canon |
| D1–D10 results | f_min = +0.37 to +0.46 | D1–D10 | Canon (Schwarzschild background) |

### 5.2 What Must Be Chosen for Integration

| Choice | Options | Impact | Status |
|--------|---------|--------|--------|
| Nuclear EOS | SLy, APR, BSk family, etc. | Determines outer-zone M-R; well-studied | Standard NS physics |
| X(r) prescription | Fixed-background or self-consistent | Determines GRUT interior coupling strength | Tractable choice |
| Central Φ_c | Free parameter to scan | Determines GRUT interior activation | Scan parameter |
| Zone boundary R_core | Where Φ ≈ X is first satisfied | Determines the extent of GRUT interior | Self-consistently determined |

### 5.3 Robustness Assessment

The STRUCTURAL predictions (Buchdahl-bound relaxation, two-zone architecture, mass-deficit interior) are **EOS-independent** — they follow from the sign of ρ_eq < 0 regardless of the nuclear EOS. The QUANTITATIVE predictions (exact M-R curves, maximum mass, tidal deformability) are **EOS-dependent** — they require a specific nuclear EOS choice. This is standard in neutron-star physics; all M-R predictions are EOS-dependent. The GRUT modification is an ADDITIONAL structural feature on top of the EOS dependence.

---

## 6. Mass-Radius / Compactness Analysis

### 6.1 Structural Prediction 1 — Relaxed Buchdahl Bound

**The Buchdahl theorem** (1959) proves C = 2M/R ≤ 8/9 for static, spherically symmetric perfect-fluid stars with ρ ≥ 0 and dρ/dr ≤ 0.

**GRUT violation of the hypothesis:** In the inner zone, ρ_eq = −X²/(2τ²) < 0. The Buchdahl proof does not apply. Therefore: **equilibrium configurations with C > 8/9 are not excluded by Buchdahl.**

**This is a theorem-level result.** It does not require numerical integration — it follows directly from the sign of ρ_eq. The Buchdahl bound is relaxed (the proof's hypothesis is violated), and ultra-compact equilibria become structurally possible.

**How much beyond 8/9?** This requires integration. The exact maximum C depends on the nuclear EOS, the GRUT interior extent, and the mass-deficit magnitude. But the EXISTENCE of C > 8/9 configurations is a structural prediction.

### 6.2 Structural Prediction 2 — Two-Zone Architecture

A GRUT-modified compact object has:
- **Outer zone:** Nuclear matter (ρ > 0, standard EOS, dm/dr > 0)
- **Inner zone:** GRUT T^Φ (ρ_eq < 0, w = −1, dm/dr < 0)
- **Transition:** At R_core, where the gravitational field is strong enough for the GRUT equilibrium to activate

The two-zone structure produces a characteristic mass profile:
```
m(r): increases through outer zone → peaks at R_core → DECREASES through inner zone
```

This is qualitatively different from all standard compact-object models (where m(r) monotonically increases toward the center).

### 6.3 Structural Prediction 3 — Mass-Deficit Interior

The Phase 4 §E result gives the mass deficit:
```
Δm = (2πX²/(3τ²))(R_core³ − R_inner³)
```

For canonical parameters (Phase 4 §F): the fractional mass reduction required for metric positivity is Δm/M ≥ 2/3 (at compactness C = 3). This is a LARGE effect — the GRUT interior removes ~2/3 of the gravitational mass from the deepest region.

The exterior observer measures:
```
M_total = M_outer_zone − Δm_inner_zone
```

This is LESS than M_outer_zone alone. The reduction produces a specific M-R relation: for given outer-zone properties, the total mass is shifted downward by the GRUT interior deficit.

### 6.4 Qualitative M-R Branch Structure

Without full integration, the qualitative branch structure can be inferred:

- **Standard branch:** At low central density (GRUT interior not activated), the M-R curve follows standard nuclear-EOS predictions. This is the GR-compatible branch.
- **GRUT-modified branch:** At high central density (GRUT interior activated), the mass deficit reduces M. This creates a branch where M DECREASES with increasing central density — the mass-deficit effect overwhelms the outer-zone mass gain. This branch has LOWER mass but HIGHER compactness than the standard branch at the same central density.
- **Ultra-compact branch (if it exists):** If the GRUT interior is extensive enough, configurations with C > 8/9 may appear as a new branch in the M-R diagram. This branch would represent the GRUT ultra-compact remnant class.

**Whether the ultra-compact branch is stable, metastable, or unstable requires turning-point analysis — which requires numerical integration.**

---

## 7. Stability / Maximum-Mass Analysis

### 7.1 Turning-Point Criterion

Standard TOV stability uses the turning-point criterion: along a sequence of increasing central density, the configuration is stable if dM/dρ_c > 0 (mass increases with central density) and unstable if dM/dρ_c < 0. The maximum mass occurs at the turning point dM/dρ_c = 0.

For the GRUT-modified system: the mass-deficit effect introduces a NEGATIVE dM contribution from the inner zone. This could create a new turning point at higher central density — potentially a NEW stability window beyond the standard maximum mass.

### 7.2 Structural Expectation

**Standard branch:** Follows nuclear-EOS turning-point criterion. Maximum mass at M_max (EOS-dependent: ~2.0–2.5 M_sun for stiff EOS).

**GRUT-modified branch:** Mass deficit reduces M. If the reduction is gradual, the sequence extends to higher compactness before becoming unstable. If the reduction is abrupt (strong GRUT activation), the sequence may develop a new turning point.

**Whether a new stability window exists requires numerical M(ρ_c) curves — not yet computed.**

### 7.3 Stability Assessment

| Configuration | Stability status | Basis |
|--------------|-----------------|-------|
| Standard branch (low density) | **STABLE (standard)** | Standard turning-point criterion |
| Near maximum mass (standard) | **UNSTABLE** above turning point | Standard |
| GRUT-modified branch | **UNKNOWN** — stability requires numerical M(ρ_c) | Not computed |
| Ultra-compact branch (C > 8/9) | **UNKNOWN** | Not computed; requires dynamical perturbation analysis |

---

## 8. Phenomenological Comparison Readiness

### 8.1 Comparison Handles

| Observable | GRUT prediction available? | Comparison-ready? | Data source |
|-----------|--------------------------|------------------|-------------|
| Mass-radius curve M(R) | **STRUCTURAL** (branch existence; qualitative shape) / NOT QUANTITATIVE | **NOT YET** (requires numerical curves) | NICER |
| Maximum mass M_max | **CONDITIONAL** (may be shifted; requires integration) | **NOT YET** | Radio pulsars |
| Compactness C > 8/9 | **STRUCTURAL** (Buchdahl bound relaxed) | **PARTIALLY** (existence predicted; exact C unknown) | X-ray timing |
| Tidal deformability Λ | **NOT COMPUTED** (perturbation theory needed) | **NOT YET** | LIGO/Virgo |
| Mass-deficit profile m(r) | **STRUCTURAL** (non-monotonic mass profile) | **NOT DIRECTLY OBSERVABLE** (internal structure) | — |

### 8.2 Assessment

The structural predictions (Buchdahl relaxation, two-zone architecture, mass-deficit interior) are **real GRUT-native predictions** with no GR counterpart. But they are not yet **comparison-ready** in the quantitative sense required for statistical comparison with astrophysical data. The gap is: numerical M-R curves from the closed system.

---

## 9. Hard-Criteria Evaluation

| Criterion | Assessment |
|-----------|-----------|
| 1. TOV system closure | **PASS** — four coupled ODEs, all components specified; boundary conditions defined |
| 2. Quantitative output existence | **PARTIAL** — three structural predictions derived; full M-R curves uncomputed |
| 3. Traceability to demonstrated surplus | **PASS** — all predictions trace to ρ_eq < 0 from Phase 4 / D1–D10 |
| 4. Distinctness from GR | **PASS** — relaxed Buchdahl bound, two-zone architecture, non-monotonic mass profile all absent in GR |
| 5. Robustness vs EOS | **STRUCTURAL predictions are EOS-independent; QUANTITATIVE curves are EOS-dependent** | Mixed |
| 6. Phenomenological specificity | **MODERATE** — predictions are specific but not yet comparison-ready |
| 7. Worth follow-up | **YES** — numerical integration is tractable and would produce comparison-ready M-R curves |

---

## 10. Failure / Limitation Localization

| Limitation | Severity | Resolution |
|-----------|----------|-----------|
| **Full numerical M-R curves not computed** | **KEY GAP** | Integrate the §4 system for standard nuclear EOS + GRUT inner zone; scan central conditions |
| **X(r) self-consistency not fully solved** | MODERATE | Fixed-background (Picard iteration, as in D9) is tractable; full self-consistent integration is harder but standard |
| **Zone-transition physics approximate** | MODERATE | The nuclear-to-GRUT transition requires specifying how the GRUT equilibrium activates; currently heuristic |
| **Stability of GRUT branch unknown** | SIGNIFICANT | Requires turning-point analysis from numerical M(ρ_c); or dynamical perturbation study |
| **Tidal deformability unformulated** | SIGNIFICANT | Requires even-parity perturbation theory for anisotropic NEC-saturating interior |

**The limitations are all COMPUTATIONAL, not STRUCTURAL.** The physics is defined; the equations are closed; the predictions are derived structurally. What remains is numerical integration — a standard computational task.

---

## 11. Frontier Consequence Audit

### Does the Singularity-Resolution Surplus Now Support a Real Quantitative Program?

**YES.** The closed TOV system with three structural predictions (relaxed Buchdahl, two-zone architecture, mass-deficit interior) constitutes a real quantitative compact-object program. The predictions are GRUT-native, distinct from GR, and structurally traceable to the demonstrated surplus.

### Does This Materially Strengthen the Frontier?

**YES.** Before XIII Beta: the frontier had one demonstrated surplus (singularity resolution) with two structural signature families identified but unquantified. After XIII Beta: the surplus has three concrete structural predictions, a closed integration system, and a defined numerical pathway to comparison-ready M-R curves.

### Does This Change Bridge-Worthiness?

**NOT YET — but the pathway is now sharper.** If the numerical M-R curves produce distinctive, falsifiable predictions (e.g., a specific compactness window or mass-radius branch not producible by any standard EOS), the bridge-commitment case strengthens substantially. The gap between "structural prediction" and "falsifiable M-R curve" is one numerical computation.

---

## 12. False-Positive Audit

| False-positive | Applies? | Reason |
|---------------|---------|--------|
| Numerically integrated but observationally empty | **NO** — structural predictions are specific (Buchdahl relaxation, two-zone, mass deficit) | Not empty; specific predictions exist |
| EOS-fitting without surplus | **Guard against** — nuclear EOS is an input; the GRUT surplus is the inner-zone ρ < 0 | Must separate EOS freedom from GRUT prediction |
| Compactness rhetoric without stable solutions | **PARTIALLY APPLIES** — C > 8/9 is structurally permitted but stability is unknown | Must not claim stability until verified |
| "Comparison-ready" without observable map | **APPLIES** — not yet comparison-ready for NICER/LIGO | Must not claim comparison readiness |
| M-R novelty as parameter artifact | **NO** — the non-monotonic mass profile follows from ρ < 0, not parameter choice | Structurally rooted |

---

## 13. GRUT-RAI TOV State-Model Requirements

Specified in the companion state-model document.

---

## 14. Program Consequence

### Does a Real Quantitative Compact-Object Prediction Program Survive?

**YES — partially.** Three structural predictions are derived from the closed system. Full numerical M-R curves are the gap. The program is real, defined, and computationally tractable.

### What Exact Predictions Are Strongest?

1. **Relaxed Buchdahl bound** (C > 8/9 permitted) — STRUCTURAL; theorem-level
2. **Two-zone architecture** (nuclear outer + GRUT inner with ρ < 0) — STRUCTURAL; qualitatively new
3. **Non-monotonic mass profile** (m(r) decreases in inner zone) — QUANTIFIABLE from Phase 4 §E

### What Should No Longer Be Claimed?

- "Full M-R curves computed" — they are not
- "Comparison-ready for NICER/LIGO" — not yet
- "Stability of ultra-compact branch demonstrated" — not verified
- "Black-hole replacement" — the GRUT remnant is a different object, not a replacement claim

### What Is the Next Correct Stage?

**Numerical GRUT TOV Integration.** This would be a computational stage (possibly Program W3 or Book XIII Gamma) that actually integrates the §4 system for a representative nuclear EOS, scans central conditions, and produces M(R) curves. This is the single highest-leverage computation the frontier program can perform — it converts three structural predictions into comparison-ready quantitative output.

---

## 15. Hard-Gated Summary Table

| Test | Verdict | Reason |
|------|---------|--------|
| Modified TOV system explicitly defined | **YES** | Four coupled ODEs; all components specified (Phase 4); boundary conditions defined |
| Quantitative outputs generated | **PARTIAL** | Three structural predictions derived; full M-R curves require numerical integration |
| Non-GR compact-object branch survives | **YES (structural)** | Buchdahl bound relaxed; two-zone architecture; mass-deficit interior; all absent in GR |
| Compactness / M-R phenomenology identified | **YES** | C > 8/9 permitted; non-monotonic m(r); qualitative branch structure inferred |
| Comparison-ready pathway exists | **CONDITIONAL** | System is closed and integrable; but integration not performed |
| Frontier strengthened by quantitative program | **YES** | Three structural predictions + closed integration system + defined numerical pathway |
| Book XIII Beta changes frontier status | **YES** | Frontier gains three concrete predictions + defined computation target |

---

## 16. Final Verdict

**A partial but real quantitative compact-object phenomenology program exists.** The modified TOV system is closed (four coupled ODEs from Phase 4). Three structural predictions are derived: relaxed Buchdahl bound (C > 8/9 permitted from ρ_eq < 0), two-zone compact-object architecture (nuclear outer + GRUT inner), and non-monotonic interior mass profile (dm/dr < 0 in inner zone). Full numerical M-R curves require integration that is tractable but unperformed. The frontier is strengthened with concrete predictions and a defined computational pathway.

---

*Modified TOV Integration and Mass-Radius Prediction Audit complete. System closed. Three structural predictions derived. Relaxed Buchdahl bound (C > 8/9). Two-zone architecture. Non-monotonic mass profile. Full M-R curves require numerical integration (tractable; defined). Frontier strengthened.*
