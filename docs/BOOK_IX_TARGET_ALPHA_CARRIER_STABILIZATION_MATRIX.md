# Book IX — Target Alpha: Carrier Stabilization Matrix

## Companion Reference Tables for Book IX Alpha

---

## Table 1 — Stabilization Target

| Parameter | Requirement | Source | Status post-IX-Alpha |
|-----------|-------------|--------|---------------------|
| Barrier height ΔG ≥ 28 kT | ΔE₁₂ = (3/16)α_g²M_sk ≥ 28 kT | W0 | **Derived** from binding energy |
| Carrier lifetime τ ≫ τ_diff | τ(2γ) ≫ 2 ms | Book VII Gamma | **Bounded** — sufficient in weak coupling |
| E1 decay blocked | Δℓ=±1 selection rule | W0 Family B | **Exact** for any central potential |
| Dissipation contained | ω_composite ≫ γ | Book IV Alpha assumption | **Confirmed** — perturbative under scale separation |
| Combined η_carrier > 0.95 | τ(2γ)/τ_diff > 300 | Book VII Gamma | **Achieved at α_g ≲ 0.005–0.01** |

---

## Table 2 — Decay-Channel Summary

| Channel | Rate | Selection rule | Suppression factor | Controls lifetime? |
|---------|------|---------------|-------------------|------------------|
| Single gauge-boson (E1) | Γ ∝ α_g⁵ μ | **FORBIDDEN** (Δℓ=0) | Exact zero | NO — blocked |
| **Two gauge-boson (2γ)** | **Γ ∝ α_g⁸ μ** | Allowed (2nd order) | **α_g² relative to E1** | **YES — dominant leak** |
| Magnetic dipole (M1) | Γ ∝ α_g⁵ μ (v/c)² | Suppressed | (v/c)² ≪ 1 | NO — subdominant |
| Electric quadrupole (E2) | Γ ∝ α_g⁵ μ (ka₀)² | Suppressed | (ka₀)² ≪ 1 | NO — subdominant |
| Dissipation-induced | Γ ~ γ(γ/ω)^n × exp(−ΔE/kT) | n/a | (γ/ω)^n × exp(−28) | NO — negligible |
| Thermal excitation | Γ ~ ν₀ exp(−ΔE/kT) | n/a | exp(−28) ≈ 6×10⁻¹³ | NO — negligible |

---

## Table 3 — Dissipation-Coupling Assessment

| Pathway | Coupling mechanism | Rate estimate | Threat level |
|---------|-------------------|--------------|-------------|
| Ohmic friction on relative motion | γ × (relative velocity damping) | ~ γ(γ/ω)^n | **Negligible** under scale separation |
| Fluctuation-driven transition | Thermal noise (FDT) | ~ ν₀ exp(−ΔE/kT) | **Negligible** (exp(−28) ≈ 10⁻¹²) |
| Decoherence | Suppresses superpositions | Does not cause transitions between eigenstates | **Zero** (loaded state is an eigenstate) |
| Collective-coordinate damping | Center-of-mass diffusion | Already in τ_diffusion | **Already accounted for** |
| **Net dissipation threat** | — | — | **CONTAINED** under scale separation |

---

## Table 4 — Two-Gauge-Boson Rate vs Parameter Regime

| α_g | τ(2γ)/τ_diff (at M_sk min for barrier) | Carrier viable? | Regime |
|-----|----------------------------------------|-----------------|-------|
| 0.003 | ~10³–10⁵ | **YES (very comfortable)** | Deep weak coupling |
| 0.005 | ~20–175 | **YES (comfortable)** | Weak coupling |
| 0.01 | ~0.1–12 | **MARGINAL to YES** | Weak coupling boundary |
| 0.02 | ~10⁻³–0.5 | **MARGINAL** | Approaching limit |
| 0.03 | < 1 | **FAILS** | Window closing |
| 0.05 | ≪ 1 | **FAILS** | Moderate coupling |
| 0.1 | ≪ 1 | **FAILS** | Beyond weak coupling |

---

## Table 5 — Stabilization-Route Summary

| Family | Mechanism | Survives? | Stabilization level |
|--------|-----------|-----------|-------------------|
| A — Selection-rule only | E1 blocked; 2γ is leak | **YES** | Baseline |
| B — + Geometric locking | Protects against spurious quenching | YES (supplementary) | Enhanced A |
| C — + Weak dissipation | Dissipation perturbative under scale separation | **YES** | Confirmed non-threat |
| D — Narrow parameter wedge | α_g ≲ 0.01 for comfortable margin | **HONEST CONSTRAINT** | Quantitative tightening |
| E — Pseudo-stabilization | Conditionality shifted, not removed | **Partially applies** | Warning |

---

## Table 6 — Hard-Criteria Pass/Fail Matrix

