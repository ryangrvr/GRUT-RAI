"""
STEP 03 — Osborn 2003 eq (36): the epsilon coefficient and its meaning

Purpose:
    Verify the epsilon formula from a published source, evaluate it for
    SM content at M_Z, and establish precisely what physical object
    epsilon is (not what we initially assumed).

Source: Hugh Osborn, "Local Couplings and Sl(2,R) Invariance for Gauge
Theories at One Loop," arXiv:hep-th/0302119 (DAMTP/03), 2003, eq (36).
Saved locally at papers/references/osborn_2003_hep-th-0302119.pdf.

    epsilon = 1 + (1/3)(29 C - 12 R_psi - (5/2) R_phi) * g^2/(16 pi^2)

with:
    g^2/(16 pi^2) = hat{g}^2 in Osborn's notation
    C  = adjoint Casimir
    R_psi = fermion index, tr(t_psi_a t_psi_b) = -delta_ab R_psi
    R_phi = scalar index, tr(t_phi_a t_phi_b) = -delta_ab R_phi

CRITICAL REFINEMENT (discovered on reading the paper):

    Epsilon is NOT a multiplicative correction to the Euler-density
    coefficient. Looking at eq (35) of the same paper:

    L = n_V {  (1/g^2) [alpha (Box g)^2 - 2 delta G^munu d_mu g d_nu g
                       - (1/3) epsilon R (d_mu g)(d^mu g)]
              - 2 kappa (1/g^3) (d_mu g)(d^mu g) Box g
              + 2 lambda (1/g^4) ((d_mu g)(d^mu g))^2 }

    Epsilon is the 2-loop coefficient of the operator

         -(1/3) n_V (1/g^2) R (d_mu g)(d^mu g)

    in the local-coupling effective-action counterterm structure.

    For CONSTANT g (no x-dependence), d_mu g = 0 and the epsilon term
    vanishes. Epsilon only contributes when couplings are x-dependent.

    This has a crucial consequence for Step 6: the identification
    R_GRUT = epsilon requires a CTP mechanism that produces an
    effective (d_mu g)^2 ≠ 0, such as Gibbons-Hawking thermal
    fluctuations at T_GH, or CTP source doubling with g_+ != g_-.

This Step 03 verifies the formula and evaluates it for SM. It does
NOT yet derive R_GRUT = epsilon — that awaits Steps 5-6.

Notation warning:
    Osborn 2003 uses 'a' for the Euler-density coefficient and 'c' for
    Weyl^2, opposite to Birrell-Davies. We continue using Birrell-Davies
    throughout (Step 1 convention), and only cite Osborn 2003 eq (36)
    for the specific epsilon formula.
"""

import math
import sympy as sp
from sympy import Rational, symbols, simplify, pi as sp_pi

# =============================================================================
# 3.1 — Symbolic form of Osborn 2003 eq (36)
# =============================================================================

C, Rpsi, Rphi, ghat2 = symbols('C R_psi R_phi ghat2', positive=True)

# Exact coefficients as printed in Osborn 2003 eq (36):
alpha_delta = 1 + Rational(1, 3) * (51*C - 20*Rpsi - Rational(7, 2)*Rphi) * ghat2
epsilon_sym = 1 + Rational(1, 3) * (29*C - 12*Rpsi - Rational(5, 2)*Rphi) * ghat2
kappa_sym   = 1 + Rational(4, 3) * (11*C -  4*Rpsi - Rational(1, 2)*Rphi) * ghat2
lambda_sym  = 1 + Rational(1, 18) * (323*C - 76*Rpsi - Rational(25, 2)*Rphi) * ghat2

print("=" * 68)
print("STEP 03 — Osborn 2003 eq (36): verified formula")
print("=" * 68)
print()
print("Source: H. Osborn, arXiv:hep-th/0302119 (Feb 2003), eq (36).")
print("Saved: papers/references/osborn_2003_hep-th-0302119.pdf")
print()
print("Symbolic form (Osborn 2003 eq 36):")
print(f"  alpha = delta = {alpha_delta}")
print(f"  epsilon        = {epsilon_sym}")
print(f"  kappa          = {kappa_sym}")
print(f"  lambda         = {lambda_sym}")
print()

