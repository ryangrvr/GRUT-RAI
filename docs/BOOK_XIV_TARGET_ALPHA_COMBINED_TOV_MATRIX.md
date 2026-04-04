# Book XIV — Target Alpha: Combined TOV Matrix

## Companion Reference Tables for Book XIV Alpha

---

## Table 1 — Three Layers of Self-Consistency

| Layer | What it resolves | Status | f_min result |
|-------|-----------------|--------|-------------|
| **1. Additive (D6)** | Scalar + defect as independent on fixed Schwarzschild | **COMPUTED** | f > 0 for λ ≥ 25 (A=1); ALL λ (A=A_crit) |
| **2. Portal-coupled (D9)** | Defect profile under portal; Picard iteration | **COMPUTED** | f > 0: ALL λ; f_min = +0.37 to +0.46; shifts constructive |
| **3. Metric back-reaction** | Combined energy → g_μν → fields → T_μν | **ESTIMATED (not computed)** | Low λ: likely positive; high λ: likely negative |

---

## Table 2 — D9 Self-Consistent Results (Existing Canon — LOCKED)

| λ | f_min (D7 frozen) | f_min (D9 SC) | Shift | Deformation | Iterations |
|---|-------------------|-------------|-------|-------------|-----------|
| 5 | +0.371 | +0.376 | +0.004 | 13.2% | 11 |
| 10 | +0.410 | +0.417 | +0.007 | 17.8% | 11 |
| 25 | +0.437 | +0.448 | +0.011 | 29.5% | 13 |
| 50 | +0.444 | +0.457 | +0.013 | 42.4% | 15 |
| 100 | +0.446 | +0.457 | +0.011 | 56.5% | 18 |
| 200 | +0.448 | +0.452 | +0.005 | 69.4% | 20 |

**All positive. All shifts constructive. D9 is a strict generalization of D7.**

---

## Table 3 — Proxy vs Self-Consistent Comparison

| Aspect | D6 (additive) | D9 (portal-coupled) | Full Layer 3 |
|--------|--------------|-------------------|-------------|
| Defect profile | Frozen BVP | **Picard-iterated under portal** | Picard + metric feedback |
| Scalar field | Fixed A_eff model | Proxy A_eff(r) | Full Φ(r) from coupled EOM |
| Metric | Fixed Schwarzschild | Fixed Schwarzschild | **Self-consistent m(r), ν(r)** |
| Portal coupling | Absent | **Active (g_p Φ²f)** | Active |
| Convergence | N/A | **YES (residual ~10⁻⁵)** | UNKNOWN |
| f_min positive | YES (most λ) | **YES (ALL λ)** | **ESTIMATED: low λ yes; high λ no** |

---

## Table 4 — Structural Back-Reaction Estimate

| λ | f_min (D9) | Est. Δf (metric BR) | Est. f_min (corrected) | Survival |
|---|-----------|---------------------|----------------------|----------|
| 5 | +0.376 | ~−0.12 | ~+0.26 | **LIKELY YES** |
| 10 | +0.417 | ~−0.18 | ~+0.24 | **LIKELY YES** |
| 25 | +0.448 | ~−0.30 | ~+0.15 | **MARGINAL** |
| 50 | +0.457 | ~−0.45 | ~+0.01 | **MARGINAL** |
| 100 | +0.457 | ~−0.60 | ~−0.14 | **LIKELY NO** |
| 200 | +0.452 | ~−0.80 | ~−0.35 | **LIKELY NO** |

**CAVEAT:** These are structural estimates from D7 back-reaction scaling, NOT exact computations.

---

## Table 5 — Branch Classification

| λ range | Status after estimated back-reaction | Branch classification |
|---------|--------------------------------------|---------------------|
| 5–10 | f_min ~ +0.24 to +0.26 | **LIKELY SURVIVING** |
| 25 | f_min ~ +0.15 | **MARGINAL** |
| 50 | f_min ~ +0.01 | **MARGINAL** |
| ≥ 100 | f_min estimated negative | **LIKELY FAILING** |

---

## Table 6 — Hard-Criteria Pass/Fail Matrix

| Criterion | Assessment |
|-----------|-----------|
| Self-consistent system defined | **PASS** |
| Solve attempted | **PARTIAL** (D9 Layer 2; Layer 3 estimated) |
| Positive-metric survives | **PARTIAL** (low λ yes; high λ no) |
| Proxy independence | **PARTIAL** (D9 removes defect-freezing; metric still Schwarzschild) |
| Non-GR branch exists | **CONDITIONAL** (low λ) |
| Stability assessed | **OPEN** |
| Frontier strengthened | **MODESTLY** |

---

## Table 7 — Limitation / Failure Table

| Limitation | Severity |
|-----------|----------|
| Metric back-reaction not exactly computed | KEY GAP (structurally estimated) |
| High-λ equilibrium likely fails | SIGNIFICANT |
| Stability not assessed | MODERATE |
| Scalar sector still adverse at equilibrium | PERMANENT |
| Low-λ window narrow (~3 of 6 values) | MODERATE |

---

## Table 8 — Final Classification

| Aspect | Status |
|--------|--------|
| Verdict | **B — equilibrium survives conditionally in narrowed window** |
| D9 self-consistency (Layer 2) | ALREADY COMPUTED; f > 0 ALL λ |
| Metric back-reaction (Layer 3) | ESTIMATED; low λ survives; high λ fails |
| Equilibrium window | Narrowed: ~{5, 10, 25} (3 of 6 tested values) |
| Frontier status | MODESTLY RESTORED (from "0 demonstrated" toward "conditional at low λ") |
| Next stage | Book XIV Terminal or exact Layer 3 computation |

---

*Combined TOV Matrix complete. Eight reference tables covering self-consistency layers, D9 results, proxy comparison, back-reaction estimates, branch classification, hard criteria, limitations, and final classification.*
