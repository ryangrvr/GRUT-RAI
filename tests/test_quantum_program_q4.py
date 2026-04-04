"""Tests for GRUT Phase Q4 — Program Fork Audit and Phase-Completion Decision.

Verifies:
1. Master result construction and classification
2. Path A (circularity break) definition and feasibility
3. Path B (noise/fluctuation) definition and feasibility
4. Path C (consolidation) definition and feasibility
5. Success criteria for all paths
6. Feasibility audits
7. Phase-completion test
8. Hard blocker inventory after Q4
9. Forbidden-claim blocking (no overclaims)
10. Validation guards
11. Document constraints
12. Export to dict
"""

import pytest

from grut.quantum_program_q4 import (
    run_q4_assessment,
    build_path_a,
    build_path_b,
    build_path_c,
    build_success_criteria_a,
    build_success_criteria_b,
    build_success_criteria_c,
    build_feasibility_a,
    build_feasibility_b,
    build_feasibility_c,
    build_phase_completion_test,
    build_hard_blockers_after_q4,
    build_document_constraints,
    _validate_q4,
    Q4Result,
    PathDefinition,
    SuccessCriteria,
    FeasibilityAudit,
    PhaseCompletionTest,
    DocumentConstraints,
    Q4_FORBIDDEN_CLAIMS,
    UNRESOLVED_AFTER_Q3,
    Q1_ESTABLISHED,
    Q2_ESTABLISHED,
    Q3_ESTABLISHED,
    PHASE_NAME,
)


# ================================================================
# Test Class: Master Result
# ================================================================

class TestQ4MasterResult:
    """Test the master Q4 assessment result."""

    def setup_method(self):
        self.result = run_q4_assessment()

    def test_valid(self):
        assert self.result.valid is True

    def test_executive(self):
        assert self.result.executive_determination == "path_c_consolidation_best_next_move"

    def test_best_path_is_c(self):
        assert self.result.best_path == "C"

    def test_best_path_status(self):
        assert self.result.best_path_status == "best_next_move"

    def test_classification(self):
        assert self.result.q4_classification == "phase_completion_audit"

    def test_three_paths(self):
        assert len(self.result.paths) == 3

    def test_path_names(self):
        names = [p.name for p in self.result.paths]
        assert names == ["A", "B", "C"]

    def test_has_safe_claims(self):
        assert len(self.result.safe_claims) >= 5

    def test_has_unsafe_claims(self):
        assert len(self.result.unsafe_claims) >= 5

    def test_has_nonclaims(self):
        assert len(self.result.nonclaims) >= 3

    def test_has_hard_blockers(self):
        assert len(self.result.hard_blockers_after_q4) >= 10

    def test_locked_inheritance_q1(self):
        assert "CTP" in self.result.q1_established or "Galley" in self.result.q1_established

    def test_locked_inheritance_q2(self):
        assert "Drude" in self.result.q2_established or "Lorentzian" in self.result.q2_established

    def test_locked_inheritance_q3(self):
        assert "interior" in self.result.q3_established.lower() or "PDE" in self.result.q3_established

    def test_unresolved_items(self):
        assert len(self.result.unresolved_after_q3) >= 5


# ================================================================
# Test Class: Path A — Circularity Break
# ================================================================

class TestPathA:
    """Test Path A (Circularity-Break Program)."""

    def setup_method(self):
        self.path = build_path_a()

    def test_name(self):
        assert self.path.name == "A"

    def test_label(self):
        assert "Circularity" in self.path.label

    def test_status_premature(self):
        assert self.path.status == "premature"

    def test_depends_on_all_prior(self):
        assert self.path.depends_on_q1 is True
        assert self.path.depends_on_q2 is True
        assert self.path.depends_on_q3 is True

    def test_risk_of_circular_restatement_high(self):
        assert "high" in self.path.risk_of_circular_restatement.lower()

    def test_risk_of_manufactured_authority_high(self):
        assert "high" in self.path.risk_of_manufactured_authority.lower()

    def test_formal_tractability_low(self):
        assert "low" in self.path.formal_tractability.lower()

    def test_canon_continuity_high(self):
        assert "high" in self.path.canon_continuity.lower()

    def test_goal_mentions_first_order(self):
        assert "first-order" in self.path.goal.lower() or "first order" in self.path.goal.lower()

    def test_appendix_c_remains_blocked(self):
        assert "appendix c" in self.path.what_remains_blocked_if_successful.lower() or \
               "Appendix C" in self.path.what_remains_blocked_if_successful


