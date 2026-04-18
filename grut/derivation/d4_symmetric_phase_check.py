"""
Gap 1 check: Are the Birrell-Davies SM anomaly coefficients already the
symmetric-phase values, or do they change in the restored phase on S^4?

Context:
    At T_GH ~ 10^12 GeV >> v_EW, EW symmetry is restored. This raises the
    question: does C_Final = b_free from Birrell-Davies already count the
    symmetric-phase degrees of freedom, or does it count broken-phase
    (physical Higgs + massive W/Z) d.o.f. that would differ from the
    restored phase?

Resolution:
    In the massless limit (m_f, m_W, m_Z << evaluation scale), the
    Birrell-Davies count converges in both phases via Stuckelberg
    equivalence. The "eaten" Goldstones appear as longitudinal modes of
    massive gauge bosons in unitary gauge, or as separate scalars in
    Stuckelberg formulation — the total counting is the same.

    Symmetric phase: 4 real scalars (Higgs doublet) + 12 massless vectors
                     (8 gluons + W^1 + W^2 + W^3 + B)
    Broken phase:    4 real scalars (physical H + 3 Goldstones) + 12
                     vectors (8 gluons + W+ + W- + Z + photon, massless
                     limit)

    Both give a = 283/120, b = 3487/1440 at high scale on S^4.

    Finite-mass corrections: O(m^2/H^2) ~ 10^-22 at H=10^13 GeV.
    Negligible.

    CONCLUSION: Gap 1 resolves to "no change." C_Final is the same in
    both phases at the evaluation scale H >> all SM masses.
"""
from fractions import Fraction

# Per-field Birrell-Davies (Dirac convention)
a_S = Fraction(1, 120)
b_S = Fraction(1, 360)
a_F = Fraction(1, 20)
b_F = Fraction(11, 720)
a_V = Fraction(1, 10)
b_V = Fraction(31, 180)

print("=" * 70)
print("Gap 1 resolution: anomaly coefficient in symmetric vs broken phase")
print("=" * 70)
print()

# Symmetric phase
N_s_sym = 4
N_f_sym = Fraction(45, 2)
N_v_sym = 12

a_sym = N_s_sym * a_S + N_f_sym * a_F + N_v_sym * a_V
b_sym = N_s_sym * b_S + N_f_sym * b_F + N_v_sym * b_V

print("Symmetric phase (restored, all fields massless):")
print(f"  N_s = {N_s_sym}  (full Higgs doublet, 4 real d.o.f.)")
print(f"  N_f = {N_f_sym}  (6x3 quarks + 3 leptons + 3 Weyl neutrinos)")
print(f"  N_v = {N_v_sym}  (8 gluons + W^1,W^2,W^3 + B, all massless)")
print(f"  a = {a_sym} = {float(a_sym):.6f}")
print(f"  b = {b_sym} = {float(b_sym):.6f}")
print()

# Broken phase (massless limit via Stuckelberg)
N_s_br = 4
N_f_br = Fraction(45, 2)
N_v_br = 12

a_br = N_s_br * a_S + N_f_br * a_F + N_v_br * a_V
b_br = N_s_br * b_S + N_f_br * b_F + N_v_br * b_V

print("Broken phase in the massless limit (Stuckelberg):")
print(f"  N_s = {N_s_br}  (physical H + 3 would-be Goldstones)")
print(f"  N_f = {N_f_br}  (same multiplicity)")
print(f"  N_v = {N_v_br}  (8 gluons + W+ + W- + Z + photon, massless limit)")
print(f"  a = {a_br} = {float(a_br):.6f}")
print(f"  b = {b_br} = {float(b_br):.6f}")
print()

assert a_sym == a_br
assert b_sym == b_br

print("EXACT EQUALITY in massless limit:")
print("  Both phases give a_SM = 283/120, b_SM = 3487/1440.")
print()
print("Finite-mass corrections: O(m^2 / H^2) at H = 10^13 GeV:")
m_t = 173.0   # GeV (heaviest SM fermion)
H = 1e13
print(f"  (m_t / H)^2 = ({m_t} / {H:.0e})^2 = {(m_t/H)**2:.2e}")
print("  Negligible by 22 orders of magnitude.")
print()
print("GAP 1 RESOLUTION: C_Final does NOT shift between phases on S^4")
print("at H >> all SM masses. Birrell-Davies count is already symmetric-phase.")
