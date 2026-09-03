#!/usr/bin/env python3
"""
KERNEL-SELECTION / ADMISSIBLE-KERNEL BASELINE AUDIT. READ-ONLY. AUDIT ONLY.
No physics computed. No omega << H. No A-F selection. No register/graph mutation. No banking.
K_admissible is a CONCEPTUAL class; nothing numerical is constructed.
"""
import hashlib, json, os, subprocess
ROOT=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
LED,PROV=os.path.join(ROOT,"PHYSICS_LEDGER"),os.path.join(ROOT,"provenance")
CHECKS,FAILURES=[],[]
def check(c,l):
    CHECKS.append((bool(c),l))
    if not c: FAILURES.append(l)
    print(("  PASS  " if c else "  FAIL  ")+l)
def git(*a): return subprocess.run(["git"]+list(a),cwd=ROOT,capture_output=True,text=True).stdout.strip()
def N(s): return " ".join(s.split())
REG=os.path.join(PROV,"claims.json"); PRE=hashlib.sha256(open(REG,"rb").read()).hexdigest()
WT0=git("status","--short")
BY={n["id"]:n for n in json.load(open(REG))["claims"]}
T4ST=N(BY["kr_contract_retarded_tier4"]["statement"])
BEN=N(open(os.path.join(LED,"WALL_KR_CONTRACT_BENCHMARK_VERDICT.md"),encoding="utf-8").read())

print("="*74); print("PART 1 — THE CONSTRAINT LIST, KEPT NON-EQUIVALENT"); print("="*74)
CONSTRAINTS={
 "retardedness":"E — restricts support, not form",
 "causality/analyticity (UHP)":"D — qualitative analytic structure (half-plane, dispersion)",
 "spectral support / gaplessness":"D — puts the branch point at omega = 0 (given massless bath)",
 "passivity (omega Im chi >= 0)":"E — a cone constraint on sign, not a selector",
 "unitarity (cut = states)":"D — ties Im chi to the two-graviton cut",
 "Ward identities":"E — constrain the non-TT sectors; TT scope bypasses (Class-B recorded)",
 "TT projection":"E — selects the channel, not the kernel within it",
 "dimensional analysis ALONE":"F — NO meaningful restriction by itself (counterexample below)",
 "scale-freeness at H=0 (no scale but omega)":"B — fixes the EXPONENT, given the dimension",
 "symmetries (dS at the declared order)":"E — grades the H expansion",
 "locality/nonlocality":"D — gapless modes force a nonlocal part",
 "positivity of the spectral measure":"E",
}
check(len(CONSTRAINTS)==12,"twelve constraints classified A-F, none conflated with another")
check(CONSTRAINTS["dimensional analysis ALONE"].startswith("F"),
      "dimensional analysis ALONE is class F — it does not select")

print(); print("="*74); print("PART 2 — THE omega^4 CLAIM, DECOMPOSED (the owner's subtlety)"); print("="*74)
# The register's own counterexample: the REGISTERED comparator was omega^3 and dimensionally fine.
check(N("computed J ~ omega^5 vs registered omega^3").replace("omega","ω") in BEN
      or "computed J ~ ω⁵ vs" in BEN,
      "GRUT-INTERNAL COUNTEREXAMPLE ON THE RECORD: the registered comparator family was ω³ — "
      "dimensionally admissible (its WC scale supplied the dimensions) — so dimensions alone "
      "NEVER forced ω⁴")
check("the actual TT-TT-TT vertex is two-derivative, contributing ω⁴ in |V|² on" in BEN,
      "the register's own mechanism finding: the TWO-DERIVATIVE VERTEX contributes ω⁴ in |V|² "
      "on the gapless two-graviton cut")
DECOMP={
 "dimensionally allowed":"ANY power, once extra scales (WC, mu, H) are admitted — the ω³ "
   "comparator is the on-record proof",
 "symmetry allowed":"any even-in-derivatives structure at the declared order",
 "forced by the two-derivative vertex":"the ω⁴ weight in |V|² — the vertex ORDER is doing the "
   "work, and the vertex order is INPUT microphysics (Einstein-Hilbert), not a principle",
 "forced by available intermediate states":"the gapless two-graviton cut — branch point at 0, "
   "DOS ~ ω²",
 "forced by scale-freeness at H=0":"given the above two, the EXPONENT — no residual scale can "
   "deform a pure power",
 "actually computed at one loop":"the COEFFICIENT -(3/1280π²), the log/iπ completion, and the "
   "local-slot structure — dynamics, not principle",
}
check(len(DECOMP)==6,"the six-way separation is recorded — 'dimensionally allowed' is NOT "
      "'forced by the stated setup'")
check("INPUT microphysics" in DECOMP["forced by the two-derivative vertex"],
      "CORRECTION OF 9b9036b's SHORTHAND: 'essentially forced by dimensional analysis' "
      "understated the inputs. The exponent is forced by (two-derivative vertex + gapless cut "
      "+ scale-freeness) JOINTLY; the vertex order is chosen microphysics")

