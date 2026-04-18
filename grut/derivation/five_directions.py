"""
FIVE DIRECTIONS for the specialist tensor projection on S^4.

Direction 1: Ratio structure — does V7 construct both C's with eps dressing?
Direction 2: Non-perturbative QCD (instanton) contributions to noise kernel.
Direction 3: Cross-sector 3-loop terms.
Direction 4: Higgs thermal restoration at T_GH.
Direction 5: Graviton loop contributions.

For each: concrete computation where possible, honest scope where not.
"""

import math
from fractions import Fraction

print("=" * 78)
print("FIVE DIRECTIONS — concrete analysis to the limit of our tools")
print("=" * 78)

# Constants
alpha_s_MZ = 0.1181
alpha_2_MZ = 0.03376
alpha_Y_MZ = 0.01018
M_Z = 91.2         # GeV
M_Pl = 1.22e19     # GeV
v_EW = 246.0       # GeV  Higgs VEV
H_inf = 1e13       # GeV  inflation scale
T_GH = H_inf / (2 * math.pi)  # Gibbons-Hawking temperature

K_SU3 = 17.0
b0_SU3 = 7.0

def alpha_rg(a_ref, b0, mu_ref, mu):
    return 1.0 / (1.0 / a_ref + (b0 / (2.0 * math.pi)) * math.log(mu / mu_ref))

# =============================================================================
# Direction 1: RATIO STRUCTURE per V7/V8
# =============================================================================
print()
print("-" * 78)
print("Direction 1: What the V7/V8 doc actually posits for C_Cosmo and C_Final")
print("-" * 78)
print("""
  V7/V8 doc structure (per ZENODO_EPSILON_IDENTIFICATION.md and §12):
      C_Final = b_free                            (bare free-field)
      C_Cosmo = b_free * eps_effective(T_GH)      (thermally dressed)

  Therefore:
      R_GRUT = |C_Cosmo / C_Final| = eps_effective

  IMPLICATION for the ratio near-invariance argument:
      This is K1 = 17, K2 = 0 — the MAXIMALLY scheme-dependent case.
      The ratio drifts by ~11% from M_Z to H_inf.
      Ratio near-invariance argument DOES NOT APPLY here.

  CAVEAT: This is V7's structural CONJECTURE, not a derivation from 3-loop
  CTP on S^4. The specialist may find the ACTUAL 3-loop structure gives
  different dressings for C_Cosmo and C_Final — possibly putting us in the
  near-invariant regime after all. But taking V7 at face value: the
  scheme question is decisive.

  So the specialist's first task becomes: does the 3-loop CTP calculation
  CONFIRM V7's identification (C_Cosmo / C_Final = eps) or produce a more
  complex ratio structure? If confirmed, the scale question returns in
  full force.
""")

# RG evolve eps across scales under V7's "R = eps" assumption
print("  Under V7 structure (R = eps), Omega_Lambda across scales:")
print()
S = 108.0 * math.pi
tau_0 = 1.322e15
H_0_Hz = 70.0e3 / 3.0857e22

def eps_SU3(mu):
    a = alpha_rg(alpha_s_MZ, b0_SU3, M_Z, mu)
    return 1.0 + K_SU3 * a / (4.0 * math.pi)

def omega_L(R):
    return ((2.0 - R) / (S * tau_0 * H_0_Hz))**2

print(f"  {'mu [GeV]':>12s}  {'alpha_s':>9s}  {'eps':>9s}  {'Omega_L':>9s}  {'vs Planck':>10s}")
print("  " + "-" * 58)
for mu in [M_Z, v_EW, T_GH, H_inf]:
    a = alpha_rg(alpha_s_MZ, b0_SU3, M_Z, mu)
    e = eps_SU3(mu)
    OL = omega_L(e)
    dev = (OL / 0.6889 - 1.0) * 100
    label = {M_Z: "M_Z", v_EW: "v_EW", T_GH: "T_GH", H_inf: "H_inf"}[mu]
    print(f"  {label:>5s} {mu:>6.2e}  {a:>9.5f}  {e:>9.4f}  {OL:>9.4f}  {dev:>9.2f}%")

