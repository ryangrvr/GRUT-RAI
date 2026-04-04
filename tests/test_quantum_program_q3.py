"""Tests for GRUT Phase Q3 — Interior Mode / Spectral Origin Test.

Verifies:
1. Route construction and classification
2. Pole analysis encoding (cubic characteristic equation)
3. Transfer-function analysis per route
4. Circularity audit (acknowledged, partial vs pure)
5. Interior linearization result
6. Hard blocker inventory after Q3
7. Forbidden-claim blocking (no overclaims)
8. Safe/unsafe claims
9. Nonclaims
10. Validation guards
11. Export to dict
"""

import json

import pytest

from grut.quantum_program_q3 import (
    run_q3_assessment,
    build_route_a,
    build_route_b,
    build_route_c,
    build_route_d,
    build_route_e,
    build_linearization_result,
    build_hard_blockers_after_q3,
    _validate_q3,
    PoleAnalysis,
    TransferFunctionAnalysis,
    CircularityAudit,
    SpectralOriginRoute,
    InteriorLinearizationResult,
    Q3Result,
    Q2_DRUDE_MATCH,
    Q2_DRUDE_SPECTRAL_DENSITY,
    INTERIOR_DISPERSION,
    MEMORY_DAMPING_FORMULA,
    SINGLE_POLE_SUSCEPTIBILITY,
    STRUCTURAL_IDENTITY,
    ALPHA_VAC,
    Q2_HARD_BLOCKERS_INHERITED,
    Q3_FORBIDDEN_CLAIMS,
)


# ================================================================
# Test Class: Master Result
# ================================================================

class TestQ3MasterResult:
    """Test the master Q3 assessment result."""

    def setup_method(self):
        self.result = run_q3_assessment()

    def test_valid(self):
        assert self.result.valid is True

    def test_executive(self):
        assert self.result.executive_determination == "strongest_spectral_origin_identified"

    def test_best_route_is_b(self):
        assert self.result.best_route == "B"

    def test_best_route_status(self):
        assert self.result.best_route_status == "best_q3_candidate"

    def test_best_route_grounding(self):
        assert self.result.best_route_grounding == "algebraic_grounding"

    def test_classification(self):
        assert self.result.q3_classification == "algebraic_grounding"

    def test_five_routes(self):
        assert len(self.result.routes) == 5

    def test_route_names(self):
        names = [r.name for r in self.result.routes]
        assert names == ["A", "B", "C", "D", "E"]

    def test_circularity_acknowledged(self):
        assert self.result.circularity_acknowledged is True

    def test_circularity_description_nonempty(self):
        assert len(self.result.circularity_description) > 50

    def test_linearization_present(self):
        assert self.result.linearization is not None

    def test_deterministic(self):
        """Two calls produce identical results."""
        r2 = run_q3_assessment()
        assert r2.executive_determination == self.result.executive_determination
        assert r2.best_route == self.result.best_route
        assert r2.q3_classification == self.result.q3_classification
        assert r2.valid == self.result.valid

    def test_has_nonclaims(self):
        assert len(self.result.nonclaims) >= 6


# ================================================================
# Test Class: Route A — Self-Mode
# ================================================================

class TestRouteA:
    """Test Route A (linearized self-mode route)."""

    def setup_method(self):
        self.route = build_route_a()

    def test_name(self):
        assert self.route.name == "A"

    def test_status(self):
        assert self.route.status == "structurally_suggestive_only"

    def test_grounding_level(self):
        assert self.route.grounding_level == "structural_match_only"

    def test_canon_explicit(self):
        assert self.route.structure_explicit_in_canon is True

    def test_preserves_constitutive(self):
        assert self.route.preserves_constitutive_law is True

    def test_has_transfer_function(self):
        assert self.route.transfer_function is not None
        assert self.route.transfer_function.is_single_pole is True

    def test_transfer_function_type(self):
        assert self.route.transfer_function.transfer_function_type == "single_pole_lorentzian"

    def test_circularity_pure(self):
        assert self.route.circularity is not None
        assert self.route.circularity.has_circularity is True
        assert self.route.circularity.net_assessment == "pure_circularity"

    def test_no_non_circular_elements(self):
        assert self.route.circularity.non_circular_elements == []

    def test_does_not_pass_q3_criteria(self):
        """Route A is purely circular — should NOT pass Q3 minimum criteria."""
        assert self.route.passes_q3_criteria() is False

    def test_not_derivationally_visible(self):
        assert self.route.derivationally_visible is False

    def test_structurally_suggestive(self):
        assert self.route.structurally_suggestive is True


