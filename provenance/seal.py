#!/usr/bin/env python3
"""seal: the precondition for any irreversible act.

WHY THIS EXISTS. On 2026-08-18 two pre-registrations were sealed and manifested, and the suite was
run afterwards. The guard governing blind-safe seals fired immediately -- on a file that could no
longer be edited, because sealing it was the point. The artifact was repaired by supersession; the
ORDERING DEFECT was not, and an ordering defect in a class where the act is irreversible will
simply recur.

Seal-then-verify is the shape. This makes verify-then-seal structural: the guard suite is a
PRECONDITION of sealing, not a thing done near it.

    python3 seal.py <file.txt>      seal one prereg into MANIFEST.txt, ONLY if the checks pass

It refuses when a NEW red exists (see expected_red.py -- declared adjudications do not block, an
undeclared failure does), when the file is already manifested, or when a blind-safe file fails the
blind-safe guard. The last is the whole point: the check that would have caught the 2026-08-18
error runs BEFORE the hash, where it can still change the outcome.

THE SAME RULE APPLIES TO EVERY IRREVERSIBLE ACT and this tool covers only one of them. Tagging,
releasing, and depositing are equally irreversible and equally outside a working tree's undo --
run the checks first there too. HOW_TO_VERIFY.md carries the rule; this file carries the one case
that can be mechanized here.
"""
import hashlib
import os
import subprocess
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
PREREG = os.path.join(HERE, "prereg")
MANIFEST = os.path.join(PREREG, "MANIFEST.txt")


def main():
    if len(sys.argv) != 2:
        print(__doc__.strip().splitlines()[0])
        print("usage: python3 seal.py <prereg filename>")
        return 2
    name = os.path.basename(sys.argv[1])
    path = os.path.join(PREREG, name)
    if not os.path.exists(path):
        print(f"REFUSED: {name} is not in prereg/")
        return 1
    if name in open(MANIFEST).read():
        print(f"REFUSED: {name} is already manifested. A seal is never re-applied.")
        return 1

    print("precondition 1/2 -- the guard suite, with declared adjudications allowed ...")
    r = subprocess.run([sys.executable, os.path.join(HERE, "expected_red.py")],
                       capture_output=True, text=True)
    if r.returncode != 0:
        print(r.stdout)
        print("REFUSED: an undeclared failure is open. Seal nothing while the suite is telling "
              "you something new.")
        return 1

    print("precondition 2/2 -- the blind-safe guard against THIS file ...")
    sys.path.insert(0, HERE)
    import test_prereg_immutable as G
    body = open(path).read()
    if "BLIND-SAFE: yes" in body:
        for pat, what in G.TestBlindSafe.LEAK_PATTERNS:
            m = pat.search(body)
            if m is not None:
                print(f"REFUSED: {name} declares BLIND-SAFE and contains {what} ({m.group(0)!r}). "
                      f"This is the check that fired too late on 2026-08-18.")
                return 1

    h = hashlib.sha256(open(path, "rb").read()).hexdigest()
    with open(MANIFEST, "a") as f:
        f.write(f"{h}  {name}\n")
    print(f"SEALED {name}\n  sha256 = {h}\nImmutable from now. Results cite it; they never join it.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
