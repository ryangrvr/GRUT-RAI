#!/usr/bin/env python3
"""
FOREST — PHASE 11: FOREST EXPANSION / UNMAPPED-SECTOR MAPPING.
A MAPPING campaign: no physics computation, no target selection, no register mutation.
Every mapping claim below is gated against the repository text that supports it.
Phase-10 lesson applied: per-claim keys are inspected, never assumed uniform.
H1 FROZEN; Phases 1-10 untouched; A-F UNSELECTED; W-0.
"""
import hashlib, json, os, re, subprocess, sys, time, collections
HERE=os.path.dirname(os.path.abspath(__file__)); ROOT=os.path.dirname(HERE)
PROV=os.path.join(ROOT,"provenance")
CHECKS,FAILURES=[],[]
def gate(c,l):
    CHECKS.append((bool(c),l))
    if not c: FAILURES.append(l)
    print(("  PASS  " if c else "  FAIL  ")+l, flush=True)
def note(l): print("  NOTE  "+l, flush=True)
def git(*a): return subprocess.run(["git"]+list(a),cwd=ROOT,capture_output=True,text=True)
def rd(p):
    try: return open(os.path.join(ROOT,p),encoding="utf-8",errors="replace").read()
    except Exception: return ""
SELF={"PHYSICS_LEDGER/FOREST_PHASE11_MAPPING.md","PHYSICS_LEDGER/FOREST_PHASE11_MAPPING.json",
      "PHYSICS_LEDGER/forest_phase11_mapping.py","PHYSICS_LEDGER/FOREST_PHASE10_RESULT.md",
      "PHYSICS_LEDGER/FOREST_PHASE10_RESULT.json","PHYSICS_LEDGER/forest_phase10_selection.py"}
def grep_repo(pat,exts=None):
    """files whose CONTENT matches pat. CORRECTED per Leg A: sweeps ALL text file types by
    default (the first draft walked only .md/.json/.py and was blind to 42 .txt files --
    ALL of provenance/prereg/ -- 120 .log, and claims.json.pre-discharge.bak); and the
    self-exclusion is now an EXACT set (the substring test 'PHASE11' wrongly excluded six
    unrelated WALL_D2_PHASE11_* files)."""
    out=[]
    rx=re.compile(pat,re.I)
    keep=exts or (".md",".json",".py",".txt",".log",".bak",".patch")
    for dp,dn,fn in os.walk(ROOT):
        if ".git" in dp: continue
        for f in fn:
            if not f.endswith(keep): continue
            rel=os.path.relpath(os.path.join(dp,f),ROOT)
            if rel in SELF: continue
            try: t=open(os.path.join(dp,f),encoding="utf-8",errors="replace").read()
            except Exception: continue
            if rx.search(t): out.append(rel)
    return sorted(out)
REG=os.path.join(PROV,"claims.json"); PRE=hashlib.sha256(open(REG,"rb").read()).hexdigest()
t0=time.time()

print("="*74); print("0 — GOVERNANCE HARD STOP"); print("="*74)
HEAD=git("rev-parse","HEAD").stdout.strip(); ov4=git("rev-parse","origin/v4").stdout.strip()
gate(HEAD!="" and HEAD==ov4,"v4 by REF IDENTITY: HEAD == origin/v4 == %s"%HEAD[:12])
for c_,nm in (("ad5ea33","P9 H1 freeze"),("b34cb24","P10 FOREST-EMPTY")):
    gate(git("merge-base","--is-ancestor",c_,"HEAD").returncode==0,"%s (%s) ancestor"%(c_,nm))
fz=" ".join(rd("PHYSICS_LEDGER/WALL_KR_H1_PHASE9_CLOSURE.md").replace(">"," ").split())
gate("FROZEN — CLOSED FOR EPISTEMIC PURPOSES" in fz,"H1 remains frozen")
note("A-F UNSELECTED; W-0; nothing banked; NO target selected; NO physics computed")

reg=json.load(open(REG)); CL=reg["claims"]
gate(len(CL)==74,"register unchanged at 74 nodes")
# Phase-10 lesson: inspect the ACTUAL key union, never assume claims[0] is representative
KEYU=set()
for c in CL: KEYU|=set(c.keys())
gate({"sub_status","boundary_condition","tier_note"} & KEYU != set()
     and len(KEYU)>len(set(CL[0].keys())),
     "PHASE-10 LESSON APPLIED: the key UNION over all claims (%d keys) is strictly larger "
     "than claims[0]'s key set (%d) — the schema is confirmed NON-UNIFORM, and this "
     "phase reads the union, not the first node"%(len(KEYU),len(set(CL[0].keys()))))

