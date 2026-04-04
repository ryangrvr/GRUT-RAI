"""Tests for GRUT Phase Q1 — Micro-to-Macro Construction Test.

Verifies:
1. Candidate family construction and classification
2. Recovery map completeness and viability
3. Hard blocker inventory
4. Appendix C boundary locking (no blocker resolution claimed)
5. Forbidden-claim blocking (no quantum overclaims)
6. Safe/unsafe claim separation
7. Export to dict
8. Minimum criteria enforcement
"""

import pytest

from grut.quantum_program_q1 import (
    run_q1_assessment,
    build_family_a,
    build_family_b,
    build_family_c,
    build_family_d,
    build_recovery_map_family_a,
    build_recovery_map_family_b,
    build_recovery_map_family_c,
    build_recovery_map_family_d,
    build_hard_blockers,
    APPENDIX_C_STRUCTURAL_BLOCKERS,
    Q1_SCOPE,
    Q1_FORBIDDEN_CLAIMS,
    ALLOWED_VOCABULARY,
    FORBIDDEN_VOCABULARY,
    GRUT_RECOVERY_MODULES,
    Q1Result,
    CandidateFamily,
    RecoveryMap,
    HardBlocker,
)


# ================================================================
# Test Class: Master Result
# ================================================================

class TestQ1MasterResult:
    """Test the master Q1 assessment result."""

    def setup_method(self):
        self.result = run_q1_assessment()

    def test_result_valid(self):
        assert self.result.valid is True

    def test_executive_determination(self):
        assert self.result.executive_determination == "narrow_q1_foundation_identified"

    def test_strongest_candidate_is_b(self):
        assert self.result.strongest_candidate == "B"

    def test_q1_classification(self):
        assert self.result.q1_classification == "recovery_program"

    def test_four_families_evaluated(self):
        assert len(self.result.families) == 4

    def test_appendix_c_blockers_locked(self):
        """CRITICAL: Q1 must NOT resolve any Appendix C blocker."""
        assert self.result.appendix_c_blockers_resolved_by_q1 == 0

    def test_appendix_c_blockers_inherited(self):
        assert len(self.result.appendix_c_blockers_inherited) == 8
        assert "no_amplitude_formalism" in self.result.appendix_c_blockers_inherited
        assert "no_born_rule" in self.result.appendix_c_blockers_inherited

    def test_has_safe_claims(self):
        assert len(self.result.safe_claims) >= 5

    def test_has_unsafe_claims(self):
        assert len(self.result.unsafe_claims) >= 5

    def test_has_hard_blockers(self):
        assert len(self.result.hard_blockers) >= 5

    def test_has_nonclaims(self):
        assert len(self.result.nonclaims) >= 5

    def test_q1_scope_set(self):
        assert len(self.result.q1_addresses) >= 4

    def test_q1_forbidden_set(self):
        assert len(self.result.q1_does_not_address) >= 5


# ================================================================
# Test Class: Family A (KG/Mori-Zwanzig)
# ================================================================

class TestFamilyA:
    """Test Family A: Reversible Substrate + Coarse Graining."""

    def setup_method(self):
        self.family = build_family_a()

    def test_status_viable(self):
        assert self.family.status == "viable_for_q1"

    def test_microphysical_object(self):
        assert self.family.microphysical_object == "scalar_field"

    def test_microdynamic_law(self):
        assert self.family.microdynamic_law == "reversible_hamiltonian"

    def test_dissipation_mechanism(self):
        assert self.family.dissipation_mechanism == "overdamped_limit"

    def test_preserves_constitutive_law(self):
        assert self.family.preserves_constitutive_law is True

    def test_preserves_memory_tensor(self):
        assert self.family.preserves_memory_tensor is True

    def test_recovery_approximate_not_exact(self):
        assert self.family.recovery_is_approximate is True
        assert self.family.recovery_is_exact is False

    def test_passes_minimum_criteria(self):
        assert self.family.passes_minimum_criteria() is True

    def test_has_grut_module_evidence(self):
        assert len(self.family.grut_modules_supporting) >= 1

    def test_has_structural_blockers(self):
        assert len(self.family.structural_blockers) >= 1

    def test_has_nonclaims(self):
        assert len(self.family.nonclaims) >= 1

    def test_assumptions_not_theory_rebuilding(self):
        assert self.family.assumption_severity != "theory_rebuilding"


# ================================================================
# Test Class: Family B (CTP/Galley) — Strongest Candidate
# ================================================================

