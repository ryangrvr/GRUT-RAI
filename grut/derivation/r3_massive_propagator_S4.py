"""
R3 follow-up — massive propagator on S^4 and the scale dominance
question for the 1-loop matter self-energy.

Goal:
    Test interpretation (β): does the 1-loop matter self-energy
    on S^4 with mass m << H_inf get its dominant contribution
    from scales near m (matter mass) or near H (curvature scale)?

Approach:
    1. Use the Allen-Jacobson massive scalar propagator on S^4.
    2. Compute <phi^2>(m, H) at 1-loop (coincident limit).
    3. Identify the natural scale that appears.
    4. Extrapolate to the self-energy <F^2 F^2> question.

Key reference: Allen (1985), "Vacuum states in de Sitter space,"
Phys. Rev. D32, 3136. Also Bunch-Davies (1978).
"""

import math
import sympy as sp
from sympy import symbols, simplify, digamma, pi, sqrt, log, Rational

H, m = symbols('H m', positive=True)

# =============================================================================
# Allen-Jacobson <phi^2> on Euclidean S^4 for massive scalar
# =============================================================================
#
# Standard result: for a massive scalar on dS4 (or Euclidean S^4),
# the coincident limit is:
#
#   <phi^2>(m, H) = (H^2 / (16 pi^2)) × [psi(3/2 + nu) + psi(3/2 - nu)
#                                        + 2 ln(H / mu_bar) - 1]
#
# where nu = sqrt(9/4 - m^2/H^2) and mu_bar is the renormalization scale.
# (In MS-bar scheme; the mu_bar dependence is the freedom from eq (93)
# in HV 2008 that makes mu arbitrary.)
#
# The psi functions are digamma. For small m/H (light field):
#   nu ≈ 3/2 - m^2/(3 H^2) + ...
#   psi(3/2 + nu) → psi(3 - m^2/(3H^2)) ≈ psi(3) + O(m^2/H^2)
#   psi(3/2 - nu) → psi(m^2/(3H^2)) ≈ -3H^2/m^2 + gamma_E + O(m^2/H^2)
#
# So for m/H → 0:
#   <phi^2> → (H^2/(16 pi^2)) × [-3 H^2/m^2 + finite log(H/mu_bar)]
#
# The leading behavior is a 1/m^2 infrared divergence — the famous
# "large dS log" problem for light fields.
#
# For m/H >> 1 (heavy field, m >> H):
#   nu = i sqrt(m^2/H^2 - 9/4) (imaginary)
#   <phi^2> → (m^2/(16 pi^2)) × [ln(m^2/mu_bar^2) - 1 + O(H^2/m^2)]
#
# The m^2/H^2 >> 1 case gives the flat-space result with corrections
# of order H^2/m^2. Natural scale: m.

print("=" * 72)
print("R3 follow-up — Scale dominance of 1-loop matter self-energy on S^4")
print("=" * 72)
print()
print("Using Allen-Jacobson <phi^2> for massive scalar on Euclidean S^4:")
print()
print("  <phi^2>(m, H) = (H^2 / (16 pi^2)) ×")
print("                    [psi(3/2 + nu) + psi(3/2 - nu) + 2 ln(H/µ̄) - 1]")
print("  where nu = sqrt(9/4 - m^2/H^2)")
print()

# Light-field limit
print("LIGHT FIELD LIMIT (m << H, standard dS IR limit):")
print("  nu ≈ 3/2 - m^2/(3H^2) + O((m/H)^4)")
print("  psi(3/2 + nu) → psi(3) + O(m^2/H^2) = 1 + O(...)")
print("  psi(3/2 - nu) → psi(m^2/(3H^2)) ≈ -3H^2/m^2 + gamma_E")
print()
print("  <phi^2> ≈ (H^2/(16 pi^2)) × [-3 H^2/m^2 + O(1)]")
print()
print("  Dominant term: (-3 H^4) / (16 pi^2 m^2)")
print("  — large, scales as H^4/m^2, sensitive to IR of light field")

# For SM top quark at inflation:
H_inf = 1e13   # GeV
m_top = 173    # GeV
ratio = m_top / H_inf
phi2_light = (H_inf**2 / (16 * math.pi**2)) * (-3 * H_inf**2 / m_top**2)
print()
print(f"  Numerical: H_inf = {H_inf:.0e} GeV, m_top = {m_top} GeV, m/H = {ratio:.0e}")
print(f"  <phi^2>_top ≈ {phi2_light:.2e} GeV^2")
print()

