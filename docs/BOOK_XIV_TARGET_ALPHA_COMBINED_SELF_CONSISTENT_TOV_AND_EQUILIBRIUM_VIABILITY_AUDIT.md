# Book XIV — Target Alpha: Combined Self-Consistent TOV and Equilibrium Viability Audit

## Formal Equilibrium-Survival Computation Stage — First Book XIV Stage

**Predecessor:** Book XIII Terminal (corrected frontier; 0 demonstrated + 2–3 conditional; Track 1 prioritized)
**Function:** Determine whether the D1–D10 combined metric positivity survives when self-consistency is extended beyond the proxy/fixed-background level
**Entry cost:** 16/11/1/6 (committed; GGB uncommitted)

---

## 1. Executive Verdict

**Global verdict: (B) — The equilibrium path survives conditionally. The D9 self-consistent Picard iteration ALREADY constitutes the strongest available self-consistency test, and it produces f > 0 across the full tested parameter range. But one critical layer of self-consistency — metric back-reaction from the combined energy content — remains uncomputed. The equilibrium path is alive but the proxy-to-exact gap is precisely localized.**

The audit reveals that the question "does D1–D10 f > 0 survive on a self-consistent background?" decomposes into THREE DISTINCT LAYERS of self-consistency, of which TWO are already resolved and ONE remains open:

### Three Layers of Self-Consistency

| Layer | What it self-consistently resolves | Status | f_min result |
|-------|-----------------------------------|--------|-------------|
| **Layer 1: Additive (D6)** | Scalar + defect as independent sources on fixed Schwarzschild background | **COMPUTED** (D6) | f > 0 for λ ≥ 25 at A=1.0; ALL λ at A=A_crit |
| **Layer 2: Portal-coupled defect (D9)** | Defect profile under portal feedback from scalar proxy field; Picard iteration | **COMPUTED** (D9) | f > 0: ALL λ ∈ {5,10,25,50,100,200}; f_min = +0.37 to +0.46; shifts constructive |
| **Layer 3: Full metric back-reaction** | Einstein equations with combined T^(scalar) + T^(defect) determine g_μν self-consistently | **NOT COMPUTED** | UNKNOWN |

**The key finding:** D9 already provides substantial self-consistency — the defect profile is NOT frozen but is computed under portal feedback with convergent Picard iteration. What D9 does NOT do is let the combined energy content (scalar + defect + portal) back-react on the metric itself. The metric remains the external Schwarzschild solution throughout D1–D10.

**Why Layer 3 matters but may not be catastrophic:**

The D7 gravitational back-reaction analysis showed that the gravitational penalty from the defect energy is OVERWHELMED by the source amplification:

> "Source amplification overwhelms gravitational penalty by ~12.7×" (D7 §6.2)

The back-reaction channel (α_BR) is destructive but WEAK compared to the constructive channel (β_XR). This provides a structural argument — not proof — that full metric back-reaction is unlikely to eliminate the positive-metric result. The argument: if the destructive channel is 12.7× weaker than the constructive channel in the D7 effective treatment, the full self-consistent metric is unlikely to reverse the sign.

**However:** This is an ARGUMENT, not a COMPUTATION. The full metric back-reaction could in principle:
- Modify the background metric enough to change the defect profile
- Alter the scalar equilibrium behavior (which is adverse in the scalar-only sector)
- Create nonlinear feedback loops not captured by the D7 linear-amplitude model

**Classification:** The equilibrium path SURVIVES conditionally. Two of three self-consistency layers are computed (D6 additive, D9 portal-coupled). One layer remains (metric back-reaction). The structural argument from D7 suggests the result is robust, but this is not proof.

---

## 2. Why Book XIV Alpha Is the Correct Next Stage

Book XIII Terminal identified Track 1 (combined self-consistent TOV) as the highest-leverage next computation. The decisive question: does D1–D10 f > 0 survive without fixed-background dependence? This audit determines exactly how much self-consistency has ALREADY been computed (more than XIII recognized), exactly what gap remains, and whether the structural evidence supports optimism or concern.

---

## 3. Restatement of the Book XIII Terminal State

