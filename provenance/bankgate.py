#!/usr/bin/env python3
"""bankgate: the bank-time gate that makes the self-audit LIVE.

The resident (propose/check_change) is a pure library; until now nothing forced a real edit to
claims.json through it, so 'self-auditing' was a property of the TESTS, not of the register. This gate
closes that gap: it diffs the working claims.json against a BASELINE (git HEAD if the tree is under
version control, else the committed snapshot claims.baseline.json) and runs the resident's propose() on
every ADDED or MODIFIED claim.

  BLOCK              -> a discipline/structural violation (laundering, unresolved dep, cycle).
                        Exit 1: STOP the bank (the 'commit').
  FLAG-FOR-FIREWALL  -> a substantive change or a consistency flag (re-opens closed, builds-on-closed,
                        tier-contradiction, orphaned result, prior-lineage). Exit 0, but SURFACED for
                        the both-directions firewall + human relay BEFORE the change is accepted.
  CLEAN              -> no added/modified/deleted claim (working == baseline).

Every new scaffold node is born marked-open / borrowed with ledger_delta 0, so it surfaces as
FLAG-FOR-FIREWALL (substantive/new) -- never a silent PASS. The gate also reports the net-ledger drift
baseline->working; the net==+13 invariant is asserted separately in tests.

Workflow: edit claims.json -> `python3 bankgate.py` -> fix any BLOCK / firewall any FLAG -> once the
firewall + human accept it, refresh the baseline with `python3 bankgate.py --accept`.

bank_gate() is pure (reads nothing, writes nothing); all I/O lives in main().
"""
import json
import os
import shutil
import subprocess
import sys

from resident import propose

HERE = os.path.dirname(os.path.abspath(__file__))
BASELINE = "claims.baseline.json"
HELDFILE = "held_flags.json"

# 1a (2026-08-09): REVIEWED-AND-HELD vs NEVER-LOOKED-AT. The process is relay-and-hold, so flags
# accumulate BY DESIGN -- permanent FLAG on an unmodified repo was not staleness, it was the gate
# lacking a distinction the process needs. A flag the overseer has reviewed is recorded here with a
# fingerprint of the claim's exact content; if the claim changes further, the fingerprint mismatches
# and the flag is NEW again. The held-ledger is display-layer only: it never changes the verdict or
# the exit code, so nothing can be waved past the firewall by holding it.


def _fingerprint(obj):
    import hashlib
    return hashlib.sha256(json.dumps(obj, sort_keys=True).encode()).hexdigest()


def _load_held():
    p = os.path.join(HERE, HELDFILE)
    if os.path.exists(p):
        with open(p) as f:
            return json.load(f)
    return {}