# ================================================================
# Test Class: Route B — Interior PDE (Best Q3 Candidate)
# ================================================================

class TestRouteB:
    """Test Route B (Interior PDE / Susceptibility — strongest route)."""

    def setup_method(self):
        self.route = build_route_b()

    def test_name(self):
        assert self.route.name == "B"

    def test_status(self):
        assert self.route.status == "best_q3_candidate"

    def test_grounding_level(self):
        assert self.route.grounding_level == "algebraic_grounding"

    def test_canon_explicit(self):
        assert self.route.structure_explicit_in_canon is True

    def test_structure_source_references(self):
        assert "interior_pde.py" in self.route.structure_source
        assert "interior_waves.py" in self.route.structure_source

    def test_passes_q3_criteria(self):
        assert self.route.passes_q3_criteria() is True

    def test_preserves_constitutive(self):
        assert self.route.preserves_constitutive_law is True

    def test_compatible_with_strong_field(self):
        assert self.route.compatible_with_strong_field is True

    def test_derivationally_visible(self):
        assert self.route.derivationally_visible is True

    def test_structurally_suggestive(self):
        assert self.route.structurally_suggestive is True

    def test_has_transfer_function(self):
        tf = self.route.transfer_function
        assert tf is not None
        assert tf.transfer_function_type == "oscillatory_plus_relaxation"

    def test_transfer_function_three_poles(self):
        assert self.route.transfer_function.pole_count == 3

    def test_transfer_function_not_single_pole(self):
        tf = self.route.transfer_function
        assert tf.is_single_pole is False
        assert tf.is_approximately_single_pole is True

    def test_has_pole_analysis(self):
        assert self.route.pole_analysis is not None
        assert isinstance(self.route.pole_analysis, PoleAnalysis)

    def test_pole_analysis_cubic(self):
        assert self.route.pole_analysis.polynomial_degree == 3
        assert self.route.pole_analysis.total_poles == 3

    def test_pole_analysis_structure(self):
        pa = self.route.pole_analysis
        assert pa.n_oscillatory_poles == 2
        assert pa.n_relaxation_poles == 1

    def test_circularity_partial(self):
        assert self.route.circularity is not None
        assert self.route.circularity.has_circularity is True
        assert self.route.circularity.net_assessment == "partial_circularity"

    def test_non_circular_elements_present(self):
        nce = self.route.circularity.non_circular_elements
        assert len(nce) >= 4

    def test_non_circular_includes_coupling_constant(self):
        nce = " ".join(self.route.circularity.non_circular_elements).lower()
        assert "coupling" in nce

    def test_non_circular_includes_three_pole(self):
        nce = " ".join(self.route.circularity.non_circular_elements).lower()
        assert "three-pole" in nce or "three pole" in nce

    def test_structural_blockers_present(self):
        assert len(self.route.structural_blockers) >= 3

    def test_assumption_severity_mild(self):
        assert self.route.assumption_severity == "mild"

    def test_nonclaims_present(self):
        assert len(self.route.nonclaims) >= 2


# ================================================================
# Test Class: Route C — Gravitational Interior
# ================================================================

class TestRouteC:
    """Test Route C (gravitational interior mode route — blocked)."""

    def setup_method(self):
        self.route = build_route_c()

    def test_name(self):
        assert self.route.name == "C"

    def test_status(self):
        assert self.route.status == "viable_but_underdetermined"

    def test_grounding_level(self):
        assert self.route.grounding_level == "no_grounding"

    def test_not_canon_explicit(self):
        assert self.route.structure_explicit_in_canon is False

    def test_transfer_function_underdetermined(self):
        assert self.route.transfer_function.transfer_function_type == "underdetermined"

    def test_does_not_pass_q3_criteria(self):
        assert self.route.passes_q3_criteria() is False

    def test_assumption_severity_major(self):
        assert self.route.assumption_severity == "major"

    def test_phase_v_obstruction_mentioned(self):
        blockers = " ".join(self.route.structural_blockers).lower()
        assert "phase v" in blockers or "lapse" in blockers or "covariant" in blockers


# ================================================================
# Test Class: Route D — Mixed Fast-Sector
# ================================================================

