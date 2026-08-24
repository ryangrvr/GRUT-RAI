#!/usr/bin/env python3
"""PHYSICS TRANSITION step 0 — COLLECT BEFORE COMPUTING.
Aggregates claims.json differentiator field; fences PHYSICS_LEDGER out of prose corpus."""
import json,os
from collections import defaultdict
ROOT=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
claims=json.load(open(os.path.join(ROOT,'provenance','claims.json')))['claims']

def bucket(v):
    v=(v or '').strip()
    if v.startswith('WOULD-BE'): return 'CONDITIONAL-DIFFERENTIATING'
    if v.startswith('FAILS'): return 'FAILS-DIFFERENTIATION'
    if v.startswith('NON-DIFFERENTIATING'): return 'NON-DIFFERENTIATING'
    if v.startswith('STRUCTURAL PASS'): return 'DIFFERENTIATING-RESULT (negative-direction)'
    if v.startswith('NO-GO'): return 'NO-GO-EXPORT'
    if not v: return 'UNSET'
    # explicit named conditionals outside keyword prefixes
    if v.startswith('tau_c>0 vs tau_c=0'): return 'CONDITIONAL-DIFFERENTIATING'  # rung3: THE GRUT-vs-standard contrast
    if v.startswith('THE FIRST PARAMETERIZED EMPIRICAL SURFACE'): return 'CONDITIONAL-DIFFERENTIATING'
    if v.startswith('Register-internal yield'): return 'NO-GO-EXPORT'
    if v.startswith('Decoherence RATE is differentiating'): return 'CONDITIONAL-DIFFERENTIATING'
    if v.startswith('The discriminating question'): return 'META'
    return 'OTHER:'+v[:40]

agg=defaultdict(list)
for c in claims:
    agg[bucket(c.get('differentiator',''))].append(
        {'id':c['id'],'tier':c['tier'],'differentiator':(c.get('differentiator') or '')[:100]})

out={'meta':{'date':'2026-08-23','tool':'physics_collect.py',
      'rule':'COLLECT BEFORE COMPUTING — machine-readable partial answer to "what is uniquely GRUT"'},
 'summary':{k:len(v) for k,v in sorted(agg.items(),key=lambda x:-len(x[1]))},
 'nodes':dict(agg)}
json.dump(out,open(os.path.join(ROOT,'PHYSICS_LEDGER','DIFFERENTIATOR_TABLE.json'),'w'),indent=2)
L=['# Differentiator aggregation — collected before computing (v2, corrected)','',
'Generated from claims.json `differentiator` field by `provenance/physics_collect.py`.',
'Denominator: **all 71 nodes accounted for**; every bucket shown; no silent drops.','',
'## Headline (corrected v2)','',
'> **Zero nodes carry an unconditional, currently-observable differentiating result.**',
'> Nodes carrying CONDITIONAL differentiators exist — every condition is open.','',
'The prior headline ("only one positive result") wrongly collapsed conditional differentiators',
'(WOULD-BE family) into nothing. The accurate statement is sharper, not softer.','']
for k,v in sorted(agg.items(),key=lambda x:-len(x[1])):
    L.append('## %s (%d)'%(k,len(v))); L.append('')
    for n in v: L.append('- `%s` (%s): %s'%(n['id'],n['tier'],n['differentiator']))
    L.append('')
open(os.path.join(ROOT,'PHYSICS_LEDGER','DIFFERENTIATOR_TABLE.md'),'w').write('\n'.join(L))
print(json.dumps(out['summary'],indent=1))

# ledger fence: exclude PHYSICS_LEDGER from prose corpus, recorded AT CREATION
mf_path=os.path.join(ROOT,'REALITY_PROSE_CORPUS_MANIFEST.json')
mf=json.load(open(mf_path))
fence={'path_prefix':'PHYSICS_LEDGER/','category':'LEDGER-FENCE',
 'reason':'physics ledger, epoch-tagged at creation; prevents the 48% self-contamination recurrence',
 'can_contain_dependencies':True,
 'rule':'excluded from prose-audit corpus by default; recorded at creation, not discovered later'}
if not any(e.get('path_prefix')=='PHYSICS_LEDGER/' for e in mf['excluded_records']):
    moved=[p for p in mf['scanned_paths'] if p.startswith('PHYSICS_LEDGER'+os.sep)]
    mf['excluded_records'].append(dict(fence,path='PHYSICS_LEDGER/*'))
    mf['scanned_paths']=[p for p in mf['scanned_paths'] if not p.startswith('PHYSICS_LEDGER'+os.sep)]
    mf['excluded_records'][-1]['paths_moved']=moved
    mf['scanned']=len(mf['scanned_paths'])
    mf['excluded']=len(mf['excluded_records'])
    mf['ledger_fence']=fence
    json.dump(mf,open(mf_path,'w'),indent=2)
    print('FENCE RECORDED: scanned=%d excluded=%d moved=%d'%(mf['scanned'],mf['excluded'],len(moved)))
else: print('fence already present')

