# GRUT-RAI v3 Hard-Theory Benchmark

## Native S4 3-loop CTP Solver Ladder

**Goal:** Build a native, auditable S4 CTP solver. Stage 1 is verified scaffolding only.

### Stage 1 — Verified scaffolding
- Curved-space conventions and bookkeeping.
- Diagram generation metadata (no evaluation).
- Scheme and regulator tracking.
- Ward-identity placeholders (no pass/fail claims).

### Stage 2 — Benchmark reproduction
- Reproduce flat-space 1-loop/2-loop/3-loop bookkeeping results.
- Reproduce known curved-space trace anomaly coefficients (a, c, b) for scalar, Weyl fermion, gauge boson.

**Stage 2 — Benchmark Reproduction (current scope)**
- Heat-kernel / Seeley-DeWitt coefficients for scalar a_0, a_1, a_2.
- Curved-space trace anomaly coefficients for scalar, Weyl fermion, gauge boson.
- S4 substitutions: W2 = 0 and Euler density survives.
- Flat-space 1-loop bubble divergence structure (1/epsilon + log term).

Sources:
- Duff 1994 (trace anomaly coefficients)
- Birrell-Davies 1982 (heat-kernel basics)

Statement:
GRUT-RAI Stage 2 validates the curved-space machinery against known results. No new physics is claimed at this stage.

### Stage 3 — S4 3-loop partials
- Compute controlled diagram subsets or asymptotic expansions.
- Label outputs as Speculative / Internal until verified.

**Stage 3 — Controlled S4 3-loop partials**
- Builds symbolic topology records for representative 3-loop diagrams.
- Produces controlled partials via large-radius, small-curvature, heat-kernel truncation, and flat-limit projections.
- Runs structural ward audits and scheme/regulator checks without numeric promotion.

What Stage 3 does NOT do:
- It does not compute the full native 3-loop S4 CTP effective action.
- It does not evaluate full tensor contractions or renormalization matching.

Topology list (representative set):
- sunset/basketball
- figure-eight-with-tail
- triple-bubble
- ghost-loop-corrected
- matter-loop-insertion
- graviton-self-energy-insertion

Partial expansion strategy:
- Large-radius expansion (truncated)
- Small-curvature expansion (truncated)
- Heat-kernel truncation
- Flat-limit projection

Audit gates:
- Transversality (structural placeholder)
- CTP unitarity (structural placeholder)
- Trace anomaly consistency (structural placeholder)
- Scheme consistency (metadata present)
- Flat-limit consistency (placeholder)

Promotion requirements:
- explicit S4 propagators
- full tensor contraction
- renormalization/scheme matching
- Ward identity verification
- independent replication

**Explicit warning:**
Stage 3 produces speculative/internal partials only. It does not compute the full native 3-loop S4 CTP effective action and does not promote any GRUT physics claim.

### Stage 4 — Full native S4 3-loop evaluation
- Promote results to Computed only after:
  - Scheme consistency checks
  - Ward identities validated
  - Independent replication
  - Numerical/symbolic cross-checks

### Stage 3B — Explicit S4 propagator ingredients
- Scalar spectral basis (eigenvalues + degeneracies).
- Conformal scalar Green-function truncation (spectral sum).
- Zero-mode warning retained for minimally coupled massless scalar.
- Tensor harmonics remain structural placeholders (no evaluated contractions).
- Contraction engine scaffold (no 3-loop integrals evaluated).

Statement:
Stage 3B benchmarks ingredients required for a future native S4 3-loop computation. It does not compute the full 3-loop CTP effective action and promotes no GRUT physics claim.

### Stage 3C — Tensor harmonic and Ward-identity structural audit
- Tensor modes matter because graviton loops require TT sector control on S4.
- Scalar spectrum remains benchmarked; vector/tensor spectra are structural placeholders.
- TT projector is recorded structurally (no explicit kernel).
- Graviton decomposition tracks TT, vector, scalar-longitudinal, and trace sectors.
- Ward/CTP branch checks are structural only and refuse claim promotion.

What remains before 3-loop computation:
- explicit TT spectrum benchmark
- explicit TT projector kernel
- full graviton/ghost propagator on S4
- renormalized tensor contraction engine
- independent audit

Statement:
Stage 3C tightens the graviton/tensor infrastructure but does not evaluate the full S4 graviton propagator, does not compute any 3-loop integral, and promotes no GRUT physics claim.

