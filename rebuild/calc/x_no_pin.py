#!/usr/bin/env python3
"""x_no_pin: the CHANNEL-DIAGONAL PASSIVITY LEMMA -- X_FLOOR_MAP attack item 2, finally built.

PRE-REGISTERED: provenance/prereg/PREREG_X_NO_PIN_2026-08-09.txt
  (sha256 = 47e3a29e7c162739ee56699d7d6403af9459225e9b63d86963334e7b3ec4ee2b -- sealed BEFORE
  this file existed; results cite it in provenance/prereg/RESULT_X_NO_PIN_2026-08-09.txt).

THE LEMMA (what this file establishes, machine-checked rather than asserted):
  For the Ward-surviving two-channel kernel family the register carries (eft_operator_basis),
      K_R(omega, k) = c2(omega, k^2) * P2  +  c0(omega, k^2) * P0s,
  with P2, P0s the ORTHOGONAL IDEMPOTENT spin projectors of operator_basis.py, the banked
  matrix-sense passivity condition (rung2's S4: omega * Im K_R positive-semidefinite) is
  EXACTLY EQUIVALENT to the two independent scalar conditions
      omega * Im c2(omega) >= 0   AND   omega * Im c0(omega) >= 0,
  channel by channel. NO combination of signs lets one channel's positivity leak into or rescue
  the other: a violating bulk coefficient is a passivity violation no matter how large the
  compliant shear coefficient is made, and vice versa.

WHAT THE LEMMA IS AND IS NOT (fences carried on the file's face, per the pre-registration):
  * It is a SIGN condition on the action-level dissipative moduli c2, c0 -- pointwise in omega.
  * It is NOT a statement about x, the phenomenological slip-sector coupling of
    mu_slip_interior.py: the x <-> c0 ACTION-LEVEL map is that file's own named OPEN item (R1).
    The transfer becomes definitional only under S_IF.md's declared construction x := normalized
    c0 modulus (see S_IF.md Part 3) -- a declaration, not an output of this calc.
  * It is NOT a ceiling, NOT a pin, and NOT a licence for (or against) the pure-TT ansatz.
    THE GUARD, verbatim from BRIEF_p_tt_interrogation.md kill-condition 4, binding here:
    "Passivity (omega*Im chi positive-semidefinite as a matrix) constrains signs and
    cross-channel magnitudes; it can propagate a channel's vanishing (a zero diagonal kills its
    cross-couplings) but can never source one. Any argument deriving channel annihilation from
    passivity alone is a category error and dies."
  * CLASSIFIER, NOT PINNER (u5 route R3, exactly as X_FLOOR_MAP prices it): the admissible set
    is a convex cone, closed under independent nonnegative rescaling of each channel -- so
    passivity fixes an orientation per channel and can never select a ratio c0/c2. The no-pin
    fragment is thereby EARNED here, not inherited.

METHOD (why the checks are not tautological): the PSD test is a generic symmetric-matrix
eigenvalue computation (cyclic Jacobi) on the explicitly assembled 6x6 kernel matrix -- it never
uses the theorem's own structure ("eigenvalues are {c2, c0, 0}"). The projectors are imported
from operator_basis.py and their algebra re-verified, not assumed. Pure stdlib. Self-tested;
mutation battery in provenance/mutation_registry.py (four pre-registered wrong answers).

REGISTER HOMES (post-ruling 2026-08-09): the GENERAL lemma banks at passivity_channel_diagonal
(shown, frame-free); the GRUT APPLICATION (this file's Parts B-E read against the two-channel
family) banks at x_no_pin_theorem (derived-pending on the enumeration's 4d-covariant frontier --
the split the bank gate's TIER-CONTRADICTION correctly demanded); the dissipative-to-STATIC
transfer gap named in Part F is registered as its own owed item, kk_static_transfer.
"""
import math
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from operator_basis import projectors, mat6, mm, tr6, norm6, sub, unit, KHATS

TOL = 1e-10

# ---------------------------------------------------------------------------------------------
# Generic symmetric-eigenvalue machinery (independent of the projector structure under test).
# ---------------------------------------------------------------------------------------------

