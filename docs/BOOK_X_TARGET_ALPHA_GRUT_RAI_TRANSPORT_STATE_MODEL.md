# Book X — Target Alpha: GRUT-RAI Transport State Model

## Machine-Readable State Model for Active-Transport Reasoning

---

## 1. Entity Types

| Entity | Description | Source |
|--------|-------------|--------|
| `boundary_mesh` | K=6/K=7 cross-linked compartment shell | Book IV Tau |
| `passive_pore` | Structural gap in mesh; size-selective; uncontrolled | Book IV Tau |
| `gated_pore` | Pore with carrier-coupled gate scaffold (PROSPECTIVE — requires Family F bridge) | Book X Alpha |
| `shuttle_channel` | Boundary-spanning translocator (PROSPECTIVE — requires Family G bridge) | Book X Alpha |
| `transportable_species` | Molecule that can cross or be moved across the boundary | Book X Alpha §4.2 |
| `carrier_loaded` | K=2 (N=2, ℓ=0) excited state; energy source for transport work | W0 + Book IX Alpha |

---

## 2. Transport State Variables

| Variable | Type | Domain | Description |
|----------|------|--------|-------------|
| `transport_level` | enum | {T0, T1, T2, T3, T4, T5} | Current transport capability |
| `active_transport_present` | bool | — | Whether any energy-coupled boundary-crossing work exists |
| `zero_cost_transport_found` | bool | — | Whether any transport route survives from existing architecture |
| `fifth_bridge_required` | bool | — | Whether a new bridge postulate is needed for any transport |
| `fifth_bridge_installed` | bool | — | Whether the bridge has been committed |
| `fifth_bridge_type` | enum | {NONE, GATE, SHUTTLE, BOTH} | Type of bridge if installed |

---

## 3. Boundary / Gate Fields

| Variable | Type | Domain | Description |
|----------|------|--------|-------------|
| `boundary_type` | str | — | "K6_K7_crosslinked_mesh" |
| `pore_selectivity` | str | — | "Size-selective: admits K=1, blocks K=2+" |
| `passive_pore_count` | int | [1, ∞) | Number of ungated pores |
| `gated_pore_count` | int | [0, ∞) | Number of carrier-coupled gated pores (0 until bridge installed) |
| `gate_state` | enum per gate | {OPEN, CLOSED} | Current pore state (if gated) |
| `gate_energy` | float | [0, ∞) | ΔG_gate: energy for conformation switch |
| `gate_carrier_compatible` | bool | — | Whether gate accepts carrier discharge |
| `shuttle_count` | int | [0, ∞) | Number of shuttle/translocator instances (0 until bridge installed) |

---

## 4. Carrier-Coupling Fields

| Variable | Type | Domain | Description |
|----------|------|--------|-------------|
| `carrier_reaches_boundary` | bool | true | Carrier diffuses to boundary interior surface |
| `carrier_has_boundary_target` | bool | false | Whether any carrier discharge site exists on boundary (false until gate bridge) |
| `carrier_drives_transport` | bool | false | Whether carrier energy powers trans-boundary work (false until bridge) |
| `carrier_budget_for_transport` | float | [0, 1] | Fraction of carrier events available for boundary work |

---

## 5. Directionality Fields

| Variable | Type | Domain | Description |
|----------|------|--------|-------------|
| `import_mechanism` | enum | {PASSIVE_ONLY, GATED, ACTIVE} | Current import capability |
| `export_mechanism` | enum | {PASSIVE_ONLY, GATED, ACTIVE} | Current export capability |
| `directional_asymmetry` | bool | false | Whether transport has intrinsic directionality (false until bridge) |
| `species_selectivity` | enum | {NONE, SIZE_ONLY, GATE_CONTROLLED, SPECIES_SPECIFIC} | Transport selectivity level |

---

## 6. Transition Rules

### 6.1 Transport-Level Determination

```
IF fifth_bridge_installed == false:
   transport_level = T1  // passive selective
   active_transport_present = false
   import_mechanism = PASSIVE_ONLY
   export_mechanism = PASSIVE_ONLY
   species_selectivity = SIZE_ONLY

IF fifth_bridge_type == GATE:
   transport_level = T2  // gated permeability (T3 if directional asymmetry)
   active_transport_present = true  // minimal: gating is energy-coupled boundary work
   import_mechanism = GATED
   export_mechanism = GATED
   carrier_has_boundary_target = true
   carrier_drives_transport = true
   species_selectivity = GATE_CONTROLLED
   IF directional_asymmetry:
      transport_level = T3  // biased transport

IF fifth_bridge_type == SHUTTLE or fifth_bridge_type == BOTH:
   transport_level = T4  // active transport
   active_transport_present = true
   import_mechanism = ACTIVE
   export_mechanism = ACTIVE (if reverse shuttle exists)
   species_selectivity = SPECIES_SPECIFIC
```

### 6.2 Bridge Installation (Prospective — Book X Beta)

```
// Family F gate installation:
IF gate_bridge_committed:
   fifth_bridge_installed = true
   fifth_bridge_type = GATE
   gated_pore_count = N_gates  // to be determined
   total_postulates += 1
   total_parameters += 1
   // cost: 15/9/1/6 → 16/10/1/6

// Family G shuttle installation (if needed):
IF shuttle_bridge_committed:
   fifth_bridge_type = BOTH (or SHUTTLE if no gate)
   shuttle_count = N_shuttles
   total_postulates += 1-2 (additional)
   total_parameters += 1-2 (additional)
```

---

## 7. Uncertainty / Fragility Fields

