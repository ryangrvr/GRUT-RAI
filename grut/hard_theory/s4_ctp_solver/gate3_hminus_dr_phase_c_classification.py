#!/usr/bin/env python3
"""
Gate 3 Hminus-Derivative-Regularized Phase C: Classification Harness

Purpose: Read Phase B prescription coefficients and classify each candidate
         against the eight acceptance criteria defined in the specification.

Specification version: gate3-hminus-dr-spec-v1.0
Date: May 15, 2026

Outputs:
- gate3_hminus_dr_classification_report.md
"""

import json
import sys
from pathlib import Path
from datetime import datetime
from typing import Dict, Any


def log(msg: str):
    print(f"[{datetime.now().isoformat()}] {msg}")


def load_json(path: Path) -> Dict[str, Any]:
    with open(path, 'r') as f:
        return json.load(f)


def safe_float(value: Any) -> float:
    try:
        return float(value)
    except Exception:
        return float('nan')


def passes_finiteness(prescription: Dict[str, Any]) -> Dict[str, Any]:
    finite = safe_float(prescription.get('epsilon_to_0_finite'))
    pole = safe_float(prescription.get('epsilon_to_0_pole'))
    
    if not (finite == finite):
        return {'result': 'FAIL', 'reason': 'finite part is NaN or not numeric'}
    if not (pole == pole):
        return {'result': 'FAIL', 'reason': 'pole part is NaN or not numeric'}
    if abs(pole) > 1e-6 * max(abs(finite), 1.0):
        return {'result': 'FAIL', 'reason': f'non-negligible pole term ({pole}) relative to finite part ({finite})'}
    return {'result': 'PASS', 'reason': f'finite={finite}, pole={pole}'}


def passes_pole_characterization(prescription: Dict[str, Any]) -> Dict[str, Any]:
    if prescription.get('status') == 'failed':
        return {'result': 'FAIL', 'reason': 'prescription failed during application'}
    if 'a0_samples' in prescription or 'a1_samples' in prescription or 'a2_samples' in prescription:
        return {'result': 'PASS', 'reason': 'sample set available for pole characterization'}
    return {'result': 'INCONCLUSIVE', 'reason': 'insufficient pole fit metadata'}


def passes_epsilon_expansion(prescription: Dict[str, Any]) -> Dict[str, Any]:
    fit_residual = safe_float(prescription.get('fit_residual'))
    if fit_residual != fit_residual:
        return {'result': 'INCONCLUSIVE', 'reason': 'no fit residual information'}
    if fit_residual < 1e-4:
        return {'result': 'PASS', 'reason': f'fit_residual={fit_residual}'}
    return {'result': 'FAIL', 'reason': f'fit_residual too large ({fit_residual})'}


def passes_universality_check(prescription: Dict[str, Any]) -> Dict[str, Any]:
    return {'result': 'INCONCLUSIVE', 'reason': 'no universality comparison data available'}


def passes_known_limit_consistency(prescription: Dict[str, Any]) -> Dict[str, Any]:
    if prescription.get('known_limit_match') is not None:
        return {'result': 'PASS' if prescription.get('known_limit_match') else 'FAIL',
                'reason': 'known-limit comparison available'}
    return {'result': 'INCONCLUSIVE', 'reason': 'no known-limit comparison provided'}


def passes_sign_scale(prescription: Dict[str, Any]) -> Dict[str, Any]:
    finite = safe_float(prescription.get('epsilon_to_0_finite'))
    if abs(finite) == float('inf') or finite != finite:
        return {'result': 'FAIL', 'reason': 'finite part is infinite or NaN'}
    if abs(finite) > 1e12:
        return {'result': 'FAIL', 'reason': f'value too large: {finite}'}
    if abs(finite) < 1e-12:
        return {'result': 'FAIL', 'reason': f'value too small: {finite}'}
    return {'result': 'PASS', 'reason': f'value={finite}'}


def passes_stability(prescription: Dict[str, Any]) -> Dict[str, Any]:
    samples = prescription.get('a0_samples') or prescription.get('a1_samples') or prescription.get('a2_samples')
    if not isinstance(samples, list) or len(samples) < 2:
        return {'result': 'INCONCLUSIVE', 'reason': 'insufficient sample data for stability check'}
    try:
        values = [safe_float(val) for _, val in samples]
        if any(v != v for v in values):
            return {'result': 'FAIL', 'reason': 'NaN in sample values'}
        ratio = max(values) / min(values) if min(values) != 0 else float('inf')
        if ratio > 10:
            return {'result': 'FAIL', 'reason': f'large variation across epsilon samples (ratio={ratio})'}
        return {'result': 'PASS', 'reason': f'variation ratio={ratio}'}
    except Exception as e:
        return {'result': 'INCONCLUSIVE', 'reason': f'stability check exception: {e}'}


