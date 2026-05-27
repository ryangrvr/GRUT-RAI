#!/usr/bin/env python3
"""
Gate 3 CTP Branch-Incidence Audit

Determines whether the three-point S4 scalar loop (the Allen-Jacobson integral)
appears symmetrically on both CTP branches or asymmetrically in a response/
projection channel.  This distinguishes the two highest-scoring candidates from
the vertex provenance audit:

  V3 (shared_normalization):  loop appears identically on both CTP branches
  V4 (final_coefficient_candidate): loop appears on one branch only, or
     asymmetrically with unequal projection weights

Method:
  1. Keldysh-basis analysis — exact 2x2 rotation matrix, then 3-point tensor
  2. CTP causality check — does V_aaa = 0 for each topology?
  3. r/a classification — noise (V_rrr) vs response (V_rra etc.)
  4. Euclidean S4 finding — all CTP propagator components equal on compact S4
  5. Sector-asymmetry analysis — can N/D sector difference produce R = sqrt(4/3)?
  6. Decision table — maps each finding to a role assignment

Key finding:
  On Euclidean S4, all CTP propagator components G^{++} = G^{--} = G^{+-} = G^{-+}
  because the spectrum is real and discrete (no Lorentzian time ordering).
  Therefore I(h_-, eps) appears SYMMETRICALLY on both branches — SYM topology.
  The SYM topology is the ONLY three-point loop topology that satisfies CTP
  causality (V_aaa = 0) for a constant-propagator background.

  This supports V3 (shared_normalization) and disfavors V4 (branch-response)
  on the basis of CTP structure alone.

  IF the GRUT quotient R = N/D has R != 1, the asymmetry must come from
  sector-level differences (different field content or coupling in N vs D),
  NOT from CTP branch topology alone.  In that case, pi/2 CANCELS in R as a
  shared normalization, and the physics of R comes from the sector prefactors.

Spec: gate3-ctp-branch-incidence-spec-v1.0
Date: 2026-05-26
"""

import json
import numpy as np
from pathlib import Path
from datetime import datetime

SPEC_VERSION = "gate3-ctp-branch-incidence-spec-v1.0"
SPEC_DATE = "2026-05-26"

PI_OVER_2 = float(np.pi / 2)
R_TARGET  = float(np.sqrt(4.0 / 3.0))
PROJ_FACTOR = PI_OVER_2 / R_TARGET          # pi*sqrt(3)/4


# ── Keldysh-basis machinery ──────────────────────────────────────────────────

def keldysh_rotation() -> dict:
    """
    The 2x2 Keldysh (r/a) rotation matrix.

    Convention:
      phi_r = (phi+ + phi-) / 2     (classical / retarded component)
      phi_a = phi+ - phi-            (quantum / advanced component)

    Matrix R with R[row, col] encoding (r or a) from (+ or -):
      R = [[1/2,  1/2],   row r
           [1,   -1  ]]   row a

    det(R) = -1.  The 'a' row is the discrete derivative (alternating sum).
    """
    R = np.array([[0.5, 0.5], [1.0, -1.0]])
    return {
        "R":         R,
        "det":       float(np.linalg.det(R)),
        "R_r_plus":  float(R[0, 0]),    # r-component from +
        "R_r_minus": float(R[0, 1]),    # r-component from -
        "R_a_plus":  float(R[1, 0]),    # a-component from +
        "R_a_minus": float(R[1, 1]),    # a-component from -
    }


def ctp_causality_check(I_pm: np.ndarray, R: np.ndarray) -> dict:
    """
    CTP causality constraint: V_aaa = 0 for any physical loop in the
    Schwinger-Keldysh effective action.

    This is equivalent to the discrete alternating sum over all +/- index
    combinations vanishing:
      V_aaa = Σ_{i,j,k} (-1)^(i+j+k) I[i,j,k] = 0
    (using 0=+, 1=-, so (-1)^{i+j+k} = R[a,i]*R[a,j]*R[a,k] / (R[a,+])^3 )

    Physical interpretation: V_aaa = 0 is a consequence of CTP normalization
    Z[J+, J+] = 1 (closed path returns to initial state).  It holds for all
    physical observables to all orders in perturbation theory.
    """
    I_ra = np.einsum('pi,qj,rk,ijk->pqr', R, R, R, I_pm)
    V_aaa = float(I_ra[1, 1, 1])
    return {
        "V_aaa":    V_aaa,
        "passes":   abs(V_aaa) < 1e-10,
        "I_ra":     I_ra,
    }