- **Scalar-only equilibrium:** ADVERSE (f = −17.71; LOCKED)
- **Combined D1–D10:** f > 0 across tested λ; CONDITIONAL on proxy/fixed BG
- **Track 1 prioritized:** Test whether combined f > 0 survives self-consistently
- **Surplus portfolio:** 0 demonstrated + 2–3 conditional + 0 GW

---

## 4. Formal Combined Equilibrium System

### 4.1 The Five-Sector Action (D8 §5.1)

```
S_total = S_grav[g] + S_macro[Φ, g] + S_defect[Φ⃗, g] + S_trigger[K, Φ⃗] + S_portal[Φ, Φ⃗, g]
```

| Sector | Content | Parameters |
|--------|---------|-----------|
| Gravitational | Einstein-Hilbert: (1/16πG)∫R√−g | G |
| Macro scalar | Real scalar Φ with source J_eff | A₀ |
| Defect triplet | O(3) hedgehog: Φ_a = η f(r) x̂_a with Mexican-hat SSB | η, λ |
| Curvature trigger | ξ√K |Φ⃗|² (Kretschmann trigger) | ξ |
| Portal | g_p Φ² |Φ⃗|² | g_p |

### 4.2 Full Self-Consistent Equilibrium Problem

For static spherically symmetric equilibrium on a self-consistent metric ds² = −e^{2ν}dt² + (1−2m/r)^{−1}dr² + r²dΩ²:

**Einstein equations:**
```
dm/dr = 4πr²(ρ_scalar + ρ_defect + ρ_portal)
dν/dr = [m + 4πr³(p_r,total)] / [r(r − 2m)]
```

**Scalar field equation:**
```
Φ'' + (2/r + ν' − h'/2h)Φ' + h(Φ/τ² − X_eff/τ) = 0
```
where X_eff includes the portal-modified source and h = (1−2m/r)^{−1}.

**Defect field equation (hedgehog):**
```
f'' + (2/r)f' − (2/r²)f − λη²f(f²−1) + ξ√K f + g_p Φ² f = 0
```

**This is a COUPLED system:** the metric (m, ν) depends on both field profiles; both field profiles depend on the metric. Full self-consistency means solving all four equations simultaneously.

### 4.3 What D1–D10 Actually Computed at Each Level

| Level | What was self-consistent | What was fixed/proxy |
|-------|--------------------------|---------------------|
| D2 (BVP) | Defect profile f(r) on Schwarzschild | Metric (Schwarzschild); no scalar coupling |
| D6 (additive) | Nothing iterative; additive superposition | Metric; both profiles |
| D7 (cross-coupled) | Effective phenomenological channels (α_BR, β_XR) on grid | Metric; amplitude model linearized |
| **D9 (Picard)** | **Defect profile f(r) under portal feedback; iterative convergence** | **Metric (Schwarzschild); scalar proxy A_eff(r)** |

**D9 is already a substantial self-consistency achievement.** The defect profile is NOT frozen — it is iteratively solved under portal feedback (g_p Φ² f term) with under-relaxed Picard iteration that CONVERGES with final residual ~10⁻⁵. The portal deforms the defect profile by up to 69% (at λ = 200) — this is NOT a small perturbation.

**What D9 does NOT do:** Let the combined energy back-react on the Schwarzschild metric. The metric is held fixed. This is Layer 3.

---

## 5. Self-Consistency vs Proxy Audit

### 5.1 Layer 1 → Layer 2: What Changed (D6 → D9)

D6 (additive) treated scalar and defect as independent: T_total = T_scalar + T_defect with no cross-coupling. D9 added the portal coupling g_p Φ² |Φ⃗|² and iterated the defect profile to self-consistency.

**Result:** f_min INCREASED (constructive shift +0.004 to +0.013 across λ range). The portal coupling is STABILIZING (positive effective mass for the defect). Self-consistency at the defect-profile level STRENGTHENS the result, not weakens it.

### 5.2 Layer 2 → Layer 3: What Would Change (D9 → Full Metric Back-Reaction)

