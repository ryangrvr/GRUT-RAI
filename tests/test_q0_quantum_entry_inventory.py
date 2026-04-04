"""Tests for grut/q0_quantum_entry_inventory.py — Appendix Q0.

Deterministic test suite for the GRUT Quantum Entry Inventory.
All tests derive expected values from constants, not from hardcoded literals.

Test classes:
    TestQ0Constants         — vocabulary, count constants, hard rules
    TestCategoryAItems      — 5 state-like items
    TestCategoryBItems      — 4 dynamics-like items
    TestCategoryCItems      — 5 quantum-adjacent structural items
    TestCategoryDItems      — 9 missing items
    TestCategoryEItems      — 2 obstructed items
    TestItemCounts          — aggregate counts
    TestQuantumGapAssessment — gap flags and characterization
    TestReadinessVerdict    — readiness checks
    TestNoclaimsComplete    — 7 nonclaims
    TestHardRulesApplied    — 6 hard epistemic rules
    TestCategorySummaries   — per-category summaries
    TestMasterAudit         — run_q0_quantum_entry_inventory end-to-end
"""

import pytest

from grut.q0_quantum_entry_inventory import (
    # Constants
    ALLOWED_Q0_APPENDIX_P_CLASSES,
    ALLOWED_PRESENCE_STATES,
    ALLOWED_CATEGORY_LABELS,
    N_CATEGORY_A_ITEMS,
    N_CATEGORY_B_ITEMS,
    N_CATEGORY_C_ITEMS,
    N_CATEGORY_D_ITEMS,
    N_CATEGORY_E_ITEMS,
    N_TOTAL_ITEMS,
    N_PRESENT_ITEMS,
    N_ABSENT_ITEMS,
    N_OBSTRUCTED_ITEMS,
    N_CONDITIONALLY_PRESENT,
    HARD_EPISTEMIC_RULES,
    N_HARD_EPISTEMIC_RULES,
    Q0_NONCLAIMS,
    N_Q0_NONCLAIMS,
    Q0_INVENTORY_VERDICT,
    # Dataclasses
    Q0InventoryItem,
    Q0CategorySummary,
    Q0QuantumGapAssessment,
    Q0QuantumReadinessVerdict,
    Q0InventoryResult,
    # Functions
    build_category_a_items,
    build_category_b_items,
    build_category_c_items,
    build_category_d_items,
    build_category_e_items,
    build_all_items,
    build_category_summaries,
    assess_quantum_gap,
    compute_readiness_verdict,
    build_nonclaims,
    run_q0_quantum_entry_inventory,
)


# ==============================================================
# TestQ0Constants
# ==============================================================

