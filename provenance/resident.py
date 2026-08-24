#!/usr/bin/env python3
"""GRUT Resident -- Layers 2-3: the dependency graph + the propose interface.

Lifts the static auditor (auditor.py, Layer 1) into a resident CONSISTENCY engine: given a
PROPOSED new claim or a CHANGE to an existing one, deterministically report the full
consistency consequences on the GRUT register. This is the DETERMINISTIC FLOOR of the
"scientific operating system":
    Layer 1 -- the auditor: per-claim discipline checks (tiered/sourced/falsifiable/not-laundered).
    Layer 2 -- the dependency graph: the DAG of rests-on edges (this module).
    Layer 3 -- the propose interface: propose()/check_change() report consequences (this module).
    Layer 4 -- LLM semantic checks (does it MEAN to re-open a no-go; is it truly novel) -- LATER.
    Layer 5 -- test wiring (each overturning_computation actually runnable) -- WIRED
               2026-08-09 (test_layer5_overturning.py: existence always; execution
               behind GRUT_RUN_SLOW=1).

THE BOUNDARY (load-bearing): the resident verifies DISCIPLINE and CONSISTENCY, NOT TRUTH. It
REPORTS consequences; it does NOT certify physical correctness and does NOT auto-bank substantive
claims. Every new substantive claim defaults to FLAG-FOR-FIREWALL -- the adversarial screen +
human sign-off remain the truth-check. The resident makes laundering HARDER, never banking EASIER:
it can BLOCK or FLAG, it can never turn a substantive claim into a silent PASS.

Pure Python stdlib.
"""
import re

from auditor import audit_claim, DEFAULT_TIERS

# STRUCTURED disposition (AUTHORITATIVE, added 2026-07-04). A claim's OWN closed/disfavored
# disposition lives in its enumerated `disposition` field -- this is what `_is_closed` reads. Because
# it is a structured field, cross-references to OTHER claims' markers and negations *in prose* CANNOT
# false-flag it (the three free-text-regex near-misses of the program: the `refuted`-negation, the
# version-token, and the `info_i2 was refuted` cross-reference). Open == the field is absent/""/"open".
CLOSED_DISPOSITIONS = frozenset({
    "screened-refuted", "settled-negative", "no_go_export", "disfavored",
    "frozen-V1", "moot", "deferred", "screened-dissolves", "forbidden",
    # ADDED 2026-08-04: a node retired because the ATOMICITY TEST split it into children. CLOSED --
    # nothing may depend on it as live ground -- but NOT deleted: the id appears in banked text, and
    # a reader resolving a live id against nothing silently inherits a default, which is the failure
    # class this program keeps finding at the bottom of its defects.
    "superseded-by-split",
})

# Free-text marker TOKENS + the negation guard -- DEMOTED to a non-authoritative HINT (may warn,
# never flags alone; see `_disposition_hint`). Retained only to surface a "did you forget to migrate?"
# warning; they never determine a flag.
CLOSED_MARKERS = ("settled-negative", "refuted", "moot", "no_go_export",
                  "disfavored", "deferred", "forbidden", "screened-dissolves",
                  "superseded-by-split")
_NEGATED_REFUTED = re.compile(r"\b(?:nor|not|never)\s+refuted\b", re.I)

# Tiers that assert a *result*. A result cannot cleanly rest on an open/assumed input.
RESULT_TIERS = frozenset({"shown", "derived"})
# Tiers that are open or merely pending/assumed (legitimate to be "pending" on, never "shown" on).
OPEN_TIERS = frozenset({"to-derive", "assumed", "derived-pending"})

# Substantive fields: changing any of these is a substantive change (-> defaults to FLAG).
# A provenance/lineage edit to a BANKED claim must never bank easier than a fresh claim:
#   overturning_computation = the falsifier (degrading it hollows the falsifiability guarantee);
#   sub_status              = carries closed-state markers (changing it re-opens a disposition);
#   sources                 = the provenance basis (gutting it removes a banked claim's support);
#   depends_on              = the lineage (emptying it orphans a banked result);
#   boundary_condition      = the conditions a claim holds UNDER (removing one silently broadens it);
#   match_verdict           = the B1 payload -- a CLAIM about GRUT's relation to a borrowed medium; a
#                             reword can pre-answer an open node it attaches_to (the superfluid/KNOB-2
#                             semantic tier-contradiction the overseer caught), so it must be firewalled;
#   attaches_to             = the B1 cross-reference edge (where a borrowed medium anchors on the map).
SUBSTANTIVE_FIELDS = ("tier", "ledger_delta", "statement", "overturning_computation", "sub_status",
                      "sources", "depends_on", "boundary_condition", "disposition", "prior_lineage",
                      "match_verdict", "attaches_to")


