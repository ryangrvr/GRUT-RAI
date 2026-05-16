"""Dependency graph for native integrand partitions."""

from typing import Dict, List, Set


def _detect_cycle(nodes: List[str], edges: List[Dict[str, str]]) -> bool:
    adjacency = {node: [] for node in nodes}
    for edge in edges:
        source = edge.get("from")
        target = edge.get("to")
        if source in adjacency:
            adjacency[source].append(target)

    visiting: Set[str] = set()
    visited: Set[str] = set()

    def visit(node: str) -> bool:
        if node in visiting:
            return True
        if node in visited:
            return False
        visiting.add(node)
        for neighbor in adjacency.get(node, []):
            if visit(neighbor):
                return True
        visiting.remove(node)
        visited.add(node)
        return False

    return any(visit(node) for node in nodes)


def build_partition_dependency_graph(partitions: List[Dict[str, object]]) -> Dict[str, object]:
    nodes = [partition.get("partition_id") for partition in partitions]
    nodes.extend(
        [
            "stage10c_consistency",
            "tensor_contraction_resolution",
            "full_pipeline_eligibility",
        ]
    )

    edges: List[Dict[str, str]] = []
    for partition in partitions:
        partition_type = partition.get("partition_type")
        partition_id = partition.get("partition_id")
        if partition_type in {"eligible_future", "tested_minimal"}:
            edges.append(
                {
                    "from": partition_id,
                    "to": "stage10c_consistency",
                    "dependency": "stage10c_consistency",
                }
            )
        if partition_type == "blocked":
            edges.append(
                {
                    "from": partition_id,
                    "to": "tensor_contraction_resolution",
                    "dependency": "tensor_contraction_resolution",
                }
            )
        if partition_type == "forbidden_full_diagram":
            edges.append(
                {
                    "from": partition_id,
                    "to": "full_pipeline_eligibility",
                    "dependency": "full_pipeline_eligibility",
                }
            )

    acyclic = not _detect_cycle(nodes, edges)

    return {
        "graph_id": "native_integrand_partition_graph",
        "nodes": nodes,
        "edges": edges,
        "acyclic": acyclic,
        "promotes_claims": False,
    }
