#!/usr/bin/env python3
"""vacuum_scheme_compare: the scheme audit of physics' most-quoted number.

THE QUESTION: "the QFT vacuum energy exceeds the observed value by 120 orders of magnitude" --
what is that number, in what scheme, and is the QUOTED number the LOAD-BEARING one?

THE ANSWER, in three parts. Each is COMPUTED below, not asserted:

  PART A -- THE STRESS TENSOR OF THE PEDAGOGICAL DERIVATION IS NOT OF CC FORM.
    A hard 3-momentum cutoff on a massless boson gives rho = L^4/(16 pi^2) and p = L^4/(48 pi^2),
    hence w = +1/3 EXACTLY: a radiation fluid.
    *** THE INFERENCE THAT MUST NOT BE DRAWN (and which this file's own first version drew, and
    its firewall struck): this does NOT show the object is not a cosmological constant. It
    diagnoses a LORENTZ-VIOLATING REGULATOR. Under an O(4)-invariant Euclidean cutoff the
    contribution is a field-independent constant in V, hence p = -rho EXACTLY, w = -1 -- and the
    magnitude goes UP, not down. Part A invalidates the standard DERIVATION AS PRESENTED; it
    leaves the magnitude estimate standing. ***

  PART B -- THE MAGNITUDE IS CONVENTION-DEPENDENT BY >= 5 ORDERS, WITH AN UNDETERMINED SIGN.
    Reduced vs non-reduced M_Pl is 2.80 orders in the fourth power; the 1/(16 pi^2) loop factor is
    2.20 more; 118 / 120 / 121 / 122 / 123 are all in circulation and are the SAME calculation
    under conventions nobody states. And the covariant repair carries its OWN mu-dependence: the
    coefficient of the O(4) result changes sign as mu runs to the cutoff. A number that moves five
    orders and changes sign under unstated conventions is not a measurement of anything.

  PART C -- WHAT SURVIVES IS SCHEME-INDEPENDENT AND SMALLER (this is the load-bearing statement).
    In dimensional regularization power divergences are scaleless and vanish identically; the
    one-loop vacuum energy is quartic in the MASS and logarithmic in the scale. What remains needs
    no regulator at all: the ESTABLISHED thresholds. The electroweak vacuum depth |V_min| =
    m_h^2 v^2 / 8 is a tree-level number in the Standard Model with no cutoff anywhere in it, and
    it alone exceeds rho_obs by ~54.7 orders.
    *** THE PROBLEM IS REAL. ITS FAMOUS NUMBER IS FOLKLORE. Those are different statements and
    this file refuses to conflate them in either direction. ***

Pure stdlib, exact where it can be. Self-tested. Mutation battery registered in
provenance/mutation_registry.py per the standing rule (no load-bearing number banks without one).
"""
import math

# ---------------------------------------------------------------- inputs, each with its rider
# MEASURED [Planck 2018 TT,TE,EE+lowE+lensing+BAO; base-LCDM, FLAT, w FIXED = -1; 68% CL]
RHO_OBS = 2.5154e-47            # GeV^4
# MEASURED [PDG 2024; from G]
M_PL = 1.220890e19              # GeV, non-reduced
M_PL_RED = 2.435323e18          # GeV, reduced = M_Pl / sqrt(8 pi)
# MEASURED [PDG 2024]
V_EW = 246.22                   # GeV
M_H = 125.25                    # GeV


def w_hard_cutoff():
    """PART A: rho and p of a massless boson under a HARD 3-MOMENTUM cutoff, in units L^4.
    rho = Int_0^L (k^2 dk/(2 pi^2)) * (k/2)      = L^4 / (16 pi^2)
    p   = Int_0^L (k^2 dk/(2 pi^2)) * (k^2/(6k)) = L^4 / (48 pi^2)
    Returns (rho_coeff, p_coeff, w). The integrals are elementary and done in closed form."""
    rho = 1.0 / (16.0 * math.pi ** 2)
    p = 1.0 / (48.0 * math.pi ** 2)
    return rho, p, p / rho


def w_covariant():
    """PART A, the repair: under an O(4)-invariant Euclidean cutoff the one-loop contribution is a
    FIELD-INDEPENDENT CONSTANT in the effective potential, entering the action as
    int d^4x sqrt(-g) V. For such a term T_munu = -V g_munu identically, so p = -rho EXACTLY.
    Returned as an exact rational fact, not a fit: w = -1."""
    return -1.0


