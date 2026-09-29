# EA-0 independent verification: ABSTRACT qubit-toy lemma check (not a physics member; no declared substrate evaluated).
"""S2: explicit L7 test cases on 2-3 qubits (x=0, y=1, spectator s=2)."""
import numpy as np
from common import *

def report(name, H, P, n, x=0, y=1):
    assert np.linalg.norm(comm(H, P)) < 1e-12, "P not H-invariant"
    hxy = h_xy_part(H, x, y, n)
    PhP = P @ hxy @ P
    r = int(round(np.trace(P).real))
    scal = np.linalg.norm(PhP - (np.trace(PhP) / r) * P)
    # does P commute with some traceless op at x ?  (dimension of local commutant at x)
    print(f"{name:55s} rank P={r}  Gamma edge={edge_strength(H, np.eye(2**n), x, y, n):.3f}  "
          f"Gamma(rho) edge={edge_strength(H, P, x, y, n):.3e}  ||P h_xy P - scalar||={scal:.3f}")
    return PhP

P0 = (I2 + Z) / 2; P1 = (I2 - Z) / 2
n = 3
J, h = 1.0, 0.7
# (A) ZZ coupling + transverse field on y + spectator coupling; sector Z_x=+1 (rank 4 of 8)
H = J * site_op(Z, 0, n) @ site_op(Z, 1, n) + h * site_op(X, 1, n) + 0.4 * site_op(X, 1, n) @ site_op(X, 2, n) + 0.3 * site_op(Z, 2, n)
P = kron(P0, I2, I2)
PhP = report("A: JZxZy + hXy + ..., sector Zx=+1 (x frozen)", H, P, n)
print("   P h_xy P == J * P Z_y P ?", np.linalg.norm(PhP - J * P @ site_op(Z, 1, n) @ P))
# check that reach of a generic rho in the sector IS the full sector
V = P @ (np.random.default_rng(0).normal(size=(8, 4)) + 0j)
Pk, rk = krylov_projector(H, V); print("   Krylov rank from generic rho in sector:", rk, " equals P:", np.linalg.norm(Pk - P) < 1e-9)

# (B) same H, sector ZxZy parity? not invariant because of hXy; use pure ZZ, 2 qubits, parity-even sector span{00,11}
n2 = 2
H = site_op(Z, 0, n2) @ site_op(Z, 1, n2)
Peven = kron(P0, P0) + kron(P1, P1)
report("B: H=ZxZy, sector span{00,11} (coupling = scalar +1)", H, Peven, n2)
# (C) same H, eigenstate |00>
report("C: H=ZxZy, eigenstate |00> (rank 1)", H, kron(P0, P0), n2)
# (D) hopping XX+YY, number sectors, 3 qubits with hopping also to spectator
n = 3
Hh = (site_op(X, 0, n) @ site_op(X, 1, n) + site_op(Y, 0, n) @ site_op(Y, 1, n)
      + 0.6 * (site_op(X, 1, n) @ site_op(X, 2, n) + site_op(Y, 1, n) @ site_op(Y, 2, n))
      + 0.2 * site_op(Z, 0, n) + 0.5 * site_op(Z, 2, n))
Ntot = sum((I2 - Z) / 2 if False else None for _ in []) if False else None
Nop = sum(site_op((np.eye(2) - Z) / 2, s, n) for s in range(n))
w, U = np.linalg.eigh(Nop)
for N in range(4):
    Q = U[:, np.abs(w - N) < 1e-9]; PN = Q @ Q.conj().T
    report(f"D: hopping, number sector N={N}", Hh, PN, n)
# (E) P-6 L-C Hamiltonian, even block
n2 = 2
HC = 0.9 * (site_op(Z, 0, n2) + site_op(Z, 1, n2)) + 0.7 * site_op(X, 0, n2) @ site_op(X, 1, n2)
report("E: P-6 H_C, even-parity block", HC, Peven, n2)
# (F) coupling non-scalar on BOTH sites inside the sector but sector = local product projector
#     x = qubit0, y = qubit1; H = Zx Zy + Xx Xy ... sector must commute: use x-local conserved Zx only if coupling commutes with Zx
H = site_op(Z, 0, 3) @ (site_op(Z, 1, 3) + site_op(X, 1, 3)) + site_op(Z, 0, 3) @ site_op(X, 2, 3) + site_op(Y, 1, 3) @ site_op(Y, 2, 3)
report("F: Zx(Zy+Xy)+ZxXs+YyYs, sector Zx=+1", H, kron(P0, I2, I2), 3)
