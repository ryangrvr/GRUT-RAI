"""Tests for grut/skyrme_term_nativity_audit.py.

Deterministic test suite pinning:
  1. Allowed verdict label set (closed)
  2. Five derivation routes — status and properties
  3. Mexican hat vs Skyrme distinction (Derrick scaling)
  4. Three nativity criteria — all fail
  5. Doctrine compatibility checks
  6. Patchwork assessment
  7. Verdict assignment (primary + secondary)
  8. Top-level Boolean summary
  9. Forbidden inference firewall
 10. Nonclaims
 11. Cross-consistency checks
 12. End-to-end master audit
"""

import math
import pytest

from grut.skyrme_term_nativity_audit import (
    # Constants
    M_EXT,
    R_EQ,
    TAU_SQ,
    ALPHA_VAC,
    BETA_Q_CANON,
    OMEGA_0_SQ,
    OMEGA_0,
    X_EQ,
    SPATIAL_DIMENSION,
    DERRICK_KINETIC_EXPONENT,
    DERRICK_POTENTIAL_EXPONENT,
    DERRICK_SKYRME_EXPONENT,
    O3_KINETIC_DERIVATIVE_ORDER,
    O3_SKYRME_DERIVATIVE_ORDER,
    SKYRME_COUPLING_E,
    SKYRME_COUPLING_FIXED_BY_GRUT,
    ALLOWED_NATIVITY_VERDICTS,
    ALLOWED_ROUTE_STATUSES,
    ALLOWED_PATCHWORK_CLASSES,
    # Dataclasses
    DerivationRoute,
    DerrickScalingComparison,
    NativityCriterion,
    DoctrineCompatibilityCheck,
    PatchworkAssessment,
    SkyrmeTermNativityResult,
    # Functions
    build_route_1_constitutive_gradient_expansion,
    build_route_2_ctp_effective_action,
    build_route_3_o3_derivative_expansion,
    build_route_4_mexican_hat_potential,
    build_route_5_barrier_underdetermination,
    build_derrick_comparison,
    build_nativity_criteria,
    build_doctrine_compatibility,
    build_patchwork_assessment,
    assign_verdicts,
    run_skyrme_term_nativity_audit,
)


# ---------------------------------------------------------------------------
# Fixtures
# ---------------------------------------------------------------------------

@pytest.fixture(scope="module")
def audit() -> SkyrmeTermNativityResult:
    return run_skyrme_term_nativity_audit()


@pytest.fixture(scope="module")
def route1() -> DerivationRoute:
    return build_route_1_constitutive_gradient_expansion()


@pytest.fixture(scope="module")
def route2() -> DerivationRoute:
    return build_route_2_ctp_effective_action()


@pytest.fixture(scope="module")
def route3() -> DerivationRoute:
    return build_route_3_o3_derivative_expansion()


@pytest.fixture(scope="module")
def route4() -> DerivationRoute:
    return build_route_4_mexican_hat_potential()


@pytest.fixture(scope="module")
def route5() -> DerivationRoute:
    return build_route_5_barrier_underdetermination()


@pytest.fixture(scope="module")
def derrick() -> DerrickScalingComparison:
    return build_derrick_comparison()


@pytest.fixture(scope="module")
def doctrine() -> DoctrineCompatibilityCheck:
    return build_doctrine_compatibility()


@pytest.fixture(scope="module")
def all_routes():
    return [
        build_route_1_constitutive_gradient_expansion(),
        build_route_2_ctp_effective_action(),
        build_route_3_o3_derivative_expansion(),
        build_route_4_mexican_hat_potential(),
        build_route_5_barrier_underdetermination(),
    ]


@pytest.fixture(scope="module")
def criteria(all_routes):
    return build_nativity_criteria(all_routes)


@pytest.fixture(scope="module")
def patchwork(all_routes, criteria):
    return build_patchwork_assessment(all_routes, criteria)


# ===========================================================================
# Class 1: Constants
# ===========================================================================

class TestConstants:
    def test_m_ext(self):
        assert M_EXT == pytest.approx(0.5)

    def test_r_eq(self):
        assert R_EQ == pytest.approx(1.0 / 3.0)

    def test_tau_sq(self):
        assert TAU_SQ == pytest.approx(1.5)

    def test_alpha_vac(self):
        assert ALPHA_VAC == pytest.approx(1.0 / 3.0)

    def test_beta_q_canon(self):
        assert BETA_Q_CANON == pytest.approx(2.0)

    def test_omega_0_sq(self):
        assert OMEGA_0_SQ == pytest.approx(27.0)

    def test_omega_0(self):
        assert OMEGA_0 == pytest.approx(math.sqrt(27.0))

    def test_x_eq(self):
        assert X_EQ == pytest.approx(4.5)

    def test_spatial_dimension(self):
        assert SPATIAL_DIMENSION == 3

    def test_derrick_kinetic_exponent(self):
        """E_2 ~ lambda^{D-2} = lambda^1 in D=3."""
        assert DERRICK_KINETIC_EXPONENT == 1

    def test_derrick_potential_exponent(self):
        """E_V ~ lambda^D = lambda^3 in D=3 (field-space potential)."""
        assert DERRICK_POTENTIAL_EXPONENT == 3

    def test_derrick_skyrme_exponent(self):
        """E_4 ~ lambda^{D-4} = lambda^{-1} in D=3 (stabilizing)."""
        assert DERRICK_SKYRME_EXPONENT == -1

    def test_o3_kinetic_derivative_order(self):
        assert O3_KINETIC_DERIVATIVE_ORDER == 2

    def test_o3_skyrme_derivative_order(self):
        assert O3_SKYRME_DERIVATIVE_ORDER == 4

    def test_skyrme_coupling_is_none(self):
        """Skyrme coupling is not fixed by GRUT — must be None."""
        assert SKYRME_COUPLING_E is None

    def test_skyrme_coupling_not_fixed_by_grut(self):
        assert SKYRME_COUPLING_FIXED_BY_GRUT is False

    def test_derrick_potential_exponent_is_d(self):
        assert DERRICK_POTENTIAL_EXPONENT == SPATIAL_DIMENSION

    def test_derrick_kinetic_exponent_is_d_minus_2(self):
        assert DERRICK_KINETIC_EXPONENT == SPATIAL_DIMENSION - 2

    def test_derrick_skyrme_exponent_is_d_minus_4(self):
        assert DERRICK_SKYRME_EXPONENT == SPATIAL_DIMENSION - 4


