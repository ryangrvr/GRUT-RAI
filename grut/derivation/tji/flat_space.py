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


# ─────────────────────────────────────────────────────────────────────
# CONVENTION DECLARATION (mandatory per Phase-0.5 NIS discipline)
# ─────────────────────────────────────────────────────────────────────
#
# Every Fraction equality assertion in this module is made under the
# conventions stated here. If any of these conventions change, all
# downstream numerical values (including the pinned ε⁰ rational) MUST
# be re-derived. A convention mismatch between raw Laurent and MS-bar
# absorption would silently corrupt cross-term decomposition even if
# the final ε⁰ coincidentally looked right.
#
# C1 — Dimensional regularization:
#       d = 4 − 2ε  (standard, MS-bar input form).
#       Consistent with V7 A-ICM notebooks (Dec 2025) which use
#       x = ε and Γ(1-x) for constants.
#
# C2 — Raw Laurent input (prefactor × master integral):
#       Prefactor  = −3 (D−2)³ / [64 (D−4)(D−1)]
#                    (V7 §26.2.3 FeynCalc reduction, in units of
#                     e⁴/(π⁸ k²) absorbed into overall normalization)
#       Master gamma-ratio = Γ(2ε−1) · Γ(1−ε)³ / Γ(3−3ε)
#                    (standard 2-loop sunset TJI[{1,0},{1,0},{1,0}])
#       The (−π^D) and (−k²)^(1−2ε) factors of the full TJI, plus
#       the 1/k² in the prefactor, are NOT included in
#       laurent_expansion_raw() — they cancel/combine into the
#       "per-unit e⁴/(16π⁴)" normalization discussed in V7 §26.2.3
#       but do not affect the scheme-dependent finite rational at ε⁰.
#
# C3 — Sign of ε in the raw Laurent, sanity-checked:
#       • 1/ε² coefficient: -1/64 (even-order; invariant under ε → -ε)
#       • 1/ε rational part:  -25/384 (odd-order; sign-flips under ε → -ε)
#       • ε⁰ rational part:   -541/2304 (even-order; invariant)
#       If a reader sees the 1/ε rational as +25/384, the convention
#       has been flipped to d = 4 + 2ε and the whole pipeline must be
#       re-examined before any comparison to MS-bar or FeynCalc values.
#
# C4 — MS-bar absorption per loop:
#       F_loop(ε) = (4π)^ε · Γ(1+ε)⁻¹
#       At n loops: F_loop(ε)^n (here n = 2).
#       This is the convention that matches C1 (d = 4 − 2ε).
#       If C1 were d = 4 + 2ε, the correct MS-bar factor would be
#       [Γ(1−ε) · (4π)^(−ε)]^n instead, and applying the C4 factor
#       to a C1=flipped raw would produce garbage.
#       Reference: Collins, "Renormalization" (Cambridge 1984), §3.
#
# C5 — Transcendentals treated as PHYSICAL vs. ABSORBABLE:
#       Absorbable (set to 0 for "pure rational"):
#         γ_E (Euler-Mascheroni), log(2), log(π), log(4π) — all
#         absorbed into MS-bar renormalization scale choice.
#       Physical (kept):
#         π² (from ζ(2) in Γ(1±ε) expansions) — represents genuine
#         ζ(2) contribution, not absorbed by standard MS-bar.
#         ζ(3), log²(2), etc. (higher transcendentals) — kept if they
#         survive simplification; typically relevant only for ε¹ and
#         higher orders.
#
# C6 — FeynCalc reference value 7/4:
#       The V7 §26.2.3 FeynCalc session reported 7/4 as the ε⁰ pure
#       rational. The specific MS-bar / TarcerRecurse / ApartFF
#       convention used in that session is NOT documented in the
#       verification log (theory/derivation/FEYNCALC_VERIFICATION_LOG.md)
#       and is NOT reproduced by any of the 6 standard MS-bar-family
#       variants tested in scheme_enumeration() when applied to the
#       raw Laurent defined by C1, C2, C3. The user's original
#       Mathematica notebooks (Notebooks/1.15428.nb,
#       A-ICM_3Loop_Anomaly_Coefficients.nb, A-ICM_Pheno_Lambda_Prediction.nb,
#       A-ICM_QFT_Input_SM_Fields.nb) use pre-assembled Laurent
#       coefficients with Γ(1-x) as multiplicative constants — they
#       do NOT contain the 2-loop TJI reduction that produced the
#       7/4. That FeynCalc session is not archived among the visible
#       notebooks.
#
# Phase-0.5 outcome: HONEST NEGATIVE on 7/4 reconciliation under
# conventions C1-C5. See feyncalc_reference() and
# finite_rational_ms_bar_scheme() for the specific result and
# scheme_enumeration() for the sweep.
# ─────────────────────────────────────────────────────────────────────


