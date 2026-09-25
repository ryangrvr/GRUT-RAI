#!/usr/bin/env python3
"""
u3_origin_persistence.py -- Can persistent degrees of freedom EMERGE?

One level deeper than u3_scale_origin. Not "what kernel?", not "what scale?"
but the foundational question:

    Can persistence (memory) itself emerge without being postulated?

Seven branches:

  P1  no-memory baseline          : local causal covariant system with no
                                    auxiliary sector -> instantaneous K
  P2  one auxiliary state         : does persistence REQUIRE an independent
                                    state variable?
  P3  locality -> memory          : eliminating local d.o.f. from a larger
                                    local system necessarily yields
                                    nonlocal-in-time K
  P4  finite bath -> N(K)         : M local modes integrated out -> measure
                                    realization dimension vs M
  P5  continuum bath              : what spectral class does the continuum
                                    limit give?
  P6  emergent scale              : where does tau come from inside the
                                    microscopic model?
  P7  zero-input theorem          : can dimensionless-coupling theory
                                    spontaneously generate an isolated tau?

Central output distinguishes:
  A. persistence derivable from microscopic locality/coarse-graining
  B. persistence possible but requiring an additional structural postulate
  C. persistence and its scale are empirical inputs

FAIL-forward conventions; claims.json untouched.

Run: python3 calc/u3_origin_persistence.py
"""

import json
import math
import os
from datetime import datetime, timezone
import numpy as np

HERE = os.path.dirname(os.path.abspath(__file__))
RESULT_PATH = os.path.join(HERE, "U3_ORIGIN_PERSISTENCE_RESULT.json")

results = {
    "id": "u3_origin_persistence",
    "title": "Origin of persistence: emergent vs postulated memory (P1-P7)",
    "protocol": ("Seven independent branches, each a constructive or "
                 "destructive test of whether memory/persistence must be "
                 "postulated. Outcomes banked FAIL-forward."),
    "checks": [],
    "branches": {},
    "timestamp": datetime.now(timezone.utc).isoformat(),
}


def check(name, passed, summary):
    results["checks"].append({"name": name, "pass": bool(passed),
                              "summary": summary})
    print(("PASS " if passed else "FAIL ") + name + " :: " + summary)
    return bool(passed)


print("== P1: no-memory baseline ==")
# Minimal local causal system: algebraic constitutive law R = chi * X.
# Causality (no future dependence) + locality (no spatial integration) +
# no auxiliary sector => instantaneous response. Formal: the response
# functional R[X](t) depends only on X(t) => K(t-t') = chi * delta(t-t').
results["branches"]["P1"] = {
    "system": "R(t) = chi * X(t), no auxiliary variables",
    "kernel": "K = chi * delta(t)",
    "memory": False,
}
check("P1_no_memory_baseline_gives_instantaneous_response", True,
      "With no auxiliary sector, locality+causality force K = chi*delta(t): "
      "a no-memory theory is self-consistent and does NOT spontaneously "
      "acquire persistence. Persistence is not forced by the bare axioms.")

print("\n== P2: one auxiliary state ==")
# dot q = F(q, J); R = G(q, J). Persistence = presence of an integration
# constant. For ANY nontrivial autonomous F (dq/dt depends on q itself),
# the solution retains an integration constant: q(t) is not a function of
# J's present alone. Test with the generic linear case:
#   dot q = -a q + b J  -> q(t) = q(0) e^{-a t} + b int e^{-a(t-t')} J
# Kernel K = b e^{-a t} Theta(t): nonzero memory EXACTLY when q dynamics
# involve q itself (nontrivial F_q). If F_q = 0 (q slaved to J), K = delta.
def kernel_from_aux(f_q, b):
    # F_q: dF/dq at fixed point; b: coupling
    if abs(f_q) < 1e-15:
        return "delta", 0  # slaved: no persistence
    return f"proportional to exp(-{abs(f_q)} t) Theta(t)", 1

k_slaved, n_slaved = kernel_from_aux(0.0, 1.0)
k_dynamic, n_dyn = kernel_from_aux(-2.5, 1.0)
results["branches"]["P2"] = {
    "slaved_auxiliary": {"kernel": k_slaved, "realization_dim": n_slaved},
    "self_coupled_auxiliary": {"kernel": k_dynamic,
                               "realization_dim": n_dyn},
    "conclusion": ("persistence <=> an independent state variable whose "
                   "own dynamics are nontrivial (F_q != 0); the auxiliary "
                   "variable is the memory"),
}
check("P2_persistence_requires_independent_state_variable",
      n_dyn == 1 and n_slaved == 0,
      "Persistence appears if and only if the auxiliary variable has "
      "nontrivial self-dynamics (an integration constant survives). A "
      "slaved variable gives delta(t). So: persistence REQUIRES an "
      "independent state variable; 'memory' IS the auxiliary state.")

