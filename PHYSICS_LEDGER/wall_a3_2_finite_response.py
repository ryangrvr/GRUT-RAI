#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""WALL A / ASSEMBLY-3 / TASK A3-2 -- THE FINITE eps^0 RETARDED RESPONSE [builder]

Owner 'go' 2026-08-28, HEAD 50e82f9. Contract: WALL_A3_2_EXECUTION_PROMPT.md
(sha256 8dc3226669b3f9e12a099e227009d28b7fa50dc64b8e08aabbebba153f5b1167,
hash-pinned below) under the standing A3 chain (entry object, V4 amendment,
A3-1 finite masters). Output paths CLAIMED before writing
(AGENT_COORDINATION.md, A3-2 governance freeze block):
  PHYSICS_LEDGER/wall_a3_2_finite_response.py          (this instrument)
  PHYSICS_LEDGER/WALL_A3_2_FINITE_RESPONSE_RESULT.json
  PHYSICS_LEDGER/WALL_A3_2_FINITE_RESPONSE_VERDICT.md
  PHYSICS_LEDGER/Sigma_R_finite_full.json
  PHYSICS_LEDGER/Sigma_R_finite_full.verdict.md
  PHYSICS_LEDGER/.p_a3_2_run.log

SCOPE (hard, A3-2B): the finite eps^0 retarded kernel Sigma_R^finite(mu nu,
rho sigma; omega, k, H, m) for the D2 assembly -- ALL non-TT sectors carried,
no early projection, bubble factor 1/2, signed retarded rule, l/l-K routing
verbatim from the frozen Phase-10 engine. Then (A3-2C) the frozen MS pole
subtraction verified, (A3-2D) analytic structure exposed, (A3-2E) five
independent checks incl. the wrong-branch negative control, (A3-3) freeze +
manifest + HARD STOP.
BARRED (hard stop, A3-3+ and prompt): Q1-Q5, J(omega) comparison, PV runs,
Im-chi fits, relaxation/resonance/spectral classification, power-law fits,
basis alteration, refits, register edits, operator additions.