def bank_gate(baseline_claims, working_claims, source_ids, valid_tiers=None):
    """Diff working vs baseline; run propose() on every added/modified claim. PURE.

    For each changed claim the reference register is the WORKING set (so co-added claims resolve each
    other's depends_on), with the changed claim itself presented in its BASELINE form for a modify
    (so propose sees is_new=False + the old ledger_delta + the old disposition for RE-OPENS), or
    removed for an add (so propose sees is_new=True). Returns a structured report dict.
    """
    # SCOPE-AWARE 2026-08-04: one register, several ledgers. Each claim is audited under ITS OWN
    # scope's tier vocabulary -- a physics node graded `measured` is valid in the vacuum-cluster
    # scope and correctly invalid in GRUT's. An explicit valid_tiers argument (used by the tests)
    # still overrides, so the gate's existing contract is unchanged.
    def _kwargs_for(claim):
        if valid_tiers is not None:
            return {"valid_tiers": valid_tiers}
        scope = claim.get("ledger_scope", "grut")
        if scope == "grut":
            return {}
        try:
            from physics_vocab import PHYSICS_TIERS
        except ImportError:
            return {}
        return {"valid_tiers": PHYSICS_TIERS}

    base_by_id = {c["id"]: c for c in baseline_claims}
    work_by_id = {c["id"]: c for c in working_claims}

    reports = []
    for c in working_claims:
        cid = c["id"]
        base = base_by_id.get(cid)
        if base is not None and base == c:
            continue  # unchanged
        if base is None:
            ref = [x for x in working_claims if x["id"] != cid]          # ADD: is_new=True
        else:
            ref = [base if x["id"] == cid else x for x in working_claims]  # MODIFY: compare to baseline
        rep = propose(c, ref, source_ids, **_kwargs_for(c))
        rep["_changed_fields"] = ([] if base is None
                                  else sorted(k for k in set(base) | set(c) if base.get(k) != c.get(k)))
        # 1a (2026-08-09): tier/ledger changes get their OWN severity. Graduating an open anchor is
        # categorically more serious than a boundary_condition edit, and they used to render
        # identically -- which is how an unearned graduation would hide inside alarm fatigue.
        ch = set(rep["_changed_fields"])
        rep["_severity"] = ("TIER-OR-LEDGER" if ch & {"tier", "ledger_delta", "disposition"}
                            else ("NEW-NODE" if base is None else "SUBSTANTIVE"))
        reports.append(rep)

    deletions = [cid for cid in base_by_id if cid not in work_by_id]

    blocks = [r for r in reports if r["verdict"] == "BLOCK"]
    flags = [r for r in reports if r["verdict"] == "FLAG-FOR-FIREWALL"]
    passes = [r for r in reports if r["verdict"] == "PASS"]

    net_base = sum(c.get("ledger_delta", 0) for c in baseline_claims if isinstance(c.get("ledger_delta"), int))
    net_work = sum(c.get("ledger_delta", 0) for c in working_claims if isinstance(c.get("ledger_delta"), int))

    if blocks:
        overall = "BLOCK"
    elif flags or deletions:
        overall = "FLAG-FOR-FIREWALL"
    else:
        overall = "CLEAN"

    return {"overall": overall, "blocks": blocks, "flags": flags, "passes": passes,
            "deletions": deletions, "net_baseline": net_base, "net_working": net_work,
            "n_changed": len(reports)}


# --------------------------------------------------------------------------- I/O + CLI

def _load(name):
    with open(os.path.join(HERE, name)) as f:
        return json.load(f)


def _resolve_baseline():
    """Return (baseline_claims, label). Prefer git HEAD if the tree is version-controlled; else the
    committed snapshot claims.baseline.json; else (None, None)."""
    try:
        top = subprocess.run(["git", "-C", HERE, "rev-parse", "--show-toplevel"],
                             capture_output=True, text=True)
        if top.returncode == 0:
            root = top.stdout.strip()
            rel = os.path.relpath(os.path.join(HERE, "claims.json"), root)
            show = subprocess.run(["git", "-C", HERE, "show", f"HEAD:{rel}"],
                                  capture_output=True, text=True)
            if show.returncode == 0 and show.stdout.strip():
                return json.loads(show.stdout)["claims"], f"git HEAD:{rel}"
    except (OSError, ValueError):
        pass
    if os.path.exists(os.path.join(HERE, BASELINE)):
        return _load(BASELINE)["claims"], BASELINE
    return None, None


