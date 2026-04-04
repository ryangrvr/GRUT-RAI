# Book V — Target Zeta: HIC Network Matrix

## Companion Reference Document

---

## 1. HIC Pairing Inventory Table

| ID | Source process | Target process | Epsilon score | Level 5 genuine? | Network node? |
|----|---------------|----------------|--------------|------------------|--------------|
| **P1** | **K=1+K=1→K=2 (soliton assembly)** | **Duplex separation** | **9/9** | **YES** | **YES** |
| **P2** | **K=1→K=6 (monomer assembly)** | **Mismatch removal** | **8/9** | **YES** | **YES** |
| P3 | K=1+K=1→K=2 | Directed monomer incorporation | 7/9 | MARGINAL (target is favorable) | NO — excluded |
| P4 | K=6/K=7 assembly | Boundary insertion against pressure | Speculative | NOT TESTED | NO — excluded |
| P5 | D↔A secondary-bond formation | Template strand release | FAILS (source too weak) | NO | NO |
| P6 | Cross-catalytic replication | Boundary repair | FAILS (source distributed) | NO | NO |

---

## 2. Source / Target / Benefit Mapping Table

| Pairing | Source (favorable) | HIC variant | Target (unfavorable) | Direct benefit | Indirect benefit |
|---------|-------------------|-------------|---------------------|---------------|-----------------|
| **P1** | Soliton singlet binding (~50 kT released) | HIC-P1: CS sized for K=2 product; DS positioned at duplex | Duplex secondary-bond peeling (~5–10 kT cost) | ~10x faster template cycling | More substrates available for P2 |
| **P2** | Monomer assembly (~cumulative gauge binding) | HIC-P2: CS sized for K=6 product; DS positioned at mismatch site | Selective mismatch removal (~3–5 kT cost) | ~40% error rate reduction | Better HIC scaffold quality in next generation |

---

## 3. Network Connectivity Summary

### 3.1 Graph Representation

```
Nodes:
  [P1] — replication accelerator (HIC-driven duplex separation)
  [P2] — fidelity enhancer (HIC-driven mismatch removal)
  [Templates] — shared resource (free template strands)
  [HIC_quality] — shared state (scaffold sequence fidelity)

Edges:
  P1 —(produces more)→ Templates
  Templates —(are substrates for)→ P2
  P2 —(improves fidelity of)→ HIC_quality
  HIC_quality —(improves function of)→ P1
  HIC_quality —(improves function of)→ P2

Loops:
  P1 → Templates → P2 → HIC_quality → P1 (closed positive-feedback loop)
  P2 → HIC_quality → P2 (self-improvement sub-loop)
```

### 3.2 Connectivity Matrix

| From \ To | P1 | P2 | Templates | HIC_quality |
|-----------|----|----|-----------|-------------|
| **P1** | — | indirect (via Templates) | **direct** (produces more) | indirect (via P2) |
| **P2** | indirect (via HIC_quality) | self-loop (via HIC_quality) | — | **direct** (improves) |
| **Templates** | — | **direct** (substrates for) | — | — |
| **HIC_quality** | **direct** (improves P1) | **direct** (improves P2) | — | — |

---

## 4. Recurrence / Multi-Cycle Persistence Table

