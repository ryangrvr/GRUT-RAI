"""GRUT ToE — claim dependency graph.

Builds the directed graph of claim → dependency relations from the
registry and provides queries for fan-out, fan-in, topological order,
and high-value next-derivation candidates.

The graph is the predictive engine's reasoning layer: ask the engine
"if this open_negative were closed, how many downstream claims would
it support?" and the answer comes back as a fan-out score. This is
how GRUT-RAI tells us where to invest derivation effort next.

Edges
-----
A → B in this module's convention means "B depends on A" — i.e. the
arrow points from prerequisite to dependent. Equivalent statement:
B's `deps` field includes A.

Glossary
--------
    direct_dependents(c)        claims with c in their deps
    transitive_dependents(c)    full downstream closure (BFS from c)
    direct_dependencies(c)      contents of c.deps
    transitive_dependencies(c)  full upstream closure
    fan_out(c)                  |transitive_dependents(c)|
    roots()                     claims with no deps (entry points)
    leaves()                    claims with no dependents (terminal nodes)
    topological_order()         claims sorted so each appears after its deps
    high_value_open_negatives() open negatives ranked by downstream impact
"""

from __future__ import annotations

from collections import deque
from typing import Iterable

from grut.toe.registry import REGISTRY, Claim, by_id


# ─────────────────────────────────────────────────────────────────────
# Adjacency helpers
# ─────────────────────────────────────────────────────────────────────

def _build_dependents_index() -> dict[str, tuple[str, ...]]:
    """Inverse of the deps field: {prerequisite_id: (dependent_ids,)}."""
    index: dict[str, list[str]] = {c.id: [] for c in REGISTRY}
    for c in REGISTRY:
        for dep in c.deps:
            if dep in index:
                index[dep].append(c.id)
    return {k: tuple(v) for k, v in index.items()}


_DEPENDENTS_INDEX: dict[str, tuple[str, ...]] = _build_dependents_index()


def direct_dependents(claim_id: str) -> tuple[str, ...]:
    """Return ids of claims that directly depend on claim_id."""
    return _DEPENDENTS_INDEX.get(claim_id, ())


def direct_dependencies(claim_id: str) -> tuple[str, ...]:
    """Return ids of claims that claim_id directly depends on."""
    c = by_id(claim_id)
    return c.deps if c is not None else ()


def _bfs(start: str, neighbors_of) -> set[str]:
    """Generic BFS closure starting from start, excluding start itself."""
    seen: set[str] = set()
    queue = deque([start])
    while queue:
        current = queue.popleft()
        for n in neighbors_of(current):
            if n not in seen and n != start:
                seen.add(n)
                queue.append(n)
    return seen


def transitive_dependents(claim_id: str) -> set[str]:
    """All claims downstream of claim_id (depend on it, directly or via chain)."""
    return _bfs(claim_id, direct_dependents)


def transitive_dependencies(claim_id: str) -> set[str]:
    """All claims upstream of claim_id (it depends on them, directly or via chain)."""
    return _bfs(claim_id, direct_dependencies)


def fan_out(claim_id: str) -> int:
    """Number of transitive dependents — proxy for downstream value."""
    return len(transitive_dependents(claim_id))


def fan_in(claim_id: str) -> int:
    """Number of transitive dependencies — proxy for upstream load."""
    return len(transitive_dependencies(claim_id))


# ─────────────────────────────────────────────────────────────────────
# Graph-level queries
# ─────────────────────────────────────────────────────────────────────

def roots() -> tuple[Claim, ...]:
    """Claims with no dependencies — the framework's entry points."""
    return tuple(c for c in REGISTRY if not c.deps)


def leaves() -> tuple[Claim, ...]:
    """Claims that nothing else depends on — terminal predictions."""
    return tuple(
        c for c in REGISTRY if not direct_dependents(c.id)
    )


