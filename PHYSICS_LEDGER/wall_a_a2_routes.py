#!/usr/bin/env python3
"""A2 Phase 2: the 4d-covariant Ward enumeration, two independent routes, exact arithmetic.

W-0 FENCE: COMPUTED-AND-REPORTED, NOT BANKED. The low-omega spectral question is the
frontier; banking an in-house resolution is an automatic fail (CHARTER.md:73). This file
establishes operator-space dimensions only.

PRE-REGISTERED PREDICTION (2026-08-24, external analysis, checker-verified in scratchpad):
    full covariant basis: 6  ->  diagonal retarded-slot Ward: 3  ->  + S7 pair symmetry: 2
The code below must be ABLE to return otherwise: plants (no-Ward -> 6, both-slot Ward -> 2)
demonstrate the constraint machinery is not hard-wired to the prediction.

ROUTE A: Barnes-Rivers coefficient algebra (theta/omega projector construction).
ROUTE B: INDEPENDENT construction from raw eta/k monomials; Ward imposed as exact linear
         constraints; nullity by Fraction row-reduction. No projector objects reused.
GRADUATION CRITERION: Route A and Route B agree at every stage, at two generic k.

AUTHORSHIP DISCLOSURE: both routes implemented by the checker (Claude) after three failed
builder attempts (session boundary ab1b9ab). Routes are METHODOLOGICALLY independent but
same-author; second-author review by Ox is required before the graduation screen.

LICENSING (printed on this artifact's face, per the frozen brief):
  A: exactly-two = diagonal Ward (booked, SCDP-corrected) + S7 pair symmetry
     (S7 CURRENTLY UNBOOKED -- register's own RESULTS_operator_basis flags Onsager pair
     symmetry as 'inherited (no declaring claim)'. Where S7's license derives from
     equilibrium/KMS, the out-of-equilibrium sector must re-derive it or admit the third
     structure X_sw.)
  B: c0 = 0 is NOT licensed by anything above. EH = (1/2)k^2[P2 - 2 P0s] stands as the
     counterexample: GR's own kernel carries the scalar channel.
BARDEEN CAVEAT: this is the eta,k-only Lorentz-covariant sector. FRW/dS adds u^mu and
time dependence; the full completion is the KC5-reserved frontier. Nothing here closes it.
"""
from fractions import Fraction as F
from itertools import product as prod
import json, sys

ETA=[[F(1 if i==j==0 else (-1 if i==j else 0)) for j in range(4)] for i in range(4)]
IDX=list(prod(range(4),repeat=4))

def rank(rows):
    rows=[r[:] for r in rows if any(x!=0 for x in r)]
    rk=0; col=0; n=len(rows[0]) if rows else 0
    while rows and col<n:
        piv=next((i for i,r in enumerate(rows) if r[col]!=0),None)
        if piv is None: col+=1; continue
        rows[0],rows[piv]=rows[piv],rows[0]; pr=rows[0]
        rows=[[r[c]-r[col]/pr[col]*pr[c] for c in range(n)] for r in rows[1:]]
        rows=[r for r in rows if any(x!=0 for x in r)]
        rk+=1; col+=1
    return rk

def check(cond,msg,log):
    log.append({"check":msg,"pass":bool(cond)})
    print(("  ok  " if cond else "  FAIL")+" "+msg)
    return cond