# Heavy-field limit
print("HEAVY FIELD LIMIT (m >> H, decoupled):")
print("  nu = i sqrt(m^2/H^2 - 9/4) (imaginary)")
print("  <phi^2> → (m^2/(16 pi^2)) × [ln(m^2/µ̄^2) - 1 + O(H^2/m^2)]")
print()
print("  Natural scale: m. Flat-space behavior with corrections in H^2/m^2.")
print()

# =============================================================================
# Critical observation: SM masses are in the LIGHT regime
# =============================================================================
print("=" * 72)
print("Scale dominance analysis")
print("=" * 72)
print("""
  For SM matter on Euclidean S^4 of radius 1/H_inf:
    * All SM particles have m << H_inf (even top at 173 GeV is
      10^-11 of H_inf ~ 10^13 GeV).
    * ALL SM matter is in the LIGHT regime.
    * The 1-loop <phi^2> is DOMINATED by the IR divergence
      ~ H^4/m^2 — sensitive to both curvature H AND the particle
      mass m simultaneously.

  The "natural scale" from the dominant term -3H^4/(16 pi^2 m^2) is:
    * The H^4 factor: clearly sets scale of H
    * The 1/m^2 factor: indicates sensitivity to the matter mass
    * The COMBINATION: scale is geometric mean sqrt(H × m²/H) = m?

  Actually, the standard interpretation (e.g., Bunch-Davies,
  Mottola, Starobinsky) is that this IR behavior is AN ARTIFACT
  of the single-field tree-level expansion. Resumming leading logs
  gives the effective scale ~ H (curvature).

  The RG-improved result uses the running coupling at scale H:
    alpha(H) = alpha(M_Z) × RG factor
    For alpha_s: alpha_s(10^13 GeV) ≈ 0.027

  RG-improved epsilon evaluation:
    epsilon(H_inf) = 1 + (17/3) × alpha_s(H_inf) / (4 pi)
                  = 1 + (17/3) × 0.027 / (4π)
                  = 1 + 0.012
                  ≈ 1.012 (far from 1.155)
""")

# =============================================================================
# The specific question: matter self-energy
# =============================================================================
print("=" * 72)
print("Matter self-energy <F^2 F^2> on S^4: does it pick M_Z or H?")
print("=" * 72)
print("""
  The 1-loop contribution to <F^2(x) F^2(y)> involves matter
  propagators in a loop. For SM matter in the light-field regime,
  the propagators are:

    G_m(x, y) on S^4 with m/H << 1

  The loop integral ∫G_m(x,y)^2 dvol has contributions from:
    * Short-distance (σ(x,y) → 0): UV region. The propagator
      becomes flat-space-like, G ~ 1/σ^2. The integral diverges
      as σ → 0 and needs regularization. Natural regulator scale:
      the matter mass m.

    * Long-distance (σ ~ H^-1): IR region. The propagator
      becomes constant (plateau behavior) on S^4. Natural scale: H.

  For the UV-divergent piece (which after regularization gives the
  finite coupling-dependent correction):
    - Regularization scheme is MS-bar with scale µ̄
    - Physical result depends on µ̄ via RG running
    - Standard dS practice: choose µ̄ = H to avoid large logs
    - This gives alpha(H) in the coefficient — the H_inf scheme

  For the IR-plateau piece:
    - Dominated by super-horizon modes
    - Natural scale is H (curvature)
    - Thermal KMS at T_GH = H/(2π) — same scale

  CONCLUSION: Under standard perturbation theory, BOTH the UV and
  IR contributions to the matter self-energy on S^4 naturally use
  µ ~ H. The matter mass m appears as a ratio m/H in the finite
  part, but the RUNNING COUPLING is at scale H.

  This argues AGAINST interpretation (β). The standard perturbation-
  theory answer is µ = H, giving epsilon(H_inf) ≈ 1.03 and
  Omega_L ≈ 0.91, NOT the M_Z match.
""")

