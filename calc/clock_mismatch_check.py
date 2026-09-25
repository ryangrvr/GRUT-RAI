#!/usr/bin/env python3
"""clock_mismatch_check: the one-clock recomputation of the rung3/rung7 rate comparison.

CHARTER: CLOCK_MISMATCH_CHARTER_01.md (pre-registration frozen at commit b25d79f BEFORE this
instrument ran; the transformation rule, comparison rule, reading set and verdict semantics
are fixed there and this file implements them mechanically -- no rule is invented here).

OBJECT: the stage-close addendum's finding (2026-08-19/20) that every "Ht ~ 1 versus
Ht > 4.3" comparison filed into rung3 compares two clocks without checking they are the same
one. RUNG3_KEYSTONE_MAP.md (screened 2026-08-21) derived the clock maps D1-D6 and ordered the
recomputation (its section 9.1) without performing it. This instrument performs it.

NAMED CLOCK: comoving proper time on the shared axis worldline (charter section 2; selection
forced by the screened D1/D3a derivations, which predate the charter -- no downstream GRUT
conclusion is consulted anywhere in this file, and no normalization is chosen: every
comparison below is a dimensionless ratio).

CONTROLS: the original calculations are UNTOUCHED. finite_T_pole_structure.py's ladder-share
numbers are re-derived independently here and must match (halt on miss). Background inputs are
the repository's own declared central values (Om = 0.315 flat LCDM, isw_exclusion.py:70);
H0 enters only through dimensionless products. No new numerical input.

VERDICT: exactly one of
  (A) adverse mismatch survives in a common coordinate
  (B) mismatch disappears as a coordinate artifact
  (C) comparison underdetermined: the conversion itself requires an unresolved physical input
computed by the charter's section-5 rule. Register untouched; ledger 0; banks nothing.

Pure stdlib. Run: python3 calc/clock_mismatch_check.py
"""
import hashlib
import json
import math
import os
import sys
import time

FAIL = []
CHECKS = []


def check(ok, msg, kind="ok"):
    tag = {"ok": "ok  ", "ctrl": "ctrl-DETECTED", "note": "note", "halt": "HALT"}[kind]
    line = f"  {tag if ok or kind=='note' else 'FAIL'}   {msg}"
    print(line)
    CHECKS.append({"ok": bool(ok), "kind": kind, "msg": msg})
    if not ok and kind != "note":
        FAIL.append(msg)


H = 1.0  # the dS rate; dimensionless products only, per charter (no normalization chosen)


# =============================================================================================
# S1 -- the transformation rule D1-D6, re-verified numerically from the hyperboloid embedding
# =============================================================================================
def embed_flat(t, x):
    """Flat-slicing embedding (keystone map section 1.2, screen-corrected form)."""
    a = math.exp(H * t)
    return (math.sinh(H * t) / H + 0.5 * H * a * x * x,
            a * x,
            math.cosh(H * t) / H - 0.5 * H * a * x * x)


def embed_static(T, r):
    f = math.sqrt(max(0.0, 1.0 - H * H * r * r))
    return (f * math.sinh(H * T) / H, r, f * math.cosh(H * T) / H)


def hyper(X):
    return -X[0] * X[0] + X[1] * X[1] + X[2] * X[2]


def invariant(P, Q):
    """de Sitter invariant Z = H^2 (X . X') with signature (-,+,+)."""
    return H * H * (-P[0] * Q[0] + P[1] * Q[1] + P[2] * Q[2])


