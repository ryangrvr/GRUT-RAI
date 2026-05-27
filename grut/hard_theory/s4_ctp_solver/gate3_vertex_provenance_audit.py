#!/usr/bin/env python3
"""
Gate 3 Vertex Provenance Audit

Determines which CTP action vertex produces the Allen-Jacobson S4 integral:

  I(h_-, eps) = 2 * 4^((D-3)/2) * int_0^1 2F1(D-1, h_-; D/2; u)^3
                * [u(1-u)]^((D-3)/2) du,  D = 4 - 2*eps

with exact seed I(0,0) = 4*B(3/2, 3/2) = pi/2.

This audit addresses Criterion R1 (Operator Source) in the coefficient-role
assignment gate.  It cannot resolve R1 numerically — that requires theoretical
identification of the CTP action term.  What it CAN do:

  1. Compute the projection-factor hypothesis exactly.
  2. Identify the geometric dimensional ladder connecting I(0,0) to R_target.
  3. Score each candidate vertex for structural consistency with I(h_-, eps).
  4. Record the blocking question for R1 in a form ready for theory input.

Projection-factor hypothesis:
  N = C_seed^(3) / R_target = (pi/2) / (2/sqrt(3)) = pi*sqrt(3)/4

Geometric ladder (exact):
  I(0,0) = pi/2 = Vol(S3) / Vol(S2)
  R_target = sqrt(4/3) = sqrt(Vol(S4)/Vol(S3))
  => N = Vol(S3) / (Vol(S2) * sqrt(Vol(S4)/Vol(S3)))

Green-function structural observation:
  The integrand 2F1(D-1, h_-; D/2; u) is the chordal-distance representation
  of the massive scalar propagator on S^D.  The triple product 2F1^3 is
  consistent with a three-point function of such propagators.

Five candidate vertex sources (see GATE3_VERTEX_PROVENANCE_AUDIT.md):
  V1: R log□R nonlocal Euler kernel
  V2: Cosmological/Euler projection term
  V3: Shared S4 Green kernel normalization
  V4: CTP branch-response vertex
  V5: Pure benchmark Allen-Jacobson scalar seed

Current status: R1 = NEEDS_THEORY; role = role_unassigned.

Spec: gate3-vertex-provenance-audit-spec-v1.0
Date: 2026-05-26
"""

import json
import numpy as np
from pathlib import Path
from datetime import datetime
from scipy.special import gamma as sp_gamma

SPEC_VERSION = "gate3-vertex-provenance-audit-spec-v1.0"
SPEC_DATE = "2026-05-26"

PI_OVER_2 = float(np.pi / 2)
R_TARGET = float(np.sqrt(4.0 / 3.0))       # sqrt(4/3) = 2/sqrt(3)
PROJ_FACTOR = PI_OVER_2 / R_TARGET          # pi*sqrt(3)/4


# ── Geometric dimensional ladder ─────────────────────────────────────────────

def sphere_volume(n: int) -> float:
    """
    Volume of unit n-sphere S^n: 2 * pi^((n+1)/2) / Gamma((n+1)/2).

    n=2: 4*pi        (2-sphere)
    n=3: 2*pi^2      (3-sphere)
    n=4: 8*pi^2/3    (4-sphere)
    n=5: pi^3        (5-sphere)
    """
    return 2.0 * float(np.pi ** ((n + 1) / 2.0)) / float(sp_gamma((n + 1) / 2.0))


