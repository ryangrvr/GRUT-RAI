# HISA-01 — Repaired / Re-adjudicated 43 Occurrences

Repair population derived mechanically from the containment audit.
19 passing occurrences untouched. 43 fresh adjudications, each
validated by exact byte containment against the frozen package.

## Accounting

| population | count |
|---|---|
| verified before (PASS_*) | 19 |
| repaired / re-adjudicated | 43 |
| total | 62 |

## Change status

| status | count |
|---|---|
| JUDGMENT_CHANGED | 30 |
| NEWLY_UNRESOLVED | 5 |
| SAME_JUDGMENT_RE_GROUNDED | 8 |

## Repaired records

**stmt 0 — `gauge`** (JUDGMENT_CHANGED)
- original: FAIL_MALFORMED_REFERENCE
- repaired: SEMANTIC / LOCALLY_TYPABLE / UNSPECIFIED / LEGITIMATE
- evidence (exact_source_line): exact_source_line: 'the gauge/scheme/prescription-dependent part of the object'
- LOCALLY ESTABLISHED. The line names gauge as one of the dependence axes (gauge/scheme/prescription) that the low-omega TT transport class carries explicitly; no gauge transformation or gauge object is constructed on this line.

**stmt 1 — `Mori-Zwanzig`** (JUDGMENT_CHANGED)
- original: FAIL_MALFORMED_REFERENCE
- repaired: SEMANTIC / EXPLICITLY_UNRESOLVED / UNSPECIFIED / UNRESOLVED
- evidence (exact_source_line): exact_source_line: 'DOES NOT DENOTE A UNIQUE OBJECT'
- EXPLICITLY UNRESOLVED BY THE SOURCE. The statement itself says the phrase 'the Mori-Zwanzig kernel' DOES NOT DENOTE A UNIQUE OBJECT; the frozen evidence preserves the ambiguity rather than resolving it.

**stmt 1 — `correlator`** (SAME_JUDGMENT_RE_GROUNDED)
- original: FAIL_SOURCE_NOT_CONTAINED
- repaired: SEMANTIC / LOCALLY_TYPABLE / INFERABLE / LEGITIMATE
- evidence (exact_source_line): exact_source_line: 'committing the system/bath partition yields only the FREE bath correlator (super-Ohmic, collisionless-AT-FREE-LEVEL)'
- LOCALLY ESTABLISHED. The free bath correlator is characterized as super-Ohmic and collisionless-AT-FREE-LEVEL and is the yield of the first transport-fork step; it does not by itself decide the fork.

**stmt 1 — `cutoff`** (JUDGMENT_CHANGED)
- original: FAIL_MALFORMED_REFERENCE
- repaired: SEMANTIC / LOCALLY_TYPABLE / INFERABLE / LEGITIMATE
- evidence (exact_source_line): exact_source_line: 'memory stays cutoff-set (tau_c~1/omega_c)'
- LOCALLY ESTABLISHED. The line asserts 'memory stays cutoff-set (tau_c~1/omega_c)' in the context of the ladder / slowest-kernel timing argument; the cutoff referent is a memory-time scale, not a named UV regulator symbol.

**stmt 1 — `inner product`** (JUDGMENT_CHANGED)
- original: FAIL_MALFORMED_REFERENCE
- repaired: SEMANTIC / LOCALLY_TYPABLE / INFERABLE / LEGITIMATE
- evidence (exact_source_line): exact_source_line: 'conventionally uses the KUBO-MORI (canonical) inner product'
- LOCALLY ESTABLISHED. The line states that the Mori-Zwanzig projection conventionally uses the Kubo-Mori (canonical) inner product, and that the Kubo correlation carries C_K. The inner-product object is conventionally identified, not formally defined here.

**stmt 2 — `GAUGE`** (SAME_JUDGMENT_RE_GROUNDED)
- original: FAIL_SOURCE_NOT_CONTAINED
- repaired: SEMANTIC / LOCALLY_TYPABLE / UNSPECIFIED / LEGITIMATE
- evidence (exact_source_line): exact_source_line: 'THE 4D-COVARIANT AVAILABILITY OF THE WARD-SOURCED GAUGE-ORBIT ZERO'
- LOCALLY ESTABLISHED. The line names the 4d-covariant availability of the Ward-sourced gauge-orbit zero (the KC5-reserved covariantization). The gauge prescription itself is not formally typed.

