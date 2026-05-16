from grut.hard_theory.s4_ctp_solver.stage10d_integrand_partition_map import (
    run_stage10d_integrand_partition_map,
)
from grut.hard_theory.s4_ctp_solver.native_integrand_partition import (
    partition_native_integrand,
    TESTED_SUBINTEGRAND_IDS,
)
from grut.hard_theory.s4_ctp_solver.partition_eligibility import (
    classify_partition_eligibility,
)
from grut.hard_theory.s4_ctp_solver.partition_dependency_graph import (
    build_partition_dependency_graph,
)
from grut.hard_theory.s4_ctp_solver.stage9c_regularized_integrand import (
    run_stage9c_regularized_integrand,
)


def test_partitions_include_required_types():
    integrand = run_stage9c_regularized_integrand().get("stage9b", {}).get("integrand", {})
    partitions = partition_native_integrand(integrand)
    types = {partition["partition_type"] for partition in partitions}
    assert "tested_minimal" in types
    assert "eligible_future" in types
    assert "blocked" in types
    assert "forbidden_full_diagram" in types


def test_exactly_three_tested_partitions():
    report = run_stage10d_integrand_partition_map()
    assert report["tested_partition_count"] == 3
    tested_ids = {
        partition["partition_id"]
        for partition in report["partitions"]
        if partition["partition_type"] == "tested_minimal"
    }
    assert tested_ids == set(TESTED_SUBINTEGRAND_IDS)


def test_all_can_integrate_now_false():
    report = run_stage10d_integrand_partition_map()
    assert all(
        entry["can_integrate_now"] is False
        for entry in report["classifications"]
    )


def test_no_integration_performed():
    report = run_stage10d_integrand_partition_map()
    assert report["integrations_performed"] is False


def test_no_full_integrand_used():
    report = run_stage10d_integrand_partition_map()
    assert report["full_integrand_used"] is False


def test_dependency_graph_acyclic():
    report = run_stage10d_integrand_partition_map()
    assert report["graph"]["acyclic"] is True


def test_audit_blocks_finite_parts_and_extraction():
    report = run_stage10d_integrand_partition_map()
    assert report["audit"]["can_compute_finite_parts"] is False
    assert report["audit"]["can_extract"] is False
    assert report["audit"]["can_compute_r"] is False


def test_no_claim_promotion():
    report = run_stage10d_integrand_partition_map()
    assert report["promotes_claims"] is False


def test_recursive_guard_invoked():
    report = run_stage10d_integrand_partition_map()
    assert report["guard"]["guard"] == "tensor_placeholder_guard"


def test_package_imports_cleanly():
    import grut.hard_theory.s4_ctp_solver as pkg

    assert pkg.S4CTPPipeline is not None


def test_classification_rules_apply():
    integrand = run_stage9c_regularized_integrand().get("stage9b", {}).get("integrand", {})
    partitions = partition_native_integrand(integrand)
    classifications = [classify_partition_eligibility(partition) for partition in partitions]
    assert all(entry["can_integrate_now"] is False for entry in classifications)


def test_dependency_graph_nodes_and_edges():
    integrand = run_stage9c_regularized_integrand().get("stage9b", {}).get("integrand", {})
    partitions = partition_native_integrand(integrand)
    graph = build_partition_dependency_graph(partitions)
    assert graph["graph_id"] == "native_integrand_partition_graph"
    assert graph["nodes"]
    assert graph["edges"]
