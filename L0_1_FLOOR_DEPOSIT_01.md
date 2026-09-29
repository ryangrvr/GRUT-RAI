# L0-1 FORMULABILITY FLOOR — DEPOSIT 01

**STATUS: COMPLETE** (T5 of `L0_1_FLOOR_TERMINATION_ADOPTION_01.md`).
O-1 … O-6 carry terminal labels accepted by owner ruling, and the O-7
synthesis is recorded and ruled on (`L0_1_FLOOR_O7_OWNER_RULING_01.md`).

**Rules of this document:**
- It is a ledger. It asserts nothing beyond the records it cites (T7).
- **No new physics** was run for it.
- It does not modify any floor record.
- Per T6, FALSIFIED completes an obligation exactly as DISCHARGED does.

**Date:** 2026-09-29 · **Branch:** `master-w25bu9`.

## §1 Terminal labels

| Obligation | Content (T1) | Terminal label | Ruling record |
|---|---|---|---|
| O-1 | D-HERM-a: cycle affinity vs asymmetry (response) | **CLASS-SPLIT** | `L0_1D_OWNER_RULING_01.md` (`05cc424`) |
| O-2 | D-HERM-b: accretivity vs spectral stability | **FALSIFIED** | `L0_1H_OWNER_RULING_03.md` (`35f62a6`) |
| O-3 | D-DET-a: primitive noise, FDT held | **DISCHARGED** | `L0_1E_OWNER_RULING_01.md` (`550a237`; comment `5888965691`) |
| O-4 | D-DET-b: noise–dissipation mismatch vs P^corr | **CLASS-SPLIT** | `L0_1E_OWNER_RULING_02.md` (`5969888`) |
| O-5 | D-ORD-a: formulability of order, dissipative classes | **DISCHARGED** (theorem-document scope) | `L0_1F_OWNER_RULING_01.md` (`61ad17a`) |
| O-6 | D-ORD-b: window-relative ordering, conservative split | **FALSIFIED** (strict pointwise form only) | `L0_1G_OWNER_RULING_02.md` (`6f3c54b`) |
| O-7 | Synthesis: the two-property reduction hypothesis | **FALSIFIED** | `L0_1_FLOOR_O7_OWNER_RULING_01.md` |

## §2 Qualifications that travel with each label (binding; not to be dropped in citation)

**O-1.**
- On one ring with one symmetric part: zero-affinity asymmetry is
  reducible to a reciprocal twin, and response CM survives.
- Cycle affinity breaks response CM at every declared member. The memory
  envelope survives.
- **Asymmetry ≠ the relevant distinction.** This is a class split, not
  a universal theorem.

**O-2.** Retained site, n = 23, a = 1, eight declared g.
- H2-m is FALSIFIED by theorem P-1 (state growth is invisible at the
  retained site).
- H2-s is FALSIFIED by exact certified counterexamples (margin ≥ 1.44).
- H2-n holds at tested scope, is recorded independently, and rescues
  nothing.
- Certified nesting at each tested g: **w\* < d_acc < d_mono.**
- **The mechanism is not established** (the lap reading is untested).
- The affinity/CM line (J-4) is outside O-2.
- The label rests on H2-s's positive findings, not on the observability
  identity alone (termination adoption, the O-2 limitation).

**O-3.**
- With FDT held, determinism is not load-bearing for any tested
  predicate (identity-grade, recorded as such).
- Primitive vs derived noise is unformulable at second order (S-1).

**O-4.**
- Correlation CM is a convex polyhedral cone in temperature space, with
  FDT in its interior.
- **Placement, not the magnitude of the detailed-balance break,**
  decides.
- Part of the placement effect reduces to the odd-moment locality
  hierarchy (synthesis draft, operator note 3).

**O-5.** Theorem-document scope.
- Strict-Lyapunov structure is sufficient for derived order.
- Recurrence (α∩ω ≠ ∅) obstructs it (Conley).
- The pole-sensitive memory form holds.
- **The generator is presupposed, not derived (S-5).**

