# Book V — Target Epsilon: GRUT-RAI Energy-Flow State Model

## Minimum Machine-Usable State Model for Post-Delta Energy Reasoning

---

## 1. Purpose

This document defines the minimum state model GRUT-RAI needs to reason over energy-flow questions in the HIC-equipped scaffold. It extends the Delta grammar with flux-tracking, threshold-verdict fields, and the concerted-operation revision from the Epsilon stress test.

---

## 2. Entity Types

| Entity ID | Name | Description | Parent |
|-----------|------|-------------|--------|
| `HIC` | Hybrid Intercepting Catalyst | Scaffold with capture-discharge coupling; operates as direct transducer | `CatalyticScaffold` |
| `HIC_unloaded` | HIC relaxed state | Backbone unstrained; CS available; DS available | `HIC` state |
| `HIC_loaded` | HIC strained state | Backbone strained; transient (~fs in concerted mode) | `HIC` state |
| `HIC_primed` | HIC with both substrates pre-bound | CS has source substrate; DS has target substrate; ready for concerted capture-discharge | `HIC` state |
| `SourceSubstrate` | Source reaction substrate | Consumed by favorable reaction at CS | `Soliton` / `Monomer` |
| `SourceProduct` | Source reaction product | Produced in CS; geometry triggers loading | `Composite` |
| `TargetSubstrate` | Target reaction substrate | Bound at DS; driven by strain release | `Duplex` / `Mismatch` |
| `TargetProduct` | Target reaction product | Produced at DS by driven process | `SeparatedStrands` / `CorrectedChain` |
| `ThermalBath` | Environment | Sink for leaked/dissipated energy | Environment |
| `ProtoCell` | Compartmentalized system | Contains HIC(s) + templates + catalysts + monomers | System |

---

## 3. State Variables