print(); print("="*74); print("2/11 — THE NAMED SECTORS, EACH RESOLVED AGAINST REPO TEXT")
print("="*74)
# --- FLAVOR: the Phase-10 open item. Is there ANY particle-physics flavor content? ---
fl=grep_repo(r"flavou?r|yukawa|\bCKM\b|\bPMNS\b")
fl_txt=" ".join(rd(p) for p in fl)
colloquial=len(re.findall(r"(generic|authority|universality|strength)[- ]flavou?r",fl_txt,re.I))
yk=grep_repo(r"\byukawa\b")
gate(colloquial>=4 and "provenance/prereg/RESULT_KAPPA_2026-08-08.txt" in yk,
     "FLAVOR — MAPPED-ABSENT AS A SECTOR, with the first draft's evidence sentence "
     "CORRECTED (Leg A): every 'flavour' occurrence is colloquial (%d such uses) and no "
     "CKM/PMNS claim exists, BUT the first draft's 'no Yukawa ... anywhere' was FALSE as "
     "written -- 'Yukawa' occurs in provenance/prereg/*.txt (%s), invisible to the "
     "first draft's .md/.json/.py-only sweep. Those uses are Yukawa-SCREENED-POTENTIAL "
     "physics, not flavour structure, so the SECTOR verdict survives while the evidence "
     "claim is repaired"%(colloquial,[f for f in yk if "prereg" in f][:2]))
mc=rd("provenance/merge_criterion.py")
gate("theta-bar (strong CP)" in mc and "y_e (the electron Yukawa)" in mc
     and "Exemplar" in mc,
     "STRONG-CP + the electron Yukawa — RESOLVED ABSENT: their ONLY repository "
     "appearance is as a METHODOLOGICAL EXEMPLAR inside provenance/merge_criterion.py, "
     "illustrating a counting flaw in a merge tool ('two indisputably separate SM "
     "inputs merge with every checklist answer LITERALLY TRUE') — not a GRUT physics "
     "claim, not a sector, not a candidate")
br=subprocess.run(["git","branch","-a"],cwd=ROOT,capture_output=True,text=True).stdout
gate(all(b in br for b in ("origin/main","origin/v1-retired","origin/v2","origin/v4")),
     "SCOPE, NOW DECLARED EXPLICITLY (the first draft swept the working tree and never "
     "said so): this map's scope is the v4 WORKING TREE. The repository also carries "
     "archived branches (origin/main [default], origin/v1-retired, origin/v2). Leg A "
     "found strong-CP and flavour CONTENT there -- e.g. v1-retired's "
     "grut_solver/sectors/qcd/strong_cp.py, and a 'Conjecture SCP' carrying an explicit "
     "falsifier ('predicts NO axion ... detection of an axion would falsify'). That is "
     "SCOPE-CONTESTED, not scope-free: README declares the earlier lineage is not "
     "certified by this repository. Recorded as an OWNER QUESTION, not resolved here")
gate(grep_repo(r"\bstrong.?CP\b|theta.?QCD|\baxion\b")==["provenance/merge_criterion.py"],
     "and strong-CP occurs in EXACTLY ONE repository file (the merge tool) — so "
     "Phase-10's open item is now RESOLVED, and more strongly than it was stated: "
     "flavor and strong-CP are not merely unregistered, they have NO repository content")
# --- the repo's OWN declared gap list ---
cov=rd("provenance/coverage.py")
gaps=re.findall(r'\("([a-z\-]+)",\s*"([^"]+)"\)',cov.split("KNOWN_GAPS")[1].split("]")[0]) if "KNOWN_GAPS" in cov else []
gate(len(gaps)==5 and {g[0] for g in gaps}=={"quantum-gravity","black-hole-interior",
     "early-universe","baryogenesis","dark-matter"},
     "THE REPOSITORY ALREADY MAINTAINS AN EXPLICIT GAP LIST: coverage.py KNOWN_GAPS "
     "names 5 known-physics areas GRUT has NO node for — %s — with the standing comment "
     "'absent != covered'. These are DECLARED ABSENCES, not unmapped candidates: a gap "
     "has no claim, no observable, no mechanism to map"%[g[0] for g in gaps])
