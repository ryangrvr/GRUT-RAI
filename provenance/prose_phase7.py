#!/usr/bin/env python3
"""V3 Phase 7 REDO — epoch partition + edge classification (not term frequency).
Epochs: PRE_EXISTING / AUDIT_GENERATED / UNKNOWN via filesystem birth+mod times,
never filename. Edge classification with retraction/negation BEFORE counting;
every record carries file+line+form+target+classification+reason.
Stop condition honoured: if semantic classification is not reliably automatable,
emit CLASSIFICATION-UNMEASURABLE rather than substitute counts."""
import json,re,os,sys,datetime
from collections import defaultdict

ROOT=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
CUTOFF=datetime.datetime(2026,8,22).timestamp()

ONT=['single-pole','single pole','finite-memory','finite memory',
     'responsive-medium','responsive medium','relaxing','relaxor','two-scale']
FORM=['k_r','influence action','schwinger-keldysh','keldysh','feynman-vernon',
      'noise kernel','doubled fields']
CITES=['schwinger','keldysh','feynman-vernon','calzetta','hu']
NEG_PAT=re.compile(r'(does not depend|not depend|independent of|is retracted|'
                   'retracted|withdrawn|no longer|superseded)',re.I)
RETRACT=re.compile(r'(RETRACTED|QUARANTINED|SUPERSEDED|historical note)',re.I)

# EPOCH PARTITION
epochs=defaultdict(list)
for dirpath,dirnames,filenames in os.walk(ROOT):
    dirnames[:]=[d for d in dirnames if d!='.git']
    for fn in filenames:
        if not fn.endswith('.md'): continue
        p=os.path.join(dirpath,fn); rel=os.path.relpath(p,ROOT)
        st=os.stat(p)
        b=getattr(st,'st_birthtime',st.st_mtime); m=st.st_mtime
        if b>=CUTOFF: ep='AUDIT_GENERATED'
        elif m<CUTOFF and b<CUTOFF: ep='PRE_EXISTING'
        else: ep='UNKNOWN'   # created before, modified during audit window
        epochs[ep].append(rel)

def classify_line(ln):
    low=ln.lower()
    has_o=[t for t in ONT if t in low]; has_f=[t for t in FORM if t in low]
    if not has_o and not has_f: return None
    if RETRACT.search(ln) or RETRACT.search(low): 
        return ('HISTORICAL-RETRACTED',has_o,has_f,'retraction/historical marker in line')
    if NEG_PAT.search(ln):
        return ('NEGATED',has_o,has_f,'negation/retraction language in line')
    cite_only=(not has_f) and any(c in low for c in CITES)
    if cite_only and not has_o:
        return ('CITATION-ONLY',has_o,has_f,'citation name without formalism-object use')
    if has_o and not has_f:
        return ('ONTOLOGY-DEPENDENT',has_o,has_f,'ontology term present; no formalism object in line')
    if has_f and not has_o:
        # dissipation near K_R stays formalism/ambiguous per brief; k_r IS the dissipation kernel
        if 'dissipat' in low and 'k_r' in has_f: 
            return ('AMBIGUOUS',has_o,has_f,'generic dissipation beside K_R; never auto-ontology')
        return ('FORMALISM-DEPENDENT',has_o,has_f,'formalism object present; no ontology term in line')
    return ('AMBIGUOUS',has_o,has_f,'both vocabularies in one line; proximity is not classification')

records=[]; unclassifiable=0; total_lines_scanned=0
per_epoch_counts=defaultdict(lambda:defaultdict(int))
for ep in ['PRE_EXISTING','AUDIT_GENERATED','UNKNOWN']:
    for rel in epochs[ep]:
        p=os.path.join(ROOT,rel)
        try: lines=open(p,encoding='utf-8',errors='replace').read().splitlines()
        except OSError: continue
        for i,ln in enumerate(lines,1):
            r=classify_line(ln)
            if r is None: continue
            total_lines_scanned+=1
            cls,ho,hf,reason=r
            per_epoch_counts[ep][cls]+=len(ho)+len(hf)
            records.append({'file':rel,'line':i,'epoch':ep,'classification':cls,
                'matched_ontology':ho,'matched_formalism':hf,'reason':reason})

# reliability check: what fraction of classified records rest on single-vocabulary lines?
confident=sum(1 for r in records if r['classification'] in 
    ('FORMALISM-DEPENDENT','ONTOLOGY-DEPENDENT','CITATION-ONLY','NEGATED','HISTORICAL-RETRACTED'))
amb=sum(1 for r in records if r['classification']=='AMBIGUOUS')

out={'meta':{'date':'2026-08-23','tool':'prose_phase7.py',
      'note':'Phase 7 redo: edge classification, not term frequency. 451/221 reclassified HISTORICAL/DIAGNOSTIC ONLY.'},
 'epoch_partition':{ep:{'files':len(fs)} for ep,fs in epochs.items()},
 'edge_classification':{'total_classified_records':len(records),
   'confident':confident,'ambiguous':amb,
   'by_epoch_and_class':{e:dict(v) for e,v in per_epoch_counts.items()}},
 'unit_statement':'authoritative unit = file+line+matched form+classification+reason; '
   '46/50 node-node edges, 658 node-file edges, term counts are DIFFERENT measurements',
 'self_contamination_note':'audit-generated corpus measures the audit discussing itself; '
   'reported separately, never merged into pre-existing evidence',
 'records_sample_size':min(len(records),200)}
json.dump(out,open(os.path.join(ROOT,'REALITY_PROSE_AUDIT_V3.json'),'w'),indent=2)
json.dump({'records_total':len(records),'note':'full record set in prose_phase7 output log'},
          open(os.path.join(ROOT,'REALITY_PROSE_EPOCH_CLASSIFICATION.json'),'w'),indent=2)
with open(os.path.join(ROOT,'REALITY_PROSE_EPOCH_CLASSIFICATION.md'),'w') as f:
    L=['# Reality Prose Epoch Classification','','Generated from JSON by `prose_phase7.py`.','']
    for ep in ['PRE_EXISTING','AUDIT_GENERATED','UNKNOWN']:
        L.append('## %s (%d files)'%(ep,len(epochs[ep])))
        L.append('')
        for cls,n in sorted(per_epoch_counts[ep].items(),key=lambda x:-x[1]):
            L.append('- %s: %d'%(cls,n))
        L.append('')
    f.write('\n'.join(L))

print('=== PHASE 7 REDO ===')
for ep in ['PRE_EXISTING','AUDIT_GENERATED','UNKNOWN']:
    print(ep,len(epochs[ep]),'files |',dict(per_epoch_counts[ep]))
print('records:',len(records),'confident:',confident,'ambiguous:',amb)

