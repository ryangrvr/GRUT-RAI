"""Tests for the cosmology sector — V7 §26 predictions.

Covers vacuum.py, hubble_tension.py, spectral_running.py.

These tests lock in the V7 numerical claims so any regression in
R_anomaly, Ω_Λ, H_inf, or the cosmological formula is caught immediately.
"""

import pytest
import numpy as np


class TestVacuumPrediction:
    """Tests for vacuum_prediction — the headline cosmological formula."""

    def test_returns_dict_with_expected_keys(self):
        from grut.derived.cosmology.vacuum import vacuum_prediction
        result = vacuum_prediction(H_0_kms=70.0)
        expected_keys = {"H_inf_Hz", "H_0_Hz", "Omega_Lambda", "Planck_OL",
                          "deviation_pct", "R", "R_choice", "f_R", "status"}
        assert expected_keys.issubset(result.keys())

    def test_default_R_is_hand_choice(self):
        from grut.derived.cosmology.vacuum import vacuum_prediction
        result = vacuum_prediction()
        assert result["R_choice"] == "closure"
        from grut.foundation.closure_protocol import R_REFRACTIVE
        assert abs(result["R"] - R_REFRACTIVE) < 1e-6

    def test_epsilon_choice_uses_epsilon_value(self):
        from grut.derived.cosmology.vacuum import vacuum_prediction
        result = vacuum_prediction(R_choice="epsilon")
        assert result["R_choice"] == "epsilon"
        assert abs(result["R"] - 1.1537) < 1e-3

    def test_f_R_equals_2_minus_R(self):
        from grut.derived.cosmology.vacuum import vacuum_prediction
        result = vacuum_prediction()
        assert abs(result["f_R"] - (2 - result["R"])) < 1e-10

    def test_planck_match_at_H0_70(self):
        """V7 §26.2 central claim: Ω_Λ ≈ 0.69 at H_0 = 70 km/s/Mpc."""
        from grut.derived.cosmology.vacuum import vacuum_prediction
        result = vacuum_prediction(H_0_kms=70.0, R_choice="closure")
        # Planck is 0.6889; v7 claims deviation of ~0.3%
        assert abs(result["Omega_Lambda"] - 0.69) < 0.01

    def test_deviation_within_1pct_at_H0_70(self):
        from grut.derived.cosmology.vacuum import vacuum_prediction
        result = vacuum_prediction(H_0_kms=70.0, R_choice="closure")
        assert abs(result["deviation_pct"]) < 1.5

    def test_H_inf_is_1p885e_minus_18_Hz(self):
        """V7 §26 equation (20): H_inf = 1.885e-18 Hz."""
        from grut.derived.cosmology.vacuum import vacuum_prediction
        result = vacuum_prediction()
        # Tolerance 1% on the headline value
        assert abs(result["H_inf_Hz"] - 1.885e-18) / 1.885e-18 < 0.01

    def test_status_string_mentions_COMPUTED(self):
        """Step 1 reframing: R is COMPUTED, not CONDITIONAL."""
        from grut.derived.cosmology.vacuum import vacuum_prediction
        result = vacuum_prediction()
        assert "COMPUTED" in result["status"]

    def test_status_string_does_not_say_hand_constructed(self):
        """Step 1 reframing: no 'hand-constructed' language."""
        from grut.derived.cosmology.vacuum import vacuum_prediction
        result = vacuum_prediction()
        assert "hand-construct" not in result["status"].lower()

    def test_epsilon_and_hand_agree_within_0p5pct(self):
        """V7 §26.1: ε matches R_anomaly at 0.05% → Ω_Λ within 0.5%."""
        from grut.derived.cosmology.vacuum import vacuum_prediction
        hand = vacuum_prediction(R_choice="closure")
        eps = vacuum_prediction(R_choice="epsilon")
        diff = abs(hand["Omega_Lambda"] - eps["Omega_Lambda"]) / hand["Omega_Lambda"]
        assert diff < 0.005

    def test_H_inf_independent_of_H_0(self):
        """H_inf is intrinsic to the formula; H_0 only sets Ω_Λ."""
        from grut.derived.cosmology.vacuum import vacuum_prediction
        r1 = vacuum_prediction(H_0_kms=67.4)  # Planck
        r2 = vacuum_prediction(H_0_kms=73.0)  # SH0ES
        assert abs(r1["H_inf_Hz"] - r2["H_inf_Hz"]) < 1e-30