def jacobi_eigenvalues(A, sweeps=64, tol=1e-13):
    """Eigenvalues of a symmetric matrix by cyclic Jacobi rotations. Pure stdlib, no shortcuts."""
    n = len(A)
    M = [row[:] for row in A]
    for _ in range(sweeps):
        off = math.sqrt(sum(M[i][j] ** 2 for i in range(n) for j in range(n) if i != j))
        if off < tol:
            break
        for p in range(n - 1):
            for q in range(p + 1, n):
                if abs(M[p][q]) < tol * 1e-3:
                    continue
                theta = 0.5 * math.atan2(2.0 * M[p][q], M[q][q] - M[p][p])
                c, s = math.cos(theta), math.sin(theta)
                for k in range(n):
                    mkp, mkq = M[k][p], M[k][q]
                    M[k][p] = c * mkp - s * mkq
                    M[k][q] = s * mkp + c * mkq
                for k in range(n):
                    mpk, mqk = M[p][k], M[q][k]
                    M[p][k] = c * mpk - s * mqk
                    M[q][k] = s * mpk + c * mqk
    return sorted(M[i][i] for i in range(n))


def psd(A, tol=TOL):
    """(is_positive_semidefinite, min_eigenvalue). The MATRIX condition -- the minimum eigenvalue
    decides; aggregate quantities (trace, determinant) are exactly the cross-channel-rescue
    laundering the pre-registration's mutant M1 names.

    The tolerance is RELATIVE to the matrix scale (first run's own selftest caught this: at
    channel amplitude 1e6 the Jacobi rotations' 1e-14-relative float error exceeded an absolute
    1e-10 cut and faked a ceiling -- exactly the pre-registered flattering direction, rejected).
    A genuine violation enters at the violating channel's own scale, far above float error.
    NUMERIC BOUNDARY, stated so the evidence is never quoted past it: with this tolerance a
    violation of magnitude v reads as PSD once the compliant channel exceeds ~v/1e-10 (e.g.
    v=1e-3 masks beyond ~1e7). The calc therefore claims only its tested scales (rescue sweep
    through 1e6); the exact statement at all scales is the lemma's, which is arithmetic on the
    projector direct sum, not this float check."""
    eigs = jacobi_eigenvalues(A)
    mn = eigs[0]
    scale = max(1.0, max(abs(e) for e in eigs))
    return mn >= -tol * scale, mn


def kernel_matrix(a, b, m2, m0s):
    """The assembled 6x6 matrix of omega*Im K_R = a*P2 + b*P0s (a = omega*Im c2, b = omega*Im c0)."""
    return [[a * m2[i][j] + b * m0s[i][j] for j in range(6)] for i in range(6)]


def passive(a, b, m2, m0s):
    """Is the two-channel kernel with channel weights (a, b) matrix-passive?"""
    ok, _ = psd(kernel_matrix(a, b, m2, m0s))
    return ok


# ---------------------------------------------------------------------------------------------
# The passive witness family (existence side of the floor): Debye response in each channel.
# ---------------------------------------------------------------------------------------------

def debye_im(w, tau=1.0):
    """Im chi for chi(omega) = 1/(1 - i omega tau): the standard passive relaxor.
    omega * Im chi = omega^2 tau / (1 + omega^2 tau^2) >= 0 for ALL real omega."""
    return w * tau / (1.0 + (w * tau) ** 2)


def kms_noise_coeff(im_c, w, beta=1.0):
    """The KMS/FDT lock (rung2): N(omega) = coth(beta*omega/2) * Im K_R(omega), applied to one
    channel's scalar coefficient. The thermal factor is a COMMON SCALAR -- it multiplies both
    channels identically, which is exactly why the lock is channel-diagonal at this level."""
    return (1.0 / math.tanh(0.5 * beta * w)) * im_c


# ---------------------------------------------------------------------------------------------
# The verdict -- FROZEN LITERAL, compared against the recomputed verdict by the selftest
# (the certifier outside the certified: a mutant editing either side breaks the match).
# ---------------------------------------------------------------------------------------------

FROZEN_VERDICT = {
    "channel_diagonal": True,       # Q1: matrix passivity == the two scalar conditions
    "cross_channel_rescue": False,  # Q1: no compliant channel can rescue a violating one
    "ceiling_from_passivity": False,  # Q2: no upper bound on any amplitude or ratio
    "pin_from_passivity": False,    # Q2: no ratio selected (convex cone, per-channel rescaling)
    "kms_channel_diagonal": True,   # Q3: the noise lock decomposes on the same projectors
}