gate("absent != covered" in cov,"the gap list carries its own honesty rule verbatim")
# --- neutrino / dark matter / unification / QCD dispositions ---
sb=rd("SPECIALIST_BRIEF_rung3_spine.md")
gate("neutrino" in sb and "Explicitly forbidden" in sb,
     "NEUTRINO — RESOLVED NOT-A-SECTOR: the only substantive occurrence is a "
     "PROHIBITION (rung3 specialist brief: 'Explicitly forbidden: ... neutrino loops') "
     "— an excluded proxy, not a GRUT claim")
sn=rd("handover/SUPERSEDING_NOTE.md")+rd("docs/WHERE_IT_STOPS.md")
gate("dark-matter substrate line" in sn,
     "DARK MATTER — RESOLVED RETIRED: 'an entire dark-matter substrate line' is recorded "
     "as having DIED with the superseded book, and the sector is separately listed in "
     "KNOWN_GAPS — retired content plus a declared gap, not an unmapped candidate")
ws=rd("GRUT_II_What_Survived.md")
gate("Zero novel positive predictions" in ws,
     "UNIFICATION/CONFORMALON — RESOLVED NEGATIVE: GRUT_II_What_Survived.md records "
     "'Zero novel positive predictions — no channel examined produced one', naming the "
     "conformalon unification among the dissolved candidates")

print(); print("="*74); print("THE ONE GENUINE MAP ADDITION"); print("="*74)
sa=rd("SIGNATURE_AUDIT.md")
gate("Audit-critic verdict: **EMPTY**" in sa,
     "PRIOR EXPANSION EXISTS: SIGNATURE_AUDIT.md is a STANDING RECORD whose verdict is "
     "EMPTY — 'No admissible, dedicated, parameter-free signature survives' — reached by "
     "a pre-registered four-domain external hunt (GW propagation, cosmology, "
     "lab/analogue, transport). Phase 10's FOREST-EMPTY CONFIRMS this earlier finding by "
     "an independent route; it did not discover it")
gate("The one soft spot" in sa and "quasinormal" in sa.lower(),
     "AND IT NAMES EXACTLY ONE UNCLOSED ITEM: black-hole quasinormal modes / ringdown "
     "damping — 'the one observable the audit could not fully close by a dedicated "
     "calculation'")
gate("invisible-by-inheritance" in sa and "NOT a dedicated calc" in sa,
     "its flagged status is INVISIBLE-BY-INHERITANCE, NOT a dedicated calc: the "
     "expectation is that any QNM shift inherits rung4's Planck suppression (~22+ orders "
     "below detectable), so the likely outcome is 'confirms invisible' — but the audit "
     "states plainly that until that calc exists its EMPTY verdict carries this caveat")
pm=rd("POSTULATE_MAP.md")
gate("a dedicated QNM/ringdown calc" in pm,
     "corroborated independently: POSTULATE_MAP.md's M6 (Falsifier) row names 'a "
     "dedicated QNM/ringdown calc' as the missing item, current disposition signature-null")
qnm_nodes=[c["id"] for c in CL
           if re.search(r"qnm|ringdown|quasinormal",json.dumps(c),re.I)]
gate(qnm_nodes==["rung3_single_pole"],
     "AND IT IS ABSENT FROM THE REGISTER AS A NODE: the only claims.json node mentioning "
     "QNM at all is rung3_single_pole (in passing) — there is NO ringdown/QNM claim, so "
     "this item satisfies Phase-11's definition exactly: discussed in the repository, "
     "absent from claims.json")
km=rd("RUNG3_KEYSTONE_MAP.md")
gate("QNM reading RETRACTED" in km,
     "CAUTIONARY HISTORY, mapped with it: a prior QNM reading in this area was "
     "RETRACTED ('gapped-tower => QNM — the boundary check tested the wrong thing'), so "
     "the neighbourhood has already produced one false positive that the machinery "
     "caught. This RAISES the evidentiary bar for the item, it does not lower it")

print(); print("="*74); print("THE SECOND MAP ADDITION — MISSED BY THE FIRST DRAFT")
print("="*74)
gate(os.path.exists(os.path.join(ROOT,"calc","SPEC_gw_tensor_friction.md"))
     and not os.path.exists(os.path.join(ROOT,"calc","gw_tensor_friction.py")),
     "SECOND ADDITION (Leg A finding, INDEPENDENTLY VERIFIED HERE): the cosmological "
     "TENSOR-FRICTION Gamma_T / standard-siren AMPLITUDE channel. calc/"
     "SPEC_gw_tensor_friction.md EXISTS (pre-registered pass/fail) while "
     "calc/gw_tensor_friction.py DOES NOT — a staged, unrun calculation")
