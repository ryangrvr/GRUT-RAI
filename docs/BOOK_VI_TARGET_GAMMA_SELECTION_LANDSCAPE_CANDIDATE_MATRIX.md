# Book VI — Target Gamma: Selection Landscape Candidate Matrix

## Companion Reference Document

---

## 1. Heritable Trait Inventory Table

| Trait | Encoding | Variation mechanism | Heritability | Success effect | Effect strength |
|-------|---------|-------------------|-------------|---------------|----------------|
| **HIC-P1 scaffold quality** | Sequence S_P1 | Subclass mutations alter pocket geometry | **HIGH** — sequence-replicated | Faster template cycling | **STRONG** (~30–40% replication advantage) |
| **HIC-P2 scaffold quality** | Sequence S_P2 | Subclass mutations alter discharge geometry | **HIGH** | Lower error rate | **STRONG** (~40% error reduction) |
| **Division threshold** | Assembly-catalyst branching ratio | Mutations alter content/boundary production ratio | **HIGH** | Better-equipped daughters | **MODERATE** (convergent to optimum) |
| **Assembly-catalyst efficiency** | Sequence S_assembly | Subclass mutations alter pocket geometry | **HIGH** | Faster monomer production | **MODERATE** (ceiling at substrate saturation) |
| Template content (non-functional) | Sequence | Mutations | HIGH | None directly | N/A |
| Boundary-incorporation rate | Assembly output ratio | Indirect variation | PARTIAL | Indirect (division timing) | LOW |
| Spatial-clustering propensity | Scaffold placement | Production-site determined | PARTIAL | Indirect (partition quality) | LOW |

---

## 2. Candidate Selection-Route Table

| Route | Name | Mechanism | Directional? | Cumulative? | Beyond filtering? | Verdict |
|-------|------|-----------|-------------|------------|-------------------|---------|
| **A** | Fidelity-linked advantage | Lower p_sub → better type retention → lineage expansion | **YES** | **YES** | **YES** (P2 self-reinforcement) | **SURVIVES** |
| **B** | HIC-quality-linked advantage | Better HIC → P1/P2 coupling → throughput/fidelity | **YES** | **YES** | **YES** (P1+P2 compounding) | **SURVIVES — strongest** |
| **C** | Division-quality-linked advantage | Better threshold → more viable daughters | **YES** (convergent) | **PARTIAL** | **MARGINAL** | **SURVIVES (convergent)** |
| **D** | Coupled trait-cluster advantage | Multi-trait packages yield non-additive advantage | **YES** | **YES** | **YES** | **SURVIVES** |
| E | Sequence-function lineage bias | Specific sequences → specific catalytic functions → advantage | YES | YES | YES | Subsumed into A–D |
| F | Filtering-only pseudo-selection | All enrichment = culling | NO (non-directional) | NO (one-off) | N/A (IS the filtering baseline) | **FAILS as complete account** |

---

## 3. Selection-Landscape Axis Table

| Axis | Trait | Range | Gradient direction | Shape | Ceiling | Active enrichment generations |
|------|-------|-------|-------------------|-------|---------|------------------------------|
| 1 | HIC-P1 quality | 0 (non-functional) to 1 (geometric optimum) | → 1 | Monotonically increasing | Geometric optimum | ~5–15 |
| 2 | HIC-P2 quality | 0 to 1 | → 1 | Monotonically increasing (plateau at fidelity limit) | Fidelity plateau | ~5–15 |
| 3 | Division threshold | (too low) ↔ optimal ↔ (too high) | → optimal | Unimodal peak | Optimal value | ~3–5 |
| 4 | Assembly efficiency | Low to high | → higher | Monotonically increasing (saturation) | Substrate saturation | ~5–10 |

**Landscape summary:** 4 axes, all directional, single broad optimum, bounded ceilings, convergent dynamics.

---

## 4. Multi-Generation Enrichment Table

| Generation | HIC-P1 avg quality | HIC-P2 avg quality | Div threshold alignment | Assembly efficiency | Enrichment driver |
|-----------|-------------------|-------------------|------------------------|--------------------|--------------------|
| 0 | Mixed (0.3–0.8) | Mixed (0.3–0.8) | Scattered | Mixed | — |
| 1 | ↑ (non-functional culled) | ↑ (non-functional culled) | ↑ (extremes culled) | ↑ (slow variants culled) | Filtering (Route F component) |
| 2–5 | ↑↑ (compounding via P2) | ↑↑ (self-reinforcing fidelity) | → optimal (converged) | ↑ (selection for efficiency) | Selection (Routes A+B compounding) |
| 6–10 | ↑ (approaching ceiling) | ↑ (approaching fidelity plateau) | ≈ optimal (stable) | ↑ (approaching saturation) | Diminishing returns |
| 11–15 | ≈ ceiling | ≈ plateau | ≈ optimal | ≈ ceiling | Near-optimum stabilization |
| 15+ | Stable at optimum | Stable at plateau | Stable | Stable | **CONVERGED — no further enrichment** |

**Pattern:** ~5–15 generations of active directional enrichment → convergence to bounded optimum → stable plateau. Not open-ended.

---

## 5. Hard-Criteria Pass/Fail Matrix

