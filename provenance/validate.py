#!/usr/bin/env python3
"""GRUT provenance validator (track c) -- the GRUT-specific gate.

Thin wrapper around the GENERALIZED discipline engine in auditor.py, applied to THIS repo's
register (claims.json + sources.json). The discipline itself (tiering, sourcing, falsifiability,
anti-laundering) now lives in auditor.audit() so it can audit any claim set; this file only:
  (1) loads GRUT's files, (2) calls the engine, (3) runs one GRUT-SPECIFIC ledger invariant
  (the alpha-normalization single-count, below -- NOT part of the generalized engine), and
  (4) prints the report and sets the exit code.

It verifies DISCIPLINE, not TRUTH: a wrong-but-well-provenanced claim passes, and the net is a
blind sum of ledger_delta (see auditor.py / RESULTS_auditor.md). Run it in CI / before any render.

No third-party deps. Python 3 stdlib only.
"""
import json
import os
import sys

from auditor import audit, DEFAULT_TIERS

HERE = os.path.dirname(os.path.abspath(__file__))


def load(name):
    with open(os.path.join(HERE, name), "r") as f:
        return json.load(f)


def grut_specific_checks(claims):
    """GRUT-SPECIFIC ledger invariants -- deliberately NOT part of the generalized engine.

    Closes the one caveat a blind ledger-sum cannot: the alpha-normalization cost must be
    booked EXACTLY ONCE. In this register that cost is represented by the SUSPENDED rung-9
    anchor credit (rung9a_value at 0 / dependency-ledger item #13), NOT double-booked as a
    +1 on the adopted-normalization claim rung9b_bridge. So assert rung9b_bridge carries no
    positive ledger_delta. This is a narrow repo-specific invariant, not a general truth-check;
    it lives here in the wrapper, never in auditor.py.
    """
    out = []
    by = {c.get("id"): c for c in claims}
    b = by.get("rung9b_bridge")
    if b is not None and isinstance(b.get("ledger_delta"), int) and b["ledger_delta"] > 0:
        out.append(
            "rung9b_bridge: alpha-normalization DOUBLE-COUNT - the adopted c_0 normalization "
            f"carries ledger_delta=+{b['ledger_delta']}, but its cost is already booked once as "
            "the suspended rung-9 anchor credit (rung9a_value=0 / dependency-ledger item #13). "
            "Must be 0."
        )
    return out


def main():
    sources = load("sources.json")
    source_ids = {k for k in sources if not k.startswith("_")}
    claims = load("claims.json")["claims"]
    # SCOPED 2026-08-04: this is GRUT's gate and audits GRUT's register only. Nodes carrying a
    # different ledger_scope (the vacuum-cluster physics map) live in the same file but under a
    # different tier vocabulary and a SEPARATE ledger -- see provenance/validate_scoped.py. The
    # default is "grut", so every pre-existing node keeps its meaning untouched.
    all_claims = claims
    claims = [c for c in claims if c.get("ledger_scope", "grut") == "grut"]
    other = len(all_claims) - len(claims)

    res = audit(claims, source_ids, valid_tiers=DEFAULT_TIERS)
    grut_blocks = grut_specific_checks(claims)

    print("=" * 78)
    print("GRUT PROVENANCE VALIDATOR")
    if other:
        print(f"  (scoped: {len(claims)} grut nodes audited; {other} out-of-scope nodes are "
              f"audited by validate_scoped.py under their own vocabulary)")
    print("=" * 78)

    for tier, cid, delta, flagged in res.rows:
        tier_disp = tier.upper() if tier else "?"
        flag = "  [stance/recovery: ledger %+d, declared]" % delta if flagged else ""
        print(f"  [{tier_disp:>15}] {cid:24} ledger {delta:+d}{flag}")

    print("-" * 78)
    print(f"NET underived-input ledger across ladder: {res.net:+d}")
    print("(win condition is a SHORT marked list, not zero - every +1 is flagged, not hidden)")

    if res.warnings:
        print("\nWARNINGS (non-blocking):")
        for w in res.warnings:
            print("  ! " + w)

    blocking = res.blocking + grut_blocks
    if blocking:
        print("\nBLOCKING VIOLATIONS:")
        for b in blocking:
            print("  X " + b)
        print(f"\nFAIL: {len(blocking)} blocking violation(s). No render until resolved.")
        return 1

    waived = [(c["id"], c.get("ledger_delta", 0)) for c in claims
              if c.get("laundering_ok") and isinstance(c.get("ledger_delta"), int)
              and c["ledger_delta"] > 0]
    wt = sum(d for _, d in waived)
    if waived:
        print(f"\n  WAIVED-BY-STANCE (laundering_ok, each with a declared stance_justification): "
              f"+{wt} of the net sits behind {len(waived)} waivers:")
        for cid, d in waived:
            print(f"    +{d}  {cid}")
        print("  A waiver is a DECLARED STANCE, not an exemption from arithmetic -- the +8 is in "
              "the net\n  because the register says so openly, and this line exists so that fact "
              "sits on the gate's\n  own face rather than being discoverable only by audit.")
    print("\nPASS: every claim tiered, sourced, falsifiable; laundering DISCIPLINE enforced "
          "(declared\nfields + blind sum -- discipline, not truth; see auditor.py docstring).")
    return 0


if __name__ == "__main__":
    sys.exit(main())
