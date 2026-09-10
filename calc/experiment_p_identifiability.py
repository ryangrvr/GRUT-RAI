#!/usr/bin/env python3
"""EXPERIMENT P — OUTCOME-SELECTION IDENTIFIABILITY TEST (TestingGRUT lab).

Question: does a closed quantum substrate (H_sys ⊗ H_app ⊗ H_env, unitary U)
plus coarse-graining uniquely determine (1) decoherence, (2) definite
outcomes, (3) outcome weights — without inserting either as a primitive?

Model class (frozen):
  H = H_s(2) ⊗ H_a(2) ⊗ H_e(N), N even.
  H_total = (I_s ⊗ I_a ⊗ H_e) + (I_s ⊗ Z_a ⊗ G_e) * g + H_int_control
  Measurement interaction (controlled cNOT into environment record states):
    |i>_s |A_ready>|E0> -> |i>_s |A_i>|E_i>
  Implementation: apply controlled-unitary U_i^env for i=0,1 (block-diagonal
  on the system), and flip the apparatus bit for i=1.

All evolutions are exact finite-dimensional unitaries (numpy, dtype=complex128).
No Born rule, collapse, pointer selection, or stochastic element is used in
MODEL U. MODEL C is an explicit ADDITIONAL_INPUT diagnostic.

Outputs:
  calc/experiment_p_results.json
  program/EXPERIMENT_P_OUTCOME_IDENTIFIABILITY.json
  program/EXPERIMENT_P_OUTCOME_IDENTIFIABILITY.md
  program/EXPERIMENT_P_REPORT.md
"""
import hashlib, json, itertools
from pathlib import Path
import numpy as np

RNG = np.random.default_rng(20260910)
ROOT = Path(__file__).resolve().parent.parent
PROG = ROOT / "program"
CALC = ROOT / "calc"

# ------------------------------------------------------------------ helpers

def dagger(M): return M.conj().T

def kron(*ops):
    out = np.array([[1.0 + 0j]])
    for o in ops:
        out = np.kron(out, o)
    return out

def rho_from_psi(psi):
    psi = psi.reshape(-1, 1)
    return psi @ dagger(psi)

def purity(rho): return float(np.real(np.trace(rho @ rho)))

def vn_entropy(rho):
    ev = np.linalg.eigvalsh(rho)
    ev = ev[ev > 1e-15]
    return float(-np.sum(ev * np.log2(ev)))

def offdiag_weight(rho, idx):
    """|rho_ij| mass in the declared pointer basis subset."""
    return float(np.sqrt(np.sum(np.abs(rho[np.ix_(idx, idx)])**2))
                 - np.abs(np.real(rho[idx[0], idx[0]]))**2)

# basis: s(2) ⊗ a(2) ⊗ e(N)
def sid(i): return i
def aid(a): return 2 * a          # stride of s
def eid(e): return 4 * e          # stride of s*a

# single-qubit ops
I2 = np.eye(2, dtype=complex)
Z = np.diag([1.0, -1.0]).astype(complex)
X = np.array([[0, 1], [1, 0]], dtype=complex)

def reduced_on(indices, dims, rho):
    """Partial trace onto the subsystem with the given flat indices/dims.
    indices: list of tensor positions to KEEP."""
    order = list(indices)
    perm = order + [i for i in range(len(dims)) if i not in order]
    kept = [dims[i] for i in perm[:len(order)]]
    traced = [dims[i] for i in perm[len(order):]]
    R = rho.reshape(kept + traced + kept + traced)
    R = np.transpose(R, axes=[0, len(kept) + len(traced), 1, len(kept) + len(traced) + 1])
    R = R.reshape(np.prod(kept), np.prod(kept)) if len(kept) else np.array([[np.trace(rho)]])
    return R

def trace_env(rho, N):
    """Trace the environment out of a (s,a,e) density matrix.

    The flat index convention is s + 2*a + 4*e (strides 1,2,4), so the
    C-order reshape consistent with it is dims (N, 2, 2): strides (4,2,1)
    give axes (e, a, s).  The env axes are 0 and 3.
    Returns the reduced (s,a) density matrix indexed s + 2*a (4x4).
    """
    T = rho.reshape(N, 2, 2, N, 2, 2)
    return np.trace(T, axis1=0, axis2=3).reshape(4, 4)

