#!/usr/bin/env python3
"""kk_static_transfer: does the dissipative sign floor transfer to the STATIC modulus mu couples to?

PRE-REGISTERED: provenance/prereg/PREREG_KK_STATIC_2026-08-09.txt
  (sha256 = 1f9c3bf6f2954087f1bfb24d2fe24a24e2f1d96856c3ccfcdcbb219619f37755 -- sealed BEFORE
  this file existed; results cite it in provenance/prereg/RESULT_KK_STATIC_2026-08-09.txt).

THE QUESTION (register node kk_static_transfer -- the load-bearing gap between "the family has
a floor" and "mu has a floor"): x_no_pin_theorem gives omega*Im c0(omega) >= 0 pointwise (the
dissipative floor). mu(x) couples to the STATIC quasi-static modulus Re c0(omega -> 0) at fixed
k. Does the floor transfer?

THE ANSWER THIS FILE ESTABLISHES (machine-checked; pre-registered outcomes (b) AND (c) jointly):
  THE DECOMPOSITION IDENTITY. For a retarded (upper-half-plane-analytic) channel coefficient
  chi(omega) with real high-frequency limit chi_inf (the INSTANTANEOUS/contact part) and a
  convergent dispersion integral,
      chi(0)  =  chi_inf  +  (2/pi) * INT_0^inf domega Im chi(omega)/omega .
  Passivity makes the integral nonnegative, so chi(0) >= chi_inf ALWAYS -- and nothing more:
  (b) UNCONDITIONAL TRANSFER IS REFUTED by explicit counterexample: chi(omega) = C_INF +
      B/(1 - i omega tau) with C_INF < 0, 0 < B < |C_INF| is retarded-analytic (its only pole
      sits in the LOWER half-plane), passive at every real frequency (a real constant has no
      imaginary part), and consistent with the TWO-POINT KMS/FDT lock (the lock rides Im chi,
      untouched by the contact term; no claim is made about a many-body equilibrium
      realization of this specific kernel -- the two-point lock is all the register banks at
      rung2 and all this counterexample needs) -- and its static modulus chi(0) = C_INF + B
      is NEGATIVE.
  (c) THE TRANSFER CRITERION, stated at class level where it is exact (precision corrected
      TWICE by review -- first from 'exactly as strong as single-pole' (false equivalence),
      then from 'chi(0) >= 0 iff chi_inf >= 0' (false biconditional about an individual
      kernel: a passive kernel with chi_inf < 0 can still land chi(0) >= 0 if its dissipative
      integral is large enough; nothing in passivity forbids that)): passivity gives
      chi(0) >= chi_inf, so chi_inf >= 0 is SUFFICIENT for the floor; it is NOT necessary,
      and passivity supplies NO necessary condition on chi_inf whatsoever. What is exact:
      chi_inf >= 0 is the TIGHTEST premise on the instantaneous part that yields the
      guarantee ACROSS THE WHOLE ADMISSIBLE CLASS (for any chi_inf < 0 an admissible kernel
      with chi(0) < 0 exists -- the counterexample family). Three nested facts:
        - chi_inf = 0 (the VANISHING-instantaneous-part class) gives the EQUALITY
          chi(0) = (2/pi) INT Im/omega >= 0 -- and the single-pole/Debye family that
          rung3_single_pole conjectures is IN this class, so conditional on rung3's
          conjecture the floor holds. SUFFICIENT, NOT NECESSARY.
        - chi_inf > 0 also transfers (chi(0) >= chi_inf > 0) -- the floor does NOT die with
          the single-pole class: a branch-cut kernel with vanishing or positive instantaneous
          part keeps it. (Even the strict Markovian endpoint tau -> 0, which degenerates to a
          pure POSITIVE contact term, keeps the floor via chi_inf >= 0 while exiting the
          chi_inf = 0 class -- one more reason the bankable criterion is the sign of chi_inf.)
        - chi_inf < 0 breaks it (the counterexample class): unconditionally, nothing.
      Whether GRUT's vacuum kernel has chi_inf >= 0 is a bath/UV property -- rung3's domain,
      priced there, never decided here.

CONTEXT REMARK, analogy-grade per the sealed prereg (never a proof step): the register banks at
p_tt_ansatz (exact arithmetic) that linearized Einstein-Hilbert's own kernel is
(1/2)k^2[P2 - 2*P0s] -- a NEGATIVE omega-independent scalar-channel coefficient. Negative real
contact structure in gravity's scalar channel is not exotic; but the EH kernel is the KINEMATIC
operator, not the vacuum's dissipative response deviation, and this remark transfers nothing.

CONVERGENCE, stated per the prereg: the dispersion route assumes INT Im chi/omega converges
(true for every kernel exhibited here, with the quadrature's tail bounded analytically). If the
admissible class's UV behavior forces further subtractions, more unconstrained constants enter
and the condition only TIGHTENS -- also a bath/UV property.

FENCES: no statement about the TT channel or any ceiling; no Israel-Stewart number; no
unconditional "mu has a floor" quote ever (the counterexample is permanent); no assertion about
GRUT's actual kernel class (rung3's). KC4 guard carried: the floor -- conditional or not --
licenses no channel's vanishing.

Pure stdlib. Self-tested; mutation battery in provenance/mutation_registry.py (M1-M4, each
pre-registered in the sealed prereg).
"""
import math