| Variable | Type | Domain | Description |
|----------|------|--------|-------------|
| `hic_conformation` | Enum | {`unloaded`, `primed`, `loaded`, `discharging`} | HIC conformational state (extended from Delta's binary) |
| `cs_occupancy` | Enum | {`empty`, `source_bound`, `product_formed`, `product_exiting`} | Capture site state |
| `ds_occupancy` | Enum | {`empty`, `target_bound`, `product_releasing`} | Discharge site state |
| `strain_energy_kT` | Float ≥ 0 | [0, η_couple × ΔG_source] | Current stored strain (kT units) |
| `η_couple` | Float ∈ (0,1) | Parameter | Coupling efficiency |
| `ΔG_barrier_kT` | Float > 0 | Parameter | Strain relaxation barrier |
| `operation_mode` | Enum | {`concerted`, `store_and_wait`} | Whether HIC operates with pre-bound target |
| `cycle_count` | Integer ≥ 0 | Counter | Completed successful cycles |
| `leak_count` | Integer ≥ 0 | Counter | Spontaneous relaxation events (energy wasted) |
| `useful_fraction` | Float ∈ [0,1] | Derived | cycle_count / (cycle_count + leak_count) |

### System-Level Variables

| Variable | Type | Domain | Description |
|----------|------|--------|-------------|
| `n_hic_instances` | Integer ≥ 0 | Count of HIC scaffolds in proto-cell | Determines system-level coupling density |
| `hic_flux_rate` | Float ≥ 0 | Successful discharge events per unit time across all HICs | System-level directed energy flux |
| `ambient_flux_rate` | Float ≥ 0 | Thermally-driven process events per unit time | Background ambient flux |
| `directed_fraction` | Float ∈ [0,1] | hic_flux_rate / (hic_flux_rate + ambient_flux_rate) | Fraction of useful processes that are HIC-driven vs ambient |
| `energy_level` | Enum | {`L4_asymmetry`, `L5_local`, `L5_plus_dominant`, `L6_proto_metabolic`} | Current energetic classification |
| `beta_threshold_status` | Enum | {`not_crossed`, `conditional_local`, `conditional_system`, `crossed`} | Book V Beta threshold state |

---

## 4. Event Types

| Event ID | Name | Precondition | Postcondition | Energy flow |
|----------|------|-------------|---------------|-------------|
| `SOURCE_BIND` | Source substrate binds CS | `cs_occupancy == empty` | `cs_occupancy = source_bound` | Binding energy (small) |
| `TARGET_BIND` | Target substrate binds DS | `ds_occupancy == empty` | `ds_occupancy = target_bound` | Binding energy (small) |
| `PRIME` | Both substrates in place | `cs_occupancy == source_bound` AND `ds_occupancy == target_bound` | `hic_conformation = primed` | None |
| `CAPTURE_DISCHARGE` | Concerted: source reaction + strain + discharge | `hic_conformation == primed` | `hic_conformation = unloaded`; `cs_occupancy = product_formed`; `ds_occupancy = product_releasing`; target driven | η_couple × ΔG_source transferred to target; remainder → bath |
| `SOURCE_EXIT` | Source product leaves CS | `cs_occupancy == product_formed` | `cs_occupancy = empty` | None |
| `TARGET_EXIT` | Target product leaves DS | `ds_occupancy == product_releasing` | `ds_occupancy = empty` | None |
| `RESET` | Full cycle complete | `hic_conformation == unloaded` AND `cs_occupancy == empty` AND `ds_occupancy == empty` | `cycle_count += 1` | Ready |
| `LEAK` | Spontaneous relaxation (no target) | `hic_conformation == loaded` AND `ds_occupancy == empty` | `hic_conformation = unloaded`; `strain_energy = 0`; `leak_count += 1` | strain → bath |
| `CAPTURE_ONLY` | Source reaction without target (store-and-wait) | `cs_occupancy == source_bound` AND `ds_occupancy == empty` | `hic_conformation = loaded`; `strain_energy = η_couple × ΔG_source` | Partial capture; rest → bath |

---

## 5. Transition Rules

### 5.1 Concerted Mode (Primary — Recommended)

```
HIC_unloaded
  → [SOURCE_BIND] → cs: source_bound
  → [TARGET_BIND] → ds: target_bound
  → [PRIME] → HIC_primed (both substrates in place)
  → [CAPTURE_DISCHARGE] → HIC_unloaded
      cs: product_formed; ds: product_releasing
      target process driven by transduced energy
  → [SOURCE_EXIT] → cs: empty
  → [TARGET_EXIT] → ds: empty
  → [RESET] → cycle_count += 1
```

### 5.2 Store-and-Wait Mode (Secondary — Leak-Vulnerable)

```
HIC_unloaded
  → [SOURCE_BIND] → cs: source_bound
  → [CAPTURE_ONLY] → HIC_loaded (strain stored; no target yet)
  → [SOURCE_EXIT] → cs: empty
  → if target arrives: [TARGET_BIND] → [DISCHARGE] → HIC_unloaded + driven outcome
  → if no target: [LEAK] → HIC_unloaded + heat (wasted)
```

### 5.3 Rate Equations (Concerted Mode)

```
k_prime = k_source_bind × [SourceSubstrate] × k_target_bind × [TargetSubstrate]
    (both must bind; product of binding rates)

k_capture_discharge = k_reaction × P(both bound)
    (reaction rate given primed state)

η_useful (concerted) = P(DS occupied when CS fires)
    ≈ [TargetSubstrate] × K_on(DS) / (K_off(DS) + [TargetSubstrate] × K_on(DS))

directed_fraction = n_hic × k_capture_discharge / (n_hic × k_capture_discharge + k_ambient)
```

---

## 6. Flux-Tracking Fields

| Field | Type | Computation | Meaning |
|-------|------|------------|---------|
| `total_hic_events` | Integer | cycle_count + leak_count | All capture events (successful + leaked) |
| `useful_fraction` | Float | cycle_count / total_hic_events | Per-HIC efficiency |
| `system_useful_flux` | Float | n_hic × useful_fraction × k_capture | Total driven events per unit time |
| `system_ambient_flux` | Float | k_ambient × [relevant substrates] | Total ambient-driven events per unit time |
| `directed_fraction` | Float | system_useful_flux / (system_useful_flux + system_ambient_flux) | How much of useful work is HIC-driven |
| `energy_level_auto` | Derived | if directed_fraction < 0.01: L4; elif < 0.5: L5_local; elif < 0.9: L5_plus; else: L6 | Automatic classification |

---

## 7. Uncertainty Fields

| Field | Type | Description | Status |
|-------|------|-------------|--------|
| `η_couple_value` | Unknown float | Actual coupling efficiency | **UNDETERMINED** |
| `ΔG_barrier_value` | Unknown float | Actual strain relaxation barrier | **UNDETERMINED** |
| `S_HIC_exists` | Boolean | Whether an HIC sequence exists in {D1,D2,A1,A2}^N | **POSTULATED** |
| `concerted_mode_feasible` | Boolean | Whether both substrates can be pre-positioned simultaneously | **PLAUSIBLE but unverified** |
| `n_hic_per_protocell` | Unknown integer | How many HIC instances a proto-cell contains | **UNDETERMINED** |
| `directed_fraction_estimate` | Unknown float | System-level coupling significance | **UNDETERMINED** — depends on n_hic and rates |

---

## 8. Failure Classes

| Failure ID | Condition | Consequence |
|-----------|-----------|------------|
| `F1` | S_HIC not found | Bridge postulate unfulfillable |
| `F2` | η_couple < 0.05 | Captured energy below noise floor |
| `F3` | ΔG_barrier < 3 kT AND concerted mode infeasible | Both modes fail: store-and-wait leaks, concerted can't prime |
| `F4` | No compatible source reaction fits in CS | Capture mechanism non-functional |
| `F5` | No compatible target reaction drivable at DS | Discharge mechanism non-functional |
| `F6` | Concerted mode geometrically impossible | CS and DS cannot both accommodate substrates simultaneously on one scaffold |
| `F7` | n_hic = 0 in practical proto-cells | No HIC produced by the replication/selection system |
| `F8` | directed_fraction ≈ 0 at system level | HIC has no practical effect on proto-cell operation |

---

## 9. Verdict Fields

| Field | Type | Domain | Meaning |
|-------|------|--------|---------|
| `beta_condition_A` | Enum | {`no`, `yes_conditional`, `yes`} | Favorable drives unfavorable through coupling |
| `beta_condition_B` | Enum | {`no`, `partial`, `yes_conditional`, `yes`} | Useful flux persists across cycles |
| `beta_condition_C` | Enum | {`no`, `yes_local`, `yes_system`} | More than ambient thermal |
| `beta_threshold` | Enum | {`not_crossed`, `conditional_local`, `conditional_system`, `crossed`} | Overall Beta status |
| `energy_level` | Enum | {`L4`, `L5_local`, `L5_plus`, `L6`} | Energetic classification |
| `epsilon_global_verdict` | Enum | {`A_not_reopened`, `B_conditional_local`, `C_genuine_positive`} | Epsilon outcome |

---

## 10. Minimal Serialized Example

```json
{
  "stage": "BOOK_V_TARGET_EPSILON",
  "audit_type": "threshold_reassessment",

  "hic_state": {
    "conformation": "unloaded",
    "cs_occupancy": "empty",
    "ds_occupancy": "empty",
    "strain_energy_kT": 0,
    "operation_mode": "concerted",
    "cycle_count": 47,
    "leak_count": 3,
    "useful_fraction": 0.94
  },

  "system_state": {
    "n_hic_instances": 4,
    "hic_flux_rate": 12.5,
    "ambient_flux_rate": 850.0,
    "directed_fraction": 0.014,
    "energy_level": "L5_local"
  },

  "parameters": {
    "η_couple": {"value": null, "threshold": 0.1, "status": "undetermined"},
    "ΔG_barrier_kT": {"value": null, "requirement": ">= 5", "status": "undetermined"}
  },

  "threshold_verdict": {
    "beta_condition_A": "yes_conditional",
    "beta_condition_B": "partial",
    "beta_condition_C": "yes_local",
    "beta_threshold": "conditional_local",
    "energy_level": "L5_local",
    "epsilon_global_verdict": "B_conditional_local"
  },

  "stress_test": {
    "primary_pairing": "P1_assembly_to_separation",
    "p1_score": "9/9",
    "concerted_operation_required": true,
    "hic_is_transducer_not_battery": true,
    "eta_functional_window": [0.10, 0.50]
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
    "note": "Epsilon adds no cost; reassesses Delta bridge"
  },

  "program_consequence": {
    "beta_threshold_reopened": "conditional_local",
    "proto_metabolism_justified": "conditional",
    "active_transport_justified": false,
    "atp_language_justified": false,
    "level_upgrade": "L4 -> L5_local",
    "next_audit": "proto_metabolism_re_evaluation_under_HIC"
  },

  "critical_revision": {
    "delta_claimed": "HIC is energy-storage device with loaded state",
    "epsilon_revised_to": "HIC is direct transducer in concerted mode; no significant storage phase",
    "implication": "narrower capability than Delta suggested; but genuine Level 5 coupling"
  }
}
```

---

## 11. Integration Notes

### 11.1 Relation to Delta Grammar

The Epsilon state model extends the Delta grammar (from `BOOK_V_TARGET_DELTA_GRUT_RAI_ENERGY_BRIDGE_GRAMMAR.md`) with:

- **New state:** `HIC_primed` (both substrates pre-bound; concerted mode).
- **New event:** `CAPTURE_DISCHARGE` (concerted capture + discharge in one event).
- **New event:** `PRIME` (both substrates in place; triggers concerted mode).
- **System-level variables:** `n_hic_instances`, `directed_fraction`, `energy_level`.
- **Flux-tracking fields:** `system_useful_flux`, `system_ambient_flux`, `directed_fraction`.
- **Verdict fields:** `beta_condition_A/B/C`, `beta_threshold`, `epsilon_global_verdict`.
- **Critical revision:** HIC reclassified from energy-storage device to direct transducer.

### 11.2 Breaking Change from Delta

Delta described the HIC as having a meaningful storage phase (loaded state persisting until target arrives). Epsilon's stress test revealed that store-and-wait mode is dominated by thermal leak (k_leak ≫ k_encounter). The concerted-operation revision means:

- The `HIC_loaded` state is transient (~femtoseconds), not persistent.
- The `LEAK` event is relevant only in store-and-wait mode (secondary).
- The primary operational pathway is `PRIME → CAPTURE_DISCHARGE` (concerted).
- The HIC is a **transducer**, not a **battery**.

This does not invalidate Delta's bridge postulate. It narrows the HIC's capability: it can couple processes that occur simultaneously at the same scaffold, but it cannot store energy for later asynchronous use.

### 11.3 What GRUT-RAI Must Track

Post-Epsilon, GRUT-RAI must be able to:

1. Represent HIC in concerted mode (primed → capture_discharge as one transition).
2. Track system-level directed_fraction (how much of useful flux is HIC-driven).
3. Classify the scaffold's energy level (L4 / L5_local / L5+ / L6).
4. Evaluate the Beta threshold under HIC (conditional_local / conditional_system / crossed).
5. Detect failure conditions F1–F8.
6. Report the critical revision (transducer, not battery) in any downstream reasoning.

---

*GRUT-RAI Energy-Flow State Model complete. Entity types, state variables (including system-level), event types (including concerted CAPTURE_DISCHARGE), transition rules, flux-tracking, uncertainty fields, failure classes, verdict fields, and example JSON. Critical revision documented: HIC is a direct transducer in concerted mode, not an energy-storage device.*