**stmt 2 — `response kernel`** (JUDGMENT_CHANGED)
- original: FAIL_TERM_EVIDENCE_MISMATCH
- repaired: SEMANTIC / LOCALLY_TYPABLE / INFERABLE / LEGITIMATE
- evidence (exact_source_line): exact_source_line: 'GR's own response kernel carries a scalar component TWICE its spin-2 one'
- LOCALLY ESTABLISHED. The line gives the linearized Einstein-Hilbert response structure (1/2)k^2[P^(2)-2P^(0,s)] and states GR's own response kernel carries a scalar component twice its spin-2 one.

**stmt 4 — `projector`** (SAME_JUDGMENT_RE_GROUNDED)
- original: FAIL_CONTEXT_NOT_CONTAINED
- repaired: SEMANTIC / LOCALLY_TYPABLE / INFERABLE / LEGITIMATE
- evidence (exact_source_line): exact_source_line: 'K^R = alpha*chi*P^TT'
- LOCALLY ESTABLISHED. The TT projector P^TT appears as the projector factor of the TT response kernel K^R = alpha*chi*P^TT and as the subject of the projector-orthogonality obstruction; no explicit projector formula is supplied in this statement.

**stmt 5 — `Mori-Zwanzig`** (JUDGMENT_CHANGED)
- original: FAIL_SOURCE_NOT_CONTAINED
- repaired: SEMANTIC / NOT_SPECIFIED / UNSPECIFIED / UNRESOLVED
- evidence (exact_source_line): exact_source_line: '**C** the Mori-Zwanzig projection P'
- NOT ESTABLISHED FROM SUPPLIED EVIDENCE. Named as a distinct enumerated construction choice; no definition of the projection is supplied.

**stmt 5 — `projection P`** (JUDGMENT_CHANGED)
- original: FAIL_SOURCE_NOT_CONTAINED
- repaired: SEMANTIC / NOT_SPECIFIED / UNSPECIFIED / UNRESOLVED
- evidence (exact_source_line): exact_source_line: '**C** the Mori-Zwanzig projection P'
- NOT ESTABLISHED FROM SUPPLIED EVIDENCE. Named (P, in the Mori-Zwanzig construction) but not defined; mathematical type unspecified.

**stmt 5 — `system/bath`** (JUDGMENT_CHANGED)
- original: FAIL_SOURCE_NOT_CONTAINED
- repaired: SEMANTIC / NOT_SPECIFIED / UNSPECIFIED / UNRESOLVED
- evidence (exact_source_line): exact_source_line: '**B** system/bath partition'
- NOT ESTABLISHED FROM SUPPLIED EVIDENCE. Named as a distinct enumerated construction choice; no definition, type, or construction is supplied on this line.

**stmt 6 — `cutoff`** (JUDGMENT_CHANGED)
- original: FAIL_SOURCE_NOT_CONTAINED
- repaired: SEMANTIC / NOT_SPECIFIED / UNSPECIFIED / UNRESOLVED
- evidence (exact_source_line): exact_source_line: '**F** cutoff/separation'
- NOT ESTABLISHED FROM SUPPLIED EVIDENCE. Named as a distinct enumerated construction choice; no cutoff/separation object is defined on this line.

**stmt 6 — `inner product`** (JUDGMENT_CHANGED)
- original: FAIL_SOURCE_NOT_CONTAINED
- repaired: SEMANTIC / NOT_SPECIFIED / UNSPECIFIED / UNRESOLVED
- evidence (exact_source_line): exact_source_line: '**D** inner-product choice'
- LOCALLY ESTABLISHED ONLY AS ENUMERATED. The enumeration lists an inner-product choice (D) and separately 'the state supplying the inner product' (E) as distinct entries; neither is defined.

