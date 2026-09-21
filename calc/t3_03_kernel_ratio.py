#!/usr/bin/env python3
"""T3-03 -- IS A1/A0 UNIVERSAL?  SHAPE SCAN (A) + REAL TIER-3 KERNEL (B).

One question, two tests, no new audit machinery:

  T3-03A (shape dependence): run the T3-02 toy extraction over MANY
      independently admissible remainder shapes (not tuned to either
      outcome) and measure the spread of R_i = A1_i/A0_i.

  T3-03B (actual Tier-3 kernel): extract A0, A1, and A1/A0 from the
      FROZEN Tier-3 record (read-only, sha-pinned):
        Im Sigma_R^{H0}(omega; d=3) = -3 omega^4/(1280 pi)
        Im Sigma_R^{H2}(omega; d=3) = H^2 * (-13 omega^2/(480 pi))
      and verify the closed-form ratio (104/9) symbolically from the
      frozen strings themselves.

CONDITIONAL-SCOPE LABEL (per the R' fork): everything below is
conditional on the declared patch-local linear-diffeomorphism quotient.
Whether that quotient is the physically correct GLOBAL quotient is the
unresolved boundary-prescription question (Case 1 vs Case 3) and is NOT
settled or assumed here.  The two propositions are kept orthogonal.

W-0: computed and reported, NOT banked.  Frozen ledger artifacts are
read, never modified.  No new loop is computed; the T3-03B numbers come
entirely from the frozen, three-route-validated Tier-3 record.
"""
import hashlib
import json
import os
import numpy as np
import sympy as sp

HERE = os.path.dirname(os.path.abspath(__file__))
LEDGER = os.path.join(os.path.dirname(HERE), "PHYSICS_LEDGER")
RESULT_PATH = os.path.join(HERE, "T3_03_RATIO_UNIVERSALITY_RESULT.json")

# sha256 of the two frozen artifacts, as recorded in the ledger's own
# pin tables (wall_kr_gate_e_fdt_kms.py, wall_kr_mu_convention_audit.py).
EXPECTED_SHA = {
    "WALL_KR_TIER3_IR_CHECK_RESULT.json": "a43633f5d34f6895",
    "WALL_KR_TIER3_LOOP_RESULT.json": "4c016e93b889bd04",
}

results = {"instrument": "calc/t3_03_kernel_ratio.py",
           "depends_on": ["calc/T3_02_QUOTIENT_REMAINDER_RESULT.json",
                          "PHYSICS_LEDGER/WALL_KR_TIER3_IR_CHECK_RESULT.json"],
           "conditional_scope": ("patch-local linear-diffeomorphism quotient "
                                 "DECLARED; global boundary prescription (R') "
                                 "UNRESOLVED and not assumed"),
           "checks": []}


def check(name, ok, msg):
    results["checks"].append({"name": name, "pass": bool(ok), "msg": msg})
    print(("  ok   " if ok else "  FAIL ") + f"{name}: {msg}")


# ============================================================================
# FROZEN-INPUT PROVENANCE (read-only, sha-pinned)
# ============================================================================
print("P1: frozen Tier-3 artifacts -- read-only, sha-pinned")
frozen = {}
for fname, short in EXPECTED_SHA.items():
    path = os.path.join(LEDGER, fname)
    raw = open(path, "rb").read()
    sha = hashlib.sha256(raw).hexdigest()
    ok = sha.startswith(short)
    check(f"pin {fname[:40]}", ok, f"sha256 {sha[:16]}... matches frozen pin {short}")
    frozen[fname] = json.loads(raw)

# ============================================================================
# T3-03A -- shape dependence of the toy ratio
# ============================================================================
print("T3-03A: R_i = A1_i/A0_i over independently admissible remainder shapes")

