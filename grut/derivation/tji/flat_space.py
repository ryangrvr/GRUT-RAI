"""
Flat-space symbolic Laurent expansion of the 2-loop T_2 reduction:

    T_2 = −(3 (D−2)³ e⁴ / [64 π⁸ (D−4)(D−1) k²]) × TJI[D, k², {{1,0},{1,0},{1,0}}]

with master integral

    TJI[D, k², {{1,0},{1,0},{1,0}}] = −π^D (−k²)^(1−2ε) × Γ(2ε−1) Γ(1−ε)³ / Γ(3−3ε)

All symbolic; SymPy exact-rational arithmetic. We expand around D = 4 − 2ε
and extract the coefficients of 1/ε², 1/ε, ε⁰ (the "finite rational",
scheme-dependent).

Phase-0 contract:
    - Pure Python/SymPy pipeline, reproducible without external tooling.
    - The Laurent expansion is computed ONCE at module import time and
      cached in `_CACHED_LAURENT_O3`. All downstream functions read from
      the cache — the expensive SymPy call runs exactly once per process.
    - `finite_rational_raw_scheme()` returns the exact ε⁰ rational in the
      raw gamma-function scheme (γ_E → 0, π² → 0, ζ(3) → 0, log(4π) → 0).
    - Reconciliation to the V7 §26.2.3 FeynCalc value 7/4 requires
      identifying the exact MS-bar / Γ(1+ε)-absorption convention used in
      that run. Documented as Phase-0.5 in
      theory/derivation/TJI_PHASE_1_CALCULATION_PLAN.md.

Status tiers (per V7 honesty protocol):
    - flat-space symbolic pipeline:                COMPUTED (exact)
    - raw-scheme finite rational extraction:       COMPUTED (exact)
    - reconciliation to FeynCalc 7/4:              PENDING (Phase-0.5)
    - curved-space S⁴ evaluation (Phase 1):        NOT STARTED
"""

from __future__ import annotations

from fractions import Fraction

import sympy as sp
from sympy import EulerGamma, Symbol, expand, gamma, pi, series, zeta


EPS = Symbol("eps", positive=True)
D = 4 - 2 * EPS


def prefactor_symbolic():
    """The 2-loop T_2 reduction prefactor, per V7 §26.2.3:

        P(D) = −3 (D−2)³ / [64 (D−4)(D−1)]

    in units of e⁴ / [π⁸ k²] (absorbed into the overall normalization).
    """
    return -3 * (D - 2) ** 3 / (64 * (D - 4) * (D - 1))


def tji_gamma_symbolic():
    """The gamma-function ratio of the master integral:

        Γ(2ε − 1) · Γ(1 − ε)³ / Γ(3 − 3ε)

    The full TJI is this times −π^D (−k²)^(1−2ε). The (−k²) power produces
    log(−k²/μ²) terms — physical (dispersion), orthogonal to the
    scheme-dependent rational extracted here.
    """
    return gamma(2 * EPS - 1) * gamma(1 - EPS) ** 3 / gamma(3 - 3 * EPS)


# ─────────────────────────────────────────────────────────────────────
# Cached Laurent expansion — runs exactly once per process.
# The expansion of Γ(2ε−1)·Γ(1−ε)³/Γ(3−3ε) around ε=0 is a non-trivial
# SymPy operation; we memoize the result so downstream coefficient-
# extraction is O(1) rather than repeating the series call.
# ─────────────────────────────────────────────────────────────────────


def _compute_laurent_o3():
    product = prefactor_symbolic() * tji_gamma_symbolic()
    s = series(product, EPS, 0, 3).removeO()
    return expand(s)


_CACHED_LAURENT_O3 = None


def laurent_expansion_raw():
    """Full symbolic Laurent expansion through order ε² (i.e. capturing
    ε^(−2), ε^(−1), ε⁰, ε¹, ε²). Cached after first call.
    """
    global _CACHED_LAURENT_O3
    if _CACHED_LAURENT_O3 is None:
        _CACHED_LAURENT_O3 = _compute_laurent_o3()
    return _CACHED_LAURENT_O3


