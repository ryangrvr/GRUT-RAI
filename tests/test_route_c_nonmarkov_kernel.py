"""Unit tests for Route C non-Markov kernel test (grut/route_c_nonmarkov_kernel.py).

Tests that the source profile locking theorem holds for all tested kernel
classes, and that no non-Markov kernel can generate 1/r^2 Component B support.
10 test classes, ~57 tests.
"""

from __future__ import annotations

import math
import pytest

from grut.route_c_nonmarkov_kernel import (
    compute_route_c_nonmarkov_assessment,
    route_c_nonmarkov_result_to_dict,
    recover_markov_baseline,
    define_kernel_classes,
    prove_source_profile_locking,
    compute_kernel_support_profiles,
    assess_spectral_richness,
    assess_component_b_compatibility,
    assess_localizability,
    assess_physical_promotability,
    classify_nonmarkov_route_c,
    RouteCNonMarkovParams,
    ALPHA_VAC,
    R_S,
    M_EXT,
    R_EQ,
    TAU_CANONICAL,
    A_CRIT,
    EPSILON_RC_COEFF,
    COMP_B_COEFF,
    RHO_EQ_COEFF,
    N_KERNEL_CLASSES,
    COMPONENT_B_TARGET_EXPONENT,
    LOCKED_SPATIAL_EXPONENT,
    NONCLAIMS,
    NONMARKOV_ASSUMPTIONS,
)


# ================================================================
# Module-scoped fixtures
# ================================================================

@pytest.fixture(scope="module")
def params():
    return RouteCNonMarkovParams(n_r=500, n_t=200)


@pytest.fixture(scope="module")
def master_result(params):
    return compute_route_c_nonmarkov_assessment(params)


@pytest.fixture(scope="module")
def markov_baseline(params):
    return recover_markov_baseline(params)


@pytest.fixture(scope="module")
def kernel_classes(params):
    return define_kernel_classes(params)


@pytest.fixture(scope="module")
def source_locking(params):
    return prove_source_profile_locking(params)


@pytest.fixture(scope="module")
def kernel_profiles(params):
    return compute_kernel_support_profiles(params)


# ================================================================
# Test Classes
# ================================================================

class TestConstants:
    """Verify module-level constants."""

    def test_alpha_vac(self):
        assert abs(ALPHA_VAC - 1.0 / 3.0) < 1e-10

    def test_M_ext(self):
        assert abs(M_EXT - 0.5) < 1e-10

    def test_R_eq(self):
        assert abs(R_EQ - 1.0 / 3.0) < 1e-10

    def test_tau_canonical(self):
        assert abs(TAU_CANONICAL - math.sqrt(1.5)) < 1e-10

    def test_epsilon_rc_coeff(self):
        expected = A_CRIT ** 2 * M_EXT ** 2 / (2.0 * TAU_CANONICAL ** 2)
        assert abs(EPSILON_RC_COEFF - expected) / expected < 1e-10


class TestMarkovBaselineRecovery:
    """Verify single exponential baseline recovery."""

    def test_epsilon_rc_coeff_value(self, markov_baseline):
        assert abs(markov_baseline.epsilon_rc_coeff - 0.0940) < 0.001

    def test_scaling_exponent(self, markov_baseline):
        assert abs(markov_baseline.scaling_exponent - (-4.0)) < 1e-6

    def test_is_pure_r4(self, markov_baseline):
        assert markov_baseline.is_pure_r4 is True

    def test_matches_locked_result(self, markov_baseline):
        assert markov_baseline.matches_locked_result is True

    def test_deviation_small(self, markov_baseline):
        assert markov_baseline.deviation_from_locked < 1e-10

    def test_has_notes(self, markov_baseline):
        assert len(markov_baseline.notes) >= 3


class TestKernelClassDefinitions:
    """Verify kernel class definitions."""

    def test_n_kernel_classes(self, kernel_classes):
        assert kernel_classes.n_kernel_classes == 4

    def test_kernel_names_present(self, kernel_classes):
        names = kernel_classes.kernel_names
        assert "single_exponential" in names
        assert "two_pole" in names
        assert "power_law" in names
        assert "generic_spectral" in names

    def test_all_spectral_representable(self, kernel_classes):
        assert all(kernel_classes.has_spectral_representation)

    def test_has_descriptions(self, kernel_classes):
        assert len(kernel_classes.kernel_descriptions) == 4

    def test_has_formulas(self, kernel_classes):
        assert len(kernel_classes.kernel_formulas) == 4


class TestSourceProfileLocking:
    """Verify the source profile locking theorem — THE KEY RESULT."""

    def test_source_separable(self, source_locking):
        assert source_locking.source_is_separable is True

    def test_field_response_separable(self, source_locking):
        assert source_locking.field_response_separable is True

    def test_spatial_scaling_locked(self, source_locking):
        assert source_locking.spatial_scaling_locked is True

    def test_locked_exponent(self, source_locking):
        assert abs(source_locking.locked_scaling_exponent - (-4.0)) < 1e-10

    def test_numerical_verification(self, source_locking):
        assert source_locking.numerical_verification_passed is True

    def test_max_deviation(self, source_locking):
        assert source_locking.max_deviation_from_minus4 < 0.05

    def test_structural_argument(self, source_locking):
        assert "separable" in source_locking.structural_argument.lower()