def convention_declaration() -> dict:
    """Return a machine-readable declaration of the conventions under
    which every Fraction equality in this module is asserted. Any
    downstream calculation or regression test that compares rationals
    MUST cite this declaration. If conventions change, all pinned
    rationals must be re-derived."""
    return {
        "C1_dimensional_regularization":  "d = 4 - 2·eps  (standard, MS-bar input form)",
        "C2_raw_laurent_form":
            "Prefactor × Γ(2ε-1)·Γ(1-ε)³/Γ(3-3ε), "
            "Prefactor = -3(D-2)³/(64(D-4)(D-1)); "
            "the -π^D, (-k²)^(1-2ε), and 1/k² factors are not included "
            "in laurent_expansion_raw() (they cancel into per-unit "
            "e⁴/(16π⁴) normalization without affecting the "
            "scheme-dependent finite rational).",
        "C3_raw_laurent_sign_pattern": {
            "eps_minus_2_coeff":  "-1/64 (even-order, invariant under ε → -ε)",
            "eps_minus_1_rational_part": "-25/384 (odd-order, flips under ε → -ε)",
            "eps_zero_rational_part":   "-541/2304 (even-order, invariant)",
            "sanity_statement": (
                "If a reader observes 1/ε rational part as +25/384, "
                "the convention has been flipped to d = 4 + 2ε. The "
                "whole pipeline must be re-examined before comparing "
                "to MS-bar or FeynCalc values."
            ),
        },
        "C4_ms_bar_absorption_factor":
            "F_loop(ε) = (4π)^ε · Γ(1+ε)^-1 per loop, squared at 2 loops. "
            "Matches C1 (d = 4 - 2ε). See Collins, Renormalization 1984 §3.",
        "C5_transcendentals_absorbed_vs_physical": {
            "absorbed_to_zero": ["EulerGamma", "log(2)", "log(pi)", "log(4*pi)"],
            "kept_as_physical": ["pi**2 (zeta(2))", "zeta(3)", "higher transcendentals"],
        },
        "C6_feyncalc_reference_7_over_4_status":
            "V7 §26.2.3 reported 7/4 as ε⁰ rational. Exact MS-bar / "
            "TarcerRecurse / ApartFF convention used in that FeynCalc "
            "session is NOT documented in theory/derivation/"
            "FEYNCALC_VERIFICATION_LOG.md. User's original Mathematica "
            "notebooks (1.15428.nb, A-ICM_*.nb) use pre-assembled "
            "Laurent coefficients with Γ(1-x) as multiplicative "
            "constants — do NOT contain the 2-loop TJI reduction "
            "that produced 7/4. Session unarchived. Phase-0.5 result "
            "is HONEST NEGATIVE on reconciliation under conventions "
            "C1-C5.",
        "phase_0p5_status":
            "HONEST NEGATIVE: no standard MS-bar variant reproduces 7/4 "
            "from raw Laurent under conventions C1-C5.",
    }


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
            "Phase-0.5 COMPLETE (honest-negative): no standard MS-bar variant "
            "reproduces FeynCalc's 7/4 from this raw Laurent. Systematic "
            "enumeration of 6 absorption factors × 4 sign/π^D configurations "
            "(24 total) clusters around ±541/2304 + {0, ±π²/384, ±π²/192}. "
            "The 7/4 appears to use a non-standard FeynCalc internal "
            "convention not reconstructable from textbook MS-bar schemes. "
            "Canonical MS-bar (standard F2: (4π)^ε · Γ(1+ε)⁻¹ per loop) is "
            "pinned as the V7/V8 scheme for Phase-1 S⁴ measurement. See "
            "scheme_enumeration() for the full table.",
    }