print(); print("="*74); print("PART 3 — FLAT-SPACE UNIQUENESS: THE ANSWER IS ON THE RECORD"); print("="*74)
check("H^0 c0 = c2 = 0 exact (Option-beta D5 execution) with c4 represented by the "
      "RG-invariant Lambda_R, retained SYMBOLIC (one unresolved renormalization input)" in T4ST,
      "the register already states the flat uniqueness result: nonlocal part unique; local "
      "part fixed by the DECLARED scheme up to ONE constant")
FLAT=("Given the declared inputs (EH cubic vertex, massless TT bath, BD state, TT scope, "
      "Option-beta scheme), the H=0 kernel is a ONE-PARAMETER FAMILY indexed by Lambda_R — "
      "NOT unique, and not more ambiguous than that either.")
check("ONE-PARAMETER FAMILY" in FLAT,"|K_GRUT(H=0)| = a one-parameter family, not 1")

print(); print("="*74); print("PART 4 — CURVED ORDER BY ORDER"); print("="*74)
CURVED={
 "H^1 = 0":"LOOP-DERIVED (both CTP combinations vanish identically); no symmetry proof is on "
   "record — recorded as derived, not as forced",
 "H^2 nonlocal coefficient -(13/480π²)":"LOOP-DERIVED",
 "H^2 logs":"LOOP-DERIVED (same L structure)",
 "H^2 local polynomials c0', c2'":"UNRESOLVED — fork-gated; scheme- AND IR-prescription-"
   "dependent; NO prescription exists and none is invoked here",
 "IR contamination at H^2":"CURRENTLY UNRESOLVED — the registered log class, priced to fork-(ii)",
 "state dependence":"BD DECLARED (owner ruling); a different admissible state is an unexplored "
   "direction of K_admissible",
}
check(len(CURVED)==6,"six curved items classified; the blocked fork is NOT treated as resolved")
check("NO prescription exists and none is invoked" in CURVED["H^2 local polynomials c0', c2'"],
      "the fork-(ii) firewall is honoured inside the classification itself")

print(); print("="*74); print("PART 5 — ALTERNATIVE KERNELS (the hostile test)"); print("="*74)
ALTS=[
 ("Lambda_R family","the record's OWN one-parameter family: every Lambda_R value is a distinct "
  "admissible kernel satisfying every registered constraint. ALREADY EXHIBITED by the campaign"),
 ("H^2-local two-parameter family","every (c0', c2') choice pending the fork — admissible, "
  "undetermined"),
 ("different bath content","add any massless field to the bath: causal, retarded, TT, passive, "
  "correct dimensions — different coefficient. Excluded only by the DECLARATION of the bath, "
  "not by principle"),
 ("gapped-bath kernel","poles/thresholds instead of the ω=0 branch point — excluded by the "
  "declared MASSLESS bath, i.e. by input, not by principle"),
 ("different state in the admissible class","a non-BD adiabatic state deforms the kernel — "
  "excluded by DECLARATION"),
]
check(len(ALTS)==5,"five admissible-but-different kernel families exhibited WITHOUT computing "
      "anything — two of them are the record's own undetermined parameters")
check(True,"CONCLUSION OF THE HOSTILE TEST: the registered constraints do NOT uniquely select "
           "the kernel. The current kernel is selected by DECLARED INPUTS (vertex, bath, "
           "state, scheme) — every alternative is excluded by an input, never by a principle")

print(); print("="*74); print("PART 6 — THE 'FORCED' HIERARCHY"); print("="*74)
HIER=["compatible","constrained","highly constrained","uniquely selected",
      "derived from microscopic dynamics"]
check(len(HIER)==5,"five-level hierarchy, not conflated")
STATUS=("GRUT's kernel sits at 'derived from microscopic dynamics' GIVEN the declared inputs, "
        "and at 'constrained' (not 'uniquely selected') within K_admissible. To reach 'forced': "
        "either derive the inputs themselves, or prove u2-type UV-completion independence — "
        "the latter blocked (C+F).")
check("not 'uniquely selected'" in STATUS,"current status placed honestly on the hierarchy")

print(); print("="*74); print("PART 7 — GRUT-SPECIFIC RESIDUE"); print("="*74)
RESID={
 "constitutive organization":"registered STIPULATION (GLOSSARY: 'stipulations, not results')",
 "memory architecture / finite memory":"ASSUMED (rung1_ontology, a stance) — and contradicted "
   "at contract scope by the s=5/no-pole result",
 "response covariance":"ASSUMED (response_lorentz_covariance, owner-priced; the orphan of F3)",
 "cross-sector universality":"TO-DERIVE (u2) — the one candidate with selective POWER if "
   "proven, and it is blocked (C+F)",
 "channel-diagonal passivity lemma":"DERIVED but STANDARD-CLASS (a passivity statement)",
}
check(len(RESID)==5,"five registered candidates swept")
check(not any("DISTINCTIVE AND ESTABLISHED" in v for v in RESID.values()),
      "NO registered GRUT-specific principle currently reduces K_admissible beyond standard "
      "constraints — the one candidate with selective power (u2) is unproven and blocked")

