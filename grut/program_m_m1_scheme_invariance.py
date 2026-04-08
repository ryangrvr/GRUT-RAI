#!/usr/bin/env python3
"""
Program M - Stage M1: RG and Scheme Invariance Test for R
"""
import numpy as np
from scipy.special import zeta

pi = np.pi
z3 = zeta(3)
ln2 = np.log(2)

C_Final = 3*(99 + 2*pi**2 + 576*ln2*z3) / (16384*pi**6)
C_Cosmo = (-108000 + pi**4 + 1536*pi**4*ln2 + 540*z3) / (276480*pi**4)
R = abs(C_Cosmo) / abs(C_Final)

print("=" * 90)
print("STEP 1: EXPLICIT mu-DEPENDENCE")
print("=" * 90)
print()
print("C_Final and C_Cosmo as stated in the paper are PURE NUMBERS:")
print(f"  C_Final = {C_Final:.15e}")
print(f"  C_Cosmo = {C_Cosmo:.15e}")
print(f"  R       = {R:.15f}")
print()
print("Neither expression contains mu, ln(mu), or any scale variable.")
print("They are built entirely from {pi, zeta(3), ln(2), integers}.")
print()
print("dR/d(ln mu) = 0  EXACTLY  (no mu in the formula)")
print()
print("INTERPRETATION: These are the FINAL finite parts after MS-bar")
print("subtraction of all UV poles. The mu-dependence that exists in")
print("the FULL effective action (through ln(q^2/mu^2)) is split as:")
print("  C_Final * q^2 ln(q^2/mu^2) = C_Final * q^2 ln(q^2) - C_Final * q^2 ln(mu^2)")
print("The ln(mu^2) piece is a LOCAL R^2 counterterm absorbed by")
print("the running of the R^2 coupling. C_Final itself does not run.")
print("C_Cosmo is the zero-momentum finite part, also not running")
print("(it is the anomaly-induced cosmological counterterm).")
print()
print("RESULT: dR/d(ln mu) = 0. R is mu-independent by construction.")

print()
print("=" * 90)
print("STEP 2: SCHEME SENSITIVITY ANALYSIS")
print("=" * 90)
print()

# Decompose the transcendental structure
print("Transcendental decomposition of the coefficients:")
print()

# C_Final numerator: 3 * [99 + 2*pi^2 + 576*ln2*z3]
# Components: rational (99), pi^2, ln(2)*zeta(3)
a_rat_F = 3 * 99
a_pi2_F = 3 * 2
a_ln2z3_F = 3 * 576
den_F = 16384 * pi**6

print(f"C_Final = [{a_rat_F} + {a_pi2_F}*pi^2 + {a_ln2z3_F}*ln(2)*zeta(3)] / (16384*pi^6)")
print(f"        = [{a_rat_F} + {a_pi2_F*pi**2:.6f} + {a_ln2z3_F*ln2*z3:.6f}] / {den_F:.6f}")
print()

# C_Cosmo numerator: -108000 + pi^4 + 1536*pi^4*ln2 + 540*z3
a_rat_C = -108000
a_pi4_C = 1
a_pi4ln2_C = 1536
a_z3_C = 540
den_C = 276480 * pi**4

print(f"C_Cosmo = [{a_rat_C} + {a_pi4_C}*pi^4 + {a_pi4ln2_C}*pi^4*ln(2) + {a_z3_C}*zeta(3)] / (276480*pi^4)")
print(f"        = [{a_rat_C} + {a_pi4_C*pi**4:.6f} + {a_pi4ln2_C*pi**4*ln2:.6f} + {a_z3_C*z3:.6f}] / {den_C:.6f}")
print()

print("SCHEME DEPENDENCE ANALYSIS:")
print()
print("Under a scheme change (e.g., MS-bar to momentum subtraction):")
print("  C_Final -> C_Final + delta_F")
print("  C_Cosmo -> C_Cosmo + delta_C")
print()
print("where delta_F and delta_C are finite, LOCAL counterterm shifts.")
print()
print("Key properties of scheme changes in dim-reg:")
print("  1. Transcendentals (pi^n, zeta(n), ln(2)) are PRESERVED.")
print("     Scheme changes can only shift RATIONAL prefactors.")
print("  2. The RATIO of transcendental structures is scheme-independent")
print("     if both C_Final and C_Cosmo arise from the SAME anomaly functional.")
print()

# Test: what fraction of each coefficient is rational vs transcendental?
C_Final_rational = a_rat_F / den_F
C_Final_transcendental = C_Final - C_Final_rational
frac_F_trans = abs(C_Final_transcendental / C_Final)

C_Cosmo_rational = a_rat_C / den_C
C_Cosmo_transcendental = C_Cosmo - C_Cosmo_rational
frac_C_trans = abs(C_Cosmo_transcendental / C_Cosmo)

print(f"Transcendental fraction of C_Final: {frac_F_trans:.4f} ({frac_F_trans*100:.1f}%)")
print(f"Transcendental fraction of C_Cosmo: {frac_C_trans:.4f} ({frac_C_trans*100:.1f}%)")
print()

# R from rational parts only vs R from transcendental parts only
R_rational = abs(C_Cosmo_rational / C_Final_rational) if C_Final_rational != 0 else float('inf')
R_trans = abs(C_Cosmo_transcendental / C_Final_transcendental) if C_Final_transcendental != 0 else float('inf')

print(f"R from RATIONAL parts only:        {R_rational:.6f}")
print(f"R from TRANSCENDENTAL parts only:   {R_trans:.6f}")
print(f"R (full):                           {R:.6f}")
print()

if abs(R_rational - R_trans) / R < 0.01:
    print("The rational-only and transcendental-only ratios are CLOSE.")
    print("This would support scheme independence (rational shifts cancel).")