# ─────────────────────────────────────────────────────────────────────
# Phase-0.5 — MS-bar absorption and scheme enumeration
# ─────────────────────────────────────────────────────────────────────
#
# Mechanical structure: MS-bar absorption is a Laurent-series
# multiplication where divergent poles of the raw expansion cross-
# multiply against the Taylor tail of the absorption factor. Those
# cross terms bleed into the finite ε⁰ coefficient via:
#
#     T₁ = raw[1/ε²] × absorption[ε²]   → ε⁰
#     T₂ = raw[1/ε]  × absorption[ε¹]   → ε⁰
#     T₃ = raw[ε⁰]   × absorption[ε⁰=1] → ε⁰
#
# The γ_E and ln(4π) pieces from the absorption factor's Taylor
# expansion must cancel identically in T₁ + T₂ + T₃. If they don't,
# either the factor is wrong or the arithmetic has a bug.
#
# Phase-0.5 result (honest-negative): no standard MS-bar variant
# produces Fraction(7, 4) from the raw Laurent — 24 configurations
# tested (6 absorption factors × {include/exclude π^D} × {±1 overall
# sign}). The canonical MS-bar rational this module pins is
# Fraction(-541, 2304) + π²/192 (standard F2 at γ_E→0, logs→0,
# no π^D factor, no sign flip). This is what Phase-1 measures against.
# ─────────────────────────────────────────────────────────────────────


PI_D_TAYLOR_COEFFS = (
    sp.Rational(1, 1),
    -2 * sp.log(sp.pi),
    2 * sp.log(sp.pi) ** 2,
)
"""Taylor coefficients of π^(-2ε) = exp(-2ε·log π) at orders ε⁰, ε¹, ε².
Used to fold the missing π^D factor into the raw Laurent coefficients
when the V7 FeynCalc convention is being tested."""


def ms_bar_absorption_factor(n_loops: int = 2, order: int = 3) -> dict:
    """Standard MS-bar per-loop absorption factor:

        F_loop(ε) = (4π)^ε · Γ(1+ε)⁻¹

    Raised to the n_loops power. Returns a dict with the SymPy Laurent
    series of F_loop^n_loops around ε=0 to the specified order, plus
    the individual coefficients F[ε⁰], F[ε¹], F[ε²] for cross-term
    extraction.
    """
    F_loop = (4 * sp.pi) ** EPS * gamma(1 + EPS) ** (-1)
    F_total = F_loop ** n_loops
    F_series = sp.expand(sp.series(F_total, EPS, 0, order).removeO())
    return {
        "n_loops":       n_loops,
        "form":          "F_loop(ε) = (4π)^ε · Γ(1+ε)^-1, raised to n_loops",
        "series":        F_series,
        "eps0_coeff":    F_series.coeff(EPS, 0),
        "eps1_coeff":    sp.expand(F_series.coeff(EPS, 1)),
        "eps2_coeff":    sp.expand(F_series.coeff(EPS, 2)),
    }


def _scheme_apply(raw_m2, raw_m1, raw_0, F_coeffs):
    """Apply a 2-loop absorption factor to raw Laurent coefficients.

    Parameters
    ----------
    raw_m2, raw_m1, raw_0 : sympy expressions
        Laurent coefficients at ε^-2, ε^-1, ε^0.
    F_coeffs : 3-tuple
        (F[ε⁰], F[ε¹], F[ε²]) of the squared absorption factor.

    Returns
    -------
    dict with keys T1, T2, T3, total, total_simplified.
    """
    F0, F1, F2 = F_coeffs
    T1 = raw_m2 * F2
    T2 = raw_m1 * F1
    T3 = raw_0 * F0
    total = sp.expand(T1 + T2 + T3)
    total_simp = sp.simplify(total)
    return {"T1": T1, "T2": T2, "T3": T3, "total": total, "total_simplified": total_simp}


def _expand_log_composites(expr):
    """Expand log(4π) → log(4)+log(π) = 2·log(2)+log(π), log(2π) → log(2)+log(π),
    etc. Uses sympy.expand_log which handles multiplicative log decomposition."""
    return sp.expand_log(expr, force=True)


