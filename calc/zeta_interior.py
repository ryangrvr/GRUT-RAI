#!/usr/bin/env python3
"""zeta_interior: the first exploration of the {shear, bulk} INTERIOR -- the region the p_tt
interrogation opened (register: the CHOSEN verdict in p_tt_ansatz.boundary_condition; the admissible
kernel family K = c2*P^TT + c0*P0s from eft_operator_basis).

THE QUESTION (default-BROKEN, both horns first-class): the banked mu_linear enumeration is two
ENDPOINTS -- TT-only (x=0, mu=1=LCDM) and trace-only (x=1, mu=4/3, excluded ~32sigma by the low-ell
ISW + separate-universe no-go). The INTERIOR 0 < x < 1 was never computed (calc/mu_linear.py raises
ValueError on it). WHAT IS ACTUALLY COMPUTED (framing corrected by the firewall): given ANY finite-
significance amplitude exclusion of the endpoint, a non-empty window is STRUCTURALLY GUARANTEED under
linear scaling (N(0)=0; a stronger bound SHRINKS the window -- a 32x stronger one gives x < 1/512 --
it can never EMPTY it), so non-emptiness is NOT the result. The first-class computed content is
(i) the window EDGE (x < 1/16 at 2sigma; mu-1 ceiling alpha/16) and (ii) the BINDING STRUCTURE (the
ISW anchor binds alone against the banked growth/lensing constraints). [CORRECTED 2026-08-03 by
calc/isw_exclusion.py: the anchor computed to ~2.0sigma cross-channel, Sigma-corrected (32 retired);
BINDING INVERSION -- lensing binds at x < ~0.59 (loose-upper, F-MAP fence); this first-pass record
stands as history.] What would move it: the
rigorous mu(c0)/slip computation shifting the edge materially, or a derivation forcing x=0 (the
interrogation showed none exists from the declared structure).

THE FAMILY (toy/scaling, stated precisely):
  x in [0,1] parameterizes the scalar-channel (bulk) admixture, normalized so x=1 reproduces the
  banked trace-only endpoint coupling. At LINEAR RESPONSE the scalar-channel contribution to the
  modified-Poisson sector is linear in the scalar coupling, so the leading-order interpolation is
      mu(x) = 1 + x*alpha,   alpha = 1/3 (the banked conformal coefficient; mu(1) = 4/3 exact).
  FENCE: the exact map x <-> c0 (the P0s modulus) inherits mu_linear's bookkeeping conventions and
  is NOT derived here; what IS exact is the two endpoints (banked) and the linearity of the leading
  order in the coupling. Admissibility of the scalar channel (KMS/passivity) is the operator-basis
  Part-D exhibit, not assumed here.

THE DATA (banked inputs ONLY -- no new external numbers):
  D1  The low-ell ISW exclusion of the trace-only endpoint: ~32sigma at x=1 (banked in mu_linear).
      The ISW test statistic is amplitude-over-error, so significance scales LINEARLY with the
      deviation amplitude at leading order: N_sigma(x) ~ 32*x.  FENCE: linear scaling is the
      leading-order reading of a chi^2-type amplitude test; the banked number is the anchor.
      ANCHOR-SOFTNESS FENCE: the window edge inherits O(1) uncertainty in BOTH directions from this
      linear reading -- endpoint-variance inflation (cosmic variance computed against the endpoint
      model's own excess low-ell power) would SHRINK the true window; a quadratic (auto-spectrum)
      response component would WIDEN it -- and the ~32sigma anchor is an in-house-DERIVED exclusion
      significance (sources isw_lowl caveat; calc/isw_exclusion.py LANDED 2026-08-03), not an in-repo computation; every number below is a
      linear rescaling of it.
  D2  The mu0-Sigma0 growth/lensing constraints banked in SIGNATURE_AUDIT (overseer-verified):
      mu0 = 0.05 +/- 0.22, Sigma0 = 0.009 +/- 0.045. CONVENTION: pure 2sigma width (2*err) is used
      throughout for comparability; central values dropped (the conservative direction for ISW-binds).
      For the Sigma comparison, Sigma-1 = (mu-1)/2 is EXACT in the inherited mu_linear bookkeeping
      (trace-only slip eta = 1/(1+alpha); verified 7/6 - 1 = (1/3)/2), not merely conservative.
      ROBUSTNESS: ISW binds for ANY slip in [1/mu, 1] -- even the most aggressive reading (eta=1,
      Sigma-1 = mu-1) leaves the Sigma bound ~4.3x weaker than the ceiling; the printed '9x' is the
      slip-dependent end of a 4-9x range. The full slip/Sigma(x) computation stays OWED.

WHAT THIS CALC DOES NOT DO: it does NOT demote mu_linear (that screen is open, separately); it does
NOT touch the TT channel (rung4's suppression stands); it does NOT rescue DESI (a bulk response is
one passive channel -- the no-crossing export rung7_w3 is untouched; any w(z) leg rides the ALREADY
BOOKED rung7 dials and is not recomputed here); it banks NO new ledger input (exploring the interior
of an admissible family named by the interrogation adds no dial -- x is the c0 modulus the basis
already carries; the CHOICE c0=0 is what p_tt_ansatz's +1 books).

Pure stdlib. Self-tested. Style of rung3_spectral_structure.py / u5u6_deformability.py.
"""

