#!/usr/bin/env python3
"""RAI-FINAL-BOSS -- gates the committed record. Read-only. Banks nothing. W-0.

Journal-read AND de-pinned (the twice-caught lesson): no verdict value is a pass condition;
gates assert well-formedness and record/journal consistency via dynamic needles; the blocked
stage must be DISCLOSED, not hidden; free-text quality is not mechanically certifiable.
"""
import json, sys, os, re

import rai_gate_lib as G

ROOT = os.path.dirname(os.path.abspath(__file__))
# Journal location: override with the RAI_JOURNAL env var; fall back to the
# recorded absolute path only when it actually exists (portable default).
JPATH = os.environ.get("RAI_JOURNAL") or (
    "/Users/mpg/.claude/projects/-Users-mpg-Library-Mobile-Documents-com-apple-"
    "CloudDocs-Ryans-Projects-GRUT-ResponsiveAI/7469561b-1dc7-4147-85e7-95af0652a664/"
    "subagents/workflows/wf_9f83fdcf-1df/journal.jsonl")

print("\n== A. GOVERNANCE ==")
claims, BY = G.check_governance()
for nid in ("u3_split_origin","u4_constitutive_origin"):
    G.gate(BY[nid].get("tier") == "to-derive", f"{nid} fence unmoved", "GRAPH")

print("\n== B. JOURNAL (well-formedness; no verdict value is a pass condition) ==")
res, failed = [], []
if not os.path.exists(JPATH):
    G.gate(False, f"journal not found: {JPATH} (set RAI_JOURNAL to override)")
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
            if d.get("type") == "failed":
                failed.append(d.get("key", ""))
def last(pred):
    xs=[r for r in res if pred(r)]; return xs[-1] if xs else None
recon_c = last(lambda r: "deletion_table" in r)
recon_w = last(lambda r: "arrow_test" in r)
att_c   = last(lambda r: "discharge_class" in r and "verification" in r)
syn     = last(lambda r: "clpw_final" in r)
fin     = last(lambda r: "o1_clpw" in r)
sents   = [r for r in res if "sentence" in r and "grades" in r]
hosts   = [r for r in res if "hidden_input" in r and "attack" in r]
resd    = last(lambda r: "residue_verdict" in r)
G.gate(recon_c is not None and recon_w is not None, "both reconstructions present")
G.gate(att_c is not None, "clpw attack present")
G.gate(len(failed) >= 3, f"the wiesbrock:attack refusals are ON THE RECORD ({len(failed)} failed events)")
G.gate(len(hosts) >= 2, f"double hostile ran ({len(hosts)} hostiles)")
G.gate(syn is not None and syn.get("clpw_final") and syn.get("wiesbrock_final") and syn.get("final_state"),
     f"synthesis well-formed (journal: {(syn or {}).get('clpw_final')} / {(syn or {}).get('wiesbrock_final')} / {(syn or {}).get('final_state')})")
G.gate(len(sents) == 2, "blind sentence pair present")
G.gate(fin is not None and all(fin.get(k) for k in
     ("o1_clpw","o8_1space","o14_empirical_discriminator","o15_mathematical_discriminator",
      "o17_primary_sentence","o18_hostile_sentence","o19_sentence_comparison","final_classification")),
     f"final output complete (classification: {fin.get('final_classification') if fin else None})")
G.gate(resd is not None and resd.get("residue_verdict") in ("PHYSICAL","GAUGE","INPUT","MIXED","UNDETERMINED"),
     f"residue verdict well-formed (journal: {resd.get('residue_verdict') if resd else None})")

print("\n== C. MAIN-LOOP DIFF (the blocked stage's replacement, computed here) ==")
rw = json.dumps(recon_w) if recon_w else ""
hb = " ".join(json.dumps(x) for x in hosts)
G.gate("Remark (19)" in rw or "(19)" in rw, "recon: both hsm orientations located in sources", "DIFF")
G.gate("inclusion order alone" in rw or "orientation-free" in rw,
     "recon: positivity from inclusion order alone", "DIFF")
G.gate("epsilon" in hb or "sign" in hb.lower(),
     "hostile B independently names the signed nesting datum", "DIFF")
G.gate(("hsm" in rw.lower() or "half-sided" in rw.lower()) and ("hsm" in hb.lower() or "half-sided" in hb.lower()),
     "both independent passes attribute the orientation to the half-sided clause", "DIFF")

print("\n== D. RECORD/JOURNAL CONSISTENCY (dynamic needles) ==")
rec = "RAI_FINAL_BOSS.md"
MD = G.render_record(rec)
if MD is not None:
    G.gate("[[" not in MD, "no template token", "GRAPH")
    for val, lbl in (((syn or {}).get("clpw_final"), "record states the journal's CLPW class"),
                     ((syn or {}).get("wiesbrock_final"), "record states the journal's Wiesbrock class"),
                     ((fin or {}).get("final_classification"), "record states the final classification"),
                     ((resd or {}).get("residue_verdict"), "record states the residue verdict")):
        G.gate(val is not None and (val in MD or val.replace("-", " ") in MD),
             f"{lbl} ({val})", "GRAPH")
    G.gate("classifier" in MD.lower() and ("refused" in MD.lower() or "blocked" in MD.lower()),
         "record DISCLOSES the blocked stage", "GRAPH")
    G.gate("own derivation" in MD.lower() or "campaign's own derivations" in MD.lower()
         or "OWN-DERIVATION" in MD,
         "record flags the campaign-own derivations as unverified-by-literature", "GRAPH")
else:
    print("  [ -- ] record not yet written")

p_, n_, fails_ = G.battery_summary()
print(f"\nBATTERY: {p_}/{n_}" + (f"  FAILURES: {fails_}" if fails_ else ""))
print(f"FROM JOURNAL: CLPW={(syn or {}).get('clpw_final')} WIES={(syn or {}).get('wiesbrock_final')} "
     f"STATE={(syn or {}).get('final_state')} FINAL={(fin or {}).get('final_classification')}")
print("W-0 -- reported, NOT banked. Register unmodified. Fences unmoved.")
sys.exit(1 if fails_ else 0)