def s1_transformation_rule():
    print("\n=== S1: TRANSFORMATION RULE (D1-D6), re-verified from the embedding ===")
    # constraint checks
    worst = 0.0
    for (t, x) in [(0.0, 0.0), (0.7, 0.3), (-1.2, 1.1), (2.0, 0.05)]:
        worst = max(worst, abs(hyper(embed_flat(t, x)) - 1.0 / H ** 2))
    for (T, r) in [(0.0, 0.0), (0.9, 0.5), (-0.4, 0.99), (1.5, 0.2)]:
        worst = max(worst, abs(hyper(embed_static(T, r)) - 1.0 / H ** 2))
    check(worst < 1e-12, f"both embeddings satisfy the hyperboloid constraint (worst residual {worst:.1e})")

    # ctrl: the screen-caught typo (X_i = H r n_i) must be DETECTED by the same constraint.
    # Run at h != 1, else the erroneous factor h is numerically invisible (run-1 defect, fixed).
    h, T_, r_ = 0.5, 0.9, 0.5
    f_ = math.sqrt(1.0 - h * h * r_ * r_)
    bad = (f_ * math.sinh(h * T_) / h, h * r_, f_ * math.cosh(h * T_) / h)
    check(abs((-bad[0] ** 2 + bad[1] ** 2 + bad[2] ** 2) - 1.0 / h ** 2) > 1e-3,
          "control: the pre-screen embedding typo (X_i = H r n_i) violates the constraint at H != 1 -- detected",
          "ctrl")

    # D1: axis identity T = t (the two filed clocks are the SAME clock on the shared worldline)
    worst = 0.0
    for t in (-1.5, -0.3, 0.0, 0.8, 2.4):
        X = embed_flat(t, 0.0)
        T = math.asinh(H * X[0]) / H
        worst = max(worst, abs(T - t))
    check(worst < 1e-12, f"D1 axis identity: static Killing T == cosmic t on r = 0 (worst |T-t| {worst:.1e})")

    # D2: a comoving x != 0 worldline is NOT static (its static radius moves)
    r_early = abs(embed_flat(-1.0, 0.4)[1])
    r_late = abs(embed_flat(1.0, 0.4)[1])
    check(abs(r_late - r_early) > 0.1,
          f"D2: comoving x=0.4 sits at static r={r_early:.3f} then r={r_late:.3f} -- off-axis, no shared clock")

    # D3a: equal-space invariant depends on Delta t only (worldline stationarity in cosmic time)
    worst = 0.0
    for x in (0.0, 0.3, 0.9):
        for dt in (0.4, 1.3):
            zs = [invariant(embed_flat(t0, x), embed_flat(t0 + dt, x)) for t0 in (-1.0, 0.0, 1.7)]
            worst = max(worst, max(zs) - min(zs))
            if x == 0.0:
                worst = max(worst, abs(zs[0] - math.cosh(H * dt)))
    check(worst < 1e-10,
          f"D3a: equal-space invariant reduces to cosh(H dt), independent of t0 (worst spread {worst:.1e})")

    # D3b: spatially separated pairs depend on t1+t2 as well
    z1 = invariant(embed_flat(0.0, 0.0), embed_flat(0.5, 0.6))
    z2 = invariant(embed_flat(1.0, 0.0), embed_flat(1.5, 0.6))
    check(abs(z1 - z2) > 1e-3,
          f"D3b: separated pairs at the same dt but different t0 give distinct invariants ({z1:.4f} vs {z2:.4f})")

    # D4 face-tension resolution: exp<->power-law belongs to the cosmic<->CONFORMAL pair;
    # the Killing<->cosmic axis pair is the identity (D1), so a rate per T is a rate per t there.
    G = 0.7
    worst = 0.0
    for (t1, t2) in [(0.0, 1.3), (-0.5, 2.0)]:
        eta1, eta2 = -math.exp(-H * t1) / H, -math.exp(-H * t2) / H
        worst = max(worst, abs(math.exp(-G * (t2 - t1)) - (eta2 / eta1) ** (G / H)))
    check(worst < 1e-12,
          "D4 (resolved): e^{-G dt} == (eta'/eta)^{G/H} -- the exponential/power-law mismatch attaches to the "
          f"conformal pair, while the Killing/cosmic axis pair is the identity (worst {worst:.1e})")
    check(True, "D6 carried: T_dS = H/2pi is defined on the Killing flow; D3a gives the same temperature "
                "along comoving worldlines -- transport beyond those scopes stays an assumption (keystone)", "note")


# =============================================================================================
# S2 -- Q-rung3 control reproduction (originals untouched; independent re-derivation must match)
# =============================================================================================
def share_closed(Ht):
    x = math.exp(-Ht)
    return (1 - x) ** 4 / (1 + 4 * x + x * x)


def share_sum(Ht, nmax=6000):
    x = math.exp(-Ht)
    return x / sum(n ** 3 * x ** n for n in range(1, nmax + 1))


def bisect_share(target, lo, hi):
    for _ in range(200):
        mid = 0.5 * (lo + hi)
        if share_closed(mid) < target:
            lo = mid
        else:
            hi = mid
    return hi