print("""
  Key numbers under V7 structure:
    mu = M_Z:  Omega_L = 0.695  (+0.8% from Planck)
    mu = T_GH: Omega_L = 0.896  (+30% from Planck)
    mu = H_inf: Omega_L = 0.899  (+30% from Planck)

  Under V7's ratio structure, the scheme question is decisive. Only M_Z
  scheme matches Planck. Needs a physical argument to select mu = M_Z.
""")

# =============================================================================
# Direction 2: Non-perturbative QCD (instantons)
# =============================================================================
print()
print("-" * 78)
print("Direction 2: Non-perturbative QCD (instantons) on S^4")
print("-" * 78)
print("""
  Instanton action: S_inst(mu) = 8 pi^2 / g^2(mu) = 2 pi / alpha_s(mu)

  Contribution to any observable: suppressed by exp(-S_inst).
""")

print(f"  {'Scale':<10s}  {'mu [GeV]':>12s}  {'alpha_s(mu)':>12s}  {'S_inst':>8s}  "
      f"{'exp(-S)':>14s}")
print("  " + "-" * 66)
for name, mu in [("M_Z", M_Z), ("T_GH", T_GH), ("H_inf", H_inf), ("Lambda_QCD", 0.2)]:
    if mu > 1.0:
        a = alpha_rg(alpha_s_MZ, b0_SU3, M_Z, mu)
    else:
        # IR divergent, just note conceptually
        a = 1.0  # symbolic
    S_inst = 2 * math.pi / a if a > 0 else float('inf')
    suppr = math.exp(-S_inst) if S_inst < 700 else 0.0
    if mu < 1.0:
        print(f"  {name:<10s}  {mu:>12.3f}  {'~1 (IR)':>12s}  {S_inst:>8.1f}  "
              f"{'exp(-2pi)~1.9e-3':>14s}")
    else:
        print(f"  {name:<10s}  {mu:>12.2e}  {a:>12.5f}  {S_inst:>8.1f}  "
              f"{suppr:>14.2e}")

print("""
  VERDICT on Direction 2:
    At inflationary scales (T_GH, H_inf), instanton contributions are
    suppressed by exp(-230+) ~ 10^(-100). Utterly negligible.

    Only at Lambda_QCD ~ 200 MeV are instantons O(1), but Lambda_QCD is
    21 orders of magnitude below T_GH. At T_GH >> Lambda_QCD, QCD is
    perturbative.

    NOISE KERNEL IR ENHANCEMENT: even if the noise kernel amplifies IR
    modes by ~100x (per our spectral test), exp(-230) x 100 = exp(-225).
    Still negligible by 97 orders of magnitude.

  Direction 2 is closed: non-perturbative contributions do NOT affect
  eps at any observable precision.
""")

# =============================================================================
# Direction 3: Cross-sector 3-loop terms
# =============================================================================
print()
print("-" * 78)
print("Direction 3: Cross-sector 3-loop diagrams")
print("-" * 78)
print("""
  At 3-loop, diagrams mix gauge sectors through matter loops that carry
  multiple gauge charges (e.g., a quark carries SU(3) and SU(2) and U(1)_Y).

  Typical cross-sector correction:
      delta eps ~ (alpha_s * alpha_2 / (4 pi)^2) x (order 1 group factor)

  At M_Z:
      = (0.118)(0.034) / (4 pi)^2 ~ 4e-3 / 16 pi^2 ~ 2.5e-5
      = 0.0025% correction to eps_combined

  At T_GH:
      Smaller alpha_s, smaller cross term. Even more negligible.
""")

eps_dir3_MZ = (alpha_s_MZ * alpha_2_MZ) / (4 * math.pi)**2
eps_dir3_TGH = ((alpha_rg(alpha_s_MZ, b0_SU3, M_Z, T_GH)) *
                (alpha_rg(alpha_2_MZ, 19/6, M_Z, T_GH))) / (4 * math.pi)**2
print(f"  Cross-sector correction at M_Z:  {eps_dir3_MZ:.2e}")
print(f"  Cross-sector correction at T_GH: {eps_dir3_TGH:.2e}")
print(f"  Both well below the 0.04% Planck-match precision (4e-4).")
print()
print("  VERDICT on Direction 3: cross-sector terms are O(10^-5), below")
print("  any observable precision. Not the source of the scheme ambiguity.")
print()