def topological_order() -> tuple[Claim, ...]:
    """Claims sorted so each appears after all its dependencies.

    Uses Kahn's algorithm. Raises ValueError if a cycle is present
    (which would also fail the registry's acyclicity test).
    """
    in_degree: dict[str, int] = {
        c.id: len([d for d in c.deps if by_id(d) is not None])
        for c in REGISTRY
    }
    queue: deque[str] = deque(cid for cid, d in in_degree.items() if d == 0)
    out: list[str] = []

    while queue:
        cid = queue.popleft()
        out.append(cid)
        for child in direct_dependents(cid):
            in_degree[child] -= 1
            if in_degree[child] == 0:
                queue.append(child)

    if len(out) != len(REGISTRY):
        missing = set(c.id for c in REGISTRY) - set(out)
        raise ValueError(
            f"Dependency cycle prevents topological order; "
            f"unresolved: {sorted(missing)}"
        )

    return tuple(by_id(cid) for cid in out)  # type: ignore[misc]


# ─────────────────────────────────────────────────────────────────────
# Director — what to derive next
# ─────────────────────────────────────────────────────────────────────

def fan_out_ranking(
    tier: str | None = None,
) -> tuple[tuple[Claim, int], ...]:
    """Return (claim, fan_out_score) tuples sorted descending.

    If tier is provided, only claims of that tier are ranked.
    """
    if tier is None:
        candidates: Iterable[Claim] = REGISTRY
    else:
        candidates = (c for c in REGISTRY if c.tier == tier)
    pairs = [(c, fan_out(c.id)) for c in candidates]
    pairs.sort(key=lambda x: (-x[1], x[0].id))
    return tuple(pairs)


def high_value_open_negatives() -> tuple[tuple[Claim, int], ...]:
    """Open negatives ranked by downstream fan-out.

    The first entry is the open negative whose closure would unlock
    the most downstream claims — the next derivation effort with
    maximum fan-out value.
    """
    return fan_out_ranking(tier="open_negative")


def upstream_chain(claim_id: str) -> tuple[Claim, ...]:
    """Topologically-ordered list of claim_id's upstream dependencies.

    Useful for: "what do I need to have read to understand this claim?"
    """
    upstream_ids = transitive_dependencies(claim_id)
    topo = topological_order()
    return tuple(c for c in topo if c.id in upstream_ids)


def downstream_chain(claim_id: str) -> tuple[Claim, ...]:
    """Topologically-ordered list of claim_id's downstream dependents.

    Useful for: "if this changes, what else moves?"
    """
    downstream_ids = transitive_dependents(claim_id)
    topo = topological_order()
    return tuple(c for c in topo if c.id in downstream_ids)


def graph_summary() -> dict[str, object]:
    """Summary statistics of the dependency graph."""
    n_edges = sum(
        len([d for d in c.deps if by_id(d) is not None])
        for c in REGISTRY
    )
    return {
        "n_nodes": len(REGISTRY),
        "n_edges": n_edges,
        "n_roots": len(roots()),
        "n_leaves": len(leaves()),
        "max_fan_out": max((fan_out(c.id) for c in REGISTRY), default=0),
        "max_fan_in": max((fan_in(c.id) for c in REGISTRY), default=0),
    }


if __name__ == "__main__":
    # CLI: print graph summary, top fan-out claims, high-value open negatives
    print("=" * 72)
    print("Dependency graph summary")
    print("=" * 72)
    for k, v in graph_summary().items():
        print(f"  {k:<14}  {v}")

    print()
    print("=" * 72)
    print("Top 10 claims by downstream fan-out")
    print("=" * 72)
    for c, score in fan_out_ranking()[:10]:
        print(f"  [{score:>3}]  {c.id}  ({c.tier})")

    print()
    print("=" * 72)
    print("Roots (zero dependencies — entry points to the framework)")
    print("=" * 72)
    for c in roots():
        print(f"  [{c.tier:<13}]  {c.id}")

    print()
    print("=" * 72)
    print("High-value open negatives (closing them unlocks the most)")
    print("=" * 72)
    for c, score in high_value_open_negatives():
        print(f"  [fan_out={score:>2}]  {c.id}")
        print(f"             {c.statement[:90]}...")