def s2_control():
    print("\n=== S2: CONTROL REPRODUCTION (frozen toy numbers; halt on miss) ===")
    worst = max(abs(share_closed(u) - share_sum(u)) for u in (0.5, 1.0, 2.0, 4.33, 6.68))
    check(worst < 1e-12, f"closed form matches direct n^3-weighted summation (worst {worst:.1e})")
    s1v = share_closed(1.0)
    t90 = bisect_share(0.90, 1.0, 20.0)
    t99 = bisect_share(0.99, 1.0, 40.0)
    check(abs(s1v - 0.0612) < 0.001, f"share(Ht=1) = {s1v*100:.2f}% (frozen: 6.1%)")
    check(abs(t90 - 4.33) < 0.02, f"t90 = {t90:.3f} (frozen: 4.33)")
    check(abs(t99 - 6.68) < 0.02, f"t99 = {t99:.3f} (frozen: 6.68)")
    # ctrl: a wrong-weight mutant (n^2) must NOT reproduce the frozen numbers
    x = math.exp(-1.0)
    mut = x / sum(n ** 2 * x ** n for n in range(1, 6000))
    check(abs(mut - 0.0612) > 0.01, f"control: n^2-weight mutant gives {mut*100:.1f}% at Ht=1, not 6.1% -- detected", "ctrl")
    check(True, "tower rates carried at cited strength: lowest (l+1)H, l=2 graviton -> 3H per Killing time; "
                "E4 retraction rides along (frequencies not established quasinormal; free response pole-free)", "note")
    return {"share_at_1": s1v, "t90": t90, "t99": t99}


# =============================================================================================
# S3 -- the FRW side in the named clock (repo central background, Om = 0.315 flat LCDM)
# =============================================================================================
OM = 0.315
OL = 1.0 - OM


def Efunc(a):
    return math.sqrt(OM / a ** 3 + OL)


def age(a_end, n=200000):
    """H0 * t(a_end) = int_0^a da / (a E(a)); integrand = sqrt(a)/sqrt(Om + OL a^3) -- regular."""
    total = 0.0
    h = a_end / n
    def f(a):
        return math.sqrt(a) / math.sqrt(OM + OL * a ** 3)
    for i in range(n):
        a0, a1 = i * h, (i + 1) * h
        total += (f(a0) + 4.0 * f(0.5 * (a0 + a1)) + f(a1)) * h / 6.0
    return total


def s3_frw(ctl):
    print("\n=== S3: THE FRW SIDE IN THE NAMED CLOCK ===")
    # integrator validation on the exact matter-only law a ~ t^{2/3}: H0 t0 = 2/3
    global OM, OL
    OM_save, OL_save = OM, OL
    OM, OL = 1.0, 0.0
    t_ein = age(1.0)
    OM, OL = OM_save, OL_save
    check(abs(t_ein - 2.0 / 3.0) < 1e-6, f"integrator control: Om=1 gives H0 t0 = {t_ein:.6f} (exact 2/3)")

    t0 = age(1.0)
    check(abs(t0 - 0.951) < 0.01, f"H0 t0 = {t0:.4f} for Om = {OM} (the repo's declared background)")
    zL = (OL / OM) ** (1.0 / 3.0) - 1.0
    tL = age(1.0 / (1.0 + zL))
    lagL = t0 - tL
    check(True, f"Lambda-domination onset: z_L = {zL:.3f}; lag since then = {lagL:.4f}/H0", "note")
    z_thresh90 = math.exp(ctl["t90"]) - 1.0
    z_thresh99 = math.exp(ctl["t99"]) - 1.0
    check(True, f"e-fold clock: DN(z_on) = ln(1+z_on) crosses t90 = {ctl['t90']:.2f} at z_on = {z_thresh90:.0f} "
                f"and t99 = {ctl['t99']:.2f} at z_on = {z_thresh99:.0f}", "note")
    Tvar90 = Efunc(1.0 / (1.0 + z_thresh90))
    check(True, f"fixed-T premise factor (priced, not disqualifying): across the up-to-t90 span the "
                f"would-be ladder temperature T = H(z)/2pi varies by H(z={z_thresh90:.0f})/H0 = {Tvar90:.0f}x", "note")
    return {"H0_t0": t0, "z_Lambda": zL, "lag_since_zL": lagL,
            "z_onset_for_t90": z_thresh90, "z_onset_for_t99": z_thresh99, "T_variation_factor_t90": Tvar90}


