"""
STEP 02 — Wick rotation and the Euler-density i

Purpose:
    Derive where the Euler-density contribution to the 1-loop effective
    action on S^4 lands in the Lorentzian CTP framework — specifically,
    whether it lives in the real part (dissipation) or the imaginary
    part (decoherence/noise) of the Lorentzian effective action.

Method:
    1. Evaluate integral of E_4 on Euclidean S^4 using Gauss-Bonnet.
    2. Track factors of i and sign conventions explicitly through the
       Wick rotation t_E = -i·t_L.
    3. Identify which piece of the Lorentzian effective action inherits
       the Euler contribution.
    4. Connect to CTP formalism: Gamma_CTP = Re(Gamma_CTP) + i Im(Gamma_CTP).

Inputs (ASSUMED, published):
    - Gauss-Bonnet theorem: int E_4 sqrt(g_E) d^4x_E = 32 pi^2 chi(M)
    - chi(S^4) = 2 (Euler characteristic of 4-sphere)
    - Wick rotation standard: t_E = -i t_L, giving d^4x_L = +i d^4x_E
    - Effective-action relation: W_L = -i W_E (Euclidean to Lorentzian)

Status target: DERIVED (algebraic consequence of Wick rotation + Gauss-Bonnet).
"""

import sympy as sp
from sympy import pi, I, integrate, symbols, simplify, Rational

print("=" * 68)
print("STEP 02 — Wick rotation and Euler-density in Im(Gamma_CTP)")
print("=" * 68)
print()

# =============================================================================
# 2.1 — Euclidean integrated Euler density on S^4
# =============================================================================
print("2.1 — Gauss-Bonnet evaluation on Euclidean S^4")
print("-" * 68)

chi_S4 = 2                              # Euler characteristic of S^4
# Gauss-Bonnet: int E_4 sqrt(g_E) d^4x_E = 32 pi^2 chi for compact 4-manifold
int_E4_euclidean = 32 * pi**2 * chi_S4
print(f"  chi(S^4) = {chi_S4}")
print(f"  ∫ E_4 √g_E d⁴x_E = 32π² · χ(S⁴) = 32π² · 2 = {int_E4_euclidean}")
print(f"  Numerically: {float(int_E4_euclidean):.6f}")
print()
print("  This is a REAL POSITIVE number (Gauss-Bonnet is a topological invariant).")
print()

# =============================================================================
# 2.2 — The Wick rotation
# =============================================================================
print("2.2 — Wick rotation from Euclidean S^4 to Lorentzian dS_4")
print("-" * 68)
print("""
  Convention (standard HEP / Srednicki):
      t_E = -i · t_L    (Euclidean time from Lorentzian)
      dt_E = -i · dt_L
      d⁴x_E = dt_E · d³x = -i · dt_L · d³x = -i · d⁴x_L
  Equivalently:
      d⁴x_L = +i · d⁴x_E                                     (Rel. 1)

  Metric signatures:
      g_E = +1111 (positive definite, √g_E real positive)
      g_L = -111  (Lorentzian, √(-g_L) real positive)
  Their magnitudes are equal (same spatial volume element), so
      √g_E = √(-g_L)                                         (Rel. 2)

  Euler density E_4 is built from the Riemann tensor as a scalar
  contraction. Wick rotation flips Riemann components in specific
  ways, but E_4 remains a REAL SCALAR on both signatures. E_4 itself
  does not pick up an i.                                      (Rel. 3)
""")

# =============================================================================
# 2.3 — Integrated Euler in Lorentzian signature
# =============================================================================
print("2.3 — Lorentzian integrated Euler density")
print("-" * 68)
print("""
  From (1), (2), (3):
      ∫ E_4 √(-g_L) d⁴x_L = ∫ E_4 √g_E · (+i) · d⁴x_E = i · ∫ E_4 √g_E d⁴x_E
""")

int_E4_lorentzian = I * int_E4_euclidean
print(f"  ∫ E_4 √(-g_L) d⁴x_L = i · 64π² = {int_E4_lorentzian}")
print(f"  = {64} · i · π² = 64π² · i")
print()
print("  The integrated Euler density on Lorentzian dS₄ is PURELY IMAGINARY.")
print("  This is a direct consequence of Wick rotation: the spacetime volume")
print("  picks up an i, while E_4 itself does not.")
print()

# =============================================================================
# 2.4 — Where does the Euler term live in the CTP effective action?
# =============================================================================
print("2.4 — Euler term in the CTP effective action")
print("-" * 68)
print("""
  The 1-loop Euclidean effective action on S^4 includes a Euler-density
  contribution from the heat kernel expansion:

      W_E ⊃ b · ∫ E_4 √g_E d⁴x_E = 64π² · b       (Step 1 result, REAL)

  Standard relation between Euclidean and Lorentzian effective actions
  (Srednicki §6, Peskin-Schroeder §9.5):

  The partition functions are related by analytic continuation:
      Z_E = exp(-W_E),  Z_L = exp(+i · W_L)
  Continuation Z_L → Z_E ⇒ i · W_L = -W_E ⇒
      W_L = +i · W_E                                 (Rel. 4)

  Applying (4) to the Euler piece:
""")