# ---------------------------------------------------------------------------------------------
# Kernel constructors: sums of Debye relaxors plus a real contact (instantaneous) term.
# A kernel is represented as (c_inf, [(chi_i, tau_i), ...]).
# ---------------------------------------------------------------------------------------------

def chi_value(kernel, w):
    """chi(omega) = c_inf + sum_i chi_i / (1 - i omega tau_i), as (re, im)."""
    c_inf, poles = kernel
    re, im = c_inf, 0.0
    for chi0, tau in poles:
        den = 1.0 + (w * tau) ** 2
        re += chi0 / den
        im += chi0 * w * tau / den
    return re, im


def im_over_omega(kernel, w):
    """Im chi(omega)/omega, extended by its finite omega->0 limit (sum chi_i tau_i)."""
    _c_inf, poles = kernel
    if w == 0.0:
        return sum(chi0 * tau for chi0, tau in poles)
    return sum(chi0 * tau / (1.0 + (w * tau) ** 2) for chi0, tau in poles)


def instantaneous_part(kernel):
    """chi_inf: the real high-frequency (contact) part -- the datum passivity never constrains."""
    c_inf, _poles = kernel
    return c_inf


def pole_locations(kernel):
    """Poles of chi in the complex omega plane: 1 - i omega tau = 0 -> omega = -i/tau.
    Retarded analyticity requires every pole strictly in the LOWER half-plane (Im < 0)."""
    _c_inf, poles = kernel
    return [complex(0.0, -1.0 / tau) for _chi0, tau in poles]


def kms_noise(kernel, w, beta=1.0):
    """The KMS lock: N(omega) = coth(beta*omega/2) * Im chi(omega). Rides Im alone -- a real
    contact term never enters, which is exactly why KMS cannot rescue (or see) chi_inf."""
    _re, im = chi_value(kernel, w)
    return (1.0 / math.tanh(0.5 * beta * w)) * im


# ---------------------------------------------------------------------------------------------
# The dispersion quadrature: (2/pi) INT_0^W Im chi/omega + analytic tail bound.
# ---------------------------------------------------------------------------------------------

def kk_static(kernel, n=20001):
    """(2/pi) * INT_0^inf domega Im chi(omega)/omega via the tan substitution omega = tan(theta):
    the half-line maps to [0, pi/2) where the transformed integrand
        g(theta) = [Im chi(tan theta)/tan theta] * sec^2(theta)
    is smooth and FINITE at both ends (at 0 it is the integrand's omega->0 limit; at pi/2 it
    tends to sum_i chi_i/tau_i), so one composite Simpson resolves every relaxor timescale at
    once. (The first build used uniform Simpson on [0, W] -- h = W/n under-resolved any feature
    narrower than the step and the selftest rejected the reconstruction; this substitution is
    the fix, not a tolerance loosening.)"""
    if n % 2 == 0:
        n += 1
    _c_inf, poles = kernel
    h = (math.pi / 2.0) / (n - 1)

    def g(theta):
        if theta >= math.pi / 2.0 - 1e-12:
            return sum(chi0 / tau for chi0, tau in poles)  # the finite endpoint limit
        w = math.tan(theta)
        sec2 = 1.0 + w * w
        return im_over_omega(kernel, w) * sec2

    total = g(0.0) + g(math.pi / 2.0)
    for i in range(1, n - 1):
        total += (4.0 if i % 2 else 2.0) * g(i * h)
    total *= h / 3.0
    return (2.0 / math.pi) * total


# ---------------------------------------------------------------------------------------------
# The exhibits.
# ---------------------------------------------------------------------------------------------

