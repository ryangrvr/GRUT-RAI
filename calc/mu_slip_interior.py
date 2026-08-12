#!/usr/bin/env python3
"""mu_slip_interior: the RIGOROUS (inherited-bookkeeping) mu/eta/Sigma computation across the
{shear, bulk} interior -- the graduation-path calc zeta_interior_family's first pass owed.

WHAT THIS CLOSES (the first pass's named fences):
  F1 'linear interpolation is a toy' -> CLOSED AT BOOKKEEPING LEVEL: in mu_linear.py's own
     conventions (Pogosian-Silvestri modified Poisson + slip + Weyl), the scalar-channel coupling
     enters the Poisson sector LINEARLY, so mu(x) = 1 + x*alpha is EXACT here, not leading-order.
  F2 'the slip computation is owed' -> CLOSED AT THE SAME LEVEL: eta(x) = 1/(1 + x*alpha),
     INHERITED from the same one-sided structure (the coupling enters the Psi-equation ONLY; Phi
     stays GR -- eta = 1/mu is CONDITIONAL on that one-sidedness, which mu_linear.py postulates
     rather than derives; a genuine P0s admixture could source scalar anisotropic stress and split
     the law -- that case is R2's, owned by the demotion screen). Given it: the IDENTITY
     Sigma(x) - 1 = (mu(x) - 1)/2 holds for ALL x (not just endpoints).
  F3 'linear ISW significance scaling is assumed' -> PARTLY CLOSED: within this bookkeeping x is a
     PURE AMPLITUDE RESCALE of one fixed modification shape, so the template is x-independent and
     the significance is LEADING-ORDER-EXACT given the fixed-template assumption. NOTE the
     bookkeeping itself contains no ISW dynamics -- linearity of the SIGNAL in x is an additional
     leading-order dynamical statement, with O((x*alpha)^2) growth-feedback corrections (~2% at the
     edge): a small, NAMED family-side softness.
  ANCHOR CORRECTION 2026-08-03 (calc/isw_exclusion.py -- the anchor's own computation, closing the
     provenance caveat): the banked ~32sigma was NOT confirmed. Cross-channel endpoint exclusion
     N(1) ~ 2.0 (computed 1.97 central, Sigma-corrected per firewall B1; band ~0.6-4.8; a 32-class
     number is IMPOSSIBLE in that channel -- capped at ~9-12sigma for a signal-suppressing model),
     and at central inputs the cross channel ALONE no longer 2sigma-excludes any x <= 1. BINDING
     INVERSION: the family window is bound by DESI Sigma0 LENSING (x < ~0.59 under the banked slip;
     CENTRAL-INPUTS + LOOSE-UPPER per the F-MAP fence -- shape-weighted mapping plausibly 2-3x
     tighter). The low-ell TT AUTO channel (estimate-grade order-10^2-sigma-class at x=1, est. edge
     BAND ~0.03-0.14) is OWED its own calc and likely re-tightens the true edge to the retired-1/16
     neighborhood.

WHAT REMAINS OPEN (the node's continuing to-derive content -- named, not hidden):
  R1 the x <-> c0 ACTION-LEVEL map: this bookkeeping has ONE scalar coupling dial; tying x to the
     P0s modulus normalization from the action is the deeper step (partly frontier-reserved,
     conformal/Riegert-Paneitz). The identification 'mu_linear's trace-coupling == the P0s
     channel's Poisson-sector effect' is at the inherited-model level.
     [R1 DISCHARGED-BY-CONSTRUCTION 2026-08-09, overseer-ruled (RELAY_kernel_reframe): S_IF.md
     defines x := c0/c0^trace-only, closing the map BY DECLARATION -- which is what the deeper
     step turned out to be. Two residues stay live and are homed elsewhere: x is declared a
     KERNEL x(omega,k^2) (constant-x numbers are cut-conditional -- zeta_interior_family), and
     the dissipative-to-STATIC sign transfer is ANSWERED at register node kk_static_transfer
     (2026-08-09: refuted unconditionally; derived conditionally at the tightest class-level criterion chi_inf >= 0 -- sufficient, not
     necessary -- of which rung3's single-pole class is a sufficient subclass).]
  R2 the inherited MODEL itself: one scalar dial (a fuller model could split Poisson-vs-slip
     couplings); the mu_linear demotion screen owns the model question.
  R3 the u5-facing dynamics classification (which kernel dynamics live in the window).

THE FAMILY (derived, not interpolated):
  The kernel K = c2*P^TT + c0*P0s. The TT part contributes NOTHING to scalar perturbations
  (mu_linear branch 'TT' -> GR exactly, banked). The P0s part sources the scalar sector with
  relative strength x (normalized so x=1 is the trace-only endpoint's coupling). One effective
  scalar coupling x*alpha then flows through the SAME banked bookkeeping:
      mu(x)    = 1 + x*alpha                      (Poisson-sector coupling, linear -- exact)
      eta(x)   = 1/(1 + x*alpha)                  (slip from the unmatched scalar response)
      Sigma(x) = mu(x) * (1 + eta(x)) / 2  =  1 + x*alpha/2      (identity: Sigma-1 = (mu-1)/2)
  Endpoints are VERIFIED against calc/mu_linear.py's own musigma() outputs, exactly.

Pure stdlib. Self-tested (imports mu_linear and checks against it). Default-BROKEN: the win is the
closed fences and the confirmed edge, not a prediction -- the family ALLOWS, it does not predict.
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from mu_linear import musigma, ALPHA  # the inherited bookkeeping -- the SOURCE of truth here

# ANCHOR CORRECTED 2026-08-03 (calc/isw_exclusion.py): the banked "~32" was NOT confirmed.
# FIREWALL B1 (2026-08-03): the Weyl-source Sigma(x) factor added to the cross amplitude.
N_CROSS_ENDPOINT = 2.0       # banked (computed 1.97 central, Sigma-corrected; band ~0.6-4.8)
# NO in-family 2sigma cross edge at central inputs (N(1) < 2 -- firewall B1; band-hi corners still
# give one, e.g. x ~ 0.56 at A_obs = 1.20). The pre-B1 "EDGE_CROSS = 0.84" is RETIRED.
AUTO_EDGE_EST = 0.034        # ESTIMATE-GRADE ONLY, unfiltered; BAND ~0.03-0.14 (filter/normalization-
                             # sensitive; TT-auto channel, own rigorous calc OWED; not a register number)
N_SIGMA_ENDPOINT = N_CROSS_ENDPOINT  # retained name = the CROSS-channel endpoint significance


def mu_x(x):
    return 1.0 + x * ALPHA

def eta_x(x):
    return 1.0 / (1.0 + x * ALPHA)

def Sigma_x(x):
    return mu_x(x) * (1.0 + eta_x(x)) / 2.0

def isw_sigma(x):
    """Cross-channel significance, leading-order-linear (computed curve deviates -1.8% at the cross
    edge -- calc/isw_exclusion.py); the COMPUTED anchor, not the retired 32."""
    return N_CROSS_ENDPOINT * x

# The COMPUTED-CHANNEL family edge: DESI Sigma0 lensing binds under the banked slip (BINDING
# INVERSION 2026-08-03 -- ISW-cross no longer binds): Sigma-1 < 0.009 + 2*0.045 -> x*alpha/2 < 0.099.
# F-MAP FENCE (firewall B2, named, direction TIGHTER): DESI's Sigma0 multiplies an OmegaL(a)/OmegaL0
# shape; the family's Sigma-1 is CONSTANT in a; the direct identification makes this a CENTRAL-INPUTS
# LOOSE-UPPER edge (shape-weighted mapping plausibly 2-3x tighter, edge ~0.2-0.35 -- plausible-grade).
EDGE = (0.009 + 2 * 0.045) * 2.0 / ALPHA  # ~0.594


def main():
    print("=" * 94)
    print("mu/eta/Sigma ACROSS THE INTERIOR -- rigorous at the inherited-bookkeeping level")
    print("=" * 94)

    print("\nPART A -- endpoint verification against calc/mu_linear.py (the inherited source of truth):")
    mu_tt, Sig_tt, eta_tt = musigma("TT")
    mu_tr, Sig_tr, eta_tr = musigma("trace-only")
    print(f"   mu_linear TT         : mu={mu_tt:.6f} Sigma={Sig_tt:.6f} eta={eta_tt:.6f}")
    print(f"   family   x=0         : mu={mu_x(0):.6f} Sigma={Sigma_x(0):.6f} eta={eta_x(0):.6f}")
    print(f"   mu_linear trace-only : mu={mu_tr:.6f} Sigma={Sig_tr:.6f} eta={eta_tr:.6f}")
    print(f"   family   x=1         : mu={mu_x(1):.6f} Sigma={Sigma_x(1):.6f} eta={eta_x(1):.6f}")
    print("   => the family REPRODUCES the banked endpoints exactly; the interior is the same")
    print("      bookkeeping with the scalar coupling scaled by x -- derived, not interpolated.")

    print("\nPART B -- the two closed fences (exactness, not approximation):")
    print("   F1 LINEARITY: mu(x) = 1 + x*alpha is EXACT in this bookkeeping (the coupling enters")
    print("      the Poisson sector linearly). The first pass's 'leading-order interpolation' fence")
    print("      CLOSES at this level.")
    print("   F2 SLIP/Sigma: eta(x) = 1/(1+x*alpha); Sigma(x)-1 = (mu(x)-1)/2 is an IDENTITY for all")
    print("      x (machine-checked below across the family). The 'slip owed' fence CLOSES: the")
    print("      first pass's conservative reading was in fact exact, family-wide.")

    print("\nPART C -- the window, ANCHOR-CORRECTED 2026-08-03 (calc/isw_exclusion.py):")
    print("   The banked ~32sigma endpoint anchor was COMPUTED and NOT confirmed: cross-channel")
    print(f"   N(1) ~ {N_CROSS_ENDPOINT} (computed 1.97 central, Sigma-corrected; band ~0.6-4.8); NO in-family")
    print("   2sigma cross edge at central inputs (firewall B1).")
    print("   BINDING INVERSION: the family window is now bound by DESI Sigma0 LENSING under the")
    print(f"   banked slip eta=1/mu: Sigma-1 < 0.099 -> x < {EDGE:.3f}. At that edge:")
    print(f"      mu - 1    = {mu_x(EDGE)-1:.4f}")
    print(f"      Sigma - 1 = {Sigma_x(EDGE)-1:.4f}")
    print(f"      1 - eta   = {1-eta_x(EDGE):.4f}")
    print(f"   [F-MAP fence: central-inputs, loose-upper -- shape-weighted mapping plausibly tighter.]")
    print(f"   The TT-AUTO channel (estimate-grade edge BAND ~0.03-0.14) is OWED its own calc and")
    print("   likely re-tightens the true edge to the retired-1/16 neighborhood; until it exists the")
    print("   computed-channel edge above is the honest banked bound.")
    print("\nPART D -- what stays open (the node's to-derive content, named):")
    print("   R1 the x<->c0 ACTION-level map -- DISCHARGED-BY-CONSTRUCTION 2026-08-09 (S_IF.md")
    print("      defines x := c0/c0^trace-only; kernel-not-constant + static-transfer residues")
    print("      homed at zeta_interior_family / kk_static_transfer).")
    print("   R2 the inherited MODEL question (one scalar dial; Poisson-vs-slip splitting would be a")
    print("      richer model) -- owned by the open mu_linear demotion screen.")
    print("   R3 the u5-facing dynamics classification (which kernel dynamics live in the window).")
    print("   The family ALLOWS deviations up to the edge; it does NOT predict any (x has no floor).")

    ok = _selftest()
    print(f"\n  SELFTEST: {'PASS' if ok else 'FAIL'}")
    return 0 if ok else 1


def _selftest():
    ok = True
    # endpoints EXACT against the inherited bookkeeping
    mu_tt, Sig_tt, eta_tt = musigma("TT")
    mu_tr, Sig_tr, eta_tr = musigma("trace-only")
    for (a, b) in ((mu_x(0), mu_tt), (Sigma_x(0), Sig_tt), (eta_x(0), eta_tt),
                   (mu_x(1), mu_tr), (Sigma_x(1), Sig_tr), (eta_x(1), eta_tr)):
        if abs(a - b) > 1e-15:
            print(f"   [FAIL] endpoint mismatch {a} vs {b}"); ok = False
    # the Sigma identity across the family (exact, machine precision)
    for i in range(101):
        x = i / 100.0
        if abs((Sigma_x(x) - 1.0) - (mu_x(x) - 1.0) / 2.0) > 1e-15:
            print(f"   [FAIL] Sigma identity at x={x}"); ok = False
        if abs(Sigma_x(x) - mu_x(x) * (1 + eta_x(x)) / 2.0) > 1e-15:
            print(f"   [FAIL] Sigma definition at x={x}"); ok = False
    # exact linearity of mu (second difference identically zero)
    for x in (0.1, 0.3, 0.7):
        if abs(mu_x(x + 0.1) - 2 * mu_x(x) + mu_x(x - 0.1)) > 1e-15:
            print("   [FAIL] mu not exactly linear"); ok = False
    # window arithmetic + edge values (lensing-bound computed-channel edge, 2026-08-03)
    if abs(EDGE - (0.009 + 2 * 0.045) * 2.0 / ALPHA) > 1e-15 or not (0.55 < EDGE < 0.65) \
       or abs((Sigma_x(EDGE) - 1) - (0.009 + 2 * 0.045)) > 1e-12:
        print("   [FAIL] window/edge arithmetic"); ok = False
    # monotonicity: mu, Sigma increase; eta decreases
    for a, b in ((0.0, 0.2), (0.2, 0.6), (0.6, 1.0)):
        if not (mu_x(a) < mu_x(b) and Sigma_x(a) < Sigma_x(b) and eta_x(a) > eta_x(b)):
            print("   [FAIL] monotonicity"); ok = False
    # significance scaling anchored to the COMPUTED cross-channel number
    if abs(isw_sigma(1.0) - N_CROSS_ENDPOINT) > 1e-12:
        print("   [FAIL] ISW anchor"); ok = False
    # NON-TAUTOLOGICAL PIN on the DEFINITION (mutation-battery fix 2026-08-04: the checks above and
    # below are both tautological -- isw_sigma is DEFINED as N_CROSS_ENDPOINT*x, and N_SIGMA_ENDPOINT
    # is DEFINED as N_CROSS_ENDPOINT -- so a wrong value restored at the definition line passed the
    # whole selftest. The banked computed value is 2.0 (1.97 central, Sigma-corrected).)
    if not (1.5 < N_CROSS_ENDPOINT < 2.5):
        print(f"   [FAIL] N_CROSS_ENDPOINT = {N_CROSS_ENDPOINT} is outside the banked computed "
              f"range [1.5, 2.5]; the ~32sigma anchor is RETIRED (calc/isw_exclusion.py)")
        ok = False
    # the LEGACY NAME must not smuggle the retired anchor back in (mutation-battery guard,
    # 2026-08-03: N_SIGMA_ENDPOINT is a compatibility alias and a future reader restoring it to
    # 32.0 would otherwise be invisible)
    if N_SIGMA_ENDPOINT != N_CROSS_ENDPOINT:
        print(f"   [FAIL] N_SIGMA_ENDPOINT ({N_SIGMA_ENDPOINT}) has been detached from the "
              f"computed N_CROSS_ENDPOINT ({N_CROSS_ENDPOINT}) -- the ~32sigma anchor is RETIRED")
        ok = False
    return ok


if __name__ == "__main__":
    raise SystemExit(main())