**stmt 7 — `GAUGE`** (JUDGMENT_CHANGED)
- original: FAIL_MALFORMED_REFERENCE
- repaired: SEMANTIC / LOCALLY_TYPABLE / UNSPECIFIED / LEGITIMATE
- evidence (exact_source_line): exact_source_line: 'that K_R annihilates the FULL 4d gauge orbit'
- LOCALLY ESTABLISHED. The line states that K_R annihilates the FULL 4d gauge orbit (the Ward-sourced gauge-orbit zero). The gauge prescription object itself is not formally typed here.

**stmt 7 — `correlator`** (JUDGMENT_CHANGED)
- original: FAIL_MALFORMED_REFERENCE
- repaired: SEMANTIC / LOCALLY_TYPABLE / INFERABLE / LEGITIMATE
- evidence (exact_source_line): exact_source_line: 'the symmetrized correlator of any genuine state is PSD by construction'
- LOCALLY ESTABLISHED. The line states the symmetrized correlator of any genuine state is PSD by construction, in the argument ruling out constitutive symmetrized correlators.

**stmt 7 — `system/bath`** (JUDGMENT_CHANGED)
- original: FAIL_SOURCE_NOT_CONTAINED
- repaired: SEMANTIC / LOCALLY_TYPABLE / UNSPECIFIED / LEGITIMATE
- evidence (exact_source_line): exact_source_line: '+3 declared inputs: system/bath split, Gaussian/linear-response truncation, background Lorentzian causal structure. STANCE, not derivation.'
- LOCALLY ESTABLISHED AS A DECLARED INPUT. The line lists '+3 declared inputs: system/bath split, Gaussian/linear-response truncation, background Lorentzian causal structure. STANCE, not derivation.' The split is declared as a construction input; its internal specification is not given.

**stmt 8 — `gauge`** (JUDGMENT_CHANGED)
- original: FAIL_MALFORMED_REFERENCE
- repaired: SEMANTIC / LOCALLY_TYPABLE / UNSPECIFIED / LEGITIMATE
- evidence (exact_source_line): exact_source_line: 'the FRW gauge-allowed bilinear response space is 11-dimensional (two independent constructions, countersigned)'
- LOCALLY ESTABLISHED. The line gives the FRW gauge-allowed bilinear response space as 11-dimensional with two independent constructions, countersigned. The gauge prescription itself is not formally typed.

**stmt 9 — `susceptibility`** (SAME_JUDGMENT_RE_GROUNDED)
- original: FAIL_SOURCE_NOT_CONTAINED
- repaired: SEMANTIC / LOCALLY_TYPABLE / INFERABLE / LEGITIMATE
- evidence (exact_source_line): exact_source_line: 'if the vacuum susceptibility contains a second dynamical scale'
- LOCALLY ESTABLISHED. The line names 'the vacuum susceptibility' as the object whose possible second dynamical scale (e.g. J~omega^3/(1+omega^2 tau^2) or an internal resonance/diffusive mode) is the remaining falsifier. Its construction is not defined on this line.

**stmt 10 — `KUBO`** (JUDGMENT_CHANGED)
- original: FAIL_SOURCE_NOT_CONTAINED
- repaired: SEMANTIC / LOCALLY_TYPABLE / INFERABLE / LEGITIMATE
- evidence (exact_source_line): exact_source_line: 'conventionally uses the KUBO-MORI'
- LOCALLY ESTABLISHED. The line states the Mori-Zwanzig projection conventionally uses the KUBO-MORI inner product; the convention is named, not formally defined here.

**stmt 10 — `Mori-Zwanzig`** (JUDGMENT_CHANGED)
- original: FAIL_MALFORMED_REFERENCE
- repaired: SEMANTIC / LOCALLY_TYPABLE / UNSPECIFIED / LEGITIMATE
- evidence (exact_source_line): exact_source_line: 'Mori-Zwanzig projection for a quantum system conventionally uses the KUBO-MORI'
- LOCALLY ESTABLISHED. The Mori-Zwanzig projection is named with its conventional (Kubo-Mori) inner product pairing; the projection object is not formally defined on this line.

