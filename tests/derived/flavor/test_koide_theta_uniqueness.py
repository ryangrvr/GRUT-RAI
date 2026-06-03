"""Tests for grut.derived.flavor.koide_theta_uniqueness.

Pins the formal uniqueness finding: θ = 2/9 is the unique best rational
approximant to θ_fit mod(2π/3) for all denominators ≤ 193, with the
nearest irreducible competitor (43/194) at 557× larger deviation.

Registry claim: koide_theta_2_over_9_uniqueness (CANDIDATE IDENTITY)
"""

import math
from fractions import Fraction

import pytest

from grut.derived.flavor.koide_theta_uniqueness import (
    CANDIDATE_DEV_PPM,
    CANDIDATE_FRAC,
    CANDIDATE_FRAC_VAL,
    COMPETITOR_RATIO,
    EXPERIMENTAL_WINDOW_PPM,
    K_KOIDE,
    SECOND_BEST_DEV_PPM,
    SECOND_BEST_DENOMINATOR,
    SECOND_BEST_NUMERATOR,
    THETA_MOD_RAD,
    TWO_PI_OVER_3,
    UNIQUE_BEST_DENOM_THRESHOLD,
    WINDOW_PPM_FOR_UNIQUE_SCAN,
    koide_theta_uniqueness_verdict,
    scan_rational_approximants,
    uniqueness_check,
    z3_algebraic_check,
)
from grut.derived.flavor.koide_operator import THETA_FIT_RAD
from grut.foundation.closure_protocol import ALPHA_VAC


# ─────────────────────────────────────────────────────────────────────
# Class 1 — Module constants
# ─────────────────────────────────────────────────────────────────────


class TestModuleConstants:
    """Pin all exported constants to their numerical values."""

    def test_two_pi_over_3_value(self):
        assert abs(TWO_PI_OVER_3 - 2.0 * math.pi / 3.0) < 1e-15

    def test_theta_mod_is_fit_mod_period(self):
        assert abs(THETA_MOD_RAD - (THETA_FIT_RAD % TWO_PI_OVER_3)) < 1e-15

    def test_theta_mod_in_range(self):
        """θ_mod is in (0, 2π/3)."""
        assert 0.0 < THETA_MOD_RAD < TWO_PI_OVER_3

    def test_theta_mod_near_2_over_9(self):
        """θ_mod ≈ 0.2222 rad."""
        assert 0.221 < THETA_MOD_RAD < 0.223

    def test_k_koide_is_two_thirds(self):
        assert abs(K_KOIDE - 2.0 / 3.0) < 1e-15

    def test_candidate_frac_is_two_ninths(self):
        assert CANDIDATE_FRAC == Fraction(2, 9)

    def test_candidate_frac_val(self):
        assert abs(CANDIDATE_FRAC_VAL - 2.0 / 9.0) < 1e-15

    def test_candidate_dev_ppm_is_about_4p6(self):
        """2/9 matches θ_mod at ~4.62 ppm."""
        assert 4.0 < CANDIDATE_DEV_PPM < 5.5

    def test_experimental_window_ppm(self):
        """PDG m_τ propagated window ~258 ppm."""
        assert 200.0 < EXPERIMENTAL_WINDOW_PPM < 350.0

    def test_candidate_well_inside_window(self):
        """Candidate is 50+ times inside the experimental window."""
        assert EXPERIMENTAL_WINDOW_PPM / CANDIDATE_DEV_PPM > 50.0

    def test_unique_best_denom_threshold(self):
        """2/9 wins all denominators through at least 100."""
        assert UNIQUE_BEST_DENOM_THRESHOLD >= 100

    def test_second_best_fraction_values(self):
        assert SECOND_BEST_NUMERATOR == 43
        assert SECOND_BEST_DENOMINATOR == 194

    def test_second_best_dev_ppm_range(self):
        """43/194 is at ~2573 ppm."""
        assert 2500.0 < SECOND_BEST_DEV_PPM < 2700.0

    def test_competitor_ratio_is_large(self):
        """Next competitor is 500+ times worse than 2/9."""
        assert COMPETITOR_RATIO > 500.0

    def test_k_times_alpha_vac_equals_2_9(self):
        """K_koide × α_vac = (2/3)(1/3) = 2/9 exactly."""
        product = Fraction(2, 3) * Fraction(1, 3)
        assert product == Fraction(2, 9)
        assert abs(K_KOIDE * ALPHA_VAC - CANDIDATE_FRAC_VAL) < 1e-15


# ─────────────────────────────────────────────────────────────────────
# Class 2 — Rational approximant scan
# ─────────────────────────────────────────────────────────────────────


