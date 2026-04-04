"""Tests for GRUT Appendix D — Thermodynamic Properties of the GRUT Interior.

Verifies:
1. Master result construction and classification
2. Candidate temperature definitions and convergence
3. Entropy analysis (area-law proxy + memory correction)
4. First law consistency test
5. Entropy production monotonicity test
6. FDT compatibility test
7. Thermodynamic translation map
8. Hard blocker inventory
9. Forbidden-claim blocking
10. Validation guards
11. Export to dict
12. Appendix C boundary preservation
"""

import math
import pytest

from grut.thermodynamic_sector import (
    run_thermodynamic_audit,
    build_candidate_temperatures,
    build_temperature_audit,
    audit_temperature_convergence,
    analyze_entropy,
    test_first_law,
    test_entropy_production,
    test_fdt_compatibility,
    build_translation_map,
    build_hard_blockers_after_thermo,
    _validate_thermo,
    _ref_bh_quantities,
    EXECUTIVE_CLASSIFICATIONS,
    TEMPERATURE_CLASSIFICATIONS,
    ENTROPY_CLASSIFICATIONS,
    FIRST_LAW_CLASSIFICATIONS,
    ENTROPY_PRODUCTION_CLASSIFICATIONS,
    FDT_CLASSIFICATIONS,
    THERMO_FORBIDDEN_CLAIMS,
    ALPHA_VAC,
    BETA_Q,
    EPSILON_Q,
    R_EQ_OVER_RS,
    OMEGA_0_TAU_IDENTITY,
    G_SI,
    C_SI,
    HBAR_SI,
    K_B,
    L_PLANCK,
    M_REF_KG,
    ThermoResult,
)


# ================================================================
# Test Class: Master Result
# ================================================================

class TestThermoMasterResult:
    """Test the master thermodynamic audit result."""

    def setup_method(self):
        self.result = run_thermodynamic_audit()

    def test_valid(self):
        assert self.result.valid is True

    def test_executive(self):
        assert self.result.executive_determination == "thermodynamic_sector_partially_consistent"

    def test_executive_in_allowed(self):
        assert self.result.executive_determination in EXECUTIVE_CLASSIFICATIONS

    def test_temperature_classification(self):
        assert self.result.temperature_classification in TEMPERATURE_CLASSIFICATIONS

    def test_entropy_classification(self):
        assert self.result.entropy_classification in ENTROPY_CLASSIFICATIONS

    def test_first_law_classification(self):
        assert self.result.first_law_classification in FIRST_LAW_CLASSIFICATIONS

    def test_entropy_production_classification(self):
        assert self.result.entropy_production_classification in ENTROPY_PRODUCTION_CLASSIFICATIONS

    def test_fdt_classification(self):
        assert self.result.fdt_classification in FDT_CLASSIFICATIONS

    def test_has_safe_claims(self):
        assert len(self.result.safe_claims) >= 5

    def test_has_unsafe_claims(self):
        assert len(self.result.unsafe_claims) >= 5

    def test_has_nonclaims(self):
        assert len(self.result.nonclaims) >= 5

    def test_has_hard_blockers(self):
        assert len(self.result.hard_blockers_after_thermo) >= 8


# ================================================================
# Test Class: Candidate Temperatures
# ================================================================