# ===========================================================================
# Class 2: Allowed verdict label sets
# ===========================================================================

class TestAllowedLabelSets:
    EXPECTED_NATIVITY_VERDICTS = {
        "no_native_skyrme_support_found",
        "effective_skyrme_analog_possible",
        "native_higher_gradient_stabilizer_conditionally_supported",
        "requires_external_extension",
    }

    EXPECTED_ROUTE_STATUSES = {
        "established",
        "conditionally_open",
        "open_but_unbuilt",
        "not_established",
        "unexplored",
        "not_skyrme_analog",
        "compatible_but_undetermined",
    }

    EXPECTED_PATCHWORK_CLASSES = {
        "derives_from_native_architecture",
        "motivated_but_unbuilt",
        "compatible_but_ad_hoc",
        "incompatible_with_prior_doctrine",
    }

    def test_nativity_verdict_set_exact(self):
        assert ALLOWED_NATIVITY_VERDICTS == self.EXPECTED_NATIVITY_VERDICTS

    def test_nativity_verdict_count(self):
        assert len(ALLOWED_NATIVITY_VERDICTS) == 4

    def test_route_status_set_exact(self):
        assert ALLOWED_ROUTE_STATUSES == self.EXPECTED_ROUTE_STATUSES

    def test_patchwork_class_set_exact(self):
        assert ALLOWED_PATCHWORK_CLASSES == self.EXPECTED_PATCHWORK_CLASSES

    def test_no_native_support_present(self):
        assert "no_native_skyrme_support_found" in ALLOWED_NATIVITY_VERDICTS

    def test_effective_analog_possible_present(self):
        assert "effective_skyrme_analog_possible" in ALLOWED_NATIVITY_VERDICTS

    def test_conditionally_supported_present(self):
        assert "native_higher_gradient_stabilizer_conditionally_supported" in ALLOWED_NATIVITY_VERDICTS

    def test_requires_external_extension_present(self):
        assert "requires_external_extension" in ALLOWED_NATIVITY_VERDICTS

    def test_all_sets_are_frozensets(self):
        assert isinstance(ALLOWED_NATIVITY_VERDICTS, frozenset)
        assert isinstance(ALLOWED_ROUTE_STATUSES, frozenset)
        assert isinstance(ALLOWED_PATCHWORK_CLASSES, frozenset)


# ===========================================================================
# Class 3: Route 1 — Constitutive gradient expansion
# ===========================================================================

class TestRoute1ConstitutiveGradient:
    def test_route_id(self, route1):
        assert route1.route_id == 1

    def test_name(self, route1):
        assert route1.name == "constitutive_gradient_expansion"

    def test_status_is_not_established(self, route1):
        assert route1.status == "not_established"

    def test_is_established_false(self, route1):
        assert route1.is_established is False

    def test_is_open_false(self, route1):
        assert route1.is_open is False

    def test_skyrme_coupling_not_derivable(self, route1):
        assert route1.skyrme_coupling_derivable is False

    def test_source_module_mentions_tau_eff(self, route1):
        assert "tau_eff" in route1.source_module.lower() or \
               "constitutive" in route1.source_module.lower() or \
               "action_principle" in route1.source_module.lower()

    def test_mechanism_mentions_linear_ode(self, route1):
        mech = route1.mechanism.lower()
        assert "linear" in mech or "first-order" in mech

    def test_mechanism_mentions_no_quartic_from_linear(self, route1):
        mech = route1.mechanism.lower()
        assert "quartic" in mech or "l_4" in mech or "gradient" in mech

    def test_status_in_allowed_set(self, route1):
        assert route1.status in ALLOWED_ROUTE_STATUSES

    def test_prerequisite_unmet_nonempty(self, route1):
        assert route1.prerequisite_unmet is not None
        assert len(route1.prerequisite_unmet) > 0

    def test_notes_nonempty(self, route1):
        assert len(route1.notes) > 0


# ===========================================================================
# Class 4: Route 2 — Galley CTP effective action
# ===========================================================================

class TestRoute2CTPEffectiveAction:
    def test_route_id(self, route2):
        assert route2.route_id == 2

    def test_name(self, route2):
        assert route2.name == "ctp_effective_action"

    def test_status_is_open_but_unbuilt(self, route2):
        assert route2.status == "open_but_unbuilt"

    def test_is_established_false(self, route2):
        assert route2.is_established is False

    def test_is_open_true(self, route2):
        assert route2.is_open is True

    def test_skyrme_coupling_not_derivable(self, route2):
        assert route2.skyrme_coupling_derivable is False

    def test_mechanism_mentions_ctp(self, route2):
        mech = route2.mechanism.lower()
        assert "ctp" in mech or "galley" in mech or "closed-time-path" in mech

    def test_mechanism_mentions_g_minus(self, route2):
        mech = route2.mechanism.lower()
        assert "g_-" in mech or "g-" in mech or "minus" in mech

    def test_mechanism_mentions_equilibrium_vanishes(self, route2):
        mech = route2.mechanism.lower()
        assert "vanishes" in mech or "zero" in mech or "equilibrium" in mech

    def test_prerequisite_unmet_mentions_computation(self, route2):
        prereq = route2.prerequisite_unmet.lower()
        assert "computation" in prereq or "computed" in prereq or "one-loop" in prereq

    def test_status_in_allowed_set(self, route2):
        assert route2.status in ALLOWED_ROUTE_STATUSES


