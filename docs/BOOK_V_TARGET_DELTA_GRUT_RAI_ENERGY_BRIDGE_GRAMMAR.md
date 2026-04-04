# Book V — Target Delta: GRUT-RAI Energy Bridge Grammar

## Minimum Formal Grammar for Machine-Readable Energy-Coupling Reasoning

---

## 1. Purpose

This document defines the minimum formal grammar GRUT-RAI needs to reason over the energy-coupling bridge stage. It provides entity types, state variables, event types, transition rules, uncertainty fields, failure classes, cost/debt fields, and an example serialized representation.

---

## 2. Entity Types

| Entity ID | Name | Description | Parent type |
|-----------|------|-------------|-------------|
| `HIC` | Hybrid Intercepting Catalyst | Scaffold with capture-discharge coupling through backbone strain | `CatalyticScaffold` |
| `HIC_unloaded` | HIC in unloaded state | Relaxed backbone; capture site available; discharge site inactive | `HIC` state |
| `HIC_loaded` | HIC in loaded state | Strained backbone; capture site occupied/reset; discharge site active | `HIC` state |
| `SourceSubstrate` | Source reaction substrate | Object consumed by favorable reaction at capture site | `Monomer` or `Soliton` |
| `SourceProduct` | Source reaction product | Object produced by favorable reaction; its geometry triggers loading | `Composite` |
| `TargetSubstrate` | Target reaction substrate | Object bound at discharge site; driven by strain release | `Duplex` or `Chain` |
| `TargetProduct` | Target reaction product | Object produced by driven unfavorable reaction | `SeparatedStrands` or `CorrectedChain` |
| `ThermalBath` | Thermal environment | Sink for leaked/dissipated energy | Environment |

---

## 3. State Variables

| Variable | Type | Domain | Description |
|----------|------|--------|-------------|
| `conformation` | Enum | {`unloaded`, `loaded`} | Current conformational state of HIC |
| `strain_energy` | Float ≥ 0 | [0, ΔG_source × η_couple_max] | Energy stored in backbone strain (kT units) |
| `capture_site_occupancy` | Enum | {`empty`, `substrate_bound`, `product_formed`} | State of capture pocket |
| `discharge_site_occupancy` | Enum | {`empty`, `target_bound`, `product_released`} | State of discharge site |
| `η_couple` | Float ∈ (0, 1) | Coupling efficiency parameter | Fraction of source energy captured as strain |
| `ΔG_barrier` | Float > 0 | Strain relaxation barrier (kT) | Kinetic stability of loaded state |
| `leak_rate` | Float ≥ 0 | exp(−ΔG_barrier / kT) × ν_0 | Rate of spontaneous unloading |
| `cycle_count` | Integer ≥ 0 | N | Number of completed capture-discharge cycles |

---

## 4. Event Types

| Event ID | Name | Precondition | Postcondition | Energy flow |
|----------|------|-------------|---------------|-------------|
| `CAPTURE` | Source reaction in pocket | `conformation == unloaded` AND `capture_site == substrate_bound` | `conformation = loaded`; `strain_energy = η_couple × ΔG_source`; `capture_site = product_formed` | ΔG_source released; fraction η_couple stored; remainder → ThermalBath |
| `PRODUCT_EXIT` | Source product leaves pocket | `capture_site == product_formed` | `capture_site = empty` | None (mechanical release) |
| `TARGET_BIND` | Target substrate binds discharge site | `discharge_site == empty` AND `target available` | `discharge_site = target_bound` | None (binding may be favorable or neutral) |
| `DISCHARGE` | Backbone relaxation drives target reaction | `conformation == loaded` AND `discharge_site == target_bound` | `conformation = unloaded`; `strain_energy = 0`; `discharge_site = product_released`; target reaction driven | strain_energy transferred to target process; ΔG_target offset |
| `PRODUCT_RELEASE` | Target product leaves discharge site | `discharge_site == product_released` | `discharge_site = empty` | None |
| `LEAK` | Spontaneous thermal relaxation | `conformation == loaded` AND `discharge_site == empty` | `conformation = unloaded`; `strain_energy = 0` | strain_energy → ThermalBath (wasted) |
| `RESET` | Full cycle completion check | `conformation == unloaded` AND `capture_site == empty` AND `discharge_site == empty` | `cycle_count += 1` | Ready for next capture |

---

## 5. Transition Rules

### 5.1 The Coupling Cycle (successful)

