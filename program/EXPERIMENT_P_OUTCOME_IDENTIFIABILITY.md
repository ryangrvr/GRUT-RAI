# EXPERIMENT P — Outcome-Selection Identifiability

Minimal closed model (s2 ⊗ a2 ⊗ eN), exact unitary measurement interaction.
Decoherence, definite outcome, and outcome weights evaluated as SEPARATE questions.

## Decision table

| question | result |
|---|---|
| closed dynamics yields decoherence | YES (exact) |
| decoherence yields definite outcome | NO |
| outcome weights uniquely determined by (C,G) | NO — STATE-DEPENDENT |
| Born weights derived | NO |
| outcome selection identifiable | NON-IDENTIFIABLE |
| depends on coarse-graining | outcome APPEARANCE depends on G (control F) |
| depends on partition | decoherence invariant; outcome question open in both |
| additional structure required | YES — a selection rule and/or probability postulate |

## Key control results

- Control A (decoherence): {"N=8": {"branch_cross_term_abs": 0.0, "offdiag_in_pointer_basis": 0.0, "purity_reduced": 0.5, "vn_entropy_reduced": 1.0, "decoherence": true, "global_state_purity": 1.0}, "N=64": {"branch_cross_term_abs": 0.0, "offdiag_in_pointer_basis": 0.0, "purity_reduced": 0.5, "vn_entropy_reduced": 1.0, "decoherence": true, "global_state_purity": 1.0}}
- Control B (outcome): {"global_state_purity": 1.0, "reduced_branch_populations": [0.5000000000000001, 0.4999999999999999], "global_state_is_single_outcome": false, "global_state_is_entangled_superposition": true, "definite_outcome": "NOT_DERIVED"}
- Control D (purifications): {"cases": [{"purification": "E0=|0>", "p0": 0.5000000000000001, "cross_term": 0.0, "env_e0_overlap_first_record_state": null}, {"purification": "E0=generic superposition", "p0": 0.5000000000000002, "cross_term": 0.16337142957077358, "env_e0_overlap_first_record_state": 0.0010487688392035945}], "identical_reduced_decoherence": false, "identical_global_states": false, "outcome_weight_identifiable_from_reduced_state_alone": true, "verdict": "NON-IDENTIFIABLE at the reduced level; weights are STATE-DEPENDENT (trace initial amplitudes), not dynamics-derived"}
- Control H (identifiability): {"pairs": [{"alpha2": 0.2, "decoherence_observables": {"cross": 0.0, "purity": 0.6799999999999999}, "outcome_weight_p0": 0.19999999999999998}, {"alpha2": 0.5, "decoherence_observables": {"cross": 0.0, "purity": 0.5}, "outcome_weight_p0": 0.5000000000000001}, {"alpha2": 0.8, "decoherence_observables": {"cross": 0.0, "purity": 0.6799999999999999}, "outcome_weight_p0": 0.7999999999999999}], "identical_decoherence_observables": true, "different_outcome_weights": true, "conclusion": "NON-IDENTIFIABLE: (C,G) fixed; initial-state amplitudes change outcome weights while decoherence observables are identical. Weights are carried by the initial state, not determined by closed dynamics + coarse-graining.", "verdict": "NON-IDENTIFIABLE"}

## Verdict

**PRIMARY:**
For the declared minimal closed model, closed unitary dynamics plus coarse-graining derive decoherence exactly but determine neither a definite outcome nor a unique outcome-weight law: outcome information is non-identifiable from the effective decoherence structure and is carried by the initial state.

**POSITIVE:**
Exact, artifact-verifiable demonstration that the closed model reproduces decoherence (cross term → 0) with zero stochastic/collapse input.

**NEGATIVE:**
Identical decoherence observables arise from initial states with different outcome weights (control H): outcome selection and Born weights are NON-IDENTIFIABLE from (C, G, decoherence observables).

**ADDITIONAL INPUT REQUIRED:**
An explicit outcome-selection rule and/or probability postulate (e.g. Born weights or a stochastic law) — an irreducible ADDITIONAL_INPUT for this model class.

**DOES NOT PROVE:**
It does not prove that no closed dynamics whatsoever can select outcomes; it establishes non-identifiability for the declared minimal identifiability model class.

sha256: `590a676e65006dff75adc9f8409820d284cfaeed90e231b2b5948ad0866b3e5c`