# Probe weights for the equivalence sweep. The selftest carries ITS OWN independent probes --
# this grid is for the report, so a mutant thinning it cannot blind the selftest.
GRID = (-2.0, -1.0, -0.35, 0.0, 0.35, 1.0, 2.0)
RESCUE_SCALES = (1.0, 1e2, 1e4, 1e6)


def compute_verdict(m2, m0s):
    """Recompute every FROZEN_VERDICT entry from scratch on the given projector matrices."""
    v = {}
    # Q1 equivalence, both directions, full sign grid
    eq = True
    for a in GRID:
        for b in GRID:
            want = (a >= -TOL) and (b >= -TOL)
            got = passive(a, b, m2, m0s)
            if want != got:
                eq = False
    v["channel_diagonal"] = eq
    # Q1 no-rescue: a violating channel stays violating under ANY compliant amplification
    rescue = False
    for s in RESCUE_SCALES:
        if passive(s, -1e-3, m2, m0s) or passive(-1e-3, s, m2, m0s):
            rescue = True
    v["cross_channel_rescue"] = rescue
    # Q2 no ceiling: independent nonnegative rescaling stays admissible at every scale
    ceiling = False
    for s in RESCUE_SCALES:
        if not passive(s * 1.0, 1.0, m2, m0s) or not passive(1.0, s * 1.0, m2, m0s):
            ceiling = True
    v["ceiling_from_passivity"] = ceiling
    # Q2 no pin: every nonnegative ratio r = b/a is realized by an admissible kernel
    pin = False
    for r in (0.0, 1e-6, 0.5, 1.0, 2.0, 1e6):
        if not passive(1.0, r, m2, m0s):
            pin = True
    v["pin_from_passivity"] = pin
    # Q3 KMS channel-diagonality: N = coth * Im K_R decomposes on the SAME projectors with the
    # SAME scalar factor, so N's PSD condition is the same two scalar conditions (checked at a
    # positive and a negative frequency; the sign of Im c must carry through the lock).
    kms_diag = True
    for w in (0.7, 2.3, -0.7):
        a_im, b_im = debye_im(w), 0.6 * debye_im(w)
        na, nb = kms_noise_coeff(a_im, w), kms_noise_coeff(b_im, w)
        # noise PSD must hold for the passive pair at every temperature-sign combination
        ok_n, _ = psd(kernel_matrix(na, nb, m2, m0s))
        if not ok_n:
            kms_diag = False
        # and a dissipation-sign violation must SURVIVE the lock (not be masked by it):
        nv = kms_noise_coeff(-abs(b_im) * (1.0 if w > 0 else -1.0), w)
        ok_v, _ = psd(kernel_matrix(abs(na), nv, m2, m0s))
        if ok_v:
            kms_diag = False
    v["kms_channel_diagonal"] = kms_diag
    return v


# ---------------------------------------------------------------------------------------------
# Report
# ---------------------------------------------------------------------------------------------

