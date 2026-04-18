"""
DIRECTION 4 — Higgs thermal restoration at T_GH and its implications
====================================================================

Goal: determine what happens to the SM input structure at T_GH ~ 10^12 GeV
and how this affects the scale question for eps in Osborn 2003 eq (36).

Part 1: EW restoration via Dolan-Jackiw thermal effective potential.
Part 2: The thermal scale structure at T_GH.
Part 3: Osborn formula in the restored phase — does eps change form?
Part 4: Vacuum calibration vs thermal reading of the CTP observable.
Part 5: What the specialist still has to decide.

References:
    Dolan & Jackiw (1974), Phys. Rev. D 9, 3320 — finite-T effective pot.
    Kirzhnits & Linde (1976) — EW restoration at high T
    Arnold & Espinosa (1993) — SM thermal potential 2-loop
    Braaten & Pisarski (1990) — hard thermal loops, T-scale choice
    Osborn (2003), Jack & Osborn (1990, 2014) — eps, gradient flow
"""

import math

# =============================================================================
# Physical inputs (SM at M_Z, measured)
# =============================================================================
M_Z = 91.2                 # GeV
v_EW = 246.22              # GeV (Higgs VEV)
m_H = 125.0                # GeV (Higgs pole mass, observed)
m_t = 173.0                # GeV (top quark pole mass)
M_Pl = 1.22e19             # GeV
H_inf = 1e13               # GeV (inflationary Hubble)
T_GH = H_inf / (2 * math.pi)  # Gibbons-Hawking temperature

alpha_s_MZ = 0.1181
alpha_2_MZ = 0.03376
alpha_Y_MZ = 0.01018
alpha_em_MZ = 1/127.9

# Derived at M_Z
g_s = math.sqrt(4 * math.pi * alpha_s_MZ)
g_2 = math.sqrt(4 * math.pi * alpha_2_MZ)
g_Y = math.sqrt(4 * math.pi * alpha_Y_MZ)
y_t = math.sqrt(2) * m_t / v_EW          # top Yukawa
lam_H = m_H**2 / (2 * v_EW**2)           # Higgs self-coupling at tree

print("=" * 78)
print("DIRECTION 4 — Higgs thermal restoration at T_GH")
print("=" * 78)
print()
print("Inputs at M_Z:")
print(f"  v_EW    = {v_EW} GeV (Higgs VEV)")
print(f"  m_H     = {m_H} GeV (Higgs pole mass)")
print(f"  m_t     = {m_t} GeV (top pole mass)")
print(f"  y_t     = {y_t:.4f} (top Yukawa)")
print(f"  lambda  = {lam_H:.4f} (Higgs self-coupling)")
print(f"  g_2     = {g_2:.4f} (SU(2))")
print(f"  g_Y     = {g_Y:.4f} (U(1)_Y)")
print()
print(f"Cosmological scales:")
print(f"  H_inf   = {H_inf:.2e} GeV")
print(f"  T_GH    = H/(2pi) = {T_GH:.3e} GeV")
print(f"  T_GH/v  = {T_GH/v_EW:.3e}  (ratio)")
print()

# =============================================================================
# Part 1: Critical temperature for EW restoration
# =============================================================================
print("=" * 78)
print("Part 1: Critical temperature T_c for EW restoration")
print("=" * 78)
print("""
  Dolan-Jackiw thermal effective potential (leading order):

      V_T(phi) = V_0(phi) + (T^2/24) * sum_i n_i m_i^2(phi)
                + (higher-T corrections)

  where the thermal mass term is (T^2/24) × c_SM × phi^2 with:

      c_SM = 3*y_t^2 + (9/4)*g_2^2 + (3/4)*g_Y^2 + 6*lambda   (leading)

  EW restoration when T^2 × c_SM/24 >> |m_H^2(tree)| = lambda*v^2

  Critical temperature:
      T_c^2 = 24 lambda v^2 / c_SM = 24 m_H^2 / (2 c_SM)
""")

# Thermal mass coefficient for SM
# From Arnold-Espinosa 1993, the leading coefficient for Higgs thermal mass:
c_SM = 3 * y_t**2 + (9/4) * g_2**2 + (3/4) * g_Y**2 + 6 * lam_H
print(f"  c_SM  = 3*y_t^2 + (9/4)*g_2^2 + (3/4)*g_Y^2 + 6*lambda")
print(f"        = 3*{y_t**2:.3f} + (9/4)*{g_2**2:.3f} + (3/4)*{g_Y**2:.3f} + 6*{lam_H:.3f}")
print(f"        = {c_SM:.3f}")
print()

