# Book VI — Target Beta: Lineage Robustness Candidate Matrix

## Companion Reference Document

---

## 1. Essential Content-Class Inventory Table

| Class | Minimum per daughter | Typical pre-div copies (D3) | P(missing per daughter) at N copies | Failure consequence |
|-------|---------------------|---------------------------|-------------------------------------|-------------------|
| Template strands (per type) | ≥ 1 | 4–8 | 0.016–0.004 per type | Cannot replicate missing sequence; permanent loss |
| Replication catalysts | ≥ 1 | 2–4 | 0.06–0.25 | Reverts to uncatalyzed; severe rate penalty |
| Assembly catalysts | ≥ 1 | 2–4 | 0.06–0.25 | Cannot produce monomers; feedstock-dependent only |
| HIC-P1 scaffolds | ≥ 1 | 2–3 | 0.13–0.25 | Loses replication acceleration |
| HIC-P2 scaffolds | ≥ 1 | 2–3 | 0.13–0.25 | Loses proofreading; fidelity degrades |
| Boundary material (K=6/K=7) | Sufficient to reseal | Abundant | < 0.01 | Contents leak |

**Highest-risk classes:** HIC scaffolds (low copy number, ~13–25% loss probability per type per daughter without partition bias). With Route B partition bias (~30% improvement): ~9–18%.

---

## 2. Candidate Robustness Route Table

| Route | Name | Mechanism | Level of action | Cost | Verdict |
|-------|------|-----------|----------------|------|---------|
| **A** | Redundancy-assisted retention | Higher pre-div copy numbers from P1 acceleration | Individual daughter | 0 | **SURVIVES** |
| **B** | Partition-bias amplification | Spatial-cluster self-reinforcement across generations | Individual → lineage | 0 | **SURVIVES** |
| **C** | Quality-linked lineage filtering | P2 quality filter enriches population for high-quality lineages | Population level | 0 | **SURVIVES (as culling, not retention)** |
| **D** | Timing-linked completeness bias | Division at content-complete threshold | Individual daughter | 0 | **SURVIVES** |
| **E** | HIC-linked inheritance support | HIC catch-up: under-equipped daughters recover faster | Individual daughter | 0 | **SURVIVES (for under-equipped, not missing-type)** |
| **F** | Connected robustness package | A+B+C+D+E combined | System-wide | 0 | **SURVIVES — the realized L3 system** |

---

## 3. Multi-Generation Persistence Table

| Metric | Pre-Alpha (D1) | Post-Alpha (D3) | Post-Beta (D3+L3) | Change |
|--------|----------------|-----------------|-------------------|--------|
| p_any_loss per generation | ~0.10–0.30 | ~0.03–0.08 | ~0.03–0.08 (same Division level) | D3 inherited |
| Single-lineage half-life | ~3–7 gen | ~9–23 gen | ~9–23 gen | Same (single-lineage = Alpha result) |
| Branching lineage status | Fragile | Resilient | **Resilient + self-reinforcing** | L3 adds compounding |
| Net population growth rate | 0.40–0.80 per gen | 0.84–0.92 per gen | 0.84–0.92 per gen | Same growth rate |
| Partition-bias self-reinforcement | None | Present (D) | **Compounding across gen (B)** | New in Beta |
| Quality-linked population enrichment | None | Present (C) | **Active across gen** | Reinforced by Beta analysis |
| Under-equipped catch-up | None | None (not analyzed) | **Present (E)** | New in Beta |
| Lineage-level classification | L0 | L1 | **L3** | +2 levels |

---

## 4. Hard-Criteria Pass/Fail Matrix

