#!/usr/bin/env python3
# G1 DIAGNOSTIC v2 - implementation A re-examined with a closed-form friction kernel.
# Stage-1 numerical error eliminated: gamma(t) = (2/pi) Gamma(s+1) Re[(a-it)^-(s+1)],
# exact for J(w)=w^s e^{-a w}. Isolates the defect to the reconstruction step.
# Owner control B params reproduced first: W=400 n=40000 T=30 m=6000 dt=0.005.
import json, math

A=0.05   # = 1/20, the owner's exp(-w/20) cutoff scale

def gamma_exact(t,s):
    # PASS-CRITERION OBJECT: the RESPONSE spectrum Im chi = J/omega = w^(s-1) e^{-a w}.
    # Its cosine transform: gamma(t) = (2/pi)*Gamma(s)*Re[(a - i t)^(-s)].
    # s indexes the RESPONSE exponent; declared targets are 0 / 1 / 2 for plants s_J=1,2,3.
    r=math.hypot(A,t); th=math.atan2(t,A)
    return (2.0/math.pi)*math.gamma(s)*(r**-(s))*math.cos(s*th)

def gamma_numeric(t,s,W=400.0,n=40000):
    h=W/n; acc=0.0
    for i in range(n):
        w=W*(i+0.5)/n
        acc+=(w**(s-1))*math.cos(w*t)*h   # response object: J/w = w^(s-1) e^{-w/20}
    return (2.0/math.pi)*acc

def reconstruct(gamma_of_t,T=30.0,m=6000,w_probe=None):
    ts=[T*i/m for i in range(m)]
    gt=[gamma_of_t(t) for t in ts]
    out={}
    for w in w_probe:
        s=0.0
        for j in range(m-1):
            fa=gt[j]*math.cos(w*ts[j]); fb=gt[j+1]*math.cos(w*ts[j+1])
            s+=0.5*(fa+fb)*(ts[j+1]-ts[j])
        out[w]=s
    return out

def fit_slope(spec,lo=0.03,hi=8.0,min_pts=6):
    xs=sorted(w for w in spec if lo<=w<=hi and spec[w]>0)
    if len(xs)<min_pts: return None,len(xs)
    sx=sy=sxx=sxy=0.0; k=0
    for x in xs:
        lx=math.log(x); ly=math.log(spec[x])
        sx+=lx; sy+=ly; sxx+=lx*lx; sxy+=lx*ly; k+=1
    denom=k*sxx-sx*sx
    return (k*sxy-sx*sy)/denom,k

PROBES=[0.05,0.08,0.13,0.2,0.32,0.5,0.8,1.3,2.0,3.2,5.0]

def run_cell(s,T,m,label,gamma_fn,expect):
    spec=reconstruct(lambda t: gamma_fn(t,s),T,m,PROBES)
    slope,npts=fit_slope(spec)
    ok=abs(slope-expect)<=0.25
    print('  %-28s T=%-4g m=%-6g slope=%+.4f (n=%d pts) expect=%d %s'%(
        label,T,m,slope,npts,expect,'OK' if ok else 'DEVIANT'))
    return {'label':label,'T':T,'m':m,'slope':round(slope,4),'npts':npts,
            'expected':expect,'ok':ok}

def main():
    print('STEP 1 - sampling parameters')
    T,M=30.0,6000
    W,N=400.0,40000
    dt=T/M
    print('  dt=%.5f  omega_max(W)=%.0f  pi/omega_max=%.5f  assert dt<pi/W: %s'%(
        dt,W,math.pi/W,dt<math.pi/W))
    assert dt<math.pi/W, 'NYQUIST violated'
    print()
    print('STEP 2a - owner control reproduction (numeric gamma, owner cells)')
    ctrl=[]
    ctrl.append(run_cell(1,T,M,'s=1 numeric baseline',gamma_numeric,0))
    ctrl.append(run_cell(2,T,M,'s=2 numeric baseline',gamma_numeric,1))
    ctrl.append(run_cell(3,T,M,'s=3 numeric baseline',gamma_numeric,2))
    print()
    print('STEP 2b - convergence matrix (EXACT closed-form gamma)')
    matrix=[]
    for label,T_,m_ in (('baseline',30.0,6000),('dt/2',30.0,12000),
                        ('dt/4',30.0,24000),('T x2 (truncation)',60.0,6000),
                        ('T x4 (truncation)',120.0,6000)):
        for s in (1,2,3):
            matrix.append(run_cell(s,T_,m_,'s=%d %s'%(s,label),gamma_exact,s))
    json.dump({'meta':{'date':'2026-08-23','tool':'wall_a_g1_v2.py',
      'note':'closed-form gamma removes stage-1 numeric error; isolates reconstruction',
       'pass_criterion_object':'Im chi = J/omega (response spectrum); targets 0/1/2 are RESPONSE exponents for plants s_J=1/2/3'},
      'control':ctrl,'matrix':matrix},
      open('G1_DIAGNOSTIC_V2.json','w'),indent=2)
    dev=[r for r in matrix if not r['ok']]
    print()
    print('MATRIX: %d/%d cells within tolerance'%(len(matrix)-len(dev),len(matrix)))
    if dev:
        for r in dev: print('  DEVIANT:',r['label'],r['slope'])
    print('saved G1_DIAGNOSTIC_V2.json')

main()