| Criterion | Route A | Route B | Route C | Route D | Route F |
|-----------|---------|---------|---------|---------|---------|
| 1. Trait heritability | **PASS** | **PASS** | **PASS** | **PASS** | N/A |
| 2. Success effect | **PASS** | **PASS** | **PASS** | **PASS** (non-additive) | N/A |
| 3. Directional enrichment | **PASS** | **PASS** | **PARTIAL** (convergent) | **PASS** | **FAIL** (one-off) |
| 4. Multi-gen persistence | **PASS** | **PASS** | **PASS** | **PASS** | **FAIL** |
| 5. Beyond neutral drift | **PASS** | **PASS** | **PARTIAL** | **PASS** | N/A |
| 6. Scaffold compatibility | **PASS** | **PASS** | **PASS** | **PASS** | N/A |
| 7. Parameter sensitivity | LOW | LOW | LOW | MODERATE | N/A |
| 8. Significance level | LINEAGE | **SYSTEM** | LINEAGE | **SYSTEM** | N/A |
| 9. Cost | ZERO | ZERO | ZERO | ZERO | N/A |
| **Overall** | **SURVIVES** | **SURVIVES (strongest)** | **SURVIVES (convergent)** | **SURVIVES** | **FAILS** |

---

## 6. Fragility / Sensitivity Matrix

| Factor | Route A | Route B | Route C | Route D |
|--------|---------|---------|---------|---------|
| HIC quality variance low | N/A | **VULNERABLE** — if all HICs are similar, no selection gradient | N/A | MODERATE |
| Mutation rate too low | **VULNERABLE** — insufficient variation for selection to act on | Same | N/A | Same |
| Mutation rate too high | VULNERABLE — beneficial mutations washed out by errors | Same | N/A | Same |
| Environmental fluctuation | LOW — selection pressures are intrinsic | LOW | LOW | MODERATE |
| Population too small | MODERATE — drift can overwhelm selection in small populations | Same | Same | Same |
| Fidelity plateau reached quickly | N/A | Enrichment saturates early | N/A | Coupled improvement also saturates |
| No ecological structure | Routes operate in same pool | Same | Same | Same — limits landscape complexity |

---

## 7. Local vs Lineage vs Population Significance Table

| Route | Individual effect | Lineage effect | Population effect | Overall significance |
|-------|-----------------|---------------|-------------------|---------------------|
| A (fidelity) | Better copies | Lineage maintains quality | Higher-fidelity lineages dominate | LINEAGE-POPULATION |
| B (HIC quality) | Better coupling | Lineage replicates faster + more accurately | HIC-optimized lineages dominate | **SYSTEM** |
| C (threshold) | Better-timed division | Lineage produces more viable daughters | Near-optimal-threshold lineages dominate | LINEAGE |
| D (coupled) | Multi-trait advantage | Lineage with best package dominates | Multi-trait-optimized population | **SYSTEM** |

---

## 8. False-Positive Disqualification Table

| Category | Applies? | Why / why not |
|----------|---------|---------------|
| Survival of least bad | PARTIALLY — initial culling is part of dynamics; later enrichment goes beyond | Honest: both components present |
| Culling without improvement | **NO** — HIC-quality enrichment is genuine optimization via P1+P2 compounding | Compounding is cumulative improvement |
| Redundancy-only success | **NO** — selection operates on quality, not just quantity | Better HICs outcompete more-redundant-but-lower-quality variants |
| Correlation without causation | **NO** — HIC quality causally affects replication + fidelity (mechanism demonstrated) | Mechanism from Delta/Epsilon |
| Enrichment without persistence | **NO** — enrichment persists through convergence to stable optimum | Landscape is stable |
| Convergent = open-ended | **APPLIES — this is the boundary** | Correctly classified A3, not A4/A5 |
| One-time sorting | **NO** — enrichment continues for ~5–15 generations beyond initial sort | P1+P2 compounding provides continued improvement |

---

## 9. Adaptive-Classification Comparison Table

| Level | Name | Enrichment | Duration | Landscape | Innovation | Pre-Beta? | Post-Gamma? |
|-------|------|-----------|----------|-----------|-----------|----------|------------|
| A0 | No selection | None | — | None | None | Historical | Superseded |
| A1 | Filtering only | One-off culling | 1 gen | None | None | YES (Beta) | Superseded |
| A2 | Differential success without enrichment | Transient | Few gen | Weak | None | MARGINAL | Superseded |
| **A3** | **Proto-Darwinian dynamics** | **Directional, cumulative, compounding** | **~5–15 gen** | **Low-dim, convergent** | **None** | **NO** | **YES** |
| A4 | Strong adaptive dynamics | Directional, sustained | Many gen | High-dim, rugged | Some | NO | NO |
| A5 | Open-ended evolution | Continuous | Indefinite | Complex, dynamic | Continuous | NO | NO |

---

## 10. Cost/Debt Comparison Table

| Item | Pre-Gamma | Gamma adds | Post-Gamma |
|------|----------|-----------|-----------|
| Postulates | 14 | +0 | **14** |
| Parameters | 7 | +0 | **7** |
| Fields | 1 | +0 | **1** |
| DOF | 6 | +0 | **6** |
| Zero-cost targets | 21 | +1 | **22** |

---

*Selection Landscape Candidate Matrix complete. Four heritable trait axes with directional gradients. Convergent selection landscape with single broad optimum. Enrichment for ~5–15 generations via P1+P2 compounding. Routes A–D survive; Route F (filtering only) fails as complete account. A3 supplementary proto-Darwinian dynamics. Zero cost. Twenty-second zero-cost target.*
