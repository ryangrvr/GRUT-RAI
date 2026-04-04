# Book VII — Target Beta: Carrier Candidate Matrix

## Companion Reference Document

---

## 1. Baseline HIC Ceiling Table

| Metric | M2 (Book V Zeta) | M3 (Book VII Alpha) | M3 ceiling | Gap to M4 |
|--------|------------------|--------------------|-----------|----|
| HIC pairings | 2 (P1, P2) | 4 (P1, P2, P3, P4) | 4 (adding more yields diminishing returns) | Not closable by pairings alone |
| HIC instances | 4–6 | 8–16 | ~16–20 (saturation) | Not closable by multiplication |
| Directed fraction | ~5–10% | ~15–25% | ~25–35% (concerted-mode saturation) | ~5–10% gap to ~30% threshold |
| Ceiling mechanism | — | — | Substrate competition across shared pools | Requires source-target decoupling |

---

## 2. Candidate Carrier-Family Table

| Family | Name | Concept | Breaks locality? | Cost | Verdict |
|--------|------|---------|-----------------|------|---------|
| **G/J** | **HIC-to-carrier hybrid (diffusible)** | HIC loads small composite; carrier diffuses; discharges at remote target | **YES — full internal diffusion** | 1 postulate + 1–2 params | **SURVIVES — minimum viable** |
| H | Semi-diffusible shuttle | Limited-range carrier between adjacent scaffolds | PARTIAL — one-hop range | 1 postulate + 2 params | **INFERIOR to G/J** |
| I | Boundary-coupled relay | Mechanical propagation along mesh backbone | NO — boundary processes only | 1 postulate + 1 param | **FAILS (too narrow)** |
| K | Overbuilt pseudo-carrier | Multiple new bond types / force mechanisms | YES but excessive | 2+ postulates | **REJECTED (overbuilt)** |

---

## 3. Locality / Storage / Delivery Comparison Table

| Property | HIC (existing) | Family G/J (carrier) | Family H (shuttle) | Family I (boundary) |
|----------|---------------|---------------------|-------------------|---------------------|
| Source-target coupling | Concerted (same scaffold) | **Decoupled (diffusion)** | Partially decoupled (adjacent) | Coupled (boundary propagation) |
| Loaded-state storage | ~fs (concerted) | **τ_carrier >> τ_diffusion needed** | Similar to G/J | Propagation time |
| Spatial range | Zero (fixed-site) | **Full proto-cell interior** | ~1 scaffold length | Along boundary only |
| Scaling with HIC count | Saturating | **Linear** | Sublinear | Not applicable |
| Substrate competition | YES (shared pools) | **NO (independent carrier packets)** | Reduced | Not applicable |
| Selective delivery | Geometry-locked (DS) | **Geometry-locked (target pocket)** | Same | Same |

---

## 4. Directed-Flux Consequence Table

| Configuration | HIC direct events | Carrier-mediated events | Total directed | Level |
|--------------|-------------------|----------------------|---------------|-------|
| Book VI terminal (M2) | ~80–120 / cycle | 0 | ~5–10% | M2 |
| Alpha M3 (no carrier) | ~160–320 / cycle | 0 | ~15–25% | M3 |
| Alpha M3 at ceiling | ~200–350 / cycle | 0 | ~25–35% | M3 (ceiling) |
| **Beta + carrier (M4 target)** | ~200–350 / cycle | **~30–220 / cycle** | **~15–40%** | **M4 (conditional)** |
| Beta + carrier (optimistic) | ~200–350 | ~150–220 | **~35–55%** | **M4 (strong)** |

---

## 5. Multi-Domain Impact Table

| Domain | M3 (no carrier) | M4 (with carrier) | Qualitative change |
|--------|-----------------|-------------------|--------------------|
| Replication | HIC-driven at fixed sites (~15% of events) | HIC + carrier-driven anywhere (~30%+ of events) | **System-wide replication support** |
| Fidelity | HIC-driven at fixed sites | HIC + carrier-driven anywhere | **System-wide error correction** |
| Boundary | P3 at fixed boundary sites | P3 + carrier-driven at any boundary site | **Full boundary maintenance** |
| Repair | P4 at fixed sites | P4 + carrier-driven anywhere | **System-wide repair** |
| Division | D3 with M3 support | D3→D4 with dominant energetic backing | **Potential division upgrade** |
| Lineage | L3 with M3 support | L3→L4 approaches with dominant backing | **Potential robustness upgrade** |
| Adaptation | A3 convergent | A3→A4 approaches with richer landscape | **Potential adaptive upgrade** |
| **Overall** | **Supplementary** | **First organizational inversion** | **Directed > ambient for key processes** |

---

## 6. Hard-Criteria Pass/Fail Matrix

