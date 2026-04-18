"""
R3 — Scale selection on S^4: at what mu is g(mu) evaluated in the
     CTP effective action?

This is the single remaining open question of the derivation. We tackle
it by (A) enumerating candidate scales, (B) evaluating eps and Omega_L at
each, (C) identifying the physical argument that would select one.

Candidate scales mu:
    1. H_inf ~ 10^13 GeV (curvature scale on S^4; standard Hu-Verdaguer
       choice to avoid large logs)
    2. M_Z ~ 91 GeV (EW matching scale; all SM gauge content active)
    3. m_t ~ 173 GeV (top mass threshold; heaviest SM particle)
    4. Lambda_QCD ~ 0.3 GeV (IR confinement; non-perturbative, risky)
    5. m_thermal ~ H_inf × sqrt(alpha) ~ 3 x 10^12 GeV (thermal mass
       from Gibbons-Hawking temperature)
    6. M_Planck ~ 10^19 GeV (UV boundary)

For each, compute alpha_s, eps_SU3, eps_combined, and Omega_Lambda.
Only the specific scale that reproduces Planck Omega_L = 0.6889 at
< 1% is "selected" by the observation.
"""

import math

# =============================================================================
# 1-loop SM RG running (using standard values and QCD only for simplicity;
# full 2-loop SM running would be more accurate but the trends are clear)
# =============================================================================

alpha_s_MZ = 0.1181
alpha_2_MZ = 0.03376
alpha_Y_MZ = 0.01018
M_Z_GeV = 91.2

# Standard SM 1-loop beta function coefficients
# dalpha/dlnmu = -b_alpha^2/(2*pi) with negative sign for AF
b_s = -7.0     # SU(3), N_f = 6 (all quarks active at high scales)
b_2 = +19/6    # SU(2), normalized
b_Y = -41/10   # U(1), GUT-normalized

def run_alpha_1loop(alpha_MZ, b, mu):
    """Run alpha from M_Z to mu using 1-loop beta function.
    alpha(mu) = alpha(M_Z) / [1 + (b/2pi) alpha(M_Z) ln(mu/M_Z)]
    where sign of b is such that b > 0 for asymptotic freedom (alpha decreases).
    """
    return alpha_MZ / (1 + (-b/(2*math.pi)) * alpha_MZ * math.log(mu/M_Z_GeV))

# Actually let me use the standard convention:
# For asymptotic freedom: alpha(mu) = alpha(M_Z) / [1 + b * alpha(M_Z) / (2 pi) * ln(mu/M_Z)]
# with b > 0 for AF.

def alpha_s_at(mu):
    """Run alpha_s from M_Z to mu using 1-loop QCD."""
    b_AF = 7.0  # QCD is AF, alpha_s decreases at higher mu
    return alpha_s_MZ / (1 + b_AF * alpha_s_MZ / (2*math.pi) * math.log(mu/M_Z_GeV))

def alpha_2_at(mu):
    """Run alpha_2 from M_Z to mu."""
    b_AF = 19/6  # SU(2) is AF (with SM fermion content)
    return alpha_2_MZ / (1 + b_AF * alpha_2_MZ / (2*math.pi) * math.log(mu/M_Z_GeV))

def alpha_Y_at(mu):
    """Run alpha_Y from M_Z to mu (non-AF; grows to UV)."""
    b_NAF = 41/10  # U(1) hypercharge, not AF
    return alpha_Y_MZ / (1 - b_NAF * alpha_Y_MZ / (2*math.pi) * math.log(mu/M_Z_GeV))

# =============================================================================
# Candidate scales
# =============================================================================
H_inf_GeV = 1e13
M_Z_GeV_val = 91.2
m_t_GeV = 173.0
Lambda_QCD_GeV = 0.3
M_Pl_GeV = 1.221e19

# Thermal mass: m_thermal ~ H_inf * sqrt(alpha) at T_GH = H_inf/(2 pi)
# alpha_s(H_inf) ~ 0.027, so m_thermal ~ H_inf * 0.16 ~ 1.6e12 GeV
# This is just an estimate.
m_thermal_GeV = H_inf_GeV * math.sqrt(0.027)

scales = [
    ("Lambda_QCD", Lambda_QCD_GeV, "IR confinement; non-perturbative"),
    ("M_Z", M_Z_GeV_val, "EW matching; all SM active above this"),
    ("m_top", m_t_GeV, "heaviest SM mass; decoupling"),
    ("1 TeV", 1000.0, "EW-scale but above top"),
    ("10 TeV", 10000.0, "trans-EW"),
    ("m_thermal", m_thermal_GeV, "Gibbons-Hawking thermal mass"),
    ("H_inf", H_inf_GeV, "curvature scale; standard HV choice"),
    ("M_GUT", 1e16, "GUT scale"),
    ("M_Planck", M_Pl_GeV, "UV boundary"),
]

# =============================================================================
# eps and Omega_L at each candidate scale
# =============================================================================
S_CTP = 108 * math.pi
tau_0_s = 41.9e6 * 3.156e7
H_0_Hz = 70 * 1e3 / 3.0857e22
Planck_OL = 0.6889

def epsilon_combined_at(mu):
    """Compute eps_combined at scale mu using A * g^4 weighting."""
    a_s = alpha_s_at(mu)
    a_2 = alpha_2_at(mu)
    a_Y = alpha_Y_at(mu)
    # eps_i = 1 + (1/3)(29 C_i - 12 R_psi_i - 5/2 R_phi_i) × alpha_i/(4 pi)
    eps_SU3 = 1 + (1/3) * (29*3 - 12*3 - 0) * a_s / (4*math.pi)
    eps_SU2 = 1 + (1/3) * (29*2 - 12*3 - 2.5) * a_2 / (4*math.pi)
    eps_U1  = 1 + (1/3) * (0 - 12*10 - 1.25) * a_Y / (4*math.pi)
    # A × g^4 weighting
    w3 = 8 * a_s**2
    w2 = 3 * a_2**2
    w1 = 1 * a_Y**2
    W = w3 + w2 + w1
    return (w3*eps_SU3 + w2*eps_SU2 + w1*eps_U1) / W, (a_s, a_2, a_Y, eps_SU3, eps_SU2, eps_U1)