### Stage 3D — Renormalization and scheme-consistency audit
- Renormalization must be explicit before any native 3-loop claim can be trusted.
- Counterterms registered: Lambda, R, R^2, Ricci^2, Riemann^2, E4, W^2, box R.
- Divergences tracked with regulator/scheme metadata.
- Scheme invariants vs scheme-fragile quantities classified (a, c, b, C_Cosmo, C_Final, R_ratio).
- C_Cosmo is local/scheme-fragile; C_Final treated as scheme-protected candidate.
- R_ratio meaningful only with scheme-aligned numerator/denominator.

Statement:
Stage 3D registers and audits renormalization structure. It does not compute renormalized 3-loop coefficients, does not seal the R-route, and promotes no GRUT physics claim.

### Stage 3E — Independent cross-check harness
- Multi-route validation across heat-kernel, spectral sums, flat-limit, and Ward-identity structure.
- Consistency metrics compare symbolic forms, limit behavior, and scheme metadata.
- Partial comparisons are expected to be inconclusive until full evaluations exist.

Statement:
Stage 3E introduces cross-representation consistency checks. It does not compute full loop integrals and promotes no GRUT physics claim.

### Stage 3F — External audit package and reproducibility bundle
- Audit manifest summarizes stage status, tests, and limitations for reviewers.
- Capability matrix enumerates what is available vs not available.
- Refusal report documents out-of-scope requests and required prerequisites.
- Reproducibility bundle lists test commands and known limitations.

Statement:
Stage 3F makes the hard-theory ladder externally auditable. It does not compute the full native 3-loop S4 CTP effective action and promotes no GRUT physics claim.

### Stage 4A — Controlled benchmark integral evaluation
- Toy integrals: scalar bubble, scalar tadpole, dim-reg pole and log structure.
- Curved-space checks: low-order heat-kernel trace and low-l S4 spectral truncation.
- Evaluation engine compares symbolic structure and divergence behavior.
- Limitations: no multi-loop curved-space evaluation, no full 3-loop CTP action.

Statement:
Stage 4A validates the evaluation engine against known results. It does not compute the full 3-loop S4 CTP effective action and promotes no GRUT physics claim.

### Stage 4B — Controlled 3-loop subset evaluation
- Evaluated subsets: scalar triple-bubble, figure-eight x bubble, nested double loop + bubble, sunset extensions (scalar only).
- Factorization strategy uses products of lower-loop integrals where allowed.
- Divergence patterns checked against expected structure.
- Limitations: no full tensor contractions, no curved S4 evaluation.

Statement:
Stage 4B evaluates controlled 3-loop subsets in flat-space/scalar sectors. It does not compute the full S4 3-loop CTP effective action and promotes no GRUT physics claim.

### Stage 4C — Curved S4 scalar subset evaluation
- Curved subset topologies: S4 scalar triple-bubble, bubble x curvature insertion, curvature-corrected sunset, truncated spectral triple product.
- Spectral truncation uses scalar S4 modes and conformal coupling.
- Curvature expansion uses low-order heat-kernel coefficients.
- Flat-limit consistency is checked against Stage 4B structure.
- Limitations: no tensor sector, no convergence proof.

Statement:
Stage 4C evaluates scalar-sector 3-loop subsets on S4 using controlled truncations. It does not compute the full S4 3-loop CTP effective action and promotes no GRUT physics claim.

### Stage 4D — Tensor-sector subset structure
- Tensor subset topologies: scalar loop with TT insertion, TT bubble x scalar bubble, tensor-corrected sunset, graviton self-energy insertion.
- TT constraints tracked symbolically; no tensor propagator evaluation.
- Contractions are scaffolded only; Ward consistency remains structural.
- Limitations: no explicit tensor propagators, no full contractions.

Statement:
Stage 4D introduces tensor-sector structure into subset evaluation. It does not compute tensor propagators, does not perform full contractions, and does not compute the full S4 3-loop CTP effective action.

### Stage 4E — Mixed scalar–tensor subset evaluation
- Mixed subset topologies: scalar triple-bubble with TT insertion, scalar bubble x tensor bubble, scalar spectral with tensor vertex correction, curvature-corrected scalar with tensor insertion.
- Scalar spectral/curvature pieces combined with tensor placeholders.
- Reduction checks enforce scalar and tensor structural consistency.
- Scheme metadata preserved across mixed structures.
- Limitations: no full contraction, no tensor propagator evaluation.

