# RRT-0 — PREFLIGHT FINAL REPORT

Status: **PREFLIGHT COMPLETE — Phase-1 battery MAY proceed under restricted claims.**

## 1. Preflight sequence completed

| Check | Result |
|---|---|
| Structural no-go derivation | CONFIRMED (exact, analytic) |
| Reducibility decomposition | registered (`model/reducibility.py`) |
| Verdict | banked in `MODEL_CLASS_VERDICT.md` |

## 2. Verdict

`FULLY_REDUCIBLE_IN_LINEAR_UNITARY_MODEL_CLASS`

The raw influence statistic Phi is, in this model class, exactly a
propagation/response quantity. The irreducibility question is decided
in preflight, not by the battery.

## 3. Numerical confirmation (Route A vs Route B)

Route A propagates the injected difference directly; Route B propagates
`rho_0` and `rho_E` independently and subtracts. Analytically identical.

- acceptance band: residual ratio <= 1e-10  (float64 roundoff expected ~1e-13)
- verdict ladder: REDUCIBLE / NUMERICALLY_UNRESOLVED / RESIDUAL_REQUIRES_AUDIT

## 4. Consequences for the Phase-1 battery

Permitted claims:
- propagation / scrambling diagnostics
- sector (representation) dependence of response
- numerical conditioning audits

Prohibited claims (in this model class):
- any verdict of irreducible emergence
- any causal structure not supplied by {U, E, B}

The battery remains informative as a propagation and representation
audit; it cannot be used to certify emergence in this class.

## 5. Inputs to Phase-1 (frozen before run)

- `INPUT_LEDGER.md` — declared inputs and tolerances (no post hoc tuning)
- `SPEC.md` — registered specification
- `model/core.py`, `model/sectors.py` — frozen implementation

## 6. Sign-off

Preflight owner: GRUT RRT-0 working notes
Date: 2026-08-14
Next gate: Phase-1 run under restricted-claims protocol.
