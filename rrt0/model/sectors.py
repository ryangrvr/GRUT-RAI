"""Sector discovery (frozen S1 primary, S2 secondary) — no post-hoc choice."""
import numpy as np
from rrt0.model.core import BASIS, NB, D, support_projector, LEDGER

K = int(LEDGER["parameters"]["N_sectors"])


def kmeans(X, k, rng, iters=100, n_init=10):
    best = None
    for _ in range(n_init):
        C = X[rng.choice(len(X), k, replace=False)].copy()
        lab = None
        for _ in range(iters):
            d2 = ((X[:, None, :] - C[None, :, :]) ** 2).sum(-1)
            new = d2.argmin(1)
            if lab is not None and (new == lab).all():
                break
            lab = new
            for j in range(k):
                if (lab == j).any():
                    C[j] = X[lab == j].mean(0)
        d2 = ((X[:, None, :] - C[None, :, :]) ** 2).sum(-1)
        inertia = d2.min(1).sum()
        if best is None or inertia < best[0]:
            best = (inertia, lab.copy())
    return best[1]


def probe_influence_rows(U, lam_probe, tau, rng):
    """Bootstrap influence matrix among BASIS operators:
    row a = response of all basis ops to perturbation sigma_a, at fixed tau.
    Used ONLY for blind clustering (pre-registered)."""
    from rrt0.model.core import evolve_steps, internal_operation
    rows = []
    for a in range(NB):
        row = np.zeros((NB,), dtype=float)
        for rho in [np.eye(D, dtype=complex) / D]:
            # REPAIR (Phase-2 semantic decision): was `BASIS[a] and _sig(a)`,
            # a Python truthiness defect returning BASIS[a] itself. The
            # spec-consistent intervention state is sigma_alpha = _sig(a).
            rp = internal_operation(rho, _sig(a), lam_probe)
            rp = evolve_steps(rp, U, tau)
            rb = evolve_steps(rho, U, tau)
            for b in range(NB):
                row[b] = abs(np.trace(BASIS[b] @ (rp - rb)))
        rows.append(row)
    return np.array(rows)


def _sig(a):
    return support_projector(BASIS[a])


def discover_sectors(U, rng):
    """PRIMARY S1: kmeans k=K on influence rows. Returns list of op-index lists."""
    X = probe_influence_rows(U, float(LEDGER["parameters"]["lam"]), 5, rng)
    labels = kmeans(X, K, rng)
    clusters = [[a for a in range(NB) if labels[a] == j] for j in range(K)]
    return [c for c in clusters if c]


def commutant_sectors(U):
    """SECONDARY S2 (frozen): spectral projectors of H inside U's generator.

    FORBIDDEN ROUTE (superseded): this function previously diagonalized the
    unitary U directly with np.linalg.eigh(U). U is unitary, NOT Hermitian,
    so eigh silently returned garbage (the root cause of the superseded
    failed audit reports/REDUCIBILITY_GATE.FAILED-eigh_on_unitary-*.json).
    Any future implementation MUST decompose the Hermitian generator H, e.g.
    w, v = np.linalg.eigh(H); H is available from the same seed via
    model.core.gue_hamiltonian. This stub is retained as provenance and to
    make the invalid route impossible to call accidentally."""
    raise NotImplementedError(
        "commutant_sectors: the eigh(U) route is invalid (U is unitary, "
        "not Hermitian); rebuild this on the Hermitian generator H only."
    )
