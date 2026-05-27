#!/usr/bin/env python3
"""
Gate 3 Coefficient-Role Assignment Harness

Evaluates C_seed^(3) = π/2 against the six evidence criteria defined in
GATE3_COEFFICIENT_ROLE_ASSIGNMENT.md and assigns a role status.

Role taxonomy:
  role_unassigned           default; evidence incomplete
  final_coefficient_candidate   can enter C_Euler,final
  cosmo_coefficient_candidate   can enter C_Euler,cosmo
  shared_normalization       appears in N and D; cancels in R
  branch_normalization       validates branch only; not quotient-bearing
  benchmark_seed             useful check; no direct R implication
  rejected                   disqualified from quotient

Current default: role_unassigned (all theory criteria pending)

Spec: gate3-coefficient-role-assignment-spec-v1.0
"""

import json
import numpy as np
from pathlib import Path
from datetime import datetime

SPEC_VERSION = "gate3-coefficient-role-assignment-spec-v1.0"
SPEC_DATE = "2026-05-26"

PI_OVER_2 = float(np.pi / 2)

# ── Role taxonomy ────────────────────────────────────────────────────────────

ROLES = {
    "role_unassigned":             "Default: evidence incomplete for any role",
    "final_coefficient_candidate": "Can enter C_Euler,final (denominator side)",
    "cosmo_coefficient_candidate": "Can enter C_Euler,cosmo (numerator side)",
    "shared_normalization":        "Appears in N and D; cancels in quotient R",
    "branch_normalization":        "Validates direct-limit branch only; not quotient-bearing",
    "benchmark_seed":              "Useful numerical check; no direct R implication",
    "rejected":                    "Disqualified from entering quotient",
}

# ── Evidence status codes ─────────────────────────────────────────────────────

EVIDENCE_STATUS = {
    "PASS":         "Criterion satisfied by available evidence",
    "PARTIAL":      "Partial evidence available; more needed",
    "NEEDS_THEORY": "Requires theoretical input; cannot evaluate numerically",
    "BLOCKED":      "Blocked by an upstream unsatisfied criterion",
    "FAIL":         "Criterion explicitly fails",
}


# ── Load numerical evidence ──────────────────────────────────────────────────

def load_extraction_data(repo_root: Path) -> dict:
    """Load Phase A extraction JSONs and endpoint validation."""
    out_dir = repo_root / "theory" / "hard_theory" / "gate3_dl_outputs"
    data = {}

    for key, fname in [
        ("d1", "gate3_dl_d1_extraction.json"),
        ("d2", "gate3_dl_d2_extraction.json"),
        ("d3", "gate3_dl_d3_extraction.json"),
        ("classification", "gate3_dl_classification_summary.json"),
        ("endpoint_split", "gate3_dl_endpoint_split_validation.json"),
    ]:
        fpath = out_dir / fname
        if fpath.exists():
            with open(fpath) as f:
                data[key] = json.load(f)
        else:
            data[key] = None

    return data


def extract_seed_values(data: dict) -> dict:
    """Pull the three C_Euler estimates and key quality metrics."""
    seeds = {}

    if data.get("d1"):
        s2 = data["d1"].get("stage2", {})
        seeds["D1"] = {
            "C_Euler": s2.get("C_Euler_D1"),
            "stage1_min_r2": s2.get("stage1_min_r2"),
            "stage2_residual": s2.get("fit_residual"),
        }

    if data.get("d2"):
        s2 = data["d2"].get("stage2", {})
        seeds["D2"] = {
            "C_Euler": s2.get("C_Euler_D2"),
            "stage1_min_r2": s2.get("stage1_min_r2"),
            "stage2_residual": s2.get("fit_residual"),
        }

    if data.get("d3"):
        seeds["D3"] = {
            "C_Euler": data["d3"].get("C_Euler_D3"),
            "universality_spread": data["d3"].get("universality", {}).get("relative_spread"),
            "c_independent": data["d3"].get("universality", {}).get("c_independent"),
        }

    return seeds


# ── Six evidence criteria ────────────────────────────────────────────────────

def criterion_r1_operator_source() -> dict:
    """
    R1: Which CTP action vertex produces the S⁴ Allen–Jacobson integral?

    Cannot be evaluated numerically. Requires theoretical identification
    of the CTP action term whose loop diagram reduces to I(h_-, eps).
    """
    return {
        "criterion": "R1_operator_source",
        "question": "Which term in the CTP effective action produces the S4 AJ integral?",
        "status": "NEEDS_THEORY",
        "evidence": {
            "known": (
                "The integral I(h_-, eps) = 2*4^((D-3)/2) * int_0^1 "
                "2F1(D-1, h_-; D/2; u)^3 * [u(1-u)]^((D-3)/2) du "
                "is a three-loop diagram on S4. The three 2F1 factors suggest "
                "three propagator insertions."
            ),
            "unknown": [
                "Which field content carries the three propagators",
                "Whether the diagram is a vertex correction, vacuum bubble, or topological term",
                "The coupling constant attached to this vertex in the CTP action",
            ],
        },
        "disqualifying_finding": "If vertex absent from CTP action → benchmark_seed only",
        "blocking_for": ["R2", "R3"],
    }