Statement:
Stage 4E combines scalar and tensor subset structures under strict control. It does not compute the full S4 3-loop CTP effective action and promotes no GRUT physics claim.

### Stage 5A — Constrained native 3-loop attempt
- Chosen topology: s4_3loop_scalar_triple_bubble_native_attempt.
- Pipeline integrates spectral setup, scalar subset evaluation, scheme tagging, divergence tracking, and cross-check routing.
- Evaluation remains truncated and audited with explicit limitations.

Statement:
Stage 5A executes a single constrained native 3-loop attempt under full audit. It does not compute a complete S4 3-loop CTP effective action and promotes no GRUT physics claim.

### Stage 5B — Multi-topology native attempts
- Topologies: scalar triple-bubble, scalar bubble x bubble with curvature insertion, mixed structural scalar-tensor attempt.
- Comparison logic checks divergence structure and scheme metadata alignment.
- Audits enforce no promotion and no hidden evaluation.
- Limitations: no finite 3-loop values, no full tensor propagators.

Statement:
Stage 5B extends constrained native attempts to multiple topologies. It does not compute the full S4 3-loop CTP effective action and promotes no GRUT physics claim.

### Stage 5C — Deep tensor involvement in native attempts
- Chosen topology: s4_3loop_mixed_tensor_native_deep.
- Tensor flow tracking records index propagation and TT constraints.
- Constraint engine applies transversality/tracelessness placeholders without contraction.
- Consistency checks remain structural only.
- Limitations: no tensor propagator evaluation, no full contraction.

Statement:
Stage 5C deepens tensor involvement in native attempts under strict structural control. It does not compute tensor propagators, does not perform full contractions, and does not compute the full S4 3-loop CTP effective action.

### Stage 5D — Candidate extraction readiness audit
- Purpose: scan native attempts for repeated symbolic structures that could become legal extraction targets later.
- Candidate structures record symbolic form, associated invariant, occurrence count, and scheme sensitivity.
- Scheme-safety assessment distinguishes scheme-protected candidates from scheme-fragile or total-derivative terms.
- Blockers document why extraction is not legal yet (finite parts, convergence, tensor contractions, scheme alignment, Ward verification, independent replication).

Statement:
Stage 5D does not extract R, C_Cosmo, C_Final, or any finite 3-loop coefficient. It only identifies candidate symbolic structures and records the blockers that prevent legal extraction.

### Stage 5E — Legal extraction criteria and dry-run report
- Extraction criteria checklist formalizes the legal conditions required before any coefficient could be extracted.
- Blockers from Stage 5D are mapped to required actions, difficulty levels, and dependency stages.
- Dry-run output simulates the extraction pipeline with missing inputs and an undefined coefficient.

Statement:
Stage 5E defines the conditions required for legal extraction and simulates the extraction pipeline without computing any coefficient. No GRUT physics claim is promoted.

### Stage 6A — Targeted closure: scheme alignment
- Chosen blocker: scheme_alignment_missing.
- Reference scheme defines regulator, subtraction convention, normalization, and invariant basis.
- Alignment maps native-attempt structures into the scheme basis with scheme tags.
- Consistency checks compare scheme-protected vs scheme-fragile invariants across topologies.
- Limitations: no finite coefficients, no extraction, partial alignment only.

Statement:
Stage 6A attempts partial closure of scheme alignment. It does not compute finite coefficients and does not permit extraction.

### Stage 6B — Multi-blocker closure harness
- Registers remaining extraction blockers with required inputs, tests, and dependencies.
- Builds a dependency graph to coordinate closure sequencing.
- Defines closure plans without closing any blocker.

Statement:
Stage 6B does not close all blockers. It creates the coordinated closure machinery required to attack them without hidden dependencies.

### Stage 6C — Targeted blocker closure: conformal scalar propagator on S4
- Partially closes the conformal scalar propagator subproblem only.
- Closed-form scalar propagator is recorded with explicit normalization and singularity structure.
- Spectral truncation comparison is structural and does not claim convergence proof.
- Remaining open propagator pieces: TT graviton propagator, ghost propagator, vector/tensor modes.

Statement:
Stage 6C partially closes the scalar conformal S4 propagator subproblem only. It does not close the full S4 propagator blocker and promotes no GRUT physics claim.

### Stage 6D — Targeted closure: ghost propagator on S4
- Defines the Faddeev-Popov ghost operator with curvature coupling on S4.
- Builds a structural ghost propagator representation in a spectral-like form.
- Validation checks confirm operator structure, curvature dependence, and vector index preservation.
- Limitations: no full inversion, no TT graviton closure, no vector/tensor harmonic completion.