# ================================================================
# Test Class: Path B — Noise/Fluctuation
# ================================================================

class TestPathB:
    """Test Path B (Noise/Fluctuation Program)."""

    def setup_method(self):
        self.path = build_path_b()

    def test_name(self):
        assert self.path.name == "B"

    def test_label(self):
        assert "Noise" in self.path.label or "Fluctuation" in self.path.label

    def test_status_secondary(self):
        assert self.path.status == "valuable_but_secondary"

    def test_depends_on_q1_q2(self):
        assert self.path.depends_on_q1 is True
        assert self.path.depends_on_q2 is True

    def test_does_not_require_q3(self):
        assert self.path.depends_on_q3 is False

    def test_risk_of_manufactured_authority(self):
        assert "high" in self.path.risk_of_manufactured_authority.lower()

    def test_goal_mentions_noise_or_fluctuation(self):
        goal_lower = self.path.goal.lower()
        assert "noise" in goal_lower or "fluctuation" in goal_lower

    def test_q1_dependency_mentions_ctp_or_ghost(self):
        dep = self.path.q1_dependency_description.lower()
        assert "ctp" in dep or "galley" in dep or "ghost" in dep or "phi" in dep

    def test_q2_dependency_mentions_drude_or_fdt(self):
        dep = self.path.q2_dependency_description.lower()
        assert "drude" in dep or "fdt" in dep or "bath" in dep


# ================================================================
# Test Class: Path C — Consolidation
# ================================================================

class TestPathC:
    """Test Path C (Canon-Closure / Consolidation)."""

    def setup_method(self):
        self.path = build_path_c()

    def test_name(self):
        assert self.path.name == "C"

    def test_label(self):
        assert "Consolidation" in self.path.label or "Closure" in self.path.label

    def test_status_best_next_move(self):
        assert self.path.status == "best_next_move"

    def test_depends_on_all_prior(self):
        assert self.path.depends_on_q1 is True
        assert self.path.depends_on_q2 is True
        assert self.path.depends_on_q3 is True

    def test_lowest_manufactured_authority_risk(self):
        assert "low" in self.path.risk_of_manufactured_authority.lower()

    def test_low_circular_restatement_risk(self):
        assert "low" in self.path.risk_of_circular_restatement.lower()

    def test_highest_canon_continuity(self):
        assert "high" in self.path.canon_continuity.lower()

    def test_high_formal_tractability(self):
        assert "high" in self.path.formal_tractability.lower()

    def test_goal_mentions_consolidation_or_register(self):
        goal_lower = self.path.goal.lower()
        assert "register" in goal_lower or "consolidat" in goal_lower

    def test_why_needed_mentions_no_route(self):
        why_lower = self.path.why_needed_now.lower()
        assert "no visible" in why_lower or "not present" in why_lower


# ================================================================
# Test Class: Success Criteria
# ================================================================

