# OBJECT_IDENTITY_AUDIT_01 (lab artifact)

Commit: `0cf4a9a76faab2e4ed1fb819938ef1dbd4aa9121`

> Identity judgments come ONLY from explicit phrases in the source corpus. No external QFT knowledge applied.

## Summary

- pairs_examined: 21
- SAME_CONSTRUCTION: 2
- DISTINCT_CONSTRUCTION: 0
- RELATED_NOT_IDENTIFIED: 0
- UNRESOLVED: 18
- CONTRADICTORY_SOURCE_STATEMENTS_PRESENT: 1
- pairs_with_no_usable_evidence: 16
- source_statements_used: 305
- explicit_corpus_identifications: 36
- explicit_corpus_distinctions: 8

## Pair classifications

### cutoff / separation scale ⟷ gauge / field-redefinition freedom
- classification: **UNRESOLVED** (29 statement(s))
- distribution: {'RELATED_NOT_IDENTIFIED': 2, 'UNRESOLVED': 23, 'SAME_CONSTRUCTION': 4}

- `PHYSICS_LEDGER/WALL_KR_D5_RENORMALIZATION_RESULT.json:191` [RELATED_NOT_IDENTIFIED, MEDIUM] via relational phrase
  -   "THE DETERMINATION, from the frozen texts -- CORRECTED BY THE ADVERSARIAL REVIEW (the first draft classified A/UNIQUE and the review REFUTED it on the scheme level; the refutation is adopted): TWO t
- `PHYSICS_LEDGER/wall_kr_d5_audit_run3.log:37` [UNRESOLVED, LOW] via co-occurrence only
  -   note THE DETERMINATION, from the frozen texts -- CORRECTED BY THE ADVERSARIAL REVIEW (the first draft classified A/UNIQUE and the review REFUTED it on the scheme level; the refutation is adopted): T
- `calc/class_c_solver.py:11` [UNRESOLVED, LOW] via co-occurrence only
  -   * EVERY clock/gauge/regulator/approximation/boundary parameter is obtained CONTRACT (hard):   * EVERY clock/gauge/regulator/approximation/boundary parameter is obtained     through provenance.class_
- `program/CANDIDATE_MINING_02.md:223` [UNRESOLVED, LOW] via co-occurrence only
  - > system/bath partition, the projection P, inner-product choice, the state supplying it, cutoff > construction choices, and the record must not collapse distinct choices — slow-variable selection, > s
- `program/CANDIDATE_MINING_02.md:224` [UNRESOLVED, LOW] via co-occurrence only
  - > choice, gauge/field-redefinition freedom — into one "effective description" decision **unless the > system/bath partition, the projection P, inner-product choice, the state supplying it, cutoff > ch

### cutoff / separation scale ⟷ inner product / state
- classification: **UNRESOLVED** (10 statement(s))
- distribution: {'UNRESOLVED': 8, 'SAME_CONSTRUCTION': 2}

- `program/CANDIDATE_MINING_02.md:274` [UNRESOLVED, LOW] via co-occurrence only
  - **A** slow-variable selection · **B** system/bath partition · **C** the Mori-Zwanzig projection P · **A** slow-variable selection · **B** system/bath partition · **C** the Mori-Zwanzig projection P · 
- `program/CANDIDATE_MINING_02.md:275` [UNRESOLVED, LOW] via co-occurrence only
  - **D** inner-product choice · **E** the state supplying the inner product · **F** cutoff/separation **A** slow-variable selection · **B** system/bath partition · **C** the Mori-Zwanzig projection P · *
- `program/CANDIDATE_MINING_02.md:276` [UNRESOLVED, LOW] via co-occurrence only
  - scale · **G** gauge/field-redefinition freedom. **D** inner-product choice · **E** the state supplying the inner product · **F** cutoff/separation scale · **G** gauge/field-redefinition freedom.
- `program/DEPENDENCY_EQUIVALENCE_AUDIT_01.md:55` [UNRESOLVED, LOW] via co-occurrence only
  - | 2 | **B slow variables ↔ C `P`** | **UNRESOLVED** | H established these cannot be declared identical | | 1 | **A split ↔ E cutoff** | **UNRESOLVED** | the corpus carries an actual historical contrad
- `program/DEPENDENCY_EQUIVALENCE_AUDIT_01_BRIEF.md:48` [UNRESOLVED, LOW] via co-occurrence only
  - | **D** | inner product / the state supplying it | | **C** | projection **P** | | **D** | inner product / the state supplying it | | **E** | cutoff / separation-scale choice |

### cutoff / separation scale ⟷ projection P
- classification: **UNRESOLVED** (9 statement(s))
- distribution: {'UNRESOLVED': 9}

- `PHYSICS_LEDGER/WALL_KR_D5_EXECUTION_RESULT.json:191` [UNRESOLVED, LOW] via co-occurrence only
  -    "msg": "CONTROL: #1 WRONG REGULATOR CONTINUATION: continuing the measure in d while freezing the projector algebra at d = 3 (dropped evanescent terms) CHANGES the MS finite part -- the gate detects