class TestTwoPoleKernel:
    """Verify two-pole kernel analysis."""

    def test_spatial_exponent(self, kernel_profiles):
        tp = [p for p in kernel_profiles if p.kernel_name == "two_pole"]
        assert len(tp) == 1
        assert abs(tp[0].spatial_scaling_exponent - (-4.0)) < 0.01

    def test_temporal_differs(self, kernel_profiles):
        tp = [p for p in kernel_profiles if p.kernel_name == "two_pole"][0]
        assert tp.temporal_profile_differs is True

    def test_not_component_b(self, kernel_profiles):
        tp = [p for p in kernel_profiles if p.kernel_name == "two_pole"][0]
        assert tp.matches_component_b is False

    def test_amplitude_differs(self, kernel_profiles):
        tp = [p for p in kernel_profiles if p.kernel_name == "two_pole"][0]
        assert tp.effective_amplitude_differs is True

    def test_exponent_stable_across_time(self, kernel_profiles):
        tp = [p for p in kernel_profiles if p.kernel_name == "two_pole"][0]
        assert tp.exponent_std_across_time < 0.05


class TestPowerLawKernel:
    """Verify power-law kernel analysis."""

    def test_spatial_exponent(self, kernel_profiles):
        pl = [p for p in kernel_profiles if p.kernel_name == "power_law"]
        assert len(pl) == 1
        assert abs(pl[0].spatial_scaling_exponent - (-4.0)) < 0.01

    def test_temporal_differs(self, kernel_profiles):
        pl = [p for p in kernel_profiles if p.kernel_name == "power_law"][0]
        assert pl.temporal_profile_differs is True

    def test_not_component_b(self, kernel_profiles):
        pl = [p for p in kernel_profiles if p.kernel_name == "power_law"][0]
        assert pl.matches_component_b is False

    def test_amplitude_differs(self, kernel_profiles):
        pl = [p for p in kernel_profiles if p.kernel_name == "power_law"][0]
        assert pl.effective_amplitude_differs is True

    def test_exponent_stable_across_time(self, kernel_profiles):
        pl = [p for p in kernel_profiles if p.kernel_name == "power_law"][0]
        assert pl.exponent_std_across_time < 0.05


class TestSpectralRichness:
    """Verify spectral richness assessment."""

    def test_can_change_temporal(self, master_result):
        sr = master_result.spectral_richness
        assert sr.can_change_temporal_profile is True

    def test_can_change_amplitude(self, master_result):
        sr = master_result.spectral_richness
        assert sr.can_change_peak_amplitude is True

    def test_cannot_change_spatial(self, master_result):
        sr = master_result.spectral_richness
        assert sr.can_change_spatial_scaling is False

    def test_cannot_redistribute(self, master_result):
        sr = master_result.spectral_richness
        assert sr.can_redistribute_radially is False

    def test_history_scaling(self, master_result):
        sr = master_result.spectral_richness
        assert sr.history_term_spatial_scaling == "1/r^4"


class TestComponentBCompatibility:
    """Verify Component B compatibility assessment."""

    def test_none_match(self, master_result):
        cb = master_result.component_b_compat
        assert cb.any_matches_component_b is False

    def test_best_exponent(self, master_result):
        cb = master_result.component_b_compat
        assert abs(cb.best_scaling_exponent - (-4.0)) < 0.01

    def test_target_exponent(self, master_result):
        cb = master_result.component_b_compat
        assert abs(cb.target_exponent - (-2.0)) < 1e-10

    def test_gap_to_target(self, master_result):
        cb = master_result.component_b_compat
        assert abs(cb.gap_to_target - 2.0) < 0.01

    def test_n_kernel_results(self, master_result):
        cb = master_result.component_b_compat
        assert len(cb.kernel_results) == 4

    def test_all_results_negative(self, master_result):
        cb = master_result.component_b_compat
        assert all(
            kr["matches_component_b"] is False for kr in cb.kernel_results
        )


class TestLocalizabilityPromotability:
    """Verify localizability and physical promotability."""

    def test_nonlocal_time(self, master_result):
        lz = master_result.localizability
        assert lz.nonlocal_in_time is True

    def test_local_space(self, master_result):
        lz = master_result.localizability
        assert lz.local_in_space is True

    def test_not_promotable(self, master_result):
        pr = master_result.promotability
        assert pr.any_kernel_promotable is False

    def test_obstruction(self, master_result):
        pr = master_result.promotability
        assert pr.obstruction == "source_profile_locking"

    def test_remaining_loophole(self, master_result):
        pr = master_result.promotability
        assert pr.remaining_loophole == "modified_source_law"


class TestClassificationNonclaims:
    """Verify final classification, nonclaims, and serialization."""

    def test_classification_string(self, master_result):
        cl = master_result.classification
        assert cl.classification == (
            "nonmarkov_route_c_insufficient_for_component_b"
        )

    def test_source_locking_proven(self, master_result):
        cl = master_result.classification
        assert cl.source_profile_locking_proven is True

    def test_n_kernel_classes(self, master_result):
        cl = master_result.classification
        assert cl.n_kernel_classes_tested == 4

    def test_all_insufficient(self, master_result):
        cl = master_result.classification
        assert cl.all_tested_insufficient is True

    def test_nonclaim_count(self, master_result):
        assert len(master_result.nonclaims) == 10

    def test_assumption_count(self, master_result):
        assert len(master_result.assumptions) == 10

    def test_nonclaims_content(self, master_result):
        assert any(
            "NOT prove Route C physically incorrect" in nc
            for nc in master_result.nonclaims
        )

    def test_serialization(self, master_result):
        d = route_c_nonmarkov_result_to_dict(master_result)
        assert d["valid"] is True
        assert d["classification"]["classification"] == (
            "nonmarkov_route_c_insufficient_for_component_b"
        )
