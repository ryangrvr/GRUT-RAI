# Book VIII — Target Alpha: M4 Division Upgrade Matrix

## Companion Reference Tables for Book VIII Alpha

---

## Table 1 — Baseline D3 Division-Control Package

| Route | Mechanism | Component controlled | Earned | Cost | Source |
|-------|-----------|---------------------|--------|------|--------|
| A | Content-to-boundary threshold timing | When division occurs | Book VI Alpha | 0 | Existing assembly catalysts + boundary incorporation |
| C | Content-quality gate via P2 proofreading | Which proto-cells divide efficiently | Book VI Alpha | 0 | Existing P2 HIC pairing |
| D | Partition-bias geometry via K=7 mesh topology | How content distributes at fission | Book VI Alpha | 0 | Existing mesh topology + spatial correlation |
| **Package** | **A+C+D connected** | **Timing + quality + partition** | **D3** | **0** | **All existing structures** |

---

## Table 2 — D3 Failure Mode Baseline

| Failure mode | D3 frequency | Cause | Addressable by M4? |
|-------------|-------------|-------|-------------------|
| Residual timing variance | ~1–2% | Stochastic fluctuation in content/boundary ratio | YES — Family A (reduced variance) |
| Partition split through cluster | ~1–3% | Fission plane intersects functional cluster | PARTIAL — Family E (stronger correlation) |
| Under-equipped daughter (chance) | ~0.5–2% | Low copy number of essential type | YES — Family D (carrier-driven recovery) |
| Boundary resealing failure | ~0.5–1% | Insufficient mesh material at fission site | YES — Family C (full-boundary conditioning) |
| Catastrophic rupture | ~0.5–1% | Multi-point mesh failure | YES — Family C (boundary maintenance reduces defects) |
| **Total D3 nonviable rate** | **~3–8%** | Sum of overlapping modes | — |

---

## Table 3 — M4-Backed Upgrade Route Families

| Family | Mechanism | Target component | New or strengthened D3? | Survives? | D4-qualifying? |
|--------|-----------|-----------------|------------------------|-----------|---------------|
| A — Timing sharpening | Carrier-backed content accumulation reduces timing variance | Timing control | Strengthened D3 (Route A) | YES | NO (alone) |
| B — Repair-before-fission | System-wide P4/P2 via carrier improves pre-fission content quality | Daughter quality | Borderline | YES | NO (alone) |
| C — Boundary conditioning | Carrier-driven K=6/K=7 incorporation across full boundary | Boundary integrity / resealing | **Genuinely new** | **YES** | **YES** |
| D — Bad-partition recovery | Carrier-driven repair in under-equipped daughters | Post-fission recovery | **Genuinely new** | **YES** | **YES** |
| E — Partition reliability | Better-maintained spatial correlation strengthens Route D | Partition quality | Strengthened D3 (Route D) | YES | NO (alone) |
| F — Pseudo-upgrade | Apparent improvement is only D3 with better energetics | None (no new mechanism) | Applies to A, E | DISQUALIFIED | NO |

---

## Table 4 — Division-Component Consequence Matrix

| Component | D3 baseline | M4-backed (robust regime) | Improvement | Source family |
|-----------|-------------|--------------------------|-------------|---------------|
| Timing control | Content-load responsive; ~5–10% CV | ~15–25% reduced variance | Modest | A |
| Daughter completeness (pre-fission) | Quality-filtered (Route C) | ~40–50% fewer degraded catalysts | Moderate | B |
| Boundary integrity | Passive + local P3 (~20–30% coverage) | Directed full-boundary (~70–90% coverage) | **Significant** | C |
| Partition bias | Spatial correlation + K=7 geometry | ~10% stronger correlation fraction | Modest | E |
| Resealing quality | Passive re-bonding | Better mesh at fission → faster, cleaner resealing | Moderate | C |
| Post-fission recovery | **None** | **Carrier-driven rescue of marginally nonviable** | **Significant (new)** | D |
| Net daughter survival | ~92–97% | **~97–99%** | ~2–4× failure reduction | Package |

---

## Table 5 — Hard-Criteria Pass/Fail Matrix

| Criterion | A (timing) | B (repair) | C (boundary) | D (recovery) | E (partition) |
|-----------|-----------|-----------|-------------|-------------|--------------|
| Timing-control gain | **PASS** | INDIRECT | FAIL | FAIL | FAIL |
| Daughter-quality gain | INDIRECT | **PASS** | **PASS** | **PASS** | INDIRECT |
| Partition/resealing gain | FAIL | FAIL | **PASS** | FAIL | MODEST |
| Recurrence across cycles | **PASS** | **PASS** | **PASS** | **PASS** | **PASS** |
| Depends on robust M4 | **YES** | **YES** | **YES** | **YES** | **YES** |
| Scaffold compatible | **PASS** | **PASS** | **PASS** | **PASS** | **PASS** |
| Low carrier-param sensitivity | **PASS** | **PASS** | MODERATE | MODERATE | **PASS** |
| Package-level (not single-metric) | FAIL | FAIL | **PASS** | **PASS** | FAIL |
| Zero-cost under installed M4 | **PASS** | **PASS** | **PASS** | **PASS** | **PASS** |
| **Genuinely new (not strengthened D3)** | **FAIL** | **BORDERLINE** | **PASS** | **PASS** | **FAIL** |

---

