"""
TJI flat-space 2-loop T_2 reduction — Phase-0.5 MS-bar reconciliation.

PHASE-0.5 STATUS: PENDING (Failure mode A - transcendentals not canceling)

This module investigates the reconciliation from raw dimensional regularization
scheme to MS-bar convention. The standard Collins MS-bar absorption factor
[Γ(1+ε)⁻¹ · (4π)^ε]² does not produce cancellation of transcendental terms.
"""

from fractions import Fraction
import sympy as sp
from sympy import symbols, gamma, log, pi, series, simplify, nsimplify, expand
from sympy import EulerGamma, preorder_traversal, Rational, trigsimp
from typing import Dict, Tuple, Optional, Any

# SymPy constants and symbols
EPS = symbols('epsilon', real=True)
MS_BAR_EPSILON_ZERO_EXPECTED = Fraction(7, 4)
RAW_SCHEME_EPSILON_ZERO = Fraction(-541, 2304)
ARITHMETIC_SHIFT_TARGET = Fraction(4573, 2304)

def laurent_expansion_raw() -> Dict[str, Rational]:
    """Raw-scheme Laurent expansion of 2-loop T_2 reduction."""
    return {
        '1/eps2': Rational(-1, 64),
        '1/eps': Rational(-25, 384),
        'eps0': Rational(-541, 2304),
    }

def ms_bar_absorption_factor(n_loops: int = 2, order: int = 3) -> sp.Expr:
    """Standard MS-bar absorption factor: [Γ(1+ε)⁻¹ · (4π)^ε]^n_loops."""
    per_loop = (1 / gamma(1 + EPS)) * (4 * pi) ** EPS
    factor = per_loop ** n_loops
    expanded = series(factor, EPS, 0, n=order)
    return expanded

def _extract_laurent_coefficients(expr: sp.Expr) -> Dict[str, sp.Expr]:
    """Extract Laurent coefficients using .coeff() method."""
    coeffs = {}
    expr_clean = expr.removeO() if hasattr(expr, 'removeO') else expr
    power_map = {
        -2: '1/eps2',
        -1: '1/eps',
        0: 'eps0',
        1: 'eps1',
        2: 'eps2',
    }
    for power, key in power_map.items():
        coeff = expr_clean.coeff(EPS, power)
        coeffs[key] = coeff if coeff is not None else 0
    return coeffs

def reconcile_to_ms_bar(raw_laurent: Optional[Dict[str, Rational]] = None) -> Tuple[sp.Expr, Dict[str, Any]]:
    """Reconcile raw Laurent to MS-bar via standard absorption factor."""
    if raw_laurent is None:
        raw_laurent = laurent_expansion_raw()

    absorption = ms_bar_absorption_factor(n_loops=2, order=3)
    raw_eps2, raw_eps, raw_eps0 = raw_laurent['1/eps2'], raw_laurent['1/eps'], raw_laurent['eps0']

    abs_coeffs = _extract_laurent_coefficients(absorption)
    abs_eps2 = abs_coeffs.get('eps2', 0)
    abs_eps = abs_coeffs.get('eps1', 0)
    abs_eps0 = abs_coeffs.get('eps0', 1)

    T1 = raw_eps2 * abs_eps2
    T2 = raw_eps * abs_eps
    T3 = raw_eps0 * abs_eps0

    sum_before = T1 + T2 + T3
    sum_after = expand(sum_before)
    sum_after = simplify(sum_after)
    try:
        sum_after = trigsimp(sum_after)
    except:
        pass
    sum_after = nsimplify(sum_after, rational=True)

    has_gamma = EulerGamma in sum_after.free_symbols
    has_log = any(expr == log(4 * pi) for expr in preorder_traversal(sum_after))
    transcendentals_canceled = not (has_gamma or has_log)

    details = {
        'raw_eps2': raw_eps2, 'raw_eps': raw_eps, 'raw_eps0': raw_eps0,
        'absorption_eps2': abs_eps2, 'absorption_eps': abs_eps,
        'T1': T1, 'T2': T2, 'T3': T3,
        'sum_before_simplify': sum_before, 'sum_after_simplify': sum_after,
        'transcendentals_canceled': transcendentals_canceled,
    }
    return sum_after, details

def finite_rational_ms_bar_scheme() -> Dict[str, Any]:
    """End-to-end reconciliation pipeline."""
    try:
        reconciled_expr, details = reconcile_to_ms_bar()
        if not details['transcendentals_canceled']:
            return {
                'status': 'FAILED: Transcendentals did not cancel',
                'transcendentals_canceled': False,
                'sum_after_simplify': details['sum_after_simplify'],
                'matches_expected': False,
            }
        try:
            rational_result = Rational(reconciled_expr)
            python_fraction = Fraction(int(rational_result.p), int(rational_result.q))
            matches = (python_fraction == MS_BAR_EPSILON_ZERO_EXPECTED)
            return {
                'status': 'SUCCESS' if matches else 'MISMATCH',
                'python_fraction': python_fraction,
                'transcendentals_canceled': True,
                'matches_expected': matches,
            }
        except:
            return {
                'status': 'PARTIAL: Cannot convert to rational',
                'transcendentals_canceled': details['transcendentals_canceled'],
                'matches_expected': False,
            }
    except Exception as e:
        return {'status': f'ERROR: {str(e)}', 'matches_expected': False}
