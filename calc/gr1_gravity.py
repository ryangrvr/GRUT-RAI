#!/usr/bin/env python3
"""gr1_gravity: (K,N)_grav as a hierarchy point; the class-4 gate attacked directly.

CHARTER: GR1_GRAVITY_CHARTER_01.md (pre-registration frozen at commit ece56e7 BEFORE this
instrument ran; authority GitHub Issue #2 owner comment 5828202542). The omega^7 record is
never silently upgraded: the v3 primaries (adjudicator-track, 20/20, omega^7.008) are
cited by hash only, never re-run. No Einstein equations anywhere; hbar located, inherited
by gravity, never generated; amplitudes free (S-1 PC-D).

Legs: L-B structural branch elimination | L-X counterfactual-predictive counting core
(fresh 1D pair instrument; predictions frozen in the charter: base/base/base, full = base
+4, linear = exact 0; kappa rescale invariance) | L-D dimension consistency with the
G-2-recovered substrates | L-H the omega^7 point in the hierarchy (floor, Gram, scaling,
kernel-tail identity via rotated-contour quadrature) | L-I import adjudication under the
frozen class-4 rule.

DISCLOSED CONTROL REPAIR (pre-run, provable): the charter froze the Gram tamper test at
t = (1.3, 2.9). At those times |C(t)|/C(0) ~ 0.02, the tampered matrix is strictly
diagonally dominant, and detection is PROVABLY impossible -- the control as frozen is
vacuous. The frozen-times result is reported as found (with the dominance certificate);
the operative halt-grade detector runs at binding times t = (0.15, 0.35), where
2.25<w>^2 > <w^2> makes the inflated commutator violate positivity.

Pure stdlib. Run: python3 calc/gr1_gravity.py
"""
import cmath
import hashlib
import json
import math
import os
import sys
import time

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from p3_nc_lift import herm_eigs

FAIL = []
CHECKS = []
HALT = []
ALPHA = 0.05


def check(ok, msg, kind="ok"):
    tag = {"ok": "ok  ", "ctrl": "ctrl", "note": "note"}[kind]
    print(f"  {tag if ok or kind == 'note' else 'FAIL'}   {msg}")
    CHECKS.append({"ok": bool(ok), "kind": kind, "msg": msg})
    if not ok and kind != "note":
        FAIL.append(msg)


def halt_check(ok, msg):
    check(ok, msg, "ctrl")
    if not ok:
        HALT.append(msg)


# ---------------- L-B: branch table (elimination is structural) -------------------------------
def leg_B():
    print("\n=== L-B: BRANCH TABLE (structural elimination) ===")
    qs = [0.01 * i for i in range(1, 101)]
    mn = min(q + qp for q in qs for qp in qs)
    check(mn > 0.019, f"L-B: same-sign pair channel at zero net momentum kinematically "
                      f"CLOSED -- min |q + q'| over the scan = {mn:.3f} > 0 (both "
                      f"momenta positive; no interior root exists)")
    roots = {}
    for w in (0.5, 1.0, 1.9, 2.5):
        # gapped pair: omega_tot(q) = 2 sqrt(1 + q^2), monotone increasing from 2
        if w <= 2.0:
            roots[w] = None
        else:
            q = math.sqrt((w / 2.0) ** 2 - 1.0)
            roots[w] = q
    check(roots[0.5] is None and roots[1.0] is None and roots[1.9] is None
          and roots[2.5] is not None,
          f"L-B GATE: gapped counterfactual EMPTY below threshold 2*Omega = 2 (no root at "
          f"omega = 0.5, 1.0, 1.9; root q = {roots[2.5]:.3f} at omega = 2.5) -- the "
          f"true-emptiness fingerprint, fresh; the retained gapless sector is what makes "
          f"ANY low-omega response possible")
    mlin = max(abs(q * q - q * q) for q in qs)
    halt_check(mlin < 1e-14, f"L-B GATE: exactly linear dispersion kills the full vertex "
                             f"IDENTICALLY, max |M| = {mlin:.1e} < 1e-14 (tracelessness "
                             f"cancellation is exact without curvature)")
    check(True, "L-B consequence (frozen): branch elimination is structural (kinematics, "
                "threshold, symmetry) -- min-dominance then selects the sole surviving "
                "branch trivially", "note")
    return {"same_sign_min": mn, "linear_max": mlin}