# ===========================================================================
# Class 5: Route 3 — O(3) derivative expansion (strongest route)
# ===========================================================================

class TestRoute3O3DerivativeExpansion:
    def test_route_id(self, route3):
        assert route3.route_id == 3

    def test_name(self, route3):
        assert route3.name == "o3_derivative_expansion"

    def test_status_is_conditionally_open(self, route3):
        """Route 3 is the strongest: conditionally open."""
        assert route3.status == "conditionally_open"

    def test_is_established_false(self, route3):
        """Not yet established — O(3) nativity is prerequisite."""
        assert route3.is_established is False

    def test_is_open_true(self, route3):
        assert route3.is_open is True

    def test_skyrme_coupling_not_yet_derivable(self, route3):
        """e is not fixed — N2 criterion fails."""
        assert route3.skyrme_coupling_derivable is False

    def test_mechanism_mentions_uniqueness(self, route3):
        mech = route3.mechanism.lower()
        assert "unique" in mech

    def test_mechanism_mentions_next_order(self, route3):
        mech = route3.mechanism.lower()
        assert "next" in mech or "next-order" in mech

    def test_mechanism_mentions_o3_eft(self, route3):
        mech = route3.mechanism.lower()
        assert "o(3)" in mech or "o3" in mech or "sigma model" in mech

    def test_prerequisite_unmet_mentions_o3_nativity(self, route3):
        prereq = route3.prerequisite_unmet.lower()
        assert "o(3)" in prereq or "o3" in prereq or "nativity" in prereq or "canon" in prereq

    def test_notes_mention_skyrme_reference(self, route3):
        combined = " ".join(route3.notes).lower()
        assert "skyrme" in combined

    def test_notes_mention_uniqueness(self, route3):
        combined = " ".join(route3.notes).lower()
        assert "unique" in combined

    def test_status_in_allowed_set(self, route3):
        assert route3.status in ALLOWED_ROUTE_STATUSES

    def test_route3_is_strongest_route(self, route3, route1, route2, route4, route5):
        """Route 3 is the only conditionally_open route — makes it strongest."""
        assert route3.status == "conditionally_open"
        assert route1.status != "conditionally_open"
        assert route2.status != "conditionally_open"
        assert route4.status != "conditionally_open"
        assert route5.status != "conditionally_open"


# ===========================================================================
# Class 6: Route 4 — Mexican hat potential (NOT a Skyrme analog)
# ===========================================================================

class TestRoute4MexicanHat:
    def test_route_id(self, route4):
        assert route4.route_id == 4

    def test_name(self, route4):
        assert "mexican_hat" in route4.name.lower() or "field_space" in route4.name.lower()

    def test_status_is_not_skyrme_analog(self, route4):
        """Critical: the Mexican hat is explicitly NOT a Skyrme analog."""
        assert route4.status == "not_skyrme_analog"

    def test_is_established_false(self, route4):
        assert route4.is_established is False

    def test_is_open_false(self, route4):
        assert route4.is_open is False

    def test_skyrme_coupling_not_derivable(self, route4):
        assert route4.skyrme_coupling_derivable is False

    def test_mechanism_mentions_field_space_vs_gradient(self, route4):
        mech = route4.mechanism.lower()
        assert "field space" in mech or "field-space" in mech or "gradient" in mech

    def test_mechanism_mentions_derrick_still_active(self, route4):
        mech = route4.mechanism.lower()
        assert "derrick" in mech or "positive" in mech or "collapse" in mech

    def test_mechanism_mentions_lambda_phi4(self, route4):
        mech = route4.mechanism.lower()
        assert "lambda" in mech or "mexican" in mech or "quartic" in mech

    def test_mechanism_shows_de_dlambda_positive(self, route4):
        """dE/dλ = E₂ + 3E_V > 0: no minimum, still collapses."""
        mech = route4.mechanism
        assert "E_2 + 3" in mech or "e_2 + 3" in mech.lower() or \
               ("positive" in mech.lower() and "collapse" in mech.lower())

    def test_source_module_mentions_defect_admissibility(self, route4):
        assert "defect_admissibility" in route4.source_module.lower()

    def test_notes_mention_forbidden_inference(self, route4):
        combined = " ".join(route4.notes).lower()
        assert "forbidden" in combined or "not" in combined

    def test_status_in_allowed_set(self, route4):
        assert route4.status in ALLOWED_ROUTE_STATUSES

    def test_prerequisite_unmet_is_none(self, route4):
        """Route 4 is not 'open' — there's no prerequisite that would fix it."""
        assert route4.prerequisite_unmet is None


# ===========================================================================
# Class 7: Route 5 — Barrier action underdetermination
# ===========================================================================