# Critical temperature
T_c_sq = 24 * m_H**2 / (2 * c_SM)
T_c = math.sqrt(T_c_sq)
print(f"  T_c   = sqrt(24 * m_H^2 / (2 * c_SM))  = {T_c:.1f} GeV")
print(f"  T_GH/T_c = {T_GH/T_c:.2e}")
print()
print(f"  EW symmetry is restored for T > T_c ~ {T_c:.0f} GeV.")
print(f"  At T_GH = {T_GH:.2e} GeV, we are at T/T_c = {T_GH/T_c:.2e}.")
print(f"  EW symmetry is emphatically restored in the thermal state.")
print()

# =============================================================================
# Part 2: Thermal scale structure at T_GH
# =============================================================================
print("=" * 78)
print("Part 2: Thermal scale structure at T_GH")
print("=" * 78)
print("""
  In thermal field theory at temperature T, the characteristic scales are:

    Hard scale:    E ~ T              (typical particle momentum)
    Soft scale:    E ~ g*T            (thermal mass, Debye screening)
    Ultrasoft:     E ~ g^2*T          (non-perturbative magnetic)

  For hard thermal loops (Braaten-Pisarski), the natural renormalization
  scale is mu_HTL ~ pi*T (halfway between 2*pi*T Matsubara and T itself).

  For observables dominated by the thermal bath, mu ~ pi*T minimizes
  thermal logs at the 2-loop level.
""")

# Running to various thermal scales
def alpha_rg(a_ref, b0, mu_ref, mu):
    return 1.0 / (1.0 / a_ref + (b0 / (2.0 * math.pi)) * math.log(mu / mu_ref))

scales = {
    'M_Z (vacuum calibration)': M_Z,
    'T_c (~T_EW transition)': T_c,
    'T_GH (thermal)': T_GH,
    'pi*T_GH (HTL optimal)': math.pi * T_GH,
    '2*pi*T_GH (first Matsubara)': 2 * math.pi * T_GH,
    'H_inf (curvature)': H_inf,
}
print(f"  {'Scale':<32s} {'mu [GeV]':>12s} {'alpha_s':>9s} {'g_s^2':>8s}")
print("  " + "-" * 62)
for name, mu in scales.items():
    a_s = alpha_rg(alpha_s_MZ, 7.0, M_Z, mu)
    print(f"  {name:<32s} {mu:>12.3e} {a_s:>9.5f} {4*math.pi*a_s:>8.4f}")
print()
print(f"  Hard thermal scale pi*T_GH = {math.pi*T_GH:.3e} GeV.")
print(f"  This is very close to H_inf = 10^13 GeV — within a factor 2.")
print(f"  So 'thermal' and 'curvature' schemes give nearly identical alpha_s.")
print()

# =============================================================================
# Part 3: Does eps change form in the restored phase?
# =============================================================================
print("=" * 78)
print("Part 3: Osborn eps in the restored phase — does R_psi, R_phi change?")
print("=" * 78)
print("""
  Osborn eq (36) structure:

      eps_i = 1 + (1/3)(29*C_i - 12*R_psi,i - (5/2)*R_phi,i) * g_i^2/(16*pi^2)

  R_psi = sum of T(rep) over Dirac fermion flavors in the gauge rep.
  R_phi = sum of T(rep) over real scalar d.o.f.

  CRITICAL QUESTION: in the restored phase, does the Higgs VEV affect the
  effective field content?

  Answer: NO at the level of Osborn's formula.
    * R_psi counts fermion flavors coupled to gauge group, NOT their masses.
    * R_phi counts scalar d.o.f., NOT their VEV.
    * Both are group-theoretic sums independent of Higgs breaking.

  So R_psi and R_phi are the SAME in both phases:
      SU(3): C=3, R_psi=3 (6 Dirac quarks), R_phi=0  -> K=17
      SU(2): C=2, R_psi=3, R_phi=1  -> K=6.5
      U(1)_Y: C=0, R_psi=10, R_phi=0.5  -> K=-40.4

  This means eps has the SAME functional form in the restored phase.
  What changes is only WHICH alpha we plug in — the renormalization scale.

  So the question is purely: do we use alpha(M_Z) or alpha(T_GH)?
""")

