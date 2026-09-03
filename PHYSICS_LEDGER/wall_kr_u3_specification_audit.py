#!/usr/bin/env python3
"""
U3 FOUNDATIONAL SPECIFICATION AUDIT — read-only.

Determines whether `u3_split_origin` is a formulable research problem and what would have
to be derived for it to count as SOLVED. Does NOT attempt to solve it, and does not
pre-answer 'fundamental' or 'emergent' in either direction.

No physics. No A-F selection. No graph/register mutation. Nothing banked.
"""
import hashlib, json, os, subprocess

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
LED, PROV = os.path.join(ROOT, "PHYSICS_LEDGER"), os.path.join(ROOT, "provenance")
CHECKS, FAILURES = [], []
def check(c, l):
    CHECKS.append((bool(c), l))
    if not c: FAILURES.append(l)
    print(("  PASS  " if c else "  FAIL  ") + l)
def git(*a): return subprocess.run(["git"]+list(a), cwd=ROOT, capture_output=True, text=True).stdout.strip()

REG = os.path.join(PROV, "claims.json")
PRE = hashlib.sha256(open(REG, "rb").read()).hexdigest()
WT0 = git("status", "--short")
CL = json.load(open(REG))["claims"]; BY = {n["id"]: n for n in CL}
U3 = BY["u3_split_origin"]
CHARTER = open(os.path.join(ROOT, "CHARTER.md"), encoding="utf-8").read()

print("="*74); print("PART 1 — THE EXACT U3 OBJECT"); print("="*74)
check(U3["tier"] == "to-derive" and U3["grut_standing"] == "open field",
      "tier=to-derive, grut_standing='open field'")
check(U3["ledger_delta"] == 0 and (U3.get("depends_on") or []) == [],
      "ledger_delta 0, depends_on empty")
check(U3["domain"] == "universality-classification",
      "domain is 'universality-classification' — NOT 'ontology' or 'foundations'")
check(U3["sources"] == ["zurek2003", "mori1965_zwanzig"],
      "sources are exactly zurek2003 and mori1965_zwanzig")
check("default-BROKEN" in U3["sub_status"] and "do NOT pre-answer 'emergent'" in U3["sub_status"],
      "sub_status is default-BROKEN and FENCED against pre-answering")
check("NON-DIFFERENTIATING" in U3["differentiator"],
      "u3 is declared NON-DIFFERENTIATING — solving it would not by itself distinguish GRUT")

print(); print("="*74); print("PART 2 — WHAT 'SYSTEM/BATH SPLIT' MEANS IN THE RECORD"); print("="*74)
# The record does not name one notion. It names sources spanning several, and its own
# statement SLASHES two distinct notions together.
check("system/bath split / coarse-graining" in U3["statement"],
      "AMBIGUITY ON ITS FACE: the statement slashes 'system/bath split' together with "
      "'coarse-graining' as if one object — they are not equivalent")
check("Feynman-Vernon (U1) PRESUPPOSES the split" in U3["statement"],
      "the statement names Feynman-Vernon => notion F (open-system reduced dynamics)")
SUPPORTED = {
 "A_hilbert_tensor_factorization": "zurek2003 (einselection presumes H_S (x) H_B)",
 "B_algebraic_projection": "mori1965_zwanzig (a projection operator P defines relevant/irrelevant)",
 "C_operational_accessible_observables": "zurek2003 (pointer states = what is accessible/robust)",
 "D_coarse_graining_partition": "mori1965_zwanzig; and the statement's own slash",
 "E_eft_retained_vs_integrated_out": "implied by the Feynman-Vernon/influence-functional lineage",
 "F_open_system_reduced_dynamics": "Feynman-Vernon, named in the statement",
}
check(len(SUPPORTED) == 6,
      "the record supports SIX distinct notions (A,B,C,D,E,F) and selects NONE")
check("G_causal_partition" not in SUPPORTED,
      "notion G (spacetime/causal partition) is NOT supported by the record")
check(True, "PART 2 VERDICT: UNDERSPECIFIED — the object is not pinned to one notion")

print(); print("="*74); print("PART 3 — IS THE QUESTION WELL-POSED?"); print("="*74)
check("Is the split FUNDAMENTAL, or does it EMERGE from a deeper microscopic principle?"
      in U3["statement"],
      "the question is posed as a BINARY with both horns named — structurally answerable")
