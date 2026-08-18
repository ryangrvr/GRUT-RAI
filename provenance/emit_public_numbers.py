#!/usr/bin/env python3
"""emit_public_numbers: the ONE place any count in the public document comes from.

THE ONE-NUMBER RULE (overseer, 2026-08-12): no count is ever typed into prose. Every count the
public document uses is emitted by this script from the register on a stated date, and included
verbatim. The rule is a prohibition on the BODY, not an appendix convention -- and it is only real
if a script enforces it, which is what `test_public_numbers.py` does.

Run:  python3 emit_public_numbers.py            print the dated block
      python3 emit_public_numbers.py --write    write it to ../PUBLIC_NUMBERS.md
      python3 emit_public_numbers.py --check    regenerate and diff against the written block

The emitted block deliberately contains NO prose interpretation. It is counts and nothing else, so
that a reader can diff it against a fresh run without reading around an argument.
"""
import json
import os
import re
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
OUT = os.path.join(ROOT, "PUBLIC_NUMBERS.md")

# The date is an ARGUMENT, never `today` -- a block that silently re-dates itself on every run
# cannot be diffed, and "generated on a stated date" is the property the rule needs.
STAMP_DATE = "2026-08-12"
# Date split (2026-08-17 pre-screen ruling): the correction record is a frozen historical
# stamp; the byline and completeness line are living wave stamps. One shared token let the
# banner mis-date the Part-I correction.
CORRECTION_DATE = "2026-08-14"   # the Part-I correction arc (register-first, then prose)
WAVE_DATE = "2026-08-18"         # bumped at the close of every wave

# The collected-test count is a STAMPED CONSTANT, not a live collection.
# WHY (found by the guard on its first run): the emitter originally shelled out to pytest to count
# tests -- so the drift check ran pytest FROM INSIDE pytest, and adding the very test that verifies
# this block changed the number the block asserts. A number-emitter that recurses through its own
# verifier is not a stable reference. The constant is enforced against a real collection by
# test_public_numbers.py::test_the_stamped_test_count_is_true, so it cannot silently rot.
STAMPED_TEST_COUNT = 213


def _load():
    with open(os.path.join(HERE, "claims.json")) as f:
        return json.load(f)["claims"]



def _empty_tier_row(tier):
    """A tier with no members still gets a row. `derived` empty is the document's headline; any
    other tier emptying is a fact the appendix must show rather than hide, so the text is
    parameterized rather than hard-coded to one tier's story."""
    note = ("*no claim in the register holds this tier — the document's headline result*"
            if tier == "derived" else
            f"*no claim in the register holds this tier*")
    return f"| *(none)* | **{tier}** | — | {note} |"


def register_table():
    """Appendix A, generated: every framework-scope claim, its tier, its ledger delta, and the
    first sentence of its statement. Generated so the appendix cannot drift from the register;
    a reader wanting the full text reads claims.json, which this table indexes."""
    with open(os.path.join(HERE, "claims.json")) as f:
        cl = json.load(f)["claims"]
    grut = [c for c in cl if c.get("ledger_scope", "grut") == "grut"]
    order = {"shown": 0, "derived": 1, "derived-pending": 2, "assumed": 3, "to-derive": 4}
    grut.sort(key=lambda c: (order.get(c.get("tier"), 9), c["id"]))
    rows = ["| claim | tier | ledger | statement (opening) |",
            "|---|---|---|---|"]
    empty = [t for t in order if not any(g.get("tier") == t for g in grut)]
    seen_tiers = set()
    for c in grut:
        # THE EMPTY TIER GETS A ROW. An appendix ordered by tier that silently omits the tier
        # with no members hides the document's own headline result (figure lens, 2026-08-17).
        t = c.get("tier")
        for missing in [x for x in empty if order[x] < order.get(t, 9) and x not in seen_tiers]:
            rows.append(_empty_tier_row(missing))
            seen_tiers.add(missing)
        seen_tiers.add(t)
        st = re.split(r"(?<=[.])\s", c.get("statement", ""), 1)[0].strip()
        st = st.replace("|", "/")
        if len(st) > 150:
            cut = st[:150]
            sp = cut.rfind(" ")
            st = (cut[:sp] if sp > 60 else cut).rstrip(" ,;:(-") + " …"
            if st.count("(") > st.count(")"):
                st += ")"
        d = c.get("ledger_delta", 0)
        d = f"+{d}" if isinstance(d, int) and d > 0 else str(d)
        rows.append(f"| `{c['id']}` | {c.get('tier')} | {d} | {st} |")
    # trailing empty tiers too: the first version's loop only fired when a LATER populated tier
    # arrived, so an emptied last tier would have vanished from an appendix ordered by tier --
    # the same omission class the empty-row fix was written for (re-screen, 2026-08-17).
    for missing in [x for x in empty if x not in seen_tiers]:
        rows.append(_empty_tier_row(missing))
    return "\n".join(rows)


