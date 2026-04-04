# Book IX — Target Alpha: GRUT-RAI Unconditional-M4 State Model

## Machine-Readable State Model for M4-Stabilized Reasoning

---

## 1. Entity Types

| Entity | Description | Source |
|--------|-------------|--------|
| `carrier_loaded` | K=2 composite in (N=2, ℓ=0, S=0) excited state | W0 + Book IX Alpha |
| `carrier_unloaded` | K=2 composite in (N=1, ℓ=0, S=0) ground state | W0 |
| `gauge_boson` | SU(2) gauge field quantum; mediates binding and transitions | Book IV Beta |
| `two_boson_decay` | (N=2,ℓ=0) → (N=1,ℓ=0) + 2 gauge bosons | Book IX Alpha §5 |
| `dissipation_field` | GRUT native τ dΦ/dt + Φ = X background | GRUT core |

---

## 2. Barrier-Stability Fields

| Variable | Type | Domain | Description |
|----------|------|--------|-------------|
| `barrier_height_kT` | float | [0, ∞) | ΔE₁₂/kT = (3/16)α_g²(M_sk/kT) |
| `barrier_height_status` | enum | {MATCHED, SUPPORTED, DERIVED} | Epistemic status of barrier height |
| `barrier_mechanism` | str | — | "Selection-rule-protected (N=2,ℓ=0) metastable state" |
| `barrier_mechanism_status` | enum | {POSTULATED, IDENTIFIED, CONFIRMED} | Epistemic status of mechanism |
| `barrier_regime` | enum | {WEAK, MARGINAL, ROBUST} | Based on barrier_height_kT |

---

## 3. Decay-Channel Fields

| Variable | Type | Domain | Description |
|----------|------|--------|-------------|
| `e1_decay_status` | str | "BLOCKED" | Δℓ=±1 selection rule forbids ℓ=0→ℓ=0 |
| `two_boson_rate_scaling` | str | "Γ ∝ α_g⁸ × M_sk" | Dominant leak channel |
| `two_boson_suppression_factor` | str | "α_g² relative to E1" | Additional suppression from second vertex |
| `tau_two_boson_vs_tau_diff` | float | — | Ratio τ(2γ)/τ_diffusion; must be ≫ 1 |
| `alpha_g_ceiling_for_carrier` | float | ~0.02 | Above this, τ(2γ) < τ_diff |
| `two_boson_assessment` | enum | {CONTAINED, MARGINAL, FAILS} | Current assessment |
| `m1_decay_status` | str | "NEGLIGIBLE" | Suppressed by (v/c)² |
| `e2_decay_status` | str | "NEGLIGIBLE" | Suppressed by (ka₀)² |

---

## 4. Dissipation Fields

| Variable | Type | Domain | Description |
|----------|------|--------|-------------|
| `scale_separation_assumed` | bool | true | ω_composite ≫ γ (inherited from bridge architecture) |
| `dissipation_induced_rate` | str | "~ γ(γ/ω)^n × exp(-ΔE/kT)" | Strongly suppressed |
| `dissipation_assessment` | enum | {CONTAINED, MARGINAL, THREATENS} | Current assessment |
| `dissipation_new_constraint` | bool | false | No new constraint beyond existing assumption |
| `thermal_transition_rate` | str | "~ ν₀ exp(-28) ≈ 6×10⁻¹³ ν₀" | Negligible |

---

## 5. Regime Fields

| Variable | Type | Domain | Description |
|----------|------|--------|-------------|
| `m_level_stabilized` | enum | {NONE, M4_STABILIZED} | Whether M4-stabilized is achieved |
| `m_level_unconditional` | enum | {M3} | Unconditional floor (always M3) |
| `m_level_truly_unconditional` | bool | false | M4 is stabilized, not unconditional |
| `conditioning_type` | enum | {EXTERNAL_PARAMETER, STRUCTURAL_ASSUMPTION, NONE} | Type of remaining condition |
| `structural_conditions` | list[str] | — | ["weak_coupling_alpha_g_le_0.02", "scale_separation_omega_gg_gamma"] |
| `conditions_pre_existing` | bool | true | Both conditions already assumed for bridge architecture |

---

## 6. Debt-Status Fields

