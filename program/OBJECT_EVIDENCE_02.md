# OBJECT_EVIDENCE_02 — lossless evidence graph (lab artifact)

Commit: `0cf4a9a76faab2e4ed1fb819938ef1dbd4aa9121`

> LEVEL 1: unique statements (file:line). LEVEL 2: many-to-many object associations.

## Counts
- original evidence records: 2370
- unique source statements: 2231
- total object associations: 2167
- association kinds: {'TERM_ONLY': 1287, 'DIRECT_ASSOCIATION': 774, 'CONTEXTUAL_ASSOCIATION': 106}
- statements with 0 objects: 212
- statements with 1 object: 1889
- statements with 2+ objects: 130
- recovered cross-object associations: 130
- duplicate source statements: 0
- gen-1 records with no traceable successor: 0
- information lost: 309

## Statements with 2+ object associations (first 40)

### PHYSICS_LEDGER/ROOT1_KERNEL_ORIGIN.md:169
- gen-1 records: [86]
- gauge_field_redefinition [DIRECT_ASSOCIATION] via ['gauge']
- system_bath_partition [CONTEXTUAL_ASSOCIATION] via []

### PHYSICS_LEDGER/ROOT1_KERNEL_ORIGIN.md:170
- gen-1 records: [87]
- gauge_field_redefinition [CONTEXTUAL_ASSOCIATION] via []
- system_bath_partition [DIRECT_ASSOCIATION] via ['system/bath']

### PHYSICS_LEDGER/WALL_A_SESSION_BOUNDARY.md:27
- gen-1 records: [181, 182]
- gauge_field_redefinition [TERM_ONLY] via ['gauge']
- projection_P [TERM_ONLY] via ['projection onto']

### PHYSICS_LEDGER/WALL_KR_D4_DUAL_GAUGE_RESULT.json:140
- gen-1 records: [278, 279]
- gauge_field_redefinition [TERM_ONLY] via ['gauge']
- projection_P [TERM_ONLY] via ['projector']

### PHYSICS_LEDGER/WALL_KR_D4_KTERM_COMPLETION_RESULT.json:36
- gen-1 records: [302]
- gauge_field_redefinition [TERM_ONLY] via ['gauge']
- projection_P [CONTEXTUAL_ASSOCIATION] via []

### PHYSICS_LEDGER/WALL_KR_D4_KTERM_COMPLETION_RESULT.json:216
- gen-1 records: [315]
- gauge_field_redefinition [TERM_ONLY] via ['gauge']
- projection_P [CONTEXTUAL_ASSOCIATION] via []

### PHYSICS_LEDGER/WALL_KR_D5_EXECUTION_RESULT.json:191
- gen-1 records: [344, 345]
- cutoff_separation_scale [DIRECT_ASSOCIATION] via ['REGULATOR']
- projection_P [DIRECT_ASSOCIATION] via ['projector']

### PHYSICS_LEDGER/WALL_KR_FOUNDATIONAL_LADDER_RESULT.json:45
- gen-1 records: [377]
- slow_variable_coarse_graining [CONTEXTUAL_ASSOCIATION] via []
- system_bath_partition [TERM_ONLY] via ['system/bath']

### PHYSICS_LEDGER/WALL_KR_FOUNDATIONAL_LADDER_RESULT.json:46
- gen-1 records: [378]
- slow_variable_coarse_graining [TERM_ONLY] via ['coarse-grain']
- system_bath_partition [CONTEXTUAL_ASSOCIATION] via []

### PHYSICS_LEDGER/WALL_KR_INDEPENDENCE_AUDIT_RESULT.json:53
- gen-1 records: [447]
- slow_variable_coarse_graining [CONTEXTUAL_ASSOCIATION] via []
- system_bath_partition [TERM_ONLY] via ['system/bath']

### PHYSICS_LEDGER/WALL_KR_INDEPENDENCE_AUDIT_RESULT.json:54
- gen-1 records: [448]
- slow_variable_coarse_graining [TERM_ONLY] via ['coarse-grain']
- system_bath_partition [CONTEXTUAL_ASSOCIATION] via []

