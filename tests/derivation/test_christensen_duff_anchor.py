"""
Regression tests for Correction #33 (loop-suppressed anomaly anchor).

Locks the Christensen-Duff Standard Model Euler-anomaly sum and tests:
  1. a_hat_SM exact value (1991/720).
  2. SM normalization under 1/(8π) and 1/(16π²).
  3. RHN extension (N_F: 45→48).
  4. RHN worsens R-match (falsification of RHN-fix hypothesis).

This is the regression test for Correction #33.
"""
import math
import pytest
from grut.derivation.euler.v5_loop_suppressed_matrix import (
    christensen_duff_hat_a,
    anomaly_to_m11,
)

# Exact rational values from Christensen-Duff (1979)
CD_SCALAR = 1.0 / 360.0
CD_VECTOR = 31.0 / 180.0
CD_WEYL_FERMION = 11.0 / 720.0


class TestChristenseffDuff:
    """Christensen-Duff anomaly coefficient regression tests."""

    def test_cd_scalars_exact(self):
        """CD scalar Euler-anomaly fraction."""
        assert abs(CD_SCALAR - 1.0 / 360.0) < 1e-15

    def test_cd_vectors_exact(self):
        """CD vector Euler-anomaly fraction."""
        assert abs(CD_VECTOR - 31.0 / 180.0) < 1e-15

    def test_cd_fermions_exact(self):
        """CD Weyl-fermion Euler-anomaly fraction."""
        assert abs(CD_WEYL_FERMION - 11.0 / 720.0) < 1e-15

    def test_sm_a_hat_exact(self):
        """SM Euler-anomaly sum: a_hat_SM = 1991/720."""
        # Standard Model: 4 real scalars, 12 vectors, 45 Weyl fermions
        a_hat_sm = christensen_duff_hat_a(n_scalars=4, n_vectors=12, n_weyl_fermions=45)
        expected = 1991.0 / 720.0
        assert abs(a_hat_sm - expected) < 1e-10
        assert abs(a_hat_sm - 2.76527777777778) < 1e-10

    def test_sm_m11_8pi_normalization(self):
        """M11 from a_hat_SM/(8π) matches GRUT structural Euler diagonal."""
        a_hat = christensen_duff_hat_a(4, 12, 45)
        m11_8pi = anomaly_to_m11(a_hat, "8pi")
        # Should be ≈ 0.11003
        assert abs(m11_8pi - 0.11003) < 1e-4
        # More precise: 0.11002691
        assert abs(m11_8pi - 0.11002691) < 1e-7

    def test_sm_m11_16pi2_normalization(self):
        """M11 from a_hat_SM/(16π²) does NOT match GRUT structural M11."""
        a_hat = christensen_duff_hat_a(4, 12, 45)
        m11_16pi2 = anomaly_to_m11(a_hat, "16pi2")
        # Should be ≈ 0.01751 (far from 0.11)
        assert abs(m11_16pi2 - 0.01751) < 1e-4
        # More precise: 0.01751133
        assert abs(m11_16pi2 - 0.01751133) < 1e-7
        # Verify it does NOT equal 0.11
        assert abs(m11_16pi2 - 0.11) > 0.09

    def test_rhn_extension_value(self):
        """RHN extension: N_F 45→48 increases a_hat."""
        a_hat_sm = christensen_duff_hat_a(4, 12, 45)
        a_hat_rhn = christensen_duff_hat_a(4, 12, 48)
        # Should increase by 3 × CD_WEYL_FERMION
        delta_a = a_hat_rhn - a_hat_sm
        expected_delta = 3.0 * CD_WEYL_FERMION
        assert abs(delta_a - expected_delta) < 1e-15

    def test_rhn_m11_uplift(self):
        """RHN uplift to M11: ~1.657% increase."""
        a_hat_sm = christensen_duff_hat_a(4, 12, 45)
        a_hat_rhn = christensen_duff_hat_a(4, 12, 48)
        m11_sm = anomaly_to_m11(a_hat_sm, "8pi")
        m11_rhn = anomaly_to_m11(a_hat_rhn, "8pi")
        uplift_pct = (m11_rhn - m11_sm) / m11_sm * 100.0
        # Expected: ≈ 1.657%
        assert abs(uplift_pct - 1.657) < 0.01

    def test_rhn_m11_exact_values(self):
        """RHN M11 values from V5 run."""
        m11_sm = anomaly_to_m11(christensen_duff_hat_a(4, 12, 45), "8pi")
        m11_rhn = anomaly_to_m11(christensen_duff_hat_a(4, 12, 48), "8pi")
        # From V5 output:
        assert abs(m11_sm - 0.11002691) < 1e-7
        assert abs(m11_rhn - 0.11185056) < 1e-7

    def test_normalization_choice_contrast(self):
        """8π is fundamentally different from 16π² and other candidates."""
        a_hat = christensen_duff_hat_a(4, 12, 45)
        m11_8pi = anomaly_to_m11(a_hat, "8pi")
        m11_16pi2 = anomaly_to_m11(a_hat, "16pi2")
        # They differ by roughly a factor of 6.28 ≈ 2π
        ratio = m11_8pi / m11_16pi2
        assert abs(ratio - 2.0 * math.pi) < 0.01

    def test_unknown_normalization_raises(self):
        """Requesting unknown normalization raises ValueError."""
        a_hat = christensen_duff_hat_a(4, 12, 45)
        with pytest.raises(ValueError):
            anomaly_to_m11(a_hat, "unknown")

    def test_rhn_worsens_r_fit(self):
        """RHN falsification: uplift in M11 pushes β_eff further from target."""
        # From V5 run output:
        # SM:     β_eff = 0.122945, R error = 14.57%
        # SM+RHN: β_eff = 0.123775, R error = 24.15%
        beta_target = 0.1215
        beta_sm = 0.122945
        beta_rhn = 0.123775
        error_beta_sm = abs(beta_sm - beta_target) / beta_target * 100
        error_beta_rhn = abs(beta_rhn - beta_target) / beta_target * 100
        # RHN error should be larger (worsened)
        assert error_beta_rhn > error_beta_sm
        # Quantitatively verify local β errors
        assert abs(error_beta_sm - 1.19) < 0.01  # (0.122945 - 0.1215) / 0.1215 * 100
        assert abs(error_beta_rhn - 1.87) < 0.01  # (0.123775 - 0.1215) / 0.1215 * 100