# =============================================================================
# 3.2 — What epsilon actually is (reading eq 35 carefully)
# =============================================================================
print("3.2 — Physical meaning of epsilon (Osborn 2003 eq 35)")
print("-" * 68)
print("""
  eq (35) of the paper writes the local-coupling counterterm Lagrangian:

    L = n_V { (1/g^2) [ alpha (Box g)^2
                       - 2 delta G^{mu nu} d_mu g d_nu g
                       - (1/3) epsilon R (d_mu g)(d^mu g) ]
              - 2 kappa (1/g^3) (d_mu g)(d^mu g) Box g
              + 2 lambda (1/g^4) ((d_mu g)(d^mu g))^2 }

  epsilon is the 2-loop-computed coefficient of the operator
  -(1/3) n_V R (d_mu g)(d^mu g) / g^2.

  Key property: this operator vanishes identically when g is constant.
  epsilon contributes to the effective action only when the coupling
  is promoted to a local field g(x) with (d_mu g) != 0.

  This has direct consequences for the CTP-on-S^4 identification:
    - On S^4 with strictly constant g, the epsilon term is zero.
    - For R_GRUT to identify with epsilon, the CTP construction
      must produce an effective (d_mu g)^2 ≠ 0 between forward
      and backward branches, e.g., via Gibbons-Hawking thermal
      fluctuations or explicit CTP source doubling.
""")

# =============================================================================
# 3.3 — Cross-check against Jack-Osborn 1990 eq (5.8)
# =============================================================================
print("3.3 — Cross-check: Jack-Osborn 1990 eq (5.8) contains the same")
print("     transcendental coefficients (51C-20R, 29C-12R, 11C-4R)")
print("-" * 68)
print("""
  Jack-Osborn 1990 eq (5.8) computes the 2-loop DIVERGENT counterterm
  polynomial for pure gauge theory in dim reg. Its coefficients include:
      (ε/6)(51C - 20R) -- coefficient of 2 G^munu v_mu v_nu - (∇v)^2
      (ε/6)(29C - 12R) -- coefficient of H v^2  (where H ~ R/(d-1))
      -(2/3)(11C - 4R) -- coefficient of various v-structured terms
      -(5ε/9)(23C - 4R) -- coefficient of v^2 v^2
      -(ε/3)(7C  - 4R) -- coefficient of v^2 ∇v

  Here 'ε' is the dim-reg parameter (d = 4 - 2ε), NOT the epsilon of
  Osborn 2003 eq (36). But the group-theory coefficients (51C-20R),
  (29C-12R), (11C-4R) match, reflecting that Osborn 2003 is the
  RENORMALIZED (finite, after subtraction) form of Jack-Osborn 1990's
  structure.

  Osborn 2003 extends Jack-Osborn 1990 by (a) adding scalars (the R_phi
  terms with -(7/2) R_phi, -(5/2) R_phi etc.) and (b) rearranging the
  finite local counterterms into the alpha, delta, epsilon, kappa, lambda
  basis of eq (35) rather than the original v-structured basis.

  Cross-check passed: the 29C-12R coefficient in Osborn 2003 eq (36)
  is the same 29C-12R coefficient that appears in Jack-Osborn 1990
  eq (5.8), just attached to the renormalized operator
  (1/3)(1/g^2) R (d_mu g)^2 rather than the divergent H v^2 counterterm.
""")

# =============================================================================
# 3.4 — Numerical evaluation for SM gauge groups at M_Z
# =============================================================================
print("3.4 — Numerical evaluation: epsilon for SM at M_Z (Dirac convention)")
print("-" * 68)

# SM content per gauge group (Dirac fermion convention, from Step 1 context)
# For SU(3) QCD: C = 3 (adjoint Casimir), R_psi = 3 (6 Dirac quarks, T_F=1/2),
#                R_phi = 0 (no SU(3) scalars in SM)
# For SU(2):     C = 2, R_psi = 3 (SM fermion content in SU(2) doublets, Dirac convention),
#                R_phi = 1 (Higgs doublet)
# For U(1):      C = 0 (abelian), R_psi = 10 (sum Y^2 for SM fermions),
#                R_phi = 0.5 (Higgs Y^2)

alpha_s_MZ = 0.1181   # PDG
alpha_2_MZ = 0.03376
alpha_Y_MZ = 0.01018

