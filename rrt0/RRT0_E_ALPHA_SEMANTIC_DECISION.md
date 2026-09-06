# RRT-0 — E_ALPHA SEMANTIC DECISION (APPEND-ONLY)

Status: RESOLVED — OPTION 1 AUTHORIZED
Date: (see commit record)
Authority chain: RRT0_FREEZE.json -> canonical E_alpha semantics -> implementation -> semantic tests -> simulation eligibility.

## Decision

**Option 1 selected.** The canonical intervention map for Phase 2 is the
literal frozen specification, interpreted as the map:

    E_alpha[rho] = (1 - lambda) rho + lambda sigma_alpha

**Unit propagation is a subsequent and separate operation:**

    rho(t + tau_op) = U^{tau_op} E_alpha[rho(t)] U^{-tau_op}

The intervention map itself contains NO unitary conjugation. Any reading in
which U^{tau_op} conjugation is embedded inside E_alpha is a noncanonical
operational interpretation and is not the frozen semantic content.

## Frozen artifact hashes

The SHA-256 hashes recorded in `RRT0_FREEZE.json` remain authoritative.
No frozen artifact is modified by this decision. Freeze verification after
Phase-2 implementation must reproduce every recorded hash exactly; any
mismatch is a hard stop.

## Disposition of prior nonconforming implementation / outputs

- The prior implementation history is retained as provenance; nothing is erased.
- Any output generated before this semantic correction that relied on a
  different operational interpretation of E_alpha is classified:

      NONCONFORMING / OUTSIDE FROZEN RRT-0 EVIDENTIARY SCOPE

  unless independently reproduced under the canonical implementation above.

  Known affected artifact: pre-correction influence/sector probes computed
  with the legacy internal_operation docstring framing (the U-conjugation-
  embedded reading), including any influence matrices or sector clusters
  derived from them. These are diagnostics provenance only, not evidence.

- Prior outputs are NOT retroactively reinterpreted as results.

## Implementation policy

- E_alpha is implemented in exactly ONE authoritative function
  (`rrt0.model.core.e_alpha`). No module (influence, calibration, controls,
  sector discovery, reporting) may duplicate its mathematics; all call the
  authoritative function.
- The confirmed defect in `rrt0/model/sectors.py`
  (`internal_operation(rho, BASIS[a] and _sig(a), lam_probe)`) is repaired to
  call the authoritative map with the intended sigma_alpha = support
  projector of BASIS[a], per the spec-consistent operation. Frozen
  specification is untouched.

## No-go scope note

The reducibility no-go applies to the finite closed, linear-unitary,
externally intervened model class only — not to RRT as a whole. The expected
analytic result of the Phase-2 scientific gate is:

    Delta_residual = 0  (FULLY_REDUCIBLE_IN_CLOSED_LINEAR_UNITARY_MODEL_CLASS)

for the registered model class, subject to the Route A/B/C and residual
diagnostics actually being run. This expectation is NOT hard-coded in the
implementation.

---
*Append-only: subsequent entries are added below; earlier text is never edited.*