ALPHA = 1.0 / 3.0          # banked conformal coefficient (rung9a value; mu(1) = 1 + alpha = 4/3)
N_SIGMA_ENDPOINT = 32.0    # banked ISW exclusion significance at the trace-only endpoint x=1
MU0_ERR = 0.22             # banked: mu0 = 0.05 +/- 0.22  (SIGNATURE_AUDIT, overseer-verified)
SIG0_ERR = 0.045           # banked: Sigma0 = 0.009 +/- 0.045


def mu(x):
    """Leading-order interpolation across the admissible family; endpoints banked-exact."""
    return 1.0 + x * ALPHA

def isw_sigma(x):
    """ISW exclusion significance at admixture x (linear amplitude scaling off the banked anchor)."""
    return N_SIGMA_ENDPOINT * x

def window_x(n_sigma=2.0):
    """The ISW-allowed admixture window at the given confidence: x < n_sigma/32."""
    return n_sigma / N_SIGMA_ENDPOINT

def mu_ceiling(n_sigma=2.0):
    """The viable window's ceiling in mu-1."""
    return window_x(n_sigma) * ALPHA


def main():
    print("=" * 94)
    print("THE {SHEAR, BULK} INTERIOR -- first pass (default-BROKEN; both horns first-class)")
    print("=" * 94)

    print("\nPART A -- the family (endpoints banked-exact, interior linear at leading order):")
    print("   x      mu(x)      ISW N_sigma(x)   status")
    for x in (0.0, 0.01, 0.03125, 0.0625, 0.125, 0.25, 0.5, 1.0):
        ns = isw_sigma(x)
        status = "LCDM endpoint (banked)" if x == 0 else (
                 "EXCLUDED endpoint (banked ~32sigma)" if x == 1.0 else (
                 "allowed (<2sigma)" if ns < 2.0 else ("edge (2sigma)" if abs(ns - 2.0) < 1e-12 else "excluded (>2sigma)")))
        print(f"   {x:<9.5g}{mu(x):<11.5f}{ns:<17.2f}{status}")

    print("PART B -- the window (the load-bearing arithmetic):")
    x2 = window_x(2.0)
    print(f"   ISW-allowed window at 2sigma:  x < {x2:.5f}  (= 2/32 = 1/16)")
    print(f"   => mu - 1 ceiling: {mu_ceiling(2.0):.5f}  (= alpha/16 ~ 0.0208)")
    print(f"   Cross-checks against the OTHER banked constraints (which must be weaker, or ISW isn't")
    print(f"   the binding bound): mu0 growth bound (2sigma): |mu-1| < {2*MU0_ERR:.2f}  -> weaker by "
          f"{2*MU0_ERR/mu_ceiling(2.0):.0f}x")
    print(f"   Sigma0 lensing (2sigma, conservative Sigma-1~(mu-1)/2): |mu-1| < {2*SIG0_ERR*2:.2f}  -> "
          f"weaker by {2*SIG0_ERR*2/mu_ceiling(2.0):.0f}x")
    print("   => the ISW anchor BINDS; the window is set by it alone at current data.")

    print("\nPART C -- the verdict (framing per the firewall correction):")
    print("   NON-EMPTINESS WAS STRUCTURALLY GUARANTEED (N(0)=0 + linear scaling: no finite bound can")
    print("   empty the window; a 32x stronger bound gives x < 1/512, still non-empty). It is NOT the")
    print("   result. THE COMPUTED CONTENT: (i) the window EDGE -- x < 1/16 at 2sigma, mu-1 ceiling")
    print("   alpha/16 ~ 0.021; (ii) the ISW anchor BINDS ALONE (growth ~21x, lensing 4-9x weaker).")
    print("   [CORRECTED 2026-08-03, calc/isw_exclusion.py: anchor computed ~2.0sigma (32 RETIRED);")
    print("    binding INVERTED -- DESI Sigma0 lensing binds at x < ~0.59; these first-pass numbers")
    print("    stand as the historical record only.]")
    print("   GRUT's family, for the first time, has a region whose observables are ALLOWED UP TO the")
    print("   percent level -- at the edge of current low-ell ISW sensitivity -- rather than 20+")
    print("   orders below any measurement (a contrast of CEILINGS with the c0=0 branch; the family")
    print("   ALLOWS, it does not predict -- x has no lower observable floor).")

    print("\nPART D -- honest scale-reading of the window ceiling (no new external numbers):")
    print("   - The ceiling mu-1 ~ 0.021 sits ~10x below the current growth-survey sensitivity")
    print("     (banked sigma(mu0)=0.22) -- so the interior is NOT yet probed by growth data;")
    print("     the ISW cross-correlation that anchors the window is the live discriminator, and")
    print("     anything near the ceiling is at the edge of improved low-ell cross-correlations")
    print("     (whether future growth surveys reach sigma(mu0)~0.02 is an EXTERNAL number, owed,")
    print("     not asserted here).")
    print("   - COHERENCE NOTE (u5/rung9a-facing, NOT a claim): the interrogation located alpha's")
    print("     legitimate linear-response carrier in the SCALAR channel -- exactly the channel the")
    print("     interior opens. An alpha-normalized scalar coupling (x set by alpha rather than free)")
    print("     would be the natural GRUT-motivated point of the family: x=alpha -> N_sigma ~ 10.7,")
    print("     EXCLUDED; x=alpha^2 ~ 0.11 -> N_sigma ~ 3.6 nominal (within the anchor fence's O(1)")
    print("     band, but disfavored). For scale: the 2sigma window edge is x = alpha/16 in alpha")
    print("     units -- a DATA-derived factor, not an alpha-normalization.")
    print("     No normalization is banked -- this maps where GRUT-natural points fall, nothing more.")

    print("\nFENCES: toy/scaling (linear interpolation in the coupling; exact x<->c0 map inherits")
    print("mu_linear conventions, NOT derived); ISW linear-significance scaling off the banked 32sigma")
    print("anchor; Sigma leg conservative (slip not recomputed -- owed); does NOT demote mu_linear")
    print("(open screen), does NOT touch rung4/rung7_w3, banks NO new ledger input; the c0=0 choice")
    print("remains p_tt_ansatz's booked +1.")

    ok = _selftest()
    print(f"\n  SELFTEST: {'PASS' if ok else 'FAIL'}")
    return 0 if ok else 1