def compute_geometric_ladder() -> dict:
    """
    Compute the sphere-volume dimensional ladder and confirm the two key
    exact identities connecting C_seed^(3) to R_target.

    Identity 1:  I(0,0) = pi/2 = Vol(S3)/Vol(S2)   [exact: diff < 1e-15]
    Identity 2:  R_target = sqrt(4/3) = sqrt(Vol(S4)/Vol(S3))  [exact]

    Projection factor:
      N = I(0,0) / R_target = pi*sqrt(3)/4           [exact]
      Verification: I(0,0) / N = R_target             [diff < 1e-15]
    """
    vols = {n: sphere_volume(n) for n in range(2, 7)}

    id1_val = vols[3] / vols[2]
    id2_val = float(np.sqrt(vols[4] / vols[3]))
    pf_val  = float(np.pi * np.sqrt(3.0) / 4.0)

    return {
        "sphere_volumes": {f"S{n}": float(v) for n, v in vols.items()},
        "volume_ratios": {
            f"Vol_S{n}_over_S{n-1}": float(vols[n] / vols[n - 1])
            for n in range(3, 7)
        },
        "identity_1_seed": {
            "claim":      "I(0,0) = pi/2 = Vol(S3)/Vol(S2)",
            "I_00":       PI_OVER_2,
            "ratio":      float(id1_val),
            "difference": float(abs(id1_val - PI_OVER_2)),
            "exact":      abs(id1_val - PI_OVER_2) < 1e-14,
        },
        "identity_2_R": {
            "claim":      "R_target = sqrt(4/3) = sqrt(Vol(S4)/Vol(S3))",
            "R_target":   R_TARGET,
            "ratio_sqrt": float(id2_val),
            "difference": float(abs(id2_val - R_TARGET)),
            "exact":      abs(id2_val - R_TARGET) < 1e-14,
        },
        "projection_factor": {
            "N_computed":     float(PROJ_FACTOR),
            "N_exact_form":   "pi*sqrt(3)/4",
            "N_exact_value":  float(pf_val),
            "difference":     float(abs(PROJ_FACTOR - pf_val)),
            "verification":   float(PI_OVER_2 / PROJ_FACTOR),
            "verif_equals_R": abs(PI_OVER_2 / PROJ_FACTOR - R_TARGET) < 1e-14,
            "interpretation": (
                "If C_seed^(3)=pi/2 is quotient-bearing on exactly one side of R, "
                "then the other side must supply a factor of pi*sqrt(3)/4 for "
                "R = sqrt(4/3) to emerge.  If pi/2 cancels (shared normalization), "
                "the projection factor is irrelevant and R comes from other structure."
            ),
        },
    }


# ── Green-function structural observation ────────────────────────────────────

def green_function_observation() -> dict:
    """
    Mathematical observation: the integrand 2F1(D-1, h_-; D/2; u) is the
    chordal-distance spectral function of the massive scalar propagator on
    S^D.

    On S^D with unit radius, the scalar propagator of mass^2 proportional to
    h_- has the form (in chordal distance u = sin^2(d/2)):

      G_h(u) ~ C * 2F1(D-1, h_-; D/2; u)

    with:
      a = D-1  (= 3 at D=4)
      b = h_-  (mass parameter; h_-=0 → massless)
      c = D/2  (= 2 at D=4)

    This matches the AJ integrand exactly.  The triple product 2F1^3 is
    therefore consistent with a three-point function of these propagators on S4.

    At h_- = 0:  2F1(a, 0; c; u) = 1  (series terminates at zeroth term),
    so I(0,0) = 4 * int_0^1 [u(1-u)]^(1/2) du = 4*B(3/2,3/2) = pi/2.

    This structural match does NOT identify the CTP vertex.  It is consistent
    with:
      V3 (shared S4 Green kernel): three propagators in a loop
      V4 (CTP branch-response): three CTP legs with propagator structure
    Both remain NEEDS_THEORY.
    """
    # Verify 2F1(a,0;c;u) = 1 numerically at several points
    from scipy.special import hyp2f1
    test_u = [0.1, 0.3, 0.5, 0.7, 0.9]
    a, c = 3.0, 2.0
    deviations = [abs(hyp2f1(a, 0.0, c, u) - 1.0) for u in test_u]

    return {
        "claim": "2F1(D-1, h_-; D/2; u) = G_h(u) = massive scalar propagator on S^D",
        "parameters_at_D4": {"a": "D-1=3", "b": "h_-", "c": "D/2=2"},
        "massless_limit": {
            "h_minus_to_0": "2F1(a,0;c;u) = 1  (series terminates at n=0)",
            "verification_u_points": test_u,
            "deviations_from_1":   [float(d) for d in deviations],
            "all_pass":            all(d < 1e-14 for d in deviations),
        },
        "triple_product_interpretation": (
            "2F1^3 = three-point function of scalar propagators on S4. "
            "Consistent with V3 (shared Green kernel) and V4 (CTP branch-response). "
            "Not consistent with V1 (R log□R, which is a 2-point kernel)."
        ),
        "ctp_h_minus_interpretation": (
            "In the CTP formalism, h_- parameterizes the branch separation "
            "(h_- = h_+ - h_-).  The AJ parameter h_- in the integrand is "
            "therefore a direct CTP observable, making V4 (branch-response) "
            "a structurally natural candidate."
        ),
    }


