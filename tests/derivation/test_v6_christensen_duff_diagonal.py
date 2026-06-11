"""
Tests for V6 Christensen-Duff Diagonal.

Verifies the exact first-principles Euler anomaly coefficient:

    a_hat = 43/16  (SM gauge + FP ghosts + fermions, no Higgs)
    M11   = 43/(128π) = 0.10693…

and the associated R-prediction with the full V5 matrix.

CLAIM: christensen_duff_euler_diagonal_exact
  The SM gauge+FP-ghost+fermion (Higgs-excluded) sector gives
  a_hat = 43/16, M11 = 43/(128π), which reduces the R error
  from 14.44% (structural M11=0.11) to 0.96% (error vs √(4/3)).
"""

import math
import pytest

from grut.derivation.euler.v6_christensen_duff_diagonal import (
    SMCensus,
    standard_model_censuses,
    evaluate_census,
    exact_cd_m11,
    binary_search_m11_star,
    gap_decomposition,
    run_v6,
    exact_m11,
    a_hat_gauge_ghost_fermion,
    CD_FP_GHOST_COMPLEX,
    CD_VECTOR_NET,
    R_CANONICAL,
)
from grut.derivation.euler.v5_loop_suppressed_matrix import (
    CD_SCALAR,
    CD_VECTOR,
    CD_WEYL_FERMION,
)


# ──────────────────────────────────────────────────────────────────────────────
# Christensen-Duff coefficient values
# ──────────────────────────────────────────────────────────────────────────────

class TestCDCoefficients:
    """Verify the exact Christensen-Duff 1979 coefficients on S⁴."""

    def test_cd_scalar(self):
        assert abs(CD_SCALAR - 1.0 / 360.0) < 1e-12

    def test_cd_vector(self):
        assert abs(CD_VECTOR - 31.0 / 180.0) < 1e-12

    def test_cd_fermion(self):
        assert abs(CD_WEYL_FERMION - 11.0 / 720.0) < 1e-12

    def test_fp_ghost_complex(self):
        """FP ghost = complex anticommuting scalar → −2/360 per ghost."""
        assert abs(CD_FP_GHOST_COMPLEX - (-2.0 / 360.0)) < 1e-12

    def test_net_vector_equals_30_over_180(self):
        """Vector + ghost = 31/180 − 2/360 = 30/180 = 1/6."""
        expected = 30.0 / 180.0
        assert abs(CD_VECTOR_NET - expected) < 1e-12

    def test_net_vector_equals_one_sixth(self):
        assert abs(CD_VECTOR_NET - 1.0 / 6.0) < 1e-12


# ──────────────────────────────────────────────────────────────────────────────
# Exact rational: a_hat = 43/16
# ──────────────────────────────────────────────────────────────────────────────

class TestExactRationalResult:
    """Verify the exact a_hat = 43/16 and M11 = 43/(128π)."""

    def test_a_hat_gauge_ghost_fermion_is_43_over_16(self):
        a = a_hat_gauge_ghost_fermion()
        assert abs(a - 43.0 / 16.0) < 1e-12

    def test_a_hat_numerical_value(self):
        assert abs(a_hat_gauge_ghost_fermion() - 2.6875) < 1e-12

    def test_m11_exact_is_43_over_128pi(self):
        m = exact_m11()
        assert abs(m - 43.0 / (128.0 * math.pi)) < 1e-12

    def test_m11_numerical_value(self):
        """M11 = 43/(128π) ≈ 0.106932."""
        m = exact_m11()
        assert abs(m - 0.106932) < 1e-5

    def test_exact_cd_is_43_over_16(self):
        ex = exact_cd_m11()
        assert ex["is_43_over_16"] is True

    def test_exact_cd_rational_fraction(self):
        ex = exact_cd_m11()
        assert ex["numerator"] == 43
        assert ex["denominator"] == 16

    def test_exact_cd_below_structural_estimate(self):
        """43/(128π) < 0.11 (the structural estimate)."""
        assert exact_m11() < 0.11

    def test_structural_estimate_overestimates(self):
        """Structural estimate 0.11 overestimates by ~2.8%."""
        ex = exact_cd_m11()
        # The delta is negative (exact < structural)
        assert ex["delta_vs_structural_pct"] < 0.0
        assert ex["delta_vs_structural_pct"] > -5.0  # within 5%

    def test_sm_bare_close_to_structural(self):
        """SM bare (with Higgs, no ghosts) ≈ 0.11003 ≈ structural estimate."""
        ex = exact_cd_m11()
        assert abs(ex["m11_sm_bare"] - 0.11003) < 1e-4

    def test_exact_below_sm_bare(self):
        """Exact (no Higgs, with ghosts) < SM bare (with Higgs, no ghosts)."""
        assert exact_m11() < exact_cd_m11()["m11_sm_bare"]