def main(argv=None):
    argv = sys.argv[1:] if argv is None else argv

    if "--hold-all" in argv:
        # Record every CURRENT flag as reviewed-and-held at its exact content. Run this after a
        # relay is delivered; a later edit to any held claim un-holds it automatically (fingerprint
        # mismatch). Never affects verdicts -- display only.
        working = _load("claims.json")["claims"]
        sources = _load("sources.json")
        source_ids = {k for k in sources if not k.startswith("_")}
        baseline, _lbl = _resolve_baseline()
        if baseline is None:
            print("no baseline; nothing to hold.")
            return 0
        rep = bank_gate(baseline, working, source_ids)
        wby = {c["id"]: c for c in working}
        held = {}
        for r in rep["flags"]:
            held[r["claim_id"]] = {"sha": _fingerprint(wby[r["claim_id"]]),
                                   "severity": r.get("_severity", "SUBSTANTIVE")}
        for cid in rep["deletions"]:
            held["DELETED:" + cid] = {"sha": "deleted", "severity": "DELETION"}
        with open(os.path.join(HERE, HELDFILE), "w") as f:
            json.dump(held, f, indent=1)
        print(f"held-ledger written: {len(held)} flag(s) marked reviewed-and-held.")
        return 0

    if "--accept" in argv:
        # Refresh the baseline to the CURRENT claims.json -- do this ONLY after the firewall + human
        # have accepted the change. Copies verbatim to avoid reformatting churn.
        shutil.copyfile(os.path.join(HERE, "claims.json"), os.path.join(HERE, BASELINE))
        n = len(_load("claims.json")["claims"])
        print(f"baseline refreshed: {BASELINE} <- claims.json ({n} claims).")
        return 0

    working = _load("claims.json")["claims"]
    sources = _load("sources.json")
    source_ids = {k for k in sources if not k.startswith("_")}

    baseline, label = _resolve_baseline()
    if baseline is None:
        print(f"no baseline found (no git HEAD, no {BASELINE}). Seed one with `bankgate.py --accept`.")
        return 0

    rep = bank_gate(baseline, working, source_ids)
    print("=" * 78)
    print(f"BANK-TIME GATE   (baseline: {label})")
    print("=" * 78)
    drift = "UNCHANGED" if rep["net_baseline"] == rep["net_working"] else "CHANGED"
    print(f"changed claims: {rep['n_changed']}   net ledger: {rep['net_baseline']} -> {rep['net_working']} ({drift})")

    for r in rep["blocks"]:
        print(f"\n  [BLOCK] {r['claim_id']}  (changed: {r.get('_changed_fields')})")
        for b in r["discipline"]["blocking"]:
            print(f"     - {b}")
        for d in r["dependencies"]["unresolved"]:
            print(f"     - unresolved dep: {d}")
        for cyc in r["dependencies"]["introduces_cycle"]:
            print(f"     - {cyc}")
    held = _load_held()
    wby = {c["id"]: c for c in working}
    n_new = n_held = 0
    for r in rep["flags"]:
        cid = r["claim_id"]
        rec = held.get(cid)
        is_held = bool(rec) and rec.get("sha") == _fingerprint(wby[cid])
        sev = r.get("_severity", "SUBSTANTIVE")
        if is_held:
            n_held += 1
            print(f"  [HELD/{sev}] {cid}  (reviewed-and-held; unchanged since review)")
            continue
        n_new += 1
        loud = "!!! " if sev == "TIER-OR-LEDGER" else ""
        tag = "NEW" if r["is_new"] else "changed: " + str(r.get("_changed_fields"))
        print(f"\n  {loud}[NEW-FLAG/{sev}] {cid}  ({tag})")
        if sev == "TIER-OR-LEDGER":
            print("     ^ TIER/LEDGER/DISPOSITION MOVED -- categorically above a field edit; "
                  "this line is loud on purpose.")
        for fl in r["consistency_flags"]:
            print(f"     - {fl}")
    for cid in rep["deletions"]:
        key = "DELETED:" + cid
        if key in held:
            n_held += 1
            print(f"  [HELD/DELETION] {cid}  (reviewed-and-held)")
        else:
            n_new += 1
            print(f"\n  [NEW-FLAG/DELETION] DELETED claim: {cid} (removing a banked claim is substantive)")
    if rep["flags"] or rep["deletions"]:
        print(f"\n  flags: {n_new} NEW (never reviewed) / {n_held} held (reviewed, awaiting accept)")

    print(f"\nOVERALL: {rep['overall']}")
    if rep["overall"] == "BLOCK":
        print("  -> bank BLOCKED. Fix the discipline/structural violation before banking.")
        return 1
    if rep["overall"] == "FLAG-FOR-FIREWALL":
        print("  -> surfaced for the both-directions firewall + human relay before acceptance.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
