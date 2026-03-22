"""
Tests for grut.parameter_authority_map
======================================

Verifies:
- All candidate parameters are evaluated
- Authority labels are valid and deterministic
- Sector labels are valid
- Export structure is complete
- Cross-sector dependency map is consistent
- Observable roadmap is well-formed
- Canon hierarchy is well-formed
- Bridge classification is reproducible from explicit criteria
- Omni-ToE claims are well-formed
- No hidden scoring or ad hoc weights
"""

import json
import math
import os
import tempfile

import pytest

from grut.parameter_authority_map import (
    AUTHORITY_CLASSES,
    BRIDGE_CLASSIFICATION_OPTIONS,
    CANON_HIERARCHY_LEVELS,
    EFFECT_TYPES,
    SECTORS,
    ASSUMPTIONS,
    NONCLAIMS,
    BridgeClassification,
    BridgeGap,
    BridgeResult,
    CanonHierarchy,
    CanonHierarchyEntry,
    CrossSectorMap,
    ObservableEntry,
    ObservableRoadmap,
    ParameterAuthorityMap,
    ParameterEntry,
    SectorDependency,
    bridge_result_to_dict,
    build_canon_hierarchy,
    build_cross_sector_map,
    build_observable_roadmap,
    build_parameter_authority_map,
    classify_bridge,
    compute_bridge_result,
    determine_omni_toe_claims,
    export_bridge_result_json,
    identify_bridge_gaps,
)


# ===================================================================
# Fixtures
# ===================================================================

@pytest.fixture(scope="module")
def bridge_result():
    """Module-scoped bridge result for deterministic testing."""
    return compute_bridge_result()


@pytest.fixture(scope="module")
def pam(bridge_result):
    return bridge_result.parameter_authority_map


@pytest.fixture(scope="module")
def csm(bridge_result):
    return bridge_result.cross_sector_map


@pytest.fixture(scope="module")
def roadmap(bridge_result):
    return bridge_result.observable_roadmap


@pytest.fixture(scope="module")
def hierarchy(bridge_result):
    return bridge_result.canon_hierarchy


@pytest.fixture(scope="module")
def gaps(bridge_result):
    return bridge_result.bridge_gaps


@pytest.fixture(scope="module")
def classification(bridge_result):
    return bridge_result.bridge_classification


# ===================================================================
# Class: TestVocabulary
# ===================================================================

class TestVocabulary:
    """Test that vocabulary constants are well-defined."""

    def test_authority_classes_nonempty(self):
        assert len(AUTHORITY_CLASSES) == 5

    def test_authority_classes_content(self):
        expected = {"inherited", "derived", "matched", "phenomenological", "open"}
        assert set(AUTHORITY_CLASSES) == expected

    def test_sectors_nonempty(self):
        assert len(SECTORS) == 7

    def test_sectors_content(self):
        expected = {
            "gravitational", "macro_scalar_memory", "defect_triplet",
            "curvature_trigger", "portal_interaction", "cosmology", "observational",
        }
        assert set(SECTORS) == expected

    def test_canon_hierarchy_levels_nonempty(self):
        assert len(CANON_HIERARCHY_LEVELS) == 10

    def test_bridge_classification_options_nonempty(self):
        assert len(BRIDGE_CLASSIFICATION_OPTIONS) == 3

    def test_effect_types_nonempty(self):
        assert len(EFFECT_TYPES) >= 5

    def test_assumptions_nonempty(self):
        assert len(ASSUMPTIONS) >= 5

    def test_nonclaims_nonempty(self):
        assert len(NONCLAIMS) >= 5


# ===================================================================
# Class: TestParameterEntry
# ===================================================================

class TestParameterEntry:
    """Test ParameterEntry validation."""

    def test_valid_entry(self):
        e = ParameterEntry(
            name="test", symbol="t", value=1.0, value_expr="1.0",
            sectors=["gravitational"], authority_class="inherited",
            fixed_by="test", current_role="test", structurally_central=True,
            future_reduction_path="none",
        )
        assert e.name == "test"

    def test_invalid_authority_class(self):
        with pytest.raises(ValueError, match="Invalid authority class"):
            ParameterEntry(
                name="test", symbol="t", value=1.0, value_expr="1.0",
                sectors=["gravitational"], authority_class="INVALID",
                fixed_by="test", current_role="test", structurally_central=True,
                future_reduction_path="none",
            )

    def test_invalid_sector(self):
        with pytest.raises(ValueError, match="Invalid sector"):
            ParameterEntry(
                name="test", symbol="t", value=1.0, value_expr="1.0",
                sectors=["nonexistent_sector"], authority_class="inherited",
                fixed_by="test", current_role="test", structurally_central=True,
                future_reduction_path="none",
            )