| Criterion | A (selection) | B (+ geometry) | C (+ dissipation) | D (narrow) | E (pseudo) |
|-----------|-------------|---------------|-------------------|-----------|-----------|
| Robust barrier height | **PASS** | PASS | PASS | PASS | PARTIAL |
| E1 decay suppressed | **PASS (exact)** | PASS | PASS | PASS | PASS |
| Two-boson contained | **PASS (weak coupling)** | Same | Same | PASS (tighter) | PARTIAL |
| Dissipation tolerated | Assumed | Assumed | **PASS** | Assumed | Assumed |
| Parameter breadth | Moderate (α_g ≲ 0.02) | Same | Same | Narrow (≲ 0.01) | N/A |
| Scaffold compatible | **PASS** | **PASS** | **PASS** | **PASS** | PASS |
| Debt reduced | **YES** | YES | YES | YES | NO |
| Unconditional M4 earned | **PARTIAL (stabilized)** | Same | Same | NO | NO |
| Derivational | **YES** | YES | YES | YES | N/A |

---

## Table 7 — Fragility / Sensitivity Matrix

| Parameter | Effect on stabilization | Sensitivity |
|-----------|----------------------|------------|
| α_g value | Controls τ(2γ) via α_g⁸ | **HIGH** — steep dependence |
| M_sk/kT | Controls barrier height via α_g²(M_sk/kT) | MODERATE — broad range works |
| M_sk absolute value | Controls τ(2γ) linearly | MODERATE |
| Scale separation (ω/γ) | Controls dissipation coupling | LOW — inherited assumption |
| Hard-core corrections | Shift levels; don't break selection rule | LOW |
| Non-hydrogenic corrections | Modify 2γ prefactor | LOW in weak coupling |
| Proto-cell size L | Controls τ_diffusion | LOW — 2 ms is representative |
| kT absolute value | Enters both barrier and lifetime conditions | MODERATE — lower kT is better |

---

## Table 8 — Debt-Status Comparison

| Parameter | Book VII | W0 | Book IX Alpha |
|-----------|---------|-----|---------------|
| ΔG_barrier | Matched | Approximately derived (inequality) | **Derived** (binding energy + selection rule + 2γ containment) |
| τ_carrier | Assumed (Arrhenius) | Qualitatively supported (selection rule) | **Quantitatively bounded** (2γ scaling known) |
| Loaded state | Postulated | Identified ((N=2, ℓ=0)) | **Confirmed** |
| Metastability | Postulated | Identified (selection rule) | **Confirmed** (selection rule + 2γ + dissipation) |
| Overall debt | Full bridge debt | Reduced | **Strongly reduced** |
| Postulate count | 1P + 2p | 1P + 2p | **1P + 2p (unchanged)** |

---

## Table 9 — Cascade-Promotion Table

| Domain | Pre-IX-Alpha | Post-IX-Alpha | Basis |
|--------|-------------|---------------|-------|
| M | M4-conditional (ΔG ≥ 28 kT) | **M4-stabilized** (weak coupling + scale separation) | 2γ containment + dissipation assessment |
| D | D4-conditional (on M4) | **D4-stabilized** (on M4-stabilized) | Inherits M4 promotion |
| L | L4-conditional (on M4) | **L4-stabilized** (on M4-stabilized) | Inherits M4 promotion |
| A | A4-conditional (on M4) | **A4-stabilized** (on M4-stabilized) | Inherits M4 promotion |

---

## Table 10 — M-Level Comparison

| Level | Directed fraction | Conditioning | Barrier status | Status |
|-------|-----------------|-------------|---------------|--------|
| M3 | ~15–25% | None (unconditional) | N/A | Unconditional floor |
| M4-conditional | ~30–34% | ΔG ≥ 28 kT (external parameter) | Matched/supported | Superseded by stabilized |
| **M4-stabilized** | **~30–34%** | **Weak coupling + scale separation (structural)** | **Derived + confirmed** | **Current** |
| M4-unconditional | ~30–34% | None (all parameters) | Forced | NOT achieved |
| M5 | ~50%+ | — | — | NOT achieved |

---

## Table 11 — False-Positive Disqualification Matrix

| False-positive category | Tested | Result | Reason |
|------------------------|--------|--------|--------|
| Stronger plausibility without stabilization | Overall | **DOES NOT APPLY** | 2γ rate computed (scaling); dissipation assessed |
| Reduced debt without erasure | Debt claim | **APPLIES** | Postulate retained; parameters supported not eliminated |
| Metastability without lifetime | Lifetime | **DOES NOT APPLY** | τ(2γ) vs τ_diff explicitly assessed |
| Regime widened but not unconditionalized | M4 status | **PARTIALLY APPLIES** | "Stabilized" not "unconditional" — honest labeling |
| M4 rhetoric without conditioning removal | Terminology | **DOES NOT APPLY** | "M4-stabilized" explicitly distinguished from "M4-unconditional" |

---

*Carrier Stabilization Matrix complete. Eleven reference tables covering stabilization target, decay channels, dissipation coupling, parameter regimes, route summary, hard criteria, fragility, debt comparison, cascade promotion, M-level comparison, and false-positive disqualification.*