def omega_lambda(R):
    H_inf = (2 - R) / (S_CTP * tau_0_s)
    return (H_inf / H_0_Hz)**2

# =============================================================================
# Run scan
# =============================================================================
print("=" * 90)
print("R3 — Scale selection scan: eps and Omega_L at each candidate scale")
print("=" * 90)
print()
print(f"{'Scale':<12} {'mu [GeV]':>10} {'alpha_s':>9} {'eps_SU3':>9} "
      f"{'eps_comb':>9} {'Omega_L':>9} {'vs Planck':>10}")
print("-" * 90)

for name, mu, desc in scales:
    try:
        eps_comb, (a_s, a_2, a_Y, e3, e2, e1) = epsilon_combined_at(mu)
        OL = omega_lambda(eps_comb)
        dev = (OL / Planck_OL - 1) * 100
        flag = " ← PLANCK" if abs(dev) < 1.0 else ""
        print(f"{name:<12} {mu:>10.2g} {a_s:>9.4f} {e3:>9.4f} "
              f"{eps_comb:>9.4f} {OL:>9.4f} {dev:>+9.2f}%{flag}")
    except (ValueError, ZeroDivisionError) as e:
        print(f"{name:<12} {mu:>10.2g} (calculation breaks down: {e})")

# =============================================================================
# Interpretation
# =============================================================================
print()
print("=" * 90)
print("Interpretation")
print("=" * 90)
print("""
  The Planck match (< 1% deviation from Omega_L = 0.6889) occurs
  SPECIFICALLY in the M_Z - m_top window. NO other candidate scale
  reproduces observations.

  * Lambda_QCD: non-perturbative (alpha_s diverges)
  * M_Z (91 GeV):  eps ~ 1.155, Omega_L ~ 0.69 → MATCHES
  * m_top (173 GeV): eps ~ 1.145, Omega_L ~ 0.71 → close (+3%)
  * 1 TeV: eps ~ 1.12, Omega_L ~ 0.75 → misses (+9%)
  * H_inf (10^13): eps ~ 1.03, Omega_L ~ 0.90 → misses (+30%)
  * M_Planck: eps ~ 1.02, Omega_L ~ 0.91 → misses (+32%)

  Standard Hu-Verdaguer / Buchbinder prescription: mu = H (curvature
  scale) to avoid large curvature logs. This gives Omega_L ~ 0.90.
  NOT consistent with Planck.

  For R_GRUT = eps to work, GRUT needs a mechanism that selects the
  EW scale (not H_inf or M_Planck) as the evaluation scale.
""")

# =============================================================================
# Why the standard scale-selection gives H_inf
# =============================================================================
print("Standard HV/Buchbinder rationale for mu = H_inf:")
print("-" * 90)
print("""
  On curved space with characteristic curvature scale H_inf, the
  effective action has terms like alpha(mu) × ln(H_inf^2/mu^2) × (curvature
  invariants). Choosing mu = H_inf eliminates the log and makes the
  perturbative expansion well-behaved.

  Choosing mu = M_Z introduces large logarithms ln(H_inf/M_Z)^2 ~ (21.5)^2
  ~ 460, which would need to be resummed to all orders — i.e., the
  "naive" M_Z evaluation is NOT the renormalized effective action in
  standard perturbation theory.

  This suggests: either (a) the CTP source doubling mechanism picks
  out a different scale via its specific structure, or (b) the
  identification R_GRUT = eps requires a re-derivation of the scale
  selection beyond standard dS perturbation theory.

  Option (a): worth exploring. The CTP forward/backward asymmetry
  might get its dominant contribution from scales where matter-thermal
  interactions are maximal (m ~ T_GH), which would pick a specific
  scale — but T_GH >> M_Z, so this doesn't give M_Z either.

  Option (b): the CTP doubling mechanism from Step 5 involves
  integrating out matter loops to generate (g_+ - g_-). If we view this
  integration as a MATCHING at the scale where SM is 'complete as an
  EFT' (= M_Z), we naturally use alpha(M_Z). But this matching
  interpretation is NOT the same as standard RG-improved effective
  action on dS.

  This is the crux of R3. The M_Z selection would need either:
     (b1) A matching argument at the EW scale that survives RG running
          up to H_inf, OR
     (b2) A novel CTP-specific selection mechanism.

  Neither is standard. Either would be a genuine physics novelty
  that the GRUT framework would need to justify.
""")

print("=" * 90)
print("R3 Honest Assessment")
print("=" * 90)
print("""
  The Planck-matching scale (M_Z) is NOT the standard HV/Buchbinder
  choice for dS effective actions. Standard practice selects mu = H_inf.

  Under standard practice: Omega_L = 0.90 (fails Planck by 30%).
  Under M_Z evaluation: Omega_L = 0.69 (matches Planck at 0.04%).

  THE IDENTIFICATION R_GRUT = eps REQUIRES A NON-STANDARD SCALE SELECTION.

  Three paths forward:
    (i)  Accept that standard dS perturbation theory gives H_inf
         and the identification fails.
    (ii) Find a specific CTP-doubling argument that selects M_Z.
    (iii) Argue that the eps_combined prediction is RG-invariant
         (not true at 1-loop as we showed; ε(mu) varies strongly).

  This is honestly the hardest piece of the derivation.
""")