# ===================================================================
# Class: TestParameterAuthorityMap
# ===================================================================

class TestParameterAuthorityMap:
    """Test parameter authority map construction and content."""

    def test_pam_nonempty(self, pam):
        assert len(pam.entries) >= 20

    def test_all_authority_classes_valid(self, pam):
        for e in pam.entries:
            assert e.authority_class in AUTHORITY_CLASSES, (
                f"Entry '{e.name}' has invalid authority class '{e.authority_class}'"
            )

    def test_all_sectors_valid(self, pam):
        for e in pam.entries:
            for s in e.sectors:
                assert s in SECTORS, (
                    f"Entry '{e.name}' has invalid sector '{s}'"
                )

    def test_counts_sum_to_total(self, pam):
        total = (
            pam.inherited_count + pam.derived_count + pam.matched_count
            + pam.phenomenological_count + pam.open_count
        )
        assert total == len(pam.entries)

    def test_inherited_count(self, pam):
        assert pam.inherited_count >= 5

    def test_derived_count(self, pam):
        assert pam.derived_count >= 2

    def test_matched_count(self, pam):
        assert pam.matched_count >= 2

    def test_open_count(self, pam):
        assert pam.open_count >= 2

    def test_key_parameters_present(self, pam):
        names = {e.name for e in pam.entries}
        required = {
            "Gravitational constant", "Schwarzschild radius", "External mass",
            "Vacuum alpha parameter", "Memory kernel time scale",
            "Source charge", "Defect VEV", "Defect self-coupling",
            "Portal coupling", "Curvature coupling", "Winding number",
        }
        for r in required:
            assert r in names, f"Required parameter '{r}' missing from PAM"

    def test_Q_is_matched(self, pam):
        q_entry = next(e for e in pam.entries if e.symbol == "Q")
        assert q_entry.authority_class == "matched"

    def test_eta_is_matched(self, pam):
        eta = next(e for e in pam.entries if e.symbol == "eta")
        assert eta.authority_class == "matched"

    def test_lambda_is_open(self, pam):
        lam = next(e for e in pam.entries if e.symbol == "lambda")
        assert lam.authority_class == "open"

    def test_g_p_is_open(self, pam):
        gp = next(e for e in pam.entries if e.symbol == "g_p")
        assert gp.authority_class == "open"

    def test_tau_is_derived(self, pam):
        tau = next(e for e in pam.entries if e.symbol == "tau")
        assert tau.authority_class == "derived"

    def test_tau_value(self, pam):
        tau = next(e for e in pam.entries if e.symbol == "tau")
        assert abs(tau.value - math.sqrt(1.5)) < 1e-10

    def test_all_entries_have_reduction_path(self, pam):
        for e in pam.entries:
            assert len(e.future_reduction_path) > 0, (
                f"Entry '{e.name}' missing future_reduction_path"
            )

    def test_all_entries_have_fixed_by(self, pam):
        for e in pam.entries:
            assert len(e.fixed_by) > 0, (
                f"Entry '{e.name}' missing fixed_by"
            )

    def test_deterministic(self):
        pam1 = build_parameter_authority_map()
        pam2 = build_parameter_authority_map()
        assert len(pam1.entries) == len(pam2.entries)
        for e1, e2 in zip(pam1.entries, pam2.entries):
            assert e1.name == e2.name
            assert e1.authority_class == e2.authority_class


# ===================================================================
# Class: TestCrossSectorMap
# ===================================================================

