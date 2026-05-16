"""Assemble a symbolic loop-integrand scaffold."""

from typing import Dict


def assemble_loop_integrand_scaffold(components: Dict[str, object]) -> Dict[str, object]:
    symbolic_form = (
        "symmetry_factor * vertices * propagators * index_structure"
    )
    integrand_summary = {
        "propagator_count": len(components.get("propagators", [])),
        "vertex_count": len(components.get("vertices", [])),
        "loop_variable_count": len(components.get("loop_variables", [])),
        "scheme": components.get("scheme"),
        "regulator": components.get("regulator"),
        "evaluation_status": "symbolic_only",
    }

    return {
        "integrand_id": "s4_ctp_loop_integrand_scaffold",
        "symbolic_form": symbolic_form,
        "components": components,
        "integrand_summary": integrand_summary,
        "integration_performed": False,
        "propagators_evaluated": False,
        "amplitude_computed": False,
        "finite_part_computed": False,
        "status": "integrand_scaffold",
        "promotes_claims": False,
    }