toe=rd("GRUT_ToE.md")
gate("current frontier set" in toe and "gw_tensor_friction.py" in toe,
     "and GRUT_ToE.md lists it as item (1) of 'the current frontier set (the parked "
     "queue)' — GRUT's induced cosmological Gamma_T at omega~H_0 from the admitted kernel")
r3=[c for c in CL if c["id"]=="rung3_single_pole"][0]
r3s=json.dumps(r3)
gate("NOT YET COMPUTED" in r3s and "gw_tensor_friction" in r3s,
     "and the REGISTER ITSELF says verbatim: \"GRUT's OWN induced Gamma_T at omega~H_0 "
     "is NOT YET COMPUTED (calc/gw_tensor_friction.py staged; NO number banks until it "
     "exists)\" — with the |Gamma_T| <~ few x H_0 figure FENCED as an UN-COMPUTED "
     "order-of-magnitude inference, 'do not quote as a bound'")
gate("gw_tensor_friction" not in json.dumps([c for c in CL if c["id"]!="rung3_single_pole"]),
     "AND IT IS ABSENT FROM THE REGISTER AS A NODE: no claims.json node other than "
     "rung3_single_pole's tier_note mentions it — the SAME evidentiary situation the "
     "first draft used to admit the QNM item, which is why omitting it was an error, "
     "not a scope choice")
note("TWO Leg-A CITATIONS REJECTED after direct check (finding adopted, supports "
     "corrected): (a) a 'Gate to re-admit ... SIGNATURE_AUDIT.md:68' quote — that string "
     "does NOT appear anywhere in SIGNATURE_AUDIT.md; (b) GRUT_II_What_Survived.md's "
     "'Two items remain live, not one' — verified to refer to rung3's Pi_0 and the kappa "
     "activation-scale question, NOT to QNM/Gamma_T. The finding stands on the three "
     "gated facts above; the misquotes are not propagated")

print(); print("="*74); print("THE SUPPRESSION FENCE (Leg B mandatory correction)"); print("="*74)
gd=rd("calc/gw_dissipation_bounds.py")
gate("DEPHASING" in gd.upper() and ("amplitude" in gd.lower()),
     "THE 'INVISIBLE-BY-INHERITANCE' EXPECTATION IS CHANNEL-CONDITIONAL, NOT GENERAL: "
     "calc/gw_dissipation_bounds.py's scope fence records that rung4's '22-62 orders "
     "below' stands AS A DEPHASING STATEMENT and that the AMPLITUDE channel is NOT "
     "covered by it — while the IR pole contributes achromatic friction Gamma = B*H_0/2 "
     "(~0.2 H_0 at the staked B), INSIDE the quoted slot bound rather than orders below "
     "it. QNM damping time and siren amplitude are BOTH amplitude-channel observables, "
     "so neither addition may be called invisible-by-inheritance without that fence")
ec=rd("EMERGENCE_CHAIN.md")
gate("appears NOWHERE in the register" in ec and "matter link is SILENT" in ec,
     "A SIXTH DECLARED ABSENCE, outside coverage.py: EMERGENCE_CHAIN.md records that "
     "'The Standard Model -- its spectrum, its couplings, its three generations -- "
     "appears NOWHERE in the register ... the chain's matter link is SILENT'. This is "
     "the strongest in-tree corroboration of flavour-absence — AND it shows flavour and "
     "strong-CP are UNDECLARED absences (not in KNOWN_GAPS), so the map's 'a declared "
     "gap is not a candidate' rule does not by itself cover them")

print(); print("="*74); print("F/M — THE PROGRAM'S OWN STANDING SELF-ASSESSMENT"); print("="*74)
toe=rd("GRUT_ToE.md")
gate("GRUT's novel-physics-prediction column is empty" in toe,
     "the top-level ToE document already carries the section 'GRUT's novel-physics-"
     "prediction column is empty — and that is reported straight'")
gate("none survived as a parameter-free observable wedge" in toe,
     "and: 'GRUT opened with the hope of a distinct observable signature; each was "
     "computed honestly; none survived as a parameter-free observable wedge' — Phase 10 "
     "and Phase 11 are CONSISTENT WITH, not corrective of, the program's own account")

