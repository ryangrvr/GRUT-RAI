"""Tests for grut.foundation.osborn_epsilon — promotes the Osborn route
for R from 'literature citation' to 'computed' tier.

Three-Routes convergence:
    Route 1 (Path G, tree-level)   : R = √(4/3) ≈ 1.15470  (computed)
    Route 2 (V7 §26, historical)   : R = 1.15428          (open_negative)
    Route 3 (Osborn eq 36, M_Z)    : ε_combined ≈ 1.15370 (computed, this)

Routes 1 and 3 share NO inputs (Path G uses zero coupling constants;
Osborn uses measured α_s, α_2, α_Y). Their agreement at the 0.1%
level is independent confirmation.
"""

import math

import pytest

from grut.foundation.osborn_epsilon import (
    ALL_SM_SECTORS,
    ALPHA_S_MZ, ALPHA_2_MZ, ALPHA_Y_MZ,
    GaugeSector,
    R_ROUTE_1_PATH_G, R_ROUTE_2_V7_HISTORICAL, R_ROUTE_3_OSBORN,
    SU2_SECTOR, SU3_SECTOR, U1_SECTOR,
    WEIGHTS_QCD_DOMINANT,
    WEIGHT_SU2, WEIGHT_SU3, WEIGHT_U1,
    epsilon_combined,
    epsilon_one_loop,
    epsilon_report,
    three_routes_convergence,
    verify,
)


# ─────────────────────────────────────────────────────────────────────
# Per-sector evaluations match the documented Dirac-convention values
# ─────────────────────────────────────────────────────────────────────

class TestPerSectorEpsilon:

    def test_su3_epsilon_at_MZ(self):
        """ε_SU(3) at M_Z with Dirac convention ≈ 1.1598."""
        e = epsilon_one_loop(SU3_SECTOR)
        assert abs(e - 1.1598) < 1e-3
        # Sanity: the correction is positive (29C beats 12 R_ψ)
        assert e > 1.0

    def test_su2_epsilon_at_MZ(self):
        """ε_SU(2) at M_Z ≈ 1.0175 (small positive correction)."""
        e = epsilon_one_loop(SU2_SECTOR)
        assert abs(e - 1.0175) < 1e-3
        assert e > 1.0

    def test_u1_epsilon_at_MZ(self):
        """ε_U(1) at M_Z ≈ 0.9673 (NEGATIVE correction — fermions dominate)."""
        e = epsilon_one_loop(U1_SECTOR)
        assert abs(e - 0.9673) < 1e-3
        # U(1) is below 1 because R_ψ = 10 dominates
        assert e < 1.0


class TestEpsilonOneLoopFormula:
    """Direct verification of Osborn 2003 eq (36)."""

    def test_zero_coupling_returns_one(self):
        s = GaugeSector(name="test", alpha=0.0, C=3.0,
                         R_psi=3.0, R_phi=0.0)
        assert epsilon_one_loop(s) == 1.0

    def test_pure_gauge_correction_is_positive(self):
        """A = (1/3)(29C) > 0 with no fermions/scalars."""
        s = GaugeSector(name="test", alpha=0.1, C=3.0,
                         R_psi=0.0, R_phi=0.0)
        assert epsilon_one_loop(s) > 1.0

    def test_pure_fermion_correction_is_negative(self):
        """A = (1/3)(−12 R_ψ) < 0 with no gauge/scalars."""
        s = GaugeSector(name="test", alpha=0.1, C=0.0,
                         R_psi=10.0, R_phi=0.0)
        assert epsilon_one_loop(s) < 1.0

    def test_linear_in_alpha(self):
        """ε − 1 ∝ α at fixed (C, R_ψ, R_φ)."""
        kwargs = dict(name="test", C=3.0, R_psi=3.0, R_phi=0.0)
        e_a = epsilon_one_loop(GaugeSector(alpha=0.05, **kwargs))
        e_b = epsilon_one_loop(GaugeSector(alpha=0.10, **kwargs))
        assert abs((e_b - 1.0) - 2 * (e_a - 1.0)) < 1e-12


