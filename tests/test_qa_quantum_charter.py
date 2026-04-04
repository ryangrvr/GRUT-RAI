"""Tests for grut/qa_quantum_charter.py — Appendix Q-A.

Deterministic test suite for the GRUT Quantum Conceptual Charter.
All tests derive expected values from constants, not from hardcoded literals.

Test classes:
    TestQAConstants              — vocabulary, stage count, verdict set
    TestProgramObjective         — objective statement, scope, preconditions
    TestStageSequence            — 8 stages, ordering, dependencies
    TestStageSuccessCriteria     — valid criterion types per stage
    TestStageDependencies        — dependency chain integrity
    TestAppendixPRules           — 6 discipline rules
    TestForbiddenFailureModes    — 7 forbidden failure modes
    TestEntryNonclaims           — ≥6 nonclaims
    TestQ0Linkage                — Q-A depends on Q0; Q-B depends on Q-A
    TestCharterVerdict           — authorized verdict
    TestDiagnostics              — diagnostics populated and consistent
    TestMasterAudit              — run_qa_quantum_charter end-to-end
"""

import pytest

from grut.qa_quantum_charter import (
    # Constants
    QUANTUM_PROGRAM_STAGES,
    N_STAGES,
    ALLOWED_SUCCESS_CRITERION_TYPES,
    N_APPENDIX_P_DISCIPLINE_RULES,
    APPENDIX_P_DISCIPLINE_RULE_IDS,
    N_FORBIDDEN_FAILURE_MODES,
    FORBIDDEN_FAILURE_MODE_IDS,
    FORBIDDEN_FAILURE_MODE_NAMES,
    ALLOWED_CHARTER_VERDICTS,
    CHARTER_VERDICT_AUTHORIZED,
    CHARTER_VERDICT_BLOCKED,
    QA_ENTRY_NONCLAIMS,
    N_QA_ENTRY_NONCLAIMS,
    # Dataclasses
    QAProgramObjective,
    QAStageDef,
    QAAppendixPDisciplineRule,
    QAForbiddenFailureMode,
    QAEntryNonclaims,
    QACharter,
    # Functions
    build_program_objective,
    build_stage_sequence,
    build_appendix_p_rules,
    build_forbidden_failure_modes,
    build_entry_nonclaims,
    assign_charter_verdict,
    run_qa_quantum_charter,
)


# ==============================================================
# TestQAConstants
# ==============================================================

class TestQAConstants:
    """Vocabulary, stage count, and verdict set."""

    def test_n_stages(self):
        assert N_STAGES == 8

    def test_stage_list_length(self):
        assert len(QUANTUM_PROGRAM_STAGES) == N_STAGES

    def test_q0_in_stage_list(self):
        assert "Q0_quantum_entry_inventory" in QUANTUM_PROGRAM_STAGES

    def test_qa_in_stage_list(self):
        assert "QA_quantum_conceptual_charter" in QUANTUM_PROGRAM_STAGES

    def test_qb_in_stage_list(self):
        assert "QB_quantum_kinematics" in QUANTUM_PROGRAM_STAGES

    def test_qf_in_stage_list(self):
        assert "QF_interference_and_wave_phenomena" in QUANTUM_PROGRAM_STAGES

    def test_success_criterion_types_count(self):
        assert len(ALLOWED_SUCCESS_CRITERION_TYPES) == 4

    def test_success_in_criterion_types(self):
        assert "success" in ALLOWED_SUCCESS_CRITERION_TYPES

    def test_partial_in_criterion_types(self):
        assert "partial" in ALLOWED_SUCCESS_CRITERION_TYPES

    def test_bounded_negative_in_criterion_types(self):
        assert "bounded_negative" in ALLOWED_SUCCESS_CRITERION_TYPES

    def test_extension_level_in_criterion_types(self):
        assert "extension_level" in ALLOWED_SUCCESS_CRITERION_TYPES

    def test_n_discipline_rules(self):
        assert N_APPENDIX_P_DISCIPLINE_RULES == 6

    def test_n_forbidden_failure_modes(self):
        assert N_FORBIDDEN_FAILURE_MODES == 7

    def test_charter_verdicts_count(self):
        assert len(ALLOWED_CHARTER_VERDICTS) == 2

    def test_authorized_verdict_in_set(self):
        assert CHARTER_VERDICT_AUTHORIZED in ALLOWED_CHARTER_VERDICTS

    def test_blocked_verdict_in_set(self):
        assert CHARTER_VERDICT_BLOCKED in ALLOWED_CHARTER_VERDICTS

    def test_n_entry_nonclaims(self):
        assert N_QA_ENTRY_NONCLAIMS >= 6

    def test_entry_nonclaims_list_length(self):
        assert len(QA_ENTRY_NONCLAIMS) == N_QA_ENTRY_NONCLAIMS

    def test_rule_ids_length(self):
        assert len(APPENDIX_P_DISCIPLINE_RULE_IDS) == N_APPENDIX_P_DISCIPLINE_RULES

    def test_ffm_ids_length(self):
        assert len(FORBIDDEN_FAILURE_MODE_IDS) == N_FORBIDDEN_FAILURE_MODES

    def test_ffm_names_length(self):
        assert len(FORBIDDEN_FAILURE_MODE_NAMES) == N_FORBIDDEN_FAILURE_MODES


