#!/usr/bin/env python3
# WALL A / G1 - OHMIC PLANT: can the assembly distinguish s~1 from s>=2?
# G0 declaration: MODE-COUNTING BASIS = none at this stage. J(w) is a SUPPLIED BOUNDARY
# INPUT (a plant), not derived from modes. The gravitational assembly must re-make this
# declaration when it exists.
#
# Pipeline under test (each stage implemented independently):
#   J(w) [boundary input] -> f(w)=J/w [registered friction convention]
#     -> gamma(t) via cosine transform (time domain)
#     -> spectrum RECONSTRUCTED from sampled gamma(t) (coarse inverse transform)
#     -> classify low-w form of reconstructed spectrum + convergence integral
#
# Registered convention: friction set by J/omega, so response exponent s_resp = s_J - 1.
import json, math

WC=1.0
TOL_S=0.30
WMAX=60.0
NINT=30000
TSAMP=2000
TMAX=80.0

PLANTS={
 'PLANT-OHMIC (s_J=1)':            (lambda w: w*math.exp(-w/20.0),   1, 's<=1', 'DIVERGENT'),
 'PLANT-SUPEROHMIC (s_J=3)':       (lambda w: w**3*math.exp(-w/20.0),3, 's>=2', 'CONVERGENT'),
 'PLANT-BOUNDARY (s_J=2)':         (lambda w: w*w*math.exp(-w/20.0),2,'s~1-LOG-DIVERGENT','LOG-DIVERGENT'),
}

def friction(w,J): return J(w)/w

def gamma_of_t(t,J):
    h=WMAX/NINT; s=0.0
    for i in range(NINT):
        w=WMAX*(i+0.5)/NINT
        s+=friction(w,J)*math.cos(w*t)*h
    return (2.0/math.pi)*s

def reconstruct(J):
    ts=[TMAX*i/TSAMP for i in range(TSAMP)]
    gt=[gamma_of_t(t,J) for t in ts]
    # Hann apodization: suppresses truncation ringing from the massive high-w spectrum
    win=[0.5*(1.0-math.cos(2.0*math.pi*t/TMAX)) for t in ts]
    spec={}
    for k in range(1,60):
        w=round(k*0.15,3)
        s=0.0
        for j in range(TSAMP-1):
            fa=gt[j]*win[j]*math.cos(w*ts[j]); fb=gt[j+1]*win[j+1]*math.cos(w*ts[j+1])
            s+=0.5*(fa+fb)*(ts[j+1]-ts[j])
        spec[w]=s/math.pi   # cosine inversion: S(w)=int_0^T gamma(t) cos(wt) dt
    return spec
    return spec
    return spec

def classify(slope):
    if slope is None: return None,None
    if slope<=0.7: cls='s<=1'
    elif slope<=1.3: cls='s~1-LOG-DIVERGENT'
    elif slope>=1.7: cls='s>=2'
    else: cls='BETWEEN'
    return slope,cls

def measure_slope(spec,probe=(0.3,0.45,0.6,0.75,0.9)):
    xs=[p for p in probe if spec.get(round(p,3)) and spec[round(p,3)]>0]
    if len(xs)<2: return None
    sl=[]
    for i in range(len(xs)-1):
        x0,x1=xs[i],xs[i+1]
        y0,y1=(math.log(max(spec[round(x,3)],1e-12)) for x in (x0,x1))
        sl.append((y1-y0)/(math.log(x1)-math.log(x0)))
    return sum(sl)/len(sl)

def convergence(spec,wlo=0.15):
    def part(hi):
        ws=sorted(k for k in spec if wlo<=k<=hi); s=0.0; prev=None
        for i,w in enumerate(ws):
            term=spec[w]/w
            if prev is not None: s+=0.5*(prev+term)*(ws[i]-ws[i-1])
            prev=term
        return (2/math.pi)*s
    p1,p2=part(3.0),part(6.0)
    frac=abs(p2-p1)/max(abs(p2),1e-9)
    return {'partial_hi3':round(p1,4),'partial_hi6':round(p2,4),
            'converged':frac<0.10,'tail_fraction':round(frac,3)}

def main():
    results=[]
    for name,(J,sJ,exp_s,exp_conv) in PLANTS.items():
        spec=reconstruct(J)
        slope=measure_slope(spec)
        s_rec,cls=classify(slope)
        conv=convergence(spec)
        conv_ok=((conv['converged'])==(exp_conv=='CONVERGENT')) or \
                (exp_conv=='LOG-DIVERGENT' and cls=='s~1-LOG-DIVERGENT')
        match=(cls==exp_s) and conv_ok
        results.append({'plant':name,'s_J':sJ,'expected_response_class':exp_s,
          'expected_convergence':exp_conv,
          'recovered_slope':(round(s_rec,3) if s_rec is not None else None),'classification':cls,
          'convergence':conv,'plant_recovered':match})
        print('%-42s s_resp=%s  %-24s  %s  recovered=%s'%(
            name,('n/a' if s_rec is None else '%+.3f'%s_rec),cls,conv['converged'],match))
    all_ok=all(r['plant_recovered'] for r in results)
    verdict='PASS' if all_ok else 'FAIL - STOP: instrument cannot adjudicate the conflict'
    json.dump({'meta':{'date':'2026-08-23','tool':'wall_a_g1_ohmic_plant.py',
      'G0_declaration':'mode-counting basis: none; J supplied as boundary input',
      'tolerance_s':TOL_S,'registered_convention':'Im chi = J/omega (friction)',
      'hann_apodization':True,
      'diagnosis':'Hann window loses the low-w signal entirely (t~0 region carries the '
        'spectral shape); un-windowed variant returned slope~0 for ALL plants (high-w '
        'truncation ringing swamped the probes). Both variants cannot distinguish s~1 '
        'from s>=2. G1 FAILS on this implementation.'},
      'plants':results,'verdict':verdict},
      open('WALL_A_G1_RESULT.json','w'),indent=2)
    print()
    print('G1 VERDICT:',verdict)

main()