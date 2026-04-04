# Book XI — Target Alpha: Binary Pulsar Constraint Matrix

## Companion Reference Tables for Book XI Alpha

---

## Table 1 — Gravity-Ingredient Inventory

| Ingredient | Source | Description | Binary-pulsar relevance |
|-----------|--------|-------------|------------------------|
| Native equation: τ dΦ/dt + Φ = X | GRUT core | First-order dissipative scalar ODE | **HURTS** — scalar, dissipative |
| Static sector: ∇²Φ − Φ/c² = source | Appendix W-F | Helmholtz/screened; Yukawa potential | **HURTS** — screened, not 1/r |
| Effective metric: conformal, slaved to Φ | Appendix W-E | No independent dynamics | **HURTS** — no tensor waves |
| Probe coupling: F = −α∇Φ | Appendix W-D | Gradient force; test-probe limit | NEUTRAL — static only |
| Einstein + T^Φ: G_μν = 8πG T^Φ_μν | Phase 4 xAct | GR metric with GRUT matter source | **CONDITIONAL** — imports GR gravity |
| Strong-field interior (D1–D10) | Strong-field closure | Two-component support; metric positivity | IRRELEVANT — static interior |
| Collapse dynamics | collapse.py | Spherical dust + memory kernel | PARTIALLY RELEVANT |
| τ-reduction heuristic | Appendix G | τ_local = τ₀·t_dyn/(τ₀ + t_dyn) | NEUTRAL — not derived |
| Cosmological extension | Appendix A | FRW + memory; singularity softened | PARTIALLY RELEVANT |

---

## Table 2 — Observable Inventory

| Observable | GR formula | Measured value | Required precision | GRUT native? |
|-----------|-----------|---------------|-------------------|-------------|
| **P-dot (orbital decay)** | **Quadrupole: −(192π/5)(G^(5/3)/c⁵)(P/2π)^(−5/3) × ...** | **−2.4056 × 10⁻¹²** | **~0.2%** | **NO — requires tensor radiation** |
| ω-dot (periastron advance) | 1PN: 3(G(m₁+m₂)/c²)^(2/3)(P/2π)^(−5/3)/(1−e²) | 4.226595°/yr | ~0.001% | NO — requires 1/r potential (screened in GRUT) |
| γ (redshift + time dilation) | 1PN: e(P/2π)^(1/3)(G/c²)^(2/3)m₂(m₁+2m₂)/(m₁+m₂)^(4/3) | 4.2919 ms | ~0.02% | CONDITIONAL — requires metric dynamics |
| Shapiro delay (J0737) | Range r, shape s parameters | Measured | < 0.05% | NO — requires GR metric |

---

## Table 3 — Candidate Mapping-Route Summary

| Family | Mechanism | Produces tensor GW? | Matches P-dot? | Cost | Verdict |
|--------|-----------|---------------------|----------------|------|---------|
| A — Native direct | Scalar radiation from Φ | **NO** — scalar | **NO** — wrong multipole | 0 | **FAILS** |
| B — Effective GR | G_μν = 8πG T^Φ_μν (import GR) | **YES** (from GR) | **YES** (from GR) | 0 (imports GR) | **CONDITIONAL** — not native |
| C — Qualitative trend | Dissipative decay has correct sign | N/A | **NO** — wrong scaling | 0 | **FAILS** |
| D — Structural obstruction | Scalar theory cannot produce tensor GW | N/A | N/A | N/A | **CONFIRMS FAILURE** |

---

## Table 4 — Hard-Criteria Pass/Fail Matrix

| Criterion | A (native) | B (effective GR) | C (trend) | D (obstruction) |
|-----------|-----------|-----------------|----------|-----------------|
| Well-defined observable | PARTIAL | **PASS** | PARTIAL | N/A |
| Sign correct | **PASS** | **PASS** | **PASS** | N/A |
| Scaling correct | **FAIL** | **PASS** (GR) | **FAIL** | N/A |
| Magnitude compatible | **FAIL** | **PASS** (GR) | **FAIL** | N/A |
| Native GRUT only | **PASS** | **FAIL** (imports GR) | **PASS** | N/A |
| No extra bridges | **PASS** | CONDITIONAL | **PASS** | N/A |
| Predictive | SUGGESTIVE | PREDICTIVE (GR) | SUGGESTIVE | N/A |
| Passes gate | **FAIL** | **CONDITIONAL** | **FAIL** | CONFIRMS FAIL |