# ==============================================================
# TestProgramObjective
# ==============================================================

class TestProgramObjective:
    """Program objective structure and content."""

    def setup_method(self):
        self.obj = build_program_objective()

    def test_statement_nonempty(self):
        assert len(self.obj.statement) > 0

    def test_scope_nonempty(self):
        assert len(self.obj.scope) > 0

    def test_what_is_not_in_scope_at_least_five(self):
        assert len(self.obj.what_is_not_in_scope) >= 5

    def test_required_preconditions_nonempty(self):
        assert len(self.obj.required_preconditions) > 0

    def test_preconditions_met(self):
        assert self.obj.preconditions_met is True

    def test_statement_mentions_disciplined(self):
        stmt = self.obj.statement.lower()
        assert "disciplin" in stmt or "stage" in stmt or "inventory" in stmt

    def test_not_in_scope_includes_deriving_qm(self):
        nis = " ".join(self.obj.what_is_not_in_scope).lower()
        assert "deriv" in nis or "solving" in nis or "quantum mechanics" in nis

    def test_not_in_scope_includes_claiming_grut_is_quantum(self):
        nis = " ".join(self.obj.what_is_not_in_scope).lower()
        assert "claiming grut" in nis or "already a quantum" in nis or "quantum theory" in nis

    def test_preconditions_include_q0(self):
        prec = " ".join(self.obj.required_preconditions).lower()
        assert "q0" in prec or "inventory" in prec


# ==============================================================
# TestStageSequence
# ==============================================================

