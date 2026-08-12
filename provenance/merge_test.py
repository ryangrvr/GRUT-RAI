#!/usr/bin/env python3
"""merge_test v3: mechanizes the LEDGER-VECTOR arithmetic of merge_criterion.py.

v2 repairs four defects found by independent review of v1, each with a constructed counterexample.
The repair order was: vector verdict (D4) -> dimension counting (D3) -> the tally fix + validator
(D2) -> n sides and two new classes (D1). See merge_criterion.py for the full diagnosis.

v3 repairs what a NARROW review of v2's NEW machinery found: every v2 repair was real, and every
one RELOCATED the free parameter rather than eliminating it. v1 counted analyst-chosen LABELS; v2
summed analyst-chosen INTEGERS, which is strictly MORE expressive for an attacker. The verdict was
"sound in the refusal direction, unsound in the reduction direction" -- the exact wrong half, since
a live sweep can only ever BANK a reduction.
  F1/F2 the registry is a real frozen object; dimensions are NEVER read from the proposal.
  F3     `relation_inputs` is mandatory and eliminations must be bound to it -- v2 let an
         IRRELEVANT EXTRA SIDE fund -1 each, so reduction depth was a free parameter equal to the
         number of sides listed.
  F4/F5  the sensitivity span is structural and BOTH directions are computed; THE WORST READING IS
         THE VERDICT. v2's flag fired on 0/244,888 REDUCTIONs and 0/244,888 TRADEs -- provably mute
         in exactly the direction the guard exists for.
  F6     three axes {continuous, discrete, posit}, never summed -- v2 summed three incommensurable
         things inside "numeric", which is D4's own error one level down.

Pure stdlib. Self-tested. Mutation battery registered per the standing rule.
"""
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)

from merge_criterion import (MERGE_CLASSES, RELATION_STATUS, HUMAN_CHECKLIST, VERDICTS,
                             RETIRED_INPUTS,
                             ATOMIC, AXES, SCOPES)


def relation_cost(status):
    if status not in RELATION_STATUS:
        raise ValueError(f"relation status must be one of {sorted(RELATION_STATUS)}; got {status!r}")
    return RELATION_STATUS[status]


def _vec(ids):
    """F1+F6: dimensions come ONLY from the frozen registry, split by KIND. Never from a proposal."""
    v = {"continuous": 0, "discrete": 0}
    for i in ids:
        e = ATOMIC.get(i, {"dim": 1, "kind": "continuous"})   # unreachable via evaluate():
        # _validate refuses unregistered ids first. Present so that DISABLING the validator
        # yields a wrong VERDICT (which a control catches) instead of a traceback (which
        # proves only that the program broke).
        v[e["kind"]] += e["dim"]
    return v


