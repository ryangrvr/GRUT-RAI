"""
STEP 01b — Honest audit of field-count choice

The Step 01 result (R = 1.155) looks extraordinary — it matches the
target R_hand and epsilon_combined almost exactly. But GRUT's V7 docs
and our earlier anomaly_derived.py give R = 1.027 from the same
Birrell-Davies formulae. Where does the difference come from?

Answer: field-count conventions and which sectors are included.

This script enumerates the field counts carefully and identifies exactly
which convention gives which R value.

CRITICAL: this is the step where I must not fool myself. The 1.155
result could be correct, or it could be the result of accidentally
picking field counts that match the target. Honesty requires settling
this before declaring anything.
"""

from fractions import Fraction

# Per-species coefficients (Birrell-Davies / Duff, verified in Step 01)
a_S = Fraction(1, 120)    # real scalar
a_F = Fraction(6, 120)    # Dirac
a_V = Fraction(12, 120)   # gauge boson

b_S = Fraction(1, 360)
b_F = Fraction(11, 360)
b_V = Fraction(31, 180)

# =============================================================================
# Convention A: "standard SM particle count"
# =============================================================================
# gauge bosons: 8 gluons + 3 W/Z + 1 photon = 12
# fermions: 6 quark flavors x 3 colors + 3 leptons + 3 neutrinos = 18+3+3 = 24 Dirac
# scalars: Higgs doublet = 4 real
n_V_A = 12
n_F_A = 24
n_S_A = 4

a_A = n_S_A * a_S + n_F_A * a_F + n_V_A * a_V
b_A = n_S_A * b_S + n_F_A * b_F + n_V_A * b_V
R_A = b_A / a_A

# =============================================================================
# Convention B: Duff 1994 "SM a-anomaly"
# =============================================================================
# Counts with the conformal anomaly literature convention, where sometimes
# neutrinos are not counted (2 lepton species per generation x 3 = 6 Dirac)
# instead of 3+3=6. Let's try the common "no right-handed neutrinos" count:
# fermions: 18 quarks (6 flavors x 3 colors) + 6 charged leptons + 3 neutrinos
#         = 24 Dirac-equivalent  (same as A actually)
# but SOME conventions count neutrinos as 1.5 Dirac (= 3 Weyl)
n_V_B = 12
n_F_B = Fraction(45, 2)   # 45 Weyl = 22.5 Dirac (with single-chirality neutrinos)
n_S_B = 4

a_B = n_S_B * a_S + n_F_B * a_F + n_V_B * a_V
b_B = n_S_B * b_S + n_F_B * b_F + n_V_B * b_V
R_B = b_B / a_B

# =============================================================================
# Convention C: GRUT anomaly_derived.py convention
# =============================================================================
# Let's see what counts produce a = 283/120, b = 3487/1440 exactly.
#
# a = n_S * 1/120 + n_F * 6/120 + n_V * 12/120 = 283/120
# => n_S + 6 n_F + 12 n_V = 283
#
# b = n_S * 1/360 + n_F * 11/360 + n_V * 62/360 = 3487/1440
# => n_S + 11 n_F + 62 n_V = 3487/4 = 871.75
#
# Second equation has 3487/4 — that's not an integer, so either the
# formula or the target uses a different normalization.
# Let's try:  b/360 sums with b_V = 31/180 = 62/360:  yes.
# So n_S + 11 n_F + 62 n_V = 3487/(1440/360) = 3487/4. Non-integer.
#
# That means a = 283/120, b = 3487/1440 cannot both come from
# the simple Birrell-Davies sum with integer field counts using these
# per-species values. Something else is going on.

print("=" * 68)
print("STEP 01b — Field-count audit")
print("=" * 68)
print()
print("Per-species (DERIVED from Birrell-Davies heat kernel):")
print(f"  a_S = 1/120, a_F = 6/120 = 1/20, a_V = 12/120 = 1/10")
print(f"  b_S = 1/360, b_F = 11/360, b_V = 31/180 = 62/360")
print()
print(f"Convention A (n_S=4, n_F=24, n_V=12):")
print(f"  a = {a_A} = {float(a_A):.6f}")
print(f"  b = {b_A} = {float(b_A):.6f}")
print(f"  R = b/a = {R_A} = {float(R_A):.6f}")
print()
print(f"Convention B (n_F = 45/2 for single-chirality neutrino count):")
print(f"  a = {a_B} = {float(a_B):.6f}")
print(f"  b = {b_B} = {float(b_B):.6f}")
print(f"  R = b/a = {R_B} = {float(R_B):.6f}")
print()

# Target: a = 283/120, b = 3487/1440
a_tgt = Fraction(283, 120)
b_tgt = Fraction(3487, 1440)
R_tgt = b_tgt / a_tgt

print(f"GRUT V7 cited target:")
print(f"  a = 283/120 = {float(a_tgt):.6f}")
print(f"  b = 3487/1440 = {float(b_tgt):.6f}")
print(f"  R = {R_tgt} = {float(R_tgt):.6f}")
print()

# Try solving for integer field counts that match a = 283/120:
# n_S + 6 n_F + 12 n_V = 283
# with SM-reasonable values (n_V in [1,12], n_F in [1,24], n_S in [1,4]):

print("Searching for (n_S, n_F, n_V) satisfying a = 283/120 exactly:")
found_a = []
for n_V in range(0, 30):
    for n_F in range(0, 50):
        for n_S in range(0, 10):
            if n_S + 6*n_F + 12*n_V == 283:
                a_val = Fraction(n_S, 120) + Fraction(n_F*6, 120) + Fraction(n_V*12, 120)
                b_val = Fraction(n_S, 360) + Fraction(n_F*11, 360) + Fraction(n_V*62, 360)
                R_val = float(b_val / a_val)
                found_a.append((n_S, n_F, n_V, b_val, R_val))

# Filter for SM-plausible field counts
print(f"  Found {len(found_a)} integer solutions. Showing those with n_V in [6,14]:")
for sol in found_a:
    n_S, n_F, n_V, b_val, R_val = sol
    if 6 <= n_V <= 14:
        match_b = "YES" if b_val == b_tgt else "NO"
        print(f"    n_S={n_S}, n_F={n_F}, n_V={n_V}: "
              f"b = {b_val} ({float(b_val):.4f}), R = {R_val:.6f}, matches b? {match_b}")

print()
print("=" * 68)
print("Interpretation")
print("=" * 68)
print(f"""
Convention A (n_S=4, n_F=24, n_V=12) gives R = {float(R_A):.4f}.
This matches the target ratio 1.155 nearly exactly.

GRUT V7 cites R = 283/120 / (3487/1440) = {float(R_tgt):.4f}, which
is the widely-quoted 'Birrell-Davies free-field R' of 1.027.

The difference comes from the field-count convention. Let's check
which one the standard SM literature uses.

If R = 1.155 comes from the STANDARD SM FIELD COUNT (all SM particles,
Dirac fermions), then the free-field R is 1.155 — and we never had a
12.5% gap. The entire 'gap' narrative was based on the wrong convention.

If R = 1.027 is the correct free-field value and R = 1.155 is what I
just computed only because I used a non-standard field count, then
Step 01 has not yet succeeded — it produced a result that matches the
target by accident.

To settle this I need to check the GRUT V7 derivation of a = 283/120
and b = 3487/1440 to see which field counts it uses.
""")