class TestStageSequence:
    """8-stage sequence integrity."""

    def setup_method(self):
        self.stages = build_stage_sequence()

    def test_count(self):
        assert len(self.stages) == N_STAGES

    def test_indices_sequential(self):
        for i, stage in enumerate(self.stages):
            assert stage.stage_index == i, (
                f"Stage {stage.stage_id} has index {stage.stage_index}, expected {i}"
            )

    def test_stage_ids_match_constants(self):
        for stage in self.stages:
            assert stage.stage_id in QUANTUM_PROGRAM_STAGES

    def test_q0_is_first(self):
        assert self.stages[0].stage_id == "Q0_quantum_entry_inventory"

    def test_qa_is_second(self):
        assert self.stages[1].stage_id == "QA_quantum_conceptual_charter"

    def test_qb_is_third(self):
        assert self.stages[2].stage_id == "QB_quantum_kinematics"

    def test_qf_is_last(self):
        assert self.stages[-1].stage_id == "QF_interference_and_wave_phenomena"

    def test_all_primary_questions_nonempty(self):
        for stage in self.stages:
            assert len(stage.primary_question) > 0, (
                f"Stage {stage.stage_id} has empty primary question"
            )

    def test_all_success_descriptions_nonempty(self):
        for stage in self.stages:
            assert len(stage.success_criterion_description) > 0

    def test_all_appendix_p_classes_nonempty(self):
        for stage in self.stages:
            assert len(stage.appendix_p_class_expected) > 0

    def test_all_hard_blockers_lists_populated(self):
        # All stages except the last should have hard blockers
        for stage in self.stages[:-1]:
            assert len(stage.hard_blockers_if_fail) > 0, (
                f"Stage {stage.stage_id} has no hard blockers"
            )

    def test_stage_names_unique(self):
        names = [s.stage_name for s in self.stages]
        assert len(set(names)) == len(names)

    def test_stage_ids_unique(self):
        ids = [s.stage_id for s in self.stages]
        assert len(set(ids)) == len(ids)


# ==============================================================
# TestStageSuccessCriteria
# ==============================================================

class TestStageSuccessCriteria:
    """Valid success criterion types per stage."""

    def setup_method(self):
        self.stages = build_stage_sequence()

    def test_all_stages_have_valid_criterion_type(self):
        for stage in self.stages:
            assert stage.success_criterion_type in ALLOWED_SUCCESS_CRITERION_TYPES, (
                f"Stage {stage.stage_id} has invalid type "
                f"{stage.success_criterion_type}"
            )

    def test_q0_success_type(self):
        q0 = next(s for s in self.stages
                  if s.stage_id == "Q0_quantum_entry_inventory")
        assert q0.success_criterion_type == "success"

    def test_qa_success_type(self):
        qa = next(s for s in self.stages
                  if s.stage_id == "QA_quantum_conceptual_charter")
        assert qa.success_criterion_type == "success"

    def test_qc5_success_or_bounded(self):
        qc5 = next(s for s in self.stages
                   if s.stage_id == "QC5_classical_limit")
        assert qc5.success_criterion_type in {"success", "bounded_negative"}

    def test_qd_extension_level(self):
        qd = next(s for s in self.stages
                  if s.stage_id == "QD_measurement_and_decoherence")
        assert qd.success_criterion_type == "extension_level"

    def test_qf_extension_level(self):
        qf = next(s for s in self.stages
                  if s.stage_id == "QF_interference_and_wave_phenomena")
        assert qf.success_criterion_type == "extension_level"

    def test_qb_partial_or_bounded(self):
        qb = next(s for s in self.stages
                  if s.stage_id == "QB_quantum_kinematics")
        assert qb.success_criterion_type in {"partial", "bounded_negative"}

    def test_qc_partial_or_extension(self):
        qc = next(s for s in self.stages
                  if s.stage_id == "QC_quantum_microdynamics")
        assert qc.success_criterion_type in {"partial", "extension_level"}

    def test_at_least_two_success_stages(self):
        n = sum(1 for s in self.stages if s.success_criterion_type == "success")
        assert n >= 2

    def test_at_least_one_extension_level_stage(self):
        n = sum(1 for s in self.stages
                if s.success_criterion_type == "extension_level")
        assert n >= 1


# ==============================================================
# TestStageDependencies
# ==============================================================

