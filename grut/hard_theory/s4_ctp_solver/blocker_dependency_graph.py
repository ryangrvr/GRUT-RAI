"""Dependency graph for blocker closure sequencing."""

from typing import Dict, List, Tuple


def build_blocker_dependency_graph() -> Dict[str, List[str]]:
    return {
        "full_S4_propagator_missing": ["tensor_contractions_not_resolved"],
        "tensor_contractions_not_resolved": ["finite_part_not_computed", "r_computation_blocked"],
        "convergence_not_established": [
            "finite_part_not_computed",
            "r_computation_blocked",
        ],
        "ward_identity_not_fully_verified": ["extraction_blocked"],
        "independent_replication_missing": ["r_route_promotion_blocked"],
        "scheme_alignment_missing": [
            "extraction_blocked",
            "r_computation_blocked",
        ],
        "finite_part_not_computed": ["r_computation_blocked", "extraction_blocked"],
        "extraction_blocked": ["r_route_promotion_blocked"],
        "r_computation_blocked": ["r_route_promotion_blocked"],
    }


def _walk(node: str, graph: Dict[str, List[str]], visiting: set, visited: set) -> bool:
    if node in visiting:
        return False
    if node in visited:
        return True
    visiting.add(node)
    for neighbor in graph.get(node, []):
        if neighbor in graph and not _walk(neighbor, graph, visiting, visited):
            return False
    visiting.remove(node)
    visited.add(node)
    return True


def graph_is_acyclic(graph: Dict[str, List[str]]) -> bool:
    visiting = set()
    visited = set()
    for node in graph:
        if node not in visited:
            if not _walk(node, graph, visiting, visited):
                return False
    return True


def graph_edges(graph: Dict[str, List[str]]) -> List[Tuple[str, str]]:
    edges: List[Tuple[str, str]] = []
    for parent, children in graph.items():
        for child in children:
            edges.append((parent, child))
    return edges