# =============================================================================================
# S4 -- the declared reading set (charter section 6): ALL computed, NONE selected
# =============================================================================================
def s4_readings(ctl, frw):
    print("\n=== S4: DECLARED READING SET (all computed, none selected) ===")
    t90 = ctl["t90"]
    rows = []

    def row(rid, desc, D, needs, defined=True):
        side = ("UNDEFINED" if not defined else ("AT/ABOVE t90" if D >= t90 else "BELOW t90"))
        rows.append({"id": rid, "reading": desc, "D": (None if not defined else D),
                     "vs_t90": side, "unbanked_input": needs})
        dtxt = "--" if not defined else f"{D:.3f}"
        print(f"  {rid}: D = {dtxt:>8}  [{side}]  {desc}")
        print(f"        requires: {needs}")

    # R1: as filed -- lag = tau_2 = 1/H0, H frozen at H0
    row("R1", "lag tau_2 = 1/H0, H_bath frozen at H0 (the filed reading)", 1.0,
        "dS->FRW identification H_bath = H0 (constant-H kernel applied on a non-constant-H solution)")
    check(1.0 > frw["H0_t0"],
          f"R1 rider (computed): the filed lag 1/H0 EXCEEDS the age of the universe ({frw['H0_t0']:.3f}/H0) -- "
          "the kernel is probed at a lag longer than the available history of the background it is applied to")

    # R2: lag = t0 (all available history), H frozen at H0
    row("R2", "lag t0 (all available history), H_bath frozen at H0", frw["H0_t0"],
        "same identification, plus onset = initial time")

    # R3: lag = time since Lambda-domination, H frozen at H0
    row("R3", f"lag since z_L = {frw['z_Lambda']:.2f}, H_bath frozen at H0", frw["lag_since_zL"],
        "same identification, plus onset = Lambda-domination")

    # R4: contemporaneous e-fold promotion, three lags
    row("R4a", "e-fold clock, lag tau_2 = 1/H0 before today", 0.0,
        "adiabatic promotion H -> H(z) of a constant-H kernel; lag reaches before the initial time",
        defined=False)
    row("R4b", f"e-fold clock, onset z_on >= {frw['z_onset_for_t90']:.0f} (DN = ln(1+z_on) >= t90)",
        math.log(1.0 + frw["z_onset_for_t90"]),
        f"adiabatic promotion H -> H(z); fixed-T ladder premise varies {frw['T_variation_factor_t90']:.0f}x over the span")
    row("R4c", f"e-fold clock, onset z_L = {frw['z_Lambda']:.2f}", math.log(1.0 + frw["z_Lambda"]),
        "adiabatic promotion H -> H(z), onset = Lambda-domination")

    # R5: conformal control only (not a physical reading)
    check(True, "R5 control: in conformal time the ladder exponentials are power laws (S1/D4) -- rate language "
                "is clock-form-dependent; computed as control only, never a candidate reading (charter 6)", "note")
    return rows


# =============================================================================================
# S5 -- verdict, by the pre-registered rule (charter section 5), mechanically
# =============================================================================================
def s5_verdict(rows, ctl, frw):
    print("\n=== S5: VERDICT (charter section-5 rule, mechanical) ===")
    t90 = ctl["t90"]

    # Comparability test (facts pre-registered in the charter):
    #  - the toy kernel is derived on constant-H dS (exact); tau_2 lives on FRW with Om != 0;
    #  - the 2026-08-19 X2 refusal records these as DIFFERENT SOLUTIONS;
    #  - the register prices the background-flow question as the +1 omission
    #    background_time_translation_flow.
    # Therefore every reading in the declared set carries a non-empty unbanked_input field:
    all_need_input = all(r["unbanked_input"] for r in rows)
    check(all_need_input, "comparability test: every declared reading requires an identification beyond D1-D6 "
                          "(the D1 identity removes the CLOCK difference, not the BACKGROUND difference)")

    defined = [r for r in rows if r["D"] is not None]
    below = [r["id"] for r in defined if r["D"] < t90]
    above = [r["id"] for r in defined if r["D"] >= t90]
    flip = bool(below) and bool(above)
    print(f"  below t90: {below}   at/above t90: {above}   undefined: "
          f"{[r['id'] for r in rows if r['D'] is None]}")

    if not all_need_input:
        verdict = "A" if not above else "B"  # direct comparability branch (not reached on the recorded facts)
    elif flip:
        verdict = "C"
    else:
        verdict = "A" if not above else "B"
    check(verdict == "C",
          "verdict = (C): the comparison is underdetermined -- the D1 identity makes the two filed clocks THE "
          "SAME clock on the shared worldline (not (B): no coordinate re-expression changes any number), and "
          "the shortfall is not invariant (not (A)): the verdict flips between the H0-frozen readings "
          "(R1/R2/R3 below t90) and the e-fold promotion (R4b at/above t90), so it is decided by WHICH "
          "unbanked identification carries the constant-H kernel onto the FRW solution")
    print("\n  NAMED UNRESOLVED INPUTS (each flips or defines the verdict):")
    print("   1. the dS->FRW kernel transport rule: H_bath = H0 (frozen) vs the adiabatic promotion")
    print("      H -> H(z) -- different solutions per the X2 refusal; priced in the register only as the")
    print("      +1 omission background_time_translation_flow, never as a usable rule;")
    print("   2. the onset/lag specification (elapsed-since-when vs the relaxation constant tau_2 --")
    print("      the keystone map's surviving defect (i)); R4a is UNDEFINED and R4b/R4c straddle t90;")
    print("   3. the D3b reduction: whether rung3's asserted object (static-patch tower / assembled TT")
    print("      response) reduces to an along-worldline kernel at all (wall A) -- without it the toy's")
    print("      licensed scope (D3a) does not cover the object the comparison is about.")
    print("\n  SUB-FINDINGS (scope, not verdict):")
    print("   - the pure Killing-vs-cosmic clock concern is EXONERATED on the axis: T = t exactly (D1),")
    print("     so the addendum's 'two clocks' framing dissolves at along-worldline scope; the real seam")
    print("     is two BACKGROUNDS, not two clocks;")
    print("   - the within-toy statement STANDS (control reproduced exactly: 6.1% / 4.33 / 6.68) -- the")
    print("     ladder-dominance shortfall is coherent inside the toy's own stationary clock;")
    print(f"   - the fixed-T premise factor prices R4b at ~{frw['T_variation_factor_t90']:.0f}x temperature variation across its span:")
    print("     the e-fold escape is not free -- it is a different (unbanked) kernel, not a re-reading.")
    return verdict


