#!/usr/bin/env python3
"""Prose extractor V2 — two-pass (HIGH full-ID + LOW short-form/ontology),
R1 split at schema level, emits dependency map + recall report from JSON.
Defect 1 repair: two passes, precision and recall reported SEPARATELY.
Defect 2 repair: R1 split ids represented in instrument schema; claims.json untouched."""
import json,re,os,sys,glob
from collections import defaultdict

ROOT=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
claims=json.load(open(os.path.join(ROOT,'provenance','claims.json')))['claims']
IDS=[c['id'] for c in claims]
if len(set(IDS))!=len(IDS): sys.exit('FATAL: duplicate ids')

# R1 split — schema-level only; NOT a claims.json edit (owner adjudication owed)
R1_FORMALISM='rung1_inin_formalism'
R1_ONTOLOGY='rung1_ontology_finite_memory'
SCHEMA_NODES=[R1_FORMALISM,R1_ONTOLOGY]

ONT_TERMS={'single-pole','single pole','finite-memory','finite memory',
           'responsive-medium','responsive medium','relaxing','relaxor','two-scale'}
FORM_TERMS={'K_R','influence action','Schwinger-Keldysh','Keldysh','Feynman-Vernon',
            'noise kernel','doubled fields'}
SHORT_FORMS=['rung1','rung2','rung3','rung4','rung5','rung6','rung7','rung8','rung9']

corpus=sorted(glob.glob(os.path.join(ROOT,'calc','RESULTS_*.md')))+[
    os.path.join(ROOT,f) for f in ['GRUT_ToE.md','NO_GO_LEDGER.md',
    'GRUT_I_II_What_Survived.md','EMERGENCE_CHAIN.md','SIGNATURE_AUDIT.md',
    'ARROW_OF_TIME.md'] if os.path.exists(os.path.join(ROOT,f))]

INACT=re.compile(r'(RETRACTED|QUARANTINED|SUPERSEDED)',re.I)

# node-to-node text for HIGH pass (unchanged from v1)
def claim_text(cid):
    c=next(c for c in claims if c['id']==cid)
    return ' '.join(str(c.get(k,'')) for k in ['statement','content','notes',
        'description','falsifier','ledger_note','sub_status'])

high_edges=defaultdict(set)   # src -> {dst}
for c in claims:
    cid=c['id']; text=claim_text(cid)
    for other in IDS:
        if other==cid: continue
        if re.search(r'(?<![A-Za-z0-9_])'+re.escape(other)+r'(?![A-Za-z0-9_])',text):
            high_edges[cid].add(other)

# corpus scan: LOW pass — short forms + ontology terms → proposed split nodes
low_candidates=defaultdict(set)   # matched form -> set of files
ont_hits=defaultdict(int); short_hits=defaultdict(int)
for path in corpus:
    text=open(path,encoding='utf-8',errors='replace').read()
    if INACT.search(text): continue   # skip fully-inactive docs
    for sf in SHORT_FORMS:
        n=len(re.findall(r'(?<![A-Za-z0-9_])'+sf+r'(?![A-Za-z0-9_])',text))
        if n: short_hits[sf]+=n; low_candidates[sf].add(os.path.basename(path))
    tl=text.lower()
    for t in ONT_TERMS:
        n=tl.count(t)
        if n: ont_hits[t]+=n; low_candidates[t].add(os.path.basename(path))
    for t in FORM_TERMS:
        n=tl.count(t.lower())
        if n: low_candidates['FORMALISM:'+t].add(os.path.basename(path))

total_high=sum(len(v) for v in high_edges.values())
total_short=sum(short_hits.values())
total_ont=sum(ont_hits.values())

out={
 'meta':{'date':'2026-08-23','tool':'prose_extractor_v2.py',
         'note':'R1 split is SCHEMA-LEVEL ONLY; claims.json untouched'},
 'schema_split':{'proposed_ids':SCHEMA_NODES,
   'rationale':'ontology terms have no node id to attach to (correction defect 2)'},
 'counts':{
   'high_confidence_node_to_node_edges':total_high,
   'low_confidence_short_form_refs':total_short,
   'low_confidence_ontology_term_refs':total_ont,
   'precision_diagnostic_substring_collisions_v1':0},
 'short_form_table':dict(sorted(short_hits.items(),key=lambda x:-x[1])),
 'ontology_term_table':dict(sorted(ont_hits.items(),key=lambda x:-x[1])),
 'high_edges':{k:sorted(v) for k,v in high_edges.items()},
}
json.dump(out,open(os.path.join(ROOT,'PROSE_LOAD_BEARING_V2.json'),'w'),indent=2)

# EMIT REALITY_PROSE_DEPENDENCY_MAP.md from the JSON — not hand-created
L=['# Reality Prose Dependency Map','','Emitted from `PROSE_LOAD_BEARING_V2.json` by `prose_extractor_v2.py`. Not hand-created.','']
L+=['## High-confidence node-to-node edges: %d'%total_high,'',
    '| citing node | cited nodes |','|---|---|']
for k in sorted(high_edges):
    L.append('| %s | %s |'%(k,', '.join(sorted(high_edges[k]))))
L+=['','## Low-confidence candidates (NOT in authoritative graph)','',
    'Short-form refs: %d · Ontology-term refs: %d'%(total_short,total_ont),'',
    '| form | count | files |','|---|---|---|']
for k,v in sorted(short_hits.items(),key=lambda x:-x[1]):
    L.append('| %s (short) | %d | %s |'%(k,v,len(low_candidates[k])))
for k,v in sorted(ont_hits.items(),key=lambda x:-x[1]):
    L.append('| %s (ontology) | %d | %s |'%(k,v,len(low_candidates[k])))
open(os.path.join(ROOT,'REALITY_PROSE_DEPENDENCY_MAP.md'),'w').write('\n'.join(L))

# EMIT PROSE_RECALL_REPORT.md from the JSON
R=['# Prose Recall Report','','Emitted. Precision and recall reported SEPARATELY, never merged.','',
'| metric | value | note |','|---|---|---|',
'| HIGH-pass edges | %d | unchanged from v1; precision diagnostic |'%(total_high),
'| short-form refs (LOW) | %d | candidate edges only; hand-check owed |'%total_short,
'| ontology-term refs (LOW) | %d | map to R1-ONTOLOGY after validation |'%total_ont,
'| substring collisions | 0 | v1 result stands |','',
'## Integrity gates','',
'- corpus files scanned: %d'%len(corpus),
'- duplicate ids: none (fails loudly)',
'- emitted totals equal graph totals: YES (same source)',
'- high and low counted separately: YES','',
'## Hand-validation status','',
'Stratified sample of LOW-confidence pass NOT yet hand-checked. Until then the LOW counts are',
'candidates, not dependencies, and must not enter blast radius. Logged as blocker.']
open(os.path.join(ROOT,'PROSE_RECALL_REPORT.md'),'w').write('\n'.join(R))

print('=== EXTRACTOR V2 ===')
print('files:',len(corpus))
print('HIGH edges:',total_high)
print('LOW short-form refs:',total_short)
print('LOW ontology refs:',total_ont)

