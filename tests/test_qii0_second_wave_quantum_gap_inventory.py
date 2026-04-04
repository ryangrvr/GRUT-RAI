"""
Tests for Appendix Q-II.0 --- Second-Wave Quantum Gap Inventory
===============================================================
"""

import pytest

from grut.qii0_second_wave_quantum_gap_inventory import (
    TAU_SQ, TAU, GAMMA,
    ALLOWED_PRESENCE_STATES, ALLOWED_APPENDIX_P_CLASSES, ALLOWED_CATEGORY_LABELS,
    N_CATEGORY_A_ITEMS, N_CATEGORY_B_ITEMS, N_CATEGORY_C_ITEMS,
    N_CATEGORY_D_ITEMS, N_CATEGORY_E_ITEMS, N_CATEGORY_F_ITEMS,
    N_TOTAL_ITEMS, N_QII0_NONCLAIMS, N_HARD_RULES,
    QF_INHERITED_AUTHORIZATION,
    QII0_INVENTORY_VERDICT, HARD_EPISTEMIC_RULES, QII0_NONCLAIMS,
    run_qii0_second_wave_gap_inventory, _self_test,
)


@pytest.fixture(scope="module")
def result():
    return run_qii0_second_wave_gap_inventory()


# ===========================================================================
# TestQII0Constants
# ===========================================================================

class TestQII0Constants:
    def test_n_total_items(self):
        assert N_TOTAL_ITEMS == 29

    def test_category_sum_equals_total(self):
        s = N_CATEGORY_A_ITEMS + N_CATEGORY_B_ITEMS + N_CATEGORY_C_ITEMS + \
            N_CATEGORY_D_ITEMS + N_CATEGORY_E_ITEMS + N_CATEGORY_F_ITEMS
        assert s == N_TOTAL_ITEMS

    def test_n_nonclaims(self):
        assert N_QII0_NONCLAIMS == 8

    def test_n_hard_rules(self):
        assert N_HARD_RULES == 7

    def test_hard_rules_length(self):
        assert len(HARD_EPISTEMIC_RULES) == N_HARD_RULES

    def test_nonclaims_length(self):
        assert len(QII0_NONCLAIMS) == N_QII0_NONCLAIMS

    def test_all_nonclaims_start_with_not_claiming(self):
        for nc in QII0_NONCLAIMS:
            assert nc.startswith("NOT_claiming_")

    def test_qf_inherited_authorization(self):
        assert QF_INHERITED_AUTHORIZATION == "authorized_to_close_first_wave_quantum_program"

    def test_inventory_verdict_string(self):
        assert "gap_inventory_complete" in QII0_INVENTORY_VERDICT

    def test_allowed_presence_states_size(self):
        assert len(ALLOWED_PRESENCE_STATES) == 5

    def test_allowed_appendix_p_classes_size(self):
        assert len(ALLOWED_APPENDIX_P_CLASSES) == 8

    def test_allowed_category_labels_size(self):
        assert len(ALLOWED_CATEGORY_LABELS) == 6


# ===========================================================================
# TestCategoryAItems
# ===========================================================================

class TestCategoryAItems:
    def test_count(self, result):
        cat_a = [it for it in result.items if it.category == "A_composite_state"]
        assert len(cat_a) == N_CATEGORY_A_ITEMS

    def test_a1_tensor_product(self, result):
        a1 = [it for it in result.items if it.item_id == "A1"][0]
        assert a1.presence_state == "absent"
        assert "tensor" in a1.item_name.lower()

    def test_a2_subsystem(self, result):
        a2 = [it for it in result.items if it.item_id == "A2"][0]
        assert a2.presence_state == "absent"

    def test_a3_reduced_state(self, result):
        a3 = [it for it in result.items if it.item_id == "A3"][0]
        assert a3.presence_state == "absent"

    def test_a4_many_body(self, result):
        a4 = [it for it in result.items if it.item_id == "A4"][0]
        assert a4.presence_state == "absent"

    def test_all_a_absent(self, result):
        cat_a = [it for it in result.items if it.category == "A_composite_state"]
        for it in cat_a:
            assert it.presence_state == "absent"