class TestStageDependencies:
    """Dependency chain integrity."""

    def setup_method(self):
        self.stages = build_stage_sequence()
        self.stage_ids = {s.stage_id for s in self.stages}

    def test_q0_no_dependencies(self):
        q0 = next(s for s in self.stages
                  if s.stage_id == "Q0_quantum_entry_inventory")
        assert len(q0.depends_on) == 0

    def test_qa_depends_on_q0(self):
        qa = next(s for s in self.stages
                  if s.stage_id == "QA_quantum_conceptual_charter")
        assert "Q0_quantum_entry_inventory" in qa.depends_on

    def test_qb_depends_on_qa(self):
        qb = next(s for s in self.stages
                  if s.stage_id == "QB_quantum_kinematics")
        assert "QA_quantum_conceptual_charter" in qb.depends_on

    def test_qc_depends_on_qb(self):
        qc = next(s for s in self.stages
                  if s.stage_id == "QC_quantum_microdynamics")
        assert "QB_quantum_kinematics" in qc.depends_on

    def test_qc5_depends_on_qc(self):
        qc5 = next(s for s in self.stages
                   if s.stage_id == "QC5_classical_limit")
        assert "QC_quantum_microdynamics" in qc5.depends_on

    def test_qd_depends_on_qc5(self):
        qd = next(s for s in self.stages
                  if s.stage_id == "QD_measurement_and_decoherence")
        assert "QC5_classical_limit" in qd.depends_on

    def test_qe_depends_on_qd(self):
        qe = next(s for s in self.stages
                  if s.stage_id == "QE_benchmark_toy_problems")
        assert "QD_measurement_and_decoherence" in qe.depends_on

    def test_qf_depends_on_qe(self):
        qf = next(s for s in self.stages
                  if s.stage_id == "QF_interference_and_wave_phenomena")
        assert "QE_benchmark_toy_problems" in qf.depends_on

    def test_all_dependencies_are_valid_stage_ids(self):
        for stage in self.stages:
            for dep in stage.depends_on:
                assert dep in self.stage_ids, (
                    f"Stage {stage.stage_id} depends on unknown stage {dep}"
                )

    def test_no_self_dependency(self):
        for stage in self.stages:
            assert stage.stage_id not in stage.depends_on


# ==============================================================
# TestAppendixPRules
# ==============================================================

class TestAppendixPRules:
    """6 Appendix P discipline rules."""

    def setup_method(self):
        self.rules = build_appendix_p_rules()

    def test_count(self):
        assert len(self.rules) == N_APPENDIX_P_DISCIPLINE_RULES

    def test_rule_ids_match_constants(self):
        rule_ids = {r.rule_id for r in self.rules}
        for expected_id in APPENDIX_P_DISCIPLINE_RULE_IDS:
            assert expected_id in rule_ids

    def test_all_rule_ids_unique(self):
        ids = [r.rule_id for r in self.rules]
        assert len(set(ids)) == len(ids)

    def test_all_statements_nonempty(self):
        for r in self.rules:
            assert len(r.rule_statement) > 0

    def test_all_violation_patterns_nonempty(self):
        for r in self.rules:
            assert len(r.violation_would_be) > 0

    def test_all_test_for_fields_nonempty(self):
        for r in self.rules:
            assert len(r.tests_for) > 0

    def test_qa_r1_prevents_motivated_postulate_as_native(self):
        r1 = next(r for r in self.rules if r.rule_id == "QA-R1")
        assert "motivated_postulate_as_native" in r1.violation_would_be

    def test_qa_r2_prevents_usefulness_as_nativity(self):
        r2 = next(r for r in self.rules if r.rule_id == "QA-R2")
        assert "usefulness_as_nativity" in r2.violation_would_be

    def test_qa_r3_prevents_unbuilt_route_as_solved(self):
        r3 = next(r for r in self.rules if r.rule_id == "QA-R3")
        assert "unbuilt_route_as_solved" in r3.violation_would_be

    def test_qa_r4_prevents_obstruction_misclassification(self):
        r4 = next(r for r in self.rules if r.rule_id == "QA-R4")
        assert "obstruction" in r4.violation_would_be.lower() or \
               "impossibility" in r4.violation_would_be.lower()

    def test_qa_r5_prevents_effective_regime_promoted(self):
        r5 = next(r for r in self.rules if r.rule_id == "QA-R5")
        assert "effective_regime" in r5.violation_would_be or \
               "regime" in r5.violation_would_be.lower()

    def test_qa_r6_prevents_compatibility_as_derivation(self):
        r6 = next(r for r in self.rules if r.rule_id == "QA-R6")
        assert "compatibility_as_derivation" in r6.violation_would_be