| Variable | Type | Domain | Description |
|----------|------|--------|-------------|
| `carrier_postulate_status` | enum | {BRIDGE, REDUCED, STRONGLY_REDUCED, ERASED} | Current postulate status |
| `carrier_postulate_count` | str | "1P + 2p" | Unchanged |
| `e_carrier_status` | enum | {MATCHED, SUPPORTED, STRONGLY_SUPPORTED, DERIVED} | Energy parameter status |
| `tau_carrier_status` | enum | {MATCHED, SUPPORTED, BOUNDED, DERIVED} | Lifetime parameter status |
| `dg_barrier_status` | enum | {MATCHED, SUPPORTED, APPROXIMATELY_DERIVED, DERIVED} | Barrier status |
| `overall_debt` | enum | {FULL, REDUCED, STRONGLY_REDUCED, ERASED} | Aggregate assessment |

---

## 7. Transition Rules

### 7.1 M4-Stabilized Determination

```
IF alpha_g <= 0.02
   AND scale_separation_assumed == true
   AND barrier_height_kT >= 28:

   m_level_stabilized = M4_STABILIZED
   conditioning_type = STRUCTURAL_ASSUMPTION
   two_boson_assessment = CONTAINED
   dissipation_assessment = CONTAINED
   barrier_mechanism_status = CONFIRMED
   barrier_height_status = DERIVED

ELIF alpha_g <= 0.03:
   m_level_stabilized = NONE  // marginal; not stabilized
   conditioning_type = EXTERNAL_PARAMETER  // still externally conditioned
   two_boson_assessment = MARGINAL

ELSE:
   m_level_stabilized = NONE
   two_boson_assessment = FAILS
   // Scaffold reverts to M4-conditional or M3
```

### 7.2 Cascade Promotion

```
IF m_level_stabilized == M4_STABILIZED:
   d_level = D4_STABILIZED  // inherits M4 status
   l_level = L4_STABILIZED  // inherits M4 status
   a_level = A4_STABILIZED  // inherits M4 status
ELSE:
   d_level = D4_CONDITIONAL or D3  // depending on ΔG
   l_level = L4_CONDITIONAL or L3
   a_level = A4_CONDITIONAL or A3
```

### 7.3 Fallback

```
IF alpha_g > 0.03 OR scale_separation_fails:
   m_level_stabilized = NONE
   // Revert to Book VIII dual-state:
   // M4-conditional / M3-unconditional
   // D4-conditional / D3-unconditional
   // L4-conditional / L3-unconditional
   // A4-conditional / A3-unconditional
```

---

## 8. Uncertainty / Fragility Fields

| Variable | Type | Value | Source |
|----------|------|-------|--------|
| `alpha_g_determined` | bool | false | Free parameter of gauge bridge |
| `alpha_g_ceiling` | float | ~0.02 | Two-boson lifetime constraint |
| `alpha_g_hydrogenic_ceiling` | float | ~0.1–0.3 | Pre-existing weak-coupling assumption |
| `constraint_tightening` | str | "α_g ceiling narrowed from ~0.1–0.3 to ~0.02" | Genuine tightening |
| `scale_separation_derived` | bool | false | Assumed, not derived (inherited) |
| `two_boson_rate_exact` | bool | false | Scaling known; exact prefactor from hydrogen analogy |
| `m4_stabilized_fragility` | enum | MODERATE | Depends on α_g being sufficiently weak |
| `residual_vulnerability` | str | "If α_g > 0.03 required for other reasons, carrier fails" | Open |

---

## 9. Verdict Fields

| Field | Value | Authority |
|-------|-------|----------|
| `m4_stabilized_justified` | `YES` | Book IX Alpha |
| `m4_unconditional_justified` | `NO` | Book IX Alpha |
| `carrier_debt_status` | `STRONGLY_REDUCED` | Book IX Alpha |
| `carrier_debt_erased` | `NO` | Book IX Alpha |
| `cascade_promoted` | `YES` | D4/L4/A4 → stabilized |
| `cascade_unconditional` | `NO` | Inherits M4-stabilized, not unconditional |
| `book_ix_alpha_changes_state` | `YES` | M4-conditional → M4-stabilized |
| `new_cost` | `0` | No new postulates or parameters |
| `global_verdict` | `B` | Strengthened but not fully secured |

---

## 10. Minimal Serialized Example