# ===========================================================================
# TestCategoryBItems
# ===========================================================================

class TestCategoryBItems:
    def test_count(self, result):
        cat_b = [it for it in result.items if it.category == "B_entanglement"]
        assert len(cat_b) == N_CATEGORY_B_ITEMS

    def test_b1_nonfactorized(self, result):
        b1 = [it for it in result.items if it.item_id == "B1"][0]
        assert b1.presence_state == "absent"

    def test_b5_entanglement_route(self, result):
        b5 = [it for it in result.items if it.item_id == "B5"][0]
        assert b5.presence_state == "absent"
        assert b5.appendix_p_class == "bounded_structural_result"

    def test_no_entanglement_hint(self, result):
        cat_b = [it for it in result.items if it.category == "B_entanglement"]
        for it in cat_b:
            assert it.presence_state in ("absent",)

    def test_b4_bell_chsh(self, result):
        b4 = [it for it in result.items if it.item_id == "B4"][0]
        assert "bell" in b4.item_name.lower() or "chsh" in b4.item_name.lower()


# ===========================================================================
# TestCategoryCItems
# ===========================================================================

class TestCategoryCItems:
    def test_count(self, result):
        cat_c = [it for it in result.items if it.category == "C_observable_algebra"]
        assert len(cat_c) == N_CATEGORY_C_ITEMS

    def test_c1_multi_observable(self, result):
        c1 = [it for it in result.items if it.item_id == "C1"][0]
        assert c1.presence_state == "absent"
        assert "QE3" in c1.supporting_audit

    def test_c2_noncommuting(self, result):
        c2 = [it for it in result.items if it.item_id == "C2"][0]
        assert c2.presence_state == "absent"

    def test_all_c_absent(self, result):
        cat_c = [it for it in result.items if it.category == "C_observable_algebra"]
        for it in cat_c:
            assert it.presence_state == "absent"


# ===========================================================================
# TestCategoryDItems
# ===========================================================================

class TestCategoryDItems:
    def test_count(self, result):
        cat_d = [it for it in result.items if it.category == "D_excitation_field_mode"]
        assert len(cat_d) == N_CATEGORY_D_ITEMS

    def test_d5_toy_level_limitation(self, result):
        d5 = [it for it in result.items if it.item_id == "D5"][0]
        assert d5.presence_state == "first_wave_established"
        assert d5.appendix_p_class == "bounded_structural_result"

    def test_d4_not_ladder_operator(self, result):
        d4 = [it for it in result.items if it.item_id == "D4"][0]
        assert d4.presence_state == "absent"
        # Notes should clarify L is dissipative not ladder
        notes_text = " ".join(d4.notes).lower()
        assert "dissipat" in notes_text or "not" in notes_text


# ===========================================================================
# TestCategoryEItems
# ===========================================================================

class TestCategoryEItems:
    def test_count(self, result):
        cat_e = [it for it in result.items if it.category == "E_probability_determination"]
        assert len(cat_e) == N_CATEGORY_E_ITEMS

    def test_e1_born_rule(self, result):
        e1 = [it for it in result.items if it.item_id == "E1"][0]
        assert e1.presence_state == "absent"
        assert e1.appendix_p_class == "bounded_structural_result"

    def test_e5_effective_tendency(self, result):
        e5 = [it for it in result.items if it.item_id == "E5"][0]
        assert e5.presence_state == "extension_level"
        assert e5.appendix_p_class == "motivated_but_unbuilt"

    def test_born_rule_distinct_from_decoherence(self, result):
        e1 = [it for it in result.items if it.item_id == "E1"][0]
        assert "decoherence" in e1.forbidden_claim.lower() or \
               "pointer" in e1.forbidden_claim.lower()