class TestSuccessCriteria:
    """Test success criteria for all paths."""

    def setup_method(self):
        self.criteria_a = build_success_criteria_a()
        self.criteria_b = build_success_criteria_b()
        self.criteria_c = build_success_criteria_c()

    def test_path_a_has_criteria(self):
        assert len(self.criteria_a.criteria) >= 3

    def test_path_a_upgrade_is_material(self):
        assert self.criteria_a.upgrade_is_material is True

    def test_path_a_upgrade_from_grounding(self):
        assert "grounding" in self.criteria_a.would_upgrade_from.lower()

    def test_path_a_upgrade_to_derivational(self):
        assert "derivat" in self.criteria_a.would_upgrade_to.lower()

    def test_path_b_has_criteria(self):
        assert len(self.criteria_b.criteria) >= 3

    def test_path_b_upgrade_is_material(self):
        assert self.criteria_b.upgrade_is_material is True

    def test_path_c_has_criteria(self):
        assert len(self.criteria_c.criteria) >= 3

    def test_path_c_upgrade_not_material(self):
        assert self.criteria_c.upgrade_is_material is False

    def test_all_have_minimum_for_success(self):
        for c in [self.criteria_a, self.criteria_b, self.criteria_c]:
            assert len(c.minimum_for_success) > 0


# ================================================================
# Test Class: Feasibility Audits
# ================================================================

class TestFeasibilityAudits:
    """Test feasibility audits for all paths."""

    def setup_method(self):
        self.audit_a = build_feasibility_a()
        self.audit_b = build_feasibility_b()
        self.audit_c = build_feasibility_c()

    def test_path_a_premature(self):
        assert self.audit_a.feasibility == "likely_premature"

    def test_path_a_will_not_produce_derivation(self):
        assert self.audit_a.likely_to_produce_real_derivation is False

    def test_path_a_will_restate(self):
        assert self.audit_a.likely_to_restate_existing is True

    def test_path_a_has_questions(self):
        assert len(self.audit_a.questions) >= 4

    def test_path_a_has_missing_structures(self):
        assert len(self.audit_a.structures_missing) >= 3

    def test_path_b_not_ready(self):
        assert self.audit_b.feasibility == "conceptually_required_but_not_ready"

    def test_path_b_will_import(self):
        assert self.audit_b.likely_to_import_external is True

    def test_path_b_will_not_derive(self):
        assert self.audit_b.likely_to_produce_real_derivation is False

    def test_path_b_has_questions(self):
        assert len(self.audit_b.questions) >= 4

    def test_path_b_missing_temperature(self):
        missing = " ".join(self.audit_b.structures_missing).lower()
        assert "temperature" in missing or "energy scale" in missing

    def test_path_c_feasible_now(self):
        assert self.audit_c.feasibility == "feasible_now"

    def test_path_c_will_not_restate(self):
        assert self.audit_c.likely_to_restate_existing is False

    def test_path_c_will_not_import(self):
        assert self.audit_c.likely_to_import_external is False

    def test_path_c_no_missing_structures(self):
        assert len(self.audit_c.structures_missing) == 0

    def test_path_c_all_present(self):
        assert len(self.audit_c.structures_present) >= 3


# ================================================================
# Test Class: Phase Completion
# ================================================================

class TestPhaseCompletion:
    """Test the phase-completion determination."""

    def setup_method(self):
        self.pct = build_phase_completion_test()

    def test_complete_for_consolidation(self):
        assert self.pct.phase_status == "complete_for_consolidation"

    def test_consolidation_sufficient(self):
        assert self.pct.consolidation_sufficient_for_completion is True

    def test_circularity_break_not_required(self):
        assert self.pct.circularity_break_required_for_completion is False

    def test_fluctuation_not_required(self):
        assert self.pct.fluctuation_structure_required_for_completion is False

    def test_q1_contribution_nonempty(self):
        assert len(self.pct.q1_contribution) > 0

    def test_q2_contribution_nonempty(self):
        assert len(self.pct.q2_contribution) > 0

    def test_q3_contribution_nonempty(self):
        assert len(self.pct.q3_contribution) > 0

    def test_combined_statement_nonempty(self):
        assert len(self.pct.combined_statement) > 0

    def test_combined_statement_mentions_circular(self):
        assert "circular" in self.pct.combined_statement.lower()

    def test_combined_statement_mentions_appendix_c(self):
        assert "appendix c" in self.pct.combined_statement.lower() or \
               "Appendix C" in self.pct.combined_statement

    def test_has_next_phase_targets(self):
        assert len(self.pct.next_phase_targets) >= 3

    def test_next_phase_targets_include_circularity(self):
        targets = " ".join(self.pct.next_phase_targets).lower()
        assert "circularity" in targets

    def test_next_phase_targets_include_noise(self):
        targets = " ".join(self.pct.next_phase_targets).lower()
        assert "noise" in targets or "fluctuation" in targets

    def test_rationale_nonempty(self):
        assert len(self.pct.rationale) > 0