class TestRoute5BarrierUnderdetermination:
    def test_route_id(self, route5):
        assert route5.route_id == 5

    def test_name(self, route5):
        assert "barrier" in route5.name.lower() or "underdetermination" in route5.name.lower()

    def test_status_is_compatible_but_undetermined(self, route5):
        assert route5.status == "compatible_but_undetermined"

    def test_is_established_false(self, route5):
        assert route5.is_established is False

    def test_is_open_true(self, route5):
        assert route5.is_open is True

    def test_skyrme_coupling_not_derivable(self, route5):
        assert route5.skyrme_coupling_derivable is False

    def test_mechanism_mentions_equilibrium_source_degeneracy_theorem(self, route5):
        mech = route5.mechanism.lower()
        assert "degeneracy" in mech or "barrier_action_sector" in mech or \
               "underdetermination" in mech

    def test_mechanism_permits_but_does_not_derive(self, route5):
        mech = route5.mechanism.lower()
        assert "permits" in mech or "compatible" in mech
        assert "required" in mech or "require" in mech or "not required" in mech

    def test_source_module_mentions_barrier_action(self, route5):
        assert "barrier_action_sector" in route5.source_module.lower()

    def test_status_in_allowed_set(self, route5):
        assert route5.status in ALLOWED_ROUTE_STATUSES


# ===========================================================================
# Class 8: All routes structural checks
# ===========================================================================

class TestAllRoutes:
    def test_five_routes_defined(self, all_routes):
        assert len(all_routes) == 5

    def test_route_ids_are_1_through_5(self, all_routes):
        ids = [r.route_id for r in all_routes]
        assert sorted(ids) == [1, 2, 3, 4, 5]

    def test_no_route_is_established(self, all_routes):
        """Critical: no route produces a native Skyrme term."""
        assert not any(r.is_established for r in all_routes)

    def test_exactly_one_conditionally_open_route(self, all_routes):
        """Only Route 3 is conditionally_open."""
        cond_open = [r for r in all_routes if r.status == "conditionally_open"]
        assert len(cond_open) == 1
        assert cond_open[0].name == "o3_derivative_expansion"

    def test_at_least_two_open_but_unbuilt_routes(self, all_routes):
        """Routes 2 and 5 are open_but_unbuilt (plus compatible_but_undetermined)."""
        open_routes = [r for r in all_routes if r.is_open]
        assert len(open_routes) >= 2

    def test_no_skyrme_coupling_derivable_in_any_route(self, all_routes):
        """e is a free parameter — no route fixes it."""
        assert not any(r.skyrme_coupling_derivable for r in all_routes)

    def test_all_route_statuses_in_allowed_set(self, all_routes):
        for r in all_routes:
            assert r.status in ALLOWED_ROUTE_STATUSES, (
                f"Route {r.route_id} has invalid status '{r.status}'"
            )

    def test_all_routes_have_nonempty_mechanism(self, all_routes):
        for r in all_routes:
            assert r.mechanism, f"Route {r.route_id} has empty mechanism"

    def test_all_routes_have_nonempty_notes(self, all_routes):
        for r in all_routes:
            assert r.notes, f"Route {r.route_id} has empty notes"

    def test_route4_is_not_skyrme_analog(self, all_routes):
        r4 = next(r for r in all_routes if r.route_id == 4)
        assert r4.status == "not_skyrme_analog"

    def test_route3_is_only_conditionally_open(self, all_routes):
        for r in all_routes:
            if r.route_id != 3:
                assert r.status != "conditionally_open"


# ===========================================================================
# Class 9: Derrick scaling comparison
# ===========================================================================

class TestDerrickScalingComparison:
    def test_spatial_dimension_is_3(self, derrick):
        assert derrick.spatial_dimension == 3

    def test_kinetic_exponent(self, derrick):
        assert derrick.kinetic_exponent == 1

    def test_potential_exponent(self, derrick):
        """Mexican hat potential: E_V ~ lambda^3 in D=3."""
        assert derrick.potential_exponent == 3

    def test_skyrme_exponent(self, derrick):
        """Skyrme term: E_4 ~ lambda^{-1} in D=3 (stabilizing)."""
        assert derrick.skyrme_exponent == -1

    def test_mexican_hat_does_not_stabilize(self, derrick):
        """dE/dlambda = E_2 + 3*E_V > 0: no minimum."""
        assert derrick.mexican_hat_stabilizes is False

    def test_skyrme_stabilizes(self, derrick):
        """dE/dlambda = E_2 - E_4 = 0 at skyrmion radius: stable minimum."""
        assert derrick.skyrme_stabilizes is True

    def test_potential_stationarity_condition_shows_positive(self, derrick):
        cond = derrick.derrick_stationarity_condition_kinetic_potential
        assert "0" in cond or "positive" in cond.lower() or "no min" in cond.lower()

    def test_skyrme_stationarity_condition_shows_zero(self, derrick):
        cond = derrick.derrick_stationarity_condition_kinetic_skyrme
        assert "= 0" in cond or "stable" in cond.lower() or "minimum" in cond.lower()

    def test_verdict_mentions_not_skyrme_analog(self, derrick):
        assert "not_skyrme" in derrick.verdict.lower() or \
               "field_space" in derrick.verdict.lower()

    def test_verdict_mentions_derrick_still_active(self, derrick):
        assert "derrick" in derrick.verdict.lower() or "active" in derrick.verdict.lower()

    def test_notes_explain_opposite_scaling(self, derrick):
        combined = " ".join(derrick.notes).lower()
        assert "opposite" in combined or "negative" in combined or \
               "positive" in combined

    def test_potential_and_skyrme_have_opposite_signs(self, derrick):
        """Potential scales +3, Skyrme scales -1: opposite signs."""
        assert derrick.potential_exponent > 0
        assert derrick.skyrme_exponent < 0

    def test_kinetic_exponent_matches_constant(self, derrick):
        assert derrick.kinetic_exponent == DERRICK_KINETIC_EXPONENT

    def test_potential_exponent_matches_constant(self, derrick):
        assert derrick.potential_exponent == DERRICK_POTENTIAL_EXPONENT

    def test_skyrme_exponent_matches_constant(self, derrick):
        assert derrick.skyrme_exponent == DERRICK_SKYRME_EXPONENT


