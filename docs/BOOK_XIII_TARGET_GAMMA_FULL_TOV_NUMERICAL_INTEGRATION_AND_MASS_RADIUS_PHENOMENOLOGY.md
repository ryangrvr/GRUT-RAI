# Book XIII — Target Gamma: Full TOV Numerical Integration and Mass-Radius Phenomenology

## Formal Numerical Production Stage — Third Book XIII Stage

**Predecessor:** Book XIII Beta (closed TOV system; three structural predictions; numerical M-R gap identified)
**Function:** Perform numerical integration of the GRUT-modified TOV system; determine whether structural predictions survive as quantitative compact-object phenomenology
**Entry cost:** 16/11/1/6 (committed; GGB uncommitted)

---

## 1. Executive Verdict

**Global verdict: (A) — The numerical integration reveals a CRITICAL CORRECTION to the program's gravity-side surplus narrative. The "demonstrated singularity resolution" is not a permanent equilibrium feature — it is a transient effect during dynamic supercritical processing that decays on timescale τ. The static equilibrium WORSENS the interior metric. The structural predictions from XIII Alpha/Beta must be substantially revised.**

The existing numerical code (`grut/tov_interior.py` + `grut/interior_metric_closure.py`) already contains the full integration results. They were locked in the canon but NOT propagated into the Book XI–XIII frontier narrative. The results:

### The Static-Equilibrium Scalar-Only TOV (tov_interior.py — LOCKED)

| τ | m(R_eq) | f(R_eq) | Δm/M | Verdict |
|---|---------|---------|------|---------|
| 0.50 | 16.21 | −96.25 | +31.42 | CATASTROPHICALLY WORSE |
| 1.00 | 4.43 | −25.56 | +7.85 | MUCH WORSE |
| 1.22 (canonical) | 3.12 | **−17.71** | +5.24 | **MUCH WORSE than A_Schw = −2** |
| 2.00 | 1.48 | −7.89 | +1.96 | WORSE |
| 5.00 | 0.66 | −2.94 | +0.31 | WORSE |
| 10.0 | 0.54 | −2.24 | +0.08 | SLIGHTLY WORSE |

**At static equilibrium (Φ = X, Φ̇ = 0), the scalar field makes the interior MUCH WORSE.** The negative ρ_eq causes mass to ACCUMULATE inward (not reduce), driving f to −17.71 at canonical parameters — far below the Schwarzschild value of −2. The Phase 4 sign interpretation ("mass DECREASES toward center") was INCORRECT. The tov_interior.py code CORRECTS this.

### The Five-Layer Interior Structure (interior_metric_closure.py — LOCKED)

| Layer | f(R_eq) | Mechanism | Status |
|-------|---------|-----------|--------|
| 1. Schwarzschild (GR) | −2.0 | Pure GR baseline | LOCKED |
| 2. Constitutive correction | −1.0 | Phase V post-Newtonian correction | LOCKED |
| 3. **Static TOV (scalar only)** | **−17.71** | **rho_eq < 0 → mass accumulation → WORSENS** | **LOCKED — MUCH WORSE** |
| 4. Dynamic natural rate (A=1) | −2.0 | Kinetic energy exactly cancels equilibrium deficit | LOCKED |
| 5. **Supercritical (A > A_crit)** | **→ 0** | **Kinetic overshoot > equilibrium deficit → metric approaches 0** | **LOCKED — TRANSIENT** |

**The metric positivity result (f → 0) occurs ONLY at Layer 5** — during transient supercritical processing with Φ̇ ~ A_crit·M/(τr²) where A_crit ≈ 1.062. This processing DECAYS on timescale τ (the constitutive relaxation time). After one τ, f returns to −17.71 (static TOV value).

**The transient caveat (from interior_metric_closure.py — LOCKED):**
- Classification: `metric_positivity_achievable_transient_supercritical_processing`
- Decay timescale: O(τ)
- Late-time f: −17.71
- Mechanism: "Φ̇ decays as exp(−t/τ) during dynamical relaxation. The kinetic energy surplus that drives f(R_eq) to 0 dissipates on the relaxation timescale."
- Nonclaim: "A_crit > 1 is NOT shown to be physically realized; it is a threshold"