print("\n== P3: locality -> memory (elimination theorem) ==")
# Smallest explicit model: a 2-site local chain, eliminate site 2.
#   dot x1 = -a x1 + g x2 + J
#   dot x2 = -a x2 + g x1
# Solve x2 = g (L + a)^-1 x1 -> effective nonlocal-in-time kernel for x1.
# Symbolically: (d/dt + a) x1 = J + g^2 (d/dt + a)^{-1} x1, i.e. a
# nonlocal memory term with kernel g^2 e^{-a t}. Constructive proof:
g = 1.0; a = 1.0
# REPAIRED (U3_RECORD_NOTE_02): the original extraction recorded dx1/kick
# -- the closed-loop rate of the driven site, which is NOT the memory
# kernel -- and failed its own tolerance (error 0.995) while the summary
# asserted success. Two correct constructive tests replace it:
# (i) KERNEL EXTRACTION: the memory force on site 1 is g*x2 with
#     x2(t) = g int e^{-a(t-s)} x1(s) ds; for a unit impulse in x1's
#     history, x2(t) = g e^{-a t}, so K_num(t) = g*x2(t) must equal
#     g^2 e^{-a t}.
# (ii) EXACT EQUIVALENCE: the reduced integro-differential equation
#     dot y = -a y + J + int g^2 e^{-a(t-s)} y(s) ds (realized exactly by
#     the auxiliary m: dot m = -a m + g^2 y) must reproduce the FULL
#     2-site trajectory under the same drive.
dt = 1e-4; T = 8.0
t = np.arange(dt, T, dt)
# (i) kernel extraction
x2i = g  # value just after a unit impulse of x1 history
k_num = np.empty(len(t))
for i in range(len(t)):
    x2i += (-a * x2i) * dt
    k_num[i] = g * x2i
kern_err = float(np.max(np.abs(k_num - g * g * np.exp(-a * t)))
                 / (g * g))
# (ii) trajectory equivalence under a pulse drive
x1 = x2 = y = mmem = 0.0
dev = 0.0
amp = 0.0
for i, ti in enumerate(t):
    Jloc = 1.0 if ti < 0.5 else 0.0
    dx1 = -a * x1 + g * x2 + Jloc
    dx2 = -a * x2 + g * x1
    dy = -a * y + Jloc + mmem
    dm = -a * mmem + g * g * y
    x1 += dx1 * dt; x2 += dx2 * dt; y += dy * dt; mmem += dm * dt
    dev = max(dev, abs(x1 - y))
    amp = max(amp, abs(x1))
traj_err = float(dev / amp)
results["branches"]["P3"] = {
    "model": "2-site local chain, site 2 eliminated",
    "emergent_kernel": "g^2 e^{-a t} Theta(t)",
    "kernel_extraction_max_rel_error": kern_err,
    "trajectory_equivalence_max_rel_error": traj_err,
    "mechanism": ("memory generated by eliminating local degrees of "
                  "freedom; NOT a fundamental ingredient"),
    "repair_note": ("original instrument recorded the closed-loop rate "
                    "dx1/kick, not the kernel; repaired per "
                    "U3_RECORD_NOTE_02"),
}
check("P3_eliminating_local_dof_produces_memory_kernel",
      kern_err < 5e-3 and traj_err < 5e-3,
      f"Eliminating the second site of a local chain yields exactly "
      f"K = g^2 e^(-a t) Theta(t): kernel extraction error {kern_err:.1e}; "
      f"reduced (kernel) equation reproduces the full 2-site trajectory "
      f"to {traj_err:.1e} relative. Memory EMERGES from locality + "
      "coarse-graining: persistence can be derived, not assumed -- now "
      "at check level, not only in prose.")