Statement:
Stage 6D partially closes the ghost propagator subproblem. It does not close the full S4 propagator blocker and promotes no GRUT physics claim.

### Stage 6E — Vector/tensor harmonic sector benchmarking
- Defines scalar, vector, and tensor harmonic spectra on S4 (structural only).
- Vector harmonics are decomposed into transverse and longitudinal components.
- Tensor harmonics include TT placeholders, trace parts, and scalar-derived components.
- Consistency checks audit orthogonality structure, mode counting, and decomposition completeness.
- Readiness for TT propagator remains structural and non-extractive.

Statement:
Stage 6E benchmarks the harmonic sector required for TT propagator construction. It does not construct the TT graviton propagator and promotes no GRUT physics claim.

### Stage 6F — TT graviton propagator scaffold
- Defines a Lichnerowicz-type TT operator on S4 (structural only).
- Extends the TT projector into harmonic-space placeholders with transverse/traceless conditions.
- Builds a propagator scaffold without inversion or spectral sums.
- Validation checks confirm projector placement and structural TT constraints.
- Limitations: operator not inverted, spectral sum not performed, no mode-by-mode solution.

Statement:
Stage 6F constructs a formal TT graviton propagator scaffold on S4. It does not invert the operator, does not compute propagator coefficients, and does not close the full S4 propagator blocker.

### Stage 6G — Spectral inversion strategy
- Defines TT mode decomposition in S4 harmonic space.
- Records eigenvalue and degeneracy structures (symbolic only).
- Specifies zero-mode handling rules for l=0 and l=1.
- Formal inversion formula is documented without executing spectral sums.

Statement:
Stage 6G defines the spectral inversion strategy for the TT propagator. It does not perform inversion, compute coefficients, or close the full propagator blocker.

### Stage 7A — Scalar spectral inversion benchmark
- Performs controlled scalar spectral inversion with finite l_max cutoffs.
- Compares partial sums to the known closed-form scalar propagator.
- Tracks convergence behavior without claiming a proof.
- Limitations: finite l_max, no uniform convergence proof, coincident singularity unresolved.

Statement:
Stage 7A performs a controlled scalar spectral inversion benchmark. It demonstrates inversion capability in a known case and does not perform TT graviton inversion or extract any GRUT physics result.

### Stage 7B — Ghost/vector spectral inversion benchmark
- Performs controlled ghost/vector spectral inversion with finite l_max cutoffs.
- Uses the ghost operator structure with vector harmonic placeholders.
- Compares to the scalar benchmark structurally only (no equality claims).
- Limitations: finite l_max, structural vector eigenvalues, no full vector propagator closure, no convergence proof.

Statement:
Stage 7B performs a controlled ghost/vector spectral inversion benchmark. It does not perform TT graviton inversion, compute coefficients, or extract any GRUT physics result.

### Stage 7C — TT truncated spectral inversion attempt
- Attempts a truncated TT spectral inversion using TT eigenvalues, degeneracies, and TT projectors.
- Truncates the TT sum to low l_max values without full spectral sums.
- Checks tensor structure preservation without scalar/vector collapse.
- Limitations: finite l_max, truncated sum only, no convergence claims, no TT closure.

Statement:
Stage 7C performs a truncated TT spectral inversion attempt. It does not perform a full TT inversion, compute coefficients, or extract any GRUT physics result.

### Stage 7D — TT inversion diagnostics
- Analyzes stability of the truncated TT inversion across low l_max runs.
- Diagnoses divergence characteristics and regularization needs.
- Examines mode-by-mode behavior and dominant low-l contributions.
- Classifies failure modes without extending the inversion depth.

Statement:
Stage 7D analyzes the behavior of truncated TT inversion. It does not extend inversion, compute coefficients, or extract GRUT physics results.

### Stage 7E — TT regularization layer
- Introduces cutoff, exponential damping, and zeta placeholders for TT sums.
- Compares scheme behavior for stability and divergence suppression.
- Tracks tensor structure preservation under regularization.
- Limitations: finite cutoff, scheme dependence, no renormalization.

Statement:
Stage 7E introduces regularization to stabilize TT spectral inversion. It does not perform renormalization, compute coefficients, or extract GRUT physics results.