```
HIC_unloaded
  → [CAPTURE] → HIC_loaded (strain_energy > 0)
  → [PRODUCT_EXIT] → HIC_loaded (capture site free)
  → [TARGET_BIND] → HIC_loaded (discharge site occupied)
  → [DISCHARGE] → HIC_unloaded (target driven; strain released)
  → [PRODUCT_RELEASE] → HIC_unloaded (discharge site free)
  → [RESET] → cycle_count += 1
```

### 5.2 The Leak Path (failure)

```
HIC_loaded (no target substrate available)
  → [LEAK] → HIC_unloaded (strain energy wasted to bath)
  → [RESET] → cycle_count not incremented (failed cycle)
```

### 5.3 Transition Conditions

| Transition | Rate / probability | Depends on |
|-----------|-------------------|-----------|
| CAPTURE | k_source × [SourceSubstrate] | Source reaction kinetics; substrate availability |
| DISCHARGE | k_discharge × [TargetSubstrate] | Target binding kinetics; discharge geometry |
| LEAK | k_leak = ν_0 × exp(−ΔG_barrier / kT) | Barrier height; temperature |
| Useful fraction | η_useful = k_discharge / (k_discharge + k_leak) | Relative rates of useful discharge vs leak |

---

## 6. Uncertainty Fields

| Field | Type | Description | Current status |
|-------|------|-------------|---------------|
| `η_couple_value` | Unknown float | Actual coupling efficiency for specific S_HIC + R_source | **NOT DETERMINED** — requires specific sequence + reaction pair |
| `ΔG_barrier_value` | Unknown float | Actual strain relaxation barrier for specific S_HIC | **NOT DETERMINED** — requires conformational analysis |
| `S_HIC_exists` | Boolean | Whether a sequence satisfying HIC.1 exists in the 4-class alphabet | **POSTULATED** — not demonstrated; bridge-level |
| `η_couple_threshold` | Float | Minimum η_couple for useful coupling (~0.1) | **ESTIMATED** — order-of-magnitude |
| `source_reaction_compatibility` | Boolean | Whether the specific source reaction's product geometry deforms the capture pocket | **NOT TESTED** for specific reaction |
| `target_reaction_compatibility` | Boolean | Whether backbone relaxation at DS can drive the specific target reaction | **NOT TESTED** for specific reaction |

---

## 7. Failure Classes

| Failure ID | Name | Condition | Consequence |
|-----------|------|-----------|------------|
| `F1` | **No HIC sequence exists** | S_HIC not found in 4-class alphabet | Bridge postulate unfulfillable; energy gap permanent |
| `F2` | **η_couple too low** | η_couple < 0.1 for all accessible sequences | Stored energy below noise floor; coupling non-functional |
| `F3` | **ΔG_barrier too low** | ΔG_barrier < 3 kT | Leak dominates; loaded state too short-lived for useful transfer |
| `F4` | **No compatible source reaction** | No favorable reaction fits in capture pocket with deforming product | Capture mechanism non-functional |
| `F5` | **No compatible target reaction** | No unfavorable reaction drivable by backbone relaxation at DS | Discharge mechanism non-functional |
| `F6` | **Leak dominates useful transfer** | k_leak ≫ k_transfer for all target processes | Energy wasted; coupling efficiency ~0 |
| `F7` | **Incompatible with existing scaffold** | HIC structure conflicts with existing bonding/compartment grammar | Integration failure |

---

## 8. Cost/Debt Fields

| Field | Value | Classification |
|-------|-------|---------------|
| `new_postulates` | 1 (HIC functional class) | Bridge-level MIP |
| `new_parameters` | 1 (η_couple) | Phenomenological |
| `new_fields` | 0 | — |
| `new_dof` | 0 | — |
| `total_postulates` | 14 (13 prior + 1) | Updated from Book IV Omega |
| `total_parameters` | 7 (6 prior + 1) | Updated |
| `total_fields` | 1 (unchanged) | — |
| `total_dof` | 6 (unchanged) | — |
| `bridge_authority` | `bridge_level_mip` | Not native; not derived from τ-substrate |
| `zero_cost_streak_status` | `ENDED` | First upper-stack postulate cost |
| `streak_length_at_end` | 17 targets (Epsilon–Gamma) | Longest zero-cost run in program |

---

## 9. Example Minimal Serialized Representation

