#!/usr/bin/env python3
"""coverage: the coverage-map generator -- the register as a MAP of known physics, GRUT's fills marked.

The register is no longer a fill-only ledger. Every node carries a `domain` and a `grut_standing`:
  covered     -- GRUT makes a definite claim here (a fill: a result, a no-go, or a posited input).
  borrowed    -- GRUT imports this as an input (ZERO GRUT-derivation credit; see the A3 nodes).
  open field  -- GRUT poses it as an explicit open question / marks it undetermined (marked-open).
  silent      -- a piece of known physics represented on the map that GRUT makes NO claim about.

coverage_map() buckets the nodes (covered / borrowed / marked-open / silent) and, alongside, reports
the ABSENT bucket: a curated list of known-physics areas GRUT has NO node for -- so the map names its
own gaps rather than hiding them. Growing the map must never let a borrowed / silent node read as a
GRUT fill: the standing is EXPLICIT and machine-checkable (see test_coverage).

Pure (coverage_map reads nothing); I/O in main().
"""
import collections
import json
import os

HERE = os.path.dirname(os.path.abspath(__file__))

# 'silent' is a reserved bucket (currently unpopulated): a map-only known-physics node GRUT makes NO
# claim about. Its empty count is a reserved slot, not missing enforcement.
VALID_STANDINGS = ("covered", "borrowed", "open field", "silent")
# grut_standing -> coverage-map bucket label
BUCKET = {"covered": "covered", "borrowed": "borrowed", "open field": "marked-open", "silent": "silent"}

# ABSENT: known-physics areas GRUT has NO node for. Named explicitly so the map is honest about its
# gaps (absent != covered). A topic graduates OUT of here when it gets a node.
KNOWN_GAPS = [
    ("quantum-gravity", "UV completion / non-perturbative definition of the graviton sector"),
    ("black-hole-interior", "singularity / interior structure"),
    ("early-universe", "inflation model + primordial spectrum"),
    ("baryogenesis", "matter-antimatter asymmetry"),
    ("dark-matter", "particle content / non-gravitational sector"),
]


def coverage_map(claims):
    """Return the structured coverage map. PURE."""
    by_standing = collections.defaultdict(list)
    by_domain = collections.defaultdict(lambda: collections.defaultdict(list))
    unknown = []
    for c in claims:
        st = c.get("grut_standing")
        dom = c.get("domain", "<undomained>")
        if st not in VALID_STANDINGS:
            unknown.append((c.get("id"), st))
            continue
        by_standing[st].append(c["id"])
        by_domain[dom][st].append(c["id"])
    return {
        "by_standing": {k: sorted(v) for k, v in by_standing.items()},
        "by_domain": {d: {s: sorted(ids) for s, ids in sm.items()} for d, sm in by_domain.items()},
        "totals": {BUCKET[s]: len(by_standing.get(s, [])) for s in VALID_STANDINGS},
        "absent": [f"{d}: {t}" for d, t in KNOWN_GAPS],
        "unknown_standing": unknown,  # nodes with a bad/missing grut_standing -- a schema error
        "n_nodes": len(claims),
        "n_domains": len(by_domain),
    }


def _load():
    with open(os.path.join(HERE, "claims.json")) as f:
        return json.load(f)["claims"]


def main():
    m = coverage_map(_load())
    print("=" * 78)
    print("GRUT COVERAGE MAP -- known physics, GRUT's fills marked")
    print("=" * 78)
    t = m["totals"]
    print(f"\n{m['n_nodes']} nodes across {m['n_domains']} domains:")
    print(f"  covered (GRUT fill)          : {t['covered']}")
    print(f"  borrowed (imported, 0 credit): {t['borrowed']}")
    print(f"  marked-open (open field)     : {t['marked-open']}")
    print(f"  silent (no GRUT claim)       : {t['silent']}")
    print(f"  absent (no node; named gaps) : {len(m['absent'])}")
    if m["unknown_standing"]:
        print(f"  !! nodes with bad grut_standing: {m['unknown_standing']}")

    print("\nby domain (standing -> count):")
    for dom in sorted(m["by_domain"]):
        sm = m["by_domain"][dom]
        cells = ", ".join(f"{BUCKET[s]} {len(sm[s])}" for s in VALID_STANDINGS if s in sm)
        print(f"  {dom:34} {cells}")

    print("\nABSENT (known physics with NO node -- named gaps, not hidden):")
    for a in m["absent"]:
        print(f"  - {a}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
