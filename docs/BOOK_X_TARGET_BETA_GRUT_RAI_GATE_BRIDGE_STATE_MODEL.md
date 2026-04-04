# Book X — Target Beta: GRUT-RAI Gate-Bridge State Model

## Machine-Readable State Model for Boundary-Gate Reasoning

---

## 1. Entity Types

| Entity | Description | Source |
|--------|-------------|--------|
| `ccbg_gate` | Carrier-Coupled Boundary Gate — mesh-embedded scaffold with carrier-responsive conformational pore switch | Book X Beta |
| `passive_pore` | Structural gap in mesh; size-selective; no energetic control | Book IV Tau |
| `gated_pore` | Pore controlled by CCBG; carrier-actuated open/closed | Book X Beta |
| `carrier_loaded` | K=2 (N=2, ℓ=0) excited state; energy source for gate actuation | W0 + Book IX Alpha |
| `transportable_species` | Molecule that can transit through an open gated pore | Book X Alpha §4.2 |
| `binding_pocket` | Optional exterior-face pocket on CCBG for directional transport (T3) | Book X Beta §5 (directional extension) |

---

## 2. Gate / Transport State Variables

| Variable | Type | Domain | Description |
|----------|------|--------|-------------|
| `transport_level` | enum | {T0, T1, T2, T3, T4, T5} | Current transport capability |
| `ccbg_installed` | bool | — | Whether the CCBG bridge is committed |
| `n_gated_pores` | int | [0, ∞) | Number of carrier-coupled gated pores |
| `n_passive_pores` | int | [1, ∞) | Number of ungated passive pores |
| `gate_fraction` | float | [0, 1] | n_gated / (n_gated + n_passive); transport impact scales with this |
| `directional_extension` | bool | — | Whether binding-pocket directional bias is included |
| `dg_gate` | float | [0, ∞) | Gate switching energy (must be ≤ E_carrier) |
| `tau_reset` | float | (0, ∞) | Gate spontaneous reset timescale |

---

## 3. Carrier-Coupling Fields

| Variable | Type | Domain | Description |
|----------|------|--------|-------------|
| `carrier_reaches_gate` | bool | — | Whether loaded carriers can diffuse to gate pockets (true if gate is interior-accessible) |
| `carrier_discharge_at_gate` | bool | — | Whether carrier can dock and discharge at gate pocket |
| `carrier_budget_for_gates` | float | [0, 1] | Fraction of carrier events allocated to gate actuation |
| `carrier_events_per_cycle` | int | — | Total carrier events per reproductive cycle (from M4 budget) |
| `gate_events_per_cycle` | int | — | Number of gate actuations per cycle |

---

## 4. Directionality Fields

| Variable | Type | Domain | Description |
|----------|------|--------|-------------|
| `import_mechanism` | enum | {PASSIVE_ONLY, GATED_TIMING, BIASED_IMPORT, ACTIVE_IMPORT} | Import capability |
| `export_mechanism` | enum | {PASSIVE_ONLY, GATED_TIMING, BIASED_EXPORT, ACTIVE_EXPORT} | Export capability |
| `directional_asymmetry` | bool | — | Whether gate has intrinsic import/export bias |
| `target_species_binding` | bool | — | Whether gate has species-specific binding pocket |
| `species_selectivity` | enum | {NONE, SIZE_ONLY, GATE_CONTROLLED, SPECIES_SPECIFIC} | Selectivity level |

---

## 5. Transition Rules

### 5.1 Transport-Level Determination

```
IF ccbg_installed == false:
   transport_level = T1
   import_mechanism = PASSIVE_ONLY
   export_mechanism = PASSIVE_ONLY

IF ccbg_installed == true AND directional_extension == false:
   transport_level = T2  // gated permeability
   import_mechanism = GATED_TIMING
   export_mechanism = GATED_TIMING
   species_selectivity = GATE_CONTROLLED

IF ccbg_installed == true AND directional_extension == true:
   transport_level = T3  // biased transport
   import_mechanism = BIASED_IMPORT
   export_mechanism = BIASED_EXPORT
   directional_asymmetry = true
   species_selectivity = SPECIES_SPECIFIC (for target species)
```

### 5.2 Gate Actuation Cycle

```
WHILE gate in CLOSED state:
   IF carrier_loaded approaches gate_pocket:
      carrier docks (geometry-locked)
      carrier discharges: ΔE₁₂ → gate backbone
      gate_state: CLOSED → OPEN
      carrier_unloaded detaches → returns to pool

WHILE gate in OPEN state:
   // Species can transit through open pore
   IF directional_extension AND target_species at exterior:
      target binds at exterior pocket
      conformational reset displaces target → interior
      target released to interior (import event)
   ELSE:
      species transit by concentration gradient (passive through open pore)

   AFTER τ_reset:
      gate_state: OPEN → CLOSED (spontaneous thermal reset)
```

### 5.3 Bridge Installation (Commitment — Book X Gamma decision)

```
IF ccbg_bridge_committed:
   ccbg_installed = true
   total_postulates += 1
   total_parameters += 1  // ΔG_gate
   IF directional_extension:
      total_parameters += 1  // K_bind

   // Transport level upgrades:
   transport_level = T2 (or T3 with directional)

   // Cost update:
   // 15/9/1/6 → 16/10/1/6 (T2) or 16/11/1/6 (T3)
```

---

## 6. Uncertainty / Fragility Fields

