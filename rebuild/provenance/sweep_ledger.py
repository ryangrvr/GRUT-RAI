"""sweep_ledger: EVERY RAISED CANDIDATE GETS A RECORDED DISPOSITION. Ruled 2026-08-04 (R2).

WHY THIS EXISTS. The 2026-08-04 omission sweep raised 24 candidates and the relayed material
accounted for 14. The other 10 were absorbed into clusters during dedup and silently ceased to
exist. One of the vanished was Q2(e) COSMIC TIME / GLOBAL FOLIATION -- a PRE-REGISTERED candidate,
absorbed into the FLRW compound and never adjudicated on its own. The same modality then went
missing from the quantum-foundations map. Twice is systematic.

The standard already forbade this in prose ("record the argument for every node examined, including
the ones that yield nothing"). A remembered rule is not a rule. THIS TURNS IT INTO A BROKEN BUILD:

    raw candidates raised  ==  sum over dispositions,  or the sweep does not reconcile.

*** "ABSORBED INTO A COMPOUND" IS A DISPOSITION, NOT A REASON TO DROP. *** That is the whole ruling.
An absorbed candidate must name the canonical it was absorbed into, and that canonical must itself
carry a real disposition -- so absorption is a POINTER, never a hole. A chain of absorptions
terminating in nothing is exactly the failure this file exists to make impossible.

NOTE ON WHERE THIS SITS. This checks BOOKKEEPING, not physics. It cannot tell you whether a
disposition is correct -- only that one was recorded and that the arithmetic closes. Same class as
the ledger's blind sum: a mechanical check on a human judgement, valuable precisely because it
touches no judgement at all.
"""
import json
import os

HERE = os.path.dirname(os.path.abspath(__file__))
SWEEPS = os.path.join(HERE, "sweeps")

# Frozen enumeration. A disposition not on this list is a refusal, not a new category -- adding one
# is a deliberate edit, reviewed, not something a sweep can do to itself at write time.
DISPOSITIONS = {
    "survived-verify":          "survived the adversarial lenses; a CANDIDATE, never a banked finding",
    "refuted-at-verify":        "failed the adversarial lenses",
    "already-booked":           "failed conjunct 2 -- carried elsewhere in THIS cluster's inventory",
    "dropped-membership-fence": "no named position denies it, or the denial changes nothing here",
    "absorbed-into-cluster":    "the same proposition as a canonical candidate, in other words; MUST "
                                "name that canonical, which must itself carry a real disposition",
    "not-adjudicated":          "raised and never ruled on -- ALWAYS BLOCKING. This value exists so "
                                "the gap can be RECORDED rather than hidden, not so it can be kept.",
}
TERMINAL = {"survived-verify", "refuted-at-verify", "already-booked", "dropped-membership-fence"}


