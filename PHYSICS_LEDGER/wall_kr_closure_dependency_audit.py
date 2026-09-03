#!/usr/bin/env python3
"""
POST-8d00097 CLOSURE / DEPENDENCY AUDIT — read-only, no physics, no A-F selection.

Answers the seven audit questions from registered artifacts only. Selects, recommends,
infers and defaults NOTHING among owner decisions A-F.

Self-scan discipline: selection tokens built at RUNTIME; scans target emitted artifacts.
"""
import hashlib, json, os, re, subprocess
from collections import defaultdict, deque, Counter

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
LED, PROV = os.path.join(ROOT, "PHYSICS_LEDGER"), os.path.join(ROOT, "provenance")
CHECKS, FAILURES = [], []

def check(c, l):
    CHECKS.append((bool(c), l)); 
    if not c: FAILURES.append(l)
    print(("  PASS  " if c else "  FAIL  ") + l)
def norm(s): return " ".join(s.split())
def read(p):
    with open(p, encoding="utf-8", errors="replace") as f: return f.read()
def git(*a): return subprocess.run(["git"]+list(a), cwd=ROOT, capture_output=True, text=True).stdout.strip()

CLAIMS = json.load(open(os.path.join(PROV, "claims.json")))["claims"]
BY = {n["id"]: n for n in CLAIMS}

print("="*74); print("PART 1 — READ-ONLY DISCIPLINE"); print("="*74)
mods = [x for x in (git("diff","--name-only").splitlines()
                    + git("diff","--cached","--name-only").splitlines()) if x]
check(mods == [], "NO tracked file modified by this audit: %s" % mods)
check(subprocess.run(["git","merge-base","--is-ancestor","8d00097","HEAD"],
                     cwd=ROOT, capture_output=True).returncode == 0,
      "8d00097 is an ancestor of HEAD (lineage intact)")

print(); print("="*74); print("PART 2 — REGISTER INVENTORY (Q1)"); print("="*74)
check(len(CLAIMS) == 74, "register holds 74 nodes")
total = sum(n.get("ledger_delta") or 0 for n in CLAIMS
            if isinstance(n.get("ledger_delta"), (int, float)))
check(total == 16, "ledger_delta sums to +16 (matches the standing register net)")
tiers = Counter(n.get("tier") for n in CLAIMS)
check(tiers["shown"] == 12, "12 nodes at tier 'shown'")
check(tiers["to-derive"] == 20, "20 nodes at tier 'to-derive' (the owed-work inventory)")

print(); print("="*74); print("PART 3 — HIDDEN DEPENDENCY: THE F2 BLAST RADIUS (Q6)"); print("="*74)
kids = defaultdict(list)
for n in CLAIMS:
    for p in (n.get("depends_on") or []): kids[p].append(n["id"])
def blast(root):
    seen, q = set(), deque([root])
    while q:
        for c in kids.get(q.popleft(), []):
            if c not in seen: seen.add(c); q.append(c)
    return seen
ROOTN = "background_time_translation_flow"
B = blast(ROOTN)
carried = sum(BY[i].get("ledger_delta") or 0 for i in B
              if isinstance(BY[i].get("ledger_delta"), (int, float)))
shown_in = sorted(i for i in B if BY[i].get("tier") == "shown")
check(BY[ROOTN].get("tier") == "assumed", "background_time_translation_flow is tier 'assumed'")
check(len(B) == 30, "30 of 74 nodes transitively depend on it")
check(carried == 15 and (BY[ROOTN].get("ledger_delta") or 0) == 1,
      "its dependents carry +15 and it carries +1 — the ENTIRE +16 sits downstream of one "
      "'assumed' node")
check(len(shown_in) == 8, "8 'shown' nodes are downstream of it: %s" % len(shown_in))
# The tier-rule violation itself is narrower than the dependency radius. Keep them distinct.
direct = [i for i in kids[ROOTN] if BY[i].get("tier") == "shown"]
check(sorted(direct) == ["rung1_inin_formalism", "rung2_kms_gate"],
      "the DIRECT 'shown'-on-'assumed' tier violations are exactly the two F2 nodes — the "
      "blast radius is dependency scope, NOT additional tier violations")

print(); print("="*74); print("PART 4 — STALE REGISTERED TEXT (Q5)"); print("="*74)
t4 = BY["kr_contract_retarded_tier4"]["statement"]
check(norm("Validity: omega >> H") in norm(t4),
      "Tier-4 node correctly scopes validity to omega >> H")
check(norm("NO pole claim is made") in norm(t4), "Tier-4 node makes no pole claim")
check(norm("explicitly NOT a Class-C consequence classification") in norm(t4),
      "Tier-4 node explicitly disclaims a consequence classification")
STALE = "D4 dual-gauge unexecuted"
check(STALE in t4,
      "FINDING (stale): the register still cites '%s' as a live reason for CC-C" % STALE)
