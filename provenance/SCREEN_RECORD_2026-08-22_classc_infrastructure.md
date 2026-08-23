# Screen record — Class-C infrastructure + first executable skeleton (2026-08-22)

> **Four-lens adversarial screen per the owner brief** (object identity / parameter
> leakage / numerical validity / outcome bias), attacking the INFRASTRUCTURE and the
> first executable skeleton — not just documentation. Includes the owner's named
> mutation test: inject forbidden parameters and verify the system catches them
> before a result can be emitted.

## Surfaces attacked

`CLASS_C_MANIFEST.json` · `provenance/class_c_manifest_gate.py` ·
`calc/class_c_solver.py` · `provenance/class_c_dependency_closure.py` ·
`provenance/class_c_contamination_audit.py` · `provenance/class_c_benchmark_matrix.py`

## Lens results

### Lens A — mathematical correctness
- Caught during development: the INDEPENDENT-CODE benchmark's fold integral used
  the wrong domain ([0, Λ] instead of [ω, Λ]) and disagreed at 3.5e-04. Per Phase 5,
  disagreement = investigation trigger; root cause was in the checker, fixed on its
  face (docstring records the catch). Post-fix agreement: exact (Simpson is exact
  for a quadratic integrand).
- Half-line transform expectation corrected by factor derived from first principles
  (∫ from 0 gives π not 2π); pipeline then matched to <3%.

### Lens B — object identity
- The solver computes NOTHING while prerequisites are undecided (exit-2 refusal,
  selftest-verified) — it cannot silently compute a different object than declared.
- The manifest's primary_object names class C explicitly; `not_the_object` lists
  the worldline proxy, any staked J(ω), and scalar-surrogate exports.

### Lens C — parameter leakage
- Dependency-closure scanner: 8 bypass channels (env vars, seeds, config reads,
  historical imports, module constants, numeric default args, forbidden tokens,
  pole-injection flags) — ALL EIGHT MUTANTS CAUGHT in-memory; clean source passes;
  live surface (class_c_solver.py) scans CLEAN.
- Known residual (declared): the closure audit polices files matching
  calc/class_c*.py by filename. A future solver that evades the naming convention
  would be invisible to it. Mitigation: the dispatch freeze enumerates the
  authorized execution surface; anything outside it is unauthorized by definition.

### Lens D — outcome bias
- Mutation test executed: a fake favourable pole (`pole_found = True`) and a
  staked J ∼ ω³ line injected into candidate solver sources are BOTH caught by the
  detector (POLE_INJECTION / FORBIDDEN_TOKEN rules) before any result could emit.
- The manifest carries no preferred outcome: permitted_outcome_classes are
  symmetric across all six resolutions.

## Catches made during this screen's own construction

1. Contamination audit initially flagged its own machinery and the checker tools'
   reference/test data as CONTAMINATION → reclassified (CHECKER /
   REFERENCE-DATA-INERT), with the rule recorded: checkers hold reference data;
   solvers may not.
2. A false positive where the independence criterion ∂τ_phys/∂k_min = 0 tripped
   the hard-coded-regulator pattern → lookbehind fix.
3. The benchmark matrix initially reported FAILURES because the independent fold
   route disagreed — investigation trigger honored (Lens A above).

## Status

INFRASTRUCTURE SCREEN: PASS with the three catches recorded and remediated.
Queued: repeat of this screen against the grown solver when class-C physics code
first executes; provenance ledger maintained per Phase 11.