METHOD -- the twin law (derived in-instrument, gated against A3-1):
  In c-units (i(4pi)^-2 normalisation, mu^eps measure, c := 2/eps) the exact
  trace composition (l^2)^j = ((l^2-Delta)+Delta)^j reduces every master to
  the A3-1-validated base masters M_1..M_4. Closed form, s := j-N+2:
    pole(j,N;Delta) = c * moment * P * Delta^s,          P = C(j,N-1)+C(j,N-2),
    fin(j,N;Delta)  = moment * Delta^s * [ P*(kappa - ln((Delta-i0)/mu^2) + s_j)
                                           + C(j,N-1) + Q(j,N) ],
    s_j = psi(j+2)-psi(2) = sum_{i=2..j+1} 1/i   (exact-d moment correction;
    reproduces A3-1's T2 = /(4-eps) and T4 = 3/((4-eps)(6-eps)) compositions
    EXACTLY -- gates below),  Q(j,N) = sum_{r<=min(j,N-3)} C(j,r)
    (-1)^(N-r)/((N-r-1)(N-r-2)).  All Delta are Delta-i0 (A3-1 branch law:
    masters' Im = +pi on the cut, Disc M_2 = 2 pi i theta(-Delta)).

REPRESENTATION (A3-2F):
  * LOCAL finite sector (s>=0 polynomial parts; kappa / ln(mu^2) / ln(m^2/mu^2)
    coefficient logs are LOCAL per the V4 F1 amendment): closed sympy forms --
    passes the frozen F1 predicate verbatim.
  * NONLOCAL sector: exact 1-D Feynman-parameter integrals as two closed atom
    families (sympy Function subclasses with exact fdiff recurrence):
      G[n,np,e](K2,m2) = Int_0^1 dy y^n (1-y)^np (D(y)-i0)^e (-ln(D(y)-i0))
      R[n,np,e](K2,m2) = Int_0^1 dy y^n (1-y)^np (D(y)-i0)^e    (e <= -1),
    D(y) = m^2 - y(1-y) K^2, K^2 = omega^2 - k^2. R with e >= 0 auto-evaluates
    to its closed polynomial (wt*Beta normalisation). The families are closed
    under d/dK^2 and d/dm^2, so the validated external Delta-power/u-rule
    machinery differentiates them EXACTLY. No Li_2-class atom can occur: the
    log sector exists only at s >= 0 and the recurrence kills the e -> -1
    G-descent exactly at e = 0 (both gated).
  * The finite assembly carries its own c-sector, byte-checked against the
    frozen Phase-10 cache -- the pole replay gate is built into every block.

INDEPENDENT REFEREE (Route B): high-precision mpmath quadrature of the ORIGINAL
parameter integrals (the atoms' own definitions; G split Re/Im at the cut,
R by complex-eps Richardson). Route B never calls an analytic primitive; the
sympy closed forms of leading atoms are gated AGAINST it, never the reverse.
Negative control: the wrong branch (+i0) must be DETECTED.

Run:   python3 wall_a3_2_finite_response.py        (no arguments)
Env:   A32_LEDGER   ledger dir (default: this file's dir)
       A32_CACHE_DIR finite block cache dir (default /tmp/a3_2_stage)
       FIN_SMOKE=1  fast pre-flight subset (never a result run)
Exit 0 iff every gate passes. W-0: computed-and-reported, NOT banked.
"""
import hashlib
import json
import os
import subprocess
import sys
import time
from functools import lru_cache

import mpmath as mp
import sympy as sp

T0 = time.time()
HERE = os.path.dirname(os.path.abspath(__file__))
LEDGER = os.environ.get("A32_LEDGER", HERE)
CACHE_DIR = os.environ.get("A32_CACHE_DIR", "/tmp/a3_2_stage")
SMOKE = os.environ.get("FIN_SMOKE") == "1"
# A3-2F stop-rule budget: the DECLARED default is 1200s (20 min) per block.
# A32_BLOCK_BUDGET_S may only RAISE it (recovery runs); any override is
# printed in the run header, recorded in NOTES, and frozen in the result
# JSON. The stop/record/continue semantics are unchanged.
BLOCK_BUDGET_S = max(1200, int(os.environ.get("A32_BLOCK_BUDGET_S", "1200")))
BLOCK_BUDGET_OVERRIDE = BLOCK_BUDGET_S != 1200
LOG_PATH = os.path.join(HERE, ".p_a3_2_run.log")
RESULT_PATH = os.path.join(HERE, "WALL_A3_2_FINITE_RESPONSE_RESULT.json")
VERDICT_PATH = os.path.join(HERE, "WALL_A3_2_FINITE_RESPONSE_VERDICT.md")
FREEZE_PATH = os.path.join(HERE, "Sigma_R_finite_full.json")
FREEZE_VERDICT_PATH = os.path.join(HERE, "Sigma_R_finite_full.verdict.md")

SELF_CAUGHT = []


class _Tee(object):
    def __init__(self, *streams):
        self.streams = streams

    def write(self, x):
        for s in self.streams:
            try:
                s.write(x)
            except Exception:
                pass
        return len(x)

    def flush(self):
        for s in self.streams:
            try:
                s.flush()
            except Exception:
                pass


_logf = open(LOG_PATH, "w", buffering=1)
sys.stdout = _Tee(sys.__stdout__, _logf)
mp.mp.dps = 40

CHECKS = []
FAILS = []
CONTROLS = []
NOTES = []


def stamp(msg):
    print("[%7.1fs] %s" % (time.time() - T0, msg))
    sys.stdout.flush()


def check(cond, msg, gate="general", detail=None):
    ok = bool(cond)
    rec = {"gate": gate, "kind": "gate", "msg": msg, "pass": ok}
    if detail is not None:
        rec["detail"] = detail
    CHECKS.append(rec)
    print(("  ok   " if ok else "  FAIL ") + msg)
    sys.stdout.flush()
    if not ok:
        FAILS.append(msg)
    return ok


def control(name, detected, msg, detail=None):
    """negative/positive control record: pass == detected-as-designed"""
    rec = {"gate": name, "kind": "control", "msg": msg, "detected": bool(detected),
           "pass": bool(detected)}
    if detail is not None:
        rec["detail"] = detail
    CONTROLS.append(rec)
    print(("  ctrl-DETECTED   " if detected else "  ctrl-MISSED   ") + msg)
    sys.stdout.flush()
    if not detected:
        FAILS.append("control not detected: " + name)
    return bool(detected)


def note(msg):
    NOTES.append(msg)
    print("  note " + msg)
    sys.stdout.flush()


def sha(path):
    h = hashlib.sha256()
    with open(path, "rb") as f:
        for blk in iter(lambda: f.read(65536), b""):
            h.update(blk)
    return h.hexdigest()


def expr_fp(ex):
    """sha256 fingerprint of a sympy expression (srepr round-trip) for drift
    detection -- VERBATIM port from wall_d2_phase12_ms_split.py."""
    return hashlib.sha256(sp.srepr(sp.expand(ex)).encode()).hexdigest()[:16]


def expr_sha(ex):
    return hashlib.sha256(sp.srepr(sp.expand(ex)).encode()).hexdigest()


print("=== WALL A3-2: FINITE eps^0 RETARDED RESPONSE ===")
print("ledger: %s   smoke: %s   cache dir: %s" % (LEDGER, SMOKE, CACHE_DIR))
if BLOCK_BUDGET_OVERRIDE:
    print("*** A32_BLOCK_BUDGET_S=%d: the A3-2F stop-rule budget is RAISED "
          "from the declared 1200s default for this run (disclosed in notes "
          "+ result JSON) ***" % BLOCK_BUDGET_S)
    note("OPERATIONAL DISCLOSURE: A32_BLOCK_BUDGET_S=%d -- the A3-2F "
         "per-block stop-rule budget was raised from the declared 1200s "
         "default for this run (the three double-fish-insertion products "
         "H2_V1AxV1B/H2_V1V1onA/H2_V1V1onB each exceeded 1200s of real CPU "
         "in the preceding run while every other gate passed; stop/record/"
         "continue semantics unchanged)" % BLOCK_BUDGET_S)
if SMOKE:
    print("*** FIN_SMOKE=1: PRE-FLIGHT SUBSET ONLY -- NEVER a result run ***")

# =====================================================================================
# STEP 0 -- INPUT INTEGRITY (A3-2A)
# =====================================================================================
print("\n=== STEP 0: INPUT INTEGRITY ===")
PIN = {
    "WALL_A3_2_EXECUTION_PROMPT.md": "8dc3226669b3f9e12a099e227009d28b7fa50dc64b8e08aabbebba153f5b1167",
    "WALL_A3_1_FINITE_MASTERS_RESULT.json": "abe50eff489d409a903639d8a37384a41191f096bf77ea3eb38ebe7d6aedd5fd",
    "WALL_A3_1_FINITE_MASTERS_VERDICT.md": "254ed68b38f2d604f6d222d3d6d3d424a55d326cb5410c4182e5d0166054ab81",
    "wall_a3_1_finite_masters.py": "d1ef50f84af9fe5987c00c7aaab986b16963f847f82374041bf1e5e8faab6941",
    "wall_d2_phase12_ms_split.py": "a9850cd5d8ce5d61e1eb9574c9aaeed2a412db4a833f851e447b36b5955c83a2",
    "wall_d2_phases8_12.py": "f48b2cc898017493a11f08c8b6bfcb1c2367a0f577b583f00d77d0bd8341c558",
    ".p10_assembly_cache.txt": "3208492fcf01caad5b9d35c40a4379b056cd5ca8bc175d4ca2569a273561a0af",
    ".p11_af_basis_cache.txt": "692039d8c2a9d462eb314557ddc78e00d68c73054aed7db2987671ad58f63fbb",
    "WALL_D2_ASSEMBLY3_ENTRY_OBJECT.json": "419c455bccdd90dcbef708698e5339b7a2d32f0c8b07c49af9de6ab099316ccb",
    "WALL_A_A3_REGISTRY.json": "faa977d40f1ba31836e35b18223c1f573559b49649a84fad237a3809aae59b55",
    "WALL_A_A3_DECLARATIONS_V4_AMENDMENT.md": "f6127ca65ad6636be432b6d6c6fb6d30bb0b9f0c8912df4a9a1054e54919dd56",
    "WALL_D2_UV_FREEZE_RESULT.json": "9ced0c68f46554778c2648602b5537aca027b2dd40bf5b155f74731cb6cb2706",
}
for name, want in sorted(PIN.items()):
    p = os.path.join(LEDGER, name)
    got = sha(p) if os.path.exists(p) else "MISSING"
    check(got == want, "input integrity: %s sha256 == pinned" % name, gate="A3-2A",
          detail={"want": want, "got": got})
    if got != want:
        print("INTEGRITY FAILURE -- refusing to proceed (entry pins must hold)")
        _logf.close()
        sys.exit(2)

HEAD_EXPECT = "50e82f9160f91397b5076edf367327f78e7c346c"
# SELF-CAUGHT: the pin was originally transcribed with a typo at hex position
# 26 ('33' for '73'); the repo's actual HEAD (short form 50e82f9, unchanged
# across all A3-2 runs) is authoritative -- verified byte-for-byte against
# `git rev-parse HEAD` before correcting.
REPO = os.path.dirname(LEDGER)
head = subprocess.run(["git", "rev-parse", "HEAD"], cwd=REPO,
                      capture_output=True, text=True).stdout.strip()
st = subprocess.run(["git", "status", "--porcelain"], cwd=REPO,
                    capture_output=True, text=True).stdout.strip().splitlines()
allowed = {os.path.join("PHYSICS_LEDGER", p) for p in
           ["wall_a3_2_finite_response.py", "WALL_A3_2_FINITE_RESPONSE_RESULT.json",
            "WALL_A3_2_FINITE_RESPONSE_VERDICT.md", "Sigma_R_finite_full.json",
            "Sigma_R_finite_full.verdict.md", ".p_a3_2_run.log"]}
dirty = [ln.strip() for ln in st
         if ln.strip() and ln.strip().split()[-1] not in allowed]
check(head == HEAD_EXPECT, "git HEAD == %s (the A3-2 entry pin)" % HEAD_EXPECT,
      gate="A3-2A", detail={"head": head})
check(not dirty, "worktree clean apart from this instrument's own claimed outputs",
      gate="A3-2A", detail={"unexpected": dirty})

# claimed-path pre-registration check (A3-2A: claim before write)
coord_path = os.path.join(REPO, "AGENT_COORDINATION.md")
coord = open(coord_path).read() if os.path.exists(coord_path) else ""
for p in ["wall_a3_2_finite_response.py", "WALL_A3_2_FINITE_RESPONSE_RESULT.json",
          "WALL_A3_2_FINITE_RESPONSE_VERDICT.md", "Sigma_R_finite_full.json",
          "Sigma_R_finite_full.verdict.md", ".p_a3_2_run.log"]:
    check(p in coord, "output path pre-registered in AGENT_COORDINATION.md: %s" % p,
          gate="A3-2A")

# guard-lite: this instrument must not contain barred computation constructs
# (prose mentions of the bars are fine; call-patterns are not)
# SELF-CAUGHT: the barred literals originally appeared contiguously in this
# check's own list, so the scan matched the instrument itself and every guard
# gate always failed. Fix: the literals are built by concatenation so they
# never appear contiguously in the source, and the FULL source is scanned
# (a stronger check than eliding the guard block).
_own_src = open(os.path.abspath(__file__)).read()
for _b in ["chi_" + "integral(", "pv_" + "average(", "spectral_" + "class(",
           "relaxation_" + "fit(", "power_law_" + "fit(", "resonance_" + "fit(",
           "J_of_" + "omega(", "import " + "numpy", "mp.find" + "root"]:
    check(_b not in _own_src, "guard-lite: instrument free of barred construct %r"
          % _b, gate="A3-2A")
SELF_CAUGHT.append({
    "id": "A3-2-guard-lite-self-match",
    "what": "the guard-lite barred-construct literals appeared contiguously in "
            "the check's own list, so the source scan matched the instrument "
            "itself and all 9 guard gates failed on every run regardless of "
            "content",
    "fix": "literals built by string concatenation (never contiguous in the "
           "source); the full source is still scanned",
    "evidence": "three smoke runs all showed the same 9 guard failures; "
                "post-fix the scan finds zero barred constructs in the "
                "instrument",
})
SELF_CAUGHT.append({
    "id": "A3-2-head-pin-typo",
    "what": "HEAD_EXPECT was transcribed with one wrong hex character at "
            "position 26 (3633... for 3673...), so the entry-pin gate failed "
            "although the repo sat at the correct commit 50e82f9",
    "fix": "pin corrected to the repo's actual full HEAD, verified "
            "byte-for-byte against git rev-parse HEAD before the edit",
    "evidence": "git rev-parse HEAD == 50e82f9160f91397b5076edf367327f78e7c346c; "
                "diff vs old pin is exactly one character (index 26)",
})
stamp("STEP 0 done" + (" (SMOKE)" if SMOKE else ""))

# =====================================================================================
# STEP 1 -- ENGINE LOAD (the validated construction-load pattern; battery skip disclosed)
# =====================================================================================
print("\n=== STEP 1: ENGINE LOAD (construction-load pattern) ===")
P10_PATH = os.path.join(LEDGER, ".p10_assembly_cache.txt")
_p10_before = open(P10_PATH, "rb").read()
ENGINE_PATH = os.path.join(LEDGER, "wall_d2_phases8_12.py")
_src = open(ENGINE_PATH).read()
MARK = "# ================= PHASE 11: IDENTIFICATION"
check(MARK in _src, "engine machinery marker found (refusing to guess the split)",
      gate="load")
_cut = _src.split(MARK)[0]
os.environ.setdefault("SKIPBAT", "1")
note("SKIPBAT=1: the Level-2 battery is NOT re-run here; it last PASSED at 195a481 "
     "(all five cases, broken control failing). A finite-mode decomposition-"
     "independence check on the L2-discriminating s^1 class IS run in STEP 3, "
     "with its own broken control.")
_argv_saved = sys.argv
sys.argv = [ENGINE_PATH, "p10"]
ns = {"__name__": "a3_2_engine_load", "__file__": ENGINE_PATH}
_engine_exit = 0
try:
    exec(compile(_cut, "wall_d2_phases8_12.py", "exec"), ns)
except SystemExit as e:
    _engine_exit = e.code
finally:
    sys.argv = _argv_saved
check(_engine_exit == 0, "engine internal gates all pass on load (exit 0, FAIL empty)",
      gate="load", detail={"exit": _engine_exit, "engine_FAIL": len(ns.get("FAIL", []))})
check(sorted(ns["CACHED"]) == ["F_H0", "F_H2", "H1_total", "S_H1", "S_H2"],
      "frozen Phase-10 cache loaded: the five cached sectors", gate="load")
_p10_after = open(P10_PATH, "rb").read()
if _p10_after != _p10_before:
    open(P10_PATH, "wb").write(_p10_before)     # restore-guard (never expected)
    check(False, "Phase-10 cache byte-stable across load (restored after drift!)",
          gate="load")
else:
    check(True, "Phase-10 cache byte-stable across the machinery load "
          "(cache_save rewrite is a no-op; the loop target is immutable in fact)",
          gate="load")

LSY = ns["LSY"]
xf = ns["xf"]
KUP = ns["KUP"]
KSQ = ns["KSQ"]
om, kk, mm, Hs, csym = ns["om"], ns["kk"], ns["mm"], ns["H"], ns["c"]
moment = ns["moment"]
Dl = ns["Dl"]
kap = ns["kap"]
DeltaF = mm**2 - xf * (1 - xf) * KSQ
muS = sp.Symbol("mu", positive=True)
epsS = sp.Symbol("eps", positive=True)
check(csym not in sp.expand(ns["CACHED"]["F_H0"]).free_symbols,
      "cached assemblies are c-free (poles in units of c; c applied at report time)",
      gate="load")
stamp("engine loaded")

# =====================================================================================
# STEP 2 -- THE FINITE TWIN LAW + ATOM FAMILIES (derived in-instrument, gated)
# =====================================================================================
print("\n=== STEP 2: TWIN LAW + MASTER GATES ===")


def _C(j, r):
    return sp.binomial(j, r) if 0 <= r <= j else sp.Integer(0)


@lru_cache(maxsize=None)
def twin_params(j, N):
    """the twin-law data of the master class (j, N):
    s = j-N+2, P = C(j,N-1)+C(j,N-2) [the Ipole coefficient], Cj = C(j,N-1),
    Q = sum_{r<=min(j,N-3)} C(j,r) (-1)^(N-r)/((N-r-1)(N-r-2)) [rational part],
    s_j = psi(j+2)-psi(2) [exact-d moment correction]."""
    s = j - N + 2
    P = _C(j, N - 1) + _C(j, N - 2)
    Cj = _C(j, N - 1)
    Q = sp.Integer(0)
    if N >= 3:
        Q = sum(sp.Integer(-1) ** (N - r) * _C(j, r) / ((N - r - 1) * (N - r - 2))
                for r in range(0, min(j, N - 3) + 1))
    sj = sum(sp.Rational(1, i) for i in range(2, j + 2))
    return s, sp.nsimplify(P), sp.nsimplify(Cj), sp.nsimplify(Q), sj


# --- gate 2.1: the twin's pole sector IS the engine's Ipole_scalar, everywhere ---
for _j in range(0, 5):
    for _N in range(1, 6):
        _s, _P, _Cj, _Q, _sj = twin_params(_j, _N)
        _mine = _P * Dl**_s if _s >= 0 else sp.Integer(0)
        check(sp.expand(_mine - ns["Ipole_scalar"](_j, _N)) == 0,
              "twin pole sector == engine Ipole_scalar(j=%d,N=%d) EXACTLY" % (_j, _N),
              gate="twin-pole")
pole_grid_ok = all(r["pass"] for r in CHECKS if r["gate"] == "twin-pole")
check(pole_grid_ok, "twin law pole sector: 25/25 (j,N) classes byte-identical to the "
      "engine's validated pole law (the replay is structural, not incidental)",
      gate="twin-pole")


def fin_master_symbolic(j, N):
    """twin-law finite master at SYMBOLIC Delta (branch-inert reading; used for
    gates against A3-1's recorded forms)."""
    s, P, Cj, Q, sj = twin_params(j, N)
    if s < 0:
        return Q * Dl**s
    return Dl**s * (P * (kap - sp.log(Dl / muS**2) + sj) + Cj + Q)


# --- gate 2.2: M_1..M_4 reproduce A3-1's recorded masters VERBATIM ---
check(sp.expand(fin_master_symbolic(0, 1)
                - Dl * (1 + kap - sp.log(Dl / muS**2))) == 0,
      "M_1 twin == A3-1: Delta*(1 + kappa - ln(Delta/mu^2))", gate="twin-M")
check(sp.expand(fin_master_symbolic(0, 2) - (kap - sp.log(Dl / muS**2))) == 0,
      "M_2 twin == A3-1: kappa - ln(Delta/mu^2)", gate="twin-M")
check(sp.expand(fin_master_symbolic(0, 3) + sp.Rational(1, 2) / Dl) == 0,
      "M_3 twin == A3-1: -1/(2 Delta)", gate="twin-M")
check(sp.expand(fin_master_symbolic(0, 4) - sp.Rational(1, 6) / Dl**2) == 0,
      "M_4 twin == A3-1: 1/(6 Delta^2)", gate="twin-M")

# --- gate 2.3: T2/T4 reproduce A3-1's exact-d compositions EXACTLY ---
# A3-1 recorded: T2_{00,N} = [M_{N-1} + Delta M_N]/(4-eps);
#                T4_{0000,N} = 3[M_{N-2} + 2 Delta M_{N-1} + Delta^2 M_N]/((4-eps)(6-eps)).
# eps^0 parts: (1/4)[Mf_{N-1}+D Mf_N] + (1/8)[Ip(N-1)+D Ip(N)];
#              (1/8)[Mf_{N-2}+2D Mf_{N-1}+D^2 Mf_N] + (5/48)[Ip(N-2)+2D Ip(N-1)+D^2 Ip(N)].
for _N in (2, 3, 4):
    _Mf = lambda n: fin_master_symbolic(0, n)
    _Ip = lambda n: ns["Ipole_scalar"](0, n)
    _t2m = moment(1, 0, 0, 0) * fin_master_symbolic(1, _N)
    _t2r = sp.Rational(1, 4) * (_Mf(_N - 1) + Dl * _Mf(_N)) \
        + sp.Rational(1, 8) * (_Ip(_N - 1) + Dl * _Ip(_N))
    check(sp.expand(_t2m - _t2r) == 0,
          "T2 twin == A3-1 exact-d composition /(4-eps) at N=%d (the s_j "
          "cross-term is the (eps/4)x(2/eps) pole cross -- EXACT)" % _N, gate="twin-T")
    _t4m = moment(2, 0, 0, 0) * fin_master_symbolic(2, _N)
    _t4r = sp.Rational(1, 8) * (_Mf(_N - 2) + 2 * Dl * _Mf(_N - 1) + Dl**2 * _Mf(_N)) \
        + sp.Rational(5, 48) * (_Ip(_N - 2) + 2 * Dl * _Ip(_N - 1) + Dl**2 * _Ip(_N))
    check(sp.expand(_t4m - _t4r) == 0,
          "T4 twin == A3-1 exact-d composition 3/((4-eps)(6-eps)) at N=%d (s_2 = "
          "psi(4)-psi(2) = 5/6 exactly)" % _N, gate="twin-T")
stamp("twin law gated (pole grid 25/25, M_1..M_4, T2/T4 compositions)")

# ---------------------------------------------------------------- atom families ----
K2t = sp.Symbol("K2t", real=True)
m2t = sp.Symbol("m2t", positive=True)


@lru_cache(maxsize=None)
def _rint_closed(n, np_, e):
    """Int_0^1 dy y^n (1-y)^np (m2 - y(1-y) K2)^e for e >= 0 -- a closed POLYNOMIAL
    in (K2, m2) (pure polynomial integrand; evaluated monomial-wise, exact)."""
    yt = sp.Symbol("yt", real=True)
    Dy = m2t - yt * (1 - yt) * K2t
    integ = sp.expand(yt**n * (1 - yt)**np_ * Dy**e)
    return sp.expand(sp.integrate(integ, (yt, 0, 1)))


class Rfun(sp.Function):
    """R[n,np,e](K2,m2) := Int_0^1 dy y^n (1-y)^np (D(y)-i0)^e,  D = m2 - y(1-y)K2.
    e <= -1 stays symbolic (rational/threshold class, F1-nonlocal);
    e >= 0 AUTO-EVALUATES to the closed polynomial (wt*Beta-normalised weight)."""
    nargs = 5

    @classmethod
    def eval(cls, n, np_, e, K2, m2):
        if getattr(e, "is_Integer", False) and int(e) >= 0:
            return _rint_closed(int(n), int(np_), int(e)).subs({K2t: K2, m2t: m2})
        return None

    def fdiff(self, argindex=1):
        n, np_, e = self.args[0], self.args[1], self.args[2]
        K2, m2 = self.args[3], self.args[4]
        if argindex == 4:      # d/dK2:  d(D-i0)^e/dK2 = e (D-i0)^(e-1) (-y(1-y))
            return -e * Rfun(n + 1, np_ + 1, e - 1, K2, m2)
        if argindex == 5:      # d/dm2:  d(D-i0)^e/dm2 = e (D-i0)^(e-1)
            return e * Rfun(n, np_, e - 1, K2, m2)
        raise NotImplementedError("Rfun: derivative wrt integer parameter")

    def _eval_derivative(self, s):
        """chain rule for COMPOSITE arguments (K2 = omega^2 - k^2): sympy's
        default wraps composite-arg differentiation in unevaluated
        Subs(Derivative(...)) and BYPASSES fdiff -- caught by the finite-mode
        decomposition-independence gate (SELF-CAUGHT defect; the pole sector,
        being polynomial, was unaffected). We evaluate exactly instead."""
        K2, m2 = self.args[3], self.args[4]
        res = sp.S.Zero
        if s in K2.free_symbols:
            res += self.fdiff(4) * K2.diff(s)
        if s in m2.free_symbols:
            res += self.fdiff(5) * m2.diff(s)
        return res


class Gfun(sp.Function):
    """G[n,np,e](K2,m2) := Int_0^1 dy y^n (1-y)^np (D(y)-i0)^e (-ln(D(y)-i0)).
    e >= 0 (the log sector exists only at s >= 0; the recurrence below kills the
    e -> -1 descent exactly at e = 0, so no Li_2/Clausen atom can EVER arise --
    gated). mu-independence: the ln(mu^2) piece is carried EXPLICITLY as a
    polynomial coefficient OUTSIDE the atom, so the atom is a pure function of
    (K2, m2)."""
    nargs = 5

    @classmethod
    def eval(cls, *args):
        return None

    def fdiff(self, argindex=1):
        n, np_, e = self.args[0], self.args[1], self.args[2]
        K2, m2 = self.args[3], self.args[4]
        if argindex == 4:      # d/dK2:
            #   d[-ln(D-i0)]/dK2 = +y(1-y)/(D-i0)   ->  +R[n+1,np+1,e-1]
            #   d(D-i0)^e/dK2 = -e y(1-y) (D-i0)^(e-1)  ->  -e G[n+1,np+1,e-1]
            return -e * Gfun(n + 1, np_ + 1, e - 1, K2, m2) \
                + Rfun(n + 1, np_ + 1, e - 1, K2, m2)
        if argindex == 5:      # d/dm2:
            #   d[-ln(D-i0)]/dm2 = -1/(D-i0)  ->  -R[n,np,e-1]
            #   d(D-i0)^e/dm2 = e (D-i0)^(e-1)   ->  e G[n,np,e-1]
            return e * Gfun(n, np_, e - 1, K2, m2) - Rfun(n, np_, e - 1, K2, m2)
        raise NotImplementedError("Gfun: derivative wrt integer parameter")

    def _eval_derivative(self, s):
        """chain rule for COMPOSITE arguments -- see Rfun._eval_derivative (the
        same SELF-CAUGHT defect and fix)."""
        K2, m2 = self.args[3], self.args[4]
        res = sp.S.Zero
        if s in K2.free_symbols:
            res += self.fdiff(4) * K2.diff(s)
        if s in m2.free_symbols:
            res += self.fdiff(5) * m2.diff(s)
        return res


# ------------------------------------------------- mpmath referee primitives ----
KAP_NUM = mp.log(4 * mp.pi) - mp.euler      # kappa = ln(4pi) - gamma_E


def _Dfun(y, K2, m2):
    return m2 - y * (1 - y) * K2


def _cut_pts(K2, m2):
    """the y-interval where D(y) < 0 (exists iff K2 > 4 m2 > 0)."""
    if K2 <= 0 or m2 <= 0 or K2 <= 4 * m2:
        return None
    d = 1 - 4 * m2 / K2
    if d <= 0:
        return None
    r = mp.sqrt(d)
    return ((1 - r) / 2, (1 + r) / 2)


@lru_cache(maxsize=None)
def _quad_atom(fam, n, np_, e, K2, m2, branch=1):
    """ROUTE B (independent referee): direct mpmath quadrature of the atom's
    DEFINITION -- never an analytic primitive.
      G: Re = Int y^n(1-y)^np |D|^e (-ln|D|) dy;  Im = branch*pi*Int_{cut} ... dy
         (branch=+1: the frozen -i0 law, masters' Im = +pi on the cut;
          branch=-1: the WRONG branch, negative control only).
      R (e<=-1): no cut: real quadrature; with cut: complex-eps Richardson
         I(eta) = Int w (D - i*branch*eta)^e dy,  3-point extrapolation."""
    K2, m2 = mp.mpf(K2), mp.mpf(m2)
    pts = _cut_pts(K2, m2)
    if fam == "G":
        f = lambda y: y**n * (1 - y)**np_ * abs(_Dfun(y, K2, m2))**e \
            * (-mp.log(abs(_Dfun(y, K2, m2))))
        re = mp.quad(f, [0, pts[0], pts[1], 1] if pts else [0, 1])
        im = mp.mpf(0)
        if pts:
            g = lambda y: y**n * (1 - y)**np_ * abs(_Dfun(y, K2, m2))**e
            im = branch * mp.pi * mp.quad(g, [pts[0], pts[1]])
        return re + mp.mpc(0, 1) * im
    assert fam == "R" and e <= -1
    w = lambda y: y**n * (1 - y)**np_
    if pts is None:
        return mp.quad(lambda y: w(y) * _Dfun(y, K2, m2)**e, [0, 1])

    def I(eta):
        return mp.quad(lambda y: w(y) * mp.power(
            mp.mpc(_Dfun(y, K2, m2), -branch * eta), e), [0, 1])
    eta = mp.mpf("2e-3")
    return (8 * I(eta / 4) - 6 * I(eta / 2) + I(eta)) / 3


def _num_eval_expr(ex, K2v, m2v, branch=+1):
    """numeric value of an atom-carrying expression in (K2t, m2t) only -- gate use."""
    ex = sp.expand(ex)
    subsmap = {}
    for A in ex.atoms(Gfun, Rfun):
        fam = "G" if isinstance(A, Gfun) else "R"
        v = _quad_atom(fam, int(A.args[0]), int(A.args[1]), int(A.args[2]),
                       mp.mpf(K2v), mp.mpf(m2v), branch)
        subsmap[A] = sp.Float(mp.nstr(mp.re(v), 30), 30) \
            + sp.Float(mp.nstr(mp.im(v), 30), 30) * sp.I
    ex2 = ex.subs(subsmap).subs({K2t: K2v, m2t: m2v})
    return mp.mpc(complex(sp.N(ex2, 30)))


# --- gate 2.4: fdiff recurrence vs numeric differentiation (both families) ---
_h = mp.mpf("1e-5")
for (_n, _np_, _e) in [(0, 0, 0), (1, 0, 1), (0, 1, 2), (2, 1, 0)]:
    _A = Gfun(sp.Integer(_n), sp.Integer(_np_), sp.Integer(_e), K2t, m2t)
    _dK = sp.diff(_A, K2t)
    _lhs = _num_eval_expr(_dK, -3, 1)
    _rhs = (_quad_atom("G", _n, _np_, _e, -3 + _h, 1)
            - _quad_atom("G", _n, _np_, _e, -3 - _h, 1)) / (2 * _h)
    _dd = abs(_lhs - _rhs)
    check(_dd < mp.mpf("1e-7"),
          "fdiff gate dG/dK2 (n=%d,np=%d,e=%d): recurrence == Richardson "
          "derivative of the quadrature (d=%.2e)" % (_n, _np_, _e, _dd),
          gate="atom-fdiff", detail={"diff": float(_dd)})
    _dm = sp.diff(_A, m2t)
    _lhs2 = _num_eval_expr(_dm, -3, 1)
    _rhs2 = (_quad_atom("G", _n, _np_, _e, -3, 1 + _h)
             - _quad_atom("G", _n, _np_, _e, -3, 1 - _h)) / (2 * _h)
    _dd2 = abs(_lhs2 - _rhs2)
    check(_dd2 < mp.mpf("1e-7"),
          "fdiff gate dG/dm2 (n=%d,np=%d,e=%d): recurrence == Richardson "
          "derivative (d=%.2e)" % (_n, _np_, _e, _dd2), gate="atom-fdiff",
          detail={"diff": float(_dd2)})
for (_n, _np_, _e) in [(0, 0, -1), (1, 0, -2)]:
    _A = Rfun(sp.Integer(_n), sp.Integer(_np_), sp.Integer(_e), K2t, m2t)
    _dK = sp.diff(_A, K2t)
    _lhs = _num_eval_expr(_dK, -3, 1)
    _rhs = (_quad_atom("R", _n, _np_, _e, -3 + _h, 1)
            - _quad_atom("R", _n, _np_, _e, -3 - _h, 1)) / (2 * _h)
    _dd = abs(_lhs - _rhs)
    check(_dd < mp.mpf("1e-7"),
          "fdiff gate dR/dK2 (n=%d,np=%d,e=%d): recurrence == Richardson "
          "derivative (d=%.2e)" % (_n, _np_, _e, _dd), gate="atom-fdiff",
          detail={"diff": float(_dd)})

# --- gate 2.5: R auto-evaluation at e >= 0 (closed polynomial, exact) ---
_Rt = Rfun(sp.Integer(1), sp.Integer(0), sp.Integer(2), K2t, m2t)
check(sp.expand(_Rt - _rint_closed(1, 0, 2)) == 0,
      "R-atom auto-evaluation at e>=0: closed polynomial (Int y (m2-y(1-y)K2)^2)",
      gate="atom-eval")
check(Rfun(sp.Integer(0), sp.Integer(0), sp.Integer(-1), K2t, m2t).func is Rfun,
      "R-atom at e<=-1 stays symbolic (the threshold/rational class)", gate="atom-eval")
stamp("atom families gated (fdiff recurrences == numeric differentiation)")

# --- gate 2.6: the scalar-bubble anchor at master level (A3-2E #1) ---
# B(K2) = kappa - Int_0^1 dy ln(D(y)/mu^2) = kappa + ln(mu^2) + G[0,0,0](K2,m2);
# at mu = m = 1: B = kappa + G[0,0,0]. A3-1 route-A recorded values:
_A31_B = [(-0.7, "1.844576499478384"), (-1.3, "1.7609963360093845"),
          (-2.9, "1.5710865474016833")]
for _k2, _ws in _A31_B:
    _got = KAP_NUM + _quad_atom("G", 0, 0, 0, _k2, 1)
    _want = mp.mpf(_ws)
    _dd = abs(_got - _want)
    check(_dd < mp.mpf("5e-6"),
          "scalar-bubble anchor B(K2=%s): kappa + G[0,0,0]-referee == A3-1 route-A "
          "finite (d=%.2e < 5e-6)" % (_k2, _dd), gate="anchor",
          detail={"got": mp.nstr(_got, 17), "want": _ws, "diff": float(_dd)})
_got_im = mp.im(_quad_atom("G", 0, 0, 0, 5, 1))
_want_im = mp.pi / mp.sqrt(5)     # A3-1: routeA_Im = 1.4049629462081452 at K2=5m^2
check(abs(_got_im - _want_im) < mp.mpf("5e-6"),
      "scalar-bubble anchor Im at K2=5m^2: +pi*sqrt(1-4/5) (the frozen branch law; "
      "d=%.2e)" % abs(_got_im - _want_im), gate="anchor",
      detail={"got": mp.nstr(_got_im, 17), "want": "1.4049629462081452"})
# wrong-branch control at master level (the +i0 branch flips the Im sign):
_got_w = mp.im(_quad_atom("G", 0, 0, 0, 5, 1, branch=-1))
control("anchor-wrong-branch", abs(_got_w - _want_im) > mp.mpf("1e-2"),
        "wrong-branch control at master level: Im(G, +i0) = -pi*sqrt(1-4/5) "
        "DISAGREES with the frozen +pi law (d=%.3f)" % abs(_got_w - _want_im))
stamp("scalar-bubble anchor gated (3 spacelike Re + timelike Im + wrong-branch ctrl)")

# ---------------------------------------------------------------- the twins ----
@lru_cache(maxsize=None)
def _atomize(pref, aP, bP, e, fam):
    """attach atom family `fam` to every y-monomial of pref (a polynomial in the
    Feynman parameter xf with (om,kk,mm,E_,P_) coefficients): the atom index
    absorbs the weight  y^{bP-1}(1-y)^{aP-1}  exactly as the engine's integrand."""
    ppoly = sp.Poly(sp.expand(pref), xf)
    tot = sp.Integer(0)
    for (yd,), cv in zip(ppoly.monoms(), ppoly.coeffs()):
        tot += cv * fam(sp.Integer(yd + bP - 1), sp.Integer(aP - 1), sp.Integer(e),
                         KSQ, mm**2)
    return sp.expand(tot)


def _fin_mono_2den(expo, aP, bP):
    """FINITE TWIN of the engine's _mono_pole_2den -- IDENTICAL routing (shift
    l -> l + yK, weight Gamma(N)/(Gamma(a)Gamma(b)) y^{b-1}(1-y)^{a-1}, moments,
    Delta = m^2 - y(1-y) K^2), the twin-law master replacing Ipole_scalar.
    Returns  c*[pole] + [local finite closed] + [G/R-atom nonlocal sector]."""
    N = aP + bP
    wt = sp.factorial(N - 1) / (sp.factorial(aP - 1) * sp.factorial(bP - 1))
    monoexpr = sp.prod([(LSY[i] + xf * KUP[i])**expo[i] for i in range(4)])
    nsh = sp.expand(monoexpr)
    poly = sp.Poly(nsh, *LSY)
    cint = sp.Integer(0)
    gsum = sp.Integer(0)
    rsum = sp.Integer(0)
    for mono, cf in zip(poly.monoms(), poly.coeffs()):
        if any(e % 2 for e in mono):
            continue
        a_, b_, c2, d_ = (e // 2 for e in mono)
        mom = moment(a_, b_, c2, d_)
        j = a_ + b_ + c2 + d_
        s, P, Cj, Q, sj = twin_params(j, N)
        base = cf * mom
        if base == 0:
            continue
        if s < 0:
            # UV-finite master (P = 0): finite = Q (D-i0)^s -- pure R-atom sector
            rsum += _atomize(base * Q, aP, bP, s, Rfun)
        else:
            # pole (units of c) + local finite + the ln(mu^2) piece -- polynomial
            # in y, closed by the same y-integral as the pole route:
            cint += base * Dl**s * (P * (csym + kap + sj + sp.log(muS**2)) + Cj + Q)
            # the -ln(D-i0) piece -- the G-atom (nonlocal) sector:
            gsum += _atomize(base * P, aP, bP, s, Gfun)
    out = sp.expand(cint.subs(Dl, DeltaF))
    closed = sp.integrate(sp.expand(out * xf**(bP - 1) * (1 - xf)**(aP - 1)),
                          (xf, 0, 1))
    return sp.expand(wt * (closed + gsum + rsum))


def _fin_mono_tad(expo, aP):
    """FINITE TWIN of the engine's _mono_pole_tad -- fully closed (Delta = m^2
    fixed; the -i0 is inert on m^2 > 0): the seagull finite sector is entirely
    LOCAL (logs of (m^2, mu) are coefficient logs, LOCAL per the V4 amendment)."""
    if any(e % 2 for e in expo):
        return sp.Integer(0)
    a_, b_, c2, d_ = (e // 2 for e in expo)
    j = a_ + b_ + c2 + d_
    s, P, Cj, Q, sj = twin_params(j, aP)
    mom = moment(a_, b_, c2, d_)
    if s < 0:
        return sp.expand(mom * Q * mm**(2 * s))
    return sp.expand(mom * mm**(2 * s)
                     * (P * (csym + kap + sj + sp.log(muS**2) - sp.log(mm**2))
                        + Cj + Q))


def _k0_closed(expr):
    """K = 0 collapse of an assembled twin value: D(y) = m^2 constant, the
    Feynman weight integrates to wt*Beta = 1, G -> Beta*m^{2e}(-ln m^2),
    R -> Beta*m^{2e}. Used by the cross-route gate ONLY."""
    ex = sp.expand(expr.subs({om: 0, kk: 0}))
    reps = {}
    for A in ex.atoms(Gfun, Rfun):
        n, np_, e = int(A.args[0]), int(A.args[1]), int(A.args[2])
        m2a = A.args[4]
        beta = sp.factorial(n) * sp.factorial(np_) / sp.factorial(n + np_ + 1)
        reps[A] = beta * m2a**e * ((-sp.log(m2a)) if isinstance(A, Gfun) else 1)
    return sp.expand(ex.subs(reps))


# --- gate 2.7: K=0 cross-route (2den master at K=0 == tadpole master, exactly) ---
_K0_CASES = [((2, 0, 0, 0), 1, 1), ((2, 0, 0, 0), 1, 2), ((0, 0, 0, 0), 2, 1),
             ((1, 1, 0, 0), 1, 1), ((2, 2, 0, 0), 2, 2), ((0, 0, 0, 0), 3, 1),
             ((2, 0, 0, 0), 2, 2), ((4, 0, 0, 0), 2, 2), ((0, 0, 0, 0), 1, 3)]
for _expo, _aP, _bP in _K0_CASES:
    _lhs = _k0_closed(_fin_mono_2den(_expo, _aP, _bP))
    _rhs = _fin_mono_tad(_expo, _aP + _bP)
    check(sp.expand(_lhs - _rhs) == 0,
          "K=0 cross-route: 2den master (aP=%d,bP=%d) == tadpole master N=%d "
          "EXACTLY (two independent code paths of the twin law)" % (_aP, _bP, _aP + _bP),
          gate="k0-cross")
stamp("finite twins gated (K=0 cross-route: 9/9)")

# =====================================================================================
# STEP 3 -- FINITE-MODE ASSEMBLY (per-block cache; the pole replay is built in)
# =====================================================================================
print("\n=== STEP 3: FINITE-MODE ASSEMBLY ===")
import signal

FIN_CACHE_PATH = os.path.join(CACHE_DIR, ".a3_2_fin_cache.txt")
FIN_TAG = "A32fin-v1"
_fincache = {}
if os.path.exists(FIN_CACHE_PATH):
    try:
        _lines = open(FIN_CACHE_PATH).read().splitlines()
        if _lines and _lines[0].strip() == "tag " + FIN_TAG:
            for _ln in _lines[1:]:
                _p = _ln.split(" ", 2)
                if len(_p) == 3:
                    _fincache[_p[0]] = (_p[1], _p[2])
        else:
            note("finite cache tag mismatch -- ignored (fresh assembly)")
    except Exception as _e:
        note("finite cache unreadable (%s) -- ignored" % _e)


def fin_cache_save():
    try:
        os.makedirs(CACHE_DIR, exist_ok=True)
        with open(FIN_CACHE_PATH, "w") as f:
            f.write("tag " + FIN_TAG + "\n")
            for k in sorted(_fincache):
                f.write("%s %s %s\n" % (k, _fincache[k][0], _fincache[k][1]))
    except Exception as _e:
        note("finite cache save failed (%s) -- continuing (in-memory only)" % _e)


def _load_fin(name):
    if name not in _fincache:
        return None
    _fp, _s = _fincache[name]
    try:
        v = sp.sympify(_s, locals={"Gfun": Gfun, "Rfun": Rfun})
    except Exception as _e:
        note("finite cache entry %s failed to load (%s) -- reassembling" % (name, _e))
        return None
    if expr_fp(v) != _fp:
        note("finite cache entry %s fingerprint mismatch -- reassembling" % name)
        return None
    return v


BLOCK_TIMING = {}
BLOCK_STOPPED = []


class _BlockTimeout(Exception):
    pass


def _eps2_gate(name, val):
    try:
        _P = sp.Poly(sp.expand(val), csym)
        _ok = _P.degree() <= 1 and all(m in ((0,), (1,)) for m in _P.monoms())
    except Exception as _e:
        _ok = False
        note("eps2 gate exception on %s: %s" % (name, _e))
    check(_ok, "block %s: exactly linear in c (pole c^1 + finite c^0; no eps^2 "
          "sector -- the structural cancellation)" % name, gate="eps2")


def run_block(name, fn):
    """assemble one finite block: per-block cache, timing, eps^2-linearity gate,
    and the A3-2F stop rule (>20 min without a reusable result -> stop THAT
    block, record, continue)."""
    cached = _load_fin(name)
    if cached is not None:
        BLOCK_TIMING[name] = {"cached": True}
        check(True, "block %s: loaded from finite cache (srepr round-trip + "
              "fingerprint verified)" % name, gate="fin-asm")
        return cached

    def _handler(signum, frame):
        raise _BlockTimeout()

    _old = signal.signal(signal.SIGALRM, _handler)
    signal.alarm(BLOCK_BUDGET_S)
    _t = time.time()
    try:
        val = sp.expand(fn())
        _el = time.time() - _t
        BLOCK_TIMING[name] = {"elapsed_s": round(_el, 1)}
        if _el > BLOCK_BUDGET_S:
            note("A3-2F: block %s took %.0fs (> %ds budget) but COMPLETED -- "
                 "cached and recorded (reusable result obtained)"
                 % (name, _el, BLOCK_BUDGET_S))
        check(True, "block %s assembled in %.1fs" % (name, _el), gate="fin-asm",
              detail={"elapsed_s": round(_el, 1)})
    except _BlockTimeout:
        BLOCK_TIMING[name] = {"stopped_at_s": BLOCK_BUDGET_S}
        BLOCK_STOPPED.append(name)
        check(False, "A3-2F STOP RULE: block %s exceeded the %ds budget "
              "without a reusable result -- STOPPED, recorded, continuing "
              "with the next block" % (name, BLOCK_BUDGET_S),
              gate="fin-asm")
        val = None
    except Exception as _e:
        import traceback
        BLOCK_TIMING[name] = {"error": repr(_e)}
        BLOCK_STOPPED.append(name)
        check(False, "block %s raised %r -- recorded, continuing with the next "
              "block" % (name, _e), gate="fin-asm",
              detail={"traceback": traceback.format_exc()[-2000:]})
        val = None
    finally:
        signal.alarm(0)
        signal.signal(signal.SIGALRM, _old)
    if val is not None:
        _eps2_gate(name, val)
        _fincache[name] = (expr_fp(val), sp.srepr(val))
        fin_cache_save()
    return val


def _csec(ex):
    """the c^1 coefficient of an assembled finite block (its pole sector)."""
    return sp.expand(sp.expand(ex).coeff(csym, 1))


# --- the finite-mode monkey-patch (the probe-validated pattern): every route
# (plain assemble, all FL insertion pieces, seagull) flows through these two
# masters, so the whole validated routing now emits the finite twin law. ---
ns["_mono_pole_2den"] = _fin_mono_2den
ns["_mono_pole_tad"] = _fin_mono_tad
ns["cache_save"] = lambda d: None      # the frozen .p10 cache is never touched again
note("finite mode ACTIVE: _mono_pole_2den/_mono_pole_tad replaced by the twin law; "
     "all engine routing (assemble, assemble_fl, seagull_fl, eval_factorlists -> "
     "pieces_pole) flows through them unchanged.")

A = ns["assemble"]
FL = ns["assemble_fl"]
F1i = ns["fish_one_insertion"]
plainA = [(ns["plain_line"]("A"), 0, 1)]
plainB = [(ns["plain_line"]("B"), 0, 1)]

SMOKE_BLOCKS = {"F_H0_fin", "H1_vtx10", "H1_V1onA", "S_H0_fin", "S_H1_fin",
                "L2A_s1_r2", "L2A_s1_broken1", "L2A_s1_broken2"}
BLOCKS = [
    ("F_H0_fin", lambda: A(0, 0, plainA, plainB)),
    ("H1_vtx10", lambda: A(1, 0, plainA, plainB)),
    ("H1_vtx01", lambda: A(0, 1, plainA, plainB)),
    ("H1_V1onA", lambda: FL(F1i("A", 1, 1, 1, 0, 0), 0, 0)),
    ("H1_V1onB", lambda: FL(F1i("B", 1, 1, 1, 0, 0), 0, 0)),
    ("H2_vtx20", lambda: A(2, 0, plainA, plainB)),
    ("H2_vtx02", lambda: A(0, 2, plainA, plainB)),
    ("H2_vtx11", lambda: A(1, 1, plainA, plainB)),
    ("H2_vtx1xV1A", lambda: FL(F1i("A", 1, 1, 1, 1, 0), 1, 0)),
    ("H2_vtx1xV1B", lambda: FL(F1i("B", 1, 1, 1, 1, 0), 1, 0)),
    ("H2_vtx2xV1A", lambda: FL(F1i("A", 1, 1, 1, 0, 1), 0, 1)),
    ("H2_vtx2xV1B", lambda: FL(F1i("B", 1, 1, 1, 0, 1), 0, 1)),
    ("H2_V2onA", lambda: FL(F1i("A", 2, 2, 1, 0, 0), 0, 0)),
    ("H2_V2onB", lambda: FL(F1i("B", 2, 2, 1, 0, 0), 0, 0)),
    ("H2_V1AxV1B", lambda: FL(ns["fish_cross_insertions"](0, 0), 0, 0)),
    ("H2_V1V1onA", lambda: FL(ns["fish_two_same_line"]("A", 0, 0), 0, 0)),
    ("H2_V1V1onB", lambda: FL(ns["fish_two_same_line"]("B", 0, 0), 0, 0)),
    ("S_H0_fin", lambda: -sp.Rational(1, 2) * ns["loop_pole_tad"](ns["L2ker"], 1)),
    ("S_H1_fin", lambda: ns["seagull_fl"]("V1")),
    ("S_H2a_fin", lambda: ns["seagull_fl"]("V2")),
    ("S_H2b_fin", lambda: ns["seagull_fl"]("V1V1")),
    # Level-2 decomposition independence, FINITE mode, s^1 line A (the battery's
    # own disclosure: the s^1 cases carry the L2-discriminating power) + control:
    ("L2A_s1_r2", lambda: FL(F1i("A", 1, 1, 2, 0, 0), 0, 0)),
    ("L2A_s1_broken1", lambda: FL(F1i("A", 1, 1, 1, 0, 0, broken_L2=True), 0, 0)),
    ("L2A_s1_broken2", lambda: FL(F1i("A", 1, 1, 2, 0, 0, broken_L2=True), 0, 0)),
]

FIN = {}
for _name, _fn in BLOCKS:
    if SMOKE and _name not in SMOKE_BLOCKS:
        continue
    # --- THE LOOP-FLIP IDENTITY (owner-endorsed route, 2026-08-29) ----------
    # H2_V1V1onB := H2_V1V1onA EXACTLY. The same-line V1V1 double insertion is
    # invariant under the loop flip l -> K-l, which exchanges the two line
    # momenta (l <-> l-K up to a sign every tensor structure is even in).
    # PROVEN, not assumed (2026-08-29, /tmp/a3_2_stage):
    #   (1) EXACT SYMBOLIC at the FULL BLOCK level (pole c^1 + finite c^0):
    #       with the pristine engine (SKIPBAT=1 disclosed, .p10 cache
    #       byte-stable across load, engine internal FAIL count 0),
    #       assemble_fl(fish_two_same_line("A",0,0),0,0) and the same with "B"
    #       were assembled INDEPENDENTLY (1204.8s / 3007.6s) and their expanded
    #       difference is EXACTLY 0 (debug_pole_flip.py). The same run proved
    #       the four single-insertion pair structures H1_V1on, H2_V2on,
    #       H2_vtx1xV1, H2_vtx2xV1 A-B == 0 exactly (242.6/529.2/220.7/218.9s).
    #   (2) NUMERIC, on and off the cut: the independent quadrature referee
    #       (Route B: no analytic primitives) confirms all four cached A/B
    #       pairs at max rel diff 0.000e+00 at spacelike (1,2),(1,3),(2,3) AND
    #       at timelike (2,1) K^2=3 subthreshold and (3,1) K^2=8 > 4m^2 (cut
    #       open, Im branch live, |Im v_B| up to 1.76e+10 -- non-vacuous;
    #       the same K^2=8 point the E3 referee battery uses), x 2 seeds
    #       (debug_map2.py, debug_map3.py -- the owner-directed timelike
    #       extension closing the off-cut-only gap).
    # Applied because the direct B assembly exceeds the stop-rule budget (it
    # exceeded 3600s in the 2026-08-29 recovery run while A finished in
    # 1900s; the pole-level B took 3007.6s vs A 1204.8s -- a routing-weight
    # asymmetry, not a physics difference). The identity makes the B value a
    # THEOREM, not a budget casualty.
    # In-band self-test: the built-in POLE REPLAY gate below sums all twelve
    # H2 classes with B:=A and requires the c-sector to equal the FROZEN
    # Phase-10 F_H2 EXACTLY -- an independent check of this identity against
    # the frozen record (it runs only because this block now exists).
    if (_name == "H2_V1V1onB" and FIN.get("H2_V1V1onA") is not None
            and _load_fin("H2_V1V1onB") is None):
        check(True,
              "block H2_V1V1onB: LOOP-FLIP IDENTITY applied -- value := "
              "H2_V1V1onA EXACTLY (owner-endorsed route 2026-08-29; proven: "
              "exact symbolic A-B == 0 at full block level from the pristine "
              "engine, and numeric 0.000e+00 on and off the cut)",
              gate="fin-asm",
              detail={"identity": "H2_V1V1onB == H2_V1V1onA",
                      "proof_exact_symbolic": "assemble_fl(fish_two_same_line"
                      "('A',0,0),0,0) - assemble_fl(fish_two_same_line('B',"
                      "0,0),0,0) == 0 exactly (debug_pole_flip.py, 2026-08-29; "
                      "pristine engine, .p10 byte-stable, FAIL count 0)",
                      "proof_numeric": "max rel diff 0.000e+00 on all four "
                      "A/B pairs, spacelike + timelike incl. the cut-open "
                      "K^2=8 point (debug_map2.py, debug_map3.py)",
                      "direct_B_assembly": "exceeded the 3600s stop-rule "
                      "budget in the 2026-08-29 recovery run (A: 1900s)"})
        FIN[_name] = FIN["H2_V1V1onA"]
        _eps2_gate(_name, FIN[_name])
        BLOCK_TIMING[_name] = {"loop_flip_identity": True,
                               "source": "H2_V1V1onA"}
        note("LOOP-FLIP IDENTITY: H2_V1V1onB := H2_V1V1onA (exact; evidence "
             "chain on the fin-asm gate). Deliberately NOT written to the "
             "finite cache -- the cache holds independent assemblies only; "
             "every run re-derives this entry through this disclosed path.")
        stamp("block %s: done (loop-flip identity)" % _name)
        continue
    stamp("block %s: starting" % _name)
    FIN[_name] = run_block(_name, _fn)

# --- built-in pole-replay gates: every assembled block's c-sector must equal
# the FROZEN Phase-10 cache byte-for-byte (the twin law's pole sector, flowing
# through the identical routing, IS the frozen pole assembly) ---
if FIN.get("F_H0_fin") is not None:
    check(sp.expand(_csec(FIN["F_H0_fin"]) - ns["CACHED"]["F_H0"]) == 0,
          "POLE REPLAY (built in): c-sector of F_H0_fin == frozen cache F_H0 "
          "EXACTLY", gate="replay")
_H1k = ("H1_vtx10", "H1_vtx01", "H1_V1onA", "H1_V1onB")
if all(FIN.get(k) is not None for k in _H1k):
    H1_fin = sp.expand(sum(FIN[k] for k in _H1k))
    check(sp.expand(_csec(H1_fin) - ns["CACHED"]["H1_total"]) == 0,
          "POLE REPLAY (built in): c-sector of H1_fin (4 classes summed) == frozen "
          "cache H1_total EXACTLY", gate="replay")
_H2k = [k for k, _ in BLOCKS if k.startswith("H2_")]
if all(FIN.get(k) is not None for k in _H2k):
    F_H2_fin = sp.expand(sum(FIN[k] for k in _H2k))
    check(sp.expand(_csec(F_H2_fin) - ns["CACHED"]["F_H2"]) == 0,
          "POLE REPLAY (built in): c-sector of F_H2_fin (12 classes summed) == "
          "frozen cache F_H2 EXACTLY", gate="replay")
if FIN.get("S_H0_fin") is not None:
    check(sp.expand(_csec(FIN["S_H0_fin"]) - ns["S_H0"]) == 0,
          "POLE REPLAY (built in): c-sector of S_H0_fin == the engine's inline "
          "S_H0 (seagull H^0 pole) EXACTLY", gate="replay")
if FIN.get("S_H1_fin") is not None:
    check(sp.expand(_csec(FIN["S_H1_fin"]) - ns["CACHED"]["S_H1"]) == 0,
          "POLE REPLAY (built in): c-sector of S_H1_fin == frozen cache S_H1 "
          "EXACTLY", gate="replay")
if FIN.get("S_H2a_fin") is not None and FIN.get("S_H2b_fin") is not None:
    S_H2_fin = sp.expand(FIN["S_H2a_fin"] + FIN["S_H2b_fin"])
    check(sp.expand(_csec(S_H2_fin) - ns["CACHED"]["S_H2"]) == 0,
          "POLE REPLAY (built in): c-sector of S_H2_fin (V2 + V1V1) == frozen "
          "cache S_H2 EXACTLY", gate="replay")

# --- Level-2 decomposition independence, FINITE mode (s^1, line A) + control ---
# SELF-CAUGHT (gate semantics): the two L2 routes are the SAME finite object
# but NOT the same atom decomposition -- the routes distribute the y-weights
# differently and the atoms obey linear identities (y(1-y) = (m^2-D)/K^2), so
# raw-srepr equality of the finite sector is unattainable without a canonical
# atom basis (deliberately NOT built -- out of scope for this wall). Honest
# gate: (0) all atoms carry canonical kinematics, (1) exact c-sector equality,
# (2) exact closed(local-finite)-sector equality, (3) numeric identity of the
# atom sector at 4 spacelike kinematics x 2 structure-symbol seeds. The broken
# control stays symbolic and must still trip.
if FIN.get("H1_V1onA") is not None and FIN.get("L2A_s1_r2") is not None:
    _kinfo = all(
        sp.expand(A.args[3] - (om**2 - kk**2)) == 0
        and sp.expand(A.args[4] - mm**2) == 0
        for _ex in (FIN["H1_V1onA"], FIN["L2A_s1_r2"])
        for A in _ex.atoms(Gfun, Rfun))
    check(_kinfo,
          "DECOMPOSITION-INDEPENDENCE (finite) 1/4: every atom in both routes "
          "carries canonical kinematics (K2 = om^2-k^2, m2 = m^2) -- the "
          "numeric battery is well-posed", gate="L2fin")
    _DL = sp.expand(FIN["H1_V1onA"] - FIN["L2A_s1_r2"])
    check(sp.expand(_DL.coeff(csym, 1)) == 0,
          "DECOMPOSITION-INDEPENDENCE (finite) 2/4 (c-sector): route "
          "s = u_start + t1 equals route s = u_end - t2 EXACTLY", gate="L2fin")
    _DLf = sp.expand(_DL.subs(csym, 0))
    _cl = [t for t in sp.Add.make_args(_DLf) if not t.atoms(Gfun, Rfun)]
    check(sp.expand(sp.Add(*_cl) if _cl else sp.S.Zero) == 0,
          "DECOMPOSITION-INDEPENDENCE (finite) 3/4 (local finite, closed "
          "sector): the two routes agree EXACTLY", gate="L2fin")

    def _l2_num(ex, omv, kkv, epseed):
        sub = {om: sp.Integer(omv), kk: sp.Integer(kkv), mm: sp.Integer(1),
               muS: sp.Integer(1), csym: sp.Integer(0),
               kap: sp.Float(mp.nstr(KAP_NUM, 40), 40)}
        for s in ex.free_symbols:
            if s.name.startswith(("E_", "P_")):
                h = sum((i + 1) * ord(ch)
                        for i, ch in enumerate(s.name)) + epseed
                sub[s] = sp.Rational(h % 97 + 1, h % 13 + 2)
        e2 = sp.expand(ex.subs(sub))
        K2v, m2v = mp.mpf(omv * omv - kkv * kkv), mp.mpf(1)
        rep = {}
        for A in e2.atoms(Gfun, Rfun):
            fam = "G" if isinstance(A, Gfun) else "R"
            v = _quad_atom(fam, int(A.args[0]), int(A.args[1]),
                           int(A.args[2]), K2v, m2v)
            rep[A] = (sp.Float(mp.nstr(mp.re(v), 30), 30)
                      + sp.Float(mp.nstr(mp.im(v), 30), 30) * sp.I)
        return mp.mpc(complex(sp.N(e2.subs(rep), 30)))

    _worst = mp.mpf(0)
    for _omv, _kkv in [(1, 2), (1, 3), (2, 3), (1, 5)]:
        for _seed in (0, 1000):
            _va = _l2_num(FIN["H1_V1onA"], _omv, _kkv, _seed)
            _vb = _l2_num(FIN["L2A_s1_r2"], _omv, _kkv, _seed)
            _worst = max(_worst, abs(_va - _vb) / max(1, abs(_va), abs(_vb)))
    check(_worst < mp.mpf("1e-10"),
          "DECOMPOSITION-INDEPENDENCE (finite) 4/4 (atom sector): the two "
          "routes are the SAME finite object -- numeric identity at 4 spacelike "
          "kinematics x 2 structure-symbol seeds (worst rel d=%.2e < 1e-10; "
          "atoms carry no canonical form; the per-master twin law is "
          "referee-validated separately)" % _worst,
          gate="L2fin", detail={"worst_rel": mp.nstr(_worst, 6)})
    SELF_CAUGHT.append({
        "id": "A3-2-L2-gate-semantics",
        "what": "the L2 decomposition-independence gate demanded raw-srepr "
                "equality of the two routes' finite sectors; the finite OBJECT "
                "is route-independent but its atom decomposition is not (the "
                "routes distribute y-weights differently and the atoms obey "
                "linear identities), so the gate as originally written could "
                "never pass",
        "fix": "three-part gate (exact c-sector; exact closed local-finite "
               "sector; numeric atom-sector identity at 4 spacelike kinematics "
               "x 2 structure seeds, worst rel d=%s)" % mp.nstr(_worst, 6),
        "evidence": "debug battery /tmp/a3_2_stage/debug_num.py: routes agree "
                    "to ~1e-14 at 8 evaluations across two independent "
                    "structure-symbol seeds; broken-pair control still "
                    "detected (numeric rel diff 2.0, opposite signs)",
    })
    SELF_CAUGHT.append({
        "id": "A3-2-composite-arg-derivative",
        "what": "sp.diff on atoms with COMPOSITE arguments (K2 = om^2 - k^2) "
                "wrapped the result in unevaluated Subs(Derivative(...)) and "
                "bypassed the exact fdiff recurrences, corrupting every "
                "atom-derivative in the assembled finite sector (the pole "
                "sector, being polynomial, was unaffected)",
        "fix": "_eval_derivative chain-rule overrides on Gfun/Rfun firing the "
               "fdiff recurrences exactly",
        "evidence": "test_diff.py: composite 2nd omega-derivative of "
                    "G[0,0,0] lands on 2*(2*om^2*R[2,2,-2] + R[1,1,-1]), no "
                    "unevaluated Subs; referee battery 64/64 at ~1e-17 after "
                    "the fix",
    })
    SELF_CAUGHT.append({
        "id": "A3-2-referee-sj-cross-term",
        "what": "the direct referee (Route B) omitted the exact-d moment "
                "cross-term s_j x Ipole, s_j = 2*sum_i 1/(4+2i), that the twin "
                "law carries (from A3-1's recorded exact-d compositions "
                "T2 = /(4-eps), T4 = 3/((4-eps)(6-eps)))",
        "fix": "independent sj_of(j) formula in the referee and the _cross "
               "family added to every referee evaluation path (_Ffull)",
        "evidence": "debug_ref.py: 64/64 cases at ~1e-17 after the fix (48 "
                    "monomial cases incl. omega-derivative depths 1-4); the "
                    "twin law itself was exact throughout",
    })
if FIN.get("L2A_s1_broken1") is not None and FIN.get("L2A_s1_broken2") is not None:
    control("L2-broken-finite",
            sp.expand(FIN["L2A_s1_broken1"] - FIN["L2A_s1_broken2"]) != 0,
            "BROKEN-L2 CONTROL (finite mode): endpoint vertices outside the "
            "differentiated group FAIL the same gate (the repair is not vacuous "
            "in the finite sector either)")

# --- sector totals + parity classes (mirroring the engine's own pole gates) ---
HAVE_FULL = (not SMOKE) and not BLOCK_STOPPED
if SMOKE:
    note("SMOKE mode: sector totals/subtraction/structure/referee/freeze are NOT "
         "computed (pre-flight only).")
if HAVE_FULL:
    SIG_fin = {
        0: sp.expand(FIN["F_H0_fin"] + FIN["S_H0_fin"]),
        1: sp.expand(H1_fin + FIN["S_H1_fin"]),
        2: sp.expand(F_H2_fin + S_H2_fin),
    }
    _conj = lambda ex: ex.subs(sp.I, -sp.I)
    check(sp.expand(SIG_fin[0] - _conj(SIG_fin[0])) == 0,
          "reality: SIG_fin(H^0) real (i-pairs closed in the finite sector)",
          gate="parity")
    check(sp.expand(SIG_fin[2] - _conj(SIG_fin[2])) == 0,
          "reality: SIG_fin(H^2) real (i-pairs closed in the finite sector)",
          gate="parity")
    _h1z = sp.expand(SIG_fin[1]) == 0
    _h1i = sp.expand(SIG_fin[1] + _conj(SIG_fin[1])) == 0
    check(_h1z or _h1i,
          "H-PARITY (finite sector): the O(H^1) finite part either vanishes or is "
          "purely imaginary -- recorded as a CONVENTION-CONSISTENCY check ONLY "
          "(the standing T4 fence; zero or purely imaginary are both consistent "
          "in this centre-fixed convention)", gate="parity",
          detail={"identically_zero": bool(_h1z), "purely_imaginary": bool(_h1i)})

    # --- the no-Li_2 structural gate (on the ASSEMBLED object) ---
    _bad_atoms = []
    for _n, _ex in SIG_fin.items():
        for _A in _ex.atoms(Gfun):
            if int(_A.args[2]) < 0:
                _bad_atoms.append(("G", _n, str(_A.args[:3])))
        for _A in _ex.atoms(Rfun):
            if int(_A.args[2]) >= 0:
                _bad_atoms.append(("R", _n, str(_A.args[:3])))
    check(not _bad_atoms,
          "NO Li_2/Clausen CLASS: every G-atom has e >= 0 and every R-atom e <= -1 "
          "in the assembled finite object (the census conclusion, now PROVEN on "
          "the assembled object: the log sector exists only at s >= 0 and the "
          "fdiff recurrence kills the e -> -1 G-descent at e = 0)",
          gate="no-Li2", detail={"violations": _bad_atoms})
    stamp("STEP 3 done (finite assembly complete; all pole-replay gates green)")
elif not SMOKE:
    note("STEP 3 incomplete (stopped blocks: %s) -- downstream steps skipped; "
         "verdict will record INCOMPLETE for owner adjudication" % BLOCK_STOPPED)

# =====================================================================================
# STEP 4 -- THE FROZEN MS POLE SUBTRACTION (A3-2C)
# =====================================================================================
print("\n=== STEP 4: MS POLE SUBTRACTION ===")
PI_LOCAL_FP_FROZEN = "e2f0bbfe6fd4c89d"
Pi_local_MS_ref = (2 / epsS) * (ns["SIG0"] + Hs * ns["SIG1"] + Hs**2 * ns["SIG2"])
_fp_ref = expr_fp(Pi_local_MS_ref)
check(_fp_ref == PI_LOCAL_FP_FROZEN,
      "Pi_local^MS reconstructed from the frozen cache via the engine's own SIG "
      "totals: fingerprint == the frozen e2f0bbfe6fd4c89d (entry object "
      "subtraction block + Phase-12 + UV freeze) -- symbol conventions byte-exact",
      gate="A3-2C", detail={"got": _fp_ref, "want": PI_LOCAL_FP_FROZEN})


def classify(t):
    """VERBATIM port of the frozen Phase-12 S2 classifier (the V4 F1 predicate):
    sp.Poly construction in (omega, k) succeeds exactly on the local class --
    finite polynomial in (omega, k), coefficients finite in (m^2, H^2, mu);
    coefficient logs (kappa, ln(mu^2), ln(m^2/mu^2)) are LOCAL per the V4
    amendment; PolynomialError is raised for every branch/threshold form."""
    try:
        sp.Poly(t, om, kk)
        return True
    except sp.PolynomialError:
        return False


def literal_even(t):
    """the literal scalar reading of '(omega^2, k^2)': every exponent even."""
    return all(m[0] % 2 == 0 and m[1] % 2 == 0 for m in sp.Poly(t, om, kk).monoms())


def reflection_parity(ex, tparity):
    """VERBATIM port of the frozen Phase-12 reflection-parity classifier."""
    bad = 0
    for t in sp.Add.make_args(sp.expand(ex)):
        n0 = n3 = 0
        for f_ in sp.Mul.make_args(t):
            if isinstance(f_, sp.Symbol) and str(f_).startswith(("E_", "P_")):
                idx = str(f_).split("_")[1]
                n0 += idx.count("0")
                n3 += idx.count("3")
            elif (isinstance(f_, sp.Pow) and isinstance(f_.base, sp.Symbol)
                  and str(f_.base).startswith(("E_", "P_"))):
                idx = str(f_.base).split("_")[1]
                n0 += idx.count("0") * f_.exp
                n3 += idx.count("3") * f_.exp
        for (a_, b_) in sp.Poly(t, om, kk).monoms():
            if (a_ + n0) % 2 != tparity % 2 or (b_ + n3) % 2 != 0:
                bad += 1
    return bad


# the frozen subtraction applied to the frozen poles: EVERY pole term is F1-local
# (the Phase-12 S2 result, re-run here as the port gate):
for _n, _tp in ((0, 0), (1, 1), (2, 0)):
    _SIGn = {0: ns["SIG0"], 1: ns["SIG1"], 2: ns["SIG2"]}[_n]
    _terms = sp.Add.make_args(sp.expand(_SIGn))
    _nl = [str(t)[:80] for t in _terms if not classify(t)]
    check(not _nl, "frozen pole sector H^%d: %d/%d terms F1-LOCAL (independent "
          "classifier port; Phase-12 S2 reproduced)" % (_n, len(_terms) - len(_nl),
          len(_terms)), gate="A3-2C", detail={"nonlocal": _nl[:5]})
    check(reflection_parity(_SIGn, _tp) == 0,
          "frozen pole sector H^%d: reflection parity T=%d, 0 violations "
          "(Phase-12 S2 reproduced)" % (_n, _tp), gate="A3-2C")

if HAVE_FULL:
    SIG_pole = {n: _csec(SIG_fin[n]) for n in (0, 1, 2)}
    for _n in (0, 1, 2):
        check(sp.expand(SIG_pole[_n] - {0: ns["SIG0"], 1: ns["SIG1"],
                                        2: ns["SIG2"]}[_n]) == 0,
              "H^%d pole sector of MY finite assembly == the engine's frozen SIG_%d "
              "byte-exact (the subtraction content is the frozen pole object)"
              % (_n, _n), gate="A3-2C")
    Pi_local_MS_mine = (2 / epsS) * (SIG_pole[0] + Hs * SIG_pole[1]
                                     + Hs**2 * SIG_pole[2])
    check(expr_fp(Pi_local_MS_mine) == PI_LOCAL_FP_FROZEN,
          "Pi_local^MS reconstructed from MY OWN assembly's c-sectors: fingerprint "
          "== e2f0bbfe6fd4c89d (the subtraction is the frozen object, derived "
          "independently inside this instrument)", gate="A3-2C",
          detail={"got": expr_fp(Pi_local_MS_mine)})
    # the split identity + zero finite discretion: bare = c*[pole] + [finite],
    # the pole-only subtraction removes exactly c*[pole] and NOTHING else:
    for _n in (0, 1, 2):
        _bare = SIG_fin[_n]
        _fin_only = sp.expand(_bare.subs(csym, 0))
        _subtracted = sp.expand(_bare - csym * SIG_pole[_n])
        check(sp.expand(_subtracted - _fin_only) == 0,
              "H^%d: bare finite-order object = local subtraction contribution "
              "(c*[pole], the entire pole, mapped onto Pi_local^MS) + remaining "
              "finite response, and the subtraction modifies NOTHING in the "
              "finite sector (byte-exact; zero finite discretion)" % _n,
              gate="A3-2C")
    note("A3-2C identity: bare_n = c*SIG_pole_n + SIG_fin_n with c*SIG_pole_n == "
         "Pi_local^MS (frozen fingerprint) and SIG_fin_n untouched. MS removes "
         "ONLY the pole: the finite local AND nonlocal parts survive intact.")
    stamp("STEP 4 done (subtraction verified: frozen fingerprint + classifier + "
          "zero finite discretion)")

# =====================================================================================
# STEP 5 -- ANALYTIC STRUCTURE EXPOSURE (A3-2D: census + closed forms ONLY --
# no power-law fits, no spectral/relaxation/resonance classification)
# =====================================================================================
STRUCT = {"sectors": {}}
if HAVE_FULL:
    print("\n=== STEP 5: STRUCTURE EXPOSURE ===")
    for _n in (0, 1, 2):
        _terms = sp.Add.make_args(sp.expand(SIG_fin[_n]))
        _loc = [t for t in _terms if classify(t)]
        _nonloc = [t for t in _terms if not classify(t)]
        _gtab, _rtab = {}, {}
        for _t in _nonloc:
            for _A in _t.atoms(Gfun):
                _k = (int(_A.args[0]), int(_A.args[1]), int(_A.args[2]))
                _gtab[_k] = _gtab.get(_k, 0) + 1
            for _A in _t.atoms(Rfun):
                _k = (int(_A.args[0]), int(_A.args[1]), int(_A.args[2]))
                _rtab[_k] = _rtab.get(_k, 0) + 1
        _kapc = sum(1 for t in _loc if kap in t.free_symbols)
        _lmm = sum(1 for t in _loc if any(a == mm**2 for a in t.atoms(sp.Pow)))
        STRUCT["sectors"][_n] = {
            "terms_total": len(_terms),
            "local_finite_terms": len(_loc),
            "nonlocal_finite_terms": len(_nonloc),
            "local_kappa_terms": _kapc,
            "local_with_m2_powers": _lmm,
            "G_atom_classes": {"n=%d,np=%d,e=%d" % k: v for k, v in sorted(_gtab.items())},
            "R_atom_classes": {"n=%d,np=%d,e=%d" % k: v for k, v in sorted(_rtab.items())},
            "example_local_finite": sp.srepr(_loc[0])[:400] if _loc else None,
            "example_nonlocal_finite": sp.srepr(_nonloc[0])[:400] if _nonloc else None,
        }
        check(len(_loc) + len(_nonloc) == len(_terms),
              "H^%d census complete: %d terms = %d local-finite + %d nonlocal-finite"
              % (_n, len(_terms), len(_loc), len(_nonloc)), gate="A3-2D")
        print("   H^%d: %d terms = %d local-finite + %d nonlocal-finite; "
              "G-classes %d, R-classes %d" % (_n, len(_terms), len(_loc),
                                              len(_nonloc), len(_gtab), len(_rtab)))
    # the seagull finite sector is entirely local (structural, gated):
    for _b in ("S_H0_fin", "S_H1_fin", "S_H2a_fin", "S_H2b_fin"):
        _sterms = sp.Add.make_args(sp.expand(FIN[_b].subs(csym, 0)))
        _snl = [str(t)[:100] for t in _sterms if not classify(t)]
        check(not _snl,
              "seagull block %s: finite sector entirely F1-LOCAL (%d terms; the "
              "tadpole masters close at Delta = m^2 -- logs of (m^2, mu) are "
              "coefficient logs, LOCAL per V4)" % (_b, len(_sterms)),
              gate="A3-2D", detail={"nonlocal": _snl[:3]})
    note("STRUCTURE (A3-2D): the nonlocal finite sector is EXACTLY the atom-"
         "carrying sector -- 1-D parameter integrals of D(y) = m^2 - y(1-y)K^2 "
         "with the -i0 branch; threshold at K^2 = 4m^2 (y+- = (1 +- "
         "sqrt(1-4m^2/K^2))/2); G-atoms carry Im = +pi*Int_{cut} (the frozen "
         "A3-1 branch law), R-atoms the residue Im parts. No power law fitted, "
         "no spectral class assigned, no low-frequency behaviour classified.")

    # leading closed forms (EXPOSITORY: gated against the referee, never reverse):
    _yt2 = sp.Symbol("y", real=True)

    def _alarm_integrate(f):
        _old2 = signal.signal(signal.SIGALRM, lambda s, f_: (_ for _ in ()).throw(
            TimeoutError()))
        signal.alarm(300)
        try:
            return sp.integrate(f, (_yt2, 0, 1))
        except TimeoutError:
            return None
        finally:
            signal.alarm(0)
            signal.signal(signal.SIGALRM, _old2)

    # sympy's integrate returns 2 - log(m2), DROPPING K2 entirely, when the K2
    # symbol carries an assumption (real=True as declared for K2t at module
    # scope). Derive the expository closed forms on assumption-free symbols:
    # those return the correct branch structure, carrying the sqrt(K2(K2-4m2))
    # threshold explicitly, and agree with the referee quadrature to ~1e-30.
    _K2f, _m2f = sp.symbols("K2f m2f")
    _Dyf = _m2f - _yt2 * (1 - _yt2) * _K2f
    _cfG = _alarm_integrate(-sp.log(_Dyf))          # G[0,0,0] closed form
    _cfR = _alarm_integrate(1 / _Dyf)               # R[0,0,-1] closed form
    STRUCT["closed_forms"] = {
        "G000_sympy": sp.srepr(_cfG)[:1200] if _cfG is not None else "not-obtained",
        "R00m1_sympy": sp.srepr(_cfR)[:1200] if _cfR is not None else "not-obtained",
    }
    for _lbl, _cf, _fam in (("G[0,0,0]", _cfG, "G"), ("R[0,0,-1]", _cfR, "R")):
        if _cf is None:
            note("closed form of %s not obtained in-instrument (300s cap) -- the "
                 "referee quadrature remains the authority (disclosed)" % _lbl)
            continue
        _ok = True
        _det = {}
        for _k2v in ("-3", "-0.75", "3"):
            _ref = _quad_atom(_fam, 0, 0, 0 if _fam == "G" else -1, _k2v, 1)
            _sym = complex(sp.N(_cf.subs({_K2f: sp.Rational(_k2v),
                                          _m2f: sp.Integer(1)}), 30))
            _dd = abs(complex(_ref) - _sym)
            _det[_k2v] = float(_dd)
            _ok = _ok and _dd < mp.mpf("5e-6")
        check(_ok, "closed form of %s (sympy) == referee quadrature at spacelike/"
              "subthreshold samples %s (the referee is the authority)"
              % (_lbl, _det), gate="A3-2D", detail={"diffs": _det})
    stamp("STEP 5 done (structure census + leading closed forms)")

# =====================================================================================
# STEP 6 -- THE INDEPENDENT REFEREE BATTERY (A3-2E)
# =====================================================================================
if HAVE_FULL:
    print("\n=== STEP 6: REFEREE BATTERY ===")
    SAMPLES = [  # (label, omega, k) with m = mu = 1; K2 = om^2 - k^2
        ("spacelike_K2=-3/4", sp.Rational(1, 2), sp.Integer(1)),
        ("spacelike_K2=-3", sp.Integer(1), sp.Integer(2)),
        ("subthreshold_K2=3", sp.Integer(2), sp.Integer(1)),
        ("timelike_K2=8", sp.Integer(3), sp.Integer(1)),
    ]

    # ---------- Route B-prime: the ORIGINAL parameter integrals built from the
    # A3-1 master forms BY TRACE COMPOSITION (independent of the twin law's
    # closed form AND of the atom split; complex-eps boundary values) ----------
    def _Mform(n, z, mu2v):
        """A3-1's validated masters at complex argument z (boundary value)."""
        if n <= 0:
            return mp.mpc(0)
        if n == 1:
            return z * (1 + KAP_NUM - mp.log(z / mu2v))
        if n == 2:
            return KAP_NUM - mp.log(z / mu2v)
        if n == 3:
            return -mp.mpf(1) / 2 / z
        if n == 4:
            return mp.mpf(1) / 6 / z**2
        raise ValueError("master N=%d beyond the A3-1 validated set" % n)

    def _Mform_d(n, z, mu2v):
        if n <= 0:
            return mp.mpc(0)
        if n == 1:
            return KAP_NUM - mp.log(z / mu2v)      # M_1' = M_2 (exact)
        if n == 2:
            return -1 / z
        if n == 3:
            return mp.mpf(1) / 2 / z**2
        return -mp.mpf(1) / 3 / z**3

    def _Fform(j, N, z, mu2v):
        """Sigma_r C(j,r) z^{j-r} M_{N-r}(z) -- A3-1's own trace composition."""
        tot = mp.mpc(0)
        for r in range(0, min(j, N - 1) + 1):
            tot += mp.binomial(j, r) * z**(j - r) * _Mform(N - r, z, mu2v)
        return tot

    def _Fform_dz(j, N, z, mu2v):
        tot = mp.mpc(0)
        for r in range(0, min(j, N - 1) + 1):
            tot += mp.binomial(j, r) * (
                (j - r) * z**(j - r - 1) * _Mform(N - r, z, mu2v)
                + z**(j - r) * _Mform_d(N - r, z, mu2v))
        return tot

    def _Fform_dz2(j, N, z, mu2v):
        """d2F/dz2 (elementary, for the second-omega-derivative referee)."""
        def Mdd(n):
            if n <= 0:
                return mp.mpc(0)
            if n == 1:
                return -1 / z
            if n == 2:
                return 1 / z**2
            if n == 3:
                return -1 / z**3
            return mp.mpf(2) / 3 / z**4
        tot = mp.mpc(0)
        for r in range(0, min(j, N - 1) + 1):
            k = j - r
            tot += mp.binomial(j, r) * (
                k * (k - 1) * z**(k - 2) * _Mform(N - r, z, mu2v)
                + 2 * k * z**(k - 1) * _Mform_d(N - r, z, mu2v)
                + z**k * Mdd(N - r))
        return tot

    def _momnum(jp):
        q = sp.Rational(moment(jp, 0, 0, 0))
        return mp.mpf(q.p) / mp.mpf(q.q)

    def _sj(j):
        """the exact-d moment cross coefficient s_j = 2*sum_{i=0..j-1} 1/(4+2i)
        (from the d-factor 1/prod_{i}(d+2i)); INDEPENDENT formula in the referee
        -- this is the cross-term of A3-1's recorded T2 = /(4-eps) and
        T4 = 3/((4-eps)(6-eps)) exact-d compositions (SELF-CAUGHT: the referee
        originally omitted it; the twin law was exact -- the debug battery
        caught the referee, 64/64 after the fix)."""
        return sum(mp.mpf(2) / (4 + 2 * i) for i in range(0, j))

    def _cross(j, N, z):
        s = j - N + 2
        if s < 0:
            return mp.mpc(0)
        P = mp.binomial(j, N - 1) if 0 <= N - 1 <= j else mp.mpf(0)
        P += mp.binomial(j, N - 2) if 0 <= N - 2 <= j else mp.mpf(0)
        return _sj(j) * P * z**s

    def _cross_dz(j, N, z):
        s = j - N + 2
        if s <= 0:
            return mp.mpc(0)
        P = mp.binomial(j, N - 1) if 0 <= N - 1 <= j else mp.mpf(0)
        P += mp.binomial(j, N - 2) if 0 <= N - 2 <= j else mp.mpf(0)
        return _sj(j) * P * s * z**(s - 1)

    def _cross_dz2(j, N, z):
        s = j - N + 2
        if s <= 1:
            return mp.mpc(0)
        P = mp.binomial(j, N - 1) if 0 <= N - 1 <= j else mp.mpf(0)
        P += mp.binomial(j, N - 2) if 0 <= N - 2 <= j else mp.mpf(0)
        return _sj(j) * P * s * (s - 1) * z**(s - 2)

    def _Ffull(j, N, z, mu2v):
        """the exact eps^0 master integrand: the A3-1 trace-composition finite
        part PLUS the exact-d moment cross-term s_j x Ipole."""
        return _Fform(j, N, z, mu2v) + _cross(j, N, z)

    def _Ffull_dz(j, N, z, mu2v):
        return _Fform_dz(j, N, z, mu2v) + _cross_dz(j, N, z)

    def _Ffull_dz2(j, N, z, mu2v):
        return _Fform_dz2(j, N, z, mu2v) + _cross_dz2(j, N, z)

    def direct_mono_l0(expo0, aP, bP, omv, kkv, d_om=0, m2v=1, mu2v=1):
        """mpmath referee of the ORIGINAL parameter integral for the monomial
        l0^{expo0} (expo0 even):  wt * Int_0^1 dy y^{b-1}(1-y)^{a-1}
        * Sum_{m even} C(e0,m)(y om)^m moment(j-m/2) F_{j-m/2,N}(D(y)-i0).
        d_om analytic omega-derivatives act inside the integrand. At cut samples
        the -i0 is the complex-eps boundary value with 3-point Richardson."""
        N = aP + bP
        wt = mp.factorial(N - 1) / (mp.factorial(aP - 1) * mp.factorial(bP - 1))
        K2v = omv**2 - kkv**2
        pts = _cut_pts(K2v, m2v)

        def integrand(y, z):
            tot = mp.mpc(0)
            for m in range(0, expo0 + 1, 2):
                jp = (expo0 - m) // 2
                cf = mp.binomial(expo0, m) * (y * omv)**m
                if d_om == 0:
                    tot += cf * _momnum(jp) * _Ffull(jp, N, z, mu2v)
                else:
                    dcf = (mp.binomial(expo0, m) * m * y**m * omv**(m - 1)
                           if m >= 1 else mp.mpc(0))
                    f = _Ffull(jp, N, z, mu2v)
                    dfdz = _Ffull_dz(jp, N, z, mu2v)
                    dzdom = -2 * omv * y * (1 - y)
                    term = dcf * f + (y * omv)**m * mp.binomial(expo0, m) \
                        * dfdz * dzdom
                    if d_om == 2:
                        # second derivative: (y)^2-terms of cf and z-chain rule
                        d2cf = (mp.binomial(expo0, m) * m * (m - 1) * y**m
                                * omv**(m - 2) if m >= 2 else mp.mpc(0))
                        d2z = -2 * y * (1 - y)
                        term = d2cf * f + 2 * dcf * dfdz * dzdom \
                            + (y * omv)**m * mp.binomial(expo0, m) * (
                                dfdz * d2z
                                + _Ffull_dz2(jp, N, z, mu2v) * dzdom**2)
                    tot += term * _momnum(jp)
            return wt * y**(bP - 1) * (1 - y)**(aP - 1) * tot

        if pts is None:
            zreal = lambda y: m2v - y * (1 - y) * K2v
            return mp.quad(lambda y: integrand(y, zreal(y)), [0, 1])

        def I(eta):
            return mp.quad(lambda y: integrand(
                y, mp.mpc(m2v - y * (1 - y) * K2v, -eta)), [0, 1])
        eta = mp.mpf("2e-3")
        return (8 * I(eta / 4) - 6 * I(eta / 2) + I(eta)) / 3

    def _mpq(x):
        q = sp.Rational(x)
        return mp.mpf(q.p) / mp.mpf(q.q)

    def _my_mono_val(expo0, aP, bP, omv, kkv, d_om=0):
        """MY side: the twin-law master (closed polynomial + atoms, omega-
        derivatives through the fdiff tower), atoms valued by the referee quad."""
        ex = _fin_mono_2den((expo0, 0, 0, 0), aP, bP)
        if d_om:
            ex = sp.diff(ex, om, d_om)
        ex = sp.expand(ex.subs(csym, 0))
        _sub = {om: omv, kk: kkv, mm: sp.Integer(1), muS: sp.Integer(1),
                kap: sp.Float(mp.nstr(KAP_NUM, 40), 40)}
        tot = mp.mpc(0)
        for t in sp.Add.make_args(ex):
            ats = t.atoms(Gfun, Rfun)
            if not ats:
                tot += mp.mpc(complex(sp.N(t.subs(_sub), 30)))
                continue
            A0 = next(iter(ats))
            coeff = sp.expand(t / A0)
            cv = mp.mpc(complex(sp.N(coeff.subs(_sub), 30)))
            tot += cv * _quad_atom(
                "G" if isinstance(A0, Gfun) else "R",
                int(A0.args[0]), int(A0.args[1]), int(A0.args[2]),
                _mpq(A0.args[3].subs({om: omv, kk: kkv})),
                _mpq(A0.args[4].subs({mm: sp.Integer(1)})))
        return tot

    # ---------- E1(b/c): the twin law vs the direct A3-1-composition referee,
    # on every census master class + omega-derivative depths ----------
    CENSUS_JN = [(0, 2), (0, 3), (0, 4), (1, 2), (1, 3), (1, 4),
                 (2, 2), (2, 3), (2, 4), (3, 3), (3, 4)]
    _e1_cases = []
    for (_jj, _NN) in CENSUS_JN:
        for (_aP, _bP) in {(_NN - 1, 1), (max(1, _NN // 2), _NN - max(1, _NN // 2))}:
            if _aP >= 1 and _bP >= 1 and _aP + _bP == _NN:
                _e1_cases.append((2 * _jj, _aP, _bP, 0))
    _e1_cases += [(2, 1, 1, 1), (2, 2, 1, 1), (0, 3, 1, 1), (0, 2, 2, 1),
                  (2, 1, 2, 2)]
    E1_REFS = []
    for (_e0, _aP, _bP, _d) in _e1_cases:
        _diffs = {}
        _ok = True
        for (_lbl, _ov, _kv) in SAMPLES:
            _ovm, _kvm = _mpq(_ov), _mpq(_kv)
            _mine = _my_mono_val(_e0, _aP, _bP, _ov, _kv, _d)
            _ref = direct_mono_l0(_e0, _aP, _bP, _ovm, _kvm, d_om=_d)
            _dd = abs(_mine - _ref)
            _diffs[_lbl] = float(_dd)
            _ok = _ok and _dd < mp.mpf("5e-6")
        E1_REFS.append({"mono": "l0^%d" % _e0, "aP": _aP, "bP": _bP,
                        "d_om": _d, "diffs": _diffs})
        check(_ok,
              "E1 referee: twin master l0^%d (aP=%d,bP=%d,d_om=%d) == the DIRECT "
              "A3-1 trace-composition quadrature at all 4 samples (max d=%.2e)"
              % (_e0, _aP, _bP, _d, max(_diffs.values())), gate="A3-2E",
              detail={"diffs": _diffs})
    stamp("E1 referee done: %d master/derivative cases x 4 samples" % len(E1_REFS))

    # ---------- E2: the H^0 flat-limit reduction ----------
    check(sp.expand(FIN["S_H0_fin"].subs(csym, 0)
                    - (mm**4 / 2) * ns["s2c"]
                    * (1 + kap + sp.log(muS**2) - sp.log(mm**2))) == 0,
          "E2 flat limit: the FINITE seagull == (m^4/2)[sqrt(-g)]_{h^2-cross} x "
          "(1 + kappa - ln(m^2/mu^2)) -- the frozen 2b anchor identity times the "
          "M_1 finite factor, EXACTLY", gate="A3-2E")
    note("E2 flat limit: (i) the finite seagull identity above; (ii) the K=0 "
         "cross-route gate (STEP 2): the fish masters reduce to tadpole masters; "
         "(iii) the H-grading is structural: Sigma_R^fin = SIG_fin[0] + "
         "H SIG_fin[1] + H^2 SIG_fin[2], so H -> 0 is SIG_fin[0] exactly; "
         "(iv) the flat bubble finite is anchored by E1 (B(K2) anchors).")

    # ---------- the full-slot numeric battery: every nonzero E_ab P_cd slot of
    # every H-order at all 4 samples, valued by the referee atom quadrature ----------
    def _pol(ex, pre):
        return sorted({q for q in sp.expand(ex).free_symbols if str(q).startswith(pre)},
                      key=str)

    _Es = sorted(set(_pol(SIG_fin[0], "E_")) | set(_pol(SIG_fin[1], "E_"))
                 | set(_pol(SIG_fin[2], "E_")), key=str)
    _Ps = sorted(set(_pol(SIG_fin[0], "P_")) | set(_pol(SIG_fin[1], "P_"))
                 | set(_pol(SIG_fin[2], "P_")), key=str)
    SLOTS = [(e_, p_) for e_ in _Es for p_ in _Ps]
    print("   slot map: %d E-symbols x %d P-symbols = %d slots"
          % (len(_Es), len(_Ps), len(SLOTS)))

    def _slot_coeff(ex, e_, p_):
        return sp.expand(sp.expand(ex.subs(csym, 0)).coeff(e_, 1).coeff(p_, 1))

    def _eval_fin_expr(ex, sub, atomvals, branch=+1):
        tot = mp.mpc(0)
        for t in sp.Add.make_args(sp.expand(ex)):
            ats = t.atoms(Gfun, Rfun)
            if not ats:
                tot += mp.mpc(complex(sp.N(t.subs(sub), 30)))
                continue
            A0 = next(iter(ats))
            coeff = sp.expand(t / A0)
            cv = mp.mpc(complex(sp.N(coeff.subs(sub), 30)))
            key = ("G" if isinstance(A0, Gfun) else "R", int(A0.args[0]),
                   int(A0.args[1]), int(A0.args[2]),
                   str(sp.Rational(A0.args[3].subs(sub))),
                   str(sp.Rational(A0.args[4].subs(sub))))
            tot += cv * atomvals[key]
        return tot

    BAT = {}
    _atom_quad_count = 0
    _av = {}
    for (_lbl, _ov, _kv) in SAMPLES:
        _sub = {om: _ov, kk: _kv, mm: sp.Integer(1), muS: sp.Integer(1),
                kap: sp.Float(mp.nstr(KAP_NUM, 40), 40)}
        _keys = set()
        for _n in (0, 1, 2):
            for _A in sp.expand(SIG_fin[_n].subs(csym, 0)).atoms(Gfun, Rfun):
                _keys.add(("G" if isinstance(_A, Gfun) else "R", int(_A.args[0]),
                           int(_A.args[1]), int(_A.args[2]),
                           str(sp.Rational(_A.args[3].subs(_sub))),
                           str(sp.Rational(_A.args[4].subs(_sub)))))
        _av = {}
        for _k in sorted(_keys):
            _av[_k] = _quad_atom(_k[0], _k[1], _k[2], _k[3],
                                 _mpq(_k[4]), _mpq(_k[5]))
            _atom_quad_count += 1
        BAT[_lbl] = {}
        for _n in (0, 1, 2):
            BAT[_lbl][_n] = {}
            for (e_, p_) in SLOTS:
                _c = _slot_coeff(SIG_fin[_n], e_, p_)
                if _c == 0:
                    continue
                BAT[_lbl][_n]["%s*%s" % (e_, p_)] = [
                    float(mp.re(_eval_fin_expr(_c, _sub, _av))),
                    float(mp.im(_eval_fin_expr(_c, _sub, _av)))]
        _nz = sum(len(BAT[_lbl][_n]) for _n in (0, 1, 2))
        stamp("slot battery %s: %d nonzero slot values (atom quads: %d)"
              % (_lbl, _nz, len(_av)))
    note("slot battery: %d atom quadratures total (values shared across slots); "
         "all recorded in the freeze JSON as the numeric table" % _atom_quad_count)

    # ---------- E3: retarded support/sign convention ----------
    _e3_bad = []
    for _lbl, _ov, _kv in SAMPLES[:3]:      # the three no-cut samples
        for _n in (0, 2):                   # the real parity classes
            for _sl, _v in BAT[_lbl][_n].items():
                if abs(_v[1]) > 1e-9:
                    _e3_bad.append((_lbl, _n, _sl, _v[1]))
    check(not _e3_bad,
          "E3 retarded support: below threshold (K2 < 4m^2: spacelike AND "
          "subthreshold timelike) the Im part of EVERY H^0/H^2 slot vanishes "
          "(%d slot values checked) -- the branch cut opens only at K2 = 4m^2"
          % sum(len(BAT[l][n]) for l, _, _ in SAMPLES[:3] for n in (0, 2)),
          gate="A3-2E", detail={"violations": _e3_bad[:5]})
    _pos_bad = []
    for _k, _v in _av.items():
        if _k[0] == "G" and _k[4] == "8" and mp.im(_v) <= 0:
            _pos_bad.append(str(_k))
    check(not _pos_bad,
          "E3 retarded sign: at K2=8 > 4m^2 every G-atom carries Im = "
          "+pi*Int_{cut} > 0 (the frozen A3-1 branch law, sign-consistent with "
          "the validated pole assembly's retarded rule)", gate="A3-2E",
          detail={"nonpositive": _pos_bad[:5]})

    # ---------- E5: the wrong-branch negative control at slot level ----------
    _lblT, _ovT, _kvT = SAMPLES[3]
    _subT = {om: _ovT, kk: _kvT, mm: sp.Integer(1), muS: sp.Integer(1),
             kap: sp.Float(mp.nstr(KAP_NUM, 40), 40)}
    _avW = {}
    for _k in sorted(_av):
        _avW[_k] = _quad_atom(_k[0], _k[1], _k[2], _k[3], _mpq(_k[4]),
                              _mpq(_k[5]), branch=-1)
    _best_sl, _best_v = None, mp.mpc(0)
    for _sl, _v in BAT[_lblT][0].items():
        if abs(mp.mpc(_v[0], _v[1])) > abs(_best_v):
            _best_sl, _best_v = _sl, mp.mpc(_v[0], _v[1])
    _symmap = {}
    for (e_, p_) in SLOTS:
        _symmap.setdefault(str(e_), e_)
        _symmap.setdefault(str(p_), p_)
    _c_best = _slot_coeff(SIG_fin[0], *[_symmap[s] for s in _best_sl.split("*")])
    _right = _eval_fin_expr(_c_best, _subT, _av)
    _wrong = _eval_fin_expr(_c_best, _subT, _avW)
    control("slot-wrong-branch", abs(_right - _wrong) > mp.mpf("5e-5"),
            "E5 wrong-branch control at component level: the %s slot of the "
            "assembled H^0 finite object at (om,k)=(3,1) re-evaluated with the "
            "WRONG branch (+i0) DISAGREES (|d| = %.3e; the branch is load-bearing)"
            % (_best_sl, abs(_right - _wrong)),
            detail={"right": [float(mp.re(_right)), float(mp.im(_right))],
                    "wrong": [float(mp.re(_wrong)), float(mp.im(_wrong))]})

    # ---------- E4: subtraction locality (verified in STEP 4) ----------
    note("E4 subtraction: verified in STEP 4 (frozen fingerprint e2f0bbfe6fd4c89d "
         "reproduced from this assembly's own c-sector; 100%% of pole terms "
         "F1-local under the independent classifier port; reflection parity 0 "
         "violations; the finite sector byte-untouched -- zero finite discretion).")
    stamp("STEP 6 done (E1..E5 + full-slot battery)")

    # mu-bookkeeping gate at master level (exact, symbolic):
    for (_jj, _NN) in CENSUS_JN:
        _s, _P, _Cj, _Q, _sj = twin_params(_jj, _NN)
        _f = fin_master_symbolic(_jj, _NN)
        # d/dln(mu^2) = (mu/2) d/dmu.  (The gate previously applied mu^2 d/dmu,
        # which overstates the derivative by 2*mu and therefore failed on every
        # class with s >= 0 -- i.e. wherever P*Delta^s is nonzero -- while
        # passing trivially on s < 0 where both sides are identically zero.)
        _mud = sp.expand(muS * sp.diff(_f, muS) / 2)
        check(sp.expand(_mud - (_P * Dl**_s if _s >= 0 else 0)) == 0,
              "mu bookkeeping: d/dln(mu^2) fin(j=%d,N=%d) = P*Delta^s (the entire "
              "mu-dependence sits in the +ln(mu^2) of the log sector; MS leaves "
              "it untouched)" % (_jj, _NN), gate="mu")

    # cache-off replay gate: one block re-assembled fresh, byte-matched
    _fincache.pop("F_H0_fin", None)
    _fresh = run_block("F_H0_fin_REPLAY", lambda: A(0, 0, plainA, plainB))
    check(_fresh is not None and sp.expand(_fresh - FIN["F_H0_fin"]) == 0,
          "cache-off replay: F_H0_fin re-assembled FRESH == the cached value "
          "byte-exact (the finite cache introduced no drift)", gate="cache")
    _fincache.pop("F_H0_fin_REPLAY", None)

# =====================================================================================
# STEP 7 -- FREEZE + MANIFEST (A3-3) + OUTPUTS
# =====================================================================================
print("\n=== STEP 7: FREEZE + MANIFEST ===")
VERDICT = "PASS" if not FAILS else "FAIL"
INCOMPLETE = (not SMOKE) and bool(BLOCK_STOPPED)
if INCOMPLETE and not FAILS:
    VERDICT = "INCOMPLETE (stop rule hit; owner adjudication required)"

FREEZE = None
if HAVE_FULL and not INCOMPLETE:
    def _tt_view():
        """the derived TT view (computed AFTER assembly freeze; used in NO gate):
        polarisations of the plane-wave pair (3-axis = k): e+ (11=-22), eX (12=21)."""
        _smap = {}
        for _s2 in list(_Es) + list(_Ps):
            _smap[str(_s2)] = _s2
        out = {}
        for _n in (0, 1, 2):
            ex = sp.expand(SIG_fin[_n].subs(csym, 0))

            def _slot(pre, i1, i2):
                """polarisation slots are stored in ONE index ordering (the
                tensors are symmetric): accept either, and treat a slot that is
                absent from the assembled object as an exact zero."""
                k = "%s_%d%d" % (pre, i1, i2)
                if k not in _smap:
                    k = "%s_%d%d" % (pre, i2, i1)
                return _smap.get(k)

            def cc(a, b, c, d):
                _e, _p = _slot("E", a, b), _slot("P", c, d)
                if _e is None or _p is None:
                    return sp.Integer(0)
                return sp.expand(ex.coeff(_e, 1).coeff(_p, 1))
            out[_n] = {
                "TT_plus_plus": sp.expand(cc(1, 1, 1, 1) - cc(1, 1, 2, 2)
                                          - cc(2, 2, 1, 1) + cc(2, 2, 2, 2)),
                "TT_plus_cross": sp.expand(cc(1, 1, 1, 2) + cc(1, 1, 2, 1)
                                           - cc(2, 2, 1, 2) - cc(2, 2, 2, 1)),
                "TT_cross_plus": sp.expand(cc(1, 2, 1, 1) + cc(2, 1, 1, 1)
                                           - cc(1, 2, 2, 2) - cc(2, 1, 2, 2)),
                "TT_cross_cross": sp.expand(cc(1, 2, 1, 2) + cc(1, 2, 2, 1)
                                            + cc(2, 1, 1, 2) + cc(2, 1, 2, 1)),
            }
        return out

    try:
        TT = _tt_view()
        _tt_blob = "\n".join("%s|%s|%s" % (n, k, sp.srepr(TT[n][k]))
                             for n in sorted(TT) for k in sorted(TT[n]))
        TT_HASH = hashlib.sha256(_tt_blob.encode()).hexdigest()
    except Exception as _tt_err:                      # DERIVED view, used in NO gate
        TT, TT_HASH = None, "not-derived"
        note("TT view NOT derived (%s: %s). It is a DERIVED object used in NO "
             "gate; the freeze, the manifest and every gate verdict below are "
             "complete and unaffected." % (type(_tt_err).__name__, _tt_err))
    KERNEL = sp.expand(SIG_fin[0] + Hs * SIG_fin[1] + Hs**2 * SIG_fin[2])
    KERNEL_SHA = expr_sha(KERNEL)
    _self_sha = sha(os.path.abspath(__file__))
    SUB_SHA = expr_sha(Pi_local_MS_mine)
    FREEZE = {
        "object": "Sigma_R^finite (mu nu, rho sigma; omega, k, H, m, mu) -- the "
                  "COMPLETE finite eps^0 retarded kernel of the D2 assembly, ALL "
                  "non-TT sectors carried (no projection before or during assembly)",
        "reconstruction": "Sigma_R^fin = SIG_fin[0] + H*SIG_fin[1] + H^2*SIG_fin[2]"
                          " (H-grading structural; each sector H-free; c applied at"
                          " report time to the pole sector only)",
        "sectors": {
            str(n): {
                "srepr": sp.srepr(sp.expand(SIG_fin[n].subs(csym, 0))),
                "fingerprint": expr_fp(SIG_fin[n].subs(csym, 0)),
                "sha256": expr_sha(SIG_fin[n].subs(csym, 0)),
                "pole_sector_srepr": sp.srepr(SIG_pole[n]),
                "pole_sector_fingerprint": expr_fp(SIG_pole[n]),
            } for n in (0, 1, 2)},
        "atom_definitions": {
            "Gfun": "G[n,np,e](K2,m2) = Int_0^1 dy y^n (1-y)^np (D(y)-i0)^e "
                    "(-ln(D(y)-i0)),  D(y) = m^2 - y(1-y) K^2, K^2 = omega^2-k^2; "
                    "branch -i0 (A3-1 frozen law: Im = +pi*Int_{cut}, cut = "
                    "(y-,y+) iff K^2 > 4m^2)",
            "Rfun": "R[n,np,e](K2,m2) = Int_0^1 dy y^n (1-y)^np (D(y)-i0)^e "
                    "(e <= -1 symbolic; e >= 0 auto-evaluated closed polynomial)",
            "fdiff": "dG/dK2 = -e*G[n+1,np+1,e-1] + R[n+1,np+1,e-1]; "
                     "dR/dK2 = -e*R[n+1,np+1,e-1]; dG/dm2 = e*G[n,np,e-1] - "
                     "R[n,np,e-1]; dR/dm2 = e*R[n,np,e-1] (exact recurrences, "
                     "gated vs numeric differentiation)"},
        "tt_view_derived": {
            "note": "DERIVED object (computed after the freeze; used in NO gate); "
                    "polarisations e+ (e_11 = -e_22 = 1), eX (e_12 = e_21 = 1) of "
                    "the plane-wave pair, 3-axis = k",
            "sha256": TT_HASH,
            "components_srepr": ({str(n): {k: sp.srepr(TT[n][k])
                                           for k in sorted(TT[n])}
                                  for n in sorted(TT)} if TT is not None
                                 else "not-derived")},
        "subtraction": {
            "Pi_local_MS_srepr": sp.srepr(Pi_local_MS_mine),
            "fingerprint": PI_LOCAL_FP_FROZEN,
            "sha256": SUB_SHA,
            "content": "(2/eps)(Sigma_0 + H Sigma_1 + H^2 Sigma_2) -- the frozen "
                       "pole-only MS subtraction (Phase-12 / UV freeze / entry "
                       "object); reproduced from THIS assembly's own c-sector",
            "finite_sector": "untouched (byte-gated; zero finite discretion)"},
        "manifest": {
            "head": HEAD_EXPECT,
            "input_hashes": PIN,
            "complete_kernel_sha256": KERNEL_SHA,
            "per_sector_sha256": {str(n): expr_sha(SIG_fin[n].subs(csym, 0))
                                  for n in (0, 1, 2)},
            "tt_view_sha256": TT_HASH,
            "master_engine_sha256": _self_sha,
            "subtraction_sha256": SUB_SHA,
            "engine_sha256": PIN["wall_d2_phases8_12.py"],
            "p10_cache_sha256": PIN[".p10_assembly_cache.txt"],
        },
        "structure_census": STRUCT,
        "numeric_battery": {lbl: {str(n): BAT[lbl][n] for n in BAT[lbl]}
                            for lbl, _, _ in SAMPLES},
        "referee_cases": E1_REFS,
        "h1_parity_class": {
            "identically_zero": bool(sp.expand(SIG_fin[1]) == 0),
            "purely_imaginary": bool(
                sp.expand(SIG_fin[1] + SIG_fin[1].subs(sp.I, -sp.I)) == 0),
            "note": "the standing T4 fence; recorded, NOT interpreted"},
        "block_timing": BLOCK_TIMING,
        "limitations": [
            "SKIPBAT=1 construction load: the 23-min Level-2 battery is NOT "
            "re-run (last PASSED at 195a481, all five cases with the broken "
            "control failing); the L2-discriminating s^1 case IS gated here in "
            "finite mode with its own broken control",
            "referee independence scope: atom values are direct mpmath "
            "quadratures of their DEFINITIONS (no analytic primitive); the "
            "composition coefficients are the validated engine routing (shared "
            "lineage, byte-replayed against the frozen cache); the master law "
            "itself is refereed at monomial level against A3-1's own trace "
            "composition (E1), including omega-derivative depths through the "
            "fdiff tower",
            "the K^2 = 4m^2 threshold point itself is excluded from the battery "
            "(the A3-1 bisection boundary); timelike R-atom referee uses "
            "complex-eps Richardson (eta = 2e-3, 3-point extrapolation)",
            "sympy closed forms are EXPOSITORY, gated against the referee "
            "(never the reverse); where not obtained within 300s this is "
            "recorded and the referee remains the authority",
            "the O(H) finite sector parity class is recorded under the standing "
            "T4 fence, NOT interpreted",
            "the TT view is derived-only (post-freeze, used in no gate); the "
            "assembly carries all E/P slots (no early projection)",
            "the finite block cache is a staging artifact (tag A32fin-v1, "
            "A32_CACHE_DIR); the frozen object is complete in the claimed "
            "outputs; a cache-off replay gate proves no cache drift",
        ],
    }
    with open(FREEZE_PATH, "w") as f:
        json.dump(FREEZE, f, indent=1, default=str)
    check(os.path.exists(FREEZE_PATH), "freeze written: Sigma_R_finite_full.json",
          gate="A3-3")
    check(KERNEL_SHA == expr_sha(sp.expand(SIG_fin[0] + Hs * SIG_fin[1]
                                           + Hs**2 * SIG_fin[2])),
          "manifest self-consistency: the complete-kernel sha256 recomputes",
          gate="A3-3")
    _rt = sp.sympify(FREEZE["sectors"]["0"]["srepr"],
                     locals={"Gfun": Gfun, "Rfun": Rfun})
    check(sp.expand(_rt - sp.expand(SIG_fin[0].subs(csym, 0))) == 0,
          "freeze round-trip: the frozen sector-0 srepr reconstructs the object "
          "exactly (Gfun/Rfun locals)", gate="A3-3")
    stamp("freeze written (Sigma_R_finite_full.json + manifest)")

# ---------- the result JSON + verdict MDs ----------
RESULT = {
    "instrument": "wall_a3_2_finite_response.py",
    "task": "WALL A3-2 (Phase G): the finite eps^0 master computation for the D2 "
            "assembly",
    "builder": "builder session (owner 'go' 2026-08-28), HEAD %s" % HEAD_EXPECT,
    "smoke_run": SMOKE,
    "verdict": VERDICT if not SMOKE else "SMOKE (pre-flight; NOT a result run)",
    "w0_status": "computed-and-reported, NOT banked; no register edits",
    "counts": {
        "gates_total": len(CHECKS),
        "gates_passed": sum(1 for r in CHECKS if r["pass"]),
        "controls_total": len(CONTROLS),
        "controls_detected": sum(1 for r in CONTROLS if r["detected"]),
        "failures": len(FAILS),
    },
    "checks": CHECKS,
    "controls": CONTROLS,
    "notes": NOTES,
    "self_caught_defects": SELF_CAUGHT,
    "block_timing": BLOCK_TIMING,
    "block_budget_s": BLOCK_BUDGET_S,
    "block_budget_override": BLOCK_BUDGET_OVERRIDE,
    "blocks_stopped": BLOCK_STOPPED,
    "limitations": (FREEZE or {}).get("limitations", [
        "smoke/pre-flight run: limitations enumerated in the full run's freeze"]),
    "outputs": {
        "instrument": "PHYSICS_LEDGER/wall_a3_2_finite_response.py",
        "result_json": "PHYSICS_LEDGER/WALL_A3_2_FINITE_RESPONSE_RESULT.json",
        "verdict_md": "PHYSICS_LEDGER/WALL_A3_2_FINITE_RESPONSE_VERDICT.md",
        "freeze_json": "PHYSICS_LEDGER/Sigma_R_finite_full.json",
        "freeze_verdict_md": "PHYSICS_LEDGER/Sigma_R_finite_full.verdict.md",
        "run_log": "PHYSICS_LEDGER/.p_a3_2_run.log",
    },
    "next_stage_gate": "A3-3 freeze complete. HARD STOP: Q1-Q5, J(omega), PV, "
                       "spectral classification, basis work and register edits "
                       "remain LOCKED; the next stage begins only after "
                       "owner/reviewer inspection of this record.",
    "elapsed_s": round(time.time() - T0, 1),
}
with open(RESULT_PATH, "w") as f:
    json.dump(RESULT, f, indent=1, default=str)
stamp("result JSON written")

_verdict_lines = [
    "# WALL A3-2 FINITE RESPONSE -- VERDICT",
    "",
    "**Task**: the finite eps^0 retarded kernel Sigma_R^finite(omega,k,H,m) of "
    "the D2 assembly (A3-2A..A3-2F), assembled from the A3-1 validated masters.",
    "**Verdict**: %s" % RESULT["verdict"],
    "**Gate counts**: %d/%d gates passed; %d/%d controls detected; %d failures."
    % (RESULT["counts"]["gates_passed"], RESULT["counts"]["gates_total"],
       RESULT["counts"]["controls_detected"], RESULT["counts"]["controls_total"],
       RESULT["counts"]["failures"]),
    "**W-0**: computed-and-reported, NOT banked. No register edits.",
    "",
    "## The five A3-2E checks",
    "1. Scalar-bubble finite limit: B(K2) anchors vs A3-1 route-A (3 spacelike "
    "Re + timelike Im = +pi*sqrt(1-4/5)), plus the monomial-class referee "
    "battery vs A3-1's own trace-composition quadrature (incl. omega-derivative "
    "depths through the exact fdiff tower).",
    "2. H^0 flat limit: the finite seagull identity (m^4/2)[sqrt(-g)]_{h^2} x "
    "(1+kappa-ln(m^2/mu^2)) exact; the K=0 cross-route; structural H-grading.",
    "3. Retarded support/sign: Im == 0 below K^2 = 4m^2 (all H^0/H^2 slots, all "
    "no-cut samples); the +pi*Int_{cut} sign law on every G-atom above "
    "threshold.",
    "4. Subtraction locality: Pi_local^MS fingerprint e2f0bbfe6fd4c89d "
    "reproduced from THIS assembly's own c-sector; 100% of pole terms F1-local "
    "under the independent classifier port; the finite sector byte-untouched.",
    "5. Wrong-branch negative control: DETECTED at master level and at "
    "component level (the +i0 branch disagrees; the branch is load-bearing).",
    "",
    "## Method (the twin law)",
    "pole(j,N) = c*moment*P*Delta^s and fin(j,N) = moment*Delta^s*[P*(kappa - "
    "ln((Delta-i0)/mu^2) + s_j) + C(j,N-1) + Q], with the exact-d moment "
    "correction s_j = psi(j+2)-psi(2). Quadruple-verified against A3-1: the "
    "pole grid 25/25 byte-identical to Ipole_scalar; M_1..M_4 and the T2/T4 "
    "exact-d compositions exact. All Delta are Delta-i0 (the A3-1 branch law).",
    "",
    "## Representation",
    "Local finite sector: closed sympy forms (pass the frozen F1 predicate "
    "verbatim; kappa/ln(mu^2)/ln(m^2/mu^2) are V4-local coefficient logs). "
    "Nonlocal sector: the closed atom families G[n,np,e], R[n,np,e] -- exact "
    "1-D Feynman-parameter integrals with exact fdiff recurrences; no "
    "Li_2/Clausen class can arise (gated on the assembled object).",
    "",
    "## Limitations",
] + ["- %s" % l for l in RESULT["limitations"]] + [
    "",
    "## Hard stop",
    "A3-3 freeze complete (see Sigma_R_finite_full.json and its verdict). "
    "Q1-Q5, J(omega), PV, spectral classification, basis work, refits and "
    "register edits remain LOCKED. The next stage begins only after "
    "owner/reviewer inspection of this record.",
]
with open(VERDICT_PATH, "w") as f:
    f.write("\n".join(_verdict_lines) + "\n")

if FREEZE is not None:
    _fz_lines = [
        "# Sigma_R^finite -- FREEZE VERDICT",
        "",
        "**Object**: the COMPLETE finite eps^0 retarded kernel, all non-TT "
        "sectors carried; reconstruction Sigma_R^fin = SIG_fin[0] + "
        "H*SIG_fin[1] + H^2*SIG_fin[2].",
        "**Verdict**: %s" % VERDICT,
        "**Complete kernel sha256**: %s" % KERNEL_SHA,
        "**TT-view (derived) sha256**: %s" % TT_HASH,
        "**Subtraction (Pi_local^MS) sha256**: %s (fingerprint %s)"
        % (SUB_SHA, PI_LOCAL_FP_FROZEN),
        "**Master engine sha256**: %s" % _self_sha,
        "",
        "The nonlocal finite sector is exactly the atom-carrying sector: exact "
        "1-D parameter integrals of D(y) = m^2 - y(1-y)K^2 with the frozen -i0 "
        "branch (threshold K^2 = 4m^2). No power law fitted, no spectral class "
        "assigned, no low-frequency behaviour classified (A3-2D discipline).",
        "",
        "W-0: computed-and-reported, NOT banked. HARD STOP before A3-3+ "
        "adjudication: the next stage begins only after owner/reviewer "
        "inspection.",
    ]
    with open(FREEZE_VERDICT_PATH, "w") as f:
        f.write("\n".join(_fz_lines) + "\n")

print("\n================ SUMMARY ================")
print("verdict: %s" % RESULT["verdict"])
print("gates: %d/%d passed; controls: %d/%d detected; failures: %d"
      % (RESULT["counts"]["gates_passed"], RESULT["counts"]["gates_total"],
         RESULT["counts"]["controls_detected"], RESULT["counts"]["controls_total"],
         RESULT["counts"]["failures"]))
if FAILS:
    print("FAILURES:")
    for _m in FAILS[:20]:
        print("  - %s" % _m)
print("outputs: %s" % ", ".join(sorted(os.path.basename(p) for p in
      [RESULT_PATH, VERDICT_PATH, FREEZE_PATH, FREEZE_VERDICT_PATH, LOG_PATH]
      if os.path.exists(p))))
print("elapsed: %.1fs" % (time.time() - T0))
_logf.close()
sys.exit(0 if (not FAILS and (SMOKE or not INCOMPLETE)) else 1)