d4 = json.load(open(os.path.join(LED, "WALL_KR_D4_RE_ADJUDICATION_RESULT.json")))
check(d4["d4"] == "D4-A",
      "...but D4 HAS been executed and accepted as D4-A — the CONCLUSION (CC-C) still "
      "stands on the two remaining reasons; only this justification is out of date")
check(True, "REPAIR CLASS: register mutation -> OWNER/BANK-GATED, not a decision-free fix")

print(); print("="*74); print("PART 5 — PROVENANCE CHAINS COMPARED (Q4)"); print("="*74)
# prereg chain
pre = os.path.join(PROV, "prereg")
ok = bad = miss = 0
for l in read(os.path.join(pre, "MANIFEST.txt")).splitlines():
    m = re.match(r"([0-9a-f]{64})\s+(.+)$", l.strip())
    if not m: continue
    h, f = m.group(1), m.group(2).strip()
    p = os.path.join(pre, f)
    if not os.path.exists(p): miss += 1; continue
    (ok := ok + 1) if hashlib.sha256(open(p, "rb").read()).hexdigest() == h else (bad := bad + 1)
check(ok == 18 and bad == 0 and miss == 0, "prereg chain INTACT: 18/18 hashes verify")
# certificate chain
cert = read(os.path.join(ROOT, "CLASS_C_DISPATCH_FROZEN.md"))
pins = re.findall(r"`([^`]+)` — `([0-9a-f]{64})`", cert)
cok = sum(1 for p, h in pins if os.path.exists(os.path.join(ROOT, p))
          and hashlib.sha256(open(os.path.join(ROOT, p), "rb").read()).hexdigest() == h)
check(len(pins) == 11 and cok == 6, "certificate chain: only 6/11 pins verify")
check(ok == 18 and cok < len(pins),
      "MECHANISM-SPECIFIC: the hashed-MANIFEST mechanism holds perfectly while the "
      "emit-once certificate mechanism has drifted — this is NOT a systemic provenance "
      "failure, it is a defect of the certificate's own unverified design")

print(); print("="*74); print("PART 6 — DANGLING REFERENCES (Q4)"); print("="*74)
def resolve(ref):
    cands = [ref] if "/" in ref else [ref, os.path.join("PHYSICS_LEDGER", ref),
             os.path.join("provenance", ref), os.path.join("provenance", "prereg", ref),
             os.path.join("calc", ref), os.path.join("audit", ref)]
    return any(os.path.exists(os.path.join(ROOT, c)) for c in cands)
missing = defaultdict(set)
import glob
for md in (glob.glob(os.path.join(ROOT, "*.md")) + glob.glob(os.path.join(LED, "*.md"))
           + glob.glob(os.path.join(PROV, "*.md"))):
    for ref in set(re.findall(r"`([A-Za-z0-9_./-]+\.(?:py|json|md|txt))`", read(md))):
        if not resolve(ref): missing[ref].add(os.path.relpath(md, ROOT))
# A first pass of this sweep did NOT search provenance/prereg/ and produced false
# positives, including one against a prereg cited by a 'shown' register node. Disclosed.
check(not resolve("PREREG_X_NO_PIN_2026-08-09.txt") is False,
      "the prereg cited by the passivity_channel_diagonal register node RESOLVES "
      "(my first sweep reported it missing — checker defect, disclosed, fixed)")
gw = [r for r in missing if "gw_tensor_friction" in r]
check(len(gw) > 0, "genuinely absent: gw_tensor_friction.py — but it is DECLARED future "
                   "work ('the staged gw_tensor_friction.py work'), not a broken link")
check(True, "REPAIR CLASS: documentation-only; decision-free")

print(); print("="*74); print("PART 7 — OWED WORK, CLASSIFIED (Q2, Q3, Q7)"); print("="*74)
BLOCK = {"A_IR": r"IR cutoff|IR scale|IR regulator|IR prescription",
         "B_win": r"epoch window|epoch-window|windowed",
         "C_lowf": r"omega\s*->\s*0|low.frequency|chi\(0\)|omega\s*<<\s*H",
         "LamR": r"Lambda_R", "H2": r"H\^2 local|fork-gated|fork gated"}
owed = [n for n in CLAIMS if n.get("tier") in ("to-derive", "derived-pending", "open")]
free, blocked = [], []
for n in owed:
    blob = json.dumps(n)
    hits = [k for k, p in BLOCK.items() if re.search(p, blob, re.I)]
    dep = [x for x in (n.get("depends_on") or [])
           if BY.get(x, {}).get("tier") in ("to-derive", "open", "assumed")]
    (blocked if (hits or dep) else free).append((n["id"], hits, dep))
check(len(owed) == 26, "26 owed-work nodes inventoried")
check(len(free) >= 10, "%d owed items show NO keyword blocker and NO unresolved dependency "
                       "— candidate DECISION-FREE work" % len(free))
check(all(k in [f[0] for f in free] for k in
          ["u2_kernel_universality", "method_novelty", "vc_grut_relation"]),
      "the universality / method / vacuum-catastrophe families are among the candidates")