---

## 2. Why This Changes Everything

### What XIII Alpha/Beta Claimed

- "Singularity resolution: DEMONSTRATED (D1–D10; f_min > 0)"
- "ρ_eq < 0 reduces interior mass"
- "Metric positivity restored across tested parameter range"
- "Three EOS-independent structural predictions: relaxed Buchdahl, two-zone architecture, non-monotonic mass profile"

### What the Numerical Code Actually Shows

1. **Static equilibrium ρ_eq < 0 INCREASES mass inward** (tov_interior.py Result 1 — LOCKED sign correction). f goes to −17.71, not positive.

2. **Metric positivity requires DYNAMIC supercritical processing** (Layer 5) with A > A_crit ≈ 1.062. This is a TRANSIENT state during active relaxation, not a static equilibrium.

3. **The transient decays on timescale τ.** After the processing ends, f returns to the static TOV value of −17.71. There is no permanent singularity-free equilibrium in the scalar-only sector.

4. **The D1–D10 two-component result (f_min > 0) is from the COMBINED scalar + defect system on a FIXED Schwarzschild background.** It demonstrates that the defect sector (Component B, η²/r²) can provide ENOUGH positive energy to overcome the scalar sector's worsening — but only in the specific D1–D10 framework with Picard proxy closure.

5. **The structural predictions from XIII Beta (Buchdahl relaxation, two-zone architecture, non-monotonic mass profile) relied on "ρ_eq < 0 reduces mass" — which is the Phase 4 sign error.** The actual mass profile is MONOTONICALLY INCREASING inward (m(r) increases as r decreases), not non-monotonic.

### Revised Surplus Status

| Claimed surplus | Previous status | Revised status |
|----------------|----------------|---------------|
| Singularity resolution (static equilibrium) | DEMONSTRATED | **INCORRECT — static equilibrium WORSENS metric** |
| Singularity resolution (transient supercritical) | Not distinguished | **TRANSIENT — decays on timescale τ; A_crit not shown physically realized** |
| Singularity resolution (combined A+B on fixed background) | DEMONSTRATED (D1–D10) | **CONDITIONAL — proxy closure; fixed background; defect sector needed** |
| Relaxed Buchdahl bound | STRUCTURAL | **INCORRECT — relies on Phase 4 sign error** |
| Two-zone architecture | STRUCTURAL | **INCORRECT — scalar-only sector worsens, not improves** |
| Non-monotonic mass profile | STRUCTURAL | **INCORRECT — mass monotonically increases inward** |

---

## 3. What the D1–D10 Result Actually Is

The D1–D10 program operates differently from the scalar-only TOV:

1. It uses a **fixed Schwarzschild background** (not self-consistent metric)
2. It adds the **O(3) defect sector** (Component B: hedgehog with ε ~ η²/r²) as ADDITIONAL positive-energy support
3. It uses **Picard proxy closure** (not full coupled field equations)
4. Under these conditions, the COMBINED A+B energy support IS sufficient to make f > 0

**The D1–D10 result IS a legitimate numerical demonstration** — but it is a demonstration of the COMBINED two-component system on a FIXED background with proxy closure. It is NOT a demonstration of the GRUT scalar sector alone resolving singularities. The scalar sector alone makes things worse.

### What D1–D10 Actually Demonstrated

- That the DEFECT sector (hedgehog Component B) provides crucial positive-energy support
- That the COMBINED energy (kinetic + defect − equilibrium) CAN produce f > 0
- That the result holds across tested λ range {5, 10, 25, 50, 100, 200}
- That Picard iteration converges (D9)

### What D1–D10 Did NOT Demonstrate

- That a self-consistent TOV with the full coupled system produces permanent equilibrium with f > 0
- That the scalar sector alone contributes positively
- That the result survives without the Schwarzschild background assumption
- That A_crit > 1 is physically realized in a dynamic collapse

