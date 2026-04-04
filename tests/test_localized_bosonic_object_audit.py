"""Tests for grut/localized_bosonic_object_audit.py.

Deterministic test suite pinning:
  1. Allowed verdict label set (closed)
  2. Nonclaim enforcement
  3. Shell vs profile vs object distinctions
  4. Topological charge vs particle-status distinction
  5. Finite-energy gating
  6. Stabilization mechanism classification
  7. Domain limitation enforcement
  8. Derrick's theorem analysis
  9. Field content inventory categories
 10. End-to-end master audit output
"""

import math
import pytest

from grut.localized_bosonic_object_audit import (
    # Constants
    M_EXT,
    R_EQ,
    TAU_SQ,
    ALPHA_VAC,
    BETA_Q_CANON,
    OMEGA_0_SQ,
    OMEGA_0,
    X_EQ,
    RHO_EQ_AT_R_EQ,
    SPATIAL_DIMENSION,
    DERRICK_KINETIC_EXPONENT,
    DERRICK_SKYRME_EXPONENT,
    ALLOWED_VERDICT_LABELS,
    FORBIDDEN_CLAIM_LABELS,
    # Dataclasses
    FieldContentItem,
    TrackA_FieldInventory,
    TrackB_DomainValidity,
    TrackC_StaticLocalization,
    TrackD_Stability,
    TrackE_FiniteEnergy,
    TrackF_TopologicalBosonic,
    TrackG_NoclaimFirewall,
    LocalizedBosonicObjectResult,
    DerrickAnalysis,
    # Functions
    build_field_inventory,
    build_domain_validity,
    build_static_localization,
    build_stability,
    build_derrick_analysis,
    build_finite_energy,
    build_topological_track,
    build_nonclaim_firewall,
    assign_primary_verdict,
    assign_secondary_verdicts,
    run_localized_bosonic_object_audit,
)


# ---------------------------------------------------------------------------
# Fixtures
# ---------------------------------------------------------------------------

@pytest.fixture(scope="module")
def audit() -> LocalizedBosonicObjectResult:
    return run_localized_bosonic_object_audit()


@pytest.fixture(scope="module")
def track_a() -> TrackA_FieldInventory:
    return build_field_inventory()


@pytest.fixture(scope="module")
def track_b() -> TrackB_DomainValidity:
    return build_domain_validity()


@pytest.fixture(scope="module")
def track_c() -> TrackC_StaticLocalization:
    return build_static_localization()


@pytest.fixture(scope="module")
def track_d() -> TrackD_Stability:
    return build_stability()


@pytest.fixture(scope="module")
def track_e() -> TrackE_FiniteEnergy:
    return build_finite_energy()


@pytest.fixture(scope="module")
def track_f() -> TrackF_TopologicalBosonic:
    return build_topological_track()


@pytest.fixture(scope="module")
def track_g() -> TrackG_NoclaimFirewall:
    return build_nonclaim_firewall()


@pytest.fixture(scope="module")
def derrick() -> DerrickAnalysis:
    return build_derrick_analysis()


# ===========================================================================
# Class 1: Constants and numerical anchors
# ===========================================================================

class TestConstants:
    """Pin all fundamental constants used in the audit."""

    def test_m_ext(self):
        assert M_EXT == pytest.approx(0.5)

    def test_r_eq(self):
        assert R_EQ == pytest.approx(1.0 / 3.0)

    def test_tau_sq(self):
        assert TAU_SQ == pytest.approx(1.5)

    def test_alpha_vac(self):
        assert ALPHA_VAC == pytest.approx(1.0 / 3.0)

    def test_beta_q_canon(self):
        assert BETA_Q_CANON == pytest.approx(2.0)

    def test_omega_0_sq_formula(self):
        """omega_0^2 = beta_Q * M_ext / R_eq^3 = 2 * 0.5 / (1/27) = 27."""
        expected = BETA_Q_CANON * M_EXT / (R_EQ ** 3)
        assert OMEGA_0_SQ == pytest.approx(expected)

    def test_omega_0_sq_value(self):
        assert OMEGA_0_SQ == pytest.approx(27.0)

    def test_omega_0_value(self):
        assert OMEGA_0 == pytest.approx(math.sqrt(27.0))

    def test_x_eq_value(self):
        assert X_EQ == pytest.approx(4.5)

    def test_rho_eq_at_r_eq_formula(self):
        """rho_eq = -M^2 / (2*tau^2*R_eq^4) = -0.25 / (2 * 1.5 * (1/81)) = -6.75."""
        expected = -(M_EXT ** 2) / (2.0 * TAU_SQ * (R_EQ ** 4))
        assert RHO_EQ_AT_R_EQ == pytest.approx(expected)

    def test_rho_eq_at_r_eq_value(self):
        assert RHO_EQ_AT_R_EQ == pytest.approx(-6.75)

    def test_rho_eq_is_negative(self):
        assert RHO_EQ_AT_R_EQ < 0.0

    def test_spatial_dimension(self):
        assert SPATIAL_DIMENSION == 3

    def test_derrick_kinetic_exponent(self):
        """D - 2 = 1 for D=3: kinetic energy scales linearly under rescaling."""
        assert DERRICK_KINETIC_EXPONENT == 1

    def test_derrick_skyrme_exponent(self):
        """D - 4 = -1 for D=3: Skyrme term opposes kinetic collapse."""
        assert DERRICK_SKYRME_EXPONENT == -1


# ===========================================================================
# Class 2: Verdict label set — closed and immutable
# ===========================================================================