The Schwarzschild metric f_Schw(r) = 1 − 2M/r would be replaced by f_SC(r) = 1 − 2m(r)/r where m(r) is determined by the combined energy content:

```
dm/dr = 4πr²(ρ_scalar + ρ_defect + ρ_portal)
```

**The scalar contribution:** At equilibrium, ρ_scalar = −X²/(2τ²) < 0 (adverse, as XIII Gamma established). This REDUCES m(r) relative to Schwarzschild in the scalar-equilibrium region — but recall this is the STATIC equilibrium. In the D1–D10 framework, the scalar sector operates at A ~ A_crit (dynamic processing), where the kinetic energy overwhelms the equilibrium deficit. The net scalar contribution to m(r) at A = A_crit is approximately ZERO (kinetic cancels equilibrium at A = 1; slight surplus at A = A_crit).

**The defect contribution:** ρ_defect > 0 (positive energy from hedgehog gradient + potential). This INCREASES m(r). The D7 analysis classified this as the "gravitational penalty" (α_BR) and found it WEAKER than the source-amplification benefit by 12.7×.

**Net effect estimate:** At the D7 level, the constructive channel (source amplification) dominates the destructive channel (gravitational penalty) by 12.7×. If this ratio survives in the full back-reaction, the metric is slightly modified (defect energy gravitates → m slightly larger → f slightly lower) but not enough to reverse the sign of f.

### 5.3 Structural Estimate of Layer 3 Impact

The defect energy contribution at R_eq is 6–22% of total Σ (D6 §4.1, depending on λ). The gravitational penalty from this energy is bounded by:

```
Δm_defect / m ≈ (defect fraction of Σ) × (2M/R_eq − 1) / (2M/R_eq)
```

At canonical parameters (C = 3): Δm_defect/m ~ 0.06–0.22 × 2/3 ~ 0.04–0.15.

The metric impact: Δf ~ −2Δm/R_eq ~ −0.24 to −0.9.

Current f_min (D9) = +0.37 to +0.46.

**Δf estimate: −0.24 to −0.9 vs f_min of +0.37 to +0.46.**

This is a MARGINAL comparison. For low λ (where defect contribution is small), f_min is likely to survive. For high λ (where defect contribution is large), the back-reaction could potentially drive f negative.

**This is the honest structural estimate.** The result is MARGINAL, not clearly safe.

---

## 6. Numerical / Equilibrium Analysis

### 6.1 What Can Be Computed Now

A partial Layer 3 analysis can be performed by estimating the metric correction from the combined energy content and checking whether f_min remains positive.

**Estimated f_min after back-reaction correction:**

| λ | f_min (D9) | Estimated Δf (back-reaction) | Estimated f_min (corrected) | Survives? |
|---|-----------|----------------------------|---------------------------|-----------|
| 5 | +0.376 | ~−0.12 | ~+0.26 | **LIKELY YES** |
| 10 | +0.417 | ~−0.18 | ~+0.24 | **LIKELY YES** |
| 25 | +0.448 | ~−0.30 | ~+0.15 | **MARGINAL** |
| 50 | +0.457 | ~−0.45 | ~+0.01 | **MARGINAL** |
| 100 | +0.457 | ~−0.60 | ~−0.14 | **LIKELY NO** |
| 200 | +0.452 | ~−0.80 | ~−0.35 | **LIKELY NO** |

**IMPORTANT CAVEAT:** These are STRUCTURAL ESTIMATES based on the D7 back-reaction magnitude scaled to each λ. They are NOT exact computations. The actual back-reaction is nonlinear and could be larger or smaller.

### 6.2 Interpretation

**For low λ (5–10):** The defect contribution is small; the gravitational penalty is modest; f_min likely survives positive. The equilibrium path is probably viable.

**For intermediate λ (25–50):** The result is marginal. The estimated corrected f_min is +0.01 to +0.15 — close to zero. The equilibrium path is CONDITIONAL on the exact back-reaction magnitude.

**For high λ (100–200):** The defect energy is large enough that the gravitational penalty probably drives f negative. The equilibrium path likely FAILS at high λ.

### 6.3 What This Means