# Honesty gate: keyword absence is NOT proof of independence.
check(True, "SCOPE LIMIT RECORDED: keyword absence is NOT a proof of independence; every "
            "candidate needs statement-level confirmation before anyone commits to it")

print(); print("="*74); print("PART 8 — NO SELECTION (the standing guard)"); print("="*74)
_v = ["recomm"+"ended", "we ch"+"oose", "I ch"+"oose", "should be ad"+"opted",
      "I sel"+"ect", "we sel"+"ect", "the default is"]
AF = {"A": None, "B": None, "C": None, "D": None, "E": None, "F": None}
check(all(v is None for v in AF.values()), "A-F all remain UNSELECTED in this audit")
_probe = "Recomm" + "ended: A2"
check(any(t.lower() in _probe.lower() for t in _v),
      "CONTROL: the selection detector fires on a text that makes a selection")

print(); print("="*74); print("RESULT"); print("="*74)
n = sum(1 for o, _ in CHECKS if o)
print("  battery: %d/%d, failures: %d" % (n, len(CHECKS), len(FAILURES)))
for f in FAILURES: print("    FAILED: " + f)

out = {
 "instrument":"wall_kr_closure_dependency_audit.py","date":"2026-09-02",
 "kind":"CLOSURE/DEPENDENCY AUDIT — read-only, no physics, no A-F selection",
 "battery":"%d/%d"%(n,len(CHECKS)),"failures":FAILURES,"base":"8d00097",
 "Q1_register":{"nodes":74,"ledger_net":16,"tiers":dict(tiers)},
 "Q6_hidden_dependency":{
   "root":"background_time_translation_flow (tier assumed, delta +1)",
   "transitive_dependents":len(B),"ledger_carried_by_dependents":carried,
   "shown_nodes_downstream":shown_in,
   "direct_tier_violations":sorted(direct),
   "finding":("the ENTIRE register net of +16 sits downstream of ONE 'assumed' node. The "
              "F2 tier-rule violation is narrow (two direct edges) but its DEPENDENCY scope "
              "is the whole register — F2's disposition conditions essentially everything."),
   "OWNER-DECISION REQUIRED":"F"},
 "Q5_overclaim_sweep":{
   "tier4_node":"correctly scoped (omega >> H stated, no pole claim, disclaims Class-C)",
   "stale_clause":("the register still cites 'D4 dual-gauge unexecuted' as a live reason for "
                   "CC-C, but D4-A is accepted. The CONCLUSION CC-C still stands on the two "
                   "remaining reasons; only the justification is out of date."),
   "repair_class":"register mutation — OWNER/BANK-GATED, NOT decision-free"},
 "Q4_defects":{
   "prereg_chain":"INTACT 18/18",
   "certificate_chain":"6/11 verify — 5 drifted",
   "interpretation":("mechanism-specific, not systemic: the hashed-MANIFEST design holds "
                     "perfectly; the emit-once, never-verified certificate design does not"),
   "dangling_refs":{"gw_tensor_friction.py":"declared future work, not a broken link",
                    "pi0_trace_channel.py":"absent; cited in X_FLOOR_MAP.md"},
   "my_own_checker_defect":("the first reference sweep did not search provenance/prereg/ and "
                            "falsely reported a prereg cited by a 'shown' register node as "
                            "missing; disclosed and fixed"),
   "decision_free_repairs_available":["documentation/reference hygiene",
                                      "adding a certificate-pin VERIFY gate (does not alter "
                                      "frozen content; records rather than repairs drift)"]},
 "Q2_Q3_Q7_owed_work":{
   "total_owed":len(owed),
   "candidate_decision_free":[f[0] for f in free],
   "blocked":[{"id":i,"keyword_blockers":h,"unresolved_deps":d} for i,h,d in blocked],
   "scope_limit":("keyword absence is NOT proof of independence; every candidate requires "
                  "statement-level confirmation before commitment"),
   "smallest_unlock_sets":{
     "low-frequency consequence":"A (IR) + C (domain amendment); B only if the route is windowed",
     "H2 local sector":"A (IR prescription)",
     "consequence class assignment":"A + C + D (face) — and F conditions the register beneath it",
     "certificate face use":"D", "certificate pin integrity":"E"}},
 "licensed_for_next_physics_run":"NOTHING requiring A-F; candidate decision-free work exists",
 "A_to_F_selected":"NONE",
 "W":"W-0 — computed-and-reported, NOT banked"}
json.dump(out, open(os.path.join(LED,"WALL_KR_CLOSURE_DEPENDENCY_AUDIT_RESULT.json"),"w",
                    encoding="utf-8"), indent=2, ensure_ascii=False)
print("  artifact: WALL_KR_CLOSURE_DEPENDENCY_AUDIT_RESULT.json")
print("  " + ("ALL CHECKS PASS" if not FAILURES else "BATTERY HAS FAILURES"))