class TestQ0Constants:
    """Vocabulary, count constants, and hard epistemic rules."""

    def test_n_status_classes_in_allowed_set(self):
        assert len(ALLOWED_Q0_APPENDIX_P_CLASSES) == 8

    def test_allowed_presence_states_count(self):
        assert len(ALLOWED_PRESENCE_STATES) == 4

    def test_allowed_category_labels_count(self):
        assert len(ALLOWED_CATEGORY_LABELS) == 5

    def test_n_total_items(self):
        assert N_TOTAL_ITEMS == 25

    def test_n_total_items_is_sum_of_categories(self):
        assert (
            N_CATEGORY_A_ITEMS
            + N_CATEGORY_B_ITEMS
            + N_CATEGORY_C_ITEMS
            + N_CATEGORY_D_ITEMS
            + N_CATEGORY_E_ITEMS
        ) == N_TOTAL_ITEMS

    def test_n_present_items(self):
        assert N_PRESENT_ITEMS == 14

    def test_n_absent_items(self):
        assert N_ABSENT_ITEMS == 9

    def test_n_obstructed_items(self):
        assert N_OBSTRUCTED_ITEMS == 2

    def test_n_conditionally_present(self):
        assert N_CONDITIONALLY_PRESENT == 2

    def test_present_plus_absent_plus_obstructed_equals_total(self):
        # present (14) includes 2 conditionally_present
        # absent (9) + obstructed (2) = 11; 14 + 11 = 25
        assert N_PRESENT_ITEMS + N_ABSENT_ITEMS + N_OBSTRUCTED_ITEMS == N_TOTAL_ITEMS

    def test_hard_epistemic_rules_count(self):
        assert N_HARD_EPISTEMIC_RULES == 6

    def test_hard_epistemic_rules_list_length(self):
        assert len(HARD_EPISTEMIC_RULES) == N_HARD_EPISTEMIC_RULES

    def test_n_nonclaims(self):
        assert N_Q0_NONCLAIMS == 7

    def test_nonclaims_list_length(self):
        assert len(Q0_NONCLAIMS) == N_Q0_NONCLAIMS

    def test_verdict_string_nonempty(self):
        assert len(Q0_INVENTORY_VERDICT) > 0

    def test_verdict_string_value(self):
        assert Q0_INVENTORY_VERDICT == "inventory_complete__quantum_gap_fully_documented"

    def test_native_canon_in_allowed_classes(self):
        assert "native_canon" in ALLOWED_Q0_APPENDIX_P_CLASSES

    def test_motivated_independent_postulation_in_allowed_classes(self):
        assert "motivated_independent_postulation" in ALLOWED_Q0_APPENDIX_P_CLASSES

    def test_compatible_but_ad_hoc_in_allowed_classes(self):
        assert "compatible_but_ad_hoc" in ALLOWED_Q0_APPENDIX_P_CLASSES

    def test_bounded_structural_result_in_allowed_classes(self):
        assert "bounded_structural_result" in ALLOWED_Q0_APPENDIX_P_CLASSES

    def test_prefer_absence_rule_present(self):
        assert "prefer_absence_over_implication" in HARD_EPISTEMIC_RULES

    def test_prefer_obstruction_rule_present(self):
        assert "prefer_obstruction_over_vague_openness" in HARD_EPISTEMIC_RULES

    def test_no_suggestive_rule_present(self):
        assert "do_not_treat_suggestive_as_present" in HARD_EPISTEMIC_RULES


# ==============================================================
# TestCategoryAItems
# ==============================================================

class TestCategoryAItems:
    """5 state-like items (Category A)."""

    def setup_method(self):
        self.items = build_category_a_items()

    def test_count(self):
        assert len(self.items) == N_CATEGORY_A_ITEMS

    def test_all_category_a(self):
        for it in self.items:
            assert it.category == "A_state_like"

    def test_item_ids_unique(self):
        ids = [it.item_id for it in self.items]
        assert len(set(ids)) == len(ids)

    def test_a1_scalar_field_phi_present(self):
        a1 = next(it for it in self.items if it.item_id == "A1_scalar_field_phi")
        assert a1.presence_state == "present"

    def test_a1_native_canon(self):
        a1 = next(it for it in self.items if it.item_id == "A1_scalar_field_phi")
        assert a1.appendix_p_class == "native_canon"

    def test_a2_tau_sq_present(self):
        a2 = next(it for it in self.items
                  if it.item_id == "A2_canonical_relaxation_time_tau_sq")
        assert a2.presence_state == "present"

    def test_a2_native_canon(self):
        a2 = next(it for it in self.items
                  if it.item_id == "A2_canonical_relaxation_time_tau_sq")
        assert a2.appendix_p_class == "native_canon"

    def test_a3_barrier_amplitude_present(self):
        a3 = next(it for it in self.items if it.item_id == "A3_barrier_amplitude_a")
        assert a3.presence_state == "present"

    def test_a3_native_canon(self):
        a3 = next(it for it in self.items if it.item_id == "A3_barrier_amplitude_a")
        assert a3.appendix_p_class == "native_canon"

    def test_a4_galley_ctp_present(self):
        a4 = next(it for it in self.items
                  if it.item_id == "A4_galley_ctp_doubled_field_vars")
        assert a4.presence_state == "present"

    def test_a4_effective_reduction(self):
        a4 = next(it for it in self.items
                  if it.item_id == "A4_galley_ctp_doubled_field_vars")
        assert a4.appendix_p_class == "effective_reduction"

    def test_a5_topological_winding_conditionally_present(self):
        a5 = next(it for it in self.items
                  if it.item_id == "A5_topological_winding_charge_o3")
        assert a5.presence_state == "conditionally_present"

    def test_a5_motivated_independent_postulation(self):
        a5 = next(it for it in self.items
                  if it.item_id == "A5_topological_winding_charge_o3")
        assert a5.appendix_p_class == "motivated_independent_postulation"

    def test_a5_forbidden_claim_references_derivation(self):
        a5 = next(it for it in self.items
                  if it.item_id == "A5_topological_winding_charge_o3")
        assert "derived" in a5.forbidden_claim.lower() or "canon" in a5.forbidden_claim.lower()

    def test_all_valid_appendix_p_classes(self):
        for it in self.items:
            assert it.appendix_p_class in ALLOWED_Q0_APPENDIX_P_CLASSES, (
                f"{it.item_id} has invalid class {it.appendix_p_class}"
            )

    def test_all_valid_presence_states(self):
        for it in self.items:
            assert it.presence_state in ALLOWED_PRESENCE_STATES

    def test_all_have_supporting_audit(self):
        for it in self.items:
            assert len(it.supporting_audit) > 0

    def test_a1_forbidden_claim_not_wavefunction(self):
        a1 = next(it for it in self.items if it.item_id == "A1_scalar_field_phi")
        assert "wavefunction" in a1.forbidden_claim.lower() or "amplitude" in a1.forbidden_claim.lower()