# ================================================================
# Test Class: Hard Blockers After Q4
# ================================================================

class TestHardBlockersQ4:
    """Test the hard blocker inventory surviving Q4."""

    def setup_method(self):
        self.blockers = build_hard_blockers_after_q4()

    def test_at_least_10_blockers(self):
        assert len(self.blockers) >= 10

    def test_circularity_survives(self):
        names = [b["name"] for b in self.blockers]
        assert "circularity_not_broken" in names

    def test_noise_survives(self):
        names = [b["name"] for b in self.blockers]
        assert "noise_spectrum_unknown" in names

    def test_born_rule_survives(self):
        names = [b["name"] for b in self.blockers]
        assert "no_born_rule" in names

    def test_measurement_survives(self):
        names = [b["name"] for b in self.blockers]
        assert "no_measurement_coupling" in names

    def test_temperature_blocker_present(self):
        names = [b["name"] for b in self.blockers]
        assert "no_temperature_or_energy_scale" in names

    def test_bath_dof_blocker_present(self):
        names = [b["name"] for b in self.blockers]
        assert "bath_dof_unidentified" in names

    def test_all_survive_q4(self):
        for b in self.blockers:
            assert b["survives_q4"] is True

    def test_all_have_q4_update(self):
        for b in self.blockers:
            assert "q4_update" in b
            assert len(b["q4_update"]) > 0

    def test_appendix_c_blockers_unchanged(self):
        appendix_c = [b for b in self.blockers if "Appendix C" in b.get("q4_update", "")]
        assert len(appendix_c) >= 4


# ================================================================
# Test Class: Forbidden Claims
# ================================================================

class TestForbiddenClaims:
    """Test that forbidden claims are blocked."""

    def setup_method(self):
        self.result = run_q4_assessment()

    def test_forbidden_claims_list_exists(self):
        assert len(Q4_FORBIDDEN_CLAIMS) >= 8

    def test_breaks_circularity_forbidden(self):
        assert "breaks_circularity" in Q4_FORBIDDEN_CLAIMS

    def test_derives_noise_forbidden(self):
        assert "derives_noise_spectrum" in Q4_FORBIDDEN_CLAIMS

    def test_resolves_appendix_c_forbidden(self):
        assert "resolves_appendix_c" in Q4_FORBIDDEN_CLAIMS

    def test_derives_born_rule_forbidden(self):
        assert "derives_born_rule" in Q4_FORBIDDEN_CLAIMS

    def test_completes_quantum_program_forbidden(self):
        assert "completes_quantum_program" in Q4_FORBIDDEN_CLAIMS

    def test_safe_claims_do_not_break_circularity(self):
        for claim in self.result.safe_claims:
            low = claim.lower()
            assert "circularity is broken" not in low
            assert "circularity has been broken" not in low

    def test_safe_claims_do_not_derive_noise(self):
        for claim in self.result.safe_claims:
            low = claim.lower()
            assert "noise spectrum has been derived" not in low

    def test_safe_claims_do_not_resolve_appendix_c(self):
        for claim in self.result.safe_claims:
            low = claim.lower()
            assert "appendix c blocker is resolved" not in low