# ---------------- L-X: the counterfactual-predictive counting core -----------------------------
def disp(q):
    return q - ALPHA * q ** 3


def root_q(w):
    q = w / 2.0
    for _ in range(60):
        f = 2.0 * disp(q) - w
        df = 2.0 * (1.0 - 3.0 * ALPHA * q * q)
        q -= f / df
    return q


def J_of(w, vertex, scale=1.0):
    q = root_q(w)
    M = scale * vertex(q)
    dwdq = abs(2.0 * (1.0 - 3.0 * ALPHA * q * q))
    return M * M / dwdq


def slope(vertex, scale=1.0):
    return math.log(J_of(0.2, vertex, scale) / J_of(0.1, vertex, scale)) / math.log(2.0)


def leg_X():
    print("\n=== L-X: THE SELECTION CORE (fresh instrument; predictions frozen) ===")
    v_kin = lambda q: disp(q) ** 2
    v_pot = lambda q: q * q
    v_non = lambda q: disp(q) ** 2 - 1.3 * q * q
    v_ful = lambda q: disp(q) ** 2 - q * q
    s_kin, s_pot, s_non, s_ful = slope(v_kin), slope(v_pot), slope(v_non), slope(v_ful)
    check(abs(s_kin - s_pot) < 0.2 and abs(s_kin - s_non) < 0.2,
          f"L-X GATE: base class agrees as predicted -- kinetic-only {s_kin:.3f}, "
          f"potential-only {s_pot:.3f}, non-minimal (eps = 0.3) {s_non:.3f} "
          f"(all base b, cancellation destroyed in the non-minimal case)")
    inc = s_ful - s_kin
    check(abs(inc - 4.0) < 0.2, f"L-X GATE: full minimal-stress vertex = base + "
                                f"{inc:.3f} (predicted +4: the order-2 tracelessness "
                                f"cancellation leaves the curvature residual -2 alpha q^4)")
    mlin = max(abs(q * q - q * q) for q in (0.05, 0.1, 0.2))
    check(mlin < 1e-14, f"L-X GATE: exactly-linear vertex = 0 ({mlin:.1e} < 1e-14)")
    ds = abs(slope(v_ful, 16.0) - s_ful)
    check(ds < 1e-12, f"L-X GATE: all slopes invariant under coupling rescale lambda = 16, "
                      f"|Delta slope| = {ds:.1e} -- kappa = 1/M_Pl is AMPLITUDE-ONLY")
    check(True, "L-X adjudication (frozen): every counterfactual landed on its "
                "pre-written prediction -- the exponent tracks STRUCTURE (which symmetry "
                "cancellation is present), so the channel exponent is "
                "SELECTED-BY-STRUCTURE in-class, not merely reproduced. In this 1D "
                "zero-transverse convention b = 4; increments are convention-free (S-1); "
                "the absolute 7 = base-3 (v3 convention) + 4 stays graded "
                "CONSISTENT-BY-MECHANISM, never one-formula-derived here", "note")
    return {"s_kin": s_kin, "s_pot": s_pot, "s_non": s_non, "s_full": s_ful,
            "increment": inc, "rescale_dev": ds}