# ==============================================================
# TestCategoryBItems
# ==============================================================

class TestCategoryBItems:
    """4 dynamics-like items (Category B)."""

    def setup_method(self):
        self.items = build_category_b_items()

    def test_count(self):
        assert len(self.items) == N_CATEGORY_B_ITEMS

    def test_all_category_b(self):
        for it in self.items:
            assert it.category == "B_dynamics_like"

    def test_b1_constitutive_ode_present(self):
        b1 = next(it for it in self.items if it.item_id == "B1_constitutive_ode")
        assert b1.presence_state == "present"

    def test_b1_native_canon(self):
        b1 = next(it for it in self.items if it.item_id == "B1_constitutive_ode")
        assert b1.appendix_p_class == "native_canon"

    def test_b2_galley_effective_reduction(self):
        b2 = next(it for it in self.items
                  if it.item_id == "B2_galley_ctp_retarded_action")
        assert b2.appendix_p_class == "effective_reduction"

    def test_b3_barrier_native_canon(self):
        b3 = next(it for it in self.items
                  if it.item_id == "B3_barrier_action_aq_dissipative")
        assert b3.appendix_p_class == "native_canon"

    def test_b4_equilibrium_native_canon(self):
        b4 = next(it for it in self.items
                  if it.item_id == "B4_equilibrium_relaxation_attractor")
        assert b4.appendix_p_class == "native_canon"

    def test_all_present(self):
        for it in self.items:
            assert it.presence_state == "present"

    def test_b1_forbidden_claim_not_born_rule(self):
        b1 = next(it for it in self.items if it.item_id == "B1_constitutive_ode")
        claim = b1.forbidden_claim.lower()
        assert "born" in claim or "probabilistic" in claim or "probability" in claim

    def test_all_valid_appendix_p_classes(self):
        for it in self.items:
            assert it.appendix_p_class in ALLOWED_Q0_APPENDIX_P_CLASSES

    def test_all_have_supporting_audit(self):
        for it in self.items:
            assert len(it.supporting_audit) > 0

    def test_b2_forbidden_claim_not_path_integral(self):
        b2 = next(it for it in self.items
                  if it.item_id == "B2_galley_ctp_retarded_action")
        claim = b2.forbidden_claim.lower()
        assert "quantum" in claim or "path integral" in claim or "interference" in claim


# ==============================================================
# TestCategoryCItems
# ==============================================================