def _validate(proposal, sides, merged, new, rel_inputs):
    bad = []
    for k in HUMAN_CHECKLIST:
        if not proposal.get(k):
            bad.append(f"missing checklist item {k!r}")
    if proposal.get("merge_class") not in MERGE_CLASSES:
        bad.append(f"merge_class must be one of {sorted(MERGE_CLASSES)}")
    if len(sides) < 2:
        bad.append("a merge needs at least two sides")
    # F1: an id absent from the frozen registry is REFUSED, never defaulted. Amending the registry
    # is a dated, hashed event -- the dimension of an input must not be settleable inside the
    # proposal that needs a particular answer.
    for i in set().union(*sides) | merged | new | rel_inputs:
        if i in RETIRED_INPUTS:
            bad.append(f"input {i!r} is RETIRED: {RETIRED_INPUTS[i]}. Name its children instead -- "
                       f"a retired id must never resolve to a silent default dimension.")
        elif i not in ATOMIC:
            bad.append(f"input {i!r} is not in the frozen ATOMIC registry -- amend the registry "
                       f"(a dated, hashed event), do not declare a dimension inside a proposal")
    if bad:
        return bad
    union = set().union(*sides)
    # F3(a): eliminations must be BOUND TO THE RELATION. v2 checked only subset-of-union, so a
    # relation could "eliminate" inputs it never mentions.
    elim = set(proposal.get("eliminates", []))
    if elim - union:
        bad.append(f"'eliminates' names {sorted(elim - union)}, which no side required")
    unbound = elim - rel_inputs
    if unbound:
        bad.append(f"'eliminates' names {sorted(unbound)}, which the relation does not reference "
                   f"(F3: an elimination must be bound to R, or reduction depth is just the number "
                   f"of inputs the analyst chose to list)")
    # BLOCK-8: an EMPTY merged account was v2's maximal reduction and required no content at all.
    # "R eliminates everything" is a deletion, not a merge; nothing can remain of the joint object.
    if not (merged | new):
        bad.append("the merged account is EMPTY -- 'R eliminates everything' is a deletion, not a "
                   "reduction, and was v2's highest-scoring proposal while requiring no content")
    dropped = union - merged - elim
    if dropped:
        bad.append(f"the merged account drops {sorted(dropped)} with no declared account")
    # F3(b): every side must actually participate. DEFENSE IN DEPTH, and honestly labelled as such:
    # while writing its mutation battery I could not construct a case this catches that F3(a) does
    # not already catch. The reviewer's padding attack ("append an irrelevant side and name it in
    # eliminates") is blocked by F3(a), because the elimination is unbound to R; and padding with a
    # RETAINED input provably cannot inflate depth, since it adds +1 to BOTH tallies. So this check
    # ships with NO mutant -- a battery entry nothing can isolate would be decoration, and claiming
    # coverage it does not have is the failure this program keeps finding in its own guards.
    for k, s in enumerate(sides):
        if not (s & (rel_inputs | merged)):
            bad.append(f"side {k} ({sorted(s)}) is touched neither by the relation nor by the "
                       f"merged account -- an unrelated side cannot fund a reduction (F3)")
    return bad


def _classify(dv, posit):
    """F6: axes are never summed. A reduction must not increase any axis and must not buy with a
    posit; anything bought with a posit or offset on another axis is a TRADE."""
    neg = any(dv[a] < 0 for a in ("continuous", "discrete"))
    pos = any(dv[a] > 0 for a in ("continuous", "discrete"))
    if neg and not pos and posit == 0:
        return "REDUCTION"
    if neg:
        return "TRADE"
    return "NO-REDUCTION"


_ORDER = {"REDUCTION": 0, "TRADE": 1, "NO-REDUCTION": 2}   # F5: worst = most conservative