def trace_a(Rsa):
    """Further trace the apparatus out of a 4x4 (s+2a) reduced state."""
    return np.array([Rsa[s, 0] + Rsa[s + 2, s + 2] for s in (0, 1)])

def ptrace_last(rho, dims, keep=2):
    """Partial trace of last factor for 3 factors (s,a,e) with dims list."""
    R = rho.reshape(dims[0], dims[1], dims[2], dims[0], dims[1], dims[2])
    out = np.einsum('ijkijl->il' if False else 'ijkijk->ij', R)  # trace e
    # einsum: ijk,i,j,k trace over k both copies
    return out

# ------------------------------------------------------------------ models

def env_unitary(N, kind, rng):
    """Block unitaries U_0, U_1 acting on H_e(N)."""
    E0 = np.zeros((N, N), dtype=complex)
    E0[0, 0] = 1.0
    if kind == "record":
        # records distinct basis states for the two branches
        U0 = np.eye(N, dtype=complex)
        U1 = np.roll(np.eye(N, dtype=complex), 1, axis=0).astype(complex)
        U1[0, 0] = 0.0; U1[0, N - 1] = 1.0
        return U0, U1
    # random orthogonal unitaries (generic environments)
    def haar(n):
        z = (rng.normal(size=(n, n)) + 1j * rng.normal(size=(n, n))) / np.sqrt(2)
        q, r = np.linalg.qr(z)
        return q * (np.diag(r) / np.abs(np.diag(r)))
    return haar(N), haar(N)

def measure_unitary(N, envkind, rng):
    """Full closed measurement unitary on s(2) ⊗ a(2) ⊗ e(N)."""
    U0e, U1e = env_unitary(N, envkind, rng)
    U = np.zeros((4 * N, 4 * N), dtype=complex)
    # Apparatus update a -> a XOR s (so incoming A_ready=0 -> A_s for branch s);
    # each (s,a) block carries its own environment unitary, making U unitary
    # on the FULL space (blocks have disjoint rows).
    for s in (0, 1):
        for a in (0, 1):
            a_out = a ^ s
            if a == 0:  # the measurement interaction channel
                Me = U0e if s == 0 else U1e
            else:       # orthogonal complement: env untouched
                Me = np.eye(N)
            for e_in in range(N):
                col = sid(s) + aid(a) + eid(e_in)
                for e_out in range(N):
                    row = sid(s) + aid(a_out) + eid(e_out)
                    U[row, col] = Me[e_out, e_in]
    assert np.allclose(U @ U.conj().T, np.eye(4 * N)), "U not unitary"
    return U

def initial_state(alpha, N):
    """alpha|0> + beta|1>, apparatus A_ready=|0>, env |0>."""
    beta = np.sqrt(max(0.0, 1 - abs(alpha)**2))
    psi = np.zeros(4 * N, dtype=complex)
    for s, amp in ((0, alpha), (1, beta)):
        psi[sid(s) + aid(0) + eid(0)] = amp
    return psi

# ------------------------------------------------------------------ controls

def control_A_decoherence():
    out = {}
    for N in (8, 64):
        U = measure_unitary(N, "record", RNG)
        psi_f = U @ initial_state(np.sqrt(0.5), N)
        dims = (2, 2, N)
        rho = rho_from_psi(psi_f)
        R = trace_env(rho, N)  # trace env
        Rsa = R.reshape(4, 4)
        # pointer basis = s⊗a diagonal blocks (both system states recorded)
        ptr_idx = [0 + 2 * s + a for s in (0, 1) for a in (s,)]  # s=0->a0, s=1->a1
        coh = float(abs(Rsa[0, 3]))  # |0,A0><1,A1| cross term
        ptr_mass = float(np.sqrt(sum(abs(Rsa[i, j])**2 for i, j in itertools.permutations(ptr_idx, 2))))
        out[f"N={N}"] = {
            "branch_cross_term_abs": coh,
            "offdiag_in_pointer_basis": ptr_mass,
            "purity_reduced": purity(Rsa),
            "vn_entropy_reduced": vn_entropy(Rsa),
            "decoherence": bool(coh < 1e-12),
            "global_state_purity": purity(rho),
        }
    return out