def ra_components(I_pm: np.ndarray, R: np.ndarray) -> dict:
    """
    Compute all 8 r/a components for a given +/- loop topology.
    Label r=0, a=1.
    """
    I_ra = np.einsum('pi,qj,rk,ijk->pqr', R, R, R, I_pm)
    labels = ['r', 'a']
    result = {}
    for p in range(2):
        for q in range(2):
            for r in range(2):
                key = f"V_{labels[p]}{labels[q]}{labels[r]}"
                result[key] = float(I_ra[p, q, r])
    return result


# ── CTP loop topology definitions ────────────────────────────────────────────

def topology_sym() -> tuple:
    """
    SYM: All I[i,j,k] = 1.

    Physical meaning: Euclidean S4 where G^{++}=G^{--}=G^{+-}=G^{-+}=G_E.
    The loop is IDENTICAL on both CTP branches.  This is the rigorous result
    for a compact Euclidean background with real discrete spectrum.
    """
    I = np.ones((2, 2, 2))
    return I, {
        "id":          "SYM",
        "name":        "Symmetric (Euclidean S4)",
        "description": (
            "All eight +/- index combinations are equal.  "
            "Arises on Euclidean S4: real discrete spectrum → G^{++}=G^{--}=G^{+-}=G^{-+}."
        ),
        "physical_scenario": "Compact Euclidean S4 background, no Lorentzian time ordering",
        "role_implication":  "shared_normalization — loop cancels in R=N/D",
    }


def topology_antisym() -> tuple:
    """
    ANTISYM: I[+,+,+]=1, I[-,-,-]=-1, rest 0.

    Physical meaning: the loop amplitude changes sign under CTP branch exchange.
    This would arise if the CTP action assigns opposite signs to the two branches
    without mixing.
    """
    I = np.zeros((2, 2, 2))
    I[0, 0, 0] = 1.0    # +++
    I[1, 1, 1] = -1.0   # ---
    return I, {
        "id":          "ANTISYM",
        "name":        "Antisymmetric (branch sign flip)",
        "description": (
            "I[+,+,+] = +1, I[-,-,-] = -1.  "
            "Would arise if the CTP action assigns opposite signs to forward/backward."
        ),
        "physical_scenario": "CTP branch sign asymmetry, no mixing",
        "role_implication":  "final_coefficient_candidate or cosmo_coefficient_candidate — but CTP causality violated",
    }


def topology_resp1() -> tuple:
    """
    RESP1: I[+,+,-]=I[+,-,+]=I[-,+,+]=1, rest 0.

    Physical meaning: one vertex of the triangle is on the backward (-) branch,
    two are on the forward (+) branch.  This is a 'one-response-leg' topology.
    """
    I = np.zeros((2, 2, 2))
    I[0, 0, 1] = 1.0    # ++-
    I[0, 1, 0] = 1.0    # +-+
    I[1, 0, 0] = 1.0    # -++
    return I, {
        "id":          "RESP1",
        "name":        "One-response (one backward vertex)",
        "description": (
            "One of the three triangle vertices is on the - branch.  "
            "Represents a cross-branch mixing with one response insertion."
        ),
        "physical_scenario": "CTP cross-propagator G^{-+} inserting one backward vertex",
        "role_implication":  "final_coefficient_candidate or cosmo_coefficient_candidate — but CTP causality violated",
    }