### Stage 7F — TT renormalization dry-run
- Maps regularized TT divergences to Stage 3D counterterms.
- Builds a dry-run subtraction plan without executing any subtraction.
- Checks scheme alignment against the Stage 6A reference scheme.
- Ensures Ward/CTP tracking remains structural.

Statement:
Stage 7F maps regularized TT divergences to counterterms and checks scheme alignment. It does not perform renormalization, compute finite parts, or extract GRUT physics results.

### Stage 7G — Finite-part eligibility audit
- Defines requirements for finite-part eligibility.
- Evaluates readiness across divergence mapping, scheme alignment, stability, and structure.
- Identifies blockers and applies eligibility decision logic.

Statement:
Stage 7G determines whether the system is permitted to attempt finite-part computation. It does not perform renormalization, compute finite parts, or extract GRUT physics results.

### Stage 7H — Finite-part blocker repair plan
- Converts finite-part blockers into a repair registry.
- Prioritizes repairs by dependency and eligibility impact.
- Generates a stepwise repair roadmap with completion tests.

Statement:
Stage 7H converts finite-part blockers into a repair roadmap. It does not perform repairs, compute finite parts, or extract GRUT physics results.

### Stage 7I — Targeted repair: convergence control
- Computes convergence metrics across regularized TT inversion outputs.
- Applies threshold checks for partial repair status.
- Records convergence diagnostics without proof of convergence.
- Limitations: no finite-part computation, no divergence subtraction, no proof.

Statement:
Stage 7I attempts partial repair of convergence control for regularized TT inversion. It does not prove convergence, compute finite parts, or extract GRUT physics results.

### Stage 7J — Tensor contraction readiness
- Audits TT index structure, pairing completeness, and TT constraints.
- Defines structural contraction rules and forbidden patterns.
- Verifies TT projector consistency through the inversion pipeline.
- Readiness result recorded without performing contractions.

Statement:
Stage 7J evaluates whether tensor contractions are structurally well-defined. It does not perform contractions, compute finite parts, or extract GRUT physics results.

### Stage 7K — Targeted repair: tensor contraction structure
- Proposes repairs for TT index pairing and free-index issues.
- Proposes canonical TT projector placement for future sandbox usage.
- Defines contraction ordering protocol without executing contractions.
- Records future sandbox eligibility without closing the blocker.

Statement:
Stage 7K repairs tensor contraction structure but does not perform contractions, compute finite parts, or extract GRUT physics results.

### Stage 8A — Controlled tensor contraction sandbox
- Sandbox rules permit only minimal symbolic contractions.
- Symbolic contractions include TT trace removal, transverse placeholder, projector idempotence, and paired indices.
- Forbidden contractions include full diagrams, propagators, and finite coefficient extraction.
- Validation and audit block finite parts and extraction while recording sandbox eligibility.

Statement:
Stage 8A performs only minimal symbolic tensor-contraction sandbox checks. It does not perform full diagram contractions, compute finite parts, or extract GRUT physics results.

### Stage 8B — Limited diagram-local tensor contractions
- Local fragments include projector-metric, TT trace removal, paired indices, and local vertex-index pairing.
- Allowed operations stay local: metric-index contraction, trace removal, projector idempotence, and vertex pairing.
- Validation and audit confirm no propagators, no full diagram contraction, and no finite parts.

Statement:
Stage 8B performs only local symbolic tensor contractions inside isolated diagram fragments. It does not perform full diagram contractions, evaluate propagators, compute finite parts, or extract GRUT physics results.

### Stage 8C — Controlled diagram-fragment tensor contractions
- Controlled fragment combines local fragments (projector-metric, TT trace removal, paired indices, vertex pairing).
- Ordering protocol from Stage 7K is applied before local operations.
- Validation and audit confirm projector/TT constraints preserved with no propagator evaluation or full diagram contraction.

Statement:
Stage 8C performs constrained symbolic contractions across one controlled diagram fragment. It does not perform full diagram contractions, evaluate propagators, compute finite parts, or extract GRUT physics results.

### Stage 8D — Single diagram skeleton contraction (structural only)
- Skeleton defines nodes, edges, projector placement, and index flow across the diagram.
- Structural contraction propagates index pairing and TT constraints without evaluating propagators or loops.
- Constraint checks and audit confirm structure-only handling before any propagator symbolics.

Statement:
Stage 8D constructs and contracts a full diagram skeleton at the structural level only. It does not evaluate propagators, perform loop integrations, compute finite parts, or extract GRUT physics results.

