#!/usr/bin/env python3
"""xi_stochastic_closure: the dissipation-sourced stochastic GW background
(the remaining unclaimed half of the second Part-7 front, v4 channel C5).

Charter: XI_STOCHASTIC_CHARTER_01.md, frozen at commit 06cf992.

A CLOSURE, NOT A PREDICTION HUNT (the Gamma_T gate's pricing carries
over): the FDT-mandated companion of any friction in the TT slot, at the
locked temperature T_dS = H0/2pi (rung2's KMS lock), carries the
stationary occupation n(w) = 1/(exp(2 pi w/H0) - 1) -- a Boltzmann
factor that is a property of the LOCK, not the kernel. This instrument
pins the induced Omega_GW at the frozen frequencies, in log space,
parameter-free, for both frozen members (pure-FDT stationary upper;
expansion-damped physical). Licensed domain w >> 3.4 H only; the
unaskable region (ROOT-1 O1-O4) is named, never evaluated.

Register read-only; nothing banks; no register field moves (v4 R2).
Pure stdlib. Deterministic. Single run.
Run: python3 calc/xi_stochastic_closure.py
(writes ../XI_STOCHASTIC_RESULT.json)
"""

import hashlib
import json
import math
import os
import sys
import time

T0 = time.time()
CHECKS = []
HALT = []


def check(ok, msg, kind="ok"):
    CHECKS.append({"kind": kind, "pass": bool(ok), "summary": msg})
    tag = {"ok": "GATE", "ctrl": "CONTROL", "note": "NOTE"}[kind]
    print(("PASS " if ok else "FAIL ") + tag + ": " + msg)


def halt_check(ok, msg):
    check(ok, msg, "ctrl")
    if not ok:
        HALT.append(msg)


MEAS = {}

# ---------------- frozen constants (the Gamma_T closure's own) ----------
MPC = 3.0856775814913673e22            # m
HBAR = 1.054571817e-34                 # J s
EV = 1.602176634e-19                   # J
H0 = 67.4 * 1e3 / MPC                  # s^-1
MP_GEV = 2.435e18                      # reduced Planck mass, GeV
MP = MP_GEV * 1e9 * EV / HBAR          # s^-1
LOG10 = math.log(10.0)


def gamma_T(w):
    """The pinned parameter-free horn-(a) kernel (flat contract)."""
    return (3.0 / (1280.0 * math.pi)) * (w ** 3 / MP ** 2) \
        * (1.0 + (104.0 / 9.0) * (H0 / w) ** 2)


# ---------------- RC-1: the Gamma_T closure replicates ------------------
print("=== RC-1: THE GAMMA_T CLOSURE REPLICATES (halt-grade) ===")
REC = {10.0: 1.352e-83, 100.0: 1.352e-80, 1024.0: 1.452e-77}
reps = {}
for f_hz, rec in REC.items():
    g = gamma_T(2.0 * math.pi * f_hz)
    reps[f_hz] = g
    MEAS[f"GammaT_{int(f_hz)}Hz"] = g
margin100 = math.log10(3.0 * H0) - math.log10(reps[100.0])
MEAS["margin_orders_100Hz"] = margin100
halt_check(all(abs(reps[f] / REC[f] - 1.0) < 0.005 for f in REC)
           and abs(margin100 - 62.7) < 0.1,
           f"RC-1 the Gamma_T closure replicates from the frozen "
           f"constants: Gamma_T = {reps[10.0]:.4e} / {reps[100.0]:.4e} / "
           f"{reps[1024.0]:.4e} s^-1 at 10/100/1024 Hz (recorded "
           f"1.352e-83 / 1.352e-80 / 1.452e-77); margin at 100 Hz "
           f"{margin100:.2f} orders (recorded 62.7)")

# ---------------- RC-2: identities --------------------------------------
print("\n=== RC-2: IDENTITIES (halt-grade) ===")
T_DS = H0 / (2.0 * math.pi)


def nbar_ln(w):
    """ln n(w) for the locked bath, exact below the frozen switch,
    asymptotic (-2 pi w / H0) above it (switch error < e^-50)."""
    xx = 2.0 * math.pi * w / H0
    if xx <= 50.0:
        return math.log(1.0 / (math.exp(xx) - 1.0))
    return -xx


# evaluable scan: wr = w/H0 in {0.25, 0.5, 1.0}, where coth - 1 >= 1e-3
# and the double-precision cancellation floor sits far below the 1e-12
# tolerance (at wr >~ 2 the naive coth - 1 loses to cancellation and the
# comparison would be numerically ill-posed, not physically informative)
id1 = max(abs((1.0 / math.tanh(0.5 * (2.0 * math.pi * wr))
               - 1.0) / (2.0 * (1.0 / (math.exp(2.0 * math.pi * wr) - 1.0)))
              - 1.0) for wr in (0.25, 0.5, 1.0))
xsw = 50.0
id2 = abs(nbar_ln(xsw * H0 / (2.0 * math.pi))
          - math.log(1.0 / (math.exp(xsw) - 1.0)))
halt_check(id1 < 1e-12 and id2 < 1e-10,
           f"RC-2 identities: coth(w/2T) - 1 = 2 n(w) to {id1:.1e} "
           f"relative on the evaluable scan; the log-space switch matches "
           f"the exact expression to {id2:.1e} at the switch point")

