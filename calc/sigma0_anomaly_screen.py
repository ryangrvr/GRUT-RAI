#!/usr/bin/env python3
"""sigma0_anomaly_screen: SCREEN the Du et al. (arXiv:2602.03110) Sigma_0 anomaly against GRUT's
interior family. NOTHING HERE IS BANKED. This is a screen, and it is default-broken TOWARD the
anomaly being less informative than it looks.

WHY DEFAULT-BROKEN THAT WAY. This is the first observational result in the program's history that
lands INSIDE GRUT's own channel rather than being invisible to it. CHARTER Sec.4 says a predicted
scale landing near an observed one is "scrutinized hardest, never celebrated", and Sec.1 discipline 4
says the loop over-claims toward strengthening the result. Both fire here at maximum strength.

THE SOURCE, VERIFIED IN-SESSION 2026-08-05 by fetching the arXiv abstract page:
  Du, Li, Liu, Zhang & Zhang, "Evidence for deviation in gravitational light deflection from general
  relativity at cosmological scales with KiDS-Legacy and CMB lensing", arXiv:2602.03110
  (submitted 2026-02-03, revised 2026-04-28).
  FULL PDF READ 2026-08-05; every number below is off the source's own Table I, not recalled.
  LCDM  background: Sigma_0 = 0.149 +/- 0.051 (3.0 sigma), mu_0 = 0.21 +/- 0.21
  w0waCDM background: Sigma_0 = 0.115 +/- 0.053 (2.2 sigma), mu_0 = 0.09 +0.28/-0.24
                      (w0 = -0.827 +/- 0.055, wa = -0.59 +/- 0.21)
  authors' own caveat: "likely driven by the higher amplitudes in the large-scale CMB lensing
  measurements"; and on the background swing: "the introduction of a dynamical DE background
  absorbs a fraction of the anomalous lensing signal" -- a PARAMETER DEGENERACY, their words.
  Their own model comparison PREFERS the dynamical background: Delta-DIC = -12.64 (w0waCDM) and
  -14.36 (mu0Sigma0w0wa) relative to LCDM.
Data: KiDS-Legacy WL (1347 deg^2, z<=2.0) + Planck/ACT/SPT CMB + DESI DR2 BAO + DES-Dovekie SNe.

*** THE PARAMETERIZATION, verified from the source (their Eqs. 6-7) -- THE F-MAP FENCE FIRES: ***
    mu(a)    = 1 + mu_0    * Omega_DE(a)/Omega_Lambda
    Sigma(a) = 1 + Sigma_0 * Omega_DE(a)/Omega_Lambda        [scale-independent, quasi-static]
Their deviation SWITCHES ON LATE (the ratio -> 0 at high z, -> 1 today). GRUT'S Sigma - 1 = x*alpha/2
IS CONSTANT IN TIME. At z = 0 the amplitudes are directly comparable, which is why the tensions below
are computed as they are.

*** THE SIGN OF THE MISMATCH IS UNDETERMINED, AND SAYING OTHERWISE WAS AN ERROR (2026-08-05). ***
The builder first wrote that the fence "moves tension UP" and that every tension here is a LOWER
BOUND. That applied the reasoning to ONE SIDE ONLY. A flat shape carries ~2.1x the integrated
deviation of theirs per unit z=0 amplitude, and that cuts BOTH ways:
  (i)  ON THE MEASUREMENT -- the same observed signal implies a SMALLER constant amplitude for us,
       so our inferred Sigma_0-equivalent is lower.  => LESS tension.
  (ii) ON OUR CAP -- more signal per unit amplitude means a TIGHTER ISW/lensing bound on us.
       => MORE tension.
Both are live, they have opposite signs, and which dominates cannot be settled without their
likelihood. THE HONEST STATEMENT IS: SHAPE-MISMATCHED, DIRECTION UNDETERMINED.
Recorded because the erroneous version ran AGAINST GRUT: an unearned pressure against the framework
is still an unearned claim, and this register's honesty is not permitted to be one-directional.

GRUT SIDE (banked): the interior two-moduli family is
    mu = 1 + x*alpha,   eta = 1/(1 + x*alpha),   Sigma = 1 + x*alpha/2
so in the observational deviation variables (Sigma_0 := Sigma - 1, mu_0 := mu - 1) the family
carries an EXACT LOCK,  Sigma_0 = mu_0 / 2,  inherited-conditional. alpha = a/c = 1/3 is the
rung9a conditional-theorem axiom.

*** THE SCREEN'S CENTRAL POINT, and it is the opposite of the intuitive reading: a CONFIRMED anomaly
of this amplitude EXCLUDES the family rather than supporting it. *** Sigma_0 = 0.149 sits ABOVE every
gate the program holds. "A 3-sigma result in our channel" is a potential kill, not a potential win,
and the pull to read it the other way is exactly what Sec.4 warns about.
"""
import math

