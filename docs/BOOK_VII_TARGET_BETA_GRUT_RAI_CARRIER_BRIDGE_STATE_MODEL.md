# Book VII — Target Beta: GRUT-RAI Carrier-Bridge State Model

## Minimum Machine-Usable State Model for Carrier-Bridge Reasoning

---

## 1. Entity Types

| Entity ID | Name | Description | Parent |
|-----------|------|-------------|--------|
| `Carrier` | Energy carrier molecule | Small composite (K=2 scale) with loaded/unloaded conformational switch | Bridge object |
| `Carrier_unloaded` | Relaxed carrier | Low-energy conformation; ready for loading at HIC site | Carrier state |
| `Carrier_loaded` | Activated carrier | High-energy conformation; carries transferable energy; diffuses to targets | Carrier state |
| `CarrierPool` | Internal carrier population | Collection of all carriers (loaded + unloaded) inside proto-cell | System |
| `TargetDischargeSite` | Remote carrier-discharge pocket | A scaffold geometry that accepts and discharges a loaded carrier | Catalyst extension |
| `ProtoCell_M4` | M4-level proto-cell | Proto-cell with HIC network + carrier bridge; dominant metabolism | System (conditional) |

---

## 2. Carrier State Variables

### 2.1 Per-Carrier Variables

| Variable | Type | Domain | Description |
|----------|------|--------|-------------|
| `carrier_state` | Enum | {`unloaded`, `loaded`, `docked_at_hic`, `in_transit`, `docked_at_target`, `degraded`} | Current carrier status |
| `energy_content` | Float ≥ 0 | [0, E_carrier_max] | Energy stored in loaded state (kT) |
| `time_since_loading` | Float ≥ 0 | | Time elapsed since carrier was loaded |
| `position` | Vector | Interior of proto-cell | Spatial location (for diffusion tracking) |

### 2.2 Per-Proto-Cell Carrier-Pool Variables

| Variable | Type | Domain | Description |
|----------|------|--------|-------------|
| `n_carriers_total` | Integer ≥ 0 | | Total carriers (all states) |
| `n_carriers_loaded` | Integer ≥ 0 | | Currently loaded carriers in transit |
| `n_carriers_unloaded` | Integer ≥ 0 | | Currently unloaded carriers available for reloading |
| `carrier_production_rate` | Float ≥ 0 | | Carriers loaded per unit time (= HIC discharge rate × loading efficiency) |
| `carrier_utilization_rate` | Float ≥ 0 | | Carriers discharged at targets per unit time |
| `carrier_leak_rate` | Float ≥ 0 | | Carriers that discharge without target (wasted) per unit time |
| `carrier_utilization_efficiency` | Float ∈ [0,1] | utilization / (utilization + leak) | Fraction of carriers that do useful work |
| `carrier_driven_events_per_cycle` | Float ≥ 0 | | Total carrier-mediated target events per reproductive cycle |

### 2.3 Combined Energetic Variables

| Variable | Type | Domain | Description |
|----------|------|--------|-------------|
| `hic_direct_events` | Float | | HIC concerted-mode events per cycle (from Alpha model) |
| `carrier_mediated_events` | Float | | Carrier-driven remote events per cycle |
| `total_directed_events` | Float | | hic_direct + carrier_mediated |
| `total_ambient_events` | Float | | Thermally-driven events per cycle |
| `directed_fraction_combined` | Float ∈ [0,1] | | total_directed / (total_directed + ambient) |
| `metabolic_level` | Enum | {`M0`–`M5`} | Current energetic classification |

---

## 3. Carrier Parameters (Bridge Postulate)

| Parameter | Type | Domain | Description | Status |
|-----------|------|--------|-------------|--------|
| `E_carrier` | Float > 0 | kT units | Energy content of loaded carrier | **POSTULATED** — may be derivable from HIC discharge energy |
| `τ_carrier` | Float > 0 | seconds | Loaded-state lifetime (= 1/k_leak) | **POSTULATED** — critical parameter; must exceed τ_diffusion |
| `ΔG_carrier_barrier` | Float > 0 | kT units | Conformational barrier protecting loaded state | **DERIVED** from τ_carrier: ΔG = kT × ln(ν₀ × τ_carrier) |

---

## 4. Transport / Relay Fields

| Variable | Type | Description |
|----------|------|-------------|
| `τ_diffusion` | Float > 0 | Mean time for carrier to traverse proto-cell by diffusion |
| `diffusion_coefficient` | Float > 0 | Carrier diffusion coefficient in proto-cell interior |
| `proto_cell_diameter` | Float > 0 | Characteristic internal distance to traverse |
| `carrier_reachable_fraction` | Float ∈ [0,1] | Fraction of proto-cell interior reachable before carrier leaks |
| `n_target_sites` | Integer ≥ 0 | Number of compatible carrier-discharge sites in proto-cell |
| `target_encounter_rate` | Float ≥ 0 | Rate at which a loaded carrier finds a target |

### Critical Condition

