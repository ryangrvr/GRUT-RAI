# Book VI — Target Alpha: Division Control Candidate Matrix

## Companion Reference Document

---

## 1. Candidate Route Family Table

| Route | Name | Concept | Core mechanism | New postulates | Verdict |
|-------|------|---------|---------------|---------------|---------|
| **A** | **Content-to-boundary threshold timing** | Division timing coupled to content-load ratio through HIC-linked assembly | Assembly catalysts produce both content monomers and boundary monomers; ratio determines division timing | **0** | **SURVIVES** |
| B | HIC-assisted timing control | HIC variant triggers boundary weakening for fission | HIC discharge breaks mesh bonds to initiate fission | 0 | **FAILS** (faster ≠ better; criterion 2) |
| **C** | **Content-quality gate** | P2 proofreading creates quality-dependent timing bias | Higher-quality content accumulates at different rate; quality filters which proto-cells divide efficiently | **0** | **SURVIVES** |
| **D** | **Partition-bias geometry** | Boundary topology + spatial clustering biases partition toward coherent functional clusters | K=7 mesh topology creates preferential fission sites; large chains cluster near production sites | **0** | **SURVIVES** |
| E | Localized strain / cleavage-site bias | Fission location determined by local pressure hotspots | Non-uniform internal pressure distribution | 0 | **Subsumed into D** (location without content correlation is insufficient) |
| F | Sequence-dependent boundary-incorporation control | Specific sequences direct K=7 placement to create controlled weak zones | Spatial targeting of boundary composition | 1+ | **CONDITIONAL** (requires new bridge debt; not pursued at zero cost) |

---

## 2. Timing-Control / Quality-Gate / Partition-Bias Mapping Table

| Route | Timing control? | Quality gate? | Partition bias? | Mechanism | Benefit |
|-------|----------------|--------------|----------------|-----------|---------|
| **A** | **YES** — content-load responsive | NO (directly) | NO | Content/boundary ratio → division threshold | More reproducible division timing |
| B | YES — but only faster, not better | NO | NO | HIC weakens boundary | Speed without quality; fails |
| **C** | **INDIRECT** — quality affects accumulation rate | **YES** — quality-dependent timing | NO | P2 fidelity → content quality → functional-copy rate | Quality-filtered parents; fewer degraded daughters |
| **D** | NO | **YES** — coherent clusters → complete sets | **YES** — spatial correlation + preferential cleavage | K=7 topology + large-object clustering | Better content distribution at fission |
| E | NO | NO | PARTIAL — location only | Local strain concentration | Subsumed into D |
| F | NO | YES — controlled boundary topology | YES — directed weak zones | Spatial targeting | Conditional (cost) |

---

## 3. Hard-Criteria Pass/Fail Matrix

| Criterion | A | B | C | D | E | F |
|-----------|---|---|---|---|---|---|
| 1. Timing-control plausibility | **PASS** | PASS (speed only) | **PASS (indirect)** | — | — | — |
| 2. Daughter-quality improvement | **INDIRECT** | **FAIL** | **PASS** | **PASS** | FAIL (alone) | PASS |
| 3. Partition-bias plausibility | — | — | — | **PASS** | PARTIAL | PASS |
| 4. Recurrence across cycles | **PASS** | PASS | **PASS** | **PASS** | PARTIAL | COND |
| 5. Scaffold compatibility | **PASS** | PASS | **PASS** | **PASS** | PASS | COND |
| 6. Fine-tuning dependence | **LOW** | LOW | **LOW** | **MODERATE** | LOW | HIGH |
| 7. Fragility | **LOW** | LOW | **LOW** | **MODERATE** | LOW | HIGH |
| 8. System-level benefit | **MODERATE** | NEGLIGIBLE | **MODERATE** | **HIGH** | LOW | HIGH |
| 9. Cost | **ZERO** | ZERO | **ZERO** | **ZERO** | ZERO | 1+ |
| **Overall** | **SURVIVES** | **FAILS** | **SURVIVES** | **SURVIVES** | Subsumed | Conditional |

---

## 4. Fragility / Sensitivity Matrix