def evaluate(proposal):
    sides = [set(s) for s in proposal.get("inputs_sides", [])]
    merged = set(proposal.get("merged_inputs", []))
    new = set(proposal.get("new_inputs", []))
    rel_inputs = set(proposal.get("relation_inputs", []) or [])

    bad = _validate(proposal, sides, merged, new, rel_inputs)
    if bad:
        return {"output_kind": "structural-verdict", "verdict": "REFUSED-INCOMPLETE",
                "refusals": bad, "note": VERDICTS["REFUSED-INCOMPLETE"]}
    try:
        cost = relation_cost(proposal["relation_status"])
    except (ValueError, KeyError) as e:
        return {"verdict": "REFUSED-INCOMPLETE", "refusals": [str(e)],
                "note": VERDICTS["REFUSED-INCOMPLETE"]}

    union = set().union(*sides)
    account = merged | new

    def delta(sep_ids):
        s, m = _vec(sep_ids), _vec(account)
        return {"continuous": m["continuous"] - s["continuous"],
                "discrete": m["discrete"] - s["discrete"], "posit": cost}

    # F4/F5: the sensitivity SPAN is structural and BOTH directions are computed. v2 tested one
    # direction, driven off `new` alone -- which is arithmetically inert (merged|new is unioned),
    # so an analyst could zero out the only warning by moving a string between two fields; and the
    # direction it did test could never flip a REDUCTION or a TRADE.
    readings = {}
    readings["as-declared"] = delta(union)
    drag = account - union
    if drag:
        readings["drag-as-side-requirement"] = delta(union | drag)
    # F5 (corrected): side inputs the RELATION does not touch, whether or not the merged
    # account retains them. The first cut of this was dead code -- it also subtracted `merged`,
    # and an input outside both must be eliminated, which F3 requires be relation-bound, so the
    # set was empty in every VALID proposal and the dual reading never fired.
    optional = union - rel_inputs
    if optional:
        readings["optional-side-inputs-dropped"] = delta(union - optional)

    scored = {k: (_classify(v, cost), v) for k, v in readings.items()}
    worst = max(scored.values(), key=lambda kv: _ORDER[kv[0]])[0]
    verdict = worst                                    # F5: THE WORST READING IS THE VERDICT
    declared = scored["as-declared"][0]

    # PART 1: which ledger could this reading even concern? A reduction whose eliminated ids
    # contain NO grut-input cannot be a GRUT ledger move, and that is said HERE, structurally,
    # rather than in a note a reader may skip. Same shape as ledger_scope keeping the two ledgers
    # from bleeding, one level down.
    eliminated = set(proposal.get("eliminates", []))
    # same defensive pattern as _vec: unreachable via evaluate() (the validator refuses
    # unregistered ids first), present so that DISABLING the validator yields a wrong
    # ANSWER a control can catch rather than a traceback that proves only a crash.
    elim_scopes = {ATOMIC.get(i, {"scope": "grut-input"})["scope"] for i in eliminated} \
        if eliminated else set()
    if "grut-input" in elim_scopes:
        ledger_scope = "grut" if elim_scopes == {"grut-input"} else "mixed"
    elif not eliminated:
        ledger_scope = "n/a"
    elif elim_scopes == {"borrowed-physics"}:
        ledger_scope = "borrowed-only"
    elif elim_scopes <= {"cluster-input"}:
        ledger_scope = "cluster"
    else:
        ledger_scope = "mixed"

    return {
        # CARDINAL INVARIANT: this is a DECLARED READING (arithmetic over analyst judgements), not
        # an adjudication. Only REFUSED-INCOMPLETE is a verdict the tool is entitled to reach.
        "output_kind": "declared-reading",
        "ledger_scope_of_reduction": ledger_scope,
        "eliminated_scopes": sorted(elim_scopes),
        "can_move_grut_ledger": ledger_scope in ("grut", "mixed"),
        "verdict": verdict,
        "verdict_as_declared": declared,
        "enumeration_sensitive": len({v[0] for v in scored.values()}) > 1,
        "readings": {k: {"verdict": v[0], "delta": v[1]} for k, v in scored.items()},
        "merge_class": proposal["merge_class"],
        "relation": proposal.get("relation"),
        "relation_status": proposal["relation_status"],
        "n_sides": len(sides),
        "separate": _vec(union), "separate_inputs": sorted(union),
        "merged": _vec(account), "merged_inputs": sorted(account),
        "delta": scored["as-declared"][1],
        "note": VERDICTS[verdict],
    }


def report(p):
    r = evaluate(p)
    print(f"\n  PROPOSAL: {p.get('name','<unnamed>')}")
    if r["verdict"] == "REFUSED-INCOMPLETE":
        print("    -> REFUSED-INCOMPLETE")
        for x in r["refusals"][:4]:
            print(f"       - {x}")
        return r
    d = r["delta"]
    print(f"    separate {r['separate']}   merged {r['merged']}   (R: {r['relation_status']})")
    print(f"    *** VECTOR: continuous {d['continuous']:+d}, discrete {d['discrete']:+d}, "
          f"posit {d['posit']:+d}  (NEVER summed) ***")
    if not r["can_move_grut_ledger"]:
        print(f"    [SCOPE: {r['ledger_scope_of_reduction']} -- eliminates "
              f"{r['eliminated_scopes'] or 'nothing'}; THIS READING CANNOT BE A GRUT LEDGER MOVE]")
    print(f"    -> {r['verdict']}  [DECLARED READING -- a candidate for adjudication, not a "
          f"verdict]" + ("" if not r["enumeration_sensitive"] else
          f"   [WORST of {len(r['readings'])} readings; as-declared was {r['verdict_as_declared']}]"))
    if r["enumeration_sensitive"]:
        for k, v in r["readings"].items():
            print(f"        {k:32s} {v['verdict']}")
    return r