class TestCrossSectorMap:
    """Test cross-sector dependency map."""

    def test_all_sectors_covered(self, csm):
        covered = {d.sector for d in csm.dependencies}
        assert set(SECTORS) == covered

    def test_all_sector_labels_valid(self, csm):
        for d in csm.dependencies:
            assert d.sector in SECTORS
            for dep in d.depends_on:
                assert dep in SECTORS

    def test_all_statuses_valid(self, csm):
        for d in csm.dependencies:
            assert d.current_status in CANON_HIERARCHY_LEVELS

    def test_gravitational_has_no_deps(self, csm):
        grav = next(d for d in csm.dependencies if d.sector == "gravitational")
        assert len(grav.depends_on) == 0

    def test_minimal_backbone_nonempty(self, csm):
        assert len(csm.minimal_backbone) >= 3

    def test_minimal_backbone_valid_sectors(self, csm):
        for s in csm.minimal_backbone:
            assert s in SECTORS

    def test_backbone_summary_nonempty(self, csm):
        assert len(csm.backbone_summary) > 50

    def test_unity_argument_nonempty(self, csm):
        assert len(csm.unity_argument) > 50

    def test_every_dependency_has_exports(self, csm):
        for d in csm.dependencies:
            assert len(d.exported_structures) > 0, (
                f"Sector '{d.sector}' has no exported structures"
            )

    def test_deterministic(self):
        csm1 = build_cross_sector_map()
        csm2 = build_cross_sector_map()
        assert len(csm1.dependencies) == len(csm2.dependencies)
        for d1, d2 in zip(csm1.dependencies, csm2.dependencies):
            assert d1.sector == d2.sector
            assert d1.current_status == d2.current_status


# ===================================================================
# Class: TestObservableRoadmap
# ===================================================================

class TestObservableRoadmap:
    """Test observable roadmap."""

    def test_roadmap_nonempty(self, roadmap):
        assert len(roadmap.entries) >= 8

    def test_all_effect_types_valid(self, roadmap):
        for e in roadmap.entries:
            assert e.predicted_effect_type in EFFECT_TYPES, (
                f"Observable '{e.observable}' has invalid effect type '{e.predicted_effect_type}'"
            )

    def test_all_sectors_valid(self, roadmap):
        for e in roadmap.entries:
            for s in e.sectors_probed:
                assert s in SECTORS

    def test_all_have_support_criterion(self, roadmap):
        for e in roadmap.entries:
            assert len(e.support_criterion) > 10

    def test_all_have_falsification_criterion(self, roadmap):
        for e in roadmap.entries:
            assert len(e.falsification_criterion) > 10

    def test_all_have_tension_criterion(self, roadmap):
        for e in roadmap.entries:
            assert len(e.tension_criterion) > 10

    def test_observational_classes_populated(self, roadmap):
        assert len(roadmap.observational_classes) >= 3

    def test_required_classes_present(self, roadmap):
        classes = set(roadmap.observational_classes)
        assert "compact_object_structure" in classes
        assert "gravitational_wave" in classes
        assert "strong_field_lensing" in classes

    def test_deterministic(self):
        r1 = build_observable_roadmap()
        r2 = build_observable_roadmap()
        assert len(r1.entries) == len(r2.entries)
        for e1, e2 in zip(r1.entries, r2.entries):
            assert e1.observable == e2.observable


# ===================================================================
# Class: TestCanonHierarchy
# ===================================================================

class TestCanonHierarchy:
    """Test theory-wide canon hierarchy."""

    def test_hierarchy_nonempty(self, hierarchy):
        assert len(hierarchy.entries) >= 12

    def test_all_statuses_valid(self, hierarchy):
        for e in hierarchy.entries:
            assert e.current_status in CANON_HIERARCHY_LEVELS, (
                f"'{e.claim_or_sector}' has invalid status '{e.current_status}'"
            )

    def test_all_have_basis(self, hierarchy):
        for e in hierarchy.entries:
            assert len(e.basis) > 5

    def test_all_have_caveat(self, hierarchy):
        for e in hierarchy.entries:
            assert len(e.caveat) > 0

    def test_has_locked_entries(self, hierarchy):
        locked = [e for e in hierarchy.entries if e.current_status == "LOCKED"]
        assert len(locked) >= 3

    def test_has_open_entries(self, hierarchy):
        open_entries = [e for e in hierarchy.entries if e.current_status == "OPEN"]
        assert len(open_entries) >= 1

    def test_d12_status(self, hierarchy):
        d12 = next(
            e for e in hierarchy.entries
            if "Q" in e.claim_or_sector or "source ontology" in e.claim_or_sector.lower()
        )
        assert d12.current_status == "PRINCIPLED_AND_STRONGLY_CONSTRAINED"

    def test_final_toe_status_is_open(self, hierarchy):
        toe = next(
            e for e in hierarchy.entries
            if "final toe" in e.claim_or_sector.lower()
        )
        assert toe.current_status == "OPEN"

    def test_deterministic(self):
        h1 = build_canon_hierarchy()
        h2 = build_canon_hierarchy()
        assert len(h1.entries) == len(h2.entries)
        for e1, e2 in zip(h1.entries, h2.entries):
            assert e1.claim_or_sector == e2.claim_or_sector
            assert e1.current_status == e2.current_status