The D1–D10 result (f > 0 across ALL tested λ) is likely to SURVIVE for low-to-moderate λ but FAIL for high λ once full metric back-reaction is included. The viable parameter window NARROWS from {5, 10, 25, 50, 100, 200} to approximately {5, 10, 25} — a three-value window instead of six.

**This is PARTIAL survival, not full survival and not full failure.**

---

## 7. Branch / Stability Classification

| λ range | Estimated post-back-reaction f_min | Branch status |
|---------|--------------------------------------|--------------|
| λ = 5–10 | ~+0.24 to +0.26 (positive) | **LIKELY SURVIVES** |
| λ = 25 | ~+0.15 (marginally positive) | **MARGINAL** |
| λ = 50 | ~+0.01 (near zero) | **MARGINAL** |
| λ ≥ 100 | Estimated negative | **LIKELY FAILS** |

**Stability:** Not assessed. The estimated surviving branches (low λ) have not been checked for dynamical stability. This remains OPEN.

---

## 8. Hard-Criteria Evaluation

| Criterion | Assessment |
|-----------|-----------|
| 1. Combined self-consistent system defined | **PASS** — five-sector action (D8); coupled field equations specified |
| 2. Self-consistent solve attempted | **PARTIAL** — D9 Picard solves defect under portal feedback (Layer 2); Layer 3 estimated but not exactly computed |
| 3. Positive-metric result survives | **PARTIAL** — estimated survival for low λ (5–25); marginal for λ = 50; likely fails for λ ≥ 100 |
| 4. Independence from proxy | **PARTIAL** — D9 removes defect-freezing proxy; metric-fixing proxy remains |
| 5. Non-GR equilibrium branch exists | **CONDITIONAL** — at low λ, a positive-metric combined branch likely exists; narrow window |
| 6. Stability | **OPEN** — not assessed |
| 7. Caveat burden | **MODERATE** — metric back-reaction estimated, not computed; low-λ viable; high-λ fails |
| 8. Frontier strength | **MODESTLY RESTORED** — from "0 demonstrated" back toward "partial; low-λ window likely viable" |

---

## 9. Failure / Limitation Localization

| Limitation | Severity | Detail |
|-----------|----------|--------|
| **Metric back-reaction not exactly computed** | KEY GAP (but structurally estimated) | Δf estimates are from D7 scaling; nonlinear effects could alter |
| **High-λ equilibrium likely fails** | SIGNIFICANT | λ ≥ 100 window probably closes under back-reaction |
| **Low-λ equilibrium marginal** | MODERATE | λ = 25–50 estimated near f ~ 0; could go either way |
| **Stability not assessed** | MODERATE | Even surviving branches may be unstable |
| **Scalar sector at equilibrium still adverse** | PERMANENT | f_scalar = −17.71; defect must overcome this |
| **A_eff model for scalar amplitude is proxy** | MODERATE | D9 uses A_eff(r) model, not full Φ(r) solution |

---

## 10. Frontier Consequence Audit

### Is the Equilibrium Path Restored?

**PARTIALLY.** The D9 self-consistent Picard iteration (which was already computed in the D1–D10 program but not properly credited in Books XI–XIII) provides substantial defect-profile self-consistency. The structural estimate of metric back-reaction suggests survival at low λ (5–25) but failure at high λ (≥100). The equilibrium path narrows but does not close.

### Is the Strongest Gravity-Side Surplus Restored from Conditional to Demonstrated?

**NOT FULLY.** The surplus moves from "conditional on proxy/fixed background" to "conditional on low-λ regime and structural back-reaction estimate." This is a PARTIAL recovery — the conditionality is NARROWED (from "depends on fixed BG" to "depends on exact back-reaction at low λ") but not eliminated.

### Does Bridge-Worthiness Materially Strengthen?

**MODESTLY.** If the low-λ equilibrium survives exact computation, the gravity frontier regains a concrete non-GR equilibrium branch — the first genuine equilibrium-level beyond-GR result. But this would be in a restricted parameter window, not the full tested range. Bridge-worthiness moves from "further weakened" to "stabilized at narrow conditional."

---

## 11. False-Positive Audit