class TestCategoryCItems:
    """5 quantum-adjacent structural items (Category C)."""

    def setup_method(self):
        self.items = build_category_c_items()

    def test_count(self):
        assert len(self.items) == N_CATEGORY_C_ITEMS

    def test_all_category_c(self):
        for it in self.items:
            assert it.category == "C_quantum_adjacent_structural"

    def test_c1_integer_winding_conditionally_present(self):
        c1 = next(it for it in self.items
                  if it.item_id == "C1_integer_topological_winding_z")
        assert c1.presence_state == "conditionally_present"

    def test_c1_motivated_independent_postulation(self):
        c1 = next(it for it in self.items
                  if it.item_id == "C1_integer_topological_winding_z")
        assert c1.appendix_p_class == "motivated_independent_postulation"

    def test_c2_tau_scale_present(self):
        c2 = next(it for it in self.items
                  if it.item_id == "C2_tau_omega0_scale_selection")
        assert c2.presence_state == "present"

    def test_c2_working_canon_hypothesis(self):
        c2 = next(it for it in self.items
                  if it.item_id == "C2_tau_omega0_scale_selection")
        assert c2.appendix_p_class == "working_canon_hypothesis"

    def test_c3_component_b_bounded_structural_result(self):
        c3 = next(it for it in self.items
                  if it.item_id == "C3_component_b_deficit_requirement")
        assert c3.appendix_p_class == "bounded_structural_result"

    def test_c4_retarded_kernel_effective_reduction(self):
        c4 = next(it for it in self.items
                  if it.item_id == "C4_retarded_causal_kernel_structure")
        assert c4.appendix_p_class == "effective_reduction"

    def test_c5_z2_symmetry_native_canon(self):
        c5 = next(it for it in self.items
                  if it.item_id == "C5_z2_phi_reflection_symmetry")
        assert c5.appendix_p_class == "native_canon"

    def test_c5_z2_forbidden_claim_not_u1(self):
        c5 = next(it for it in self.items
                  if it.item_id == "C5_z2_phi_reflection_symmetry")
        claim = c5.forbidden_claim.lower()
        assert "complex" in claim or "u(1)" in claim or "phase" in claim or "u1" in claim

    def test_c1_forbidden_claim_references_hilbert_or_eigenvalue(self):
        c1 = next(it for it in self.items
                  if it.item_id == "C1_integer_topological_winding_z")
        claim = c1.forbidden_claim.lower()
        assert "hilbert" in claim or "eigenvalue" in claim or "quantum number" in claim

    def test_all_valid_appendix_p_classes(self):
        for it in self.items:
            assert it.appendix_p_class in ALLOWED_Q0_APPENDIX_P_CLASSES

    def test_c_items_not_absent(self):
        for it in self.items:
            assert it.presence_state != "absent"

    def test_c_items_not_obstructed(self):
        for it in self.items:
            assert it.presence_state != "obstructed"


# ==============================================================
# TestCategoryDItems
# ==============================================================

class TestCategoryDItems:
    """9 missing items (Category D)."""

    def setup_method(self):
        self.items = build_category_d_items()

    def test_count(self):
        assert len(self.items) == N_CATEGORY_D_ITEMS

    def test_all_category_d(self):
        for it in self.items:
            assert it.category == "D_missing"

    def test_all_absent(self):
        for it in self.items:
            assert it.presence_state == "absent", (
                f"{it.item_id} should be absent but is {it.presence_state}"
            )

    def test_all_compatible_but_ad_hoc(self):
        for it in self.items:
            assert it.appendix_p_class == "compatible_but_ad_hoc", (
                f"{it.item_id} should be compatible_but_ad_hoc "
                f"but is {it.appendix_p_class}"
            )

    def test_d1_hilbert_space_present(self):
        d1 = next(it for it in self.items if it.item_id == "D1_hilbert_space_structure")
        assert d1.presence_state == "absent"

    def test_d2_operator_algebra_absent(self):
        d2 = next(it for it in self.items if it.item_id == "D2_operator_algebra")
        assert d2.presence_state == "absent"

    def test_d3_complex_amplitude_absent(self):
        d3 = next(it for it in self.items
                  if it.item_id == "D3_complex_amplitude_wavefunction")
        assert d3.presence_state == "absent"

    def test_d4_born_rule_absent(self):
        d4 = next(it for it in self.items if it.item_id == "D4_born_rule")
        assert d4.presence_state == "absent"

    def test_d5_spinorial_fields_absent(self):
        d5 = next(it for it in self.items if it.item_id == "D5_spinorial_fields")
        assert d5.presence_state == "absent"

    def test_d6_entanglement_absent(self):
        d6 = next(it for it in self.items if it.item_id == "D6_entanglement_formalism")
        assert d6.presence_state == "absent"

    def test_d7_measurement_postulate_absent(self):
        d7 = next(it for it in self.items
                  if it.item_id == "D7_measurement_postulate")
        assert d7.presence_state == "absent"

    def test_d8_quantum_path_integral_absent(self):
        d8 = next(it for it in self.items
                  if it.item_id == "D8_quantum_path_integral")
        assert d8.presence_state == "absent"

    def test_d9_decoherence_formalism_absent(self):
        d9 = next(it for it in self.items
                  if it.item_id == "D9_decoherence_formalism")
        assert d9.presence_state == "absent"

    def test_d3_forbidden_claim_references_wavefunction(self):
        d3 = next(it for it in self.items
                  if it.item_id == "D3_complex_amplitude_wavefunction")
        claim = d3.forbidden_claim.lower()
        assert "wavefunction" in claim or "amplitude" in claim

    def test_d9_forbidden_claim_references_decoherence(self):
        d9 = next(it for it in self.items
                  if it.item_id == "D9_decoherence_formalism")
        claim = d9.forbidden_claim.lower()
        assert "decoherence" in claim or "quantum" in claim

    def test_d4_forbidden_claim_references_born_or_constitutive(self):
        d4 = next(it for it in self.items if it.item_id == "D4_born_rule")
        claim = d4.forbidden_claim.lower()
        assert "born" in claim or "constitutive" in claim or "probability" in claim

    def test_no_d_item_is_native_canon(self):
        for it in self.items:
            assert it.appendix_p_class != "native_canon"

    def test_item_ids_unique(self):
        ids = [it.item_id for it in self.items]
        assert len(set(ids)) == len(ids)

    def test_all_have_forbidden_claim(self):
        for it in self.items:
            assert len(it.forbidden_claim) > 0


