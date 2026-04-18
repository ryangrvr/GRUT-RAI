"""
STEP 01 — Heat kernel on S^4 and free-field |b/a|  [CORRECTED]

See STEP_01_HONEST_LOG.md for the story of this correction. An earlier
version used b_F = 11/360 (Weyl convention) with Dirac field counts,
producing R = 1.155 — a spurious match to the target. The correct
Dirac convention gives b_F = 11/720, yielding R = 1.027 for SM with
Weyl neutrinos (N_f = 45/2).

Purpose:
    Reproduce the Birrell-Davies 1-loop trace anomaly coefficients for
    Standard Model content, establish the baseline free-field |b/a|
    ratio, and note that the Weyl tensor vanishes on S^4 so only b
    contributes to the bulk anomaly.

Cross-check: grut/foundation/anomaly_derived.py (independent
implementation in the repository).

Status at end of step: DERIVED (exact fractions from published
Birrell-Davies coefficients).
"""

from fractions import Fraction

# =============================================================================
# Per-species Birrell-Davies coefficients (Table 6.1, verified against
# grut/foundation/anomaly_derived.py)
#
# Convention: a = coefficient of F = Weyl^2, b = coefficient of G = Euler
# (magnitudes; overall sign depends on the metric convention and whether
# b is reported as -b or |b|).
# =============================================================================

# Per real conformal scalar
a_S = Fraction(1, 120)
b_S = Fraction(1, 360)

# Per Dirac fermion (= 2 Weyl fermions)
a_F = Fraction(6, 120)       # = 1/20
b_F = Fraction(11, 720)      # CORRECTED: was 11/360 in earlier draft

# Per gauge vector
a_V = Fraction(12, 120)      # = 1/10
b_V = Fraction(31, 180)      # = 62/360

# =============================================================================
# SM field content (matches grut/foundation/anomaly_derived.py)
# =============================================================================

# Standard: 3 Weyl neutrinos (minimal SM)
#   Quarks:       6 flavors × 3 colors = 18 Dirac
#   Chgd leptons:                         3 Dirac
#   Neutrinos:    3 Weyl = 3/2 Dirac equivalent
#   Total:        N_f = 45/2
N_s = 4                     # Higgs doublet: 4 real scalars
N_f_weyl_nu = Fraction(45, 2)
N_v = 12                    # 8 gluons + 3 W/Z + 1 photon

# Alternative: 3 Dirac neutrinos
N_f_dirac_nu = 24

# =============================================================================
# Compute totals and ratios
# =============================================================================

def totals(N_s, N_f, N_v):
    a = N_s * a_S + N_f * a_F + N_v * a_V
    b = N_s * b_S + N_f * b_F + N_v * b_V
    return a, b

a_weyl, b_weyl = totals(N_s, N_f_weyl_nu, N_v)
R_weyl = b_weyl / a_weyl

a_dirac, b_dirac = totals(N_s, N_f_dirac_nu, N_v)
R_dirac = b_dirac / a_dirac

print("=" * 68)
print("STEP 01 — Free-field |b/a| for SM content (corrected)")
print("=" * 68)
print()
print("Per-species coefficients:")
print(f"  a_scalar  = {a_S}      b_scalar  = {b_S}")
print(f"  a_fermion = {a_F}       b_fermion = {b_F}")
print(f"  a_vector  = {a_V}       b_vector  = {b_V}")
print()
print(f"SM with 3 Weyl neutrinos (N_s={N_s}, N_f={N_f_weyl_nu}, N_v={N_v}):")
print(f"  a = {a_weyl} = {float(a_weyl):.6f}")
print(f"  b = {b_weyl} = {float(b_weyl):.6f}")
print(f"  R = b/a = {R_weyl} = {float(R_weyl):.6f}")
print()
print(f"SM with 3 Dirac neutrinos (N_s={N_s}, N_f={N_f_dirac_nu}, N_v={N_v}):")
print(f"  a = {a_dirac} = {float(a_dirac):.6f}")
print(f"  b = {b_dirac} = {float(b_dirac):.6f}")
print(f"  R = b/a = {R_dirac} = {float(R_dirac):.6f}")
print()

# =============================================================================
# Cross-check against grut/foundation/anomaly_derived.py
# =============================================================================

expected_a = Fraction(283, 120)
expected_b = Fraction(3487, 1440)
expected_R = expected_b / expected_a

print("Cross-check against grut/foundation/anomaly_derived.py (Weyl nu):")
match_a = a_weyl == expected_a
match_b = b_weyl == expected_b
print(f"  a: {a_weyl} == 283/120 ? {match_a}")
print(f"  b: {b_weyl} == 3487/1440 ? {match_b}")
print(f"  R: matches? {'YES' if match_a and match_b else 'NO'}")
print()

# =============================================================================
# The S^4 conclusion
# =============================================================================

print("=" * 68)
print("Conclusion of Step 01")
print("=" * 68)
print("""
Free-field baseline: R = b/a = 3487/3396 ≈ 1.0268 (SM, Weyl neutrinos)

Observation for the S^4 derivation: the Weyl tensor vanishes on S^4
(conformally flat). Therefore F = Weyl^2 = 0 on S^4, and the bulk
trace anomaly on S^4 is:

    <T^mu_mu>|_S^4 = b × E_4 + c × Box R

The 'a' coefficient does NOT appear in the S^4 bulk anomaly. Only 'b'
(the Euler-density coefficient) enters — and that coefficient can
receive coupling-dependent corrections per Osborn's local-coupling
framework (to be developed in Steps 02-06).

The free-field ratio |b/a| = 1.0268 is therefore a FLAT-SPACE
Birrell-Davies quantity, not the object GRUT's CTP-on-S^4 formula
computes. That object is the coupling-corrected Euler coefficient,
which Steps 02-06 will show is Osborn's epsilon.

STATUS: DERIVED (exact fractions from Birrell-Davies Table 6.1).
Cross-checked against grut/foundation/anomaly_derived.py: EXACT MATCH.
""")