def topology_sector_asym() -> tuple:
    """
    SECTOR_ASYM: I[+,+,+]=pi/2, I[-,-,-]=pi*sqrt(3)/4, rest 0.

    Physical meaning: if the N sector (forward branch) has the S4 scalar loop
    with coefficient pi/2, and the D sector (backward branch) has a different
    loop with coefficient pi*sqrt(3)/4, then R = N/D = (pi/2)/(pi*sqrt(3)/4) = sqrt(4/3).

    This is the specific projection-factor hypothesis.  It is not a branch-topology
    claim — it is a SECTOR-level difference where each sector independently has a
    symmetric (SYM-type) loop, but with different sector-specific prefactors.
    """
    I = np.zeros((2, 2, 2))
    I[0, 0, 0] = PI_OVER_2           # +++ sector: pi/2
    I[1, 1, 1] = PROJ_FACTOR         # --- sector: pi*sqrt(3)/4
    return I, {
        "id":          "SECTOR_ASYM",
        "name":        "Sector-asymmetric (N != D sector prefactors)",
        "description": (
            "I[+,+,+]=pi/2, I[-,-,-]=pi*sqrt(3)/4. "
            "Models the scenario where N and D sectors have different Euler-density "
            "prefactors (C_Euler,cosmo vs C_Euler,final), with the S4 loop appearing "
            "in both but with sector-specific weights."
        ),
        "physical_scenario": "Two-sector GRUT action: C_cosmo=pi/2 in N, C_final=pi*sqrt(3)/4 in D",
        "role_implication":  "pi/2 is NOT a branch-topology coefficient; sectors carry the asymmetry",
    }


TOPOLOGIES = [topology_sym, topology_antisym, topology_resp1, topology_sector_asym]


# ── Euclidean S4 propagator equality ─────────────────────────────────────────

