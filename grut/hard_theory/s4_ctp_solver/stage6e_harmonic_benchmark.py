"""Stage 6E vector/tensor harmonic sector benchmarking on S4."""

from typing import Dict

from grut.hard_theory.s4_ctp_solver.s4_harmonic_spectra import (
    define_s4_harmonic_spectra,
)
from grut.hard_theory.s4_ctp_solver.s4_vector_harmonics import (
    build_vector_harmonics_structure,
)
from grut.hard_theory.s4_ctp_solver.s4_tensor_harmonics_extended import (
    extend_tensor_harmonics,
)
from grut.hard_theory.s4_ctp_solver.harmonic_consistency_checks import (
    check_harmonic_consistency,
)
from grut.hard_theory.s4_ctp_solver.stage5c_tensor_native import (
    evaluate_tensor_native_attempt,
)
from grut.hard_theory.s4_ctp_solver.tensor_placeholder_guard import (
    enforce_tensor_placeholder_guard,
)


def run_stage6e_harmonic_benchmark() -> Dict[str, object]:
    spectra = define_s4_harmonic_spectra()
    vector_structure = build_vector_harmonics_structure()
    tensor_structure = extend_tensor_harmonics()
    consistency = check_harmonic_consistency(
        spectra,
        vector_structure,
        tensor_structure,
    )

    ready_for_tt = (
        consistency["status"] == "consistent"
        and tensor_structure.get("status") == "structural_placeholder"
    )

    guard = enforce_tensor_placeholder_guard(evaluate_tensor_native_attempt())

    return {
        "stage": "6E",
        "status": "harmonic_sector_benchmark",
        "scalar_modes_defined": bool(spectra.get("scalar_modes")),
        "vector_modes_defined": bool(spectra.get("vector_modes")),
        "tensor_modes_placeholder": tensor_structure.get("status") == "structural_placeholder",
        "consistency_status": consistency.get("status"),
        "ready_for_tt_propagator": ready_for_tt,
        "can_extract": False,
        "can_compute_r": False,
        "promotes_claims": False,
        "spectra": spectra,
        "vector_structure": vector_structure,
        "tensor_structure": tensor_structure,
        "consistency": consistency,
        "guard": guard,
    }