def passes_endpoint_singularity(prescription: Dict[str, Any]) -> Dict[str, Any]:
    if prescription.get('endpoint_warnings') is not None:
        if prescription['endpoint_warnings']:
            return {'result': 'FAIL', 'reason': 'endpoint warnings reported'}
        return {'result': 'PASS', 'reason': 'no endpoint warnings reported'}
    return {'result': 'INCONCLUSIVE', 'reason': 'no endpoint warning metadata available'}


def classify_prescription(label: str, prescription: Dict[str, Any]) -> Dict[str, Any]:
    results = {
        'finiteness': passes_finiteness(prescription),
        'pole_characterization': passes_pole_characterization(prescription),
        'epsilon_expansion': passes_epsilon_expansion(prescription),
        'universality_check': passes_universality_check(prescription),
        'known_limit_consistency': passes_known_limit_consistency(prescription),
        'sign_and_scale': passes_sign_scale(prescription),
        'stability': passes_stability(prescription),
        'endpoint_singularity_absence': passes_endpoint_singularity(prescription),
    }
    
    pass_count = sum(1 for r in results.values() if r['result'] == 'PASS')
    fail_count = sum(1 for r in results.values() if r['result'] == 'FAIL')
    inconclusive_count = sum(1 for r in results.values() if r['result'] == 'INCONCLUSIVE')
    
    overall = 'PASS' if fail_count == 0 and inconclusive_count == 0 else ('INCONCLUSIVE' if fail_count == 0 else 'FAIL')
    
    return {
        'prescription_label': label,
        'overall': overall,
        'pass_count': pass_count,
        'fail_count': fail_count,
        'inconclusive_count': inconclusive_count,
        'criteria': results
    }


def write_report(report_path: Path, extraction_data: Dict[str, Any], classification: Dict[str, Any]):
    lines = [
        '# Gate 3 Hminus-Derivative-Regularized Classification Report',
        '',
        f'Date: {datetime.now().isoformat()}',
        f'Spec version: {extraction_data.get("spec_version", "unknown")}',
        '',
        '## Summary',
        ''
    ]
    
    for label, result in classification.items():
        lines.append(f'### {label}')
        lines.append('')
        lines.append(f'- overall: {result["overall"]}')
        lines.append(f'- pass_count: {result["pass_count"]}')
        lines.append(f'- fail_count: {result["fail_count"]}')
        lines.append(f'- inconclusive_count: {result["inconclusive_count"]}')
        lines.append('')
        lines.append('| Criterion | Result | Reason |')
        lines.append('|---|---|---|')
        for criterion, detail in result['criteria'].items():
            lines.append(f'| {criterion} | {detail["result"]} | {detail["reason"]} |')
        lines.append('')

    lines.append('## Notes')
    lines.append('')
    lines.append('- Classification is based on available Phase B output fields.')
    lines.append('- Universality and known-limit checks are inconclusive unless explicit data is provided.')
    lines.append('- Endpoint singularity absence is inconclusive unless warnings metadata is available.')
    lines.append('')
    
    report_path.write_text('\n'.join(lines))


def main():
    log("=" * 80)
    log("Gate 3 Phase C: Classification Harness")
    log("Specification: gate3-hminus-dr-spec-v1.0")
    log("=" * 80)

    repository_root = Path(__file__).resolve().parents[3]
    base_dir = repository_root / "theory" / "hard_theory" / "gate3_outputs"
    pres_file = base_dir / "gate3_hminus_dr_prescription_coefficients.json"
    report_file = base_dir / "gate3_hminus_dr_classification_report.md"

    if not pres_file.exists():
        log(f"ERROR: Prescription coefficients file not found: {pres_file}")
        sys.exit(1)

    log(f"Loading prescription data from: {pres_file}")
    pres_data = load_json(pres_file)
    extraction_data = {'spec_version': pres_data.get('spec_version', 'unknown')}

    prescriptions = pres_data.get('prescriptions', {})
    classification = {}
    
    for label, prescription in prescriptions.items():
        classification[label] = classify_prescription(label, prescription)
        log(f"Classified {label}: {classification[label]['overall']} ({classification[label]['pass_count']} passes, {classification[label]['fail_count']} fails, {classification[label]['inconclusive_count']} inconclusive)")
    
    write_report(report_file, extraction_data, classification)
    log(f"Report written to: {report_file}")
    log("=" * 80)
    log("Phase C COMPLETE")
    log("Specification: gate3-hminus-dr-spec-v1.0")
    log(f"Output: {report_file}")
    log("=" * 80)


if __name__ == '__main__':
    main()