# The vanishing-instantaneous-part (single-pole-class) samples: chi_inf = 0, passive weights.
CLASS_SAMPLES = [
    (0.0, [(1.0, 1.0)]),                       # single Debye
    (0.0, [(0.7, 0.3), (0.5, 4.0)]),           # two relaxors, distinct times
    (0.0, [(0.2, 10.0), (1.1, 0.05), (0.4, 1.0)]),
]

# THE COUNTEREXAMPLE (pre-named by form in the sealed prereg; constants chosen here):
# a negative contact term dominating a passive relaxor's static weight.
C_INF = -1.0
B_RELAX = 0.4
TAU_CE = 1.0
COUNTEREXAMPLE = (C_INF, [(B_RELAX, TAU_CE)])

PASSIVITY_GRID = [s * 10.0 ** e for e in range(-3, 4) for s in (-1.0, 1.0)]

# A passive kernel with POSITIVE contact term: outside the chi_inf = 0 class, floor still holds
# (the witness that the criterion is chi_inf >= 0, not single-pole membership).
POSITIVE_CONTACT_SAMPLE = (0.5, [(0.4, 1.0)])

FROZEN_VERDICT = {
    "unconditional_transfer": False,           # outcome (a) did NOT bank -- the flattering branch
    "passive_counterexample_exists": True,     # outcome (b): negative static modulus exhibited
    "conditional_transfer_on_vanishing_instantaneous_part": True,   # outcome (c), sufficient leg
    "criterion_is_sign_of_instantaneous_part": True,  # class-level: chi_inf >= 0 sufficient + tightest
    "class_condition_is_bath_property": True,  # chi_inf is UV/contact structure -> rung3's domain
}


def compute_verdict():
    """Recompute every FROZEN_VERDICT entry from scratch (the certifier outside the certified)."""
    v = {}
    # (b) the counterexample: retarded-analytic, passive, negative at DC
    ce_re0, _ = chi_value(COUNTEREXAMPLE, 0.0)
    analytic = all(p.imag < 0.0 for p in pole_locations(COUNTEREXAMPLE))
    passive = all(w * chi_value(COUNTEREXAMPLE, w)[1] >= -1e-15 for w in PASSIVITY_GRID)
    v["passive_counterexample_exists"] = analytic and passive and (ce_re0 < 0.0)
    # (a) refuted by (b); it could only bank if no such kernel existed
    v["unconditional_transfer"] = not v["passive_counterexample_exists"]
    # (c) the class result: on chi_inf = 0 samples the KK-static equals the (nonnegative) integral
    cond = True
    for kern in CLASS_SAMPLES:
        static = kk_static(kern)
        closed = chi_value(kern, 0.0)[0]
        if abs(static - closed) > 1e-6 * max(1.0, abs(closed)) or static < -1e-12:
            cond = False
        if abs(instantaneous_part(kern)) > 0.0:
            cond = False
    # ... and the decomposition identity holds ON the counterexample too (chi(0)-chi_inf = integral)
    gap = chi_value(COUNTEREXAMPLE, 0.0)[0] - instantaneous_part(COUNTEREXAMPLE)
    if abs(kk_static(COUNTEREXAMPLE) - gap) > 1e-6:
        cond = False
    v["conditional_transfer_on_vanishing_instantaneous_part"] = cond
    # the exact criterion: a POSITIVE-contact kernel (outside the chi_inf=0 class) keeps the
    # floor, and for negative chi_inf the counterexample family breaks the class guarantee --
    # chi_inf >= 0 is sufficient and class-level tightest (never a per-kernel biconditional)
    pos_ok = (all(w * chi_value(POSITIVE_CONTACT_SAMPLE, w)[1] >= -1e-15 for w in PASSIVITY_GRID)
              and chi_value(POSITIVE_CONTACT_SAMPLE, 0.0)[0] >= 0.0
              and instantaneous_part(POSITIVE_CONTACT_SAMPLE) > 0.0)
    v["criterion_is_sign_of_instantaneous_part"] = pos_ok and v["passive_counterexample_exists"]
    # chi_inf is a reactive contact datum: passivity is blind to it (the counterexample's Im is
    # IDENTICAL to the same kernel with the contact term deleted -- checked numerically)
    stripped = (0.0, COUNTEREXAMPLE[1])
    blind = all(abs(chi_value(COUNTEREXAMPLE, w)[1] - chi_value(stripped, w)[1]) < 1e-15
                for w in PASSIVITY_GRID)
    v["class_condition_is_bath_property"] = blind
    return v


