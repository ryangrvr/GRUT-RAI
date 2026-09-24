#!/usr/bin/env python3
"""RAI-DIALECTIC -- BUILDER/WRECKER CHAMBER. Gates the committed record.

Read-only. Banks nothing. W-0. Register untouched; u3/u4 fences unmoved.

DESIGN (the twice-caught lesson applied from the start): every chamber verdict is READ FROM
THE WORKFLOW JOURNAL at gate time and NO verdict value is a pass condition. Gates assert
(i) well-formedness of each agent result, (ii) that the record states WHATEVER the journal
says, and (iii) live recomputation of the two mechanically checkable corpus claims. A
different chamber outcome would change the record, not the battery. Free-text quality is not
mechanically certifiable and is not certified.
"""
import json, subprocess, sys, os, re

import rai_gate_lib as G

ROOT = os.path.dirname(os.path.abspath(__file__))
# Journal location: override with the RAI_DIALECTIC_JOURNAL env var; fall back to
# the recorded absolute path only when it actually exists (portable default).
JPATH = os.environ.get("RAI_DIALECTIC_JOURNAL") or (
    "/Users/mpg/.claude/projects/-Users-mpg-Library-Mobile-Documents-com-apple-"
    "CloudDocs-Ryans-Projects-GRUT-ResponsiveAI/7469561b-1dc7-4147-85e7-95af0652a664/"
    "subagents/workflows/wf_3215b415-fe5/journal.jsonl")

gate = G.gate
read = G.read

print("\n== A. GOVERNANCE ==")
claims, BY = G.check_governance()

print("\n== B. CHAMBER JOURNAL (well-formedness only; no verdict is a pass condition) ==")
res = []
if not os.path.exists(JPATH):
    G.gate(False, f"journal not found: {JPATH} (set RAI_DIALECTIC_JOURNAL to override)")
else:
    with open(JPATH, encoding="utf-8") as f:
        for line in f:
            if not line.strip():
                continue
            try:
                d = json.loads(line)
            except json.JSONDecodeError as e:
                G.gate(False, f"malformed journal line skipped: {e}")
                continue
            if d.get("type") == "result" and isinstance(d.get("result"), dict):
                res.append(d["result"])
turns = [r for r in res if "convergence_signal" in r]
outs  = [r for r in res if "strongest_hidden_assumption" in r]
sas   = [r for r in res if "strongest_wrongness" in r]
fins  = [r for r in res if "s1_survivor" in r]
G.gate(len(turns) >= 6, f"blind round-1 pair + dialectic rounds exist ({len(turns)} turns)")
SIGS = [t.get("convergence_signal") for t in turns]
G.gate(all(s in ("CONTINUE","AGREEMENT","CONDITIONAL-AGREEMENT","IRREDUCIBLE-DISAGREEMENT","COLLAPSE")
         for s in SIGS), f"all signals well-formed (sequence: {SIGS} -- reported, not a pass condition)")
changes = sum(1 for t in turns if (t.get("position_changes") or "").strip().upper() not in ("","NONE")
              and "NONE (" not in (t.get("position_changes") or ""))
G.gate(changes >= 2, f"belief revision actually occurred ({changes} turns carry V-format changes)")
G.gate(len(outs) == 1 and outs[0].get("verdict") in ("GENUINE-CONVERGENCE","MUTUAL-REINFORCEMENT","MIXED"),
     f"outsider ran, blinded, well-formed (verdict: {outs[0].get('verdict') if outs else 'MISSING'})")
G.gate(len(sas) == 2 and all(s.get("strongest_wrongness") for s in sas),
     "both self-attacks exist and filled the wrongness field")
F = fins[0] if fins else {}
CONV = F.get("convergence_class"); GRUT = F.get("s8_grut_status")
G.gate(CONV in ("A-AGREEMENT","B-CONDITIONAL-AGREEMENT","C-IRREDUCIBLE-DISAGREEMENT","D-COLLAPSE"),
     f"final synthesis convergence class well-formed (journal: {CONV})")
G.gate(GRUT in ("FOUNDATIONAL","EMERGENT","EFFECTIVE","PARTIAL","REFUTED","MALFORMED",
              "IRRELEVANT-TO-FINAL-STRUCTURE","UNDETERMINED"),
     f"GRUT status well-formed (journal: {GRUT})")
G.gate(all(F.get(k) for k in ("s1_survivor","x1_smallest_unremovable","x2_what_would_falsify_it",
                            "x3_if_grut_disappeared","s10_gorilla","s12_next_test")),
     "XVII/XVIII required fields all present (content not value-gated)")

print("\n== C. THE TWO MECHANICALLY CHECKABLE CORPUS CLAIMS (recomputed live) ==")
gg = subprocess.run(["git","-C",ROOT,"grep","-l","ordinary input"],capture_output=True,text=True)
G.gate(gg.stdout.strip() == "" and gg.returncode == 1,
     "'ordinary input' occurs in ZERO committed files -- the endgame predicate was unfrozen",
     "RECOMPUTE")
pm = read("POSTULATE_MAP.md")
G.gate("The Born measure" in pm and "laundering" in pm,
     "Bin 1 carries the Born measure + the laundering doctrine (the preload and the unsorted door)",
     "QUOTE")

print("\n== D. RECORD/JOURNAL CONSISTENCY (dynamic needles) ==")
rec = "RAI_DIALECTIC_CHAMBER.md"
MD = G.render_record(rec)
if MD is not None:
    G.gate("[[" not in MD, "no template token", "GRAPH")
    for val, lbl in ((CONV, "record states the journal's convergence class"),
                     (GRUT, "record states the journal's GRUT status"),
                     (outs[0].get("verdict") if outs else None, "record states the outsider verdict")):
        # match on the value with hyphens or spaces (record renders 'B — CONDITIONAL AGREEMENT')
        ok = val is not None and (val in MD or val.replace("-", " ") in MD
                                  or val.split("-",1)[-1].replace("-"," ") in MD)
        G.gate(ok, f"{lbl} ({val})", "GRAPH")
    G.gate("frame" in MD.lower() and "calibration" in MD.lower(),
         "record carries the self-conviction (frame-entailed null, missing calibration) prominently",
         "GRAPH")
    G.gate("Born measure" in MD and "CLPW" in MD, "record carries both unopened doors", "GRAPH")
    G.gate("SUPPORTED" in MD and ("capped" in MD.lower()),
         "record carries the SUPPORTED cap on the differential record", "GRAPH")
else:
    print("  [ -- ] record not yet written")

p_, n_, fails_ = G.battery_summary()
print(f"\nBATTERY: {p_}/{n_}" + (f"  FAILURES: {fails_}" if fails_ else ""))
print(f"CONVERGENCE (from journal): {CONV} | GRUT (from journal): {GRUT}")
print("W-0 -- chamber verdicts reported, NOT banked. Register unmodified. Fences unmoved.")
sys.exit(1 if fails_ else 0)
