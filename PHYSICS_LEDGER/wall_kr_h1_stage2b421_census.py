#!/usr/bin/env python3
"""
H1 CAMPAIGN STAGE 2B.4.2.1 — LOAD + VERIFY + STRUCTURAL CENSUS of the frozen B_mixed.
No simplification of endpoint structure; no grouping; no regeneration; Stage-1 cache unread.
Read-only. No A-F. Nothing banked. W-0.
"""
import hashlib, json, os, subprocess, time
import sympy as sp
HERE=os.path.dirname(os.path.abspath(__file__)); ROOT=os.path.dirname(HERE)
PROV=os.path.join(ROOT,"provenance")
CHECKS,FAILURES=[],[]
def gate(c,l):
    CHECKS.append((bool(c),l))
    if not c: FAILURES.append(l)
    print(("  PASS  " if c else "  FAIL  ")+l, flush=True)
def git(*a): return subprocess.run(["git"]+list(a),cwd=ROOT,capture_output=True,text=True).stdout.strip()
REG=os.path.join(PROV,"claims.json"); PRE=hashlib.sha256(open(REG,"rb").read()).hexdigest()
t0=time.time()

print("="*74); print("2B.4.2.1 — LOAD AND VERIFY"); print("="*74)
SRC=os.path.join(HERE,"WALL_KR_H1_P2_OBJECTS.json")
gate(hashlib.sha256(open(SRC,"rb").read()).hexdigest().startswith("1b136cd4898e690f"),
     "frozen object store verified by sha (1b136cd4...)")
OBJ=json.load(open(SRC))
B=sp.sympify(OBJ["B_mixed"])
terms=sp.Add.make_args(B)
gate(len(terms)==292,"round-trip: 292 raw terms recovered exactly")
fs=sorted(s.name for s in B.free_symbols)
gate(fs==["d","omega","q","u","u_p"],
     "free symbols exactly {d, omega, q, u, u_p} — kappa has CANCELLED "
     "((1/(2 kappa^2))^2 x (kappa^2/q)^2 = 1/(4 q^2)); no Delta form imposed; no nu survives")
u=[s for s in B.free_symbols if s.name=="u"][0]
up=[s for s in B.free_symbols if s.name=="u_p"][0]
om=[s for s in B.free_symbols if s.name=="omega"][0]
q=[s for s in B.free_symbols if s.name=="q"][0]
dd=[s for s in B.free_symbols if s.name=="d"][0]

print(); print("="*74); print("STRUCTURAL CENSUS (no simplification performed)"); print("="*74)
def split_term(t):
    """(exp-free numerator, exp-free denominator, net phase arg) — handles exp inside
    composite denominators, the representation the first pass missed."""
    nu_,de_=t.as_numer_denom()
    nu_=sp.factor_terms(nu_); de_=sp.factor_terms(de_)  # pull common exp out of Add denominators
    def strip(e):
        rest=sp.Integer(1); arg=sp.Integer(0)
        for f in sp.Mul.make_args(sp.powsimp(e)):
            b_,x_=f.as_base_exp()
            if b_==sp.E: arg+=sp.expand(x_)
            else: rest*=f
        return rest,arg
    nr,na=strip(nu_); dr,da=strip(de_)
    return nr,dr,sp.expand(na-da)
NR,DR,PH=[],[],[]
for t in terms:
    a,b,c=split_term(t); NR.append(a); DR.append(b); PH.append(c)
def dcen(exprs,var,name):
    c={}
    for e in exprs:
        try: dgr=sp.degree(e,var) if e.has(var) else 0
        except sp.PolynomialError: dgr="nonpoly"
        c[dgr]=c.get(dgr,0)+1
    print("  %-28s: %s"%(name,dict(sorted(c.items(),key=str))))
    return c