---

## 4. Formal Corrected Numerical System

### 4.1 The Scalar-Only Modified TOV (tov_interior.py)

**System:** dm/dr = 4πr²ρ_eq, where ρ_eq = −X²/(2τ²) < 0 and X = m/r² (self-consistent).

**Result:** dm/dr < 0 (mass decreases with increasing r, meaning mass INCREASES toward center). At canonical parameters: m(R_eq) = 3.12 (vs M = 0.5). f(R_eq) = −17.71 (vs A_Schw = −2).

**Self-consistent ODE:** 1/m(r) = 1/M + (2π/τ²)(1/R_ext − 1/r). This has a SINGULARITY at r* = 1.023 r_s where m → ∞.

**Conclusion:** The scalar equilibrium does NOT resolve singularities. It makes them worse.

### 4.2 The Dynamic Supercritical Processing (interior_metric_closure.py)

**System:** Φ̇ = A·M/(τ·r²) provides kinetic energy ε_kin = (1/2)Φ̇² = A²M²/(2τ²r⁴). This kinetic contribution is POSITIVE and can overwhelm the negative ρ_eq.

**At A = 1:** ε_kin exactly cancels ρ_eq. f recovers to Schwarzschild (−2).
**At A = A_crit ≈ 1.062:** ε_kin exceeds ρ_eq by enough to make f = 0 (horizon threshold).

**Transient:** The processing decays as exp(−t/τ). After one relaxation time, Φ̇ → 0 and f → −17.71 (static value). Metric positivity is TEMPORARY.

### 4.3 The D1–D10 Combined System

**Additional support:** O(3) hedgehog defect with ε_defect ~ η²/r². This is Component B, providing PERMANENT positive-energy support (not transient).

**Combined:** ε_total = ε_scalar + ε_defect. The defect contribution is large enough (for tested λ values) to make f > 0 even at static equilibrium — on the fixed Schwarzschild background.

**The gap:** Whether this combined system produces f > 0 on a SELF-CONSISTENT (not fixed Schwarzschild) background is not tested.

---

## 5. Mass-Radius / Compactness Outputs (Corrected)

### The Scalar-Only TOV Produces NO Ultra-Compact Equilibria

The scalar-only modified TOV generates M-R behavior that is WORSE than GR, not better:
- Mass accumulates inward → total enclosed mass increases → compactness INCREASES → but f becomes MORE negative, not less
- There are no stable ultra-compact equilibria from the scalar sector alone
- The Buchdahl bound is NOT relaxed by the scalar sector — it is violated in the wrong direction (f more negative, not less)

### The Combined System May Produce Ultra-Compact Objects — But Only with Defect Support

If the full D1–D10 two-component system (scalar + defect) is integrated self-consistently as a TOV, the defect sector's positive energy COULD support ultra-compact equilibria. But this integration has NOT been performed. The D1–D10 result on a fixed background is SUGGESTIVE but NOT a self-consistent TOV solution.

---

## 6. Stability / Branch Analysis (Corrected)

**The scalar-only branch is UNSTABLE.** The self-consistent scalar-only ODE has a singularity at r* ≈ 1.023 r_s. No smooth static solution exists. The scalar sector alone cannot support a stable compact object beyond GR.

**The transient processing "branch" is not a static equilibrium.** It is a dynamic state during active relaxation. It does not appear on an M-R diagram (which plots static equilibria).

**The D1–D10 combined branch is CONDITIONAL.** It exists on a fixed Schwarzschild background with proxy closure. Its survival on a self-consistent background is untested.

---

## 7. Hard-Criteria Evaluation (Revised)

