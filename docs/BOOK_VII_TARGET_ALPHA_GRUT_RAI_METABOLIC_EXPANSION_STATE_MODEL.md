# Book VII — Target Alpha: GRUT-RAI Metabolic Expansion State Model

## Minimum Machine-Usable State Model for Dominant-Metabolism Reasoning

---

## 1. Entity Types

| Entity ID | Name | Description | Parent |
|-----------|------|-------------|--------|
| `HIC_P3` | HIC variant for Pairing 3 | CS for soliton assembly; DS for boundary mesh incorporation | `HIC` |
| `HIC_P4` | HIC variant for Pairing 4 | CS for monomer assembly; DS for degraded-catalyst replacement | `HIC` |
| `HIC_Network_Expanded` | 4-node HIC network | P1+P2+P3+P4 with cascading connections | Network |
| `DiffusibleCarrier` | Loaded mobile molecule (Family G, conditional) | Produced at HIC CS; diffuses; discharges at remote target | Bridge object (if accepted) |
| `ProtoCell_M3` | M3-level proto-cell | Proto-cell with expanded supplementary metabolism (~15–25% directed) | ProtoCell |
| `ProtoCell_M4` | M4-level proto-cell (conditional) | Proto-cell with dominant metabolism (~30%+ directed) | ProtoCell (if G accepted) |

---

## 2. Energetic State Variables

### 2.1 Per-Proto-Cell Variables

| Variable | Type | Domain | Description |
|----------|------|--------|-------------|
| `n_hic_p1` | Integer ≥ 0 | | P1 HIC instance count |
| `n_hic_p2` | Integer ≥ 0 | | P2 HIC instance count |
| `n_hic_p3` | Integer ≥ 0 | | P3 HIC instance count |
| `n_hic_p4` | Integer ≥ 0 | | P4 HIC instance count |
| `n_hic_total` | Integer | Sum | Total HIC instances |
| `directed_events_per_cycle` | Float | | HIC-driven events per reproductive cycle |
| `ambient_events_per_cycle` | Float | | Thermally-driven events per cycle |
| `total_events_per_cycle` | Float | | Total events |
| `directed_fraction` | Float ∈ [0,1] | directed / total | System-level coupling significance |
| `cascade_amplification` | Float ≥ 1 | | Multiplier from P1→P2→P1 cascading |
| `saturation_factor` | Float ∈ (0,1] | | Per-HIC efficiency reduction from substrate competition |
| `effective_directed` | Float | directed_events × saturation_factor × cascade_amplification | Net directed flux |

### 2.2 Network Connectivity Fields

| Variable | Type | Description |
|----------|------|-------------|
| `network_nodes` | Set | {P1, P2, P3, P4} |
| `network_edges` | Set of tuples | Directed benefit links between nodes |
| `network_loops` | List | Identified reinforcing loops |
| `network_connectivity_score` | Float ∈ [0,1] | Fraction of possible edges that exist |

### 2.3 Flux / Accounting Fields

| Variable | Type | Description |
|----------|------|-------------|
| `directed_replication_fraction` | Float | Fraction of replication events that are HIC-driven |
| `directed_fidelity_fraction` | Float | Fraction of proofreading events that are HIC-driven |
| `directed_boundary_fraction` | Float | Fraction of boundary-growth events that are HIC-driven (P3) |
| `directed_repair_fraction` | Float | Fraction of catalyst-repair events that are HIC-driven (P4) |
| `ambient_dominant_processes` | List | Processes still overwhelmingly ambient-thermal |
| `saturation_ceiling_estimate` | Float ∈ [0,1] | Estimated maximum directed fraction under concerted mode |

### 2.4 Carrier Fields (Conditional — Only if Family G Accepted)

| Variable | Type | Description |
|----------|------|-------------|
| `carrier_present` | Boolean | Whether diffusible carrier is installed |
| `carrier_production_rate` | Float ≥ 0 | Loaded carriers produced per unit time |
| `carrier_lifetime` | Float > 0 | Mean time before carrier degrades or leaks |
| `carrier_utilization_rate` | Float ≥ 0 | Carriers consumed by useful discharge per unit time |
| `carrier_waste_rate` | Float ≥ 0 | Carriers lost to degradation or leakage per unit time |
| `carrier_utilization_efficiency` | Float ∈ [0,1] | utilization / (utilization + waste) |

---

## 3. Downstream-Impact Fields

| Variable | Type | Description |
|----------|------|-------------|
| `division_quality_impact` | Enum | {`none`, `incremental`, `significant`, `dominant`} |
| `lineage_robustness_impact` | Enum | Same |
| `adaptive_dynamics_impact` | Enum | Same |
| `boundary_maintenance_impact` | Enum | Same |
| `catalyst_repair_impact` | Enum | Same |
| `n_domains_with_directed_impact` | Integer | Count of domains where directed flux is non-negligible |
| `qualitative_organizational_inversion` | Boolean | True if directed > ambient for key processes |

