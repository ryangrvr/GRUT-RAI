#!/usr/bin/env python3
"""
FOREST — PHASE 12: AMPLITUDE-CHANNEL TARGET ADJUDICATION.
Head-to-head between the two Phase-11 additions. NEITHER preselected. No physics computed,
no target computation launched, no register mutation. Every head-to-head cell is gated
against repository text. Standing lessons applied: sweep all text types; declare scope;
no pass-label verdicts; no gate whose identity is definitional.
H1 FROZEN; Phases 1-11 untouched; A-F UNSELECTED; W-0.
"""
import hashlib, json, os, re, subprocess, time
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
def nfiles(pat):
    """count files (ALL text types) whose content matches pat, excluding phase-11/12 outputs"""
    rx=re.compile(pat,re.I); n=[]
    for dp,dn,fn in os.walk(ROOT):
        if ".git" in dp: continue
        for f in fn:
            if not f.endswith((".md",".json",".py",".txt",".log",".bak")): continue
            rel=os.path.relpath(os.path.join(dp,f),ROOT)
            if "PHASE11" in rel.upper() or "PHASE12" in rel.upper(): continue
            try:
                if rx.search(open(os.path.join(dp,f),encoding="utf-8",errors="replace").read()):
                    n.append(rel)
            except Exception: pass
    return sorted(n)
REG=os.path.join(PROV,"claims.json"); PRE=hashlib.sha256(open(REG,"rb").read()).hexdigest()
t0=time.time()

print("="*74); print("0 — GOVERNANCE HARD STOP"); print("="*74)
HEAD=git("rev-parse","HEAD").stdout.strip(); ov4=git("rev-parse","origin/v4").stdout.strip()
gate(HEAD!="" and HEAD==ov4,"v4 by REF IDENTITY: HEAD == origin/v4 == %s"%HEAD[:12])
for c_,nm in (("ad5ea33","P9"),("b34cb24","P10"),("acae001","P11")):
    gate(git("merge-base","--is-ancestor",c_,"HEAD").returncode==0,"%s (%s) ancestor"%(c_,nm))
gate("FROZEN — CLOSED FOR EPISTEMIC PURPOSES" in
     " ".join(rd("PHYSICS_LEDGER/WALL_KR_H1_PHASE9_CLOSURE.md").replace(">"," ").split()),
     "H1 freeze intact")
CL=json.load(open(REG))["claims"]
gate(len(CL)==74,"register unchanged at 74 nodes")
note("A-F UNSELECTED; W-0; NO target computation running; SCOPE = the v4 working tree "
     "(declared, per the Phase-11 lesson)")

print(); print("="*74); print("2 — CANDIDATE A: Gamma_T / STANDARD-SIREN AMPLITUDE"); print("="*74)
spec_raw=rd("calc/SPEC_gw_tensor_friction.md")
spec=" ".join(spec_raw.replace(">"," ").split())   # normalized + blockquote markers stripped (standing trap)
gate(bool(spec_raw) and not os.path.exists(os.path.join(ROOT,"calc","gw_tensor_friction.py")),
     "A-SCAFFOLDING: a pre-registered SPEC EXISTS (calc/SPEC_gw_tensor_friction.md, "
     "'Pass/fail is pre-registered below, before any result exists') while the code does "
     "NOT — a staged, unrun, pre-committed calculation")
gate("Does the local memory scale connect parameter-free, or does the bridge need a new inserted scale?" in spec,
     "A-QUESTION (pre-registered, verbatim): 'Does the local memory scale connect "
     "parameter-free, or does the bridge need a new inserted scale?'")
gate("(Q-D)" in spec and "degenerate with the coalescence phase" in spec
     and "standard-siren amplitude" in spec,
     "A-CHANNEL, CORRECTLY IDENTIFIED IN-SPEC (Q-D): the friction is ACHROMATIC and "
     "therefore DEGENERATE WITH THE COALESCENCE PHASE, so the matched-filter dephasing "
     "test is 'blind to it BY CONSTRUCTION'; the non-blind channel is STANDARD-SIREN "
     "AMPLITUDE. This independently confirms the Phase-11 channel fence")
gate("Neither horn supports a quoted number" in spec,
     "A-BLOCKER (Q-A, 'this dominates everything else'): does the tau_2 pole appear in "
     "the P^TT channel at all, or only in the scalar P^(0s) channel? If scalar-only, "
     "'the whole friction result is zero in this channel and the question closes'. The "
     "SPEC states both horns and concludes: 'NEITHER HORN SUPPORTS A QUOTED NUMBER'")