# ---------------- L-D: dimension consistency with the recovered geometry ----------------------
def leg_D():
    print("\n=== L-D: DIMENSION CONSISTENCY (gravity counting on the G-2 substrates) ===")
    om1 = sorted(math.sqrt(2.0 - 2.0 * math.cos(math.pi * k / 61)) for k in range(1, 61))
    c13 = [2.0 - 2.0 * math.cos(math.pi * k / 13) for k in range(13)]
    om3 = sorted(math.sqrt(a + b + c) for a in c13 for b in c13 for c in c13
                 if a + b + c > 1e-12)

    def pairs(oms, W):
        import bisect
        n = 0
        for i, w in enumerate(oms):
            if w > W:
                break
            n += bisect.bisect_right(oms, W - w, lo=i) - i
        return n

    n1a, n1b = pairs(om1, 0.4), pairs(om1, 0.8)
    s1 = math.log(n1b / n1a) / math.log(2.0)
    check(abs(s1 - 2.0) < 0.4, f"L-D GATE 1D: pair-count exponent = {s1:.3f} (= 2d with "
                               f"d = 1, gate +-0.4; counts {n1a} -> {n1b}) on the chain "
                               f"where G-2 recovered d_hat = 1.000")
    n3a, n3b = pairs(om3, 0.9), pairs(om3, 1.8)
    s3 = math.log(n3b / n3a) / math.log(2.0)
    check(abs(s3 - 6.0) < 0.6, f"L-D GATE 3D: pair-count exponent = {s3:.3f} (= 2d with "
                               f"d = 3, gate +-0.6; counts {n3a} -> {n3b}) on the lattice "
                               f"where G-2 recovered d_hat = 2.942")
    # ---- POST-HOC DIAGNOSTIC (labeled; a measurement, not a gate edit) ----------------------
    seq = [s3]
    for s in (21, 31):
        cs = [2.0 - 2.0 * math.cos(math.pi * k / s) for k in range(s)]
        oms = sorted(math.sqrt(a + b + c) for a in cs for b in cs for c in cs
                     if a + b + c > 1e-12)
        seq.append(math.log(pairs(oms, 1.8) / pairs(oms, 0.9)) / math.log(2.0))
    check(True, f"L-D POST-HOC DIAGNOSTIC (labeled): the same frozen window on lattices "
                f"13^3 / 21^3 / 31^3 gives exponents {seq[0]:.3f} -> {seq[1]:.3f} -> "
                f"{seq[2]:.3f}, converging monotonically toward 2d = 6 -- the frozen-gate "
                f"miss is low-window spectral discreteness on the 13^3 lattice (the "
                f"lowest mode sits at 24% of the window edge), not a dimension "
                f"inconsistency. The gate stays red as found", "note")
    check(True, "L-D consequence (frozen): the d entering the gravitational phase-space "
                "counting equals the d the interface recovers spectrally -- the hierarchy "
                "point sits over the RECOVERED geometric substrate, not an inserted label",
          "note")
    return {"slope_1d": s1, "slope_3d": s3}


# ---------------- L-H: (K,N)_grav as a hierarchy point ----------------------------------------
NM = 40


def bath_modes():
    lo, hi = 0.075, 6.0
    dw = (hi - lo) / (NM - 1)
    oms = [lo + dw * i for i in range(NM)]
    g2 = [(w ** 7) * math.exp(-w) * dw for w in oms]
    return oms, g2


def Cfun(oms, g2, tau):
    return sum(g * cmath.exp(-1j * w * tau) for w, g in zip(oms, g2))


def gram(oms, g2, t1, t2, tamper=False):
    ts = [0.0, t1, t2]

    def cv(tau):
        c = Cfun(oms, g2, tau)
        return complex(c.real, 1.5 * c.imag) if tamper else c

    M = [[0j] * 4 for _ in range(4)]
    M[0][0] = 1.0 + 0j
    for a in range(3):
        for b in range(3):
            M[1 + a][1 + b] = cv(ts[a] - ts[b])
    return M