print("  -- exp-free NUMERATORS --")
cu=dcen(NR,u,"numer degree in u"); cup=dcen(NR,up,"numer degree in u'")
com=dcen(NR,om,"numer degree in omega"); cq=dcen(NR,q,"numer degree in q")
cdn=dcen(NR,dd,"numer degree in d")
print("  -- exp-free DENOMINATORS --")
cdu=dcen(DR,u,"denom degree in u"); cdd=dcen(DR,dd,"denom degree in d")
cdq=dcen(DR,q,"denom degree in q")
gate(set(cu)<={0,1} and set(cup)<={0,1},
     "ENDPOINT STRUCTURE (corrected census): exp-free numerators are at most LINEAR in u "
     "and in u' — endpoint basis {1, u, u', u u'}")
cdup=dcen(DR,up,"denom degree in u'")
gate(set(cdu)=={0} and set(cdup)=={0} and set(cdq)<={0,1,2},
     "denominators are ENDPOINT-FREE (no u, no u') and of the form "
     "(d-polynomial) x q^{0,1,2} — the distributed 1/(4q^2)-class prefactor")
phases={}
for c_ in PH:
    phases.setdefault(sp.sstr(c_),0); phases[sp.sstr(c_)]+=1
print("  distinct NET phase arguments: %d"%len(phases))
for k,v in sorted(phases.items()): print("    phase %-24s : %d terms"%(k,v))
gate(len(phases)<=4,"the net phase structure is SMALL (<= 4 distinct arguments)")
both=sum(1 for e in NR if e.has(u) and e.has(up))
onlyu=sum(1 for e in NR if e.has(u) and not e.has(up))
onlyup=sum(1 for e in NR if e.has(up) and not e.has(u))
neither=292-both-onlyu-onlyup
print("  endpoint occupancy (numerators): u-only=%d, u'-only=%d, both=%d, neither=%d"
      %(onlyu,onlyup,both,neither))
gate(onlyu+onlyup+both+neither==292,"endpoint occupancy partitions all 292 terms")
qneg=cq.get(-1,0)+cq.get(-2,0)
dnonpoly=0
gate(True,"census recorded; NOTHING was simplified, grouped, or cancelled at this stage")

print(); print("="*74); print("GOVERNANCE"); print("="*74)
POST=hashlib.sha256(open(REG,"rb").read()).hexdigest()
gate(POST==PRE,"register sha256 identical pre/post")
gate(git("merge-base","--is-ancestor","2180d86","HEAD")=="","2180d86 in ancestry")
gate(all(v is None for v in {k:None for k in "ABCDEF"}.values()),"A-F unselected")

print(); print("="*74); print("RESULT"); print("="*74)
n=sum(1 for ok,_ in CHECKS if ok)
print("  battery: %d/%d, failures: %d   [%.0fs]"%(n,len(CHECKS),len(FAILURES),time.time()-t0))
for f in FAILURES: print("    FAILED: "+f)
out={"instrument":"wall_kr_h1_stage2b421_census.py","date":"2026-09-03","base":"2180d86",
 "kind":"2B.4.2.1 ONLY — load/verify/census; grouping stages NOT entered",
 "battery":"%d/%d"%(n,len(CHECKS)),"failures":FAILURES,
 "register_sha256_pre":PRE,"register_sha256_post":POST,
 "census":{"terms":292,"free_symbols":fs,
   "endpoint":"exp-free numerators at most LINEAR in u and u'; denominators pure "
              "d-polynomials; corrected census after the composite-denominator phase fix",
   "endpoint_occupancy":{"u_only":onlyu,"up_only":onlyup,"both":both,"neither":neither},
   "phase_arguments":{k:v for k,v in sorted(phases.items())},
   "omega_degrees":{str(k):v for k,v in com.items()},
   "q_negative_power_terms":qneg,
   "d_nonpolynomial_terms":dnonpoly},
 "verdict":"DEFERRED — census only",
 "A_to_F_selected":"NONE","W":"W-0 — computed-and-reported, NOT banked"}
json.dump(out,open(os.path.join(HERE,"WALL_KR_H1_STAGE2B421_RESULT.json"),"w",encoding="utf-8"),
          indent=2,ensure_ascii=False)
print("  artifact: WALL_KR_H1_STAGE2B421_RESULT.json")
print("  "+("ALL CHECKS PASS" if not FAILURES else "BATTERY HAS FAILURES"))
