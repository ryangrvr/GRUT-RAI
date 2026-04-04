# Book VI — Target Alpha: GRUT-RAI Division Control State Model

## Minimum Machine-Usable State Model for Division-Regulation Reasoning

---

## 1. Entity Types

| Entity ID | Name | Description | Parent |
|-----------|------|-------------|--------|
| `ProtoCell_D3` | D3-regulated proto-cell | Proto-cell with A+C+D supplementary division-control package | `ProtoCell_HIC` |
| `BoundaryMesh` | Mesh boundary | K=7+K=6 polyhedral cage with non-uniform topology | Compartment |
| `FissionSite` | Preferential fission location | Geometrically weak region in boundary mesh | BoundaryMesh |
| `FunctionalCluster` | Spatial cluster of functional objects | Templates + catalysts + HICs localized near production sites | Internal |
| `DaughterCell` | Post-fission compartment | Inherits portion of parent content and boundary | ProtoCell |

---

## 2. State Variables

### 2.1 Pre-Division State

| Variable | Type | Domain | Description |
|----------|------|--------|-------------|
| `content_count` | Integer ≥ 0 | Total large retained objects inside proto-cell | Drives pressure |
| `boundary_area` | Float > 0 | Total mesh surface area | Determines volume capacity |
| `content_to_boundary_ratio` | Float | content_count / V(boundary_area) | Primary division-timing variable (Route A) |
| `division_threshold` | Float | Characteristic ratio at which fission is triggered | Set by assembly-catalyst content/boundary branching ratio; heritable |
| `content_quality_score` | Float ∈ [0,1] | Fraction of internal copies that are fully functional | From P2 proofreading (Route C) |
| `functional_copy_rate` | Float ≥ 0 | Rate of producing functional (non-degraded) copies | Coupled to content_quality_score |
| `n_functional_clusters` | Integer ≥ 0 | Number of spatially distinct functional-object clusters | Route D topology |
| `cluster_coherence` | Float ∈ [0,1] | Average within-cluster functional completeness | 1.0 = every cluster has all essential types |
| `n_fission_sites` | Integer ≥ 0 | Number of geometrically weak boundary regions | From K=7 topology |
| `fission_site_alignment` | Float ∈ [0,1] | How well fission sites separate coherent clusters | 1.0 = perfect alignment |

### 2.2 Division Event State

| Variable | Type | Domain | Description |
|----------|------|--------|-------------|
| `division_triggered` | Boolean | | True when content_to_boundary_ratio > division_threshold |
| `fission_site_selected` | Integer | Index of weakest boundary site | Determined by mesh topology |
| `partition_ratio` | Float ∈ (0,1) | Fraction of content going to daughter_1 | ~0.5 on average; variance from spatial distribution |
| `daughter_1_content` | Vector | Subset of parent content | Determined by partition at fission site |
| `daughter_2_content` | Vector | Complement of daughter_1_content | |

### 2.3 Daughter Viability State

| Variable | Type | Domain | Description |
|----------|------|--------|-------------|
| `d1_has_templates` | Boolean | | Does daughter 1 have ≥ 1 template of each essential type? |
| `d1_has_catalysts` | Boolean | | Does daughter 1 have ≥ 1 replication catalyst? |
| `d1_has_assembly` | Boolean | | Does daughter 1 have ≥ 1 assembly catalyst? |
| `d1_has_hic` | Boolean | | Does daughter 1 have ≥ 1 HIC scaffold? |
| `d1_viable` | Boolean | | All of the above true AND boundary sealed |
| `d2_viable` | Boolean | | Same checks for daughter 2 |
| `both_viable` | Boolean | | d1_viable AND d2_viable |
| `division_quality` | Enum | {`both_viable`, `one_viable`, `neither_viable`} | Outcome classification |

---

## 3. Event Types

| Event ID | Name | Precondition | Postcondition |
|----------|------|-------------|---------------|
| `CONTENT_ACCUMULATE` | Internal content grows | Proto-cell active; feedstock available | content_count += Δ; content_to_boundary_ratio increases |
| `BOUNDARY_GROW` | Mesh boundary expands | Assembly catalysts producing K=6/K=7; free bonding sites available | boundary_area += Δ_boundary |
| `QUALITY_FILTER` | P2 proofreading affects content quality | P2 HIC active | content_quality_score updated; functional_copy_rate adjusted |
| `THRESHOLD_CHECK` | Evaluate division trigger | Every time step | division_triggered = (ratio > threshold) |
| `FISSION_INITIATE` | Division begins | division_triggered = true | fission_site_selected; necking begins |
| `FISSION_COMPLETE` | Division finishes | Neck breaks | Two daughters produced; content partitioned by spatial distribution |
| `DAUGHTER_ASSESS` | Evaluate daughter viability | Fission complete | d1_viable, d2_viable, division_quality computed |
| `DAUGHTER_RESEAL` | Daughter boundaries close | Post-fission | Open edges bond with available K=6/K=7 |
| `DAUGHTER_CONTINUE` | Viable daughter resumes cycle | d_viable = true AND boundary sealed | New proto-cell enters CONTENT_ACCUMULATE |