# =============================================================================================
def main():
    t_start = time.time()
    print("CLOCK-MISMATCH INSTRUMENT -- the one-clock recomputation (charter: CLOCK_MISMATCH_CHARTER_01.md,")
    print("pre-registration frozen at commit b25d79f before this run)")
    s1_transformation_rule()
    ctl = s2_control()
    if FAIL:
        print("\nHALT: control reproduction or transformation verification failed; NO VERDICT is issued.")
        sys.exit(1)
    frw = s3_frw(ctl)
    rows = s4_readings(ctl, frw)
    verdict = s5_verdict(rows, ctl, frw)

    out = {
        "instrument": "clock_mismatch_check",
        "charter": "CLOCK_MISMATCH_CHARTER_01.md",
        "charter_commit": "b25d79f",
        "date": "2026-09-25",
        "declarations": {
            "named_clock": "comoving proper time on the shared axis worldline (D1: = static Killing there)",
            "background": {"Om": OM, "OL": OL, "source": "calc/isw_exclusion.py:70 (repo central)"},
            "controls_untouched": ["calc/finite_T_pole_structure.py", "calc/two_scale_desitter.py",
                                   "calc/wz_dark_energy.py", "calc/static_patch_tt_response.py"],
        },
        "control_reproduction": ctl,
        "frw": frw,
        "readings": rows,
        "verdict": verdict,
        "verdict_text": "(C) underdetermined: the conversion itself requires an unresolved physical input",
        "named_inputs": [
            "dS->FRW kernel transport rule (H_bath = H0 vs adiabatic H -> H(z); different solutions per X2; "
            "priced only as the +1 omission background_time_translation_flow)",
            "onset/lag specification (elapsed-time vs relaxation-constant; keystone defect (i))",
            "D3b reduction of the assembled object to an along-worldline kernel (wall A)",
        ],
        "sub_findings": [
            "pure Killing-vs-cosmic exonerated on the axis (D1 identity): the seam is two backgrounds, not two clocks",
            "within-toy statement stands (6.1% at Ht=1; t90=4.33; t99=6.68 reproduced)",
            f"fixed-T premise factor ~{frw['T_variation_factor_t90']:.0f}x prices the e-fold escape as a different unbanked kernel",
        ],
        "checks": CHECKS,
        "failures": FAIL,
        "elapsed_s": round(time.time() - t_start, 2),
        "hard_stop": "verdict recorded; owner selects the next instrument; Lambda_R/Matsubara/Pi_0/U5 fenced "
                     "until then per the owner charter",
    }
    path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "CLOCK_MISMATCH_RESULT.json")
    path = os.path.normpath(path)
    blob = json.dumps(out, indent=1, sort_keys=True).encode()
    with open(path, "wb") as fh:
        fh.write(blob)
    sha = hashlib.sha256(open(path, "rb").read()).hexdigest()
    print(f"\nartifact written: {path} (sha {sha[:16]}...)")
    n_ok = sum(1 for c in CHECKS if c["ok"])
    print(f"\nCLOCK-MISMATCH INSTRUMENT: {n_ok}/{len(CHECKS)} checks passed; failures: {len(FAIL)}")
    print("HARD STOP: verdict (C) recorded pending owner selection of the next instrument.")
    sys.exit(0 if not FAIL else 1)


if __name__ == "__main__":
    main()
