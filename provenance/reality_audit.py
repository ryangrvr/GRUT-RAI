#!/usr/bin/env python3
"""REALITY AUDIT execution — Ox (builder). Per REALITY_AUDIT_CHARTER.md §8
and REALITY_AUDIT_BRIEF.md ADDED-2/ADDED-7. Not a provenance audit.
Outputs: REALITY_AUDIT_RESULTS.md/.json, REALITY_LOAD_BEARING_MAP.md,
REALITY_AUDIT_BLOCKERS.md. Does NOT mutate claims.json."""
import json, os, random
from collections import defaultdict, deque, Counter

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
with open(os.path.join(ROOT,'provenance','claims.json')) as f:
    REG = json.load(f)['claims']
BY_ID = {c['id']: c for c in REG}

# ADDED-1 type assignment: MATHEMATICAL / FRAMEWORK / PHYSICAL
TYPE = {
 'founding_h1_zeta_casimir':'MATHEMATICAL','l0_r1_redundancy_exists':'MATHEMATICAL',
 'l0_r2_exact_unique_breaker':'MATHEMATICAL','l0_r3_payoff_mu_linear':'MATHEMATICAL',
 'x_no_pin_theorem':'MATHEMATICAL','u1_form_universality':'MATHEMATICAL',
 'u2_kernel_universality':'MATHEMATICAL','u3_split_origin':'MATHEMATICAL',
 'zeta_interior_family':'MATHEMATICAL','mu_linear':'MATHEMATICAL',
 'u4_constitutive_origin':'FRAMEWORK','u5_constitutive_phases':'FRAMEWORK',
 'u6_constitutive_order':'FRAMEWORK','rung2_kms_gate':'FRAMEWORK',
 'kk_static_transfer':'FRAMEWORK','passivity_channel_diagonal':'FRAMEWORK',
 'p_tt_ansatz':'FRAMEWORK',
}
def get_type(cid): return TYPE.get(cid,'PHYSICAL')

EVIDENCE = {
 'founding_h1_zeta_casimir':'BORROWED','rung2_kms_gate':'BORROWED',
 'kk_static_transfer':'DERIVED','mu_linear':'DERIVED',
 'passivity_channel_diagonal':'DERIVED','x_no_pin_theorem':'DERIVED',
 'u1_form_universality':'DERIVED','l0_r1_redundancy_exists':'DERIVED',
 'rung3_single_pole':'DERIVED',
 'vc_m_planck':'EMPIRICAL','vc_rho_lambda':'EMPIRICAL','vc_v_ew':'EMPIRICAL',
}
def get_evidence(cid): return EVIDENCE.get(cid,'ASSERTED')


# Dependency graph for Q3 blast radius
DEPS={}; ATTACHES={}
for c in REG:
    DEPS[c['id']]=set(c.get('depends_on') or [])
    ATTACHES[c['id']]=set(c.get('attaches_to') or [])
def forward_closure(start):
    seen=set(); q=deque(start)
    while q:
        cur=q.popleft()
        if cur in seen: continue
        seen.add(cur)
        for nid in BY_ID:
            if cur in DEPS.get(nid,set()) or cur in ATTACHES.get(nid,set()):
                if nid not in seen: q.append(nid)
    return seen-set(start)
BLAST={c['id']:len(forward_closure([c['id']])) for c in REG}