# ===========================================================================
# Class 10: Nativity criteria
# ===========================================================================

class TestNativityCriteria:
    def test_three_criteria_defined(self, criteria):
        assert len(criteria) == 3

    def test_criterion_ids_are_1_2_3(self, criteria):
        ids = [c.criterion_id for c in criteria]
        assert sorted(ids) == [1, 2, 3]

    def test_all_criteria_fail(self, criteria):
        """Critical: no nativity criterion is satisfied in current architecture."""
        assert not any(c.passes for c in criteria)

    def test_n1_derivability_fails(self, criteria):
        n1 = next(c for c in criteria if c.criterion_id == 1)
        assert n1.passes is False

    def test_n2_parameter_free_fails(self, criteria):
        n2 = next(c for c in criteria if c.criterion_id == 2)
        assert n2.passes is False

    def test_n3_architectural_origin_fails(self, criteria):
        n3 = next(c for c in criteria if c.criterion_id == 3)
        assert n3.passes is False

    def test_all_have_reason_for_failure(self, criteria):
        for c in criteria:
            if not c.passes:
                assert c.reason_for_failure is not None
                assert len(c.reason_for_failure) > 0

    def test_n1_mentions_o3_prerequisite(self, criteria):
        n1 = next(c for c in criteria if c.criterion_id == 1)
        reason = (n1.reason_for_failure or "").lower()
        assert "o(3)" in reason or "o3" in reason or "nativity" in reason or \
               "established" in reason

    def test_n2_mentions_free_parameter(self, criteria):
        n2 = next(c for c in criteria if c.criterion_id == 2)
        reason = (n2.reason_for_failure or "").lower()
        assert "free parameter" in reason or "coupling" in reason or "e" in reason

    def test_n3_mentions_architectural_specificity(self, criteria):
        n3 = next(c for c in criteria if c.criterion_id == 3)
        reason = (n3.reason_for_failure or "").lower()
        assert "grut" in reason or "specific" in reason or "architectural" in reason

    def test_all_have_conditional_path(self, criteria):
        """Each criterion has a path to satisfaction in future."""
        for c in criteria:
            assert c.conditional_path is not None
            assert len(c.conditional_path) > 0

    def test_n3_conditional_path_mentions_route_2(self, criteria):
        n3 = next(c for c in criteria if c.criterion_id == 3)
        path = (n3.conditional_path or "").lower()
        assert "ctp" in path or "route 2" in path or "g_-" in path or "route2" in path

    def test_n1_description_is_nonempty(self, criteria):
        for c in criteria:
            assert c.description, f"Criterion {c.criterion_id} has empty description"


# ===========================================================================
# Class 11: Doctrine compatibility
# ===========================================================================

class TestDoctrineCompatibility:
    def test_preserves_o3_symmetry(self, doctrine):
        assert doctrine.preserves_o3_symmetry is True

    def test_preserves_spherical_symmetry(self, doctrine):
        assert doctrine.preserves_spherical_symmetry is True

    def test_does_not_introduce_spinors(self, doctrine):
        assert doctrine.introduces_spinors is False

    def test_does_not_introduce_gauge_fields(self, doctrine):
        assert doctrine.introduces_gauge_fields is False

    def test_does_not_violate_tau_eff_domain(self, doctrine):
        assert doctrine.violates_tau_eff_domain is False

    def test_does_not_violate_beta_q_hypothesis(self, doctrine):
        assert doctrine.violates_beta_q_hypothesis is False

    def test_does_not_violate_phi_bifurcation(self, doctrine):
        assert doctrine.violates_phi_bifurcation is False

    def test_does_not_change_theory_class(self, doctrine):
        assert doctrine.changes_theory_class is False

    def test_introduces_new_free_parameter(self, doctrine):
        """Skyrme coupling e is a new free parameter — this is acknowledged."""
        assert doctrine.introduces_new_free_parameter is True

    def test_compatible_with_prior_doctrine(self, doctrine):
        """Despite the new parameter, adding L_4 is compatible."""
        assert doctrine.compatible_with_prior_doctrine is True

    def test_doctrine_impact_summary_nonempty(self, doctrine):
        assert len(doctrine.doctrine_impact_summary) > 0

    def test_doctrine_impact_mentions_compatible(self, doctrine):
        summary = doctrine.doctrine_impact_summary.lower()
        assert "compatible" in summary

    def test_doctrine_impact_mentions_new_parameter(self, doctrine):
        summary = doctrine.doctrine_impact_summary.lower()
        assert "parameter" in summary or "coupling" in summary or "e" in summary

    def test_notes_nonempty(self, doctrine):
        assert len(doctrine.notes) > 0


# ===========================================================================
# Class 12: Patchwork assessment
# ===========================================================================