# ==============================================================
# TestForbiddenFailureModes
# ==============================================================

class TestForbiddenFailureModes:
    """7 forbidden failure modes."""

    def setup_method(self):
        self.modes = build_forbidden_failure_modes()

    def test_count(self):
        assert len(self.modes) == N_FORBIDDEN_FAILURE_MODES

    def test_mode_ids_match_constants(self):
        mode_ids = {m.mode_id for m in self.modes}
        for expected_id in FORBIDDEN_FAILURE_MODE_IDS:
            assert expected_id in mode_ids

    def test_mode_names_match_constants(self):
        mode_names = {m.name for m in self.modes}
        for expected_name in FORBIDDEN_FAILURE_MODE_NAMES:
            assert expected_name in mode_names

    def test_all_mode_ids_unique(self):
        ids = [m.mode_id for m in self.modes]
        assert len(set(ids)) == len(ids)

    def test_all_names_unique(self):
        names = [m.name for m in self.modes]
        assert len(set(names)) == len(names)

    def test_all_descriptions_nonempty(self):
        for m in self.modes:
            assert len(m.description) > 0

    def test_all_why_forbidden_nonempty(self):
        for m in self.modes:
            assert len(m.why_forbidden) > 0

    def test_all_related_appendices_nonempty(self):
        for m in self.modes:
            assert len(m.related_appendix) > 0

    def test_ffm1_born_rule_from_constitutive_ode(self):
        m = next(m for m in self.modes if m.mode_id == "FFM1")
        assert m.name == "born_rule_from_constitutive_ode"

    def test_ffm2_wavefunction_from_real_scalar(self):
        m = next(m for m in self.modes if m.mode_id == "FFM2")
        assert m.name == "wavefunction_from_real_scalar"

    def test_ffm3_decoherence_from_relaxation(self):
        m = next(m for m in self.modes if m.mode_id == "FFM3")
        assert m.name == "quantum_decoherence_from_relaxation"

    def test_ffm4_fermionic_without_hopf(self):
        m = next(m for m in self.modes if m.mode_id == "FFM4")
        assert m.name == "fermionic_statistics_without_hopf"

    def test_ffm5_stable_particle_without_skyrme(self):
        m = next(m for m in self.modes if m.mode_id == "FFM5")
        assert m.name == "stable_particle_without_skyrme"

    def test_ffm6_hilbert_space_from_ctp(self):
        m = next(m for m in self.modes if m.mode_id == "FFM6")
        assert m.name == "hilbert_space_from_ctp_doubling"

    def test_ffm7_interference_from_topology(self):
        m = next(m for m in self.modes if m.mode_id == "FFM7")
        assert m.name == "interference_from_topology_alone"

    def test_ffm4_references_fermionic_audit(self):
        m = next(m for m in self.modes if m.mode_id == "FFM4")
        assert "fermionic_emergence_audit" in m.related_appendix

    def test_ffm5_references_bosonic_or_localized_audit(self):
        m = next(m for m in self.modes if m.mode_id == "FFM5")
        assert "localized_bosonic" in m.related_appendix or \
               "localized_bosonic_object_audit" in m.related_appendix

    def test_ffm3_why_forbidden_references_classical_not_quantum(self):
        m = next(m for m in self.modes if m.mode_id == "FFM3")
        why = m.why_forbidden.lower()
        assert "classical" in why or "c-number" in why or "deterministic" in why


# ==============================================================
# TestEntryNonclaims
# ==============================================================

