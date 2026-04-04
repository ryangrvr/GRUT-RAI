# Book X — Target Gamma: GRUT-RAI Transport-Threshold State Model

## Machine-Readable State Model for T2/T3 Transport Reasoning

---

## 1. Entity Types

| Entity | Description | Source |
|--------|-------------|--------|
| `ccbg_gate` | Carrier-Coupled Boundary Gate; committed fifth bridge | Book X Beta/Gamma |
| `passive_pore` | Ungated structural pore in K=6/K=7 mesh | Book IV Tau |
| `gated_pore` | Pore with installed CCBG; carrier-actuated | Book X Gamma |
| `large_waste` | Degradation products too big for passive pores | Book X Alpha §4.4 |
| `large_precursor` | Large feedstock species near pore-size threshold | Book X Gamma §7 |
| `carrier_loaded` | K=2 (N=2, ℓ=0) energy carrier | W0 + Book IX |

---

## 2. Gate State Variables

| Variable | Type | Domain | Description |
|----------|------|--------|-------------|
| `transport_level` | enum | {T1, T2, T3_CONDITIONAL, T3_STABILIZED, T4} | Current transport |
| `ccbg_committed` | bool | true | Fifth bridge committed |
| `n_gated_pores` | int | [10, 30] | Gated pores (estimated) |
| `n_passive_pores` | int | [70, 270] | Ungated pores |
| `gate_fraction` | float | [0.05, 0.15] | Gated / total pores |
| `gate_state` | enum per gate | {CLOSED, OPEN} | Current conformation |
| `dg_gate` | float | ≤ E_carrier | Gate switching energy |
| `tau_reset` | float | 1–10 ms | Spontaneous reset timescale |
| `directional_extension` | bool | true | Binding-pocket extension adopted |
| `k_bind` | float | ~10³ M⁻¹ | Binding affinity for target species |
| `eta_displace` | float | 0.3–0.7 | Displacement efficiency |

---

## 3. Carrier-Coupling Fields

| Variable | Type | Domain | Description |
|----------|------|--------|-------------|
| `carrier_budget_for_gates` | float | 0.05–0.10 | Fraction of M4 carrier events for gates |
| `gate_events_per_cycle` | int | 15–55 | Total gate actuations per reproductive cycle |
| `per_gate_actuations` | float | 0.5–5.5 | Actuations per gate per cycle |

---

## 4. Transport / Accounting Fields

| Variable | Type | Domain | Description |
|----------|------|--------|-------------|
| `waste_export_rate` | float | [0, ∞) | Large-waste molecules exported per cycle |
| `large_precursor_import_rate` | float | [0, ∞) | Large precursors imported per cycle (T3) |
| `small_species_benefit` | enum | NEGLIGIBLE | Gate adds nothing for species ≪ pore size |
| `net_transport_vs_passive` | float | — | Ratio of gate-mediated to passive flux (species-dependent) |

---

## 5. Directionality Fields

| Variable | Type | Domain | Description |
|----------|------|--------|-------------|
| `import_mechanism` | enum | {PASSIVE, GATED_TIMING, BIASED_LARGE_SPECIES} | Import capability |
| `export_mechanism` | enum | {PASSIVE, GATED_PULSE, BIASED_WASTE} | Export capability |
| `directional_for_large` | bool | true | T3 works for large species |
| `directional_for_small` | bool | false | T3 fails for small species |
| `species_selectivity` | enum | {SIZE_PLUS_GATE, BINDING_SPECIFIC} | Selectivity level |

---

## 6. Downstream-Impact Fields

| Variable | Type | Domain | Description |
|----------|------|--------|-------------|
| `waste_management_enabled` | bool | true | Large-waste export now possible |
| `environmental_responsiveness` | enum | {ABSENT, PARTIAL} | Gate reflects internal state |
| `division_integrity_improved` | bool | true | Gates closed pre-fission |
| `lineage_improvement` | enum | MODEST | Waste reduction helps persistence |
| `adaptive_expansion` | enum | MODEST | Gate-quality traits selectable |

---

## 7. Transition Rules

### 7.1 Transport-Level Determination

```
IF ccbg_committed == true:
   transport_level = T2  // minimum: gated permeability

   IF directional_extension == true
      AND species is LARGE (near pore-size threshold)
      AND k_bind >= 1000
      AND eta_displace >= 0.3:
      transport_level = T3_CONDITIONAL  // for that species class

   // T3 does NOT apply for small species
   IF species is SMALL:
      transport_level = T2  // gate helps with timing only; no directionality
```

### 7.2 Waste-Export Logic

```
IF gate_state == OPEN:
   large_waste CAN transit through gated pore
   // This is IMPOSSIBLE at T1 (waste too big for passive pores)

IF gate_state == CLOSED:
   large_waste CANNOT transit (backbone blocks)
   // Proto-cell controls WHEN waste exits
```

### 7.3 Fallback