# --------------------------------------------------------------------------- graph

def dependency_graph(claims):
    """Build the DAG {id: [depends_on ids]} and validate it.

    Returns (graph, errors). errors == [] iff the graph is a valid DAG:
      - every depends_on resolves to a real claim id, and
      - the graph is acyclic.
    """
    by_id = {c["id"]: c for c in claims}
    graph = {c["id"]: list(c.get("depends_on", [])) for c in claims}
    errors = []

    for cid, deps in graph.items():
        for d in deps:
            if d not in by_id:
                errors.append(f"{cid}: depends_on '{d}' does not resolve to a real claim id")

    WHITE, GREY, BLACK = 0, 1, 2
    color = {cid: WHITE for cid in graph}

    def visit(u, path):
        color[u] = GREY
        for v in graph.get(u, []):
            if v not in color:
                continue  # unresolved edge, already reported
            if color[v] == GREY:
                errors.append("CYCLE detected: " + " -> ".join(path + [u, v]))
                continue
            if color[v] == WHITE:
                visit(v, path + [u])
        color[u] = BLACK

    for cid in graph:
        if color[cid] == WHITE:
            visit(cid, [])
    return graph, errors


def downstream(claim_id, claims):
    """Transitive set of claims that would be AFFECTED if claim_id changes (its dependents)."""
    rev = {}
    for c in claims:
        for d in c.get("depends_on", []):
            rev.setdefault(d, []).append(c["id"])
    seen, stack, out = set(), [claim_id], []
    while stack:
        u = stack.pop()
        for v in rev.get(u, []):
            if v not in seen:
                seen.add(v)
                out.append(v)
                stack.append(v)
    return out


# --------------------------------------------------------------------------- helpers

def _is_closed(claim):
    """AUTHORITATIVE: is this claim a closed / disfavored disposition? Reads the STRUCTURED
    `disposition` field ONLY -- so a claim is closed iff its OWN enumerated marker says so. Prose
    (sub_status/tier) is NOT scanned here: cross-references to other claims' markers and negations
    cannot false-flag. The free-text scan survives only as `_disposition_hint` (non-authoritative)."""
    return claim.get("disposition") in CLOSED_DISPOSITIONS


def _disposition_hint(claim):
    """NON-AUTHORITATIVE hint (may warn, never flags). If prose (sub_status/tier) mentions a
    closed-marker token but the structured `disposition` is OPEN, surface a hint -- it is EITHER a
    legitimate cross-reference/negation (fine) OR a missed migration (fix it). Never a flag."""
    if claim.get("disposition") in CLOSED_DISPOSITIONS:
        return None                                   # already closed by the structured field
    blob = ((claim.get("sub_status") or "") + " " + (claim.get("tier") or "")).lower()
    blob = _NEGATED_REFUTED.sub(" ", blob)            # 'neither...nor refuted' is not a marker
    hit = next((m for m in CLOSED_MARKERS if m in blob), None)
    if hit:
        return (f"HINT (non-authoritative): sub_status prose mentions '{hit}' but the structured "
                f"`disposition` is open -- verify it is a cross-reference/negation, not a missed migration.")
    return None


def _is_substantive(claim):
    """Does this claim assert physics content (has a tier in the physics vocabulary)?"""
    return claim.get("tier") in DEFAULT_TIERS


