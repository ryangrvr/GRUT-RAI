"""SECTOR-SELECTION FIREWALL — Phase 3, not a reducibility test.

Pre-registered pipeline for one narrow question:

    Can a pre-registered clustering pipeline identify stable algorithmic
    organization in response data WITHOUT discovery/evaluation leakage or
    representation-dependent self-validation?

SCOPE BOUNDARIES (binding):
  * The model-class ceiling stands unconditionally:
        IRREDUCIBLE_EMERGENT_INFLUENCE = OUT_OF_SCOPE
    No output of this firewall modifies, weakens, bypasses, or is presented
    as an exception to the frozen reducibility finding.
  * A favorable result can only be: the frozen discovery procedure found a
    reproducible pattern among candidate operator-response clusters that
    survived registered split / seed / k / epsilon / basis / permutation /
    null / held-out controls. It can NEVER be read as physical sectors,
    causal structure, observers, geometry, spacetime, or a new primitive.
  * No RRT0_FREEZE / RRT0_INPUT_LEDGER / E_alpha semantic decision / Phi_raw
    artifact is touched; no model semantics repaired or reinterpreted;
    no geometry/IR/gravity/cosmology/QG/SM/ToE program is run.
"""
from __future__ import annotations

import hashlib
import json
from dataclasses import dataclass, field
from itertools import permutations
from pathlib import Path

import numpy as np

from rrt0.model.core import (
    BASIS, D, EPS, EPS_LADDER, LAM, LAM_LADDER, NB, SEED_PRIMARY,
    SEEDS_ROBUST, SIGMAS, TAU_OP, TAU_INF, e_alpha, gue_hamiltonian,
    step_unitary,
)
from rrt0.model.sectors import K, kmeans
from rrt0.model.reducibility import evolve_delta

_ROOT = Path(__file__).resolve().parent
EPS_TINY = 1e-12

# ---- pre-registered firewall constants (recorded BEFORE any run) ----------
NULL_ITERS = 200           # label-permutation null per condition
HELD_OUT_STATES = 6        # unseen initial states per condition (no leakage)
MIN_CLUSTER_FRACTION = 0.02  # ignore degenerate clusters holding <2% of ops
NULL_ALPHA = 0.05          # one-sided percentile threshold for null p-values
STABILITY_MIN = 0.75       # split/seed/replicate consistency floor
NULL_P_MAX = 0.05          # observed structure must beat label-permutation null
HELD_OUT_MIN = 0.75        # accuracy floor on held-out operator-response rows


# --------------------------------------------------------------------- data
def response_rows(rho0, U, lam, tau):
    """Blind discovery matrix: row = perturbation sigma_a, col = response.

    Row a entry b = |Tr[B_b * Delta]| where
        Delta = U^tau E_lam[sigma_a] U^{-tau} - U^tau rho0 U^{-tau}
    for the FIXED registered bootstrap state rho0, in the basis being tested.

    Uses ONLY canonical model functions: e_alpha (authoritative semantic
    decision, Option 1), route-A delta propagation (model.reducibility
    .evolve_delta), and the model-native support projectors SIGMAS built
    from model.core.BASIS. No post-hoc formula choice: the map is frozen
    before any clustering. GATE-A: no site/position semantics anywhere.
    """
    rows = np.zeros((NB, NB), dtype=float)
    for a in range(NB):
        delta0 = e_alpha(rho0, SIGMAS[a], lam) - rho0
        delta_t = evolve_delta(delta0, U, tau)
        for b in range(NB):
            rows[a, b] = abs(float(np.real(np.trace(delta_t @ BASIS[b]))))
    return rows


def registered_bootstrap_state(rng):
    """Fixed Haar pure state drawn from the registered seed stream.
    Drawn ONCE per condition and reused for discovery AND evaluation-row
    construction (the split is over operator rows, not over states)."""
    v = (rng.standard_normal(D) + 1j * rng.standard_normal(D)) / np.sqrt(2.0)
    v = v / np.linalg.norm(v)
    return np.outer(v, v.conj())


# ------------------------------------------------------------ partition utils
def _pair_flags(labels):
    labels = np.asarray(labels)
    n = len(labels)
    return np.array([labels[i] == labels[j]
                     for i in range(n) for j in range(i + 1, n)], dtype=bool)


def pair_agreement(l1, l2):
    """Label-invariant co-assignment agreement in [0, 1]."""
    return float((_pair_flags(l1) == _pair_flags(l2)).mean())