# ===========================================================================
# TestCategoryFItems
# ===========================================================================

class TestCategoryFItems:
    def test_count(self, result):
        cat_f = [it for it in result.items if it.category == "F_matter_readiness"]
        assert len(cat_f) == N_CATEGORY_F_ITEMS

    def test_f2_fermionic_obstructed(self, result):
        f2 = [it for it in result.items if it.item_id == "F2"][0]
        assert f2.presence_state == "obstructed"
        assert f2.appendix_p_class == "bounded_structural_result"

    def test_f1_bosonic(self, result):
        f1 = [it for it in result.items if it.item_id == "F1"][0]
        assert f1.presence_state == "absent"

    def test_f5_appendix_r_handoff(self, result):
        f5 = [it for it in result.items if it.item_id == "F5"][0]
        assert f5.presence_state == "absent"
        assert "appendix_r" in f5.item_name.lower() or "handoff" in f5.item_name.lower()


# ===========================================================================
# TestItemCounts
# ===========================================================================

class TestItemCounts:
    def test_total_items(self, result):
        assert result.n_total == N_TOTAL_ITEMS

    def test_items_list_length(self, result):
        assert len(result.items) == N_TOTAL_ITEMS

    def test_n_absent(self, result):
        counted = sum(1 for it in result.items if it.presence_state == "absent")
        assert counted == result.n_absent

    def test_n_obstructed(self, result):
        counted = sum(1 for it in result.items if it.presence_state == "obstructed")
        assert counted == result.n_obstructed
        assert counted == 1  # only F2

    def test_n_extension_level(self, result):
        counted = sum(1 for it in result.items if it.presence_state == "extension_level")
        assert counted == result.n_extension_level
        assert counted == 1  # only E5

    def test_n_first_wave_established(self, result):
        counted = sum(1 for it in result.items if it.presence_state == "first_wave_established")
        assert counted == result.n_first_wave_established
        assert counted == 1  # only D5

    def test_counts_sum_to_total(self, result):
        s = result.n_absent + result.n_obstructed + result.n_extension_level + \
            result.n_first_wave_established
        assert s == result.n_total

    def test_unique_item_ids(self, result):
        ids = [it.item_id for it in result.items]
        assert len(ids) == len(set(ids))


# ===========================================================================
# TestPresenceStatesAndClasses
# ===========================================================================

class TestPresenceStatesAndClasses:
    def test_all_presence_states_valid(self, result):
        for it in result.items:
            assert it.presence_state in ALLOWED_PRESENCE_STATES, \
                f"{it.item_id}: {it.presence_state}"

    def test_all_appendix_p_classes_valid(self, result):
        for it in result.items:
            assert it.appendix_p_class in ALLOWED_APPENDIX_P_CLASSES, \
                f"{it.item_id}: {it.appendix_p_class}"

    def test_all_categories_valid(self, result):
        for it in result.items:
            assert it.category in ALLOWED_CATEGORY_LABELS, \
                f"{it.item_id}: {it.category}"

    def test_no_native_canon(self, result):
        for it in result.items:
            assert it.appendix_p_class != "native_canon", \
                f"{it.item_id} should not be native_canon"

    def test_all_items_have_allowed_claim(self, result):
        for it in result.items:
            assert len(it.allowed_claim) > 10, f"{it.item_id} missing allowed_claim"

    def test_all_items_have_forbidden_claim(self, result):
        for it in result.items:
            assert len(it.forbidden_claim) > 10, f"{it.item_id} missing forbidden_claim"

    def test_all_items_have_notes(self, result):
        for it in result.items:
            assert len(it.notes) >= 1, f"{it.item_id} missing notes"


# ===========================================================================
# TestCategorySummaries
# ===========================================================================