```json
{
  "program_phase": "BOOK_IX_ALPHA",
  "stage": "unconditional_M4_verification_carrier_stabilization",

  "m_level": {
    "stabilized": "M4_STABILIZED",
    "unconditional_floor": "M3",
    "truly_unconditional": false,
    "conditioning_type": "STRUCTURAL_ASSUMPTION",
    "structural_conditions": [
      "weak_coupling_alpha_g_le_0.02",
      "scale_separation_omega_gg_gamma"
    ],
    "conditions_pre_existing": true
  },

  "carrier_barrier": {
    "height_formula": "delta_E_12 = (3/16) alpha_g^2 M_sk",
    "height_status": "DERIVED",
    "mechanism": "selection_rule_protected_N2_ell0_state",
    "mechanism_status": "CONFIRMED",
    "e1_decay": "BLOCKED_exact",
    "two_boson_decay": "CONTAINED_in_weak_coupling",
    "two_boson_scaling": "Gamma proportional to alpha_g^8 times M_sk",
    "alpha_g_ceiling": 0.02,
    "dissipation": "PERTURBATIVE_under_scale_separation",
    "dissipation_new_constraint": false
  },

  "cascade": {
    "d_level": "D4_STABILIZED",
    "l_level": "L4_STABILIZED",
    "a_level": "A4_STABILIZED",
    "cascade_basis": "inherits_M4_stabilized_status"
  },

  "debt": {
    "carrier_postulate": "1P_2p_retained",
    "e_carrier": "STRONGLY_SUPPORTED",
    "tau_carrier": "QUANTITATIVELY_BOUNDED",
    "dg_barrier": "DERIVED",
    "overall": "STRONGLY_REDUCED",
    "erased": false
  },

  "fragility": {
    "alpha_g_determined": false,
    "alpha_g_ceiling_carrier": 0.02,
    "alpha_g_ceiling_hydrogenic": "0.1-0.3",
    "scale_separation_derived": false,
    "m4_fragility": "MODERATE",
    "residual_vulnerability": "alpha_g_gt_0.03_would_kill_carrier"
  },

  "cost": {
    "total_postulates": 15,
    "total_parameters": 9,
    "total_fields": 1,
    "total_dof": 6,
    "book_ix_alpha_added": {"postulates": 0, "parameters": 0},
    "zero_cost_targets": 26
  },

  "verdict": {
    "global": "B",
    "m4_stabilized": "JUSTIFIED",
    "m4_unconditional": "NOT_JUSTIFIED",
    "debt_erased": false,
    "cascade_promoted": true,
    "state_change": true,
    "next_options": ["book_ix_terminal_capstone", "active_transport_audit", "further_stabilization"]
  }
}
```

---

## 11. Integration Notes

### 11.1 What GRUT-RAI Must Update from Book IX Alpha

1. **M4-stabilized replaces M4-conditional as the primary operating level.** M4 now depends on structural assumptions (weak coupling, scale separation) rather than an externally matched parameter (ΔG ≥ 28 kT).

2. **Cascade promotion:** D4/L4/A4 are all promoted to "stabilized" — conditioned on the same structural assumptions as M4.

3. **Carrier debt strongly reduced.** Barrier height derived from binding energy. Metastability mechanism confirmed (selection rule + 2γ containment + dissipation assessment). Lifetime quantitatively bounded. Postulate retained but parameters strongly supported.

4. **New constraint recognized:** α_g ≲ 0.02 for comfortable carrier lifetime. This is tighter than the general weak-coupling requirement but within the same regime.

5. **Conditioning type changed:** From `EXTERNAL_PARAMETER` to `STRUCTURAL_ASSUMPTION`. This is the key epistemic shift.

### 11.2 What GRUT-RAI Must NOT Update

- No change to total cost (15/9/1/6)
- No claim of M4-unconditional (stabilized ≠ unconditional)
- No claim of carrier debt erased (postulate retained)
- No claim of ATP equivalence (proto-currency)
- No claim of active transport
- No claim of life
- No change to zero-cost target count (still 26; Book IX Alpha is an assessment, not a new zero-cost organizational advance)

### 11.3 Current Program State

```
M4-stabilized / M3-unconditional    (conditioning: structural, not external)
D4-stabilized / D3-unconditional    (inherits M4)
L4-stabilized / L3-unconditional    (inherits M4)
A4-stabilized / A3-unconditional    (inherits M4)

Carrier debt: STRONGLY REDUCED (1P + 2p retained; parameters derived/bounded)
Total cost: 15/9/1/6
Bridges: 4 (matter, gauge, HIC, carrier)
Zero-cost targets: 26
```

---

*GRUT-RAI Unconditional-M4 State Model complete. Entity types, barrier-stability fields, decay-channel fields, dissipation fields, regime fields, debt-status fields, transition rules, fragility fields, verdict fields, and minimal serialized example provided. M4-stabilized justified. Cascade promoted to D4/L4/A4-stabilized. Carrier debt strongly reduced but not erased.*
