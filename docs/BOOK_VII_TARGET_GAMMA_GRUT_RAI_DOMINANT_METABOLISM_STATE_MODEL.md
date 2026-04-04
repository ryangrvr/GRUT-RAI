# Book VII — Target Gamma: GRUT-RAI Dominant Metabolism State Model

## Minimum Machine-Usable State Model for M4 Reasoning

---

## 1. Entity Types

| Entity ID | Name | Description | Parent |
|-----------|------|-------------|--------|
| `Carrier_committed` | Committed energy carrier | K=2-scale composite; provisionally committed bridge object | Carrier |
| `CarrierPool_M4` | M4-level carrier pool | Internal population of carriers supporting dominant metabolism | System |
| `ProtoCell_M4` | M4-level proto-cell | Proto-cell with HIC network + committed carrier; dominant metabolism | System |
| `RemoteTargetSite` | Carrier-compatible remote discharge site | Scaffold pocket at any internal location accepting carrier discharge | Target |

---

## 2. Carrier State Variables (Verified)

| Variable | Type | Domain | Description | Verified value |
|----------|------|--------|-------------|---------------|
| `carrier_state` | Enum | {`unloaded`, `loaded`, `in_transit`, `at_target`, `leaked`, `degraded`} | Current carrier status | — |
| `E_carrier` | Float | kT | Energy content of loaded state | ~5–10 kT (from HIC discharge) |
| `τ_carrier` | Float | seconds | Loaded-state lifetime | Must be ≥ ~0.5 s (ΔG ≥ 28 kT) |
| `ΔG_barrier` | Float | kT | Conformational barrier | **≥ 28 kT for robust regime** |
| `τ_diffusion` | Float | seconds | Mean transit time across proto-cell | ~2 ms (from L²/6D) |
| `η_carrier` | Float ∈ [0,1] | | Utilization efficiency (deliver / (deliver + leak)) | **> 0.95 in robust regime** |

---

## 3. Flux / Accounting Fields (Verified)

| Variable | Type | Description | Verified range |
|----------|------|-------------|---------------|
| `hic_direct_events` | Float | Concerted-mode HIC events per cycle | ~200–350 |
| `carrier_production` | Float | Carriers loaded per cycle | ~100–320 |
| `carrier_delivered` | Float | Carriers successfully discharged at targets | ~95–305 (at η > 0.95) |
| `carrier_leaked` | Float | Carriers lost to spontaneous decay | ~5–15 (at η > 0.95) |
| `total_directed` | Float | HIC-direct + carrier-driven | ~295–655 |
| `total_ambient` | Float | Thermally-driven events | ~1200–2000 minus directed |
| `total_events` | Float | All events per cycle | ~1200–2000 |
| `directed_fraction_verified` | Float ∈ [0,1] | Verified combined directed share | **~0.25–0.34 (robust regime)** |
| `metabolic_level_verified` | Enum | {M2, M3, M3+, M4-conditional, M4, M5} | **M4-conditional** |

---

## 4. Transport / Delivery Fields

| Variable | Type | Description | Value |
|----------|------|-------------|-------|
| `diffusion_coefficient` | Float | Carrier D in proto-cell interior | ~10⁻¹⁰ m²/s |
| `proto_cell_diameter` | Float | Characteristic internal distance | ~1 μm |
| `carrier_mean_free_time` | Float | τ_diffusion = L²/6D | ~2 ms |
| `n_compatible_target_types` | Integer | Number of process types with carrier-discharge pockets | 4 (separation, proofread, boundary, repair) |
| `n_compatible_target_sites` | Integer | Total discharge sites in proto-cell | ~20–100 |
| `target_encounter_rate` | Float | Rate a carrier finds a target | ~k_on × [targets] × [carriers] |
| `spatial_coverage` | Float ∈ [0,1] | Fraction of proto-cell interior reachable by carrier | ~1.0 (full interior) at robust τ_carrier |