class TestPatchworkAssessment:
    def test_does_not_derive_from_native_architecture(self, patchwork):
        assert patchwork.derives_from_native_architecture is False

    def test_is_motivated_but_unbuilt(self, patchwork):
        """Route 3 makes L_4 motivated — not pure patchwork."""
        assert patchwork.motivated_but_unbuilt is True

    def test_is_compatible_but_ad_hoc(self, patchwork):
        """If added NOW (before O(3) nativity): ad hoc."""
        assert patchwork.compatible_but_ad_hoc is True

    def test_not_incompatible_with_doctrine(self, patchwork):
        assert patchwork.incompatible_with_prior_doctrine is False

    def test_patchwork_verdict_is_motivated_but_unbuilt(self, patchwork):
        assert patchwork.patchwork_verdict == "motivated_but_unbuilt"

    def test_patchwork_verdict_in_allowed_set(self, patchwork):
        assert patchwork.patchwork_verdict in ALLOWED_PATCHWORK_CLASSES

    def test_condition_for_motivated_status_nonempty(self, patchwork):
        assert len(patchwork.condition_for_motivated_status) > 0

    def test_condition_mentions_o3_nativity(self, patchwork):
        cond = patchwork.condition_for_motivated_status.lower()
        assert "o(3)" in cond or "o3" in cond or "nativity" in cond

    def test_what_prevents_ad_hoc_nonempty(self, patchwork):
        assert len(patchwork.what_would_prevent_ad_hoc) > 0

    def test_what_prevents_ad_hoc_mentions_prerequisite_chain(self, patchwork):
        prereq = patchwork.what_would_prevent_ad_hoc.lower()
        assert "prerequisite" in prereq or "chain" in prereq or "step" in prereq

    def test_what_prevents_ad_hoc_mentions_coupling_matching(self, patchwork):
        prereq = patchwork.what_would_prevent_ad_hoc.lower()
        assert "coupling" in prereq or "e" in prereq or "parameter" in prereq


# ===========================================================================
# Class 13: Primary and secondary verdicts
# ===========================================================================

class TestVerdicts:
    def test_primary_verdict_is_no_native_support(self, audit):
        assert audit.primary_verdict == "no_native_skyrme_support_found"

    def test_secondary_verdict_is_effective_analog_possible(self, audit):
        assert audit.secondary_verdict == "effective_skyrme_analog_possible"

    def test_primary_verdict_in_allowed_set(self, audit):
        assert audit.primary_verdict in ALLOWED_NATIVITY_VERDICTS

    def test_secondary_verdict_in_allowed_set(self, audit):
        assert audit.secondary_verdict in ALLOWED_NATIVITY_VERDICTS

    def test_primary_is_not_native_conditionally_supported(self, audit):
        assert audit.primary_verdict != "native_higher_gradient_stabilizer_conditionally_supported"

    def test_primary_is_not_requires_external_extension(self, audit):
        """Route 3 (conditionally open) prevents the strictest verdict."""
        assert audit.primary_verdict != "requires_external_extension"

    def test_secondary_is_not_no_native_support(self, audit):
        assert audit.secondary_verdict != "no_native_skyrme_support_found"

    def test_verdict_pair_is_deterministic(self):
        """Running twice gives the same verdicts."""
        r1 = run_skyrme_term_nativity_audit()
        r2 = run_skyrme_term_nativity_audit()
        assert r1.primary_verdict == r2.primary_verdict
        assert r1.secondary_verdict == r2.secondary_verdict


# ===========================================================================
# Class 14: Top-level Boolean summary
# ===========================================================================

class TestTopLevelBooleans:
    def test_native_skyrme_support_not_found(self, audit):
        assert audit.native_skyrme_support_found is False

    def test_no_route_established(self, audit):
        assert audit.any_route_established is False

    def test_route_conditionally_open(self, audit):
        """Route 3 is conditionally open."""
        assert audit.any_route_conditionally_open is True

    def test_route_open_but_unbuilt(self, audit):
        """Routes 2 and 5 are open but unbuilt."""
        assert audit.any_route_open_but_unbuilt is True

    def test_mexican_hat_is_not_skyrme_analog(self, audit):
        assert audit.mexican_hat_is_not_skyrme_analog is True

    def test_skyrme_coupling_not_fixed_by_grut(self, audit):
        assert audit.skyrme_coupling_fixed_by_grut is False

    def test_not_all_nativity_criteria_pass(self, audit):
        assert audit.all_nativity_criteria_pass is False

    def test_doctrine_compatible(self, audit):
        assert audit.doctrine_compatible is True

    def test_strongest_route_is_o3_derivative_expansion(self, audit):
        assert audit.strongest_route_name == "o3_derivative_expansion"

    def test_strongest_route_status_is_conditionally_open(self, audit):
        assert audit.strongest_route_status == "conditionally_open"


# ===========================================================================
# Class 15: Forbidden inferences
# ===========================================================================

class TestForbiddenInferences:
    EXPECTED_INFERENCES = {
        "mexican_hat_potential_implies_skyrme_stabilization",
        "lambda_phi4_is_l4_gradient_quartic",
        "field_space_quartic_stabilizes_derrick",
        "barrier_underdetermination_derives_l4",
        "o3_topological_charge_implies_skyrme_term_present",
        "l4_compatible_therefore_l4_native",
        "adding_l4_is_patchwork_therefore_impossible",
        "no_native_support_means_l4_is_excluded_forever",
    }

    def test_all_expected_inferences_present(self, audit):
        for inf in self.EXPECTED_INFERENCES:
            assert inf in audit.forbidden_inferences, (
                f"Missing forbidden inference: {inf}"
            )

    def test_count_at_least_eight(self, audit):
        assert len(audit.forbidden_inferences) >= 8

    def test_mexican_hat_inference_present(self, audit):
        assert "mexican_hat_potential_implies_skyrme_stabilization" in audit.forbidden_inferences

    def test_l4_compatible_native_inference_present(self, audit):
        assert "l4_compatible_therefore_l4_native" in audit.forbidden_inferences

    def test_excluded_forever_inference_present(self, audit):
        assert "no_native_support_means_l4_is_excluded_forever" in audit.forbidden_inferences

    def test_field_space_quartic_inference_present(self, audit):
        assert "field_space_quartic_stabilizes_derrick" in audit.forbidden_inferences


# ===========================================================================
# Class 16: Nonclaims
# ===========================================================================