# ------------------------------------------------- measured inputs, BOTH BACKGROUNDS (Table I)
# *** OPEN MEANS CARRY BOTH, NOT ADOPT ONE (overseer ruling 2026-08-05). ***
# The register books vc_w_equals_minus_one as OPEN. An open node is not a licence to pick the
# branch you prefer -- and the w0wa branch is the FLATTERING one on all four axes at once (lower
# significance, lower central value, lower tension, lower implied x). Selecting it silently is the
# same directional error as leading with the 3.0: over-claiming toward "less pressure" instead of
# toward "data touches us". BOTH ARE REPORTED AND THE SPREAD IS THE RESULT.
BACKGROUNDS = {
    "LCDM":    dict(sig0=0.149, sig0_err=0.051, mu0=0.21, mu0_err=0.21, quoted_sigma=3.0),
    # w0wa mu_0 = 0.09 +0.28/-0.24; the average half-width is used and the asymmetry is small
    # relative to the conclusion (the channel is uninformative either way).
    "w0waCDM": dict(sig0=0.115, sig0_err=0.053, mu0=0.09, mu0_err=0.26, quoted_sigma=2.2),
}
SIG0, SIG0_ERR = BACKGROUNDS["LCDM"]["sig0"], BACKGROUNDS["LCDM"]["sig0_err"]
MU0,  MU0_ERR = BACKGROUNDS["LCDM"]["mu0"], BACKGROUNDS["LCDM"]["mu0_err"]
SIG_SIGMA_LCDM = 3.0
SIG_SIGMA_W0WA = 2.2

ALPHA = 1.0 / 3.0           # rung9a a/c, conditional-theorem axiom

# The F-MAP shape mismatch has TWO opposing effects (see header). Any value other than
# "undetermined" is a claim this screen is not entitled to make.
FMAP_SIGN = "undetermined"

# Gates held by the program, expressed as upper bounds on x (see X_FLOOR_MAP / isw_tt_auto).
# A8-CORRECTED 2026-08-09: the kappa wave demoted the TT-auto headline. "Unconditional" no longer
# exists -- every TT-auto number is INSERTION-CONTAMINATED (GRUT-plus-an-unbanked-filter) and
# family-conditional; no upper bound on kappa exists in banked physics, so the family's cap has NO
# LOWER BOUND and the tension against it has NO FLOOR.
GATES = {
    "TT-auto kappa=1 edge (family-conditional, insertion-contaminated)": 0.037,
    "TT-auto kappa<=3 family bound (was 'unconditional'; demoted A8)":   0.358,
    "ISW/DESI Sigma_0 loose-upper (F-MAP)":      0.59,
    "retired 2-sigma window (superseded)":       1.0 / 16.0,
}

# THE DIRECTION RULE (comparison-rule extension, ruled 2026-08-09): any calc applying a CORRECTION
# must report WHICH WAY IT CUTS, so a favorable revision can never read as neutral housekeeping.
# This correction FAVORS GRUT: it removes a claimed floor on the tension. Stated per the ruling
# that the register's honesty must run both ways or it is not honesty.
A8_CORRECTION_DIRECTION = "favors-GRUT"