# ──────────────────────────────────────────────────────────────────────────────
# SMCensus particle counting
# ──────────────────────────────────────────────────────────────────────────────

class TestSMCensus:
    """Verify individual particle census calculations."""

    def test_sm_bare_a_hat_is_1991_over_720(self):
        c = SMCensus("test", n_scalars=4, n_vectors=12, n_ghosts_complex=0, n_weyl=45)
        assert abs(c.a_hat - 1991.0 / 720.0) < 1e-10

    def test_sm_with_ghosts_a_hat_is_1943_over_720(self):
        c = SMCensus("test", n_scalars=4, n_vectors=12, n_ghosts_complex=12, n_weyl=45)
        assert abs(c.a_hat - 1943.0 / 720.0) < 1e-10

    def test_gauge_ghost_fermion_a_hat_is_43_over_16(self):
        c = SMCensus("test", n_scalars=0, n_vectors=12, n_ghosts_complex=12, n_weyl=45)
        assert abs(c.a_hat - 43.0 / 16.0) < 1e-10

    def test_higgs_contribution_to_a_hat(self):
        """4 real Higgs scalars add 4/360 = 1/90 to a_hat."""
        c_no_higgs = SMCensus("nh", n_scalars=0, n_vectors=12, n_ghosts_complex=12, n_weyl=45)
        c_with_higgs = SMCensus("h", n_scalars=4, n_vectors=12, n_ghosts_complex=12, n_weyl=45)
        delta = c_with_higgs.a_hat - c_no_higgs.a_hat
        assert abs(delta - 4.0 / 360.0) < 1e-12

    def test_rhn_contribution_to_a_hat(self):
        """3 RHN add 3×(11/720) = 33/720 to a_hat."""
        c_sm = SMCensus("sm", n_scalars=0, n_vectors=12, n_ghosts_complex=12, n_weyl=45)
        c_rhn = SMCensus("rhn", n_scalars=0, n_vectors=12, n_ghosts_complex=12, n_weyl=48)
        delta = c_rhn.a_hat - c_sm.a_hat
        assert abs(delta - 3.0 * 11.0 / 720.0) < 1e-12

    def test_rhn_increases_a_hat(self):
        """RHN make a_hat larger (wrong direction)."""
        c_sm = SMCensus("sm", n_scalars=0, n_vectors=12, n_ghosts_complex=12, n_weyl=45)
        c_rhn = SMCensus("rhn", n_scalars=0, n_vectors=12, n_ghosts_complex=12, n_weyl=48)
        assert c_rhn.a_hat > c_sm.a_hat

    def test_ghost_subtraction_reduces_a_hat(self):
        """FP ghosts reduce a_hat (negative contribution)."""
        c_no_ghost = SMCensus("ng", n_scalars=0, n_vectors=12, n_ghosts_complex=0, n_weyl=45)
        c_ghost = SMCensus("g", n_scalars=0, n_vectors=12, n_ghosts_complex=12, n_weyl=45)
        assert c_ghost.a_hat < c_no_ghost.a_hat

    def test_12_ghosts_reduce_by_24_over_360(self):
        """12 complex FP ghosts reduce a_hat by 12 × (2/360) = 24/360."""
        c_no_ghost = SMCensus("ng", n_scalars=0, n_vectors=12, n_ghosts_complex=0, n_weyl=45)
        c_ghost = SMCensus("g", n_scalars=0, n_vectors=12, n_ghosts_complex=12, n_weyl=45)
        delta = c_no_ghost.a_hat - c_ghost.a_hat
        assert abs(delta - 24.0 / 360.0) < 1e-12


# ──────────────────────────────────────────────────────────────────────────────
# M11 → R predictions
# ──────────────────────────────────────────────────────────────────────────────