# ---------------------------------------------------------------------------------------------
# Report
# ---------------------------------------------------------------------------------------------

def main():
    print("=" * 94)
    print("kk_static_transfer -- does the dissipative floor reach the static modulus mu couples to?")
    print("pre-registered: PREREG_KK_STATIC_2026-08-09.txt (sealed before this file existed)")
    print("=" * 94)

    print("\nPART A -- the dispersion machinery, verified against closed forms (chi_inf = 0 class):")
    for kern in CLASS_SAMPLES:
        static = kk_static(kern)
        closed = chi_value(kern, 0.0)[0]
        print(f"  kernel {kern[1]}: KK-static = {static:.8f}   closed form chi(0) = {closed:.8f}"
              f"   |diff| = {abs(static - closed):.2e}")
    print("  => (2/pi) INT Im chi/omega reconstructs the static modulus exactly on the class;")
    print("     every value is NONNEGATIVE because the integrand is (passivity, pointwise).")

    print("\nPART B -- THE COUNTEREXAMPLE (pre-named by form in the sealed prereg):")
    print(f"  chi(omega) = {C_INF} + {B_RELAX}/(1 - i omega); checks:")
    poles = pole_locations(COUNTEREXAMPLE)
    print(f"  retarded-analytic: poles at {poles} -- all in the LOWER half-plane: "
          f"{all(p.imag < 0 for p in poles)}")
    worst = min(w * chi_value(COUNTEREXAMPLE, w)[1] for w in PASSIVITY_GRID)
    print(f"  passive: min over grid of omega*Im chi = {worst:.3e}  (>= 0 -- the contact term has")
    print("           no imaginary part, so passivity cannot see it)")
    nv = kms_noise(COUNTEREXAMPLE, 0.7)
    print(f"  two-point KMS/FDT lock rides Im alone: N(0.7) = {nv:.6f} -- identical with or without")
    print("  the contact term (no many-body-realization claim; the two-point lock is all rung2 banks)")
    ce0 = chi_value(COUNTEREXAMPLE, 0.0)[0]
    print(f"  STATIC MODULUS: chi(0) = {C_INF} + {B_RELAX} = {ce0:.3f}  < 0")
    print("  => a retarded, passive, KMS-consistent kernel with NEGATIVE static response exists.")
    print("     UNCONDITIONAL TRANSFER IS REFUTED. Pre-registered outcome (b) obtains.")

    print("\nPART C -- the decomposition identity (why (b) and (c) are the same fact seen twice):")
    gap = ce0 - instantaneous_part(COUNTEREXAMPLE)
    kkval = kk_static(COUNTEREXAMPLE)
    print(f"  chi(0) - chi_inf = {gap:.6f}   vs   (2/pi) INT Im/omega = {kkval:.6f}")
    print("  chi(0) = chi_inf + (nonnegative integral): the floor pushes the static modulus up")
    print("  FROM chi_inf, never below it -- so the transfer question IS the sign of chi_inf,")
    print("  a reactive contact datum passivity never constrains.")

    print("\nPART D -- the conditional result (pre-registered outcome (c)), stated at its exact edge:")
    print("  THE CRITERION (class-level, where it is exact): passivity gives chi(0) >= chi_inf, so")
    print("  chi_inf >= 0 is SUFFICIENT for the floor -- not necessary, and passivity supplies no")
    print("  necessary condition on chi_inf at all; chi_inf >= 0 is the tightest class-level premise.")
    print("  chi_inf = 0 gives the equality chi(0) = (2/pi) INT Im/omega >= 0; the single-pole/")
    print("  Debye family rung3_single_pole conjectures is IN that class -- so conditional on")
    print("  rung3's conjecture the floor holds. SUFFICIENT, NOT NECESSARY: any kernel with")
    print("  chi_inf >= 0 keeps the floor (verified below on a positive-contact sample), so the")
    print("  floor does NOT die if single-pole falls -- and it is never unconditional (Part B).")
    print("  Whether GRUT's vacuum kernel has chi_inf >= 0 is bath/UV structure: rung3's question,")
    print("  priced there, never decided here.")

    print("\nPART E -- fences (per the sealed prereg):")
    print("  * NO unconditional 'mu has a floor' quote, ever -- the counterexample is permanent.")
    print("  * NO TT-channel or ceiling statement; NO Israel-Stewart number.")
    print("  * NO assertion about GRUT's actual kernel class (rung3's, priced there).")
    print("  * Context remark stays analogy-grade: linearized EH's own scalar coefficient is a")
    print("    negative contact structure (banked, p_tt_ansatz) -- kinematic, transfers nothing.")
    print("  * KC4: the floor, conditional or not, licenses no channel's vanishing.")

    verdict = compute_verdict()
    print("\nVERDICT (recomputed, compared to frozen -- outcomes (b) AND (c), the default-broken set):")
    for k in FROZEN_VERDICT:
        print(f"  {k:52s} computed={verdict[k]!s:5s} frozen={FROZEN_VERDICT[k]!s:5s}")

    ok = _selftest()
    print(f"\n  SELFTEST: {'PASS' if ok else 'FAIL'}")
    return 0 if ok else 1