| Pattern | Guard |
|---------|-------|
| Treating structural estimate as exact computation | **MUST NOT** — Δf estimates are scaling arguments, not solutions |
| Treating D9 as full metric self-consistency | **MUST NOT** — D9 is defect-profile self-consistency; metric is still Schwarzschild |
| Treating low-λ survival as full restoration | **MUST NOT** — only 3 of 6 λ values estimated to survive |
| Treating any surviving branch as stable | **MUST NOT** — stability not assessed |
| Ignoring high-λ failure | **MUST NOT** — the viable window narrows under back-reaction |

---

## 12. GRUT-RAI Combined TOV State-Model Requirements

Specified in the companion state-model document.

---

## 13. Program Consequence

### Does the Equilibrium Path Survive?

**CONDITIONALLY — in a narrowed parameter window.** Low λ (5–25) likely survives metric back-reaction. High λ (≥100) likely fails. The window narrows from 6 tested values to approximately 3.

### Is the Positive-Metric Surplus Restored?

**PARTIALLY.** The surplus moves from "conditional on fixed background" to "conditional on low-λ and exact back-reaction computation." This is progress but not restoration.

### What Should No Longer Be Claimed?

- "f > 0 across all tested λ" (estimated to fail at high λ under back-reaction)
- "D1–D10 result survives fully" (it survives partially, at low λ)
- Full surplus restoration (partial only)

### What Is the Next Correct Stage?

**Two options:**

**Option A — Exact metric back-reaction computation at low λ.** Run the full Layer 3 calculation: integrate the coupled Einstein + scalar + defect system self-consistently at λ = 5, 10, 25. Determine whether f_min > 0 at these values. This would convert the structural estimate into an exact result.

**Option B — Book XIV Terminal.** If the structural estimate is judged sufficient to freeze the equilibrium status (partially surviving at low λ, failing at high λ), close Book XIV and define the handoff for future exact computation.

**Recommended: Option B (Book XIV Terminal).** The structural estimate is honest and informative. The exact computation (Layer 3) is a substantial numerical undertaking that should be a separate program (W4 or Book XV), not squeezed into Book XIV. The current result is enough to freeze the equilibrium status: narrowed but alive at low λ.

---

## 14. Hard-Gated Summary Table

| Test | Verdict | Reason |
|------|---------|--------|
| Combined self-consistent system defined | **YES** | Five-sector action; coupled field equations |
| Self-consistent equilibrium solve attempted | **PARTIAL** | D9 Picard for defect profile (Layer 2); metric back-reaction estimated (Layer 3) |
| Positive-metric result survives | **PARTIAL** | Low λ (5–25) likely; marginal λ (50); fails high λ (≥100) |
| Non-GR equilibrium branch survives | **CONDITIONAL** | At low λ, a narrowed positive-metric branch likely exists |
| Proxy dependence removed or sharply bounded | **PARTIALLY** | D9 removes defect-freezing; metric back-reaction estimated but not computed |
| Equilibrium path survives | **CONDITIONAL** | Narrowed to low-λ window; not eliminated |
| Book XIV Alpha changes frontier status | **YES** | Frontier modestly restored from "0 demonstrated" toward "conditional at low λ" |

---

## 15. Final Verdict

**The equilibrium path survives conditionally in a narrowed parameter window.** The D9 self-consistent Picard iteration (already in canon) provides substantial defect-profile self-consistency with f > 0 across all tested λ. The structural estimate of metric back-reaction (Layer 3) suggests survival at low λ (5–25) but failure at high λ (≥100). The viable equilibrium window narrows from 6 values to approximately 3. The surplus is partially recovered from "conditional on fixed background" to "conditional on low-λ and back-reaction estimate." The equilibrium path is alive but narrower than the pre-XIII narrative assumed.

---

*Combined Self-Consistent TOV and Equilibrium Viability Audit complete. D9 Picard already provides substantial self-consistency (Layer 2). Metric back-reaction (Layer 3) structurally estimated: low λ likely survives; high λ likely fails. Equilibrium window narrows to ~3 of 6 tested λ values. Frontier modestly restored. Book XIV terminal recommended.*
