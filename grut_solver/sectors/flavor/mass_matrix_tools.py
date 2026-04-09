"""Generic fermion mass-matrix utilities."""
import numpy as np

def diagonalize(M: np.ndarray) -> dict:
    """Diagonalize a 3x3 mass matrix via SVD. Returns masses and mixing."""
    U, s, Vh = np.linalg.svd(M)
    return {"masses": np.sort(s), "U_L": U, "U_R": Vh.conj().T,
            "hierarchy": s.max()/(s.min()+1e-30)}

def mass_matrix_from_yukawas(y_up: np.ndarray, y_down: np.ndarray,
                              v: float = 246.0) -> dict:
    """Build diagonal mass matrices from Yukawa vectors (no mixing)."""
    M_up = np.diag(y_up) * v / np.sqrt(2)
    M_down = np.diag(y_down) * v / np.sqrt(2)
    return {"M_up": M_up, "M_down": M_down}