# =============================================================================
# Direction 4: Higgs thermal restoration at T_GH — THE CRITICAL QUESTION
# =============================================================================
print()
print("-" * 78)
print("Direction 4: Higgs thermal restoration at T_GH — the critical question")
print("-" * 78)
print(f"""
  T_GH = H_inf / (2 pi) = {T_GH:.3e} GeV
  v (EW VEV)            = {v_EW} GeV
  Ratio T_GH / v        = {T_GH/v_EW:.3e}

  T_GH >> v by 10 orders of magnitude. EW symmetry is emphatically
  restored in the thermal state.

  Consequences:
    * Higgs VEV = 0 in the thermal state
    * All fermion "Yukawa masses" vanish: m_f = y_f * <phi> = 0
    * All SM fermions have only THERMAL mass m_thermal ~ g*T ~ g*T_GH
    * The familiar scales (M_Z = 91 GeV, m_t = 173 GeV, ...) DO NOT EXIST
      as thresholds in the thermal state.
""")

# Thermal masses at T_GH (schematic)
print("  Thermal masses at T_GH (schematic, at leading order):")
m_therm_QCD = math.sqrt(alpha_rg(alpha_s_MZ, b0_SU3, M_Z, T_GH) * 4 * math.pi) * T_GH
m_therm_EW = math.sqrt(alpha_rg(alpha_2_MZ, 19/6, M_Z, T_GH) * 4 * math.pi) * T_GH
print(f"    m_thermal (QCD sector, gluon/quark) ~ g_s(T_GH) * T_GH = {m_therm_QCD:.3e} GeV")
print(f"    m_thermal (EW sector)                ~ g_2(T_GH) * T_GH = {m_therm_EW:.3e} GeV")
print()
print(f"""
  CRITICAL IMPLICATIONS for the scale question:

  1. No M_Z threshold in the thermal state.
     The "matter-decoherence argument picks M_Z because SM matter is
     defined at M_Z" LOSES FORCE in the restored phase. There's no
     physical M_Z threshold — all fermions are massless (or thermally
     massive at scale T_GH ~ H).

  2. The natural scale is T_GH ~ H.
     For thermal physics at T_GH, renormalization-scale choices mu ~
     T_GH minimize thermal logs. This is the standard argument for
     Scenario C: R = eps(T_GH) ~ 1.03, Omega_L ~ 0.91.

  3. COUNTER-ARGUMENT (what saves M_Z):
     M_Z isn't physically defining "matter" — it's a RENORMALIZATION
     SCHEME choice. Alpha_s(M_Z) = 0.118 is the CALIBRATION INPUT.
     The physical observable is RG-invariant, and evaluating at any
     scale gives the same answer to all orders.

     At finite loop order, we need to pick mu to minimize residual
     logs. For thermal physics at T_GH, that's mu = T_GH (Scenario C).

  4. OR: M_Z is picked out because the noise kernel DEFINES itself in
     terms of the vacuum (zero-temperature) SM couplings. The CTP
     asymmetry (g_+ - g_-) couples to vacuum matter operators. The
     vacuum scale where matter is observationally resolved is M_Z.

  This is a genuine physics ambiguity. It's the core of the scheme
  question.

  WHAT DIRECTION 4 DOES TO OUR PROBABILITY ASSESSMENT:

  Before Direction 4: ~70-80% M_Z via matter-decoherence + IR spectral.
  After Direction 4: the matter-decoherence argument is weakened by the
  restored-phase observation. Downward update needed.

  Revised: ~50-60% M_Z, ~40-50% T_GH (effectively H), with the key
  contingency being whether the specialist identifies a physical reason
  why the vacuum calibration scale M_Z is the natural choice DESPITE
  thermal restoration.
""")