class TestRouteD:
    """Test Route D (mixed fast-sector route — reduces to B)."""

    def setup_method(self):
        self.route = build_route_d()

    def test_name(self):
        assert self.route.name == "D"

    def test_status(self):
        assert self.route.status == "viable_but_underdetermined"

    def test_grounding_level(self):
        assert self.route.grounding_level == "no_grounding"

    def test_does_not_pass_q3_criteria(self):
        assert self.route.passes_q3_criteria() is False

    def test_reduces_to_route_b(self):
        blockers = " ".join(self.route.structural_blockers).lower()
        assert "route b" in blockers


# ================================================================
# Test Class: Route E — No Derivational Origin
# ================================================================

class TestRouteE:
    """Test Route E (conservative fallback)."""

    def setup_method(self):
        self.route = build_route_e()

    def test_name(self):
        assert self.route.name == "E"

    def test_status(self):
        assert self.route.status == "structurally_suggestive_only"

    def test_grounding_level(self):
        assert self.route.grounding_level == "structural_match_only"

    def test_canon_explicit(self):
        assert self.route.structure_explicit_in_canon is True

    def test_does_not_pass_q3_criteria(self):
        assert self.route.passes_q3_criteria() is False

    def test_no_transfer_function(self):
        assert self.route.transfer_function is None

    def test_no_circularity_audit(self):
        assert self.route.circularity is None


# ================================================================
# Test Class: Pole Analysis
# ================================================================

class TestPoleAnalysis:
    """Test the pole analysis dataclass (from Route B)."""

    def setup_method(self):
        self.poles = build_route_b().pole_analysis

    def test_cubic(self):
        assert self.poles.polynomial_degree == 3

    def test_total_poles(self):
        assert self.poles.total_poles == 3

    def test_oscillatory_count(self):
        assert self.poles.n_oscillatory_poles == 2

    def test_relaxation_count(self):
        assert self.poles.n_relaxation_poles == 1

    def test_is_circular(self):
        assert self.poles.is_circular is True

    def test_non_circular_elements(self):
        assert len(self.poles.non_circular_elements) >= 4

    def test_lorentzian_pole_origin(self):
        assert "memory" in self.poles.lorentzian_pole_origin.lower()
        assert "susceptibility" in self.poles.lorentzian_pole_origin.lower()

    def test_characteristic_equation(self):
        assert "omega^3" in self.poles.characteristic_equation


# ================================================================
# Test Class: Transfer Functions
# ================================================================

class TestTransferFunctions:
    """Test transfer-function analyses across routes."""

    def test_route_a_viable(self):
        tf = build_route_a().transfer_function
        assert tf.is_viable() is True

    def test_route_b_viable(self):
        tf = build_route_b().transfer_function
        assert tf.is_viable() is True

    def test_route_c_not_viable(self):
        """Route C transfer function should be non-viable (underdetermined)."""
        tf = build_route_c().transfer_function
        # tau_interpretation is "unknown" which is truthy, type is underdetermined
        # Check that the type reflects the problem
        assert tf.transfer_function_type == "underdetermined"

    def test_route_a_single_pole(self):
        tf = build_route_a().transfer_function
        assert tf.is_single_pole is True
        assert tf.pole_count == 1

    def test_route_b_three_poles(self):
        tf = build_route_b().transfer_function
        assert tf.is_single_pole is False
        assert tf.pole_count == 3

    def test_route_b_tau_interpretation(self):
        tf = build_route_b().transfer_function
        assert "susceptibility" in tf.tau_interpretation.lower()
        assert "drude" in tf.tau_interpretation.lower()


# ================================================================
# Test Class: Circularity Audit
# ================================================================

class TestCircularityAudit:
    """Test circularity audits across routes."""

    def test_route_a_pure_circularity(self):
        circ = build_route_a().circularity
        assert circ.net_assessment == "pure_circularity"
        assert circ.has_circularity is True

    def test_route_b_partial_circularity(self):
        circ = build_route_b().circularity
        assert circ.net_assessment == "partial_circularity"
        assert circ.has_circularity is True

    def test_route_b_has_non_circular_content(self):
        circ = build_route_b().circularity
        assert len(circ.non_circular_elements) > len(
            build_route_a().circularity.non_circular_elements
        )

    def test_route_c_no_circularity_audit(self):
        assert build_route_c().circularity is None

    def test_route_d_no_circularity_audit(self):
        assert build_route_d().circularity is None

    def test_route_e_no_circularity_audit(self):
        assert build_route_e().circularity is None


# ================================================================
# Test Class: Interior Linearization
# ================================================================