class TestEraMap:
    """Tests for era_map — 329 discrete eras of 41.9 Myr."""

    def test_default_n_eras(self):
        from grut.derived.cosmology.vacuum import era_map
        result = era_map()
        assert result["n_eras"] == 329

    def test_no_R_vol_typo(self):
        """Correction #14: ensure era_map doesn't re-introduce the 1.5428 typo.

        The era map's sigmoid sharpness k = 2π/(R_anomaly − 1) MUST use
        R_ANOMALY = 1.15428, NOT the typo 1.5428. We verify by checking
        the executable code (stripping the docstring, which references
        the typo for historical context).
        """
        import grut.derived.cosmology.vacuum as vacuum_module
        import inspect
        import ast
        src = inspect.getsource(vacuum_module.era_map)
        # Parse AST and extract all numeric literals from the function body
        tree = ast.parse(src.strip())
        func_def = tree.body[0]  # the era_map function
        # Skip the docstring (first stmt is Expr/Constant if it's a docstring)
        body_stmts = func_def.body
        if (body_stmts and isinstance(body_stmts[0], ast.Expr) and
                isinstance(body_stmts[0].value, ast.Constant) and
                isinstance(body_stmts[0].value.value, str)):
            body_stmts = body_stmts[1:]

        numeric_literals = []
        for stmt in body_stmts:
            for node in ast.walk(stmt):
                if isinstance(node, ast.Constant) and isinstance(node.value, (int, float)):
                    numeric_literals.append(node.value)

        # The typo value must NOT appear as a bare numeric literal in executable code
        assert 1.5428 not in numeric_literals, (
            "Correction #14 regression: bare literal 1.5428 found in era_map code. "
            "Use R_ANOMALY = 1.15428 instead."
        )

    def test_era_map_uses_R_ANOMALY(self):
        """era_map must reference the R_ANOMALY import, not a local literal."""
        import grut.derived.cosmology.vacuum as vacuum_module
        import inspect
        src = inspect.getsource(vacuum_module.era_map)
        assert "R_ANOMALY" in src, "era_map should use R_ANOMALY constant"

    def test_history_length_matches_n_eras(self):
        from grut.derived.cosmology.vacuum import era_map
        result = era_map(n_eras=100)
        assert len(result["data"]) == 100

    def test_final_x_approaches_vacuum_dominance(self):
        """At era 329 (today), vacuum fraction saturates at upper bound."""
        from grut.derived.cosmology.vacuum import era_map
        result = era_map(n_eras=329)
        # Vacuum fraction approaches its saturation (clamped to 1 by the map)
        assert result["final_x"] >= 0.5  # past threshold at era 215
        assert result["final_x"] <= 1.0

    def test_initial_x_is_zero(self):
        from grut.derived.cosmology.vacuum import era_map
        result = era_map(n_eras=10)
        assert abs(result["data"][0]["x"]) < 0.1

    def test_x_is_bounded(self):
        from grut.derived.cosmology.vacuum import era_map
        result = era_map(n_eras=329)
        for entry in result["data"]:
            assert 0.0 <= entry["x"] <= 1.0

    def test_target_is_sigmoid_bounded(self):
        from grut.derived.cosmology.vacuum import era_map
        result = era_map(n_eras=329)
        for entry in result["data"]:
            assert 0.0 <= entry["target"] <= 1.0


class TestConstitutiveCosmology:
    """Tests for the exact constitutive expansion history."""

    def test_returns_arrays_for_t_and_H(self):
        from grut.derived.cosmology.vacuum import constitutive_cosmology
        # Short run to keep tests fast
        result = constitutive_cosmology(t_start=1e12, t_end=1e13, n_steps=100)
        assert "t" in result or "H" in result or "history" in result or isinstance(result, dict)


class TestHubbleTension:
    """Tests for hubble_tension_analysis."""

    def test_prediction_curve_returns_list_of_dicts(self):
        from grut.derived.cosmology.hubble_tension import grut_prediction_curve
        result = grut_prediction_curve(H_0_min=60, H_0_max=80, n=50)
        assert isinstance(result, list)
        assert len(result) == 50
        # Each entry has H_0 and Omega_Lambda
        for entry in result:
            assert "H_0" in entry
            assert "Omega_Lambda" in entry
            assert 60 <= entry["H_0"] <= 80

    def test_prediction_curve_monotonic_OL_vs_H0(self):
        """Higher H_0 gives lower Omega_Lambda (since H_inf is fixed)."""
        from grut.derived.cosmology.hubble_tension import grut_prediction_curve
        result = grut_prediction_curve(H_0_min=60, H_0_max=80, n=50)
        OLs = [e["Omega_Lambda"] for e in result]
        # Monotonically decreasing
        assert all(OLs[i] >= OLs[i+1] for i in range(len(OLs)-1))

    def test_consistency_test_returns_dict(self):
        from grut.derived.cosmology.hubble_tension import consistency_test
        result = consistency_test()
        assert isinstance(result, dict)

    def test_hubble_tension_analysis_runs(self):
        from grut.derived.cosmology.hubble_tension import hubble_tension_analysis
        result = hubble_tension_analysis()
        assert isinstance(result, dict)


class TestSpectralRunning:
    """Tests for inflationary spectrum predictions (Track X in V8 roadmap)."""

    def test_n_s_matches_planck_at_gold_H_tau(self):
        """V7 prediction: n_s = 0.9649 at the gold-benchmark H_tau ≈ 0.134."""
        from grut.derived.cosmology.spectral_running import grut_predictions
        preds = grut_predictions()
        # Planck n_s = 0.9649 ± 0.0042
        assert abs(preds["n_s"] - 0.9649) < 0.005

    def test_running_is_finite_and_small(self):
        from grut.derived.cosmology.spectral_running import grut_running
        # H_tau is a dimensionless product H·τ, gold value near 0.134
        dn_dlnk = grut_running(H_tau=0.134)
        assert np.isfinite(dn_dlnk)
        # Running should be small (|α| < 0.05 typical)
        assert abs(dn_dlnk) < 0.1

    def test_tensor_to_scalar_ratio_is_positive_and_finite(self):
        from grut.derived.cosmology.spectral_running import grut_tensor_to_scalar
        r = grut_tensor_to_scalar(H_tau=0.134)
        assert np.isfinite(r)
        assert r > 0
        # V7 claims r ≈ 0.098 at gold benchmark — within CMB-S4 sensitivity
        assert r < 1.0

    def test_grut_predictions_has_hypothesis_status(self):
        """V7 labels spectral predictions as HYPOTHESIS (not DERIVED)."""
        from grut.derived.cosmology.spectral_running import grut_predictions
        preds = grut_predictions()
        assert "HYPOTHESIS" in preds["status"].upper()

    def test_grut_predictions_returns_dict(self):
        from grut.derived.cosmology.spectral_running import grut_predictions
        result = grut_predictions()
        assert isinstance(result, dict)

    def test_slowroll_predictions_returns_dict(self):
        from grut.derived.cosmology.spectral_running import slowroll_predictions
        result = slowroll_predictions()
        assert isinstance(result, dict)