```
τ_carrier > τ_diffusion
⟺ ΔG_carrier_barrier > kT × ln(ν₀ × L² / D)

where:
  L = proto-cell diameter
  D = carrier diffusion coefficient
  ν₀ = molecular vibration frequency (~10¹³ Hz)
```

If this condition is met: carrier reaches targets before leaking → M4 plausible.
If not met: carrier leaks before reaching targets → M3 ceiling persists.

---

## 5. Event Types

| Event ID | Name | Precondition | Postcondition |
|----------|------|-------------|---------------|
| `CARRIER_LOAD` | HIC loads carrier | HIC discharged + C_unloaded at HIC pocket | C_loaded produced; detaches from HIC |
| `CARRIER_DIFFUSE` | Loaded carrier moves through interior | C_loaded in transit | Position updates by diffusion |
| `CARRIER_DELIVER` | Carrier reaches and binds target site | C_loaded encounters compatible target | C_loaded docked at target |
| `CARRIER_DISCHARGE` | Carrier discharges at target; drives process | C_loaded at target site + target substrate | C_unloaded + driven outcome |
| `CARRIER_LEAK` | Carrier discharges without target (wasted) | time_since_loading > τ_carrier | C_unloaded + heat |
| `CARRIER_RECYCLE` | Unloaded carrier returns to HIC pool | C_unloaded in interior | Available for reloading |
| `CARRIER_DEGRADE` | Carrier molecule breaks down | Random damage or repeated cycling | Carrier lost; must be replaced by assembly |

---

## 6. Transition Rules

### 6.1 Carrier Production

```
for each HIC in proto_cell:
    if HIC completes capture-discharge cycle:
        if C_unloaded available at HIC secondary pocket:
            CARRIER_LOAD → C_loaded produced
            carrier_production_rate += 1
        else:
            HIC discharges directly at fixed DS (concerted mode fallback)
```

### 6.2 Carrier Diffusion and Delivery

```
for each C_loaded in transit:
    CARRIER_DIFFUSE: position += random_displacement(D, dt)

    if position near compatible target_site:
        CARRIER_DELIVER → C_loaded docked
        CARRIER_DISCHARGE → C_unloaded + driven_outcome
        carrier_utilization_rate += 1

    if time_since_loading > τ_carrier:
        CARRIER_LEAK → C_unloaded + heat
        carrier_leak_rate += 1
```

### 6.3 Directed-Fraction Computation

```
hic_direct_events = Σ(HIC concerted-mode events) × saturation_factor  # from Alpha model
carrier_mediated_events = carrier_production_rate × carrier_utilization_efficiency × events_per_carrier
total_directed = hic_direct_events + carrier_mediated_events
directed_fraction = total_directed / (total_directed + ambient_events)
```

### 6.4 Metabolic-Level Auto-Classification

```
if directed_fraction < 0.03:   metabolic_level = "M1"
elif directed_fraction < 0.10: metabolic_level = "M2"
elif directed_fraction < 0.30: metabolic_level = "M3"
elif directed_fraction < 0.50: metabolic_level = "M4"
else:                          metabolic_level = "M5"
```

---

## 7. Downstream-Impact Fields

| Variable | Type | Description |
|----------|------|-------------|
| `carrier_serves_replication` | Boolean | Carriers discharge at replication-support targets |
| `carrier_serves_fidelity` | Boolean | Carriers discharge at proofreading targets |
| `carrier_serves_boundary` | Boolean | Carriers discharge at boundary-growth targets |
| `carrier_serves_repair` | Boolean | Carriers discharge at catalyst-repair targets |
| `n_carrier_served_domains` | Integer | Count of domains with carrier-driven support |
| `organizational_inversion` | Boolean | True if directed_fraction > 0.5 for key processes |

---

## 8. Uncertainty / Fragility Fields

| Field | Type | Description | Status |
|-------|------|-------------|--------|
| `τ_carrier_value` | Unknown float | Actual carrier lifetime | **POSTULATED** — critical parameter |
| `ΔG_barrier_value` | Unknown float | Actual conformational barrier | **REQUIRES ≳ 25 kT** for sufficient lifetime |
| `E_carrier_value` | Unknown float | Actual energy per carrier | **~5–10 kT** estimated from HIC discharge |
| `carrier_exists` | Boolean | Whether a K=2-scale loaded-state composite can be produced | **POSTULATED** |
| `τ_carrier_sufficient` | Boolean | Whether τ_carrier > τ_diffusion | **CRITICAL CONDITION** |
| `utilization_efficiency_estimate` | Float | Expected η_carrier | **~0.3–0.7** estimated |
| `m4_reachable` | Boolean | Whether directed_fraction exceeds ~30% | **CONDITIONAL on τ_carrier** |

---

## 9. Verdict Fields