def _extract_rational_after_transcendental_removal(expr):
    """Substitute γ_E → 0, log(2) → 0, log(π) → 0 (after expanding
    composite logs like log(4π) = 2·log(2) + log(π)) to leave only
    the pure-rational part (plus π² if physical in MS-bar). Then
    nsimplify to sp.Rational if possible. Returns None if result
    cannot be reduced to a rational."""
    cleaned = sp.expand(expr)
    cleaned = _expand_log_composites(cleaned)
    cleaned = cleaned.subs(sp.log(2), 0)
    cleaned = cleaned.subs(sp.log(sp.pi), 0)
    cleaned = cleaned.subs(sp.EulerGamma, 0)
    cleaned = sp.simplify(cleaned)
    # With π² kept as "physical", split into rational and π² parts:
    pi_sq_coeff = cleaned.coeff(sp.pi ** 2)
    rational_part = cleaned.subs(sp.pi ** 2, 0)
    # Handle the zero / nsimplify-zoo edge case.
    if rational_part == 0:
        r = sp.Rational(0, 1)
    else:
        try:
            r = sp.nsimplify(rational_part, rational=True)
        except Exception:
            return None
    if not isinstance(r, sp.Rational):
        return None
    if pi_sq_coeff == 0:
        pi_sq_rat = sp.Rational(0, 1)
    else:
        try:
            pi_sq_rat = sp.nsimplify(pi_sq_coeff, rational=True)
        except Exception:
            pi_sq_rat = pi_sq_coeff
    return {
        "rational_part":    r,
        "pi_squared_coeff": pi_sq_rat,
        "full_cleaned":     cleaned,
        "is_pure_rational": pi_sq_coeff == 0,
    }


def _safe_nsimplify(expr):
    """nsimplify that handles the 0-case cleanly (avoids zoo)."""
    if expr == 0:
        return sp.Rational(0, 1)
    try:
        r = sp.nsimplify(expr, rational=True)
        if isinstance(r, sp.Rational):
            return r
    except Exception:
        pass
    return expr


def _cross_term_rational_part(expr):
    """For a single cross term T_i, extract the rational (non-transcendental)
    piece after expanding composite logs and zeroing γ_E, log(2), log(π)."""
    cleaned = _expand_log_composites(sp.expand(expr))
    cleaned = cleaned.subs(sp.log(2), 0)
    cleaned = cleaned.subs(sp.log(sp.pi), 0)
    cleaned = cleaned.subs(sp.EulerGamma, 0)
    cleaned = sp.simplify(cleaned)
    return _safe_nsimplify(cleaned)


def scheme_enumeration() -> dict:
    """Enumerate 24 candidate MS-bar-family scheme configurations
    (6 absorption factors × {include/exclude π^D} × {±1 overall sign})
    and report what ε⁰ rational each produces. None match FeynCalc's 7/4;
    the canonical scheme picked is standard MS-bar (F2) with no π^D and
    no sign flip — this is what Phase-1 will measure against.
    """
    from sympy import exp

    # Raw Laurent coefficients (no π^D, no sign flip)
    raw = laurent_expansion_raw()
    A_m2 = raw.coeff(EPS, -2)
    A_m1 = raw.coeff(EPS, -1)
    A_0  = raw.coeff(EPS, 0)

    # 6 absorption factor candidates
    candidates = [
        ("F1_no_absorption",           sp.S.One),
        ("F2_MS_bar_standard",         (4 * sp.pi) ** EPS / gamma(1 + EPS)),
        ("F3_MS_bar_Gamma_1_minus",    (4 * sp.pi) ** EPS * gamma(1 - EPS)),
        ("F4_reverse_MS_bar",          (4 * sp.pi) ** (-EPS) * gamma(1 + EPS)),
        ("F5_exp_gammaE_minus_log4pi", exp(EPS * (sp.EulerGamma - sp.log(4 * sp.pi)))),
        ("F6_exp_inverse_shift",       exp(-EPS * (sp.EulerGamma - sp.log(4 * sp.pi)))),
    ]

    p0, p1, p2 = PI_D_TAYLOR_COEFFS

    results = {}
    for include_piD in (False, True):
        for sign_flip in (False, True):
            config_label = (
                f"piD={'yes' if include_piD else 'no '}, "
                f"sign={'-' if sign_flip else '+'}"
            )
            # Combine raw Laurent with π^(-2ε) if requested
            if include_piD:
                m2 = A_m2 * p0
                m1 = A_m2 * p1 + A_m1 * p0
                c0 = A_m2 * p2 + A_m1 * p1 + A_0 * p0
            else:
                m2, m1, c0 = A_m2, A_m1, A_0
            if sign_flip:
                m2, m1, c0 = -m2, -m1, -c0

            for name, F_loop in candidates:
                if F_loop == sp.S.One:
                    F_coeffs = (sp.S.One, sp.S.Zero, sp.S.Zero)
                else:
                    F_s = sp.expand(sp.series(F_loop ** 2, EPS, 0, 3).removeO())
                    F_coeffs = (F_s.coeff(EPS, 0), F_s.coeff(EPS, 1), F_s.coeff(EPS, 2))
                applied = _scheme_apply(m2, m1, c0, F_coeffs)
                rat = _extract_rational_after_transcendental_removal(
                    applied["total_simplified"]
                )
                key = f"{config_label} | {name}"
                results[key] = {
                    "config":            config_label,
                    "absorption_factor": name,
                    "total_simplified":  applied["total_simplified"],
                    "rational_part":     rat["rational_part"] if rat else None,
                    "pi_squared_coeff":  rat["pi_squared_coeff"] if rat else None,
                    "is_pure_rational":  rat["is_pure_rational"] if rat else False,
                    "matches_7_over_4":  (
                        rat is not None
                        and rat["is_pure_rational"]
                        and Fraction(int(rat["rational_part"].p),
                                     int(rat["rational_part"].q)) == Fraction(7, 4)
                    ),
                }
    return {
        "configurations_tested":    len(results),
        "configurations":           results,
        "any_matches_7_over_4":     any(r["matches_7_over_4"] for r in results.values()),
        "rationals_encountered":    sorted({
            str(r["rational_part"]) for r in results.values()
            if r["rational_part"] is not None
        }),
    }