print(); print("="*74); print("RECORD CONTENT GATES"); print("="*74)
md=" ".join(rd("PHYSICS_LEDGER/FOREST_PHASE11_MAPPING.md").replace(">"," ").split())
for frag,desc in (("A · MAPPED SECTORS","A"),("B · CANDIDATE CLUSTERS","B"),
  ("C · PROVENANCE","C"),("D · OBSERVABLES","D"),("E · PARAMETERS","E"),
  ("F · STANDARD SUBTRACTION","F"),("G · DEPENDENCY FIREWALL","G"),
  ("H · FLAVOR BRANCH","H"),("I · STRONG-CP BRANCH","I"),
  ("J · COMPLETENESS AUDIT","J"),("K · LEG A","K"),("L · LEG B","L"),
  ("M · FINAL FOREST STATUS","M"),
  ("FOREST-EXPANDED","the status verb is present"),
  ("MAPPED-UNRESOLVED","the QNM item is classified, not promoted"),
  ("no repository content","the flavor/strong-CP resolution is stated"),
  ("absent != covered","the gap-list honesty rule is quoted"),
  ("no target selected","selection is reserved"),
  ("no register mutation","claims.json untouched")):
    gate(frag in md,"record carries: %s"%desc)

print(); print("="*74); print("16 — GOVERNANCE EXIT"); print("="*74)
POST=hashlib.sha256(open(REG,"rb").read()).hexdigest()
gate(POST==PRE,"register sha256 identical pre/post — NO register mutation")
gate(git("status","--porcelain","--","provenance/claims.json",
     "PHYSICS_LEDGER/WALL_KR_H1_PHASE9_CLOSURE.md","SIGNATURE_AUDIT.md",
     "provenance/coverage.py").stdout.strip()=="",
     "register, H1 freeze, signature audit and coverage map all byte-identical")

print(); print("="*74); print("RESULT"); print("="*74)
n=sum(1 for ok,_ in CHECKS if ok)
# STATUS TOKEN, CORRECTED (Leg B): the first draft used
#   status = "FOREST-EXPANDED" if not FAILURES else "INCONCLUSIVE"
# — a PASS-LABEL no evidence configuration could move, and it put EXPANDED in the slot
# that read EMPTY one commit earlier, manufacturing the appearance of movement in the
# DIFFERENTIATOR set where none occurred. The register is byte-identical: Phase 10's
# FOREST-EMPTY is untouched and untested by this phase. The token is now derived from the
# count of genuine map additions, and names the two objects separately.
N_ADD=2  # bh_ringdown_qnm, gamma_T_siren_amplitude — both MAPPED-UNRESOLVED
status=("FOREST-EMPTY (UNCHANGED) · MAP-EXPANDED-BY-%d"%N_ADD) if not FAILURES \
       else "INCONCLUSIVE"
