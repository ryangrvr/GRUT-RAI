"""MS scheme variant audit — test each absorption convention."""

from fractions import Fraction
import sympy as sp
from sympy import Rational, EulerGamma, log, pi, preorder_traversal, simplify, nsimplify, expand
from typing import Dict, Any, Optional

# Import from local modules
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).parent))

from ms_scheme_variants import SCHEME_REGISTRY, MSSchemeVariant


def audit_scheme(scheme: MSSchemeVariant, n_loops: int = 2, order: int = 3) -> Dict[str, Any]:
    """Audit a single MS scheme against raw Laurent coefficients."""
    
    # Raw coefficients
    raw_eps2 = Rational(-1, 64)
    raw_eps = Rational(-25, 384)
    raw_eps0 = Rational(-541, 2304)
    
    from sympy import symbols
    EPS = symbols('epsilon', real=True)
    
    try:
        # Get absorption factor
        absorption = scheme.absorption_factor(n_loops=n_loops, order=order)
        
        # Extract coefficients using .coeff() method
        expr_clean = absorption.removeO() if hasattr(absorption, 'removeO') else absorption
        abs_eps2 = expr_clean.coeff(EPS, 2)
        abs_eps = expr_clean.coeff(EPS, 1)
        abs_eps0 = expr_clean.coeff(EPS, 0)
        
        if abs_eps2 is None: abs_eps2 = 0
        if abs_eps is None: abs_eps = 0
        if abs_eps0 is None: abs_eps0 = 1
        
        # Compute cross terms
        T1 = raw_eps2 * abs_eps2
        T2 = raw_eps * abs_eps
        T3 = raw_eps0 * abs_eps0
        
        # Sum and simplify
        total = T1 + T2 + T3
        total = expand(total)
        total = simplify(total)
        total = nsimplify(total, rational=True)
        
        # Check for transcendentals
        has_gamma = EulerGamma in total.free_symbols
        has_log2 = any(expr == log(2) for expr in preorder_traversal(total))
        has_logpi = any(expr == log(pi) for expr in preorder_traversal(total))
        has_pi2 = any(expr == pi ** 2 for expr in preorder_traversal(total))
        
        cancel = not (has_gamma or has_log2 or has_logpi or has_pi2)
        
        # Try rational extraction
        matches = False
        try:
            if cancel:
                rat = Rational(total)
                frac = Fraction(int(rat.p), int(rat.q))
                matches = (frac == Fraction(7, 4))
        except:
            pass
        
        residuals = []
        if has_gamma: residuals.append("γ_E")
        if has_log2: residuals.append("ln(2)")
        if has_logpi: residuals.append("ln(π)")
        if has_pi2: residuals.append("π²")
        
        return {
            'scheme_name': scheme.name,
            'status': 'SUCCESS' if matches else 'FAILED',
            'transcendentals_canceled': cancel,
            'residual_transcendentals': residuals,
            'matches_expected': matches,
        }
    except Exception as e:
        return {
            'scheme_name': scheme.name,
            'status': 'ERROR',
            'error': str(e),
            'transcendentals_canceled': False,
            'matches_expected': False,
        }


def audit_all_schemes() -> Dict[str, Dict[str, Any]]:
    """Audit all registered schemes."""
    results = {}
    for name, scheme in SCHEME_REGISTRY.items():
        results[name] = audit_scheme(scheme)
    return results