# Verdicts. Fragile eight graded from session work; rest start BLOCKED.
V={
 'rung3_single_pole':('HOLDS-NARROWER','class-A pair adverse to super-Ohmic premise; free theory gives a FAMILY indexed by multipole, not THE memory time'),
 'rung1_inin_action':('HOLDS-NARROWER','COMPOUND: shown formalism (SK influence action, borrowed) + assumed ontology (finite-memory stance); SPLIT repair owed. Class-C branches = EXPOSURE (4/7 hypothetical, none realised); class-A pair = ADVERSE AT PROXY SCOPE'),
 'rung4_love_kk':('HOLDS-NARROWER','22-62 orders correct for dephasing only; amplitude channel uncovered'),
 'rung7_wz':('UNRESOLVED-BLOCKED','+2/+3 statement-vs-ledger discrepancy needs owner adjudication'),
 'p_tt_ansatz':('HOLDS-NARROWER','TT-only choice is CHOSEN not forced per own rung3 text'),
 'method_novelty':('UNRESOLVED-BLOCKED','prior-art screen never ran against formal-methods corpora'),
}
# Calibration batch: 10 random nodes, seed 42
random.seed(42)
CALIB=sorted(random.sample(sorted(c['id'] for c in REG),10))
for cid in CALIB:
    if cid in V: continue   # fragile-eight / explicit verdicts take precedence
    ev=get_evidence(cid); tier=BY_ID[cid].get('tier')
    if ev=='ASSERTED' and tier in ('assumed','postulate'):
        V[cid]=('NULL-ASSERTED',f'{tier}-tier asserted; null result per ADDED-2')
    elif ev=='EMPIRICAL':
        V[cid]=('HOLDS',f'measured value ({tier}); external-validation debt unchanged')
    else:
        V[cid]=('UNRESOLVED-BLOCKED','reproduction harness / source-open not yet run for this node')
for c in REG:
    if c['id'] not in V:
        V[c['id']]=('UNRESOLVED-BLOCKED','audit sweep incomplete; tooling gap')

TOP_LOAD=sorted(BLAST.items(),key=lambda x:-x[1])[:15]

# Blast radii as SETS with overlaps (correction 1: never addable integers)
CHAIN_ROOT='background_time_translation_flow'
chain_reach=forward_closure([CHAIN_ROOT])
nested={}
for cid,_ in TOP_LOAD[:5]:
    r=forward_closure([cid])
    nested[cid]={'reach':len(r),'is_subset_of_root':r.issubset(chain_reach),
                 'overlap_with_root':len(r & chain_reach)}
UNION_ALL=len(set().union(*[forward_closure([c]) for c in [CHAIN_ROOT,'rung1_inin_action','rung2_kms_gate']]))

def VERD_CLASS(v):
    if 'BLOCKED' in v: return 'BLOCKED'
    if 'NULL' in v: return 'NULL'
    if v.startswith('HOLDS-NARROWER'): return 'HOLDS-NARROWER'
    if v.startswith('DOES'): return 'DOES-NOT-HOLD'
    if v=='HOLDS': return 'HOLDS'
    return v
matrix=defaultdict(lambda:defaultdict(int))
for c in REG: matrix[c['tier']][VERD_CLASS(V[c['id']][0])]+=1
TIERS=['shown','assumed','postulate','to-derive','derived-pending','measured','heuristic','open']
VCOLS=['HOLDS','HOLDS-NARROWER','DOES-NOT-HOLD','NULL','BLOCKED']

out={'meta':{'date':'2026-08-23','auditor':'Ox (builder), self-audit; charter sec.7 limitation applies'},'nodes':[]}
for c in REG:
    vd,rsn=V[c['id']]
    out['nodes'].append({'id':c['id'],'tier':c['tier'],'type':get_type(c['id']),
      'evidence':get_evidence(c['id']),'verdict':vd,'reason':rsn,'blast_radius':BLAST[c['id']]})
json.dump(out,open(os.path.join(ROOT,'REALITY_AUDIT_RESULTS.json'),'w'),indent=2)

L=['# Reality Audit — Results','','**Date:** 2026-08-23. Auditor: Ox (builder). Self-audit limitation (charter §7) applies.','',
'> **This audit cannot discharge the external-validation debt.** No outside human has ever been contacted by this program.','',
'## Mismatch matrix (tier × reality verdict)','',
'| tier | '+' | '.join(VCOLS)+' |','|'+'---|'*len(VCOLS)]
for t in TIERS: L.append('| '+t+' | '+' | '.join(str(matrix[t].get(v,0)) for v in VCOLS)+' |')
L+=['','## Per-node table','',
'| id | tier | type | evidence | verdict | blast | reason |','|---|---|---|---|---|---|---|']
for c in REG:
    vd,rsn=V[c['id']]
    L.append('| %s | %s | %s | %s | %s | %d | %s |'%(c['id'],c['tier'],get_type(c['id']),get_evidence(c['id']),vd,BLAST[c['id']],rsn[:90]))
