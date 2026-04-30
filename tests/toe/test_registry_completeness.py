"""Enforcement tests for the GRUT ToE Claim Registry.

The registry at grut/toe/registry.py is the load-bearing inventory for
the GRUT ToE document. These tests ensure it stays internally
consistent: no duplicate ids, no invalid tiers, no orphan dependencies,
no unclassified claims, and full chapter coverage (1-12).

Coherence checks against V7 prose and against the broader codebase
test suite are Phase-2 components and live in their own modules
(grut/toe/coherence.py, grut/toe/dependencies.py) once those exist.
"""

import pytest

from grut.toe.registry import (
    CHAPTER_TITLES,
    REGISTRY,
    VALID_TIERS,
    Claim,
    all_claim_ids,
    by_chapter,
    by_tier,
    chapter_summary,
)


class TestRegistryStructuralIntegrity:
    """Internal consistency of the registry itself."""

    def test_registry_is_non_empty(self):
        assert len(REGISTRY) > 0

    def test_all_claim_ids_unique(self):
        ids = [c.id for c in REGISTRY]
        assert len(ids) == len(set(ids)), (
            f"Duplicate claim ids: "
            f"{[i for i in ids if ids.count(i) > 1]}"
        )

    def test_all_tiers_valid(self):
        for c in REGISTRY:
            assert c.tier in VALID_TIERS, (
                f"Claim {c.id!r} has invalid tier {c.tier!r}; "
                f"must be one of {VALID_TIERS}"
            )

    def test_all_chapters_in_range_1_to_12(self):
        for c in REGISTRY:
            assert 1 <= c.chapter <= 12, (
                f"Claim {c.id!r} chapter={c.chapter} out of range 1-12"
            )

    def test_all_statements_non_empty(self):
        for c in REGISTRY:
            assert c.statement.strip(), (
                f"Claim {c.id!r} has empty statement"
            )

    def test_all_ids_snake_case(self):
        for c in REGISTRY:
            assert c.id == c.id.lower(), (
                f"Claim id {c.id!r} must be lowercase snake_case"
            )
            assert " " not in c.id and "-" not in c.id, (
                f"Claim id {c.id!r} must not contain spaces or hyphens"
            )


class TestDependencyClosure:
    """Every dep must point to an existing claim id."""

    def test_all_deps_resolve_to_registered_claims(self):
        registered = all_claim_ids()
        for c in REGISTRY:
            for dep in c.deps:
                assert dep in registered, (
                    f"Claim {c.id!r} depends on {dep!r} which is not "
                    f"registered. Add the dependency or fix the claim."
                )

    def test_no_self_dependencies(self):
        for c in REGISTRY:
            assert c.id not in c.deps, (
                f"Claim {c.id!r} lists itself as a dependency"
            )

    def test_dependency_graph_is_acyclic(self):
        """Detects circular dependencies via DFS."""
        registered = {c.id: c for c in REGISTRY}

        WHITE, GRAY, BLACK = 0, 1, 2
        color = {cid: WHITE for cid in registered}

        def dfs(cid: str, stack: list[str]) -> None:
            color[cid] = GRAY
            for dep in registered[cid].deps:
                if dep not in registered:
                    continue
                if color[dep] == GRAY:
                    raise AssertionError(
                        f"Dependency cycle: "
                        f"{' -> '.join(stack + [cid, dep])}"
                    )
                if color[dep] == WHITE:
                    dfs(dep, stack + [cid])
            color[cid] = BLACK

        for cid in registered:
            if color[cid] == WHITE:
                dfs(cid, [])