| Variable | Type | Value | Source |
|----------|------|-------|--------|
| `zero_cost_transport_exhausted` | bool | true | Book X Alpha: all 5 families fail |
| `gap_characterized` | bool | true | Structural gap: no carrier target at boundary |
| `minimum_bridge_identified` | bool | true | Family F: carrier-coupled boundary gate (1P + 1p) |
| `fuller_bridge_identified` | bool | true | Family G: carrier-driven shuttle (2P + 2p) |
| `bridge_committed` | bool | false | Not yet — Book X Beta decision pending |
| `gate_sufficient_for_program` | enum | OPEN | Whether gating alone meets downstream requirements |
| `transport_fragility` | enum | N/A | Transport not yet installed |

---

## 8. Verdict Fields

| Field | Value | Authority |
|-------|-------|----------|
| `zero_cost_transport_found` | `NO` | Book X Alpha |
| `fifth_bridge_required` | `YES` | Book X Alpha |
| `active_transport_justified` | `NO` (not yet installed) | Book X Alpha |
| `transport_level` | `T1` (passive selective) | Book X Alpha |
| `minimum_bridge` | `Family_F_gate_1P_1p` | Book X Alpha |
| `fuller_bridge` | `Family_G_shuttle_2P_2p` | Book X Alpha |
| `book_x_alpha_changes_state` | `PARTIAL` (gap characterized; threshold NOT crossed) | Book X Alpha |
| `global_verdict` | `A` | No transport from current structure; fifth bridge required |
| `next_stage` | `book_x_beta_boundary_gate_bridge_architecture` | Book X Alpha recommendation |

---

## 9. Minimal Serialized Example

```json
{
  "program_phase": "BOOK_X_ALPHA",
  "stage": "active_transport_and_boundary_crossing_audit",

  "transport": {
    "level": "T1_passive_selective",
    "active_transport": false,
    "zero_cost_found": false,
    "fifth_bridge_required": true,
    "fifth_bridge_installed": false,
    "minimum_bridge": {
      "family": "F_carrier_coupled_boundary_gate",
      "postulates": 1,
      "parameters": 1,
      "transport_level": "T2_T3"
    },
    "fuller_bridge": {
      "family": "G_carrier_driven_shuttle",
      "postulates": 2,
      "parameters": 2,
      "transport_level": "T3_T4"
    }
  },

  "boundary": {
    "type": "K6_K7_crosslinked_mesh",
    "passive_pores": true,
    "gated_pores": 0,
    "shuttles": 0,
    "selectivity": "SIZE_ONLY",
    "import": "PASSIVE_ONLY",
    "export": "PASSIVE_ONLY",
    "dynamic_gating": false,
    "carrier_target_at_boundary": false
  },

  "zero_cost_routes": {
    "A_carrier_pore": "FAILS",
    "B_gate_switch": "FAILS",
    "C_repair_retention": "FAILS",
    "D_growth_transport": "FAILS",
    "E_pseudo": "CONFIRMED_all_fail"
  },

  "gap_characterization": {
    "root_cause": "No mechanism connects internal energetic expenditure to trans-boundary material movement",
    "carrier_terminates_at": "internal_scaffold_discharge_pockets",
    "boundary_has": "no_functional_transport_components",
    "pattern": "analogous_to_Book_V_Beta_coupling_gap_and_Book_VII_Alpha_M4_ceiling"
  },

  "cost": {
    "total_postulates": 15,
    "total_parameters": 9,
    "total_fields": 1,
    "total_dof": 6,
    "book_x_alpha_added": {"postulates": 0, "parameters": 0},
    "prospective_with_gate": {"postulates": 16, "parameters": 10},
    "prospective_with_shuttle": {"postulates": 17, "parameters": 11}
  },

  "verdict": {
    "global": "A",
    "active_transport": "NOT_JUSTIFIED",
    "transport_level": "T1",
    "fifth_bridge": "REQUIRED",
    "state_change": "PARTIAL_gap_characterized_threshold_not_crossed",
    "next_stage": "book_x_beta_boundary_gate_bridge_architecture"
  }
}
```

---

## 10. Integration Notes

### 10.1 What GRUT-RAI Must Update from Book X Alpha

1. **Transport level: T1 (passive selective).** No change from Book IX. All zero-cost routes fail.
2. **Fifth bridge required.** The structural gap is definitively characterized: no carrier target exists at the boundary; no mechanism connects internal energy to trans-boundary work.
3. **Minimum bridge identified:** Family F carrier-coupled boundary gate (1P + 1p) provides T2–T3 gated/biased transport.
4. **Fuller bridge identified:** Family G carrier-driven shuttle (2P + 2p) provides T3–T4 active import.
5. **Book X Beta is the correct next stage:** Bridge architecture design, analogous to Book V Delta (HIC) and Book VII Beta (carrier).
6. **Pattern confirmed:** Zero-cost exhaustion → gap characterization → minimum bridge identification → bridge-architecture stage. This is the third time the program has followed this pattern (Book V coupling → HIC; Book VII ceiling → carrier; Book X boundary → gate).

### 10.2 What GRUT-RAI Must NOT Update

- No change to transport level (still T1)
- No claim of active transport (absent)
- No change to M/D/L/A levels (all unchanged)
- No change to cost (15/9/1/6)
- No commitment to fifth bridge yet (that is Book X Beta's decision)
- No claim of ATP equivalence (proto-currency; internal diffusion only)

---

*GRUT-RAI Transport State Model complete. Entity types, transport variables, boundary/gate fields, carrier-coupling fields, directionality fields, transition rules, verdict fields, and minimal serialized example provided. Transport level: T1. Fifth bridge required. Gap characterized. Book X Beta: boundary-gate bridge architecture.*