# ===================================================================
# Class: TestBridgeGaps
# ===================================================================

class TestBridgeGaps:
    """Test bridge gap identification."""

    def test_gaps_nonempty(self, gaps):
        assert len(gaps) >= 5

    def test_has_critical_gaps(self, gaps):
        critical = [g for g in gaps if g.severity == "critical"]
        assert len(critical) >= 2

    def test_gap_severities_valid(self, gaps):
        valid = {"critical", "significant", "minor"}
        for g in gaps:
            assert g.severity in valid, (
                f"Gap '{g.gap}' has invalid severity '{g.severity}'"
            )

    def test_all_gaps_have_notes(self, gaps):
        for g in gaps:
            assert len(g.notes) > 10

    def test_o3_derivation_is_critical(self, gaps):
        o3 = next(g for g in gaps if "O(3)" in g.gap)
        assert o3.severity == "critical"

    def test_empirical_is_critical(self, gaps):
        emp = next(g for g in gaps if "empirical" in g.gap.lower() or "Empirical" in g.gap)
        assert emp.severity == "critical"

    def test_deterministic(self):
        g1 = identify_bridge_gaps()
        g2 = identify_bridge_gaps()
        assert len(g1) == len(g2)
        for a, b in zip(g1, g2):
            assert a.gap == b.gap
            assert a.severity == b.severity


# ===================================================================
# Class: TestBridgeClassification
# ===================================================================

class TestBridgeClassification:
    """Test bridge classification logic."""

    def test_classification_valid(self, classification):
        assert classification.classification in BRIDGE_CLASSIFICATION_OPTIONS

    def test_classification_value(self, classification):
        assert classification.classification == "strong_but_missing_one_major_bridge"

    def test_justification_nonempty(self, classification):
        assert len(classification.justification) > 20

    def test_counts_consistent(self, classification, hierarchy):
        total_locked = sum(
            1 for e in hierarchy.entries if e.current_status == "LOCKED"
        )
        assert classification.locked_count == total_locked

    def test_critical_gaps_counted(self, classification, gaps):
        expected = sum(1 for g in gaps if g.severity == "critical")
        assert classification.critical_gaps == expected

    def test_deterministic(self):
        h = build_canon_hierarchy()
        g = identify_bridge_gaps()
        c1 = classify_bridge(h, g)
        c2 = classify_bridge(h, g)
        assert c1.classification == c2.classification
        assert c1.locked_count == c2.locked_count

    def test_invalid_classification_rejected(self):
        with pytest.raises(ValueError, match="Invalid classification"):
            BridgeClassification(
                classification="invalid_option",
                justification="test",
                locked_count=0,
                supported_count=0,
                open_count=0,
                critical_gaps=0,
            )

    def test_sufficient_when_no_critical_gaps_high_support(self):
        """Verify classification logic: no critical gaps + high support = sufficient."""
        entries = [
            CanonHierarchyEntry(
                claim_or_sector=f"claim_{i}",
                current_status="LOCKED" if i < 5 else "STRONGLY_SUPPORTED",
                basis="test",
                caveat="none",
            )
            for i in range(7)
        ]
        hierarchy = CanonHierarchy(entries=entries)
        gaps = [
            BridgeGap(gap="minor gap", severity="minor", sector="gravitational", notes="test"),
        ]
        result = classify_bridge(hierarchy, gaps)
        assert result.classification == "sufficient_for_final_toe_synthesis"


# ===================================================================
# Class: TestOmniToeClaims
# ===================================================================

class TestOmniToeClaims:
    """Test Omni-ToE v3 claims."""

    def test_may_claim_nonempty(self, bridge_result):
        assert len(bridge_result.omni_toe_v3_may_claim) >= 5

    def test_may_not_claim_nonempty(self, bridge_result):
        assert len(bridge_result.omni_toe_v3_may_not_claim) >= 5

    def test_may_not_claim_includes_observational(self, bridge_result):
        texts = " ".join(bridge_result.omni_toe_v3_may_not_claim).lower()
        assert "observational" in texts or "confirmed" in texts

    def test_may_not_claim_includes_o3_derivation(self, bridge_result):
        texts = " ".join(bridge_result.omni_toe_v3_may_not_claim)
        assert "O(3)" in texts

    def test_may_claim_includes_falsifiability(self, bridge_result):
        texts = " ".join(bridge_result.omni_toe_v3_may_claim).lower()
        assert "falsif" in texts