### PHYSICS_LEDGER/WALL_KR_U3_AQFT_RECONCILIATION.md:82
- gen-1 records: [507, 508]
- projection_P [DIRECT_ASSOCIATION] via ['projector']
- slow_variable_coarse_graining [DIRECT_ASSOCIATION] via ['Mori-Zwanzig']

### PHYSICS_LEDGER/WALL_KR_U3_AQFT_RECONCILIATION.md:85
- gen-1 records: [509, 510]
- cutoff_separation_scale [TERM_ONLY] via ['cutoff']
- slow_variable_coarse_graining [TERM_ONLY] via ['coarse-grain']

### PHYSICS_LEDGER/WALL_KR_U3_AQFT_RECONCILIATION.md:119
- gen-1 records: [512]
- projection_P [TERM_ONLY] via ['projector']
- slow_variable_coarse_graining [CONTEXTUAL_ASSOCIATION] via []

### PHYSICS_LEDGER/WALL_KR_U3_AQFT_RECONCILIATION.md:120
- gen-1 records: [513]
- projection_P [CONTEXTUAL_ASSOCIATION] via []
- slow_variable_coarse_graining [TERM_ONLY] via ['coarse-grain']

### PHYSICS_LEDGER/WALL_KR_U3_AQFT_RECONCILIATION_RESULT.json:47
- gen-1 records: [516]
- projection_P [CONTEXTUAL_ASSOCIATION] via []
- slow_variable_coarse_graining [TERM_ONLY] via ['Mori-Zwanzig']

### PHYSICS_LEDGER/WALL_KR_U3_AQFT_RECONCILIATION_RESULT.json:48
- gen-1 records: [517]
- projection_P [TERM_ONLY] via ['projector']
- slow_variable_coarse_graining [CONTEXTUAL_ASSOCIATION] via []

### PHYSICS_LEDGER/WALL_KR_U3_AQFT_RECONCILIATION_RESULT.json:65
- gen-1 records: [518]
- cutoff_separation_scale [CONTEXTUAL_ASSOCIATION] via []
- slow_variable_coarse_graining [TERM_ONLY] via ['coarse-grain']

### PHYSICS_LEDGER/WALL_KR_U3_AQFT_RECONCILIATION_RESULT.json:66
- gen-1 records: [519]
- cutoff_separation_scale [TERM_ONLY] via ['cutoff']
- slow_variable_coarse_graining [CONTEXTUAL_ASSOCIATION] via []

### PHYSICS_LEDGER/WALL_KR_U3_EFT_BASELINE.md:57
- gen-1 records: [528]
- projection_P [CONTEXTUAL_ASSOCIATION] via []
- slow_variable_coarse_graining [TERM_ONLY] via ['Mori-Zwanzig']

### PHYSICS_LEDGER/WALL_KR_U3_EFT_BASELINE.md:58
- gen-1 records: [529]
- projection_P [TERM_ONLY] via ['projector']
- slow_variable_coarse_graining [CONTEXTUAL_ASSOCIATION] via []

### PHYSICS_LEDGER/WALL_KR_U3_EFT_BASELINE.md:108
- gen-1 records: [532]
- cutoff_separation_scale [CONTEXTUAL_ASSOCIATION] via []
- system_bath_partition [DIRECT_ASSOCIATION] via ['partition of']

### PHYSICS_LEDGER/WALL_KR_U3_EFT_BASELINE.md:109
- gen-1 records: [533]
- cutoff_separation_scale [DIRECT_ASSOCIATION] via ['cutoff']
- system_bath_partition [CONTEXTUAL_ASSOCIATION] via []

### PHYSICS_LEDGER/WALL_KR_U3_EFT_BASELINE_RESULT.json:27
- gen-1 records: [539]
- projection_P [TERM_ONLY] via ['projector']
- slow_variable_coarse_graining [CONTEXTUAL_ASSOCIATION] via []

### PHYSICS_LEDGER/WALL_KR_U3_PROGRAM.md:47
- gen-1 records: [543, 544]
- projection_P [TERM_ONLY] via ['projector']
- slow_variable_coarse_graining [TERM_ONLY] via ['Mori-Zwanzig']

### PHYSICS_LEDGER/WALL_KR_U3_PROGRAM.md:67
- gen-1 records: [547]
- response_object [DIRECT_ASSOCIATION] via ['response function']
- slow_variable_coarse_graining [CONTEXTUAL_ASSOCIATION] via []