def sigma0_of_x(x, alpha=None):
    """The family's predicted present-day lensing deviation.

    alpha RESOLVES AT CALL TIME, not as a default argument. The first run of the mutation battery
    caught this: with `alpha=ALPHA` in the signature, the value binds when the function is DEFINED,
    so the alpha mutant SURVIVED -- and, worse, a future edit to ALPHA would silently fail to
    propagate while every selftest stayed green. A frozen-at-import constant masquerading as a
    live one is the same shape as a guard that verifies itself."""
    return x * (ALPHA if alpha is None else alpha) / 2.0


def x_of_sigma0(s0, alpha=None):
    return 2.0 * s0 / (ALPHA if alpha is None else alpha)


def tension(value, ceiling, err):
    """How far the measurement sits ABOVE a ceiling, in sigma. Negative == below."""
    return (value - ceiling) / err


def lock_test():
    """Does the measured pair satisfy the family's OWN internal lock Sigma_0 = mu_0/2?

    Reported with its DISCRIMINATING POWER, because a consistency check against a measurement that
    cannot distinguish the hypotheses is not evidence -- it is the absence of evidence wearing the
    appearance of agreement. That distinction is the whole content of this function."""
    mu_pred = 2.0 * SIG0                      # lock: mu_0 = 2 * Sigma_0
    mu_pred_err = 2.0 * SIG0_ERR
    comb = math.hypot(mu_pred_err, MU0_ERR)
    agreement = abs(mu_pred - MU0) / comb     # how well the lock agrees with the measured mu_0
    # The separation the measurement would have to resolve to ADJUDICATE lock vs GR:
    # the lock predicts mu_0 = mu_pred; GR predicts mu_0 = 0. Only MU0_ERR is relevant, because the
    # question is whether the mu channel can tell those two apart.
    discrimination = abs(mu_pred - 0.0) / MU0_ERR
    mu_vs_gr = abs(MU0 - 0.0) / MU0_ERR       # is mu_0 even nonzero?
    return dict(mu_pred=mu_pred, mu_pred_err=mu_pred_err, agreement_sigma=agreement,
                discrimination_sigma=discrimination, mu_vs_gr_sigma=mu_vs_gr)


def report_background(bg):
    """The full screen for ONE background. Both are always reported; neither is adopted."""
    b = BACKGROUNDS[bg]
    s0, se = b["sig0"], b["sig0_err"]
    mu_pred, mu_pred_err = 2.0 * s0, 2.0 * se
    comb = math.hypot(mu_pred_err, b["mu0_err"])
    gates = {name: dict(x_max=xm, sigma0_ceiling=sigma0_of_x(xm),
                        tension_sigma=tension(s0, sigma0_of_x(xm), se))
             for name, xm in GATES.items()}
    return dict(background=bg, sig0=s0, sig0_err=se, quoted_sigma=b["quoted_sigma"],
                x_implied=x_of_sigma0(s0), x_implied_err=x_of_sigma0(se), gates=gates,
                lock=dict(mu_pred=mu_pred, mu_pred_err=mu_pred_err,
                          agreement_sigma=abs(mu_pred - b["mu0"]) / comb,
                          discrimination_sigma=abs(mu_pred) / b["mu0_err"],
                          mu_vs_gr_sigma=abs(b["mu0"]) / b["mu0_err"]))


def spread():
    """THE DELIVERABLE: the RANGE across two choices the register has not made. A single number
    here would be a choice disguised as a measurement."""
    rs = {bg: report_background(bg) for bg in BACKGROUNDS}
    tight = "TT-auto kappa=1 edge (family-conditional, insertion-contaminated)"
    loose = "ISW/DESI Sigma_0 loose-upper (F-MAP)"
    lo = min(r["gates"][loose]["tension_sigma"] for r in rs.values())
    hi = max(r["gates"][tight]["tension_sigma"] for r in rs.values())
    # A8: the "low end" is a FAMILY-CONDITIONAL diagnostic, not a floor. With no banked upper
    # bound on kappa the cap has no lower bound, so the tension is "<= high, UNBOUNDED BELOW".
    return dict(per_background=rs, tension_low=lo, tension_high=hi,
                tension_floor_exists=False, correction_direction=A8_CORRECTION_DIRECTION,
                x_low=min(r["x_implied"] for r in rs.values()),
                x_high=max(r["x_implied"] for r in rs.values()))