def reconcile(record):
    """Return a list of blocking reasons. Empty list == the sweep reconciles.

    OPEN vs CLOSED (added 2026-08-05). A sweep may be `"status": "open"` -- still owed work, gaps
    RECORDED rather than hidden. reconcile() reports its gaps either way; what `open` changes is
    only whether the build goes red, and `close_blockers()` is what refuses to let an open sweep be
    declared done. This is NOT an escape hatch: closing requires zero gaps, and a sweep cannot be
    marked closed while carrying a single not-adjudicated candidate.

    WHY IT WAS NEEDED, and it is the same defect a third time: the follow-up wave's own scoring rule
    was `survives = (votes_for >= 2)`. When the verifying agents died mid-run, ZERO votes were cast,
    0 >= 2 is false, and candidates NOBODY HAD EXAMINED were silently filed as REFUTED. A gap
    wearing a verdict -- exactly what the 10 absorbed candidates were, reproduced inside the very
    machinery built to catch them. An absent verdict must never be scored as a negative verdict."""
    bad = []
    raw = record.get("raw", [])
    disp = record.get("dispositions", {})
    ids = [r["id"] for r in raw]

    if len(set(ids)) != len(ids):
        bad.append("duplicate raw candidate ids -- the arithmetic cannot close over a bag")

    for rid in ids:
        if rid not in disp:
            bad.append(f"raw candidate {rid!r} has NO recorded disposition -- this is the exact "
                       f"hole that swallowed the pre-registered cosmic-time candidate")
    for rid in disp:
        if rid not in ids:
            bad.append(f"disposition recorded for {rid!r}, which was never raised")

    for rid, d in disp.items():
        kind = d.get("disposition")
        if kind not in DISPOSITIONS:
            bad.append(f"{rid}: disposition {kind!r} is not in the frozen enumeration")
            continue
        if kind == "not-adjudicated":
            bad.append(f"{rid}: NOT ADJUDICATED. Recording the gap is better than hiding it, and it "
                       f"is still a gap: rule on it or state why it cannot be ruled on.")
        if kind == "absorbed-into-cluster":
            tgt = d.get("canonical")
            if not tgt:
                bad.append(f"{rid}: absorbed-into-cluster without naming a canonical -- absorption "
                           f"must be a POINTER, never a hole")
            elif tgt not in disp:
                bad.append(f"{rid}: absorbed into {tgt!r}, which has no disposition of its own")
            elif disp[tgt].get("disposition") not in TERMINAL:
                bad.append(f"{rid}: absorbed into {tgt!r}, whose disposition "
                           f"{disp[tgt].get('disposition')!r} is not terminal -- a chain of "
                           f"absorptions must END in an adjudication")

    # The headline arithmetic, stated as the ruling states it.
    n_disp = sum(1 for r in ids if r in disp)
    if n_disp != len(ids):
        bad.append(f"RECONCILIATION FAILED: {len(ids)} raised, {n_disp} dispositioned")

    # ---- THE SECOND HOLE, AND THE ONE THAT ACTUALLY SWALLOWED COSMIC TIME ----
    # Q2(e) was never RAISED at all, so a raw-candidate ledger alone would have reconciled
    # perfectly while the pre-registered candidate vanished. A sweep must also answer for the
    # candidates its own pre-registration named: "the sweep did not raise it" IS a disposition
    # (NOT-RAISED), and it is reportable rather than silent.
    pre = record.get("prereg_candidates", {})
    if not pre:
        bad.append("no prereg_candidates block -- a sweep must answer for the candidates its own "
                   "pre-registration named, or a named expectation can vanish without trace")
    for pid, p in pre.items():
        outcome = p.get("outcome")
        if outcome not in ("raised", "not-raised"):
            bad.append(f"prereg candidate {pid!r}: outcome must be 'raised' or 'not-raised'")
            continue
        if outcome == "raised":
            if p.get("raw_id") not in disp:
                bad.append(f"prereg candidate {pid!r} claims to have been raised as "
                           f"{p.get('raw_id')!r}, which carries no disposition")
        else:
            if not p.get("note"):
                bad.append(f"prereg candidate {pid!r} was NOT RAISED and carries no note -- a "
                           f"pre-registered expectation that the sweep did not reach is a finding "
                           f"about the sweep, and must be stated")
    return bad


def close_blockers(record):
    """What stands between this sweep and being CLOSED. A sweep with any of these may be recorded,
    relayed and reasoned about -- it may not be called finished."""
    return [b for b in reconcile(record) if "NOT ADJUDICATED" in b or "under-verified" in b]


def load_all():
    if not os.path.isdir(SWEEPS):
        return []
    out = []
    for fn in sorted(os.listdir(SWEEPS)):
        if fn.endswith(".json"):
            with open(os.path.join(SWEEPS, fn)) as f:
                out.append((fn, json.load(f)))
    return out


def main():
    rc = 0
    for fn, rec in load_all():
        bad = reconcile(rec)
        openq = rec.get("status") == "open"
        tally = {}
        for d in rec.get("dispositions", {}).values():
            tally[d.get("disposition")] = tally.get(d.get("disposition"), 0) + 1
        print(f"{fn}: {len(rec.get('raw', []))} raised -> " +
              ", ".join(f"{k} {v}" for k, v in sorted(tally.items())))
        if bad and openq:
            print(f"  OPEN -- {len(bad)} gap(s) RECORDED, not hidden. Cannot be closed until zero:")
            for b in bad[:12]:
                print("   -", b)
        elif bad:
            rc = 1
            print(f"  BLOCKING ({len(bad)}):")
            for b in bad[:12]:
                print("   -", b)
        else:
            print("  RECONCILES: every raised candidate carries a disposition.")
    return rc


if __name__ == "__main__":
    raise SystemExit(main())