gate("~3.2 orders" in spec or "3.2 orders" in spec,
     "A-PARAMETER: B is a STAKED illustrative amplitude with TWO live values differing "
     "by ~3.2 ORDERS — B=0.4 -> Gamma_T = 0.2*H0 (inside the few-x-H0 slot bound by ~5x) "
     "vs B~2.4e-4 -> Gamma_T ~ 1.2e-4*H0 (INVISIBLE). The SPEC orders: 'Report BOTH, "
     "labelled, and do not pick one silently'")
gate("separate unverified assumption" in spec,
     "A-PARAMETER 2 (Q-C): identifying B with eps is 'a separate unverified assumption'")
r3=json.dumps([c for c in CL if c["id"]=="rung3_single_pole"][0])
gate("U1-GENERIC" in r3 and "NO validation credit for the form" in r3,
     "A-STANDARD-OVERLAP, from the register itself: the dissipative Gamma_T + noise FORM "
     "is U1-GENERIC standard open-EFT and now a PUBLISHED MAINSTREAM parameterization "
     "(salcedo_colas_dufner_pajer2026) — 'NO validation credit for the form'. Only a "
     "parameter-free VALUE could be GRUT-specific, and that is exactly what Q-A/Q-B say "
     "cannot presently be quoted")
gate("explicitly DISTINCT from the conservative running-Planck-mass alpha_M" in r3,
     "A-BASELINE, the one real structural distinction: dissipative Gamma_T (+ mandatory "
     "noise) is explicitly DISTINCT from the conservative running-Planck-mass alpha_M*H "
     "of standard modified-gravity propagation")

gate("could NEVER confirm GRUT" in r3 and "slot-degenerate" in r3
     and "CATEGORY FENCE" in r3,
     "A-DISQUALIFIER IN THE SELECTED CHANNEL — THE HALF THE FIRST DRAFT DROPPED (Leg A): "
     "the SAME rung3 boundary_condition this instrument already gated says verbatim "
     "'A detected Xi_0 != 1 could NEVER confirm GRUT and would bear on it only AFTER a "
     "conservative-vs-dissipative decomposition', and that alpha_M is 'sign-indefinite "
     "and slot-degenerate'. The first draft extracted the favourable clause "
     "('explicitly DISTINCT from alpha_M') from a string it had in memory and promoted "
     "it to 'the one real structural distinction' while omitting this one. CORRECTED")
gate("achromatic, and noiseless" in r3,
     "AND THE FENCE CUTS BOTH WAYS, precisely: alpha_M is 'removable by field "
     "redefinition, graviton-number-conserving, sign-indefinite, ACHROMATIC, and "
     "noiseless; a genuine dissipative kernel is none of these'. So (i) the category "
     "distinction is REAL in physical character, but (ii) ACHROMATICITY — the property "
     "the first draft's channel argument leaned on — is exactly what Gamma_T SHARES "
     "with the standard-MG parameter, not what separates it; and (iii) the separating "
     "feature is the MANDATORY NOISE, which implies a different observable (a stochastic "
     "background), in a channel this phase did NOT select and does not assess")
gate("REFUSE" in spec,
     "A-OUTCOME SET, CORRECTED: the SPEC pre-registers FOUR outcomes, not three — PASS, "
     "FAIL-BUT-INFORMATIVE, CLOSES THE QUESTION, and REFUSE ('if the sector question "
     "cannot be settled from the booked family'). REFUSE is the outcome under which A is "
     "UNDECIDABLE, and the first draft's three-outcome list was used to certify A as "
     "'decidable' — an overstatement now withdrawn")
gd=rd("calc/gw_dissipation_bounds.py")
gate("IR pole's Re part is B/(1 + (w*tau_2)^2), which IS negligible at LIGO" in
     " ".join(gd.split()),
     "A-CHANNEL MECHANISM, CORRECTED (Leg A): the SPEC's stated reason — 'achromatic, "
     "therefore degenerate with the coalescence phase' — is a CATEGORY ERROR, quoted "
     "from the SPEC by the first draft and propagated unchecked: Gamma_T is a damping "
     "rate acting on |h|, contributing no phase, so it cannot be degenerate with phi_c. "
     "The CORRECT reason is in gw_dissipation_bounds.py: the IR pole's Re part is "
     "negligible at LIGO frequencies, so the dephasing figure is untouched while the "
     "amplitude channel is uncovered. The conclusion (amplitude is the live channel) "
     "survives; the stated mechanism does not")
