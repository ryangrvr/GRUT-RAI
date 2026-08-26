#!/usr/bin/env python3
"""D2-R1 FINAL PUSH -- Phases 0-12 in ONE instrument (fresh paths; 14-step binding spec).

STANDING STATE: 0bcc379 lineage (final handoff). R1 frozen. W-0 binding. Register untouched.
FILE CLAIM: AGENT_COORDINATION.md, Ox, 2026-08-26 (fresh paths; nothing resumed).
BARRED BY PINNED DIRECTIVE: wall_d2_r1.py (OBSOLETE) and wall_d2_phase2.py (UNVERIFIED).
  This file imports NOTHING from either; the Phase-0 guard scans both names LIVE and
  fails the run on any hit (modules, tracked reads, own-source identifiers).
ORDER (binding): 0 claim/guard -> 1 covariance -> 2 Riccati W2 + order chain ->
  EPSILON^2-CANCELLATION GATE EARLY -> 3 measured residual (two regimes) ->
  4 normalization/typed objects -> 5 matched physical H->0 -> 6 corrected-object
  parity -> 7 per-mode validity -> 8 mechanically-wired dressing plant (prohibited
  hybrids FAIL) -> 9 matched-order vertex -> 10 fish+seagull (bubble 1/2 emergent,
  signed retarded rule) -> 11 multi-K^2 identification modulo the known null relation
  -> 12 MS split Pi_local^MS + Pi_nonlocal^invariant. HARD STOP after 12: no
  Q1-Q5/J(omega)/PV/dual-gauge. Withdrawn odd-H prediction barred from interpretation.
No numbers from memory; no hand-entered PASS.

Run: python3 PHYSICS_LEDGER/wall_d2_final_push.py   # exit 0 iff all gates pass
"""
import ast
import hashlib
import json
import os
import sys
import time as _time

import sympy as sp

HERE = os.path.dirname(os.path.abspath(__file__))
READS = []
FAIL = []
_T0 = _time.time()


def stamp(msg):
    print(f"[{_time.time()-_T0:7.1f}s] {msg}"); sys.stdout.flush()


def tracked_read(path):
    READS.append(path)
    with open(path) as f:
        return f.read()


def check(cond, msg):
    ok = bool(cond)
    print(("  ok   " if ok else "  FAIL ") + msg); sys.stdout.flush()
    if not ok:
        FAIL.append(msg)
    return ok


# =====================================================================================
# PHASE 0a -- BARRED-INPUTS GUARD, LIVE (registry law + D2 housekeeping bars)
# =====================================================================================
print("=== PHASE 0a: BARRED-INPUTS GUARD (LOAD/ECHO/SCAN/FAIL) ===")
registry = json.loads(tracked_read(os.path.join(HERE, "WALL_A_A3_REGISTRY.json")))
print("   registry status:", registry["status"])
check(registry["status"].startswith("FROZEN"), "guard registry is the FROZEN declaration")
barred_names, barred_sha = set(), {}
for entry in registry["g0_spectral_wiring"]["barred_inputs"]:
    barred_names.update(entry.get("objects", []))
    for f in entry.get("files", []):
        bh = entry.get("sha256", {}).get(f)
        if f != "WALL_A_A3_REGISTRY.json":
            barred_sha[f] = bh
# D2-specific bars pinned by owner (housekeeping + review directives):
D2_BARRED_FILES = {"wall_d2_r1.py", "wall_d2_phase2.py", "WALL_D2_PHASE2_RESULT.json"}
mod_hits = sorted({m.rsplit(".", 1)[-1] for m in list(sys.modules)} & D2_BARRED_FILES)
read_hits = []
for p in READS:
    base = os.path.basename(p)
    if base in D2_BARRED_FILES or base in barred_sha:
        read_hits.append(base + " (by name)")
    h = hashlib.sha256(open(p, "rb").read()).hexdigest()
    for bf, bh in barred_sha.items():
        if bh and h == bh:
            read_hits.append(f"{p} (hash match to barred {bf})")
own_src = tracked_read(os.path.abspath(__file__))
_ids = set()
for _node in ast.walk(ast.parse(own_src)):
    for _at in ("id", "attr", "name", "arg"):
        _v = getattr(_node, _at, None)
        if isinstance(_v, str):
            _ids.add(_v)
sym_hits = [b for b in ("wall_d2_r1", "wall_d2_phase2") if b in _ids]
hits = mod_hits + read_hits + sym_hits
print(f"   scan: {len(list(sys.modules))} modules, {len(READS)} tracked reads, "
      f"{len(barred_names)} registry symbols, "
      f"{len(barred_sha) + len(D2_BARRED_FILES)} barred files")
if hits:
    print(f"   GUARD TRIPPED: {hits} -- RUN VOID."); sys.exit(2)
print("   GUARD CLEAN.")
check(len(barred_names) >= 5 and len(D2_BARRED_FILES) == 3,
      "guard armed and clean (registry bars + D2 obsolete/unverified bars)")

# =====================================================================================
# PHASE 0b -- STATE CHECK (declared lineage; no git dependency)
# =====================================================================================
print("\n=== PHASE 0b: STATE CHECK ===")
print("   standing commit lineage (declared): 0bcc379 final handoff")
print("   barred instruments present-but-unread:",
      sorted(D2_BARRED_FILES & set(os.listdir(HERE))))
check(all(not os.path.basename(p).startswith(("wall_d2_r1", "wall_d2_phase2"))
          for p in READS), "no barred artifact entered the read set")

# =====================================================================================
# PHASE 1 -- D2-0 VARIABLE/EQUATION COVARIANCE (re-derived, substitution-gated)
# =====================================================================================
print("\n=== PHASE 1: D2-0 VARIABLE/EQUATION COVARIANCE ===")
H, t, t0, kp, mp = sp.symbols('H t t0 k m', positive=True)
aa = sp.exp(H * (t - t0))                       # a(t)/a0 about the reference event
ph = sp.Function('phi')(t)
ddt = lambda f: sp.diff(f, t)
cosmic_eq = sp.expand(sp.simplify(
    aa**2 * (ddt(ddt(ph)) + 3 * H * ddt(ph) + (kp**2 / aa**2 + mp**2) * ph)))
test_phi = (1 + t) * sp.exp(-2 * t)             # arbitrary nonzero test function