| Factor | Route A sensitivity | Route C sensitivity | Route D sensitivity |
|--------|-------------------|--------------------|--------------------|
| Soliton feedstock fluctuation | MODERATE — affects both content and boundary growth | LOW — P2 operates regardless | LOW — topology is structural |
| η_couple variation | LOW — Route A uses assembly catalysts, not HIC coupling | LOW — P2 is independent HIC pairing | N/A |
| Proto-cell population size | LOW — every proto-cell has timing | LOW — every proto-cell is quality-filtered | LOW — every proto-cell has boundary topology |
| Spatial clustering strength | N/A | N/A | **HIGH** — if clustering is weak, partition bias is negligible |
| Stochastic content fluctuation | MODERATE — threshold is statistical | LOW — quality is averaged | MODERATE — cluster integrity varies |
| Division at unusual geometry | LOW | LOW | **MODERATE** — non-standard fission geometry may bypass preferred cleavage sites |

---

## 5. Local vs System-Significance Table

| Route | Local benefit | System-level benefit | Significance classification |
|-------|-------------|---------------------|---------------------------|
| A | More reproducible division timing per proto-cell | Population-level: fewer under/over-equipped daughters | **MODERATE** — reduces timing-failure modes |
| C | Quality-filtered parents per proto-cell | Population-level: fewer degraded-content daughters | **MODERATE** — reduces quality-failure modes |
| D | Better partition per division event | Population-level: fewer missing-function daughters | **HIGH** — directly addresses the largest failure mode |
| A+C+D combined | All three per proto-cell | **Population-level: nonviable rate ~10–30% → ~3–8%** | **SYSTEM-RELEVANT** — ~3x improvement in reproductive efficiency |

---

## 6. False-Positive Disqualification Table

| Potential false positive | Applies? | Why / why not |
|-------------------------|---------|---------------|
| Larger cells splitting later = regulated division | **NO** — Route A is content-LOAD responsive, not just size-responsive; coupled to assembly rate | A is sharpened version of size regulation, not mere size increase |
| Local strain without recurrent control | **NO** — all three routes are structural and recurrent | Not one-off |
| Better average partition without timing | **NO** — A provides timing; D provides partition; both present | Connected package |
| Timing without daughter quality | **NO** — C provides quality filter; D provides partition bias | Quality addressed |
| Quality filter alone = regulation | **MARGINAL** — C alone is a bias, not a decision | C combined with A+D is stronger |
| Modest improvement = inheritance robustness | **YES — this IS a concern** | ~3–8% nonviable is better but not "robust" | Inheritance robustness NOT claimed |
| Checkpoint behavior | **NO — correctly NOT claimed** | No decision logic; no molecular sensor; no halt-and-test | The package is bias, not checkpoint |

---

## 7. Division-Level Comparison Table

| Level | Name | Nonviable rate | Timing control | Quality control | Partition control | Pre-Alpha? | Post-Alpha? |
|-------|------|---------------|---------------|----------------|------------------|-----------|------------|
| D0 | Uncontrolled fission | ~30–50% | NONE | NONE | NONE | Historical | Superseded |
| D1 | Passive size regulation | ~10–30% | Passive pressure | NONE | NONE | YES | Retained |
| D2 | Locally biased timing | ~8–15% | Content-load responsive | NONE | NONE | NO | Route A alone |
| **D3** | **Supplementary regulated** | **~3–8%** | **Content-load (A)** | **Quality filter (C)** | **Partition bias (D)** | **NO** | **A+C+D package** |
| D4 | System-significant regulated | <~5% | Active timing | Quality gate | Partition control | NO | CONDITIONAL |
| D5 | Inheritance-robust | <~1% | Checkpoint-like | Full quality gate | Guaranteed partition | NO | NO |

---

## 8. Cost/Debt Comparison Table

| Route | New postulates | New parameters | New fields | New DOF | Total new items | Pre-existing structure used |
|-------|---------------|---------------|-----------|---------|----------------|---------------------------|
| A | 0 | 0 | 0 | 0 | 0 | Assembly catalysts + boundary incorporation |
| B | 0 | 0 | 0 | 0 | 0 | (Fails — not costed) |
| C | 0 | 0 | 0 | 0 | 0 | P2 HIC proofreading |
| D | 0 | 0 | 0 | 0 | 0 | K=7 mesh topology + spatial clustering |
| E | 0 | 0 | 0 | 0 | 0 | (Subsumed — not costed) |
| F | 1+ | 0+ | 0 | 0 | 1+ | Would need spatial targeting |
| **A+C+D package** | **0** | **0** | **0** | **0** | **0** | All from existing scaffold |

---

*Division Control Candidate Matrix complete. Six route families tested. Three survive (A, C, D) at zero cost. One fails (B: faster ≠ better). One subsumed (E into D). One conditional on new bridge debt (F). The A+C+D connected package advances D1 → D3. Nonviable rate: ~10–30% → ~3–8%. Zero new postulates.*