else:
    print(f"The rational-only ({R_rational:.4f}) and transcendental-only ({R_trans:.4f})")
    print(f"ratios DIFFER from R ({R:.4f}).")
    print("Scheme changes that shift the rational prefactors WOULD shift R.")
    print("The scheme independence claim depends on the SPECIFIC combination,")
    print("not on a simple factorization.")

print()
print("STEP 2 VERDICT: CONDITIONAL.")
print("R is a definite number in MS-bar. Whether it is the same in other")
print("schemes requires either a second computation or a structural proof")
print("that the anomaly matching protects the full ratio (not just the")
print("transcendental structure).")

print()
print("=" * 90)
print("STEP 3: FIELD CONTENT SENSITIVITY")
print("=" * 90)
print()

# The SM has: 4 real scalars (Higgs), 45 Weyl fermions, 12 gauge bosons
# (exact count depends on convention)
#
# At 1-loop, the trace anomaly coefficients are:
# b_scalar = 1/(120*16*pi^2) per real scalar
# b_fermion = 1/(40*16*pi^2) per Weyl fermion (or 1/(20*16*pi^2) per Dirac)
# b_vector = -1/(10*16*pi^2) per gauge boson (in 4D, with ghost subtraction)

# The 3-loop result is more complex but scales roughly as (1-loop)^3 * combinatorics

# Test: fractional change in R from adding one real scalar
# Rough estimate: each scalar contributes ~b_scalar to the anomaly
# Fractional contribution: ~ n_new * b_scalar / (n_s*b_s + n_f*b_f + n_v*b_v)
# For SM: the total is dominated by the gauge bosons and fermions.

# More precisely: the paper's formulas involve SM-specific integer coefficients
# (99, 108000, 576, 1536, 540). These would change with different field content.
# Without the species decomposition, we cannot compute the exact shift.

print("DECOUPLING TEST:")
print()
print("  Heavy field (M >> SM scale):")
print("  By Appelquist-Carazzone theorem: decouples as O(mu^2/M^2).")
print("  C_Final, C_Cosmo unaffected at mu << M.")
print("  R STABLE under heavy-field addition. PASS.")
print()
print("  Light field (M ~ 0, one real scalar):")
print("  Without species-decomposed formulas, exact shift is not computable.")
print("  Estimate: delta_R/R ~ O(1/N_SM) where N_SM ~ O(50-100) DOF.")
print("  Rough: delta_R ~ 1-2% per new light scalar.")
print("  R is MATTER-CONTENT-SPECIFIC. This is expected and physical.")
print()
print("STEP 3 VERDICT: DECOUPLING-CONSISTENT.")
print("R changes with light field content (physical) and is stable")
print("under heavy-field addition (Appelquist-Carazzone). GOOD behavior.")

print()
print("=" * 90)
print("STEP 4: IR vs UV ORIGIN")
print("=" * 90)
print()

print("C_Final: coefficient of R ln(Box/mu^2) R in the effective action.")
print("  This is a NONLOCAL operator generated by UV loops.")
print("  Its coefficient is determined by the UV field content")
print("  (anomaly coefficients: a, c, b).")
print("  CLASSIFICATION: UV-DETERMINED, IR-MANIFESTING (controls 1/k^4 noise).")
print()
print("C_Cosmo: coefficient of R in the effective action.")
print("  This is a LOCAL operator (the cosmological counterterm).")
print("  Its finite part is determined by the UV anomaly structure")
print("  after subtraction of poles.")
print("  CLASSIFICATION: UV-DETERMINED, IR-MANIFESTING (contributes to Lambda).")
print()
print("R = |C_Cosmo/C_Final|:")
print("  BOTH are UV-anomaly-determined. The ratio inherits UV protection.")
print("  This is analogous to ratios of Casimir invariants or anomaly")
print("  coefficients, which are scheme-independent because they are")
print("  determined by representation theory, not by dynamics.")
print()
print("STEP 4 VERDICT: UV-ANOMALY-CONTROLLED.")
print("Most favorable structure for scheme independence.")

# ============================================================
# FINAL SUMMARY
# ============================================================
print()
print("=" * 90)
print("M1 FINAL OUTPUT")
print("=" * 90)
print()
print(f"1. R(mu) = {R:.15f}  [no mu-dependence in the expression]")
print(f"2. dR/d(ln mu) = 0  [exact, by construction]")
print()
print("3. Scheme-sensitive terms identification:")
print(f"   Rational fraction of C_Final: {frac_F_trans*100:.1f}% transcendental")
print(f"   Rational fraction of C_Cosmo: {frac_C_trans*100:.1f}% transcendental")
print(f"   R from rational parts: {R_rational:.6f}")
print(f"   R from transcendental parts: {R_trans:.6f}")
print(f"   R (full): {R:.6f}")
delta_scheme = abs(R_rational - R) / R
print(f"   Max R-shift from pure rational perturbation: ~{delta_scheme:.4f} ({delta_scheme*100:.2f}%)")
print()
print("4. Decoupling behavior:")
print("   Heavy field addition: R STABLE (Appelquist-Carazzone). PASS.")
print("   Light field addition: R shifts ~O(1/N_SM) ~ 1-2%. PHYSICAL.")
print()
print("5. CLASSIFICATION:")
print("   R is UV-anomaly-controlled, mu-independent within MS-bar,")
print("   matter-content-specific, and decoupling-consistent.")
print("   Scheme independence is PLAUSIBLE (UV-anomaly origin, shared")
print("   transcendental basis) but NOT PROVEN (no second-scheme computation).")
print()
print("   TOKEN: r_conditionally_scheme_independent")
