"""Tests for GRUT Phase Q2 — Bath Specification and Reduction Test.

Verifies:
1. Bath candidate construction and classification
2. Drude/Lorentzian structural match encoding
3. Reduction map viability checks
4. Q2 minimum criteria enforcement
5. Hard blocker inventory after Q2
6. Forbidden-claim blocking (no overclaims)
7. Canon compatibility checks
8. Markovian vs memory audit encoding
9. Export to dict
10. Validation guards
"""

import pytest

from grut.quantum_program_q2 import (
    run_q2_assessment,
    build_bath_a,
    build_bath_b,
    build_bath_c,
    build_bath_d,
    build_bath_e,
    build_hard_blockers_after_q2,
    DrudeStructuralMatch,
    Q1_HARD_BLOCKERS_INHERITED,
    Q2_TARGET_BLOCKER,
    Q2_FORBIDDEN_CLAIMS,
    TAU_EFF_COLLAPSE,
    TAU_EFF_COSMOLOGICAL,
    DRUDE_SPECTRAL_DENSITY,
    STRUCTURAL_IDENTITY,
    _validate_q2,
)


# ================================================================
# Test Class: Master Result
# ================================================================

class TestQ2MasterResult:
    """Test the master Q2 assessment result."""

    def setup_method(self):
        self.result = run_q2_assessment()

    def test_valid(self):
        assert self.result.valid is True

    def test_executive(self):
        assert self.result.executive_determination == "best_physical_bath_identified"

    def test_best_candidate_is_c(self):
        assert self.result.best_candidate == "C"

    def test_classification(self):
        assert self.result.q2_classification == "bath_specification_program"

    def test_blocker_partially_sharpened(self):
        assert self.result.q2_blocker_resolution_level == "partially_sharpened"

    def test_q2_targets_bath_blocker(self):
        assert self.result.q2_blocker_addressed == "bath_dof_unspecified"

    def test_five_bath_candidates(self):
        assert len(self.result.bath_candidates) == 5

    def test_drude_match_present(self):
        assert self.result.drude_match is not None
        assert self.result.drude_match.structural_match is True

    def test_has_safe_claims(self):
        assert len(self.result.safe_claims) >= 5

    def test_has_unsafe_claims(self):
        assert len(self.result.unsafe_claims) >= 5

    def test_has_hard_blockers(self):
        assert len(self.result.hard_blockers_after_q2) >= 5

    def test_has_nonclaims(self):
        assert len(self.result.nonclaims) >= 5

    def test_q1_blockers_inherited(self):
        assert len(self.result.q1_blockers_inherited) >= 5
        assert "no_born_rule" in self.result.q1_blockers_inherited


# ================================================================
# Test Class: Drude Structural Match
# ================================================================

class TestDrudeMatch:
    """Test the Drude/Lorentzian structural match analysis."""

    def setup_method(self):
        self.match = DrudeStructuralMatch()

    def test_structural_match_true(self):
        assert self.match.structural_match is True

    def test_match_strength_not_derivational(self):
        assert self.match.match_strength == "structural_not_derivational"

    def test_implies_drude_bath(self):
        text = self.match.implies_bath_type.lower()
        assert "drude" in text or "single-pole" in text or "ohmic" in text

    def test_does_not_imply_list(self):
        """Must explicitly list what the match does NOT imply."""
        assert len(self.match.does_not_imply) >= 3

    def test_existence_caveat(self):
        """Must explicitly caveat that match ≠ existence proof."""
        caveats = " ".join(self.match.does_not_imply).lower()
        assert "existence" in caveats or "proof" in caveats

    def test_resonance_condition_documented(self):
        assert "equilibrium" in self.match.resonance_condition.lower()

    def test_dispersion_connection_documented(self):
        assert "dispersion" in self.match.dispersion_connection.lower()


# ================================================================
# Test Class: Bath C (Best Candidate)
# ================================================================