### Stage 9A — Propagator symbolic attachment layer
- Attaches scalar conformal, ghost structural, and TT scaffold propagator records to skeleton edges.
- Compatibility checks enforce field-type matching with symbolic/scaffold status only.
- Validation and audit confirm no propagator evaluation, loops, or finite parts.

Statement:
Stage 9A attaches symbolic propagator records to the diagram skeleton. It does not evaluate propagators, perform loop integration, compute finite parts, or extract GRUT physics results.

### Stage 9B — Loop integrand assembly scaffold
- Assembles symbolic components (propagators, vertices, index flow, symmetry factor, scheme/regulator, loop variables).
- Builds a non-evaluated integrand scaffold without amplitude computation.
- Validation and audit confirm no integration or finite-part computation.

Statement:
Stage 9B assembles a symbolic loop-integrand scaffold. It does not evaluate propagators, perform loop integration, compute amplitudes, compute finite parts, or extract GRUT physics results.

### Stage 9C — Regularized loop-integrand scaffold
- Defines symbolic regularization schemes and attaches regulator factors to the scaffold.
- Tags divergence-sensitive components without evaluation or integration.
- Validation and audit confirm no amplitude computation or finite parts.

Statement:
Stage 9C attaches symbolic regularization to the loop-integrand scaffold. It does not perform loop integration, compute amplitudes, compute finite parts, or extract GRUT physics results.

### Stage 9D — Integration dry-run plan
- Defines symbolic integration variables, domains, and ordering for loop integrals.
- Specifies regulator handling strategy and scheme dependence without execution.
- Audit confirms structure-only plan with no integration or finite parts.

Statement:
Stage 9D defines a plan for loop integration but does not perform integration, compute amplitudes, compute finite parts, or extract GRUT physics results.

### Stage 10A — Controlled partial integration benchmark
- Runs known benchmark sub-integrals (Gaussian, tadpole, one-loop bubble) only.
- Compares benchmark results to known analytic structures.
- Audit confirms no native TT integration or GRUT coefficient extraction.

Statement:
Stage 10A performs controlled benchmark integrations only. It does not integrate the native TT integrand, compute finite GRUT coefficients, or extract GRUT physics results.

### Stage 10B — Native sub-integrand dry-run
- Selects a minimal native sub-integrand slice with regulator retained.
- Attempts symbolic/partial integration without finite parts or amplitudes.
- Audit confirms no full integrand use and no extraction.

Statement:
Stage 10B performs a controlled integration attempt on a minimal native sub-integrand. It does not compute finite parts, amplitudes, or extract GRUT physics results.

### Stage 10C — Multi-subintegrand consistency check
- Selects 2–3 minimal native sub-integrands under a shared regulator/scheme (native_subintegrand_chain_v1, native_subintegrand_scalar_slice_v1, native_subintegrand_ghost_vector_slice_v1).
- Compares symbolic/partial integration behavior without amplitudes or finite parts.
- Audit confirms no full integrand use and no extraction.

Statement:
Stage 10C compares multiple minimal native sub-integrand dry-runs. It does not integrate the full native integrand, compute amplitudes, compute finite parts, or extract GRUT physics results.

### Stage 10D — Native integrand partition map
- Partitions the native integrand into tested, eligible, blocked, and forbidden regions.
- Maps dependencies without integrating any partition or combining amplitudes.
- Audit confirms no full integrand use and no extraction.

Statement:
Stage 10D maps the native integrand into auditable partitions. It does not integrate new partitions, combine amplitudes, compute finite parts, or extract GRUT physics results.

### Stage 10E — Eligible partition dry-runs
- Runs symbolic dry-runs only on eligible future partitions.
- Skips blocked and forbidden partitions without combining amplitudes.
- Audit confirms no full integrand use and no extraction.

Statement:
Stage 10E runs symbolic dry-runs only on eligible future partitions. It does not run blocked or forbidden partitions, combine amplitudes, compute finite parts, or extract GRUT physics results.

### Stage 10F — Partition consistency audit
- Audits consistency across tested and eligible partition dry-runs (sources: 10C, 10E).
- Checks scheme and regulator alignment without any new integration.
- Audit confirms no full integrand use and no extraction.

Statement:
Stage 10F audits consistency across previously tested and eligible partition dry-runs. It does not run new integrations, combine amplitudes, compute finite parts, or extract GRUT physics results.

### Stage 11A — Single partition integration attempt
- Selects one approved partition for controlled symbolic integration (native_subintegrand_chain_v1).
- Keeps regulator active with no subtraction or amplitude construction.
- Audit confirms no full integrand use and no extraction.