class TestNonclaims:
    def test_nonclaims_nonempty(self, audit):
        assert len(audit.nonclaims) > 0

    def test_at_least_six_nonclaims(self, audit):
        assert len(audit.nonclaims) >= 6

    def test_nonclaim_about_not_ruling_out_forever(self, audit):
        combined = " ".join(audit.nonclaims).lower()
        assert "ruling out" in combined or "not ruling" in combined or "forever" in combined

    def test_nonclaim_about_mexican_hat_not_skyrme(self, audit):
        combined = " ".join(audit.nonclaims).lower()
        assert "mexican" in combined or "field-space" in combined or \
               "field space" in combined or "lambda" in combined

    def test_nonclaim_about_coupling_not_excluded(self, audit):
        combined = " ".join(audit.nonclaims).lower()
        assert "coupling" in combined or "e cannot" in combined or \
               "parameter" in combined

    def test_nonclaim_about_compatibility_not_nativity(self, audit):
        combined = " ".join(audit.nonclaims).lower()
        assert "compatible" in combined

    def test_nonclaim_about_ctp_route_open(self, audit):
        combined = " ".join(audit.nonclaims).lower()
        assert "ctp" in combined or "galley" in combined or \
               "route" in combined or "loop" in combined

    def test_nonclaim_about_not_contradictory(self, audit):
        combined = " ".join(audit.nonclaims).lower()
        assert "contradictory" in combined or "contradiction" in combined or \
               "ad hoc" in combined or "compatible" in combined


# ===========================================================================
# Class 17: Diagnostics dict
# ===========================================================================

class TestDiagnosticsDict:
    def test_m_ext(self, audit):
        assert audit.diagnostics["M_EXT"] == pytest.approx(0.5)

    def test_r_eq(self, audit):
        assert audit.diagnostics["R_EQ"] == pytest.approx(1.0 / 3.0)

    def test_tau_sq(self, audit):
        assert audit.diagnostics["TAU_SQ"] == pytest.approx(1.5)

    def test_alpha_vac(self, audit):
        assert audit.diagnostics["ALPHA_VAC"] == pytest.approx(1.0 / 3.0)

    def test_omega_0_sq(self, audit):
        assert audit.diagnostics["OMEGA_0_SQ"] == pytest.approx(27.0)

    def test_spatial_dimension(self, audit):
        assert audit.diagnostics["SPATIAL_DIMENSION"] == 3

    def test_derrick_kinetic_exponent(self, audit):
        assert audit.diagnostics["DERRICK_KINETIC_EXPONENT"] == 1

    def test_derrick_potential_exponent(self, audit):
        assert audit.diagnostics["DERRICK_POTENTIAL_EXPONENT"] == 3

    def test_derrick_skyrme_exponent(self, audit):
        assert audit.diagnostics["DERRICK_SKYRME_EXPONENT"] == -1

    def test_skyrme_coupling_is_none(self, audit):
        assert audit.diagnostics["SKYRME_COUPLING_E"] is None

    def test_skyrme_coupling_not_fixed(self, audit):
        assert audit.diagnostics["SKYRME_COUPLING_FIXED_BY_GRUT"] is False

    def test_native_skyrme_support_false(self, audit):
        assert audit.diagnostics["native_skyrme_support_found"] is False

    def test_any_route_established_false(self, audit):
        assert audit.diagnostics["any_route_established"] is False

    def test_any_route_conditionally_open_true(self, audit):
        assert audit.diagnostics["any_route_conditionally_open"] is True

    def test_all_nativity_criteria_fail(self, audit):
        assert audit.diagnostics["all_nativity_criteria_pass"] is False

    def test_mexican_hat_not_analog(self, audit):
        assert audit.diagnostics["mexican_hat_is_not_skyrme_analog"] is True

    def test_barrier_permits_l4(self, audit):
        assert audit.diagnostics["barrier_underdetermination_permits_l4"] is True

    def test_doctrine_compatible_true(self, audit):
        assert audit.diagnostics["doctrine_compatible"] is True

    def test_theory_class_preserved(self, audit):
        assert audit.diagnostics["theory_class_preserved"] is True

    def test_introduces_new_parameter_true(self, audit):
        assert audit.diagnostics["introduces_new_free_parameter"] is True

    def test_patchwork_verdict_in_diagnostics(self, audit):
        assert audit.diagnostics["patchwork_verdict"] == "motivated_but_unbuilt"

    def test_strongest_route_in_diagnostics(self, audit):
        assert audit.diagnostics["strongest_route_name"] == "o3_derivative_expansion"

    def test_num_routes(self, audit):
        assert audit.diagnostics["num_routes"] == 5

    def test_num_criteria(self, audit):
        assert audit.diagnostics["num_nativity_criteria"] == 3

    def test_primary_verdict_in_diagnostics(self, audit):
        assert audit.diagnostics["primary_verdict"] == "no_native_skyrme_support_found"

    def test_secondary_verdict_in_diagnostics(self, audit):
        assert audit.diagnostics["secondary_verdict"] == "effective_skyrme_analog_possible"


# ===========================================================================
# Class 18: Cross-consistency checks
# ===========================================================================