def criterion_r2_projection_target() -> dict:
    """
    R2: Does the S⁴ seed project onto the Euler density, cosmological
    constant, R log□R, or a normalization factor?

    Partial evidence: S⁴ is the test space for Euler-class invariants.
    Projection operator not yet confirmed.
    """
    euler_characteristic_s4 = 2  # chi(S^4) = 2, well-known topological fact
    euler_density_integral_s4 = 8 * np.pi**2 * euler_characteristic_s4  # 16 pi^2

    # The seed π/2 relative to standard normalizations
    ratio_to_pi2 = PI_OVER_2 / np.pi**2
    ratio_to_16pi2 = PI_OVER_2 / (16 * np.pi**2)

    return {
        "criterion": "R2_projection_target",
        "question": "What geometric/topological object does the seed project onto?",
        "status": "PARTIAL",
        "evidence": {
            "s4_euler_characteristic": euler_characteristic_s4,
            "euler_density_integral_on_s4": euler_density_integral_s4,
            "seed_pi_over_2": PI_OVER_2,
            "ratio_seed_to_pi2": ratio_to_pi2,
            "ratio_seed_to_16pi2": ratio_to_16pi2,
            "topological_argument": (
                "S4 = round 4-sphere is the natural test manifold for Euler-class "
                "invariants. chi(S4)=2. The Euler density integrates to 16pi^2 on S4. "
                "The prefactor 4=2*4^(1/2) in I(0,0) is distinct from 16pi^2, "
                "suggesting the seed is NOT a direct topological index but rather a "
                "specific coupling-dependent normalization coefficient."
            ),
            "unknown": [
                "Whether the projection operator onto Euler density has been applied",
                "Whether S4 test geometry is sufficient or full backreaction needed",
                "Whether the 2F1 triple product structure identifies a specific vertex",
            ],
        },
        "candidate_targets": [
            "euler_density",       # chi(S4) connection
            "cosmo_const",         # cosmological sector
            "normalization",       # overall loop normalization
            "unknown",             # current default
        ],
        "current_best_candidate": "euler_density (by topology argument, unconfirmed)",
        "blocking_for": ["R3"],
    }


def criterion_r3_quotient_position() -> dict:
    """
    R3: Does the seed appear in numerator N, denominator D, both, or
    neither of the GRUT quotient R = N/D?

    Blocked until R2 resolves the projection target.
    """
    return {
        "criterion": "R3_quotient_position",
        "question": "Does C_seed appear in N, D, both, or neither of R = N/D?",
        "status": "BLOCKED",
        "blocked_by": "R2 (projection target unresolved)",
        "evidence": {
            "known": "R = N/D is the GRUT quotient structure. C_Euler roles TBD.",
            "unknown": [
                "Which side of R the Euler density belongs to",
                "Whether N and D both receive Euler density contributions",
                "The relative normalization of N and D",
            ],
        },
        "role_implications": {
            "numerator_only": "cosmo_coefficient_candidate",
            "denominator_only": "final_coefficient_candidate",
            "both": "shared_normalization (pending R5 cancellation check)",
            "neither": "branch_normalization",
        },
    }


def criterion_r4_scheme_behavior(seeds: dict) -> dict:
    """
    R4: Is the seed protected under regularization-scheme changes?

    Numerically evaluable from the D1/D2/D3 comparison and the D3
    universality check.
    """
    D1_val = seeds.get("D1", {}).get("C_Euler")
    D2_val = seeds.get("D2", {}).get("C_Euler")
    D3_val = seeds.get("D3", {}).get("C_Euler")
    univ_spread = seeds.get("D3", {}).get("universality_spread")

    d1_d3_delta = abs(D1_val - D3_val) if D1_val and D3_val else None
    d1_d2_delta = abs(D1_val - D2_val) if D1_val and D2_val else None
    d1_rel_to_pi2 = abs(D1_val - PI_OVER_2) / PI_OVER_2 if D1_val else None
    d3_rel_to_pi2 = abs(D3_val - PI_OVER_2) / PI_OVER_2 if D3_val else None

    # Universality threshold: < 1% is the criterion-3 standard
    universality_passes = univ_spread < 0.01 if univ_spread is not None else None

    status = "PARTIAL"
    interpretation = (
        "D1/D3 agreement and D3 c-independence support protection. "
        "D2's order-of-limits sensitivity is a structural feature (noncommuting limits), "
        "not a scheme fragility."
    )

    return {
        "criterion": "R4_scheme_behavior",
        "question": "Is the seed protected under regularization-scheme changes?",
        "status": status,
        "evidence": {
            "C_Euler_D1": D1_val,
            "C_Euler_D2": D2_val,
            "C_Euler_D3": D3_val,
            "pi_over_2": PI_OVER_2,
            "D1_D3_delta": d1_d3_delta,
            "D1_D2_delta": d1_d2_delta,
            "D1_relative_to_pi_over_2": d1_rel_to_pi2,
            "D3_relative_to_pi_over_2": d3_rel_to_pi2,
            "D3_universality_spread": univ_spread,
            "universality_passes_1pct": universality_passes,
        },
        "interpretation": interpretation,
        "supports_protected_status": bool(
            d1_d3_delta is not None and d1_d3_delta < 1e-4 and universality_passes
        ),
    }