## Table 6 — Parameter-Fragility Matrix

| Parameter / condition | Family C (boundary) | Family D (recovery) | Combined D4 |
|----------------------|--------------------|--------------------|-------------|
| ΔG_barrier ≥ 28 kT | REQUIRED | REQUIRED | REQUIRED |
| ΔG_barrier = 25 kT | Partial (~50% boundary coverage) | Marginal (η ~0.75; slow recovery) | D3+ at best |
| ΔG_barrier < 23 kT | FAILS (carrier negligible) | FAILS (no recovery) | D3 only |
| Carrier congestion | LOW (dilute regime) | LOW (dilute regime) | LOW |
| Delivery selectivity loss | MODERATE (wrong-site discharge wastes carrier) | MODERATE (same) | MODERATE |
| Daughter inherits < 3 HICs | N/A (pre-fission) | **FAILS** (insufficient carrier production) | ~5% of daughters |
| M4 → M3 fallback | Full-boundary → local-P3 only | Recovery → none | Clean revert to D3 |
| Boundary area >> carrier reach | Partial coverage; gains diluted | N/A | MODERATE for large cells |

---

## Table 7 — D-Level Comparison Table

| Level | Nonviable rate | Timing control | Partition control | Post-fission recovery | Boundary quality | New cost |
|-------|---------------|---------------|-------------------|----------------------|-----------------|----------|
| D0 | ~10–30% | None | None | None | Passive | — |
| D1 | ~10–25% | Passive size regulation | None | None | Passive | 0 |
| D3 | ~3–8% | Content-load responsive (A) | Spatial-cluster bias (D) | None | Passive + local P3 | 0 |
| D3+ | ~2–5% | Strengthened A under M4 | Strengthened D under M4 | None | Local P3 + partial carrier | 0 |
| **D4-cond** | **~1–3%** | **Strengthened A** | **Strengthened D** | **Carrier-driven rescue** | **Full-boundary directed** | **0** |
| D4 | ~1–3% | Same but unconditional | Same but unconditional | Same but unconditional | Same but unconditional | — |
| D5 | ~0% | Active checkpoint | Active partition | Active repair | Active maintenance | Unknown |

---

## Table 8 — False-Positive Disqualification Matrix

| False-positive category | Tested against | Result | Reason |
|------------------------|---------------|--------|--------|
| Stronger D3 relabeled as D4 | Families A, B, E | **APPLIES** — these are strengthened D3 | D4 claim does NOT rest on A, B, E |
| Stronger D3 relabeled as D4 | Families C, D | **DOES NOT APPLY** | C and D are genuinely new M4-dependent capabilities |
| Better repair ≠ better division | Family B alone | **APPLIES** | Repair improvement alone does not justify D4 |
| Better repair + boundary + recovery | Families B, C, D together | **DOES NOT APPLY** | C and D directly affect division mechanics |
| Lower failure without package regulation | Single-family claims | **APPLIES** | No single family justifies D4 |
| Lower failure without package regulation | C + D together | **DOES NOT APPLY** | Two-layer safety net is package-level |
| M4 survival without division improvement | Family D alone | **PARTIAL CONCERN** | Recovery improves outcome, not process |
| M4 survival without division improvement | Family C + D together | **DOES NOT APPLY** | C improves process; D improves outcome |
| Conditional labeled unconditional | D4-conditional claim | **DOES NOT APPLY** | Explicitly conditional; unconditional D4 denied |
| D4 rhetoric without substance | Overall claim | **DOES NOT APPLY** | Rests on two new capabilities + threshold analysis |

---

## Table 9 — Cost/Debt Comparison

| Stage | Postulates | Parameters | Fields | DOF | D-level | New cost |
|-------|-----------|-----------|--------|-----|---------|----------|
| Book VI Alpha (D3 earned) | 14 | 7 | 1 | 6 | D3 | 0 |
| Book VII Gamma (carrier committed) | 15 | 9 | 1 | 6 | D3 + D4-projected | +1P +2p |
| **Book VIII Alpha (D4-cond verified)** | **15** | **9** | **1** | **6** | **D3 + D4-conditional** | **+0** |

**Total zero-cost upper-stack targets:** 24 (17 Book IV + 2 Book V post-Delta + 3 Book VI + 1 Book VII Alpha + 1 Book VIII Alpha).

---

## Table 10 — M4 Division Upgrade Summary

| Question | Answer |
|----------|--------|
| Does M4 improve division? | YES — two new capabilities + three strengthened routes |
| Is D4-conditional justified? | CONDITIONAL — justified in robust M4 regime |
| Is unconditional D4 justified? | NO — all gains depend on carrier (ΔG ≥ 28 kT) |
| Is D5 (inheritance robustness) justified? | NO — ~1–3% nonviable; not zero |
| How many components improve? | Six (timing, daughter quality, boundary, partition, resealing, recovery) |
| How many are genuinely new? | Two (boundary conditioning, post-fission recovery) |
| How many are strengthened D3? | Three (timing sharpening, repair-before-fission, partition reliability) |
| Cost added? | Zero — all gains from installed M4 infrastructure |
| Next audit? | Book VIII Beta — lineage robustness reassessment under M4 |

---

*M4 Division Upgrade Matrix complete. Nine reference tables covering D3 baseline, route families, component consequences, hard criteria, parameter fragility, D-level comparison, false-positive disqualification, cost accounting, and upgrade summary.*