---

## 4. Event Types

| Event ID | Name | Precondition | Postcondition |
|----------|------|-------------|---------------|
| `P3_CYCLE` | P3 HIC completes boundary-growth coupling | P3 primed + concerted | Boundary K=6/K=7 incorporated at driven site |
| `P4_CYCLE` | P4 HIC completes catalyst-repair coupling | P4 primed + concerted | Degraded catalyst chain displaced by functional one |
| `CASCADE_EVENT` | P1 output becomes P2 input (or vice versa) | P1 product (free template) → P2 DS | Cascading amplification of directed flux |
| `SATURATION_CHECK` | Evaluate substrate competition across all HICs | Every time step | saturation_factor updated |
| `CARRIER_PRODUCE` | (Conditional) HIC produces loaded carrier | CS reaction complete; carrier chemistry available | carrier_count += 1 |
| `CARRIER_DISCHARGE` | (Conditional) Carrier discharges at remote target | Carrier meets compatible target by diffusion | Target process driven; carrier → unloaded |
| `CARRIER_LEAK` | (Conditional) Carrier degrades without useful discharge | carrier_lifetime exceeded | carrier_count -= 1; energy wasted |

---

## 5. Transition Rules

### 5.1 Directed-Fraction Computation (Concerted Mode — M3)

```
total_hic_events = Σ(n_hic_i × events_per_hic_i × saturation_factor)
cascade_events = total_hic_events × (cascade_amplification - 1)
effective_directed = total_hic_events + cascade_events
directed_fraction = effective_directed / (effective_directed + ambient_events)

saturation_factor = substrate_pool / (substrate_pool + n_hic_total × K_half_per_hic)
# Michaelis-Menten-like saturation as HICs compete for substrates
```

### 5.2 Directed-Fraction Computation (With Carrier — M4, Conditional)

```
carrier_production = n_hic_total × carrier_production_per_hic
carrier_available = carrier_production × carrier_lifetime × carrier_utilization_efficiency
carrier_driven_events = carrier_available × discharge_rate_per_carrier
total_directed = hic_site_events + carrier_driven_events
directed_fraction = total_directed / (total_directed + ambient_events)
# No substrate-competition ceiling for carrier-driven events
```

### 5.3 Energetic Level Auto-Classification

```
if directed_fraction < 0.03:
    metabolic_level = "M1_local"
elif directed_fraction < 0.10:
    metabolic_level = "M2_networked_supplementary"
elif directed_fraction < 0.30:
    metabolic_level = "M3_expanded_supplementary"
elif directed_fraction < 0.50:
    metabolic_level = "M4_dominant"
else:
    metabolic_level = "M5_dominant_with_currency"
```

---

## 6. Uncertainty / Fragility Fields

| Field | Type | Description | Status |
|-------|------|-------------|--------|
| `saturation_ceiling_exact` | Unknown float | Exact concerted-mode ceiling | **ESTIMATED ~25–35%** |
| `cascade_amplification_exact` | Unknown float | Exact amplification factor | **ESTIMATED ~1.3–1.5x** |
| `p3_feasibility` | Boolean | Whether P3 (boundary coupling) works in practice | **PLAUSIBLE but unverified** |
| `p4_feasibility` | Boolean | Whether P4 (catalyst repair) works in practice | **PLAUSIBLE but unverified** |
| `carrier_postulate_needed` | Boolean | Whether Family G bridge is required for M4 | **YES for guaranteed M4; NO for M3** |
| `carrier_chemistry_exists` | Boolean | Whether a loaded-state diffusible molecule can be produced | **POSTULATE-DEPENDENT** |
| `carrier_lifetime_sufficient` | Boolean | Whether carrier persists long enough to diffuse to target | **UNKNOWN** |
| `m4_reachable_zero_cost` | Boolean | Whether favorable parameters place M3 ceiling above 30% | **CONDITIONAL** |

---

## 7. Verdict Fields