class TestAllowedVerdictLabels:
    """The allowed verdict set is closed; no new labels may appear."""

    EXPECTED_LABELS = {
        "no_native_localized_bosonic_object_support",
        "shell_localization_only",
        "distributed_profile_without_objecthood",
        "bosonic_topological_defect_supported",
        "stable_bosonic_localized_object_conditionally_supported",
        "particle_candidate_not_yet_established",
    }

    def test_exact_label_set(self):
        assert ALLOWED_VERDICT_LABELS == self.EXPECTED_LABELS

    def test_label_count(self):
        assert len(ALLOWED_VERDICT_LABELS) == 6

    def test_no_native_support_present(self):
        assert "no_native_localized_bosonic_object_support" in ALLOWED_VERDICT_LABELS

    def test_shell_localization_only_present(self):
        assert "shell_localization_only" in ALLOWED_VERDICT_LABELS

    def test_distributed_profile_without_objecthood_present(self):
        assert "distributed_profile_without_objecthood" in ALLOWED_VERDICT_LABELS

    def test_bosonic_topological_defect_supported_present(self):
        assert "bosonic_topological_defect_supported" in ALLOWED_VERDICT_LABELS

    def test_stable_bosonic_conditionally_supported_present(self):
        assert "stable_bosonic_localized_object_conditionally_supported" in ALLOWED_VERDICT_LABELS

    def test_particle_candidate_not_yet_established_present(self):
        assert "particle_candidate_not_yet_established" in ALLOWED_VERDICT_LABELS

    def test_is_frozenset(self):
        assert isinstance(ALLOWED_VERDICT_LABELS, frozenset)


# ===========================================================================
# Class 3: Forbidden claim labels
# ===========================================================================

class TestForbiddenClaimLabels:
    """Pin the list of forbidden inference labels."""

    EXPECTED_LABELS = {
        "nontrivial_profile_implies_particle",
        "shell_equilibrium_implies_localized_bosonic_matter",
        "topological_charge_implies_stable_bosonic_particle",
        "constitutive_field_profile_implies_matter_sector_solved",
        "o3_hedgehog_is_a_stable_particle",
        "phi_eq_profile_is_a_bosonic_particle",
        "shell_localization_implies_matter_objecthood",
        "derrick_obstruction_can_be_ignored",
        "bosonic_charge_sufficient_for_particle_status",
        "profile_objecthood_without_finite_energy_lump",
    }

    def test_all_expected_labels_present(self):
        for label in self.EXPECTED_LABELS:
            assert label in FORBIDDEN_CLAIM_LABELS, f"Missing forbidden label: {label}"

    def test_count_at_least_ten(self):
        assert len(FORBIDDEN_CLAIM_LABELS) >= 10

    def test_derrick_obstruction_cannot_be_ignored(self):
        assert "derrick_obstruction_can_be_ignored" in FORBIDDEN_CLAIM_LABELS

    def test_topological_charge_not_sufficient(self):
        assert "topological_charge_implies_stable_bosonic_particle" in FORBIDDEN_CLAIM_LABELS

    def test_shell_equilibrium_not_matter(self):
        assert "shell_equilibrium_implies_localized_bosonic_matter" in FORBIDDEN_CLAIM_LABELS


# ===========================================================================
# Class 4: Track A — Field Content Inventory
# ===========================================================================

class TestTrackAFieldInventory:
    """Track A: inventory categories and item properties."""

    def test_shell_quantities_contains_phi_trajectory(self, track_a):
        assert "phi_trajectory" in track_a.shell_quantities

    def test_distributed_fields_contains_phi_field(self, track_a):
        assert "phi_field" in track_a.distributed_fields

    def test_topological_objects_contains_o3_triplet(self, track_a):
        assert "o3_triplet" in track_a.topological_objects

    def test_effective_observables_contains_tau_eff(self, track_a):
        assert "tau_eff" in track_a.effective_observables

    def test_effective_observables_contains_r_eq(self, track_a):
        assert "r_eq" in track_a.effective_observables

    def test_effective_observables_contains_omega_0(self, track_a):
        assert "omega_0" in track_a.effective_observables

    def test_effective_observables_contains_psi_proxy(self, track_a):
        assert "psi_proxy" in track_a.effective_observables

    def test_candidate_localized_contains_o3_hedgehog(self, track_a):
        assert "o3_hedgehog_n1" in track_a.candidate_localized_entities

    def test_candidate_count_is_one(self, track_a):
        """Only one candidate entity: the O(3) hedgehog."""
        assert track_a.candidate_count == 1

    def test_phi_trajectory_not_physical_localized(self, track_a):
        """M_drive(t) is a point value, not a localized object."""
        item = next(i for i in track_a.items if i.name == "phi_trajectory")
        assert item.could_be_physical_localized is False

    def test_phi_field_not_physical_localized(self, track_a):
        """Phi(r,t) = M/r^2 is distributed profile, not localized object."""
        item = next(i for i in track_a.items if i.name == "phi_field")
        assert item.could_be_physical_localized is False

    def test_o3_triplet_is_candidate(self, track_a):
        """O(3) triplet with topological charge is candidate (not established)."""
        item = next(i for i in track_a.items if i.name == "o3_triplet")
        assert item.could_be_physical_localized is True

    def test_o3_hedgehog_n1_is_candidate(self, track_a):
        item = next(i for i in track_a.items if i.name == "o3_hedgehog_n1")
        assert item.could_be_physical_localized is True

    def test_psi_proxy_is_diagnostic(self, track_a):
        item = next(i for i in track_a.items if i.name == "psi_proxy")
        assert item.is_diagnostic is True

    def test_tau_eff_is_diagnostic(self, track_a):
        item = next(i for i in track_a.items if i.name == "tau_eff")
        assert item.is_diagnostic is True

    def test_phi_trajectory_domain_is_point_valued(self, track_a):
        item = next(i for i in track_a.items if i.name == "phi_trajectory")
        assert "0+1D" in item.domain or "point" in item.domain.lower()

    def test_phi_field_domain_is_distributed(self, track_a):
        item = next(i for i in track_a.items if i.name == "phi_field")
        assert "distributed" in item.domain.lower() or "r-distributed" in item.domain.lower()

    def test_all_items_have_nonempty_name(self, track_a):
        for item in track_a.items:
            assert item.name, f"Empty name found in inventory"

    def test_all_items_have_nonempty_symbol(self, track_a):
        for item in track_a.items:
            assert item.symbol, f"Empty symbol for item {item.name}"

    def test_all_items_have_valid_category(self, track_a):
        valid_cats = {
            "shell_quantity", "distributed_field", "topological_object",
            "effective_observable", "candidate_localized"
        }
        for item in track_a.items:
            assert item.category in valid_cats, (
                f"Item '{item.name}' has invalid category '{item.category}'"
            )


