"""GRUT-RAI v4.1 — the one-pass reader view (the SUCCESS CRITERION).

Renders the registry so an outside physicist can see, in one pass and without
trusting us: what is DERIVED (and clean vs provisional vs anchored-SPLIT), what is
ANCHORED, what is OPEN (with its computable target), what is BORROWED (novelty),
and what would FALSIFY each forward claim.

Run:  python -m v41.audit
"""
from __future__ import annotations

from v41.gate import Tier, validate, provisional_on, anchored_inputs, transitive_inputs
from v41.registry import REGISTRY as R


def _derived_status(cid: str) -> str:
    prov = provisional_on(R, cid)
    if prov:
        return "PROVISIONAL (rests on OPEN: " + ", ".join(prov) + ")"
    anc = anchored_inputs(R, cid)
    if anc:
        return "SPLIT (mechanism derived; consumes anchored: " + ", ".join(anc) + ")"
    return "clean"


def render() -> str:
    L = []
    def p(s=""): L.append(s)
    by = lambda t: [c for c in R.values() if c.tier == t]

    p("GRUT-RAI v4.1 — REGISTRY AUDIT  (the one-pass reader view)")
    p("=" * 64)

    p("\nANCHORS — load-bearing inputs, entered visibly (never silently promoted):")
    for c in by(Tier.ANCHOR):
        p(f"  • {c.id:<32} {c.statement.split('—')[0].strip()[:64]}")

    p("\nOPEN — no mechanism yet; each names the computable target that closes it:")
    for c in by(Tier.OPEN):
        p(f"  • {c.id:<32} → target: {c.target}")

    p("\nDERIVED — derivation_ref + a PASSING runnable check + novelty tag:")
    for c in by(Tier.DERIVED):
        ok = "✓" if (c.check and c.check()) else "✗"
        p(f"  • {c.id:<28} [{c.step.value if c.step else '—'}] "
          f"[{c.novelty.value if c.novelty else '—'}] check:{ok}  — {_derived_status(c.id)}")
        if c.novelty_cite:
            p(f"        novelty: {c.novelty_cite}")

    p("\nFORBIDDEN — no-go theorems (the framework ruling something out by its axioms):")
    for c in by(Tier.FORBIDDEN):
        prov = provisional_on(R, c.id)
        tail = f"  — PROVISIONAL (rests on OPEN: {', '.join(prov)})" if prov else ""
        p(f"  • {c.id:<32} [{(c.novelty.value if c.novelty else '—')}]{tail}")
        if c.novelty_cite:
            p(f"        novelty: {c.novelty_cite}")

    p("\nHOSTED — received from outside, or resting on an OPEN input (NOT derivable):")
    for c in by(Tier.HOSTED):
        opens = sorted(i for i in c.inputs if i in R and R[i].tier == Tier.OPEN)
        tail = f"  — rests on OPEN: {', '.join(opens)} (gate forbids DERIVED)" if opens else ""
        p(f"  • {c.id:<32} [{c.step.value if c.step else 'PLACE'}]{tail}")

    p("\nCONJECTURAL — a structural hook only:")
    for c in by(Tier.CONJECTURAL):
        p(f"  • {c.id:<32} {c.statement[:60]}…")

    # Summary
    counts = {t.value: len(by(t)) for t in Tier}
    derived = by(Tier.DERIVED)
    clean = [c for c in derived if not provisional_on(R, c.id)]
    derive_rungs = [c for c in R.values() if getattr(c.step, "value", None) == "DERIVE"]
    place_rungs = [c for c in R.values() if getattr(c.step, "value", None) == "PLACE"]
    viols = validate(R)
    p("\n" + "-" * 64)
    p("SUMMARY")
    p("  tiers: " + " | ".join(f"{k} {v}" for k, v in counts.items() if v))
    p(f"  forward score: {len(derive_rungs)} DERIVE rungs, {len(place_rungs)} PLACE rungs")
    p(f"  DERIVED: {len(derived)} total — {len(clean)} clean, {len(derived)-len(clean)} provisional")
    p("  research spine (the two OPEN targets every sector inherits):")
    for c in by(Tier.OPEN):
        p(f"     - {c.id}: {c.target}")
    p(f"  GATE: {'PASS (0 violations)' if not viols else 'FAIL — ' + str(len(viols)) + ' violations'}")
    return "\n".join(L)


if __name__ == "__main__":
    print(render())