# Prior-lineage detection, split so the version token is CASE-SENSITIVE and capped at the ACTUAL
# prior versions (v2/v3/v4). Conventions this encodes (decided 2026-06-29, after the old `\bv[2-9]\b`
# false-flagged the current version AND capital-V program phases):
#   - prior lineage is written LOWERCASE   ("the v4 dark-matter line")        -> FLAG
#   - the current rebuild is v5 (NOT lineage); future phases v6+ don't exist  -> CLEAN  (capped at v4)
#   - the program PHASES are CAPITAL-V      ("Version II", "V2 frontier")      -> CLEAN  (case-sensitive)
# The PHRASE markers stay case-insensitive. KNOWN FRAGILITY: free-text regex for disposition is
# structurally brittle -- this is the 2nd such false-positive of the session (cf. `_is_closed` matching
# "refuted" inside "neither refuted"). Durable direction (a V2-era floor-cleanup, NOT done now): a
# structured lineage marker field, with this regex demoted to a backstop. See RESULTS_resident.md.
_PRIOR_LINEAGE_VERSION = re.compile(r"\bv[2-4]\b|\bv[2-4]/")  # case-SENSITIVE: lowercase 'v' only
_PRIOR_LINEAGE_PHRASE = re.compile(
    r"prior[- ]lineage import|propagating[- ]relic|(?:previous|prior|earlier)\s+version", re.I)


def _prior_lineage(claim):
    """AUTHORITATIVE: does this claim import a prior GRUT lineage? Reads the STRUCTURED
    `prior_lineage` boolean ONLY -- a claim imports lineage iff it DECLARES so. The free-text version
    regex is NOT authoritative here (it survives as `_lineage_hint`), so v5 / capital-V program phases
    ('Version II' / 'V2') and cross-references cannot false-flag. It FLAGs, never blocks."""
    return bool(claim.get("prior_lineage", False))


def _lineage_hint(claim):
    """NON-AUTHORITATIVE hint (may warn, never flags). If the statement matches the (lowercase v2-v4 /
    phrase) prior-lineage regex but `prior_lineage` is not declared, surface a hint -- EITHER a
    current-version / cross reference (fine) OR an undeclared import (declare it). Never a flag."""
    if claim.get("prior_lineage"):
        return None
    blob = re.sub(r"\s+", " ", str(claim.get("statement", "")))
    if _PRIOR_LINEAGE_VERSION.search(blob) or _PRIOR_LINEAGE_PHRASE.search(blob):
        return ("HINT (non-authoritative): statement matches the prior-lineage regex but "
                "`prior_lineage` is not declared -- verify it is a current-version/cross reference.")
    return None


def _hints(claim):
    """All non-authoritative hints for a claim (may warn; never flag / never affect the verdict)."""
    return [h for h in (_disposition_hint(claim), _lineage_hint(claim)) if h]


def _substantive_change(old, new):
    """Did a CHANGE alter a load-bearing field (tier / ledger_delta / statement)?"""
    return any(old.get(f) != new.get(f) for f in SUBSTANTIVE_FIELDS)


# --------------------------------------------------------------------------- consistency

def consistency_flags(claim, claims):
    """Machine-checkable consistency flags (NOT truth checks). Returns list[str].

    These never BLOCK on their own (a heuristic should not hard-block) -- they push the
    verdict to FLAG-FOR-FIREWALL so the adversarial screen + human decide.
    """
    flags = []
    by_id = {c["id"]: c for c in claims}

    # (1a) re-opens a closed disposition by CHANGING it  (authoritative: the structured `disposition`)
    existing = by_id.get(claim.get("id"))
    if existing is not None and _is_closed(existing):
        flags.append(
            f"RE-OPENS: '{claim['id']}' is currently a closed/disfavored disposition "
            f"(disposition={existing.get('disposition')!r}); changing it re-opens settled ground -- firewall must decide.")

    # (1b) builds on closed ground: depends_on a closed/disfavored claim
    for d in claim.get("depends_on", []):
        dep = by_id.get(d)
        if dep is not None and _is_closed(dep):
            flags.append(
                f"BUILDS-ON-CLOSED: rests on '{d}' which is closed/disfavored "
                f"(disposition={dep.get('disposition')!r}); a surviving result here would re-open it -- firewall must decide.")

    # (2) tier contradiction: a RESULT tier resting on an OPEN/assumed input
    if claim.get("tier") in RESULT_TIERS:
        for d in claim.get("depends_on", []):
            dep = by_id.get(d)
            if dep is not None and dep.get("tier") in OPEN_TIERS:
                flags.append(
                    f"TIER-CONTRADICTION: tier '{claim.get('tier')}' rests on '{d}' "
                    f"(tier '{dep.get('tier')}') -- a result cannot cleanly stand on an open/assumed input "
                    f"(at most 'derived-pending' on it).")

    # (3) orphaned result: a result-tier claim that rests on NOTHING. Flag a CHANGE that empties a
    #     previously non-empty depends_on (orphaning a banked result), and a NEW result-tier claim
    #     with empty depends_on. Legitimately-rootless foundational claims (the stance / borrowed
    #     axioms, e.g. rung1/rung9a/founding_h1) keep their empty depends_on and are NOT re-flagged.
    if claim.get("tier") in RESULT_TIERS and not claim.get("depends_on"):
        if existing is None:
            flags.append(
                f"ORPHANED-RESULT: a new '{claim.get('tier')}' result with empty depends_on rests on "
                "nothing -- a result should rest on something (or be marked a borrowed axiom).")
        elif existing.get("depends_on"):
            flags.append(
                f"ORPHANED-RESULT: '{claim['id']}' ('{claim.get('tier')}') had depends_on "
                f"{existing.get('depends_on')}; emptying it orphans a banked result.")

    # (4) prior-lineage import (forbidden; authoritative: the structured `prior_lineage` declaration)
    if _prior_lineage(claim):
        flags.append(
            "PRIOR-LINEAGE: the claim DECLARES prior_lineage (imports a prior GRUT version) -- "
            "forbidden; re-derive and bank inside this register first.")

    return flags


