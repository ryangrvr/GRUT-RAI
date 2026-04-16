"""
Gravitational Anomaly Coefficients — Derived from Published Physics

This module computes the trace anomaly coefficients from first principles
using ESTABLISHED, PUBLISHED 1-loop results for the Standard Model field
content. Every coefficient traces to a specific reference.

STATUS: 1-LOOP APPROXIMATION
The 1-loop coefficients are exact and published (Birrell-Davies 1982,
Duff 1977, Christensen-Duff 1978). Higher-loop corrections (2-loop, 3-loop)
are NOT included and would require professional-level QFT calculation.

The ratio R_1loop computed here is an honest starting point. The gap between
R_1loop and the value needed for GRUT's cosmological predictions (~1.15) is
what higher-loop corrections would need to close. Whether they DO close it
is an open question for a trained theorist.

REFERENCES:
[1] Birrell & Davies, "Quantum Fields in Curved Space", CUP 1982, Table 6.1
[2] Duff, "Observations on conformal anomalies", Nucl.Phys.B125 (1977) 334
[3] Christensen & Duff, "New gravitational index theorems", Nucl.Phys.B154 (1979) 301
[4] Duff, "Twenty years of the Weyl anomaly", Class.Quant.Grav.11 (1994) 1387
"""

from fractions import Fraction
import math

# ═══════════════════════════════════════════════════════
# 1-LOOP COEFFICIENTS (exact fractions, published)
# ═══════════════════════════════════════════════════════
#
# The trace anomaly in 4D:
#   <T^mu_mu> = (1/16pi^2) [ a F + b G + c Box R ]
#
# F = Weyl tensor squared (C_munurhosigma C^munurhosigma)
# G = Euler density (Gauss-Bonnet)
# Box R = d'Alembertian of Ricci scalar
#
# Convention: Birrell-Davies Table 6.1

# Per-field 1-loop coefficients: (a, b, c)
COEFF_SCALAR = {
    'a': Fraction(1, 120),    # Weyl^2
    'b': Fraction(-1, 360),   # Euler
    'c': Fraction(1, 180),    # Box R
    'ref': 'Birrell-Davies Table 6.1: real conformal scalar'
}

COEFF_DIRAC = {
    'a': Fraction(1, 20),     # = 6/120
    'b': Fraction(-11, 720),
    'c': Fraction(-1, 30),    # = -6/180
    'ref': 'Birrell-Davies Table 6.1: Dirac fermion'
}

COEFF_VECTOR = {
    'a': Fraction(1, 10),     # = 12/120
    'b': Fraction(-31, 180),  # = -62/360
    'c': Fraction(-1, 10),    # = -18/180
    'ref': 'Birrell-Davies Table 6.1: vector (gauge) boson'
}


def sm_field_content(neutrino_type="weyl"):
    """Standard Model field content.

    Parameters
    ----------
    neutrino_type : str
        "weyl" (3 left-handed, minimal SM) or "dirac" (3 massive Dirac)

    Returns
    -------
    dict with N_s (real scalars), N_f (Dirac fermion equivalents), N_v (vectors)
    """
    N_s = 4  # Higgs doublet: 4 real components

    N_f_quarks = 6 * 3          # 6 flavors × 3 colors = 18 Dirac
    N_f_charged_leptons = 3     # e, mu, tau = 3 Dirac

    if neutrino_type == "weyl":
        N_f_neutrinos = Fraction(3, 2)  # 3 Weyl = 3/2 Dirac equivalent
    else:
        N_f_neutrinos = 3               # 3 Dirac

    N_f = N_f_quarks + N_f_charged_leptons + N_f_neutrinos

    N_v = 8 + 3 + 1  # 8 gluons + W+,W-,Z + photon = 12

    return {
        'N_s': N_s, 'N_f': N_f, 'N_v': N_v,
        'neutrino_type': neutrino_type,
        'detail': {
            'scalars': '4 (Higgs doublet real components)',
            'quarks': f'{N_f_quarks} (6 flavors x 3 colors)',
            'charged_leptons': f'{N_f_charged_leptons} (e, mu, tau)',
            'neutrinos': f'{N_f_neutrinos} ({neutrino_type})',
            'gluons': 8, 'weak_bosons': 3, 'photon': 1,
        },
    }