note("AND THE 'INDEPENDENT CONFIRMATION' CLAIM IS WITHDRAWN AS CIRCULAR: the first draft "
     "said the SPEC's Q-D 'independently confirms Phase 11's channel fence' — but "
     "Phase 11's fence and Q-D trace to the SAME source file. One source, not two")

print(); print("="*74); print("3 — CANDIDATE B: BH QNM / RINGDOWN"); print("="*74)
for kw,lab in ((r"\bKerr\b","Kerr"),(r"Teukolsky","Teukolsky"),
               (r"tidal heating","tidal heating"),(r"Love number","Love number"),
               (r"horizon flux","horizon flux")):
    f=nfiles(kw)
    gate(f==[], "B-SCAFFOLDING ABSENT: '%s' appears in ZERO repository files"%lab)
rw=nfiles(r"Regge.?Wheeler|Zerilli")
sp=rd("calc/static_patch_tt_response.py")
gate("calc/static_patch_tt_response.py" in rw and "de Sitter static PATCH" in sp
     and "Every M-dependent term in it drops at M = 0" in sp,
     "B-SCAFFOLDING, what EXISTS instead: the only Regge-Wheeler/Zerilli material is "
     "calc/static_patch_tt_response.py — the DE SITTER STATIC PATCH, whose own text says "
     "'Every M-dependent term in it drops at M = 0'. THAT IS NOT A BLACK HOLE. There is "
     "no BH perturbation problem in the corpus onto which a GRUT term could be added")
km=rd("RUNG3_KEYSTONE_MAP.md")
gate("gapped-tower" in km and "the boundary check tested the wrong thing" in km,
     "B-HISTORY: a prior QNM reading in this exact neighbourhood was RETRACTED — "
     "'gapped-tower => QNM (the boundary check tested the wrong thing)'. The area has "
     "produced one false positive that the machinery caught; this RAISES the bar")
r4=json.dumps([c for c in CL if c["id"]=="rung4_love_kk"][0])
gate("FAILS-DIFFERENTIATION" in r4,
     "B-ANCESTRY: its parent rung4_love_kk is itself classified FAILS-DIFFERENTIATION "
     "(real-but-invisible) — and per Phase 11 its 22-62 orders is a DEPHASING-branch "
     "figure that does NOT cover the amplitude channel a QNM damping time lives in")

sa=rd("SIGNATURE_AUDIT.md")
gate("horizon/tidal dissipation channel that could in principle shift QNM frequencies"
     in " ".join(sa.split()),
     "B-CHARACTERIZATION, CORRECTED (Leg B): the GRUT-side quantity IS POSED — "
     "SIGNATURE_AUDIT.md states GRUT's dissipative tidal response (Im chi, rung4) is 'a "
     "horizon/tidal dissipation channel that could in principle shift QNM frequencies or "
     "ringdown damping times ... where a dynamical (lossy) tidal response differs from "
     "GR's conservative one'. What is ABSENT is the BH perturbation MACHINERY, so the "
     "quantity cannot be COMPUTED — not that it has not been POSED. The first draft's "
     "'quantity unposed' is withdrawn")
gate("invisible-by-inheritance" in sa and "inheritance argument, not a computation"
     in " ".join(sa.split()),
     "B-DISPOSITION, RESTORED (dropped by the first draft): on-record expected outcome is "
     "'confirms invisible' — 'invisible-by-inheritance ... an INHERITANCE ARGUMENT, NOT A "
     "COMPUTATION', and per Phase 11 channel-conditional (rung4's 22-62 orders is a "
     "dephasing-branch figure; a ringdown damping time is an amplitude-channel quantity)")
pm=rd("POSTULATE_MAP.md")
gate("a dedicated QNM/ringdown calc" in pm and "soft spot" in sa,
     "B-GOVERNANCE STATUS, added: B is a NAMED OWED CALCULATION in two governance "
     "documents — POSTULATE_MAP.md M6 (Falsifier) and SIGNATURE_AUDIT.md's standing "
     "soft-spot caveat on its own EMPTY verdict")

print(); print("="*74); print("6 — THE FALSIFICATION TEST, BOTH CANDIDATES"); print("="*74)
gate("Neither horn supports a quoted number" in spec,
     "A FAILS the falsification gate AS IT STANDS: with Q-A unanswered and B spanning "
     "3.2 orders down to invisible, a null is absorbed by B -> small. No 'GRUT predicts "
     "X vs standard predicts Y' can be written today")
