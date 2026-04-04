# Book VIII — Target Gamma: GRUT-RAI A4 State Model

## Machine-Readable State Model for A4-Under-M4 Reasoning

---

## 1. Entity Types

| Entity | Description | Source |
|--------|-------------|--------|
| `population` | Collection of proto-cells in a shared resource pool | Book VI Gamma |
| `trait_axis` | A heritable, selectable feature dimension | Book VI Gamma §4 |
| `selection_landscape` | Multi-dimensional fitness surface over trait space | Book VI Gamma §7 |
| `enrichment_phase` | Temporal stage of adaptive dynamics | Book VIII Gamma §7 |
| `beneficial_variant` | A proto-cell with above-average trait values on one or more axes | Book VI Gamma |
| `multi_domain_coupling` | Non-additive fitness interaction between energetic, division, and lineage domains | Book VIII Gamma §5.3 |

---

## 2. Adaptive-Dynamics State Variables

| Variable | Type | Domain | Description |
|----------|------|--------|-------------|
| `a_level_unconditional` | enum | {A0, A1, A2, A3, A4, A5} | Current unconditional adaptive level |
| `a_level_conditional` | enum | {NONE, A3_PLUS, A4_CONDITIONAL} | Adaptive level under M4 backing |
| `landscape_dimensionality` | int | [0, ∞) | Number of independently selectable trait axes |
| `landscape_structure` | enum | {NONE, ADDITIVE, MULTI_DOMAIN_COUPLED} | Fitness-function structure |
| `gradient_strength_multiplier` | float | [0, ∞) | Gradient strength relative to A3 baseline (1.0 = A3) |
| `active_enrichment_generations` | int | [0, ∞) | Estimated generations of active directional enrichment |
| `enrichment_phases` | int | [1, ∞) | Number of distinct enrichment phases |
| `convergent` | bool | — | Whether dynamics plateau at a bounded optimum |
| `innovation_present` | bool | — | Whether qualitatively new functions emerge |
| `ecological_structure_present` | bool | — | Whether niches, gradients, frequency-dependence exist |

---

## 3. M4-Backing Fields

| Variable | Type | Domain | Description |
|----------|------|--------|-------------|
| `m_level_conditional` | enum | {M3, M4_CONDITIONAL} | Conditional metabolic level |
| `d_level_conditional` | enum | {D3, D4_CONDITIONAL} | Conditional division level |
| `l_level_conditional` | enum | {L3, L4_CONDITIONAL} | Conditional lineage level |
| `directed_fraction` | float | [0.0, 1.0] | Combined directed energetic fraction |
| `carrier_committed` | bool | — | Carrier bridge status |
| `dg_barrier_regime` | enum | {WEAK, MARGINAL, ROBUST} | Carrier barrier regime |

---

## 4. Trait / Gradient Fields

| Variable | Type | Domain | Description |
|----------|------|--------|-------------|
| `a3_axes` | list[str] | — | A3 trait axes: ["HIC_P1", "HIC_P2", "div_threshold", "assembly_eff"] |
| `m4_new_axes` | list[str] | — | M4-only axes: ["carrier_loading", "carrier_target_compat", "HIC_carrier_coupling"] |
| `total_axes` | int | — | len(a3_axes) + len(m4_new_axes) |
| `gradient_a3_baseline` | float | 1.0 | Normalized A3 gradient strength |
| `gradient_m4` | float | [1.0, ∞) | M4 gradient strength (~3–5 × baseline) |
| `coupling_depth` | enum | {NONE, ADDITIVE, WEAK_COUPLED, STRONG_COUPLED} | Fitness-function interaction depth |
| `optimum_status` | enum | {UNEXPLORED, APPROACHING, NEAR, AT_PLATEAU} | Population's position relative to optimum |

---

## 5. Transition Rules

### 5.1 A-Level Determination

```
IF m_level_conditional == M4_CONDITIONAL
   AND d_level_conditional == D4_CONDITIONAL
   AND l_level_conditional == L4_CONDITIONAL
   AND dg_barrier_regime == ROBUST
   AND carrier_committed == true:

   landscape_dimensionality = len(a3_axes) + len(m4_new_axes)  // 4 + 3 = 7
   gradient_strength_multiplier = directed_fraction / directed_fraction_m3  // ~3-5x
   landscape_structure = MULTI_DOMAIN_COUPLED
   active_enrichment_generations = 30-40
   enrichment_phases = 3  // convergence + carrier exploration + multi-domain coupling

   IF landscape_dimensionality >= 6
      AND gradient_strength_multiplier >= 2.5
      AND enrichment_phases >= 3
      AND landscape_structure == MULTI_DOMAIN_COUPLED:
      a_level_conditional = A4_CONDITIONAL
   ELIF gradient_strength_multiplier >= 2.0:
      a_level_conditional = A3_PLUS
   ELSE:
      a_level_conditional = NONE

ELSE:
   a_level_conditional = NONE
   landscape_dimensionality = len(a3_axes)  // 4
   gradient_strength_multiplier = 1.0
   landscape_structure = ADDITIVE
   active_enrichment_generations = 5-15
   enrichment_phases = 1

a_level_unconditional = A3  // always
convergent = true  // always (no innovation)
innovation_present = false  // always
ecological_structure_present = false  // always
```