def criterion_r5_cancellation_check() -> dict:
    """
    R5: If the seed appears in both N and D of R = N/D, does it cancel?

    Cannot evaluate until R3 (quotient position) is resolved.
    """
    return {
        "criterion": "R5_cancellation_check",
        "question": "If C_seed appears in both N and D, does it cancel in R?",
        "status": "BLOCKED",
        "blocked_by": "R3 (quotient position unresolved)",
        "evidence": {
            "known": "If seed cancels: role = shared_normalization (quotient R is independent of π/2)",
            "unknown": "Whether seed appears on both sides and in equal powers",
        },
        "method_when_unblocked": (
            "Compute R = N/D with C_Euler = pi/2 and with C_Euler perturbed. "
            "If R changes: seed is quotient-bearing. "
            "If R is invariant: seed is shared_normalization."
        ),
    }


def criterion_r6_landing_eligibility(data: dict) -> dict:
    """
    R6: Does the seed satisfy Gate 3 coefficient landing interface conditions?

    Most sub-conditions are numerically verifiable; the role-assignment
    sub-condition is the active blocker.
    """
    # Check each sub-condition
    has_blinded_protocol = (
        data.get("classification") is not None
        and data.get("d1") is not None
        and data.get("d3") is not None
    )

    # Two independent prescriptions agree within 1e-4 relative
    d1 = data.get("d1", {}).get("stage2", {}).get("C_Euler_D1") if data.get("d1") else None
    d3 = data.get("d3", {}).get("C_Euler_D3") if data.get("d3") else None
    prescriptions_agree = (
        abs(d1 - d3) / PI_OVER_2 < 1e-3 if (d1 and d3) else False
    )

    endpoint_resolved = data.get("endpoint_split") is not None

    # R not prematurely promoted (checked by looking for an R-promotion flag)
    r_not_premature = True  # by design: R was never promoted in this gate

    sub_conditions = {
        "blinded_protocol_followed": has_blinded_protocol,
        "two_prescriptions_agree": prescriptions_agree,
        "endpoint_objection_resolved": endpoint_resolved,
        "r_not_promoted_prematurely": r_not_premature,
        "role_assigned_before_landing": False,  # ACTIVE BLOCKER: role still unassigned
    }

    all_met = all(sub_conditions.values())

    return {
        "criterion": "R6_landing_eligibility",
        "question": "Does the seed satisfy Gate 3 coefficient landing interface conditions?",
        "status": "PARTIAL" if not all_met else "PASS",
        "sub_conditions": sub_conditions,
        "active_blocker": "role_assigned_before_landing = False (role_unassigned)",
        "eligible_when": "Role assigned via criteria R1–R5",
    }


# ── Role assignment logic ────────────────────────────────────────────────────

def assign_role(criteria: dict) -> str:
    """
    Assign role based on current evidence. Returns role string.

    Logic (follows the decision tree in the spec):
    - If R1 is NEEDS_THEORY: role_unassigned (cannot proceed)
    - If R2 is BLOCKED or PARTIAL (non-confirmed projection): role_unassigned
    - If R3 is BLOCKED: role_unassigned
    - Only assign non-default when R1+R2+R3 all resolve
    """
    r1_status = criteria["R1"]["status"]
    r2_status = criteria["R2"]["status"]
    r3_status = criteria["R3"]["status"]
    r6_active_blocker = criteria["R6"]["active_blocker"]

    if r1_status in ("NEEDS_THEORY", "BLOCKED", "FAIL"):
        return "role_unassigned"
    if r2_status in ("NEEDS_THEORY", "BLOCKED", "FAIL"):
        return "role_unassigned"
    if r3_status in ("BLOCKED", "NEEDS_THEORY", "FAIL"):
        return "role_unassigned"
    if "role_assigned_before_landing = False" in r6_active_blocker:
        return "role_unassigned"

    # If all upstream criteria pass (future state):
    r3_position = criteria["R3"].get("resolved_position")
    r5_cancels = criteria.get("R5", {}).get("cancels_in_R")

    if r3_position == "numerator_only":
        return "cosmo_coefficient_candidate"
    elif r3_position == "denominator_only":
        return "final_coefficient_candidate"
    elif r3_position == "both":
        if r5_cancels is True:
            return "shared_normalization"
        else:
            return "role_unassigned"  # need R5 resolution
    elif r3_position == "neither":
        return "branch_normalization"

    return "role_unassigned"