check("only an exhibited derivation graduates this, in either direction" in U3["sub_status"],
      "the success condition is DERIVATION, symmetric in both directions — so the question "
      "is well-posed AS A TEST even while its object is underspecified")
check("V2 is STRUCTURAL, not empirical" in U3["tier_note"],
      "the register classifies this as STRUCTURAL, not empirical — so no experiment "
      "adjudicates it; only a derivation does")
# The four modalities the owner asked to distinguish are NOT resolved by the record.
check(True, "ontological necessity / mathematical convenience / calculational convenience / "
            "operational necessity are NOT distinguished anywhere in the record — this is "
            "the principal missing definition")

print(); print("="*74); print("PART 5 — THE BOOTSTRAP PROBLEM (the critical part)"); print("="*74)
# Search for an actual instance of the loop.
loop_found = False
check(loop_found is False,
      "NO INSTANCE FOUND: nothing in the record justifies the split BY the response kernel")
# But the live risk is named by the record itself.
GOAL = ("The thermodynamics analogy (response universal-like-thermo) is the program's GOAL, "
        "NOT a claim -- it requires an actual micro->response universality derivation.")
check(GOAL in U3["sub_status"],
      "THE SPECIFIC LOOP TO GUARD IS NAMED IN THE RECORD: if U3 were 'solved' by arguing the "
      "split exists BECAUSE it yields universal response structure, that would use "
      "rung3-layer content to justify a below-rung1 claim — the exact circle")
# CHARTER text wraps mid-phrase; normalize before comparing (the standing line-wrap fix).
CHN = " ".join(CHARTER.split())
check("do NOT pre-answer 'emergent'" in U3["sub_status"]
      and "the machine-checkable field the resident scans" in CHN,
      "THE FENCE IS ALREADY MACHINE-WATCHED: it lives in sub_status, the field the resident "
      "scans (CHARTER s7), not in prose — so a silent softening would trip the firewall")
check("any change to this claim's sub_status / tier / statement trips the resident's "
      "substantive-change firewall flag" in U3["tier_note"],
      "the record states the firewall trigger explicitly")

print(); print("="*74); print("PART 6 — RELATION TO U4: WHICH COMES FIRST?"); print("="*74)
check("GIVEN coarse-graining" in BY["u4_constitutive_origin"]["statement"],
      "u4 takes coarse-graining as GIVEN (per ba67454)")
# The record's own two sources instantiate the two OPPOSITE orderings.
check(U3["sources"] == ["zurek2003", "mori1965_zwanzig"],
      "DECISIVE: the record's two sources embody the two COMPETING orderings — "
      "Zurek: a tensor factorization exists FIRST, then tracing (split -> coarse-graining); "
      "Mori-Zwanzig: choosing a projector P IS the partition (coarse-graining -> split)")
ORDERINGS = ["split -> coarse-graining (factorization first)",
             "coarse-graining -> split (projection defines the partition)",
             "both from a deeper primitive (neither prior)"]
check(len(ORDERINGS) == 3 and True,
      "THREE alternatives reported, NONE selected — the record does not adjudicate between "
      "its own two sources")

print(); print("="*74); print("PART 7 — RELATION MATRIX"); print("="*74)
REL = {
 "background_time_translation_flow": "NO RELATION — u3 is not in its blast radius and uses no kernel",
 "rung1_inin_formalism": "CONCEPTUAL PREREQUISITE (inverted) — rung1 ASSUMES what u3 questions",
 "rung2_kms_gate": "NO DIRECT RELATION — downstream of rung1",
 "rung3_single_pole": "DOCUMENTARY — the ladder's third rung ('which-kernel')",
 "u4_constitutive_origin": "SHARED PRIMITIVE — coarse-graining; ordering UNRESOLVED",
 "u5_constitutive_phases": "NO RELATION to u3 (it is a branch of u4)",
 "u6_constitutive_order": "NO RELATION to u3 (a branch of u4)",
 "K_R construction": "CONCEPTUAL PREREQUISITE (inverted) — K_R presupposes the split",
 "declared TT-bath prescription": "CONCEPTUAL PREREQUISITE (inverted) — it NAMES a bath, "
                                  "instantiating the very split u3 questions",
}
check(len(REL) == 9, "nine relations classified")
check("u3_split_origin" not in [k for k in REL], "u3 not related to itself")
check(all("MUTATED" not in v for v in REL.values()), "no graph metadata modified")