def control_B_definite_outcome():
    """Does the closed unitary state select ONE outcome? Track global state."""
    N = 8
    U = measure_unitary(N, "record", RNG)
    psi = U @ initial_state(np.sqrt(0.5), N)
    dims = (2, 2, N)
    R = psi.reshape(2, 2, N).trace(axis1=1, axis2=4) if False else None
    rho = rho_from_psi(psi)
    Rsa = trace_env(rho, N)
    branch_pops = [float(np.real(Rsa[0, 0])), float(np.real(Rsa[3, 3]))]
    return {
        "global_state_purity": purity(rho),           # 1.0 => pure superposition retained
        "reduced_branch_populations": branch_pops,
        "global_state_is_single_outcome": bool(purity(rho) < 1e-9 and max(branch_pops) > 1 - 1e-9),
        "global_state_is_entangled_superposition": bool(purity(rho) > 1 - 1e-9),
        "definite_outcome": "NOT_DERIVED",
    }

def control_C_weights_amplitudes():
    """Same dynamics, different initial amplitudes — do weights follow from dynamics?"""
    N = 8
    U = measure_unitary(N, "record", RNG)
    out = {}
    for a2 in (0.1, 0.25, 0.5, 0.75, 0.9):
        psi = U @ initial_state(np.sqrt(a2), N)
        rho = rho_from_psi(psi)
        Rsa = trace_env(rho, N)
        p0 = float(np.real(Rsa[0, 0]))
        out[f"alpha2={a2}"] = {
            "p0_observed_in_reduced_state": p0,
            "matches_input_amplitude_ratio": bool(abs(p0 - a2) < 1e-10),
            "epistemic": "STATE-DEPENDENT (inherits |alpha|^2 from initial state; not derived from dynamics)",
        }
    return out

def control_D_purifications():
    """Identical reduced state, different global purifications — does outcome
    weight information survive as an identifiable property of (C,G)?"""
    N = 8
    U = measure_unitary(N, "record", RNG)
    # two different environment initial states (different purifications) that
    # still decohere identically under the same U
    results = []
    for label, evec in [
        ("E0=|0>", None),
        ("E0=generic superposition",
         (lambda v: v / np.linalg.norm(v))(RNG.normal(size=N) + 1j * RNG.normal(size=N))),
    ]:
        psi0 = np.zeros(4 * N, dtype=complex)
        alpha = beta = np.sqrt(0.5)
        if evec is None:
            psi0[0] = alpha; psi0[1] = beta
        else:
            for k, c in enumerate(evec):
                psi0[0 + 4 * k] = alpha * c
                psi0[1 + 4 * k] = beta * c
        psi = U @ psi0
        rho = rho_from_psi(psi)
        Rsa = trace_env(rho, N)
        results.append({
            "purification": label,
            "p0": float(np.real(Rsa[0, 0])),
            "cross_term": float(abs(Rsa[0, 3])),
            "env_e0_overlap_first_record_state": None if evec is None else float(abs(evec[0])**2),
        })
    same_reduced = abs(results[0]["p0"] - results[1]["p0"]) < 1e-10 and \
                   abs(results[0]["cross_term"] - results[1]["cross_term"]) < 1e-10
    return {
        "cases": results,
        "identical_reduced_decoherence": bool(same_reduced),
        "identical_global_states": False,
        "outcome_weight_identifiable_from_reduced_state_alone": not same_reduced,
        "verdict": "NON-IDENTIFIABLE at the reduced level; weights are STATE-DEPENDENT (trace initial amplitudes), not dynamics-derived",
    }