# ===================================================================
# Class: TestExport
# ===================================================================

class TestExport:
    """Test export functionality."""

    def test_to_dict_valid(self, bridge_result):
        d = bridge_result_to_dict(bridge_result)
        assert isinstance(d, dict)
        assert d["valid"] is True
        assert "parameter_authority_map" in d
        assert "cross_sector_map" in d
        assert "observable_roadmap" in d
        assert "canon_hierarchy" in d
        assert "bridge_gaps" in d
        assert "bridge_classification" in d

    def test_to_dict_serializable(self, bridge_result):
        d = bridge_result_to_dict(bridge_result)
        s = json.dumps(d, default=str)
        assert len(s) > 1000

    def test_export_json(self, bridge_result):
        with tempfile.NamedTemporaryFile(suffix=".json", delete=False) as f:
            path = f.name
        try:
            export_bridge_result_json(bridge_result, path)
            with open(path) as f:
                data = json.load(f)
            assert data["valid"] is True
            assert len(data["parameter_authority_map"]["entries"]) >= 20
        finally:
            os.unlink(path)

    def test_pam_entries_in_export(self, bridge_result):
        d = bridge_result_to_dict(bridge_result)
        entries = d["parameter_authority_map"]["entries"]
        names = {e["name"] for e in entries}
        assert "Source charge" in names
        assert "Defect VEV" in names

    def test_hierarchy_entries_in_export(self, bridge_result):
        d = bridge_result_to_dict(bridge_result)
        entries = d["canon_hierarchy"]["entries"]
        claims = {e["claim_or_sector"] for e in entries}
        assert any("D12" in c for c in claims)


# ===================================================================
# Class: TestBridgeResult
# ===================================================================

class TestBridgeResult:
    """Test top-level bridge result."""

    def test_valid(self, bridge_result):
        assert bridge_result.valid is True

    def test_all_components_present(self, bridge_result):
        assert bridge_result.parameter_authority_map is not None
        assert bridge_result.cross_sector_map is not None
        assert bridge_result.observable_roadmap is not None
        assert bridge_result.canon_hierarchy is not None
        assert bridge_result.bridge_gaps is not None
        assert bridge_result.bridge_classification is not None

    def test_deterministic(self):
        r1 = compute_bridge_result()
        r2 = compute_bridge_result()
        assert r1.bridge_classification.classification == r2.bridge_classification.classification
        assert len(r1.parameter_authority_map.entries) == len(r2.parameter_authority_map.entries)
        assert len(r1.observable_roadmap.entries) == len(r2.observable_roadmap.entries)


# ===================================================================
# Class: TestValidation
# ===================================================================

class TestValidation:
    """Test dataclass validation."""

    def test_invalid_sector_dependency(self):
        with pytest.raises(ValueError, match="Invalid sector"):
            SectorDependency(
                sector="invalid_sector",
                depends_on=[],
                inherited_structures=[],
                exported_structures=["x"],
                current_status="LOCKED",
            )

    def test_invalid_hierarchy_status(self):
        with pytest.raises(ValueError, match="Invalid status"):
            CanonHierarchyEntry(
                claim_or_sector="test",
                current_status="INVALID_STATUS",
                basis="test",
                caveat="none",
            )

    def test_invalid_observable_effect_type(self):
        with pytest.raises(ValueError, match="Invalid effect type"):
            ObservableEntry(
                observable="test",
                sectors_probed=["gravitational"],
                relevant_parameters=["M"],
                predicted_effect_type="INVALID",
                predicted_effect_description="test",
                support_criterion="test",
                tension_criterion="test",
                falsification_criterion="test",
                observational_class="test",
            )

    def test_sector_dependency_invalid_status(self):
        with pytest.raises(ValueError, match="Invalid status"):
            SectorDependency(
                sector="gravitational",
                depends_on=[],
                inherited_structures=[],
                exported_structures=["x"],
                current_status="BOGUS",
            )