def epsilon_numeric(alpha, C_val, Rpsi_val, Rphi_val):
    g2_over_16pi2 = alpha / math.pi  # since g^2 = 4pi alpha, g^2/(16pi^2) = alpha/(4pi)
    g2_over_16pi2 = alpha / (4 * math.pi)  # correction: g^2/(16pi^2) = 4pi alpha/(16pi^2) = alpha/(4pi)
    coef = (1/3) * (29*C_val - 12*Rpsi_val - (5/2)*Rphi_val)
    return 1 + coef * g2_over_16pi2, coef

groups = [
    ("SU(3)", alpha_s_MZ, 3, 3, 0),
    ("SU(2)", alpha_2_MZ, 2, 3, 1),
    ("U(1)",  alpha_Y_MZ, 0, 10, 0.5),
]

print(f"  {'Group':<8} {'alpha':>8} {'C':>3} {'R_psi':>5} {'R_phi':>5} "
      f"{'coef':>8} {'epsilon':>10}")
for name, alpha, C_v, Rp, Rphi_v in groups:
    eps, coef = epsilon_numeric(alpha, C_v, Rp, Rphi_v)
    print(f"  {name:<8} {alpha:8.4f} {C_v:3d} {Rp:5.1f} {Rphi_v:5.1f} "
          f"{coef:8.3f} {eps:10.4f}")

print()

# Check against the Step 1 numbers we've been using
print("  Cross-check against values used throughout the project:")
eps_su3, _ = epsilon_numeric(alpha_s_MZ, 3, 3, 0)
print(f"    epsilon_SU3(M_Z) = {eps_su3:.4f}  (expected 1.1596)")
print(f"    Match: {'YES' if abs(eps_su3 - 1.1596) < 0.001 else 'NO'}")

# =============================================================================
# 3.5 — Transcendentals tracking
# =============================================================================
print()
print("3.5 — Transcendentals introduced at this step")
print("-" * 68)
print("""
  Step 03 introduces no new transcendentals. The numerical coefficients
  in eq (36) are rational (17/3, 51/3 etc.) — this is a 2-loop dim-reg
  result, and 2-loop dim-reg coefficients for simple gauge theories
  are typically rational × pi^(-n).

  The ln(2) zeta(3) that appears in GRUT's C_FINAL is a 3-LOOP object,
  not 2-loop. It should appear naturally only in Step 06 when we attempt
  to assemble the 3-loop CTP result, not at this stage.

  Consistent with the plan.
""")

# =============================================================================
# Status summary for Step 3
# =============================================================================
print("=" * 68)
print("Status at end of Step 03")
print("=" * 68)
print("""
  DERIVED (from published literature):
    * Osborn 2003 eq (36) gives the 2-loop coefficient
        epsilon = 1 + (1/3)(29C - 12 R_psi - (5/2) R_phi) g^2/(16pi^2)
    * Verified against the actual PDF of arXiv:hep-th/0302119.
    * Cross-check: Jack-Osborn 1990 eq (5.8) contains the same group-
      theory coefficients (51C-20R, 29C-12R, 11C-4R) in the divergent
      counterterm polynomial.
    * Numerically: epsilon_SU3(M_Z) = 1.1598 with alpha_s = 0.1181.

  STRUCTURAL (physical interpretation):
    * epsilon is the coefficient of -(1/3) n_V (1/g^2) R (d_mu g)^2 in
      the local-coupling counterterm Lagrangian eq (35).
    * epsilon contributes to the effective action only when g(x) is
      x-dependent. For constant g, its contribution is zero.

  OPEN (requires later steps):
    * The physical mechanism by which the CTP construction on S^4
      produces an effective (d_mu g)^2 ≠ 0 is NOT in Step 03.
    * The identification R_GRUT = epsilon is a claim about the ratio
      of two pieces of the CTP effective action equaling epsilon
      through the R(d_mu g)^2 channel. This requires Step 05
      (Gibbons-Hawking thermal mechanism) and Step 06 (CTP assembly).

  IMPORTANT: Step 03 has NOT yet derived that R_GRUT = epsilon. It has
  verified that the epsilon formula is real, published, and gives the
  numerical values used in the project. The identification is still a
  conjecture, but now with a verified formula behind it.
""")