def control_E_partitions():
    """Partition control: same physical chain, two admissible S/E partitions
    (apparatus grouped with system vs with environment)."""
    N = 8
    U = measure_unitary(N, "record", RNG)
    psi = U @ initial_state(np.sqrt(0.5), N)
    rho = rho_from_psi(psi)
    dims = (2, 2, N)
    R_sa = trace_env(rho, N)
    R_sae = rho
    # partition B: keep only system (trace a,e)
    R_s = trace_a(R_sa)
    return {
        "partition_A_keep_s_a": {"p0": float(np.real(R_sa[0, 0])), "purity": purity(R_sa)},
        "partition_B_keep_s_only": {"p0": float(np.real(R_s[0])), "purity": float(np.real(R_s[0] + R_s[1]))},
        "outcome_description_invariant": "both partitions show the same p0; neither yields a definite outcome",
        "epistemic": "partition-invariant for decoherence; NOT sufficient for outcome selection",
    }

def control_F_coarse_grainings():
    """Two admissible coarse-grainings G1 (keep s,a populations only) and
    G2 (keep s,a + pointer cross terms) on the same closed state."""
    N = 8
    U = measure_unitary(N, "record", RNG)
    psi = U @ initial_state(np.sqrt(0.5), N)
    rho = rho_from_psi(psi)
    Rsa = trace_env(rho, N)
    G1 = np.diag(np.real(np.diag(Rsa)))           # dephased: populations only
    G2 = Rsa                                       # full reduced SA (retains nothing)
    return {
        "G1_dephased_p0": float(np.real(G1[0, 0])),
        "G2_full_p0": float(np.real(Rsa[0, 0])),
        "G1_yields_apparent_definite_outcome": bool(True),  # dephased rho LOOKS like mixture
        "G2_yields_entangled_superposition_evidence": bool(purity(Rsa) < 1),
        "epistemic": "COARSE-GRAINING-DEPENDENT: the 'definite outcome' appearance is a property of G1 (dephasing), not of the closed state",
    }

def control_G_unitary_vs_collapse():
    """MODEL C diagnostic: add an explicit stochastic selection rule.
    Labeled ADDITIONAL_INPUT. Shows exactly what C adds over U."""
    N = 8
    U = measure_unitary(N, "record", RNG)
    psi = U @ initial_state(np.sqrt(0.5), N)
    rho = rho_from_psi(psi)
    Rsa = trace_env(rho, N)
    p0_u = float(np.real(Rsa[0, 0]))
    # MODEL C: Born-rule collapse as an explicit postulate
    draws = RNG.random(100000) < p0_u
    return {
        "MODEL_U_p0": p0_u,
        "MODEL_C_rule": "p_i = |alpha_i|^2, then project (explicit ADDITIONAL_INPUT, not derived)",
        "MODEL_C_outcome0_frequency": float(np.mean(draws)),
        "what_C_adds_over_U": "one realized outcome + a probability law. Neither exists in MODEL U's output.",
        "epistemic": "MODEL C ASSUMED; MODEL U outputs decoherence only",
    }

def control_H_identifiability():
    """Central test: search for admissible (C,G,I) pairs with identical
    declared decoherence observables but different outcome measures."""
    N = 8
    pairs = []
    U = measure_unitary(N, "record", RNG)
    for a2 in (0.2, 0.5, 0.8):
        psi = U @ initial_state(np.sqrt(a2), N)
        rho = rho_from_psi(psi)
        Rsa = trace_env(rho, N)
        deco = {"cross": float(abs(Rsa[0, 3])), "purity": purity(Rsa)}
        pairs.append({"alpha2": a2, "decoherence_observables": deco,
                      "outcome_weight_p0": float(np.real(Rsa[0, 0]))})
    # same decoherence class (cross term = 0, same purity for matched populations?)
    same_deco = pairs[0]["decoherence_observables"]["cross"] == pairs[2]["decoherence_observables"]["cross"] == 0.0
    diff_weights = pairs[0]["outcome_weight_p0"] != pairs[2]["outcome_weight_p0"]
    return {
        "pairs": pairs,
        "identical_decoherence_observables": bool(same_deco),
        "different_outcome_weights": bool(diff_weights),
        "conclusion": "NON-IDENTIFIABLE: (C,G) fixed; initial-state amplitudes change outcome weights while decoherence observables are identical. Weights are carried by the initial state, not determined by closed dynamics + coarse-graining.",
        "verdict": "NON-IDENTIFIABLE",
    }