# ── Candidate vertex definitions ─────────────────────────────────────────────

CANDIDATE_VERTICES = [
    {
        "id": "V1",
        "name": "R_log_box_R_nonlocal_euler",
        "label": "R log□R nonlocal Euler kernel",
        "description": (
            "A non-local quantum gravity term of the form R log(□/mu^2) R "
            "appearing in the one-loop effective action on curved backgrounds. "
            "On S4 with constant curvature, the box operator has a known "
            "eigenspectrum and the kernel reduces to a Euler-density coefficient."
        ),
        "loop_order": 1,
        "propagator_count_expected": 1,    # 2-point nonlocal kernel
        "s4_compatible": True,
        "triple_2F1_match":             0.15,  # LOW: 2-point structure, not triple product
        "green_fn_consistency":         0.30,  # 2F1 does appear but as 2-pt, not 3-pt
        "s4_topology_fit":              0.90,  # Euler density on S4 is natural
        "prefactor_match":              0.50,  # 1-loop prefactor differs from 4
        "projection_factor_plausibility": 0.20, # log kernel does not produce sqrt(3)
        "role_if_confirmed": "final_coefficient_candidate",
        "theory_input_needed": (
            "Compute the one-loop R log□R coefficient on S4 and verify whether "
            "the spectral function has a 2F1 form with a=D-1, b=h_-, c=D/2. "
            "If YES: check if three such factors appear in the loop diagram."
        ),
    },
    {
        "id": "V2",
        "name": "cosmo_euler_projection",
        "label": "Cosmological/Euler projection term",
        "description": (
            "A three-loop matter correction to the cosmological constant, "
            "projected onto the Euler density via the Gauss-Bonnet identity on S4. "
            "chi(S4)=2 means the Euler density integrates to 16*pi^2. "
            "A three-loop vacuum bubble with matter propagators of the S4 "
            "Green-function form would produce the triple 2F1 structure."
        ),
        "loop_order": 3,
        "propagator_count_expected": 3,    # Three matter propagators in loop
        "s4_compatible": True,
        "triple_2F1_match":             0.55,  # MODERATE: three-loop consistent
        "green_fn_consistency":         0.55,  # Matter propagator on S4 could be 2F1
        "s4_topology_fit":              0.80,  # Euler density on S4 natural
        "prefactor_match":              0.70,  # 3-loop prefactor could give factor 4
        "projection_factor_plausibility": 0.60, # Matter content could introduce sqrt(3)
        "role_if_confirmed": "cosmo_coefficient_candidate",
        "theory_input_needed": (
            "Identify the matter sector generating the three-loop vacuum bubble "
            "in the cosmological branch of the GRUT CTP action.  Verify that the "
            "matter propagator on S4 has the 2F1(D-1, h_-; D/2; u) form.  "
            "Check whether the three-loop prefactor reproduces the factor 4."
        ),
    },
    {
        "id": "V3",
        "name": "shared_s4_green_kernel",
        "label": "Shared S4 Green kernel normalization",
        "description": (
            "The S4 scalar Green function G_h(u) ~ 2F1(D-1, h_-; D/2; u) in "
            "chordal distance u.  A three-point loop built from three such "
            "Green functions on S4 naturally produces I(h_-, eps) = 2*4^((D-3)/2) "
            "* int G^3 * measure du.  As a shared normalization appearing in both "
            "N and D of R=N/D, this vertex cancels in the quotient."
        ),
        "loop_order": 3,
        "propagator_count_expected": 3,    # Three Green functions in triangle diagram
        "s4_compatible": True,
        "triple_2F1_match":             0.95,  # HIGH: exact structural match
        "green_fn_consistency":         1.00,  # IS the Green function by definition
        "s4_topology_fit":              1.00,  # S4 is the defining background
        "prefactor_match":              0.90,  # 4^((D-3)/2) is S4-dimensional factor
        "projection_factor_plausibility": 0.00, # Shared normalization cancels in R
        "role_if_confirmed": "shared_normalization",
        "theory_input_needed": (
            "Verify that the GRUT CTP action uses the S4 scalar Green function as "
            "the propagator on BOTH branches (N and D sides).  If the Green function "
            "appears symmetrically, I(h_-,eps) cancels in R and is a shared normalization. "
            "If asymmetric appearance: could be V4 (branch-response) instead."
        ),
    },
    {
        "id": "V4",
        "name": "ctp_branch_response_vertex",
        "label": "CTP branch-response vertex",
        "description": (
            "In the Schwinger-Keldysh CTP formalism, the branch-response vertex "
            "couples three fields across the two CTP branches: (++) forward, "
            "(+-) cross, (--) backward.  The parameter h_- in I(h_-, eps) "
            "directly parameterizes the CTP branch split (h_- = h_+ - h_-). "
            "A three-point CTP vertex on S4 with massive propagators G_h would "
            "reproduce the triple 2F1 structure and h_-→0 limit."
        ),
        "loop_order": 3,
        "propagator_count_expected": 3,    # Three CTP legs
        "s4_compatible": True,
        "triple_2F1_match":             0.80,  # MODERATE-HIGH: CTP 3-vertex consistent
        "green_fn_consistency":         0.85,  # CTP propagators have 2F1 form on S4
        "s4_topology_fit":              0.70,  # CTP works on any background
        "prefactor_match":              0.70,  # CTP branch factor plausibly gives 4
        "projection_factor_plausibility": 0.50, # Branch asymmetry could introduce sqrt(3)
        "role_if_confirmed": "final_coefficient_candidate",   # or cosmo; R3 determines
        "theory_input_needed": (
            "Identify the specific three-point CTP vertex in the GRUT action that "
            "depends on h_- as a branch-split parameter.  Compute the CTP spectral "
            "function of this vertex on S4 and verify 2F1(D-1,h_-;D/2;u) form.  "
            "Determine whether the vertex appears only in N, only in D, or in both."
        ),
    },
    {
        "id": "V5",
        "name": "benchmark_aj_scalar_seed",
        "label": "Pure benchmark Allen-Jacobson scalar seed",
        "description": (
            "The integral I(h_-, eps) is used as a benchmark scalar seed for the "
            "regularized three-loop S4 computation, without a specific role in the "
            "GRUT CTP action quotient structure.  In this interpretation, pi/2 "
            "validates the extraction route and numerical methodology but enters "
            "neither N nor D in R=N/D."
        ),
        "loop_order": 3,
        "propagator_count_expected": 3,    # By construction
        "s4_compatible": True,
        "triple_2F1_match":             1.00,  # By construction (AJ = triple 2F1)
        "green_fn_consistency":         1.00,  # By construction
        "s4_topology_fit":              1.00,  # By construction
        "prefactor_match":              1.00,  # By construction
        "projection_factor_plausibility": 0.00, # No quotient implication
        "role_if_confirmed": "benchmark_seed",
        "theory_input_needed": (
            "Verify that the Allen-Jacobson S4 integral is NOT a vertex in the GRUT "
            "CTP action — i.e., that it appears only as a test computation for "
            "numerical validation.  If NO CTP vertex matches I(h_-,eps): pi/2 is "
            "a benchmark_seed only."
        ),
    },
]