class TestFamilyB:
    """Test Family B: CTP/Galley Open-System Route."""

    def setup_method(self):
        self.family = build_family_b()

    def test_status_viable(self):
        assert self.family.status == "viable_for_q1"

    def test_microphysical_object(self):
        assert self.family.microphysical_object == "doubled_field"

    def test_microdynamic_law(self):
        assert self.family.microdynamic_law == "effective_open_system"

    def test_dissipation_mechanism(self):
        assert self.family.dissipation_mechanism == "ctp_boundary_condition"

    def test_preserves_constitutive_law(self):
        assert self.family.preserves_constitutive_law is True

    def test_recovery_exact(self):
        """Family B's recovery is exact at tree level, not approximate."""
        assert self.family.recovery_is_exact is True
        assert self.family.recovery_is_approximate is False

    def test_grut_compatibility_highest(self):
        assert self.family.grut_compatibility == "highest"

    def test_assumptions_mild(self):
        assert self.family.assumption_severity == "mild"

    def test_passes_minimum_criteria(self):
        assert self.family.passes_minimum_criteria() is True

    def test_has_three_grut_modules(self):
        assert len(self.family.grut_modules_supporting) >= 3

    def test_does_not_create_false_authority(self):
        assert self.family.code_would_create_false_authority is False

    def test_has_nonclaims_about_ctp(self):
        """Must not claim CTP interpretation is established."""
        nonclaims_joined = " ".join(self.family.nonclaims).lower()
        assert "not claim" in nonclaims_joined or "does not" in nonclaims_joined

    def test_bath_dof_acknowledged_unspecified(self):
        blockers_joined = " ".join(self.family.structural_blockers).lower()
        assert "bath" in blockers_joined or "hidden" in blockers_joined


# ================================================================
# Test Class: Family C (Complexified) — Should Fail
# ================================================================

class TestFamilyC:
    """Test Family C: Complexified Memory (should be rejected/speculative)."""

    def setup_method(self):
        self.family = build_family_c()

    def test_status_too_speculative(self):
        assert self.family.status == "too_speculative"

    def test_fails_minimum_criteria(self):
        """Family C must NOT pass minimum criteria."""
        assert self.family.passes_minimum_criteria() is False

    def test_does_not_preserve_constitutive_law(self):
        assert self.family.preserves_constitutive_law is False

    def test_would_create_false_authority(self):
        assert self.family.code_would_create_false_authority is True

    def test_assumption_severity_major(self):
        assert self.family.assumption_severity == "major"

    def test_no_grut_module_evidence(self):
        assert len(self.family.grut_modules_supporting) == 0

    def test_recovery_not_viable(self):
        assert self.family.recovery_is_exact is False
        assert self.family.recovery_is_approximate is False


# ================================================================
# Test Class: Family D (History Functional)
# ================================================================

class TestFamilyD:
    """Test Family D: History Functional / Nonlocal Kernel."""

    def setup_method(self):
        self.family = build_family_d()

    def test_status_premature(self):
        assert self.family.status == "conceptually_interesting_but_premature"

    def test_preserves_constitutive_law(self):
        assert self.family.preserves_constitutive_law is True

    def test_recovery_exact(self):
        """Kernel-to-ODE reduction IS exact for exponential kernel."""
        assert self.family.recovery_is_exact is True

    def test_has_grut_module_evidence(self):
        assert len(self.family.grut_modules_supporting) >= 1

    def test_passes_minimum_criteria(self):
        assert self.family.passes_minimum_criteria() is True


# ================================================================
# Test Class: Recovery Maps
# ================================================================

class TestRecoveryMaps:
    """Test recovery map construction and viability checks."""

    def test_family_a_recovery_viable(self):
        rm = build_recovery_map_family_a()
        assert rm.is_viable() is True
        assert rm.overall_recovery_approximate is True
        assert rm.overall_recovery_exact is False
        assert rm.assessment == "complete_classical"

    def test_family_b_recovery_viable(self):
        rm = build_recovery_map_family_b()
        assert rm.is_viable() is True
        assert rm.overall_recovery_exact is True
        assert rm.overall_recovery_approximate is False
        assert rm.assessment == "complete_classical"

    def test_family_c_recovery_not_viable(self):
        rm = build_recovery_map_family_c()
        assert rm.is_viable() is False
        assert rm.assessment == "absent"

    def test_family_d_recovery_viable(self):
        rm = build_recovery_map_family_d()
        assert rm.is_viable() is True
        assert rm.assessment == "partial"

    def test_family_a_identifies_phi(self):
        rm = build_recovery_map_family_a()
        assert "KG" in rm.phi_identification or "overdamped" in rm.phi_identification

    def test_family_b_identifies_phi(self):
        rm = build_recovery_map_family_b()
        assert "physical-limit" in rm.phi_identification or "Φ₊" in rm.phi_identification

    def test_family_b_identifies_arrow(self):
        rm = build_recovery_map_family_b()
        assert "CTP" in rm.what_generates_arrow or "boundary" in rm.what_generates_arrow

    def test_family_a_has_missing_pieces(self):
        rm = build_recovery_map_family_a()
        assert len(rm.missing_pieces) >= 2

    def test_family_b_has_missing_pieces(self):
        rm = build_recovery_map_family_b()
        assert len(rm.missing_pieces) >= 3


