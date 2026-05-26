# Gate 3 hminus_direct_limit Classification Report

Date: 2026-05-25T23:07:57.563711
Spec: gate3-hminus-direct-limit-spec-v1.0

## Summary

Prescriptions evaluated: 3
Promoted (all 8 pass): 0 — NONE

**OUTCOME: Mixed failures — see per-prescription analysis below**

## prescription_1

- **C_Euler (finite part):** 1.5707294464844672
- **Overall:** FAIL
- PASS: 7  FAIL: 1  INCONCLUSIVE: 0

| Criterion | Result | Reason |
|---|---|---|
| 1_laurent_fit_quality | PASS | all 4 fits pass; worst R²=0.99999998 |
| 2_epsilon_expansion_smoothness | PASS | residual=2.322580e-05 < 0.0001 |
| 3_prescription_universality | PASS | relative spread=5.3197e-04 <= 0.01: values=['1.570729', '1.569478', '1.570732'] |
| 4_numerical_stability | FAIL | 28 samples exceed error threshold 1e-06: worst=1.90e-01 |
| 5_analytic_continuation | PASS | finite part=1.570729; no singularity indicators |
| 6_blind_protocol_integrity | PASS | Phase C receives prescription_1/2/3 labels only; source field not used in decisions |
| 7_specification_compliance | PASS | Phase A/B/C harnesses cite spec gate3-hminus-direct-limit-spec-v1.0; output files in gate3_dl_outputs/ |
| 8_reproducibility | PASS | Phase A scripts in theory/hard_theory/, Phase B/C in grut/hard_theory/s4_ctp_solver/; outputs committed to gate3_dl_outputs/ |

## prescription_2

- **C_Euler (finite part):** 1.569477814639061
- **Overall:** FAIL
- PASS: 6  FAIL: 2  INCONCLUSIVE: 0

| Criterion | Result | Reason |
|---|---|---|
| 1_laurent_fit_quality | FAIL | 2 fits below R²=0.99999: worst=0.99992059 |
| 2_epsilon_expansion_smoothness | PASS | residual=4.443689e-05 < 0.0001 |
| 3_prescription_universality | PASS | relative spread=5.3197e-04 <= 0.01: values=['1.570729', '1.569478', '1.570732'] |
| 4_numerical_stability | FAIL | 42 samples exceed error threshold 1e-06: worst=2.05e-01 |
| 5_analytic_continuation | PASS | finite part=1.569478; no singularity indicators |
| 6_blind_protocol_integrity | PASS | Phase C receives prescription_1/2/3 labels only; source field not used in decisions |
| 7_specification_compliance | PASS | Phase A/B/C harnesses cite spec gate3-hminus-direct-limit-spec-v1.0; output files in gate3_dl_outputs/ |
| 8_reproducibility | PASS | Phase A scripts in theory/hard_theory/, Phase B/C in grut/hard_theory/s4_ctp_solver/; outputs committed to gate3_dl_outputs/ |

## prescription_3

- **C_Euler (finite part):** 1.5707322699962223
- **Overall:** FAIL
- PASS: 7  FAIL: 1  INCONCLUSIVE: 0

| Criterion | Result | Reason |
|---|---|---|
| 1_laurent_fit_quality | PASS | all 5 fits pass; worst R²=0.99999977 |
| 2_epsilon_expansion_smoothness | PASS | residual=1.760127e-05 < 0.0001 |
| 3_prescription_universality | PASS | relative spread=5.3197e-04 <= 0.01: values=['1.570729', '1.569478', '1.570732'] |
| 4_numerical_stability | FAIL | 25 samples exceed error threshold 1e-06: worst=1.04e-01 |
| 5_analytic_continuation | PASS | finite part=1.570732; no singularity indicators |
| 6_blind_protocol_integrity | PASS | Phase C receives prescription_1/2/3 labels only; source field not used in decisions |
| 7_specification_compliance | PASS | Phase A/B/C harnesses cite spec gate3-hminus-direct-limit-spec-v1.0; output files in gate3_dl_outputs/ |
| 8_reproducibility | PASS | Phase A scripts in theory/hard_theory/, Phase B/C in grut/hard_theory/s4_ctp_solver/; outputs committed to gate3_dl_outputs/ |

## Notes

- Acceptance thresholds: Laurent R² > 0.99999, eps-expansion residual < 0.0001, universality < 1%.
- Criteria 6–8 are structural passes (enforced by harness design).
- Criterion 3 (universality) is evaluated identically for all prescriptions.
- Promotion requires ALL 8 criteria to pass with no INCONCLUSIVEs.

Spec: GATE3_HMINUS_DIRECT_LIMIT_SPEC.md (gate3-hminus-direct-limit-spec-v1.0)