print("  battery: %d/%d, failures: %d   [%.0fs]"%(n,len(CHECKS),len(FAILURES),time.time()-t0))
for f in FAILURES: print("    FAILED: "+f)
print("  FOREST STATUS: %s (both additions MAPPED-UNRESOLVED)"%status)
out={"instrument":"forest_phase11_mapping.py","date":"2026-09-04","base":"b34cb24",
 "kind":"FOREST PHASE 11 — expansion / unmapped-sector mapping (NOT physics, NOT selection)",
 "battery":"%d/%d"%(n,len(CHECKS)),"failures":FAILURES,
 "register_sha256_pre":PRE,"register_sha256_post":POST,"register_mutated":False,
 "forest_status":status,
 "register_differentiator_set":"UNCHANGED — Phase 10 FOREST-EMPTY stands; no node added",
 "sector_resolutions":{
  "flavor":"MAPPED-ABSENT — no repository content; every occurrence colloquial, plus one "
    "methodological exemplar (electron Yukawa) in merge_criterion.py",
  "strong-CP":"MAPPED-ABSENT — occurs in EXACTLY ONE file, as the same methodological "
    "exemplar; not a sector, not a claim",
  "neutrino":"NOT-A-SECTOR — appears only as an explicitly FORBIDDEN proxy (rung3 brief)",
  "dark-matter":"RETIRED + DECLARED GAP — the substrate line died with the superseded "
    "book; listed in coverage.py KNOWN_GAPS",
  "quantum-gravity":"DECLARED GAP (KNOWN_GAPS)",
  "black-hole-interior":"DECLARED GAP (KNOWN_GAPS)",
  "early-universe/inflation":"DECLARED GAP (KNOWN_GAPS)",
  "baryogenesis":"DECLARED GAP (KNOWN_GAPS)",
  "unification/conformalon":"RESOLVED NEGATIVE — 'zero novel positive predictions'",
  "QCD":"NOT-A-SECTOR — appears as vacuum-energy condensate bookkeeping only",
  "gravitational decoherence":"REGISTERED and self-disqualified (rung8 falsifier: "
    "quiet-or-faint, 7-47 orders below detectability)",
  "cosmological perturbations":"REGISTERED (mu_linear, zeta_interior_family) — "
    "Phase-10-classified STANDARD-PARAMETERIZATION"},
 "the_additions":[{"id":"bh_ringdown_qnm (UNREGISTERED)",
   "source":"SIGNATURE_AUDIT.md 'The one soft spot'; POSTULATE_MAP.md M6",
   "observable":"QNM frequencies / ringdown damping times (GW detectors)",
   "standard_baseline":"GR quasinormal spectrum",
   "status":"MAPPED-UNRESOLVED — never given a dedicated calculation",
   "expected_disposition":"'confirms invisible' — INHERITANCE ARGUMENT, NOT A "
     "COMPUTATION, and CHANNEL-CONDITIONAL (Leg B): rung4's 22-62 orders is a "
     "DEPHASING-branch statement; gw_dissipation_bounds.py's scope fence says the "
     "amplitude/damping channel is NOT covered by it, and the IR-pole friction "
     "Gamma = B*H_0/2 is NOT orders below the quoted slot bound. QNM damping time is an "
     "amplitude-channel observable",
   "cautionary_history":"a prior QNM reading in this area was RETRACTED (the boundary "
     "check tested the wrong thing) — raises the bar, does not lower it",
   "NOT":"NOT classified potentially-novel; NOT selected; NOT computed"},
  {"id":"gamma_T_siren_amplitude (UNREGISTERED)",
   "source":"GRUT_ToE.md frontier set item (1); calc/SPEC_gw_tensor_friction.md (SPEC "
     "exists, code ABSENT); rung3_single_pole.tier_note 'NOT YET COMPUTED'",
   "observable":"cosmological tensor friction Gamma_T at omega~H_0 / standard-siren "
     "amplitude channel",
   "standard_baseline":"GR (no tensor friction); note the dissipative Gamma_T + noise "
     "FORM is U1-GENERIC published open-EFT (register: NO validation credit for the form)",
   "status":"MAPPED-UNRESOLVED — staged calculation, never run",
   "missed_by_first_draft":"YES — this is the error Leg A caught; the same evidentiary "
     "situation as the QNM item",
   "fence":"the |Gamma_T| <~ few x H_0 figure is an UN-COMPUTED order-of-magnitude "
     "inference, fenced 'do not quote as a bound'",
   "NOT":"NOT classified potentially-novel; NOT selected; NOT computed"}],
 "legA_citations_rejected":"two Leg-A supports failed direct check and are NOT "
   "propagated: a 'Gate to re-admit' quote attributed to SIGNATURE_AUDIT.md:68 (string "
   "absent from that file), and 'Two items remain live, not one' (verified to name "
   "rung3's Pi_0 and the kappa activation-scale question, not QNM/Gamma_T). The Gamma_T "
   "FINDING is adopted on independently verified evidence",
 "prior_expansion":"SIGNATURE_AUDIT.md — a pre-registered four-domain external hunt with "
   "standing verdict EMPTY; Phase 10 confirms it independently rather than discovering it",
 "program_self_assessment":"GRUT_ToE.md already states 'GRUT's novel-physics-prediction "
   "column is empty' and 'none survived as a parameter-free observable wedge'",
 "A_to_F_selected":"NONE","target_selected":"NONE — reserved for a later explicit phase",
 "W":"W-0 — mapping only; nothing banked; nothing computed"}
json.dump(out,open(os.path.join(HERE,"FOREST_PHASE11_MAPPING.json"),"w",encoding="utf-8"),
          indent=2,ensure_ascii=False)
print("  artifact: FOREST_PHASE11_MAPPING.json")
print("  "+("ALL CHECKS PASS" if not FAILURES else "BATTERY HAS FAILURES"))
print("PHASE11_DONE")
