#!/usr/bin/env python3
"""doc_register_pins: the book is pinned to the register, so prose cannot go stale silently.

THE GAP THIS CLOSES. Three things in the public document derive from the register and are already
guarded: the counts (emitted, and a test fails if any is typed), the generated tables, and the
figures (regenerated, drift-checked). The fourth thing is PROSE -- and prose is where the document
says a node's tier, its conditionality, its disposition, what it rests on. If a claim graduates,
demotes, retires, or changes price, every sentence describing it goes stale and NOTHING FAILS.

That is the program's oldest defect shape (a figure accurate when written, stale one commit later)
pointed at the one artifact a reader actually reads. So the fields the prose depends on are
PINNED: for every register node the document names, a hash of its tier, ledger_delta, sub_status
and grut_standing. Move any of them and this check fails with the node named -- the prompt to go
read the sentences that cite it.

IT IS A PROMPT, NOT A LOCK. Like the bank gate, refreshing the pin is a human act (--accept), and
refreshing it is a claim: "I have re-read the prose that cites this node and it still says what
the register says." The pin file records WHEN that was last claimed.

Standing artifacts the document vouches for (POSTULATE_MAP, NO_GO_LEDGER, S_IF, GLOSSARY,
HOW_TO_VERIFY) are pinned the same way, by content hash -- the Wave-7 screen found an over-graded
no-go alive in one of them, under a figure caption that vouched for it.

Run:  python3 doc_register_pins.py           report drift (exit 1 if any)
      python3 doc_register_pins.py --accept   re-pin after reconciling the prose
"""
import hashlib
import json
import os
import re
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
SRC = os.path.join(ROOT, "docs", "WHERE_IT_STOPS.src.md")
PINS = os.path.join(HERE, "doc_register_pins.json")
FIELDS = ("tier", "ledger_delta", "sub_status", "grut_standing")
ARTIFACTS = ["POSTULATE_MAP.md", "NO_GO_LEDGER.md", "S_IF.md", "GLOSSARY.md", "HOW_TO_VERIFY.md"]


def node_fingerprint(node):
    return hashlib.sha256(json.dumps({f: node.get(f) for f in FIELDS},
                                     sort_keys=True).encode()).hexdigest()[:16]


def current():
    with open(os.path.join(HERE, "claims.json")) as f:
        claims = {c["id"]: c for c in json.load(f)["claims"]}
    src = open(SRC).read()
    cited = sorted(i for i in claims if re.search(rf"\b{re.escape(i)}\b", src))
    nodes = {i: node_fingerprint(claims[i]) for i in cited}
    arts = {}
    for a in ARTIFACTS:
        p = os.path.join(ROOT, a)
        if os.path.exists(p):
            arts[a] = hashlib.sha256(open(p, "rb").read()).hexdigest()[:16]
    return {"nodes": nodes, "artifacts": arts}


def main():
    cur = current()
    if "--accept" in sys.argv:
        cur["_accepted_note"] = ("Refreshed by a human act. Refreshing this file is the claim "
                                 "that the document's prose about each node below has been "
                                 "re-read and still matches the register.")
        with open(PINS, "w") as f:
            json.dump(cur, f, indent=2, sort_keys=True)
        print(f"pinned {len(cur['nodes'])} cited nodes and {len(cur['artifacts'])} artifacts.")
        return 0
    if not os.path.exists(PINS):
        print("no pin file; run --accept once to establish it.")
        return 1
    old = json.load(open(PINS))
    moved = [i for i, h in cur["nodes"].items() if old["nodes"].get(i) not in (None, h)]
    added = [i for i in cur["nodes"] if i not in old["nodes"]]
    dropped = [i for i in old["nodes"] if i not in cur["nodes"]]
    arts = [a for a, h in cur["artifacts"].items() if old["artifacts"].get(a) not in (None, h)]
    if not (moved or arts or added or dropped):
        print(f"document is current with the register "
              f"({len(cur['nodes'])} cited nodes, {len(cur['artifacts'])} artifacts).")
        return 0
    print("THE BOOK MAY BE STALE. Read the prose citing each item, then re-pin with --accept.\n")
    for i in moved:
        print(f"  MOVED     {i}  (tier / ledger / sub_status / standing changed)")
        for m in re.finditer(rf"^.*\b{re.escape(i)}\b.*$", open(SRC).read(), re.M):
            print(f"            cited: {m.group(0).strip()[:110]}")
    for a in arts:
        print(f"  ARTIFACT  {a} changed — the document vouches for it")
    for i in added:
        print(f"  NEW       {i} is now cited by the document but was never pinned")
    for i in dropped:
        print(f"  DROPPED   {i} is pinned but no longer cited")
    return 1


if __name__ == "__main__":
    raise SystemExit(main())
