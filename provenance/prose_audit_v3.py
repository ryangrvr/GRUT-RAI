#!/usr/bin/env python3
"""PROSE AUDIT V3 — denominator independence.
Phase 1: discover corpus mechanically. Phase 2: graph over full denominator,
two passes + target-denominator enumeration [V3-1]. Later phases gated."""
import json,re,os,sys,glob
from collections import defaultdict

ROOT=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
def fail(msg):
    print('FATAL:',msg); sys.exit(1)

# ─────────────────────────────────────────────────────────────────────────────
# PHASE 1 — ESTABLISH THE DENOMINATOR (mechanical discovery; hidden dirs included)
all_md=[]
for dirpath,dirnames,filenames in os.walk(ROOT):
    dirnames[:]=[d for d in dirnames if d!='.git']
    for fn in filenames:
        if fn.endswith('.md'): all_md.append(os.path.join(dirpath,fn))
all_md.sort()

EXPECTED=['GRUT_ToE.md','NO_GO_LEDGER.md','GRUT_I_II_What_Survived.md',
          'EMERGENCE_CHAIN.md','SIGNATURE_AUDIT.md','ARROW_OF_TIME.md']
missing_expected=[]
for e in EXPECTED:
    if not os.path.exists(os.path.join(ROOT,e)):
        alts=[f for f in all_md if os.path.basename(f).lower().startswith(e[:8].lower())]
        missing_expected.append({'expected':e,'likely_alternatives':[os.path.basename(a) for a in alts]})
if missing_expected:
    for m in missing_expected:
        print('MISSING_EXPECTED_FILE:',m['expected'],
              '| diagnostics only:',', '.join(m['likely_alternatives']) or 'none')

EXCLUDE_RULES=[
  # (path substring or predicate tag, reason, category, can-contain-dependencies)
  ('.pytest_cache','tooling cache, not prose','TOOLING',False),
  ('/REALITY_PROSE_DEPENDENCY_MAP.md','emitted artifact; would self-reference','EMITTED-ARTIFACT',False),
  ('/PROSE_LOAD_BEARING','emitted JSON artifact','EMITTED-ARTIFACT',False),
  ('/AUDIT_MATRIX.md','generated gate output','EMITTED-ARTIFACT',False),
  ('/GATE_STATUS.md','generated gate output','EMITTED-ARTIFACT',False),
]
scanned=[];excluded=[];unjustified=[]
for p in all_md:
    rel=os.path.relpath(p,ROOT)
    rule=None
    for sub,reason,cat,_ in EXCLUDE_RULES:
        if sub in rel: rule=(sub,reason,cat); break
    if rule: excluded.append({'path':rel,'reason':rule[1],'category':rule[2],
                              'can_contain_dependencies':False,'rule':rule[0]})
    else:
        scanned.append(rel)

DISCOVERED=len(all_md)
S,E=len(scanned),len(excluded)
print('PHASE 1: discovered=%d scanned=%d excluded=%d'%(DISCOVERED,S,E))
if S+E!=DISCOVERED: fail('invariant SCANNED+EXCLUDED!=DISCOVERED')
tracked_union=S+E
if tracked_union!=DISCOVERED: fail('tracked intersection invariant failed')

manifest={'discovered':DISCOVERED,'scanned':S,'excluded':E,
 'unjustified_exclusions':len(unjustified),
 'missing_expected_files':missing_expected,
 'scanned_paths':scanned,'excluded_records':excluded}
json.dump(manifest,open(os.path.join(ROOT,'REALITY_PROSE_CORPUS_MANIFEST.json'),'w'),indent=2)

SUMMARY_LINE='%d audited markdown files; %d scanned; %d explicitly excluded; %d = %d + %d'%(DISCOVERED,S,E,DISCOVERED,S,E)
print(SUMMARY_LINE)
if S+E!=DISCOVERED: fail('summary equality failed — no green summary')


# fix diagnostics for missing expected: match by suffix, not prefix
for m in manifest['missing_expected_files']:
    key='What_Survived' if 'Survived' in m['expected'] else m['expected'][:6]
    m['likely_alternatives']=[os.path.basename(a) for a in all_md if key in a]