# ===========================================================================
# Class 5: Track B — Domain Validity
# ===========================================================================

class TestTrackBDomainValidity:
    """Track B: domain enforcement checks."""

    def test_declared_domain_string(self, track_b):
        assert "spherically_symmetric" in track_b.declared_domain
        assert "quasi_static" in track_b.declared_domain
        assert "preferred_frame" in track_b.declared_domain

    def test_covariant_matter_dynamics_not_built(self, track_b):
        assert track_b.covariant_matter_dynamics_built is False

    def test_claims_valid_only_in_domain(self, track_b):
        assert track_b.claims_valid_only_in_domain is True

    def test_unbuilt_dynamics_rejected(self, track_b):
        assert track_b.unbuilt_dynamics_rejected is True

    def test_spherical_symmetry_required(self, track_b):
        assert track_b.spherical_symmetry_required is True

    def test_quasi_static_required(self, track_b):
        assert track_b.quasi_static_required is True

    def test_preferred_frame_required(self, track_b):
        assert track_b.preferred_frame_required is True

    def test_covariant_omega_absent(self, track_b):
        assert track_b.covariant_omega_exists is False

    def test_domain_limitations_nonempty(self, track_b):
        assert len(track_b.domain_limitations) > 0

    def test_domain_limitations_mention_spherical(self, track_b):
        combined = " ".join(track_b.domain_limitations).lower()
        assert "spherical" in combined

    def test_domain_limitations_mention_quasi_static(self, track_b):
        combined = " ".join(track_b.domain_limitations).lower()
        assert "quasi" in combined or "static" in combined

    def test_domain_limitations_mention_preferred_frame(self, track_b):
        combined = " ".join(track_b.domain_limitations).lower()
        assert "frame" in combined

    def test_covariant_matter_rejection_mentioned(self, track_b):
        combined = " ".join(track_b.domain_limitations).lower()
        assert "covariant" in combined or "unbuilt" in combined


# ===========================================================================
# Class 6: Track C — Static Localization
# ===========================================================================

class TestTrackCStaticLocalization:
    """Track C: profile types and localization source classification."""

    def test_three_profiles_defined(self, track_c):
        assert len(track_c.profiles) == 3

    def test_equilibrium_profile_type_is_monotone(self, track_c):
        assert "monotone" in track_c.equilibrium_profile_type

    def test_shell_boundary_condition_imposed(self, track_c):
        assert track_c.shell_boundary_condition_imposed is True

    def test_defect_configuration_exists(self, track_c):
        """O(3) hedgehog defect configuration exists in topology."""
        assert track_c.defect_configuration_exists is True

    def test_finite_energy_lump_not_found(self, track_c):
        assert track_c.finite_energy_lump_solution_found is False

    def test_localization_source_mentions_shell(self, track_c):
        assert "shell" in track_c.localization_source.lower()

    def test_localization_source_mentions_derrick(self, track_c):
        assert "derrick" in track_c.localization_source.lower()

    def test_phi_eq_profile_is_monotone(self, track_c):
        phi_profile = next(p for p in track_c.profiles if p.name == "phi_equilibrium_profile")
        assert phi_profile.is_monotone is True

    def test_phi_eq_profile_has_no_compact_support(self, track_c):
        phi_profile = next(p for p in track_c.profiles if p.name == "phi_equilibrium_profile")
        assert phi_profile.has_compact_support is False

    def test_phi_eq_profile_not_topological_defect(self, track_c):
        phi_profile = next(p for p in track_c.profiles if p.name == "phi_equilibrium_profile")
        assert phi_profile.is_topological_defect is False

    def test_phi_eq_profile_not_finite_energy_lump(self, track_c):
        phi_profile = next(p for p in track_c.profiles if p.name == "phi_equilibrium_profile")
        assert phi_profile.is_finite_energy_lump is False

    def test_o3_hedgehog_is_topological_defect(self, track_c):
        hedge = next(p for p in track_c.profiles if p.name == "o3_hedgehog")
        assert hedge.is_topological_defect is True

    def test_o3_hedgehog_not_finite_energy_lump(self, track_c):
        hedge = next(p for p in track_c.profiles if p.name == "o3_hedgehog")
        assert hedge.is_finite_energy_lump is False

    def test_o3_hedgehog_no_compact_support(self, track_c):
        hedge = next(p for p in track_c.profiles if p.name == "o3_hedgehog")
        assert hedge.has_compact_support is False

    def test_shell_profile_not_finite_energy_lump(self, track_c):
        shell = next(p for p in track_c.profiles if p.name == "shell_confined_profile")
        assert shell.is_finite_energy_lump is False

    def test_shell_profile_not_topological_defect(self, track_c):
        shell = next(p for p in track_c.profiles if p.name == "shell_confined_profile")
        assert shell.is_topological_defect is False

    def test_phi_eq_formula_contains_r_squared(self, track_c):
        phi_profile = next(p for p in track_c.profiles if p.name == "phi_equilibrium_profile")
        formula = phi_profile.profile_formula.lower()
        assert "r^2" in formula or "r**2" in formula or "r²" in formula or "1/r^2" in formula

    def test_o3_hedgehog_formula_contains_hedgehog(self, track_c):
        hedge = next(p for p in track_c.profiles if p.name == "o3_hedgehog")
        formula = hedge.profile_formula.lower()
        assert "hedgehog" in formula or "x^a" in formula or "eta" in formula


# ===========================================================================
# Class 7: Track D — Stability
# ===========================================================================