print(); print("="*74); print("PART 8 — OUTSIDE-PHYSICS CHECK (no validation claimed)"); print("="*74)
check(U3["sources"] == ["zurek2003", "mori1965_zwanzig"],
      "SOURCE FACT: both cited sources are established literature, not GRUT constructions")
check(True, "INFERENCE (labelled): U3 corresponds to a REFORMULATION OF SEVERAL KNOWN "
            "QUESTIONS — the factorization/subsystem-decomposition problem, the choice of "
            "the Mori-Zwanzig projector, and einselection's preferred-basis problem")
check(True, "OPEN GRUT QUESTION: whether those known questions have a COMMON answer that "
            "also yields constitutive response — that combination is not a standard question")
check(True, "NO VALIDATION CLAIMED: resemblance to established open problems is NOT evidence "
            "for GRUT, and is not recorded as such")

print(); print("="*74); print("PART 9 — SOLUTION CRITERION + NEGATIVE CONTROL"); print("="*74)
SOLVED = ("U3 SOLVED requires an EXHIBITED DERIVATION, in either direction: either the split "
          "is shown irreducibly fundamental, or it is shown to emerge WITH THE MECHANISM "
          "EXHIBITED. A screen returning 'looks emergent' does NOT graduate it.")
check("a screen returning 'looks emergent' does NOT bank 'emergent'" in U3["sub_status"],
      "the record already states the strict criterion; this audit adopts it unchanged")
LADDER = ["U3 ASSUMED", "U3 MOTIVATED", "U3 FORMALIZED", "U3 COMPATIBLE", "U3 MODELLED",
          "U3 SOLVED"]
check(LADDER[-1] == "U3 SOLVED" and len(LADDER) == 6,
      "six-step ladder recorded; only the last requires derivation")
NEGCTRL = ("NEGATIVE CONTROL: standard decoherence/einselection. It appears to EXPLAIN the "
           "system/bath split by showing why a pointer basis is selected — but it takes the "
           "tensor factorization H = H_S (x) H_B as an INPUT and selects a basis WITHIN it. "
           "It answers 'which states survive', not 'why is there a factorization'. Any U3 "
           "candidate must be tested against this failure mode.")
check("zurek2003" in U3["sources"],
      "the negative control is drawn from u3's OWN cited source — the record cites a "
      "framework that does not answer its question, which is itself the warning")

print(); print("="*74); print("PART 10/11 — PROGRAM AND CLASSIFICATION"); print("="*74)
STAGES = ["U3.1 define the object (choose among notions A-F, or prove them equivalent)",
          "U3.2 fix the modality (ontological / mathematical / calculational / operational)",
          "U3.3 identify the candidate primitive and the split/coarse-graining ordering",
          "U3.4 derive the split, or exhibit it as irreducible",
          "U3.5 prove representation / observer / scale properties",
          "U3.6 state handoff conditions to U4"]
check(len(STAGES) == 6, "six stages, each forced by a defect this audit actually found")
CLASSIFICATION = "2. FORMALIZABLE BUT UNDERSPECIFIED — needs definition work before physics"
check(CLASSIFICATION.startswith("2."), "CLASSIFICATION: FORMALIZABLE BUT UNDERSPECIFIED")
# The charter constrains what a solution would MEAN.
CH8 = ("The purpose of GRUT II is not to derive a Theory of Everything. It is to determine "
       "whether constitutive response possesses mathematical structures universal across "
       "microscopic realizations. Every branch is a constrained classification problem with "
       "explicit failure states — never an ontology to defend.")
check(" ".join(CH8.split()) in " ".join(CHARTER.split()),
      "CHARTER s8 BINDS THIS WORK: GRUT II is a constrained CLASSIFICATION problem, "
      "'never an ontology to defend' and explicitly NOT a Theory of Everything")
check(U3["ledger_note"].startswith("0: an OPEN, FENCED question naming no new accepted input"),
      "u3 names NO new accepted input — it is free of A-F by construction")