class TestScanRationalApproximants:
    """Test the systematic fraction scan."""

    @pytest.fixture(scope="class")
    def scan_200_5000(self):
        return scan_rational_approximants(max_denom=200, window_ppm=5000.0)

    @pytest.fixture(scope="class")
    def scan_200_1000(self):
        return scan_rational_approximants(max_denom=200, window_ppm=1000.0)

    def test_best_entry_is_two_ninths(self, scan_200_5000):
        """The lowest-deviation entry must be 2/9."""
        best = scan_200_5000[0]
        assert best["reduced"] == Fraction(2, 9)

    def test_best_deviation_is_about_4p6_ppm(self, scan_200_5000):
        best = scan_200_5000[0]
        assert 4.0 < best["deviation_ppm"] < 5.5

    def test_results_sorted_ascending(self, scan_200_5000):
        devs = [r["deviation_ppm"] for r in scan_200_5000]
        assert devs == sorted(devs)

    def test_all_within_1000ppm_are_multiples_of_2_9(self, scan_200_1000):
        """Within ±1000 ppm, every match is 2k/9k — only one irreducible fraction."""
        for r in scan_200_1000:
            assert r["is_multiple_of_candidate"], (
                f"{r['numerator']}/{r['denominator']} at {r['deviation_ppm']:.1f} ppm "
                "is within 1000 ppm but not a multiple of 2/9"
            )

    def test_second_best_irreducible(self, scan_200_5000):
        """First irreducible competitor in the scan is 43/194."""
        competitors = [r for r in scan_200_5000 if not r["is_multiple_of_candidate"]]
        assert len(competitors) >= 1
        best_c = competitors[0]
        assert best_c["reduced"] == Fraction(SECOND_BEST_NUMERATOR, SECOND_BEST_DENOMINATOR)

    def test_scan_contains_multiples_of_2_9(self, scan_200_5000):
        """Scan should find multiples 2/9, 4/18, 6/27, ..."""
        multiples = [r for r in scan_200_5000 if r["is_multiple_of_candidate"]]
        assert len(multiples) >= 5  # at least 2/9, 4/18, 6/27, 8/36, 10/45

    def test_scan_deviation_is_ppm_not_fraction(self, scan_200_5000):
        """Sanity: deviations are in ppm, so should be > 0 for non-exact matches."""
        for r in scan_200_5000:
            assert r["deviation_ppm"] >= 0.0
            if r["reduced"] != Fraction(2, 9):
                assert r["deviation_ppm"] > 0.0


# ─────────────────────────────────────────────────────────────────────
# Class 3 — Uniqueness check
# ─────────────────────────────────────────────────────────────────────


class TestUniquenessCheck:
    """Test the formal uniqueness report."""

    @pytest.fixture(scope="class")
    def uc(self):
        return uniqueness_check(max_denom=200)

    def test_within_1000ppm_all_multiples_of_candidate(self, uc):
        assert uc["within_1000ppm_all_multiples_of_2_9"] is True

    def test_is_unique_below_1000ppm(self, uc):
        assert uc["is_unique_below_1000ppm_for_q_leq_max_denom"] is True

    def test_candidate_wins_through_threshold(self, uc):
        """2/9 is the best rational approx for denominators ≥ 9 up to threshold."""
        assert uc["candidate_wins_all_denominators_from_9_to"] >= 100

    def test_best_irreducible_competitor_is_43_194(self, uc):
        c = uc["best_irreducible_competitor"]
        assert c is not None
        assert c["reduced"] == str(Fraction(43, 194))

    def test_competitor_uniqueness_ratio_exceeds_500(self, uc):
        c = uc["best_irreducible_competitor"]
        assert c["uniqueness_ratio"] > 500.0

    def test_theta_mod_value_present(self, uc):
        assert abs(uc["theta_mod_rad"] - THETA_MOD_RAD) < 1e-14

    def test_limit_denominator_transitions_contain_2_9_at_9(self, uc):
        """The Stern–Brocot tree first finds 2/9 at n=9."""
        trans = uc["limit_denominator_transitions"]
        assert 9 in trans
        assert trans[9] == "2/9"

    def test_limit_denominator_transitions_before_9(self, uc):
        """Before n=9, best approximant is 1/5 (at n=5,6,7,8)."""
        trans = uc["limit_denominator_transitions"]
        assert 5 in trans
        assert trans[5] == "1/5"


# ─────────────────────────────────────────────────────────────────────
# Class 4 — Z₃ algebraic check
# ─────────────────────────────────────────────────────────────────────