class TestTrackDStability:
    """Track D: stabilization mechanism classification."""

    def test_shell_stabilization_type(self, track_d):
        assert "boundary_condition" in track_d.shell_stabilization_type

    def test_constitutive_stabilization_type(self, track_d):
        assert "relaxation" in track_d.constitutive_stabilization_type or \
               "attractor" in track_d.constitutive_stabilization_type

    def test_o3_stabilization_type_mentions_derrick(self, track_d):
        assert "derrick" in track_d.o3_stabilization_type.lower()

    def test_o3_stabilization_type_mentions_topological(self, track_d):
        assert "topological" in track_d.o3_stabilization_type.lower()

    def test_energetic_minimum_not_found(self, track_d):
        assert track_d.energetic_minimum_found is False

    def test_stable_localized_object_not_found(self, track_d):
        assert track_d.stable_localized_object_found is False

    def test_stabilization_verdict_mentions_no_stable(self, track_d):
        verdict = track_d.stabilization_verdict.lower()
        assert "no" in verdict or "unstable" in verdict

    def test_stabilization_verdict_mentions_boundary_condition(self, track_d):
        assert "boundary_condition" in track_d.stabilization_verdict

    def test_stabilization_verdict_mentions_derrick(self, track_d):
        assert "derrick" in track_d.stabilization_verdict.lower()

    def test_four_mechanisms_defined(self, track_d):
        assert len(track_d.mechanisms) == 4

    def test_shell_bc_present_in_grut(self, track_d):
        shell_bc = next(m for m in track_d.mechanisms if m.name == "shell_boundary_condition")
        assert shell_bc.is_present_in_grut is True

    def test_shell_bc_insufficient_for_localized_object(self, track_d):
        shell_bc = next(m for m in track_d.mechanisms if m.name == "shell_boundary_condition")
        assert shell_bc.is_sufficient_for_localized_object is False

    def test_relaxation_attractor_present(self, track_d):
        rel = next(m for m in track_d.mechanisms if m.name == "constitutive_relaxation_attractor")
        assert rel.is_present_in_grut is True

    def test_relaxation_attractor_insufficient(self, track_d):
        rel = next(m for m in track_d.mechanisms if m.name == "constitutive_relaxation_attractor")
        assert rel.is_sufficient_for_localized_object is False

    def test_topological_conservation_present(self, track_d):
        top = next(m for m in track_d.mechanisms if m.name == "o3_topological_charge_conservation")
        assert top.is_present_in_grut is True

    def test_topological_conservation_insufficient(self, track_d):
        top = next(m for m in track_d.mechanisms if m.name == "o3_topological_charge_conservation")
        assert top.is_sufficient_for_localized_object is False

    def test_skyrme_term_absent(self, track_d):
        skyrme = next(m for m in track_d.mechanisms if m.name == "skyrme_quartic_term")
        assert skyrme.is_present_in_grut is False

    def test_skyrme_term_would_be_sufficient(self, track_d):
        """The Skyrme term IS sufficient — it is just absent."""
        skyrme = next(m for m in track_d.mechanisms if m.name == "skyrme_quartic_term")
        assert skyrme.is_sufficient_for_localized_object is True

    def test_mechanism_types_valid(self, track_d):
        valid_types = {
            "boundary_condition", "topological", "energetic",
            "constitutive_relaxation", "none"
        }
        for m in track_d.mechanisms:
            assert m.mechanism_type in valid_types, (
                f"Invalid mechanism type '{m.mechanism_type}' for '{m.name}'"
            )


# ===========================================================================
# Class 8: Derrick's Theorem
# ===========================================================================

class TestDerrickAnalysis:
    """Derrick's theorem structural facts."""

    def test_spatial_dimension_is_3(self, derrick):
        assert derrick.spatial_dimension == 3

    def test_kinetic_exponent_is_d_minus_2(self, derrick):
        assert derrick.kinetic_scaling_exponent == derrick.spatial_dimension - 2

    def test_kinetic_exponent_value(self, derrick):
        assert derrick.kinetic_scaling_exponent == 1

    def test_skyrme_exponent_is_d_minus_4(self, derrick):
        assert derrick.skyrme_scaling_exponent == derrick.spatial_dimension - 4

    def test_skyrme_exponent_value(self, derrick):
        assert derrick.skyrme_scaling_exponent == -1

    def test_kinetic_term_present(self, derrick):
        assert derrick.kinetic_term_present is True

    def test_skyrme_term_absent(self, derrick):
        assert derrick.skyrme_term_present is False

    def test_stable_soliton_not_possible(self, derrick):
        assert derrick.stable_soliton_possible is False

    def test_derrick_obstruction_active(self, derrick):
        assert derrick.derrick_obstruction_active is True

    def test_what_would_fix_it_mentions_skyrme(self, derrick):
        assert "skyrme" in derrick.what_would_fix_it.lower() or \
               "quartic" in derrick.what_would_fix_it.lower()

    def test_reference_cites_derrick_1964(self, derrick):
        assert "1964" in derrick.reference or "derrick" in derrick.reference.lower()

    def test_reference_cites_skyrme(self, derrick):
        assert "skyrme" in derrick.reference.lower() or "1961" in derrick.reference

    def test_derrick_implies_no_energetic_minimum(self, derrick):
        """Without Skyrme term, kinetic energy is linear in lambda -> no minimum."""
        assert derrick.skyrme_term_present is False
        assert derrick.stable_soliton_possible is False

    def test_kinetic_scaling_linear_in_d3(self, derrick):
        """In D=3, kinetic energy E ~ lambda^1 under r -> lambda*r."""
        assert derrick.kinetic_scaling_exponent == 1
        # Linear scaling means d(E)/d(lambda) = E > 0: no stationary point
        # (only minimum at lambda->0, i.e., collapse)

    def test_skyrme_scaling_inverse_in_d3(self, derrick):
        """In D=3, Skyrme energy E_4 ~ lambda^{-1}: opposes collapse."""
        assert derrick.skyrme_scaling_exponent == -1


# ===========================================================================
# Class 9: Track E — Finite Energy
# ===========================================================================