# ================================================================
# Test Class: Validation Guard
# ================================================================

class TestValidationGuard:
    """Test the _validate_q4 guard against overclaims."""

    def test_valid_result_passes(self):
        result = run_q4_assessment()
        # Should not raise
        _validate_q4(result)

    def test_bad_executive_raises(self):
        result = run_q4_assessment()
        result.executive_determination = "quantum_program_complete"
        with pytest.raises(ValueError, match="not in"):
            _validate_q4(result)

    def test_bad_classification_raises(self):
        result = run_q4_assessment()
        result.q4_classification = "breakthrough"
        with pytest.raises(ValueError, match="not in"):
            _validate_q4(result)

    def test_too_few_paths_raises(self):
        result = run_q4_assessment()
        result.paths = result.paths[:2]
        with pytest.raises(ValueError, match="at least 3"):
            _validate_q4(result)

    def test_no_best_path_raises(self):
        result = run_q4_assessment()
        for p in result.paths:
            p.status = "premature"
        with pytest.raises(ValueError, match="Exactly one"):
            _validate_q4(result)

    def test_two_best_paths_raises(self):
        result = run_q4_assessment()
        for p in result.paths:
            p.status = "best_next_move"
        with pytest.raises(ValueError, match="Exactly one"):
            _validate_q4(result)

    def test_mismatched_executive_raises(self):
        result = run_q4_assessment()
        result.best_path = "A"
        result.executive_determination = "path_c_consolidation_best_next_move"
        with pytest.raises(ValueError, match="path_a"):
            _validate_q4(result)

    def test_too_few_nonclaims_raises(self):
        result = run_q4_assessment()
        result.nonclaims = ["only one"]
        with pytest.raises(ValueError, match="at least 3"):
            _validate_q4(result)

    def test_too_few_blockers_raises(self):
        result = run_q4_assessment()
        result.hard_blockers_after_q4 = [{"name": "one"}]
        with pytest.raises(ValueError, match="at least 5"):
            _validate_q4(result)

    def test_bad_framing_raises(self):
        result = run_q4_assessment()
        result.document_constraints.q4_framing = "revolutionary"
        with pytest.raises(ValueError, match="not in"):
            _validate_q4(result)


# ================================================================
# Test Class: Document Constraints
# ================================================================

class TestDocumentConstraints:
    """Test document-building constraints."""

    def setup_method(self):
        self.dc = build_document_constraints()

    def test_framing_is_phase_completion_audit(self):
        assert self.dc.q4_framing == "phase_completion_audit"

    def test_has_safe_claims(self):
        assert len(self.dc.safe_claims) >= 5

    def test_has_unsafe_claims(self):
        assert len(self.dc.unsafe_claims) >= 5

    def test_strongest_classification_nonempty(self):
        assert len(self.dc.strongest_defensible_classification) > 0

    def test_safe_claims_mention_q1_q2_q3(self):
        all_safe = " ".join(self.dc.safe_claims).lower()
        assert "q1" in all_safe
        assert "q2" in all_safe
        assert "q3" in all_safe

    def test_unsafe_claims_block_circularity_break(self):
        all_unsafe = " ".join(self.dc.unsafe_claims).lower()
        assert "circularity" in all_unsafe

    def test_unsafe_claims_block_noise_derivation(self):
        all_unsafe = " ".join(self.dc.unsafe_claims).lower()
        assert "noise" in all_unsafe

    def test_unsafe_claims_block_appendix_c_resolution(self):
        all_unsafe = " ".join(self.dc.unsafe_claims).lower()
        assert "appendix c" in all_unsafe


# ================================================================
# Test Class: Export
# ================================================================

