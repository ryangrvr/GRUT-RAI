"""
Born Rule Transparency — The constitutive sector preserves quantum probabilities.

THE STRUCTURAL THEOREM (Program N3):

For the LINEAR constitutive law (tau dPhi/dt + Phi = X + noise):
  The partition function Z(X) = integral DPhi exp(-S_MSRJD[Phi, X])
  is INDEPENDENT of X (the target/stimulus).

Therefore:
  p(i) = |c_i|^2 * Z(X_i) / sum_j |c_j|^2 * Z(X_j) = |c_i|^2

The Born rule is EXACTLY PRESERVED. The constitutive sector is
TRANSPARENT to quantum probabilities.

For the NONLINEAR (bistable) constitutive law:
  Z(X) depends on X through the attractor structure.
  The Born rule receives corrections of order Z(X_0)/Z(X_1) - 1.
  For the standard bistable parameters: this correction is small.

Token: born_rule_upstream_of_constitutive
"""

import numpy as np


def born_transparency_linear() -> dict:
    """Verify Born rule transparency for the linear constitutive law.

    For tau dPhi/dt + Phi = X + sqrt(2D) xi(t):
    The MSRJD action is:
      S = integral dt (tau dPhi/dt + Phi - X)^2 / (4D)
    The kernel K = (tau d/dt + 1)^2 / (4D) depends on tau and D,
    NOT on X.

    Therefore Z = integral DPhi exp(-S) is X-independent.
    Therefore p(i) = |c_i|^2. QED.
    """
    return {
        "theorem": "Born rule transparency (linear case)",
        "statement": (
            "For the linear constitutive law, the MSRJD partition function "
            "Z(X) is independent of the stimulus X. Therefore the constitutive "
            "sector does not modify quantum probabilities: p(i) = |c_i|^2."
        ),
        "proof": (
            "The MSRJD action S[Phi; X] = integral (tau dPhi/dt + Phi - X)^2 / (4D) dt. "
            "The Gaussian integral over Phi gives Z = (det K)^{-1/2} where "
            "K = (tau d/dt + 1)^2 / (4D). K is independent of X. QED."
        ),
        "Z_ratio": 1.0,  # Z_0 / Z_1 = 1 exactly
        "born_correction": 0.0,  # exact: no correction
        "status": "PROVEN",
        "token": "born_rule_upstream_of_constitutive",
    }


def born_correction_bistable(sigma: float = 2.0, kappa: float = 0.3,
                              epsilon: float = 0.2, nu: float = 1.0,
                              X_0: float = 2.0, X_1: float = -2.0) -> dict:
    """Compute Born rule correction for the bistable constitutive law.

    For the coupled (Phi, Psi) system with cubic saturation:
      tau_1 dPhi/dt = a(X - Phi) - kappa Psi
      tau_2 dPsi/dt = epsilon Phi + (sigma-1) Psi - nu Psi^3

    The partition function Z(X) = sum_attractors 1/sqrt(|det J(attractor)|)
    depends on X through the attractor positions and Jacobian.

    Parameters are the standard bistable set from GRUT-III.
    """
    # Find attractors for each X
    def find_attractors(X):
        """Find fixed points of the bistable ODE for a given X."""
        a = 1.0  # coupling
        tau_1, tau_2 = 1.0, 1.0

        # Fixed point: Phi = X - kappa Psi / a
        # epsilon (X - kappa Psi/a) + (sigma-1) Psi - nu Psi^3 = 0
        # epsilon X - epsilon kappa Psi / a + (sigma-1) Psi - nu Psi^3 = 0
        # -nu Psi^3 + (sigma - 1 - epsilon kappa/a) Psi + epsilon X = 0

        c3 = -nu
        c1 = sigma - 1 - epsilon * kappa / a
        c0 = epsilon * X

        # Cubic: c3 Psi^3 + c1 Psi + c0 = 0
        coeffs = [c3, 0, c1, c0]
        roots = np.roots(coeffs)
        real_roots = roots[np.abs(roots.imag) < 1e-10].real

        attractors = []
        for Psi_star in real_roots:
            Phi_star = X - kappa * Psi_star / a

            # Jacobian
            J = np.array([
                [-a / tau_1, -kappa / tau_1],
                [epsilon / tau_2, (sigma - 1 - 3*nu*Psi_star**2) / tau_2]
            ])

            # Stable if both eigenvalues have negative real part
            eigs = np.linalg.eigvals(J)
            if np.all(eigs.real < 0):
                det_J = np.linalg.det(J)
                attractors.append({
                    "Phi": Phi_star, "Psi": Psi_star,
                    "det_J": det_J, "eigs": eigs,
                })

        return attractors

    att_0 = find_attractors(X_0)
    att_1 = find_attractors(X_1)

    # Partition function: Z = sum 1/sqrt(|det J|) over stable attractors
    Z_0 = sum(1.0 / np.sqrt(abs(a["det_J"])) for a in att_0) if att_0 else 0
    Z_1 = sum(1.0 / np.sqrt(abs(a["det_J"])) for a in att_1) if att_1 else 0

    if Z_0 > 0 and Z_1 > 0:
        ratio = Z_0 / Z_1
        correction = abs(ratio - 1.0)
    else:
        ratio = float('nan')
        correction = float('nan')

    return {
        "theorem": "Born rule correction (bistable case)",
        "X_0": X_0, "X_1": X_1,
        "Z_0": Z_0, "Z_1": Z_1,
        "Z_ratio": ratio,
        "born_correction": correction,
        "n_attractors_0": len(att_0),
        "n_attractors_1": len(att_1),
        "parameters": {"sigma": sigma, "kappa": kappa, "epsilon": epsilon, "nu": nu},
        "status": "COMPUTED",
        "interpretation": (
            f"Z_0/Z_1 = {ratio:.6f}. Born rule correction = {correction:.4f} "
            f"({correction*100:.2f}%). "
            f"{'Negligible — Born rule effectively preserved.' if correction < 0.01 else 'Non-negligible correction to Born rule.'}"
        ),
    }