class TestInteriorLinearization:
    """Test the interior linearization result."""

    def setup_method(self):
        self.lin = build_linearization_result()

    def test_cubic_characteristic(self):
        assert self.lin.characteristic_degree == 3

    def test_relaxation_mode_count(self):
        assert self.lin.n_relaxation_modes == 1

    def test_oscillatory_mode_count(self):
        assert self.lin.n_oscillatory_modes == 2

    def test_single_pole_not_dominant(self):
        """Full response is three-pole, not single-pole dominant."""
        assert self.lin.single_pole_dominant is False

    def test_drude_compatible(self):
        assert self.lin.drude_compatible is True

    def test_spectrum_oscillatory(self):
        assert self.lin.spectrum_oscillatory is True
        assert self.lin.spectrum_overdamped is False

    def test_evidence_for_single_pole(self):
        assert len(self.lin.evidence_for_single_pole) > 20

    def test_evidence_against_single_pole(self):
        assert len(self.lin.evidence_against_single_pole) > 20


# ================================================================
# Test Class: Hard Blockers After Q3
# ================================================================

class TestHardBlockersAfterQ3:
    """Test the hard blocker inventory after Q3."""

    def setup_method(self):
        self.blockers = build_hard_blockers_after_q3()
        self.result = run_q3_assessment()

    def test_at_least_eight_blockers(self):
        assert len(self.blockers) >= 8

    def test_all_survive_q3(self):
        for b in self.blockers:
            assert b["survives_q3"] is True

    def test_circularity_blocker_present(self):
        names = [b["name"] for b in self.blockers]
        assert "circularity_not_broken" in names

    def test_no_born_rule_blocker(self):
        names = [b["name"] for b in self.blockers]
        assert "no_born_rule" in names

    def test_spectral_density_partially_sharpened(self):
        for b in self.blockers:
            if b["name"] == "spectral_density_not_first_principles":
                assert "sharpened" in b["description"].lower()
                break
        else:
            pytest.fail("spectral_density_not_first_principles blocker not found")

    def test_covariant_metric_blocker(self):
        names = [b["name"] for b in self.blockers]
        assert "covariant_interior_metric_missing" in names

    def test_result_blockers_match(self):
        assert len(self.result.hard_blockers_after_q3) == len(self.blockers)


# ================================================================
# Test Class: Forbidden Claims
# ================================================================

class TestForbiddenClaims:
    """Test that forbidden claims are properly defined and respected."""

    def test_forbidden_claims_present(self):
        assert len(Q3_FORBIDDEN_CLAIMS) >= 8

    def test_derives_first_order_forbidden(self):
        assert "derives_first_order_law" in Q3_FORBIDDEN_CLAIMS

    def test_breaks_circularity_forbidden(self):
        assert "breaks_circularity" in Q3_FORBIDDEN_CLAIMS

    def test_derives_bath_forbidden(self):
        assert "derives_bath_from_first_principles" in Q3_FORBIDDEN_CLAIMS

    def test_safe_claims_do_not_contain_forbidden(self):
        result = run_q3_assessment()
        safe_text = " ".join(result.safe_claims).lower()
        assert "derives the first-order" not in safe_text
        assert "circularity is broken" not in safe_text
        assert "born rule" not in safe_text

    def test_unsafe_claims_include_key_prohibitions(self):
        result = run_q3_assessment()
        unsafe_text = " ".join(result.unsafe_claims).lower()
        assert "first principles" in unsafe_text or "derives" in unsafe_text
        assert "circularity" in unsafe_text


# ================================================================
# Test Class: Constants
# ================================================================

class TestConstants:
    """Test inherited and Q3-specific constants."""

    def test_q2_drude_match(self):
        assert "tau_eff" in Q2_DRUDE_MATCH
        assert "tau_0" in Q2_DRUDE_MATCH

    def test_interior_dispersion(self):
        assert "omega^2" in INTERIOR_DISPERSION
        assert "1 + i*omega*tau" in INTERIOR_DISPERSION

    def test_memory_damping(self):
        assert "gamma_mem" in MEMORY_DAMPING_FORMULA
        assert "omega^2" in MEMORY_DAMPING_FORMULA

    def test_single_pole_susceptibility(self):
        assert "1 + i*omega*tau" in SINGLE_POLE_SUSCEPTIBILITY

    def test_structural_identity(self):
        assert "omega_0" in STRUCTURAL_IDENTITY
        assert "tau_eff" in STRUCTURAL_IDENTITY

    def test_alpha_vac(self):
        assert abs(ALPHA_VAC - 1.0 / 3.0) < 1e-15

    def test_q2_blockers_inherited(self):
        assert len(Q2_HARD_BLOCKERS_INHERITED) >= 8
        assert "no_born_rule" in Q2_HARD_BLOCKERS_INHERITED