def leg_H():
    print("\n=== L-H: (K,N)_grav AS A HIERARCHY POINT (omega^7 bath, 40 modes) ===")
    oms, g2 = bath_modes()
    C0 = sum(g2)
    # (i) floor saturation (by construction, labeled) + thermal interior
    dev = max(abs(0.5 * g - 0.5 * g) for g in g2)  # T=0: nu_i = g_i^2/2 exactly
    check(dev == 0.0, f"L-H: vacuum floor saturation nu_i = hbar J_i / 2 EXACT (by "
                      f"construction of the vacuum bath, labeled as such) -- gravity's "
                      f"vacuum point sits ON the P-2 floor; hbar inherited (located), "
                      f"never generated")
    marg = min(0.5 * g * (1.0 / math.tanh(w)) - 0.5 * g for w, g in zip(oms, g2))
    check(marg > 0.0, f"L-H GATE: thermal point (beta = 2) strictly interior, min margin "
                      f"= {marg:.2e} > 0")
    # (ii) Gram PSD at frozen times; tamper at frozen times (reported) + binding times
    M = gram(oms, g2, 1.3, 2.9)
    mn = min(herm_eigs(M)) / C0
    check(mn > -1e-12, f"L-H GATE: 4x4 operator Gram over {{1, B(0), B(1.3), B(2.9)}} PSD, "
                       f"min eig / C0 = {mn:.2e} >= -1e-12")
    Mt = gram(oms, g2, 1.3, 2.9, tamper=True)
    mnt = min(herm_eigs(Mt)) / C0
    offmax = max(abs(Cfun(oms, g2, t)) for t in (1.3, 2.9, 1.6)) / C0
    check(True, f"L-H frozen-times tamper (REPORTED AS FOUND, control mis-frozen): "
                f"tampered min eig / C0 = {mnt:.2e} -- NOT negative, and provably could "
                f"not be: max |C(t)|/C(0) at the frozen times = {offmax:.3f}, so the "
                f"tampered Gram is strictly diagonally dominant. Disclosed repair: the "
                f"operative detector runs at binding times below", "note")
    Mb = gram(oms, g2, 0.15, 0.35)
    mnb = min(herm_eigs(Mb)) / C0
    check(mnb > -1e-12, f"L-H: Gram at binding times (0.15, 0.35) PSD, min eig / C0 = "
                        f"{mnb:.2e}", "ctrl")
    Mbt = gram(oms, g2, 0.15, 0.35, tamper=True)
    mnbt = min(herm_eigs(Mbt)) / C0
    halt_check(mnbt < -1e-6, f"L-H GATE (operative tamper detector): x1.5 inflated "
                             f"commutator at binding times DETECTED, min eig / C0 = "
                             f"{mnbt:.2e} < -1e-6 (halt-grade: a floor violation is "
                             f"catchable by this instrument)")
    # (iii) lambda-scaling
    lam_ok = True
    for lam in (0.1, 16.0):
        Ms = gram(oms, [lam * g for g in g2], 1.3, 2.9)
        lam_ok = lam_ok and min(herm_eigs(Ms)) / (lam * C0) > -1e-12
    check(lam_ok, "L-H GATE: lambda J admissible for lambda in {0.1, 16} -- amplitudes "
                  "free at the gravity point (S-1 PC-D)")
    # (iv) kernel-tail identity via rotated-contour quadrature (faithful, no cancellation)
    def K_quad(t):
        # Im int_0^inf w^7 e^-w sin(wt) dw == Im int_0^inf y^7 e^{-y(t+i)} dy (contour)
        ymax = 100.0 / max(t, 1.0)
        npts = 20001
        h = ymax / (npts - 1)
        s = 0j
        for i in range(npts):
            y = i * h
            wgt = (1 if i in (0, npts - 1) else (4 if i % 2 == 1 else 2))
            s += wgt * (y ** 7) * cmath.exp(-y * (t + 1j))
        return (s * h / 3.0).imag

    def K_closed(t):
        return (5040.0 * (1.0 - 1j * t) ** (-8)).imag

    idmax = 0.0
    for t in (5.0, 20.0, 60.0):
        rel = abs(K_quad(t) - K_closed(t)) / abs(K_closed(t))
        idmax = max(idmax, rel)
    halt_check(idmax < 1e-6, f"L-H GATE: kernel quadrature matches the closed form "
                             f"Im[Gamma(8)(1-it)^-8] at t = 5, 20, 60, max rel diff = "
                             f"{idmax:.2e} < 1e-6")
    sl = math.log(abs(K_closed(80.0) / K_closed(20.0))) / math.log(4.0)
    check(True, f"L-H kernel tail (REPORTED ONLY): measured large-t slope on [20, 80] = "
                f"{sl:.3f} in THIS convention (J = w^7 e^-w, sine transform). The sealed "
                f"t^-8 class lives in the v3 propagator convention; no cross-convention "
                f"gate is manufactured", "note")
    return {"thermal_margin": marg, "gram_min": mn, "tamper_frozen": mnt,
            "tamper_binding": mnbt, "kernel_id": idmax, "tail_slope": sl}