def run(kup,log):
    klo=[sum(ETA[m][n]*kup[n] for n in range(4)) for m in range(4)]
    k2=sum(kup[m]*klo[m] for m in range(4))
    th=[[ETA[m][n]-klo[m]*klo[n]/k2 for n in range(4)] for m in range(4)]
    om=[[klo[m]*klo[n]/k2 for n in range(4)] for m in range(4)]
    T4=lambda f:{x:f(*x) for x in IDX}
    # ---------------- ROUTE A: BR structures ----------------
    A={'P2':T4(lambda m,n,r,s:F(1,2)*(th[m][r]*th[n][s]+th[m][s]*th[n][r])-F(1,3)*th[m][n]*th[r][s]),
       'P1':T4(lambda m,n,r,s:F(1,2)*(th[m][r]*om[n][s]+th[m][s]*om[n][r]+th[n][r]*om[m][s]+th[n][s]*om[m][r])),
       'P0s':T4(lambda m,n,r,s:F(1,3)*th[m][n]*th[r][s]),
       'P0w':T4(lambda m,n,r,s:om[m][n]*om[r][s]),
       'Xsw':T4(lambda m,n,r,s:th[m][n]*om[r][s]),
       'Xws':T4(lambda m,n,r,s:om[m][n]*th[r][s])}
    # ---------------- ROUTE B: raw eta/k monomials (independent construction) ----------------
    B={'S1':T4(lambda m,n,r,s:F(1,2)*(ETA[m][r]*ETA[n][s]+ETA[m][s]*ETA[n][r])),
       'S2':T4(lambda m,n,r,s:ETA[m][n]*ETA[r][s]),
       'S3':T4(lambda m,n,r,s:klo[m]*klo[n]*ETA[r][s]),
       'S4':T4(lambda m,n,r,s:ETA[m][n]*klo[r]*klo[s]),
       'S5':T4(lambda m,n,r,s:klo[m]*klo[n]*klo[r]*klo[s]),
       'S6':T4(lambda m,n,r,s:F(1,4)*(klo[m]*klo[r]*ETA[n][s]+klo[m]*klo[s]*ETA[n][r]
                                     +klo[n]*klo[r]*ETA[m][s]+klo[n]*klo[s]*ETA[m][r]))}
    def basis_rank(D): return rank([[D[nm][x] for nm in D] for x in IDX])
    def ward_dim(D, both=False):
        cols=[]
        for nm in D:
            w1=[sum(kup[m]*D[nm][(m,n,r,s)] for m in range(4)) for n,r,s in prod(range(4),repeat=3)]
            if both:
                w2=[sum(kup[r]*D[nm][(m,n,r,s)] for r in range(4)) for m,n,s in prod(range(4),repeat=3)]
                cols.append(w1+w2)
            else: cols.append(w1)
        M=[[cols[i][j] for i in range(len(D))] for j in range(len(cols[0]))]
        return len(D)-rank(M)
    def ward_s7_dim(D):
        cols=[]
        for nm in D:
            w1=[sum(kup[m]*D[nm][(m,n,r,s)] for m in range(4)) for n,r,s in prod(range(4),repeat=3)]
            anti=[D[nm][(m,n,r,s)]-D[nm][(r,s,m,n)] for m,n,r,s in IDX]
            cols.append(w1+anti)
        M=[[cols[i][j] for i in range(len(D))] for j in range(len(cols[0]))]
        return len(D)-rank(M)
    res={}
    for label,D in (("A",A),("B",B)):
        d0=basis_rank(D); dW=ward_dim(D); dWS=ward_s7_dim(D)
        dP_no=len(D)-0 if False else basis_rank(D)      # no-Ward plant = full dim
        dP_both=ward_dim(D,both=True)
        res[label]=dict(full=d0,ward=dW,ward_s7=dWS,plant_noward=dP_no,plant_both=dP_both)
        print("  Route %s: full=%d  diagonal-Ward=%d  Ward+S7=%d  [plants: no-Ward=%d, both-slot=%d]"
              %(label,d0,dW,dWS,dP_no,dP_both))
    ok=True
    ok&=check(res["A"]==res["B"],"ROUTE A == ROUTE B at every stage (graduation criterion)",log)
    ok&=check(res["A"]["full"]==6 and res["A"]["ward"]==3 and res["A"]["ward_s7"]==2,
              "chain 6 -> 3 -> 2 (pre-registered prediction; plants prove reachability of otherwise)",log)
    ok&=check(res["A"]["plant_both"]==2,"plant: both-slot Ward -> 2 (machinery not hard-wired to 3)",log)
    # survivors identified (Route A): P2,P0s,Xsw satisfy slot-Ward; P2,P0s satisfy +S7
    surv=[nm for nm in A if all(sum(kup[m]*A[nm][(m,n,r,s)] for m in range(4))==0
          for n,r,s in prod(range(4),repeat=3))]
    ok&=check(sorted(surv)==['P0s','P2','Xsw'],"Ward survivors are exactly {P2,P0s,Xsw}",log)
    sym=[nm for nm in surv if all(A[nm][(m,n,r,s)]==A[nm][(r,s,m,n)] for m,n,r,s in IDX)]
    ok&=check(sorted(sym)==['P0s','P2'],"Ward+S7 survivors are exactly {P2,P0s}",log)
    return ok,res

def main():
    log=[]; allok=True; out={}
    for kup in ([F(5),F(4),F(2),F(1)],[F(2),F(1),F(1),F(1)]):
        k2=sum(kup[m]*sum(ETA[m][n]*kup[n] for n in range(4)) for m in range(4))
        print("k^mu = %s  (k^2 = %s)"%([str(x) for x in kup],k2))
        ok,res=run(kup,log); allok&=ok
        out["k=%s"%",".join(str(x) for x in kup)]=res
        print()
    print("VERDICT: %s"%("ALL PASS -- 6 -> 3 -> 2 established by two agreeing exact routes"
                         if allok else "FAILURES ABOVE"))
    print("LICENSING A: exactly-two = diagonal Ward (booked) + S7 (UNBOOKED -- declaring claim owed).")
    print("LICENSING B: c0 = 0 NOT licensed; EH counterexample stands.")
    print("W-0: computed-and-reported, NOT banked. Bardeen/FRW completion remains the frontier.")
    json.dump({"results":out,"checks":log,"authorship":"checker-implemented; second-author review owed"},
              open(__file__.replace(".py","_RESULT.json"),"w"),indent=1,default=str)
    return 0 if allok else 1

if __name__=="__main__": sys.exit(main())