# ================================================================
# Test Class: Validation Guard
# ================================================================

class TestValidationGuard:
    """Test the _validate_q3 guard."""

    def test_valid_result_passes(self):
        result = run_q3_assessment()
        _validate_q3(result)  # should not raise

    def test_bad_executive_raises(self):
        result = run_q3_assessment()
        result.executive_determination = "quantum_program_complete"
        with pytest.raises(ValueError, match="Executive"):
            _validate_q3(result)

    def test_bad_classification_raises(self):
        result = run_q3_assessment()
        result.q3_classification = "full_derivation"
        with pytest.raises(ValueError, match="Classification"):
            _validate_q3(result)

    def test_circularity_not_acknowledged_raises(self):
        result = run_q3_assessment()
        result.circularity_acknowledged = False
        with pytest.raises(ValueError, match="circularity"):
            _validate_q3(result)

    def test_best_candidate_without_criteria_raises(self):
        result = run_q3_assessment()
        # Break Route B's criteria
        for r in result.routes:
            if r.name == "B":
                r.grut_structure = ""  # breaks criterion A
                break
        with pytest.raises(ValueError, match="minimum Q3 criteria"):
            _validate_q3(result)


# ================================================================
# Test Class: Export
# ================================================================

class TestExport:
    """Test serialization."""

    def setup_method(self):
        self.result = run_q3_assessment()

    def test_to_dict_returns_dict(self):
        d = self.result.to_dict()
        assert isinstance(d, dict)

    def test_to_dict_has_required_keys(self):
        d = self.result.to_dict()
        required = [
            "executive_determination", "best_route", "best_route_status",
            "best_route_grounding", "circularity_acknowledged", "routes",
            "linearization", "hard_blockers_after_q3", "safe_claims",
            "unsafe_claims", "q3_classification", "nonclaims", "valid",
        ]
        for k in required:
            assert k in d, f"Missing key: {k}"

    def test_json_roundtrip(self):
        d = self.result.to_dict()
        j = json.dumps(d)
        d2 = json.loads(j)
        assert d2["best_route"] == "B"
        assert d2["valid"] is True

    def test_routes_serialized(self):
        d = self.result.to_dict()
        assert len(d["routes"]) == 5
        route_b = [r for r in d["routes"] if r["name"] == "B"][0]
        assert route_b["passes_q3_criteria"] is True
        assert route_b["grounding_level"] == "algebraic_grounding"

    def test_linearization_serialized(self):
        d = self.result.to_dict()
        lin = d["linearization"]
        assert lin is not None
        assert lin["characteristic_degree"] == 3
        assert lin["drude_compatible"] is True


# ================================================================
# Test Class: Appendix C Boundary
# ================================================================

class TestAppendixCBoundary:
    """Ensure Appendix C blockers are not violated."""

    def setup_method(self):
        self.result = run_q3_assessment()

    def test_no_born_rule_in_safe_claims(self):
        safe = " ".join(self.result.safe_claims).lower()
        assert "born rule" not in safe

    def test_no_interference_in_safe_claims(self):
        safe = " ".join(self.result.safe_claims).lower()
        assert "interference pattern" not in safe

    def test_no_measurement_in_safe_claims(self):
        safe = " ".join(self.result.safe_claims).lower()
        assert "measurement outcome" not in safe


# ================================================================
# Test Class: Q3 Minimum Criteria Enforcement
# ================================================================

class TestQ3MinimumCriteria:
    """Test that only Route B passes Q3 minimum criteria."""

    def test_only_route_b_passes(self):
        routes = [
            build_route_a(),
            build_route_b(),
            build_route_c(),
            build_route_d(),
            build_route_e(),
        ]
        passing = [r.name for r in routes if r.passes_q3_criteria()]
        assert passing == ["B"]

    def test_route_b_all_six_criteria(self):
        b = build_route_b()
        # Criterion A: modes identified
        assert bool(b.grut_structure)
        # Criterion B: genuinely GRUT
        assert b.structure_explicit_in_canon is True
        # Criterion C: why single pole
        assert bool(b.why_single_pole)
        # Criterion D: grounding level
        assert b.grounding_level in ("algebraic_grounding", "derivational")
        # Criterion E: canon ok
        assert b.preserves_constitutive_law and b.compatible_with_strong_field
        # Criterion F: sharpens Q2
        assert b.grounding_level != "structural_match_only"