| Criterion | Previous (XIII Beta) | Revised (XIII Gamma) |
|-----------|---------------------|---------------------|
| System integrated | STRUCTURAL (uncomputed) | **COMPUTED (tov_interior.py — LOCKED)** |
| Quantitative outputs | PARTIAL (structural predictions) | **COMPUTED — but they CONTRADICT the surplus narrative** |
| Traceability to surplus | PASS | **FAIL — the "surplus" relied on a sign error** |
| Distinctness from GR | PASS (Buchdahl relaxed) | **REVERSED — scalar sector makes things WORSE than GR** |
| Robustness | EOS-independent | **N/A — the basic mechanism is wrong for the scalar-only sector** |
| Comparison readiness | CONDITIONAL | **NOT APPLICABLE — no favorable predictions to compare** |
| Worth follow-up | YES | **YES — but for the COMBINED system (scalar + defect), not scalar-only** |

---

## 8. Frontier Consequence Audit

### The Surplus Portfolio Must Be Revised

| Surplus | Previous status | Revised status |
|---------|----------------|---------------|
| 1. Singularity resolution (scalar) | DEMONSTRATED | **INCORRECT — scalar worsens interior** |
| 1'. Singularity resolution (transient) | Not distinguished | **TRANSIENT — decays on timescale τ** |
| 1''. Singularity resolution (combined A+B) | DEMONSTRATED (D1–D10) | **CONDITIONAL — fixed background; proxy closure; defect sector required** |
| 2. Cosmological regulator | CONDITIONAL/NARROWED | UNCHANGED (independent of compact-interior mechanism) |
| 3. GW modification | ABSENT | UNCHANGED |

### The Frontier Is WEAKENED, Not Killed

The D1–D10 result IS real numerical work showing f > 0 in the combined system. The defect sector IS part of the GGB architecture. The result survives as a CONDITIONAL demonstration on a fixed background. But the claim "singularity resolution demonstrated" was overstated — it should have always been "singularity resolution demonstrated in the combined scalar+defect system on a fixed Schwarzschild background with proxy closure."

### What Remains

- The D1–D10 combined result: **CONDITIONAL** (proxy closure + fixed background)
- The scalar-only TOV: **WORSENS the interior** (locked numerical result)
- The transient supercritical processing: **REAL but TEMPORARY** (decays on τ)
- The cosmological regulator: **UNCHANGED** (independent of this correction)
- The full self-consistent combined TOV: **NEVER COMPUTED** (the actual gap)

---

## 9. False-Positive Audit (Self-Correcting)

| Previous claim | Status | Correction |
|---------------|--------|-----------|
| "ρ_eq < 0 reduces interior mass" | **PHASE 4 SIGN ERROR** | ρ_eq < 0 INCREASES interior mass (tov_interior.py locked correction) |
| "Singularity resolution demonstrated" | **OVERSTATED** | Transient supercritical + D1–D10 combined on fixed background; not permanent equilibrium |
| "Relaxed Buchdahl bound" | **INCORRECT** | Scalar sector violates Buchdahl in the wrong direction |
| "Two-zone architecture" | **INCORRECT** | Scalar-only interior WORSENS; not a "support zone" |
| "Non-monotonic mass profile" | **INCORRECT** | Mass MONOTONICALLY INCREASES inward |
| "Three EOS-independent structural predictions" | **ALL THREE INCORRECT** for scalar-only sector | — |

This self-correction is one of the most important results in the entire program. The canon's own locked numerical code CONTRADICTS the surplus narrative that was built on it. The program's integrity requires acknowledging this.

---

## 10. GRUT-RAI Numerical TOV State-Model Requirements

Specified in the companion state-model document.

---

## 11. Program Consequence

### Does a Real Quantitative Compact-Object Prediction Program Survive?

**NOT in the form previously claimed.** The scalar-only predictions (Buchdahl relaxation, two-zone architecture, non-monotonic mass profile) are all based on a sign error and are INCORRECT. The surviving content is:

1. **D1–D10 combined (scalar + defect) result:** f > 0 on fixed Schwarzschild background with proxy closure. CONDITIONAL. The FULL self-consistent combined TOV has never been computed.

2. **Transient supercritical processing:** Metric positivity during active relaxation (A > A_crit). REAL but TEMPORARY. Decays on timescale τ.