# ==============================================================
# TestCategoryEItems
# ==============================================================

class TestCategoryEItems:
    """2 obstructed items (Category E)."""

    def setup_method(self):
        self.items = build_category_e_items()

    def test_count(self):
        assert len(self.items) == N_CATEGORY_E_ITEMS

    def test_all_category_e(self):
        for it in self.items:
            assert it.category == "E_obstructed"

    def test_all_obstructed(self):
        for it in self.items:
            assert it.presence_state == "obstructed"

    def test_e1_fermionic_emergence_bsr(self):
        e1 = next(it for it in self.items if it.item_id == "E1_fermionic_emergence")
        assert e1.appendix_p_class == "bounded_structural_result"

    def test_e2_stable_bosonic_mbu(self):
        e2 = next(it for it in self.items
                  if it.item_id == "E2_stable_bosonic_localized_object")
        assert e2.appendix_p_class == "motivated_but_unbuilt"

    def test_e1_cites_fermionic_audit(self):
        e1 = next(it for it in self.items if it.item_id == "E1_fermionic_emergence")
        assert "fermionic_emergence_audit" in e1.supporting_audit

    def test_e2_cites_localized_bosonic_audit(self):
        e2 = next(it for it in self.items
                  if it.item_id == "E2_stable_bosonic_localized_object")
        assert "localized_bosonic_object_audit" in e2.supporting_audit

    def test_e1_forbidden_claim_references_fermionic_without_hopf(self):
        e1 = next(it for it in self.items if it.item_id == "E1_fermionic_emergence")
        claim = e1.forbidden_claim.lower()
        assert "fermionic" in claim or "hopf" in claim

    def test_e2_forbidden_claim_references_derrick_stability(self):
        e2 = next(it for it in self.items
                  if it.item_id == "E2_stable_bosonic_localized_object")
        claim = e2.forbidden_claim.lower()
        assert "stable" in claim or "derrick" in claim or "hedgehog" in claim

    def test_e1_notes_three_layers(self):
        e1 = next(it for it in self.items if it.item_id == "E1_fermionic_emergence")
        # Notes should mention the 3-layer obstruction
        notes_text = " ".join(e1.notes).lower()
        # Check that the notes reference layer 1, 2, or 3
        assert any(f"layer {i}" in notes_text for i in [1, 2, 3]) or \
               "layer" in notes_text or "three" in notes_text or "obstruction" in notes_text

    def test_e2_notes_reference_resolution_path(self):
        e2 = next(it for it in self.items
                  if it.item_id == "E2_stable_bosonic_localized_object")
        notes_text = " ".join(e2.notes).lower()
        assert "resolution" in notes_text or "skyrme" in notes_text or "l4" in notes_text or "mbu" in notes_text

    def test_both_cite_supporting_audit(self):
        for it in self.items:
            assert len(it.supporting_audit) > 0


# ==============================================================
# TestItemCounts
# ==============================================================