class TestBathC:
    """Test Bath C: Self-bath / Drude internal memory substructure."""

    def setup_method(self):
        self.bath = build_bath_c()

    def test_status_best(self):
        assert self.bath.status == "best_q2_candidate"

    def test_passes_q2_criteria(self):
        assert self.bath.passes_q2_criteria() is True

    def test_physically_motivated(self):
        assert self.bath.is_physically_motivated is True

    def test_reduction_viable(self):
        assert self.bath.reduction_map is not None
        assert self.bath.reduction_map.is_viable() is True

    def test_reduction_complete_schematic(self):
        assert self.bath.reduction_map.assessment == "complete_schematic"

    def test_approximately_markovian(self):
        assert self.bath.markovian_status == "approximately_markovian"

    def test_tau_as_susceptibility(self):
        assert self.bath.reduction_map.tau_interpretation == \
               "effective_susceptibility_timescale"

    def test_tau_interpretable(self):
        assert self.bath.tau_interpretable is True

    def test_assumptions_mild(self):
        assert self.bath.assumption_severity == "mild"

    def test_canon_compatible(self):
        assert self.bath.canon_compatibility is not None
        assert self.bath.canon_compatibility.is_compatible() is True

    def test_has_structural_blockers(self):
        assert len(self.bath.structural_blockers) >= 3

    def test_has_nonclaims(self):
        assert len(self.bath.nonclaims) >= 3

    def test_drude_mentioned_in_label(self):
        assert "Drude" in self.bath.label or "Self-Bath" in self.bath.label

    def test_spectral_modes_in_integrated_out(self):
        assert "fast" in self.bath.integrated_out_dof.lower() or \
               "mode" in self.bath.integrated_out_dof.lower()


# ================================================================
# Test Class: Bath A (Gravitational)
# ================================================================

class TestBathA:
    """Test Bath A: Gravitational-sector bath."""

    def setup_method(self):
        self.bath = build_bath_a()

    def test_status_viable(self):
        assert self.bath.status == "viable_but_underdetermined"

    def test_passes_q2_criteria(self):
        assert self.bath.passes_q2_criteria() is True

    def test_physically_motivated(self):
        assert self.bath.is_physically_motivated is True

    def test_reduction_partial(self):
        assert self.bath.reduction_map.assessment == "partial_schematic"

    def test_approximately_markovian(self):
        assert self.bath.markovian_status == "approximately_markovian"

    def test_canon_compatible(self):
        assert self.bath.canon_compatibility.is_compatible() is True

    def test_assumption_severity_moderate(self):
        assert self.bath.assumption_severity == "moderate"


# ================================================================
# Test Class: Bath B (Matter-Coupled) — Should Be Weak
# ================================================================

class TestBathB:
    """Test Bath B: Matter-coupled bath (should be weak)."""

    def setup_method(self):
        self.bath = build_bath_b()

    def test_status_weak(self):
        assert self.bath.status == "formally_possible_but_physically_weak"

    def test_fails_q2_criteria(self):
        assert self.bath.passes_q2_criteria() is False

    def test_not_physically_motivated(self):
        assert self.bath.is_physically_motivated is False

    def test_reduction_formal_only(self):
        assert self.bath.reduction_map.assessment == "formal_only"

    def test_assumption_severity_major(self):
        assert self.bath.assumption_severity == "major"

    def test_canon_tension(self):
        assert self.bath.canon_compatibility.assessment == "tension"


# ================================================================
# Test Class: Bath D (Mixed)
# ================================================================

class TestBathD:
    """Test Bath D: Mixed bath."""

    def setup_method(self):
        self.bath = build_bath_d()

    def test_status_viable(self):
        assert self.bath.status == "viable_but_underdetermined"

    def test_passes_q2_criteria(self):
        assert self.bath.passes_q2_criteria() is True

    def test_reduction_partial(self):
        assert self.bath.reduction_map.assessment == "partial_schematic"

    def test_assumption_severity_moderate(self):
        assert self.bath.assumption_severity == "moderate"


# ================================================================
# Test Class: Bath E (No Bath) — Formal Shell
# ================================================================

class TestBathE:
    """Test Bath E: No physical bath (formal shell only)."""

    def setup_method(self):
        self.bath = build_bath_e()

    def test_status_weak(self):
        assert self.bath.status == "formally_possible_but_physically_weak"

    def test_fails_q2_criteria(self):
        assert self.bath.passes_q2_criteria() is False

    def test_not_physically_motivated(self):
        assert self.bath.is_physically_motivated is False

    def test_no_reduction_map(self):
        assert self.bath.reduction_map is None

    def test_canon_compatible(self):
        """Bath E should be canon-compatible (it doesn't change anything)."""
        assert self.bath.canon_compatibility.is_compatible() is True


# ================================================================
# Test Class: Reduction Maps
# ================================================================