def report():
    out = {}
    out["x_implied"] = x_of_sigma0(SIG0)
    out["x_implied_err"] = x_of_sigma0(SIG0_ERR)
    out["gates"] = {}
    for name, xmax in GATES.items():
        ceil = sigma0_of_x(xmax)
        out["gates"][name] = dict(x_max=xmax, sigma0_ceiling=ceil,
                                  tension_sigma=tension(SIG0, ceil, SIG0_ERR))
    out["lock"] = lock_test()
    out["background_swing_sigma"] = SIG_SIGMA_LCDM - SIG_SIGMA_W0WA
    return out


def selftest():
    ok = True

    def chk(cond, msg):
        nonlocal ok
        if not cond:
            print("  FAIL:", msg)
            ok = False

    r = report()

    # --- the family relation is a genuine round trip, not an assertion in a print statement ---
    chk(abs(sigma0_of_x(x_of_sigma0(0.077)) - 0.077) < 1e-12, "sigma0/x round trip broken")
    # --- the lock is Sigma_0 = mu_0/2, so mu_pred must be exactly twice Sigma_0 ---
    chk(abs(r["lock"]["mu_pred"] - 2 * SIG0) < 1e-12, "lock is not mu_0 = 2*Sigma_0")

    # --- the implied x, and that it lies ABOVE the held gates (the exclusion direction) ---
    chk(abs(r["x_implied"] - 0.894) < 0.002, f"x_implied = {r['x_implied']:.4f}, expected ~0.894")
    tight = r["gates"]["TT-auto kappa=1 edge (family-conditional, insertion-contaminated)"]["tension_sigma"]
    chk(2.7 < tight < 2.9, f"tightest-gate tension {tight:.2f} sigma, expected ~2.8")
    loose = r["gates"]["ISW/DESI Sigma_0 loose-upper (F-MAP)"]["tension_sigma"]
    chk(0.9 < loose < 1.1, f"loose-gate tension {loose:.2f} sigma, expected ~1.0")
    chk(all(g["tension_sigma"] > 0 for g in r["gates"].values()),
        "the measurement must sit ABOVE every gate -- that is the exclusion direction")

    # --- THE SCREEN'S LOAD-BEARING CLAIM: the mu channel cannot adjudicate ---
    L = r["lock"]
    chk(L["agreement_sigma"] < 0.5,
        f"lock agrees with measured mu_0 at {L['agreement_sigma']:.2f} sigma (expected <0.5)")
    chk(L["discrimination_sigma"] < 2.0,
        f"mu channel separates lock from GR at only {L['discrimination_sigma']:.2f} sigma -- if this "
        f"ever exceeds 2, the 'uninformative' finding must be re-derived, not reasserted")
    chk(L["mu_vs_gr_sigma"] < 1.5,
        "measured mu_0 must itself be consistent with GR, else the framing changes")
    # the two must not be confused: agreement is small AND discrimination is small. Good agreement
    # with a blunt instrument is the trap this whole function exists to expose.
    chk(L["agreement_sigma"] < L["discrimination_sigma"],
        "agreement must be tighter than discrimination for the 'uninformative' reading to hold")

    # --- the F-MAP sign must stay UNDETERMINED: two live effects, opposite signs ---
    chk(FMAP_SIGN == "undetermined",
        f"F-MAP sign is {FMAP_SIGN!r}. The shape mismatch moves the MEASUREMENT one way and our CAP "
        f"the other; without their likelihood neither dominates. A signed claim here is unearned -- "
        f"and the first version of this file made exactly that error, in the direction AGAINST GRUT.")

    # --- the background dependence, which is the screen's top finding ---
    chk(abs(r["background_swing_sigma"] - 0.8) < 1e-9, "background swing must be 3.0 - 2.2 = 0.8")

    # --- BOTH BACKGROUNDS CARRIED; the deliverable is the SPREAD, never one branch ---
    # Checked FIRST and guarded, so that dropping a background produces a clean FAIL rather than a
    # KeyError. A crash is not a catch -- this program ruled that when a mutant died on a TypeError
    # and was scored as caught. The guard must SEE the defect, not trip over it.
    chk(set(BACKGROUNDS) == {"LCDM", "w0waCDM"},
        f"BOTH backgrounds must be carried; found {sorted(BACKGROUNDS)}. An OPEN node collapsed to "
        f"one branch is a choice disguised as a measurement.")
    if set(BACKGROUNDS) != {"LCDM", "w0waCDM"}:
        print("  SELFTEST:", "FAIL")
        return False
    sp = spread()
    chk(abs(sp["x_low"] - 0.690) < 0.002, f"w0wa implied x = {sp['x_low']:.3f}, expected ~0.690")
    chk(abs(sp["x_high"] - 0.894) < 0.002, f"LCDM implied x = {sp['x_high']:.3f}, expected ~0.894")
    chk(0.28 < sp["tension_low"] < 0.35, f"kappa=1 member {sp['tension_low']:.2f}, expected ~0.31")
    chk(2.7 < sp["tension_high"] < 2.9, f"high end {sp['tension_high']:.2f}, expected ~2.80")
    # A8: the spread must DECLARE that no floor exists and which way the correction cuts.
    chk(sp.get("tension_floor_exists") is False,
        "A8: the tension has NO FLOOR (no banked upper bound on kappa -> the cap has no lower "
        "bound). A spread reporting a floor has silently re-promoted the demoted gate.")
    chk(sp.get("correction_direction") == "favors-GRUT",
        "THE DIRECTION RULE: a correction must state which way it cuts. This one removes claimed "
        "pressure (favors GRUT); stripping the statement makes a favorable revision read as "
        "neutral housekeeping, which is the exact laundering the rule exists to stop.")
    w = sp["per_background"]["w0waCDM"]
    chk(abs(w["quoted_sigma"] - w["sig0"] / w["sig0_err"]) < 0.15,
        "the w0wa central/error must reproduce the authors' own quoted 2.2 sigma")
    # the flattering-branch check, stated as a test so it cannot be quietly dropped
    L, W = sp["per_background"]["LCDM"], sp["per_background"]["w0waCDM"]
    chk(W["sig0"] < L["sig0"] and W["quoted_sigma"] < L["quoted_sigma"]
        and W["x_implied"] < L["x_implied"]
        and W["gates"]["ISW/DESI Sigma_0 loose-upper (F-MAP)"]["tension_sigma"]
            < L["gates"]["ISW/DESI Sigma_0 loose-upper (F-MAP)"]["tension_sigma"],
        "w0wa must be the FLATTERING branch on all four axes -- if that ever stops being true the "
        "carry-both ruling needs re-deriving rather than reasserting")
    # the mu channel must be uninformative in BOTH backgrounds, else the framing changes
    for bg, rr in sp["per_background"].items():
        chk(rr["lock"]["discrimination_sigma"] < 2.0,
            f"{bg}: mu channel discriminates lock-vs-GR at "
            f"{rr['lock']['discrimination_sigma']:.2f} sigma")

    print("  SELFTEST:", "PASS" if ok else "FAIL")
    return ok