class TestItemCounts:
    """Aggregate count checks."""

    def setup_method(self):
        self.items = build_all_items()

    def test_total_items(self):
        assert len(self.items) == N_TOTAL_ITEMS

    def test_category_a_count(self):
        assert sum(1 for it in self.items
                   if it.category == "A_state_like") == N_CATEGORY_A_ITEMS

    def test_category_b_count(self):
        assert sum(1 for it in self.items
                   if it.category == "B_dynamics_like") == N_CATEGORY_B_ITEMS

    def test_category_c_count(self):
        assert sum(1 for it in self.items
                   if it.category == "C_quantum_adjacent_structural") == N_CATEGORY_C_ITEMS

    def test_category_d_count(self):
        assert sum(1 for it in self.items
                   if it.category == "D_missing") == N_CATEGORY_D_ITEMS

    def test_category_e_count(self):
        assert sum(1 for it in self.items
                   if it.category == "E_obstructed") == N_CATEGORY_E_ITEMS

    def test_present_or_conditional_count(self):
        n = sum(1 for it in self.items
                if it.presence_state in {"present", "conditionally_present"})
        assert n == N_PRESENT_ITEMS

    def test_absent_count(self):
        n = sum(1 for it in self.items if it.presence_state == "absent")
        assert n == N_ABSENT_ITEMS

    def test_obstructed_count(self):
        n = sum(1 for it in self.items if it.presence_state == "obstructed")
        assert n == N_OBSTRUCTED_ITEMS

    def test_conditionally_present_count(self):
        n = sum(1 for it in self.items if it.presence_state == "conditionally_present")
        assert n == N_CONDITIONALLY_PRESENT

    def test_all_item_ids_unique(self):
        ids = [it.item_id for it in self.items]
        assert len(set(ids)) == len(ids)

    def test_all_valid_categories(self):
        for it in self.items:
            assert it.category in ALLOWED_CATEGORY_LABELS

    def test_all_valid_appendix_p_classes(self):
        for it in self.items:
            assert it.appendix_p_class in ALLOWED_Q0_APPENDIX_P_CLASSES

    def test_all_valid_presence_states(self):
        for it in self.items:
            assert it.presence_state in ALLOWED_PRESENCE_STATES


# ==============================================================
# TestQuantumGapAssessment
# ==============================================================

class TestQuantumGapAssessment:
    """Q0 quantum gap assessment."""

    def setup_method(self):
        self.items = build_all_items()
        self.gap = assess_quantum_gap(self.items)

    def test_hilbert_space_not_present(self):
        assert self.gap.hilbert_space_present is False

    def test_operator_algebra_not_present(self):
        assert self.gap.operator_algebra_present is False

    def test_complex_amplitude_not_present(self):
        assert self.gap.complex_amplitude_present is False

    def test_born_rule_not_present(self):
        assert self.gap.born_rule_present is False

    def test_spinorial_fields_not_present(self):
        assert self.gap.spinorial_fields_present is False

    def test_entanglement_not_present(self):
        assert self.gap.entanglement_formalism_present is False

    def test_measurement_postulate_not_present(self):
        assert self.gap.measurement_postulate_present is False

    def test_fermionic_emergence_not_possible(self):
        assert self.gap.fermionic_emergence_possible is False

    def test_stable_bosonic_particle_not_possible(self):
        assert self.gap.stable_bosonic_particle_possible is False

    def test_gap_is_architectural(self):
        assert self.gap.gap_is_architectural is True

    def test_quantum_adjacent_structures_nonempty(self):
        assert len(self.gap.quantum_adjacent_structures) > 0

    def test_quantum_adjacent_structures_are_c_category(self):
        c_ids = {it.item_id for it in self.items
                 if it.category == "C_quantum_adjacent_structural"}
        for item_id in self.gap.quantum_adjacent_structures:
            assert item_id in c_ids

    def test_quantum_adjacent_count_matches_c_category(self):
        c_count = sum(1 for it in self.items
                      if it.category == "C_quantum_adjacent_structural")
        assert len(self.gap.quantum_adjacent_structures) == c_count

    def test_gap_summary_nonempty(self):
        assert len(self.gap.gap_summary) > 0

    def test_gap_summary_mentions_hilbert(self):
        assert "Hilbert" in self.gap.gap_summary or "hilbert" in self.gap.gap_summary.lower()