**stmt 11 — `Green's function`** (JUDGMENT_CHANGED)
- original: FAIL_MALFORMED_REFERENCE
- repaired: SEMANTIC / LOCALLY_TYPABLE / INFERABLE / LEGITIMATE
- evidence (exact_source_line): exact_source_line: 'a STABLE late-time Green's function without SECULAR BLOW-UP'
- LOCALLY ESTABLISHED. The line poses the remaining open computation as whether the Delta_4 inverse on de Sitter admits a STABLE late-time Green's function without secular blow-up; a stability question, not a construction.

**stmt 11 — `gauge`** (SAME_JUDGMENT_RE_GROUNDED)
- original: FAIL_MALFORMED_REFERENCE
- repaired: SEMANTIC / NOT_SPECIFIED / UNSPECIFIED / UNRESOLVED
- evidence (exact_source_line): exact_source_line: 'leaning 'gauge=harmless/stable' -- so recorded as CONTESTED'
- The line leans 'gauge=harmless/stable' for the <T_ab T_cd> two-point and the critic flagged the synthesis for that lean; the gauge treatment is recorded as CONTESTED. No gauge object is defined on this line.

**stmt 11 — `projector`** (JUDGMENT_CHANGED)
- original: FAIL_MALFORMED_REFERENCE
- repaired: SEMANTIC / LOCALLY_TYPABLE / INFERABLE / LEGITIMATE
- evidence (exact_source_line): exact_source_line: 'a tracefree projector P^TT that annihilates exactly that mode'
- LOCALLY ESTABLISHED. The line defines a tracefree projector P^TT that annihilates exactly the trace mode (the double-trace eta.eta.P^TT is identically zero); no explicit projector formula is supplied here.

**stmt 12 — `gauge`** (NEWLY_UNRESOLVED)
- original: FAIL_WRONG_EVIDENCE_SCOPE
- repaired: SEMANTIC / EXPLICITLY_UNRESOLVED / UNSPECIFIED / UNRESOLVED
- evidence (exact_source_line): exact_source_line: 'OWNER-DECLARED and UNDERDEFINED'
- EXPLICITLY UNRESOLVED BY THE SOURCE. The line states that the TT-bath declaration does not establish that the TT-bath declaration is the unique admissible gauge choice; D3(iii), the graviton-bath state/gauge prescription, is OWNER-DECLARED and UNDERDEFINED.

**stmt 13 — `gauge`** (NEWLY_UNRESOLVED)
- original: FAIL_SOURCE_NOT_CONTAINED
- repaired: SEMANTIC / EXPLICITLY_UNRESOLVED / UNSPECIFIED / UNRESOLVED
- evidence (exact_source_line): exact_source_line: 'OWNER-DECLARED and UNDERDEFINED'
- EXPLICITLY UNRESOLVED BY THE SOURCE (duplicate statement of S12). The TT-bath gauge prescription D3(iii) is OWNER-DECLARED and UNDERDEFINED.

**stmt 14 — `projection P`** (JUDGMENT_CHANGED)
- original: FAIL_MALFORMED_REFERENCE
- repaired: SEMANTIC / NOT_SPECIFIED / UNSPECIFIED / UNRESOLVED
- evidence (exact_source_line): exact_source_line: 'the projection P'
- NOT ESTABLISHED FROM SUPPLIED EVIDENCE. Named in the enumeration but not defined on this line.

**stmt 14 — `system/bath`** (JUDGMENT_CHANGED)
- original: FAIL_MALFORMED_REFERENCE
- repaired: SEMANTIC / NOT_SPECIFIED / UNSPECIFIED / UNRESOLVED
- evidence (exact_source_line): exact_source_line: 'system/bath partition'
- NOT ESTABLISHED FROM SUPPLIED EVIDENCE. Named in the enumeration > system/bath partition, the projection P, inner-product choice, the state supplying it, cutoff; not defined on this line.

**stmt 15 — `response function`** (JUDGMENT_CHANGED)
- original: FAIL_MALFORMED_REFERENCE
- repaired: SEMANTIC / LOCALLY_TYPABLE / UNSPECIFIED / LEGITIMATE
- evidence (exact_source_line): exact_source_line: 'the equivalence class of response functionals chi(omega,k) producing identical observable transport under admissible coarse-grainings'
- LOCALLY ESTABLISHED. The line defines 'constitutive organization' (glossary, provisional/revisable per u0) as the equivalence class of response functionals chi(omega,k) producing identical observable transport under admissible coarse-grainings.