b = symbols('b', real=True)
W_E_euler = b * int_E4_euclidean   # Real on Euclidean
W_L_euler = I * W_E_euler          # W_L = +i · W_E

print(f"      W_E_Euler = b · ∫E₄√g_E d⁴x_E = b · 64π²           (real)")
print(f"      W_L_Euler = +i · W_E_Euler    = +i · b · 64π²      (purely imaginary)")
print()
print("  In CTP formalism, Gamma_CTP is decomposed into real (dissipative)")
print("  and imaginary (noise/decoherence) parts:")
print()
print("      Gamma_CTP = Re(Gamma_CTP) + i · Im(Gamma_CTP)")
print()
print("  The Euler contribution +i · b · 64π² lands in Im(Gamma_CTP):")
print()
print(f"      Im(Gamma_CTP) ⊃ +b · 64π²          (CONTRIBUTES)")
print(f"      Re(Gamma_CTP) ⊃ 0                   (from Euler term)")
print()
print("  The Weyl² coefficient 'a' does NOT contribute on S^4 at all")
print("  (because C_μνρσ = 0 there — Step 1 result). So:")
print()
print(f"      On S^4:   Im(Gamma_CTP) = +b · 64π² + (other terms)")
print(f"                Re(Gamma_CTP) = (terms not from bulk anomaly)")

# =============================================================================
# 2.5 — Cross-check: the CTP noise-kernel picture
# =============================================================================
print()
print("2.5 — Cross-check against GRUT's decoherence framework")
print("-" * 68)
print("""
  GRUT's CTP action (from V7 §2 and decoherence paper):

      S_CTP[z_r, z_a] = z_a · F[z_r] + (i/2) · z_a · N · z_a       (eq 1 GRUT)

  where F[z_r] is the dissipation kernel (real part of influence
  functional) and N is the noise kernel (imaginary part).

  Our Step 2 result says: the Euler contribution on S^4 lives in the
  imaginary part of Gamma_CTP, i.e., it couples to the noise kernel N,
  not to F. This is structurally consistent with GRUT's claim that the
  cosmological formula derives from decoherence physics — because N
  is the decoherence/noise sector.

  This is a consistency check, not a derivation: it shows that IF GRUT's
  CTP construction follows standard Wick rotation conventions, the
  Euler term is naturally in the decoherence sector. It does NOT yet
  show that the specific C_Cosmo/C_Final ratio equals epsilon —
  that requires Steps 3-6.
""")

# =============================================================================
# 2.6 — Transcendentals tracking (per STEP_00)
# =============================================================================
print("2.6 — Transcendentals appearing in Step 2")
print("-" * 68)
print("""
  Step 2 produced:
      ∫E₄√g_E d⁴x_E = 64π²
      Im(Gamma_CTP) ⊃ +64π² b

  Transcendentals: π² (from 4-dim integration measure on S^4).

  Expected at 1-loop: rationals, π². ✓ Consistent.
  No ζ(3) yet. That should appear only at 3-loop in Step 6.
""")

# =============================================================================
# Status summary
# =============================================================================
print("=" * 68)
print("Status at end of Step 2")
print("=" * 68)
print("""
  DERIVED:
    • ∫E₄√g_E d⁴x_E = 32π² · χ(S⁴) = 64π² (Gauss-Bonnet + χ(S⁴)=2)
    • Wick rotation gives d⁴x_L = +i · d⁴x_E, so the integrated
      Euler density on dS_4 is 64π²·i (purely imaginary)
    • The Euler-density piece of the 1-loop effective action lands
      entirely in Im(Gamma_CTP) under W_L = +i · W_E
      (convention cross-checked: Srednicki §6, Peskin-Schroeder §9.5)

  STRUCTURAL:
    • GRUT's CTP decoherence sector (the noise kernel N in eq 1)
      is naturally coupled to the Euler term on S^4, while
      the Weyl²-coefficient 'a' does not contribute at all
      (because C²=0 on S^4, per Step 1)

  OPEN / FOR LATER STEPS:
    • Does the coefficient that enters Im(Gamma_CTP) equal b_free × ε
      (coupling-corrected Euler coefficient)?
         → Step 3: Osborn's ε structure
    • How does the Gibbons-Hawking thermal asymmetry split forward/
      backward branches?
         → Step 5
    • Does the final ratio C_Cosmo / C_Final = ε?
         → Step 6 (load-bearing)

  Step 2 has not derived R = ε. It has shown that the physical object
  naturally coupled in GRUT's CTP-on-S⁴ formula is the coefficient of
  the Euler term in the imaginary action, not the flat-space ratio |b/a|.
""")