class TestCandidateTemperatures:
    """Test candidate temperature definitions."""

    def setup_method(self):
        self.candidates = build_candidate_temperatures()

    def test_at_least_3_candidates(self):
        assert len(self.candidates) >= 3

    def test_at_least_4_candidates(self):
        assert len(self.candidates) >= 4

    def test_all_have_formula(self):
        for c in self.candidates:
            assert len(c.formula) > 0

    def test_all_have_positive_temperature(self):
        for c in self.candidates:
            assert c.T_kelvin_at_ref > 0

    def test_surface_gravity_present(self):
        names = [c.name for c in self.candidates]
        assert "T_surface_gravity" in names

    def test_dissipation_present(self):
        names = [c.name for c in self.candidates]
        assert "T_dissipation" in names

    def test_structural_present(self):
        names = [c.name for c in self.candidates]
        assert "T_structural" in names

    def test_hawking_present_as_comparison(self):
        names = [c.name for c in self.candidates]
        assert "T_hawking" in names

    def test_at_least_2_grut_native(self):
        native = [c for c in self.candidates if c.grut_native]
        assert len(native) >= 2

    def test_hawking_not_grut_native(self):
        hawking = [c for c in self.candidates if c.name == "T_hawking"][0]
        assert hawking.grut_native is False

    def test_dissipation_is_grut_native(self):
        diss = [c for c in self.candidates if c.name == "T_dissipation"][0]
        assert diss.grut_native is True

    def test_structural_is_grut_native(self):
        struct = [c for c in self.candidates if c.name == "T_structural"][0]
        assert struct.grut_native is True

    def test_T_structural_equals_Q_times_T_dissipation(self):
        diss = [c for c in self.candidates if c.name == "T_dissipation"][0]
        struct = [c for c in self.candidates if c.name == "T_structural"][0]
        Q = 6.0
        ratio = struct.T_kelvin_at_ref / diss.T_kelvin_at_ref
        assert abs(ratio - Q) < 0.01


# ================================================================
# Test Class: Temperature Convergence
# ================================================================

class TestTemperatureConvergence:
    """Test temperature convergence analysis."""

    def setup_method(self):
        self.audit = build_temperature_audit()

    def test_convergence_tested(self):
        assert self.audit.convergence.candidates_tested >= 2

    def test_converged_within_order_of_magnitude(self):
        assert self.audit.convergence.converged is True

    def test_convergence_factor_is_Q(self):
        # T_structural / T_dissipation = Q ~ 6
        assert abs(self.audit.convergence.convergence_factor - 6.0) < 0.01

    def test_classification_definable(self):
        assert self.audit.classification == "temperature_definable_but_not_uniquely_derived"

    def test_best_candidate_is_dissipation(self):
        assert self.audit.best_candidate == "T_dissipation"

    def test_has_best_candidate_reason(self):
        assert len(self.audit.best_candidate_reason) > 0

    def test_n_grut_native_at_least_2(self):
        assert self.audit.n_grut_native >= 2

    def test_n_imported_at_least_1(self):
        assert self.audit.n_imported >= 1


# ================================================================
# Test Class: Entropy Analysis
# ================================================================

class TestEntropyAnalysis:
    """Test entropy analysis at the GRUT endpoint."""

    def setup_method(self):
        self.entropy = analyze_entropy()

    def test_area_law_formula(self):
        assert "R_eq" in self.entropy.area_law_formula
        assert "l_P" in self.entropy.area_law_formula

    def test_S_BH_positive(self):
        assert self.entropy.S_BH_at_ref > 0

    def test_S_BH_huge(self):
        # For 30 Msun BH, S_BH ~ 10^79
        assert self.entropy.S_BH_at_ref > 1e70

    def test_memory_correction_positive(self):
        assert self.entropy.memory_correction_sign == "positive"

    def test_memory_correction_comparable(self):
        assert self.entropy.memory_correction_magnitude == "comparable"

    def test_classification(self):
        assert self.entropy.classification == "area_law_modified_by_memory"

    def test_has_nonclaims(self):
        assert len(self.entropy.nonclaims) >= 3

    def test_nonclaims_mention_proxy(self):
        all_nc = " ".join(self.entropy.nonclaims).lower()
        assert "proxy" in all_nc


# ================================================================
# Test Class: First Law Test
# ================================================================

class TestFirstLaw:
    """Test the first law consistency check."""

    def setup_method(self):
        self.fl = test_first_law()

    def test_uses_dissipation_temperature(self):
        assert self.fl.temperature_candidate == "T_dissipation"

    def test_classification_partially_consistent(self):
        assert self.fl.classification == "first_law_partially_consistent"

    def test_first_law_satisfied(self):
        assert self.fl.first_law_satisfied is True

    def test_ratio_near_unity(self):
        # The residual should mention a ratio near 1
        assert "1.2" in self.fl.residual_description or "1.1" in self.fl.residual_description

    def test_has_conditionality(self):
        assert len(self.fl.conditionality) > 0
        assert "Conditional" in self.fl.conditionality

    def test_dM_formula_nonempty(self):
        assert len(self.fl.dM_formula) > 0

    def test_TdS_formula_nonempty(self):
        assert len(self.fl.TdS_formula) > 0

    def test_classification_in_allowed(self):
        assert self.fl.classification in FIRST_LAW_CLASSIFICATIONS