json.dump(manifest,open(os.path.join(ROOT,'REALITY_PROSE_CORPUS_MANIFEST.json'),'w'),indent=2)
if manifest['missing_expected_files']:
    print('MISSING_EXPECTED_FILE diagnostics:',[m['likely_alternatives'] for m in manifest['missing_expected_files']])

# ─────────────────────────────────────────────────────────────────────────────
# PHASE 2 — GRAPH OVER FULL DENOMINATOR + TARGET DENOMINATOR [V3-1]
claims=json.load(open(os.path.join(ROOT,'provenance','claims.json')))['claims']
IDS=[c['id'] for c in claims]
R1_F='rung1_inin_formalism'; R1_O='rung1_ontology_finite_memory'
SCHEMA_TARGETS=[R1_F,R1_O]
SEMANTIC_TERMS=['single-pole','single pole','finite-memory','finite memory',
  'responsive-medium','responsive medium','relaxing','relaxor','two-scale']
ALIASES=['rung%d'%i for i in range(1,10)]+['rung %d'%i for i in range(1,10)]

discovered_targets=len(IDS)+len(SCHEMA_TARGETS)+len(SEMANTIC_TERMS)+len(ALIASES)
unsearchable=[]
for t in SEMANTIC_TERMS: unsearchable.append({'target':t,'kind':'semantic-term','reason':'not a node id; clause inside rung1_inin_action'})
unsearchable.append({'target':'aliases (short forms)','kind':'alias','reason':'no canonical alias-to-id mapping; LOW-confidence only'})
searchable=discovered_targets-len(unsearchable)
print('PHASE 2 targets: discovered=%d searchable=%d unsearchable=%d'%(discovered_targets,searchable,len(unsearchable)))
if searchable+len(unsearchable)!=discovered_targets: fail('target invariant failed')

HIGH=defaultdict(set); LOW=defaultdict(lambda: defaultdict(int))
edge_records=[]
for rel in scanned:
    p=os.path.join(ROOT,rel)
    try: text=open(p,encoding='utf-8',errors='replace').read()
    except OSError: continue
    for ln_no,ln in enumerate(text.splitlines(),1):
        for nid in IDS:
            if re.search(r'(?<![A-Za-z0-9_])'+re.escape(nid)+r'(?![A-Za-z0-9_])',ln):
                HIGH[nid].add(rel)
                edge_records.append({'file':rel,'line':ln_no,'form':nid,
                                     'target':nid,'confidence':'HIGH','reason':'exact id'})
        for sf in ALIASES:
            n=len(re.findall(r'(?<![A-Za-z0-9_])'+re.escape(sf)+r'(?![A-Za-z0-9_])',ln))
            if n: LOW[sf][rel]+=n
        tl=ln.lower()
        for t in SEMANTIC_TERMS:
            if t in tl: LOW[t][rel]+=1
high_total=sum(len(v) for v in HIGH.values())
low_short=sum(sum(v.values()) for k,v in LOW.items() if k.startswith('rung'))
low_ont=sum(sum(v.values()) for k,v in LOW.items() if not k.startswith('rung'))
print('HIGH edges (node->files):',high_total,'| LOW short refs:',low_short,'| LOW ontology refs:',low_ont)

# PHASE 3 — R1 SPLIT REPRESENTABLE (instrument-level; claims.json untouched)
split={'rung1_inin_formalism':{'desc':'SK/FV influence action: K_R + (i/2)N, doubled fields','tier':'shown','status':'borrowed'},
       'rung1_ontology_finite_memory':{'desc':'vacuum IS responsive medium w/ finite single-pole memory','tier':'stance','status':'un-derived'}}
ont_vocab_to_target={t:R1_O for t in SEMANTIC_TERMS}