---

## 5. Downstream-Impact Fields (Verified)

| Variable | Type | Description | M3 value | M4-conditional value |
|----------|------|-------------|----------|---------------------|
| `directed_replication_fraction` | Float | Replication events with energetic support | ~0.15 | **~0.30** |
| `directed_fidelity_fraction` | Float | Proofreading events with support | ~0.15 | **~0.30** |
| `directed_boundary_fraction` | Float | Boundary-growth events with support | ~0.08 | **~0.18** |
| `directed_repair_fraction` | Float | Catalyst-repair events with support | ~0.08 | **~0.18** |
| `division_level_conditional` | Enum | Division level if M4 holds | D3 | **D4-conditional** |
| `lineage_level_conditional` | Enum | Lineage level if M4 holds | L3 | **L4-approaches** |
| `adaptive_level_conditional` | Enum | Adaptive level if M4 holds | A3 | **A4-conditional** |
| `organizational_inversion` | Boolean | Directed > ambient for key processes | false | **true (for replication + fidelity)** |

---

## 6. Transition Rules

### 6.1 Carrier Production (per HIC per cycle)

```
if HIC_cycle_complete AND C_unloaded_available_at_secondary_pocket:
    CARRIER_LOAD → C_loaded produced
    carrier_production += 1
```

### 6.2 Carrier Transit and Delivery

```
for each C_loaded:
    transit_time = sample_from_diffusion(τ_diffusion)
    leak_time = sample_from_exponential(τ_carrier)

    if transit_time < leak_time AND target_available:
        CARRIER_DELIVER → C_loaded discharges at target
        carrier_delivered += 1
    else:
        CARRIER_LEAK → C_loaded → C_unloaded + heat
        carrier_leaked += 1

η_carrier = carrier_delivered / (carrier_delivered + carrier_leaked)
```

### 6.3 Combined Flux

```
total_directed = hic_direct_events + carrier_delivered
directed_fraction = total_directed / (total_directed + ambient_events)

if directed_fraction >= 0.30:
    metabolic_level = "M4_conditional"
elif directed_fraction >= 0.15:
    metabolic_level = "M3"
else:
    metabolic_level = "M2"
```

### 6.4 Downstream Level Updates (Conditional on M4)

```
if metabolic_level == "M4_conditional":
    division_level = "D4_conditional"  # carrier-backed repair/maintenance
    lineage_level = "L4_approaches"    # carrier-backed recovery
    adaptive_level = "A4_conditional"  # expanded landscape
else:
    # retain Book VI levels
    division_level = "D3"
    lineage_level = "L3"
    adaptive_level = "A3"
```

---

## 7. Uncertainty / Fragility Fields

| Field | Type | Description | Status |
|-------|------|-------------|--------|
| `ΔG_barrier_actual` | Unknown float | Actual conformational barrier for K=2 carrier | **POSTULATED ≥ 28 kT; not derived** |
| `ΔG_barrier_sufficient` | Boolean | Whether barrier meets robust-regime requirement | **CONDITIONAL** |
| `carrier_commitment_status` | Enum | {`provisional`, `confirmed`, `revoked`} | **PROVISIONAL** |
| `m4_status` | Enum | {`not_reached`, `conditional`, `verified`, `robust`} | **CONDITIONAL** |
| `regime_classification` | Enum | {`weak_<23`, `marginal_23-28`, `robust_>=28`} | **TARGET: robust** |
| `downstream_conditional` | Boolean | Whether D4/L4/A4 upgrades depend on M4 holding | **TRUE** |

---

## 8. Verdict Fields

