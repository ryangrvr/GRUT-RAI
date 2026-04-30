"""Tests for grut.toe.dependencies — the dependency graph layer.

Verifies:
  - Adjacency consistency (deps ↔ dependents are inverses)
  - BFS closures terminate and are correct
  - Topological order respects all edges
  - Fan-out / fan-in monotonic w.r.t. graph structure
  - High-value-open-negative ranking returns sane results
  - Graph is acyclic (already enforced at registry level — re-checked here)
"""

import pytest

from grut.toe.registry import REGISTRY, by_id, by_tier
from grut.toe.dependencies import (
    direct_dependencies,
    direct_dependents,
    downstream_chain,
    fan_in,
    fan_out,
    fan_out_ranking,
    graph_summary,
    high_value_open_negatives,
    leaves,
    roots,
    topological_order,
    transitive_dependencies,
    transitive_dependents,
    upstream_chain,
)


class TestAdjacencyConsistency:
    """deps and dependents are inverses of each other."""

    def test_each_dep_appears_in_dependents(self):
        for c in REGISTRY:
            for dep in c.deps:
                if by_id(dep) is None:
                    continue
                assert c.id in direct_dependents(dep), (
                    f"{c.id!r} declares dep on {dep!r} but {dep!r}'s "
                    f"dependents list does not contain {c.id!r}"
                )

    def test_each_dependent_lists_us_as_dep(self):
        for c in REGISTRY:
            for child_id in direct_dependents(c.id):
                child = by_id(child_id)
                assert child is not None
                assert c.id in child.deps, (
                    f"{child_id!r} appears as dependent of {c.id!r} "
                    f"but does not list {c.id!r} in its deps"
                )

    def test_self_excluded_from_own_dependents(self):
        for c in REGISTRY:
            assert c.id not in direct_dependents(c.id)


class TestBFSClosures:
    """Transitive closures terminate and exclude the start node."""

    def test_transitive_dependents_excludes_start(self):
        for c in REGISTRY:
            assert c.id not in transitive_dependents(c.id)

    def test_transitive_dependencies_excludes_start(self):
        for c in REGISTRY:
            assert c.id not in transitive_dependencies(c.id)

    def test_direct_subset_of_transitive_dependents(self):
        for c in REGISTRY:
            direct = set(direct_dependents(c.id))
            trans = transitive_dependents(c.id)
            assert direct.issubset(trans), c.id

    def test_direct_subset_of_transitive_dependencies(self):
        for c in REGISTRY:
            direct = set(d for d in direct_dependencies(c.id) if by_id(d))
            trans = transitive_dependencies(c.id)
            assert direct.issubset(trans), c.id


class TestTopologicalOrder:
    """Every claim appears after all of its dependencies."""

    def test_topo_includes_all_claims_exactly_once(self):
        topo = topological_order()
        assert len(topo) == len(REGISTRY)
        assert {c.id for c in topo} == {c.id for c in REGISTRY}

    def test_topo_respects_edges(self):
        topo = topological_order()
        position = {c.id: i for i, c in enumerate(topo)}
        for c in REGISTRY:
            for dep in c.deps:
                if by_id(dep) is None:
                    continue
                assert position[dep] < position[c.id], (
                    f"{c.id!r} appears before its dependency {dep!r} "
                    f"in topological order"
                )


class TestFanOutAndFanIn:
    """Numerical sanity for fan-out / fan-in scores."""

    def test_fan_out_non_negative(self):
        for c in REGISTRY:
            assert fan_out(c.id) >= 0

    def test_fan_in_non_negative(self):
        for c in REGISTRY:
            assert fan_in(c.id) >= 0

    def test_fan_out_at_least_direct_dependents(self):
        for c in REGISTRY:
            assert fan_out(c.id) >= len(direct_dependents(c.id))

    def test_fan_in_at_least_direct_dependencies(self):
        for c in REGISTRY:
            valid_deps = [d for d in c.deps if by_id(d) is not None]
            assert fan_in(c.id) >= len(valid_deps)

    def test_root_has_zero_fan_in(self):
        for c in roots():
            assert fan_in(c.id) == 0, (
                f"{c.id!r} has no deps but fan_in = {fan_in(c.id)}"
            )


class TestRootsAndLeaves:
    def test_roots_have_no_dependencies(self):
        for c in roots():
            assert not c.deps

    def test_leaves_have_no_dependents(self):
        for c in leaves():
            assert direct_dependents(c.id) == ()

    def test_all_claims_reachable_from_roots(self):
        """BFS from all roots must cover the whole graph."""
        reached: set[str] = {c.id for c in roots()}
        frontier = list(reached)
        while frontier:
            cid = frontier.pop()
            for child in direct_dependents(cid):
                if child not in reached:
                    reached.add(child)
                    frontier.append(child)
        assert reached == {c.id for c in REGISTRY}, (
            f"Unreachable from roots: "
            f"{ {c.id for c in REGISTRY} - reached }"
        )


class TestRanking:
    """fan_out_ranking and high_value_open_negatives behave correctly."""

    def test_fan_out_ranking_descending(self):
        ranks = fan_out_ranking()
        scores = [s for _, s in ranks]
        assert scores == sorted(scores, reverse=True)

    def test_fan_out_ranking_full_coverage(self):
        ranks = fan_out_ranking()
        assert len(ranks) == len(REGISTRY)
        assert {c.id for c, _ in ranks} == {c.id for c in REGISTRY}

    def test_open_negative_filter(self):
        ranks = high_value_open_negatives()
        assert len(ranks) == len(by_tier("open_negative"))
        for c, _ in ranks:
            assert c.tier == "open_negative"


class TestUpstreamDownstreamChains:
    def test_upstream_chain_in_topo_order(self):
        topo_pos = {c.id: i for i, c in enumerate(topological_order())}
        for c in REGISTRY:
            chain = upstream_chain(c.id)
            positions = [topo_pos[x.id] for x in chain]
            assert positions == sorted(positions), (
                f"upstream_chain({c.id!r}) not in topological order"
            )

    def test_downstream_chain_in_topo_order(self):
        topo_pos = {c.id: i for i, c in enumerate(topological_order())}
        for c in REGISTRY:
            chain = downstream_chain(c.id)
            positions = [topo_pos[x.id] for x in chain]
            assert positions == sorted(positions), (
                f"downstream_chain({c.id!r}) not in topological order"
            )


class TestGraphSummary:
    def test_summary_keys_present(self):
        s = graph_summary()
        for key in ("n_nodes", "n_edges", "n_roots", "n_leaves",
                    "max_fan_out", "max_fan_in"):
            assert key in s

    def test_n_nodes_matches_registry(self):
        assert graph_summary()["n_nodes"] == len(REGISTRY)

    def test_n_edges_non_negative(self):
        assert graph_summary()["n_edges"] >= 0