# ================================================================
# Test Class: Entropy Production
# ================================================================

class TestEntropyProduction:
    """Test entropy production during collapse."""

    def setup_method(self):
        self.ep = test_entropy_production()

    def test_area_decreases(self):
        assert self.ep.area_decreases_during_collapse is True

    def test_memory_produces_entropy(self):
        assert self.ep.memory_dissipation_produces_entropy is True

    def test_classification_underdetermined(self):
        assert self.ep.classification == "underdetermined"

    def test_S_ratio_is_one_ninth(self):
        # R_eq = r_s/3, so (R_eq/r_s)^2 = 1/9
        assert abs(self.ep.S_ratio - 1.0/9.0) < 0.01

    def test_has_interpretation(self):
        assert len(self.ep.interpretation) > 0

    def test_interpretation_mentions_horizon(self):
        assert "horizon" in self.ep.interpretation.lower()


# ================================================================
# Test Class: FDT Compatibility
# ================================================================

class TestFDTCompatibility:
    """Test fluctuation-dissipation compatibility."""

    def setup_method(self):
        self.fdt = test_fdt_compatibility()

    def test_requires_temperature(self):
        assert self.fdt.requires_temperature is True

    def test_noise_form_determined(self):
        assert self.fdt.noise_form_determined_up_to_T is True

    def test_classification_conditional(self):
        assert self.fdt.classification == "fdt_conditional_on_temperature"

    def test_has_noise_formula(self):
        assert len(self.fdt.fdt_noise_formula) > 0
        assert "Lorentzian" in self.fdt.fdt_noise_formula or "tau" in self.fdt.fdt_noise_formula

    def test_has_dissipation_kernel(self):
        assert "exp" in self.fdt.dissipation_kernel

    def test_has_drude_density(self):
        assert "Omega" in self.fdt.drude_spectral_density

    def test_has_observable_consequence(self):
        assert len(self.fdt.observable_consequence) > 0

    def test_classification_in_allowed(self):
        assert self.fdt.classification in FDT_CLASSIFICATIONS


# ================================================================
# Test Class: Translation Map
# ================================================================

class TestTranslationMap:
    """Test the GRUT-to-thermodynamic translation map."""

    def setup_method(self):
        self.tm = build_translation_map()

    def test_has_entries(self):
        assert len(self.tm.entries) >= 6

    def test_all_entries_have_grut_quantity(self):
        for e in self.tm.entries:
            assert "grut_quantity" in e
            assert len(e["grut_quantity"]) > 0

    def test_all_entries_have_thermo_quantity(self):
        for e in self.tm.entries:
            assert "thermo_quantity" in e
            assert len(e["thermo_quantity"]) > 0

    def test_all_entries_have_status(self):
        for e in self.tm.entries:
            assert "status" in e

    def test_omega_0_mapped(self):
        grut_qs = " ".join(e["grut_quantity"] for e in self.tm.entries)
        assert "omega_0" in grut_qs

    def test_quality_factor_mapped(self):
        grut_qs = " ".join(e["grut_quantity"] for e in self.tm.entries)
        assert "Q" in grut_qs or "quality" in grut_qs.lower()


# ================================================================
# Test Class: Hard Blockers
# ================================================================

class TestHardBlockers:
    """Test hard blockers after thermodynamic audit."""

    def setup_method(self):
        self.blockers = build_hard_blockers_after_thermo()

    def test_at_least_10(self):
        assert len(self.blockers) >= 10

    def test_temperature_blocker(self):
        names = [b["name"] for b in self.blockers]
        assert "temperature_not_uniquely_derived" in names

    def test_entropy_blocker(self):
        names = [b["name"] for b in self.blockers]
        assert "entropy_is_proxy" in names

    def test_hawking_blocker(self):
        names = [b["name"] for b in self.blockers]
        assert "no_hawking_radiation" in names

    def test_information_blocker(self):
        names = [b["name"] for b in self.blockers]
        assert "information_paradox_unsolved" in names

    def test_born_rule_blocker(self):
        names = [b["name"] for b in self.blockers]
        assert "no_born_rule" in names

    def test_measurement_blocker(self):
        names = [b["name"] for b in self.blockers]
        assert "no_measurement_coupling" in names

    def test_all_survive(self):
        for b in self.blockers:
            assert b["survives_thermo"] is True

    def test_noise_conditional(self):
        names = [b["name"] for b in self.blockers]
        assert "noise_spectrum_conditional" in names

    def test_second_law_underdetermined(self):
        names = [b["name"] for b in self.blockers]
        assert "generalized_second_law_underdetermined" in names