class TestTrackEFiniteEnergy:
    """Track E: finite-energy and normalizability gating."""

    def test_finite_energy_lump_not_found(self, track_e):
        assert track_e.finite_energy_lump_found is False

    def test_phi_field_energy_density_formula(self, track_e):
        formula = track_e.phi_field_energy_density_formula.lower()
        assert "m^2" in formula or "m**2" in formula or "m²" in formula
        assert "tau" in formula or "τ" in formula
        assert "r^4" in formula or "r**4" in formula or "r⁴" in formula

    def test_phi_field_energy_diverges_at_origin(self, track_e):
        assert track_e.phi_field_energy_diverges_at_origin is True

    def test_phi_field_energy_requires_cutoffs(self, track_e):
        assert track_e.phi_field_energy_requires_cutoffs is True

    def test_shell_provides_ir_cutoff(self, track_e):
        assert track_e.shell_provides_ir_cutoff is True

    def test_energy_classification_mentions_cutoff_dependent(self, track_e):
        assert "cutoff" in track_e.energy_classification.lower()

    def test_energy_classification_not_intrinsic(self, track_e):
        assert "intrinsic" in track_e.energy_classification.lower()

    def test_rho_eq_at_r_eq_value(self, track_e):
        assert track_e.rho_eq_at_r_eq == pytest.approx(-6.75)

    def test_rho_eq_at_r_eq_is_negative(self, track_e):
        assert track_e.rho_eq_at_r_eq < 0.0

    def test_derrick_analysis_embedded(self, track_e):
        assert isinstance(track_e.derrick_analysis, DerrickAnalysis)

    def test_derrick_obstruction_in_track_e(self, track_e):
        assert track_e.derrick_analysis.derrick_obstruction_active is True

    def test_skyrme_absent_in_track_e(self, track_e):
        assert track_e.derrick_analysis.skyrme_term_present is False

    def test_shell_cutoff_makes_localization_non_intrinsic(self, track_e):
        """Shell provides IR cutoff — localization is not intrinsic to field dynamics."""
        assert track_e.shell_provides_ir_cutoff is True
        assert track_e.phi_field_energy_requires_cutoffs is True
        assert track_e.finite_energy_lump_found is False


# ===========================================================================
# Class 10: Track F — Topological Bosonic Content
# ===========================================================================

class TestTrackFTopologicalBosonic:
    """Track F: topological charge vs particle-status distinction."""

    def test_pi2_s2_is_Z(self, track_f):
        assert track_f.pi2_s2 == "Z"

    def test_winding_number_type_integer(self, track_f):
        assert "integer" in track_f.winding_number_type.lower() or \
               "Z" in track_f.winding_number_type

    def test_bosonic_topological_charge_present(self, track_f):
        """π₂(S²) = ℤ gives bosonic integer winding numbers."""
        assert track_f.bosonic_topological_charge_present is True

    def test_hedgehog_n1_configuration_defined(self, track_f):
        assert track_f.hedgehog_n1_configuration_defined is True

    def test_hedgehog_statistics_is_bosonic(self, track_f):
        assert track_f.hedgehog_statistics == "bosonic"

    def test_stable_bosonic_defect_not_present(self, track_f):
        """Derrick's theorem: no stable defect without Skyrme term."""
        assert track_f.stable_bosonic_defect_present is False

    def test_skyrme_term_absent(self, track_f):
        assert track_f.skyrme_term_absent is True

    def test_particle_interpretation_not_established(self, track_f):
        assert track_f.particle_interpretation_established is False

    def test_o3_is_not_canonical_grut(self, track_f):
        """O(3) is a candidate extension (Phase D1+), not canonical GRUT."""
        assert track_f.o3_is_canonical_grut is False

    def test_topological_charge_not_sufficient_for_particle(self, track_f):
        """Bosonic charge is necessary but not sufficient for particle status."""
        assert track_f.topological_charge_sufficient_for_particle is False

    def test_classification_mentions_bosonic_charge(self, track_f):
        assert "bosonic" in track_f.classification.lower() or \
               "topological" in track_f.classification.lower()

    def test_classification_mentions_candidate_not_established(self, track_f):
        assert "candidate" in track_f.classification.lower() or \
               "not_yet" in track_f.classification.lower()

    def test_charge_present_but_particle_absent(self, track_f):
        """The key distinction: charge exists, particle does not."""
        assert track_f.bosonic_topological_charge_present is True
        assert track_f.particle_interpretation_established is False

    def test_hedgehog_statistics_not_fermionic(self, track_f):
        assert "fermionic" not in track_f.hedgehog_statistics.lower()

    def test_winding_type_not_half_integer(self, track_f):
        wt = track_f.winding_number_type.lower()
        assert "half" not in wt


# ===========================================================================
# Class 11: Track G — Nonclaim Firewall
# ===========================================================================

