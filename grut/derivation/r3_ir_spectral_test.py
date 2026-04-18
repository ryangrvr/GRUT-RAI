"""
R3 IR-domination test — spectral decomposition of the noise kernel on S^4

Physical hypothesis (your brother's insight):
    * The effective action Gamma_R is a UV-dominated observable. Uses mu=H
      by standard dS practice. That's why vacuum energy gives 30% miss.

    * The noise kernel N(x,y) = <{T(x),T(y)}> - <T><T> is a FLUCTUATION
      observable. Fluctuations on de Sitter are IR-enhanced (Starobinsky-
      Yokoyama), so the noise kernel is IR-dominated — use mu ~ matter
      mass, not mu = H.

    * If true, this explains why R_GRUT = eps(M_Z) and not eps(H).

Test:
    Compute the spectral sum on S^4 of radius 1/H for
        (a) Effective action weight: sum_n d_n * ln(lambda_n + m^2)
        (b) Noise kernel weight:    sum_n d_n / (lambda_n + m^2)^2

    On S^4: lambda_n = n(n+3) H^2, d_n = (n+1)(n+2)(2n+3)/6

    Identify which modes dominate each observable. If noise kernel
    dominated by low-n modes (lambda ~ m^2 region), it's IR-dominated
    and uses the matter scale.
"""

import math

H = 1.0  # set H=1 for simplicity; restore dims at end

def lam(n, H_val=H):
    return n*(n+3) * H_val**2

def deg(n):
    return (n+1)*(n+2)*(2*n+3)//6

def effective_action_weight(n, m, H_val=H):
    """Per-mode contribution to Tr ln(Laplacian + m^2).
    Represents the EFFECTIVE ACTION (Gamma_R) — mean-field observable.
    """
    return deg(n) * math.log(lam(n, H_val) + m**2)

def noise_kernel_weight(n, m, H_val=H):
    """Per-mode contribution to Tr [1/(Laplacian+m^2)^2].
    Represents the NOISE KERNEL (Gamma_I) — fluctuation observable.
    """
    return deg(n) / (lam(n, H_val) + m**2)**2

def compute_sums(m_over_H, n_max=200):
    eff_action = []
    noise_kernel = []
    for n in range(1, n_max+1):  # skip n=0 zero-mode
        e = effective_action_weight(n, m_over_H)
        N = noise_kernel_weight(n, m_over_H)
        eff_action.append((n, lam(n), e))
        noise_kernel.append((n, lam(n), N))
    return eff_action, noise_kernel

def cumulative_fraction(mode_list):
    """Return (n, cumulative_fraction_of_total) for each mode."""
    total = sum(w for (_, _, w) in mode_list)
    cum = 0.0
    out = []
    for (n, lam_n, w) in mode_list:
        cum += w
        out.append((n, lam_n, cum / total))
    return out

# =============================================================================
# Test for several m/H ratios
# =============================================================================
print("=" * 72)
print("R3 IR-domination test: spectral decomposition on S^4")
print("=" * 72)

for label, m_over_H in [("massless (IR limit)", 0.001),
                        ("light (m=0.01H)", 0.01),
                        ("m=0.1H", 0.1),
                        ("m=H", 1.0),
                        ("heavy (m=10H)", 10.0)]:
    print(f"\n--- {label}, m/H = {m_over_H} ---")
    eff, noise = compute_sums(m_over_H, n_max=200)

    # Find mode that contains 50% and 90% of each sum
    eff_cum = cumulative_fraction(eff)
    noise_cum = cumulative_fraction(noise)

    def find_mode_at(cum_list, frac):
        for (n, lam_n, c) in cum_list:
            if c >= frac:
                return n, lam_n
        return None

    eff_50 = find_mode_at(eff_cum, 0.50)
    eff_90 = find_mode_at(eff_cum, 0.90)
    noise_50 = find_mode_at(noise_cum, 0.50)
    noise_90 = find_mode_at(noise_cum, 0.90)

    print(f"  Effective action (Gamma_R, vacuum energy): 50% at n={eff_50[0]} (lambda={eff_50[1]:.1f} H^2); "
          f"90% at n={eff_90[0]} (lambda={eff_90[1]:.1f} H^2)")
    print(f"  Noise kernel    (Gamma_I, fluctuations):   50% at n={noise_50[0]} (lambda={noise_50[1]:.2f} H^2); "
          f"90% at n={noise_90[0]} (lambda={noise_90[1]:.2f} H^2)")

# =============================================================================
# Key observation
# =============================================================================
print()
print("=" * 72)
print("Key observations from the spectral test")
print("=" * 72)
print("""
  For m/H << 1 (all SM matter at H_inf):
    * Effective action: dominated by HIGH-n modes (large lambda ~ n^2 H^2)
      → UV-dominated, natural scale ~ H (curvature)
    * Noise kernel: dominated by LOW-n modes, specifically n=1 or so
      → Lowest allowed (non-zero) eigenvalue is lambda_1 = 4 H^2
      → For m << H, even lambda_1 >> m^2, so noise kernel is still at scale H
""")