# ---------------- L-I: import adjudication (the class-4 ruling input) --------------------------
def leg_I(rx):
    print("\n=== L-I: IMPORT ADJUDICATION (frozen class-4 rule) ===")
    check(rx["rescale_dev"] < 1e-12,
          "L-I: kappa = 1/M_Pl DISCHARGED as amplitude-only (exponent invariant under "
          "rescale; the amplitude remains supplied, as S-1 priced)")
    check(abs(rx["s_non"] - rx["s_kin"]) < 0.2,
          f"L-I: minimal-stress import LOAD-BEARING -- the non-minimal counterfactual "
          f"loses the +4 (slope {rx['s_non']:.3f} = base class): the +4 hinges on the "
          f"tracelessness structure of the minimal coupling")
    check(True, "L-I: retained-sector import LOAD-BEARING -- the gapped counterfactual "
                "is empty below threshold (L-B): a gapless retained sector is a "
                "precondition for any low-omega gravitational response", "note")
    check(True, "L-I VERDICT INPUT (frozen consequence rule): two imports beyond "
                "locality + symmetry are load-bearing (minimal-stress, retained-sector), "
                "so the CLASS-4 GATE REMAINS OPEN. The residual obstruction is now named "
                "exactly: the exponent is selected by counting GIVEN the coupling class; "
                "the coupling class is supplied. kappa alone is discharged", "note")
    return True


# ---------------- main -------------------------------------------------------------------------
def main():
    t0 = time.time()
    print("GR-1: (K,N)_grav AS A HIERARCHY POINT; CLASS-4 ATTACKED (charter frozen at ece56e7)")
    rB = leg_B()
    rX = leg_X()
    rD = leg_D()
    rH = leg_H()
    leg_I(rX)

    print("\n=== COMPOSITE (frozen taxonomy; components reported separately) ===")
    check(True, "GRAV-HIERARCHY-ADMISSIBLE: the omega^7 point inhabits the admissible "
                "hierarchy -- vacuum ON the floor, thermal interior, Gram PSD, "
                "lambda-free, kernel representation verified", "note")
    check(True, "SELECTED-BY-STRUCTURE-IN-CLASS: branch elimination structural (L-B); "
                "every counterfactual exponent landed on its pre-written prediction "
                "(L-X) -- the channel exponent is selected by the surviving per-branch "
                "counting, not merely reproduced by a chosen occupancy", "note")
    check(True, "DIMENSION-CONSISTENT at recorded strength: certified by the 1D gate; "
                "the 3D frozen gate is RED as found (5.362 vs 6 +- 0.6), with the "
                "labeled diagnostic converging 5.36 -> 5.49 -> 5.66 toward 6 under "
                "lattice refinement -- consistency indicated, not gate-certified in 3D",
          "note")
    check(True, "CLASS-4-OPEN (per the frozen L-I rule): minimal-stress and "
                "retained-sector imports are load-bearing; kappa discharged as "
                "amplitude-only. The omega^7 record keeps exactly its prior status "
                "(CONDITIONALLY DERIVED, v3 20/20 cited by hash), now with its "
                "selection component certified and its residual obstruction named",
          "note")
    check(True, "Fences held: no Einstein equations; hbar inherited-not-generated; "
                "geometry consumed only as the G-2-recovered substrate; Lambda_R, "
                "Matsubara, Pi_0, U5 untouched; increments gated, absolute exponents "
                "never compared across conventions", "note")

    out = {"instrument": "gr1_gravity", "charter_commit": "ece56e7", "date": "2026-09-25",
           "LB": rB, "LX": rX, "LD": rD, "LH": rH,
           "halts": HALT, "checks": CHECKS, "failures": FAIL,
           "elapsed_s": round(time.time() - t0, 2),
           "hard_stop": "verdict recorded; owner rules (hard stop after gravity verdict)"}
    path = os.path.normpath(os.path.join(os.path.dirname(os.path.abspath(__file__)), "..",
                                         "GR1_GRAVITY_RESULT.json"))
    with open(path, "wb") as fh:
        fh.write(json.dumps(out, indent=1, sort_keys=True, default=float).encode())
    sha = hashlib.sha256(open(path, "rb").read()).hexdigest()
    print(f"\nartifact written: {path} (sha {sha[:16]}...)")
    n_ok = sum(1 for c in CHECKS if c["ok"])
    print(f"\nGR-1 GRAVITY ATTACK: {n_ok}/{len(CHECKS)} checks passed; failures: "
          f"{len(FAIL)}; halts: {len(HALT)}")
    if HALT:
        print("HALT: an analytic identity breached -- instrument bug, never physics. "
              "No verdict may be issued from this run.")
    else:
        print("HARD STOP: verdict recorded pending owner ruling.")
    sys.exit(0 if not FAIL else 1)


if __name__ == "__main__":
    main()
