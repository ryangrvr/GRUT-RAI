# S7 regime adjudication — Onsager reciprocity in the open de Sitter setting

**Date:** 2026-08-23 · Classification: **ADOPTED-WITH-SCOPE** · Drafted for owner, not booked.

## The question

Does pair symmetry K_{ij,ab} = K_{ab,ij} survive in the open, non-equilibrium de Sitter
influence-action setting, or was it imported from equilibrium/closed-system intuition?

## What the record establishes

### Where S7's license lives

| regime | license | mechanism |
|---|---|---|
| Equilibrium / KMS state | **derived** | microscopic reversibility + detailed balance ⇒ reciprocity automatic |
| Static patch of dS (BD state) | **KMS holds** at T_H = H/2π (Gibbons–Hawking); reciprocity follows | observer-dependent thermality |
| Cosmological frame (flat slicing), BD state | pure state, **no global KMS**, no global timelike Killing vector; reciprocity NOT automatic | |
| Registered (ε,τ₂) quasi-equilibrium family | **family-conditional closure theorem** derives the two-parameter restriction WITHOUT separate S7 (positivity + FDT + Ward jointly suffice) | |
| Beyond (ε,τ₂) family (SCDP Eq. 1.11 class) | **larger space**; S7 unlicensed; X_sw admissible | |

### Key structural facts from the register

- `RESULTS_operator_basis.md` S7: "for the *retarded* kernel a substantive microscopic
  time-reversal assumption **not implied by S1–S6**"
- `rung2_kms_gate`: "IN EQUILIBRIUM… OUT OF EQUILIBRIUM there is no KMS temperature by definition;
  the departure of N from its KMS-locked value is parameterized by exactly the two dials"
- `p_tt_ansatz.boundary_condition`: "within the booked FDT-locked scalar-dial family the
  admissible (K_R, N) pair closes on the transverse pair P^(2), P^(0s) — a **family-conditional
  closure theorem**"; outside the family, SCDP's strictly larger space stands
- `rung7_wz` third input (+1): the RESTRICTION to the (ε,τ₂) family is itself priced —
  acknowledging that out-of-equilibrium states are more general than the ansatz

## Adjudication

> **S7 is ADOPTED-WITH-SCOPE.**
>
> - **Inside the FDT-locked / KMS-compatible sub-sector:** S7 is derived-in-regime
>   (follows from detailed balance). The two-parameter family is legitimate there.
> - **Outside that sub-sector:** S7 is unsupported. The Ward-surviving family is honestly
>   three-dimensional ({P², P⁰s, X_sw}). The third structure reads longitudinal/trace sources
>   and emits transverse-trace response — admissible precisely because open systems break
>   the doubled gauge symmetry to diagonal.
> - **Inside the registered (ε,τ₂) family specifically:** S7 is SUBSUMED by the
>   family-conditional closure theorem (positivity+FDT+Ward jointly derive the restriction).
>   S7 need not be booked separately here — but the closure theorem's own conditions must be.

## Practical consequence for the Bardeen/FRW completion

Start from the **three-dimensional** Ward-surviving family {P², P⁰s, X_sw}. Then:

1. Determine whether the de Sitter/open-system state lies inside the KMS/FDT sub-sector.
2. If yes → the closure theorem reduces to two parameters; cite the theorem, not bare S7.
3. If no → the three-parameter family stands; c₀=0 AND c_sw=0 are both constitutive choices.

Do not start from two and try to justify the third structure away after the fact.

## Status

ADOPTED-WITH-SCOPE. Drafted for owner adjudication. Not booked by builder.
No claims.json edit. W-0 binding.