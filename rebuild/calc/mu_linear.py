#!/usr/bin/env python3
"""mu_linear: linear cosmology bookkeeping + the no-go export.  (BOOKKEEPING ONLY.)

GRUT = LCDM at linear order (mu_linear = 1) is entered DERIVED-PENDING, framed as a NO-GO
EXPORT -- per the overseer's Sec1.4 adversarial pre-screen. This file computes ONLY the safe
in-house piece the pre-screen blessed: the mu-Sigma (modified-Poisson + lensing) bookkeeping
that tabulates the consequence of EACH admissible response projector. It does NOT, and must
not, do either of these:
  * the CIRCULAR check 'confirm P^TT annihilates scalars' -- that re-detects the inserted ansatz;
  * the REAL settling check -- deriving the scalar projection's vanishing FROM THE ACTION without
    inserting P^TT. That is OPEN and partly FRONTIER-RESERVED (conformal/Riegert-Paneitz sector);
    it goes to the specialist, not in-house.

THE BREAK (why this is not 'derived clean'): the kernel K^R = alpha*chi(omega)*P^TT has P^TT
INSERTED BY HAND (a postulate). Other projectors (trace-only) are admissible in principle. So
'mu=1' is selected by which projector you write down -- definition-as-target. What actually
survives is a NO-GO EXPORT: the trace-only branch (mu=1+alpha) is excluded, so the TT branch
(mu=1=LCDM) is what's left -- by exclusion, NOT by positive derivation.

Carry alpha FREE (Sec4: never fit, expose no scale to match). Units dimensionless. Pure stdlib.
"""

ALPHA = 1.0 / 3.0   # GRUT conformal/trace-anomaly ratio (rung9a_value: conditional-theorem axiom). Carried, not fit.


def musigma(branch, alpha=ALPHA):
    """The mu-Sigma linear-MG bookkeeping (Pogosian-Silvestri / MGCAMB conventions):
        modified Poisson:  k^2 Psi = -4 pi G a^2 mu     rho Delta   (mu  = growth coupling)
        lensing (Weyl):    k^2(Phi+Psi) = -8 pi G a^2 Sigma rho Delta (Sigma = lensing coupling)
        slip:              eta = Phi/Psi
    Given a response-projector BRANCH, return (mu, Sigma, eta). This is the consequence of the
    branch, NOT a derivation of which branch is correct."""
    if branch == "TT":
        # pure transverse-traceless response annihilates ALL scalar perturbations (incl. the
        # traceless-scalar / anisotropic-stress piece -> viscous shear lives in spin-2, decouples).
        return 1.0, 1.0, 1.0                       # = GR / LCDM exactly
    if branch == "trace-only":
        # the trace mode is sourced -> effective coupling shifts by alpha (repo no-go value).
        mu = 1.0 + alpha                            # alpha=1/3 -> 4/3
        eta = 1.0 / (1.0 + alpha)                   # slip from the unmatched scalar response
        Sigma = mu * (1.0 + eta) / 2.0
        return mu, Sigma, eta
    raise ValueError("branch must be 'TT' or 'trace-only'")


