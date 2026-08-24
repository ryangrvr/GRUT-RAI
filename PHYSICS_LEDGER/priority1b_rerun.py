#!/usr/bin/env python3
# PRIORITY 1b RERUN - passive-oscillatory (Lorentz) vs frozen criterion.
# ADD-2: convention anchored empirically via registered single-pole kernel FIRST.
import json, math, cmath, sys, os
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'gate'))
import kms

def H(a, Om=0.3, OL=0.7): return (Om/a**3+OL)**0.5

# convention anchor: registered single-pole Debye must come out PASSIVE
def chi_debye(x): return complex(1.0,x)/(1.0+x*x)
debye_min = min(chi_debye(0.01*i).imag for i in range(1,500))
CONVENTION_OK = debye_min > 0
print('ADD-2 convention anchor: Debye min Im chi =', round(debye_min,6),
      '-> passive under this convention:', CONVENTION_OK)
if not CONVENTION_OK:
    print('STOP: registered kernel fails passivity under both conventions'); sys.exit(1)

def chi_cos(x, g=1.0, Om=2.0):
    # the INADMISSIBLE cos-kernel, for the record: Im goes negative near resonance
    return 0.5/(complex(g,-(x+Om))) + 0.5/(complex(g,-(x-Om)))

def chi_lorentz(x, g=0.5, w0=2.0):
    return complex(w0*w0,0.0)/complex(w0*w0-x*x,-g*x)

def passivity(chi,name='',n=500):
    worst=min(chi(0.01*i).imag for i in range(1,n+1))
    return {'min_Im_chi_w_pos':worst,'passive':worst>=-1e-12}

def causality_poles(name,poles):
    ok=all(p.imag<0 for p in poles)
    return {'kernel':name,'poles':poles,'causal':ok}

def kk_resid(chi,xmax=20.0,n=4000):
    xs=[xmax*i/n for i in range(n+1)]
    re=[chi(x).real for x in xs]
    dx=xs[1]-xs[0]; num=[]; tru=[]
    for k in range(0,n+1,50):
        xk=xs[k]; s=0.0
        for j in range(n+1):
            if abs(xs[j]-xk)<1e-9: continue
            s+=re[j]*xs[j]/(xs[j]*xs[j]-xk*xk)
        num.append(s*dx*2/math.pi); tru.append(chi(xk).imag)
    sc=max(1e-9,max(abs(t) for t in tru))
    return round(max(abs(a-b) for a,b in zip(num,tru))/sc,4)

def kms_gate(chi,T=1.0):
    ws=[0.05*i for i in range(1,200)]
    GR=[chi(w) for w in ws]
    GK=[cmath.tanh if False else None for _ in ws]  # build below
    out=[]
    for w,gr in zip(ws,GR):
        gk = 1.0/math.tanh(w/(2.0*T))*(gr-gr.conjugate())  # FDT-constructed noise
        out.append(complex(gk))
    r=kms.gate(ws,GR,out,T)
    return r

def classify(vals,ref):
    sc=any(v>0 for v in vals) and any(v<0 for v in vals)
    scr=any(v>0 for v in ref) and any(v<0 for v in ref)
    if sc and scr: return 'TRUE CROSSING'
    if sc: return 'NUMERICAL ARTIFACT'
    if min(abs(v) for v in vals)<1e-6: return 'TANGENCY'
    if not sc: return 'APPROACH WITHOUT CROSSING'
    return 'UNRESOLVED'

def run_kernel(name,chi,params=''):
    out={'kernel':name,'params':params,'crossing_by_framing':{}}
    for frame,key in (('phase-lag/elastic','real'),('dissipative','imag')):
        vals=[]; ref=[]
        for N,acc in ((400,vals),(1600,ref)):
            for i in range(N):
                a=0.02+0.98*i/(N-1)
                acc.append(getattr(chi(a*H(a)),key))
        out['crossing_by_framing'][frame]=classify(vals,ref)
    out['passivity']=passivity(chi)
    out['KK']=kk_resid(chi)
    out['KMS']=kms_gate(chi)
    return out

results=[]
results.append(run_kernel('registered single-pole Debye (convention control)',chi_debye,'tau=1'))
results.append(run_kernel('INADMISSIBLE cos-kernel (prior run, for record)',
                          lambda x: chi_cos(x,1.0,2.0),'gamma=1 Omega=2'))
results.append(run_kernel('PASSIVE Lorentz oscillatory',lambda x: chi_lorentz(x,0.5,2.0),
                          'gamma=0.5 omega0=2'))
res=[r for r in results]
json.dump({'meta':{'date':'2026-08-23','tool':'priority1b_rerun.py',
   'convention_anchor':{'debye_min_Im':round(debye_min,6),'frozen':True},
   'note':'cos-kernel retained as inadmissible test case; not evidence'},'results':res},
   open('PRIORITY1B_RERUN.json','w'),indent=2,default=str)
for r in results:
    print(r['kernel'],'|',r['crossing_by_framing'],'| passive:',r['passivity']['passive'],
          '| KMS passed:',r['KMS']['passed'])