### 5.2 Enrichment Phase Transitions

```
IF a_level_conditional == A4_CONDITIONAL:
   // Phase 1: rapid convergence on existing axes (gen 0-10)
   IF generation <= 10:
      enrichment_phase = RAPID_CONVERGENCE
      dominant_process = "A3 axes converge with amplified gradients"

   // Phase 2: carrier-axis exploration (gen 10-25)
   ELIF generation <= 25:
      enrichment_phase = CARRIER_EXPLORATION
      dominant_process = "Carrier-related trait optimization"

   // Phase 3: multi-domain coupling (gen 25-40)
   ELIF generation <= 40:
      enrichment_phase = MULTI_DOMAIN_COUPLING
      dominant_process = "Coordinated cross-domain optimization"

   // Phase 4: plateau
   ELSE:
      enrichment_phase = M4_PLATEAU
      dominant_process = "Convergence to M4 optimum"
      optimum_status = AT_PLATEAU
```

### 5.3 Fallback to M3

```
IF dg_barrier_regime != ROBUST:
   a_level_conditional = NONE
   landscape_dimensionality = len(a3_axes)  // revert to 4
   gradient_strength_multiplier = 1.0
   landscape_structure = ADDITIVE
   active_enrichment_generations = 5-15
   enrichment_phases = 1
   m4_new_axes = []  // carrier axes vanish
```

---

## 6. Fallback-Condition Fields

| Condition | Threshold | Effect on A-level |
|-----------|-----------|------------------|
| ΔG_barrier < 23 kT | Carrier non-functional | A4-conditional → A3 (full revert) |
| ΔG_barrier 23–28 kT | Carrier marginal | A4-conditional → A3+ (partial) |
| ΔG_barrier ≥ 28 kT | Carrier robust | A4-conditional justified |
| Directed fraction < 20% | Gradients only ~2× | A3+ at best |
| Directed fraction ≥ 30% | Gradients ~3–5× | A4-conditional |
| L4 half-life < 30 gen | Enrichment window truncated | A3+ (insufficient time for Phases 2–3) |
| L4 half-life ≥ 50 gen | Full enrichment window | A4-conditional |

---

## 7. Uncertainty / Fragility Fields

| Variable | Type | Value | Source |
|----------|------|-------|--------|
| `carrier_axis_count_uncertainty` | str | "±1 axis" | Exact number of carrier-related axes debatable |
| `gradient_multiplier_uncertainty` | str | "±1× around central estimate" | Depends on exact directed-fraction allocation |
| `enrichment_window_uncertainty` | str | "±10 generations" | Depends on carrier-axis landscape depth |
| `coupling_depth_quantified` | bool | false | Multi-domain coupling argued from mechanism, not computed |
| `innovation_remains_absent` | bool | true | No mechanism for qualitative novelty |
| `ecology_remains_absent` | bool | true | No niche, no environmental gradient |
| `a4_fragility` | enum | MODERATE | Carrier-dependent; landscape still convergent |
| `a4_to_a3_transition` | enum | SHARP | Binary: carrier works → A4; fails → A3 |

---

## 8. Verdict Fields

| Field | Value | Authority |
|-------|-------|----------|
| `a4_conditional_justified` | `CONDITIONAL` | Book VIII Gamma |
| `a4_unconditional_justified` | `NO` | Book VIII Gamma |
| `a5_open_ended_justified` | `NO` | Book VIII Gamma |
| `a4_qualifying_families` | `["B_plateau_shift", "C_multi_domain_coupling", "E_carrier_coopt"]` | Book VIII Gamma |
| `a4_strengthened_a3` | `["A_gradient_reinforcement", "D_retention"]` | Book VIII Gamma |
| `book_viii_gamma_changes_state` | `YES` | A4-conditional verified |
| `new_cost` | `0` | Twenty-sixth zero-cost target |
| `global_verdict` | `B` | M4 conditionally upgrades to A4-cond; unconditional A4 absent |

---

## 9. Minimal Serialized Example