# ============================== CONTROLS (v3) ==============================
# Ids are frozen-registry entries; control fixtures are prefixed _ctl_ so they cannot be mistaken
# for physics. Every control names the defect or regime it exists to catch.
CK = {"relation_status_justification": "control", "discharge_at_observed_values": "control",
      "input_enumeration_source": "control",
      # C1a: controls are synthetic, so their base is the fixture algebra itself. Stated rather
      # than left blank -- a blank here would be the silent resolution the field exists to stop.
      "relation_axioms": "control fixture; base = the synthetic relation as written"}

def C(**kw):
    d = dict(CK); d.update(kw); return d

CONTROLS = [
    C(name="C1 identity", merge_class="identity", relation="same values discharge both",
      relation_status="derived", relation_inputs=["_ctl_p", "_ctl_a1"],
      inputs_sides=[["_ctl_p", "_ctl_a1"], ["_ctl_p", "_ctl_a1"]], merged_inputs=["_ctl_p"],
      new_inputs=[], eliminates=["_ctl_a1"], expect="REDUCTION"),

    C(name="C2 D4: posited binary relation must be REACHABLE as a TRADE",
      merge_class="functional-relation", relation="x_B = R(x_A), posited", relation_status="posited",
      relation_inputs=["_ctl_xA", "_ctl_xB"], inputs_sides=[["_ctl_xA"], ["_ctl_xB"]],
      merged_inputs=["_ctl_xA"], new_inputs=[], eliminates=["_ctl_xB"], expect="TRADE"),

    C(name="C3 derived relation, drags nothing", merge_class="functional-relation",
      relation="x_B = R(x_A), derived", relation_status="derived",
      relation_inputs=["_ctl_xA", "_ctl_xB"], inputs_sides=[["_ctl_xA"], ["_ctl_xB"]],
      merged_inputs=["_ctl_xA"], new_inputs=[], eliminates=["_ctl_xB"], expect="REDUCTION"),

    C(name="C4 D3 BUNDLE: relabelling two atoms as one 'V' must NOT reduce (registry says dim 2)",
      merge_class="common-cause", relation="x_i = pi_i(V)", relation_status="derived",
      relation_inputs=["_ctl_xA", "_ctl_xB", "_ctl_V"], inputs_sides=[["_ctl_xA"], ["_ctl_xB"]],
      merged_inputs=["_ctl_V"], new_inputs=[], eliminates=["_ctl_xA", "_ctl_xB"],
      expect="NO-REDUCTION"),

    C(name="C5 F3 SIDE-PADDING: an irrelevant extra side must be REFUSED, not worth -1",
      merge_class="functional-relation", relation="x_B = R(x_A); _ctl_z does not appear in R",
      relation_status="derived", relation_inputs=["_ctl_xA", "_ctl_xB"],
      inputs_sides=[["_ctl_xA"], ["_ctl_xB"], ["_ctl_z"]], merged_inputs=["_ctl_xA"],
      new_inputs=[], eliminates=["_ctl_xB", "_ctl_z"], expect="REFUSED-INCOMPLETE"),

    C(name="C6 D1 shared constraint, n=3 (Friedmann shape)", merge_class="shared-constraint",
      relation="Om + OL + Ok = 1; the surface is 2-dimensional", relation_status="derived",
      relation_inputs=["_ctl_Om", "_ctl_OL", "_ctl_Ok", "_ctl_surface"],
      inputs_sides=[["_ctl_Om"], ["_ctl_OL"], ["_ctl_Ok"]], merged_inputs=["_ctl_surface"],
      new_inputs=[], eliminates=["_ctl_Om", "_ctl_OL", "_ctl_Ok"], expect="REDUCTION"),

    C(name="C7 D1 pairwise blindness: any PAIR of the same three must NOT reduce",
      merge_class="shared-constraint", relation="not localizable to a pair", relation_status="derived",
      relation_inputs=["_ctl_Om", "_ctl_OL"], inputs_sides=[["_ctl_Om"], ["_ctl_OL"]],
      merged_inputs=["_ctl_Om", "_ctl_OL"], new_inputs=[], eliminates=[], expect="NO-REDUCTION"),

    C(name="C8 obviously-distinct pair", merge_class="functional-relation",
      relation="asserted coincidence", relation_status="posited",
      relation_inputs=["_ctl_u", "_ctl_w"], inputs_sides=[["_ctl_u"], ["_ctl_w"]],
      merged_inputs=["_ctl_u", "_ctl_w"], new_inputs=[], eliminates=[], expect="NO-REDUCTION"),

    C(name="C9 definitional redundancy", merge_class="definitional", relation="B is A renamed",
      relation_status="derived", relation_inputs=["_ctl_p", "_ctl_palias"],
      inputs_sides=[["_ctl_p"], ["_ctl_palias"]], merged_inputs=["_ctl_p"], new_inputs=[],
      eliminates=["_ctl_palias"], expect="REDUCTION"),

    C(name="C10 dissolution", merge_class="dissolution", relation="B's discharge falsifies A's presupposition",
      relation_status="derived", relation_inputs=["_ctl_sA", "_ctl_sB"],
      inputs_sides=[["_ctl_sA"], ["_ctl_sB"]], merged_inputs=["_ctl_sB"], new_inputs=[],
      eliminates=["_ctl_sA"], expect="REDUCTION"),

    C(name="C11 F1 ISOLATED: an unregistered id that is RELATION-BOUND must still be REFUSED",
      # relation_inputs includes the unregistered id, so F3(a) and F3(b) both pass and ONLY the
      # registry check can catch it. Without this isolation the registry mutant survived, because
      # C11's earlier shape was refused by the relation-binding guard instead.
      merge_class="functional-relation", relation="x_B = R(x_A)", relation_status="derived",
      relation_inputs=["_ctl_xA", "not_in_registry"],
      inputs_sides=[["_ctl_xA"], ["not_in_registry"]],
      merged_inputs=["_ctl_xA"], new_inputs=[], eliminates=["not_in_registry"],
      expect="REFUSED-INCOMPLETE"),

    C(name="C12 unbound elimination is REFUSED (F3: R must reference what it removes)",
      merge_class="functional-relation", relation="x_B = R(x_A)", relation_status="derived",
      relation_inputs=["_ctl_xA"], inputs_sides=[["_ctl_xA"], ["_ctl_xB"]],
      merged_inputs=["_ctl_xA"], new_inputs=[], eliminates=["_ctl_xB"],
      expect="REFUSED-INCOMPLETE"),

    C(name="C13 F6 DISCRETE stance must not masquerade as a saved real parameter",
      merge_class="common-cause", relation="a discrete stance is subsumed", relation_status="derived",
      relation_inputs=["_ctl_gauge", "_ctl_xA"], inputs_sides=[["_ctl_gauge"], ["_ctl_xA"]],
      merged_inputs=["_ctl_xA"], new_inputs=[], eliminates=["_ctl_gauge"], expect="REDUCTION"),

    C(name="C16 BLOCK-8: an EMPTY merged account is REFUSED, not scored as a maximal reduction",
      merge_class="dissolution", relation="R eliminates everything", relation_status="derived",
      relation_inputs=["_ctl_xA", "_ctl_xB"], inputs_sides=[["_ctl_xA"], ["_ctl_xB"]],
      merged_inputs=[], new_inputs=[], eliminates=["_ctl_xA", "_ctl_xB"],
      expect="REFUSED-INCOMPLETE"),

    C(name="C15 F3(a) ISOLATED: an elimination R never references, on a side that DOES participate",
      # The padding side here is legitimate (it carries _ctl_c, which R references), so F3(b)
      # passes; only the relation-binding check can catch the unbound elimination of _ctl_xB.
      # Without this control, F3(a) and F3(b) each caught only the OTHER's mutant and neither was
      # isolated -- defense in depth that no test could distinguish from a single guard.
      merge_class="functional-relation", relation="x_A = R(c); xB is not referenced by R",
      relation_status="derived", relation_inputs=["_ctl_xA", "_ctl_c"],
      inputs_sides=[["_ctl_xA"], ["_ctl_xB", "_ctl_c"]], merged_inputs=["_ctl_xA", "_ctl_c"],
      new_inputs=[], eliminates=["_ctl_xB"], expect="REFUSED-INCOMPLETE"),

    C(name="C14 F5 the WORST reading is the verdict, not the favourable one",
      # _ctl_c sits on a side but R never references it. As declared this scores REDUCTION (-1);
      # under the reading where c is NOT a standing side requirement the saving evaporates. v2
      # reported only the favourable reading and its flag could never fire on a reduction at all.
      merge_class="functional-relation", relation="x_B = R(x_A); c is not referenced by R",
      relation_status="derived", relation_inputs=["_ctl_xA", "_ctl_xB"],
      inputs_sides=[["_ctl_xA", "_ctl_c"], ["_ctl_xB"]], merged_inputs=["_ctl_xA", "_ctl_c"],
      new_inputs=[], eliminates=["_ctl_xB"], expect="NO-REDUCTION"),
]