class TestTrackGNoclaimFirewall:
    """Track G: nonclaim enforcement and forbidden claim checks."""

    def test_no_forbidden_claims_triggered(self, track_g):
        assert track_g.any_triggered is False

    def test_all_forbidden_checks_not_triggered(self, track_g):
        for check in track_g.forbidden_checks:
            assert not check.triggered, (
                f"Forbidden claim triggered: {check.claim_label}"
            )

    def test_nontrivial_profile_not_particle(self, track_g):
        check = next(
            c for c in track_g.forbidden_checks
            if c.claim_label == "nontrivial_profile_implies_particle"
        )
        assert not check.triggered

    def test_shell_equilibrium_not_matter(self, track_g):
        check = next(
            c for c in track_g.forbidden_checks
            if c.claim_label == "shell_equilibrium_implies_localized_bosonic_matter"
        )
        assert not check.triggered

    def test_topological_charge_not_particle(self, track_g):
        check = next(
            c for c in track_g.forbidden_checks
            if c.claim_label == "topological_charge_implies_stable_bosonic_particle"
        )
        assert not check.triggered

    def test_constitutive_profile_not_matter_solved(self, track_g):
        check = next(
            c for c in track_g.forbidden_checks
            if c.claim_label == "constitutive_field_profile_implies_matter_sector_solved"
        )
        assert not check.triggered

    def test_o3_hedgehog_not_stable_particle(self, track_g):
        check = next(
            c for c in track_g.forbidden_checks
            if c.claim_label == "o3_hedgehog_is_a_stable_particle"
        )
        assert not check.triggered

    def test_derrick_obstruction_not_ignored(self, track_g):
        check = next(
            c for c in track_g.forbidden_checks
            if c.claim_label == "derrick_obstruction_can_be_ignored"
        )
        assert not check.triggered

    def test_nonclaims_nonempty(self, track_g):
        assert len(track_g.nonclaims) > 0

    def test_nonclaims_count_at_least_six(self, track_g):
        assert len(track_g.nonclaims) >= 6

    def test_nonclaim_about_shell(self, track_g):
        combined = " ".join(track_g.nonclaims).lower()
        assert "shell" in combined

    def test_nonclaim_about_o3_hedgehog(self, track_g):
        combined = " ".join(track_g.nonclaims).lower()
        assert "hedgehog" in combined or "o(3)" in combined or "o3" in combined

    def test_nonclaim_about_topological_charge(self, track_g):
        combined = " ".join(track_g.nonclaims).lower()
        assert "topological" in combined or "charge" in combined

    def test_nonclaim_not_ruling_out_forever(self, track_g):
        combined = " ".join(track_g.nonclaims).lower()
        assert "forever" in combined or "ruling out" in combined or "not ruling" in combined

    def test_nonclaim_about_profile_not_object(self, track_g):
        combined = " ".join(track_g.nonclaims).lower()
        assert "profile" in combined

    def test_all_check_labels_nonempty(self, track_g):
        for check in track_g.forbidden_checks:
            assert check.claim_label, "Empty claim label in firewall check"

    def test_all_check_reasons_nonempty(self, track_g):
        for check in track_g.forbidden_checks:
            assert check.reason, f"Empty reason for claim: {check.claim_label}"


# ===========================================================================
# Class 12: Verdict assignment logic
# ===========================================================================

class TestVerdictAssignment:
    """Test the deterministic verdict assignment function."""

    def test_primary_verdict_is_particle_candidate_not_yet_established(self, audit):
        assert audit.primary_verdict == "particle_candidate_not_yet_established"

    def test_primary_verdict_in_allowed_set(self, audit):
        assert audit.primary_verdict in ALLOWED_VERDICT_LABELS

    def test_secondary_verdicts_all_in_allowed_set(self, audit):
        for sv in audit.secondary_verdicts:
            assert sv in ALLOWED_VERDICT_LABELS, (
                f"Secondary verdict '{sv}' not in allowed set"
            )

    def test_secondary_verdicts_contains_shell_localization_only(self, audit):
        assert "shell_localization_only" in audit.secondary_verdicts

    def test_secondary_verdicts_contains_distributed_profile_without_objecthood(self, audit):
        assert "distributed_profile_without_objecthood" in audit.secondary_verdicts

    def test_no_stable_object_verdict(self, audit):
        """Verdict must NOT claim stable object or solved matter."""
        assert audit.primary_verdict != "stable_bosonic_localized_object_conditionally_supported"
        assert audit.primary_verdict != "bosonic_topological_defect_supported"

    def test_not_no_support_verdict(self, audit):
        """O(3) topological charge is present -> not 'no_native_support'."""
        assert audit.primary_verdict != "no_native_localized_bosonic_object_support"

    def test_verdict_reflects_bosonic_charge_without_stability(self, audit):
        """Verdict: charge present, stability not established -> candidate not established."""
        assert audit.topological_bosonic_charge_present is True
        assert audit.stable_bosonic_defect_present is False
        assert audit.primary_verdict == "particle_candidate_not_yet_established"

    def test_secondary_verdict_count_is_two(self, audit):
        assert len(audit.secondary_verdicts) == 2


# ===========================================================================
# Class 13: Top-level boolean summary
# ===========================================================================

class TestTopLevelBooleans:
    """Pin the top-level summary booleans of the master audit result."""

    def test_constitutive_phi_supports_spatial_profile(self, audit):
        assert audit.constitutive_phi_supports_spatial_profile is True

    def test_shell_supported_localization_is_true(self, audit):
        assert audit.shell_supported_localization is True

    def test_finite_energy_lump_not_found(self, audit):
        assert audit.finite_energy_lump_found is False

    def test_topological_bosonic_charge_present(self, audit):
        assert audit.topological_bosonic_charge_present is True

    def test_stable_bosonic_defect_not_present(self, audit):
        assert audit.stable_bosonic_defect_present is False

    def test_particle_like_object_not_present(self, audit):
        assert audit.particle_like_object_present is False

    def test_no_forbidden_claims_triggered(self, audit):
        assert audit.forbidden_claims_triggered == []

    def test_nonclaims_nonempty(self, audit):
        assert len(audit.nonclaims) > 0


# ===========================================================================
# Class 14: Stabilization mechanism verdict string
# ===========================================================================

class TestStabilizationMechanismVerdict:
    """The stabilization_mechanism field must accurately describe the situation."""

    def test_mentions_no_stable_object(self, audit):
        vm = audit.stabilization_mechanism.lower()
        assert "no" in vm or "unstable" in vm

    def test_mentions_boundary_condition(self, audit):
        assert "boundary_condition" in audit.stabilization_mechanism.lower()

    def test_mentions_o3_topological(self, audit):
        vm = audit.stabilization_mechanism.lower()
        assert "topological" in vm or "o3" in vm

    def test_mentions_derrick(self, audit):
        assert "derrick" in audit.stabilization_mechanism.lower()

    def test_mentions_skyrme(self, audit):
        assert "skyrme" in audit.stabilization_mechanism.lower()


# ===========================================================================
# Class 15: Domain limitations in master result
# ===========================================================================