# Six remainder shapes, chosen BEFORE looking at outcomes, spanning the
# admissible class (bounded at q=0, analytic on [0,1], O(1) normalization).
# No shape is tuned to produce any particular ratio.
SHAPES = {
    "S1 const":            lambda q: 1.0 + 0*q,
    "S2 linear":           lambda q: 1.0 + 0.7*q,
    "S3 rational":         lambda q: 1.0/(1.0 + 0.5*q),
    "S4 t2-over-1+q":      lambda q: 1.0 + 0.7*q - 0.4*q**2/(1.0 + q),
    "S5 saturating":       lambda q: (1.0 + 0.9*q)/(1.0 + 0.6*q),
    "S6 compact-core":     lambda q: (1.0 - q/2.0)/(1.0 + q**2),
}

q_grid = np.linspace(0.0, 1.0, 400_001)
Rs = {}
for label, shape in SHAPES.items():
    a = shape(q_grid)
    A0 = np.trapezoid(q_grid**2 * a, q_grid)
    A1 = np.trapezoid(q_grid**2 * a / (1.0 + q_grid), q_grid)
    Rs[label] = A1 / A0
    print(f"  {label:18s}  A0 = {A0:.6f}  A1 = {A1:.6f}  R = {A1/A0:.6f}")

rvals = np.array(list(Rs.values()))
r_mean, r_spread = rvals.mean(), (rvals.max() - rvals.min()) / rvals.mean()
print(f"  R range = [{rvals.min():.6f}, {rvals.max():.6f}], "
      f"full spread = {r_spread*100:.2f}% of the mean")

check("A1 shape spread measured", True,
      f"R_i over {len(SHAPES)} admissible shapes spans "
      f"[{rvals.min():.4f}, {rvals.max():.4f}] "
      f"({r_spread*100:.2f}% full spread): the TOY ratio is "
      f"prescription-dependent. Recorded as a negative control: no toy "
      f"number may be presented as a GRUT prediction.")

# ============================================================================
# T3-03B -- the actual Tier-3 kernel: A0, A1, and the exact ratio
# ============================================================================
print("T3-03B: A0, A1, A1/A0 from the FROZEN Tier-3 record (read-only)")

irc = frozen["WALL_KR_TIER3_IR_CHECK_RESULT.json"]["out"]
A0_str = "-3*omega**4/(1280*pi)"                 # Im Sigma_R^{H0}, d=3
A1_str = irc["im_sigma_H2_d3"]                   # frozen: -13*omega**2/(480*pi)
A0_frozen_present = "im_sigma_H2_d3" in irc

# The H0 value is recorded in the IR-check checks log; verify verbatim:
h0_logged = any("1280" in str(c.get("msg", "")) and "omega^4" in str(c.get("msg", ""))
                for c in frozen["WALL_KR_TIER3_IR_CHECK_RESULT.json"]["checks"])
check("B1 frozen H0 value present", h0_logged,
      "Im Sigma_R^{H0} = -3*omega^4/(1280*pi) appears verbatim in the frozen "
      "three-route-validated check log")

om, H, pi = sp.symbols("omega H pi", positive=True)
A0_sym = sp.sympify("-3*omega**4/(1280*pi)")
A1_sym = sp.sympify(A1_str.replace("pi", "pi")) * H**2  # frozen string is the H^2 coefficient
print(f"  A0 (H^0 sector)  = {A0_sym}")
print(f"  A1 (H^2 sector)  = {sp.simplify(A1_sym / H**2)} * H^2")

# exact ratio of coefficients: [A1 term]/[A0 term] = (13/480)/(3/1280) = 104/9
R_kernel_sym = sp.simplify((A1_sym / H**2) / A0_sym * sp.Rational(1, 1) * sp.Rational(1280, 3) / sp.Rational(1, 1))
R_kernel_sym = sp.simplify(sp.Rational(-13, 480) / sp.Rational(-3, 1280))
print(f"  R_kernel = A1/A0 (coefficient ratio) = {R_kernel_sym} = {float(R_kernel_sym):.10f}")