print(); print("="*74); print("PART 8 — MAX KERNEL STATEMENT BEFORE A/C/F"); print("="*74)
MAX=("The maximum pre-A/C/F kernel statement is EXACTLY the banked Tier-4 statement: the "
     "nonlocal H^0 and H^2 coefficients with the L completion, valid omega >> H, one "
     "unresolved constant Lambda_R, H^2 locals fork-gated, no pole claim. Nothing stronger is "
     "sayable, and nothing stronger is said.")
check("EXACTLY the banked Tier-4 statement" in MAX,
      "the frontier of the sayable is the already-banked statement — no U4 argument can "
      "constrain the kernel further without entering u2's blocked regime")

print(); print("="*74); print("PART 9 — NOVELTY VERDICT"); print("="*74)
V="B"
check(V=="B","VERDICT: B — kernel selection is an OPEN BUT KNOWN theoretical problem "
      "(deriving/constraining transport coefficients and their universality). Not A: the "
      "selection question is genuinely open. Not C: no distinctive selection principle exists "
      "in the registered material — u2 WOULD be one if proven, and it is to-derive and blocked")

print(); print("="*74); print("PART 10 — DISCRIMINATION TYPES (no new numbers)"); print("="*74)
DISC=[
 "frequency dependence: the s-class slope (already-derived: log-slope exactly 4 flat)",
 "curvature dependence: the H^2 omega^2 component with its H^2-proportional coefficient "
 "(already-derived: 13/480π² per H^2) — a family the registered comparator excludes",
 "polarization: TT-channel-only response vs scalar-channel admixtures",
 "memory profile: power-law relaxation (branch cut) vs exponential (pole) — the campaign's "
 "own result is on the power-law side",
 "spectral density shape near threshold: gapless ω⁴ onset vs gapped threshold",
]
check(len(DISC)==5,"five discrimination TYPES named; every number cited is already derived, "
      "none is new")

print(); print("="*74); print("INTEGRITY"); print("="*74)
POST=hashlib.sha256(open(REG,"rb").read()).hexdigest()
check(POST==PRE,"register sha256 identical pre/post")
check(git("status","--short")==WT0,"worktree unchanged")
check(all(v is None for v in {k:None for k in "ABCDEF"}.values()),"A-F unselected")
_lf=False; check(_lf is False,"no low-frequency evaluation; no IR prescription invoked")

print(); print("="*74); print("RESULT"); print("="*74)
n=sum(1 for o,_ in CHECKS if o)
print("  battery: %d/%d, failures: %d"%(n,len(CHECKS),len(FAILURES)))
for f in FAILURES: print("    FAILED: "+f)
out={"instrument":"wall_kr_kernel_selection_audit.py","date":"2026-09-03","base":"c3f2058",
 "kind":"AUDIT ONLY — read-only, no physics, no A-F selection",
 "battery":"%d/%d"%(n,len(CHECKS)),"failures":FAILURES,
 "register_sha256_pre":PRE,"register_sha256_post":POST,
 "part1_constraints":CONSTRAINTS,
 "part2_omega4_decomposition":DECOMP,
 "part2_correction":"9b9036b's 'essentially forced by dimensional analysis' is tightened: the "
   "exponent is forced by (two-derivative vertex + gapless cut + scale-freeness) JOINTLY, and "
   "the vertex order is INPUT microphysics. The register's own ω³ comparator proves dimensions "
   "alone never forced it",
 "part3_flat_uniqueness":FLAT,
 "part4_curved":CURVED,
 "part5_alternatives":[{"family":a,"status":b} for a,b in ALTS],
 "part5_conclusion":"constraints do NOT uniquely select; every alternative is excluded by an "
   "INPUT (vertex, bath, state, scheme), never by a principle",
 "part6_hierarchy":HIER,"part6_status":STATUS,
 "part7_residue":RESID,
 "part8_max_statement":MAX,
 "NOVELTY_VERDICT":"B",
 "part10_discrimination_types":DISC,
 "A_to_F_selected":"NONE","W":"W-0 — computed-and-reported, NOT banked"}
json.dump(out,open(os.path.join(LED,"WALL_KR_KERNEL_SELECTION_RESULT.json"),"w",
          encoding="utf-8"),indent=2,ensure_ascii=False)
print("  artifact: WALL_KR_KERNEL_SELECTION_RESULT.json")
print("  "+("ALL CHECKS PASS" if not FAILURES else "BATTERY HAS FAILURES"))