| Field | Type | Domain | Meaning |
|-------|------|--------|---------|
| `metabolic_level` | Enum | {`M0`–`M5`} | Current energetic classification |
| `directed_fraction_class` | Enum | {`negligible`, `supplementary`, `expanded_supplementary`, `dominant`, `dominant_with_currency`} | Fraction category |
| `zero_cost_expansion_achieved` | Boolean | Whether M3 is reached at zero cost | YES |
| `dominant_achieved` | Enum | {`no`, `conditional`, `yes`} | Whether M4 is reached |
| `new_bridge_needed_for_m4` | Boolean | Whether Family G is required for guaranteed M4 | YES |
| `carrier_bridge_justified` | Boolean | Whether the program should invest in Family G | PROGRAM DECISION |
| `alpha_changes_state` | Boolean | Whether this audit upgrades metabolic level | YES (M2→M3) |
| `alpha_global_verdict` | Enum | {`A_ceiling_reached`, `B_conditional_approach`, `C_dominant_achieved`} | Alpha outcome |

---

## 8. Minimal Serialized Example

```json
{
  "stage": "BOOK_VII_TARGET_ALPHA",
  "audit_type": "dominant_metabolism_and_energetic_expansion",

  "energetic_state": {
    "n_hic_p1": 3,
    "n_hic_p2": 3,
    "n_hic_p3": 2,
    "n_hic_p4": 2,
    "n_hic_total": 10,
    "directed_events_per_cycle": 180,
    "ambient_events_per_cycle": 820,
    "total_events_per_cycle": 1000,
    "directed_fraction": 0.18,
    "cascade_amplification": 1.35,
    "saturation_factor": 0.75,
    "effective_directed_fraction": 0.22,
    "saturation_ceiling_estimate": 0.30
  },

  "network": {
    "nodes": ["P1", "P2", "P3", "P4"],
    "edges": [
      ["P1", "P2", "template_feed"],
      ["P2", "P1", "fidelity_improvement"],
      ["P2", "P3", "quality_support"],
      ["P2", "P4", "quality_support"],
      ["P3", "all", "boundary_maintenance"],
      ["P4", "all", "catalyst_repair"]
    ],
    "loops": ["P1->P2->quality->P1", "P3->boundary->retention->all", "P4->repair->function->all"],
    "connectivity_score": 0.75
  },

  "downstream_impact": {
    "division_quality": "incremental",
    "lineage_robustness": "incremental",
    "adaptive_dynamics": "incremental",
    "boundary_maintenance": "significant",
    "catalyst_repair": "significant",
    "n_domains_with_impact": 5,
    "organizational_inversion": false
  },

  "carrier_state": {
    "carrier_present": false,
    "carrier_bridge_status": "identified_not_installed",
    "carrier_cost": {"postulates": 1, "parameters": "1-2"}
  },

  "classification": {
    "metabolic_level": "M3_expanded_supplementary",
    "directed_fraction_class": "expanded_supplementary",
    "dominant_achieved": "conditional",
    "new_bridge_needed_for_m4": true
  },

  "cost": {
    "new_postulates": 0,
    "new_parameters": 0,
    "new_fields": 0,
    "new_dof": 0,
    "total_postulates": 14,
    "total_parameters": 7,
    "total_fields": 1,
    "total_dof": 6,
    "zero_cost_target_number": 23
  },

  "verdict": {
    "alpha_global_verdict": "B_conditional_approach",
    "alpha_changes_state": true,
    "level_upgrade": "M2 -> M3",
    "m4_status": "conditional_on_parameters_or_carrier_bridge",
    "program_decision_needed": "accept_M3_or_invest_in_carrier_bridge",
    "next_audit": "carrier_bridge_architecture_or_m3_downstream_consequences"
  }
}
```

---

## 9. Integration Notes

### 9.1 What This Extends

Book VII Alpha extends the Book VI terminal state model with:
- Two new HIC pairing types (P3 boundary, P4 repair)
- 4-node network representation (up from 2-node)
- Cascade amplification field
- Saturation/ceiling modeling
- Conditional carrier fields (for Family G if accepted)
- Downstream multi-domain impact tracking
- M0–M5 metabolic level ladder
- Program-decision fields

### 9.2 What GRUT-RAI Must Track Post-Alpha

1. **Metabolic level = M3** (expanded supplementary; ~15–25% directed).
2. **4-node HIC network** (P1+P2+P3+P4) with cascading connections.
3. **P3 = first directed boundary growth.** New process domain.
4. **P4 = first directed catalyst repair.** New process domain.
5. **Saturation ceiling ~25–35%.** Concerted-mode structural limit.
6. **Family G carrier identified but not installed.** Program decision pending.
7. **Zero cost achieved.** Twenty-third zero-cost target.
8. **Program decision needed:** Accept M3 (zero cost) or invest in M4 (1 postulate + 1–2 params).

---

*GRUT-RAI Metabolic Expansion State Model complete. Entity types, energetic state variables, network/connectivity fields, downstream-impact fields, saturation modeling, conditional carrier fields, M0–M5 classification, verdict fields, JSON serialization. M3 at zero cost. M4 conditional on carrier bridge. Program decision pending.*