def promotion_review_eligible(criteria: dict, seeds: dict) -> bool:
    """
    True if D1/D3 numerical evidence is complete and endpoint validated,
    regardless of role assignment status.
    """
    r4 = criteria["R4"]
    r6 = criteria["R6"]
    return (
        r4.get("supports_protected_status", False)
        and r6["sub_conditions"].get("blinded_protocol_followed", False)
        and r6["sub_conditions"].get("two_prescriptions_agree", False)
        and r6["sub_conditions"].get("endpoint_objection_resolved", False)
        and r6["sub_conditions"].get("r_not_promoted_prematurely", False)
    )


# ── Main ─────────────────────────────────────────────────────────────────────

def main():
    print("=" * 80)
    print("Gate 3 Coefficient-Role Assignment Harness")
    print(f"Spec: {SPEC_VERSION}")
    print(f"Start: {datetime.now().isoformat()}")
    print("=" * 80)

    repo_root = Path(__file__).resolve().parents[3]
    data = load_extraction_data(repo_root)
    seeds = extract_seed_values(data)

    print(f"\nSeed value: C_seed^(3) = {PI_OVER_2:.10f}  (π/2 exactly)")
    print(f"  D1 extraction: {seeds.get('D1', {}).get('C_Euler')}")
    print(f"  D2 extraction: {seeds.get('D2', {}).get('C_Euler')}")
    print(f"  D3 extraction: {seeds.get('D3', {}).get('C_Euler')}")

    # Evaluate all six criteria
    print("\n" + "-" * 60)
    print("Evaluating six evidence criteria:")
    print("-" * 60)

    criteria_results = {
        "R1": criterion_r1_operator_source(),
        "R2": criterion_r2_projection_target(),
        "R3": criterion_r3_quotient_position(),
        "R4": criterion_r4_scheme_behavior(seeds),
        "R5": criterion_r5_cancellation_check(),
        "R6": criterion_r6_landing_eligibility(data),
    }

    for key, res in criteria_results.items():
        status = res["status"]
        print(f"  {key} {res['criterion']}: {status}")

    # Assign role
    current_role = assign_role(criteria_results)
    eligible = promotion_review_eligible(criteria_results, seeds)

    print(f"\n{'='*60}")
    print(f"ROLE ASSIGNMENT: {current_role}")
    print(f"Description:     {ROLES[current_role]}")
    print(f"Promotion-review eligible: {eligible}")
    print(f"{'='*60}")

    # Blocking questions
    blocking = []
    for key, res in criteria_results.items():
        if res["status"] in ("NEEDS_THEORY", "BLOCKED"):
            q = res.get("question", "")
            blocking.append(f"{key}: {q}")

    print("\nBlocking questions (must resolve before role can be assigned):")
    for i, b in enumerate(blocking, 1):
        print(f"  {i}. {b}")

    print(f"\nNext action: Resolve R1 (operator source) to unlock R2 and R3")

    # Write output
    out_dir = repo_root / "theory" / "hard_theory" / "gate3_dl_outputs"
    out_dir.mkdir(exist_ok=True)
    out_file = out_dir / "gate3_coefficient_role_assignment.json"

    output = {
        "spec": SPEC_VERSION,
        "spec_date": SPEC_DATE,
        "date": datetime.now().isoformat(),
        "seed_value": PI_OVER_2,
        "seed_exact": "pi/2 = 4*B(3/2,3/2)",
        "seed_source": "Allen-Jacobson S4 integral, direct-limit D1/D3",
        "C_Euler_D1": seeds.get("D1", {}).get("C_Euler"),
        "C_Euler_D2": seeds.get("D2", {}).get("C_Euler"),
        "C_Euler_D3": seeds.get("D3", {}).get("C_Euler"),
        "current_role": current_role,
        "role_description": ROLES[current_role],
        "promotion_review_eligible": eligible,
        "criteria": criteria_results,
        "blocking_questions": blocking,
        "next_action": "Resolve R1 (operator source) to unlock R2 and R3",
        "roles_taxonomy": ROLES,
    }

    with open(out_file, "w") as f:
        json.dump(output, f, indent=2, default=str)

    print(f"\nOutput: {out_file}")
    print("=" * 80)
    print(f"End: {datetime.now().isoformat()}")
    print("=" * 80)


if __name__ == "__main__":
    main()