class TestReductionMaps:
    """Test reduction map viability and content."""

    def test_bath_c_reduction_viable(self):
        bath = build_bath_c()
        assert bath.reduction_map.is_viable() is True

    def test_bath_a_reduction_viable(self):
        bath = build_bath_a()
        assert bath.reduction_map.is_viable() is True

    def test_bath_b_reduction_not_viable(self):
        bath = build_bath_b()
        assert bath.reduction_map.is_viable() is False

    def test_bath_c_identifies_eliminated_dof(self):
        bath = build_bath_c()
        assert "fast" in bath.reduction_map.eliminated_dof.lower()

    def test_bath_c_explains_first_order(self):
        bath = build_bath_c()
        assert len(bath.reduction_map.why_first_order) > 50

    def test_bath_c_tau_is_susceptibility(self):
        bath = build_bath_c()
        assert bath.reduction_map.tau_interpretation == \
               "effective_susceptibility_timescale"

    def test_bath_a_tau_is_damping(self):
        bath = build_bath_a()
        assert bath.reduction_map.tau_interpretation == "damping_timescale"


# ================================================================
# Test Class: Markovian Audit
# ================================================================

class TestMarkovianAudit:
    """Test Markovian vs memory classification."""

    def test_bath_c_approximately_markovian(self):
        bath = build_bath_c()
        assert bath.markovian_status == "approximately_markovian"

    def test_bath_a_approximately_markovian(self):
        bath = build_bath_a()
        assert bath.markovian_status == "approximately_markovian"

    def test_bath_b_unclear(self):
        bath = build_bath_b()
        assert bath.markovian_status == "unclear"

    def test_bath_e_unclear(self):
        bath = build_bath_e()
        assert bath.markovian_status == "unclear"

    def test_bath_c_has_markovian_justification(self):
        bath = build_bath_c()
        assert len(bath.markovian_justification) > 30


# ================================================================
# Test Class: Canon Compatibility
# ================================================================

class TestCanonCompatibility:
    """Test canon compatibility assessments."""

    def test_bath_c_compatible(self):
        bath = build_bath_c()
        assert bath.canon_compatibility.is_compatible() is True
        assert bath.canon_compatibility.assessment == "compatible"

    def test_bath_b_tension(self):
        bath = build_bath_b()
        assert bath.canon_compatibility.assessment == "tension"
        assert bath.canon_compatibility.imports_inconsistent_ontology is True

    def test_all_preserve_constitutive_law(self):
        """All bath candidates must preserve the constitutive law."""
        for builder in [build_bath_a, build_bath_b, build_bath_c,
                        build_bath_d, build_bath_e]:
            bath = builder()
            assert bath.canon_compatibility.preserves_constitutive_law is True, \
                f"Bath {bath.name} does not preserve constitutive law"

    def test_none_require_failed_tensor_memory(self):
        for builder in [build_bath_a, build_bath_b, build_bath_c,
                        build_bath_d, build_bath_e]:
            bath = builder()
            assert bath.canon_compatibility.requires_failed_tensor_memory is False


# ================================================================
# Test Class: Hard Blockers After Q2
# ================================================================

class TestHardBlockersAfterQ2:
    """Test hard blocker inventory after Q2."""

    def setup_method(self):
        self.blockers = build_hard_blockers_after_q2()

    def test_at_least_five(self):
        assert len(self.blockers) >= 5

    def test_born_rule_survives(self):
        born = [b for b in self.blockers if b["name"] == "no_born_rule"]
        assert len(born) == 1
        assert born[0]["survives_q2"] is True

    def test_measurement_survives(self):
        meas = [b for b in self.blockers
                 if b["name"] == "no_measurement_coupling"]
        assert len(meas) == 1
        assert meas[0]["survives_q2"] is True

    def test_spectral_density_blocker_present(self):
        """Q2 should add a new blocker about spectral density."""
        spec = [b for b in self.blockers
                 if b["name"] == "spectral_density_not_derived"]
        assert len(spec) == 1
        assert spec[0]["type"] == "currently_missing_potentially_extendable"

    def test_noise_spectrum_blocker_present(self):
        """Q2 should identify noise spectrum as new blocker."""
        noise = [b for b in self.blockers
                  if b["name"] == "noise_spectrum_unknown"]
        assert len(noise) == 1

    def test_all_survive_q2(self):
        for b in self.blockers:
            assert b["survives_q2"] is True


# ================================================================
# Test Class: Forbidden Claims
# ================================================================