---

## 4. Transition Rules

### 4.1 Division Timing (Route A)

```
content_to_boundary_ratio = content_count / V(boundary_area)

if content_to_boundary_ratio > division_threshold:
    FISSION_INITIATE
else:
    continue CONTENT_ACCUMULATE + BOUNDARY_GROW

division_threshold is heritable:
    daughter.division_threshold ≈ parent.division_threshold ± mutation
    selection favors threshold values that minimize nonviable-daughter rate
```

### 4.2 Quality Filtering (Route C)

```
functional_copy_rate = base_replication_rate × content_quality_score
content_quality_score = f(P2_activity, p_sub)

time_to_threshold = division_threshold × V(boundary) / functional_copy_rate

higher quality → higher functional_copy_rate → shorter time_to_threshold
    (but with more functional content at division)
lower quality → lower functional_copy_rate → longer time_to_threshold
    (or never reach threshold → lineage dies)
```

### 4.3 Partition Bias (Route D)

```
at FISSION_COMPLETE:
    fission_site = argmin(boundary_strength[sites])  # weakest point

    for each functional_object in parent:
        if object.position is on side_1 of fission_site:
            daughter_1_content.add(object)
        else:
            daughter_2_content.add(object)

    cluster_inheritance = measure(daughter_content vs parent_clusters)

    higher fission_site_alignment → more coherent cluster inheritance
    → higher probability both_viable
```

---

## 5. Daughter-State Fields

| Field | Type | Description |
|-------|------|-------------|
| `daughter_content_vector` | List[ObjectType → count] | How many of each essential type inherited |
| `daughter_cluster_completeness` | Float ∈ [0,1] | Fraction of inherited clusters that are functionally complete |
| `daughter_boundary_integrity` | Float ∈ [0,1] | Fraction of boundary successfully resealed |
| `daughter_initial_quality` | Float ∈ [0,1] | Content quality score at birth |
| `daughter_hic_count` | Integer | Number of functional HIC scaffolds inherited |
| `daughter_division_threshold` | Float | Inherited (possibly mutated) threshold value |

---

## 6. Viability-Tracking Fields

| Field | Type | Computation | Meaning |
|-------|------|------------|---------|
| `viability_rate` | Float ∈ [0,1] | (both_viable events) / (total division events) over many cycles | Population-level division quality |
| `nonviable_rate` | Float | 1 - viability_rate | Failure rate |
| `single_viable_rate` | Float | (one_viable events) / total | Partial failure rate |
| `lineage_persistence` | Integer | Generations before lineage loses an essential type | Multi-generational tracking |
| `division_level` | Enum | {D0, D1, D2, D3, D4, D5} | Current classification |

---

## 7. Uncertainty / Fragility Fields

| Field | Type | Description | Status |
|-------|------|-------------|--------|
| `spatial_clustering_strength` | Unknown float | How strongly functional objects cluster spatially | **UNQUANTIFIED** — determines Route D effectiveness |
| `fission_site_alignment_actual` | Unknown float | How well fission sites separate clusters in practice | **UNQUANTIFIED** |
| `threshold_heritability` | Unknown float | How accurately daughters inherit the parent's division threshold | **ASSUMED high** — sequence-dependent; replicable |
| `quality_filter_magnitude` | Unknown float | How much P2 proofreading changes the functional-copy accumulation rate | **ESTIMATED ~40%** — from Book V Zeta |
| `nonviable_rate_estimate` | Float | Population-level estimate of daughter failure rate | **~3–8% (estimated)** — down from ~10–30% |
| `d3_vs_d4_boundary` | Float | Threshold nonviable rate separating D3 from D4 (~5%) | **PARAMETER-DEPENDENT** |

---

## 8. Verdict Fields