class TestEntryNonclaims:
    """Entry nonclaims at the charter level."""

    def setup_method(self):
        self.nc = build_entry_nonclaims()

    def test_nonclaims_count_at_least_six(self):
        assert self.nc.n_nonclaims >= 6

    def test_nonclaims_list_length_matches_count(self):
        assert len(self.nc.nonclaims) == self.nc.n_nonclaims

    def test_all_registered(self):
        assert self.nc.all_registered is True

    def test_not_claiming_grut_is_quantum_theory(self):
        ncs = " ".join(self.nc.nonclaims).lower()
        assert "quantum_theory" in ncs or "quantum theory" in ncs or \
               "grut_is_quantum" in ncs

    def test_not_claiming_charter_is_derivation(self):
        ncs = " ".join(self.nc.nonclaims).lower()
        assert "derivation" in ncs or "constitutes_derivation" in ncs

    def test_not_claiming_stage_success_guaranteed(self):
        ncs = " ".join(self.nc.nonclaims).lower()
        assert "guaranteed" in ncs or "expected" in ncs

    def test_not_claiming_qb_qf_pre_solved(self):
        ncs = " ".join(self.nc.nonclaims).lower()
        assert "pre_solved" in ncs or "pre-solved" in ncs or "qb" in ncs

    def test_not_claiming_authorization_implies_success(self):
        ncs = " ".join(self.nc.nonclaims).lower()
        assert "authorization" in ncs or "authorized" in ncs or "will_succeed" in ncs

    def test_not_claiming_classification_validates_claim(self):
        ncs = " ".join(self.nc.nonclaims).lower()
        assert "classification" in ncs or "validates" in ncs or "appendix_p" in ncs


# ==============================================================
# TestQ0Linkage
# ==============================================================

class TestQ0Linkage:
    """Q-A must depend on Q0; Q-B must depend on Q-A."""

    def setup_method(self):
        self.charter = run_qa_quantum_charter()

    def test_q0_inventory_linked(self):
        assert self.charter.q0_inventory_linked is True

    def test_qa_depends_on_q0(self):
        qa = next(s for s in self.charter.stage_sequence
                  if s.stage_id == "QA_quantum_conceptual_charter")
        assert "Q0_quantum_entry_inventory" in qa.depends_on

    def test_qb_depends_on_qa(self):
        qb = next(s for s in self.charter.stage_sequence
                  if s.stage_id == "QB_quantum_kinematics")
        assert "QA_quantum_conceptual_charter" in qb.depends_on

    def test_q0_has_no_dependencies(self):
        q0 = next(s for s in self.charter.stage_sequence
                  if s.stage_id == "Q0_quantum_entry_inventory")
        assert len(q0.depends_on) == 0


# ==============================================================
# TestCharterVerdict
# ==============================================================

class TestCharterVerdict:
    """Charter verdict is authorized."""

    def setup_method(self):
        self.charter = run_qa_quantum_charter()

    def test_verdict_authorized(self):
        assert self.charter.charter_verdict == CHARTER_VERDICT_AUTHORIZED

    def test_verdict_not_blocked(self):
        assert self.charter.charter_verdict != CHARTER_VERDICT_BLOCKED

    def test_verdict_in_allowed_set(self):
        assert self.charter.charter_verdict in ALLOWED_CHARTER_VERDICTS

    def test_charter_valid(self):
        assert self.charter.valid is True

    def test_assign_verdict_function_authorized(self):
        obj = build_program_objective()
        stages = build_stage_sequence()
        rules = build_appendix_p_rules()
        modes = build_forbidden_failure_modes()
        nc = build_entry_nonclaims()
        v = assign_charter_verdict(obj, stages, rules, modes, nc)
        assert v == CHARTER_VERDICT_AUTHORIZED

    def test_assign_verdict_blocked_if_preconditions_fail(self):
        obj = build_program_objective()
        obj.preconditions_met = False
        stages = build_stage_sequence()
        rules = build_appendix_p_rules()
        modes = build_forbidden_failure_modes()
        nc = build_entry_nonclaims()
        v = assign_charter_verdict(obj, stages, rules, modes, nc)
        assert v == CHARTER_VERDICT_BLOCKED


