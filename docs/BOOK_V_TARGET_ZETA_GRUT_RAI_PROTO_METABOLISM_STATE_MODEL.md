# Book V — Target Zeta: GRUT-RAI Proto-Metabolism State Model

## Minimum Machine-Usable State Model for Network-Level Energetic Reasoning

---

## 1. Purpose

This document extends the Epsilon energy-flow state model with network-level constructs: HIC site classes, source-target pairings, network nodes and edges, benefit-flow representation, recurrence/multi-cycle tracking, fragility fields, and energetic level classification at the network (not just site) level.

---

## 2. Entity Types

| Entity ID | Name | Description | Parent |
|-----------|------|-------------|--------|
| `HIC_P1` | HIC variant for Pairing 1 | Scaffold sequence encoding CS for soliton assembly + DS for duplex separation | `HIC` |
| `HIC_P2` | HIC variant for Pairing 2 | Scaffold sequence encoding CS for monomer assembly + DS for mismatch removal | `HIC` |
| `HIC_network` | Connected HIC subnetwork | The P1+P2 connected benefit loop as a system-level entity | Network |
| `Template_pool` | Free template population | Shared resource connecting P1 output to P2 input | Resource |
| `HIC_quality_state` | Scaffold sequence fidelity | Shared state connecting P2 output to P1/P2 input | State |
| `ProtoCell_HIC` | HIC-equipped proto-cell | Proto-cell containing HIC_P1 + HIC_P2 instances + standard scaffold | System |

---

## 3. Node and Edge Types

### 3.1 Network Nodes

| Node ID | Type | Function | Metrics |
|---------|------|---------|---------|
| `N_P1` | HIC coupling node | Drives duplex separation from soliton assembly energy | Events per cycle; speedup factor |
| `N_P2` | HIC coupling node | Drives mismatch removal from monomer assembly energy | Events per cycle; error reduction |
| `N_templates` | Shared resource node | Free template strands available for replication and P2 proofreading | Count; turnover rate |
| `N_hic_quality` | Shared state node | Average fidelity of HIC-encoding sequences in the population | Error rate per HIC position |

### 3.2 Network Edges

| Edge ID | From | To | Mechanism | Weight |
|---------|------|----|-----------| -------|
| `E_P1_templates` | N_P1 | N_templates | P1 accelerates separation → more free templates per unit time | Throughput multiplier (~1.3–1.4x) |
| `E_templates_P2` | N_templates | N_P2 | More templates = more substrates for P2 proofreading | Substrate availability |
| `E_P2_quality` | N_P2 | N_hic_quality | P2 removes mismatches → better HIC copies in next generation | Fidelity improvement (~0.6x error rate) |
| `E_quality_P1` | N_hic_quality | N_P1 | Better HIC sequences → better P1 scaffold function | Functional improvement (~1.02x per generation) |
| `E_quality_P2` | N_hic_quality | N_P2 | Better HIC sequences → better P2 scaffold function | Functional improvement (~1.02x per generation) |

---

## 4. State Variables

### 4.1 Per-HIC Variables (inherited from Epsilon)

| Variable | Type | Domain | Description |
|----------|------|--------|-------------|
| `hic_conformation` | Enum | {`unloaded`, `primed`, `loaded`, `discharging`} | HIC conformational state |
| `cs_occupancy` | Enum | {`empty`, `source_bound`, `product_formed`} | Capture site |
| `ds_occupancy` | Enum | {`empty`, `target_bound`, `product_releasing`} | Discharge site |
| `cycle_count` | Integer ≥ 0 | Per-HIC instance | Completed successful cycles |
| `leak_count` | Integer ≥ 0 | Per-HIC instance | Wasted cycles |

### 4.2 Network-Level Variables (new in Zeta)

| Variable | Type | Domain | Description |
|----------|------|--------|-------------|
| `n_P1_instances` | Integer ≥ 0 | Per proto-cell | Number of functional HIC-P1 scaffolds |
| `n_P2_instances` | Integer ≥ 0 | Per proto-cell | Number of functional HIC-P2 scaffolds |
| `template_pool_size` | Integer ≥ 0 | Per proto-cell | Free template count |
| `hic_quality_score` | Float ∈ [0,1] | Per proto-cell | Fraction of HIC copies that are fully functional |
| `P1_events_per_cycle` | Float ≥ 0 | Per reproductive cycle | Total P1 discharge events |
| `P2_events_per_cycle` | Float ≥ 0 | Per reproductive cycle | Total P2 discharge events |
| `directed_fraction` | Float ∈ [0,1] | Per proto-cell | (P1_events + P2_events) / total_events |
| `network_connected` | Boolean | Per proto-cell | True if both P1 and P2 instances are present and template pool is shared |
| `compounding_active` | Boolean | Per proto-cell | True if P2 fidelity improvement feeds back to HIC quality across generations |
| `reproductive_advantage` | Float | Per lineage | Reproductive rate relative to non-HIC proto-cells |

### 4.3 Classification Variables