### What Should No Longer Be Claimed?

- "Singularity resolution DEMONSTRATED" as a permanent equilibrium feature — it is transient (scalar) or conditional on proxy closure (combined)
- "ρ_eq < 0 reduces interior mass" — it INCREASES mass (tov_interior.py locked correction)
- "Relaxed Buchdahl bound" — incorrect (scalar sector worsens compactness)
- "Two-zone architecture" — incorrect (scalar interior is not a support zone)
- "Non-monotonic mass profile" — incorrect (mass monotonically increases inward)
- "Three EOS-independent structural predictions" — all three are based on the sign error

### What Is the Correct Next Step?

**The program must decide:**

1. **Integrate the FULL combined (scalar + defect) TOV self-consistently.** This is the actual gap. If f > 0 survives on a self-consistent background, the surplus is restored (conditional on the defect sector). If it doesn't, the singularity-resolution surplus fails entirely.

2. **OR: Acknowledge the corrected status and revise the frontier narrative.** The frontier's demonstrated surplus is weaker than claimed. The D1–D10 result is conditional. The scalar-only sector worsens the interior. The program should state this honestly.

Either path is viable. What is NOT viable is continuing to claim "singularity resolution demonstrated" without acknowledging the sign correction and the transient/conditional nature of the result.

---

## 12. Hard-Gated Summary Table

| Test | Verdict | Reason |
|------|---------|--------|
| Modified TOV system numerically integrated | **YES** | tov_interior.py — LOCKED; already in canon |
| Quantitative branch families generated | **YES — but they CONTRADICT the surplus** | Scalar sector worsens interior; f = −17.71 |
| Non-GR compact-object branch survives | **NO (scalar-only); CONDITIONAL (combined A+B)** | Scalar alone worsens; combined needs self-consistent TOV |
| Compactness / M-R phenomenology identified | **CORRECTED — previous predictions INCORRECT** | Sign error in mass profile; Buchdahl NOT relaxed |
| Comparison-ready pathway exists | **NO** (for scalar-only); **CONDITIONAL** (for combined) | Must integrate combined system first |
| Frontier strengthened | **NO — frontier WEAKENED by numerical correction** | Previous surplus claims were overstated |
| Book XIII Gamma changes frontier status | **YES — CRITICAL CORRECTION** | The program's strongest surplus is weaker than claimed |

---

## 13. Final Verdict

**No real quantitative compact-object prediction program survives in the form previously claimed.** The numerical integration (already locked in canon as tov_interior.py) shows that the scalar-only modified TOV WORSENS the interior metric (f = −17.71 vs Schwarzschild f = −2). The "demonstrated singularity resolution" was based on: (a) a Phase 4 sign error about mass reduction, (b) transient supercritical processing that decays on timescale τ, and (c) the D1–D10 combined scalar+defect system on a fixed Schwarzschild background with proxy closure. The three "EOS-independent structural predictions" from XIII Beta (Buchdahl relaxation, two-zone architecture, non-monotonic mass profile) are ALL INCORRECT for the scalar-only sector.

The D1–D10 combined result (f > 0 with defect sector) remains a legitimate CONDITIONAL demonstration, but it requires the defect sector and has not been verified on a self-consistent background. The frontier is WEAKENED, not killed — but its strongest surplus must be REVISED from "demonstrated" to "conditional on the combined system and proxy closure."

This is one of the most important corrections in the program. The canon's own locked code contradicts the narrative. Honesty requires acknowledging this.

---

*Full TOV Numerical Integration and Mass-Radius Phenomenology complete. CRITICAL CORRECTION: scalar-only TOV WORSENS interior (f = −17.71; mass accumulates inward). Phase 4 sign interpretation was incorrect. "Demonstrated singularity resolution" is actually transient/conditional. Three structural predictions from XIII Beta are ALL INCORRECT. D1–D10 combined result survives as conditional. Frontier weakened. Program must decide: integrate combined system self-consistently, or revise frontier narrative.*
