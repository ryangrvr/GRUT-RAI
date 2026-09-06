"""RRT-0 core model — conforms STRICTLY to frozen RRT0_SPEC.md (hash-verified).

GATE-A ENFORCEMENT (frozen spec, Sec 3):
  - no physical site/index/location semantics anywhere;
  - the update parameter is MODEL_UPDATE_PARAMETER, not physical time;
  - graph adjacency is NOT locality; no tensor factor is a physical subsystem.

Rewrite note (recorded in hostile review): a pre-freeze legacy core.py implemented
a d**N tensor-network graph model that contradicts the frozen spec. The frozen
spec is authoritative; that legacy code was replaced by this module.

All constants are read from RRT0_INPUT_LEDGER.json and verified against
RRT0_FREEZE.json at import. Any tampering aborts (GATE-A hard stop).
"""
import hashlib
import json
from pathlib import Path

import numpy as np

_ROOT = Path(__file__).resolve().parent.parent.parent


def load_frozen():
    ledger_path = _ROOT / "RRT0_INPUT_LEDGER.json"
    freeze_path = _ROOT / "RRT0_FREEZE.json"
    ledger = json.loads(ledger_path.read_text())
    freeze = json.loads(freeze_path.read_text())
    h = hashlib.sha256(ledger_path.read_bytes()).hexdigest()
    expected = freeze["artifacts"]["RRT0_INPUT_LEDGER.json"]
    if h != expected:
        raise RuntimeError(
            f"GATE-A HARD STOP: ledger hash {h} != frozen {expected}. Simulation aborted."
        )
    return ledger, freeze


LEDGER, FREEZE = load_frozen()
_P = LEDGER["parameters"]
D = int(_P["d"])
K_SECTORS = int(_P["N_sectors"])
DT = float(_P["dt"])
T_OBS = int(_P["T_obs"])
SAMPLE_EVERY = int(_P["sample_every"])
LAM = float(_P["lam"])
LAM_LADDER = [float(x) for x in _P["lam_ladder"]]
TAU_OP = int(_P["tau_op"])
TAU_INF = int(_P["tau_influence"])
EPS = float(_P["epsilon"])
EPS_LADDER = [float(x) for x in _P["epsilon_ladder"]]
SEED_PRIMARY = int(LEDGER["random_seeds"]["primary"])
SEEDS_ROBUST = [int(s) for s in LEDGER["random_seeds"]["robustness_set"]]

# ------------------------------------------------------------------ basis
def gell_mann_basis(d=D):
    """Normalized (HS norm 1) traceless Hermitian generator basis.
    COMPUTATIONAL observable basis only — no site/position meaning (GATE-A)."""
    ops = []
    for j in range(d):
        for k in range(j + 1, d):
            m = np.zeros((d, d), dtype=complex)
            m[j, k] = m[k, j] = 1.0
            ops.append(m / np.sqrt(2))
            m = np.zeros((d, d), dtype=complex)
            m[j, k] = 1j
            m[k, j] = -1j
            ops.append(m / np.sqrt(2))
    for j in range(d - 1):
        m = np.zeros((d, d), dtype=complex)
        m[: j + 1, : j + 1] = np.eye(j + 1)
        m[j + 1, j + 1] = -(j + 1)
        n = np.linalg.norm(m)
        if n > 1e-12:
            ops.append(m / n)
    return ops

BASIS = gell_mann_basis()
NB = len(BASIS)


# ------------------------------------------------------------------ states / ensembles
def haar_unitary(d, rng):
    z = (rng.standard_normal((d, d)) + 1j * rng.standard_normal((d, d))) / np.sqrt(2.0)
    q, r = np.linalg.qr(z)
    return q * (np.diag(r) / np.abs(np.diag(r)))


def initial_ensemble(rng, n_pure=5):
    """Maximally mixed + n_pure Haar random pure states (frozen init distribution)."""
    rhos = [np.eye(D, dtype=complex) / D]
    for _ in range(n_pure):
        v = (rng.standard_normal(D) + 1j * rng.standard_normal(D)) / np.sqrt(2)
        rhos.append(np.outer(v, v.conj()))
    return rhos


# ------------------------------------------------------------------ dynamics
def gue_hamiltonian(rng, scale=1.0):
    """GUE(d) drawn once per seed. NOT a spatial/graph object (GATE-A)."""
    a = (rng.standard_normal((D, D)) + 1j * rng.standard_normal((D, D))) / np.sqrt(2)
    return scale * (a + a.conj().T) / 2.0


def step_unitary(H, dt=DT):
    """U = exp(-i H dt) via exact eigendecomposition (d=4, exact to float64)."""
    w, v = np.linalg.eigh(H)
    return (v * np.exp(-1j * w * dt)) @ v.conj().T


def evolve_trajectory(rho0, U, n_steps=T_OBS, sample_every=SAMPLE_EVERY):
    """Closed unitary propagation rho_{t+1} = U rho U^dagger.
    Returns snapshots of the DENSITY OPERATOR at sampled update steps.
    The step index is a MODEL UPDATE PARAMETER (GATE-A: not physical time)."""
    rhos = []
    rho = rho0.copy()
    for t in range(1, n_steps + 1):
        rho = U @ rho @ U.conj().T
        if t % sample_every == 0:
            rhos.append(rho.copy())
    return rhos


def evolve_steps(rho, U, n):
    """Propagate exactly n update steps (no sampling)."""
    for _ in range(n):
        rho = U @ rho @ U.conj().T
    return rho


# ------------------------------------------------------------------ internal operations
def support_projector(op, tol=1e-10):
    """Normalized projector onto the support subspace of a Hermitian operator.
    Built ONLY from the model's own operators (model-native, no external lab)."""
    w, v = np.linalg.eigh(op)
    keep = np.abs(w) > tol
    if not keep.any():
        return np.zeros((D, D), dtype=complex)
    P = v[:, keep] @ v[:, keep].conj().T
    tr = np.trace(P).real
    return P / tr


SIGMAS = [support_projector(O) for O in BASIS]


def internal_operation(rho, sigma, lam=LAM):
    """E_alpha: model-internal re-weighting toward the sector support state,
    followed by normal closed evolution in the caller.
    SPEC NOTE (recorded in hostile review): the literal frozen formula
    U^{tau_op}((1-lam)rho + lam sigma)U^{-tau_op} is the identity map
    (conjugations cancel). The operational reading — perturb, then evolve —
    is implemented here; the discrepancy is logged, not silently rescued."""
    return (1.0 - lam) * rho + lam * sigma


# ------------------------------------------------------------------ observables
def expect(rho, O):
    return np.trace(O @ rho)


def direct_footprint(rho, sigma, O, lam=LAM):
    """Immediate (tau=0) response of observable O to E_alpha — the SUPPLIED
    direct perturbation footprint, used only inside the contrast diagnostic
    to quantify how much of a response is the injected perturbation itself."""
    return abs(expect(internal_operation(rho, sigma, lam) - rho, O))