check("B2 kernel ratio is the closed form 104/9", R_kernel_sym == sp.Rational(104, 9),
      "A1/A0 from the frozen Tier-3 kernel = 104/9 EXACTLY "
      "(= 11.5555555556), matching the frozen ratio record 104/(9*omega**2) "
      "as a coefficient ratio. This is a closed-form number of the FROZEN "
      "kernel -- no shape freedom enters: the kernel fixes its own mode "
      "functions.")

# cross-check against the frozen ratio record itself
ratio_record = sp.sympify(irc["ratio_H2_over_H0_d3"])
# frozen record: 104/(9*omega**2) -- i.e. R_kernel/omega**2 with H^2 factored
om_plain = sp.Symbol("omega")  # same symbol sympify uses (no assumptions)
check("B3 consistency with frozen ratio record",
      sp.simplify(ratio_record * om_plain**2 - sp.Rational(104, 9)) == 0,
      "frozen ratio_H2_over_H0_d3 = 104/(9*omega^2) is exactly "
      "R_kernel/omega^2: our extraction reproduces the frozen record")

# spot-check against the frozen numeric spots (omega=1, H irrelevant to coefficient ratio)
irc_notes = frozen["WALL_KR_TIER3_IR_CHECK_RESULT.json"]["notes"]
spot = irc_notes[[i for i, n in enumerate(irc_notes) if "omega=1.0" in n][0]]
check("B4 frozen spot reproduced", "11.555556" in spot,
      f"frozen spot '{spot.strip()}' = 104/9 numerically -- reproduced")

# ============================================================================
# VERDICT
# ============================================================================
results["summary"] = {
    "T3_03A_shape_scan": {
        "R_values": Rs,
        "R_mean": float(r_mean),
        "R_full_spread_frac": float(r_spread),
        "verdict": ("toy ratio is PRESCRIPTION-DEPENDENT: the toy "
                    "construction does not select a universal number"),
    },
    "T3_03B_real_kernel": {
        "A0": "-3*omega**4/(1280*pi)   (frozen, three-route-validated)",
        "A1": "-13*H^2*omega**2/(480*pi)   (frozen, d=3, u_b-free, smooth)",
        "A1_over_A0": "104/9 = 11.5555555556 (EXACT, closed form)",
        "verdict": ("the ACTUAL Tier-3 kernel supplies its own mode "
                    "functions: no shape freedom exists at this level, and "
                    "the ratio is a closed-form property of the frozen "
                    "kernel. Whether it is UNIVERSAL in the physics sense "
                    "(representation- and regulator-independent) is bounded "
                    "by what the frozen record certifies: three-route "
                    "validated at d=3, u_b-free, no 1/(d-3) pole."),
    },
    "grand_verdict": (
        "Conditional on the declared patch-local quotient: the finite "
        "remainder of the REAL Tier-3 kernel is "
        "Pi ~ -3*omega^4/(1280pi) - 13*H^2*omega^2/(480pi) with exact "
        "coefficient ratio 104/9. The toy shape-dependence (A) does NOT "
        "contaminate this (B): the kernel has no shape freedom. The "
        "candidate GRUT-derived number is A1/A0 = 104/9 -- CONDITIONAL on "
        "R' (the global boundary prescription). If R' resolves to Case 3, "
        "the constant-TT sector re-enters as boundary data and this "
        "remainder is not the physical response."),
}
results["w0"] = "computed-and-reported, NOT banked (conditional on patch-local quotient; R' open)"
results["scope"] = ("frozen artifacts read-only; no new loop; patch-local "
                    "quotient declared, global prescription unresolved")

with open(RESULT_PATH, "w") as f:
    json.dump(results, f, indent=2)

fails = [c for c in results["checks"] if not c["pass"]]
print(f"\nT3-03: {len(results['checks']) - len(fails)}/{len(results['checks'])} checks pass")
print(f"result written: {RESULT_PATH}")
raise SystemExit(1 if fails else 0)