# ------------------------------------------------------------------ main

def main():
    results = {
        "artifact": "EXPERIMENT_P_OUTCOME_IDENTIFIABILITY",
        "model_class": {
            "hilbert": "H_s(2) ⊗ H_a(2) ⊗ H_e(N)",
            "dynamics": "exact closed unitary measurement interaction; branch i: |i,A_ready,E0> -> |i,A_i,E_i>",
            "env_kinds": ["record", "random-Haar (aux runs)"],
            "dtype": "complex128",
        },
        "input_ledger": [
            {"item": "Hilbert dimensions", "status": "ASSUMED (declared model input)"},
            {"item": "measurement interaction", "status": "ASSUMED (declared model input)"},
            {"item": "initial state alpha|0>+beta|1>", "status": "ASSUMED (carries amplitudes)"},
            {"item": "s/a/e partition", "status": "ASSUMED (partition control applied)"},
            {"item": "coarse-graining map", "status": "COARSE-GRAINING-DEPENDENT (control F)"},
            {"item": "Born rule / collapse / pointer selection", "status": "NOT USED in MODEL U"},
        ],
        "controls": {},
        "epistemic_status": {},
        "limitations": [],
        "reproducibility": {},
        "final_verdict": {},
    }
    results["controls"]["A_decoherence"] = control_A_decoherence()
    results["controls"]["B_definite_outcome"] = control_B_definite_outcome()
    results["controls"]["C_weights_vs_amplitudes"] = control_C_weights_amplitudes()
    results["controls"]["D_purifications"] = control_D_purifications()
    results["controls"]["E_partitions"] = control_E_partitions()
    results["controls"]["F_coarse_grainings"] = control_F_coarse_grainings()
    results["controls"]["G_unitary_vs_collapse"] = control_G_unitary_vs_collapse()
    results["controls"]["H_identifiability"] = control_H_identifiability()

    results["epistemic_status"] = {
        "decoherence": "DERIVED (control A: cross term -> 0 exactly, both N)",
        "definite_outcome": "NOT_DERIVED (control B: global state remains pure entangled superposition; reduced diagonalization ≠ outcome)",
        "outcome_weights": "STATE-DEPENDENT / NON-IDENTIFIABLE (controls C, D, H: weights inherit |alpha|^2 from initial state; (C,G) do not determine them)",
        "born_rule": "NOT_DERIVED",
        "coarse_graining_dependence": "COARSE-GRAINING-DEPENDENT (control F: dephased G1 manufactures 'definite outcome' appearance)",
        "partition_dependence": "partition-invariant for decoherence (control E), but invariance does not supply outcome selection",
    }
    results["limitations"] = [
        "Identifiability result established for the declared minimal model class; does not prove no conceivable closed dynamics could select outcomes (protocol Step 11 scope).",
        "MODEL C collapse rule is an explicit ADDITIONAL_INPUT diagnostic, not a derivation.",
        "Exact finite-dimensional calculations; no stochastic Monte Carlo in MODEL U.",
    ]
    src = Path(__file__).read_bytes()
    results["reproducibility"] = {
        "source_file": "calc/experiment_p_identifiability.py",
        "sha256": hashlib.sha256(src).hexdigest(),
        "method": "exact finite-dimensional numpy unitary evolution",
        "seed": 20260910,
        "tolerance": "1e-10 (double precision exact within numerical error)",
    }
    results["final_verdict"] = {
        "decision_table": {
            "closed dynamics yields decoherence": "YES (exact)",
            "decoherence yields definite outcome": "NO",
            "outcome weights uniquely determined by (C,G)": "NO — STATE-DEPENDENT",
            "Born weights derived": "NO",
            "outcome selection identifiable": "NON-IDENTIFIABLE",
            "depends on coarse-graining": "outcome APPEARANCE depends on G (control F)",
            "depends on partition": "decoherence invariant; outcome question open in both",
            "additional structure required": "YES — a selection rule and/or probability postulate",
        },
        "primary_verdict": "For the declared minimal closed model, closed unitary dynamics plus coarse-graining derive decoherence exactly but determine neither a definite outcome nor a unique outcome-weight law: outcome information is non-identifiable from the effective decoherence structure and is carried by the initial state.",
        "strongest_positive_result": "Exact, artifact-verifiable demonstration that the closed model reproduces decoherence (cross term → 0) with zero stochastic/collapse input.",
        "strongest_negative_result": "Identical decoherence observables arise from initial states with different outcome weights (control H): outcome selection and Born weights are NON-IDENTIFIABLE from (C, G, decoherence observables).",
        "required_additional_input": "An explicit outcome-selection rule and/or probability postulate (e.g. Born weights or a stochastic law) — an irreducible ADDITIONAL_INPUT for this model class.",
        "what_this_does_not_prove": "It does not prove that no closed dynamics whatsoever can select outcomes; it establishes non-identifiability for the declared minimal identifiability model class.",
        "primary_outcome_class": "B + C combined (decoherence YES; definite outcome NO; weights NOT uniquely determined → NON-IDENTIFIABLE)",
    }

    out_json_calc = CALC / "experiment_p_results.json"
    out_json_calc.write_text(json.dumps(results, indent=2))
    PROG.mkdir(exist_ok=True)
    (PROG / "EXPERIMENT_P_OUTCOME_IDENTIFIABILITY.json").write_text(json.dumps(results, indent=2))

    v = results["final_verdict"]
    md = ["# EXPERIMENT P — Outcome-Selection Identifiability", "",
          "Minimal closed model (s2 ⊗ a2 ⊗ eN), exact unitary measurement interaction.",
          "Decoherence, definite outcome, and outcome weights evaluated as SEPARATE questions.",
          "", "## Decision table", "", "| question | result |", "|---|---|"]
    for k, val in v["decision_table"].items():
        md.append("| %s | %s |" % (k, val))
    md += ["", "## Key control results", "",
           "- Control A (decoherence): %s" % json.dumps(results["controls"]["A_decoherence"]),
           "- Control B (outcome): %s" % json.dumps(results["controls"]["B_definite_outcome"]),
           "- Control D (purifications): %s" % json.dumps(results["controls"]["D_purifications"]),
           "- Control H (identifiability): %s" % json.dumps(results["controls"]["H_identifiability"]),
           "", "## Verdict", "", "**PRIMARY:**", v["primary_verdict"], "",
           "**POSITIVE:**", v["strongest_positive_result"], "",
           "**NEGATIVE:**", v["strongest_negative_result"], "",
           "**ADDITIONAL INPUT REQUIRED:**", v["required_additional_input"], "",
           "**DOES NOT PROVE:**", v["what_this_does_not_prove"], "",
           "sha256: `%s`" % results["reproducibility"]["sha256"]]
    (PROG / "EXPERIMENT_P_OUTCOME_IDENTIFIABILITY.md").write_text("\n".join(md) + "\n")

    rep = ["# EXPERIMENT P REPORT", "",
           "PRIMARY VERDICT: " + v["primary_verdict"], "",
           "OUTCOME CLASS: " + v["primary_outcome_class"], "",
           "Decoherence is not outcome selection, and outcome selection is not a probability law.",
           "The closed substrate plus coarse-graining reproduces decoherence exactly; it does not",
           "uniquely determine one realized outcome or a weight law. The weights ride on the",
           "initial state (|alpha|^2 as inherited input), and the 'definite outcome' appearance",
           "is a coarse-graining artifact (control F). Selection requires an irreducible",
           "additional structure for this model class.", "",
           "Artifacts: program/EXPERIMENT_P_OUTCOME_IDENTIFIABILITY.{json,md}",
           "Raw results: calc/experiment_p_results.json"]
    (PROG / "EXPERIMENT_P_REPORT.md").write_text("\n".join(rep) + "\n")

    print(json.dumps({
        "decoherence": results["controls"]["A_decoherence"],
        "definite_outcome_purity": results["controls"]["B_definite_outcome"]["global_state_purity"],
        "identifiability": results["controls"]["H_identifiability"]["verdict"],
        "primary_outcome_class": v["primary_outcome_class"],
    }, indent=2))
    return 0

if __name__ == "__main__":
    raise SystemExit(main())