# ================================================================
# Test Class: Hard Blockers
# ================================================================

class TestHardBlockers:
    """Test hard blocker construction and classification."""

    def setup_method(self):
        self.blockers = build_hard_blockers()

    def test_at_least_five_blockers(self):
        assert len(self.blockers) >= 5

    def test_born_rule_blocker_structural(self):
        born = [b for b in self.blockers if b.name == "no_born_rule"]
        assert len(born) == 1
        assert born[0].blocker_type == "structural"
        assert born[0].survives_even_if_q1_succeeds is True
        assert born[0].q1_can_address is False

    def test_measurement_blocker_structural(self):
        meas = [b for b in self.blockers if b.name == "no_measurement_coupling"]
        assert len(meas) == 1
        assert meas[0].blocker_type == "structural"

    def test_interference_blocker_structural(self):
        interf = [b for b in self.blockers if b.name == "no_interference_formalism"]
        assert len(interf) == 1
        assert interf[0].blocker_type == "structural"

    def test_bath_blocker_extendable(self):
        bath = [b for b in self.blockers if b.name == "bath_dof_unspecified"]
        assert len(bath) == 1
        assert bath[0].blocker_type == "currently_missing_potentially_extendable"

    def test_loop_corrections_extendable(self):
        loop = [b for b in self.blockers if b.name == "loop_corrections_unknown"]
        assert len(loop) == 1
        assert loop[0].blocker_type == "currently_missing_potentially_extendable"

    def test_all_blockers_survive_q1(self):
        """Every hard blocker must survive even if Q1 succeeds."""
        for b in self.blockers:
            assert b.survives_even_if_q1_succeeds is True, (
                f"Blocker '{b.name}' claims to not survive Q1 — this is overclaim"
            )

    def test_no_blocker_addressable_by_q1(self):
        """Q1 should not claim to address any hard blocker."""
        for b in self.blockers:
            assert b.q1_can_address is False, (
                f"Blocker '{b.name}' claims Q1 can address it — this is overclaim"
            )


# ================================================================
# Test Class: Forbidden Claim Blocking
# ================================================================

class TestForbiddenClaims:
    """Test that no forbidden claims are made anywhere in the result."""

    def setup_method(self):
        self.result = run_q1_assessment()

    def test_no_appendix_c_resolution(self):
        assert self.result.appendix_c_blockers_resolved_by_q1 == 0

    def test_executive_in_allowed_set(self):
        allowed = {
            "narrow_q1_foundation_identified",
            "promising_families_but_no_code_warranted",
            "document_only_conceptual",
            "no_viable_q1_foundation",
        }
        assert self.result.executive_determination in allowed

    def test_classification_in_allowed_set(self):
        allowed = {
            "recovery_program",
            "mechanism_proposal",
            "structured_extension",
            "speculative_horizon",
            "failure",
        }
        assert self.result.q1_classification in allowed

    def test_viable_families_preserve_constitutive_law(self):
        for f in self.result.families:
            if f.status == "viable_for_q1":
                assert f.preserves_constitutive_law is True

    def test_no_family_claims_to_derive_qm(self):
        """No family status should imply QM is derived."""
        for f in self.result.families:
            assert f.status != "derives_quantum_mechanics"

    def test_speculative_family_c_blocked(self):
        """Family C must not be viable."""
        family_c = [f for f in self.result.families if f.name == "C"]
        assert len(family_c) == 1
        assert family_c[0].status == "too_speculative"
        assert family_c[0].passes_minimum_criteria() is False

    def test_unsafe_claims_include_key_prohibitions(self):
        unsafe_joined = " ".join(self.result.unsafe_claims).lower()
        assert "interference" in unsafe_joined or "probabilities" in unsafe_joined
        assert "measurement" in unsafe_joined or "predict" in unsafe_joined
        assert "quantum" in unsafe_joined

    def test_forbidden_claims_list_nonempty(self):
        assert len(Q1_FORBIDDEN_CLAIMS) >= 8


# ================================================================
# Test Class: Vocabulary Control
# ================================================================

class TestVocabulary:
    """Test vocabulary lists are well-formed."""

    def test_allowed_vocabulary_nonempty(self):
        assert len(ALLOWED_VOCABULARY) >= 10

    def test_forbidden_vocabulary_nonempty(self):
        assert len(FORBIDDEN_VOCABULARY) >= 10

    def test_no_overlap(self):
        overlap = set(ALLOWED_VOCABULARY) & set(FORBIDDEN_VOCABULARY)
        assert len(overlap) == 0, f"Vocabulary overlap: {overlap}"


# ================================================================
# Test Class: GRUT Module Registry
# ================================================================