| Criterion | G/J (carrier) | H (shuttle) | I (boundary) | K (overbuilt) |
|-----------|--------------|-------------|-------------|---------------|
| 1. Breaks locality | **PASS** | PARTIAL | FAIL | PASS |
| 2. Loaded-state plausibility | **PASS (conditional)** | PASS (conditional) | PARTIAL | PASS |
| 3. Storage lifetime | **CONDITIONAL** (ΔG ≳ 25 kT) | Same concern | Less relevant | Less concern |
| 4. Transport plausibility | **PASS** | PARTIAL (limited range) | FAIL (boundary only) | PASS |
| 5. Selective delivery | **PASS** | PASS | PARTIAL | PASS |
| 6. Directed-flux gain | **~30–60%** | ~20–35% | ~5–10% | Excessive |
| 7. Multi-domain benefit | **ALL domains** | Some | Boundary only | All |
| 8. Scaffold compatible | **PASS** | PASS | PASS | VARIES |
| 9. Postulate cost | **1** | 1 | 1 | 2+ |
| 10. Parameter cost | **1–2** | 2 | 1 | 3+ |
| 11. New fields/DOF | **0** | 0 | 0 | 0+ |
| 12. Minimality | **HIGH** | MODERATE | LOW | LOW |
| **Overall** | **SURVIVES** | INFERIOR | FAILS | REJECTED |

---

## 7. Fragility / Sensitivity Matrix

| Factor | G/J carrier | H shuttle | I boundary |
|--------|-------------|-----------|-----------|
| τ_carrier requirement | **CRITICAL** — must exceed τ_diffusion (~10⁻² s) | Same | Less relevant |
| ΔG_barrier requirement | **HIGH** — ≳ 25 kT for sufficient lifetime | Same | Lower |
| Carrier degradation | MODERATE — waste composites; manageable | Same | N/A |
| Target-site availability | MODERATE — requires compatible discharge pockets | Same | Limited |
| Production rate | Set by HIC cycle rate; bounded | Same | N/A |
| Parameter sensitivity | **HIGH** — τ_carrier is critical; E_carrier matters | Same | LOWER |
| New failure modes | Carrier leakage, congestion, misdelivery | Same + range limitation | Propagation losses |

---

## 8. False-Positive Disqualification Table

| Category | Applies to G/J? | Why / why not |
|----------|----------------|---------------|
| Mobile in name only | **NO** — K=2-scale genuinely diffuses | Correct size for internal diffusion |
| Loaded but not deliverable | **CONDITIONAL** — deliverable if τ_carrier sufficient | Critical parameter |
| Deliverable but not selective | **NO** — geometry-locked discharge | Same mechanism as HIC DS |
| Still effectively fixed-site | **NO** — full spatial decoupling | Carrier reaches any compatible target |
| Flux inflation | POSSIBLE — must separate HIC-direct from carrier-mediated | Accounting discipline needed |
| ATP-like rhetoric | **APPLIES — must use "proto-currency" not "ATP"** | Carrier lacks biochemical specificity |
| Active transport claim | **CORRECTLY NOT MADE** | Carrier is internal diffusion, not boundary transport |

---

## 9. Energetic-Level Comparison Table

| Level | Name | Directed % | Without carrier | With carrier |
|-------|------|-----------|----------------|-------------|
| M0 | Ambient only | 0% | Historical | Superseded |
| M1 | Local coupling | ~1–3% | Book V Epsilon | Superseded |
| M2 | Networked supplementary | ~5–10% | Book V Zeta | Superseded |
| M3 | Expanded supplementary | ~15–25% | Book VII Alpha | **Still available (zero-cost fallback)** |
| M3+ | Approaching ceiling | ~25–35% | Favorable M3 params | Still fixed-site |
| **M4** | **Dominant metabolism** | **~30–60%** | NOT reachable (ceiling) | **YES (with carrier)** |
| M5 | Dominant with full currency | ~50%+ | NOT reachable | Conditional (carrier at upper range) |

---

## 10. Cost/Debt Comparison Table

| Bridge | Book | Postulates | Parameters | Fields | DOF | Character | Cumulative total |
|--------|------|-----------|-----------|--------|-----|-----------|-----------------|
| Z-B baseline | — | 7 | 3 | 0 | 0 | Sealed program | 7/3/0/0 |
| Matter | IV Alpha | +4 | +2 | 0 | 0 | Soliton matter | 11/5/0/0 |
| Gauge | IV Beta | +2 | +1 | +1 | +6 | Yang–Mills force | 13/6/1/6 |
| HIC (energy) | V Delta | +1 | +1 | 0 | 0 | Fixed-site transduction | 14/7/1/6 |
| **Carrier** | **VII Beta** | **+1** | **+1–2** | **0** | **0** | **Mobile energy distribution** | **15/8–9/1/6** |

---

*Carrier Candidate Matrix complete. Five families tested; one survivor (G/J HIC-to-carrier hybrid). Minimum cost: 1 postulate + 1–2 parameters. Breaks fixed-site ceiling through spatial source-target decoupling. M4 dominant metabolism conditionally unlockable (~30–60% directed). Proto-currency, not ATP. Critical parameter: τ_carrier > τ_diffusion (requires ΔG_barrier ≳ 25 kT). Fourth upper-stack bridge debt.*