| Field | Type | Domain | Meaning |
|-------|------|--------|---------|
| `carrier_bridge_found` | Boolean | | Whether minimum viable carrier is identified |
| `carrier_family` | String | | "G/J_HIC_to_carrier_hybrid" |
| `carrier_breaks_ceiling` | Boolean | | Whether spatial decoupling eliminates concerted saturation |
| `m4_conditionally_reachable` | Boolean | | Whether M4 is achievable with carrier |
| `new_postulates` | Integer | | 1 |
| `new_parameters` | Integer | | 1–2 |
| `beta_changes_state` | Boolean | | YES (bridge identified; M4 conditional) |
| `beta_global_verdict` | Enum | {`A_no_bridge`, `B_conditional`, `C_bridge_found_m4_plausible`} | |

---

## 10. Minimal Serialized Example

```json
{
  "stage": "BOOK_VII_TARGET_BETA",
  "audit_type": "diffusible_energy_carrier_bridge",

  "carrier_bridge": {
    "family": "J_HIC_to_carrier_hybrid",
    "status": "minimum_bridge_found",
    "object": "K2_scale_composite_with_conformational_switch",
    "production": "loaded_by_HIC_discharge_at_secondary_pocket",
    "transport": "free_internal_diffusion",
    "delivery": "geometry_locked_discharge_at_compatible_remote_target",
    "postulate_cost": 1,
    "parameter_cost": "1-2",
    "fields_cost": 0,
    "dof_cost": 0
  },

  "carrier_state": {
    "n_carriers_total": 25,
    "n_carriers_loaded": 8,
    "n_carriers_unloaded": 15,
    "n_carriers_degraded": 2,
    "carrier_production_rate": 12.0,
    "carrier_utilization_rate": 7.5,
    "carrier_leak_rate": 2.5,
    "carrier_utilization_efficiency": 0.75
  },

  "energetic_state": {
    "hic_direct_events": 250,
    "carrier_mediated_events": 150,
    "total_directed": 400,
    "ambient_events": 800,
    "directed_fraction": 0.33,
    "metabolic_level": "M4_dominant"
  },

  "critical_parameters": {
    "E_carrier_kT": {"value": null, "estimate": "5-10", "status": "postulated"},
    "τ_carrier_s": {"value": null, "requirement": "> τ_diffusion", "status": "postulated"},
    "ΔG_barrier_kT": {"value": null, "requirement": ">= 25", "status": "derived_from_τ"},
    "τ_diffusion_s": {"estimate": "0.01", "derived_from": "L²/D"}
  },

  "downstream_impact": {
    "carrier_serves_replication": true,
    "carrier_serves_fidelity": true,
    "carrier_serves_boundary": true,
    "carrier_serves_repair": true,
    "n_domains": 4,
    "organizational_inversion": false
  },

  "cost": {
    "new_postulates": 1,
    "new_parameters": "1-2",
    "new_fields": 0,
    "new_dof": 0,
    "total_postulates": 15,
    "total_parameters": "8-9",
    "total_fields": 1,
    "total_dof": 6
  },

  "verdict": {
    "beta_global_verdict": "C_bridge_found_m4_plausible",
    "carrier_bridge_found": true,
    "carrier_breaks_ceiling": true,
    "m4_conditionally_reachable": true,
    "critical_condition": "τ_carrier > τ_diffusion",
    "next_audit": "m4_threshold_verification_or_book_vii_terminal"
  }
}
```

---

## 11. Integration Notes

### 11.1 What This Extends

Book VII Beta extends the Alpha metabolic-expansion model with:
- Carrier entity type and state variables
- Carrier production/diffusion/delivery/leak event types
- Combined directed-fraction computation (HIC-direct + carrier-mediated)
- Carrier-specific parameters (E_carrier, τ_carrier)
- Critical condition field (τ_carrier vs τ_diffusion)
- Downstream multi-domain impact fields for carrier-served processes

### 11.2 What GRUT-RAI Must Track Post-Beta

1. **Carrier bridge identified** — Family J (HIC-to-carrier hybrid); minimum viable.
2. **M4 conditionally reachable** — dependent on τ_carrier > τ_diffusion (ΔG_barrier ≳ 25 kT).
3. **Cost: 1 postulate + 1–2 parameters** — fourth upper-stack bridge; lightest possible.
4. **The carrier is a proto-currency, NOT ATP** — mobile energy distribution with limited specificity.
5. **Active transport NOT justified** — carrier is internal diffusion, not boundary transport.
6. **Program decision pending** — accept carrier bridge (invest 1+1–2; target M4) or remain at M3 (zero cost; supplementary ceiling).

### 11.3 What GRUT-RAI Must NOT Carry Forward

- Any claim of ATP equivalence (use "proto-currency" or "energy carrier")
- Any claim of active transport (internal diffusion ≠ boundary-crossing)
- Any claim that M4 is guaranteed (conditional on carrier lifetime parameter)
- Any claim that the carrier is native (bridge-level postulate)

---

*GRUT-RAI Carrier-Bridge State Model complete. Carrier entity types, state variables, transport/diffusion fields, combined flux computation, critical-condition modeling, downstream-impact fields, verdict fields, JSON serialization. Family J carrier: 1 postulate + 1–2 parameters. M4 conditional on τ_carrier > τ_diffusion. Proto-currency, not ATP.*