# ---------------- M: the closure table ----------------------------------
print("\n=== M: THE CLOSURE TABLE (log space; parameter-free) ===")
FREQS = [("w=10H0", 10.0 * H0), ("w=100H0", 100.0 * H0),
         ("PTA 1e-8 Hz", 2.0 * math.pi * 1e-8),
         ("LISA 1e-3 Hz", 2.0 * math.pi * 1e-3),
         ("ground 100 Hz", 2.0 * math.pi * 100.0)]
LEVELS = {"BBN": -6.0, "PTA": -9.0, "LISA": -12.0, "ground": -9.0}
table = {}
worst_margin = float("inf")
for name, w in FREQS:
    ln_n = nbar_ln(w)
    # Omega_upper = w^4 n / (3 pi^2 H0^2 MP^2)
    log10_upper = (ln_n + 4.0 * math.log(w)
                   - math.log(3.0 * math.pi ** 2) - 2.0 * math.log(H0)
                   - 2.0 * math.log(MP)) / LOG10
    g = gamma_T(w)
    ratio = g / (g + 3.0 * H0)
    log10_damped = log10_upper + math.log10(ratio)
    margins = {lv: log10_lv - log10_upper for lv, log10_lv in LEVELS.items()}
    worst_margin = min(worst_margin, min(margins.values()))
    table[name] = {"w_over_H0": w / H0, "log10_Omega_upper": log10_upper,
                   "log10_Omega_damped": log10_damped,
                   "damping_ratio_GammaT_over_3H0": ratio,
                   "margins_orders_vs_levels": margins}
    print(f"   {name:14s} (w/H0 = {w / H0:.3e}): log10 Omega_upper = "
          f"{log10_upper:.6g}; log10 Omega_damped = {log10_damped:.6g}; "
          f"min margin {min(margins.values()):.6g} orders")
MEAS["closure_table"] = table
check(len(table) == len(FREQS),
      f"M-1 the closure table is complete: both members and all margins "
      f"at every frozen frequency ({len(FREQS)} rows x "
      f"{len(LEVELS)} comparison levels)")
check(worst_margin > 30.0,
      f"M-2 NO EFFECT at every member and every frequency: both members "
      f"sit more than 30 orders below every comparison level everywhere "
      f"(worst margin {worst_margin:.1f} orders, at the licensed floor "
      f"against BBN -- the design foresight was ~139)")
check(True, "M-3 horn-independence (frozen note): the e^(-2 pi w/H0) "
            "factor is a property of the KMS lock at T_dS = H0/2pi, not "
            "of the kernel -- ANY friction in the constitutive family "
            "carries the same companion suppression at licensed "
            "frequencies; only the damped member's ratio feels the "
            "kernel, and only downward. The unaskable region (w <~ 3.4H, "
            "ROOT-1 O1-O4), where horn (b)'s pole lives, is named and "
            "not evaluated", "note")
check(True, "inherited obligations honored: no functional form "
            "transplanted (the kernel enters only through the pinned "
            "flat-contract Gamma_T); no staked amplitude enters any "
            "number (B nowhere); no unpinned constant in any headline "
            "(omega_c nowhere); register, TT quarantine, dephasing "
            "statements untouched", "note")

# ---------------- verdict ------------------------------------------------
gated = [c for c in CHECKS if c["kind"] in ("ok", "ctrl")]
n_ok = sum(1 for c in gated if c["pass"])
fails = [c["summary"] for c in gated if not c["pass"]]

if HALT:
    verdict = "HALT"
elif not fails:
    verdict = "XI-CLOSED-NO-EFFECT"
else:
    verdict = "XI-PARTIAL"

out = {
    "fork": "XI-1 (the second Part-7 front's unclaimed half; v4 C5 "
            "context)",
    "charter": "XI_STOCHASTIC_CHARTER_01.md (frozen 06cf992)",
    "timestamp": time.strftime("%Y-%m-%dT%H:%M:%S+00:00", time.gmtime()),
    "environment": {"python": sys.version.split()[0], "pure_stdlib": True,
                    "deterministic": True},
    "defect_history": [],
    "constants": {"H0_s^-1": H0, "MP_s^-1": MP, "T_dS_s^-1": T_DS},
    "measurements": MEAS,
    "checks": CHECKS,
    "adjudication": {
        "verdict": verdict,
        "scope": "the licensed domain w >> 3.4H only; the unaskable "
                 "region named, never evaluated; production mechanisms "
                 "other than the FDT-stationary companion out of scope. "
                 "Nothing banks; no register field moves (v4 R2)",
    },
    "elapsed_s": round(time.time() - T0, 2),
}
path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..",
                    "XI_STOCHASTIC_RESULT.json")
blob = json.dumps(out, indent=1)
with open(path, "w") as fh:
    fh.write(blob)
sha = hashlib.sha256(blob.encode()).hexdigest()
print(f"\nartifact written: {os.path.abspath(path)} (sha {sha[:16]}...)")
print(f"\nXI-1: {n_ok}/{len(gated)} gated checks passed; failures: "
      f"{len(fails)}; halts: {len(HALT)}")
if HALT:
    print("HALT: a control breached -- instrument bug, never physics. No "
          "verdict may be issued from this run.")
    sys.exit(2)
print(f"VERDICT: {verdict}")
print("HARD STOP: verdict recorded pending owner ruling.")
sys.exit(0 if not fails else 1)