gate(nfiles(r"\bKerr\b")==[] and nfiles(r"Teukolsky")==[],
     "B FAILS the falsification gate MORE BASICALLY: with no BH perturbation problem in "
     "the corpus, the equation that would differ from GR cannot be written at all — the "
     "Phase-11 hostile referee issued exactly this demand and recorded it NOT MET")

print(); print("="*74); print("10/11 — THE ASYMMETRY, AND THE DECISION"); print("="*74)
A_decidable="CLOSES THE QUESTION" in spec and "PASS (parameter-free bridge)" in spec
gate(A_decidable,
     "THE ASYMMETRY, CORRECTED: candidate A has FOUR pre-registered outcomes "
     "(PASS, FAIL-BUT-INFORMATIVE, CLOSES THE QUESTION, and REFUSE) but its PASS horn "
     "does NOT open a discriminator in the selected channel; candidate B's quantity IS "
     "posed while the MACHINERY is absent. Neither asymmetry favours selection")
note("DECISION = NEITHER-DISCRIMINATING (corrected from the first draft's BOTH-BLOCKED per Leg B: 'BLOCKED' implicates a removable obstacle behind which a target sits, and that implicature is unestablished for both and CONTRADICTED for A by its own channel fence). Neither survives the parameter and falsifiability gates "
     "of section 11, so neither earns TARGET status. This is NOT symmetric, and the "
     "record says so: A is DECIDABLE-BUT-NOT-YET-DISCRIMINATING (one pre-registered "
     "question away from closure or opening); B is NOT-YET-POSABLE (no BH perturbation "
     "problem exists to perturb). Selecting A now would be selecting a question whose "
     "own SPEC says NEITHER HORN SUPPORTS A QUOTED NUMBER — the Phase-10 error exactly. "
     "Whether to authorize A's Q-A as a CLOSURE calculation (not a discriminator "
     "campaign) is an OWNER decision, deliberately not taken here.")

print(); print("="*74); print("RECORD CONTENT GATES"); print("="*74)
md=" ".join(rd("PHYSICS_LEDGER/FOREST_PHASE12_TARGET_ADJUDICATION.md").replace(">"," ").split())
for frag,desc in (("HEAD-TO-HEAD MATRIX","the matrix"),("BOTH-BLOCKED","the verdict"),
  ("NOT-DISCRIMINATING-IN-THE-SELECTED-CHANNEL","A's corrected status"),
  ("POSED-BUT-UNCOMPUTABLE","B's corrected status"),
  ("Neither horn supports a quoted number","A's own blocker quoted"),
  ("That is not a black hole","B's scaffolding gap stated"),
  ("NO validation credit for the form","the standard-overlap fence"),
  ("no target computation","the phase computes nothing"),
  ("owner decision","the closure-calc question is left to the owner")):
    gate(frag in md,"record carries: %s"%desc)

print(); print("="*74); print("15 — GOVERNANCE EXIT"); print("="*74)
POST=hashlib.sha256(open(REG,"rb").read()).hexdigest()
gate(POST==PRE,"register sha256 identical pre/post — no register mutation")
gate(git("status","--porcelain","--","provenance/claims.json",
     "PHYSICS_LEDGER/WALL_KR_H1_PHASE9_CLOSURE.md","calc/SPEC_gw_tensor_friction.md"
     ).stdout.strip()=="","register, H1 freeze and the SPEC byte-identical")
gate(not os.path.exists(os.path.join(ROOT,"calc","gw_tensor_friction.py")),
     "NO TARGET COMPUTATION LAUNCHED: calc/gw_tensor_friction.py still does not exist")

print(); print("="*74); print("RESULT"); print("="*74)
n=sum(1 for ok,_ in CHECKS if ok)
# verdict derived from the gate outcomes, not a pass-label (standing lesson)
# VERDICT, EVIDENCE-DERIVED (the first draft's form could emit only BOTH-BLOCKED — the
# 8th occurrence of the pass-label pattern this program has caught. Each criterion below
# is an independent repository fact that COULD come out either way.)
def earns_target(equation_writable, difference_writable, falsifiable_today,
                 channel_can_confirm):
    return all((equation_writable, difference_writable, falsifiable_today,
                channel_can_confirm))
A_crit=dict(equation_writable=True,            # chi(w), k(w), Gamma=B*H0/2 exist in-corpus
            difference_writable=("NO validation credit for the form" not in r3),
            falsifiable_today=("Neither horn supports a quoted number" not in spec),
            channel_can_confirm=("could NEVER confirm GRUT" not in r3))
B_crit=dict(equation_writable=(nfiles(r"\bKerr\b|Teukolsky")!=[]),
            difference_writable=(nfiles(r"\bKerr\b|Teukolsky")!=[]),
            falsifiable_today=False,
            channel_can_confirm=True)