# ================================================================
# Test Class: Forbidden Claims
# ================================================================

class TestForbiddenClaims:
    """Test that forbidden claims are blocked."""

    def setup_method(self):
        self.result = run_thermodynamic_audit()

    def test_forbidden_list_exists(self):
        assert len(THERMO_FORBIDDEN_CLAIMS) >= 8

    def test_hawking_forbidden(self):
        assert "derives_hawking_radiation" in THERMO_FORBIDDEN_CLAIMS

    def test_information_forbidden(self):
        assert "solves_information_paradox" in THERMO_FORBIDDEN_CLAIMS

    def test_unitarity_forbidden(self):
        assert "proves_unitarity" in THERMO_FORBIDDEN_CLAIMS

    def test_imports_forbidden(self):
        assert "imports_standard_bh_thermo_as_grut" in THERMO_FORBIDDEN_CLAIMS

    def test_safe_claims_no_hawking(self):
        for claim in self.result.safe_claims:
            low = claim.lower()
            assert "hawking radiation is derived" not in low

    def test_safe_claims_no_information_paradox(self):
        for claim in self.result.safe_claims:
            low = claim.lower()
            assert "information paradox is solved" not in low

    def test_safe_claims_no_unitarity(self):
        for claim in self.result.safe_claims:
            low = claim.lower()
            assert "unitarity is proven" not in low


# ================================================================
# Test Class: Validation Guard
# ================================================================

class TestValidationGuard:
    """Test the validation guard against overclaims."""

    def test_valid_result_passes(self):
        result = run_thermodynamic_audit()
        _validate_thermo(result)

    def test_bad_executive_raises(self):
        result = run_thermodynamic_audit()
        result.executive_determination = "thermodynamic_breakthrough"
        with pytest.raises(ValueError, match="not in"):
            _validate_thermo(result)

    def test_bad_temperature_classification_raises(self):
        result = run_thermodynamic_audit()
        result.temperature_classification = "temperature_proven"
        with pytest.raises(ValueError, match="not in"):
            _validate_thermo(result)

    def test_bad_entropy_classification_raises(self):
        result = run_thermodynamic_audit()
        result.entropy_classification = "entropy_exact"
        with pytest.raises(ValueError, match="not in"):
            _validate_thermo(result)

    def test_bad_first_law_classification_raises(self):
        result = run_thermodynamic_audit()
        result.first_law_classification = "first_law_proven"
        with pytest.raises(ValueError, match="not in"):
            _validate_thermo(result)

    def test_too_few_nonclaims_raises(self):
        result = run_thermodynamic_audit()
        result.nonclaims = ["one"]
        with pytest.raises(ValueError, match="at least 5"):
            _validate_thermo(result)

    def test_too_few_blockers_raises(self):
        result = run_thermodynamic_audit()
        result.hard_blockers_after_thermo = [{"name": "one"}]
        with pytest.raises(ValueError, match="at least 8"):
            _validate_thermo(result)

    def test_too_few_candidates_raises(self):
        result = run_thermodynamic_audit()
        result.temperature_audit.candidates = result.temperature_audit.candidates[:2]
        with pytest.raises(ValueError, match="at least 3"):
            _validate_thermo(result)


# ================================================================
# Test Class: Nonclaims
# ================================================================