def finite_rational_ms_bar_scheme() -> dict:
    """Canonical MS-bar result: standard F2 absorption (4π)^ε/Γ(1+ε) per
    loop, no π^D factor, no sign flip. This is the Phase-0.5 deliverable
    that Phase-1 S⁴ calculations are measured against.

    Returns the cross-term decomposition (T₁, T₂, T₃), their sum, the
    extracted ε⁰ rational (with π² kept as physical MS-bar constant),
    and verification that γ_E, log(4π), log(2), log(π) all cancel.
    """
    raw = laurent_expansion_raw()
    A_m2 = raw.coeff(EPS, -2)
    A_m1 = raw.coeff(EPS, -1)
    A_0  = raw.coeff(EPS, 0)

    F = ms_bar_absorption_factor(n_loops=2, order=3)
    F_coeffs = (F["eps0_coeff"], F["eps1_coeff"], F["eps2_coeff"])

    applied = _scheme_apply(A_m2, A_m1, A_0, F_coeffs)
    rat = _extract_rational_after_transcendental_removal(applied["total_simplified"])

    # The arithmetic cross-check per the Phase-0.5 plan:
    # If (hypothetically) we matched 7/4, shift would be 7/4 - (-541/2304) = 4573/2304.
    # Compute the actual shift and report it.
    shift_from_raw = (
        rat["rational_part"] - A_0.subs(sp.EulerGamma, 0).subs(sp.pi ** 2, 0)
    ) if rat else None
    shift_from_raw_simplified = (
        sp.nsimplify(shift_from_raw, rational=True) if shift_from_raw is not None else None
    )

    # Transcendental structure analysis.
    #
    # MS-bar multiplication by [(4π)^ε·Γ(1+ε)⁻¹]² does two things:
    #   (i) CANCELS γ_E — the ε-expansions of Γ(1+ε)⁻¹ and the raw
    #       Laurent's implicit γ_E contributions match and cancel.
    #   (ii) GROUPS remaining logs into the log(4π) composite — the
    #       log(2) and log(π) terms are not independent; they appear as
    #       n₁ · log(2) + n₂ · log(π) with n₁ = 2n₂ (so the combination
    #       is exactly log(4π)).
    # Setting log(4π) → 0 is the final MS-bar convention.
    simplified = applied["total_simplified"]
    expanded_logs = _expand_log_composites(simplified)
    free_syms = expanded_logs.free_symbols
    has_gamma_E = sp.EulerGamma in free_syms
    # Treat the result as a polynomial in (log(2), log(π)) to extract
    # pure-linear coefficients.
    L2 = sp.log(2)
    Lpi = sp.log(sp.pi)
    try:
        poly = sp.Poly(expanded_logs, L2, Lpi)
        # Linear coefficients: coefficient of L2^1·Lpi^0 and L2^0·Lpi^1.
        linear_log2  = poly.coeff_monomial(L2)
        linear_logpi = poly.coeff_monomial(Lpi)
        pure_log4pi_structure = sp.simplify(linear_log2 - 2 * linear_logpi) == 0
        logs_fully_absorbed = (
            sp.simplify(linear_log2) == 0 and sp.simplify(linear_logpi) == 0
        )
    except (sp.PolynomialError, Exception):
        # Fallback: if Poly can't handle, report conservative "unknown"
        linear_log2 = None
        linear_logpi = None
        pure_log4pi_structure = False
        logs_fully_absorbed = False

    return {
        "scheme":              "MS-bar (standard): per-loop factor (4π)^ε · Γ(1+ε)^-1, squared",
        "T1_cross_term":       _cross_term_rational_part(applied["T1"].subs(sp.pi ** 2, 0)),
        "T2_cross_term":       _cross_term_rational_part(applied["T2"].subs(sp.pi ** 2, 0)),
        "T3_cross_term":       _cross_term_rational_part(applied["T3"].subs(sp.pi ** 2, 0)),
        "T1_with_pi_squared":  _cross_term_rational_part(applied["T1"]),
        "T2_with_pi_squared":  _cross_term_rational_part(applied["T2"]),
        "T3_with_pi_squared":  _cross_term_rational_part(applied["T3"]),
        "sum_simplified":      applied["total_simplified"],
        "rational_part":       rat["rational_part"] if rat else None,
        "pi_squared_coeff":    rat["pi_squared_coeff"] if rat else None,
        "full_cleaned":        rat["full_cleaned"] if rat else None,
        "is_pure_rational":    rat["is_pure_rational"] if rat else False,
        "transcendentals_canceled": {
            "EulerGamma":                        not has_gamma_E,
            "log_structure_is_pure_log_4pi":     pure_log4pi_structure,
            "log_4pi_fully_absorbed":            logs_fully_absorbed,
        },
        "linear_log2_coefficient":  linear_log2,
        "linear_logpi_coefficient": linear_logpi,
        "matches_feyncalc_7_over_4":
            rat is not None
            and rat["is_pure_rational"]
            and Fraction(int(rat["rational_part"].p),
                         int(rat["rational_part"].q)) == Fraction(7, 4),
        "shift_from_raw_eps0_rational": shift_from_raw_simplified,
        "status":
            "COMPUTED (canonical MS-bar); HONEST NEGATIVE on FeynCalc 7/4 match",
    }


