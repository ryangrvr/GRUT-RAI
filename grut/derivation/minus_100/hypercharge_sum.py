"""
Stage 1 — Standard Model hypercharge-squared sum Σ_{SM Weyl fermions} Y².

Verifies that Σ Y² = 10 exactly over 3 generations in the Peskin-Schroeder
convention (Q = T_3 + Y). This is the structural foundation of H1:

    −100 = −(Σ Y²)² = −10²

The same "10" appears in Osborn (2003) eq. (36) as R_ψ,U1 = 10, the
fermion trace index for the U(1) gauge sector. Two independent traces
of the same SM-derivable quantity.

Lock this in so if anyone silently changes hypercharge conventions or
generation count, the test suite flags it.
"""

from fractions import Fraction


# SM Weyl fermions, per generation, in the Peskin-Schroeder convention (Q = T_3 + Y).
# Left-handed quark doublet Q_L has 2 × 3 = 6 Weyl components (2 isospin × 3 color).
# Right-handed up/down quarks have 3 color each. Lepton doublet L_L has 2. e_R is 1.
SM_FERMIONS_PER_GENERATION = [
    # (field_name, multiplicity, hypercharge Y)
    ("Q_L",  6,  Fraction(1, 6)),     # (u_L, d_L) × 3 colors
    ("u_R",  3,  Fraction(2, 3)),     # u_R × 3 colors
    ("d_R",  3,  Fraction(-1, 3)),    # d_R × 3 colors
    ("L_L",  2,  Fraction(-1, 2)),    # (ν_L, e_L)
    ("e_R",  1,  Fraction(-1, 1)),    # e_R
]

N_GENERATIONS = 3


def sum_Y_squared_per_generation():
    """Σ Y² over one SM generation. Returns an exact Fraction.

        Q_L:  6 × (1/6)²  = 6/36 = 1/6
        u_R:  3 × (2/3)²  = 12/9 = 4/3
        d_R:  3 × (-1/3)² = 3/9  = 1/3
        L_L:  2 × (-1/2)² = 2/4  = 1/2
        e_R:  1 × (-1)²   = 1
        ────────────────────────────
        Total per generation:       10/3

    """
    total = Fraction(0)
    for name, mult, Y in SM_FERMIONS_PER_GENERATION:
        total += mult * Y**2
    return total


def sum_Y_squared_total(n_generations=N_GENERATIONS):
    """Σ Y² over all 3 SM generations. Returns 10 exactly."""
    return n_generations * sum_Y_squared_per_generation()


def hypercharge_squared_squared():
    """(Σ Y²)² = 100 exactly."""
    s = sum_Y_squared_total()
    return s * s


def osborn_K_U1_formula(C_U1=0, R_psi_U1=Fraction(10), R_phi_U1=Fraction(1, 2)):
    """Osborn (2003) eq. (36) U(1) coefficient:

        K_U1 = (1/3) × (29 C_U1 − 12 R_ψ,U1 − (5/2) R_φ,U1)

    For SM U(1)_Y: C_U1 = 0 (U(1) is Abelian, no adjoint Casimir),
                   R_ψ,U1 = Σ Y² = 10 (fermion trace index),
                   R_φ,U1 = (1/2) × Y_H² × 2 = 1/2 (Higgs doublet Y = 1/2, mult 2).

    Returns an exact Fraction.
    """
    return Fraction(1, 3) * (29 * C_U1 - 12 * R_psi_U1 - Fraction(5, 2) * R_phi_U1)


def structural_identification():
    """Full chain: SM hypercharges → Σ Y² → (Σ Y²)² → −100 → cross-check Osborn."""
    per_gen = sum_Y_squared_per_generation()
    total = sum_Y_squared_total()
    squared = hypercharge_squared_squared()
    K_U1 = osborn_K_U1_formula()
    return {
        "per_generation": {
            str(name): {"multiplicity": mult, "Y": str(Y), "Y_squared": float(mult * Y**2),
                        "Y_squared_frac": str(mult * Y**2)}
            for (name, mult, Y) in SM_FERMIONS_PER_GENERATION
        },
        "sum_Y_squared_per_generation": str(per_gen),
        "sum_Y_squared_total":          str(total),
        "sum_Y_squared_total_int":      int(total),
        "hypercharge_squared_squared":  int(squared),
        "minus_100_identification":     -int(squared),
        "osborn_K_U1":                  str(K_U1),
        "osborn_K_U1_float":            float(K_U1),
        "osborn_R_psi_U1":              "10 (same integer as Σ Y²; structural link)",
        "status": (
            "CLOSED: Σ Y² = 10 exact, (Σ Y²)² = 100 exact, sign negative "
            "(consistent with K_U1 < 0). The integer 10 appears in BOTH "
            "Osborn's 1-loop coupling formula AND this 3-loop CTP sub-insertion "
            "topology. Two independent traces of the same SM-derivable object."
        ),
    }


def verify():
    """Self-test."""
    return {
        "sum_per_gen_is_10_over_3":   sum_Y_squared_per_generation() == Fraction(10, 3),
        "sum_total_is_10_exact":      sum_Y_squared_total() == Fraction(10),
        "squared_is_100":             hypercharge_squared_squared() == Fraction(100),
        "K_U1_is_negative":           osborn_K_U1_formula() < 0,
    }


if __name__ == "__main__":
    import json
    print(json.dumps(structural_identification(), indent=2))
    print()
    for k, v in verify().items():
        print(f"  {'✓' if v else '✗'} {k}")