**O-6.** Strict pointwise / whole-window form only.
- No state-function ordering (I-1 … I-4).
- Initial slip: the past hypothesis ≠ an arrow at t = 0 (I-5).
- Band-edge t⁻³ sign-alternating ripples (D-1).
- **It does not establish that no coarse-grained arrow can emerge
  (S-6).**

**O-7.**
- The reduction to "dissipation" and "detailed balance" fails on
  certified boundaries: O-2's d_mono, O-4's placement, and O-6's
  emergent dissipation without strict order.
- **No repair by redefinition or by adding a third property.**
- §1(iii) is kept but scoped: *within the declared O-2 one-way-ring
  family, detailed-balance status does not decide monotone retained
  response.* It is a scoped counterexample to sufficiency, not a
  general theorem.

## §3 The accepted surviving statement (owner, O-7 ruling)

> At the floor, the retained-site description has no single deep
> organizing pair. Its behavioral properties factor across distinct
> structural ingredients, each with its own certified boundary. The
> certified relations among them are almost entirely non-implications.

The boundary table and the certified non-implications are recorded in
`L0_1_FLOOR_O7_ADJUDICATION_01.md` §4, each at its own scope.

**Certified non-implications:**
- linearity ⇏ memory;
- locality ⇏ memory;
- asymmetry ⇏ irreversibility-relevant structure;
- noise nonequilibrium ⇏ correlation failure;
- emergent dissipation ⇏ strict ordering;
- past hypothesis ⇏ arrow at t = 0;
- spectral stability ⇏ accretivity ⇏ monotone retained response.

## §4 Registry in force

R-1 … R-4 (`L0_1_FLOOR_REGISTRY_RULINGS_01.md`):
- R-1: the envelope comparator for P_memory;
- R-2: P^resp / P^corr split;
- R-3: static readings, accepted at linear-class scope;
- R-4: passivity means accretivity, distinct from spectral stability.

## §5 Successor list (T4: preserved, not executed under floor authority)

Full text in `L0_1_FLOOR_SUCCESSOR_LIST.md`.

| # | Question |
|---|---|
| S-1 | Is noise primitive or derived? (unformulable at second order in the linear-Gaussian class) |
| S-2 | The hard D-DET: multiplicative, colored, non-Gaussian, nonlinear stochastic classes |
| S-3 | The crossed cell: does generator-side cycle affinity break correlation CM with FDT-like noise? |
| S-4 | Re-reading the two-property hypothesis (needs a T4 ruling; it would be a new hypothesis) |
| S-5 | Can the generator itself be derived rather than presupposed? |
| S-6 | Does a coarse-grained arrow survive band-edge memory? |
| S-7 | What sets the monotone boundary d_mono? *(local follow-up, not the priority front)* |
| S-8 | The affinity/CM line, pre-registered independently *(local follow-up, not the priority front)* |

**Held elsewhere, not on the floor:**
- the pin-free locality fork (L0-1b Outcome A; T8);
- the reversal/chiasm diagnostic (`L0_STRUCTURAL_DIAGNOSTIC_REVERSAL_01.md`,
  a pre-registered Level-0 synthesis test). Its status at the deposit:
  - **not evaluated, neither supported nor refuted**;
  - the floor created no property → ingredient edge, which deletion
    instruments cannot create by construction;
  - the composed graph remains acyclic.

## §6 What the floor did not do

- It did not derive the generator.
- It did not settle primitive vs derived noise.
- It did not test any coarse-grained arrow.
- It did not establish the mechanism of any boundary it certified.
- It makes **no claim about the axioms of reality** (the L0-1a ruling's
  scope discipline).

The broader investigation stays open beyond this boundary (T6). The
next work, project-state reconciliation and forest synthesis, is a
**separate post-floor task** and does not modify this deposit.