def main():
    print("=" * 94)
    print("x_no_pin -- the channel-diagonal passivity lemma (X_FLOOR_MAP attack item 2)")
    print("pre-registered: PREREG_X_NO_PIN_2026-08-09.txt (sealed before this file existed)")
    print("=" * 94)

    kh = KHATS[0]
    P2, P1, P0s, P0w, MIX, T, L = projectors(kh)
    m2, m0s = mat6(P2), mat6(P0s)

    print("\nPART A -- the projector algebra RE-VERIFIED (imported, not assumed):")
    i2 = norm6(sub(mm(m2, m2), m2))
    i0 = norm6(sub(mm(m0s, m0s), m0s))
    x12 = tr6(mm(m2, m0s))
    print(f"  idempotence |P2^2-P2| = {i2:.2e}   |P0s^2-P0s| = {i0:.2e}   tr[P2 P0s] = {x12:.2e}")
    print("  => two orthogonal idempotents; ranks tr P2 = %.0f, tr P0s = %.0f." % (tr6(m2), tr6(m0s)))

    print("\nPART B -- THE LEMMA (equivalence sweep, generic Jacobi eigenvalues, both directions):")
    print("  omega*Im K_R = a*P2 + b*P0s  is PSD  <=>  a >= 0 AND b >= 0")
    print("     a\\b   " + "  ".join(f"{b:+7.2f}" for b in GRID))
    for a in GRID:
        row = []
        for b in GRID:
            ok = passive(a, b, m2, m0s)
            row.append("  PSD " if ok else "  no  ")
        print(f"  {a:+6.2f} " + " ".join(row))
    print("  Every PSD cell sits in the closed positive quadrant; every quadrant-exterior cell fails.")

    print("\nPART C -- NO CROSS-CHANNEL RESCUE (the load-bearing negative):")
    for s in RESCUE_SCALES:
        _, mn = psd(kernel_matrix(s, -1e-3, m2, m0s))
        print(f"  a = {s:8.0e}, b = -1e-3:  min eigenvalue = {mn:+.3e}  (pinned at b -- amplifying")
    print("  the compliant shear channel by six orders of magnitude never lifts the violation.")
    print("  Positivity is decided in each spin sector separately: the sectors are orthogonal, so")
    print("  the matrix condition CANNOT trade between them. Aggregate readings (trace positivity)")
    print("  would allow the trade -- that is mutant M1's laundering, and the battery kills it.")

    print("\nPART D -- CLASSIFIER, NOT PINNER (the convex cone, exhibited):")
    print("  (i) independent nonnegative rescaling of each channel preserves admissibility at every")
    print("      tested scale up to 1e6 -- passivity is AMPLITUDE-HOMOGENEOUS per channel, so it can")
    print("      never bound an amplitude;")
    print("  (ii) every nonnegative ratio b/a tested (0 .. 1e6) is realized by an admissible kernel --")
    print("      passivity can never select a ratio. The no-pin fragment of X_FLOOR_MAP's route R3 is")
    print("      hereby EARNED (computed), not inherited.")
    print("  (iii) the passive witness family exists: Debye chi = 1/(1 - i omega tau) in each channel,")
    print("      omega*Im chi >= 0 for all omega (existence side, matching operator_basis PART D).")

    print("\nPART E -- the KMS lock is channel-diagonal at this level (Q3):")
    print("  N(omega) = coth(beta*omega/2) * Im K_R(omega): the thermal factor is a common scalar,")
    print("  so N decomposes on the SAME projectors and its PSD condition is the SAME two per-channel")
    print("  sign conditions. Verified both ways: the passive pair's noise is PSD at every probe, and")
    print("  a dissipation-sign violation is NOT masked by the lock (the noise inherits it).")

    print("\nPART F -- what this does NOT give (fences, per the pre-registration):")
    print("  * NO statement about x (mu_slip_interior's coupling): the x <-> c0 action-level map is")
    print("    that file's OPEN item R1; the transfer is definitional only under S_IF.md's declared")
    print("    x := normalized-c0 construction.")
    print("  * NO ceiling, NO pin (Part D is the computation of exactly that).")
    print("  * NO licence to zero any channel. Guard, verbatim (BRIEF_p_tt_interrogation.md KC4):")
    print("    passivity 'can propagate a channel's vanishing ... but can never source one'.")
    print("  * NO Israel-Stewart causality ceiling: that needs named background inputs (relaxation")
    print("    time, sound speed, entropy density) which exist nowhere in this corpus -- reclassified")
    print("    as a rung3-dispatch sub-question, never computed in-house from nothing.")

    verdict = compute_verdict(m2, m0s)
    print("\nVERDICT (recomputed, compared to frozen -- pre-registered outcome (a), FLOOR ONLY):")
    for k in FROZEN_VERDICT:
        print(f"  {k:24s} computed={verdict[k]!s:5s}  frozen={FROZEN_VERDICT[k]!s:5s}")

    ok = _selftest()
    print(f"\n  SELFTEST: {'PASS' if ok else 'FAIL'}")
    return 0 if ok else 1


# ---------------------------------------------------------------------------------------------
# Selftest: independent probes (not the report grid), multiple k-hats, every load-bearing claim.
# ---------------------------------------------------------------------------------------------

