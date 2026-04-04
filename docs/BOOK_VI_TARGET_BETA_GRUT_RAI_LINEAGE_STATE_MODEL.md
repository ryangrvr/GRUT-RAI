# Book VI — Target Beta: GRUT-RAI Lineage State Model

## Minimum Machine-Usable State Model for Lineage-Robustness Reasoning

---

## 1. Entity Types

| Entity ID | Name | Description | Parent |
|-----------|------|-------------|--------|
| `Lineage` | Proto-cell lineage | Genealogical tree of related proto-cells; tracks essential-type retention across generations | System |
| `Generation` | One generation of a lineage | All proto-cells at the same genealogical depth | Lineage |
| `ProtoCell_L3` | L3-robust proto-cell | Proto-cell with D3 division + L3 lineage-robustness package | ProtoCell_D3 |
| `EssentialTypeSet` | Set of essential content classes | The minimum functional types a daughter needs to be viable | Content |
| `LineageBranch` | One branch of the lineage tree | A single line of descent from parent to ultimate descendant | Lineage |

---

## 2. State Variables

### 2.1 Per-Proto-Cell Variables (inherited from Alpha model)

| Variable | Type | Domain | Description |
|----------|------|--------|-------------|
| `content_vector` | Map[TypeID → count] | {template_types, catalysts, assembly_cats, HIC_P1, HIC_P2, boundary_material} | Per-type copy count |
| `content_quality` | Float ∈ [0,1] | From P2 proofreading | Quality score of internal content |
| `division_threshold` | Float | Heritable | Content-to-boundary ratio triggering fission |
| `cluster_coherence` | Float ∈ [0,1] | From spatial organization | How well internal objects are spatially clustered |
| `viable` | Boolean | | Has all essential types at ≥ 1 copy |

### 2.2 Daughter-State Fields

| Variable | Type | Description |
|----------|------|-------------|
| `daughter_content_vector` | Map[TypeID → count] | Inherited portion |
| `daughter_has_all_essential` | Boolean | True if every essential type has ≥ 1 copy |
| `daughter_quality` | Float ∈ [0,1] | Inherited quality score |
| `daughter_hic_complete` | Boolean | Has both P1 and P2 |
| `daughter_viable` | Boolean | daughter_has_all_essential AND boundary_sealed |

### 2.3 Lineage-Tracking Fields

| Variable | Type | Domain | Description |
|----------|------|--------|-------------|
| `generation_depth` | Integer ≥ 0 | | Number of generations from original ancestor |
| `lineage_size` | Integer ≥ 0 | | Number of currently viable proto-cells in the lineage |
| `cumulative_type_loss_events` | Integer ≥ 0 | | Total essential-type loss events across all branches |
| `lineage_alive` | Boolean | | lineage_size > 0 |
| `branches_alive` | Integer ≥ 0 | | Number of surviving branches |
| `branches_extinct` | Integer ≥ 0 | | Number of branches that lost essential types |
| `essential_type_retention_rate` | Float ∈ [0,1] | Per generation | Fraction of daughters retaining all essential types |
| `lineage_half_life` | Float | Generations | Estimated generations until P(lineage survives) = 0.5 |
| `net_growth_rate` | Float | Per generation | 2 × (1 − p_loss) − 1 |

### 2.4 Robustness Classification Fields

| Variable | Type | Domain | Description |
|----------|------|--------|-------------|
| `lineage_level` | Enum | {`L0`, `L1`, `L2`, `L3`, `L4`, `L5`} | Lineage-robustness classification |
| `robustness_package_active` | Boolean | | True if A+B+C+D+E routes all operative |
| `p_any_loss_per_gen` | Float ∈ [0,1] | | Per-generation probability of any essential-type loss |
| `partition_bias_strength` | Float ∈ [0,1] | | Effectiveness of Route D spatial correlation |
| `quality_filter_active` | Boolean | | True if Route C quality-linked culling is operative |
| `catch_up_active` | Boolean | | True if Route E HIC catch-up is operative |

---

## 3. Event Types

