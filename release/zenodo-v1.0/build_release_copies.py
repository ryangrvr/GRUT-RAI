#!/usr/bin/env python3
"""Generate the release/zenodo-v1.0/03_RAI/ scripts from the TOP-LEVEL originals.

The five RAI chamber scripts previously existed twice (repo root and this release
directory) as hand-maintained byte copies, which silently drifted. They must never
be edited here: edit the top-level file and re-run this script. It fails if a
release copy would change relative to what is committed, unless --force is given.
"""
import argparse
import hashlib
import os
import shutil
import sys

HERE = os.path.dirname(os.path.abspath(__file__))          # .../release/zenodo-v1.0
ROOT = os.path.abspath(os.path.join(HERE, os.pardir, os.pardir))  # repo root
SRC_DIR = ROOT
DST_DIR = os.path.join(HERE, "03_RAI")

RAI_SCRIPTS = [
    "rai_final_boss.py",
    "rai_structural_theory_search.py",
    "rai_grut_resurrection.py",
    "rai_gorilla_t1.py",
    "rai_dialectic_chamber.py",
]


def sha(p):
    with open(p, "rb") as f:
        return hashlib.sha256(f.read()).hexdigest()


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--force", action="store_true",
                    help="overwrite release copies even if they differ from committed ones")
    args = ap.parse_args()

    missing = [f for f in RAI_SCRIPTS if not os.path.exists(os.path.join(SRC_DIR, f))]
    if missing:
        print("missing top-level sources:", ", ".join(missing))
        return 1
    os.makedirs(DST_DIR, exist_ok=True)

    changed = []
    for name in RAI_SCRIPTS:
        src = os.path.join(SRC_DIR, name)
        dst = os.path.join(DST_DIR, name)
        if os.path.exists(dst) and sha(src) != sha(dst) and not args.force:
            print(f"REFUSED: {name} differs from its release copy; "
                  f"inspect the diff and re-run with --force")
            changed.append(name)
            continue
        shutil.copyfile(src, dst)
        print(f"copied {name} -> {os.path.relpath(dst, ROOT)}")

    return 1 if changed and not args.force else 0


if __name__ == "__main__":
    sys.exit(main())