def one_loop_coefficients(N_s, N_f, N_v):
    """Sum 1-loop anomaly coefficients over field content.

    Returns exact fractions for a, b, c.
    """
    a = N_s * COEFF_SCALAR['a'] + N_f * COEFF_DIRAC['a'] + N_v * COEFF_VECTOR['a']
    b = N_s * COEFF_SCALAR['b'] + N_f * COEFF_DIRAC['b'] + N_v * COEFF_VECTOR['b']
    c = N_s * COEFF_SCALAR['c'] + N_f * COEFF_DIRAC['c'] + N_v * COEFF_VECTOR['c']
    return {'a': a, 'b': b, 'c': c}


def de_sitter_anomaly(a, b, c):
    """Evaluate the trace anomaly on de Sitter (S^4).

    On de Sitter:
    - Weyl tensor = 0 (conformally flat) → F = 0
    - R = 12H^2 (constant) → Box R = 0
    - G = 24H^4 (Euler density on S^4)

    So: <T^mu_mu>_dS = (b / 16pi^2) × 24H^4

    Returns the effective anomaly coefficient on de Sitter.
    """
    return {
        'F_contribution': 0,          # Weyl = 0 on de Sitter
        'G_contribution': float(b),   # Only Euler survives
        'BoxR_contribution': 0,       # R is constant
        'effective_coefficient': float(b),
        'note': 'On de Sitter, only the Euler density (b) contributes. '
                'Weyl = 0 (conformally flat) and Box R = 0 (R constant).'
    }


def compute_R_one_loop(neutrino_type="weyl"):
    """Compute the anomaly ratio R at 1-loop from SM field content.

    The ratio R = |b_SM / a_SM| is the 1-loop approximation to the
    anomaly ratio that enters the GRUT cosmological formula.

    On de Sitter, only b contributes (Weyl = 0).
    In the graviton propagator, a contributes (Weyl^2 governs spin-2).
    The ratio |b/a| captures the relative strength of the cosmological
    anomaly vs the graviton self-energy anomaly.

    STATUS: 1-LOOP APPROXIMATION. Higher-loop corrections would modify
    both a and b, changing the ratio. The 1-loop result is exact within
    its approximation order.
    """
    sm = sm_field_content(neutrino_type)
    coeffs = one_loop_coefficients(sm['N_s'], sm['N_f'], sm['N_v'])

    a_SM = coeffs['a']
    b_SM = coeffs['b']
    c_SM = coeffs['c']

    R_1loop = abs(Fraction(b_SM, a_SM))

    return {
        'status': '1-LOOP APPROXIMATION (published coefficients)',
        'neutrino_type': neutrino_type,
        'field_content': sm,
        'coefficients': {
            'a_SM': str(a_SM), 'a_SM_float': float(a_SM),
            'b_SM': str(b_SM), 'b_SM_float': float(b_SM),
            'c_SM': str(c_SM), 'c_SM_float': float(c_SM),
        },
        'R_1loop': {
            'exact': str(R_1loop),
            'float': float(R_1loop),
            'formula': '|b_SM / a_SM| (Euler / Weyl ratio)',
        },
        'de_sitter': de_sitter_anomaly(a_SM, b_SM, c_SM),
        'references': [
            'Birrell & Davies, Quantum Fields in Curved Space, CUP 1982, Table 6.1',
            'Duff, Nucl.Phys.B125 (1977) 334',
            'Christensen & Duff, Nucl.Phys.B154 (1979) 301',
        ],
    }


