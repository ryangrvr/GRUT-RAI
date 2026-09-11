# REALITY CHECK 04 — ADDENDUM: CONTROL D REJECTED, VERIFICATION COMPLETE

Executable independent verification: `calc/verify_experiment_p.py`
Machine output: `program/REALITY_CHECK_04_VERIFICATION.json`
Date: 2026-09-11. No Experiment P artifact modified. Canonical GRUT-RAI untouched.

## 1. Controls A and B — CONFIRMED

- **A (decoherence):** exact. `unitary` residual = 1.0 (float noise), global purity = 1.0,
  cross term = 0 exactly (shift-record U₁ has disjoint support from e₀). Reduced purity 0.5.
  → `DECOHERENCE = DERIVED` (record-type measurement model, verified).
- **B (definite outcome):** final global state = |α⟩|0,rec↓⟩ + |β⟩|1,rec↑⟩ — zero inter-branch
  coherence, both branches present, no selection operation in U.
  → `DEFINITE OUTCOME = NOT_DERIVED` (verified).

## 2. Control D — INVALID AS EXECUTED (quarantined)

Re-executed the claimed purification-pair control. The second environment state does **not**
decohere under the same U: cross term = 0.1116 ≠ 0. The pair is therefore **not** an
identical-reduced-state pair, and Control D does not test purificational indistinguishability.
It must not be cited as evidence for the non-identifiability verdict.

## 3. Control H — CONFIRMED but RE-SCOPED

α ∈ {0.2, 0.5, 0.8} all give cross = 0 with different p₀ (0.04, 0.25, 0.64).
Correct statement: decoherence class is matched while weights differ — **because the weights
are inherited from the initial amplitudes, not derived**. The stronger claim
"weights are NON-IDENTIFIABLE" holds **only relative to the decoherence-observable set**
(p₀ is itself an element of the full reduced state). The committed H scoping note already
says this; it survives verification.

## 4. Corrected status table

| CLAIM | STATUS |
|---|---|
| Closed unitary → decoherence | DERIVED (verified) |
| Decoherence suppresses reduced coherence | DERIVED (verified) |
| Global unitary state selects one outcome | NOT_DERIVED (verified) |
| Pointer basis = realized outcome | NOT_DERIVED |
| Outcome probabilities dynamically derived | NOT_DERIVED (inherited) |
| Born weights derived | NOT_DERIVED — ASSUMED/INHERITED from initial amplitudes |
| Reduced state uniquely identifies global outcome info | PURIFICATION CLAIM NOT TESTED (Control D invalid) |
| Coarse-graining uniquely selects outcome | NOT_DERIVED |
| Additional outcome-selection structure required | DERIVED (collapse supplies exactly this, as ADDITIONAL_INPUT) |
| Universal beyond tested model class | OUTSIDE_SCOPE |

## 5. Corrected final sentence

> Experiment P establishes decoherence and shows that outcome weights are inherited from
> initial amplitudes rather than derived, within the tested record-type measurement model
> class; its purificational control (D) is invalid as executed and is quarantined.

## 6. Frontier status

`EXPERIMENT_P_FRONTIER = CLOSED_AT_TESTED_MODEL_CLASS` — with the Control D defect recorded
as a limitation on the *purificational* argument only. The decoherence/not-derived-outcome
result stands on A/B/H, all verified.