class TestCrossConsistency:
    def test_no_established_route_consistent_with_primary_verdict(self, audit):
        """No established route → verdict is 'no_native_skyrme_support_found'."""
        assert not audit.any_route_established
        assert audit.primary_verdict == "no_native_skyrme_support_found"

    def test_conditionally_open_route_consistent_with_secondary_verdict(self, audit):
        """Route 3 conditionally open → secondary is 'effective_skyrme_analog_possible'."""
        assert audit.any_route_conditionally_open
        assert audit.secondary_verdict == "effective_skyrme_analog_possible"

    def test_mexican_hat_not_skyrme_consistent_with_potential_exponent(self, audit, derrick):
        """E_V ~ lambda^3 (positive) → Mexican hat doesn't stabilize."""
        assert derrick.potential_exponent == 3
        assert derrick.mexican_hat_stabilizes is False
        assert audit.mexican_hat_is_not_skyrme_analog is True

    def test_skyrme_exponent_negative_consistent_with_stabilization(self, derrick):
        """E_4 ~ lambda^{-1} (negative) → Skyrme stabilizes."""
        assert derrick.skyrme_exponent == -1
        assert derrick.skyrme_stabilizes is True

    def test_criteria_all_fail_consistent_with_no_native_support(self, audit, criteria):
        assert not any(c.passes for c in criteria)
        assert audit.all_nativity_criteria_pass is False
        assert audit.native_skyrme_support_found is False

    def test_skyrme_coupling_none_consistent_with_n2_failure(self, criteria):
        n2 = next(c for c in criteria if c.criterion_id == 2)
        assert n2.passes is False
        assert SKYRME_COUPLING_E is None
        assert SKYRME_COUPLING_FIXED_BY_GRUT is False

    def test_doctrine_compatible_consistent_with_patchwork_not_incompatible(self, audit, patchwork):
        assert audit.doctrine_compatible is True
        assert patchwork.incompatible_with_prior_doctrine is False

    def test_motivated_unbuilt_consistent_with_route3_open(self, audit, patchwork, route3):
        assert route3.is_open is True
        assert patchwork.motivated_but_unbuilt is True
        assert audit.primary_verdict == "no_native_skyrme_support_found"  # still no native

    def test_o3_kinetic_before_skyrme_in_derivative_order(self):
        """O(3) kinetic (2-derivative) comes before Skyrme (4-derivative)."""
        assert O3_KINETIC_DERIVATIVE_ORDER == 2
        assert O3_SKYRME_DERIVATIVE_ORDER == 4
        assert O3_KINETIC_DERIVATIVE_ORDER < O3_SKYRME_DERIVATIVE_ORDER

    def test_derrick_exponents_ordered_kinetic_gt_skyrme(self):
        """Kinetic exponent (1) > Skyrme exponent (-1): Skyrme opposes kinetic."""
        assert DERRICK_KINETIC_EXPONENT > DERRICK_SKYRME_EXPONENT

    def test_potential_exponent_gt_kinetic_gt_skyrme(self):
        """E_V ~ lambda^3, E_2 ~ lambda^1, E_4 ~ lambda^{-1}: all distinct."""
        assert DERRICK_POTENTIAL_EXPONENT > DERRICK_KINETIC_EXPONENT > DERRICK_SKYRME_EXPONENT

    def test_route3_source_module_mentions_defect_admissibility(self, route3):
        """Route 3 builds on Phase D1+ (defect_admissibility.py)."""
        assert "defect_admissibility" in route3.source_module.lower()

    def test_route5_source_module_mentions_barrier_action_sector(self, route5):
        assert "barrier_action_sector" in route5.source_module.lower()


# ===========================================================================
# Class 19: End-to-end master audit
# ===========================================================================

class TestMasterAudit:
    def test_returns_correct_type(self, audit):
        assert isinstance(audit, SkyrmeTermNativityResult)

    def test_five_routes_in_master(self, audit):
        assert len(audit.routes) == 5

    def test_derrick_comparison_populated(self, audit):
        assert isinstance(audit.derrick_comparison, DerrickScalingComparison)

    def test_three_nativity_criteria_in_master(self, audit):
        assert len(audit.nativity_criteria) == 3

    def test_doctrine_check_populated(self, audit):
        assert isinstance(audit.doctrine_check, DoctrineCompatibilityCheck)

    def test_patchwork_populated(self, audit):
        assert isinstance(audit.patchwork, PatchworkAssessment)

    def test_nonclaims_is_list(self, audit):
        assert isinstance(audit.nonclaims, list)

    def test_forbidden_inferences_is_list(self, audit):
        assert isinstance(audit.forbidden_inferences, list)

    def test_diagnostics_is_dict(self, audit):
        assert isinstance(audit.diagnostics, dict)

    def test_full_deterministic_summary(self, audit):
        """Pin every top-level Boolean and key string in one test."""
        assert audit.native_skyrme_support_found is False
        assert audit.any_route_established is False
        assert audit.any_route_conditionally_open is True
        assert audit.any_route_open_but_unbuilt is True
        assert audit.mexican_hat_is_not_skyrme_analog is True
        assert audit.skyrme_coupling_fixed_by_grut is False
        assert audit.all_nativity_criteria_pass is False
        assert audit.doctrine_compatible is True
        assert audit.strongest_route_name == "o3_derivative_expansion"
        assert audit.strongest_route_status == "conditionally_open"
        assert audit.primary_verdict == "no_native_skyrme_support_found"
        assert audit.secondary_verdict == "effective_skyrme_analog_possible"
        assert audit.patchwork.patchwork_verdict == "motivated_but_unbuilt"

    def test_audit_is_idempotent(self):
        r1 = run_skyrme_term_nativity_audit()
        r2 = run_skyrme_term_nativity_audit()
        assert r1.primary_verdict == r2.primary_verdict
        assert r1.secondary_verdict == r2.secondary_verdict
        assert r1.native_skyrme_support_found == r2.native_skyrme_support_found
        assert r1.all_nativity_criteria_pass == r2.all_nativity_criteria_pass
        assert r1.patchwork.patchwork_verdict == r2.patchwork.patchwork_verdict
        assert r1.strongest_route_name == r2.strongest_route_name