### PHYSICS_LEDGER/WALL_KR_U3_PROGRAM.md:68
- gen-1 records: [548]
- response_object [CONTEXTUAL_ASSOCIATION] via []
- slow_variable_coarse_graining [DIRECT_ASSOCIATION] via ['coarse-grain']

### PHYSICS_LEDGER/WALL_KR_U3_SPECIFICATION.md:38
- gen-1 records: [563, 564]
- slow_variable_coarse_graining [DIRECT_ASSOCIATION] via ['coarse-grain']
- system_bath_partition [DIRECT_ASSOCIATION] via ['system/bath']

### PHYSICS_LEDGER/WALL_KR_U3_SPECIFICATION.md:75
- gen-1 records: [568]
- projection_P [CONTEXTUAL_ASSOCIATION] via []
- slow_variable_coarse_graining [DIRECT_ASSOCIATION] via ['coarse-grain']

### PHYSICS_LEDGER/WALL_KR_U3_SPECIFICATION.md:76
- gen-1 records: [569, 570]
- projection_P [DIRECT_ASSOCIATION] via ['projector']
- slow_variable_coarse_graining [DIRECT_ASSOCIATION] via ['Mori-Zwanzig']

### PHYSICS_LEDGER/WALL_KR_U3_SPECIFICATION.md:102
- gen-1 records: [572, 573]
- projection_P [TERM_ONLY] via ['projector']
- slow_variable_coarse_graining [TERM_ONLY] via ['Mori-Zwanzig']

### PHYSICS_LEDGER/WALL_KR_U3_SPECIFICATION_RESULT.json:36
- gen-1 records: [577, 578]
- slow_variable_coarse_graining [TERM_ONLY] via ['coarse-grain']
- system_bath_partition [TERM_ONLY] via ['system/bath']

### PHYSICS_LEDGER/WALL_KR_U3_SPECIFICATION_RESULT.json:61
- gen-1 records: [581, 582]
- projection_P [TERM_ONLY] via ['projector']
- slow_variable_coarse_graining [TERM_ONLY] via ['Mori-Zwanzig']

### PHYSICS_LEDGER/WALL_KR_U4_DISTINCTIVENESS.md:26
- gen-1 records: [589]
- response_object [CONTEXTUAL_ASSOCIATION] via []
- slow_variable_coarse_graining [DIRECT_ASSOCIATION] via ['coarse-grain']

### PHYSICS_LEDGER/WALL_KR_U4_DISTINCTIVENESS.md:27
- gen-1 records: [590]
- response_object [DIRECT_ASSOCIATION] via ['susceptibility']
- slow_variable_coarse_graining [CONTEXTUAL_ASSOCIATION] via []

### PHYSICS_LEDGER/WALL_KR_U4_DISTINCTIVENESS.md:44
- gen-1 records: [591, 592]
- projection_P [DIRECT_ASSOCIATION] via ['projector']
- slow_variable_coarse_graining [DIRECT_ASSOCIATION] via ['Mori-Zwanzig']

### PHYSICS_LEDGER/WALL_KR_U4_DISTINCTIVENESS_RESULT.json:38
- gen-1 records: [601]
- projection_P [CONTEXTUAL_ASSOCIATION] via []
- slow_variable_coarse_graining [DIRECT_ASSOCIATION] via ['Mori-Zwanzig']

### PHYSICS_LEDGER/WALL_KR_U4_DISTINCTIVENESS_RESULT.json:39
- gen-1 records: [602]
- projection_P [DIRECT_ASSOCIATION] via ['projector']
- slow_variable_coarse_graining [CONTEXTUAL_ASSOCIATION] via []

### PHYSICS_LEDGER/kterm_run1.log:65
- gen-1 records: [724]
- gauge_field_redefinition [TERM_ONLY] via ['gauge']
- projection_P [CONTEXTUAL_ASSOCIATION] via []

### PHYSICS_LEDGER/wall_a_a4_dual_gauge.py:299
- gen-1 records: [823]
- gauge_field_redefinition [DIRECT_ASSOCIATION] via ['gauge']
- projection_P [CONTEXTUAL_ASSOCIATION] via []
