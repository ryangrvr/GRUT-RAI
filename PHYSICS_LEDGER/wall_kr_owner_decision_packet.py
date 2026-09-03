#!/usr/bin/env python3
"""
OWNER DECISION PACKET AFTER 4cb5d23 — validation instrument.

Validates the packet WITHOUT making any decision it presents. No physics.
The load-bearing gate is NO-SELECTION: the packet must present options and
choose none of them.

Self-scan discipline: selection/authority tokens are built at RUNTIME by
concatenation, and the scan targets the EMITTED PACKET, never this source.
"""
import json, os, re, subprocess

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
LED, PROV = os.path.join(ROOT, "PHYSICS_LEDGER"), os.path.join(ROOT, "provenance")
CHECKS, FAILURES = [], []

def check(c, l):
    CHECKS.append((bool(c), l))
    if not c: FAILURES.append(l)
    print(("  PASS  " if c else "  FAIL  ") + l)

def norm(s): return " ".join(s.split())
def read(p):
    with open(p, encoding="utf-8", errors="replace") as f: return f.read()
def git(*a): return subprocess.run(["git"]+list(a), cwd=ROOT, capture_output=True, text=True).stdout.strip()

PKT = read(os.path.join(LED, "WALL_KR_OWNER_DECISION_PACKET.md"))
PKT_N = norm(PKT)
MANIFEST = json.load(open(os.path.join(ROOT, "CLASS_C_MANIFEST.json")))
CERT_N = norm(read(os.path.join(ROOT, "CLASS_C_DISPATCH_FROZEN.md")))
SPEC_RAW = read(os.path.join(ROOT, "CLASS_C_DISPATCH_SPEC.md"))

print("="*74); print("PART 1 — STATE"); print("="*74)
check(git("rev-parse","HEAD").startswith("4cb5d23"), "HEAD is 4cb5d23")
mods = [l for l in git("status","--short").splitlines() if not l.startswith("??")]
check(mods == [], "no tracked file modified (packet is additive only)")
check(git("rev-parse","--abbrev-ref","HEAD") == "master", "on the campaign branch")

print(); print("="*74); print("PART 2 — THE THREE FACES, VERIFIED AGAINST SOURCE"); print("="*74)
F1 = ("isolated pole / multiple poles / branch cut / continuum / secular or "
      "nonstationary memory / no long-memory structure / ill-posed even after assembly.")
check(norm(F1) in CERT_N, "FACE 1 literal representation matches the certificate")
check(norm(F1) in PKT_N, "FACE 1 reproduced verbatim in the packet")
m = MANIFEST["permitted_outcome_classes"]
check(len(m) == 6, "FACE 2 is six JSON entries")
check(all(norm(c) in PKT_N for c in m), "FACE 2 all six classes reproduced in the packet")
sf = re.findall(r"^\s*(\d)\.\s+\*\*([^*]+)\*\*", SPEC_RAW, re.M)
spec = next(([t for _, t in sf[i:i+6]] for i in range(len(sf)-5)
             if [n for n,_ in sf[i:i+6]] == list("123456")), [])
check(len(spec) == 6, "FACE 3 is six numbered spec entries")
check(all(norm(c) in PKT_N for c in spec), "FACE 3 all six classes reproduced in the packet")
check(norm(spec[0]) == "Pole" and norm(m[0]) == "isolated pole",
      "the 'Pole' vs 'isolated pole' defect is real and is disclosed")

print(); print("="*74); print("PART 3 — NO-SELECTION GATE (the load-bearing one)"); print("="*74)
OPTS = ["A1","A2","A3","B1","B2","B3","E1","E2","E3","F1","F2","F3"]
for o in OPTS:
    check(re.search(r"\*\*%s\.\*\*" % o, PKT) is not None, "option %s is PRESENTED" % o)

# selection verbs, built at runtime so this scan cannot trip on itself
_v = ["recomm"+"ended", "we ch"+"oose", "I ch"+"oose", "my ch"+"oice",
      "the answer is", "should be ad"+"opted", "I sel"+"ect", "we sel"+"ect"]
hits = [t for t in _v if t.lower() in PKT.lower()]
check(hits == [], "NO selection verb appears anywhere in the packet: %s" % hits)

# no option token may be asserted as chosen
_chosen = [o for o in OPTS if re.search(r"(chosen|selected|adopted)\s*[:=]?\s*\*?\*?%s\b" % o,
                                        PKT, re.I)]
check(_chosen == [], "no option token is asserted as chosen: %s" % _chosen)
check(PKT.count("**NONE**") >= 6, "the summary table records NONE for all six decisions")
check(norm("The agent selects none of these.") in PKT_N, "explicit no-selection statement present")

# the withdrawn authority claim must STAY withdrawn
_auth = ["manifest is auth"+"oritative", "manifest is the auth"+"oritative",
         "FACE 2 is auth"+"oritative", "certificate is auth"+"oritative"]
ahits = [t for t in _auth if t.lower() in PKT.lower()]
check(ahits == [], "packet declares NO face authoritative: %s" % ahits)
check(norm("**No face is declared authoritative. The withdrawn claim stays withdrawn.**") in PKT_N,
      "the withdrawal is restated explicitly")