Statement:
Stage 11A attempts controlled integration on one approved native partition only. It does not integrate the full native integrand, construct amplitudes, compute finite parts, or extract GRUT physics results.

### Stage 11B — Divergence subtraction dry-run
- Identifies divergences and maps counterterms for one partition (cosmological_constant, Einstein_Hilbert).
- Builds a subtraction plan without performing subtraction or removing regulators.
- Audit confirms no full integrand use and no extraction.

Statement:
Stage 11B simulates divergence subtraction planning for one native partition. It does not perform subtraction, remove regulators, compute finite parts, construct amplitudes, or extract GRUT physics results.

### Stage 11C — Finite-part benchmark gate
- Runs finite-part extraction only on known benchmark expressions (scalar_tadpole_finite_v1, log_integral_finite_v1, pole_plus_finite_v1).
- Compares extracted finite parts to known benchmark values.
- Audit confirms no native inputs and no extraction.

Statement:
Stage 11C proves finite-part extraction only on known benchmark expressions. It does not compute finite parts of native GRUT partitions, compute coefficients, or extract GRUT physics results.

### Stage 11D — Native finite-part attempt: one partition only
- Attempts a partition-level finite part for one approved partition (native_subintegrand_chain_v1).
- Forbids coefficient assembly or any C_Final/C_Cosmo/R naming.
- Audit confirms no full integrand use and no extraction.

Statement:
Stage 11D attempts a finite-part extraction for one native partition only. It does not assemble amplitudes, compute C_Final or C_Cosmo, extract R, or promote any GRUT physics result.

### Stage 11E — Cross-partition finite-part consistency
- Attempts partition-level finite parts across 2–3 approved partitions (native_subintegrand_chain_v1, native_subintegrand_scalar_slice_v1, native_subintegrand_ghost_vector_slice_v1).
- Compares scheme/regulator handling without any amplitude assembly.
- Audit confirms no physical coefficient naming and no extraction.

Statement:
Stage 11E compares partition-level finite-part attempts across approved partitions. It does not assemble amplitudes, compute C_Final or C_Cosmo, extract R, or promote any GRUT physics result.

### Stage 12A — Coefficient assembly dry-run
- Builds candidate buckets from partition-level finite candidates (c_final_candidate, c_cosmo_candidate, scheme_fragile_candidate, nonlocal_scheme_protected_candidate).
- Applies assembly rules without emitting physical coefficients.
- Audit confirms no C_Final/C_Cosmo/R computed.

Statement:
Stage 12A dry-runs coefficient candidate assembly from partition-level finite candidates. It does not compute C_Final, C_Cosmo, R, or any physical GRUT coefficient.

### Stage 12B — Scheme-stability audit
- Audits candidate buckets for scheme stability (c_final_candidate, c_cosmo_candidate, scheme_fragile_candidate, nonlocal_scheme_protected_candidate).
- Classifies candidates as scheme-protected, scheme-fragile, or blocked.
- Records R-route legality without computing any coefficients.

Statement:
Stage 12B audits scheme stability of coefficient candidates. It does not compute C_Final, C_Cosmo, R, or any GRUT physics coefficient.

### Stage 12C — R Construction Legality Gate
- Determines whether a physically meaningful ratio can be formed.
- Enforces strict scheme protection and cancellation conditions.
- Produces legality decision only (no computation).

Statement:
Stage 12C determines whether R construction is legal. It does not compute C_Final, C_Cosmo, R, or any GRUT physics coefficient.

### Stage 12C-R1 — Legality repair diagnostic
- Diagnoses why Stage 12C legality fails across candidate pairs.
- Enumerates scheme, structural, and metadata blockers without changing classifications.
- Recommends minimal repair actions (report only).

Statement:
Stage 12C-R1 audits legality blockers without computing C_Final, C_Cosmo, R, or promoting any GRUT physics claim.

### Stage 12C-R2 — Candidate metadata completion
- Completes missing candidate metadata required by Stage 12C checks.
- Validates required fields and flags any remaining gaps.
- Does not reclassify candidates or override scheme rules.

Statement:
Stage 12C-R2 fills metadata fields needed for legality evaluation without computing coefficients or promoting claims.

### Stage 12C-R3 — Complete tensor-origin and regulator metadata
- Resolves tensor origin and regulator dependence fields using Stage 9C/9D context.
- Validates metadata completeness and flags invalid regulator removal.
- Reports whether legality can be rerun.

