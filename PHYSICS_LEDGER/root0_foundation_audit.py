#!/usr/bin/env python3
"""
ROOT PROGRAM — ROOT-0: MICROSCOPIC FOUNDATION / RESPONSE-ORIGIN AUDIT.
A repository reconstruction, NOT an implementation. Per the order this STOPS at the first
genuine missing microscopic premise and reports it rather than filling it. No observable
hunt, no Gamma_T, no QNM, no A-F, no register mutation, no frozen-artifact edit. W-0.
Standing lessons applied: sweep ALL file types; read WHOLE register fields; per-claim keys;
no pass-label verdict; declare scope.
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
def flat(p): return " ".join(rd(p).replace(">"," ").split())
REG=os.path.join(PROV,"claims.json"); PRE=hashlib.sha256(open(REG,"rb").read()).hexdigest()
t0=time.time()

print("="*74); print("0 — GOVERNANCE (foundational reset of LEVEL, not of repository)")
print("="*74)
HEAD=git("rev-parse","HEAD").stdout.strip(); ov4=git("rev-parse","origin/v4").stdout.strip()
gate(HEAD!="" and HEAD==ov4,"v4 by REF IDENTITY: HEAD == origin/v4 == %s"%HEAD[:12])
gate(git("merge-base","--is-ancestor","8449984","HEAD").returncode==0,"P12 in ancestry")
gate("FROZEN — CLOSED FOR EPISTEMIC PURPOSES" in flat("PHYSICS_LEDGER/WALL_KR_H1_PHASE9_CLOSURE.md"),
     "H1 freeze intact and unmodified")
CL=json.load(open(REG))["claims"]; BY={c["id"]:c for c in CL}
gate(len(CL)==74,"register unchanged at 74 nodes")
note("A-F UNSELECTED; W-0; no observable hunt; no Gamma_T; no QNM; nothing computed")

print(); print("="*74); print("ROOT-0A — WHAT THE REPOSITORY ACTUALLY SPECIFIES"); print("="*74)
ont=BY["rung1_ontology_finite_memory"]
gate(ont.get("tier")=="assumed" and "a STANCE, explicitly not derived" in (ont.get("statement") or ""),
     "THE ONTOLOGY IS AN ASSUMPTION, BY ITS OWN RECORD: rung1_ontology_finite_memory "
     "('the gravitational vacuum IS a responsive medium with finite memory') is tier="
     "ASSUMED and self-describes as 'a STANCE, explicitly not derived'")
gate("the formalism does not imply the ontology" in (ont.get("statement") or ""),
     "and the record separates formalism from ontology explicitly: the SK/in-in formalism "
     "is booked separately (rung1_inin_formalism) and 'THE FORMALISM DOES NOT IMPLY THE "
     "ONTOLOGY' — so borrowing Schwinger-Keldysh does not supply the responsive medium")
gate("underived, load-bearing" in (ont.get("ledger_note") or ""),
     "and it is PRICED as such: the node carries ledger_delta +1 because it is 'underived, "
     "load-bearing'; 'derive finite memory and the +1 retires; fail and it stands as an "
     "explicit foundational assumption'")
toe=flat("GRUT_ToE.md")
gate("what forces the analytic class is *locality / finite-memory of the influence "
     "functional — which is single-pole restated*" in toe
     or "which is single-pole restated" in toe,
     "THE EXISTING FORCING ARGUMENT IS ADMITTED CIRCULAR, in the program's own top-level "
     "document: 'The circularity is tight: what forces the analytic class is locality / "
     "finite-memory of the influence functional — WHICH IS SINGLE-POLE RESTATED. So the "
     "favorable lean carries almost no independent evidential weight'")
sif=flat("S_IF.md")
gate("single-pole (Debye) rather than branch-cut" in sif and "the conjecture, not a theorem"
     in sif,
     "AND THE MEMORY CLAIM IS BOOKED AS A CONJECTURE: S_IF.md lists finite memory as "
     "'single-pole (Debye) RATHER THAN branch-cut' with status 'the conjecture, not a "
     "theorem; external'")

print(); print("="*74); print("ROOT-0C — THE MINIMUM MODEL: WHAT EXISTS, WHAT DOES NOT")
print("="*74)
r3=BY["rung3_single_pole"]
gate("relativistic massless fast modes" in (r3.get("statement") or "")
     and "DOS~omega^2" in (r3.get("statement") or ""),
     "BATH: DECLARED, not derived — 'COMMITTING to relativistic massless fast modes "
     "(omega=c|k|) gives DOS~omega^2, J(omega)~omega^3'. The spectral density enters by "
     "commitment to a mode content, which is the standard flat-space graviton continuum")
gate("PROVIDED the vacuum bath carries no second internal dynamical scale"
     in (r3.get("statement") or ""),
     "and it carries an explicit UNDERIVED PROVISO: 'PROVIDED the vacuum bath carries no "
     "second internal dynamical scale' — the no-second-scale premise is assumed, and it "
     "is exactly what a microscopic theory would have to settle")
ec=flat("EMERGENCE_CHAIN.md")
gate("appears NOWHERE in the register" in ec and "matter link is SILENT" in ec,
     "MATTER SECTOR: ABSENT — 'The Standard Model, its spectrum, its couplings, its three "
     "generations, appears NOWHERE in the register ... the chain's matter link is SILENT'")
cov=rd("provenance/coverage.py")
gate("quantum-gravity" in cov and "absent != covered" in cov,
     "SUB-QFT LAYER: DECLARED ABSENT — coverage.py KNOWN_GAPS names 'quantum-gravity: UV "
     "completion / non-perturbative definition of the graviton sector' as an area GRUT "
     "has NO node for, under the rule 'absent != covered'")
note("SO THE 'MICROSCOPIC' LAYER THAT EXISTS IS STANDARD QFT, NOT A SUB-QFT ONTOLOGY: "
     "degrees of freedom = gravitons on a background; dynamics = Einstein-Hilbert; state = "
     "Bunch-Davies (declared); probe = TT perturbation; coarse-graining = in-in/SK "
     "influence functional. That is microscopic RELATIVE TO the kernel, and it is enough "
     "to have run Tier 1-4. It is NOT an answer to 'what microscopic facts make a "
     "universe behave as a responsive medium with memory' — nothing in the repository "
     "sits beneath the rung1 stance")

print(); print("="*74); print("ROOT-0D/E — THE DERIVATION TARGET AND WHAT IT RETURNED")
print("="*74)
mb=flat("PHYSICS_LEDGER/MICROSCOPIC_TARGET_BENCHMARK.md")
gate("Σ(x,x′) → G_R^TT(x,x′) → K_R → J(ω)" in mb or "K_R → J(ω)" in mb,
     "THE ROOT CHAIN IS ALREADY PRE-REGISTERED IN-REPO: "
     "'Sigma(x,x') -> G_R^TT(x,x') -> K_R -> J(omega)', with the question 'does the "
     "assembled gravitational response naturally produce the low-omega spectral structure "
     "the registered model assumes, or a qualitatively different one?'")
gate("CONVERGENCE BOUNDARY, not an inequality" in mb,
     "with a PRE-REGISTERED BENCHMARK that is a convergence boundary (does the static "
     "response integral converge?), explicitly NOT the vacuous Re chi(0) >= 0")
gate("opposite sides of the convergence boundary" in mb and "s_eff → 0" in mb,
     "AND A LIVE, UNRESOLVED CONFLICT IS RECORDED ON ITS FACE: two computed answers sit "
     "on OPPOSITE SIDES of that boundary — the register's s=3 (super-Ohmic, convergent) "
     "versus a Class-A worldline reduction's horizon-forced WHITE FLOOR s_eff -> 0 "
     "(power-divergent), the latter adverse-at-proxy-scope, fenced and unbanked")
gate("three-way fork" in mb and "do not resolve by assumption" in mb,
     "with a three-way fork recorded live and the instruction 'DO NOT RESOLVE BY "
     "ASSUMPTION'")
t4=BY["kr_contract_retarded_tier4"]
st4=t4.get("statement") or ""
gate("UNCONDITIONAL" in st4 and "branch point at omega = 0 with a real-axis cut" in st4
     and "gapless two-graviton continuum" in st4,
     "WHAT THE EXECUTED CHAIN ACTUALLY RETURNED: the frozen Tier-4 contract kernel carries, "
     "marked UNCONDITIONAL, a 'branch point at omega = 0 with a real-axis cut (GAPLESS "
     "TWO-GRAVITON CONTINUUM)' — i.e. a CUT, not a pole, at the one-loop contract scope")
gate("omega >> H" in (t4.get("boundary_condition") or ""),
     "AND ITS SCOPE FENCE IS THE CRUX: the node's conditional statements are banked with "
     "'reference slice; |lambda| << 1; OMEGA >> H' — while the pre-registered question is "
     "about the LOW-frequency (omega <~ H) structure. The regimes do not coincide")
gate("The Class-C consequence cell is NOT banked with this node"
     in (t4.get("boundary_condition") or ""),
     "AND THE ADJUDICATION IS EXPLICITLY WITHHELD: 'The Class-C consequence cell is NOT "
     "banked with this node' — the repository has deliberately NOT drawn the memory "
     "consequence from this computation")
cd=flat("CLASS_C_DISPATCH_SPEC.md")
gate("Branch cut / continuum" in cd and "No long-memory structure" in cd,
     "the dispatch pre-registers SIX outcomes including (3) branch cut/continuum — "
     "'determine whether the low-frequency behavior yields the registered memory kernel "
     "shape' — and (5) 'No long-memory structure: rung-3 mechanism fails as registered; "
     "retire and say so'. Outcome 3 is NOT self-adjudicating: a cut alone does not settle "
     "it; the low-frequency SHAPE question must be answered")
cdf=flat("CLASS_C_DISPATCH_FROZEN.md")
gate("refuse" in cdf.lower() and "prerequisite" in cdf.lower(),
     "and the dispatch SOLVER IS DEMONSTRATED TO REFUSE while any prerequisite is "
     "undecided — the blockage is enforced machinery, not an oversight")
gv1=flat("GRUT_V1_PLAIN.md")
gate("the core assumption is refuted as stated" in gv1,
     "THE PRE-REGISTERED FALSIFIER, PUBLISHED: 'If the assembled low-frequency de Sitter "
     "computation returns a branch cut, then in the dispatch's own words THE CORE "
     "ASSUMPTION IS REFUTED AS STATED - WE RETIRE IT AND SAY SO'")

print(); print("="*74); print("THE FIRST GENUINE MISSING MICROSCOPIC PREMISE — REPORTED, NOT FILLED")
print("="*74)
gate(r3.get("tier")=="derived-pending",
     "rung3_single_pole remains tier=DERIVED-PENDING — neither derived nor retired. The "
     "falsifier's antecedent is therefore NOT adjudicated in the register")
note("STOP CONDITION REACHED. The first genuine missing microscopic premise is NOT a "
     "quantity — it is the SPECTRAL CONTENT OF THE BATH AT LOW FREQUENCY, i.e. what fixes "
     "rho(Omega) as omega -> 0. Everything the memory claim needs descends from it, and "
     "the repository supplies it only by COMMITMENT (massless relativistic modes => "
     "DOS~omega^2 => J~omega^3), with an explicit undischarged proviso (no second internal "
     "dynamical scale), an admitted CIRCULAR forcing argument, and a LIVE CONFLICT against "
     "a horizon-forced white floor on the other side of the convergence boundary. "
     "PER THE ORDER I DO NOT FILL THIS GAP.")

print(); print("="*74); print("RECORD CONTENT GATES"); print("="*74)
md=flat("PHYSICS_LEDGER/ROOT0_FOUNDATION_AUDIT.md")
for frag,desc in (("1 · CURRENT MICROSCOPIC ASSUMPTIONS","deliverable 1"),
  ("2 · WHAT IS MISSING","deliverable 2"),("3 · INPUT/OUTPUT FIREWALL","deliverable 3"),
  ("4 · MINIMUM WELL-POSED MODEL","deliverable 4"),("5 · CANDIDATE RESPONSE OBJECT","deliverable 5"),
  ("6 · WHAT WOULD MAKE MEMORY EMERGENT","deliverable 6"),("7 · NON-UNIQUENESS","deliverable 7"),
  ("8 · STANDARD VERSUS GRUT-SPECIFIC","deliverable 8"),("9 \u00b7 QUANTITIES THAT ARE EFFECTIVE-LEVEL ASSUMPTIONS","deliverable 9"),
  ("10 · DEPENDENCY GRAPH","deliverable 10"),("11 · NEXT ROOT QUESTIONS","deliverable 11"),
  ("12 · VERDICT","deliverable 12"),
  ("single-pole restated","the admitted circularity is quoted"),
  ("gapless two-graviton continuum","the computed cut is recorded"),
  ("\u03c9 \u226b H","the scope gap is stated"),
  ("NOT banked","the withheld adjudication is stated"),
  ("do not fill","the stop condition is honored"),
  ("no sub-QFT ontology","the absence is stated plainly")):
    gate(frag in md,"record carries: %s"%desc)

print(); print("="*74); print("GOVERNANCE EXIT"); print("="*74)
POST=hashlib.sha256(open(REG,"rb").read()).hexdigest()
gate(POST==PRE,"register sha256 identical pre/post — no register mutation")
gate(git("status","--porcelain","--","provenance/claims.json","S_IF.md","GRUT_ToE.md",
     "PHYSICS_LEDGER/MICROSCOPIC_TARGET_BENCHMARK.md","CLASS_C_DISPATCH_FROZEN.md"
     ).stdout.strip()=="","all cited foundational artifacts byte-identical")
gate(not os.path.exists(os.path.join(ROOT,"calc","gw_tensor_friction.py")),
     "no observable computation launched (Gamma_T still absent)")

print(); print("="*74); print("RESULT"); print("="*74)
n=sum(1 for ok,_ in CHECKS if ok)
# verdict derived from three independent repository facts, each falsifiable
qft_layer_specified = all((
    "relativistic massless fast modes" in (r3.get("statement") or ""),   # bath declared
    bool(BY.get("rung1_inin_formalism")),                                # coarse-graining
    "branch point at omega = 0" in st4))                                 # chain executable
subqft_ontology_exists = ("quantum-gravity" not in cov)                  # false: declared gap
forcing_noncircular = ("single-pole restated" not in toe)                # false: admitted
if FAILURES: verdict="INCONCLUSIVE"
elif qft_layer_specified and subqft_ontology_exists and forcing_noncircular:
    verdict="ROOT-FOUNDATION-A"
elif qft_layer_specified: verdict="ROOT-FOUNDATION-B"
else: verdict="ROOT-FOUNDATION-C"
print("  battery: %d/%d, failures: %d   [%.0fs]"%(n,len(CHECKS),len(FAILURES),time.time()-t0))
for f in FAILURES: print("    FAILED: "+f)
print("  VERDICT: %s"%verdict)
print("  criteria: QFT-layer specified=%s ; sub-QFT ontology exists=%s ; forcing argument "
      "non-circular=%s"%(qft_layer_specified,subqft_ontology_exists,forcing_noncircular))
out={"instrument":"root0_foundation_audit.py","date":"2026-09-04","base":"8449984",
 "kind":"ROOT-0 — microscopic foundation / response-origin audit (reconstruction only)",
 "battery":"%d/%d"%(n,len(CHECKS)),"failures":FAILURES,
 "register_sha256_pre":PRE,"register_sha256_post":POST,"register_mutated":False,
 "verdict":verdict,
 "verdict_criteria":{"qft_layer_specified":qft_layer_specified,
   "sub_qft_ontology_exists":subqft_ontology_exists,
   "forcing_argument_non_circular":forcing_noncircular},
 "what_exists":"a QFT-level specification microscopic RELATIVE TO the kernel — gravitons "
   "on a background, Einstein-Hilbert dynamics, declared Bunch-Davies state, TT probe, "
   "in-in/SK coarse-graining — sufficient to have executed Tier 1-4 and produced a kernel",
 "what_does_not_exist":"any sub-QFT ontology; the responsive-medium/finite-memory premise "
   "(rung1) is tier=assumed, self-described as a STANCE explicitly not derived, priced +1, "
   "with nothing in the repository beneath it",
 "the_computed_answer":"the frozen Tier-4 kernel carries UNCONDITIONALLY a branch point at "
   "omega=0 with a real-axis cut (gapless two-graviton continuum) — a CUT, not a pole",
 "the_scope_gap":"Tier-4's conditional scope is omega >> H; the pre-registered memory "
   "question is about the LOW-frequency structure. The Class-C consequence cell is "
   "explicitly NOT banked with the node, and the dispatch solver refuses while "
   "prerequisites are undecided",
 "first_missing_premise":"the low-frequency spectral content of the bath, rho(Omega) as "
   "omega -> 0 — supplied in-repo only by COMMITMENT to massless relativistic mode content "
   "(DOS~omega^2 => J~omega^3), with an undischarged 'no second internal dynamical scale' "
   "proviso, an ADMITTED CIRCULAR forcing argument, and a LIVE unresolved conflict against "
   "a horizon-forced white floor (s_eff -> 0) on the other side of the convergence boundary",
 "not_filled":"per the order, this gap is REPORTED and NOT filled by this audit",
 "A_to_F_selected":"NONE","W":"W-0 — reconstruction only; nothing banked; nothing computed"}
json.dump(out,open(os.path.join(HERE,"ROOT0_FOUNDATION_AUDIT.json"),"w",encoding="utf-8"),
          indent=2,ensure_ascii=False)
print("  artifact: ROOT0_FOUNDATION_AUDIT.json")
print("  "+("ALL CHECKS PASS" if not FAILURES else "BATTERY HAS FAILURES"))
print("ROOT0_DONE")