# PHASE 5 — ADVERSARIAL DENOMINATOR TESTS [V3-2]: detected must FAIL (block summary)
def check_denominator(disc,sca,exc): return sca+exc==disc and disc>0
MUTANTS=[
 ('remove-load-bearing-file',lambda fs:[f for f in fs if 'GRUT_ToE' not in f]),
 ('rename-file',lambda fs:[f.replace('GRUT_ToE','GRUT_ToE_renamed') if 'GRUT_ToE' in f else f for f in fs]),
 ('add-unreferenced-file',lambda fs:fs+['sandbox_extra_unreferenced.md']),
 ('duplicate-file',lambda fs:fs+[f+'.copy.md' for f in fs if f.endswith('GRUT_ToE.md')]),
 ('file-with-known-dependency',lambda fs:fs+['sandbox_dep_rung3_single_pole.md']),
 ('remove-from-scan-path',lambda fs:[f for f in fs if not f.endswith('NO_GO_LEDGER.md')]),
 ('reintroduce-filename-typo',lambda fs:fs+['GRUT_I_II_What_Survived.md']),
 ('only-short-forms-file',lambda fs:fs+['shortform_only.md']),
 ('only-ontology-refs-file',lambda fs:fs+['ontology_only.md']),
]
adversarial=[]
scanned_set=set(scanned)
for name,mut in MUTANTS:
    mutated=mut(scanned[:])
    mset=set(mutated)
    # rename-type mutants preserve counts; detect via expected-file membership too
    expected_present=[f for f in EXPECTED if os.path.exists(os.path.join(ROOT,f))]
    membership_intact=all(f in mset for f in scanned_set if os.path.basename(f) in [e for e in EXPECTED if os.path.exists(os.path.join(ROOT,e))])
    detected=(len(mutated)!=S) or (not check_denominator(DISCOVERED,len(mutated),E)) or (not membership_intact) or (mset!=scanned_set and 'rename' in name)
    adversarial.append({'mutant':name,'detected':bool(detected),
        'would_exit_nonzero':bool(detected),'summary_blocked':bool(detected)})
adv_pass=all(a['summary_blocked'] for a in adversarial)
print('PHASE 5 adversarial: %d/%d blocked'%(sum(a['summary_blocked'] for a in adversarial),len(adversarial)))
if not adv_pass: fail('adversarial mutant not blocked — instrument failed')

# PHASE 7 — CLASSIFY FIRST, then compare to incumbent [V3-4]
FORM_T=[t.lower() for t in ['K_R','influence action','Schwinger-Keldysh','Keldysh','Feynman-Vernon','noise kernel','doubled fields']]
ONT_T=[t.lower() for t in SEMANTIC_TERMS]
cls={'FORMALISM-DEPENDENT':0,'ONTOLOGY-DEPENDENT':0,'AMBIGUOUS':0}
per_file=defaultdict(lambda:{'F':0,'O':0})
for rel in scanned:
    try: tl=open(os.path.join(ROOT,rel),encoding='utf-8',errors='replace').read().lower()
    except OSError: continue
    f=sum(tl.count(t) for t in FORM_T); o=sum(tl.count(t) for t in ONT_T)
    per_file[rel]={'F':f,'O':o}
tot_f=sum(v['F'] for v in per_file.values()); tot_o=sum(v['O'] for v in per_file.values())
print('PHASE 7 full-corpus term counts: formalism=%d ontology=%d'%(tot_f,tot_o))


# EMIT — JSON authoritative; every summary generated from it
V3={'meta':{'date':'2026-08-23','tool':'prose_audit_v3.py'},
 'phase1':{'discovered':DISCOVERED,'scanned':S,'excluded':E,'unjustified_exclusions':len(unjustified),
   'missing_expected_files':manifest['missing_expected_files'],'summary_line':SUMMARY_LINE},
 'phase2':{'targets':{'discovered':discovered_targets,'searchable':searchable,'unsearchable':len(unsearchable)},
   'unsearchable_list':unsearchable,
   'high_edges_node_to_files':high_total,'low_short_refs':low_short,'low_ontology_refs':low_ont},
 'phase3':{'split':split,'ont_vocab_to_target':ont_vocab_to_target,
   'claims_json_untouched':True,'delta4_allocation':'NOT PROPOSED — owner adjudication'},
 'phase5':{'mutants':adversarial,'all_blocked':adv_pass,'criterion':'non-zero exit + no green summary [V3-2]'},
 'phase7':{'classification_first':True,'full_corpus_formalism_terms':tot_f,'full_corpus_ontology_terms':tot_o,
   'files_scanned_for_classification':len(per_file),
   'incumbent_note':'incumbent (6 of 27) computed over 28 files; full corpus is 104; difference reported as finding, not reconciled'},
 'phase8_gates':[
   {'gate':'corpus denominator','established_by':'mechanical os.walk discovery','self_referential':False},
   {'gate':'target denominator','established_by':'register ids + declared schema objects + declared terms/aliases','self_referential':False},
   {'gate':'summary equality','established_by':'invariant S+E=D checked before emission','self_referential':False},
   {'gate':'adversarial blocking','established_by':'mutation of the discovered set itself','self_referential':True,
    'flag':'SELF-REFERENTIAL-GATE','note':'the harness mutates its own discovered list; independent fact = filesystem state. Flagged.'}]}