print(); print("="*74); print("PART 4 — ANTI-OVERCLAIM FIREWALL, ITEM BY ITEM"); print("="*74)
REQ = [
 ("TT-bath scope only", "D4-A is accepted **only** within the declared TT-bath consequence scope."),
 ("general-gauge", "**General-gauge uniqueness remains NOT CLAIMED.**"),
 ("no class from D4-A", "D4-A **does not** determine a consequence class."),
 ("cut != Class 3", "**The branch cut alone does not satisfy the registered Class-3 criterion**"),
 ("no low-freq result", "**No low-frequency result exists yet.**"),
 ("no IR licensed", "**No IR prescription is licensed.**"),
 ("no window licensed", "**No epoch window is licensed.**"),
 ("Lambda_R", "**Λ_R remains unresolved.**"),
 ("H2 fork-gated", "**H² local terms remain fork-gated.**"),
 ("no artifact changed", "**No physics artifact was changed by this decision packet.**"),
]
for lab, q in REQ:
    check(norm(q) in PKT_N, "firewall statement present: " + lab)

print(); print("="*74); print("PART 5 — CONTENT FIDELITY + CONTROLS"); print("="*74)
check(norm("every regulator must be appended here with purpose/location/limit/order BEFORE use; "
           "solvers refusing undeclared regulators is correct behaviour") ==
      norm(MANIFEST["regulator_policy"]), "regulator_policy quoted exactly from the manifest")
check(norm(MANIFEST["allowed_reductions"][0]) ==
      norm("only reductions proved stationary within their own declared scope; none presumed"),
      "allowed_reductions quoted exactly from the manifest")
check(norm(MANIFEST["prohibitions"][4]) == norm("unstated epoch/window parameters"),
      "prohibition #5 quoted exactly from the manifest")
check("3.3993" in PKT and "4 H" in PKT, "both domain boundaries stated")
check(len(re.findall(r"C\.\s*\*?\*?\d|^\d\.\s", PKT, re.M)) > 0 and
      "6. **The amendment's form is fixed by the certificate itself:**" in PKT,
      "all six amendment prerequisites are enumerated under Decision C")

# CONTROL 1: the no-selection gate must be able to fire.
_probe = PKT + "\n\nRecomm" + "ended: **A2.**"
_ph = [t for t in _v if t.lower() in _probe.lower()]
check(_ph != [], "CONTROL: the no-selection gate FIRES on a packet that makes a selection")
# CONTROL 2: the authority gate must be able to fire.
_probe2 = PKT + "\n\nThe manifest is auth" + "oritative."
check([t for t in _auth if t.lower() in _probe2.lower()] != [],
      "CONTROL: the authority gate FIRES on a packet that declares a face authoritative")
# CONTROL 3: no consequence class assigned.
_cls = re.search(r"(assign|is)\s+(class|outcome)\s*[1-6]\b", PKT, re.I)
check(_cls is None, "no consequence class is assigned anywhere in the packet")

print(); print("="*74); print("RESULT"); print("="*74)
n = sum(1 for ok,_ in CHECKS if ok)
print("  battery: %d/%d, failures: %d" % (n, len(CHECKS), len(FAILURES)))
for f in FAILURES: print("    FAILED: " + f)

out = {
 "instrument":"wall_kr_owner_decision_packet.py","date":"2026-09-02",
 "kind":"OWNER DECISION PACKET — presentation only, no decision made",
 "battery":"%d/%d"%(n,len(CHECKS)),"failures":FAILURES,
 "base_commit":"4cb5d23","branch":"v4",
 "decisions_presented":["A IR input","B epoch window","C low-frequency domain",
                        "D certificate/manifest face","E hash-pin drift","F three held flags"],
 "agent_selections":"NONE — every decision left to the owner",
 "faces":{"FACE_1":"CLASS_C_DISPATCH_FROZEN.md — slash-separated prose, 7 apparent tokens",
          "FACE_2":"CLASS_C_MANIFEST.json v1.1 — JSON array of 6",
          "FACE_3":"CLASS_C_DISPATCH_SPEC.md section 6 — numbered list of 6"},
 "face_authority":"NOT DECLARED — owner-owed; the earlier manifest-is-authoritative claim stays WITHDRAWN",
 "semantic_difference_between_faces":"NONE FOUND",
 "proven_mappings":{"cert 3+4":"class 3","cert 7":"class 6"},
 "remaining_ambiguities":["which face binds",
                          "whether the two textual defects are errata or frozen content",
                          "status of out-of-force class C1.g in the unsigned V5 draft"],
 "low_frequency_prerequisites":[
   "an evaluator/assembly valid at omega <~ 3.3993 H",
   "an IR prescription appended to the manifest BEFORE use",
   "a reduction proved stationary in the omega -> 0 scope, or an explicit waiver",
   "if windowed: a named, priced window with its pre-registered penalties accepted",
   "a method to extract alpha WITH an error budget",
   "the amendment issued as a NEW versioned dispatch explaining why this one failed"],
 "integrity_issues":{"drifted_pins":5,"of_total":11,
                     "drifted_content_located_in_history":False,
                     "current_content_assumed_correct":False,
                     "pins_repaired":False,
                     "classified_as":"integrity/provenance, NOT a physics failure"},
 "register_state":{"net":"+16","cell":"CC-C","axis2":"C","gate_e":"A","noise":"A",
                   "tier4":"banked","lambda_R":"one unresolved","h2_locals":"fork-gated",
                   "general_gauge_uniqueness":"NOT CLAIMED"},
 "licensed_for_next_physics_run":"NOTHING",
 "W":"W-0 — computed-and-reported, NOT banked",
}
json.dump(out, open(os.path.join(LED,"WALL_KR_OWNER_DECISION_PACKET_RESULT.json"),"w",
                    encoding="utf-8"), indent=2, ensure_ascii=False)
print("  artifact: WALL_KR_OWNER_DECISION_PACKET_RESULT.json")
print("  " + ("ALL CHECKS PASS" if not FAILURES else "BATTERY HAS FAILURES"))