**stmt 17 — `coarse-grain`** (SAME_JUDGMENT_RE_GROUNDED)
- original: FAIL_WRONG_EVIDENCE_SCOPE
- repaired: SEMANTIC / NOT_SPECIFIED / UNSPECIFIED / UNRESOLVED
- evidence (exact_source_line): exact_source_line: 'u6's already-held coarse-graining/slow-variable conditional'
- The line names u6's already-held coarse-graining/slow-variable conditional (staying LIVE and un-discharged); the coarse-graining operation itself is not defined on this line.

**stmt 19 — `gauge`** (SAME_JUDGMENT_RE_GROUNDED)
- original: FAIL_SOURCE_NOT_CONTAINED
- repaired: SEMANTIC / LOCALLY_TYPABLE / UNSPECIFIED / LEGITIMATE
- evidence (exact_source_line): exact_source_line: 'the synchronous-gauge computation reproduces the gauge-invariant content of the gauge-unfixed computation'
- LOCALLY ESTABLISHED. The line gives A4 PASS: the synchronous-gauge computation reproduces the gauge-invariant content of the gauge-unfixed computation; the transformation to synchronous exists with residual family zeta^0 = C(x)/a, zeta_i = C_i.

**stmt 20 — `Mori-Zwanzig`** (JUDGMENT_CHANGED)
- original: FAIL_MALFORMED_REFERENCE
- repaired: SEMANTIC / LOCALLY_TYPABLE / UNSPECIFIED / LEGITIMATE
- evidence (exact_source_line): exact_source_line: 'the Mori-Zwanzig projection conventionally uses the KUBO-MORI correlation'
- LOCALLY ESTABLISHED (print block). The statement says the Mori-Zwanzig projection conventionally uses the KUBO-MORI correlation; the pairing is stated, not formally defined.

**stmt 21 — `Mori-Zwanzig`** (JUDGMENT_CHANGED)
- original: FAIL_SOURCE_NOT_CONTAINED
- repaired: SEMANTIC / NOT_SPECIFIED / UNSPECIFIED / UNRESOLVED
- evidence (exact_source_line): exact_source_line: 'rung3's 'Mori-Zwanzig'
- The mention occurs as a truncated print-block fragment ("rung3's 'Mori-Zwanzig"); the frozen evidence does not establish which Mori-Zwanzig object is meant. The phrase is ambiguous in the supplied evidence.

**stmt 22 — `correlator`** (JUDGMENT_CHANGED)
- original: FAIL_MALFORMED_REFERENCE
- repaired: SEMANTIC / LOCALLY_TYPABLE / INFERABLE / LEGITIMATE
- evidence (exact_source_line): exact_source_line: 'the rung3 trace-correlator route ONLY'
- LOCALLY ESTABLISHED. The line names the rung3 trace-correlator route (ONLY) as the pending derivation route whose taking would cost a new +1 (relocation, not discharge).

**stmt 22 — `gauge`** (SAME_JUDGMENT_RE_GROUNDED)
- original: FAIL_MALFORMED_REFERENCE
- repaired: SEMANTIC / NOT_SPECIFIED / UNSPECIFIED / UNRESOLVED
- evidence (exact_source_line): exact_source_line: 'comoving-gauge identification'
- The line invokes comoving-gauge identification as gauge-choice terminology in the ISW/delta^0 computation context; no gauge object is defined on this line.

**stmt 23 — `coarse-grain`** (JUDGMENT_CHANGED)
- original: FAIL_SOURCE_NOT_CONTAINED
- repaired: SEMANTIC / LOCALLY_TYPABLE / INFERABLE / LEGITIMATE
- evidence (exact_source_line): exact_source_line: 'renormalization/coarse-graining is an information-projection'
- LOCALLY ESTABLISHED. The line states renormalization/coarse-graining is an information-projection and that Wilsonian coarse-graining as information loss is the Wilson motif -- explicitly a generic motif, NOT uniquely GRUT.