class TestNonclaims:
    """Test nonclaim content."""

    def setup_method(self):
        self.result = run_thermodynamic_audit()

    def test_at_least_5_nonclaims(self):
        assert len(self.result.nonclaims) >= 5

    def test_nonclaims_mention_hawking(self):
        all_nc = " ".join(self.result.nonclaims).lower()
        assert "hawking" in all_nc

    def test_nonclaims_mention_information(self):
        all_nc = " ".join(self.result.nonclaims).lower()
        assert "information" in all_nc

    def test_nonclaims_mention_unitarity(self):
        all_nc = " ".join(self.result.nonclaims).lower()
        assert "unitarity" in all_nc or "unitary" in all_nc

    def test_nonclaims_mention_appendix_c(self):
        all_nc = " ".join(self.result.nonclaims).lower()
        assert "appendix c" in all_nc

    def test_nonclaims_mention_conditional(self):
        all_nc = " ".join(self.result.nonclaims).lower()
        assert "conditional" in all_nc


# ================================================================
# Test Class: Export
# ================================================================

class TestExport:
    """Test dict export."""

    def setup_method(self):
        self.result = run_thermodynamic_audit()
        self.d = self.result.to_dict()

    def test_has_executive(self):
        assert "executive_determination" in self.d

    def test_has_temperature_audit(self):
        assert "temperature_audit" in self.d
        assert "candidates" in self.d["temperature_audit"]

    def test_has_entropy(self):
        assert "entropy_analysis" in self.d

    def test_has_first_law(self):
        assert "first_law_test" in self.d

    def test_has_fdt(self):
        assert "fdt_compatibility" in self.d

    def test_valid_in_export(self):
        assert self.d["valid"] is True

    def test_has_blockers(self):
        assert len(self.d["hard_blockers_after_thermo"]) >= 8


# ================================================================
# Test Class: Appendix C Boundary
# ================================================================

class TestAppendixCBoundary:
    """Verify Appendix C blockers preserved through thermodynamic audit."""

    def setup_method(self):
        self.result = run_thermodynamic_audit()

    def test_born_rule_blocked(self):
        names = [b["name"] for b in self.result.hard_blockers_after_thermo]
        assert "no_born_rule" in names

    def test_measurement_blocked(self):
        names = [b["name"] for b in self.result.hard_blockers_after_thermo]
        assert "no_measurement_coupling" in names

    def test_interference_blocked(self):
        names = [b["name"] for b in self.result.hard_blockers_after_thermo]
        assert "no_interference_formalism" in names

    def test_particle_ontology_blocked(self):
        names = [b["name"] for b in self.result.hard_blockers_after_thermo]
        assert "no_particle_ontology" in names

    def test_nonclaims_reference_appendix_c(self):
        all_nc = " ".join(self.result.nonclaims).lower()
        assert "appendix c" in all_nc


# ================================================================
# Test Class: Reference BH Quantities
# ================================================================

class TestRefBHQuantities:
    """Test the reference BH quantity computation."""

    def setup_method(self):
        self.ref = _ref_bh_quantities()

    def test_R_eq_is_rs_over_3(self):
        ratio = self.ref["R_eq"] / self.ref["r_s"]
        assert abs(ratio - 1.0/3.0) < 1e-10

    def test_omega_0_tau_identity(self):
        product = self.ref["omega_0"] * self.ref["tau_eff"]
        assert abs(product - 1.0) < 1e-10

    def test_T_hawking_positive(self):
        assert self.ref["T_hawking"] > 0

    def test_Q_canonical(self):
        assert self.ref["Q_canonical"] == 6.0

    def test_S_BH_positive(self):
        assert self.ref["S_BH"] > 0


# ================================================================
# Test Class: Constants
# ================================================================

class TestConstants:
    """Test module constants."""

    def test_alpha_vac(self):
        assert abs(ALPHA_VAC - 1.0/3.0) < 1e-10

    def test_beta_q(self):
        assert BETA_Q == 2.0

    def test_epsilon_q(self):
        assert abs(EPSILON_Q - 1.0/9.0) < 1e-10

    def test_r_eq_over_rs(self):
        assert abs(R_EQ_OVER_RS - 1.0/3.0) < 1e-10

    def test_structural_identity(self):
        assert OMEGA_0_TAU_IDENTITY == 1.0

    def test_planck_length(self):
        assert L_PLANCK > 1e-36
        assert L_PLANCK < 1e-34