def main():
    print("=" * 96)
    print("MERGE CRITERION v3 -- controls (registry-bound; every dimension from the frozen ATOMIC)")
    print("=" * 96)
    for p in CONTROLS:
        r = report(p)
        print(f"       expected {p['expect']}: {'OK' if r['verdict'] == p['expect'] else '*** MISMATCH ***'}")
    ok = _selftest()
    print(f"\n  SELFTEST: {'PASS' if ok else 'FAIL'}")
    return 0 if ok else 1


def _by(prefix):
    for c in CONTROLS:
        if c["name"].startswith(prefix):
            return c
    raise KeyError(prefix)


def _selftest():
    ok = True
    def chk(c, m):
        nonlocal ok
        if not c:
            print(f"   [FAIL] {m}"); ok = False
    for p in CONTROLS:
        got = evaluate(p)["verdict"]
        chk(got == p["expect"], f"{p['name']}: got {got}, expected {p['expect']}")

    # F1: dimensions are NOT settleable inside a proposal -- the v2 defect that made the tool
    # strictly more expressive for an attacker than v1.
    atk = dict(_by("C4 "), dims={"_ctl_V": 1})          # v2 would have accepted this and REDUCED
    chk(evaluate(atk)["verdict"] == "NO-REDUCTION",
        "F1 REGRESSION: a proposal-supplied 'dims' must have NO effect -- the registry is the only "
        "source of dimension")
    # F3: side-padding and unbound elimination are refused
    chk(evaluate(_by("C5 "))["verdict"] == "REFUSED-INCOMPLETE", "F3: side-padding not refused")
    chk(evaluate(_by("C12"))["verdict"] == "REFUSED-INCOMPLETE", "F3: unbound elimination not refused")
    chk(evaluate(_by("C16"))["verdict"] == "REFUSED-INCOMPLETE",
        "BLOCK-8: an empty merged account must be refused, not scored as the maximal reduction")
    chk(evaluate(_by("C15"))["verdict"] == "REFUSED-INCOMPLETE",
        "F3(a) ISOLATED: an unbound elimination on a PARTICIPATING side must still be refused")
    # F6: discrete savings land on the discrete axis, never on continuous
    d13 = evaluate(_by("C13"))["delta"]
    chk(d13["discrete"] == -1 and d13["continuous"] == 0,
        f"F6: a discrete stance must be saved on the DISCRETE axis, got {d13}")
    # F5: the span is computed in both directions and the worst is the verdict
    r14 = evaluate(_by("C14"))
    chk(len(r14["readings"]) >= 2, "F5: the sensitivity span must compute more than one reading")
    chk(_ORDER[r14["verdict"]] >= _ORDER[r14["verdict_as_declared"]],
        "F5: the reported verdict must be the WORST of the span, never the favourable reading")
    # F1 again: an unregistered id can never be scored
    chk(evaluate(_by("C11"))["verdict"] == "REFUSED-INCOMPLETE", "F1: unregistered id not refused")
    # D4 (retained): posited binary relations remain reachable
    chk(evaluate(_by("C2 "))["verdict"] == "TRADE", "D4 REGRESSION: posited binary must be reachable")
    # no verdict may claim "one input"
    for v in VERDICTS.values():
        chk("one input" not in v, "a verdict string still says 'one input'")
    return ok


if __name__ == "__main__":
    raise SystemExit(main())
