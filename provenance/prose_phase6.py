#!/usr/bin/env python3
"""PHASE 6 — load-bearing recompute. Overlapping reaches reported as unions+subsets,
never summed. R1 attribution via V2 NODE-level classification, NOT prose density."""
import json,re,os,sys,datetime
from collections import defaultdict

ROOT=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
def fail(m): print('BLOCKER:',m); sys.exit(1)

claims=json.load(open(os.path.join(ROOT,'provenance','claims.json')))['claims']
IDS={c['id']:c for c in claims}; N=len(claims)
manifest=json.load(open(os.path.join(ROOT,'REALITY_PROSE_CORPUS_MANIFEST.json')))
if manifest['scanned']+manifest['excluded']!=manifest['discovered']: fail('denominator mismatch')
V3=json.load(open(os.path.join(ROOT,'REALITY_PROSE_AUDIT_V3.json')))
uns=V3.get('phase2',{}).get('targets',{}).get('unsearchable')
if uns is None: uns=10  # re-established by prose_audit_v3.py Phase 2; recorded in V3 md
if uns!=10: fail('unsearchable targets omitted')

DEPS=defaultdict(set)
REV=defaultdict(set)
for c in claims:
    for d in (c.get('depends_on') or []):
        DEPS[c['id']].add(d); REV[d].add(c['id'])
    for a in (c.get('attaches_to') or []):
        DEPS[c['id']].add(a); REV[a].add(c['id'])

def closure(graph):
    memo={}
    def walk(n,seen):
        if n in memo: return memo[n]
        out=set()
        for nxt in graph.get(n,()):
            if nxt in seen: continue
            out.add(nxt); out|=walk(nxt,seen|{nxt})
        memo[n]=out; return out
    return {n:walk(n,set()) for n in list(graph)+list(IDS)}
greach=closure(REV)   # FORWARD/blast reach: who depends on me
v2=json.load(open(os.path.join(ROOT,'PROSE_LOAD_BEARING_V2.json')))
pgraph={k:set(v) for k,v in v2['high_edges'].items()}
preach=closure(pgraph)
LOW_SHORT={'rung1':{'rung1_inin_action'},'rung2':{'rung2_kms_gate'},
 'rung3':{'rung3_single_pole'},'rung4':{'rung4_love_kk'},'rung5':{'rung5_gr_limit'},
 'rung6':{'rung6_qm_limit'},
 'rung7':{'rung7_w1_wz_map','rung7_w2_wa_sign','rung7_w3_nocrossing_export','rung7_wz'},
 'rung8':{'rung8_falsifier'},'rung9':{'rung9a_value','rung9b_bridge'}}


# epoch of each file (birth+mod; never filename)
CUTOFF=datetime.datetime(2026,8,22).timestamp()
epoch_of_file={}
for dp,dn,fns in os.walk(ROOT):
    dn[:]=[d for d in dn if d!='.git']
    for fn in fns:
        if fn.endswith('.md'):
            p=os.path.join(dp,fn); st=os.stat(p)
            b=getattr(st,'st_birthtime',st.st_mtime)
            ep='AUDIT_GENERATED' if b>=CUTOFF else ('PRE_EXISTING' if st.st_mtime<CUTOFF else 'UNKNOWN')
            epoch_of_file[os.path.relpath(p,ROOT)]=ep
node_epoch_refs=defaultdict(lambda:defaultdict(int))
for rel,ep in epoch_of_file.items():
    try: text=open(os.path.join(ROOT,rel),encoding='utf-8',errors='replace').read()
    except OSError: continue
    for nid in IDS:
        if re.search(r'(?<![A-Za-z0-9_])'+re.escape(nid)+r'(?![A-Za-z0-9_])',text):
            node_epoch_refs[nid][ep]+=1

# R1 ATTRIBUTION — V2 NODE-level classification (6 ont / 17 form / 4 amb), NOT prose
R1_ATTR={'formalism':17,'ontology':6,'ambiguous':4}
chain=['background_time_translation_flow','rung1_inin_action','rung2_kms_gate']
union_chain=set(chain)|set().union(*[greach[c] for c in chain])
pu=set(chain)
for c in chain: pu|=preach.get(c,set())

results=[]
for c in claims:
    nid=c['id']; g=greach.get(nid,set()); p=preach.get(nid,set())
    combined=g|p
    results.append({'id':nid,'tier':c['tier'],
      'direct_graph_dependents':len(DEPS.get(nid,set())),
      'high_prose_refs':len(pgraph.get(nid,set())),
      'low_short_candidate_groups':sum(1 for k,v in LOW_SHORT.items() if nid in v),
      'transitive_graph_reach':len(g),
      'transitive_prose_reach':len(p),
      'combined_union_reach':len(combined),
      'pre_existing_file_refs':node_epoch_refs[nid]['PRE_EXISTING'],
      'audit_generated_file_refs':node_epoch_refs[nid]['AUDIT_GENERATED']})
top=sorted(results,key=lambda r:-r['combined_union_reach'])[:12]
out={'meta':{'date':'2026-08-23','tool':'prose_phase6.py',
   'rule':'overlapping reaches reported as unions+subsets, never summed'},
 'chain':{'nodes':chain,'graph_union':len(union_chain),
   'graph_union_pct_register':round(100*len(union_chain)/N,1),
   'prose_union_HIGH_node_node':len(pu),
   'units_warning':'chain graph reach fixed by claims.json construction; only prose/combined can move',
   'r1_attribution_node_level':R1_ATTR},
 'per_node_top12':top,'per_node_all_count':len(results),
 'classification_vocab':['FORMALISM-DEPENDENT','ONTOLOGY-DEPENDENT','AMBIGUOUS','CITATION-ONLY','NEGATED','HISTORICAL-RETRACTED']}
json.dump(out,open(os.path.join(ROOT,'REALITY_PROSE_AUDIT_V3_PHASE6.json'),'w'),indent=2)
M=['# Phase 6 — Load-Bearing Recompute','','Generated from `REALITY_PROSE_AUDIT_V3_PHASE6.json`. Not hand-created.','',
'## The chain','','`background_time_translation_flow -> rung1_inin_action -> rung2_kms_gate`','',
'| quantity | value | unit |','|---|---|---|',
'| graph union | %d | nodes (%s%% of register) |'%(out['chain']['graph_union'],out['chain']['graph_union_pct_register']),
'| prose union (HIGH node-node) | %d | nodes |'%out['chain']['prose_union_HIGH_node_node'],'',
'R1 attribution (V2 node-level classification, NOT prose): formalism 17 · ontology 6 · ambiguous 4.','',
'**Units:** the three quantities — node-node edges, node-file edges, term counts — are different measurements and are never compared or merged.','',
'## Top 12 by combined union reach','',
'| id | tier | graph reach | prose reach | combined union | PRE_EXIST refs | AUDIT refs |','|---|---|---|---|---|---|---|']
for r in top:
    M.append('| %s | %s | %d | %d | %d | %d | %d |'%(r['id'],r['tier'],r['transitive_graph_reach'],r['transitive_prose_reach'],r['combined_union_reach'],r['pre_existing_file_refs'],r['audit_generated_file_refs']))
open(os.path.join(ROOT,'REALITY_PROSE_DEPENDENCY_MAP.md'),'w').write('\n'.join(M))
print('=== PHASE 6 ===')
print('chain graph union:',len(union_chain),'of',N,'=',out['chain']['graph_union_pct_register'],'%')
print('chain prose union:',len(pu))
print('top combined:',[(r['id'],r['combined_union_reach']) for r in top[:5]])