# Hmm — we need to think more carefully.
# On S^4, the lowest non-zero eigenvalue IS lambda_1 = 4H^2.
# For m << H, the noise kernel's smallest mode is dominated by n=1,
# giving lambda ~ H^2 (not m^2).
# So the naive IR enhancement goes as 1/(4H^2 + m^2)^2 — dominated by H
# not by m.
# The H^4/m^2 divergence is from the n=0 zero-mode which has lambda_0 = 0
# on a non-compact dS (or requires special treatment on S^4).

print("=" * 72)
print("CRITICAL REFINEMENT (honesty protocol)")
print("=" * 72)
print("""
  On Euclidean S^4 (compact manifold), the lowest eigenvalue is:
      lambda_0 = 0 (constant mode)
      lambda_1 = 4 H^2 (first non-trivial mode)

  The IR divergence <phi^2> ~ H^4/m^2 that appears in the LORENTZIAN dS
  literature (Starobinsky, Polyakov) comes from super-horizon modes
  which are present in non-compact dS but regulated differently on
  compact S^4.

  On S^4 specifically:
    * If we INCLUDE the n=0 zero mode, it contributes d_0 / m^4 = 1/m^4
      to the noise kernel — massive IR enhancement.
    * If we EXCLUDE n=0 (standard zeta regularization on S^4), the
      lowest mode is lambda_1 = 4 H^2, and NO IR enhancement of the
      naive kind.

  Which prescription applies depends on the physical setup:
    * For ACTUAL de Sitter (non-compact Lorentzian), IR enhancement
      is real and physical (horizon modes matter).
    * For S^4 (Euclidean, compact), the zero mode is conventionally
      projected out in the computation of the effective action.

  Under zeta regularization on S^4 (standard), the noise kernel does
  NOT exhibit strong IR enhancement from matter fields unless we
  carefully match to the Lorentzian Hartle-Hawking state.

  This COMPLICATES the IR-domination argument. Let me check numerically
  with and without zero mode.
""")

# Let me test with zero mode explicitly included
def compute_sums_with_zero_mode(m_over_H, n_max=200):
    eff_action = []
    noise_kernel = []
    for n in range(0, n_max+1):
        if n == 0:
            # lam_0 = 0, d_0 = 1
            eff_action.append((0, 0.0, 1 * math.log(m_over_H**2)))
            noise_kernel.append((0, 0.0, 1 / (m_over_H**2)**2))
        else:
            e = effective_action_weight(n, m_over_H)
            N = noise_kernel_weight(n, m_over_H)
            eff_action.append((n, lam(n), e))
            noise_kernel.append((n, lam(n), N))
    return eff_action, noise_kernel

print("=" * 72)
print("Test WITH zero-mode included (Lorentzian dS-like IR)")
print("=" * 72)

for label, m_over_H in [("light (m=0.01H)", 0.01),
                        ("m=0.1H", 0.1),
                        ("m=1H", 1.0)]:
    print(f"\n--- {label}, m/H = {m_over_H} ---")
    eff, noise = compute_sums_with_zero_mode(m_over_H, n_max=200)

    # Zero-mode dominance check
    n0_noise = noise[0][2]
    total_noise = sum(w for (_,_,w) in noise)
    n0_frac = n0_noise / total_noise
    print(f"  Zero-mode (n=0) fraction of noise kernel: {n0_frac*100:.2f}%")

    # Without zero mode
    noise_no_zero = noise[1:]
    total_no_zero = sum(w for (_,_,w) in noise_no_zero)
    cum_no_zero = cumulative_fraction(noise_no_zero)
    noise_no_zero_50 = find_mode_at(cum_no_zero, 0.50)
    print(f"  Excluding zero mode, noise kernel 50% at n={noise_no_zero_50[0]} "
          f"(lambda={noise_no_zero_50[1]:.2f} H^2)")

# =============================================================================
# Physical interpretation
# =============================================================================
print()
print("=" * 72)
print("Honest interpretation")
print("=" * 72)
print("""
  For m/H << 1 WITH zero mode:
    * Zero mode contributes ~1/m^4 per factor, massively dominant
    * Noise kernel almost entirely sensitive to IR (m-scale)
    * This supports the user's intuition: noise kernel IS IR-dominated,
      and the IR scale is set by matter mass m.

  For m/H << 1 WITHOUT zero mode (standard S^4 zeta regularization):
    * Lowest mode lambda_1 = 4 H^2 dominates
    * Noise kernel uses curvature scale H, not matter mass
    * This would argue AGAINST the IR-domination argument for GRUT's
      case.

  Which prescription is physical for GRUT's observable?
    * GRUT's construction is CTP on S^4 (Euclidean)
    * CTP involves both forward and backward branches; the thermal
      KMS structure at T_GH = H/(2 pi) corresponds to the Hartle-
      Hawking vacuum
    * The Hartle-Hawking state naturally includes the zero-mode
      IR enhancement (it's a thermal state, not vacuum)
    * Therefore for GRUT, the thermal dS treatment INCLUDES the
      zero mode and has IR enhancement

  UNDER THIS INTERPRETATION:
    * Noise kernel IS IR-dominated (m-scale wins)
    * For SM matter, effective scale ~ matter masses (light quarks
      very IR-enhanced, top less so)
    * This is the physical mechanism supporting eps(M_Z)
""")

