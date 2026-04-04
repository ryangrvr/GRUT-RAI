# Book XIII — Target Gamma: TOV Numerical Matrix

## Companion Reference Tables for Book XIII Gamma

---

## Table 1 — Scalar-Only TOV Numerical Results (tov_interior.py — LOCKED)

| τ | m(R_eq) | f(R_eq) | Δm/M | GR A_Schw | Verdict |
|---|---------|---------|------|-----------|---------|
| 0.50 | 16.21 | −96.25 | +31.42 | −2.0 | CATASTROPHICALLY WORSE |
| 0.75 | 7.48 | −43.89 | +13.96 | −2.0 | MUCH WORSE |
| 1.00 | 4.43 | −25.56 | +7.85 | −2.0 | MUCH WORSE |
| **1.22 (canonical)** | **3.12** | **−17.71** | **+5.24** | **−2.0** | **MUCH WORSE** |
| 1.50 | 2.25 | −12.47 | +3.49 | −2.0 | WORSE |
| 2.00 | 1.48 | −7.89 | +1.96 | −2.0 | WORSE |
| 5.00 | 0.66 | −2.94 | +0.31 | −2.0 | WORSE |
| 10.0 | 0.54 | −2.24 | +0.08 | −2.0 | SLIGHTLY WORSE |

---

## Table 2 — Five-Layer Interior Structure (interior_metric_closure.py — LOCKED)

| Layer | f(R_eq) | Mechanism | Status |
|-------|---------|-----------|--------|
| 1. Schwarzschild (GR) | −2.0 | Pure GR; no GRUT | LOCKED |
| 2. Constitutive correction | −1.0 | Phase V post-Newtonian | LOCKED |
| 3. **Static TOV** | **−17.71** | **ρ_eq < 0 → mass ACCUMULATION → WORSENS** | **LOCKED — CRITICAL** |
| 4. Dynamic A=1 | −2.0 | Kinetic exactly cancels equilibrium | LOCKED |
| 5. **Supercritical A > A_crit** | **→ 0** | **Kinetic overshoot → metric approaches 0** | **LOCKED — TRANSIENT** |

---

## Table 3 — Surplus Revision Table

| Surplus | Previous claim | Numerical reality | Revised status |
|---------|-------------|-------------------|---------------|
| **"ρ_eq < 0 reduces mass"** | CLAIMED (Phase 4 §E) | **Mass INCREASES inward (tov_interior.py correction)** | **INCORRECT — sign error** |
| **"Singularity resolution demonstrated"** | DEMONSTRATED | **Transient (decays on τ); conditional (D1–D10 on fixed background)** | **OVERSTATED → CONDITIONAL** |
| **"Relaxed Buchdahl bound"** | STRUCTURAL | **Scalar sector violates Buchdahl in WRONG direction** | **INCORRECT** |
| **"Two-zone architecture"** | STRUCTURAL | **Scalar interior WORSENS, not supports** | **INCORRECT** |
| **"Non-monotonic mass profile"** | STRUCTURAL | **Mass MONOTONICALLY INCREASES inward** | **INCORRECT** |
| "Cosmological regulator" | CONDITIONAL | UNCHANGED (independent of compact interior) | UNCHANGED |
| "GW modification" | ABSENT | UNCHANGED | UNCHANGED |

---

## Table 4 — D1–D10 vs Scalar-Only Comparison

| Aspect | Scalar-only (tov_interior.py) | Combined A+B (D1–D10) |
|--------|------------------------------|----------------------|
| Energy density | ρ_eq < 0 (scalar) | ρ_scalar + ρ_defect (combined) |
| Mass profile | INCREASES inward (worsens) | DECREASES with defect support |
| Metric f(R_eq) | −17.71 (much worse than GR) | +0.37 to +0.46 (positive) |
| Background | Self-consistent | Fixed Schwarzschild |
| Closure | Full analytical/numerical | Picard proxy closure |
| Permanent? | YES (equilibrium) | **CONDITIONAL (proxy + fixed BG)** |
| Defect sector needed? | N/A (absent) | **YES — essential for f > 0** |