class TestRPredictions:
    """Test R predictions from census evaluations against V5 matrix."""

    def test_structural_estimate_14pct_error(self):
        """Structural M11=0.11 gives ~14% error vs R_CANONICAL."""
        c = SMCensus("struct", n_scalars=4, n_vectors=12, n_ghosts_complex=0, n_weyl=45)
        cr = evaluate_census(c)
        assert cr["error_vs_canonical_pct"] > 12.0
        assert cr["error_vs_canonical_pct"] < 17.0

    def test_exact_cd_below_5pct_error(self):
        """Exact CD (43/(128π)) gives < 5% error vs R_CANONICAL."""
        c = SMCensus("exact", n_scalars=0, n_vectors=12, n_ghosts_complex=12, n_weyl=45)
        cr = evaluate_census(c)
        assert cr["error_vs_canonical_pct"] < 5.0

    def test_exact_cd_error_is_about_1pct(self):
        """Exact CD error ≈ 0.96% vs R_CANONICAL."""
        c = SMCensus("exact", n_scalars=0, n_vectors=12, n_ghosts_complex=12, n_weyl=45)
        cr = evaluate_census(c)
        assert abs(cr["error_vs_canonical_pct"] - 0.96) < 0.3

    def test_rhn_worsens_gap(self):
        """Adding RHN increases the error vs R_CANONICAL."""
        c_sm = SMCensus("sm", n_scalars=0, n_vectors=12, n_ghosts_complex=12, n_weyl=45)
        c_rhn = SMCensus("rhn", n_scalars=0, n_vectors=12, n_ghosts_complex=12, n_weyl=48)
        cr_sm = evaluate_census(c_sm)
        cr_rhn = evaluate_census(c_rhn)
        assert cr_rhn["error_vs_canonical_pct"] > cr_sm["error_vs_canonical_pct"]

    def test_sm_bare_rhn_worsens_vs_sm_bare(self):
        """SM + RHN (no ghosts) gives larger error than SM bare (no ghosts)."""
        c_bare = SMCensus("bare", n_scalars=4, n_vectors=12, n_ghosts_complex=0, n_weyl=45)
        c_rhn = SMCensus("rhn", n_scalars=4, n_vectors=12, n_ghosts_complex=0, n_weyl=48)
        cr_bare = evaluate_census(c_bare)
        cr_rhn = evaluate_census(c_rhn)
        assert cr_rhn["error_vs_canonical_pct"] > cr_bare["error_vs_canonical_pct"]

    def test_ghosts_improve_over_no_ghosts(self):
        """FP ghost subtraction improves R prediction."""
        c_ng = SMCensus("ng", n_scalars=4, n_vectors=12, n_ghosts_complex=0, n_weyl=45)
        c_g = SMCensus("g", n_scalars=4, n_vectors=12, n_ghosts_complex=12, n_weyl=45)
        cr_ng = evaluate_census(c_ng)
        cr_g = evaluate_census(c_g)
        assert cr_g["error_vs_canonical_pct"] < cr_ng["error_vs_canonical_pct"]

    def test_no_higgs_improves_over_with_higgs(self):
        """Excluding Higgs from M11 improves R prediction."""
        c_h = SMCensus("h", n_scalars=4, n_vectors=12, n_ghosts_complex=12, n_weyl=45)
        c_nh = SMCensus("nh", n_scalars=0, n_vectors=12, n_ghosts_complex=12, n_weyl=45)
        cr_h = evaluate_census(c_h)
        cr_nh = evaluate_census(c_nh)
        assert cr_nh["error_vs_canonical_pct"] < cr_h["error_vs_canonical_pct"]

    def test_exact_cd_r_predicted_above_1(self):
        """Exact CD still gives R > 1."""
        c = SMCensus("exact", n_scalars=0, n_vectors=12, n_ghosts_complex=12, n_weyl=45)
        cr = evaluate_census(c)
        assert cr["R_predicted"] > 1.0

    def test_exact_cd_r_predicted_below_1p25(self):
        """Exact CD gives R < 1.25 (much better than structural 1.32)."""
        c = SMCensus("exact", n_scalars=0, n_vectors=12, n_ghosts_complex=12, n_weyl=45)
        cr = evaluate_census(c)
        assert cr["R_predicted"] < 1.25


# ──────────────────────────────────────────────────────────────────────────────
# M11* inversion
# ──────────────────────────────────────────────────────────────────────────────

class TestM11StarInversion:
    """Test the numerical inversion M11* for R = √(4/3)."""

    def test_m11_star_in_expected_range(self):
        """M11* should be near 0.1067 (from r_target_inversion)."""
        result = binary_search_m11_star()
        assert 0.104 < result["m11_star"] < 0.110

    def test_m11_star_achieves_target(self):
        """Inversion achieves R = √(4/3) to 0.01%."""
        result = binary_search_m11_star()
        assert result["error_pct"] < 0.01

    def test_m11_star_below_structural(self):
        """Required M11* < structural estimate 0.11."""
        result = binary_search_m11_star()
        assert result["m11_star"] < 0.11

    def test_m11_star_gap_from_exact_cd_small(self):
        """Exact CD (43/(128π)) is within 0.5% of M11*."""
        result = binary_search_m11_star()
        gap = abs(result["gap_pct_in_m11"])
        assert gap < 0.5

    def test_m11_star_structural_delta_about_3pct(self):
        """Structural estimate is ~3% above M11*."""
        result = binary_search_m11_star()
        delta_pct = abs(result["delta_m11_from_structural"] / result["m11_star"]) * 100.0
        assert 2.0 < delta_pct < 4.5


# ──────────────────────────────────────────────────────────────────────────────
# Gap decomposition
# ──────────────────────────────────────────────────────────────────────────────