class TestEpsilonCombined:
    """The weighted combination yields the documented 1.15370."""

    def test_combined_matches_1_15370_to_5e_minus_4(self):
        """ε_combined matches 1.15370 to 5 × 10⁻⁴ (4 decimal places)."""
        eps = epsilon_combined()
        assert abs(eps - 1.15370) < 5e-4

    def test_combined_matches_1_1537_to_3e_minus_4(self):
        """Tighter: ε_combined matches the V7-document 1.1537 figure."""
        eps = epsilon_combined()
        assert abs(eps - 1.1537) < 3e-4

    def test_weights_sum_to_one(self):
        assert math.isclose(
            sum(WEIGHTS_QCD_DOMINANT.values()), 1.0, abs_tol=1e-9,
        )

    def test_qcd_dominant_weighting(self):
        """w_SU3 ≫ w_SU2 ≫ w_U1 at M_Z."""
        assert WEIGHT_SU3 > WEIGHT_SU2 > WEIGHT_U1
        # QCD weight is at least 90% of the combination
        assert WEIGHT_SU3 > 0.90

    def test_invalid_weights_raise(self):
        """Mis-normalized weights should raise rather than silently miscompute."""
        bad = {"SU(3)_c": 0.5, "SU(2)_L": 0.3, "U(1)_Y": 0.1}  # sums to 0.9
        with pytest.raises(ValueError):
            epsilon_combined(weights=bad)

    def test_missing_sector_weight_raises(self):
        bad = {"SU(3)_c": 1.0}
        with pytest.raises(KeyError):
            epsilon_combined(weights=bad)


class TestEpsilonReport:
    def test_report_fields_populated(self):
        rep = epsilon_report()
        assert rep.epsilon_su3 > 1.0
        assert rep.epsilon_su2 > 1.0
        assert rep.epsilon_u1 < 1.0
        assert 1.15 < rep.epsilon_combined < 1.16
        assert rep.target == 1.15370


class TestThreeRoutesConvergence:
    """Routes 1, 2, and 3 agree at the 0.1% level."""

    def test_route_1_is_sqrt_4_over_3(self):
        assert abs(R_ROUTE_1_PATH_G - math.sqrt(4 / 3)) < 1e-12

    def test_route_2_is_v7_historical_value(self):
        assert R_ROUTE_2_V7_HISTORICAL == 1.15428

    def test_route_3_target_is_1_15370(self):
        assert R_ROUTE_3_OSBORN == 1.15370

    def test_three_routes_within_0p15_pct(self):
        """Spread of the three R candidates is below 0.15%."""
        routes = three_routes_convergence()
        assert routes["spread_max_minus_min_pct"] < 0.15

    def test_routes_dictionary_complete(self):
        routes = three_routes_convergence()
        for key in (
            "route_1_path_g_sqrt_4_over_3",
            "route_2_v7_historical",
            "route_3_osborn_epsilon",
            "spread_max_minus_min_pct",
        ):
            assert key in routes

    def test_path_g_and_osborn_agreement(self):
        """The two independent COMPUTED routes (1 and 3) agree at 0.1%."""
        routes = three_routes_convergence()
        path_g = routes["route_1_path_g_sqrt_4_over_3"]
        osborn = routes["route_3_osborn_epsilon"]
        assert abs(path_g - osborn) / path_g < 1e-3


class TestVerifyHarness:

    def test_all_pass(self):
        checks = verify()
        failed = [k for k, v in checks.items() if not v]
        assert not failed, f"Osborn ε verify failures: {failed}"

    def test_returns_six_legs(self):
        checks = verify()
        expected = {
            "epsilon_su3_within_band",
            "epsilon_su2_within_band",
            "epsilon_u1_within_band",
            "epsilon_combined_matches_1_15370",
            "three_routes_converge_within_0p15_pct",
            "weights_sum_to_one",
        }
        assert expected.issubset(checks.keys())


class TestSMCouplings:
    """Sanity bounds on the input couplings (PDG values at M_Z)."""

    def test_alpha_s_at_MZ_in_band(self):
        """α_s(M_Z) ≈ 0.118 ± 0.001 per PDG."""
        assert 0.115 < ALPHA_S_MZ < 0.122

    def test_alpha_2_at_MZ_in_band(self):
        assert 0.030 < ALPHA_2_MZ < 0.040

    def test_alpha_Y_at_MZ_in_band(self):
        assert 0.005 < ALPHA_Y_MZ < 0.015

    def test_strong_coupling_dominates(self):
        """α_s ≫ α_2 ≫ α_Y at M_Z."""
        assert ALPHA_S_MZ > ALPHA_2_MZ > ALPHA_Y_MZ


class TestSectorDefinitions:

    def test_all_sectors_present(self):
        names = {s.name for s in ALL_SM_SECTORS}
        assert names == {"SU(3)_c", "SU(2)_L", "U(1)_Y"}

    def test_su3_is_non_abelian_with_zero_higgs(self):
        assert SU3_SECTOR.C == 3.0
        assert SU3_SECTOR.R_phi == 0.0

    def test_su2_has_higgs(self):
        assert SU2_SECTOR.C == 2.0
        assert SU2_SECTOR.R_phi == 1.0

    def test_u1_is_abelian_with_higgs(self):
        assert U1_SECTOR.C == 0.0
        assert U1_SECTOR.R_phi == 0.5