def _selftest():
    ok = True
    probes = [unit([0.3, -0.7, 0.648]), unit([1.0, 0.2, -0.4]), unit([0.0, 0.0, 1.0]),
              unit([-0.5, 0.5, 0.7071])]
    for kh in probes:
        P2, P1, P0s, P0w, MIX, T, L = projectors(kh)
        m2, m0s = mat6(P2), mat6(P0s)
        # (0) the algebra this lemma stands on, re-verified per k-hat
        if norm6(sub(mm(m2, m2), m2)) > 1e-10 or norm6(sub(mm(m0s, m0s), m0s)) > 1e-10:
            print("   [FAIL] projector idempotence"); ok = False
        if abs(tr6(mm(m2, m0s))) > 1e-10:
            print("   [FAIL] projector orthogonality"); ok = False
        # (1) the Jacobi engine itself, on a matrix with KNOWN spectrum (independent of projectors)
        D = [[0.0] * 6 for _ in range(6)]
        known = [-3.0, -1.0, 0.0, 0.5, 2.0, 7.0]
        for i in range(6):
            D[i][i] = known[i]
        # conjugate by rotations in the three disjoint planes (0,5), (2,3), (1,4) so EVERY
        # diagonal entry mixes -- no eigenvalue stays exposed on the diagonal (an audit caught
        # the first version rotating only (0,5), leaving 4 of 6 exposed: a weaker check than
        # its own comment claimed)
        R = [[1.0 if i == j else 0.0 for j in range(6)] for i in range(6)]
        for (p, q, th) in ((0, 5, 0.6), (2, 3, 1.1), (1, 4, 0.35)):
            c, s = math.cos(th), math.sin(th)
            R[p][p], R[p][q], R[q][p], R[q][q] = c, -s, s, c
        A = mm(mm(R, D), [[R[j][i] for j in range(6)] for i in range(6)])
        got = jacobi_eigenvalues(A)
        if any(abs(g - k) > 1e-9 for g, k in zip(got, sorted(known))):
            print("   [FAIL] Jacobi engine wrong on known spectrum"); ok = False
        # (2) THE LEMMA, independent probe points (both directions of the equivalence)
        for (a, b, want) in ((0.0, 0.0, True), (1.3, 0.0, True), (0.0, 0.9, True),
                             (2.0, 3.7, True), (-1e-6, 5.0, False), (5.0, -1e-6, False),
                             (-0.4, -0.4, False), (1e5, -1e-4, False), (-1e-4, 1e5, False)):
            if passive(a, b, m2, m0s) != want:
                print(f"   [FAIL] lemma equivalence at (a={a}, b={b})"); ok = False
        # (3) no-rescue is decided by the MIN eigenvalue, which must sit AT the violating channel
        _, mn = psd(kernel_matrix(1e6, -0.25, m2, m0s))
        if abs(mn - (-0.25)) > 1e-6:
            print(f"   [FAIL] min eigenvalue {mn} not pinned at the violating channel"); ok = False
        # (4) convex cone: nonnegative rescaling preserves admissibility (no ceiling), every ratio
        for lam in (1.0, 1e3, 1e6):
            if not passive(lam, 1.0, m2, m0s) or not passive(1.0, lam, m2, m0s):
                print(f"   [FAIL] rescaling by {lam} broke admissibility -- a fake ceiling"); ok = False
        for r in (0.0, 0.1, 1.0, 10.0):
            if not passive(1.0, r, m2, m0s):
                print(f"   [FAIL] ratio {r} not realized -- a fake pin"); ok = False
    # (5) the witness family is genuinely passive AND correctly oriented
    for w in (-2.0, -0.5, 0.5, 2.0):
        if w * debye_im(w) < -1e-15:
            print(f"   [FAIL] Debye witness not passive at omega={w}"); ok = False
    if debye_im(1.0) <= 0.0:
        print("   [FAIL] Debye witness orientation flipped (Im chi(+omega) must be > 0)"); ok = False
    # (6) the KMS lock carries the SIGNED dissipation (a mutant taking |Im c| must die here):
    #     coth(beta*w/2)*Im c at (w=0.7, Im c = -0.3) is NEGATIVE, and the violation must
    #     survive into the noise matrix rather than being masked.
    kh = probes[0]
    P2, P1, P0s, P0w, MIX, T, L = projectors(kh)
    m2, m0s = mat6(P2), mat6(P0s)
    nv = kms_noise_coeff(-0.3, 0.7)
    if not (nv < 0.0):
        print("   [FAIL] KMS lock lost the dissipation sign (noise masked a violation)"); ok = False
    ok_v, _ = psd(kernel_matrix(kms_noise_coeff(0.5, 0.7), nv, m2, m0s))
    if ok_v:
        print("   [FAIL] a dissipation-sign violation passed the noise PSD check"); ok = False
    # (7) the frozen verdict matches the recomputed verdict, entry for entry
    verdict = compute_verdict(m2, m0s)
    for k, want in FROZEN_VERDICT.items():
        if verdict.get(k) != want:
            print(f"   [FAIL] verdict mismatch on {k!r}: computed {verdict.get(k)}, frozen {want}"); ok = False
    return ok


if __name__ == "__main__":
    raise SystemExit(main())