| Variable | Type | Domain | Description |
|----------|------|--------|-------------|
| `energy_level` | Enum | {`L4`, `L5_local`, `L5_networked_supplementary`, `L5_plus`, `L6`} | Current energetic classification |
| `network_status` | Enum | {`absent`, `isolated_nodes`, `connected_supplementary`, `connected_dominant`, `proto_metabolic`} | Network organization level |
| `metabolism_status` | Enum | {`not_crossed`, `supplementary_subnetwork`, `partial_organization`, `dominant_organization`, `full`} | Metabolism verdict |

---

## 5. Event Types (Network-Level)

| Event ID | Name | Precondition | Postcondition | Significance |
|----------|------|-------------|---------------|-------------|
| `P1_CYCLE` | P1 HIC completes one coupling cycle | P1 primed + concerted | Duplex separated; template freed; P1 reset | One replication-acceleration event |
| `P2_CYCLE` | P2 HIC completes one coupling cycle | P2 primed + concerted | Mismatch removed; fidelity improved; P2 reset | One error-correction event |
| `TEMPLATE_FREED` | Free template enters pool | P1_CYCLE or thermal separation | template_pool_size += 1 | Shared resource updated |
| `FIDELITY_UPDATE` | HIC quality improves | P2 proofreading reduces errors in HIC sequence copies | hic_quality_score adjusted upward | Cross-generational feedback |
| `GENERATION_ADVANCE` | Proto-cell divides; daughter inherits HIC instances | Division event (from Psi) | Daughter has n_P1, n_P2 from statistical partition; hic_quality_score inherited | Multi-cycle tracking |
| `NETWORK_FORM` | Both P1 and P2 present in same proto-cell | n_P1 ≥ 1 AND n_P2 ≥ 1 | network_connected = true | Network activation |
| `NETWORK_BREAK` | One HIC type lost (by mutation, partition, or degradation) | n_P1 = 0 OR n_P2 = 0 | network_connected = false; compounding_active = false | Network failure |

---

## 6. Transition / Dependency Rules

### 6.1 Intra-Cycle

```
P1_CYCLE → TEMPLATE_FREED → (template available for P2 or replication)
P2_CYCLE → FIDELITY_UPDATE → (hic_quality_score adjusts)
```

### 6.2 Cross-Generational

```
GENERATION_ADVANCE:
  daughter.n_P1 ~ Binomial(parent.n_P1, 0.5)
  daughter.n_P2 ~ Binomial(parent.n_P2, 0.5)
  daughter.hic_quality_score = parent.hic_quality_score × (1 - p_sub_effective)
  if daughter.n_P1 >= 1 AND daughter.n_P2 >= 1:
    daughter.network_connected = true
    daughter.compounding_active = true
  else:
    daughter.network_connected = false
```

### 6.3 Compounding

```
Each generation with compounding_active:
  hic_quality_score += Δ_quality (from P2 proofreading)
  P1_efficiency += f(hic_quality_score)
  P2_efficiency += f(hic_quality_score)
  reproductive_advantage += g(P1_efficiency, P2_efficiency)
```

Converges to steady state when Δ_quality → 0 (fidelity plateau).

---

## 7. Recurrence-Tracking Fields

| Field | Type | Computation | Meaning |
|-------|------|------------|---------|
| `total_P1_events` | Integer | Σ P1_CYCLE across all P1 instances per cycle | Total replication-acceleration events |
| `total_P2_events` | Integer | Σ P2_CYCLE across all P2 instances per cycle | Total error-correction events |
| `total_directed_events` | Integer | P1 + P2 events | All HIC-driven events |
| `total_ambient_events` | Integer | All non-HIC process events | Background thermal events |
| `directed_fraction` | Float | directed / (directed + ambient) | System-level coupling significance |
| `generations_with_network` | Integer | Count of consecutive generations where network_connected = true | Network persistence metric |
| `cumulative_quality_gain` | Float | Σ Δ_quality across generations | Total compounding benefit |
| `reproductive_advantage_trend` | Float | Change in reproductive_advantage per generation | Whether advantage is growing, stable, or declining |

---

## 8. Uncertainty / Fragility Fields

| Field | Type | Description | Status |
|-------|------|-------------|--------|
| `η_couple_P1` | Unknown float | Coupling efficiency for P1 pairing | **UNDETERMINED** |
| `η_couple_P2` | Unknown float | Coupling efficiency for P2 pairing | **UNDETERMINED** |
| `concerted_mode_P1` | Boolean | Whether P1 operates in concerted mode | **PLAUSIBLE** |
| `concerted_mode_P2` | Boolean | Whether P2 operates in concerted mode | **PLAUSIBLE** |
| `n_P1_minimum` | Integer | Minimum P1 instances for system-relevant benefit | **UNKNOWN** (~2–4 estimated) |
| `n_P2_minimum` | Integer | Minimum P2 instances for system-relevant benefit | **UNKNOWN** (~2–4 estimated) |
| `network_partition_risk` | Float | Probability that division separates P1 from P2 in a daughter | Computable from n_P1, n_P2 |
| `fidelity_plateau_value` | Float | Steady-state hic_quality_score under P2 proofreading | **UNKNOWN** — depends on P2 discrimination threshold |
| `directed_fraction_estimate` | Float | Expected directed fraction | **ESTIMATED: ~5–10%** |

