#!/usr/bin/env python3
# PART A - owner edge correction 2026-08-23: reattach w1_wz_map + u1 to FORMALISM.
import json, os
P=os.path.join(os.path.dirname(os.path.abspath(__file__)), '..','provenance','claims.json')
d=json.load(open(P))
MOVE={'rung7_w1_wz_map','u1_form_universality'}
EVID=("OWNER EDGE CORRECTION 2026-08-23 (adjudication; prior migration retained as history). "
      "Provenance chain: V2 preliminary split (17 formalism-only / 6 ontology-dependent / "
      "4 ambiguous) -> edge review (tier-vs-edge tension surfaced on both nodes) -> genericity "
      "evidence -> owner correction. Evidence from each node's own first clause: "
      "rung7_w1_wz_map declares GENERIC -- not uniquely GRUT (differentiator: standard "
      "relaxing-response -> w(z) map); u1_form_universality declares GENERIC/BORROWED and "
      "asserts the form is universal over ANY local causal open quantum system "
      "(Feynman-Vernon / Caldeira-Leggett). A claim universal over any open quantum system "
      "cannot depend on GRUT's particular ontological stance. Use-vs-mention: ontology "
      "vocabulary, borrowed content. Tiers remain shown; the edges were wrong, not the tiers.")
fixed=[]
for c in d['claims']:
    if c['id'] not in MOVE: continue
    for fld in ('depends_on','attaches_to'):
        v=c.get(fld)
        lst=v if isinstance(v,list) else ([v] if v else [])
        if 'rung1_ontology_finite_memory' in lst:
            lst[lst.index('rung1_ontology_finite_memory')]='rung1_inin_formalism'
            c[fld]=lst
            fixed.append((c['id'],fld))
    en=c.setdefault('edge_note',{})
    en['rung1_split_2026_08_23']=('SUPERSEDED by owner edge correction same day -- retained as history: '
        'was ONTOLOGY per V2 preliminary classification.')
    en['rung1_split_2026_08_23_owner_correction']=EVID
json.dump(d,open(P,'w'),indent=1)
print('reattached:',fixed)