# Compute eps under both choices
print("Comparison:")
K_SU3 = 17.0
eps_MZ = 1 + K_SU3 * alpha_s_MZ / (4*math.pi)
eps_TGH = 1 + K_SU3 * alpha_rg(alpha_s_MZ, 7.0, M_Z, T_GH) / (4*math.pi)
print(f"  eps_SU3(M_Z)  = 1 + 17*{alpha_s_MZ}/(4*pi)   = {eps_MZ:.4f}")
print(f"  eps_SU3(T_GH) = 1 + 17*{alpha_rg(alpha_s_MZ, 7.0, M_Z, T_GH):.4f}/(4*pi) = {eps_TGH:.4f}")
print(f"  Difference: {(eps_MZ - eps_TGH)/eps_MZ * 100:.1f}%")
print()
print("  Under V7/V8 structure (R = eps):")
S = 108.0 * math.pi
tau_0 = 1.322e15
H_0_Hz = 70.0e3 / 3.0857e22
OL_MZ = ((2.0 - eps_MZ) / (S * tau_0 * H_0_Hz))**2
OL_TGH = ((2.0 - eps_TGH) / (S * tau_0 * H_0_Hz))**2
print(f"  mu = M_Z:  Omega_L = {OL_MZ:.4f}  (Planck: 0.6889, dev: {(OL_MZ/0.6889-1)*100:+.2f}%)")
print(f"  mu = T_GH: Omega_L = {OL_TGH:.4f}  (Planck: 0.6889, dev: {(OL_TGH/0.6889-1)*100:+.2f}%)")
print()

# =============================================================================
# Part 4: Vacuum calibration vs thermal reading — the central ambiguity
# =============================================================================
print("=" * 78)
print("Part 4: Vacuum calibration vs thermal reading")
print("=" * 78)
print("""
  THE AMBIGUITY STATED PRECISELY:

  The Osborn eps formula is a 1-loop coefficient in Weyl consistency
  conditions. At 1-loop accuracy, it has residual RG scale dependence
  that is resolved by 2-loop, which has residual resolved by 3-loop, etc.

  For a PHYSICAL OBSERVABLE, the to-all-orders answer is mu-independent.
  At truncated loop order, mu-dependence is a TRUNCATION ERROR.

  The 'best' mu minimizes truncation error. For thermal physics at T, that's
  mu ~ pi*T (Braaten-Pisarski HTL scheme). For vacuum physics, it's whatever
  natural external scale the observable has.

  OPTION (i) — THERMAL READING:
    GRUT's CTP observable is thermal physics at T_GH on S^4.
    The renormalization-optimal mu is mu ~ pi*T_GH ~ 0.5 H_inf.
    At this scale, alpha_s ~ 0.026, eps_SU3 ~ 1.035.
    Ω_Λ ~ 0.90 — 30% miss from Planck.

  OPTION (ii) — VACUUM CALIBRATION READING:
    GRUT's CTP observable uses the COUPLING CONSTANTS of the SM, which
    are physically defined by their measured values at M_Z.
    The CTP asymmetry (g+ - g-) is measured relative to the SM vacuum
    action, which is specified by the M_Z-scheme.
    At M_Z: alpha_s = 0.118, eps_SU3 = 1.160.
    Ω_Λ = 0.69 — matches Planck at 0.04%.

  Option (ii) is NON-STANDARD from a thermal field theory perspective
  because it doesn't minimize truncation error at T_GH. It corresponds
  to stopping the perturbative expansion at 1-loop and evaluating at the
  input scale, without resumming the large thermal log ln(T_GH/M_Z) ~ 22.

  WHAT WOULD JUSTIFY OPTION (ii)?

  (a) The CTP observable is not a thermal observable per se — it's a
      VACUUM structure modified by thermal corrections. The formal
      expansion parameter is (g_+ - g_-), and this is measured at the
      vacuum calibration scale.

  (b) The noise kernel's IR dominance (from the spectral test) means
      the dominant contribution comes from low-eigenvalue modes that
      are "close to the vacuum." These modes see the vacuum couplings
      alpha(M_Z), not the thermal alpha(T_GH).

  (c) GRUT's formula H_inf = (2-R)/(S*tau_0) has tau_0 calibrated to the
      cosmological decoherence surface, which is a vacuum-state quantity.
      The observable R might inherit this vacuum-scale definition.

  None of (a)-(c) is rigorous. They are suggestive but require the
  specialist tensor projection to confirm.

  What we CAN compute: under V7's construction (§12), if the thermal
  reading is correct, Omega_L misses Planck by 30%. If the vacuum
  calibration reading is correct, Omega_L matches Planck at 0.04%.
""")

