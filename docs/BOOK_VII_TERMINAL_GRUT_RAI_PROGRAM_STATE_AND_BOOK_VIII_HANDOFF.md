# Book VII Terminal: GRUT-RAI Program State and Book VIII Handoff

## Machine-Readable Terminal State and Forward-Facing Handoff Specification

---

## 1. Terminal State Fields

| Field | Value | Authority |
|-------|-------|----------|
| `program_phase` | `BOOK_VII_TERMINAL` | Current |
| `scaffold_identity` | "Self-limiting reproducing proto-cell with conditionally dominant proto-metabolic organization, supplementary regulated division, lineage robustness, and convergent proto-Darwinian dynamics" | Earned |
| `energy_level` | `M4_conditional` | Book VII Gamma |
| `energy_level_unconditional` | `M3_expanded_supplementary` | Book VII Alpha |
| `carrier_status` | `provisionally_committed` | Book VII Gamma |
| `carrier_regime` | `robust_requires_DG_ge_28kT` | Book VII Gamma |
| `division_level` | `D3_supplementary_regulated` | Book VI Alpha (unchanged) |
| `division_conditional` | `D4_conditional_under_M4` | Book VII Gamma |
| `lineage_level` | `L3_supplementary_robust` | Book VI Beta (unchanged) |
| `lineage_conditional` | `L4_approaches_under_M4` | Book VII Gamma |
| `adaptive_level` | `A3_supplementary_proto_darwinian` | Book VI Gamma (unchanged) |
| `adaptive_conditional` | `A4_conditional_under_M4` | Book VII Gamma |
| `homeostasis_status` | `preconditions_crossed_passive` | Book V Alpha (unchanged) |
| `active_transport` | `not_demonstrated` | Unresolved |
| `energy_currency_status` | `proto_currency_conditional` | Book VII Gamma |
| `life_status` | `not_justified` | Multiple boundaries |

---

## 2. Threshold-Status Fields

| Threshold | Status | Stage |
|-----------|--------|-------|
| `homeostasis_preconditions` | `crossed` | Book V Alpha |
| `supplementary_proto_metabolic` | `crossed_supplementary` | Book V Zeta |
| `M3_expanded_supplementary` | `crossed` | Book VII Alpha |
| `M4_conditional_dominant` | `conditional` | Book VII Gamma |
| `M4_unconditional` | `not_crossed` | — |
| `D3_regulated_division` | `crossed` | Book VI Alpha |
| `D4_conditional` | `conditional_under_M4` | Book VII Gamma |
| `L3_lineage_robustness` | `crossed` | Book VI Beta |
| `L4_conditional` | `conditional_under_M4` | Book VII Gamma |
| `A3_proto_darwinian` | `crossed` | Book VI Gamma |
| `A4_conditional` | `conditional_under_M4` | Book VII Gamma |
| `proto_currency` | `conditional` | Book VII Gamma |
| `atp_like_currency` | `not_justified` | — |
| `active_transport` | `not_demonstrated` | — |
| `full_metabolism` | `not_achieved` | — |
| `life` | `not_justified` | — |

---

## 3. Energetic / Carrier-Commitment Classification Fields

| Field | Value |
|-------|-------|
| `energy_level_conditional` | `M4_conditional_dominant` |
| `energy_level_unconditional` | `M3_expanded_supplementary` |
| `directed_fraction_M3` | `0.15-0.25` |
| `directed_fraction_M4` | `0.30-0.34 (in robust regime)` |
| `carrier_committed` | `true (provisional)` |
| `carrier_revocation_condition` | `DG_barrier_shown_below_28kT` |
| `carrier_cost` | `{"postulates": 1, "parameters": 2}` |
| `hic_pairings` | `["P1_replication", "P2_proofreading", "P3_boundary", "P4_repair"]` |
| `hic_network_size` | `4_nodes` |
| `organizational_inversion` | `conditional (directed > ambient for key processes under M4)` |

---

## 4. Robust-Regime-Condition Fields