class TestDomainLimitationsInMasterResult:
    """Domain limitations must be present and accurate in master result."""

    def test_domain_limitations_nonempty(self, audit):
        assert len(audit.domain_limitations) > 0

    def test_domain_limitations_mention_spherical(self, audit):
        combined = " ".join(audit.domain_limitations).lower()
        assert "spherical" in combined

    def test_domain_limitations_mention_quasi_static(self, audit):
        combined = " ".join(audit.domain_limitations).lower()
        assert "quasi" in combined or "static" in combined

    def test_domain_limitations_mention_preferred_frame(self, audit):
        combined = " ".join(audit.domain_limitations).lower()
        assert "frame" in combined

    def test_domain_limitations_mention_covariant_missing(self, audit):
        combined = " ".join(audit.domain_limitations).lower()
        assert "covariant" in combined or "unbuilt" in combined


# ===========================================================================
# Class 16: Native field content inventory in master result
# ===========================================================================

class TestNativeFieldContentInventory:
    """The native_field_content_inventory dict has required categories and content."""

    def test_has_shell_quantities(self, audit):
        assert "shell_quantities" in audit.native_field_content_inventory

    def test_has_distributed_fields(self, audit):
        assert "distributed_fields" in audit.native_field_content_inventory

    def test_has_topological_objects(self, audit):
        assert "topological_objects" in audit.native_field_content_inventory

    def test_has_effective_observables(self, audit):
        assert "effective_observables" in audit.native_field_content_inventory

    def test_has_candidate_localized_entities(self, audit):
        assert "candidate_localized_entities" in audit.native_field_content_inventory

    def test_shell_quantities_has_phi_trajectory(self, audit):
        assert "phi_trajectory" in audit.native_field_content_inventory["shell_quantities"]

    def test_distributed_fields_has_phi_field(self, audit):
        assert "phi_field" in audit.native_field_content_inventory["distributed_fields"]

    def test_topological_objects_has_o3_triplet(self, audit):
        assert "o3_triplet" in audit.native_field_content_inventory["topological_objects"]

    def test_candidate_localized_entities_has_hedgehog(self, audit):
        assert "o3_hedgehog_n1" in audit.native_field_content_inventory["candidate_localized_entities"]

    def test_candidate_localized_entities_count_is_one(self, audit):
        assert len(audit.native_field_content_inventory["candidate_localized_entities"]) == 1


# ===========================================================================
# Class 17: Diagnostics dict
# ===========================================================================

class TestDiagnosticsDict:
    """Diagnostics dict pins key numerical and Boolean values."""

    def test_m_ext_in_diagnostics(self, audit):
        assert audit.diagnostics["M_EXT"] == pytest.approx(0.5)

    def test_r_eq_in_diagnostics(self, audit):
        assert audit.diagnostics["R_EQ"] == pytest.approx(1.0 / 3.0)

    def test_tau_sq_in_diagnostics(self, audit):
        assert audit.diagnostics["TAU_SQ"] == pytest.approx(1.5)

    def test_alpha_vac_in_diagnostics(self, audit):
        assert audit.diagnostics["ALPHA_VAC"] == pytest.approx(1.0 / 3.0)

    def test_omega_0_sq_in_diagnostics(self, audit):
        assert audit.diagnostics["OMEGA_0_SQ"] == pytest.approx(27.0)

    def test_rho_eq_in_diagnostics(self, audit):
        assert audit.diagnostics["RHO_EQ_AT_R_EQ"] == pytest.approx(-6.75)

    def test_spatial_dimension_in_diagnostics(self, audit):
        assert audit.diagnostics["SPATIAL_DIMENSION"] == 3

    def test_derrick_kinetic_exponent_in_diagnostics(self, audit):
        assert audit.diagnostics["DERRICK_KINETIC_EXPONENT"] == 1

    def test_derrick_skyrme_exponent_in_diagnostics(self, audit):
        assert audit.diagnostics["DERRICK_SKYRME_EXPONENT"] == -1

    def test_finite_energy_lump_found_false(self, audit):
        assert audit.diagnostics["finite_energy_lump_found"] is False

    def test_topological_charge_present_true(self, audit):
        assert audit.diagnostics["topological_bosonic_charge_present"] is True

    def test_stable_defect_false(self, audit):
        assert audit.diagnostics["stable_bosonic_defect_present"] is False

    def test_particle_like_false(self, audit):
        assert audit.diagnostics["particle_like_object_present"] is False

    def test_derrick_obstruction_active(self, audit):
        assert audit.diagnostics["derrick_obstruction_active"] is True

    def test_skyrme_term_absent(self, audit):
        assert audit.diagnostics["skyrme_term_present"] is False

    def test_o3_statistics_bosonic(self, audit):
        assert audit.diagnostics["o3_statistics"] == "bosonic"

    def test_o3_not_canonical_grut(self, audit):
        assert audit.diagnostics["o3_is_canonical_grut"] is False

    def test_covariant_matter_not_built(self, audit):
        assert audit.diagnostics["covariant_matter_dynamics_built"] is False

    def test_forbidden_claims_triggered_count_zero(self, audit):
        assert audit.diagnostics["forbidden_claims_triggered_count"] == 0

    def test_primary_verdict_in_diagnostics(self, audit):
        assert audit.diagnostics["primary_verdict"] == "particle_candidate_not_yet_established"


# ===========================================================================
# Class 18: Cross-consistency checks
# ===========================================================================