# ---------------------------------------------------------------------------------------------
# Selftest: independent probes; every load-bearing claim recomputed.
# ---------------------------------------------------------------------------------------------

def _selftest():
    ok = True
    # (1) quadrature engine vs closed forms on kernels NOT in the report list
    for kern in ((0.0, [(0.9, 2.0)]), (0.0, [(0.3, 0.1), (0.8, 7.0)])):
        static, closed = kk_static(kern), chi_value(kern, 0.0)[0]
        if abs(static - closed) > 1e-6 * max(1.0, abs(closed)):
            print(f"   [FAIL] KK reconstruction off on {kern}: {static} vs {closed}"); ok = False
    # (2) stability under n doubling, on a WIDE-timescale kernel (the case the first build's
    #     uniform grid failed on -- the probe must cover the failure that actually happened)
    kern = (0.0, [(0.2, 10.0), (1.1, 0.05), (0.4, 1.0)])
    a1, a2 = kk_static(kern, n=20001), kk_static(kern, n=40001)
    if abs(a1 - a2) > 1e-9:
        print(f"   [FAIL] quadrature not converged: {a1} vs {a2}"); ok = False
    # (3) the counterexample, all four properties, with an independent probe grid
    probe = [s * 10.0 ** e for e in range(-4, 5) for s in (-1.0, 1.0)]
    if not all(p.imag < 0.0 for p in pole_locations(COUNTEREXAMPLE)):
        print("   [FAIL] counterexample not retarded-analytic"); ok = False
    if not all(w * chi_value(COUNTEREXAMPLE, w)[1] >= -1e-15 for w in probe):
        print("   [FAIL] counterexample not passive on the independent grid"); ok = False
    ce0 = chi_value(COUNTEREXAMPLE, 0.0)[0]
    if not (ce0 < 0.0 and abs(ce0 - (C_INF + B_RELAX)) < 1e-12):
        print(f"   [FAIL] counterexample static modulus {ce0} not the negative value it must be"); ok = False
    # (4) the decomposition identity on BOTH classes (the counterexample and a clean sample)
    for kern in (COUNTEREXAMPLE, (0.0, [(0.6, 3.0)])):
        gap = chi_value(kern, 0.0)[0] - instantaneous_part(kern)
        if abs(kk_static(kern) - gap) > 1e-6:
            print(f"   [FAIL] decomposition identity broken on {kern}"); ok = False
    # (5) chi_inf is invisible to passivity AND to the KMS lock (the blindness that makes it free)
    stripped = (0.0, COUNTEREXAMPLE[1])
    for w in (0.3, 1.7, -0.9):
        if abs(chi_value(COUNTEREXAMPLE, w)[1] - chi_value(stripped, w)[1]) > 1e-15:
            print("   [FAIL] contact term leaked into Im chi"); ok = False
        if abs(kms_noise(COUNTEREXAMPLE, w) - kms_noise(stripped, w)) > 1e-12:
            print("   [FAIL] contact term leaked into the KMS noise"); ok = False
    # (6) the class theorem: pointwise-passive integrand => nonnegative static, on chi_inf=0 samples
    for kern in CLASS_SAMPLES:
        if any(im_over_omega(kern, w) < -1e-15 for w in (0.0, 0.01, 0.5, 3.0, 40.0)):
            print(f"   [FAIL] class sample {kern} not pointwise passive"); ok = False
        if kk_static(kern) < -1e-12:
            print(f"   [FAIL] class sample {kern} has negative static -- theorem broken"); ok = False
    # (7) frozen verdict vs recomputed, entry for entry
    verdict = compute_verdict()
    for k, want in FROZEN_VERDICT.items():
        if verdict.get(k) != want:
            print(f"   [FAIL] verdict mismatch on {k!r}: computed {verdict.get(k)}, frozen {want}"); ok = False
    return ok


if __name__ == "__main__":
    raise SystemExit(main())