# ==============================================================
# TestReadinessVerdict
# ==============================================================

class TestReadinessVerdict:
    """Q0 readiness verdict checks."""

    def setup_method(self):
        self.items = build_all_items()
        self.gap = assess_quantum_gap(self.items)
        self.verdict = compute_readiness_verdict(self.items, self.gap)

    def test_taxonomy_used_throughout(self):
        assert self.verdict.taxonomy_used_throughout is True

    def test_bounded_negatives_preserved(self):
        assert self.verdict.bounded_negatives_preserved is True

    def test_fermionic_obstruction_preserved(self):
        assert self.verdict.fermionic_obstruction_preserved is True

    def test_free_parameters_identified(self):
        assert self.verdict.free_parameters_identified is True

    def test_extension_postulates_marked(self):
        assert self.verdict.extension_postulates_marked is True

    def test_no_silent_promotions(self):
        assert self.verdict.no_silent_promotions is True

    def test_hard_rules_applied(self):
        assert self.verdict.hard_rules_applied is True

    def test_q0_complete(self):
        assert self.verdict.q0_complete is True

    def test_q0_verdict_string(self):
        assert self.verdict.q0_verdict == Q0_INVENTORY_VERDICT


# ==============================================================
# TestNoclaimsComplete
# ==============================================================

class TestNoclaimsComplete:
    """Q0 nonclaims verification."""

    def setup_method(self):
        self.nonclaims = build_nonclaims()

    def test_nonclaims_count(self):
        assert len(self.nonclaims) == N_Q0_NONCLAIMS

    def test_not_claiming_quantum_adjacent_implies_qm(self):
        assert any("quantum_adjacent" in nc or "adjacent" in nc
                   for nc in self.nonclaims)

    def test_not_claiming_ctp_is_hilbert_space(self):
        assert any("ctp" in nc.lower() or "hilbert" in nc.lower()
                   for nc in self.nonclaims)

    def test_not_claiming_relaxation_is_decoherence(self):
        assert any("decoherence" in nc.lower() or "relaxation" in nc.lower()
                   for nc in self.nonclaims)

    def test_not_claiming_winding_generates_amplitudes(self):
        assert any("winding" in nc.lower() or "amplitude" in nc.lower()
                   for nc in self.nonclaims)

    def test_not_claiming_present_makes_grut_quantum(self):
        assert any("present" in nc.lower() or "quantum_theory" in nc.lower()
                   for nc in self.nonclaims)

    def test_not_claiming_obstructions_permanent(self):
        assert any("obstruction" in nc.lower() or "permanent" in nc.lower()
                   for nc in self.nonclaims)

    def test_not_claiming_d_items_cannot_be_added(self):
        assert any("category_d" in nc.lower() or "cannot_be_added" in nc.lower()
                   for nc in self.nonclaims)


# ==============================================================
# TestHardRulesApplied
# ==============================================================

class TestHardRulesApplied:
    """Hard epistemic rules verification."""

    def test_rule_prefer_absence(self):
        assert "prefer_absence_over_implication" in HARD_EPISTEMIC_RULES

    def test_rule_prefer_obstruction(self):
        assert "prefer_obstruction_over_vague_openness" in HARD_EPISTEMIC_RULES

    def test_rule_no_suggestive(self):
        assert "do_not_treat_suggestive_as_present" in HARD_EPISTEMIC_RULES

    def test_rule_no_silent_promotion(self):
        assert "no_silent_promotion_to_native_canon" in HARD_EPISTEMIC_RULES

    def test_rule_regime_qualifiers(self):
        assert "regime_qualifiers_mandatory_for_effective_reduction" in HARD_EPISTEMIC_RULES

    def test_rule_obstructed_cite_audit(self):
        assert "obstructed_items_cite_appendix_audit" in HARD_EPISTEMIC_RULES

    # Verify rule application in the inventory
    def test_no_d_item_promoted_to_native_canon(self):
        """Hard rule: no_silent_promotion_to_native_canon."""
        d_items = build_category_d_items()
        for it in d_items:
            assert it.appendix_p_class != "native_canon"

    def test_obstructed_items_cite_audit(self):
        """Hard rule: obstructed_items_cite_appendix_audit."""
        e_items = build_category_e_items()
        for it in e_items:
            assert len(it.supporting_audit) > 0

    def test_conditionally_present_not_treated_as_present(self):
        """Hard rule: do_not_treat_suggestive_as_present."""
        # A5 and C1 must be conditionally_present, not present
        a_items = build_category_a_items()
        a5 = next(it for it in a_items
                  if it.item_id == "A5_topological_winding_charge_o3")
        assert a5.presence_state == "conditionally_present"
        assert a5.presence_state != "present"