---

## Table 5 — Failure-Mode Localization

| Failure mode | Status | Detail | Fixable? |
|-------------|--------|--------|---------|
| **Radiative: no tensor GW** | **STRUCTURAL** | Scalar field → monopole/dipole radiation, not quadrupole | Only by adding tensor DOF |
| **Conservative: screened potential** | **STRUCTURAL** | Yukawa exp(−r/c)/r instead of 1/r | Only by removing/modifying screening |
| **Field content: scalar not tensor** | **STRUCTURAL** | Φ is spin-0; gravity requires spin-2 | Only by adding spin-2 field |
| **Dissipative channel: overshoot** | **STRUCTURAL** | τ-dissipation adds orbital decay beyond GR | Would exceed 0.2% tolerance |
| Mapping: imports GR wholesale | CONDITIONAL | Family B works but is not native | Define program scope |
| Formalism: not extended to radiative | PARTIAL | W-appendices stopped at static/effective | Extend analysis |

---

## Table 6 — Compatibility-Level Comparison

| Level | Description | Native GRUT | GRUT-as-matter-within-GR |
|-------|-------------|------------|--------------------------|
| **G0** | **No viable account** | **CURRENT** | Superseded |
| G1 | Qualitative trend only | Available (correct sign) | Superseded |
| G2 | Bounded effective compatibility | NOT achieved | AVAILABLE (GR handles gravity) |
| **G3** | **Strong binary-pulsar compatibility** | NOT achieved | **AUTOMATIC** (GR prediction) |
| G4 | Precision-native success | NOT achieved | NOT achieved (not native) |

---

## Table 7 — False-Positive Disqualification

| False-positive category | Tested against | Result |
|------------------------|---------------|--------|
| Sign agreement without scale | Family A, C | **APPLIES** — correct sign but wrong scaling/magnitude |
| Scale agreement after hidden fitting | All | **DOES NOT APPLY** — no fitting attempted |
| GR borrowing without GRUT logic | Family B | **APPLIES** — binary-pulsar success belongs to GR |
| Conservative without radiative | All | **APPLIES** — even conservative sector fails (screened) |
| Qualitative rhetoric | Family C | **APPLIES** — trend is not precision comparison |

---

## Table 8 — Cost/Debt Comparison

| Stage | Postulates | Parameters | Fields | DOF | Gravity status |
|-------|-----------|-----------|--------|-----|---------------|
| Book X Terminal | 16 | 11 | 1 | 6 | NOT ADDRESSED |
| **Book XI Alpha** | **16** | **11** | **1** | **6** | **G0 native; G3 if matter-within-GR** |
| XI Beta Option 1 (gravity bridge) | 16 + ? | 11 + ? | 1 + 1(?) | 6 + ?(?) | Would pass by construction |
| XI Beta Option 2 (matter theory) | 16 | 11 | 1 | 6 | G3 (GR handles gravity) |
| XI Beta Option 3 (emergent) | 16 | 11 | 1 | 6 | Unknown |

---

## Table 9 — Architectural Options for Book XI Beta

| Option | Description | Cost | Binary-pulsar status | Program identity |
|--------|-------------|------|---------------------|-----------------|
| **1. Gravitational bridge** | Install tensor metric dynamics (Einstein-Hilbert or equivalent) as sixth bridge | **HIGH** (new field + DOF) | Passes by construction | ToE (replaces GR) |
| **2. Matter theory within GR** | Accept GRUT as matter/organization theory; couple to standard GR | **ZERO** (no new postulates) | **Passes via GR** | Matter theory (supplements GR) |
| **3. Emergent gravity** | Derive tensor dynamics from scalar + bridges | **ZERO** (if successful) | Unknown | ToE (derives GR) |

---

*Binary Pulsar Constraint Matrix complete. Nine reference tables covering gravity ingredients, observables, mapping routes, hard criteria, failure modes, compatibility levels, false positives, cost comparison, and architectural options.*