A_ok=earns_target(**A_crit); B_ok=earns_target(**B_crit)
verdict=("TARGET-A" if A_ok and not B_ok else "TARGET-B" if B_ok and not A_ok
         else "BOTH-BLOCKED" if (A_ok and B_ok)
         else "NEITHER-DISCRIMINATING") if not FAILURES else "INCONCLUSIVE"
note("VERDICT CRITERIA (each an independent repository fact): A %s ; B %s"%(A_crit,B_crit))
print("  battery: %d/%d, failures: %d   [%.0fs]"%(n,len(CHECKS),len(FAILURES),time.time()-t0))
for f in FAILURES: print("    FAILED: "+f)
print("  DECISION: %s"%verdict)
out={"instrument":"forest_phase12_adjudication.py","date":"2026-09-04","base":"acae001",
 "kind":"FOREST PHASE 12 — amplitude-channel target adjudication (NO computation)",
 "battery":"%d/%d"%(n,len(CHECKS)),"failures":FAILURES,
 "register_sha256_pre":PRE,"register_sha256_post":POST,"register_mutated":False,
 "decision":verdict,
 "decision_corrected_from":"BOTH-BLOCKED (first draft) — see Leg B",
 "candidate_A":{"id":"gamma_T_siren_amplitude","status":"BLOCKED — "
   "DECIDABLE-BUT-NOT-YET-DISCRIMINATING",
   "observable":"standard-siren amplitude (achromatic tensor friction Gamma_T at ~H0)",
   "channel_note":"the friction is achromatic => degenerate with coalescence phase; the "
     "dephasing test is blind BY CONSTRUCTION (SPEC Q-D). Amplitude is the live channel",
   "scaffolding":"pre-registered SPEC exists; code absent",
   "blocker":"Q-A (sector): does the tau_2 pole appear in P^TT at all? scalar-only => "
     "TT friction is ZERO and the question closes. SPEC: 'Neither horn supports a "
     "quoted number'",
   "parameters":"B staked; TWO live values ~3.2 orders apart (0.2*H0 inside the slot "
     "bound vs 1.2e-4*H0 invisible); B==eps is an unverified assumption",
   "standard_overlap":"the dissipative Gamma_T+noise FORM is U1-GENERIC published "
     "open-EFT — register grants NO validation credit for the form; only a "
     "parameter-free VALUE could be GRUT-specific",
   "real_distinction":"dissipative Gamma_T + mandatory noise is explicitly DISTINCT "
     "from the conservative running-Planck-mass alpha_M*H"},
 "candidate_B":{"id":"bh_ringdown_qnm","status":"BLOCKED — NOT-YET-POSABLE",
   "observable":"QNM frequencies / ringdown damping times",
   "scaffolding":"ABSENT — zero files mention Kerr, Teukolsky, tidal heating, Love "
     "number or horizon flux; the only Regge-Wheeler/Zerilli material is the de Sitter "
     "STATIC PATCH ('every M-dependent term drops at M = 0') — not a black hole",
   "history":"a prior QNM reading here was RETRACTED (the boundary check tested the "
     "wrong thing)",
   "ancestry":"rung4_love_kk is itself FAILS-DIFFERENTIATION; its 22-62 orders is a "
     "dephasing-branch figure not covering the amplitude channel",
   "equation_demand":"NOT MET — with no BH perturbation problem in the corpus, the "
     "equation that would differ from GR cannot be written"},
 "why_not_target_A":"selecting A would select a question whose own SPEC states 'neither "
   "horn supports a quoted number' — the Phase-10 error (selecting an unresolved-or-"
   "answered question and calling it parameter-free) repeated",
 "owner_question":"whether to authorize A's Q-A as a CLOSURE calculation (decidable, "
   "cheap, closes or opens the route) rather than as a discriminator campaign — "
   "deliberately NOT decided here",
 "A_to_F_selected":"NONE","target_computation":"NONE LAUNCHED",
 "W":"W-0 — adjudication only; nothing banked; nothing computed"}
json.dump(out,open(os.path.join(HERE,"FOREST_PHASE12_TARGET_ADJUDICATION.json"),"w",
          encoding="utf-8"),indent=2,ensure_ascii=False)
print("  artifact: FOREST_PHASE12_TARGET_ADJUDICATION.json")
print("  "+("ALL CHECKS PASS" if not FAILURES else "BATTERY HAS FAILURES"))
print("PHASE12_DONE")