# ── Vertex scoring ────────────────────────────────────────────────────────────

# Scoring dimensions and weights
SCORE_DIMS = [
    ("triple_2F1_match",    0.35, "Triple 2F1 structural match"),
    ("green_fn_consistency", 0.30, "Green-function form consistency"),
    ("s4_topology_fit",     0.20, "S4 topology/background compatibility"),
    ("prefactor_match",     0.15, "Prefactor 4=2*4^(1/2) naturalness"),
]

NOTE_DIMS = [
    # propagator_count consistency (not in composite — diagnostic only)
    ("propagator_count_expected", 3, "Propagator count vs AJ triple-product"),
    ("projection_factor_plausibility", None, "Projection-factor plausibility (separate track)"),
]


def score_vertex(v: dict) -> dict:
    """
    Compute structural-consistency composite score for one candidate vertex.

    Score dimensions are weighted contributions to a [0,1] composite.
    projection_factor_plausibility is reported separately: it measures whether
    the vertex can contribute to R=sqrt(4/3) rather than cancelling, and is
    a distinct track from structural consistency.

    The propagator-count diagnostic checks how close the expected count is to 3.
    """
    composite = sum(w * v[dim] for dim, w, _ in SCORE_DIMS)

    # Propagator count: distance penalty from 3
    pc = v["propagator_count_expected"]
    pc_score = max(0.0, 1.0 - abs(pc - 3) / 3.0)

    scores = {dim: float(v[dim]) for dim, _, _ in SCORE_DIMS}
    scores["propagator_count_consistency"] = float(pc_score)
    scores["projection_factor_plausibility"] = float(v["projection_factor_plausibility"])
    scores["composite"] = float(composite)

    return scores