class TestGapDecomposition:
    """Test the β_eff gap decomposition into diagonal and off-diagonal parts."""

    def test_euler_projection_near_97pct(self):
        """Euler channel projects ~97% onto its own eigenstate."""
        d = gap_decomposition()
        assert d["euler_projection"] > 0.94
        assert d["euler_projection"] < 0.99

    def test_exact_cd_beta_excess_small(self):
        """Exact CD gives β_eff excess vs 0.1215 of < 0.2%."""
        d = gap_decomposition(m11=exact_m11())
        assert abs(d["excess_pct"]) < 0.2

    def test_structural_beta_excess_about_1pt2pct(self):
        """Structural estimate gives ~1.2% β_eff excess."""
        d = gap_decomposition(m11=0.11)
        assert abs(d["excess_pct"]) > 1.0
        assert abs(d["excess_pct"]) < 2.0

    def test_offdiag_contamination_positive(self):
        """Off-diagonal contamination pushes β_eff above the diagonal estimate."""
        d = gap_decomposition()
        assert d["beta_offdiag_contamination"] > 0.0

    def test_exact_cd_r_within_2pct(self):
        """With exact CD M11, R is within 2% of √(4/3)."""
        d = gap_decomposition(m11=exact_m11())
        error = abs(d["R_predicted"] - R_CANONICAL) / R_CANONICAL * 100.0
        assert error < 2.0


# ──────────────────────────────────────────────────────────────────────────────
# Census ranking
# ──────────────────────────────────────────────────────────────────────────────

class TestCensusRanking:
    """Test the relative ordering of all SM particle inventories."""

    def setup_method(self):
        self.v6 = run_v6()

    def test_best_scenario_is_gauge_ghost_fermion(self):
        """The gauge+ghost+fermion (no Higgs) scenario has the smallest error."""
        best = self.v6["census_ranked"][0]
        assert "gauge+ghost+fermion" in best["name"].lower() or "no higgs" in best["name"].lower()

    def test_rhn_scenarios_rank_below_sm_only(self):
        """All RHN scenarios rank worse (higher error) than SM-only best."""
        best_error = self.v6["census_ranked"][0]["error_vs_canonical_pct"]
        for cr in self.v6["census_results"]:
            if "RHN" in cr["name"]:
                assert cr["error_vs_canonical_pct"] > best_error

    def test_structural_estimate_ranks_near_bottom(self):
        """SM bare (≈ structural estimate) is among the worst-performing scenarios."""
        errors_sorted = [cr["error_vs_canonical_pct"] for cr in self.v6["census_ranked"]]
        sm_bare_err = next(
            cr["error_vs_canonical_pct"]
            for cr in self.v6["census_results"]
            if cr["name"].startswith("SM bare (N_S=4")
        )
        # SM bare should be in the bottom half (higher error half)
        n = len(errors_sorted)
        median_error = errors_sorted[n // 2]
        assert sm_bare_err > median_error

    def test_three_scenarios_below_5pct_error(self):
        """At least 3 scenarios achieve < 5% error vs R_CANONICAL with ghost subtraction."""
        below_5 = [cr for cr in self.v6["census_results"] if cr["error_vs_canonical_pct"] < 5.0]
        assert len(below_5) >= 3

    def test_no_rhn_scenario_below_5pct_if_no_ghosts(self):
        """SM + RHN without ghost subtraction is above 5% error."""
        rhn_no_ghost = next(
            cr for cr in self.v6["census_results"]
            if "N_F=48" in cr["name"] and cr["n_ghosts"] == 0
        )
        assert rhn_no_ghost["error_vs_canonical_pct"] > 20.0


# ──────────────────────────────────────────────────────────────────────────────
# Run-v6 smoke test
# ──────────────────────────────────────────────────────────────────────────────

class TestRunV6:
    """Smoke tests for the master run_v6() function."""

    def setup_method(self):
        self.v6 = run_v6()

    def test_exact_cd_key_present(self):
        assert "exact_cd" in self.v6

    def test_m11_star_key_present(self):
        assert "m11_star" in self.v6

    def test_census_results_count(self):
        """Should have one result per SMCensus returned by standard_model_censuses()."""
        assert len(self.v6["census_results"]) == len(standard_model_censuses())

    def test_census_ranked_same_count(self):
        assert len(self.v6["census_ranked"]) == len(self.v6["census_results"])

    def test_ranked_ascending_error(self):
        """census_ranked is sorted by ascending error."""
        errors = [cr["error_vs_canonical_pct"] for cr in self.v6["census_ranked"]]
        for i in range(len(errors) - 1):
            assert errors[i] <= errors[i + 1]

    def test_decomp_structural_present(self):
        assert "decomp_structural" in self.v6

    def test_decomp_exact_cd_present(self):
        assert "decomp_exact_cd" in self.v6