```
IF ccbg fails (all gates stuck):
   transport_level = T1  // revert to passive only
   waste_management_enabled = false
   // Graceful degradation: stuck-open gates become slightly larger passive pores
```

---

## 8. Uncertainty / Fragility Fields

| Variable | Type | Value | Source |
|----------|------|-------|--------|
| `t2_fragility` | enum | LOW | T2 works across broad parameter range |
| `t3_fragility` | enum | MODERATE | K_bind and η_displace matter |
| `species_class_limitation` | str | "T3 limited to large species; T2 benefits all gated-pore-compatible species" | Gamma §6 |
| `gate_density_sufficient` | enum | PLAUSIBLE | ~10–30 gates estimated; system-level effect requires ≥ 10 |
| `passive_dilution` | enum | MODERATE | Ungated pores still dominate total exchange; gated pores add controlled component |
| `binding_pocket_verified` | bool | false | K_bind and η_displace not derived from first principles |

---

## 9. Verdict Fields

| Field | Value | Authority |
|-------|-------|----------|
| `t2_justified` | `ROBUST` | Book X Gamma |
| `t3_justified` | `CONDITIONAL_LARGE_SPECIES` | Book X Gamma |
| `t4_justified` | `NO` | Book X Gamma |
| `ccbg_committed` | `PROVISIONAL` | Book X Gamma |
| `family_g_required` | `NO` | Book X Gamma |
| `new_cost` | `1P + 2p` | 16/11/1/6 total |
| `waste_export_enabled` | `YES` | New capability |
| `book_x_gamma_changes_state` | `YES` | T1 → T2 + T3-conditional; CCBG committed |
| `global_verdict` | `B` | T2 robust + T3 conditional; CCBG provisionally commit-worthy |

---

## 10. Minimal Serialized Example

```json
{
  "program_phase": "BOOK_X_GAMMA",
  "stage": "boundary_gate_commitment_and_transport_verification",

  "transport": {
    "level": "T2_robust_plus_T3_conditional",
    "t2_status": "ROBUST",
    "t3_status": "CONDITIONAL_LARGE_SPECIES_ONLY",
    "t4_status": "NOT_PRESENT",
    "waste_export": true,
    "environmental_responsiveness": "PARTIAL"
  },

  "ccbg": {
    "committed": true,
    "commitment_type": "PROVISIONAL",
    "postulate": "boundary_embedded_carrier_responsive_conformational_pore_switch",
    "parameters": ["dg_gate", "k_bind"],
    "n_gates_estimated": "10-30",
    "gate_events_per_cycle": "15-55",
    "carrier_budget_fraction": "0.05-0.10",
    "directional_extension": true,
    "t3_species_class": "large_near_pore_threshold"
  },

  "species_benefit": {
    "large_waste": {"t2": "SIGNIFICANT_new_exit", "t3": "export_bias_possible"},
    "large_precursors": {"t2": "timed_entry", "t3": "SIGNIFICANT_directed_import"},
    "small_species": {"t2": "NEGLIGIBLE", "t3": "NEGLIGIBLE"}
  },

  "downstream": {
    "waste_management": "ENABLED",
    "pre_division_integrity": "IMPROVED",
    "environmental_responsiveness": "PARTIAL",
    "lineage_improvement": "MODEST",
    "adaptive_expansion": "MODEST"
  },

  "cost": {
    "total_postulates": 16,
    "total_parameters": 11,
    "total_fields": 1,
    "total_dof": 6,
    "bridges": 5,
    "zero_cost_targets": 26,
    "book_x_gamma_added": {"postulates": 1, "parameters": 2}
  },

  "verdict": {
    "global": "B",
    "t2": "ROBUST",
    "t3": "CONDITIONAL",
    "ccbg_committed": "PROVISIONAL",
    "family_g_needed": false,
    "state_change": true,
    "next_stage": "book_x_terminal_capstone"
  }
}
```

---

## 11. Integration Notes

### 11.1 What GRUT-RAI Must Update from Book X Gamma

1. **Transport level: T2 (robust) + T3-conditional (large species).** The scaffold can now control boundary exchange timing and export large waste.
2. **Fifth bridge committed (provisional).** CCBG: 1P + 2p. Total cost: 16/11/1/6.
3. **Waste management enabled.** Large degradation products can exit through open gated pores — impossible at T1.
4. **Environmental responsiveness initiated.** Gate state reflects carrier budget → internal energetic state. First directional interaction with environment.
5. **T3 limited to large species.** Small-species directional transport fails (passive flux overwhelms). Honest limitation.
6. **Family G reserved.** Not needed for T2–T3; available for future T4.

### 11.2 What GRUT-RAI Must NOT Update

- No claim of T4 active transport (requires Family G shuttle)
- No claim of ATP equivalence (proto-currency + gate; not ATP)
- No claim of broad-species T3 (limited to large species)
- No claim of life

---

*GRUT-RAI Transport-Threshold State Model complete. T2 robust; T3 conditional for large species. CCBG provisionally committed. Waste export enabled. Cost: 16/11/1/6. Five bridges.*
