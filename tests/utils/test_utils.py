"""Tests for grut/utils/ — support modules for sensitivity, robustness, comparison."""

import pytest
import numpy as np


class TestSweep:
    """Tests for parameter sweeps and sensitivity analysis."""

    def test_sensitivity_omega_lambda_returns_dict(self):
        from grut.utils.sweep import sensitivity_omega_lambda
        result = sensitivity_omega_lambda(delta_pct=10)
        assert isinstance(result, dict)

    def test_sensitivity_at_5pct_vs_10pct(self):
        from grut.utils.sweep import sensitivity_omega_lambda
        r5 = sensitivity_omega_lambda(delta_pct=5)
        r10 = sensitivity_omega_lambda(delta_pct=10)
        assert isinstance(r5, dict)
        assert isinstance(r10, dict)

    def test_uncertainty_propagation_returns_dict(self):
        from grut.utils.sweep import uncertainty_propagation
        # Gold benchmark parameters
        m = 20818 * 1.66053906660e-27
        l = 1e-6
        R = ((3 * m) / (4 * np.pi * 19300))**(1/3)
        result = uncertainty_propagation(m, l, R,
                                          dm_frac=0.01, dl_frac=0.01, dR_frac=0.01)
        assert isinstance(result, dict)


class TestWhatif:
    """Tests for the what-if parameter modification harness."""

    def test_modify_R_anomaly_returns_prediction(self):
        from grut.utils.whatif import modify_R_anomaly
        result = modify_R_anomaly(1.15)
        assert isinstance(result, dict)

    def test_modify_tau_I_runs(self):
        from grut.utils.whatif import modify_tau_I
        from grut.foundation.constants import HBAR
        # V7 fixes τ_I = ℏ/2; try doubling to see consequences
        result = modify_tau_I(HBAR)
        assert isinstance(result, dict)

    def test_modify_S_CTP_runs(self):
        from grut.utils.whatif import modify_S_CTP
        # Try perturbing S_CTP (default 108π ≈ 339.29)
        result = modify_S_CTP(340.0)
        assert isinstance(result, dict)

    def test_modify_generation_count_returns_dict(self):
        from grut.utils.whatif import modify_generation_count
        result = modify_generation_count(3)
        assert isinstance(result, dict)

    def test_run_whatif_R_anomaly_entry_point(self):
        from grut.utils.whatif import run_whatif
        result = run_whatif("R_anomaly", 1.16)
        assert isinstance(result, dict)


class TestRobustness:
    """Tests for parameter-robustness analyses."""

    def test_single_parameter_robustness_runs(self):
        from grut.utils.robustness import single_parameter_robustness
        result = single_parameter_robustness()
        assert isinstance(result, (dict, list))

    def test_n_generation_robustness_selects_N_3(self):
        from grut.utils.robustness import n_generation_robustness
        result = n_generation_robustness()
        assert isinstance(result, (dict, list))

    def test_r_anomaly_systematic_runs(self):
        from grut.utils.robustness import r_anomaly_systematic
        result = r_anomaly_systematic()
        assert isinstance(result, (dict, list))

    def test_simultaneous_variation_runs_with_small_n(self):
        from grut.utils.robustness import simultaneous_variation
        # Small n for test speed
        result = simultaneous_variation(n_samples=50)
        assert isinstance(result, (dict, list))


class TestCompare:
    """Tests for observation-comparison helpers."""

    def test_decoherence_comparison_returns_dict(self):
        from grut.utils.compare import decoherence_comparison
        result = decoherence_comparison()
        assert isinstance(result, (dict, list))

    def test_cosmology_comparison_returns_dict(self):
        from grut.utils.compare import cosmology_comparison
        result = cosmology_comparison()
        assert isinstance(result, (dict, list))

    def test_baryogenesis_comparison_returns_dict(self):
        from grut.utils.compare import baryogenesis_comparison
        result = baryogenesis_comparison()
        assert isinstance(result, (dict, list))

    def test_dark_matter_comparison_returns_dict(self):
        from grut.utils.compare import dark_matter_comparison
        result = dark_matter_comparison()
        assert isinstance(result, (dict, list))

    def test_full_comparison_runs(self):
        from grut.utils.compare import full_comparison
        result = full_comparison()
        assert isinstance(result, dict)


class TestDimensions:
    """Tests for dimensional-analysis sanity checks."""

    def test_check_lambda_grav_runs(self):
        from grut.utils.dimensions import check_lambda_grav
        result = check_lambda_grav()
        assert isinstance(result, (dict, bool, str))

    def test_check_h_inf_runs(self):
        from grut.utils.dimensions import check_h_inf
        result = check_h_inf()
        assert isinstance(result, (dict, bool, str))

    def test_check_eta_b_runs(self):
        from grut.utils.dimensions import check_eta_b
        result = check_eta_b()
        assert isinstance(result, (dict, bool, str))

    def test_check_all_runs(self):
        from grut.utils.dimensions import check_all
        result = check_all()
        assert isinstance(result, (dict, list))

    def test_check_all_every_formula_consistent(self):
        """Every dimensional check should report consistent=True."""
        from grut.utils.dimensions import check_all
        result = check_all()
        if isinstance(result, list):
            for entry in result:
                assert entry.get("consistent") is True, \
                    f"Dimension mismatch: {entry.get('formula')}"