class TestForbiddenClaims:
    """Test that no forbidden claims are made."""

    def setup_method(self):
        self.result = run_q2_assessment()

    def test_blocker_not_fully_resolved(self):
        assert self.result.q2_blocker_resolution_level != "fully_resolved"

    def test_executive_in_allowed_set(self):
        allowed = {
            "best_physical_bath_identified",
            "several_viable_but_underdetermined",
            "only_formal_shell_survives",
            "no_defensible_bath",
        }
        assert self.result.executive_determination in allowed

    def test_classification_in_allowed_set(self):
        allowed = {
            "bath_specification_program",
            "reduction_clarification",
            "structured_extension",
            "speculative_horizon",
            "failure",
        }
        assert self.result.q2_classification in allowed

    def test_best_candidate_passes_criteria(self):
        for b in self.result.bath_candidates:
            if b.status == "best_q2_candidate":
                assert b.passes_q2_criteria() is True

    def test_unsafe_claims_include_key_prohibitions(self):
        unsafe_joined = " ".join(self.result.unsafe_claims).lower()
        assert "derived" in unsafe_joined or "first principles" in unsafe_joined
        assert "quantum" in unsafe_joined
        assert "appendix c" in unsafe_joined or "born" in unsafe_joined

    def test_forbidden_claims_list_complete(self):
        assert len(Q2_FORBIDDEN_CLAIMS) >= 8


# ================================================================
# Test Class: Validation Guard
# ================================================================

class TestValidationGuard:
    """Test that validation catches forbidden states."""

    def test_fully_resolved_raises(self):
        result = run_q2_assessment()
        result.q2_blocker_resolution_level = "fully_resolved"
        with pytest.raises(ValueError, match="CANNOT claim to fully resolve"):
            _validate_q2(result)

    def test_bad_executive_raises(self):
        result = run_q2_assessment()
        result.executive_determination = "quantum_bath_proven"
        with pytest.raises(ValueError, match="not in"):
            _validate_q2(result)

    def test_bad_classification_raises(self):
        result = run_q2_assessment()
        result.q2_classification = "complete_quantum_theory"
        with pytest.raises(ValueError, match="not in"):
            _validate_q2(result)

    def test_best_candidate_without_criteria_raises(self):
        result = run_q2_assessment()
        for b in result.bath_candidates:
            if b.name == "C":
                b.is_physically_motivated = False  # break criteria
        with pytest.raises(ValueError, match="does not pass"):
            _validate_q2(result)


# ================================================================
# Test Class: Constants
# ================================================================

class TestConstants:
    """Test locked constants and formulas."""

    def test_tau_eff_collapse_formula(self):
        assert "tau_0" in TAU_EFF_COLLAPSE
        assert "|V/R|" in TAU_EFF_COLLAPSE

    def test_tau_eff_cosmological_formula(self):
        assert "tau_0" in TAU_EFF_COSMOLOGICAL
        assert "H" in TAU_EFF_COSMOLOGICAL

    def test_drude_density_formula(self):
        assert "omega" in DRUDE_SPECTRAL_DENSITY
        assert "Omega" in DRUDE_SPECTRAL_DENSITY

    def test_structural_identity(self):
        assert "omega_0" in STRUCTURAL_IDENTITY
        assert "tau_eff" in STRUCTURAL_IDENTITY

    def test_q1_blockers_inherited(self):
        assert "no_born_rule" in Q1_HARD_BLOCKERS_INHERITED
        assert "bath_dof_unspecified" in Q1_HARD_BLOCKERS_INHERITED

    def test_q2_target_blocker(self):
        assert Q2_TARGET_BLOCKER == "bath_dof_unspecified"


# ================================================================
# Test Class: Export
# ================================================================

class TestExport:
    """Test dict/JSON export."""

    def setup_method(self):
        self.result = run_q2_assessment()

    def test_to_dict_returns_dict(self):
        d = self.result.to_dict()
        assert isinstance(d, dict)

    def test_has_required_keys(self):
        d = self.result.to_dict()
        required = [
            "executive_determination", "best_candidate", "drude_match",
            "bath_candidates", "hard_blockers_after_q2",
            "q2_blocker_addressed", "q2_blocker_resolution_level",
            "safe_claims", "unsafe_claims", "q2_classification",
            "nonclaims", "valid",
        ]
        for key in required:
            assert key in d, f"Missing key: {key}"

    def test_five_candidates_in_export(self):
        d = self.result.to_dict()
        assert len(d["bath_candidates"]) == 5

    def test_drude_match_in_export(self):
        d = self.result.to_dict()
        assert d["drude_match"]["structural_match"] is True

    def test_candidate_export_has_status(self):
        d = self.result.to_dict()
        for b in d["bath_candidates"]:
            assert "status" in b
            assert "passes_q2_criteria" in b
            assert "canon_compatible" in b