def calc_index():
    """Appendix E, generated: the calculations, and which are cited by the register."""
    with open(os.path.join(HERE, "claims.json")) as f:
        raw = f.read()
    calcdir = os.path.join(ROOT, "calc")
    names = sorted(f for f in os.listdir(calcdir) if f.endswith(".py"))
    rows = ["| calculation | cited by the register |", "|---|---|"]
    for n in names:
        cited = "yes" if f"calc/{n}" in raw else "no (support or superseded)"
        rows.append(f"| `calc/{n}` | {cited} |")
    return "\n".join(rows)

def numbers():
    cl = _load()
    grut = [c for c in cl if c.get("ledger_scope", "grut") == "grut"]
    cluster = [c for c in cl if c.get("ledger_scope") == "vacuum-cluster"]

    def net(rows):
        return sum(c.get("ledger_delta", 0) for c in rows
                   if isinstance(c.get("ledger_delta"), int)
                   and not isinstance(c.get("ledger_delta"), bool))

    tiers = {}
    for c in grut:
        tiers[c["tier"]] = tiers.get(c["tier"], 0) + 1

    waivers = [(c["id"], c["ledger_delta"]) for c in grut
               if c.get("laundering_ok") and isinstance(c.get("ledger_delta"), int)
               and c["ledger_delta"] > 0]

    with open(os.path.join(HERE, "sources.json")) as f:
        srcs = [k for k in json.load(f) if not k.startswith("_")]

    calcs = sorted(f for f in os.listdir(os.path.join(ROOT, "calc"))
                   if f.endswith(".py") and not f.startswith("_"))
    tests = sorted(f for f in os.listdir(HERE)
                   if f.startswith("test_") and f.endswith(".py"))

    n_tests = STAMPED_TEST_COUNT

    dispositions = {}
    for c in grut:
        if c.get("disposition"):
            dispositions[c["disposition"]] = dispositions.get(c["disposition"], 0) + 1

    # ---- the B0.2 "specialist" audit, computed live (never a remembered figure) ----
    # The pattern is CASE-INSENSITIVE and the reason is on the record: the audit's first run used
    # a character class on the first letter only, silently dropped every all-caps SPECIALIST, and
    # undercounted by 8 -- six of which were the class that reads as external validation.
    spec_pat = re.compile(r"specialists?", re.I)

    # ANNOTATION BLOCKS ARE EXCLUDED FROM THE COUNT, and the reason is recorded because the
    # problem is genuinely funny and genuinely real: the 2026-08-12 annotations that DOCUMENT the
    # audited vocabulary necessarily CONTAIN the audited words, so annotating inflated the count
    # the annotations exist to explain (49 -> 58). The exclusion is narrow -- only text inside a
    # dated, uniquely-marked AUTHORITY-VOCABULARY ANNOTATION block -- and BOTH numbers are
    # emitted, so the exclusion cannot hide anything: a reader sees the register's own uses and
    # the commentary about them as separate figures.
    ANNOT = re.compile(r"\[AUTHORITY-VOCABULARY ANNOTATION.*?vocabulary drift is itself the "
                       r"finding\.\]", re.S)

    def _blob(c):
        return ANNOT.sub("", json.dumps(c))

    spec_nodes = {c["id"]: len(spec_pat.findall(_blob(c))) for c in cl
                  if spec_pat.search(_blob(c))}
    spec_raw_incl_annotations = sum(len(spec_pat.findall(json.dumps(c))) for c in cl)
    # The class-B records -- phrased as a pass having RUN -- identified by their own date/verb
    # markers. Recomputed here rather than carried as a constant.
    ran_markers = re.compile(
        r"specialist\s+confirmed|specialist-corrected|specialist\s+20\d\d-\d\d-\d\d|"
        r"by (?:an? )?[\w-]*\s*specialist|\(specialist[,)]|specialist\s*\(|specialist,\s*(?:favorable|"
        r"lean)|external specialist|independent specialist|verified specialist|"
        r"the specialist (?:explicitly|sharpened|declines)|answered by the specialist|"
        r"specialist-teed|banked \w+ specialist", re.I)
    ran_nodes = sorted({c["id"] for c in cl if ran_markers.search(json.dumps(c))})
    # The analyst classification, tallied here and CROSS-CHECKED against the live scan. A
    # disagreement REFUSES rather than reporting -- the first run's undercount survived precisely
    # because nothing compared a classification against an independent count of the same thing.
    with open(os.path.join(HERE, "specialist_audit.json")) as f:
        aud = json.load(f)["nodes"]
    senses = {k: sum(v[k] for v in aud.values()) for k in ("A", "B", "C", "D")}
    if sum(senses.values()) != sum(spec_nodes.values()):
        raise SystemExit(
            f"SPECIALIST AUDIT REFUSES: classification totals {sum(senses.values())} but a live "
            f"case-insensitive scan of the register finds {sum(spec_nodes.values())}. Reclassify "
            f"the difference -- do not adjust either number to match the other.")
    if set(aud) != set(spec_nodes):
        raise SystemExit(f"SPECIALIST AUDIT REFUSES: node sets differ. "
                         f"unclassified={sorted(set(spec_nodes) - set(aud))}, "
                         f"phantom={sorted(set(aud) - set(spec_nodes))}")

    # The six all-caps records of the single 2026-06-25 "four questions" session.
    caps_pat = re.compile(r"SPECIALIST[ -](?:CONFIRMED|CORRECTED|2026-06-25)|SPECIALIST \(Q\d\)")
    caps_occurrences = sum(len(caps_pat.findall(json.dumps(c))) for c in cl)
    # The recomputed ISW cross-channel significance, read from the register rather than typed:
    # this is THIS program's own recomputation (the retired 32-sigma anchor), so it falls under
    # neither of the document's two quoting exceptions and must be a token.
    isw = re.search(r"N\(1\) ~ ([0-9.]+)", json.dumps(cl))
    isw_sigma = isw.group(1) if isw else None
    isw_c = re.search(r"computed ([0-9.]+) central", json.dumps(cl))
    isw_central = isw_c.group(1) if isw_c else None

    caps_2026_06_25 = sorted({c["id"] for c in cl
                              if re.search(r"SPECIALIST[ -](?:CONFIRMED|CORRECTED|2026-06-25)",
                                           json.dumps(c))
                              or re.search(r"SPECIALIST \(Q\d\)", json.dumps(c))})

    # The interior family's computed edge and its empirical neighbours, read from the register
    # rather than typed (Part III.2's numbers; same rationale as the ISW pair above).
    xu = re.search(r"x < ~([0-9.]+) \(central-inputs", json.dumps(cl))
    x_upper = xu.group(1) if xu else None
    mu = re.search(r"mu-1 <= ~([0-9.]+)\)", json.dumps(cl))
    mu_allowance = mu.group(1) if mu else None
    ds = re.search(r"DESI Sigma0 ~([0-9.]+)sigma \(independent", json.dumps(cl))
    desi_sigma0 = ds.group(1) if ds else None
    xg = re.search(r"interior-viability claim above x ~ ([0-9.]+)", json.dumps(cl))
    x_gate = xg.group(1) if xg else None

    # "overseer" in the REGISTER, scope declared so the figure cannot drift: a typed
    # count of this word went stale once (2026-08-18) and its correction manufactured a
    # second error. Emitted, register-scope, occurrences not lines.
    n_overseer_register = len(re.findall(r"overseer", json.dumps(cl), re.I))

    with open(os.path.join(HERE, "construction_pressure.json")) as f:
        pressure = json.load(f)["occasions"]

    return dict(n_pressure_removals=len(pressure), total=len(cl), n_grut=len(grut), n_cluster=len(cluster),
                net_grut=net(grut), net_cluster=net(cluster), tiers=tiers,
                waivers=waivers, waived_total=sum(d for _, d in waivers),
                n_sources=len(srcs), n_calcs=len(calcs), n_test_files=len(tests),
                n_tests=n_tests, dispositions=dispositions,
                spec_total=sum(spec_nodes.values()), spec_nodes=len(spec_nodes),
                spec_raw_incl_annotations=spec_raw_incl_annotations,
                spec_nodes_detail=spec_nodes,
                spec_ran_nodes=ran_nodes,
                spec_2026_06_25_nodes=caps_2026_06_25,
                n_spec_2026_06_25_nodes=len(caps_2026_06_25),
                n_spec_2026_06_25_occurrences=caps_occurrences,
                isw_sigma=isw_sigma, isw_central=isw_central,
                x_upper=x_upper, mu_allowance=mu_allowance, desi_sigma0=desi_sigma0,
                n_overseer_register=n_overseer_register,
                x_gate=x_gate,
                spec_A=senses["A"], spec_B=senses["B"], spec_C=senses["C"], spec_D=senses["D"],
                spec_audit=aud)