# --------------------------------------------------------------------------- propose / change

def propose(claim, claims, source_ids, valid_tiers=DEFAULT_TIERS):
    """Report the full, deterministic consistency consequences of proposing `claim`.

    `claim` may be NEW (id not in claims) or a fully-merged CHANGE (id present). Returns a
    report dict with a verdict in {PASS, BLOCK, FLAG-FOR-FIREWALL}. Pure: reads, never writes,
    never banks.
    """
    by_id = {c["id"]: c for c in claims}
    cid = claim.get("id")
    is_new = cid not in by_id

    # -- discipline (Layer 1) --
    blocking, warnings, delta, flagged = audit_claim(claim, source_ids, valid_tiers)
    if flagged:  # a laundering_ok waiver suppressed a +delta LAUNDERING block -- surface it
        warnings = list(warnings) + [
            f"LAUNDERING-WAIVER: ledger_delta=+{delta} is accepted ONLY because laundering_ok is "
            "declared; the firewall/human must confirm this stance/recovery."]

    # -- ledger --
    cur_net = sum(c.get("ledger_delta", 0) for c in claims if isinstance(c.get("ledger_delta"), int))
    old_delta = 0 if is_new else by_id[cid].get("ledger_delta", 0)
    new_net = cur_net + (delta - (0 if is_new else old_delta))

    # -- dependencies --
    deps = claim.get("depends_on", [])
    unresolved = [d for d in deps if d not in by_id]
    rests_on = [d for d in deps if d in by_id]
    affected = [] if is_new else downstream(cid, claims)

    # -- structural: would this proposal introduce a CYCLE? (the DAG invariant the graph protects) --
    # Run the acyclicity detector on the register WITH this proposal applied -- a change that closes
    # a circular rests-on lineage must not slip through as a silent PASS.
    merged = [c for c in claims if c.get("id") != cid] + [claim]
    _, graph_errors = dependency_graph(merged)
    cycles = [e for e in graph_errors if e.startswith("CYCLE")]

    # -- consistency (Layer 2/3) --
    flags = list(consistency_flags(claim, claims))
    if unresolved:
        flags.append(f"UNRESOLVED-DEPS: {unresolved} do not resolve to real claim ids.")
    for cyc in cycles:
        flags.append(f"CYCLE: this proposal closes a circular rests-on lineage -- {cyc}")
    # -- hints: non-authoritative free-text-regex warnings; surfaced, but NEVER change the verdict --
    hints = _hints(claim)

    # -- substantive? --
    if is_new:
        substantive = _is_substantive(claim)
    else:
        substantive = _substantive_change(by_id[cid], claim)

    # -- verdict: BLOCK > FLAG > PASS; substantive/flags never silently PASS --
    if blocking or unresolved or cycles:
        verdict = "BLOCK"                       # discipline OR structural (unresolved / cyclic) violation
    elif substantive or flags:
        verdict = "FLAG-FOR-FIREWALL"           # default for substantive; flags never relax to PASS
    else:
        verdict = "PASS"                        # non-substantive, disciplined, consistent

    return {
        "claim_id": cid,
        "is_new": is_new,
        "substantive": substantive,
        "discipline": {
            "blocking": blocking,
            "warnings": warnings,
            "laundering_blocked": any("LAUNDERING" in b for b in blocking),
            "laundering_waiver": flagged,   # True if a laundering_ok waiver suppressed a +delta block
        },
        "ledger": {
            "delta": delta,
            "current_net": cur_net,
            "new_net": new_net,
            "net_changes": new_net != cur_net,
        },
        "dependencies": {
            "rests_on": rests_on,
            "unresolved": unresolved,
            "downstream_affected": affected,
            "introduces_cycle": cycles,
        },
        "consistency_flags": flags,
        "hints": hints,                             # non-authoritative; may warn, never flags/blocks
        "verdict": verdict,
    }