def euclidean_s4_analysis() -> dict:
    """
    On compact Euclidean S4, the scalar propagator has a real discrete spectrum
    (eigenvalues of the Laplacian: lambda_l = l(l+3), l=0,1,2,...).

    Consequences for CTP propagators:
      G^{++} = G^T = Σ_l d_l e_l(x) e_l(y) / (lambda_l + m^2)   [time-ordered]
      G^{--} = G^T  [anti-time-ordered = time-ordered on compact Euclidean]
      G^{+-} = G^<  [Wightman: same as above, no time ordering on S4]
      G^{-+} = G^>  [same]

    All four are equal to the Euclidean Green function G_E.
    This means the three-point loop I(h_-,eps) has ALL CTP index combinations
    equal:  I^{i,j,k} = I(h_-,eps) for all (i,j,k).

    This is the SYM topology.  CTP causality (V_aaa=0) is satisfied automatically.
    The loop is a SHARED NORMALIZATION: it appears identically in N and D, so
    it cancels in R=N/D.

    The loop eigenvalue spectrum: lambda_l = l(l+3) for l=0,1,2,...
    Degeneracy on S4: d_l = (2l+3)(l+1)(l+2)/6
    Propagator: G_l = 1 / (lambda_l + h_-)
    """
    # Compute a few eigenvalues and degeneracies to confirm the spectrum
    eigenvalues = [l * (l + 3) for l in range(6)]
    degeneracies = [(2*l + 3) * (l + 1) * (l + 2) // 6 for l in range(6)]

    # The spectral sum Σ_l d_l / (l(l+3) + h_-) is related to I(h_-,eps)
    # via dim-reg (the continuous extension to D=4-2eps)
    # At h_-=0: the l=0 mode has lambda_0=0 (zero mode — needs careful treatment)
    # This is what the endpoint-split validation addresses

    return {
        "claim": (
            "On compact Euclidean S4, G^{++}=G^{--}=G^{+-}=G^{-+}=G_E "
            "(all CTP propagator components are equal)."
        ),
        "reason": "Real discrete spectrum, no Lorentzian time ordering on S4",
        "implication": (
            "I(h_-,eps) = I^{+++} = I^{---} = I^{++-} = ... for all (i,j,k). "
            "This is the SYM topology.  The loop appears IDENTICALLY on both branches."
        ),
        "s4_laplacian_eigenvalues": eigenvalues,
        "s4_degeneracies": degeneracies,
        "zero_mode_note": (
            "The l=0 mode (lambda_0=0) is the zero mode.  It requires careful treatment "
            "in the h_->0 limit.  The endpoint-split validation (Gate 3 criterion 4) "
            "confirmed that this limit is numerically controlled."
        ),
        "role_implication": "shared_normalization (pi/2 cancels in R=N/D on pure Euclidean S4)",
        "ctp_causality": "SYM topology automatically satisfies V_aaa=0 (see CTP causality check)",
        "caveat": (
            "This conclusion applies to PURE Euclidean S4.  If the GRUT action involves: "
            "(a) Lorentzian continuation (de Sitter, not S4), "
            "(b) sector-specific couplings (C_cosmo != C_final), or "
            "(c) a spontaneous breaking of CTP branch symmetry, "
            "then the loop may contribute asymmetrically."
        ),
    }


# ── What would produce R = sqrt(4/3) ─────────────────────────────────────────

def r_target_analysis() -> dict:
    """
    Given that the Euclidean S4 analysis supports shared_normalization (pi/2 cancels),
    what structure WOULD produce R = sqrt(4/3)?

    Two scenarios:

    Scenario A (pi/2 cancels):
      R = C_cosmo / C_final
      where C_cosmo and C_final are sector-specific Euler-density couplings.
      pi/2 is a common kernel normalization in both sectors.
      R = sqrt(4/3) requires C_cosmo / C_final = sqrt(4/3).
      => The role of pi/2 is: shared_normalization.
      => The physics of R comes from the ratio of sector couplings.

    Scenario B (pi/2 is quotient-bearing):
      R = N / D  where N contains pi/2 and D contains the projection factor N=pi*sqrt(3)/4.
      R = (pi/2) / (pi*sqrt(3)/4) = 2/sqrt(3) = sqrt(4/3).
      => The role of pi/2 is: final_coefficient_candidate (if in D) or
                               cosmo_coefficient_candidate (if in N).
      => This requires a Lorentzian or sector-asymmetric mechanism to break
         the Euclidean S4 symmetry.
    """
    # Check Scenario B explicitly
    N_scenario_b = PI_OVER_2          # pi/2 in N (or D)
    D_scenario_b = PROJ_FACTOR        # pi*sqrt(3)/4 in D (or N)
    R_scenario_b = N_scenario_b / D_scenario_b

    # Check Scenario A: what prefactors give R = sqrt(4/3)?
    # If both sectors have pi/2 as shared kernel, R = C_cosmo/C_final
    # Any ratio C_cosmo/C_final = sqrt(4/3) works
    # Example: C_cosmo = 4, C_final = 4/sqrt(4/3) = 2*sqrt(3)
    example_C_cosmo = 4.0
    example_C_final = example_C_cosmo / R_TARGET

    return {
        "scenario_A": {
            "name": "pi/2 is shared_normalization (cancels in R)",
            "mechanism": "CTP branch symmetry → pi/2 in both N and D → cancels",
            "R_formula": "R = C_cosmo / C_final (sector-specific Euler couplings)",
            "R_check": R_TARGET,
            "example_C_cosmo": example_C_cosmo,
            "example_C_final": float(example_C_final),
            "pi_over_2_role": "shared_normalization",
            "requires": "Identification of C_cosmo and C_final as separate theory quantities",
        },
        "scenario_B": {
            "name": "pi/2 is quotient-bearing (enters R on one side)",
            "mechanism": "Sector asymmetry: N uses S4 scalar loop, D uses different loop",
            "R_formula": "R = (pi/2) / (pi*sqrt(3)/4) = sqrt(4/3)",
            "R_computed": float(R_scenario_b),
            "R_check_matches": abs(R_scenario_b - R_TARGET) < 1e-12,
            "projection_factor": float(PROJ_FACTOR),
            "pi_over_2_role": "final_coefficient_candidate or cosmo_coefficient_candidate",
            "requires": (
                "Identification of which GRUT sector uses the S4 loop and which "
                "sector uses a different loop with coefficient pi*sqrt(3)/4"
            ),
        },
        "current_conclusion": (
            "The Euclidean S4 CTP analysis supports Scenario A (shared_normalization). "
            "Scenario B is not excluded but requires a specific asymmetry mechanism "
            "that must be identified in the GRUT CTP action."
        ),
        "guardrail": (
            "Do NOT assign V4 (final_coefficient_candidate) because it produces R=sqrt(4/3). "
            "Assign V4 only if the CTP branch structure DEMANDS it."
        ),
    }


# ── Decision table ────────────────────────────────────────────────────────────

def build_decision_table() -> list:
    return [
        {
            "finding": "Loop appears identically on both CTP branches (SYM topology)",
            "ctp_causality": "PASSES",
            "euclidean_s4_consistent": True,
            "role": "shared_normalization",
            "pi_over_2_in_R": False,
            "note": "pi/2 cancels; R comes from sector prefactor ratio C_cosmo/C_final",
        },
        {
            "finding": "Loop appears only in response/retarded branch (RESP topology)",
            "ctp_causality": "FAILS (V_aaa != 0 for simple RESP topologies)",
            "euclidean_s4_consistent": False,
            "role": "final_coefficient_candidate or cosmo_coefficient_candidate",
            "pi_over_2_in_R": True,
            "note": "Only possible if Lorentzian CTP structure or sector asymmetry overrides",
        },
        {
            "finding": "Loop in both branches with unequal sector weights",
            "ctp_causality": "NOT CHECKED — requires sector decomposition",
            "euclidean_s4_consistent": "Conditional (only with sector-specific couplings)",
            "role": "branch_normalization_candidate",
            "pi_over_2_in_R": "Partial",
            "note": "R = (C_cosmo * pi/2) / (C_final * pi/2 * weight_ratio) — pi/2 partially cancels",
        },
        {
            "finding": "Loop not a vertex in the GRUT CTP action",
            "ctp_causality": "N/A",
            "euclidean_s4_consistent": "N/A",
            "role": "benchmark_seed",
            "pi_over_2_in_R": False,
            "note": "pi/2 validates numerical extraction route only",
        },
        {
            "finding": "Branch placement cannot be determined from available evidence",
            "ctp_causality": "UNKNOWN",
            "euclidean_s4_consistent": "UNKNOWN",
            "role": "role_unassigned",
            "pi_over_2_in_R": "UNKNOWN",
            "note": "Default; R1 is NEEDS_THEORY",
        },
    ]


# ── Main ──────────────────────────────────────────────────────────────────────

def main():
    print("=" * 80)
    print("Gate 3 CTP Branch-Incidence Audit")
    print(f"Spec: {SPEC_VERSION}")
    print(f"Start: {datetime.now().isoformat()}")
    print("=" * 80)

    repo_root = Path(__file__).resolve().parents[3]
    kbasis    = keldysh_rotation()
    R         = kbasis["R"]

    # ── Keldysh basis ───────────────────────────────────────────────────────
    print("\n1. Keldysh rotation matrix")
    print(f"   R =\n{R}")
    print(f"   det(R) = {kbasis['det']:.4f}")
    print(f"   r-row:  R[r,+] = {kbasis['R_r_plus']},  R[r,-] = {kbasis['R_r_minus']}")
    print(f"   a-row:  R[a,+] = {kbasis['R_a_plus']},  R[a,-] = {kbasis['R_a_minus']}")
    print(f"   V_aaa = 0 condition: Σ_{{i,j,k}} (-1)^{{i+j+k}} I[i,j,k] = 0")

    # ── Topology analysis ───────────────────────────────────────────────────
    print("\n2. CTP topology analysis")
    print("-" * 60)
    all_topology_results = {}
    for topo_fn in TOPOLOGIES:
        I_pm, meta = topo_fn()
        ctp = ctp_causality_check(I_pm, R)
        comp = ra_components(I_pm, R)
        print(f"\n   [{meta['id']}] {meta['name']}")
        print(f"   Description: {meta['description'][:70]}...")
        nonzero = {k: f"{v:.4f}" for k, v in comp.items() if abs(v) > 1e-10}
        print(f"   Non-zero r/a components: {nonzero}")
        print(f"   V_aaa = {ctp['V_aaa']:.6f}  →  CTP causality {'PASS' if ctp['passes'] else 'FAIL'}")
        print(f"   Role implication: {meta['role_implication']}")
        all_topology_results[meta['id']] = {
            **meta, "ra_components": comp, "V_aaa": ctp['V_aaa'], "ctp_passes": ctp['passes']
        }

    # ── Euclidean S4 analysis ───────────────────────────────────────────────
    print("\n" + "-" * 60)
    print("3. Euclidean S4 propagator-equality analysis")
    print("-" * 60)
    s4 = euclidean_s4_analysis()
    print(f"   Claim: {s4['claim']}")
    print(f"   Reason: {s4['reason']}")
    print(f"   Implication: {s4['implication'][:70]}...")
    print(f"   S4 Laplacian eigenvalues (l=0..5): {s4['s4_laplacian_eigenvalues']}")
    print(f"   Degeneracies: {s4['s4_degeneracies']}")
    print(f"   → Role: {s4['role_implication']}")
    print(f"   → CTP causality: {s4['ctp_causality']}")
    print(f"\n   Caveat: {s4['caveat'][:80]}...")

    # ── R = sqrt(4/3) analysis ──────────────────────────────────────────────
    print("\n" + "-" * 60)
    print("4. R_target = sqrt(4/3) scenario analysis")
    print("-" * 60)
    rta = r_target_analysis()
    for sc_key, sc in [("scenario_A", rta["scenario_A"]), ("scenario_B", rta["scenario_B"])]:
        print(f"\n   {sc_key}: {sc['name']}")
        print(f"   Mechanism: {sc['mechanism']}")
        print(f"   R formula: {sc['R_formula']}")
        print(f"   pi/2 role: {sc['pi_over_2_role']}")
        if 'R_check_matches' in sc:
            print(f"   R computed = {sc['R_computed']:.10f}  "
                  f"matches sqrt(4/3): {sc['R_check_matches']}")
    print(f"\n   Conclusion: {rta['current_conclusion']}")
    print(f"\n   GUARDRAIL: {rta['guardrail']}")

    # ── Decision table ──────────────────────────────────────────────────────
    print("\n" + "-" * 60)
    print("5. Decision table")
    print("-" * 60)
    dt = build_decision_table()
    for row in dt:
        print(f"\n   Finding: {row['finding']}")
        print(f"   CTP causality: {row['ctp_causality']}")
        print(f"   Role: {row['role']}")

    # ── Summary ─────────────────────────────────────────────────────────────
    print("\n" + "=" * 60)
    print("SUMMARY")
    print("=" * 60)
    print(f"  Euclidean S4 finding:  SYM topology only (V_aaa=0 passes)")
    print(f"  All non-SYM topologies: V_aaa != 0 (CTP causality fails)")
    print(f"  Euclidean S4 implication: pi/2 is shared_normalization")
    print(f"  Role: role_unassigned (R1 still NEEDS_THEORY)")
    print(f"  Supported scenario: A (pi/2 cancels; R from sector prefactor ratio)")
    print(f"  Not-excluded scenario: B (pi/2 quotient-bearing with sector asymmetry)")
    print(f"  Blocking question:")
    print(f"    Does the GRUT action assign equal S4 scalar loops to both sectors,")
    print(f"    or does it assign different loop structures / couplings to N vs D?")

    # ── Output ──────────────────────────────────────────────────────────────
    out_dir  = repo_root / "theory" / "hard_theory" / "gate3_dl_outputs"
    out_dir.mkdir(exist_ok=True)
    out_file = out_dir / "gate3_ctp_branch_incidence.json"

    output = {
        "spec":           SPEC_VERSION,
        "spec_date":      SPEC_DATE,
        "date":           datetime.now().isoformat(),
        "seed_value":     PI_OVER_2,
        "seed_exact":     "pi/2",
        "R_target":       R_TARGET,
        "R_exact":        "sqrt(4/3)",
        "proj_factor":    float(PROJ_FACTOR),
        "keldysh_basis":  {k: v.tolist() if isinstance(v, np.ndarray) else v
                           for k, v in kbasis.items()},
        "topology_results":  all_topology_results,
        "euclidean_s4_analysis": s4,
        "r_target_analysis": rta,
        "decision_table":    dt,
        "summary": {
            "euclidean_s4_topology":    "SYM (all propagators equal)",
            "ctp_causality_result":     "Only SYM passes V_aaa=0",
            "supported_role":           "shared_normalization (Scenario A)",
            "not_excluded_role":        "final_coefficient_candidate (Scenario B, requires sector asymmetry)",
            "r1_status":                "NEEDS_THEORY",
            "current_role":             "role_unassigned",
            "blocking_question": (
                "Does the GRUT CTP action assign equal S4 scalar loop coefficients to "
                "both N and D sectors (Scenario A: pi/2 cancels), or different coefficients "
                "(Scenario B: pi/2 is quotient-bearing)?"
            ),
        },
    }

    with open(out_file, "w") as f:
        json.dump(output, f, indent=2, default=str)

    print(f"\nOutput: {out_file}")
    print("=" * 80)
    print(f"End: {datetime.now().isoformat()}")
    print("=" * 80)


if __name__ == "__main__":
    main()