**stmt 24 — `gauge`** (NEWLY_UNRESOLVED)
- original: FAIL_WRONG_EVIDENCE_SCOPE
- repaired: SEMANTIC / NOT_SPECIFIED / UNSPECIFIED / UNRESOLVED
- evidence (exact_source_line): exact_source_line: 'not 'pure gauge by inspection', not an EOM cancellation'
- The term 'gauge' occurs on this line only inside the explicitly REJECTED classification phrase 'pure gauge by inspection'; no gauge object is defined and none is constructed here.

**stmt 25 — `gauge`** (NEWLY_UNRESOLVED)
- original: FAIL_SOURCE_NOT_CONTAINED
- repaired: SEMANTIC / NOT_SPECIFIED / UNSPECIFIED / UNRESOLVED
- evidence (exact_source_line): exact_source_line: 'not 'pure gauge by inspection', not an EOM cancellation'
- The term 'gauge' occurs on this line only inside the explicitly REJECTED classification phrase 'pure gauge by inspection'; no gauge object is defined and none is constructed here.

**stmt 26 — `gauge`** (NEWLY_UNRESOLVED)
- original: FAIL_SOURCE_NOT_CONTAINED
- repaired: SEMANTIC / NOT_SPECIFIED / UNSPECIFIED / UNRESOLVED
- evidence (exact_source_line): exact_source_line: 'not 'pure gauge by inspection', not an EOM cancellation'
- The term 'gauge' occurs on this line only inside the explicitly REJECTED classification phrase 'pure gauge by inspection'; no gauge object is defined and none is constructed here.

**stmt 27 — `Mori-Zwanzig`** (JUDGMENT_CHANGED)
- original: FAIL_SOURCE_NOT_CONTAINED
- repaired: SEMANTIC / LOCALLY_TYPABLE / INFERABLE / LEGITIMATE
- evidence (exact_source_line): exact_source_line: 'Mori-Zwanzig: choosing a projector P IS the partition (coarse-graining -> split)'
- LOCALLY ESTABLISHED. The statement states the MZ ordering claim: choosing a projector P IS the partition (coarse-graining -> split).

**stmt 28 — `Mori-Zwanzig`** (JUDGMENT_CHANGED)
- original: FAIL_MALFORMED_REFERENCE
- repaired: SEMANTIC / LOCALLY_TYPABLE / INFERABLE / LEGITIMATE
- evidence (exact_source_line): exact_source_line: '**Mori-Zwanzig:** choosing the projector **P** *is* the partition'
- LOCALLY ESTABLISHED (markdown form of the S27 claim). The statement states: Mori-Zwanzig -- choosing the projector P *is* the partition.

**stmt 28 — `projector`** (JUDGMENT_CHANGED)
- original: FAIL_SOURCE_NOT_CONTAINED
- repaired: SEMANTIC / LOCALLY_TYPABLE / INFERABLE / LEGITIMATE
- evidence (exact_source_line): exact_source_line: 'choosing the projector **P** *is* the partition'
- LOCALLY ESTABLISHED. The markdown statement states the same MZ ordering claim: choosing the projector P *is* the partition (coarse-graining -> split).

**stmt 29 — `Mori-Zwanzig`** (JUDGMENT_CHANGED)
- original: FAIL_MALFORMED_REFERENCE
- repaired: SEMANTIC / LOCALLY_TYPABLE / INFERABLE / LEGITIMATE
- evidence (exact_source_line): exact_source_line: 'Mori-Zwanzig inner product there is no ladder to inherit'
- LOCALLY ESTABLISHED (print block). The mention is the conventional Mori-Zwanzig inner product pairing in the rung3 adverse reading.

**stmt 29 — `inner product`** (JUDGMENT_CHANGED)
- original: FAIL_SOURCE_NOT_CONTAINED
- repaired: SEMANTIC / LOCALLY_TYPABLE / INFERABLE / LEGITIMATE
- evidence (exact_source_line): exact_source_line: 'Mori-Zwanzig inner product there is no ladder to inherit'
- LOCALLY ESTABLISHED (print block). The statement says: on the CONVENTIONAL Mori-Zwanzig inner product there is no ladder to inherit (rung3 adverse reading).

