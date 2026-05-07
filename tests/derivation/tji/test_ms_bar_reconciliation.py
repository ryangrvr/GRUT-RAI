"""
Tests for TJI Phase-0.5 MS-bar reconciliation.
All tests use exact Fraction equality, never float approximations.
"""

import pytest
from fractions import Fraction
import sympy as sp
from sympy import EulerGamma, log, pi, Rational

from grut_solver.derivation.tji.flat_space import (
    ms_bar_absorption_factor,
    laurent_expansion_raw,
    reconcile_to_ms_bar,
    finite_rational_ms_bar_scheme,
    MS_BAR_EPSILON_ZERO_EXPECTED,
    RAW_SCHEME_EPSILON_ZERO,
)

class TestRawLaurent:
    """Test raw Laurent expansion values."""
    def test_raw_eps_values(self):
        raw = laurent_expansion_raw()
        assert raw['1/eps2'] == Rational(-1, 64)
        assert raw['1/eps'] == Rational(-25, 384)
        assert raw['eps0'] == Rational(-541, 2304)

class TestAbsorptionFactor:
    """Test absorption factor structure."""
    def test_absorption_returns_expr(self):
        factor = ms_bar_absorption_factor(n_loops=2, order=3)
        assert isinstance(factor, sp.Expr)

class TestReconciliation:
    """Test the reconciliation result."""
    def test_reconciliation_returns_tuple(self):
        result, details = reconcile_to_ms_bar()
        assert isinstance(result, sp.Expr)
        assert isinstance(details, dict)

class TestFiniteRationalMSBar:
    """Test the final pipeline."""
    def test_returns_dict(self):
        result = finite_rational_ms_bar_scheme()
        assert isinstance(result, dict)
        assert 'status' in result

if __name__ == '__main__':
    pytest.main([__file__, '-v'])