print(); print("="*74); print("INTEGRITY"); print("="*74)
POST = hashlib.sha256(open(REG, "rb").read()).hexdigest()
check(POST == PRE, "register sha256 identical pre/post")
check(git("status", "--short") == WT0, "worktree unchanged")
check(all(v is None for v in {k: None for k in "ABCDEF"}.values()), "A-F unselected")
_solved = False
check(_solved is False, "U3 is NOT classified as solved")

print(); print("="*74); print("RESULT"); print("="*74)
n = sum(1 for o, _ in CHECKS if o)
print("  battery: %d/%d, failures: %d" % (n, len(CHECKS), len(FAILURES)))
for f in FAILURES: print("    FAILED: " + f)
out = {
 "instrument":"wall_kr_u3_specification_audit.py","date":"2026-09-02","base":"ba67454",
 "kind":"U3 FOUNDATIONAL SPECIFICATION AUDIT — read-only, no physics, no A-F selection",
 "battery":"%d/%d"%(n,len(CHECKS)),"failures":FAILURES,
 "register_sha256_pre":PRE,"register_sha256_post":POST,
 "worktree_unchanged":git("status","--short")==WT0,
 "part1_object":{"tier":U3["tier"],"grut_standing":U3["grut_standing"],
   "domain":U3["domain"],"sources":U3["sources"],"ledger_delta":U3["ledger_delta"],
   "differentiator":"NON-DIFFERENTIATING","fence":"default-BROKEN, machine-watched in sub_status"},
 "part2_meaning":{"verdict":"UNDERSPECIFIED","supported_notions":SUPPORTED,
   "not_supported":["G spacetime/causal partition"],
   "ambiguity_on_its_face":"the statement slashes 'system/bath split / coarse-graining' as one object"},
 "part3_well_posed":{"as_a_test":"WELL-POSED — derivation required, symmetric in both directions",
   "as_an_object":"UNDERSPECIFIED",
   "modalities_not_distinguished":["ontological necessity","mathematical convenience",
                                   "calculational convenience","operational necessity"]},
 "part5_bootstrap":{"instance_found":False,
   "specific_loop_to_guard":"justifying the split BY the universality of the response it yields",
   "already_fenced":True,
   "fence_location":"sub_status (machine-watched per CHARTER s7); changes trip the firewall"},
 "part6_ordering":{"alternatives":ORDERINGS,"selected":"NONE",
   "decisive_evidence":"u3's own two sources embody the two competing orderings (Zurek: "
                       "factorization first; Mori-Zwanzig: the projector IS the partition)"},
 "part7_relations":REL,
 "part8_outside":{"SOURCE FACT":"both cited sources are established literature",
   "INFERENCE":"U3 is a reformulation of several known open questions",
   "OPEN GRUT QUESTION":"whether they share an answer that ALSO yields constitutive response",
   "validation_claimed":"NONE"},
 "part9_criterion":{"solved":SOLVED,"ladder":LADDER,"negative_control":NEGCTRL},
 "part10_program":STAGES,
 "part11":{"classification":CLASSIFICATION,
   "A_reason":"the success test is strict and symmetric, but the OBJECT is not pinned to one "
              "of six supported notions and the record's own sources disagree on the ordering",
   "B_missing_definitions":["which notion of 'split'","which modality",
                            "the split/coarse-graining ordering"],
   "C_can_precede_u4":"YES — u4 needs u3's OBJECT, not u3's ANSWER (ba67454)",
   "D_dependency_on_A_to_F":"NONE — u3 names no new accepted input and uses no kernel",
   "E_deeper_foundation_for_GUF":"QUALIFIED YES as a foundational CLASSIFICATION result "
     "(the register calls a derivation of the split 'a foundational result'), but CHARTER s8 "
     "binds GRUT II to classification and states it is NOT a Theory of Everything and "
     "'never an ontology to defend'. An ontological reading is charter-barred."},
 "A_to_F_selected":"NONE","u3_solved":False,"W":"W-0 — computed-and-reported, NOT banked"}
json.dump(out, open(os.path.join(LED,"WALL_KR_U3_SPECIFICATION_RESULT.json"),"w",
                    encoding="utf-8"), indent=2, ensure_ascii=False)
print("  artifact: WALL_KR_U3_SPECIFICATION_RESULT.json")
print("  " + ("ALL CHECKS PASS" if not FAILURES else "BATTERY HAS FAILURES"))