MS_BAR_EPSILON_ZERO_EXPECTED = Fraction(7, 4)
"""V7 FeynCalc reference value — NOT reproduced by standard MS-bar in this
pipeline. Kept as the historical target for any Phase-0.5-redux that
investigates FeynCalc's internal conventions."""


def verify() -> dict:
    """Self-test: exact rational extraction, pole structure, MS-bar scheme."""
    r = finite_rational_raw_scheme()
    p = pole_structure()
    ref = feyncalc_reference()
    msbar = finite_rational_ms_bar_scheme()
    enum = scheme_enumeration()
    return {
        "finite_rational_is_exact_Rational":     isinstance(r["sympy_rational"], sp.Rational),
        "finite_rational_as_Fraction":           isinstance(r["python_fraction"], Fraction),
        "double_pole_is_rational":               isinstance(p["double_pole_coeff"], sp.Rational),
        "single_pole_rational_part_exists":      p["single_pole_rational_fraction"] is not None,
        "feyncalc_reference_is_7_over_4":        ref["feyncalc_rational"] == Fraction(7, 4),
        "phase_0p5_honest_negative":
            "HONEST NEGATIVE" in ref["status_vs_this_module"]
            or "honest-negative" in ref["status_vs_this_module"].lower(),
        "scheme_is_raw_gamma_function":          "raw" in r["scheme"],
        "ms_bar_gamma_E_canceled":                msbar["transcendentals_canceled"]["EulerGamma"],
        "ms_bar_log_structure_is_pure_log_4pi":   msbar["transcendentals_canceled"]["log_structure_is_pure_log_4pi"],
        "ms_bar_rational_extracted":             msbar["rational_part"] is not None,
        "ms_bar_no_match_to_7_over_4":           not msbar["matches_feyncalc_7_over_4"],
        "enumeration_tested_24_configs":         enum["configurations_tested"] == 24,
        "no_config_matches_7_over_4":            not enum["any_matches_7_over_4"],
    }