```json
{
  "program_phase": "BOOK_VIII_GAMMA",
  "stage": "adaptive_dynamics_reassessment_under_M4",

  "a_level": {
    "unconditional": "A3",
    "conditional": "A4_CONDITIONAL",
    "a4_justified": "CONDITIONAL",
    "a4_unconditional": false,
    "a5_justified": false
  },

  "m4_backing": {
    "m_level_conditional": "M4_CONDITIONAL",
    "d_level_conditional": "D4_CONDITIONAL",
    "l_level_conditional": "L4_CONDITIONAL",
    "carrier_committed": true,
    "dg_barrier_regime": "ROBUST",
    "directed_fraction_m4": "0.30-0.34"
  },

  "landscape": {
    "a3_axes": ["HIC_P1_quality", "HIC_P2_quality", "division_threshold", "assembly_efficiency"],
    "m4_new_axes": ["carrier_loading_efficiency", "carrier_target_compatibility", "HIC_carrier_coupling"],
    "total_dimensionality": 7,
    "structure": "MULTI_DOMAIN_COUPLED",
    "gradient_multiplier": "3-5x",
    "convergent": true,
    "innovation": false,
    "ecology": false
  },

  "enrichment": {
    "active_window_a3_gen": "5-15",
    "active_window_a4_gen": "30-40",
    "phases": [
      {"phase": 1, "gen": "0-10", "process": "rapid_convergence_existing_axes"},
      {"phase": 2, "gen": "10-25", "process": "carrier_axis_exploration"},
      {"phase": 3, "gen": "25-40", "process": "multi_domain_coupling_optimization"},
      {"phase": 4, "gen": "40+", "process": "m4_plateau"}
    ],
    "genuinely_new_phases": [2, 3]
  },

  "routes": {
    "A_gradient_reinforcement": "strengthened_a3",
    "B_plateau_shift": "SURVIVES_a4_qualifying",
    "C_multi_domain_coupling": "SURVIVES_a4_qualifying",
    "D_retention": "strengthened_l4_contribution",
    "E_carrier_cooptimization": "SURVIVES_a4_qualifying",
    "F_pseudo": "disqualified_for_B_C_E"
  },

  "fragility": {
    "carrier_dependent": true,
    "innovation_absent": true,
    "ecology_absent": true,
    "still_convergent": true,
    "a4_fragility": "MODERATE",
    "fallback_regime": "A3_unconditional"
  },

  "cost": {
    "total_postulates": 15,
    "total_parameters": 9,
    "total_fields": 1,
    "total_dof": 6,
    "book_viii_gamma_added": {"postulates": 0, "parameters": 0},
    "zero_cost_targets": 26
  },

  "verdict": {
    "global": "B",
    "a4_conditional": "JUSTIFIED_CONDITIONAL",
    "a4_unconditional": "NOT_JUSTIFIED",
    "a5_open_ended": "NOT_JUSTIFIED",
    "state_change": true,
    "next_audit": "book_viii_terminal_capstone"
  }
}
```

---

## 10. Integration Notes

### 10.1 What GRUT-RAI Must Update from Book VIII Gamma

1. **A-level dual state formalized:** A3 unconditional / A4-conditional. Use A4-conditional for M4-regime reasoning; use A3 for fallback.
2. **A4-conditional verified, not merely projected.** Book VII Gamma §8 projected A3→A4-conditional. Book VIII Gamma verified through dedicated landscape analysis with route-by-route evaluation.
3. **Landscape inventory updated:** 6–7 axes (4 existing + 3 carrier-related); multi-domain coupled fitness function; ~30–40 gen active enrichment.
4. **Three enrichment phases identified:** rapid convergence, carrier exploration, multi-domain coupling.
5. **A4-qualifying families identified:** B (plateau shift / carrier frontier), C (multi-domain coupling), E (HIC/carrier co-optimization).
6. **Zero-cost target count:** 26.

### 10.2 What GRUT-RAI Must NOT Update

- No change to total cost (15/9/1/6)
- No change to carrier commitment (still provisional)
- No change to M-level (still M4-conditional / M3-unconditional)
- No change to D-level (still D4-conditional / D3-unconditional)
- No change to L-level (still L4-conditional / L3-unconditional)
- No promotion to unconditional A4
- No promotion to A5 / open-ended evolution
- No claim of innovation or ecological structure

### 10.3 Current Full Dual-State Scaffold

```
M4-conditional / M3-unconditional
D4-conditional / D3-unconditional
L4-conditional / L3-unconditional
A4-conditional / A3-unconditional
```

All four organizational levels have been reassessed under M4. Book VIII is complete pending terminal capstone.

---

*GRUT-RAI A4 State Model complete. Entity types, state variables, landscape fields, transition rules, fallback conditions, fragility fields, verdict fields, and minimal serialized example provided. A4-conditional verified. A3 retained as unconditional floor. Innovation and ecology remain absent.*