class TestGRUTModuleRegistry:
    """Test the GRUT recovery module registry."""

    def test_registry_has_key_modules(self):
        assert "action_principle" in GRUT_RECOVERY_MODULES
        assert "galley_memory" in GRUT_RECOVERY_MODULES
        assert "galley_truncation" in GRUT_RECOVERY_MODULES
        assert "route_c_nonmarkov_kernel" in GRUT_RECOVERY_MODULES

    def test_galley_supports_family_b(self):
        assert "B" in GRUT_RECOVERY_MODULES["galley_memory"]["families_supported"]
        assert "B" in GRUT_RECOVERY_MODULES["galley_truncation"]["families_supported"]


# ================================================================
# Test Class: Export
# ================================================================

class TestExport:
    """Test dict/JSON export."""

    def setup_method(self):
        self.result = run_q1_assessment()

    def test_to_dict_returns_dict(self):
        d = self.result.to_dict()
        assert isinstance(d, dict)

    def test_to_dict_has_required_keys(self):
        d = self.result.to_dict()
        required = [
            "executive_determination",
            "strongest_candidate",
            "families",
            "hard_blockers",
            "q1_addresses",
            "q1_does_not_address",
            "appendix_c_blockers_inherited",
            "appendix_c_blockers_resolved_by_q1",
            "safe_claims",
            "unsafe_claims",
            "q1_classification",
            "nonclaims",
            "valid",
        ]
        for key in required:
            assert key in d, f"Missing key: {key}"

    def test_families_in_export(self):
        d = self.result.to_dict()
        assert len(d["families"]) == 4

    def test_family_export_has_status(self):
        d = self.result.to_dict()
        for fam in d["families"]:
            assert "status" in fam
            assert "passes_minimum_criteria" in fam

    def test_hard_blockers_in_export(self):
        d = self.result.to_dict()
        assert len(d["hard_blockers"]) >= 5
        for b in d["hard_blockers"]:
            assert "name" in b
            assert "blocker_type" in b

    def test_export_appendix_c_resolved_zero(self):
        d = self.result.to_dict()
        assert d["appendix_c_blockers_resolved_by_q1"] == 0


# ================================================================
# Test Class: Validation Guard
# ================================================================

class TestValidationGuard:
    """Test that the validation guard catches forbidden states."""

    def test_appendix_c_resolution_raises(self):
        """Attempting to set appendix_c_blockers_resolved > 0 must be caught."""
        result = run_q1_assessment()
        # Manually tamper and re-validate
        result.appendix_c_blockers_resolved_by_q1 = 1
        from grut.quantum_program_q1 import _validate_no_forbidden_claims
        with pytest.raises(ValueError, match="CANNOT claim to resolve"):
            _validate_no_forbidden_claims(result)

    def test_viable_without_constitutive_raises(self):
        """A family marked viable but not preserving constitutive law must be caught."""
        result = run_q1_assessment()
        # Tamper with family B
        for f in result.families:
            if f.name == "B":
                f.preserves_constitutive_law = False
        from grut.quantum_program_q1 import _validate_no_forbidden_claims
        with pytest.raises(ValueError, match="does not preserve the constitutive law"):
            _validate_no_forbidden_claims(result)

    def test_bad_executive_raises(self):
        result = run_q1_assessment()
        result.executive_determination = "quantum_mechanics_derived"
        from grut.quantum_program_q1 import _validate_no_forbidden_claims
        with pytest.raises(ValueError, match="not in allowed set"):
            _validate_no_forbidden_claims(result)

    def test_bad_classification_raises(self):
        result = run_q1_assessment()
        result.q1_classification = "full_quantum_theory"
        from grut.quantum_program_q1 import _validate_no_forbidden_claims
        with pytest.raises(ValueError, match="not in allowed set"):
            _validate_no_forbidden_claims(result)


# ================================================================
# Test Class: Appendix C Structural Blockers
# ================================================================

class TestAppendixCBoundary:
    """Test that Appendix C boundary is properly encoded."""

    def test_eight_structural_blockers(self):
        assert len(APPENDIX_C_STRUCTURAL_BLOCKERS) == 8

    def test_key_blockers_present(self):
        assert "no_amplitude_formalism" in APPENDIX_C_STRUCTURAL_BLOCKERS
        assert "no_phase_superposition" in APPENDIX_C_STRUCTURAL_BLOCKERS
        assert "no_born_rule" in APPENDIX_C_STRUCTURAL_BLOCKERS
        assert "no_collapse_decoherence_dynamics" in APPENDIX_C_STRUCTURAL_BLOCKERS
        assert "no_microphysical_ontology" in APPENDIX_C_STRUCTURAL_BLOCKERS

    def test_blockers_are_strings(self):
        for b in APPENDIX_C_STRUCTURAL_BLOCKERS:
            assert isinstance(b, str)
            assert len(b) > 0