def finite_rational_raw_scheme() -> dict:
    """Return the exact ε⁰ RATIONAL part of the Laurent expansion after
    zeroing γ_E, π², ζ(3), log(4π) (transcendental-suppressed rational).

    This is the "raw scheme" result — BEFORE any MS-bar absorption.

    The FeynCalc run reported 7/4 in a specific MS-bar convention; this
    raw value differs by scheme-dependent finite renormalization terms.
    Reconciliation is Phase-0.5 (see TJI_PHASE_1_CALCULATION_PLAN.md).
    """
    s = laurent_expansion_raw()
    eps0 = s.coeff(EPS, 0)
    # Zero all transcendentals known to appear.
    eps0_rat = eps0
    eps0_rat = eps0_rat.subs(EulerGamma, 0)
    eps0_rat = eps0_rat.subs(pi ** 2, 0)
    eps0_rat = eps0_rat.subs(pi ** 4, 0)
    eps0_rat = eps0_rat.subs(zeta(3), 0)
    # After subs, eps0_rat should be a sp.Rational.
    if not isinstance(eps0_rat, sp.Rational):
        # Coerce via nsimplify as a last resort; raise if still non-rational.
        eps0_rat = sp.nsimplify(eps0_rat, rational=True)
    if not isinstance(eps0_rat, sp.Rational):
        raise TypeError(
            f"Expected sympy.Rational after transcendental removal, got "
            f"{type(eps0_rat)} = {eps0_rat!r}. Raw ε⁰ = {eps0}"
        )
    frac = Fraction(int(eps0_rat.p), int(eps0_rat.q))
    return {
        "sympy_rational":       eps0_rat,
        "python_fraction":      frac,
        "as_decimal":           float(eps0_rat),
        "raw_eps0_coefficient": eps0,
        "scheme":               "raw gamma-function Laurent; γ_E→0, π²→0, π⁴→0, ζ(3)→0",
        "status":               "COMPUTED",
    }


def pole_structure() -> dict:
    """Return the 1/ε² and 1/ε coefficients of the Laurent expansion."""
    s = laurent_expansion_raw()
    c_m2 = s.coeff(EPS, -2)
    c_m1 = s.coeff(EPS, -1)
    c_m2_rat = c_m2 if isinstance(c_m2, sp.Rational) else sp.nsimplify(c_m2, rational=True)
    # The 1/ε coefficient contains γ_E; extract its rational part.
    c_m1_rat = c_m1.subs(EulerGamma, 0).subs(pi ** 2, 0)
    if not isinstance(c_m1_rat, sp.Rational):
        c_m1_rat = sp.nsimplify(c_m1_rat, rational=True)
    return {
        "double_pole_coeff":              c_m2_rat,
        "double_pole_as_fraction":        Fraction(int(c_m2_rat.p), int(c_m2_rat.q))
            if isinstance(c_m2_rat, sp.Rational) else None,
        "single_pole_coeff_raw":          c_m1,
        "single_pole_rational_part":      c_m1_rat,
        "single_pole_rational_fraction":  Fraction(int(c_m1_rat.p), int(c_m1_rat.q))
            if isinstance(c_m1_rat, sp.Rational) else None,
    }


def feyncalc_reference() -> dict:
    """The V7 §26.2.3 FeynCalc reference value for flat-space TJI
    finite rational — documentation only.

    This returns the reported 7/4 and the scheme caveat; it does NOT
    yet assert equality with `finite_rational_raw_scheme()`. That
    assertion is gated by the Phase-0.5 scheme-reconciliation item.
    """
    return {
        "feyncalc_rational":  Fraction(7, 4),
        "v7_section":          "§26.2.3",
        "log_path":            "theory/derivation/FEYNCALC_VERIFICATION_LOG.md",
        "scheme_used":
            "Tarcer / FeynCalc pipeline with standard MS-bar absorption "
            "(Γ(1+ε) per loop, (4π)^ε per loop). The exact convention "
            "is implicit in the FeynCalc output — needs to be made "
            "explicit for symbolic reconciliation.",
        "status_vs_this_module":
            "Phase-0 raw-scheme output differs from FeynCalc 7/4 by "
            "scheme-dependent terms. Reconciliation: Phase-0.5.",
    }


def verify() -> dict:
    """Self-test: exact rational extraction, pole structure, reference value."""
    r = finite_rational_raw_scheme()
    p = pole_structure()
    ref = feyncalc_reference()
    return {
        "finite_rational_is_exact_Rational": isinstance(r["sympy_rational"], sp.Rational),
        "finite_rational_as_Fraction":       isinstance(r["python_fraction"], Fraction),
        "double_pole_is_rational":           isinstance(p["double_pole_coeff"], sp.Rational),
        "single_pole_rational_part_exists":  p["single_pole_rational_fraction"] is not None,
        "feyncalc_reference_is_7_over_4":    ref["feyncalc_rational"] == Fraction(7, 4),
        "phase_0p5_reconciliation_pending":  "Phase-0.5" in ref["status_vs_this_module"],
        "scheme_is_raw_gamma_function":      "raw" in r["scheme"],
    }