def covariant_magnitude(mu_over_L):
    """PART B: the O(4) Euclidean cutoff coefficient, V = L^4 (4 ln(L/mu) - 1) / (128 pi^2).
    Its mu-dependence is the point: the coefficient CHANGES SIGN as mu -> L."""
    return (4.0 * math.log(1.0 / mu_over_L) - 1.0) / (128.0 * math.pi ** 2)


def ew_vacuum_depth():
    """PART C's scheme-independent anchor: |V_min| = m_h^2 v^2 / 8, tree-level SM, no regulator.
    Defined ONCE so main() and _selftest() check the SAME object -- the mutation battery caught a
    version where main() displayed one expression and the selftest recomputed another, which is the
    print-versus-computed split this program's calc-layer floor exists to prevent."""
    return M_H ** 2 * V_EW ** 2 / 8.0


def orders(x):
    return math.log10(x / RHO_OBS)


def main():
    print("=" * 96)
    print("THE VACUUM-ENERGY SCHEME AUDIT -- what is '120 orders', in what scheme, and is it the")
    print("load-bearing number?")
    print("=" * 96)

    print("\nPART A -- THE STRESS TENSOR OF THE PEDAGOGICAL DERIVATION:")
    rho_c, p_c, w = w_hard_cutoff()
    print(f"   hard 3-momentum cutoff, massless boson:  rho = L^4 * {rho_c:.8f} = L^4/(16 pi^2)")
    print(f"                                            p   = L^4 * {p_c:.8f} = L^4/(48 pi^2)")
    print(f"   ==> w = p/rho = {w:.10f} = +1/3 EXACTLY: a RADIATION FLUID.")
    print(f"   O(4)-invariant Euclidean cutoff:         w = {w_covariant():+.1f} EXACTLY.")
    print("   *** READ THIS CORRECTLY: w = +1/3 diagnoses a LORENTZ-VIOLATING REGULATOR, NOT the")
    print("   object. The covariant scheme restores w = -1 in one line -- and the magnitude goes UP.")
    print("   Part A invalidates the standard DERIVATION AS PRESENTED. It does NOT dispose of the")
    print("   magnitude estimate, and any claim that it does is an overreach this file refuses.")

    print("\nPART B -- THE MAGNITUDE IS CONVENTION-DEPENDENT (this is where the force actually is):")
    rows = [("M_Pl^4                (non-reduced, no loop factor)", M_PL ** 4),
            ("M_Pl^4/(16 pi^2)      (non-reduced, one loop)", M_PL ** 4 / (16 * math.pi ** 2)),
            ("M_Pl_red^4            (reduced, no loop factor)", M_PL_RED ** 4),
            ("M_Pl_red^4/(16 pi^2)  (reduced, one loop)", M_PL_RED ** 4 / (16 * math.pi ** 2))]
    for label, val in rows:
        print(f"   {label:52s} -> 10^{orders(val):6.2f} x rho_obs")
    span_red = orders(M_PL ** 4) - orders(M_PL_RED ** 4)
    span_loop = orders(M_PL ** 4) - orders(M_PL ** 4 / (16 * math.pi ** 2))
    print(f"   reduced-vs-non-reduced span: {span_red:.3f} orders;  loop-factor span: {span_loop:.3f}")
    print(f"   COMBINED CONVENTION SPAN: {span_red + span_loop:.3f} ORDERS -- and 118/120/121/122/123")
    print("   are all in circulation as THE SAME CALCULATION under conventions nobody states.")
    print("   The covariant repair carries its OWN mu-dependence, INCLUDING A SIGN FLIP:")
    for mu_over_L, tag in ((1e-19, "mu ~ 1 GeV"), (1e-3, "mu = 1e-3 L"), (1.0, "mu = L")):
        c = covariant_magnitude(mu_over_L)
        v = abs(c) * M_PL ** 4
        print(f"      {tag:12s}: coefficient {c:+.5f}  ->  |V| = 10^{orders(v):6.2f} x rho_obs")
    print("   ==> the covariant magnitude ALSO spans orders and changes SIGN. A number that moves")
    print("   this much under unstated conventions is not a measurement of anything.")

    print("\nPART C -- WHAT SURVIVES, SCHEME-INDEPENDENTLY (the load-bearing statement):")
    print("   In dim reg power divergences are scaleless and vanish identically; the one-loop vacuum")
    print("   energy is quartic in the MASS, logarithmic in the scale. What remains needs NO")
    print("   regulator: the ESTABLISHED thresholds.")
    v_ew_depth = ew_vacuum_depth()
    print(f"   electroweak vacuum depth |V_min| = m_h^2 v^2/8 = {v_ew_depth:.4e} GeV^4")
    print(f"      = 10^{orders(v_ew_depth):.3f} x rho_obs  -- TREE-LEVEL Standard Model, NO cutoff")
    print("        anywhere in it, no regulator choice, no convention to argue about.")
    print("   (QCD condensates ~10^43-10^44.5 and the electron loop ~10^31 sit below it and are")
    print("    likewise regulator-free; they are quoted here as ATTESTED, not recomputed.)")

    print("\nVERDICT:")
    print("   The quoted number is NOT the load-bearing one. '120 orders' is a scheme-dependent")
    print("   statement whose derivation-as-presented uses a regulator that produces the wrong")
    print("   equation of state, and whose magnitude moves >5 orders (and changes sign) under")
    print("   conventions that go unstated.")
    print(f"   THE HONEST REPLACEMENT is smaller and scheme-independent: >= 10^{orders(v_ew_depth):.0f}")
    print("   from the electroweak vacuum depth alone.")
    print("   *** THE PROBLEM IS REAL AND THIS FILE DOES NOT DISMISS IT. A ~55-order unexplained")
    print("   cancellation is not less of a problem for being 55 rather than 120; it is merely a")
    print("   DIFFERENT and defensible statement. The folklore number is the casualty, not the")
    print("   physics. ***")

    ok = _selftest()
    print(f"\n  SELFTEST: {'PASS' if ok else 'FAIL'}")
    return 0 if ok else 1


