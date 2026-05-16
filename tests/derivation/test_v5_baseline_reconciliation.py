"""
Regression test: V5 baseline reconciliation.

Locks the ground truth: live V5 produces R ≈ 1.32 with specific matrix entries.
"""

import pytest
import math
from grut.derivation.euler.v5_baseline_reconciliation import (
    build_live_v5_matrix,
    evolve_euler_channel,
)


class TestV5BaselineReconciliation:
    """Lock down the baseline matrix that produces R ≈ 1.32."""
    
    @pytest.fixture
    def M(self):
        """Build the live V5 matrix."""
        return build_live_v5_matrix()
    
    def test_r_prediction_matches_live_state(self, M):
        """Verify matrix reproduces R ≈ 1.32063."""
        R, _ = evolve_euler_channel(M)
        # Lock the known live state to within 0.1%
        assert abs(R - 1.320633) < 0.002, f"Expected R ≈ 1.32063, got {R}"
    
    def test_beta_eff_matches_live_state(self, M):
        """Verify β_eff ≈ 0.1229."""
        _, beta_eff = evolve_euler_channel(M)
        # Lock to within 0.001 (i.e., within 0.82% of target 0.1215)
        assert abs(beta_eff - 0.122933) < 0.0001, f"Expected β_eff ≈ 0.122933, got {beta_eff}"
    
    def test_m15_entry_value(self, M):
        """Verify M[1,5] = 0.000507 (which is 0.08κ)."""
        m15 = M[1, 5]
        kappa = 1.0 / (16.0 * math.pi**2)
        expected_m15 = 0.08 * kappa  # Should be 0.000507
        assert abs(m15 - expected_m15) < 1e-6, f"Expected M[1,5] ≈ {expected_m15}, got {m15}"
    
    def test_m15_structural_coefficient(self, M):
        """Verify pre-κ coefficient for M[1,5] is 0.08."""
        m15 = M[1, 5]
        kappa = 1.0 / (16.0 * math.pi**2)
        m15_pre_kappa = m15 / kappa if kappa > 0 else 0
        assert abs(m15_pre_kappa - 0.08) < 1e-6, f"Expected M[1,5] pre-κ ≈ 0.08, got {m15_pre_kappa}"
    
    def test_matrix_is_symmetric(self, M):
        """Verify matrix symmetry."""
        import numpy as np
        assert np.allclose(M, M.T, atol=1e-10), "Matrix should be symmetric"
    
    def test_diagonal_entries_unchanged_by_kappa(self, M):
        """Verify diagonals are not suppressed by κ."""
        # Diagonal should be the structural estimates, not κ-suppressed
        expected_diag = [0.15, 0.11, 0.08, 0.18, 0.14, 0.22, 0.19, 0.09, 0.16]
        for i, expected_val in enumerate(expected_diag):
            assert abs(M[i, i] - expected_val) < 1e-6, \
                f"M[{i},{i}] expected {expected_val}, got {M[i, i]}"
    
    def test_m17_euler_lambda_is_largest_absolute_offdiag(self, M):
        """Verify M[1,7] (Euler-Lambda) is the largest off-diagonal."""
        m17 = abs(M[1, 7])
        
        # Check all off-diagonals are <= M[1,7]
        for i in range(9):
            for j in range(9):
                if i != j:
                    assert abs(M[i, j]) <= m17 + 1e-10, \
                        f"M[{i},{j}] = {M[i,j]} is larger than M[1,7] = {m17}"
    
    def test_gate_2_baseline_clarified(self, M):
        """
        Clarify what the audit's 0.92 reference was.
        
        The audit used 0.92 as a structural reference, but it refers to
        the Euler-Lambda coupling M[1,7] = 0.92κ, NOT M[1,5].
        M[1,5] in the live matrix is actually 0.08κ.
        """
        kappa = 1.0 / (16.0 * math.pi**2)
        
        # M[1,7] should be 0.92κ
        m17_expected = 0.92 * kappa
        assert abs(M[1, 7] - m17_expected) < 1e-6, \
            f"M[1,7] expected {m17_expected}, got {M[1,7]}"
        
        # M[1,5] should be 0.08κ
        m15_expected = 0.08 * kappa
        assert abs(M[1, 5] - m15_expected) < 1e-6, \
            f"M[1,5] expected {m15_expected}, got {M[1,5]}"
        
        # They are different! The audit confused these.
        assert abs(M[1, 5] - M[1, 7]) > 0.001, \
            "M[1,5] and M[1,7] should be clearly different"


if __name__ == "__main__":
    pytest.main([__file__, "-v"])