```json
{
  "stage": "BOOK_V_TARGET_DELTA",
  "bridge_type": "energy_coupling",
  "candidate": "HIC",
  "status": "minimum_bridge_found",
  "global_verdict": "B",

  "postulate": {
    "id": "HIC.1",
    "statement": "There exists at least one sequence S_HIC in {D1,D2,A1,A2}^N whose scaffold has capture-discharge coupling through backbone strain",
    "authority": "bridge_level_mip",
    "native": false
  },

  "parameter": {
    "id": "eta_couple",
    "type": "float",
    "domain": [0.0, 1.0],
    "threshold": 0.1,
    "value": null,
    "status": "undetermined"
  },

  "cycle": {
    "source_event": "favorable_reaction_in_capture_pocket",
    "capture": "product_geometry_deforms_pocket_to_strain_backbone",
    "loaded_state": "backbone_conformational_strain",
    "storage_energy_kT": {"estimate": "6-10", "conditional_on": "eta_couple >= 0.1"},
    "storage_barrier_kT": {"requirement": ">= 5", "status": "postulated"},
    "discharge": "backbone_relaxation_drives_target_at_discharge_site",
    "target_event": "unfavorable_reaction_driven_by_strain_release",
    "reset": "scaffold_returns_to_unloaded_conformation",
    "leak": "spontaneous_thermal_relaxation_without_target"
  },

  "hard_criteria": {
    "capture_before_thermalization": true,
    "storage_above_noise": "conditional",
    "selective_transfer": true,
    "source_target_distinct": true,
    "recurrent": true,
    "compatible_with_scaffold": true,
    "non_false_positive": true,
    "cost_minimal": true,
    "pass_count": "8-9/9"
  },

  "cost": {
    "new_postulates": 1,
    "new_parameters": 1,
    "new_fields": 0,
    "new_dof": 0,
    "total_postulates": 14,
    "total_parameters": 7,
    "total_fields": 1,
    "total_dof": 6
  },

  "failures_not_triggered": ["F1","F2","F3","F4","F5","F6","F7"],
  "failures_conditional": ["F2_conditional_on_eta", "F3_conditional_on_barrier"],

  "eliminated_families": {
    "A": "subsumed_into_D",
    "B": "overbuilt_3plus_postulates",
    "C": "fails_interception_and_transfer"
  },

  "program_consequence": {
    "beta_threshold_reopenable": true,
    "metabolism_stage_justified": true,
    "active_transport_status": "open",
    "first_upper_stack_bridge_debt": true,
    "zero_cost_streak_ended": true
  }
}
```

---

## 10. Integration Notes for GRUT-RAI

### 10.1 Where This Fits

The energy-coupling grammar extends the existing catalysis grammar (from Target Pi) with a new entity type (HIC), a new state variable (conformation: loaded/unloaded), and a new event pair (CAPTURE/DISCHARGE). The existing scaffold-catalysis grammar (proximity + orientation effects) remains valid for all non-coupling catalytic processes. The HIC is a *specialization* of the scaffold catalyst, not a replacement.

### 10.2 Machine-Reasoning Requirements

To reason over energy-coupling questions, GRUT-RAI must be able to:

1. Represent the HIC as an entity with two conformational states.
2. Track strain_energy as a state variable across events.
3. Evaluate whether a specific source reaction's product geometry is compatible with the capture pocket.
4. Evaluate whether a specific target reaction is drivable by backbone relaxation.
5. Compute the useful fraction η_useful = k_discharge / (k_discharge + k_leak).
6. Detect failure conditions F1–F7 and classify the result appropriately.
7. Update the cost/debt ledger when the HIC postulate is accepted.

### 10.3 Promotion Rules

| Condition | Current status | Promotion to | Requires |
|-----------|---------------|-------------|---------|
| HIC postulate accepted | bridge_level_mip | (remains bridge unless demonstrated native) | Native derivation from τ-substrate |
| η_couple measured/bounded | undetermined | constrained or phenomenological | Specific sequence + reaction analysis |
| S_HIC demonstrated | postulated | established | Explicit sequence identification |
| HIC coupled to specific source/target pair | postulated | demonstrated | Specific reaction-pair compatibility |

---

*GRUT-RAI Energy Bridge Grammar complete. Entity types, state variables, event types, transition rules, uncertainty fields, failure classes, cost/debt fields, and example JSON serialization provided. Minimum machine-readable specification for energy-coupling reasoning.*