# ============================ MUTATION BATTERY (calc-layer floor) ============================
# Pre-registered WRONG answers. Each MUST make selftest() fail. A green selftest proves nothing
# until it is shown to go red on a wrong implementation -- this program's dominant failure mode.
MUTANTS = [
    ("sigma0_of_x drops the factor 1/2 (Sigma-1 = x*alpha, not x*alpha/2)",
     lambda: _mutate("sigma0_of_x", lambda x, alpha=ALPHA: x * alpha)),
    ("lock inverted to mu_0 = Sigma_0/2 instead of 2*Sigma_0",
     lambda: _mutate("lock_test", lambda: dict(mu_pred=SIG0 / 2, mu_pred_err=SIG0_ERR / 2,
                                               agreement_sigma=0.1, discrimination_sigma=0.1,
                                               mu_vs_gr_sigma=1.0))),
    ("alpha set to 1 instead of a/c = 1/3 (kills the implied-x scale)",
     lambda: _mutate("ALPHA", 1.0)),
    ("discrimination computed against the LOCK's error instead of the mu measurement's -- the "
     "exact move that would make a blunt instrument look decisive",
     lambda: _mutate("lock_test", lambda: dict(mu_pred=2 * SIG0, mu_pred_err=2 * SIG0_ERR,
                                               agreement_sigma=0.38,
                                               discrimination_sigma=2 * SIG0 / (2 * SIG0_ERR),
                                               mu_vs_gr_sigma=1.0))),
    ("tension sign flipped, so the measurement reads BELOW the gates (the flattering direction)",
     lambda: _mutate("tension", lambda v, c, e: (c - v) / e)),
    # THE ERROR ACTUALLY COMMITTED, 2026-08-05, in both directions on the same wave: the overseer
    # led with the LCDM 3.0; the builder then over-corrected and called w0wa's 2.2 "the number
    # consistent with this register's own state". Both are single-branch reporting of an OPEN node.
    ("the F-MAP shape mismatch given a DIRECTION -- the one-sided reading, in either direction. "
     "Both the measurement side and the cap side move, with opposite signs, and only their "
     "likelihood settles it",
     lambda: _mutate("FMAP_SIGN", "up")),
    ("the direction statement stripped -- the A8 correction applied but reported as neutral "
     "housekeeping, hiding that it removes pressure (the favorable-revision laundering)",
     lambda: _mutate("A8_CORRECTION_DIRECTION", "")),
    ("the flattering branch silently adopted -- w0wa's numbers reported as if they were the "
     "register's own position, collapsing an OPEN node to the reading that flatters GRUT",
     lambda: _mutate("BACKGROUNDS", {k: v for k, v in BACKGROUNDS.items() if k == "w0waCDM"})),
]