def rank_candidates(vertices: list) -> list:
    """Score and rank all candidate vertices by composite score (descending)."""
    scored = []
    for v in vertices:
        scores = score_vertex(v)
        scored.append({**v, "scores": scores})
    scored.sort(key=lambda x: x["scores"]["composite"], reverse=True)
    return scored


# ── Provisional R1 assessment ─────────────────────────────────────────────────

def provisional_r1_assessment(ranked: list) -> dict:
    """
    Report provisional R1 status and what theory input would resolve it.

    Key distinction: structural score ≠ evidence.  V3 and V5 score highest
    on structural consistency because they ARE defined as triple-2F1 structures.
    High structural score is necessary but not sufficient for R1 identification.

    The decisive question is whether I(h_-, eps) appears as a vertex in the
    GRUT CTP action.  That is a theoretical question, not a numerical one.
    """
    top = ranked[0]
    second = ranked[1] if len(ranked) > 1 else None

    margin = (
        top["scores"]["composite"] - second["scores"]["composite"]
        if second else None
    )

    # Candidates that could be quotient-bearing (if confirmed):
    quotient_candidates = [
        v for v in ranked
        if v["role_if_confirmed"] in (
            "final_coefficient_candidate", "cosmo_coefficient_candidate"
        )
    ]
    shared_or_bench = [
        v for v in ranked
        if v["role_if_confirmed"] in ("shared_normalization", "benchmark_seed")
    ]

    return {
        "r1_status":        "NEEDS_THEORY",
        "provisional_role": "role_unassigned",
        "top_by_structural_score": {
            "id":        top["id"],
            "label":     top["label"],
            "composite": float(top["scores"]["composite"]),
            "margin":    float(margin) if margin is not None else None,
            "role_if_confirmed": top["role_if_confirmed"],
        },
        "quotient_bearing_candidates": [
            {"id": v["id"], "label": v["label"],
             "composite": float(v["scores"]["composite"]),
             "role": v["role_if_confirmed"]}
            for v in quotient_candidates
        ],
        "cancelling_candidates": [
            {"id": v["id"], "label": v["label"],
             "composite": float(v["scores"]["composite"]),
             "role": v["role_if_confirmed"]}
            for v in shared_or_bench
        ],
        "key_fork": (
            "V3 (shared_normalization) vs V4 (final_coefficient_candidate): "
            "both have high structural scores.  If V3: pi/2 cancels in R and R "
            "comes from other structure.  If V4: pi/2 enters one side of R and "
            "requires the projection factor N=pi*sqrt(3)/4 on the other side."
        ),
        "blocking_question": (
            "Which vertex in the GRUT CTP action produces the three-loop S4 diagram "
            "with triple 2F1(D-1,h_-;D/2;u) propagators?  Does it appear on both "
            "CTP branches (shared_normalization) or on one branch only (quotient-bearing)?"
        ),
        "what_would_resolve_r1": [
            "Identify the GRUT CTP action term whose Feynman rules on S4 "
            "produce I(h_-, eps) as a loop integral",
            "Determine whether the vertex is common to both CTP branches or "
            "asymmetric between them",
            "If asymmetric: determine which branch (N or D) carries the vertex "
            "to assign final_coefficient_candidate or cosmo_coefficient_candidate",
        ],
    }