Statement:
Stage 12C-R3 completes metadata needed for legality checks without computing coefficients or promoting claims.

### Stage 12C-R4 — Rerun legality after metadata completion
- Reruns Stage 12C legality gate using repaired metadata.
- Reports valid vs blocked pairs and remaining blockers.
- Does not compute or promote R.

Statement:
Stage 12C-R4 reruns legality with updated metadata and does not compute C_Final, C_Cosmo, R, or promote any GRUT physics claim.

### Stage 12C-R5 — Protected candidate source audit
- Audits c_final_candidate source partitions for nonlocal/anomaly protection and regulator preservation.
- Determines whether sources qualify for conditional scheme protection eligibility.
- Reports disqualifying sources without reclassifying candidates.

Statement:
Stage 12C-R5 audits protected-source eligibility without computing coefficients, reclassifying candidates, or promoting claims.

### Stage 12D — Controlled R extraction attempt
- Attempts symbolic R construction only from a Stage 12C legal pair.
- Preserves scheme and regulator tags through cancellation and isolation.
- Audit rejects manual steps and hidden parameter insertion.

Statement:
Stage 12D attempts symbolic R construction only from a Stage 12C legal pair. It does not promote R as a physical result unless validation and audit pass.

### Stage 12E — R extraction result classification
- Classifies the Stage 12D symbolic R attempt without modification.
- Applies legality, validation, and audit outcomes to label the result.
- Records next required action without promoting any claim.

Statement:
Stage 12E classifies the Stage 12D symbolic R attempt. It does not compute, modify, or promote R as a physical GRUT result.

### Stage 12F — R attempt status report
- Summarizes legality, attempt status, and Stage 12E classification.
- Explains publishability blockers and required next action.
- Report-only; no computation or promotion.

Statement:
Stage 12F reports the status of the R attempt without computing, modifying, or promoting R as a physical GRUT result.

### Stage 12G — R-route terminal audit package
- Bundles Stage 12A–12F outputs into a terminal audit package.
- Includes blocker ledger and required next action.
- Audit/report only; no computation or promotion.

Statement:
Stage 12G bundles the R-route audit package without computing, modifying, or promoting R as a physical GRUT result.

### Stage N1 — Nonlocal anomaly-channel source extraction
- Scans aligned structures for nonlocal anomaly-channel sources (e.g., R log(Box) R).
- Filters out local counterterms and non-protected bookkeeping terms.
- Reports candidate nonlocal sources without reclassification.

Statement:
Stage N1 reports potential nonlocal anomaly-channel sources without computing coefficients or promoting claims.

### Stage N2 — Imaginary/causal sector audit
- Scans aligned terms and candidates for imaginary/causal indicators (Im log(Box), branch cuts, SK/CTP markers).
- Flags absorptive/dissipative or nonlocal kernel structures where present.
- Report-only; no coefficient computation or promotion.

Statement:
Stage N2 audits imaginary/causal sector indicators without computing coefficients or promoting claims.

### Stage P1 — Nonlocal anomaly source generation plan
- Defines required nonlocal anomaly source types and derivation inputs.
- Records acceptance tests and failure modes without claiming any derived source.
- Requirements-only; no computation or promotion.

Statement:
Stage P1 defines requirements for nonlocal anomaly sources without computing coefficients or promoting claims.

### Stage P2 — Nonlocal anomaly kernel derivation attempt
- Attempts to identify a non-scaffold nonlocal anomaly kernel candidate.
- Records missing reasons and remaining acceptance tests.
- Report-only; no coefficient computation or promotion.

Statement:
Stage P2 attempts a nonlocal anomaly kernel identification without computing coefficients or promoting claims.

### Stage OR4 — Formal R Definition Gate

Result:
- R is now formally defined only inside the round-S4 Euler anomaly channel.
- R_log_box_R is the only currently allowed protected kernel role.
- Weyl_log_box_Weyl is blocked on round S4 because Weyl^2 = 0.
- Im_log_minus_box_i_epsilon is blocked unless a CTP-to-Euler projection is derived.
- Numeric R remains forbidden.
- Physical R claim remains forbidden.
- Euler coefficient symbol binding is allowed.

## Labeling policy
- scaffold
- benchmarked
- speculative/internal
- computed

**Explicit warning:**
GRUT-RAI v3 does not yet compute the full 3-loop curved-space CTP effective action. This package builds the audited pathway toward that target.
