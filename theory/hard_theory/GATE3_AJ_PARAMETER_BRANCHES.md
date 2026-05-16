# Gate 3 Allen-Jacobson Parameter Branches

Date: May 9, 2026  
Scope: Define the concrete h_+/h_- branch before any 3-loop cube-integral retry.

## Why This File Exists

The current blocker is no longer Mathematica/HypExp runtime availability.
The blocker is underdefinition of the AJ hypergeometric kernel parameters:

\[
{}_2F_1(h_+, h_-; D/2; u), \quad u=\frac{1+Z}{2}, \quad D=4-2\epsilon.
\]

Without a concrete branch for \(h_+\) and \(h_-\), Laurent extraction is not physically meaningful.

## Branch Table

| Branch ID | Purpose | Promotion status |
|---|---|---|
| conformal_closed_form | benchmark only | not target |
| massive_regulated | candidate regulator branch | possible |
| hminus_direct_limit | target-like but singular risk | blocked until validated |
| hminus_derivative_regularized | likely best candidate | investigate |
| mmc_massless | zero-mode problematic | blocked |

| Branch ID | h_+ | h_- | Status | Regulator |
|---|---|---|---|---|
| conformal_closed_form | \(D/2\) | \((D-2)/2\) | benchmark | none |
| massive_regulated | \((D-1)/2 + \nu\) | \((D-1)/2 - \nu\) | candidate | GATE3_M2_OVER_H2 (required) |
| hminus_direct_limit | \(D-1\) | \(0\) | blocked until validated | none |
| hminus_derivative_regularized | regulated continuation | regulated continuation | investigate | none |
| mmc_massless | \(D-1\) | \(0\) | likely blocked | none |

where \(\nu = \sqrt{(D-1)^2/4 - m^2/H^2}\) for massive_regulated.

## Branch Notes

- conformal_closed_form: benchmark only. It has a known closed-form reduction and is the first correctness gate.
- massive_regulated: primary analytic candidate when a mass regulator is retained. Requires GATE3_M2_OVER_H2 environment variable set to a positive numeric value (e.g., 0.5, 1.0).
- mmc_massless: expected zero-mode/IR singular behavior.
- hminus_direct_limit: direct \(h_-=0\) route is blocked until a validation argument is written.
- hminus_derivative_regularized: likely best target candidate, but still requires an explicit derivative prescription.

## Regulator Parameter Specification

The `massive_regulated` branch requires an explicit regulator parameter:

```
GATE3_M2_OVER_H2 = <positive rational or decimal>
```

Validation rules:
- Must be a positive number (integer or decimal)
- Zero and negative values are rejected
- Non-numeric strings are rejected
- If unset when massive_regulated is selected, branch blocks with blocker="massive_regulated requires GATE3_M2_OVER_H2"

Example execution:
```bash
export GATE3_BRANCH_ID=massive_regulated
export GATE3_M2_OVER_H2=0.5
bash scripts/run_gate3_mathematica_handoff.sh
```

Provenance metadata added to blocked/computed outputs:
- `m2_over_h2`: the regulator parameter value (if provided)
- `regulator_role`: "massive_scalar_ir_regulator" (for massive_regulated branch)

## Mandatory Pre-Cube Sequence

1. Conformal benchmark:
   - Verify
   \[
   {}_2F_1\left(\frac{D}{2},\frac{D-2}{2};\frac{D}{2};u\right)=(1-u)^{-(D-2)/2}.
   \]
2. Branch declaration:
   - Record exact \(h_+\), \(h_-\), regulator assumptions, and any limit prescription.
3. Legality check:
   - Confirm Euler-only, round-S4 projection constraints remain intact.
4. Cube integral:
   - Only after steps 1-3 are complete, run AJ cube Laurent extraction.

## Implementation Hooks

Python module:
- grut/derivation/tji/aj_parameter_branches.py

Provides:
- explicit branch definitions,
- conformal reduction benchmark check,
- serializable branch status table for audit/report tooling.

## Current Gate 3 Implication

If branch declaration is absent or ambiguous, Gate 3 output must remain blocked and non-promotable.