class TestCrossConsistency:
    """Cross-checks across tracks for internal consistency."""

    def test_topological_charge_present_consistent_with_o3_in_inventory(self, audit, track_a):
        """If topological charge is present, O(3) must be in topological_objects."""
        assert audit.topological_bosonic_charge_present is True
        assert "o3_triplet" in track_a.topological_objects

    def test_stable_defect_false_consistent_with_derrick(self, audit, track_e):
        """stable_bosonic_defect_present=False is consistent with Derrick obstruction."""
        assert audit.stable_bosonic_defect_present is False
        assert track_e.derrick_analysis.derrick_obstruction_active is True

    def test_finite_energy_lump_false_consistent_with_skyrme_absent(self, audit, track_e):
        """finite_energy_lump_found=False consistent with Skyrme term absent."""
        assert audit.finite_energy_lump_found is False
        assert track_e.derrick_analysis.skyrme_term_present is False

    def test_shell_localization_consistent_with_track_c(self, audit, track_c):
        """shell_supported_localization=True consistent with shell BC imposed."""
        assert audit.shell_supported_localization is True
        assert track_c.shell_boundary_condition_imposed is True

    def test_profile_present_consistent_with_track_c(self, audit, track_c):
        """constitutive_phi_supports_spatial_profile consistent with M/r^2 profile."""
        assert audit.constitutive_phi_supports_spatial_profile is True
        phi_profile = next(p for p in track_c.profiles if p.name == "phi_equilibrium_profile")
        assert phi_profile.is_monotone is True

    def test_particle_false_consistent_with_track_f(self, audit, track_f):
        assert audit.particle_like_object_present is False
        assert track_f.particle_interpretation_established is False

    def test_no_forbidden_triggers_consistent_with_track_g(self, audit, track_g):
        assert audit.forbidden_claims_triggered == []
        assert track_g.any_triggered is False

    def test_domain_stated_in_track_b_and_master_result(self, audit, track_b):
        assert track_b.declared_domain in audit.diagnostics["declared_domain"]

    def test_candidate_in_inventory_consistent_with_primary_verdict(self, audit, track_a):
        """At least one candidate entity => verdict not 'no_native_localized_bosonic_object_support'."""
        assert track_a.candidate_count >= 1
        assert audit.primary_verdict != "no_native_localized_bosonic_object_support"

    def test_derrick_in_track_d_and_track_e(self, track_d, track_e):
        """Derrick obstruction appears in both stability and finite-energy tracks."""
        assert "derrick" in track_d.o3_stabilization_type.lower()
        assert track_e.derrick_analysis.derrick_obstruction_active is True

    def test_charge_bosonic_not_fermionic(self, track_f):
        """Bosonic charge from pi_2(S^2)=Z; no Hopf term -> no fermionic statistics."""
        assert track_f.hedgehog_statistics == "bosonic"
        assert track_f.pi2_s2 == "Z"

    def test_x_eq_consistent_with_m_ext_r_eq(self):
        """X_eq = M/R_eq^2 = 0.5 / (1/9) = 4.5."""
        assert X_EQ == pytest.approx(M_EXT / (R_EQ ** 2))
        assert X_EQ == pytest.approx(4.5)

    def test_omega_0_tau_product_at_canon(self):
        """omega_0 * tau_eff = 1 at equilibrium (tau_eff = 1/omega_0)."""
        tau_eff_canon = 1.0 / OMEGA_0
        assert OMEGA_0 * tau_eff_canon == pytest.approx(1.0)

    def test_rho_eq_formula_consistent_with_constants(self):
        expected = -(M_EXT ** 2) / (2.0 * TAU_SQ * (R_EQ ** 4))
        assert RHO_EQ_AT_R_EQ == pytest.approx(expected, rel=1e-10)


# ===========================================================================
# Class 19: End-to-end master audit
# ===========================================================================

class TestMasterAudit:
    """End-to-end test of run_localized_bosonic_object_audit()."""

    def test_returns_correct_type(self, audit):
        assert isinstance(audit, LocalizedBosonicObjectResult)

    def test_all_tracks_populated(self, audit):
        assert audit.track_a is not None
        assert audit.track_b is not None
        assert audit.track_c is not None
        assert audit.track_d is not None
        assert audit.track_e is not None
        assert audit.track_f is not None
        assert audit.track_g is not None

    def test_native_field_content_inventory_is_dict(self, audit):
        assert isinstance(audit.native_field_content_inventory, dict)

    def test_diagnostics_is_dict(self, audit):
        assert isinstance(audit.diagnostics, dict)

    def test_nonclaims_is_list(self, audit):
        assert isinstance(audit.nonclaims, list)

    def test_forbidden_claims_triggered_is_list(self, audit):
        assert isinstance(audit.forbidden_claims_triggered, list)

    def test_secondary_verdicts_is_list(self, audit):
        assert isinstance(audit.secondary_verdicts, list)

    def test_primary_verdict_is_string(self, audit):
        assert isinstance(audit.primary_verdict, str)

    def test_stabilization_mechanism_is_string(self, audit):
        assert isinstance(audit.stabilization_mechanism, str)

    def test_domain_limitations_is_list(self, audit):
        assert isinstance(audit.domain_limitations, list)

    def test_full_deterministic_summary(self, audit):
        """Pin every top-level Boolean in one test."""
        assert audit.constitutive_phi_supports_spatial_profile is True
        assert audit.shell_supported_localization is True
        assert audit.finite_energy_lump_found is False
        assert audit.topological_bosonic_charge_present is True
        assert audit.stable_bosonic_defect_present is False
        assert audit.particle_like_object_present is False
        assert audit.primary_verdict == "particle_candidate_not_yet_established"
        assert "shell_localization_only" in audit.secondary_verdicts
        assert "distributed_profile_without_objecthood" in audit.secondary_verdicts
        assert audit.forbidden_claims_triggered == []

    def test_audit_is_idempotent(self):
        """Running the audit twice produces identical verdicts."""
        r1 = run_localized_bosonic_object_audit()
        r2 = run_localized_bosonic_object_audit()
        assert r1.primary_verdict == r2.primary_verdict
        assert r1.secondary_verdicts == r2.secondary_verdicts
        assert r1.finite_energy_lump_found == r2.finite_energy_lump_found
        assert r1.topological_bosonic_charge_present == r2.topological_bosonic_charge_present
        assert r1.stable_bosonic_defect_present == r2.stable_bosonic_defect_present
        assert r1.forbidden_claims_triggered == r2.forbidden_claims_triggered