def _mutate(name, repl):
    g = globals()
    old = g[name]
    g[name] = repl
    return old


def _restore(name, old):
    globals()[name] = old


def run_battery():
    import io
    import contextlib
    print("\n  MUTATION BATTERY (each mutant MUST make the selftest FAIL):")
    caught = 0
    for desc, apply_mut in MUTANTS:
        g = globals()
        snapshot = {k: g[k] for k in ("sigma0_of_x", "lock_test", "ALPHA", "tension",
                                      "BACKGROUNDS", "FMAP_SIGN",
                                      "A8_CORRECTION_DIRECTION")}
        try:
            apply_mut()
            buf = io.StringIO()
            with contextlib.redirect_stdout(buf):
                passed = selftest()
            status = "CAUGHT" if not passed else "*** SURVIVED ***"
            caught += 0 if passed else 1
        except Exception as e:                       # a crash is NOT a catch
            status = f"CRASHED ({type(e).__name__}) -- does NOT count as caught"
        finally:
            for k, v in snapshot.items():
                g[k] = v
        print(f"    [{status}] {desc}")
    print(f"  BATTERY: {caught}/{len(MUTANTS)} caught by the selftest")
    return caught == len(MUTANTS)


if __name__ == "__main__":
    r = report()
    print(__doc__.split("\n")[0])
    print(f"\n  MEASURED   Sigma_0 = {SIG0} +/- {SIG0_ERR}  "
          f"({SIG_SIGMA_LCDM} sigma in LCDM, {SIG_SIGMA_W0WA} sigma in w0waCDM)")
    print(f"             mu_0    = {MU0} +/- {MU0_ERR}  (authors: consistent with GR)")
    print(f"\n  IMPLIED x (alpha = 1/3): {r['x_implied']:.3f} +/- {r['x_implied_err']:.3f}")
    print("\n  AGAINST THE HELD GATES -- positive tension means the measurement sits ABOVE the")
    print("  ceiling, i.e. a confirmed anomaly of this size EXCLUDES the family:")
    for name, g in sorted(r["gates"].items(), key=lambda kv: kv[1]["tension_sigma"], reverse=True):
        print(f"    {g['tension_sigma']:+5.2f} sigma   x < {g['x_max']:<6.4g} "
              f"=> Sigma_0 < {g['sigma0_ceiling']:.4f}   [{name}]")
    L = r["lock"]
    print(f"\n  THE LOCK  Sigma_0 = mu_0/2  =>  mu_0 predicted {L['mu_pred']:.3f} "
          f"+/- {L['mu_pred_err']:.3f}")
    print(f"    agreement with measured mu_0 : {L['agreement_sigma']:.2f} sigma  (looks like a hit)")
    print(f"    but DISCRIMINATION lock-vs-GR: {L['discrimination_sigma']:.2f} sigma  "
          f"<- the mu channel CANNOT adjudicate")
    print(f"    and measured mu_0 vs GR      : {L['mu_vs_gr_sigma']:.2f} sigma  "
          f"(mu_0 is itself consistent with zero)")
    print("    => the 0.4-sigma 'agreement' is NOT evidence for the lock. It is a blunt instrument")
    print("       agreeing with everything. Reporting it as support would be the match temptation.")
    sp = spread()
    print("\n  BACKGROUND DEPENDENCE -- *** BOTH CARRIED, NEITHER ADOPTED ***")
    print("    The register books vc_w_equals_minus_one as OPEN. OPEN MEANS CARRY BOTH.")
    print("    Quoting 3.0 while booking w as open is incoherent; so is quoting 2.2, and that")
    print("    second error is the subtler one -- w0wa is the FLATTERING branch on all four axes")
    print("    at once, so adopting it silently selects the reading where GRUT looks best.")
    print(f"    {'':22s} {'LCDM':>14s} {'w0waCDM':>14s}")
    L, W = sp["per_background"]["LCDM"], sp["per_background"]["w0waCDM"]
    tightk = "TT-auto kappa=1 edge (family-conditional, insertion-contaminated)"
    loosek = "ISW/DESI Sigma_0 loose-upper (F-MAP)"
    for label, a, b in (
            ("anomaly significance", f"{L['quoted_sigma']:.1f} sigma", f"{W['quoted_sigma']:.1f} sigma"),
            ("Sigma_0 central", f"{L['sig0']:.3f}", f"{W['sig0']:.3f}"),
            ("tension vs loosest gate", f"{L['gates'][loosek]['tension_sigma']:+.2f} sigma",
                                        f"{W['gates'][loosek]['tension_sigma']:+.2f} sigma"),
            ("tension vs tightest gate", f"{L['gates'][tightk]['tension_sigma']:+.2f} sigma",
                                         f"{W['gates'][tightk]['tension_sigma']:+.2f} sigma"),
            ("implied x", f"{L['x_implied']:.3f}", f"{W['x_implied']:.3f}"),
            ("mu-channel discrimination", f"{L['lock']['discrimination_sigma']:.2f} sigma",
                                          f"{W['lock']['discrimination_sigma']:.2f} sigma")):
        print(f"    {label:22s} {a:>14s} {b:>14s}")
    print(f"\n  *** THE RESULT (A8-corrected): tension <= {sp['tension_high']:+.2f} sigma, "
          f"UNBOUNDED BELOW ***")
    print(f"      The former 'low end' ({sp['tension_low']:+.2f}) was the kappa=1 family member --")
    print("      family-conditional and insertion-contaminated, NOT a floor. With no banked upper")
    print("      bound on kappa the family's cap has no lower bound, so the tension has NO FLOOR:")
    print("      a confirmed Sigma_0 anomaly at this amplitude MAY BE FULLY COMPATIBLE with GRUT,")
    print("      and this register currently cannot say otherwise.")
    print(f"      DIRECTION OF THIS CORRECTION: {sp['correction_direction']} -- it REMOVES claimed")
    print("      pressure. Stated per the direction rule: a favorable revision must never read as")
    print("      neutral housekeeping.")
    print(f"      Implied x spans {sp['x_low']:.3f} to {sp['x_high']:.3f} (background choice only).")
    print("      F-MAP shape fence: mismatched, SIGN UNDETERMINED (see header; two opposing")
    print("      effects, needs their likelihood).")
    print()
    selftest()
    run_battery()