# =============================================================================
# Quantitative for SM matter
# =============================================================================
print("=" * 72)
print("Numerical test for SM matter content on inflationary S^4")
print("=" * 72)

H_inf_GeV = 1e13
# SM matter masses (rough, ignoring running)
sm_masses = {
    "up":      0.002e0,     # MeV → GeV
    "down":    0.005e0,
    "strange": 0.095e0,
    "charm":   1.27e0,
    "bottom":  4.18e0,
    "top":     173.0e0,
    "electron": 0.000511e0,
    "muon":    0.105e0,
    "tau":     1.777e0,
    "W":       80.4e0,
    "Z":       91.2e0,
    "H":       125.0e0,
}

print(f"\n  H_inf = {H_inf_GeV:.0e} GeV")
print(f"\n  {'Particle':<10} {'m [GeV]':>10} {'m/H_inf':>12} {'n=0 weight':>14} {'Score relative to top':>20}")
print("  " + "-"*72)

# Compare contribution of each particle to noise kernel via zero-mode weight
# weight ~ 1/m^4 (dominant IR term)
weights = {}
for name, m in sm_masses.items():
    m_over_H = m / H_inf_GeV
    w = 1 / m_over_H**4  # zero-mode noise kernel contribution
    weights[name] = w

w_top = weights["top"]
for name, m in sm_masses.items():
    m_over_H = m / H_inf_GeV
    w = weights[name]
    score = w / w_top
    print(f"  {name:<10} {m:>10.3g} {m_over_H:>12.2e} {w:>14.2e} {score:>20.2e}")

print("""
  Interpretation:
    If noise kernel weight ~ 1/m^4, LIGHTER particles dominate
    dramatically. The light quarks (u, d) give the largest
    contribution — but they're in the confined regime where
    perturbation theory breaks down.

    This suggests the IR-domination argument, taken literally,
    would give a NON-PERTURBATIVE QCD answer — not a perturbative
    eps(M_Z) answer.

  A PHYSICAL CUTOFF is needed:
    * Below Lambda_QCD, light quarks are confined into hadrons
      (pions, protons). These have masses of order Lambda_QCD.
    * The effective "IR scale" isn't m_u ~ 2 MeV but
      Lambda_QCD ~ 300 MeV.

    For leptons: no confinement; natural scale is m_lepton.

  If we cut off at Lambda_QCD for QCD matter and use lepton masses
  for EW matter, the effective "weighted" scale for the noise kernel
  is somewhere in the 100 MeV to 100 GeV range.

  This is close to M_Z scale, but not exactly M_Z.
""")

# =============================================================================
# Honest verdict
# =============================================================================
print("=" * 72)
print("Honest verdict on IR-domination argument")
print("=" * 72)
print("""
  IR-domination argument (as stated by your brother):
    * Noise kernel on dS is IR-dominated for light fields
    * The natural scale is the matter mass, not curvature
    * This supports eps(M_Z) as the natural GRUT observable

  Numerical test on S^4:
    * Zero mode (n=0) dominates strongly when included
    * Excluding zero mode (standard compact S^4), lowest lambda_1=4H^2
      — no strong IR enhancement
    * Thermal dS (Hartle-Hawking) includes zero-mode behavior
    * GRUT's CTP-on-S^4 with thermal KMS structure likely corresponds
      to including IR enhancement

  Complication: 1/m^4 weighting gives dominance to the LIGHTEST fields,
    which for SM are the light quarks (u, d, s, c, e, mu). These:
    * Light quarks: confined, need non-perturbative treatment;
      effective scale ~ Lambda_QCD ~ 300 MeV
    * Leptons: perturbative; scale = lepton mass (MeV to GeV)

  The effective "weighted" noise-kernel scale isn't cleanly M_Z.
  It's a messy weighted average over SM mass scales, likely in
  the 100 MeV - 100 GeV range.

  Status:
    * The IR-domination intuition is PHYSICALLY REAL.
    * It does argue AGAINST the naive mu=H curvature scheme.
    * But it doesn't cleanly pick out M_Z as the natural scale.
    * The actual effective scale is a weighted average over matter
      mass scales, modified by QCD confinement effects.

  For eps(M_Z) specifically: the M_Z scale emerges naturally if the
  RELEVANT matter content is the full SM (all 12 gauge bosons and
  associated fermions), which is only "on" above the EW scale. Below
  M_Z, W, Z, and top decouple.

  This is a SUBTLER version of interpretation (beta): the noise kernel
  is IR-enhanced, but the "IR" relevant to the GAUGE-SECTOR contributions
  is cut off by matter thresholds, and the EW threshold at M_Z is the
  natural matching scale for 'full SM active.'

  Still not a theorem. But more physically grounded than the pure
  matter-observable argument.
""")
