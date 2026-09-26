"""Shared governance battery for the RAI chamber scripts.

Extracted from the copy-pasted blocks in rai_final_boss.py /
rai_dialectic_chamber.py (sections A and D scaffolding) so the governance logic
exists in exactly ONE place. Every chamber script imports read(), gate() and
check_governance() from here.

Pure stdlib.
"""
import hashlib
import json
import os
import re
import subprocess

ROOT = os.path.dirname(os.path.abspath(__file__))

# Default register and fences, overridable per script.
CLAIMS_PATH = "provenance/claims.json"
REGISTER_SHA_PREFIX = "beaeb84e8a6f8468"
REGISTER_NODE_COUNT = 74
DEFAULT_FENCES = ("u3_split_origin", "u4_constitutive_origin")

FAILS = []
N = 0


def read(p):
    with open(os.path.join(ROOT, p), encoding="utf-8") as f:
        return f.read()


def gate(cond, label, kind="JOURNAL"):
    global N
    N += 1
    ok = bool(cond)
    print(f"  [{'PASS' if ok else 'FAIL'}] {kind:9s} {label}")
    if not ok:
        FAILS.append(label)
    return ok


def battery_summary():
    return N - len(FAILS), N, list(FAILS)


def load_register(claims_path=CLAIMS_PATH):
    reg = json.loads(read(claims_path))
    claims = reg["claims"] if isinstance(reg, dict) else reg
    return claims, {c["id"]: c for c in claims}


def check_governance(claims=None, register_count=REGISTER_NODE_COUNT,
                     sha_prefix=REGISTER_SHA_PREFIX, fences=DEFAULT_FENCES,
                     claims_path=CLAIMS_PATH):
    """Run the shared section-A governance gates and return (claims, BY)."""
    print("\n== A. GOVERNANCE ==")
    if claims is None:
        claims, BY = load_register(claims_path)
    else:
        BY = {c["id"]: c for c in claims}
    gate(len(claims) == register_count, f"register {register_count} nodes", "GRAPH")
    gate(hashlib.sha256(read(claims_path).encode()).hexdigest().startswith(sha_prefix),
         "register sha256 unchanged", "GRAPH")
    h = subprocess.run(["git", "-C", ROOT, "rev-parse", "HEAD"],
                       capture_output=True, text=True).stdout.strip()
    v = subprocess.run(["git", "-C", ROOT, "rev-parse", "origin/v4"],
                       capture_output=True, text=True).stdout.strip()
    gate(h == v, "HEAD == origin/v4 by ref identity", "GRAPH")
    porc = subprocess.run(["git", "-C", ROOT, "status", "--porcelain"],
                          capture_output=True, text=True).stdout
    gate(not any(l[:2] in (" M", "M ", "MM", "D ") for l in porc.splitlines()),
         "no prior result modified", "GRAPH")
    for nid in fences:
        gate(BY[nid].get("tier") == "to-derive", f"{nid} fence unmoved", "GRAPH")
    return claims, BY


def render_record(rec_path):
    """Return the whitespace-collapsed record text, or None if not yet written."""
    if not os.path.exists(os.path.join(ROOT, rec_path)):
        return None
    return re.sub(r"\s+", " ", read(rec_path).replace(">", " ").replace("*", ""))