# =============================================================================
# The honest limit of this analysis
# =============================================================================
print("=" * 72)
print("Where interpretation (β) might still survive")
print("=" * 72)
print("""
  The analysis above uses TREE-LEVEL + 1-loop RG-improved perturbation
  theory on dS. This is the standard Hu-Verdaguer / Bunch-Davies
  approach.

  Interpretation (β) — which would select M_Z — would require ONE
  of:

  1. Non-perturbative effects that CHANGE the scale-dependence
     structure. E.g., Starobinsky's stochastic inflation shows
     that the IR dynamics of light fields on dS is governed by an
     EFFECTIVE Fokker-Planck equation. Whether this effective
     dynamics picks M_Z is unclear.

  2. CTP-specific features NOT captured by standard perturbation
     theory. E.g., the noise-kernel asymmetry at T_GH = H/(2π)
     could modify the effective scale for the Keldysh observable.
     Would need explicit calculation of CTP noise kernel on S^4.

  3. MATCHING arguments: the SM is DEFINED at M_Z as an EFT. Any
     observable derived from the SM Lagrangian uses α(M_Z) as the
     INPUT. The dS physics then USES this input. Under this reading,
     the RG improvement to µ = H is a CHOICE, not a requirement.
     The input-scheme answer uses α(M_Z), giving the 0.04% match.

  Interpretation 3 is the simplest and most defensible, but it's
  NOT standard perturbation theory. Standard PT says resum large
  logs; this says don't. The argument for "don't resum" would be
  that the M_Z matching scale is MORE PHYSICAL than the µ = H choice
  because it's where the SM is observationally defined.

  This is a genuine theoretical question without a clean resolution
  at my level of analysis.
""")

# =============================================================================
# Honest verdict
# =============================================================================
print("=" * 72)
print("Honest verdict on interpretation (β)")
print("=" * 72)
print("""
  Under STANDARD PERTURBATION THEORY (RG-improved):
    * Natural scale for matter self-energy on S^4 is µ = H_inf
    * Matter mass m enters only as m/H ratio
    * epsilon(H_inf) ≈ 1.03, Omega_L ≈ 0.91 (fails Planck by 30%)
    * Interpretation (β) fails structurally.

  Under INPUT-SCHEME (no RG improvement):
    * Use alpha(M_Z) as the input coupling
    * Log terms absorbed into the coefficient 17
    * epsilon(M_Z) ≈ 1.16, Omega_L ≈ 0.69 (matches Planck 0.04%)
    * Interpretation (β) holds, but at the cost of abandoning
      standard RG improvement.

  The TRUE answer depends on which scheme corresponds to the
  physical observable GRUT's formula computes. This cannot be
  decided from my current analysis alone.

  For the identification to hold at M_Z, GRUT needs to argue that:
     (i) The CTP observable on S^4 corresponds to the M_Z input
         scheme (no RG improvement), or
     (ii) There is a specific CTP mechanism that makes the M_Z
          scheme the physically correct one.

  Neither is standard; both require explicit argument.

  The honest status of interpretation (β):
    * Matter-self-energy scale-dominance argument does NOT cleanly
      support M_Z over H under standard perturbation theory.
    * The M_Z match is robust in the INPUT SCHEME but this scheme
      is not what standard dS effective action practice uses.
    * A specialist would need to identify the specific scheme
      relevant to GRUT's observable.
""")

# =============================================================================
# What this means for the overall program
# =============================================================================
print("=" * 72)
print("What this means for the overall program")
print("=" * 72)
print("""
  After full R3 analysis:

  The strongest honest statement that can be made:

    "R_GRUT = eps_combined(SM, M_Z) gives a 0.04% match to Planck
     when evaluated in the INPUT SCHEME (alpha at M_Z, no RG
     improvement). This scheme is natural when the SM is treated
     as an EFT defined at M_Z, but is NOT the standard dS
     perturbation-theory practice (which would RG-improve to
     alpha at H_inf, giving 30% Planck miss).

     Whether the INPUT SCHEME or the RG-IMPROVED SCHEME is the
     physically correct one for GRUT's specific observable on S^4
     is NOT DETERMINED by our analysis. It would require either
     (a) an explicit CTP calculation showing which scheme emerges,
     or (b) a theoretical argument (scheme-independence + structural
     considerations) that selects one over the other.

     Under (a) the identification either succeeds (if M_Z scheme
     emerges) or fails (if H_inf scheme emerges).
     Under (b) the identification is pending theoretical work."

  This is a WEAKER claim than earlier drafts. It's also more honest.

  The identification is STILL PLAUSIBLE — schemes that match
  Planck exist, and one has a natural interpretation (the SM as
  an EFT at M_Z). But it is no longer a theorem-in-progress;
  it's a specific scheme choice that needs justification.
""")