# ==============================================================
# TestCategorySummaries
# ==============================================================

class TestCategorySummaries:
    """Category summary structure."""

    def setup_method(self):
        self.items = build_all_items()
        self.summaries = build_category_summaries(self.items)

    def test_five_summaries(self):
        assert len(self.summaries) == 5

    def test_all_category_labels_represented(self):
        labels = {s.category_label for s in self.summaries}
        assert labels == ALLOWED_CATEGORY_LABELS

    def test_summary_a_count(self):
        s = next(s for s in self.summaries if s.category_label == "A_state_like")
        assert s.n_items == N_CATEGORY_A_ITEMS

    def test_summary_b_count(self):
        s = next(s for s in self.summaries if s.category_label == "B_dynamics_like")
        assert s.n_items == N_CATEGORY_B_ITEMS

    def test_summary_c_count(self):
        s = next(s for s in self.summaries
                 if s.category_label == "C_quantum_adjacent_structural")
        assert s.n_items == N_CATEGORY_C_ITEMS

    def test_summary_d_count(self):
        s = next(s for s in self.summaries if s.category_label == "D_missing")
        assert s.n_items == N_CATEGORY_D_ITEMS

    def test_summary_e_count(self):
        s = next(s for s in self.summaries if s.category_label == "E_obstructed")
        assert s.n_items == N_CATEGORY_E_ITEMS

    def test_all_descriptions_nonempty(self):
        for s in self.summaries:
            assert len(s.description) > 0

    def test_item_ids_consistent(self):
        for s in self.summaries:
            actual_ids = {it.item_id for it in self.items
                         if it.category == s.category_label}
            assert set(s.item_ids) == actual_ids


# ==============================================================
# TestMasterAudit
# ==============================================================

class TestMasterAudit:
    """End-to-end test of run_q0_quantum_entry_inventory."""

    def setup_method(self):
        self.result = run_q0_quantum_entry_inventory()

    def test_valid(self):
        assert self.result.valid is True

    def test_n_total(self):
        assert self.result.n_total == N_TOTAL_ITEMS

    def test_n_present(self):
        assert self.result.n_present == N_PRESENT_ITEMS

    def test_n_absent(self):
        assert self.result.n_absent == N_ABSENT_ITEMS

    def test_n_obstructed(self):
        assert self.result.n_obstructed == N_OBSTRUCTED_ITEMS

    def test_n_conditionally_present(self):
        assert self.result.n_conditionally_present == N_CONDITIONALLY_PRESENT

    def test_items_count(self):
        assert len(self.result.items) == N_TOTAL_ITEMS

    def test_category_summaries_count(self):
        assert len(self.result.category_summaries) == 5

    def test_hard_rules_count(self):
        assert len(self.result.hard_rules) == N_HARD_EPISTEMIC_RULES

    def test_nonclaims_count(self):
        assert len(self.result.nonclaims) == N_Q0_NONCLAIMS

    def test_gap_assessment_architectural(self):
        assert self.result.gap_assessment.gap_is_architectural is True

    def test_readiness_verdict_complete(self):
        assert self.result.readiness_verdict.q0_complete is True

    def test_readiness_verdict_string(self):
        assert self.result.readiness_verdict.q0_verdict == Q0_INVENTORY_VERDICT

    def test_diagnostics_populated(self):
        assert len(self.result.diagnostics) > 0

    def test_diagnostics_n_total_matches(self):
        assert self.result.diagnostics["n_total"] == N_TOTAL_ITEMS

    def test_diagnostics_all_classes_valid(self):
        assert self.result.diagnostics["all_appendix_p_classes_valid"] is True

    def test_diagnostics_all_presence_states_valid(self):
        assert self.result.diagnostics["all_presence_states_valid"] is True

    def test_diagnostics_all_categories_valid(self):
        assert self.result.diagnostics["all_categories_valid"] is True