| Event ID | Name | Precondition | Postcondition |
|----------|------|-------------|---------------|
| `GENERATION_STEP` | One generation passes | All proto-cells in current generation divide | New generation produced; lineage stats updated |
| `DIVISION_EVENT` | One proto-cell divides | Proto-cell at or above division threshold | Two daughters with content vectors from partition |
| `TYPE_LOSS_EVENT` | A daughter misses an essential type | daughter_has_all_essential = false | Branch marked for extinction or degraded operation |
| `BRANCH_EXTINCTION` | A branch produces no further viable descendants | All descendants of a branch are nonviable | branches_extinct += 1; branch removed from active tracking |
| `LINEAGE_EXTINCTION` | All branches extinct | branches_alive = 0 | lineage_alive = false |
| `CATCH_UP_EVENT` | Under-equipped daughter recovers copy count | daughter has HIC + at least 1 copy of all types | Content_vector counts increase toward normal |
| `QUALITY_CULL_EVENT` | Low-quality proto-cell fails to reach division threshold | content_quality below functional-accumulation threshold | Proto-cell stalls; effectively removed from lineage |

---

## 4. Transition Rules

### 4.1 Per-Generation Update

```
for each proto_cell in current_generation:
    if proto_cell.viable:
        daughter_1, daughter_2 = DIVIDE(proto_cell)
        for each daughter in [daughter_1, daughter_2]:
            if daughter.daughter_has_all_essential:
                next_generation.add(daughter)
            else:
                TYPE_LOSS_EVENT(daughter)
                if daughter can partially function:
                    degraded_pool.add(daughter)  # may recover via catch-up
                else:
                    BRANCH_EXTINCTION(daughter.branch)

lineage_size = len(next_generation)
generation_depth += 1
essential_type_retention_rate = len(next_generation) / (2 * len(current_generation))
```

### 4.2 Essential-Type Loss Probability

```
for each essential_type i:
    N_i = proto_cell.content_vector[type_i]
    bias_D = partition_bias_strength  # from Route D
    p_loss_i = (0.5)^N_i * (1 - bias_D)

p_any_loss = 1 - product(1 - p_loss_i for all i)
```

### 4.3 Lineage Half-Life Computation

```
# Single non-branching lineage:
half_life_single = ln(2) / p_any_loss

# Branching lineage: effectively immortal if net_growth_rate > 0
# Practical half-life = time until lineage size < initial (accounting for branching + loss)
net_growth_rate = 2 * (1 - p_any_loss) - 1
if net_growth_rate > 0:
    lineage_status = "growing"
    # Half-life in branching context is very long (exponential growth overwhelms loss)
else:
    lineage_status = "declining"
    half_life_branching = ln(2) / abs(net_growth_rate)
```

---

## 5. Extinction / Persistence Conditions

| Condition | Meaning | Outcome |
|-----------|---------|---------|
| `p_any_loss < 0.5` | More than half of daughters are fully viable | **LINEAGE GROWS** — exponential branching overwhelms loss |
| `p_any_loss > 0.5` | Fewer than half of daughters are viable | **LINEAGE DECLINES** — loss overwhelms branching |
| `p_any_loss ≈ 0.5` | Critical threshold | **LINEAGE MARGINAL** — random walk; may survive or not |
| `p_any_loss < 0.01` | Nearly all daughters viable | **INHERITANCE-ROBUST (L4)** — essential types reliably retained |
| Current scaffold: `p_any_loss ≈ 0.04` | ~96% viable | **L3 SUPPLEMENTARY ROBUSTNESS** — growing but not guaranteed |

---

## 6. Uncertainty / Fragility Fields

| Field | Type | Description | Status |
|-------|------|-------------|--------|
| `spatial_clustering_strength` | Unknown float | Route D effectiveness | **UNQUANTIFIED** |
| `partition_bias_actual` | Unknown float | Actual improvement from Route D | **ESTIMATED ~30%** |
| `catch_up_effectiveness` | Unknown float | How quickly under-equipped daughters recover | **ESTIMATED moderate** |
| `p_any_loss_exact` | Unknown float | Actual per-gen failure rate | **ESTIMATED ~0.04** |
| `lineage_half_life_exact` | Unknown float | Actual single-lineage half-life | **ESTIMATED ~16 gen** |
| `L3_vs_L4_boundary` | Float | p_any_loss threshold separating L3 from L4 (~0.01) | **DEFINED at ~1%** |

---

## 7. Verdict Fields