---

## 9. Verdict Fields

| Field | Type | Domain | Meaning |
|-------|------|--------|---------|
| `network_connectivity` | Enum | {`absent`, `isolated`, `connected`, `looped`} | P1+P2 network structure |
| `benefit_recurrence` | Enum | {`none`, `single_cycle`, `multi_cycle`, `cross_generational`} | Benefit persistence |
| `benefit_magnitude` | Enum | {`negligible`, `modest`, `system_relevant`, `dominant`} | How much the network matters |
| `directed_fraction_class` | Enum | {`negligible_<1%`, `supplementary_1-30%`, `significant_30-70%`, `dominant_>70%`} | Directed fraction category |
| `energy_level` | Enum | {`L4`, `L5_local`, `L5_networked_supplementary`, `L5_plus`, `L6`} | Updated classification |
| `proto_metabolism_status` | Enum | {`absent`, `supplementary_subnetwork`, `partial_system`, `dominant_system`, `full`} | Proto-metabolism verdict |
| `zeta_global_verdict` | Enum | {`A_no_network`, `B_supplementary_subnetwork`, `C_system_significant`} | Zeta outcome |

---

## 10. Minimal Serialized Example

```json
{
  "stage": "BOOK_V_TARGET_ZETA",
  "audit_type": "proto_metabolism_re_evaluation",

  "network": {
    "nodes": ["N_P1", "N_P2", "N_templates", "N_hic_quality"],
    "edges": [
      {"from": "N_P1", "to": "N_templates", "type": "produces"},
      {"from": "N_templates", "to": "N_P2", "type": "substrates_for"},
      {"from": "N_P2", "to": "N_hic_quality", "type": "improves"},
      {"from": "N_hic_quality", "to": "N_P1", "type": "enhances"},
      {"from": "N_hic_quality", "to": "N_P2", "type": "enhances"}
    ],
    "loops": ["P1 -> templates -> P2 -> quality -> P1"],
    "connected": true,
    "loop_type": "positive_feedback_bounded"
  },

  "protocell_state": {
    "n_P1_instances": 3,
    "n_P2_instances": 2,
    "template_pool_size": 15,
    "hic_quality_score": 0.95,
    "P1_events_per_cycle": 45,
    "P2_events_per_cycle": 30,
    "total_ambient_events": 1200,
    "directed_fraction": 0.059,
    "network_connected": true,
    "compounding_active": true,
    "reproductive_advantage": 1.42,
    "generations_with_network": 12
  },

  "classification": {
    "energy_level": "L5_networked_supplementary",
    "network_status": "connected_supplementary",
    "metabolism_status": "supplementary_subnetwork",
    "directed_fraction_class": "supplementary_1-30%",
    "benefit_magnitude": "system_relevant",
    "benefit_recurrence": "cross_generational"
  },

  "verdict": {
    "zeta_global_verdict": "B_supplementary_subnetwork",
    "proto_metabolism_justified": "partial_supplementary_only",
    "active_transport_justified": false,
    "atp_language_justified": false,
    "network_changes_program_state": true,
    "level_upgrade": "L5_local -> L5_networked_supplementary"
  },

  "cost": {
    "new_postulates": 0,
    "new_parameters": 0,
    "total_postulates": 14,
    "total_parameters": 7,
    "total_fields": 1,
    "total_dof": 6,
    "note": "Zeta adds no cost; network emerges from multiple HIC instances"
  },

  "fragility": {
    "network_partition_risk": 0.12,
    "eta_functional_window": [0.10, 0.50],
    "fidelity_plateau": null,
    "directed_fraction_stable": true
  },

  "next_step": "book_v_terminal_capstone"
}
```

---

## 11. Integration Notes

### 11.1 Relation to Epsilon State Model

Zeta extends Epsilon with:
- Network-level entities (`HIC_network`, `Template_pool`, `HIC_quality_state`)
- Network edges and loop structure
- Cross-generational compounding fields (`cumulative_quality_gain`, `generations_with_network`)
- Network-level classification variables (`network_status`, `metabolism_status`)
- Network failure event (`NETWORK_BREAK`)

All Epsilon-level per-HIC variables remain valid and are inherited.

### 11.2 What GRUT-RAI Must Track Post-Zeta

1. Network connectivity: whether both P1 and P2 are present in a proto-cell.
2. Compounding status: whether the P1→P2→quality→P1 loop is active.
3. Directed fraction: system-level significance of HIC coupling.
4. Cross-generational trends: whether reproductive advantage is stable, growing, or declining.
5. Network partition risk at division: probability of losing one HIC type.
6. Energetic level classification: L5_local vs L5_networked_supplementary vs higher.

---

*GRUT-RAI Proto-Metabolism State Model complete. Network nodes, edges, loops. Cross-generational compounding fields. Directed-fraction tracking. Energetic level and proto-metabolism classification. Fragility fields. Complete JSON serialization. Level 5 networked supplementary.*