class TestTierContracts:
    """Each tier carries obligations: computed claims need tests, etc."""

    def test_computed_claims_have_tests(self):
        violations = [
            c.id for c in by_tier("computed") if not c.tests
        ]
        assert not violations, (
            f"'computed' claims must have at least one test reference. "
            f"Missing: {violations}"
        )

    def test_computed_claims_have_refs(self):
        violations = [
            c.id for c in by_tier("computed") if not c.refs
        ]
        assert not violations, (
            f"'computed' claims must have at least one ref. "
            f"Missing: {violations}"
        )

    def test_anchored_claims_have_refs(self):
        violations = [
            c.id for c in by_tier("anchored") if not c.refs
        ]
        assert not violations, (
            f"'anchored' claims must have refs (V7 section, paper, code). "
            f"Missing: {violations}"
        )

    def test_open_negative_claims_have_refs_or_notes(self):
        for c in by_tier("open_negative"):
            assert c.refs or c.notes, (
                f"Open-negative claim {c.id!r} must reference the "
                f"correction log / honest-negative document, OR carry "
                f"notes characterizing the failure mode."
            )

    def test_conjectural_claims_have_notes(self):
        violations = [
            c.id for c in by_tier("conjectural") if not c.notes
        ]
        assert not violations, (
            f"Conjectural claims must carry interpretive notes. "
            f"Missing: {violations}"
        )

    def test_foundational_claims_have_falsifier_or_notes(self):
        for c in by_tier("foundational"):
            assert c.falsifier or c.notes, (
                f"Foundational claim {c.id!r} must articulate either a "
                f"falsifier or notes explaining the framing role."
            )


class TestChapterCoverage:
    """Every chapter must hold at least one claim — no empty chapters."""

    def test_every_chapter_has_at_least_one_claim(self):
        empty = [
            n for n in CHAPTER_TITLES if not by_chapter(n)
        ]
        assert not empty, (
            f"Chapters with zero registered claims: "
            f"{[(n, CHAPTER_TITLES[n]) for n in empty]}"
        )

    def test_chapter_summary_well_formed(self):
        s = chapter_summary()
        assert set(s.keys()) == set(CHAPTER_TITLES.keys())
        for chapter, tiers in s.items():
            for tier, count in tiers.items():
                assert tier in VALID_TIERS
                assert count > 0


class TestFalsifierDiscipline:
    """At least some claims should articulate falsifiers — a TOE that
    can't be falsified isn't a TOE. Threshold is loose by design;
    tighten as the registry matures.
    """

    def test_at_least_five_falsifiers_present(self):
        n_falsifiers = sum(
            1 for c in REGISTRY if c.falsifier and c.falsifier.strip()
        )
        assert n_falsifiers >= 5, (
            f"Only {n_falsifiers} claims articulate falsifiers; "
            f"a Theory of Everything should expose more falsification "
            f"surface than that."
        )

    def test_falsification_chapter_has_open_negatives(self):
        """Chapter 12 must include the documented honest negatives."""
        ch12 = by_chapter(12)
        open_negs = [c for c in ch12 if c.tier == "open_negative"]
        assert len(open_negs) >= 3, (
            f"Chapter 12 (Falsification) must include at least 3 "
            f"open_negative claims; found {len(open_negs)}."
        )


class TestCanonicalAnchorClaims:
    """Spot-check that the load-bearing claims are present and well-formed.

    These are the spine of the ToE: if any of these go missing, the
    document loses structural integrity.
    """

    SPINE_CLAIMS = (
        "closed_universe",
        "fixed_point_principle",
        "tau_0_derivation",
        "alpha_vac_derivation",
        "constitutive_equation",
        "memory_kernel_form",
        "threshold_bridge",
        "r_canonical_path_g",
        "r_max_ricci_saturation",
        "rho_max_universal",
        "h_inf_decomposition",
        "h_0_prediction",
        "bullet_cluster_offset",
        "mond_a_0_emergence",
        "correction_ledger",
    )

    @pytest.mark.parametrize("claim_id", SPINE_CLAIMS)
    def test_spine_claim_exists(self, claim_id):
        from grut.toe.registry import by_id
        c = by_id(claim_id)
        assert c is not None, (
            f"Spine claim {claim_id!r} missing from registry"
        )
        assert c.statement.strip()
        assert c.refs, f"Spine claim {claim_id!r} has no refs"
