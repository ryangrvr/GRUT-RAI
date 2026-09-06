# PREFLIGHT_IMPLEMENTATION_AUDIT.md — RRT-0 STOP-FOR-AUDIT (2026-09)

Status: AUDIT ONLY. No pipeline run. No commit of model-code changes.
Freeze integrity: SHA-256 of all six frozen artifacts re-verified against
`RRT0_FREEZE.json` on this date — **all six match exactly** (SPEC cbbc381a…,
LEDGER 362c1546…, CLAIM_BOUNDARIES 1f49ae98…, TEST_MATRIX d50292f4…,
CONTROL_MATRIX ad3365b1…, RECONSTRUCTION_SPEC 9f02e47c…).

Note on the freeze timestamp (`frozen_at: 2026-02-13`): the copied repository
preserves the original pre-simulation freeze. The SPEC itself states simulation
had not started at freeze time. This is treated as the intended historical
freeze, not a stale artifact; nothing frozen has been regenerated.

---

## 1. Exact frozen E_alpha definition (RRT0_SPEC.md, lines 17–22)

    E_alpha(rho) = U^{tau_op} [ (1 - lam) rho + lam sigma_alpha ] U^{-tau_op}

with lam = 0.05, sigma_alpha = normalized projector onto the sector support,
tau_op = 3 update steps, U the seed's frozen GUE step unitary.

## 2. The `core.py` comment is FALSE — record, do not silently patch

`core.py` lines 149–152 claim the literal frozen formula "is the identity map
(conjugations cancel)". **This is incorrect.** Conjugation by U does not cancel:

    U [ (1-lam) rho + lam sigma ] U^{-1} != (1-lam) rho + lam sigma

unless the argument commutes with U. Numerically verified in
`tests/test_internal_operation_audit.py::test_conjugation_does_not_cancel`
(random GUE U, random sigma: max deviation ~ O(1), far above float64 noise).

Defect classification: **documentation/interpretation defect** (a false
claim in code), not a computation defect — the function returns only the
perturbation `(1-lam) rho + lam sigma` and lets the caller evolve.

## 3. Equivalence of the implementation with the frozen formula — DISPROVED, with exact characterization

Current implementation, at a use site where the caller then evolves n steps:

    rho -> M(rho) := (1-lam) rho + lam sigma    (core.internal_operation)
    rho -> U^n M(rho) U^{-n}                    (caller evolution)

Frozen specification, followed by the same n-step caller evolution:

    rho -> U^{n + tau_op} M(rho) U^{-(n + tau_op)}

These are NOT equal in general. The exact relationship is:

    implementation result = U^{tau_op} [frozen result] U^{-tau_op}

i.e. the two agree only if `M(rho)` commutes with `U`, which is not generic.
Equivalently: **the current implementation realizes the frozen operation up to
a tau_op = 3 update-step time shift** of the entire post-perturbation history,
including the baseline. Verified numerically in
`tests/test_internal_operation_audit.py::test_implementation_vs_frozen_timeshift`.

Consequences:
- The *difference* trajectory Delta_rho(tau) = U^tau [E(rho) - rho] U^{-tau}
  is identical in both readings, merely indexed 3 steps apart. The analytic
  no-go (Section 4) is therefore unaffected.
- Pointwise influence values Phi_{a->b}(t, tau) at finite tau and the
  two-half repeatability split (t in [0,T/2), [T/2,T)) are NOT invariant
  under a 3-step shift. G1–G2 gate outcomes could in principle differ.
- Verdict on question (B): the current code **cannot yet** be certified as a
  faithful implementation of the frozen model. The discrepancy is exact,
  understood, and small (3 of 200 steps), but per the freeze protocol it must
  be resolved by an explicit, documented decision — not silently.

Required resolution (pick one, record in the audit trail before running):
  Option 1 (recommended): implement `E_alpha` literally as the frozen formula
    (perturb AND conjugate by U^{tau_op}), then let the caller evolve. No
    frozen artifact changes; the code moves to match the spec.
  Option 2: freeze an addendum declaring the operational reading
    (perturb-then-evolve) as the intended semantics, accepting the tau_op
    shift, with the equivalence-up-to-shift proof above as justification.
  Option 3 is forbidden: leaving the false "identity map" comment in place.

## 4. Exact sectors.py defect — recorded, NOT fixed in place

`rrt0/model/sectors.py` line 38:

    rp = internal_operation(rho, BASIS[a] and _sig(a), lam_probe)

`BASIS[a]` is a NumPy array; `array and expr` raises
`ValueError: The truth value of an array with more than one element is
ambiguous`. Confirmed by
`tests/test_internal_operation_audit.py::test_sectors_bug_raises`.
Intended expression per the frozen spec (perturbation sigma_alpha = normalized
support projector of basis operator a): `_sig(a)`. This is verified against
SPEC line 20 ("sigma_alpha = normalized projector onto the sector support").
The defect means **S1 has never executed**; no numerical output exists to
contaminate. Fix is deferred until the E_alpha decision (Option 1 vs 2) is
made, since the repaired probe must use whichever operation is certified.

## 5. Analytic reducibility theorem (unchanged, re-asserted)

For any intervention E and the same closed unitary propagation thereafter:

    Delta_rho(tau) = U^tau [ E(rho) - rho ] U^{-tau},   exactly.

Hence the raw response in the closed-linear-unitary model class is fully
reducible to the triple (rho, E, U): the perturbation delta = E(rho) - rho is
carried by the same propagator as everything else; no dynamics-internal
irreducibility can arise. This holds for BOTH readings of E_alpha (literal or
shifted), so the no-go is independent of the Section 3 discrepancy. It must
not be weakened to obtain a positive emergence result; H4 failing for this
model class under the irreducibility criterion is a valid negative result.

## 6. Model-class boundary

Closed, linear, unitary, d = 4, GUE generator, no environment, no
non-linearity, no feedback, update-step index not physical time (GATE-A).
The no-go conclusion is a property of THIS class. It does not license
widening the class post hoc; any widening is a new pre-registered experiment.

## 7. Changes required before execution (minimum set)

1. Resolve E_alpha per Section 3, Option 1 or 2, recorded in audit trail.
2. Correct the false comment in `core.py::internal_operation` (comment-only
   change; no frozen file touched).
3. Repair `sectors.py` line 38 to `internal_operation(rho, _sig(a), lam_probe)`
   WITH a regression test (`tests/test_internal_operation_audit.py`) committed
   alongside.
4. Implement the sector-discovery firewall of SECTOR_DISCOVERY_AUDIT.md
   (discovery window vs held-out window, split frozen before run).
5. Re-hash all frozen artifacts; only then may Phases 2+ be scheduled.