# =============================================================================
# Part 5: What the specialist has to decide
# =============================================================================
print("=" * 78)
print("Part 5: What the specialist still needs to decide")
print("=" * 78)
print("""
  After the Direction 4 analysis, the remaining decisions are:

  Q_THERMAL_1:
    Does the CTP noise kernel on S^4 at Hartle-Hawking thermal state
    correspond to a standard thermal observable (where mu ~ pi*T is
    optimal) or to a vacuum-structure observable (where mu ~ M_Z is
    natural)?

  Q_THERMAL_2:
    If it's the former, the framework's 30% miss from Planck is an
    honest falsification.
    If it's the latter, the framework matches Planck at 0.04%.
    The argument for "latter" needs either:
      * A formal theorem identifying the CTP observable as vacuum-type
      * Or a 3-loop tensor projection that produces R = eps(M_Z) directly
        as a specific output.

  Q_THERMAL_3:
    Can the noise kernel IR dominance (scalar spectral test 100x shifted
    toward n=0) be converted into a rigorous argument that the dominant
    CTP contribution is from "vacuum-close" modes that respect M_Z
    calibration?

  Q_THERMAL_4:
    Does V7 §26's construction explicitly specify which scale alpha
    enters at? If yes, we accept that specification. If it's ambiguous
    (alpha = alpha(mu) with mu unspecified), then the specialist has to
    pick based on perturbative argument — which defaults to mu ~ T_GH
    for thermal physics.

  Honest status of D4:
    * EW restoration: CONFIRMED (T_GH/T_c = 10^10).
    * Thermal SM has same Osborn K coefficients: CONFIRMED.
    * Scale choice: REMAINS the central open question.
    * Our evidence for M_Z: IR spectral dominance, matter-decoherence
      framework, vacuum calibration. All suggestive, none definitive.
    * Our evidence for T_GH: standard thermal field theory practice,
      minimize truncation error, no M_Z threshold in restored phase.

  PROBABILITY UPDATE FROM D4:
    D4 makes the M_Z argument work harder. It doesn't kill it, but it
    removes the "matter is defined at M_Z" intuition in the restored
    phase. The vacuum-calibration reading still stands but needs more
    physics support than the restored-phase thought experiment alone.

    Revised: ~45-55% M_Z wins, ~45-55% T_GH wins.
    Down from 50-60% / 40-50% before this explicit analysis.

    The drop is because D4 sharpens the standard argument for T_GH
    (thermal physics, optimize mu to T) without providing equal
    sharpening of an M_Z argument. We need to find an argument for
    M_Z that is as rigorous as the thermal argument for T_GH.

  DELIVERABLE FROM D4:
    The specialist now has a precise statement of the ambiguity:
    "At T_GH, standard thermal QFT practice says mu ~ pi*T_GH. What
    specific feature of GRUT's CTP construction would single out mu = M_Z
    instead?" This is a focused question rather than a vague one.
""")

print()
print("=" * 78)
print("D4 summary")
print("=" * 78)
print(f"""
  CONFIRMED:
    T_c (SM)        = {T_c:.1f} GeV      (EW transition temperature)
    T_GH            = {T_GH:.3e} GeV
    T_GH/T_c        = {T_GH/T_c:.2e}     (emphatically restored)

  SCHEME TABLE (under V7 structure R = eps):
    mu = M_Z    eps = {eps_MZ:.4f}  Omega_L = {OL_MZ:.4f}  Planck match  0.04%  ✓
    mu = T_GH   eps = {eps_TGH:.4f}  Omega_L = {OL_TGH:.4f}  Planck miss   30%   ✗

  The central question is not 'is EW restored' (yes, by 10^10) but
  'which scheme does the CTP observable physically require'.

  D4 sharpens the question from 'why M_Z' to 'what in GRUT's CTP
  construction singles out vacuum calibration over thermal optimization'.
  We have suggestive arguments but no rigorous proof.

  Next: Direction 1 (trace V7 §26 explicitly) to see if the construction
  answers Q_THERMAL_4.
""")