| Field | Value |
|-------|-------|
| `robust_regime_threshold` | `DG_barrier >= 28 kT` |
| `marginal_regime_range` | `DG_barrier 23-28 kT` |
| `weak_regime_threshold` | `DG_barrier < 23 kT` |
| `tau_diffusion` | `~2 ms` |
| `eta_carrier_robust` | `> 0.95` |
| `eta_carrier_marginal` | `0.1-0.6` |
| `eta_carrier_weak` | `< 0.1` |
| `regime_physically_plausible` | `robust: YES; not derived from first principles` |

---

## 5. Blocked-Boundary Fields

| Boundary | Status | Why blocked | What would unblock |
|----------|--------|-------------|-------------------|
| `unconditional_M4` | **Blocked** | ΔG_barrier not derived from scaffold physics | Quantitative analysis of K=2 conformational barriers |
| `D4_unconditional` | **Blocked** | Conditional on M4 | Unconditional M4 + D/L/A reassessment |
| `L4_unconditional` | **Blocked** | Conditional on M4 | Same |
| `A4_unconditional` | **Blocked** | Conditional on M4 | Same |
| `atp_like_currency` | **Blocked** | Carrier lacks biochemical specificity | Not achievable at bridge level |
| `active_transport` | **Blocked** | Carrier is internal diffusion | Boundary-crossing mechanism (new postulate) |
| `full_metabolism` | **Blocked** | No feedback regulation; no energy budget | Regulatory architecture |
| `open_ended_evolution` | **Blocked** | Convergent; no innovation; no ecology | Ecological structure + innovation |
| `life` | **Blocked** | All above | All above simultaneously |

---

## 6. Book VIII Entry-Condition Fields

| Field | Value |
|-------|-------|
| `book_viii_first_target` | `downstream_domain_reassessment_under_M4` |
| `entry_scaffold` | "Self-limiting reproducing proto-cell with M4-conditional dominant metabolism, D3, L3, A3" |
| `entry_cost` | `15/9/1/6` |
| `entry_energy_level` | `M4_conditional (or M3 unconditional fallback)` |
| `entry_D_level` | `D3 unconditional; D4-conditional under M4` |
| `entry_L_level` | `L3 unconditional; L4-approaches under M4` |
| `entry_A_level` | `A3 unconditional; A4-conditional under M4` |
| `problem_to_solve` | "Determine whether M4 energetic backing upgrades D3→D4, L3→L4, A3→A4" |
| `success_criterion` | "At least one D/L/A level unconditionally upgrades with M4 support" |
| `method` | "Systematic reassessment analogous to Book VI's exploitation of Book V HIC" |
| `depends_on` | `["existing_M4_conditional", "existing_D3_L3_A3", "carrier_commitment"]` |
| `does_not_inherit` | `["unconditional_M4", "ATP_currency", "active_transport", "D4_L4_A4_unconditional", "life"]` |

---

## 7. Cost/Debt Status

```json
{
  "total_postulates": 15,
  "truly_independent_postulates": 13,
  "dependent_consequences": 2,
  "total_free_parameters": 9,
  "constrained_fixed_parameters": 2,
  "new_spacetime_fields": 1,
  "new_propagating_dof": 6,
  "bridge_layers": {
    "matter_bridge": {"postulates": 4, "parameters": 2, "fields": 0, "dof": 0},
    "gauge_bridge": {"postulates": 2, "parameters": 1, "fields": 1, "dof": 6},
    "energy_bridge_HIC": {"postulates": 1, "parameters": 1, "fields": 0, "dof": 0},
    "energy_bridge_carrier": {"postulates": 1, "parameters": 2, "fields": 0, "dof": 0}
  },
  "zero_cost_upper_stack_targets": 23,
  "upper_stack_bridge_debts": 2,
  "book_vii_added_cost": {"postulates": 1, "parameters": 2},
  "book_vii_zero_cost_targets": 1
}
```

---

## 8. Minimal Serialized Terminal State

