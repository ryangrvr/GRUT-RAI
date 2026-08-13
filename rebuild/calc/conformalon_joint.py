#!/usr/bin/env python3
"""JOINT CONFORMALON CALCULATION: can ONE mode (the trace-anomaly conformalon) do BOTH jobs --
keep the alpha leg (rung 9) anchored AND supply the cosmological relaxation tau2 ~ 1/H for w(z)
(rung 7) -- with one anomaly-fixed coupling?

The conformalon sigma (metric g = e^{2sigma} ghat) has a 4th-order Paneitz kinetic term with
coefficient Q^2 = -2 b' FIXED by field content, and Liouville self-interactions e^{4 sigma}.
Its IR fluctuation strength is one number:
        eps  ==  <sigma^2>  ~  1/Q^2  x  (de Sitter factor)
and BOTH effects ride on it:
    alpha-shift:   d(alpha)/alpha  =  k_alpha * eps        (conformalon fluctuation shifts the anomaly coeff)
    w-deviation:   1 + w           =  k_w     * eps        (conformalon stress departs from pure Lambda)
So the unification is quantitative: one eps, two effects. The test is whether a single eps
(one Q^2) satisfies BOTH the alpha bound AND the DESI w-deviation -- i.e. the prefactor ratio
k_w/k_alpha, and the SIGN/shape of the lag-driven w(z).

The k's and the de Sitter gap m_eff(Q^2) are the conformalon-specific inputs the anomaly action
must supply (literature/specialist-pending); here we expose the CONSTRAINT STRUCTURE and the
lag sign, which decide whether the connection is real or a mirage. Units H0=1. Pure stdlib.
"""
import math

OM, OL = 0.31, 0.69          # LCDM background


def E2(z):                   # (H/H0)^2
    return OM * (1 + z) ** 3 + OL