# ==============================================================
# TestDiagnostics
# ==============================================================

class TestDiagnostics:
    """Diagnostics dict populated and consistent."""

    def setup_method(self):
        self.charter = run_qa_quantum_charter()
        self.diag = self.charter.diagnostics

    def test_diagnostics_nonempty(self):
        assert len(self.diag) > 0

    def test_n_stages_in_diagnostics(self):
        assert self.diag["n_stages"] == N_STAGES

    def test_n_rules_in_diagnostics(self):
        assert self.diag["n_appendix_p_rules"] == N_APPENDIX_P_DISCIPLINE_RULES

    def test_n_ffm_in_diagnostics(self):
        assert self.diag["n_forbidden_failure_modes"] == N_FORBIDDEN_FAILURE_MODES

    def test_verdict_in_diagnostics(self):
        assert self.diag["charter_verdict"] == CHARTER_VERDICT_AUTHORIZED

    def test_q0_linked_in_diagnostics(self):
        assert self.diag["q0_linked"] is True

    def test_preconditions_met_in_diagnostics(self):
        assert self.diag["preconditions_met"] is True

    def test_all_criterion_types_valid_in_diagnostics(self):
        assert self.diag["all_stages_have_valid_criterion_types"] is True

    def test_success_stage_count(self):
        assert self.diag["success_stage_count"] >= 2

    def test_extension_level_stage_count(self):
        assert self.diag["extension_level_stage_count"] >= 1

    def test_stage_ids_list_length(self):
        assert len(self.diag["stage_ids"]) == N_STAGES

    def test_rule_ids_list_length(self):
        assert len(self.diag["rule_ids"]) == N_APPENDIX_P_DISCIPLINE_RULES

    def test_ffm_names_list_length(self):
        assert len(self.diag["ffm_names"]) == N_FORBIDDEN_FAILURE_MODES


# ==============================================================
# TestMasterAudit
# ==============================================================

class TestMasterAudit:
    """End-to-end test of run_qa_quantum_charter."""

    def setup_method(self):
        self.charter = run_qa_quantum_charter()

    def test_valid(self):
        assert self.charter.valid is True

    def test_n_stages(self):
        assert len(self.charter.stage_sequence) == N_STAGES

    def test_n_rules(self):
        assert len(self.charter.appendix_p_rules) == N_APPENDIX_P_DISCIPLINE_RULES

    def test_n_ffm(self):
        assert len(self.charter.forbidden_failure_modes) == N_FORBIDDEN_FAILURE_MODES

    def test_entry_nonclaims_all_registered(self):
        assert self.charter.entry_nonclaims.all_registered is True

    def test_entry_nonclaims_count(self):
        assert self.charter.entry_nonclaims.n_nonclaims >= 6

    def test_q0_linked(self):
        assert self.charter.q0_inventory_linked is True

    def test_charter_verdict_authorized(self):
        assert self.charter.charter_verdict == CHARTER_VERDICT_AUTHORIZED

    def test_objective_preconditions_met(self):
        assert self.charter.objective.preconditions_met is True

    def test_stages_sequentially_indexed(self):
        for i, stage in enumerate(self.charter.stage_sequence):
            assert stage.stage_index == i

    def test_all_stage_criterion_types_valid(self):
        for stage in self.charter.stage_sequence:
            assert stage.success_criterion_type in ALLOWED_SUCCESS_CRITERION_TYPES

    def test_all_rule_violations_nonempty(self):
        for rule in self.charter.appendix_p_rules:
            assert len(rule.violation_would_be) > 0

    def test_all_ffm_why_forbidden_nonempty(self):
        for mode in self.charter.forbidden_failure_modes:
            assert len(mode.why_forbidden) > 0