def check_change(claim_id, new_fields, claims, source_ids, valid_tiers=DEFAULT_TIERS):
    """Report the consequences of CHANGING an existing claim's fields. Merges new_fields onto
    the existing claim and runs propose() on the result. Pure: never writes, never banks."""
    by_id = {c["id"]: c for c in claims}
    if claim_id not in by_id:
        return {"claim_id": claim_id, "verdict": "BLOCK",
                "error": f"no such claim id '{claim_id}' to change"}
    merged = dict(by_id[claim_id])
    merged.update(new_fields)
    report = propose(merged, claims, source_ids, valid_tiers)
    report["change_of_fields"] = sorted(new_fields)
    return report


# --------------------------------------------------------------------------- demo CLI

def _load(name):
    import json
    import os
    here = os.path.dirname(os.path.abspath(__file__))
    with open(os.path.join(here, name)) as f:
        return json.load(f)


def _demo():
    """Runnable demonstration (the functions above are pure; I/O lives only here)."""
    claims = _load("claims.json")["claims"]
    sources = _load("sources.json")
    source_ids = {k for k in sources if not k.startswith("_")}

    print("=" * 78)
    print("GRUT RESIDENT -- Layers 2-3 (dependency graph + propose interface) -- demo")
    print("=" * 78)
    graph, errors = dependency_graph(claims)
    edges = sum(len(v) for v in graph.values())
    print(f"\nDependency graph: {len(graph)} nodes, {edges} edges; "
          f"{'VALID DAG (acyclic, every edge resolves)' if not errors else 'ERRORS: ' + str(errors)}")

    examples = [
        ("clean new substantive claim",
         propose({"id": "demo_new", "statement": "A new responsive-vacuum sub-claim.",
                  "tier": "to-derive", "sources": ["kubo1966"],
                  "overturning_computation": "a calc that would kill it", "ledger_delta": 0,
                  "depends_on": ["rung1_inin_formalism"]}, claims, source_ids)),
        ("laundering attempt (derived, +2, unflagged)",
         propose({"id": "demo_launder", "statement": "We derived something for free.",
                  "tier": "derived", "sources": ["kubo1966"],
                  "overturning_computation": "a calc", "ledger_delta": 2,
                  "depends_on": ["rung1_inin_formalism"]}, claims, source_ids)),
        ("change a settled-negative (rung9b_bridge -> derived)",
         check_change("rung9b_bridge", {"tier": "derived"}, claims, source_ids)),
    ]
    for label, rep in examples:
        print(f"\n--- {label} ---")
        print(f"  VERDICT: {rep['verdict']}")
        if rep.get("discipline", {}).get("blocking"):
            print(f"  discipline-block: {rep['discipline']['blocking']}")
        for fl in rep.get("consistency_flags", []):
            print(f"  flag: {fl}")
        led = rep.get("ledger", {})
        if led:
            print(f"  ledger: delta {led['delta']:+d}, net {led['current_net']} -> {led['new_net']}"
                  f" ({'CHANGES' if led['net_changes'] else 'unchanged'})")
        dn = rep.get("dependencies", {}).get("downstream_affected")
        if dn:
            print(f"  downstream affected: {dn}")

    print("\n(REPORTS only -- the resident never banks. Substantive claims default to "
          "FLAG-FOR-FIREWALL:\n discipline + consistency, NOT truth.)")
    return 0


if __name__ == "__main__":
    raise SystemExit(_demo())