- `PHYSICS_LEDGER/WALL_KR_DISTINCTIVENESS_LEDGER.md:21` [UNRESOLVED, LOW] via co-occurrence only
  - | **B — standard input** | EH vertex · TT projector (*"chosen (not derived)"*) · bath content · BD state · scheme · weak coupling · Gaussianity · near-equilibrium · timescale separation | | **A — stan
- `PHYSICS_LEDGER/wall_kr_d5_exec_run8.log:57` [UNRESOLVED, LOW] via co-occurrence only
  -   ctrl-DETECTED   #1 WRONG REGULATOR CONTINUATION: continuing the measure in d while freezing the projector algebra at d = 3 (dropped evanescent terms) CHANGES the MS finite part -- the gate detects a
- `PHYSICS_LEDGER/wall_kr_d5_execution.py:543` [UNRESOLVED, LOW] via co-occurrence only
  -         "#1 WRONG REGULATOR CONTINUATION: continuing the measure in d " control(sp.simplify(fin_bad - SIG_MS) != 0,         "#1 WRONG REGULATOR CONTINUATION: continuing the measure in d "         "whi
- `PHYSICS_LEDGER/wall_kr_d5_execution.py:544` [UNRESOLVED, LOW] via co-occurrence only
  -         "while freezing the projector algebra at d = 3 (dropped " "#1 WRONG REGULATOR CONTINUATION: continuing the measure in d "         "while freezing the projector algebra at d = 3 (dropped "     

### cutoff / separation scale ⟷ response-object definition
- classification: **CONTRADICTORY_SOURCE_STATEMENTS_PRESENT** (9 statement(s))
- distribution: {'RELATED_NOT_IDENTIFIED': 1, 'DISTINCT_CONSTRUCTION': 3, 'UNRESOLVED': 3, 'SAME_CONSTRUCTION': 2}

- `provenance/claims.baseline.json:54` [RELATED_NOT_IDENTIFIED, HIGH] via relational phrase
  -    "tier_note": "BANKED 2026-06-27 (consolidated overseer relay, Brief 1 Outcome 3a -- ANCHOR confirmed, NOT refuted): single-pole is ANCHOR-class, derived-pending -- an independent referee found the 
- `provenance/claims.baseline.json:636` [DISTINCT_CONSTRUCTION, HIGH] via distinction phrase
  -    "statement": "Version II, entry U4 / Frontier 3 (the origin of the constitutive FORM): GIVEN coarse-graining, WHY does the effective description take a RESPONSE / constitutive form (a susceptibilit
- `provenance/claims.baseline.json:639` [UNRESOLVED, LOW] via co-occurrence only
  -    "tier_note": "POSED 2026-07-02 (Version II, the referee's Frontier 3, adjudicated-in). THE CATCH (conceded): the earlier map said TWO frontiers; there are THREE -- deriving coarse-graining does NOT
- `provenance/claims.json:79` [SAME_CONSTRUCTION, HIGH] via identification phrase
  -    "tier_note": "BANKED 2026-06-27 (consolidated overseer relay, Brief 1 Outcome 3a -- ANCHOR confirmed, NOT refuted): single-pole is ANCHOR-class, derived-pending -- an independent referee found the 
- `provenance/claims.json:709` [DISTINCT_CONSTRUCTION, HIGH] via distinction phrase
  -    "statement": "Version II, entry U4 / Frontier 3 (the origin of the constitutive FORM): GIVEN coarse-graining, WHY does the effective description take a RESPONSE / constitutive form (a susceptibilit

### cutoff / separation scale ⟷ slow-variable selection / coarse-graining
- classification: **UNRESOLVED** (19 statement(s))
- distribution: {'UNRESOLVED': 14, 'DISTINCT_CONSTRUCTION': 3, 'SAME_CONSTRUCTION': 2}

- `PHYSICS_LEDGER/WALL_KR_U3_AQFT_RECONCILIATION.md:85` [UNRESOLVED, LOW] via co-occurrence only
  - | Wilsonian coarse-graining | cutoff + blocking rule | the blocking rule *is* the partition | RG flow | what selects the blocking rule | | Effective field theory | field content + a scale | **BY SCALE
- `PHYSICS_LEDGER/WALL_KR_U3_AQFT_RECONCILIATION_RESULT.json:65` [UNRESOLVED, LOW] via co-occurrence only
  -     "Wilsonian coarse-graining": { },     "Wilsonian coarse-graining": {       "primitive": "a cutoff and a blocking rule",
- `PHYSICS_LEDGER/WALL_KR_U3_AQFT_RECONCILIATION_RESULT.json:66` [UNRESOLVED, LOW] via co-occurrence only
  -       "primitive": "a cutoff and a blocking rule", "Wilsonian coarse-graining": {       "primitive": "a cutoff and a blocking rule",       "partition": "the blocking rule IS the partition",
- `PHYSICS_LEDGER/WALL_KR_U3_SCALE_SPLIT_CORRECTION_RESULT.json:19` [UNRESOLVED, LOW] via co-occurrence only
  -   "category_import_hazard": "CATEGORY IMPORT (now verified): importing the foundations-of-QM preferred-factorization problem into an EFT program whose split is a cutoff choice inflates the difficulty 
- `PHYSICS_LEDGER/wall_kr_u3_aqft_reconciliation.py:114` [UNRESOLVED, LOW] via co-occurrence only
  -  "Wilsonian coarse-graining":{"primitive":"a cutoff and a blocking rule", "unexplained":"what selects the scale/split point"},  "Wilsonian coarse-graining":{"primitive":"a cutoff and a blocking rule",

### cutoff / separation scale ⟷ system/bath partition
- classification: **UNRESOLVED** (15 statement(s))
- distribution: {'UNRESOLVED': 8, 'DISTINCT_CONSTRUCTION': 1, 'RELATED_NOT_IDENTIFIED': 1, 'SAME_CONSTRUCTION': 5}

- `PHYSICS_LEDGER/WALL_KR_U3_EFT_BASELINE.md:108` [UNRESOLVED, LOW] via co-occurrence only
  - 1. **GRUT's actual split:** a diagrammatic external/internal partition of a one-loop 1. **GRUT's actual split:** a diagrammatic external/internal partition of a one-loop    influence-functional calcul
- `PHYSICS_LEDGER/WALL_KR_U3_EFT_BASELINE.md:109` [UNRESOLVED, LOW] via co-occurrence only
  -    influence-functional calculation, dimensionally regularized, with **no cutoff parameter**. 1. **GRUT's actual split:** a diagrammatic external/internal partition of a one-loop    influence-function
- `PHYSICS_LEDGER/WALL_KR_U3_EFT_BASELINE_RESULT.json:12` [UNRESOLVED, LOW] via co-occurrence only
  -     "no_cutoff_parameter": true, "category": "NOT B (Wilsonian momentum-shell). The implemented split is the EXTERNAL-LEG vs INTERNAL-LINE partition of a one-loop influence-functional calculation — cl
- `program/CANDIDATE_MINING_02.md:223` [UNRESOLVED, LOW] via co-occurrence only
  - > system/bath partition, the projection P, inner-product choice, the state supplying it, cutoff > construction choices, and the record must not collapse distinct choices — slow-variable selection, > s
- `program/CANDIDATE_MINING_02.md:224` [UNRESOLVED, LOW] via co-occurrence only
  - > choice, gauge/field-redefinition freedom — into one "effective description" decision **unless the > system/bath partition, the projection P, inner-product choice, the state supplying it, cutoff > ch

### gauge / field-redefinition freedom ⟷ inner product / state
- classification: **UNRESOLVED** (4 statement(s))
- distribution: {'UNRESOLVED': 4}

- `program/CANDIDATE_MINING_02.md:275` [UNRESOLVED, LOW] via co-occurrence only
  - **D** inner-product choice · **E** the state supplying the inner product · **F** cutoff/separation **A** slow-variable selection · **B** system/bath partition · **C** the Mori-Zwanzig projection P · *
- `program/CANDIDATE_MINING_02.md:276` [UNRESOLVED, LOW] via co-occurrence only
  - scale · **G** gauge/field-redefinition freedom. **D** inner-product choice · **E** the state supplying the inner product · **F** cutoff/separation scale · **G** gauge/field-redefinition freedom.
- `program/DEPENDENCY_EQUIVALENCE_AUDIT_01_BRIEF.md:49` [UNRESOLVED, LOW] via co-occurrence only
  - | **E** | cutoff / separation-scale choice | | **D** | inner product / the state supplying it | | **E** | cutoff / separation-scale choice | | **F** | gauge / field-redefinition freedom |
- `program/OBJECT_REGISTRY_01.md:21` [UNRESOLVED, LOW] via co-occurrence only
  - | **State / scale data** | D state · E cutoff / separation scale | | **Mathematical reduction** | C projection `P` · D inner product | | **State / scale data** | D state · E cutoff / separation scale 

### gauge / field-redefinition freedom ⟷ projection P
- classification: **UNRESOLVED** (34 statement(s))
- distribution: {'UNRESOLVED': 24, 'DISTINCT_CONSTRUCTION': 3, 'RELATED_NOT_IDENTIFIED': 4, 'SAME_CONSTRUCTION': 3}

- `PHYSICS_LEDGER/WALL_A_A4_RESULT.json:28` [UNRESOLVED, LOW] via co-occurrence only
  -   "verdict": "A4 PASS: the synchronous-gauge computation reproduces the gauge-invariant content of the gauge-unfixed computation. The transformation to synchronous exists; its residual family is zeta^
- `PHYSICS_LEDGER/WALL_A_SESSION_BOUNDARY.md:27` [UNRESOLVED, LOW] via co-occurrence only
  - 1. **A2 Phase-1 closeout** — EH channel projection onto six BR sectors + gauge contraction 1. **A2 Phase-1 closeout** — EH channel projection onto six BR sectors + gauge contraction    discriminator (
- `PHYSICS_LEDGER/WALL_KR_D4_DUAL_GAUGE_RESULT.json:140` [DISTINCT_CONSTRUCTION, HIGH] via distinction phrase
  -    "msg": "CONTROL: B/C. non-gauge mutations (pure-trace internal slot; unsymmetrized image) are NONZERO and DISTINCT from the main result -- omitted-term and projector mutations are distinguishable, 
- `PHYSICS_LEDGER/WALL_KR_D4_KTERM_COMPLETION_RESULT.json:28` [RELATED_NOT_IDENTIFIED, MEDIUM] via relational phrase
  -    "classification_of_the_residual": "category B of the required decomposition -- EXACT ZERO AFTER TT PROJECTION (not 'pure gauge by inspection', not an EOM cancellation, not a new K-term): the projec
- `PHYSICS_LEDGER/WALL_KR_D4_KTERM_COMPLETION_RESULT.json:35` [UNRESOLVED, LOW] via co-occurrence only
  -    "the_D4C_residual": "diagnosed as category B (exact zero after TT projection): the D4-C Part-2 test inserted the gauge image WITHOUT the bath projector the loop actually applies -- a builder-side m

### gauge / field-redefinition freedom ⟷ response-object definition
- classification: **SAME_CONSTRUCTION** (22 statement(s))
- distribution: {'UNRESOLVED': 8, 'SAME_CONSTRUCTION': 12, 'RELATED_NOT_IDENTIFIED': 2}

- `program/gates/Q3_OBSERVABLE_ASSEMBLY_PRECONDITION.md:213` [UNRESOLVED, LOW] via co-occurrence only
  - | R3 | **Feature-of vs function-itself.** Form-factor *feature* = a located property (a zero, a pole, a sign change, a threshold) of a response function, as against the response function itself. | Yes
- `program/gates/Q3_OBSERVABLE_ASSEMBLY_PRECONDITION.md:214` [UNRESOLVED, LOW] via co-occurrence only
  - | R4 | **Gauge/scheme status.** Form-factor-like iff its value is not invariant under the admissible gauge and scheme transformations. | Partly, now — see note | **NOTE (propagated from §6.1):** the s
- `program/gates/Q3_PHYSICAL_SCALE_BRIDGE_GATE.md:247` [UNRESOLVED, LOW] via co-occurrence only
  - Off-shell Green's functions are **not** invariant under field redefinitions. So Off-shell Green's functions are **not** invariant under field redefinitions. So `d(Im G_R)/dlog Λ_R = 9κ⁶ω²/(51200π³) + 
- `provenance/claims.baseline.json:20` [SAME_CONSTRUCTION, HIGH] via identification phrase
  -    "ledger_note": "+3 declared inputs: system/bath split, Gaussian/linear-response truncation, background Lorentzian causal structure. STANCE, not derivation. *** N-SIDED DOUBLE-COUNT CHECK COMPLETED 
- `provenance/claims.baseline.json:180` [UNRESOLVED, LOW] via co-occurrence only
  -    "tier_note": "BANKED 2026-06-27 (rung-9 SPLIT, consolidated overseer relay, Brief 2). The alpha VALUE is UNTOUCHED -- NOT refuted; conditional-theorem (ANCHOR-on-a-free-datum) support, the single a

### gauge / field-redefinition freedom ⟷ slow-variable selection / coarse-graining
- classification: **UNRESOLVED** (1 statement(s))
- distribution: {'UNRESOLVED': 1}

- `program/CANDIDATE_MINING_02.md:275` [UNRESOLVED, LOW] via co-occurrence only
  - **D** inner-product choice · **E** the state supplying the inner product · **F** cutoff/separation **A** slow-variable selection · **B** system/bath partition · **C** the Mori-Zwanzig projection P · *

### gauge / field-redefinition freedom ⟷ system/bath partition
- classification: **UNRESOLVED** (16 statement(s))
- distribution: {'UNRESOLVED': 10, 'SAME_CONSTRUCTION': 6}

- `PHYSICS_LEDGER/ROOT1_KERNEL_ORIGIN.md:169` [UNRESOLVED, LOW] via co-occurrence only
  - declaration sheet fixes D1 (probe kinematics), D2 (gauge), D3 (state + IR), D4 (dual gauge) It is admissible because — verified here, and **stated by no prior document** — the contract declaration she
- `PHYSICS_LEDGER/ROOT1_KERNEL_ORIGIN.md:170` [UNRESOLVED, LOW] via co-occurrence only
  - and D5 (renormalization), and **never declares the system/bath mode partition**: zero declaration sheet fixes D1 (probe kinematics), D2 (gauge), D3 (state + IR), D4 (dual gauge) and D5 (renormalizatio
- `program/CANDIDATE_MINING_02.md:223` [UNRESOLVED, LOW] via co-occurrence only
  - > system/bath partition, the projection P, inner-product choice, the state supplying it, cutoff > construction choices, and the record must not collapse distinct choices — slow-variable selection, > s
- `program/CANDIDATE_MINING_02.md:224` [UNRESOLVED, LOW] via co-occurrence only
  - > choice, gauge/field-redefinition freedom — into one "effective description" decision **unless the > system/bath partition, the projection P, inner-product choice, the state supplying it, cutoff > ch
- `program/CANDIDATE_MINING_02.md:275` [UNRESOLVED, LOW] via co-occurrence only
  - **D** inner-product choice · **E** the state supplying the inner product · **F** cutoff/separation **A** slow-variable selection · **B** system/bath partition · **C** the Mori-Zwanzig projection P · *

### inner product / state ⟷ projection P
- classification: **UNRESOLVED** (5 statement(s))
- distribution: {'UNRESOLVED': 5}

- `program/CANDIDATE_MINING_02.md:274` [UNRESOLVED, LOW] via co-occurrence only
  - **A** slow-variable selection · **B** system/bath partition · **C** the Mori-Zwanzig projection P · **A** slow-variable selection · **B** system/bath partition · **C** the Mori-Zwanzig projection P · 
- `program/CANDIDATE_MINING_02.md:275` [UNRESOLVED, LOW] via co-occurrence only
  - **D** inner-product choice · **E** the state supplying the inner product · **F** cutoff/separation **A** slow-variable selection · **B** system/bath partition · **C** the Mori-Zwanzig projection P · *
- `provenance/claims.baseline.json:225` [UNRESOLVED, LOW] via co-occurrence only
  -    "tier_note": "ATTACKED 2026-06-25 (calc/arrow_origin.py + 7-agent adversarial workflow, primary-source-verified). The decisive cut is EXISTENCE vs DIRECTION. The in-in machinery INTRINSICALLY suppl
- `provenance/claims.json:272` [UNRESOLVED, LOW] via co-occurrence only
  -    "tier_note": "ATTACKED 2026-06-25 (calc/arrow_origin.py + 7-agent adversarial workflow, primary-source-verified). The decisive cut is EXISTENCE vs DIRECTION. The in-in machinery INTRINSICALLY suppl
- `provenance/claims.json.pre-discharge.bak:272` [UNRESOLVED, LOW] via co-occurrence only
  -    "tier_note": "ATTACKED 2026-06-25 (calc/arrow_origin.py + 7-agent adversarial workflow, primary-source-verified). The decisive cut is EXISTENCE vs DIRECTION. The in-in machinery INTRINSICALLY suppl

### inner product / state ⟷ response-object definition
- classification: **UNRESOLVED** (10 statement(s))
- distribution: {'UNRESOLVED': 5, 'RELATED_NOT_IDENTIFIED': 3, 'SAME_CONSTRUCTION': 2}

- `calc/mz_inheritance.py:18` [UNRESOLVED, LOW] via co-occurrence only
  -       AT ALL. Mori-Zwanzig projection for a quantum system conventionally uses the KUBO-MORI (2) BUT THE SYMMETRISED ROUTE IS NOT THE ONLY ONE, AND THE OTHER STANDARD CHOICE HAS NO LADDER       AT ALL
- `calc/mz_inheritance.py:19` [UNRESOLVED, LOW] via co-occurrence only
  -       (canonical) inner product, and the Kubo correlation function carries AT ALL. Mori-Zwanzig projection for a quantum system conventionally uses the KUBO-MORI       (canonical) inner product, and t
- `program/CANDIDATE_MINING_02.md:260` [UNRESOLVED, LOW] via co-occurrence only
  - **Kubo-Mori** and the **symmetrised** inner products. The second half is booked as missing: it could denote answer this question **OPPOSITELY**"* — the same retained variable admits the **Kubo-Mori** 
- `program/CANDIDATE_MINING_02.md:261` [UNRESOLVED, LOW] via co-occurrence only
  - *"the state supplying the inner product (unpriced anywhere)."* **Kubo-Mori** and the **symmetrised** inner products. The second half is booked as missing: *"the state supplying the inner product (unpr
- `program/OBJECT_REGISTRY_01.md:77` [UNRESOLVED, LOW] via co-occurrence only
  -   *"requires `P` orthogonal w.r.t. a **state-induced Kubo–Mori inner product** — so producing GRUT's - **State dependence:** explicit. `RAI_GRUT_RESURRECTION.md:108-110` — producing the registered obj

### inner product / state ⟷ slow-variable selection / coarse-graining
- classification: **UNRESOLVED** (9 statement(s))
- distribution: {'UNRESOLVED': 7, 'SAME_CONSTRUCTION': 2}

- `calc/mz_inheritance.py:18` [UNRESOLVED, LOW] via co-occurrence only
  -       AT ALL. Mori-Zwanzig projection for a quantum system conventionally uses the KUBO-MORI (2) BUT THE SYMMETRISED ROUTE IS NOT THE ONLY ONE, AND THE OTHER STANDARD CHOICE HAS NO LADDER       AT ALL
- `calc/mz_inheritance.py:19` [UNRESOLVED, LOW] via co-occurrence only
  -       (canonical) inner product, and the Kubo correlation function carries AT ALL. Mori-Zwanzig projection for a quantum system conventionally uses the KUBO-MORI       (canonical) inner product, and t
- `calc/mz_inheritance.py:530` [UNRESOLVED, LOW] via co-occurrence only
  -     print("       Mori-Zwanzig inner product there is no ladder to inherit, and the friction") print("     WHAT IS WEAKENED, and it must be said in this direction: on the CONVENTIONAL")     print("   
- `program/CANDIDATE_MINING_02.md:274` [UNRESOLVED, LOW] via co-occurrence only
  - **A** slow-variable selection · **B** system/bath partition · **C** the Mori-Zwanzig projection P · **A** slow-variable selection · **B** system/bath partition · **C** the Mori-Zwanzig projection P · 
- `program/CANDIDATE_MINING_02.md:275` [UNRESOLVED, LOW] via co-occurrence only
  - **D** inner-product choice · **E** the state supplying the inner product · **F** cutoff/separation **A** slow-variable selection · **B** system/bath partition · **C** the Mori-Zwanzig projection P · *

### inner product / state ⟷ system/bath partition
- classification: **UNRESOLVED** (6 statement(s))
- distribution: {'UNRESOLVED': 4, 'SAME_CONSTRUCTION': 2}

- `program/CANDIDATE_MINING_02.md:274` [UNRESOLVED, LOW] via co-occurrence only
  - **A** slow-variable selection · **B** system/bath partition · **C** the Mori-Zwanzig projection P · **A** slow-variable selection · **B** system/bath partition · **C** the Mori-Zwanzig projection P · 
- `program/CANDIDATE_MINING_02.md:275` [UNRESOLVED, LOW] via co-occurrence only
  - **D** inner-product choice · **E** the state supplying the inner product · **F** cutoff/separation **A** slow-variable selection · **B** system/bath partition · **C** the Mori-Zwanzig projection P · *
- `program/OBJECT_REGISTRY_01.md:19` [UNRESOLVED, LOW] via co-occurrence only
  - | **Physical partitioning** | A system/bath split · B slow-variable selection | |---|---| | **Physical partitioning** | A system/bath split · B slow-variable selection | | **Mathematical reduction** |
- `program/OBJECT_REGISTRY_01.md:20` [UNRESOLVED, LOW] via co-occurrence only
  - | **Mathematical reduction** | C projection `P` · D inner product | | **Physical partitioning** | A system/bath split · B slow-variable selection | | **Mathematical reduction** | C projection `P` · D 
- `provenance/claims.json:79` [SAME_CONSTRUCTION, HIGH] via identification phrase
  -    "tier_note": "BANKED 2026-06-27 (consolidated overseer relay, Brief 1 Outcome 3a -- ANCHOR confirmed, NOT refuted): single-pole is ANCHOR-class, derived-pending -- an independent referee found the 

### projection P ⟷ response-object definition
- classification: **UNRESOLVED** (13 statement(s))
- distribution: {'UNRESOLVED': 7, 'SAME_CONSTRUCTION': 6}

- `calc/RESULTS_anomaly_c0_map.md:47` [UNRESOLVED, LOW] via co-occurrence only
  - 2. **To `eft_operator_basis` finding (iv).** Its second clause, "the anomaly leaves TT unaffected", is **false at two-point level** (∫C² is pure P2). The **one-point clause stands** (⟨T^μ_μ⟩ is spin-0
- `provenance/claims.baseline.json:180` [UNRESOLVED, LOW] via co-occurrence only
  -    "tier_note": "BANKED 2026-06-27 (rung-9 SPLIT, consolidated overseer relay, Brief 2). The alpha VALUE is UNTOUCHED -- NOT refuted; conditional-theorem (ANCHOR-on-a-free-datum) support, the single a
- `provenance/claims.baseline.json:201` [SAME_CONSTRUCTION, HIGH] via identification phrase
  -    "statement": "The c_0 normalization (alpha-bridge): c_0 = alpha is an ADOPTED phenomenological DC normalization of the TT response kernel (K^R = alpha*chi*P^TT) -- the conformal anomaly does NOT de
- `provenance/claims.baseline.json:269` [SAME_CONSTRUCTION, HIGH] via identification phrase
  -    "boundary_condition": "INTERROGATION RESULT 2026-08-02 (the forced-vs-chosen question ANSWERED; overseer-run five-angle interrogation, each angle adversarially verified against the five pre-registe
- `provenance/claims.baseline.json:275` [UNRESOLVED, LOW] via co-occurrence only
  -    "overturning_computation": "The settling check that would REMOVE this assumption: derive the response projector FROM the in-in action (no inserted P^TT). If it comes out non-pure-TT (e.g. carries t

### projection P ⟷ slow-variable selection / coarse-graining
- classification: **UNRESOLVED** (31 statement(s))
- distribution: {'UNRESOLVED': 29, 'SAME_CONSTRUCTION': 1, 'RELATED_NOT_IDENTIFIED': 1}

- `PHYSICS_LEDGER/WALL_KR_U3_AQFT_RECONCILIATION.md:82` [UNRESOLVED, LOW] via co-occurrence only
  - | Mori-Zwanzig | a projector `P` | **CHOSEN** (`P` *is* the partition) | generalized Langevin | what selects `P` | | Zurek / decoherence | `H_S ⊗ H_B` + interaction | **ASSUMED** | partial trace | why
- `PHYSICS_LEDGER/WALL_KR_U3_AQFT_RECONCILIATION.md:119` [UNRESOLVED, LOW] via co-occurrence only
  - moves: assuming `H_S ⊗ H_B`; assuming a projector `P`; assuming a system/environment and an "emergent" answer that smuggles in a projector — and it rejects all five disallowed moves: assuming `H_S ⊗ H
- `PHYSICS_LEDGER/WALL_KR_U3_AQFT_RECONCILIATION.md:120` [UNRESOLVED, LOW] via co-occurrence only
  - decomposition; renaming coarse-graining; deriving decoherence after assuming the split. moves: assuming `H_S ⊗ H_B`; assuming a projector `P`; assuming a system/environment decomposition; renaming coa
- `PHYSICS_LEDGER/WALL_KR_U3_AQFT_RECONCILIATION_RESULT.json:47` [UNRESOLVED, LOW] via co-occurrence only
  -     "Mori-Zwanzig": { },     "Mori-Zwanzig": {       "primitive": "a projector P onto 'relevant' variables",
- `PHYSICS_LEDGER/WALL_KR_U3_AQFT_RECONCILIATION_RESULT.json:48` [UNRESOLVED, LOW] via co-occurrence only
  -       "primitive": "a projector P onto 'relevant' variables", "Mori-Zwanzig": {       "primitive": "a projector P onto 'relevant' variables",       "partition": "CHOSEN (P IS the partition)",

### projection P ⟷ system/bath partition
- classification: **UNRESOLVED** (4 statement(s))
- distribution: {'UNRESOLVED': 4}

- `program/CANDIDATE_MINING_02.md:223` [UNRESOLVED, LOW] via co-occurrence only
  - > system/bath partition, the projection P, inner-product choice, the state supplying it, cutoff > construction choices, and the record must not collapse distinct choices — slow-variable selection, > s
- `program/CANDIDATE_MINING_02.md:224` [UNRESOLVED, LOW] via co-occurrence only
  - > choice, gauge/field-redefinition freedom — into one "effective description" decision **unless the > system/bath partition, the projection P, inner-product choice, the state supplying it, cutoff > ch
- `program/CANDIDATE_MINING_02.md:274` [UNRESOLVED, LOW] via co-occurrence only
  - **A** slow-variable selection · **B** system/bath partition · **C** the Mori-Zwanzig projection P · **A** slow-variable selection · **B** system/bath partition · **C** the Mori-Zwanzig projection P · 
- `program/CANDIDATE_MINING_02.md:275` [UNRESOLVED, LOW] via co-occurrence only
  - **D** inner-product choice · **E** the state supplying the inner product · **F** cutoff/separation **A** slow-variable selection · **B** system/bath partition · **C** the Mori-Zwanzig projection P · *

### response-object definition ⟷ slow-variable selection / coarse-graining
- classification: **UNRESOLVED** (29 statement(s))
- distribution: {'UNRESOLVED': 24, 'DISTINCT_CONSTRUCTION': 3, 'SAME_CONSTRUCTION': 2}

- `PHYSICS_LEDGER/WALL_KR_U3_PROGRAM.md:67` [UNRESOLVED, LOW] via co-occurrence only
  - equivalence class of response functionals χ(ω,k) that produce identical observable transport `u6` is a **registered branch** of the u4 classification tree, whose central object is *"the equivalence cl
- `PHYSICS_LEDGER/WALL_KR_U3_PROGRAM.md:68` [UNRESOLVED, LOW] via co-occurrence only
  - under admissible coarse-grainings"*. `u6` **labels** the classes `u5` classifies. equivalence class of response functionals χ(ω,k) that produce identical observable transport under admissible coarse-g
- `PHYSICS_LEDGER/WALL_KR_U4_DISTINCTIVENESS.md:26` [UNRESOLVED, LOW] via co-occurrence only
  - identical observable transport under admissible coarse-grainings.** Linearity is built into U4's minimal object is pinned by its own tier note: **the equivalence class of χ(ω,k) producing identical ob
- `PHYSICS_LEDGER/WALL_KR_U4_DISTINCTIVENESS.md:27` [UNRESOLVED, LOW] via co-occurrence only
  - that definition — a susceptibility *is* a linear-response object. identical observable transport under admissible coarse-grainings.** Linearity is built into that definition — a susceptibility *is* a 
- `PHYSICS_LEDGER/wall_kr_u4_distinctiveness_audit.py:34` [UNRESOLVED, LOW] via co-occurrence only
  -       "GIVEN coarse-graining,"), "u4 statement recovered; opens 'GIVEN coarse-graining'") check(ST.startswith("Version II, entry U4 / Frontier 3 (the origin of the constitutive FORM): "       "GIVEN c

### response-object definition ⟷ system/bath partition
- classification: **SAME_CONSTRUCTION** (6 statement(s))
- distribution: {'SAME_CONSTRUCTION': 5, 'RELATED_NOT_IDENTIFIED': 1}

- `provenance/claims.baseline.json:20` [SAME_CONSTRUCTION, HIGH] via identification phrase
  -    "ledger_note": "+3 declared inputs: system/bath split, Gaussian/linear-response truncation, background Lorentzian causal structure. STANCE, not derivation. *** N-SIDED DOUBLE-COUNT CHECK COMPLETED 
- `provenance/claims.baseline.json:54` [RELATED_NOT_IDENTIFIED, HIGH] via relational phrase
  -    "tier_note": "BANKED 2026-06-27 (consolidated overseer relay, Brief 1 Outcome 3a -- ANCHOR confirmed, NOT refuted): single-pole is ANCHOR-class, derived-pending -- an independent referee found the 
- `provenance/claims.json:22` [SAME_CONSTRUCTION, HIGH] via identification phrase
  -    "ledger_note": "+3 declared inputs: system/bath split, Gaussian/linear-response truncation, background Lorentzian causal structure. STANCE, not derivation. *** N-SIDED DOUBLE-COUNT CHECK COMPLETED 
- `provenance/claims.json:79` [SAME_CONSTRUCTION, HIGH] via identification phrase
  -    "tier_note": "BANKED 2026-06-27 (consolidated overseer relay, Brief 1 Outcome 3a -- ANCHOR confirmed, NOT refuted): single-pole is ANCHOR-class, derived-pending -- an independent referee found the 
- `provenance/claims.json.pre-discharge.bak:22` [SAME_CONSTRUCTION, HIGH] via identification phrase
  -    "ledger_note": "+3 declared inputs: system/bath split, Gaussian/linear-response truncation, background Lorentzian causal structure. STANCE, not derivation. *** N-SIDED DOUBLE-COUNT CHECK COMPLETED 

### slow-variable selection / coarse-graining ⟷ system/bath partition
- classification: **UNRESOLVED** (24 statement(s))
- distribution: {'UNRESOLVED': 20, 'DISTINCT_CONSTRUCTION': 2, 'SAME_CONSTRUCTION': 2}

- `PHYSICS_LEDGER/WALL_KR_FOUNDATIONAL_LADDER_RESULT.json:45` [UNRESOLVED, LOW] via co-occurrence only
  -     "1. u3_split_origin — why a system/bath split at all (deepest; presupposes nothing registered)", "foundational_research_order": [     "1. u3_split_origin — why a system/bath split at all (deepest;
- `PHYSICS_LEDGER/WALL_KR_FOUNDATIONAL_LADDER_RESULT.json:46` [UNRESOLVED, LOW] via co-occurrence only
  -     "2. u4_constitutive_origin — why coarse-graining yields response form (needs u3's OBJECT as given, NOT u3's answer; therefore pursuable in parallel with or before u3 is resolved)", "1. u3_split_or
- `PHYSICS_LEDGER/WALL_KR_INDEPENDENCE_AUDIT_RESULT.json:53` [UNRESOLVED, LOW] via co-occurrence only
  -     "u3_split_origin — why a system/bath split at all (sits BELOW rung1; cannot inherit lineage)", "legitimate_next_tasks_zero_owner_selections": [     "u3_split_origin — why a system/bath split at al
- `PHYSICS_LEDGER/WALL_KR_INDEPENDENCE_AUDIT_RESULT.json:54` [UNRESOLVED, LOW] via co-occurrence only
  -     "u4_constitutive_origin — why coarse-graining yields constitutive/response structure", "u3_split_origin — why a system/bath split at all (sits BELOW rung1; cannot inherit lineage)",     "u4_consti
- `PHYSICS_LEDGER/WALL_KR_U3_SPECIFICATION.md:38` [UNRESOLVED, LOW] via co-occurrence only
  - **Ambiguity on its face:** the statement writes *"system/bath split / coarse-graining"* — the **Ambiguity on its face:** the statement writes *"system/bath split / coarse-graining"* — the same slash-a

## Pairs with no usable evidence

- system/bath partition ⟷ slow-variable selection / coarse-graining
- system/bath partition ⟷ projection P
- system/bath partition ⟷ inner product / state
- system/bath partition ⟷ cutoff / separation scale
- system/bath partition ⟷ gauge / field-redefinition freedom
- system/bath partition ⟷ response-object definition
- slow-variable selection / coarse-graining ⟷ projection P
- slow-variable selection / coarse-graining ⟷ inner product / state
- slow-variable selection / coarse-graining ⟷ cutoff / separation scale
- slow-variable selection / coarse-graining ⟷ gauge / field-redefinition freedom
- slow-variable selection / coarse-graining ⟷ response-object definition
- projection P ⟷ inner product / state
- projection P ⟷ cutoff / separation scale
- projection P ⟷ gauge / field-redefinition freedom
- inner product / state ⟷ cutoff / separation scale
- inner product / state ⟷ gauge / field-redefinition freedom