class TestExport:
    """Test dict export."""

    def setup_method(self):
        self.result = run_q4_assessment()
        self.d = self.result.to_dict()

    def test_has_executive(self):
        assert "executive_determination" in self.d

    def test_has_best_path(self):
        assert self.d["best_path"] == "C"

    def test_has_paths(self):
        assert len(self.d["paths"]) == 3

    def test_paths_have_status(self):
        for p in self.d["paths"]:
            assert "status" in p

    def test_has_feasibility_audits(self):
        assert len(self.d["feasibility_audits"]) == 3

    def test_has_phase_completion(self):
        assert "phase_status" in self.d["phase_completion"]

    def test_has_hard_blockers(self):
        assert len(self.d["hard_blockers_after_q4"]) >= 10

    def test_has_document_constraints(self):
        assert "q4_framing" in self.d["document_constraints"]

    def test_has_next_phase_recommendation(self):
        assert len(self.d["next_phase_recommendation"]) > 0

    def test_valid_in_export(self):
        assert self.d["valid"] is True


# ================================================================
# Test Class: Path Status Consistency
# ================================================================

class TestPathStatusConsistency:
    """Test that path statuses are mutually consistent."""

    def setup_method(self):
        self.result = run_q4_assessment()

    def test_exactly_one_best(self):
        best = [p for p in self.result.paths if p.status == "best_next_move"]
        assert len(best) == 1

    def test_best_is_c(self):
        best = [p for p in self.result.paths if p.status == "best_next_move"]
        assert best[0].name == "C"

    def test_a_is_not_best(self):
        a = [p for p in self.result.paths if p.name == "A"][0]
        assert a.status != "best_next_move"

    def test_b_is_not_best(self):
        b = [p for p in self.result.paths if p.name == "B"][0]
        assert b.status != "best_next_move"

    def test_a_and_b_have_valid_status(self):
        a = [p for p in self.result.paths if p.name == "A"][0]
        b = [p for p in self.result.paths if p.name == "B"][0]
        valid = {"best_next_move", "valuable_but_secondary", "premature", "reject_for_now"}
        assert a.status in valid
        assert b.status in valid


# ================================================================
# Test Class: Appendix C Boundary Preservation
# ================================================================

class TestAppendixCBoundary:
    """Verify that Appendix C blockers are preserved through Q4."""

    def setup_method(self):
        self.result = run_q4_assessment()

    def test_born_rule_blocked(self):
        blocker_names = [b["name"] for b in self.result.hard_blockers_after_q4]
        assert "no_born_rule" in blocker_names

    def test_measurement_blocked(self):
        blocker_names = [b["name"] for b in self.result.hard_blockers_after_q4]
        assert "no_measurement_coupling" in blocker_names

    def test_interference_blocked(self):
        blocker_names = [b["name"] for b in self.result.hard_blockers_after_q4]
        assert "no_interference_formalism" in blocker_names

    def test_particle_ontology_blocked(self):
        blocker_names = [b["name"] for b in self.result.hard_blockers_after_q4]
        assert "no_particle_ontology" in blocker_names

    def test_experiment_framework_blocked(self):
        blocker_names = [b["name"] for b in self.result.hard_blockers_after_q4]
        assert "no_experiment_framework" in blocker_names

    def test_nonclaims_mention_appendix_c(self):
        all_nc = " ".join(self.result.nonclaims).lower()
        assert "appendix c" in all_nc


# ================================================================
# Test Class: Constants
# ================================================================

class TestConstants:
    """Test module constants."""

    def test_phase_name(self):
        assert PHASE_NAME == "recovery_spectral_phase"

    def test_q1_established_nonempty(self):
        assert len(Q1_ESTABLISHED) > 0

    def test_q2_established_nonempty(self):
        assert len(Q2_ESTABLISHED) > 0

    def test_q3_established_nonempty(self):
        assert len(Q3_ESTABLISHED) > 0

    def test_unresolved_after_q3_nonempty(self):
        assert len(UNRESOLVED_AFTER_Q3) >= 5

    def test_forbidden_claims_nonempty(self):
        assert len(Q4_FORBIDDEN_CLAIMS) >= 8