def block():
    n = numbers()
    L = []
    L.append(f"<!-- GENERATED by provenance/emit_public_numbers.py on {STAMP_DATE}. "
             f"DO NOT EDIT BY HAND. Regenerate with --write; verify with --check. -->")
    L.append(f"## Register counts, generated {STAMP_DATE}\n")
    L.append("| quantity | value |")
    L.append("|---|---|")
    L.append(f"| claims in `claims.json` (all scopes) | **{n['total']}** |")
    L.append(f"| — of those, GRUT-scope | **{n['n_grut']}** |")
    L.append(f"| — of those, vacuum-cluster scope | **{n['n_cluster']}** |")
    L.append(f"| net underived-input ledger, GRUT scope | **+{n['net_grut']}** |")
    L.append(f"| net underived-input ledger, vacuum-cluster scope | **+{n['net_cluster']}** |")
    L.append(f"| of the GRUT net, carried behind declared waivers | **+{n['waived_total']}** "
             f"across {len(n['waivers'])} claims |")
    L.append(f"| primary sources in `sources.json` | **{n['n_sources']}** |")
    L.append(f"| calculation files in `calc/` | **{n['n_calcs']}** |")
    L.append(f"| test files in `provenance/` | **{n['n_test_files']}** |")
    if n["n_tests"] is not None:
        L.append(f"| tests collected | **{n['n_tests']}** |")
    L.append("")
    L.append(f"### Tier histogram, GRUT scope ({n['n_grut']} claims)\n")
    L.append("| tier | count |")
    L.append("|---|---|")
    for t in ("shown", "derived", "derived-pending", "assumed", "to-derive"):
        L.append(f"| `{t}` | **{n['tiers'].get(t, 0)}** |")
    other = {k: v for k, v in n["tiers"].items()
             if k not in ("shown", "derived", "derived-pending", "assumed", "to-derive")}
    for k, v in sorted(other.items()):
        L.append(f"| `{k}` | **{v}** |")
    L.append("")
    L.append("### Waiver itemization\n")
    L.append("| claim | ledger_delta |")
    L.append("|---|---|")
    for cid, d in sorted(n["waivers"]):
        L.append(f"| `{cid}` | **+{d}** |")
    L.append("")
    L.append("### The \"specialist\" audit (B0.2)\n")
    L.append("| quantity | value |")
    L.append("|---|---|")
    L.append(f"| occurrences of specialist/specialists/SPECIALIST in `claims.json` | "
             f"**{n['spec_total']}** |")
    L.append(f"| claims containing at least one | **{n['spec_nodes']}** of {n['total']} |")
    L.append(f"| (same, counting the 2026-08-12 annotation blocks that document them) | "
             f"**{n['spec_raw_incl_annotations']}** |")
    L.append(f"| sense A — prospective/reserved (a future outside expert) | **{n['spec_A']}** |")
    L.append(f"| sense B — a pass that RAN, banked in the voice of an authority | "
             f"**{n['spec_B']}** |")
    L.append(f"| sense C — collective/generic | **{n['spec_C']}** |")
    L.append(f"| sense D — filename reference | **{n['spec_D']}** |")
    L.append(f"| — of sense B, all-caps records of the single 2026-06-25 session | "
             f"**{n['n_spec_2026_06_25_nodes']}** nodes |")
    L.append("")
    L.append("| claim | A | B | C | D |")
    L.append("|---|---|---|---|---|")
    for cid, v in sorted(n["spec_audit"].items(), key=lambda kv: (-sum(kv[1].values()), kv[0])):
        L.append(f"| `{cid}` | {v['A']} | {v['B']} | {v['C']} | {v['D']} |")
    L.append("")
    if n["dispositions"]:
        L.append("### Closed dispositions, GRUT scope\n")
        L.append("| disposition | count |")
        L.append("|---|---|")
        for k, v in sorted(n["dispositions"].items()):
            L.append(f"| `{k}` | **{v}** |")
        L.append("")
    return "\n".join(L)


def main():
    b = block()
    if "--check" in sys.argv:
        on_disk = open(OUT).read() if os.path.exists(OUT) else ""
        if on_disk.strip() != b.strip():
            print("DRIFT: PUBLIC_NUMBERS.md does not match a fresh run. Regenerate with --write.")
            return 1
        print("public numbers match the register (no drift).")
        return 0
    if "--write" in sys.argv:
        open(OUT, "w").write(b + "\n")
        print(f"wrote {OUT}")
        return 0
    print(b)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