class TestCategorySummaries:
    def test_six_summaries(self, result):
        assert len(result.category_summaries) == 6

    def test_all_summary_labels_valid(self, result):
        for s in result.category_summaries:
            assert s.category_label in ALLOWED_CATEGORY_LABELS

    def test_summary_counts_match_items(self, result):
        for s in result.category_summaries:
            cat_items = [it for it in result.items if it.category == s.category_label]
            assert s.n_items == len(cat_items)


# ===========================================================================
# TestReadinessAssessment
# ===========================================================================

class TestReadinessAssessment:
    def test_first_wave_closed(self, result):
        assert result.readiness_assessment.first_wave_closed is True

    def test_all_gaps_documented(self, result):
        assert result.readiness_assessment.all_gaps_documented is True

    def test_no_silent_promotions(self, result):
        assert result.readiness_assessment.no_silent_promotions is True

    def test_nonclaims_preserved(self, result):
        assert result.readiness_assessment.nonclaims_preserved is True

    def test_hard_rules_applied(self, result):
        assert result.readiness_assessment.hard_rules_applied is True

    def test_ready_for_qiib(self, result):
        assert result.readiness_assessment.ready_for_qiib is True


# ===========================================================================
# TestNonclaims
# ===========================================================================

class TestNonclaims:
    def test_nonclaims_count(self, result):
        assert len(result.nonclaims) == N_QII0_NONCLAIMS

    def test_all_start_with_not_claiming(self, result):
        for nc in result.nonclaims:
            assert nc.startswith("NOT_claiming_")

    def test_mentions_many_body(self, result):
        nc_text = " ".join(result.nonclaims).lower()
        assert "many_body" in nc_text or "many body" in nc_text

    def test_mentions_decoherence_not_entanglement(self, result):
        nc_text = " ".join(result.nonclaims).lower()
        assert "decoherence" in nc_text and "entanglement" in nc_text

    def test_mentions_born_rule(self, result):
        nc_text = " ".join(result.nonclaims).lower()
        assert "born" in nc_text


# ===========================================================================
# TestHardRules
# ===========================================================================

class TestHardRules:
    def test_hard_rules_count(self, result):
        assert len(result.hard_rules) == N_HARD_RULES

    def test_absence_over_implication(self, result):
        assert any("absence" in r for r in result.hard_rules)

    def test_obstruction_over_vague(self, result):
        assert any("obstruction" in r for r in result.hard_rules)

    def test_preserve_nonclaims(self, result):
        assert any("nonclaim" in r for r in result.hard_rules)

    def test_no_toy_as_many_body(self, result):
        assert any("toy" in r for r in result.hard_rules)


# ===========================================================================
# TestClaimsAndDiagnostics
# ===========================================================================

class TestClaimsAndDiagnostics:
    def test_allowed_claims_count(self, result):
        assert len(result.allowed_claims) == 7

    def test_forbidden_claims_count(self, result):
        assert len(result.forbidden_claims) == 7

    def test_diagnostics_n_total(self, result):
        assert result.diagnostics["n_total_items"] == N_TOTAL_ITEMS

    def test_diagnostics_n_categories(self, result):
        assert result.diagnostics["n_categories"] == 6

    def test_diagnostics_most_constrained(self, result):
        assert "F2" in result.diagnostics["most_constrained_gap"]

    def test_diagnostics_only_extension(self, result):
        assert "E5" in result.diagnostics["only_extension_level_item"]


# ===========================================================================
# TestMasterAudit
# ===========================================================================

class TestMasterAudit:
    def test_valid_true(self, result):
        assert result.valid is True

    def test_inventory_verdict(self, result):
        assert result.inventory_verdict == QII0_INVENTORY_VERDICT

    def test_idempotency(self):
        r1 = run_qii0_second_wave_gap_inventory()
        r2 = run_qii0_second_wave_gap_inventory()
        assert r1.valid == r2.valid
        assert r1.n_total == r2.n_total
        assert r1.inventory_verdict == r2.inventory_verdict

    def test_self_test(self):
        assert _self_test() is True