| Variable | Type | Value | Source |
|----------|------|-------|--------|
| `ccbg_committed` | bool | false | Not yet — Book X Gamma decision |
| `gate_density_sufficient` | enum | OPEN | Depends on N_gates vs N_passive; not yet determined |
| `dg_gate_achievable` | enum | PLAUSIBLE | ΔG_gate ≤ E_carrier; structurally available for conformational switches |
| `tau_reset_range` | str | "μs to ms" | Depends on backbone geometry; not pinned |
| `directional_efficiency` | enum | OPEN | Binding-release displacement efficiency not computed |
| `passive_dilution_risk` | enum | MODERATE | Many passive pores may dilute gating effect |
| `carrier_budget_impact` | enum | LOW | ~5–10% of carrier events for gates; ~90% remains for internal use |
| `gate_failure_graceful` | bool | true | Stuck-open → passive pore; stuck-closed → one blocked pore |

---

## 7. Verdict Fields

| Field | Value | Authority |
|-------|-------|----------|
| `minimum_bridge_found` | `YES` | Book X Beta |
| `bridge_family` | `F_CCBG` | Book X Beta |
| `bridge_cost` | `1P + 1p (T2) or 1P + 2p (T3)` | Book X Beta |
| `bridge_committed` | `NO (pending Book X Gamma)` | — |
| `transport_level_if_committed` | `T2 or T3` | Book X Beta |
| `family_g_necessary` | `NO (reserved)` | Book X Beta |
| `book_x_beta_changes_state` | `YES` | Fifth bridge identified and architected |
| `global_verdict` | `C` | Minimum bridge found; boundary-crossing work plausibly unlockable |
| `next_stage` | `book_x_gamma_boundary_gate_commitment_and_transport_verification` | Book X Beta recommendation |

---

## 8. Minimal Serialized Example

```json
{
  "program_phase": "BOOK_X_BETA",
  "stage": "boundary_gate_bridge_architecture",

  "bridge": {
    "family": "F_CCBG",
    "name": "Carrier-Coupled Boundary Gate",
    "postulate": "mesh-embedded scaffold with carrier-responsive conformational pore switch",
    "cost": {"postulates": 1, "parameters": 1, "fields": 0, "dof": 0},
    "cost_with_directional": {"postulates": 1, "parameters": 2, "fields": 0, "dof": 0},
    "committed": false,
    "transport_level_t2": "gated_permeability",
    "transport_level_t3": "biased_transport_with_directional_extension"
  },

  "formal_cycle": {
    "steps": [
      "Gate_closed (resting; backbone fills pore)",
      "C_loaded docks at gate discharge pocket",
      "Carrier discharges → backbone flips: closed → open",
      "C_unloaded detaches → returns to pool",
      "Species transits through open pore (T2: diffusion; T3: binding-release)",
      "Gate_open → Gate_closed: spontaneous thermal reset (τ_reset)",
      "Cycle repeats on next carrier arrival"
    ],
    "directional_extension": [
      "Target species binds at exterior pocket during Gate_open",
      "Conformational reset displaces target → interior",
      "Target released to interior (net import)"
    ]
  },

  "transport": {
    "current_level": "T1_passive_selective",
    "level_if_t2_committed": "T2_gated_permeability",
    "level_if_t3_committed": "T3_biased_transport",
    "family_g_needed": false,
    "family_g_reserved": true
  },

  "alternatives": {
    "G_shuttle": {"status": "reserved", "cost": "2P+2p", "transport": "T3-T4"},
    "H_work_cycle": {"status": "subsumed_into_G"},
    "I_pseudo_pump": {"status": "DISQUALIFIED"}
  },

  "cost": {
    "current_total": {"postulates": 15, "parameters": 9, "fields": 1, "dof": 6},
    "with_ccbg_t2": {"postulates": 16, "parameters": 10, "fields": 1, "dof": 6},
    "with_ccbg_t3": {"postulates": 16, "parameters": 11, "fields": 1, "dof": 6},
    "bridges": 4,
    "bridges_with_ccbg": 5,
    "zero_cost_targets": 26
  },

  "verdict": {
    "global": "C",
    "minimum_bridge_found": true,
    "bridge_committed": false,
    "transport_unlockable": true,
    "state_change": true,
    "next_stage": "book_x_gamma_commitment_and_transport_verification"
  }
}
```

---

## 9. Integration Notes

### 9.1 What GRUT-RAI Must Update from Book X Beta

1. **Fifth bridge identified:** CCBG (Carrier-Coupled Boundary Gate). Family F. 1P + 1p (T2) or 1P + 2p (T3). Lightest possible bridge.
2. **Formal cycle defined:** Carrier arrival → discharge → conformational switch → pore opens → transit → reset → repeat.
3. **Directional extension available:** Binding-pocket mechanism provides import/export bias at +1 parameter.
4. **Family G reserved:** Shuttle/importer not needed for T2–T3; reserved for T4 if required later.
5. **Bridge NOT yet committed:** Commitment is Book X Gamma's decision.
6. **Transport level unchanged:** Still T1 until commitment.

### 9.2 What GRUT-RAI Must NOT Update

- No change to transport level (still T1 until commitment)
- No change to cost (still 15/9/1/6 until commitment)
- No claim of active transport achieved (bridge designed but not committed)
- No claim of ATP equivalence
- No claim of life

---

*GRUT-RAI Gate-Bridge State Model complete. Entity types, gate/transport variables, carrier-coupling fields, directionality fields, transition rules, fragility fields, verdict fields, and minimal serialized example provided. CCBG identified as minimum fifth bridge. Not yet committed. Book X Gamma: commitment and verification.*