def _selftest():
    ok = True
    # endpoints banked-exact
    if abs(mu(0.0) - 1.0) > 1e-15 or abs(mu(1.0) - 4.0/3.0) > 1e-15:
        print("   [FAIL] endpoints"); ok = False
    # significance scaling anchored and linear
    if abs(isw_sigma(1.0) - 32.0) > 1e-12 or abs(isw_sigma(0.5) - 16.0) > 1e-12:
        print("   [FAIL] ISW scaling"); ok = False
    # the window: non-empty, correct arithmetic
    if not (0.0 < window_x(2.0) < 1.0):
        print("   [FAIL] window empty or unbounded"); ok = False
    if abs(window_x(2.0) - 1.0/16.0) > 1e-12 or abs(mu_ceiling(2.0) - ALPHA/16.0) > 1e-12:
        print("   [FAIL] window arithmetic"); ok = False
    # monotonicity of exclusion in x
    if not all(isw_sigma(a) < isw_sigma(b) for a, b in ((0.0, 0.1), (0.1, 0.5), (0.5, 1.0))):
        print("   [FAIL] monotonicity"); ok = False
    # ISW must be the BINDING constraint (others weaker)
    if not (2*MU0_ERR > mu_ceiling(2.0) and 2*SIG0_ERR*2 > mu_ceiling(2.0)):
        print("   [FAIL] ISW not binding vs banked mu0/Sigma0"); ok = False
    # the GRUT-natural points land where stated
    if not (isw_sigma(ALPHA) > 2.0 and isw_sigma(ALPHA**2) > 2.0 and isw_sigma(ALPHA/16) < 2.0):
        print("   [FAIL] natural-point placement"); ok = False
    return ok


if __name__ == "__main__":
    raise SystemExit(main())