| Field | Type | Domain | Meaning |
|-------|------|--------|---------|
| `m4_verified` | Enum | {`no`, `conditional`, `verified`} | M4 threshold status |
| `carrier_committed` | Boolean | | Whether carrier bridge is adopted |
| `commitment_provisional` | Boolean | | Whether commitment can be revoked |
| `directed_fraction_verified` | Float | | Verified (not projected) combined directed share |
| `multi_domain_consequence` | Boolean | | Whether ≥3 domains materially improved |
| `organizational_inversion` | Boolean | | Whether directed > ambient for key processes |
| `gamma_changes_state` | Boolean | | Whether this audit upgrades scaffold |
| `gamma_global_verdict` | Enum | {`A_not_earned`, `B_conditional_commit`, `C_robust_verified`} | |

---

## 9. Minimal Serialized Example

```json
{
  "stage": "BOOK_VII_TARGET_GAMMA",
  "audit_type": "m4_threshold_verification",

  "carrier_verified": {
    "ΔG_barrier_requirement": ">=28_kT",
    "η_carrier_robust": 0.95,
    "τ_carrier_robust": ">=0.5_s",
    "τ_diffusion": "0.002_s",
    "regime": "robust"
  },

  "flux_verified": {
    "hic_direct": 300,
    "carrier_delivered": 250,
    "total_directed": 550,
    "total_ambient": 1050,
    "total_events": 1600,
    "directed_fraction": 0.34,
    "metabolic_level": "M4_conditional"
  },

  "downstream_conditional": {
    "division": "D4_conditional",
    "lineage": "L4_approaches",
    "adaptive": "A4_conditional",
    "organizational_inversion": true
  },

  "commitment": {
    "carrier_committed": true,
    "provisional": true,
    "revocation_condition": "ΔG_barrier_shown_below_28_kT",
    "cost_accepted": {"postulates": 1, "parameters": 2}
  },

  "cost": {
    "total_postulates": 15,
    "total_parameters": 9,
    "total_fields": 1,
    "total_dof": 6,
    "bridges": ["matter_4+2", "gauge_2+1+1+6", "HIC_1+1", "carrier_1+2"]
  },

  "verdict": {
    "gamma_global_verdict": "B_conditional_commit",
    "m4_verified": "conditional",
    "carrier_committed": true,
    "gamma_changes_state": true,
    "level_upgrade": "M3 -> M4_conditional",
    "next_audit": "book_vii_terminal_capstone"
  }
}
```

---

## 10. Integration Notes

### 10.1 What This Extends

Gamma extends the Beta carrier-bridge state model with:
- Verified (not projected) flux values
- Three-regime structure (weak/marginal/robust) with explicit ΔG boundaries
- Downstream conditional level updates (D4/L4/A4 contingent on M4)
- Commitment status fields (provisional/confirmed/revoked)
- Organizational-inversion flag

### 10.2 What GRUT-RAI Must Track Post-Gamma

1. **Metabolic level = M4-conditional.** Not M4-verified (barrier not derived). Not M3 (carrier committed).
2. **Carrier provisionally committed.** Cost accepted: 15/9/1/6. Revocable if ΔG < 28 kT.
3. **Downstream levels are conditional on M4:** D4-conditional, L4-approaches, A4-conditional. These revert if M4 reverts.
4. **Organizational inversion for key processes:** Replication and fidelity are now directed-dominant (~30%) rather than thermal-dominant.
5. **Active transport: still NO.** Carrier is internal diffusion.
6. **ATP language: still NO.** Use "proto-currency."

### 10.3 What GRUT-RAI Must NOT Carry Forward

- Any claim that M4 is guaranteed (it is conditional on ΔG ≥ 28 kT)
- Any claim that D4/L4/A4 are achieved (they are conditional on M4)
- Any claim of ATP equivalence
- Any claim of active transport
- Any claim of life

---

*GRUT-RAI Dominant Metabolism State Model complete. Carrier verified in robust regime (ΔG ≥ 28 kT; η > 0.95; directed ~30–34%). Three-regime structure documented. Downstream conditional updates (D4/L4/A4). Provisional commitment. Organizational inversion for key processes. Cost: 15/9/1/6. Proto-currency. Not ATP. Not life.*