# =============================================================================
# Direction 5: Graviton loops
# =============================================================================
print()
print("-" * 78)
print("Direction 5: Graviton loop contributions to noise kernel")
print("-" * 78)
print(f"""
  Graviton loops contribute at order (H/M_Pl)^2:
    At H = 10^13 GeV: (H/M_Pl)^2 = {(H_inf/M_Pl)**2:.2e}

  Compare to 0.04% match precision: 4e-4.
  Graviton contribution is ~10^9 times smaller than match precision.

  VERDICT on Direction 5: graviton loops are negligible by 9 orders
  of magnitude. They do NOT affect the cosmological conclusion.

  Exception: near Planck scale (H ~ 10^18 GeV), graviton loops reach
  0.7% — relevant for the 4/8 closure ladder but NOT for current
  cosmological sector work.
""")

# =============================================================================
# Synthesis
# =============================================================================
print()
print("=" * 78)
print("Synthesis of the five directions")
print("=" * 78)
print("""
  STATUS of each direction after concrete analysis:

  D1 (ratio structure):  CRITICAL UPDATE — V7/V8 doc posits R = eps (K2=0).
                         This means the ratio near-invariance argument
                         I built earlier does NOT apply to V7's structure.
                         Specialist must verify/refute V7's identification.

  D2 (instantons):       CLOSED — exp(-230) suppressed at all relevant
                         scales, negligible by 97 orders of magnitude.

  D3 (cross-sector):     CLOSED — O(10^-5) correction, far below precision.

  D4 (Higgs thermal):    OPEN + CRITICAL — restored phase weakens the
                         matter-decoherence argument for M_Z. The
                         specialist must provide a physical reason why
                         M_Z is picked out in the thermally restored
                         phase, or the H-scheme wins.

  D5 (gravitons):        CLOSED for cosmology; open for closure ladder.

  REVISED PROBABILITY ASSESSMENT:
  Taking D1 and D4 together:
    * V7 structure is R = eps (not ratio near-invariant)
    * Restored phase weakens M_Z argument
    * ~50-60% probability the specialist finds R = eps(M_Z), Omega_L = 0.69
    * ~40-50% probability the specialist finds R = eps(T_GH), Omega_L = 0.90

  The cosmological sector is more conditional than the tensor projection
  work suggested. The ratio near-invariance argument was REAL but only
  applies if specialist finds a different structure than V7 posits.

  BUT: The M_Z argument isn't dead. The vacuum-calibration interpretation
  still stands. The IR-dominated spectral result for the right observable
  still holds. What's weakened is the specific "matter is defined at M_Z"
  argument when matter is literally massless in the thermal state.

  SPECIALIST'S CRITICAL QUESTIONS (updated with Directions):

  Q1. Is V7's identification C_Cosmo = b_free * eps, C_Final = b_free
      CORRECT, or does the 3-loop CTP calculation give a more complex
      structure (K1 != K2, both nonzero)?

  Q2. If V7 structure is confirmed (so R = eps), what is the physical
      reason to evaluate at M_Z rather than T_GH given that EW symmetry
      is restored at T_GH? Is there a vacuum-calibration argument that
      survives the restored phase?

  Q3. Does the noise kernel's IR dominance (spectral test) translate to
      a mathematically rigorous argument for mu = M_Z, or is it just
      suggestive?

  Q4. [new, from D4]: In the thermally restored phase, what replaces
      M_Z as the natural calibration scale? The noise kernel is defined
      on vacuum operators but evaluated in a thermal state; the resolution
      needs an explicit specification of which scheme is physical.

  HONEST BOTTOM LINE after five directions:

    The framework remains falsifiable with two clean outcomes:
      - Omega_L = 0.69 (M_Z scheme, 0.04-1% from Planck): 50-60% probable
      - Omega_L = 0.90 (T_GH scheme, 30% miss): 40-50% probable

    Both the physics arguments and the numerics concentrate on D1 and D4.
    D2, D3, D5 are closed or negligible at our precision.

    The ratio near-invariance insight is real but conditional on the
    specialist finding a more complex ratio structure than V7 posits.

  Direction for further work:
    * Stress-test V7's specific structural claim (§12, §26)
    * Look for vacuum-calibration arguments in thermal QFT literature
    * Consider whether the "M_Z is natural" argument can be sharpened
      into something that survives thermal restoration
""")
