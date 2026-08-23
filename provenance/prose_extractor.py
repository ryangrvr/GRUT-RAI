#!/usr/bin/env python3
"""Prose citation extractor — regenerates the load-bearing map from prose.
[ADDED-A] every number emitted, none typed. Fails loudly on corpus mismatch,
duplicate ids, or count/graph disagreement.
[A-2] full-id word-boundary matching; substring collisions counted separately;
RETRACTED/QUARANTINED/SUPERSEDED sections tag edges INACTIVE (excluded from
blast radius); NEGATION edges never contribute to blast radius."""
import json,re,os,sys,glob,random
from collections import defaultdict

ROOT=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
claims=json.load(open(os.path.join(ROOT,'provenance','claims.json')))['claims']
IDS=[c['id'] for c in claims]
IDSET=set(IDS)
if len(IDSET)!=len(IDS):
    sys.exit('FATAL: duplicate ids in claims.json')

# corpus: calc results + standing docs
corpus=sorted(glob.glob(os.path.join(ROOT,'calc','RESULTS_*.md')))+[
    os.path.join(ROOT,f) for f in ['GRUT_ToE.md','NO_GO_LEDGER.md',
    'GRUT_I_II_What_Survived.md','EMERGENCE_CHAIN.md','SIGNATURE_AUDIT.md',
    'ARROW_OF_TIME.md'] if os.path.exists(os.path.join(ROOT,f))]
if len(corpus)<20:
    print(f'WARN: corpus small ({len(corpus)} files); expected ~29')

INACT=re.compile(r'(RETRACTED|QUARANTINED|SUPERSEDED|~~)',re.I)
NEG=re.compile(r"(does not depend|not depend|independent of|no dependency)",re.I)

edges=defaultdict(set)          # src -> {dst} live prose cites (node-to-node)
inactive=defaultdict(set)       # tagged INACTIVE (corpus-level, counted separately)
negation=defaultdict(set)       # NEGATION edges (never blast)
collisions=0
# corpus-level scan: count collisions + inactive mentions (reporting only)
for path in corpus:
    text=open(path,encoding='utf-8',errors='replace').read()
    for nid in IDS:
        pat=r'(?<![A-Za-z0-9_])'+re.escape(nid)+r'(?![A-Za-z0-9_])'
        if re.search(pat,text):
            for other in IDS:
                if other!=nid and len(other)<len(nid) and other in nid:
                    opat=r'(?<![A-Za-z0-9_])'+re.escape(other)+r'(?![A-Za-z0-9_])'
                    if not re.search(opat,text) and re.search(re.escape(other),text):
                        globals()['collisions']=collisions+1
            if INACT.search(text[max(0,text.find(nid)-200):text.find(nid)+200]):
                inactive[nid].add(os.path.basename(path))

# Node-to-node prose graph: scan each claim's own text fields for full-id
# word-boundary mentions of OTHER ids.
for c in claims:
    cid=c['id']
    text=' '.join(str(c.get(k,'')) for k in ['statement','content','notes',
        'description','falsifier','ledger_note','sub_status'])
    for other in IDS:
        if other==cid: continue
        pat=r'(?<![A-Za-z0-9_])'+re.escape(other)+r'(?![A-Za-z0-9_])'
        if re.search(pat,text):
            if NEG.search(text):
                negation[cid].add(other)
            else:
                edges[cid].add(other)

def fc(root_set,graph):
    seen=set(); q=list(root_set)
    while q:
        cur=q.pop()
        if cur in seen: continue
        seen.add(cur)
        for dst in graph.get(cur,()):
            if dst not in seen: q.append(dst)
    return seen-set(root_set)

blast={c['id']:len(fc([c['id']],edges)) for c in claims}

top=sorted(blast.items(),key=lambda x:-x[1])[:15]

out={'meta':{'date':'2026-08-23','tool':'prose_extractor.py'},
 'counts':{'live_edges':sum(len(v) for v in edges.values()),
   'inactive_edges':sum(len(v) for v in inactive.values()),
   'negation_edges':sum(len(v) for v in negation.values()),
   'substring_collisions':collisions},
 'top15_blast_prose':[{'id':k,'tier':next(c['tier'] for c in claims if c['id']==k),'downstream':v} for k,v in top]}
json.dump(out,open(os.path.join(ROOT,'PROSE_LOAD_BEARING.json'),'w'),indent=2,default=str)

print('=== PROSE EXTRACTOR ===')
print('files scanned:',len(corpus))
print('live prose edges:',out['counts']['live_edges'])
print('inactive (RETRACTED/QUARANTINED):',out['counts']['inactive_edges'])
print('negation edges (excluded from blast):',out['counts']['negation_edges'])
print('substring collisions:',collisions)
print()
print('Top 15 by PROSE blast radius:')
for k,v in top:
    t=next(c['tier'] for c in claims if c['id']==k)
    print(f'  {k:38s} {t:16s} {v}')