L+=['','## Load-bearing map (top 15 by blast radius, edges only)','',
'| rank | id | tier | verdict | downstream |','|---|---|---|---|---|']
for i,(cid,n) in enumerate(TOP_LOAD,1):
    L.append('| %d | %s | %s | %s | %d |'%(i,cid,BY_ID[cid]['tier'],V[cid][0],n))
L+=['','## Limits paragraph (charter §7)','',
'This audit cannot discharge the external-validation debt. No outside human has ever been contacted by this program. An audit of the program by the program is the exact conflict-of-interest the method exists to flag.','']
open(os.path.join(ROOT,'REALITY_AUDIT_RESULTS.md'),'w').write('\n'.join(L))

nb=sum(1 for c in REG if 'BLOCKED' in V[c['id']][0])
B=['# Reality Audit — Blockers log','',
'A blocker is a result. Verdicts suffixed -BLOCKED were caused by missing instruments, not evidence. Counted separately.',
'',f'**{nb} of 71 nodes received a BLOCKED verdict.**','',
'| id | why | verdict consequence |','|---|---|---|']
for c in REG:
    vd,rsn=V[c['id']]
    if 'BLOCKED' in vd: B.append('| %s | %s | %s |'%(c['id'],rsn,vd))
open(os.path.join(ROOT,'REALITY_AUDIT_BLOCKERS.md'),'w').write('\n'.join(B))

M=['# Reality Load-Bearing Map','',
'The audit\'s most valuable output (charter §8.3). **Blast radii are sets with overlaps, never addable integers.**',
'Edge-graph only; prose graph (~0.78x additional) not machine-extracted.','',
'## The chain (corrected arithmetic)','',
f'**One nested chain carries {UNION_ALL} of {len(REG)} nodes ({100*UNION_ALL//len(REG)}% of the register):**','',
'```','background_time_translation_flow -> rung1_inin_action -> rung2_kms_gate -> ...','```','',
f'Root: `{CHAIN_ROOT}` — booked 2026-08-18 as an OMISSION, tier `assumed`, Δ+1,',
'sub_status: *"NOT a physics claim about de Sitter."*','',
'| node | reach | subset of root? | overlap with root | verdict |','|---|---|---|---|---|']
for cid in [CHAIN_ROOT,'rung1_inin_action','rung2_kms_gate']:
    n=nested.get(cid,BLAST[cid])
    sub='YES' if isinstance(n,dict) and n['is_subset_of_root'] else '—'
    ov = n['overlap_with_root'] if isinstance(n,dict) else '—'
    M.append(f"| {cid} | {BLAST[cid]} | {sub} | {ov} | {V[cid][0]} |")
M+=['',f'**UNION of the three: {UNION_ALL}. Do NOT sum the reach column.**','',
'## Top 15 by individual blast radius (for reference only; NOT additive)','',
'| rank | id | tier | verdict | downstream |','|---|---|---|---|---|']
for i,(cid,n) in enumerate(TOP_LOAD,1):
    M.append('| %d | %s | %s | %s | %d |'%(i,cid,BY_ID[cid]['tier'],V[cid][0],n))
open(os.path.join(ROOT,'REALITY_LOAD_BEARING_MAP.md'),'w').write('\n'.join(M))

print('=== SUMMARY ==='); print('Total:',len(REG))
vc=Counter(V[c['id']][0] for c in REG)
for k,n in vc.most_common(): print(' ',k,n)
print('Calibration batch:',CALIB)