def main():
    print("=" * 78)
    print("mu_linear -- linear cosmology bookkeeping (alpha = %.4f, carried free)" % ALPHA)
    print("=" * 78)

    print("\n(1) THE TWO ADMISSIBLE BRANCHES (both written down in the repo's no-go; the choice")
    print("    between them is NOT derived here -- P^TT is an inserted ansatz):")
    print("      branch        mu        Sigma      eta (slip)     status")
    for br in ("TT", "trace-only"):
        mu, Sig, eta = musigma(br)
        status = "= LCDM (GR)" if br == "TT" else "modifies growth+lensing"
        print(f"      {br:11}   {mu:6.4f}    {Sig:6.4f}    {eta:6.4f}      {status}")
    print("    => the number you get is SELECTED by the projector you postulate. mu=1 is the TT")
    print("       branch; trace-only gives mu = 1+alpha = %.4f. 'TT annihilates scalars' is the" % (1 + ALPHA))
    print("       ANSATZ, not a derivation (failure mode: definition-as-target).")

    print("\n(2) THE NO-GO EXPORT (what actually selects mu=1 -- by EXCLUSION, not derivation):")
    print("    The trace-only branch (mu=%.4f) is removed two independent ways:" % (1 + ALPHA))
    print("      (a) a separate-universe CONSISTENCY NO-GO excludes it internally;")
    print("      (b) it is EMPIRICALLY FALSIFIED at ~32 sigma by the low-ell ISW excess")
    print("          (mu>1 enhances late-time potential decay -> ISW-galaxy cross excess).")
    print("          [CORRECTED 2026-08-03 by calc/isw_exclusion.py: the mechanism direction above is")
    print("           BACKWARDS (mu>1 STRENGTHENS growth -> decay SUPPRESSED; the model HALVES the")
    print("           positive cross signal to ~0.57x) and the computed cross-channel number is")
    print("           ~2.0sigma (1.97 central, Sigma-corrected; band ~0.6-4.8), not 32 -- a 32-class")
    print("           number is impossible in that channel (capped ~9-12sigma). The")
    print("           exclusion survives MULTI-LEG: leg (a) (EdS-quantified) + DESI Sigma0 ~3.5sigma +")
    print("           the owed TT-auto channel (estimate-grade large).]")
    print("    So linear cosmology = LCDM (mu=1) is what SURVIVES -- a no-go export, GRUT's")
    print("    characteristic strength, NOT a clean positive 'GRUT predicts LCDM'.")
    print("    HONEST CAVEATS: (i) this is a THEOREM ABOUT GRUT-AS-WRITTEN; (ii) mu=1 was")
    print("    empirically SELECTED, not predicted a priori; (iii) tier = DERIVED-PENDING.")

    print("\n(3) WHAT IS NOT DONE HERE (and why):")
    print("    * NOT the circular 'P^TT annihilates scalars' check -- it re-detects the ansatz.")
    print("    * NOT the real settling check (scalar vanishing FROM the action, no inserted P^TT)")
    print("      -- that is OPEN and partly frontier-reserved (Riegert/conformal sector); it would")
    print("      graduate mu_linear to derived, and it goes to the specialist, not in-house.")

    print("\n" + "=" * 78)
    print("RESOLVED 2026-06-27 via the rung-9 SPLIT (was: the alpha=1/3-vs-P^TT issue)")
    print("=" * 78)
    print("""  alpha=1/3 is the conformal/trace-mode anomaly ratio; the tracefree P^TT has zero double-trace
  (eta.eta.P^TT == 0), so 1/3 is a hand-pinned structural LABEL in the TT channel, NOT a computed
  contraction output. The earlier 'either (A) alpha has NO carrier / alpha annihilated, or (B) the
  trace leg is real and mu!=1' DICHOTOMY OVER-STATED it: alpha is a scalar prefactor -- nothing
  annihilates a scalar. Resolved by SPLITTING rung 9, not re-tiering it wholesale:
    * rung9a_value  -- the alpha VALUE survives intact, a conditional-theorem dimensionless axiom
                       (anomaly coefficient one-loop-exact / safe). UNTOUCHED, NOT refuted.
    * rung9b_bridge -- the BRIDGE (1/3 normalizes the TT amplitude c_0) is SETTLED-NEGATIVE,
                       obstructed PRIMARILY by projector orthogonality (trace=spin-0 vs TT=spin-2;
                       no metric-built scalar->TT intertwiner). REPAIR OWED, NOT forbidden: a third
                       CFT route exists (a TT 2-point CAN be normalized by an anomaly coefficient --
                       the anomaly correlator is not the response correlator).
  The alpha-carrier RESOLUTION stays FRONTIER-RESERVED (Riegert/conformal sector -> specialist).
  Note: mu=1 here is alpha-FREE, so this split does NOT touch the mu_linear no-go export above.""")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
