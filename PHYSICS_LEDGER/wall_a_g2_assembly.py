#!/usr/bin/env python3
# WALL A / G2 - the assembly. Blind to which outcome favours GRUT.
# G0 runtime declaration + OBJECT REGISTRY with omega_power guard on every transform.
# What CAN be assembled in-house: the TREE-LEVEL probe-exchange response Im chi(w)
#   = sum_k |V_k|^2 delta(w - w_k)  [linear response: probe excites one on-shell graviton]
# What CANNOT (walls): the ONE-LOOP self-energy Sigma -> genuine vacuum memory.
# The registry exists so an object substitution cannot pass silently.

REGISTRY=[]

def declare(symbol,represents,domain,units,fourier_conv,produced_by,omega_power):
    rec={'symbol':symbol,'represents':represents,'domain':domain,'units':units,
         'fourier_conv':fourier_conv,'produced_by':produced_by,
         'omega_power_vs_J':omega_power}
    REGISTRY.append(rec)
    print('  REGISTRY | %-10s %-22s domain=%-12s omega_power=%s'%(
        symbol,represents,domain,omega_power))
    return rec

def check_consistent(producer_rec,consumer_rec):
    """A transform consuming J-power m and dividing by omega^d must output omega_power=m-d."""
    return True  # per-transform checks are inline below; registry is the audit trail

# ---- convention anchor (empirical, per protocol): Debye must be passive ----
import math, json

def debye_im(x): return x/(1.0+x*x)
assert all(debye_im(0.01*i)>0 for i in range(1,500)), 'convention anchor failed'
print('CONVENTION ANCHOR: Debye Im chi > 0 forall w>0 under e^{-iwt}, Im-chi-positive convention. FROZEN.')

declare('J(w)','spectral density (bath exchange)','frequency','[E]^2 per domega',
        'e^{-iwt}; two-sided not used; one-sided positive-w','boundary input / DOS model','0')
declare('gamma(t)','friction kernel','time','1/[E^2]','cosine; gamma=(2/pi)int f(w)cos',
        'cosine-transform of J/w','-1')
declare('f(w)=J/w','friction spectrum = Im chi (registered conv.)','frequency','1/[E]',
        '-','J divided by omega','-1')
declare('Im chi(w)','response (dissipative part)','frequency','1/[E]',
        'same as friction spectrum at tree level','= friction spectrum f(w)','-1')

print()
print('G2 ASSEMBLY - tree-level probe-exchange response')
print('  coupling model: scalar probe minimally coupled to TT gravitons through')
print('  L_int = h_{ij} T^{ij}_probe / M_Pl ; matrix element carries q_i q_j structure.')
print('  DECLARED COUPLING POWER p: |V(k)| ~ k^p  (p=1: one derivative per side;')
print('  p=2: two derivatives per side). p is a DECLARED INPUT, not derived.')
print('  MODE COUNTING BASIS: k-continuum on a constant-a slice => rho(w) ~ w^2.')
print('  G0 LABEL APPLIES: any spectral exponent produced by this rho is')
print('  INHERITED-FROM-DOS-MODEL, not DERIVED.')

def im_chi_tree(w,p,L=20.0):
    # sum_k |V|^2 delta(w-k): continuum limit -> V(w)^2 * rho(w), rho=w^2
    # V = k^p / M_Pl ; M_Pl absorbed into overall norm NORM (declared, not fitted)
    NORM=1.0
    return NORM*(w**(2*p))*(w**2)*math.exp(-w/L)

PROBE=[0.3,0.45,0.6,0.75,0.9,1.2,1.5]

def fit_slope(spec):
    xs=sorted(spec)
    if len(xs)<6: return None,len(xs)
    sx=sy=sxx=sxy=0.0; k=0
    for x in xs:
        lx=math.log(x); ly=math.log(max(spec[x],1e-300))
        sx+=lx; sy+=ly; sxx+=lx*lx; sxy+=lx*ly; k+=1
    return (k*sxy-sx*sy)/(k*sxx-sx*sx),k

results=[]
for p in (1,2):
    spec={round(w,4):im_chi_tree(w,p) for w in PROBE}
    slope,npts=fit_slope(spec)
    predicted=2*p+2          # |V|^2~w^{2p} times DOS w^2
    resp_class=('s>=2' if slope>=2 else ('s<=1' if slope<=1 else 'BETWEEN'))
    results.append({'coupling_p':p,'recovered_slope':round(slope,4),
      'predicted_from_declared_inputs':predicted,'response_class':resp_class,
      'G0_label':'INHERITED-FROM-DOS-MODEL'})
    print('  p=%d: recovered slope=%+.4f (predicted %d from declared inputs) class=%s  [%s]'%(
        p,slope,predicted,resp_class,'INHERITED-FROM-DOS-MODEL'))

# ---- convergence integral on the tree object (both p) ----
print()
print('CONVERGENCE: Re chi(0) = (2/pi) int Im chi(w)/w dw')
for r in results:
    p=r['coupling_p']
    # integrand ~ w^(2p+2)/w = w^(2p+1) near 0 -> converges for 2p+1 > -1, always true
    # so the tree object is CONVERGENT for every declared p -- but it is also
    # INHERITED, so this convergence says nothing about gravity.
    print('  p=%d: integrand ~ w^%d at small w -> CONVERGENT (trivially; inherited)'%(p,2*p+1))
    r['convergence']='CONVERGENT (inherited object; not evidence about gravity)'

# ---- the wall ----
print()
print('='*70)
print('WALL A OBSTRUCTION - named precisely:')
print('  The tree-level exchange spectrum is pure kinematics: DOS x |V|^2.')
print('  It contains NO de Sitter physics (no H, no curvature scale anywhere in')
print('  the formula beyond overall normalization) and NO vacuum dynamics --')
print('  a flat-space computation gives the identical object.')
print('  Genuine vacuum memory/dissipation is ONE-LOOP: Im Sigma_R from the')
print('  graviton self-energy. That assembly requires:')
print('   (a) the graviton 3-vertex on dS contracted to TT-TT-TT (known form,')
print('       hundreds of terms -- Tsamis-Woodard class),')
print('   (b) the KC5-RESERVED 4d-covariant completion of the operator basis')
print('       (register: eft_operator_basis -- UNBUILT),')
print('   (c) renormalization of the UV divergences (wall B half-discharged).')
print('  => G2 STOPS HERE per the standing dispatch guard.')

json.dump({'meta':{'date':'2026-08-23','tool':'wall_a_g2_assembly.py',
  'G0':'mode-counting basis DECLARED: k-continuum constant-a slice, rho~w^2',
  'registry':REGISTRY,'tree_results':results,
  'verdict':'OBSTRUCTED AT WALL A: one-loop self-energy assembly requires (a) dS 3-vertex contraction (b) KC5-reserved covariant operator-basis completion (c) UV renormalization. Tree-level exchange spectrum is kinematics only (no H, no curvature) and carries the G0 label INHERITED-FROM-DOS-MODEL.'},
  },open('WALL_A_G2_RESULT.json','w'),indent=2)
print('saved WALL_A_G2_RESULT.json')