---

## Table 5 — Transient Processing Caveat (LOCKED)

| Property | Value |
|----------|-------|
| Classification | `metric_positivity_achievable_transient_supercritical_processing` |
| Mechanism | Φ̇ ~ A_crit · M/(τr²); kinetic > equilibrium deficit |
| A_crit | 1.062 (threshold; NOT shown physically realized) |
| Decay timescale | O(τ) (one relaxation time) |
| Late-time f | −17.71 (static TOV equilibrium) |
| Permanent horizon? | **NO** |
| Physical realization? | **NOT SHOWN** |

---

## Table 6 — Hard-Criteria Pass/Fail (Revised)

| Criterion | XIII Beta claim | XIII Gamma corrected |
|-----------|----------------|---------------------|
| System integrated | Structural (uncomputed) | **COMPUTED — tov_interior.py LOCKED** |
| Outputs generated | Structural predictions | **Generated — but CONTRADICT surplus** |
| Traceable to surplus | PASS | **FAIL (sign error)** |
| Distinct from GR | PASS (Buchdahl relaxed) | **REVERSED (scalar worsens GR)** |
| Comparison-ready | CONDITIONAL | **NOT APPLICABLE (no favorable predictions)** |
| Worth follow-up | YES | **YES — but for COMBINED system, not scalar-only** |

---

## Table 7 — Corrected Frontier Status

| Aspect | Before Gamma | After Gamma |
|--------|-------------|-------------|
| Surplus 1 (scalar-only) | DEMONSTRATED | **INCORRECT — scalar worsens interior** |
| Surplus 1' (transient) | Not distinguished | **TRANSIENT (decays on τ; A_crit not realized)** |
| Surplus 1'' (combined A+B) | DEMONSTRATED (D1–D10) | **CONDITIONAL (fixed BG; proxy closure; defect essential)** |
| Surplus 2 (cosmology) | CONDITIONAL | UNCHANGED |
| Surplus 3 (GW) | ABSENT | UNCHANGED |
| Structural predictions | 3 (Buchdahl, two-zone, mass deficit) | **ALL THREE INCORRECT (sign error)** |
| Frontier strength | Strengthened | **WEAKENED (strongest surplus revised down)** |
| GGB commitment case | Modestly strong | **WEAKENED** |

---

## Table 8 — Next-Step Options

| Option | What it does | Leverage | Risk |
|--------|------------|---------|------|
| A. Integrate FULL combined (scalar+defect) TOV self-consistently | Tests whether D1–D10 result survives off fixed background | **HIGHEST** — the actual gap | MODERATE — may fail |
| B. Revise frontier narrative with corrected surplus | Honest downgrade; acknowledge transient/conditional status | MODERATE | LOW |
| C. Investigate whether dynamic processing can be sustained | Test if A > A_crit is physically maintained | MODERATE | HIGH — likely it cannot (τ-relaxation) |
| D. Archive the frontier | Close gravity program based on corrected surplus | LOW leverage (abandons real D1–D10 work) | LOW risk |

---

## Table 9 — Final Classification

| Aspect | Status |
|--------|--------|
| Verdict | **A — no real quantitative compact-object program survives AS PREVIOUSLY CLAIMED** |
| Scalar-only TOV | **WORSENS interior (f = −17.71)** |
| Phase 4 sign interpretation | **CORRECTED (mass increases, not decreases)** |
| Three structural predictions | **ALL INCORRECT (sign error)** |
| Transient supercritical processing | REAL but TEMPORARY |
| D1–D10 combined result | CONDITIONAL (proxy + fixed BG + defect sector) |
| Frontier status | **WEAKENED — strongest surplus revised from DEMONSTRATED to CONDITIONAL** |
| Next step | Integrate combined TOV self-consistently OR revise frontier narrative |

---

*TOV Numerical Matrix complete. Nine reference tables covering scalar-only results, five-layer structure, surplus revision, D1–D10 comparison, transient caveat, hard criteria, corrected frontier, next-step options, and final classification.*