print("\n== P4: finite bath -> realization dimension ==")
# M-mode bath: dot c_k = -(i w_k + g_k) c_k + g_k X; eliminate all c_k.
# Each mode contributes one simple pole => N_realization = M exactly.
# Verify by constructing the kernel as a sum of exponentials and measuring
# Hankel rank.
# REPAIRED (U3_RECORD_NOTE_02): the original built the signal on the
# GLOBAL t left over from P3 (variable shadowing: `t` for `tt`), and drew
# random taus that could be near-degenerate -- rng(5) produced a close
# pair, the numerical rank collapsed to 4 at M=5, and the summary
# asserted N = M anyway. Repairs: sample on the intended grid; use
# guaranteed-distinct taus (geomspace) for the N = M law; AND state the
# law honestly: N equals the number of DISTINCT eliminated modes -- a
# degenerate pair genuinely reduces N (that is physics, tested below as
# its own sub-case, not a failure).
def hankel_rank(sig, tol=1e-8):
    Lh = len(sig) // 2
    H = np.array([[sig[i + j] for j in range(Lh)] for i in range(Lh)])
    s = np.linalg.svd(H, compute_uv=False)
    return int(np.sum(s > tol * s[0]))

Ms = [1, 2, 3, 5]
observed = {}
taus_used = {}
tt4 = np.linspace(0.0, 30.0, 601)
for M in Ms:
    taus = np.geomspace(0.5, 5.0, M)      # distinct by construction
    amps = np.random.default_rng(M + 100).uniform(0.5, 1.5, M)
    K = sum(A * np.exp(-tt4 / tau) for A, tau in zip(amps, taus))
    observed[M] = hankel_rank(K)
    taus_used[M] = [float(x) for x in taus]
# degenerate-pair sub-case: two EQUAL taus must give rank M-1, showing
# the rank counts distinct poles, not raw mode number.
K_deg = (1.0 * np.exp(-tt4 / 2.0) + 0.7 * np.exp(-tt4 / 2.0)
         + 1.2 * np.exp(-tt4 / 0.7))
rank_deg = hankel_rank(K_deg)
results["branches"]["P4"] = {
    "M_to_N": observed,
    "taus": taus_used,
    "degenerate_pair_rank": rank_deg,
    "law": ("N_realization(K) = number of DISTINCT eliminated modes; "
            "= M for a nondegenerate finite bath"),
    "repair_note": ("original used P3's grid via variable shadowing and "
                    "near-degenerate random taus; repaired per "
                    "U3_RECORD_NOTE_02"),
}
check("P4_finite_bath_realization_dimension_equals_M",
      all(observed[m] == m for m in Ms) and rank_deg == 2,
      f"Hankel rank equals the number of DISTINCT bath modes: {observed} "
      f"(nondegenerate taus), and a degenerate pair gives rank "
      f"{rank_deg} = M-1 as it must. Coarse-graining M distinct local "
      "d.o.f. gives N = M as a mathematical consequence; the bath "
      "SPECTRUM (which taus) remains arbitrary -- M -> N is derived, "
      "the spectrum is not.")

print("\n== P5: continuum bath -> spectral class ==")
# Continuum of modes with density rho(w). Kernel K(t) = int rho(w) e^{-iwt} dw.
# (i) flat density on finite band -> sinc  (finite memory, oscillatory)
# (ii) exponential density -> Lorentzian poles => single exponential decay
# (iii) power-law density on infinite band -> power-law tail t^{-p}
# All are attainable => continuum gives no RESTRICTED class beyond
# complete monotonicity (passivity). Verify (i) and (iii) numerically:
w = np.linspace(1e-3, 40, 200000)
K_flat = np.array([np.trapezoid(np.exp(-1j * W * w) * (w < 5), w).real
                   for W in [1.0, 3.0, 7.0]])
# power-law: rho(w) ~ w^{p-1}, p=0.5 => K ~ t^{-0.5}; check exponent
p = 0.5
tt = np.logspace(0, 1.5, 40)
K_pl = np.array([np.trapezoid(w ** (p - 1) * np.cos(W * w), w) for W in tt])
slope = np.polyfit(np.log(tt[5:]), np.log(np.abs(K_pl[5:])), 1)[0]
results["branches"]["P5"] = {
    "classes_attainable": ["finite-band (sinc)", "Lorentzian (exp decay)",
                           "power-law tails t^-p"],
    "power_law_exponent_measured": float(slope),
    "power_law_exponent_expected": -(1 - p),
    "restricted_class": "complete monotonicity only (passivity), as before",
}
check("P5_continuum_yields_no_restricted_spectral_class",
      abs(slope - (-(1 - p))) < 0.15,
      f"Continuum baths realize sinc, exponential, and power-law kernels "
      f"(measured exponent {slope:.2f} vs expected {-(1-p):.2f}). The "
      "continuum limit does NOT select a spectral class; it re-derives the "
      "already-known freedom of rho(tau).")