# ── Main ──────────────────────────────────────────────────────────────────────

def main():
    print("=" * 80)
    print("Gate 3 Vertex Provenance Audit")
    print(f"Spec: {SPEC_VERSION}")
    print(f"Start: {datetime.now().isoformat()}")
    print("=" * 80)

    repo_root = Path(__file__).resolve().parents[3]

    # Load existing role assignment output
    role_file = (
        repo_root / "theory" / "hard_theory" / "gate3_dl_outputs"
        / "gate3_coefficient_role_assignment.json"
    )
    role_data = {}
    if role_file.exists():
        with open(role_file) as f:
            role_data = json.load(f)
        print(f"\nRole assignment input: {role_file.name}")
        print(f"  current_role:              {role_data.get('current_role')}")
        print(f"  promotion_review_eligible: {role_data.get('promotion_review_eligible')}")

    # ── Geometric ladder ────────────────────────────────────────────────────
    print("\n" + "-" * 60)
    print("1. Geometric dimensional ladder")
    print("-" * 60)
    ladder = compute_geometric_ladder()

    id1 = ladder["identity_1_seed"]
    id2 = ladder["identity_2_R"]
    pf  = ladder["projection_factor"]

    print(f"  Identity 1: I(0,0) = Vol(S3)/Vol(S2)")
    print(f"    Vol(S3)/Vol(S2) = {id1['ratio']:.10f}")
    print(f"    pi/2            = {id1['I_00']:.10f}")
    print(f"    difference      = {id1['difference']:.2e}  exact={id1['exact']}")

    print(f"\n  Identity 2: R_target = sqrt(Vol(S4)/Vol(S3))")
    print(f"    sqrt(V4/V3)  = {id2['ratio_sqrt']:.10f}")
    print(f"    sqrt(4/3)    = {id2['R_target']:.10f}")
    print(f"    difference   = {id2['difference']:.2e}  exact={id2['exact']}")

    print(f"\n  Projection factor N = I(0,0) / R_target")
    print(f"    N = pi*sqrt(3)/4 = {pf['N_exact_value']:.10f}")
    print(f"    Computed         = {pf['N_computed']:.10f}")
    print(f"    Verify I(0,0)/N == R: {pf['verif_equals_R']}")

    # ── Green-function observation ──────────────────────────────────────────
    print("\n" + "-" * 60)
    print("2. Green-function structural observation")
    print("-" * 60)
    gf_obs = green_function_observation()
    ml = gf_obs["massless_limit"]
    print(f"  2F1(D-1, 0; D/2; u) = 1  at h_-=0")
    print(f"  Verification (u={ml['verification_u_points']}):")
    print(f"    deviations from 1: {[f'{d:.2e}' for d in ml['deviations_from_1']]}")
    print(f"    all pass (<1e-14): {ml['all_pass']}")
    print(f"  Triple product: {gf_obs['triple_product_interpretation']}")
    print(f"  CTP context: h_- parameterizes branch split → V4 structurally natural")

    # ── Vertex scoring ──────────────────────────────────────────────────────
    print("\n" + "-" * 60)
    print("3. Candidate vertex structural scores")
    print("-" * 60)
    ranked = rank_candidates(CANDIDATE_VERTICES)

    print(f"  {'Rank':<5} {'ID':<4} {'Composite':>10}  {'Triple 2F1':>10}  "
          f"{'GF-consist':>10}  {'S4-fit':>7}  {'Pfactor':>8}  Role if confirmed")
    print(f"  {'-'*5} {'-'*4} {'-'*10}  {'-'*10}  {'-'*10}  {'-'*7}  {'-'*8}  {'-'*30}")
    for i, v in enumerate(ranked):
        s = v["scores"]
        print(f"  {i+1:<5} {v['id']:<4} {s['composite']:>10.3f}  "
              f"{s['triple_2F1_match']:>10.2f}  "
              f"{s['green_fn_consistency']:>10.2f}  "
              f"{s['s4_topology_fit']:>7.2f}  "
              f"{s['prefactor_match']:>8.2f}  "
              f"{v['role_if_confirmed']}")

    print(f"\n  NOTE: projection_factor_plausibility is a separate track (quotient-bearing?)")
    for v in ranked:
        print(f"    {v['id']}: proj_factor_plausibility = "
              f"{v['scores']['projection_factor_plausibility']:.2f}  "
              f"({v['label'][:45]})")

    # ── Provisional R1 assessment ───────────────────────────────────────────
    print("\n" + "-" * 60)
    print("4. Provisional R1 assessment")
    print("-" * 60)
    prov = provisional_r1_assessment(ranked)
    print(f"  R1 status:        {prov['r1_status']}")
    print(f"  Provisional role: {prov['provisional_role']}")
    print(f"\n  Key fork: {prov['key_fork']}")
    print(f"\n  Blocking question:")
    print(f"    {prov['blocking_question']}")
    print(f"\n  What would resolve R1:")
    for i, s in enumerate(prov["what_would_resolve_r1"], 1):
        print(f"    {i}. {s}")

    # ── Output ──────────────────────────────────────────────────────────────
    out_dir  = repo_root / "theory" / "hard_theory" / "gate3_dl_outputs"
    out_dir.mkdir(exist_ok=True)
    out_file = out_dir / "gate3_vertex_provenance_audit.json"

    output = {
        "spec":                     SPEC_VERSION,
        "spec_date":                SPEC_DATE,
        "date":                     datetime.now().isoformat(),
        "seed_value":               PI_OVER_2,
        "seed_exact":               "pi/2 = 4*B(3/2,3/2)",
        "R_target":                 R_TARGET,
        "R_exact":                  "sqrt(4/3) = 2/sqrt(3)",
        "projection_factor":        float(PROJ_FACTOR),
        "projection_factor_exact":  "pi*sqrt(3)/4",
        "geometric_ladder":         ladder,
        "green_function_observation": gf_obs,
        "candidate_vertices_ranked": [
            {k: v for k, v in c.items() if k != "description"}
            for c in ranked
        ],
        "candidate_descriptions": {
            c["id"]: c["description"] for c in CANDIDATE_VERTICES
        },
        "provisional_r1_assessment": prov,
        "current_role":             "role_unassigned",
        "r1_status":                "NEEDS_THEORY",
    }

    with open(out_file, "w") as f:
        json.dump(output, f, indent=2, default=str)

    print(f"\nOutput: {out_file}")
    print("=" * 80)
    print(f"End: {datetime.now().isoformat()}")
    print("=" * 80)


if __name__ == "__main__":
    main()