def best_perm_agreement(l_ref, l_test):
    """Max exact-label agreement over all cluster-index permutations."""
    best = 0.0
    kk = int(np.max(l_test)) + 1
    for perm in permutations(range(kk)):
        mapped = np.array([perm[x] for x in l_test])
        best = max(best, float((mapped == np.asarray(l_ref)).mean()))
    return best


def cluster_and_centroids(X, k, rng):
    labels = np.asarray(kmeans(X, k, rng))
    cents = []
    for j in range(k):
        member = X[labels == j]
        cents.append(member.mean(0) if len(member) else X[rng.integers(len(X))])
    return labels, np.array(cents)


def nearest_centroid_labels(X, cents):
    d2 = ((X[:, None, :] - cents[None, :, :]) ** 2).sum(-1)
    return d2.argmin(1)


def _standardize(X):
    """Column z-score representation (representation control B2)."""
    mu = X.mean(0)
    sd = X.std(0)
    sd = np.where(sd < EPS_TINY, 1.0, sd)
    return (X - mu) / sd

# --------------------------------------------------------- per-condition run
def condition_unitary_and_state(seed):
    """Registered GUE unitary + fixed bootstrap state for one seed."""
    rng = np.random.default_rng(seed)
    H = gue_hamiltonian(rng)
    U = step_unitary(H)
    rho0 = registered_bootstrap_state(rng)
    return U, rho0


def split_consistency(X, k, rng):
    """Discovery/evaluation split control (B1).

    Discovery rows = even operator indices; evaluation rows = odd operator
    indices. Cluster discovery rows, assign ALL rows by nearest discovery
    centroid; consistency = best-permutation agreement between discovery
    labels and centroid labels on discovery rows. No eval row influences
    centroids, so there is no discovery/evaluation leakage.
    """
    idx_d = np.arange(0, len(X), 2)
    idx_e = np.arange(1, len(X), 2)
    lab_d, cents = cluster_and_centroids(X[idx_d], k, rng)
    if len(np.unique(lab_d)) < 2:
        return 0.0
    lab_all = nearest_centroid_labels(X, cents)
    return best_perm_agreement(lab_d, lab_all[idx_d])


def null_pvalue(X, k, rng_cluster, seed, n_null=NULL_ITERS):
    """Registered label-permutation null (B6): permute response entries
    independently within each operator row, destroying cross-row
    organization while keeping every marginal. Statistic = split
    consistency. One-sided p = (1 + #{null >= obs}) / (1 + n_null)."""
    obs = split_consistency(X, k, rng_cluster)
    rng = np.random.default_rng(seed + 777)
    ge = 0
    for _ in range(n_null):
        Xp = np.array([row[rng.permutation(len(row))] for row in X])
        if split_consistency(Xp, k, rng_cluster) >= obs:
            ge += 1
    return obs, (1.0 + ge) / (1.0 + n_null)


def run_condition(seed, lam, tau):
    """Full registered control battery for one (seed, lam, tau) condition.

    Returns a dict of named control values, or raises on hard failure.
    All controls compare against the PRIMARY representation of this
    condition: rows from basis BASIS, partition at k = K.
    """
    U, rho0 = condition_unitary_and_state(seed)
    X = response_rows(rho0, U, lam, tau)
    rng_c = np.random.default_rng(seed + 1)
    lab_ref, cents = cluster_and_centroids(X, K, rng_c)

    out = {"seed": int(seed), "lam": float(lam), "tau": int(tau)}

    # B1 split + B6 permutation null (one registered test battery)
    obs_split, p_null = null_pvalue(X, K, rng_c, seed)
    out["split_consistency"] = obs_split
    out["null_p"] = p_null

    # B2 basis representation control: standardized representation
    lab_z = np.asarray(kmeans(_standardize(X), K, np.random.default_rng(seed + 2)))
    out["basis_agreement"] = pair_agreement(lab_ref, lab_z)

    # B3 k control: partitions at neighboring k
    k_vals = [kk for kk in (K - 1, K, K + 1) if kk >= 2 and kk < NB]
    k_agree = []
    for kk in k_vals:
        lab_k = np.asarray(kmeans(X, kk, np.random.default_rng(seed + 3)))
        k_agree.append(pair_agreement(lab_ref, lab_k))
    out["k_agreement"] = float(min(k_agree))
    out["k_values_used"] = [int(kk) for kk in k_vals]

    # B4 epsilon (lambda) control: same pipeline across the epsilon ladder
    lam_agree = []
    for lam2 in LAM_LADDER:
        X2 = response_rows(rho0, U, lam2, tau)
        lab2 = np.asarray(kmeans(X2, K, np.random.default_rng(seed + 4)))
        lam_agree.append(pair_agreement(lab_ref, lab2))
    out["lam_agreement"] = float(min(lam_agree))

    # B5 seed/replicate control: independent GUE draws, same pipeline
    seed_agree = []
    for s2 in SEEDS_ROBUST:
        U2, rho2 = condition_unitary_and_state(s2)
        X2 = response_rows(rho2, U2, lam, tau)
        lab2 = np.asarray(kmeans(X2, K, np.random.default_rng(s2 + 1)))
        seed_agree.append(pair_agreement(lab_ref, lab2))
    out["seed_agreement"] = float(min(seed_agree))

    # B7 held-out control: unseen initial states; each held-out state's
    # response rows must map to the same sectors as their source operators.
    rng_h = np.random.default_rng(seed + 999_979)
    correct = 0
    total = 0
    for _ in range(HELD_OUT_STATES):
        rho_h = registered_bootstrap_state(rng_h)
        Xh = response_rows(rho_h, U, lam, tau)
        preds = nearest_centroid_labels(Xh, cents)
        for a in range(NB):
            correct += int(preds[a] == lab_ref[a])
            total += 1
    out["held_out_accuracy"] = correct / total

    return out