```json
{
  "program_phase": "BOOK_VII_TERMINAL",
  "book_vii_global_verdict": "A_meaningful_bounded_advance",

  "scaffold_identity": "Self-limiting reproducing proto-cell with conditionally dominant proto-metabolic organization, supplementary regulated division, lineage robustness, and convergent proto-Darwinian dynamics",

  "classification": {
    "energy_level_conditional": "M4_conditional_dominant",
    "energy_level_unconditional": "M3_expanded_supplementary",
    "directed_fraction_M4": "0.30-0.34",
    "directed_fraction_M3": "0.15-0.25",
    "carrier_status": "provisionally_committed",
    "carrier_regime_required": "DG_ge_28kT",
    "division_level": "D3_unconditional",
    "division_conditional": "D4_conditional_under_M4",
    "lineage_level": "L3_unconditional",
    "lineage_conditional": "L4_approaches_under_M4",
    "adaptive_level": "A3_unconditional",
    "adaptive_conditional": "A4_conditional_under_M4",
    "homeostasis": "preconditions_passive",
    "active_transport": "not_demonstrated",
    "life_status": "not_justified"
  },

  "book_vii_advances": {
    "alpha": {"result": "M3_expanded_supplementary", "cost": 0, "new_pairings": ["P3_boundary", "P4_repair"]},
    "beta": {"result": "carrier_bridge_designed", "cost": {"postulates": 1, "parameters": 2}},
    "gamma": {"result": "M4_conditional_verified", "cost": 0, "directed_fraction": "0.30-0.34"}
  },

  "carrier": {
    "family": "J_HIC_to_carrier_hybrid",
    "object": "K2_scale_composite_conformational_switch",
    "status": "provisionally_committed",
    "regime": "robust_DG_ge_28kT",
    "eta_robust": 0.95,
    "directed_fraction_contribution": "0.10-0.15"
  },

  "cost": {
    "total_postulates": 15,
    "total_parameters": 9,
    "total_fields": 1,
    "total_dof": 6,
    "bridges": 4,
    "zero_cost_targets": 23
  },

  "blocked_boundaries": [
    "unconditional_M4",
    "D4_unconditional", "L4_unconditional", "A4_unconditional",
    "atp_like_currency", "active_transport",
    "full_metabolism", "open_ended_evolution", "life"
  ],

  "book_viii_handoff": {
    "first_target": "downstream_domain_reassessment_under_M4",
    "justification": "highest_leverage_at_zero_cost_analogous_to_book_VI",
    "entry_cost": "15/9/1/6",
    "problem": "can_M4_backing_upgrade_D3_L3_A3_to_D4_L4_A4",
    "method": "systematic_reassessment_analogous_to_book_VI"
  }
}
```

---

## 9. Integration Notes

### 9.1 What GRUT-RAI Must Carry Forward from Book VII

1. **Two energetic levels coexist:** M3 (unconditional, ~15–25%) and M4-conditional (~30–34%). Use M4 for conditional reasoning; use M3 as the fallback floor.
2. **Carrier is provisionally committed.** Revocable if ΔG < 28 kT. Use carrier in M4-conditional reasoning; exclude it in M3-fallback reasoning.
3. **D/L/A levels have dual states:** Unconditional (D3/L3/A3) and conditional-under-M4 (D4-cond/L4-app/A4-cond). Do not conflate them.
4. **Four bridges.** Matter (4+2), gauge (2+1+1+6), HIC (1+1), carrier (1+2). Total: 15/9/1/6.
5. **23 zero-cost targets.** From chemistry-entry through M3 expanded supplementary metabolism.
6. **Proto-currency, NOT ATP.** The carrier distributes energy internally but is not biochemically specific.
7. **Active transport: still NO.** The carrier does not cross the compartment boundary.
8. **Book VIII target: downstream domain reassessment.** Exploit M4 for D/L/A upgrades.

### 9.2 What GRUT-RAI Must NOT Carry Forward

- Any claim of unconditional M4 (it is conditional on ΔG ≥ 28 kT)
- Any claim of D4/L4/A4 as unconditional levels (they are conditional on M4)
- Any claim of ATP equivalence (proto-currency only)
- Any claim of active transport (internal diffusion only)
- Any claim of life

---

*Book VII Terminal GRUT-RAI Program State and Book VIII Handoff complete. Terminal state frozen. Dual-level classification (conditional M4 / unconditional M3). Carrier provisionally committed. Cost: 15/9/1/6. Four bridges. 23 zero-cost targets. Book VIII first target: downstream domain reassessment under M4. Handoff is clean.*