| Property | P1 alone | P2 alone | P1+P2 network |
|----------|---------|---------|---------------|
| Recurs within one reproductive cycle | YES (unlimited HIC cycling) | YES | YES |
| Benefit persists to next generation | YES (more copies → more in daughters) | YES (fewer errors → better daughter quality) | **YES + COMPOUNDING** (fidelity improvement compounds across generations) |
| Heritable | YES (P1-encoding sequence is replicable) | YES (P2-encoding sequence is replicable) | YES (both sequences co-inherited) |
| Selectable | YES (P1 proto-cells faster) | YES (P2 proto-cells more faithful) | **YES + SYNERGISTIC** (P1+P2 proto-cells faster AND more faithful) |
| Compounds across generations | MINIMAL (P1 alone doesn't improve fidelity) | YES (fidelity improves quality of all copies including P2) | **YES** (full P1↔P2 loop compounds both speed and fidelity) |
| Reaches steady state | YES (limited by separation rate ceiling) | YES (limited by P2 discrimination threshold) | YES (converges to fidelity plateau + speed plateau) |

---

## 5. Benefit-Magnitude Classification Table

| Benefit | Source | Magnitude | System relevance | Classification |
|---------|--------|-----------|-----------------|---------------|
| Replication throughput increase | P1 (~10x faster separation) | ~30–40% more copies per division | **MODERATE** — materially improves reproductive output | System-relevant |
| Error rate reduction | P2 (~40% lower p_sub) | N_max increases from ~20 to ~33 | **MODERATE** — extends heritable chain length | System-relevant |
| HIC quality improvement | P2 fidelity → better HIC copies | ~2% more functional HICs per generation | **SMALL** but **COMPOUNDING** | Cross-generational |
| Combined reproductive fitness | P1+P2 synergy | ~50% reproductive advantage over non-HIC proto-cells | **SIGNIFICANT** at competitive level | Selection-relevant |
| Directed fraction of total flux | P1+P2 enhanced events / all events | ~5–10% | **SUPPLEMENTARY** | Below dominance threshold |

---

## 6. Fragility / Failure Matrix

| Failure mode | Probability | Impact | Mitigated by |
|-------------|------------|--------|-------------|
| η_couple drops below 0.05 | Parameter-dependent | Both P1 and P2 become non-functional | Unknown — η is structural; cannot be tuned in situ |
| Concerted-mode pre-positioning fails | Depends on HIC placement geometry | Affected HIC instance fails; others unaffected | Multiple HIC instances provide redundancy |
| P1 and P2 sequences mutated beyond function | p_sub × N_HIC per generation | HIC degrades; benefit lost | P2's own proofreading partially protects HIC sequences |
| Parasitic sequence exploits HIC | If parasite binds CS or DS without reciprocating | HIC resources consumed unproductively | Compartment-level selection; HIC substrate specificity |
| Network loop destabilizes | If P1+P2 compounding overshoots | Unlikely — system is bounded by substrate depletion and division | Self-limiting homeostasis mechanisms |
| Ambient-thermal fluctuation overwhelms HIC benefit | If thermal noise > η × ΔG_source | HIC coupling drowned by thermal background | Requires η ≳ 0.1; structural condition |
| All HICs lost in one division | Statistical partitioning; P(both daughters lack all HICs) = (1/2)^(n_HIC × 2) | HIC lineage terminates in that daughter | Higher pre-division HIC copy numbers reduce this probability |

---

## 7. False-Positive Disqualification Table

| Potential false positive | Applies to P1+P2 network? | Why / why not |
|-------------------------|--------------------------|---------------|
| Multiple isolated events with no connectivity | **NO** — P1 and P2 are connected through templates and HIC quality |
| Connectivity without recurring benefit | **NO** — the loop compounds across generations |
| Recurring benefit without system significance | **BORDERLINE** — ~5–10% directed fraction is modest; ~50% reproductive advantage is significant |
| Sparse events claimed as organization | **HONEST CONCERN** — only 2 HIC nodes in the network; minimal, not complex |
| Local enhancement relabeled as metabolism | **PARTIALLY APPLIES** — the network enhances local steps; it does not organize system-level energy flow |
| Thermal operation relabeled | **NO** — the HIC mechanism is genuinely mechanical, not thermal |
| Process adjacency relabeled as network | **NO** — functional dependency (templates, fidelity feedback) is real |

---

## 8. Energetic Level Comparison Table

| Level | Description | Epsilon | Zeta | Advance? |
|-------|-------------|---------|------|----------|
| L4 | Energetic asymmetry | Superseded | Superseded | — |
| L5 local | True coupling at individual sites | **YES** | YES (still present) | Retained |
| **L5 networked supplementary** | **Connected HIC subnetwork; compounding; supplementary** | Not tested | **YES** | **NEW** |
| L5+ proto-metabolic supplementary | Network organizes significant system fraction | Not tested | NO (~5–10%) | Not achieved |
| L6 proto-metabolic dominant | Directed flow is primary mode | NO | NO | Not achieved |
| L7 full metabolism | Energy currency + regulated distribution | NO | NO | Not achieved |

---

*HIC Network Matrix complete. Two surviving pairings (P1, P2) form a connected benefit loop with cross-generational compounding. Directed fraction ~5–10%. Network is supplementary, not dominant. Level 5 networked supplementary. Not proto-metabolic system. Not metabolism. Not life.*