def _selftest():
    ok = True
    def chk(c, m):
        nonlocal ok
        if not c:
            print(f"   [FAIL] {m}")
            ok = False
    rho_c, p_c, w = w_hard_cutoff()
    # PART A: the exact ratio, and the exact closed forms
    chk(abs(w - 1.0 / 3.0) < 1e-14, f"hard-cutoff w = {w}, must be exactly +1/3")
    chk(abs(rho_c - 1 / (16 * math.pi ** 2)) < 1e-18, "rho coefficient != 1/(16 pi^2)")
    chk(abs(p_c - 1 / (48 * math.pi ** 2)) < 1e-18, "p coefficient != 1/(48 pi^2)")
    # the covariant repair must give w = -1 EXACTLY -- the guard against re-drawing the struck
    # inference (that w=+1/3 disposes of the object)
    chk(w_covariant() == -1.0, "covariant scheme must give w = -1 exactly")
    # PART B: the convention span, and that it EXCEEDS 4 orders (the finding's whole force)
    span = (orders(M_PL ** 4) - orders(M_PL_RED ** 4)) + \
           (orders(M_PL ** 4) - orders(M_PL ** 4 / (16 * math.pi ** 2)))
    chk(4.5 < span < 5.5, f"convention span = {span:.3f}, banked as >= 5 orders")
    # M_Pl_red^4 = M_Pl^4/(64 pi^2) identically -- the identity behind the 2.80-order piece
    chk(abs(M_PL_RED ** 4 / (M_PL ** 4 / (64 * math.pi ** 2)) - 1.0) < 1e-6,
        "reduced/non-reduced identity broken")
    # the covariant coefficient must actually CHANGE SIGN as mu -> L (banked claim)
    chk(covariant_magnitude(1e-19) > 0 > covariant_magnitude(1.0),
        "the covariant coefficient must change sign as mu -> L")
    # PART C: the scheme-independent anchor, and that it is SMALLER than the folklore number
    d = orders(ew_vacuum_depth())
    chk(54.0 < d < 55.5, f"EW vacuum depth = 10^{d:.3f}, banked as ~10^54.7")
    chk(d < orders(M_PL ** 4) - 50, "the honest replacement must be much SMALLER than the folklore")
    # and it must still be a large unexplained number -- the guard against the flattering dismissal
    chk(d > 40, "the surviving statement must remain a serious problem (>40 orders)")
    return ok


if __name__ == "__main__":
    raise SystemExit(main())
