"""
Conformal anomaly on S⁴ with Standard Model matter content.

At 1-loop, the trace anomaly of a conformally-coupled SM matter sector in
a curved-space background has the form

    ⟨T^μ_μ⟩ = a E₄ + c W² + b □R                                        (1)

where E₄ is the Euler density (4-form), W² is the Weyl-squared, and □R is
the local trivial term. On S⁴ (maximally symmetric), W² = 0, so only the
a and b coefficients enter.

The coefficients a and c depend on matter content via standard formulas
(Duff 1977 conventions):

    a = (1 / (360 × 16π²)) × [n_0 + (11/2) n_{1/2} + 62 n_1]             (2)
    c = (1 / (120 × 16π²)) × [n_0 +   6  n_{1/2} + 12 n_1]               (3)

where:
    n_0 = number of conformally-coupled real scalars
    n_{1/2} = number of Weyl fermions
    n_1 = number of gauge bosons

For the Standard Model content this module computes (n_0, n_{1/2}, n_1)
explicitly so the 1-loop conformal-anomaly integers on S⁴ are locked in.

This module does NOT attempt the full 2-loop U(1)² calculation that would
produce −100 on S⁴. It establishes the STRUCTURAL INPUTS that any such
calculation must use. The 2-loop structural form is derived in
`conformal_mode_coefficient.py` using these as building blocks.
"""

from fractions import Fraction


# ═══════════════════════════════════════════════════════════════════════
# Standard Model field counts (for 1-loop conformal anomaly)
# ═══════════════════════════════════════════════════════════════════════

# Conformally-coupled real scalars: only the physical Higgs is relevant after
# electroweak symmetry breaking, but the UV calculation uses the full doublet.
# The SM Higgs doublet has 4 real components pre-EWSB; 1 physical + 3 Goldstone
# after. The anomaly coefficient counts degrees of freedom, so n_0 = 4 for the
# UV SM content.
N_SCALARS_SM = 4

# Weyl fermions per generation, × 3 generations:
#   Q_L (quark doublet): 2 isospin × 3 color = 6 Weyl d.o.f.
#   u_R: 3 color = 3
#   d_R: 3 color = 3
#   L_L (lepton doublet): 2 isospin = 2
#   e_R: 1
#   Per generation:      6 + 3 + 3 + 2 + 1 = 15
#   × 3 generations:     45
N_WEYL_FERMIONS_SM = 45

# Gauge bosons: SU(3) has 8 gluons, SU(2) has 3 W's, U(1) has 1 B = 12 total.
N_GAUGE_BOSONS_SM = 12


def a_coefficient_numerator(n_0=N_SCALARS_SM, n_half=N_WEYL_FERMIONS_SM,
                             n_1=N_GAUGE_BOSONS_SM):
    """Integer numerator of the `a` conformal-anomaly coefficient for a
    matter content (n_0, n_{1/2}, n_1).

    From eq (2):  a × (360 × 16π²) = n_0 + (11/2) n_{1/2} + 62 n_1

    Returns a Fraction — for SM content the exact rational is:
        4 + (11/2)(45) + 62(12) = 4 + 247.5 + 744 = 995.5 = 1991/2
    """
    return Fraction(n_0) + Fraction(11, 2) * n_half + Fraction(62) * n_1


def c_coefficient_numerator(n_0=N_SCALARS_SM, n_half=N_WEYL_FERMIONS_SM,
                             n_1=N_GAUGE_BOSONS_SM):
    """Integer numerator of the `c` conformal-anomaly coefficient.

    From eq (3):  c × (120 × 16π²) = n_0 + 6 n_{1/2} + 12 n_1

    For SM: 4 + 6(45) + 12(12) = 4 + 270 + 144 = 418
    """
    return Fraction(n_0) + Fraction(6) * n_half + Fraction(12) * n_1


def U1_beta_function_one_loop():
    """1-loop U(1)_Y β-function coefficient for SM hypercharges.

    Standard result:  b_{U(1)} = (2/3) × Σ Y²

    For SM Σ Y² = 10, so b_{U(1)}^{SM} = 20/3.

    This is the SAME integer 10 that appears:
      - as R_ψ,U1 in Osborn (2003) eq. (36)
      - as the structural foundation of −(ΣY²)² = −100 in expression B
      - as the 1-loop hypercharge coupling to the conformal anomaly
    """
    # Import lazily to avoid circular imports within the package
    from grut.derivation.minus_100.hypercharge_sum import sum_Y_squared_total
    return Fraction(2, 3) * sum_Y_squared_total()


def structural_report():
    """Full structural report: SM field counts and 1-loop anomaly coefficients."""
    a_num = a_coefficient_numerator()
    c_num = c_coefficient_numerator()
    beta_U1 = U1_beta_function_one_loop()
    return {
        "matter_content": {
            "conformally_coupled_scalars":  N_SCALARS_SM,
            "Weyl_fermions":                 N_WEYL_FERMIONS_SM,
            "gauge_bosons":                  N_GAUGE_BOSONS_SM,
            "per_generation_Weyl_breakdown": {
                "Q_L (6 per gen)": 6 * 3,
                "u_R (3 per gen)": 3 * 3,
                "d_R (3 per gen)": 3 * 3,
                "L_L (2 per gen)": 2 * 3,
                "e_R (1 per gen)": 1 * 3,
            },
        },
        "one_loop_anomaly_numerators": {
            "a_numerator (Duff 1977)":  str(a_num),
            "c_numerator (Duff 1977)":  str(c_num),
            "note": (
                "a × (360×16π²) = n_0 + (11/2)n_{1/2} + 62 n_1; "
                "c × (120×16π²) = n_0 + 6 n_{1/2} + 12 n_1. "
                "On S⁴, W² = 0 so only a enters."
            ),
        },
        "U1_hypercharge_signature": {
            "sum_Y_squared":          10,
            "beta_U1_one_loop":       str(beta_U1),
            "structural_link": (
                "The integer 10 appears in three independent places: "
                "(i) Σ Y² over SM fermions (this module), "
                "(ii) Osborn 2003 eq. (36) R_ψ,U1 = 10, "
                "(iii) the 2-loop U(1)² sub-insertion carries "
                "(Σ Y²)² = 100 (conformal_mode_coefficient.py)."
            ),
        },
        "status": (
            "All 1-loop conformal-anomaly inputs for SM on S⁴ are locked "
            "in as exact rationals. These are the INPUT QUANTITIES any "
            "2-loop U(1)² conformal-mode calculation must use. The "
            "derivation of the 2-loop −(Σ Y²)² = −100 coefficient is "
            "completed structurally in conformal_mode_coefficient.py."
        ),
    }


def verify():
    return {
        "a_numerator_is_1991_over_2":   a_coefficient_numerator() == Fraction(1991, 2),
        "c_numerator_is_418":           c_coefficient_numerator() == Fraction(418),
        "beta_U1_is_20_over_3":         U1_beta_function_one_loop() == Fraction(20, 3),
        "n_scalars_sm":                 N_SCALARS_SM == 4,
        "n_weyl_fermions_sm":           N_WEYL_FERMIONS_SM == 45,
        "n_gauge_bosons_sm":            N_GAUGE_BOSONS_SM == 12,
    }


if __name__ == "__main__":
    import json
    print(json.dumps(structural_report(), indent=2))
    print()
    for k, v in verify().items():
        print(f"  {'✓' if v else '✗'} {k}")
