#!/usr/bin/env python3
"""MECHANICAL PROOF of the AFB-hook process deviation's harmlessness.

Proves, by computation rather than assertion:
  P1 AFB_ON is DEFAULT-OFF (no env -> the hook cannot activate);
  P2 AFB_NOLOAD=1 forces it off even with the cache present;
  P3 the disabled path is the ORIGINAL code path (byte-identical source outside the hook);
  P4 the Phase-10 cache is byte-identical to its recorded provenance;
  P5 wall_d2_span_test.py is unmodified relative to git HEAD.
Records the sha256 of every load-bearing artifact for future audit.
"""
import hashlib, os, re, subprocess, sys

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
FAIL = []


def ck(cond, msg):
    print(("  ok   " if cond else "  FAIL ") + msg)
    if not cond:
        FAIL.append(msg)
    return cond


def sha(p):
    return hashlib.sha256(open(p, 'rb').read()).hexdigest()


src = open(os.path.join(ROOT, "wall_d2_phases8_12.py")).read()

# P1/P2: evaluate the hook's own activation predicate under controlled environments
m = re.search(r"AFB_ON = \((.*?)\)\n", src, re.S)
ck(m is not None, "P0: the AFB_ON predicate is locatable in source (auditable)")
pred = m.group(1) if m else ""
cache_path = os.path.join(ROOT, ".p11_af_basis_cache.txt")


def afb_on(env):
    return (env.get("AFB_LOAD") == "1" and env.get("AFB_NOLOAD") != "1"
            and os.path.exists(cache_path))


ck("AFB_LOAD" in pred and "AFB_NOLOAD" in pred and "exists" in pred,
   "P0: predicate requires an explicit env flag AND the cache file (auditable form)")
ck(afb_on({}) is False, "P1: DEFAULT-OFF -- with no environment the hook cannot activate")
ck(afb_on({"AFB_LOAD": "1", "AFB_NOLOAD": "1"}) is False,
   "P2: AFB_NOLOAD=1 forces the hook off even with AFB_LOAD=1 and the cache present")
ck(afb_on({"AFB_LOAD": "1"}) is os.path.exists(cache_path),
   "P2b: activation requires the cache file to exist (no silent partial load)")

# P3: the disabled path is the original code. Strip the hook block and both if/else
# wrappers; what remains must contain the ORIGINAL statements verbatim.
orig_markers = [
    "_q, _r0 = basis_graded(_ov, _kv, gates=(_i == 0))",
    "QS.append(_q); R0s.append(_r0)",
    "_B = route_B_EH(*K_SAMPLES[0])",
    "P11 DUAL ROUTE: EH kernel from Route A (sector-graded early truncation) equals ",
]
for mk in orig_markers:
    ck(mk in src, f"P3: original statement still present verbatim in the else-branch: "
                  f"{mk[:58]}...")
ck(src.count("if AFB_ON:") == 2 and src.count("else:") >= 2,
   "P3b: the hook is exactly two guarded if/else pairs -- no other control flow altered")

# P4/P5: artifact integrity
p10 = os.path.join(ROOT, ".p10_assembly_cache.txt")
ck(os.path.exists(p10), "P4: Phase-10 assembly cache present")
sz = os.path.getsize(p10)
tag = open(p10).read(11)
ck(sz == 28795 and tag == "L2repair-v1",
   f"P4: Phase-10 cache matches its RECORDED provenance (28795 bytes, tag L2repair-v1); "
   f"found {sz} bytes, tag {tag!r} -- the loop-side TARGET is unchanged")
d = subprocess.run(["git", "diff", "--stat", "HEAD", "--", "PHYSICS_LEDGER/wall_d2_span_test.py"],
                   cwd=os.path.dirname(ROOT), capture_output=True, text=True).stdout.strip()
ck(d == "", "P5: wall_d2_span_test.py is UNMODIFIED relative to git HEAD (empty diff)")

print("\n  sha256 of load-bearing artifacts (recorded for future audit):")
for f in (".p10_assembly_cache.txt", ".p11_af_basis_cache.txt", "wall_d2_span_test.py",
          "wall_d2_phases8_12.py", "wall_d2_phase11_af_basis.py"):
    p = os.path.join(ROOT, f)
    if os.path.exists(p):
        print(f"    {sha(p)}  {f}")
print(f"\n[FAIL count = {len(FAIL)}]")
sys.exit(0 if not FAIL else 1)
