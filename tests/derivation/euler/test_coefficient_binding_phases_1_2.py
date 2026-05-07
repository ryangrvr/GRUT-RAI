"""Tests for Euler-Channel Coefficient Symbol Binding (Phases 1-2)."""

import pytest


class TestPhase1:
    """Test Phase 1: Coefficient symbol identification."""

    def test_euler_coefficient_defined(self):
        from grut_solver.derivation.euler.coefficient_binding import EulerAnomalyCoefficient
        euler = EulerAnomalyCoefficient()
        symbol_def = euler.symbol_definition()
        assert symbol_def['symbol_name'] == 'a_γ'
        assert symbol_def['anomaly_protection'] is True

    def test_c_final_value(self):
        from grut_solver.derivation.euler.coefficient_binding import EulerAnomalyCoefficient
        euler = EulerAnomalyCoefficient()
        assert 1.1e-4 < euler.c_final < 1.2e-4


class TestPhase2:
    """Test Phase 2: Scheme-invariance theorems."""

    def test_quotient_cancellation_proof(self):
        from grut_solver.derivation.euler.scheme_invariance import QuotientCancellationProof
        qcp = QuotientCancellationProof()
        proof = qcp.proof_outline()
        assert 'theorem' in proof
        assert 'conclusion' in proof

    def test_rg_invariance(self):
        from grut_solver.derivation.euler.scheme_invariance import RGInvarianceOfQuotient
        rig = RGInvarianceOfQuotient()
        rg = rig.rg_flow_structure()
        assert 'd(ln Q)/d log μ = 0' in rg.get('statement', '')


class TestSummaries:
    """Test that phase summaries work."""

    def test_phase_1_summary(self):
        from grut_solver.derivation.euler.coefficient_binding import phase_1_summary
        summary = phase_1_summary()
        assert summary['status'] == 'COMPLETE (structural analysis)'

    def test_phase_2_summary(self):
        from grut_solver.derivation.euler.scheme_invariance import phase_2_summary
        summary = phase_2_summary()
        assert 'COMPLETE' in summary['status']


if __name__ == '__main__':
    pytest.main([__file__, '-v'])