| Field | Type | Domain | Meaning |
|-------|------|--------|---------|
| `lineage_level` | Enum | {`L0`–`L5`} | Lineage-robustness classification |
| `inheritance_robust` | Boolean | | True only if p_any_loss < ~0.01 (L4) |
| `robustness_package_complete` | Boolean | | True if all five routes active |
| `beta_changes_state` | Boolean | | True if lineage level upgraded |
| `beta_global_verdict` | Enum | {`A_no_robustness`, `B_supplementary_L3`, `C_inheritance_robust_L4`} | Beta outcome |
| `new_bridge_debt` | Boolean | | False (all zero-cost) |
| `next_audit` | String | | Recommended next stage |

---

## 8. Minimal Serialized Example

```json
{
  "stage": "BOOK_VI_TARGET_BETA",
  "audit_type": "inheritance_and_lineage_robustness",

  "lineage_state": {
    "lineage_level": "L3",
    "generation_depth": 16,
    "lineage_size": 18500,
    "branches_alive": 18500,
    "branches_extinct": 3200,
    "cumulative_type_loss_events": 3200,
    "essential_type_retention_rate": 0.957,
    "p_any_loss_per_gen": 0.043,
    "net_growth_rate": 0.914,
    "lineage_status": "growing"
  },

  "robustness_package": {
    "route_A_redundancy": true,
    "route_B_partition_amplification": true,
    "route_C_quality_culling": true,
    "route_D_timing_completeness": true,
    "route_E_hic_catchup": true,
    "package_complete": true
  },

  "classification": {
    "lineage_level": "L3_supplementary",
    "inheritance_robust": false,
    "p_any_loss": 0.043,
    "L4_threshold": 0.01,
    "gap_to_L4": "4.3x"
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
    "zero_cost_target_number": 21
  },

  "verdict": {
    "beta_global_verdict": "B_supplementary_L3",
    "beta_changes_state": true,
    "level_upgrade": "L1 -> L3",
    "inheritance_robust_justified": false,
    "darwinian_adaptation_justified": false,
    "next_audit": "proto_darwinian_dynamics_and_selection_landscape"
  },

  "fragility": {
    "spatial_clustering": "unquantified",
    "partition_bias_estimate": 0.30,
    "catch_up_effectiveness": "moderate",
    "p_any_loss_estimate": 0.043,
    "lineage_half_life_estimate": 16
  }
}
```

---

## 9. Integration Notes

### 9.1 What This Extends

Book VI Beta extends the Alpha division-control state model with:
- Lineage-tracking variables (generation depth, lineage size, branch counts, extinction events)
- Multi-generation persistence logic (essential-type retention across generations)
- Five robustness routes (A–E) with connected-package representation
- Lineage-level classification ladder (L0–L5)
- Extinction/persistence conditions
- Branching-lineage growth model

### 9.2 What GRUT-RAI Must Track Post-Beta

1. **Lineage level = L3** — supplementary lineage robustness; not L4 (inheritance-robust).
2. **p_any_loss ≈ 0.04** — ~4% per-generation essential-type loss; gap to L4 is ~4x.
3. **Five robustness routes active** — A (redundancy) + B (partition amplification) + C (quality culling) + D (timing completeness) + E (HIC catch-up).
4. **Lineage persistence: resilient** — growing population; branches lost but lineage survives.
5. **Zero cost** — twenty-first zero-cost upper-stack target.
6. **Next boundary: proto-Darwinian dynamics** — hereditary variation + differential success + lineage persistence → does this produce directional adaptive change?

### 9.3 What GRUT-RAI Must NOT Carry Forward

- Any claim of inheritance-robust reproduction (L4) — ~4% per-gen failure; depends on population branching.
- Any claim of Darwinian adaptation — proto-selection present but directional improvement not demonstrated.
- Any claim of guaranteed essential-type retention — partition is biased but not enforced.
- Any claim of modern heredity machinery — no chromosome segregation, no checkpoint control.

---

*GRUT-RAI Lineage State Model complete. Entity types, state variables (per-cell, daughter, lineage, classification), event types, transition rules, extinction/persistence conditions, fragility fields, verdict fields, JSON serialization. L3 supplementary lineage robustness. Zero cost. Twenty-first zero-cost target.*