def main():
    print("=" * 80)
    print("JOINT CONFORMALON  --  one anomaly-fixed number for BOTH alpha (rung 9) and w(z) (rung 7)?")
    print("=" * 80)

    # ---- Part 1: the compatibility constraint (the sharp pass/fail) -------------------
    print("""
PART 1 -- COMPATIBILITY CONSTRAINT (one eps must satisfy both):
  alpha 'held twice' => d(alpha)/alpha <~ 0.03 (a few percent) => eps <~ 0.03/k_alpha
  DESI hint          => 1+w0 ~ 0.2                              => eps_now ~ 0.2/k_w
  Both from the SAME eps => need 0.2/k_w <= 0.03/k_alpha  =>  k_w/k_alpha >= 6.7
""")
    dalpha_max, w_dev = 0.03, 0.2
    ratio_needed = (w_dev / dalpha_max)
    print(f"  REQUIRED prefactor ratio  k_w/k_alpha >= {ratio_needed:.1f}")
    print("  => The unification WORKS iff the conformalon couples ~7x more strongly to the")
    print("     cosmological stress than to the anomaly-coefficient shift. That is a single,")
    print("     checkable number from the anomaly action -- not an assumption, a calculation.")
    print("  Interpretation: alpha responds to UV/horizon-scale <sigma^2>, w to the superhorizon")
    print("  IR fluctuation; these are DIFFERENT moments of the same field, so k_w != k_alpha is")
    print("  expected and the ratio is the whole ballgame.")

    # ---- Part 2: the lag-driven w(z) and its SIGN ------------------------------------
    print("\n" + "-" * 80)
    print("PART 2 -- LAG-DRIVEN w(z):  perfect tracking gives constant w, so evolution = the LAG")
    print("  m_eff^2 relaxes toward c*H^2 (de Sitter dynamical gap) with rate m^2/(3H^2) per e-fold:")
    print("     d(m^2)/dN = -(m^2/3H^2)(m^2 - c H^2),   eps(z) = H^2/m^2,   1+w = k_w*eps")
    print("-" * 80)
    c = 3.0          # de Sitter gap: m_eff^2 ~ c H^2 (c=3 => tau2 = 3H/m^2 = 1/H at equilibrium)
    k_w = 1.0        # normalize k_w=1 for shape; magnitude rescales w-deviation

    # integrate from high z (equilibrium) down to z=0 in e-folds N=ln a
    N0, N1, steps = -2.2, 0.0, 20000          # z ~ 8 down to 0
    dN = (N1 - N0) / steps
    def Hsq(N):  # (H/H0)^2 at e-fold N (a=e^N, z=e^-N - 1)
        a = math.exp(N); z = 1 / a - 1
        return E2(z)
    m2 = c * Hsq(N0)                          # start in equilibrium
    Ns, m2s = [N0], [m2]
    for i in range(steps):
        N = N0 + i * dN
        H2 = Hsq(N)
        dm2 = -(m2 / (3 * H2)) * (m2 - c * H2)
        m2 += dm2 * dN
        Ns.append(N + dN); m2s.append(m2)

    def eps_of_z(z):
        N = math.log(1 / (1 + z))
        # nearest grid point
        idx = min(range(len(Ns)), key=lambda i: abs(Ns[i] - N))
        return Hsq(N) / m2s[idx]

    print("      z      H^2/H0^2    m_eff^2/H0^2    eps=H^2/m^2    1+w (=k_w*eps, k_w=1)")
    for z in (3.0, 2.0, 1.0, 0.5, 0.0):
        e = eps_of_z(z)
        print(f"   {z:5.2f}    {E2(z):9.3f}    {0 if False else (E2(z)/e):11.3f}    {e:10.4f}    {k_w*e:10.4f}")

    # effective (w0, wa)
    e0 = eps_of_z(0.0); h = 1e-3
    w0 = -1 + k_w * e0
    dwdz = k_w * (eps_of_z(h) - eps_of_z(0.0)) / h
    wa = dwdz   # CPL: dw/dz|0 = wa
    print(f"\n  effective (shape):  w0 = -1 + {k_w*e0:.4f}*({k_w:.0f})  ->  w0 ~ {w0:.4f}")
    print(f"                      wa (= dw/dz|0) ~ {wa:+.4f}")
    desi_match = "MATCHES DESI sign (w0>-1, wa<0)" if (w0 > -1 and wa < 0) else \
                 "does NOT match DESI sign (DESI wants w0>-1, wa<0)"
    print(f"  => {desi_match}")

    print("\n" + "=" * 80)
    print("VERDICT  (lead; forward)")
    print("=" * 80)
    print(f"""\
  UNIFICATION STRUCTURE (solid): one anomaly-fixed number Q^2 (= field content) sets the
  conformalon IR fluctuation eps, and BOTH the alpha-shift and the w-deviation ride on eps. So
  rung 9 and rung 7 are governed by ONE object -- the most economical thing the program has
  produced. The conformalon is converted from a threat (de-anchors alpha) into a feature (its
  de Sitter gap m_eff ~ H both keeps it from being a free massless IR mode AND sets tau2 ~ 1/H).

  THE TWO THINGS THAT DECIDE IT (both sharp, both computable from the anomaly action):
   (1) PREFACTOR RATIO: the unification is viable iff k_w/k_alpha >= {ratio_needed:.0f}. This is a
       single number -- the ratio of the conformalon's coupling to the cosmological stress vs to
       the anomaly coefficient. Compute it from the Antoniadis-Mottola action: if >= {ratio_needed:.0f},
       one Q^2 does both; if < {ratio_needed:.0f}, alpha and DESI-w are incompatible and the connection
       is a mirage -- cleanly.
   (2) LAG SIGN: this toy lag gives wa {('<0 (DESI-like!)' if wa<0 else '>0 (wrong sign, as the simple relaxor did)')}.
       {'If this survives the real conformalon stress tensor, GRUT PREDICTS a w(z) shape from one coupling.' if wa<0 else 'The conformalon stress sign must be computed properly; the naive lag does not yet give the DESI sign.'}

  WHAT IS STILL ASSUMED / PENDING (marked): k_alpha, k_w, and the gap coefficient c=m_eff^2/H^2 are
  conformalon-specific numbers from the 4th-order Paneitz/Liouville de Sitter dynamics -- the hard
  literature piece (Antoniadis-Mazur-Mottola). This calc fixes the CONSTRAINT STRUCTURE and the
  question; the numbers come from the action.

  NEXT CONCRETE STEP: compute k_w/k_alpha and the conformalon stress sign from the anomaly-induced
  action in de Sitter. Two numbers decide whether two open rungs collapse into one.

  ONE-LINE QUESTION FOR THE SPECIALIST:
    'For the anomaly-induced conformal factor in de Sitter, is the ratio of its coupling to the
     cosmological (stress) sector vs to the running of the a-anomaly coefficient >~ 7 -- and does
     its stress tensor give 1+w that DECREASES with redshift (wa<0) once m_eff lags H through the
     matter->dark-energy transition?'""")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