| Criterion | A | B | C | D | E | F (package) |
|-----------|---|---|---|---|---|-------------|
| 1. Essential-class retention | **PASS** | **PASS** | FAIL (culls, doesn't retain) | **INDIRECT** | **PARTIAL** | **PASS** |
| 2. Multi-gen persistence | **PASS** | **PASS** | **PASS** | **PASS** | **PASS** | **PASS** |
| 3. Partition-drift resistance | **PASS** | **PASS** | NO | PARTIAL | PARTIAL | **PASS** |
| 4. Recurrence | **PASS** | **PASS** | **PASS** | **PASS** | **PASS** | **PASS** |
| 5. Scaffold compatibility | **PASS** | **PASS** | **PASS** | **PASS** | **PASS** | **PASS** |
| 6. Sensitivity | LOW | MODERATE | LOW | LOW | LOW | LOW-MOD |
| 7. Fine-tuning | LOW | MODERATE | LOW | LOW | LOW | LOW |
| 8. Significance | SYSTEM | LINEAGE | POPULATION | LINEAGE | INDIVIDUAL | **SYSTEM** |
| 9. Cost | **ZERO** | **ZERO** | **ZERO** | **ZERO** | **ZERO** | **ZERO** |

---

## 5. Fragility / Sensitivity Matrix

| Factor | Route A | Route B | Route C | Route D | Route E |
|--------|---------|---------|---------|---------|---------|
| Low copy number (N ≤ 2) | **VULNERABLE** | Still helps (cluster) | N/A | Helps (timing) | Limited (can't catch up from zero) |
| Weak spatial clustering | N/A | **VULNERABLE** | N/A | N/A | N/A |
| Loss of HIC function | N/A | N/A | N/A | N/A | **VULNERABLE** — catch-up fails |
| High mutation rate (p_sub > 0.1) | Reduces quality of copies | Degrades clusters over gen | **MORE CULLING** | Content quality lower at threshold | Recovery copies are error-prone |
| Environmental stress (feedstock drop) | Fewer copies per cycle | Same clusters, slower growth | More stringent filtering | Threshold reached slower | Slower recovery |
| Small population | Works per-individual | Works per-individual | **VULNERABLE** — culling needs population | Works per-individual | Works per-individual |

---

## 6. Local vs Lineage Significance Table

| Route | Individual-level effect | Lineage-level effect | Population-level effect |
|-------|----------------------|---------------------|----------------------|
| A (redundancy) | More copies per daughter | More copies compound across gen | Lineages with P1 persist longer |
| B (partition amp.) | More coherent daughters | Coherence self-reinforces across gen | Better-partitioned lineages dominate |
| C (quality culling) | — (culls, doesn't improve individual) | Weak lineages eliminated | **Population enriched for quality** |
| D (timing) | Better-timed division | Consistent content level across gen | Population has uniform division quality |
| E (catch-up) | Under-equipped daughters recover | Recovery persists across gen | Lineages tolerant of occasional deficit |
| **F (package)** | **All individual effects** | **All lineage effects + compounding** | **Population-level enrichment + resilience** |

---

## 7. False-Positive Disqualification Table

| Candidate false positive | Applies to F package? | Why / why not |
|-------------------------|----------------------|---------------|
| Better mean daughter quality = lineage robustness | **NO** — multi-gen persistence explicitly tracked | Section 7 of main document |
| Surviving a few generations by luck | **NO** — mechanisms are structural and heritable | Routes A–E are recurrent |
| Culling = inheritance guarantee | **PARTIALLY** — Route C is culling; but A,B,D,E are retention | Package is more than culling alone |
| Redundancy alone | **NO** — package includes partition bias, quality filter, timing, catch-up | Five-route connected system |
| HIC advantage = inheritance advantage | **PARTIALLY** — HIC contributes indirectly through P1,P2 | Not the sole mechanism |
| Supplementary regulation = strong heredity | **APPLIES — correctly classified L3, not L4** | ~4% per-gen failure; depends on branching |

---

## 8. Lineage-Level Comparison Table

| Level | Name | Per-gen failure | Lineage half-life | Branching status | Pre-Alpha? | Post-Beta? |
|-------|------|----------------|-------------------|-----------------|-----------|-----------|
| L0 | Daughter viability only | — | — | — | Historical | Superseded |
| L1 | Improved daughter quality | ~3–8% | ~9–23 gen | Resilient | YES (Alpha) | Superseded |
| L2 | Short lineage persistence | ~5–10% | ~7–14 gen | Moderate | MARGINAL | Superseded |
| **L3** | **Supplementary lineage robustness** | **~3–8%** | **~9–23 gen + compounding** | **Resilient + self-reinforcing** | **NO** | **YES** |
| L4 | Inheritance-robust reproduction | < ~1% | > ~70 gen | Robust per-individual | NO | NO |
| L5 | Adaptive lineage dynamics | < ~1% + directional | Long-term | Adaptive | NO | NO |

---

## 9. Cost/Debt Comparison Table

| Item | Pre-Beta | Beta adds | Post-Beta |
|------|---------|-----------|----------|
| Postulates | 14 | +0 | **14** |
| Parameters | 7 | +0 | **7** |
| Fields | 1 | +0 | **1** |
| DOF | 6 | +0 | **6** |
| Zero-cost targets | 20 | +1 | **21** |

---

*Lineage Robustness Candidate Matrix complete. Six routes tested; five survive; connected package (F) achieves L3. Essential-class retention improved ~3x. Lineage half-life ~16 gen. All at zero cost. L4 inheritance robustness NOT achieved (~4% per-gen failure persists). Twenty-first zero-cost target.*
