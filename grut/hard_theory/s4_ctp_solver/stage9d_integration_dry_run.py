"""Stage 9D loop integration dry-run plan."""

from typing import Dict

from grut.hard_theory.s4_ctp_solver.stage9c_regularized_integrand import (
    run_stage9c_regularized_integrand,
)
from grut.hard_theory.s4_ctp_solver.integration_variable_definition import (
    define_integration_variables,
)
from grut.hard_theory.s4_ctp_solver.integration_domain_specification import (
    define_integration_domain,
)
from grut.hard_theory.s4_ctp_solver.integration_ordering_plan import (
    define_integration_ordering,
)
from grut.hard_theory.s4_ctp_solver.regulator_handling_strategy import (
    define_regulator_handling,
)
from grut.hard_theory.s4_ctp_solver.integration_dry_run_audit import (
    audit_integration_dry_run,
)
from grut.hard_theory.s4_ctp_solver.stage5c_tensor_native import (
    evaluate_tensor_native_attempt,
)
from grut.hard_theory.s4_ctp_solver.tensor_placeholder_guard import (
    enforce_tensor_placeholder_guard,
)


def run_stage9d_integration_dry_run() -> Dict[str, object]:
    stage9c = run_stage9c_regularized_integrand()
    variables = define_integration_variables()
    domain = define_integration_domain()
    ordering = define_integration_ordering()
    regulator_handling = define_regulator_handling()

    plan_summary = {
        "variable_count": len(variables.get("variables", [])),
        "domain_type": domain.get("domain_type"),
        "regularization_dependent": domain.get("regularization_dependent"),
        "default_regulator": "dimensional_regularization_placeholder",
        "integration_performed": False,
        "status": "dry_run_summary",
    }

    plan = {
        "status": "integration_dry_run_plan",
        "variables": variables,
        "domain": domain,
        "ordering": ordering,
        "regulator_handling": regulator_handling,
        "plan_summary": plan_summary,
        "integration_performed": False,
        "amplitude_computed": False,
        "finite_part_computed": False,
        "extraction_performed": False,
        "r_extracted": False,
        "promotes_claims": False,
    }

    guard = enforce_tensor_placeholder_guard(evaluate_tensor_native_attempt())
    audit = audit_integration_dry_run({**plan, "guard": guard})

    return {
        "stage": "9D",
        "status": "integration_dry_run_plan",
        "integration_performed": False,
        "amplitude_computed": False,
        "can_advance_to_controlled_integration": audit.get(
            "can_advance_to_controlled_integration"
        ),
        "can_compute_finite_parts": False,
        "can_extract": False,
        "can_compute_r": False,
        "promotes_claims": False,
        "stage9c": stage9c,
        "plan": plan,
        "plan_summary": plan_summary,
        "audit": audit,
        "guard": guard,
    }