class TestZ3AlgebraicCheck:
    """Test the algebraic structure checks."""

    @pytest.fixture(scope="class")
    def alg(self):
        return z3_algebraic_check()

    def test_z3_does_not_algebraically_select_theta(self, alg):
        assert alg["test_T1_z3_algebraically_selects_theta"] is False

    def test_ctp_does_not_derive_theta(self, alg):
        assert alg["test_T2_ctp_derives_theta_from_action"] is False

    def test_structural_formula_is_2_over_9(self, alg):
        assert alg["test_T3_structural_formula_K_times_alpha_vac"] == "2/9"

    def test_product_equals_candidate(self, alg):
        assert alg["test_T3_product_equals_candidate"] is True

    def test_k_value_is_two_thirds(self, alg):
        assert abs(alg["test_T3_K_value"] - 2.0 / 3.0) < 1e-14

    def test_alpha_vac_value_is_one_third(self, alg):
        assert abs(alg["test_T3_alpha_vac_value"] - 1.0 / 3.0) < 1e-14

    def test_overall_algebraic_derivation_does_not_exist(self, alg):
        assert alg["overall_algebraic_derivation_exists"] is False

    def test_t1_reasoning_mentions_z3_and_any_theta(self, alg):
        r = alg["test_T1_reasoning"].lower()
        assert "z₃" in r or "z3" in r or "any θ" in r or "any theta" in r or "any" in r

    def test_t2_reasoning_mentions_honest_negative(self, alg):
        r = alg["test_T2_reasoning"].lower()
        assert "honest negative" in r or "underdetermined" in r

    def test_overall_status_mentions_candidate_identity(self, alg):
        s = alg["overall_status"]
        assert "CANDIDATE IDENTITY" in s


# ─────────────────────────────────────────────────────────────────────
# Class 5 — Top-level verdict
# ─────────────────────────────────────────────────────────────────────


class TestKoideThetaUniquenessVerdict:
    """Test the top-level verdict function."""

    @pytest.fixture(scope="class")
    def v(self):
        return koide_theta_uniqueness_verdict()

    def test_required_keys_present(self, v):
        required = {
            "theta_fit_rad", "theta_mod_rad",
            "candidate_fraction", "candidate_value_rad",
            "candidate_deviation_ppm", "experimental_window_ppm",
            "candidate_inside_window",
            "uniqueness_check", "uniqueness_ratio_vs_next",
            "second_best_fraction", "second_best_dev_ppm",
            "z3_algebraic_check", "algebraic_derivation_exists",
            "tier_uniqueness_scan", "tier_algebraic_mechanism", "tier_overall",
            "is_numerology", "is_derived",
            "falsifier", "structural_formula", "structural_factors",
            "verdict_paragraph",
        }
        assert required.issubset(set(v.keys()))

    def test_candidate_inside_experimental_window(self, v):
        assert v["candidate_inside_window"] is True

    def test_tier_uniqueness_scan_computed(self, v):
        assert v["tier_uniqueness_scan"] == "COMPUTED"

    def test_tier_algebraic_mechanism_open(self, v):
        assert v["tier_algebraic_mechanism"] == "OPEN"

    def test_tier_overall_candidate_identity(self, v):
        assert v["tier_overall"] == "CANDIDATE IDENTITY"

    def test_not_numerology(self, v):
        assert v["is_numerology"] is False

    def test_not_derived(self, v):
        assert v["is_derived"] is False

    def test_algebraic_derivation_does_not_exist(self, v):
        assert v["algebraic_derivation_exists"] is False

    def test_second_best_fraction_is_43_194(self, v):
        assert v["second_best_fraction"] == "43/194"

    def test_second_best_dev_ppm_range(self, v):
        assert 2500.0 < v["second_best_dev_ppm"] < 2700.0

    def test_uniqueness_ratio_exceeds_500(self, v):
        assert v["uniqueness_ratio_vs_next"] > 500.0

    def test_structural_formula_string(self, v):
        assert "2/9" in v["structural_formula"]
        assert "K" in v["structural_formula"] or "α" in v["structural_formula"]

    def test_structural_factors_keys(self, v):
        sf = v["structural_factors"]
        assert "K_koide" in sf
        assert "alpha_vac" in sf
        assert abs(sf["K_koide"] - 2.0 / 3.0) < 1e-14
        assert abs(sf["alpha_vac"] - 1.0 / 3.0) < 1e-14

    def test_falsifier_mentions_cepc_or_fcc(self, v):
        f = v["falsifier"].lower()
        assert "cepc" in f or "fcc" in f or "tau" in f

    def test_verdict_paragraph_mentions_557(self, v):
        """Paragraph must cite the 557× ratio so it's pinned."""
        assert "557" in v["verdict_paragraph"]

    def test_verdict_paragraph_mentions_4p62_ppm(self, v):
        assert "4.62" in v["verdict_paragraph"] or "4.6" in v["verdict_paragraph"]

    def test_verdict_paragraph_mentions_candidate_identity(self, v):
        assert "CANDIDATE IDENTITY" in v["verdict_paragraph"]

    def test_candidate_dev_ppm_consistent(self, v):
        assert abs(v["candidate_deviation_ppm"] - CANDIDATE_DEV_PPM) < 0.01

    def test_theta_mod_consistent(self, v):
        assert abs(v["theta_mod_rad"] - THETA_MOD_RAD) < 1e-14