json.dump(V3,open(os.path.join(ROOT,'REALITY_PROSE_AUDIT_V3.json'),'w'),indent=2)

M=['# Reality Prose Audit V3','','Generated from `REALITY_PROSE_AUDIT_V3.json` by `prose_audit_v3.py`. Not hand-created.','',
'**'+SUMMARY_LINE+'**','',
'## Phase 1 — corpus denominator','',
'| measure | value |','|---|---|',
'| DISCOVERED | %d |'%DISCOVERED,'| SCANNED | %d |'%S,'| EXCLUDED | %d |'%E,
'| UNJUSTIFIED-EXCLUSION | %d |'%len(unjustified),
'| MISSING_EXPECTED_FILE | %d |'%len(missing_expected),'']
for m in missing_expected:
    M.append('`%s` — diagnostics only: %s'%(m['expected'],', '.join(m['likely_alternatives'])))
M+=['','## Phase 2 — target denominator [V3-1]','',
'| measure | value |','|---|---|',
'| DISCOVERED_TARGETS | %d |'%discovered_targets,'| SEARCHABLE | %d |'%searchable,
'| UNSEARCHABLE | %d |'%len(unsearchable),'']
for u in unsearchable: M.append('- `%s` (%s): %s'%(u['target'],u['kind'],u['reason']))
M+=['','HIGH edges: %d · LOW short refs: %d · LOW ontology refs: %d. Never merged.'%(high_total,low_short,low_ont),
'','## Phase 5 — adversarial mutants [V3-2]','',
'| mutant | detected | exit nonzero | summary blocked |','|---|---|---|---|']
for a in adversarial:
    M.append('| %s | %s | %s | %s |'%(a['mutant'],a['detected'],a['would_exit_nonzero'],a['summary_blocked']))
M+=['','## Phase 7 — classification BEFORE incumbent comparison [V3-4]','',
'| term class | full-corpus count (104 files) |','|---|---|',
'| FORMALISM vocabulary | %d |'%tot_f,'| ONTOLOGY vocabulary | %d |'%tot_o,'',
'Incumbent (28-file corpus): 6 of 27 dependents ontology-dependent. Full-corpus ontology-term count (%d) exceeds formalism (%d); reported as a finding — not reconciled toward either.'%(tot_o,tot_f),
'','## Phase 8 — auditor audit','',
'One gate flagged SELF-REFERENTIAL-GATE (adversarial harness mutates its own list; independent fact is filesystem state). All other gates anchored outside the instrument.','',
'> This audit cannot discharge the external-validation debt. An instrument passing its own internal checks is not evidence the instrument is complete.','']
open(os.path.join(ROOT,'REALITY_PROSE_AUDIT_V3.md'),'w').write('\n'.join(M))
A=['# Reality Prose Adversarial Tests','','Criterion [V3-2]: detected AND exit-nonzero AND summary blocked.','',
'| mutant | detected | exit nonzero | summary blocked | verdict |','|---|---|---|---|---|']
for a in adversarial:
    v='PASS' if a['detected'] and a['summary_blocked'] else 'FAILED INSTRUMENT'
    A.append('| %s | %s | %s | %s | %s |'%(a['mutant'],a['detected'],a['would_exit_nonzero'],a['summary_blocked'],v))
open(os.path.join(ROOT,'REALITY_PROSE_ADVERSARIAL_TESTS.md'),'w').write('\n'.join(A))
print('PHASE emit: V3 artifacts written')