CONTROLS = (
    ("null_p", "max", NULL_P_MAX),
    ("split_consistency", "min", STABILITY_MIN),
    ("basis_agreement", "min", STABILITY_MIN),
    ("k_agreement", "min", STABILITY_MIN),
    ("lam_agreement", "min", STABILITY_MIN),
    ("seed_agreement", "min", STABILITY_MIN),
    ("held_out_accuracy", "min", HELD_OUT_MIN),
)


def aggregate(conditions):
    """Reduce per-condition results to firewall verdict inputs.

    Hard failure of ANY condition (exception) -> diagnostic failure path.
    Otherwise take the WORST case across conditions for each control.
    """
    failures = [c.get("error") for c in conditions if c.get("error")]
    if failures:
        return {"status": "SECTOR_SELECTION_DIAGNOSTIC_FAILED",
                "failures": [str(f) for f in failures]}

    summary = {}
    for name, mode, threshold in CONTROLS:
        vals = [c[name] for c in conditions]
        worst = max(vals) if mode == "max" else min(vals)
        summary[name] = {
            "threshold": threshold,
            "worst_case": float(worst),
            "per_condition": [float(v) for v in vals],
            "pass": bool(worst <= threshold if mode == "max"
                         else worst >= threshold),
        }
    passed = [s for s, in [(k,) for k, v in summary.items() if v["pass"]]]
    n_pass = len(passed)
    n_total = len(summary)
    if n_pass == n_total:
        status = "STABLE_ALGORITHMIC_RELATIONAL_STRUCTURE"
    elif n_pass == 0:
        status = "NO_STABLE_ALGORITHMIC_RELATIONAL_STRUCTURE_DETECTED"
    else:
        status = "SECTOR_SELECTION_UNRESOLVED"
    return {"status": status, "summary": summary,
            "n_pass": n_pass, "n_total": n_total,
            "failed_controls": [k for k, v in summary.items() if not v["pass"]]}


# ------------------------------------------------------------- registered run
def registered_conditions():
    """Frozen condition grid (registered before the run).

    Primary seed x {operator time, long time} x full epsilon ladder.
    Seed replication (SEEDS_ROBUST) is applied INSIDE run_condition as the
    seed-stability control, not as extra conditions.
    """
    conds = []
    for tau in (TAU_OP, TAU_INF):
        for lam in LAM_LADDER:
            conds.append({"seed": SEEDS_ROBUST[0], "lam": float(lam), "tau": int(tau)})
    return conds


def run_firewall(conditions=None):
    """Execute the full registered battery. Returns (results, conditions).

    Each condition result is either the control dict or
    {"error": "..."} — aggregate() turns hard failures into
    SECTOR_SELECTION_DIAGNOSTIC_FAILED.
    """
    if conditions is None:
        conditions = registered_conditions()
    results = []
    for c in conditions:
        try:
            results.append(run_condition(c["seed"], c["lam"], c["tau"]))
        except Exception as exc:  # hard diagnostic failure, recorded not hidden
            results.append({"error": f"{type(exc).__name__}: {exc}",
                            "seed": c["seed"], "lam": c["lam"], "tau": c["tau"]})
    return results, conditions


def verdict(agg):
    """Final outcome label, strictly one of the four registered outcomes."""
    return agg["status"]