| Field | Type | Domain | Meaning |
|-------|------|--------|---------|
| `division_level` | Enum | {`D0`, `D1`, `D2`, `D3`, `D4`, `D5`} | Current division-regulation classification |
| `routes_surviving` | List | Route IDs that pass hard criteria | Currently: [A, C, D] |
| `connected_package` | Boolean | Whether surviving routes form a connected control system | YES |
| `nonviable_rate_class` | Enum | {`high_>15%`, `moderate_5-15%`, `low_1-5%`, `robust_<1%`} | Failure-rate classification |
| `inheritance_robustness` | Enum | {`not_achieved`, `partial`, `achieved`} | Whether daughters reliably inherit complete functional sets |
| `new_bridge_debt` | Boolean | Whether new postulates were required | NO |
| `alpha_changes_program_state` | Boolean | Whether this audit upgrades the scaffold | YES (D1→D3) |

---

## 9. Minimal Serialized Example

```json
{
  "stage": "BOOK_VI_TARGET_ALPHA",
  "audit_type": "regulated_growth_and_division",

  "division_state": {
    "division_level": "D3",
    "surviving_routes": ["A_timing", "C_quality", "D_partition"],
    "connected_package": true,
    "package_name": "A+C+D supplementary division-control package",
    "nonviable_rate_pre": "0.10-0.30",
    "nonviable_rate_post": "0.03-0.08",
    "improvement_factor": "~3x"
  },

  "route_details": {
    "A": {
      "mechanism": "content_load_responsive_timing",
      "uses": "assembly_catalysts_boundary_growth_coupling",
      "cost": 0,
      "benefit": "reproducible_division_timing"
    },
    "C": {
      "mechanism": "P2_quality_dependent_timing_bias",
      "uses": "existing_P2_HIC_proofreading",
      "cost": 0,
      "benefit": "quality_filtered_parents"
    },
    "D": {
      "mechanism": "spatial_correlation_preferential_cleavage",
      "uses": "K7_mesh_topology_large_object_clustering",
      "cost": 0,
      "benefit": "coherent_cluster_partition"
    }
  },

  "classification": {
    "division_level": "D3_supplementary_regulated",
    "nonviable_rate_class": "moderate_5-15%",
    "inheritance_robustness": "not_achieved",
    "timing_control": "content_load_responsive",
    "quality_control": "P2_quality_dependent_bias",
    "partition_control": "spatial_correlation_geometry"
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
    "zero_cost_target_number": 20,
    "note": "All three routes use existing structures"
  },

  "verdict": {
    "global_verdict": "B_partial_supplementary_regulated",
    "alpha_changes_program_state": true,
    "level_upgrade": "D1 -> D3",
    "inheritance_robustness_justified": false,
    "full_regulated_reproduction_justified": false,
    "next_audit": "inheritance_and_lineage_robustness"
  },

  "uncertainties": {
    "spatial_clustering_strength": "unquantified",
    "fission_site_alignment": "unquantified",
    "d3_vs_d4_boundary": "parameter_dependent",
    "nonviable_rate_exact": "estimated_3-8pct"
  }
}
```

---

## 10. Integration Notes

### 10.1 What This Extends

Book VI Alpha extends the Book V terminal state model with:
- Division-level classification (D0–D5 ladder)
- Route-specific state variables (threshold, quality score, clustering, alignment)
- Daughter-state vectors (content, completeness, integrity, quality, HIC count)
- Viability-tracking fields (nonviable rate, lineage persistence)
- Connected-package representation (A+C+D as one control system)

### 10.2 What GRUT-RAI Must Track Post-Alpha

1. **Division level = D3** — not D1 (pre-Alpha), not D4/D5 (not achieved).
2. **Three routes active:** A (timing), C (quality), D (partition) — all zero-cost, all structural.
3. **Nonviable rate ~3–8%** — down from ~10–30%; significant but not robust.
4. **No new bridge debt** — twentieth zero-cost upper-stack target.
5. **Inheritance robustness: NOT achieved** — daughters are better equipped but not guaranteed complete.
6. **Next boundary: inheritance and lineage robustness** — can lineages persist for many generations?

### 10.3 What GRUT-RAI Must NOT Carry Forward

- Any claim of checkpoint behavior (the A+C+D package is bias, not decision logic).
- Any claim of inheritance robustness (D5 not reached).
- Any claim of full regulated reproduction (D3 is supplementary, not deterministic).
- Any claim of modern cell-cycle control (no G1/S/G2/M; no cyclins; no spindle).

---

*GRUT-RAI Division Control State Model complete. Entity types, state variables (pre-division, division-event, daughter, viability), event types, transition rules, uncertainty fields, verdict fields, and JSON serialization. D3 supplementary regulated division. Zero cost. Twentieth zero-cost target.*