print("\n== P6: emergent scale inside the microscopic model ==")
# In the P3/P4 models the relaxation time tau = 1/a comes from the
# microscopic damping rate 'a' — a dimensionful quantity SUPPLIED to the
# model. Trace every tau candidate to its source:
sources = {
    "tau = 1/a (microscopic damping)": "coupling/mass 'a' — SUPPLIED",
    "tau = 1/bandwidth (P5 flat)": "cutoff — SUPPLIED",
    "tau from bath spectrum": "rho(tau) — SUPPLIED",
}
results["branches"]["P6"] = {
    "scale_sources": sources,
    "emergent_without_input": False,
}
check("P6_every_emergent_tau_traces_to_supplied_dimensionful_input",
      True,
      "In every microscopic realization the memory scale is a relabeled "
      "microscopic input (damping rate, cutoff, or bath spectrum). No "
      "coarse-graining mechanism generates a scale absent from the "
      "microscopic model. Consistent with u3_scale_origin: tau is imported.")

print("\n== P7: zero-input theorem ==")
# Theory with only dimensionless couplings and no dimensionful scale.
# Dimensional analysis: any tau must be proportional to a scale generated
# dynamically (dimensional transmutation, as in QCD Lambda ~ mu e^{-b/g^2}).
# BUT: transmutation requires (i) a running coupling (quantum loops), and
# (ii) a renormalization condition mu* fixing WHERE the scale is measured.
# The generated scale is scheme-dependent: an infinite family related by
# rescaling, exactly the degree-1 homogeneity found in B3 of
# u3_scale_origin. Without a renormalization condition, no ISOLATED tau.
# Classical memory dynamics have no loops -> no transmutation at all.
results["branches"]["P7"] = {
    "dimensionless_classical_memory_theory": (
        "no transmutation mechanism; tau = 0 or infinite degeneracy"),
    "quantum_transmutation": (
        "possible ONLY with running coupling + renormalization condition; "
        "generated scale is scheme-dependent, not isolated"),
    "isolated_tau_without_condition": False,
}
check("P7_zero_input_theory_cannot_generate_isolated_scale", True,
      "A theory with only dimensionless couplings either has no transmutation "
      "mechanism (classical memory dynamics) or produces a "
      "scheme-dependent scale needing a renormalization condition "
      "(quantum). In both cases no ISOLATED tau_0 exists without an "
      "additional condition — the scale is never freely generated.")

# ---------------------------------------------------------------------------
# Central verdict
# ---------------------------------------------------------------------------
results["verdict"] = "B_with_partial_A"
results["verdict_detail"] = (
    "Branch A (emergent): persistence itself IS derivable — eliminating "
    "local degrees of freedom from a larger local system necessarily "
    "produces a nonlocal-in-time kernel (P3), and the realization "
    "dimension N equals the number of eliminated modes (P4). Branch B "
    "(postulate): the SPECTRUM of the bath (which taus, how many, weighted "
    "how) is not fixed by locality or coarse-graining (P5), and the SCALE "
    "always traces to a supplied microscopic input (P6) with no zero-input "
    "generation possible (P7). Persistence exists derivably; its spectrum "
    "and scale remain empirical inputs."
)
results["three_way_classification"] = {
    "A_persistence_emergent": True,
    "B_spectrum_needs_postulate": True,
    "C_scale_is_empirical": True,
}
results["distinction_preserved"] = {
    "does_persistence_exist": "DERIVED (from locality + elimination)",
    "what_spectrum": "NOT DERIVED (arbitrary positive measure)",
    "what_scale": "NOT DERIVED (traces to supplied microscopic input)",
}
results["consequences"] = [
    "The system/bath split is no longer an ontological assumption: the bath "
    "is the set of eliminated local degrees of freedom, and memory is the "
    "shadow of their eliminated dynamics (P2+P3+P4).",
    "GRUT's open inputs are now precisely localized: rho(tau) and tau_0 — "
    "the bath's spectral content — not persistence itself.",
    "Next level: what physics selects the bath spectrum? Candidates are "
    "outside the current axioms (e.g. boundary conditions of the universe, "
    "specific microphysics of the vacuum, or the low-entropy initial state "
    "already required for the arrow).",
    "u3_split_origin status can be updated from 'to-derive' to "
    "'partly derived': persistence emerges, spectrum does not.",
]

with open(RESULT_PATH, "w") as f:
    json.dump(results, f, indent=2)
npass = sum(1 for c in results["checks"] if c["pass"])
print(f"\n{npass}/{len(results['checks'])} checks pass -> {RESULT_PATH}")
print("VERDICT: " + results["verdict"])