def compare_to_asserted():
    """Compare the honest 1-loop R to the asserted R = 1.15428.

    This is the key diagnostic: how far is the 1-loop result from
    what the framework needs?
    """
    R_ASSERTED = 1.15428

    results = {}
    for nu_type in ["weyl", "dirac"]:
        r = compute_R_one_loop(nu_type)
        R_1 = r['R_1loop']['float']
        gap = R_ASSERTED - R_1
        gap_pct = gap / R_ASSERTED * 100

        # What Omega_Lambda would the 1-loop R give?
        # H_inf = (2 - R) / (S tau_0)
        # With S = 108pi, tau_0 = 41.9 Myr = 1.322e15 s
        S = 108 * math.pi
        tau_0 = 1.322e15  # seconds
        H_0 = 2.269e-18   # Hz (70 km/s/Mpc)

        H_inf_1loop = (2 - R_1) / (S * tau_0)
        OL_1loop = (H_inf_1loop / H_0) ** 2

        H_inf_asserted = (2 - R_ASSERTED) / (S * tau_0)
        OL_asserted = (H_inf_asserted / H_0) ** 2

        results[nu_type] = {
            'R_1loop': R_1,
            'R_asserted': R_ASSERTED,
            'gap': gap,
            'gap_pct': gap_pct,
            'Omega_Lambda_1loop': OL_1loop,
            'Omega_Lambda_asserted': OL_asserted,
            'Omega_Lambda_observed': 0.6889,
            'note': (f'1-loop R = {R_1:.6f} gives Omega_Lambda = {OL_1loop:.4f}. '
                     f'The gap of {gap:.4f} ({gap_pct:.1f}%) is what 2-loop and '
                     f'3-loop corrections would need to close.'),
        }

    return {
        'status': 'COMPARISON: 1-loop (published) vs asserted (unverified)',
        'results': results,
        'conclusion': (
            'The 1-loop R is in the right neighborhood (slightly above 1) but '
            f'~11-13% below the asserted value of {R_ASSERTED}. The question for '
            'a trained theorist: can 2-loop and 3-loop gravitational corrections '
            'shift R from ~1.03 to ~1.15? This is a specific, answerable question '
            'in perturbative quantum gravity.'
        ),
        'for_physicist': {
            'question': 'What are the 2-loop and 3-loop corrections to the ratio '
                        '|b_SM/a_SM| for the gravitational trace anomaly with full '
                        'SM field content?',
            'known': '1-loop: R ~ 1.03 (Weyl neutrinos) or 1.005 (Dirac neutrinos)',
            'needed': 'R ~ 1.15 for the framework to predict Omega_Lambda ~ 0.69',
            'references': [
                'Gorbar & Shapiro, JHEP 0302 (2003) 021 — 2-loop effective action',
                'Codello, DAmico, Zanusso — functional RG for gravity anomalies',
                'Donoghue, "General relativity as an EFT", gr-qc/9512024',
            ],
        },
    }


def full_derived_analysis():
    """Complete analysis: 1-loop calculation + comparison + gap assessment."""
    weyl = compute_R_one_loop("weyl")
    dirac = compute_R_one_loop("dirac")
    comparison = compare_to_asserted()

    return {
        'headline': 'Honest 1-loop anomaly ratio from SM field content',
        'weyl_neutrinos': weyl,
        'dirac_neutrinos': dirac,
        'comparison': comparison,
        'what_survives': {
            'decoherence': 'DERIVED — Lambda_grav = G m^2 S(l/R) / (hbar l) is '
                           'independent of the anomaly ratio. Fully established.',
            'scaling_laws': 'DERIVED — all six signatures follow from the Diosi-AH kernel.',
            'structural_form': 'f(R) = 2-R is determined by CTP boundary conditions '
                               'regardless of the specific R value.',
        },
        'what_depends_on_R': {
            'Omega_Lambda': 'CONDITIONAL — requires R ~ 1.15',
            'eta_B': 'CONDITIONAL — depends on anomaly decomposition',
            'dark_matter': 'CONDITIONAL — couplings depend on C_FINAL',
        },
    }


def verify():
    """Self-test: verify published coefficient relationships."""
    checks = {}

    # Check: for a single real scalar, a/b should be -1/3
    ratio = COEFF_SCALAR['a'] / COEFF_SCALAR['b']
    checks['scalar_a_over_b'] = float(ratio) == float(Fraction(-1, 3))

    # Check: vector a should be 12x scalar a
    checks['vector_12x_scalar'] = COEFF_VECTOR['a'] == 12 * COEFF_SCALAR['a']

    # Check: Dirac a should be 6x scalar a
    checks['dirac_6x_scalar'] = COEFF_DIRAC['a'] == 6 * COEFF_SCALAR['a']

    return checks
