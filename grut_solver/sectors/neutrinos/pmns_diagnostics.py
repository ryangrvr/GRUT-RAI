"""PMNS matrix diagnostics — unitarity and angle summary."""
import numpy as np

# PDG central values (approximate |U| magnitudes)
PMNS_PDG = np.array([
    [0.821, 0.550, 0.149],
    [0.352, 0.579, 0.707],
    [0.417, 0.597, 0.693],
], dtype=float)

MIXING_ANGLES_DEG = {"theta_12": 33.4, "theta_23": 49.0, "theta_13": 8.6}
DELTA_CP_DEG = 195.0  # hint, not precise

def unitarity_check(U: np.ndarray = None) -> dict:
    """Check U^dag U ~ I (approximate for |U| magnitudes)."""
    if U is None:
        U = PMNS_PDG
    product = U.T @ U
    off = float(np.max(np.abs(product - np.eye(3))))
    return {"max_off_diagonal": off, "status": "PASS" if off < 0.1 else "MARGINAL"}

def angle_summary() -> dict:
    """Mixing angle summary with status."""
    return {**MIXING_ANGLES_DEG, "delta_CP_deg": DELTA_CP_DEG,
            "note": "All values are measured inputs. NOT derived from GRUT."}
