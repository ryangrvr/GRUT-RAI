"""Tests for Z-B --- Cumulative Postulate, Parameter, Field, DOF, and Closure Accounting."""
import math
import pytest
from grut.zb_cumulative_postulate_parameter_accounting import (
    TAU_SQ, TAU, GAMMA,
    N_POSTULATES_W, N_POSTULATES_X, N_POSTULATES_Y, N_POSTULATES_TOTAL,
    N_PARAMS_FREE, N_PARAMS_DERIVED, N_NEW_FIELDS, N_NEW_DOF, N_FORMAL_OBJECTS,
    N_EQUATIONS_FOUNDATIONAL, N_EQUATIONS_OPERATIONAL, N_EQUATIONS_INTERFACE,
    N_ABSENT_SECTORS, N_POSTULATE_ITEMS, N_PARAMETER_ITEMS, N_FIELD_DOF_ITEMS,
    N_BOUGHT_VS_COST, N_ZB_NONCLAIMS, N_ALLOWED, N_FORBIDDEN,
    POSTULATE_OPTIONS, PARAMETER_OPTIONS, FIELD_DOF_OPTIONS,
    ECONOMY_OPTIONS, AUTH_OPTIONS, OVERALL_OPTIONS,
    POSTULATE_CATEGORIES, PARAMETER_CATEGORIES, FIELD_DOF_CATEGORIES,
    ABSENCE_CATEGORIES,
    ZB_POSTULATE, ZB_PARAMETER, ZB_FIELD_DOF, ZB_ECONOMY, ZB_AUTH, ZB_OVERALL,
    ZB_NONCLAIMS,
    run_zb_cumulative_postulate_parameter_accounting, _self_test,
)

@pytest.fixture(scope="module")
def result():
    return run_zb_cumulative_postulate_parameter_accounting()


# ── Constants ──

class TestConstants:
    def test_tau_sq(self): assert TAU_SQ == 1.5
    def test_tau(self): assert abs(TAU - math.sqrt(1.5)) < 1e-12
    def test_gamma(self): assert abs(GAMMA - 1.0 / TAU) < 1e-12
    def test_gamma_tau(self): assert abs(GAMMA * TAU - 1.0) < 1e-12
    def test_postulate_total(self): assert N_POSTULATES_TOTAL == 7
    def test_postulate_partition(self):
        assert N_POSTULATES_W + N_POSTULATES_X + N_POSTULATES_Y == N_POSTULATES_TOTAL
    def test_w_count(self): assert N_POSTULATES_W == 4
    def test_x_count(self): assert N_POSTULATES_X == 3
    def test_y_count(self): assert N_POSTULATES_Y == 0
    def test_params_free(self): assert N_PARAMS_FREE == 3
    def test_params_derived(self): assert N_PARAMS_DERIVED == 4
    def test_new_fields(self): assert N_NEW_FIELDS == 0
    def test_new_dof(self): assert N_NEW_DOF == 0
    def test_formal_objects(self): assert N_FORMAL_OBJECTS == 6
    def test_absent(self): assert N_ABSENT_SECTORS == 10


# ── Track A: Postulate Ledger ──

class TestPostulateLedger:
    def test_count(self, result):
        assert len(result.postulate_ledger) == N_POSTULATE_ITEMS
    def test_w_partition(self, result):
        n = sum(1 for p in result.postulate_ledger if p.layer == "W")
        assert n == N_POSTULATES_W
    def test_x_partition(self, result):
        n = sum(1 for p in result.postulate_ledger if p.layer == "X")
        assert n == N_POSTULATES_X
    def test_y_partition(self, result):
        n = sum(1 for p in result.postulate_ledger if p.layer == "Y")
        assert n == N_POSTULATES_Y
    def test_categories_valid(self, result):
        for p in result.postulate_ledger:
            assert p.category in POSTULATE_CATEGORIES
    def test_true_new_count(self, result):
        n = sum(1 for p in result.postulate_ledger if p.category == "true_new_postulate")
        assert n == 5
    def test_consequence_count(self, result):
        n = sum(1 for p in result.postulate_ledger if p.category == "consequence_of_prior_postulate")
        assert n == 2
    def test_wp3_consequence(self, result):
        wp3 = [p for p in result.postulate_ledger if p.item_id == "W.P3"][0]
        assert wp3.category == "consequence_of_prior_postulate"
        assert wp3.new_params_introduced == 0
    def test_wp4_consequence(self, result):
        wp4 = [p for p in result.postulate_ledger if p.item_id == "W.P4"][0]
        assert wp4.category == "consequence_of_prior_postulate"
        assert wp4.new_params_introduced == 0
    def test_total_new_params(self, result):
        total = sum(p.new_params_introduced for p in result.postulate_ledger)
        assert total == N_PARAMS_FREE  # only W.P1 (2) + W.P2 (1) = 3
    def test_ids_unique(self, result):
        ids = [p.item_id for p in result.postulate_ledger]
        assert len(ids) == len(set(ids))


# ── Track B: Parameter Ledger ──

class TestParameterLedger:
    def test_count(self, result):
        assert len(result.parameter_ledger) == N_PARAMETER_ITEMS
    def test_free_count(self, result):
        n = sum(1 for p in result.parameter_ledger if p.is_free)
        assert n == N_PARAMS_FREE
    def test_derived_count(self, result):
        n = sum(1 for p in result.parameter_ledger if not p.is_free)
        assert n == N_PARAMS_DERIVED
    def test_categories_valid(self, result):
        for p in result.parameter_ledger:
            assert p.category in PARAMETER_CATEGORIES
    def test_tau2_free(self, result):
        p = [x for x in result.parameter_ledger if x.param_id == "P1"][0]
        assert p.is_free and p.name == "tau2"
    def test_l2_free(self, result):
        p = [x for x in result.parameter_ledger if x.param_id == "P2"][0]
        assert p.is_free and p.name == "L2"
    def test_alpha_free(self, result):
        p = [x for x in result.parameter_ledger if x.param_id == "P3"][0]
        assert p.is_free and p.name == "alpha"
    def test_tau1_native(self, result):
        p = [x for x in result.parameter_ledger if x.param_id == "D3"][0]
        assert not p.is_free and p.category == "native_parameter"
    def test_v_derived(self, result):
        p = [x for x in result.parameter_ledger if x.param_id == "D1"][0]
        assert not p.is_free and p.category == "derived_scale"
    def test_gamma_derived(self, result):
        p = [x for x in result.parameter_ledger if x.param_id == "D4"][0]
        assert not p.is_free and p.category == "derived_scale"


# ── Track C: Field/DOF Ledger ──

class TestFieldDOFLedger:
    def test_count(self, result):
        assert len(result.field_dof_ledger) == N_FIELD_DOF_ITEMS
    def test_no_new_fields(self, result):
        assert result.n_new_fields == 0
        n = sum(1 for f in result.field_dof_ledger if f.counted_as_field)
        assert n == 0
    def test_no_new_dof(self, result):
        assert result.n_new_dof == 0
        n = sum(1 for f in result.field_dof_ledger if f.counted_as_dof)
        assert n == 0
    def test_categories_valid(self, result):
        for f in result.field_dof_ledger:
            assert f.category in FIELD_DOF_CATEGORIES
    def test_phi_native(self, result):
        phi = [f for f in result.field_dof_ledger if f.name == "Phi"][0]
        assert phi.category == "native_physical_field"
    def test_rho_state_space(self, result):
        rho = [f for f in result.field_dof_ledger if f.name == "rho"][0]
        assert rho.category == "state_space_object"
        assert not rho.counted_as_field
    def test_seff_formal(self, result):
        s = [f for f in result.field_dof_ledger if f.name == "S_eff"][0]
        assert s.category == "formal_packaging"
    def test_geff_formal(self, result):
        g = [f for f in result.field_dof_ledger if f.name == "g_eff"][0]
        assert g.category == "formal_packaging"
    def test_formal_count(self, result):
        assert result.n_formal_objects == N_FORMAL_OBJECTS


# ── Track D: Equation Ledger ──

class TestEquationLedger:
    def test_total(self, result):
        assert len(result.equation_ledger) == (
            N_EQUATIONS_FOUNDATIONAL + N_EQUATIONS_OPERATIONAL + N_EQUATIONS_INTERFACE)
    def test_foundational(self, result):
        assert result.n_equations_foundational == N_EQUATIONS_FOUNDATIONAL
    def test_operational(self, result):
        assert result.n_equations_operational == N_EQUATIONS_OPERATIONAL
    def test_interface(self, result):
        assert result.n_equations_interface == N_EQUATIONS_INTERFACE
    def test_eq1_telegrapher(self, result):
        eq = [e for e in result.equation_ledger if e.eq_id == "EQ1"][0]
        assert "tau2" in eq.equation and eq.category == "foundational"
    def test_eq3_born(self, result):
        eq = [e for e in result.equation_ledger if e.eq_id == "EQ3"][0]
        assert "Tr" in eq.equation and eq.category == "foundational"
    def test_eq4_lindblad(self, result):
        eq = [e for e in result.equation_ledger if e.eq_id == "EQ4"][0]
        assert "rho" in eq.equation and eq.category == "foundational"


# ── Track E: Bought vs Cost ──

class TestBoughtVsCost:
    def test_count(self, result):
        assert len(result.bought_vs_cost) == N_BOUGHT_VS_COST
    def test_layers_present(self, result):
        layers = {b.layer for b in result.bought_vs_cost}
        assert "W" in layers and "X" in layers and "Y" in layers
    def test_ids_unique(self, result):
        ids = [b.entry_id for b in result.bought_vs_cost]
        assert len(ids) == len(set(ids))
    def test_w_propagation(self, result):
        b = [x for x in result.bought_vs_cost if x.entry_id == "BvC1"][0]
        assert "speed" in b.what_bought.lower() or "propagation" in b.what_bought.lower()
    def test_x_probability(self, result):
        b = [x for x in result.bought_vs_cost if x.entry_id == "BvC4"][0]
        assert "probability" in b.what_bought.lower() or "Born" in b.what_bought


# ── Track F: Absent Sectors ──

class TestAbsentSectors:
    def test_count(self, result):
        assert len(result.absent_sectors) == N_ABSENT_SECTORS
    def test_categories_valid(self, result):
        for a in result.absent_sectors:
            assert a.absence_class in ABSENCE_CATEGORIES
    def test_blocked_count(self, result):
        n = sum(1 for a in result.absent_sectors if a.absence_class == "blocked_by_structure")
        assert n == 2  # fermions and chemistry
    def test_absent_count(self, result):
        n = sum(1 for a in result.absent_sectors if a.absence_class == "absent_unbuilt")
        assert n == 8
    def test_fermion_blocked(self, result):
        f = [a for a in result.absent_sectors if a.sector_id == "ABS2"][0]
        assert f.absence_class == "blocked_by_structure"
        assert "3-layer" in f.description
    def test_chemistry_blocked(self, result):
        c = [a for a in result.absent_sectors if a.sector_id == "ABS3"][0]
        assert c.absence_class == "blocked_by_structure"
    def test_gauge_absent(self, result):
        g = [a for a in result.absent_sectors if a.sector_id == "ABS1"][0]
        assert g.absence_class == "absent_unbuilt"


# ── Track G: Economy ──

class TestEconomy:
    def test_assessment_nonempty(self, result):
        assert len(result.economy_assessment) > 0
    def test_economy_verdict(self, result):
        assert result.economy_status == ZB_ECONOMY
        assert result.economy_status in ECONOMY_OPTIONS


# ── Track H: Firewall ──

class TestNonclaims:
    def test_count(self): assert len(ZB_NONCLAIMS) == N_ZB_NONCLAIMS
    def test_prefix(self):
        for nc in ZB_NONCLAIMS:
            assert nc.startswith("NOT_claiming_")
    def test_firewall(self, result):
        assert result.nonclaim_firewall.n_nonclaims == N_ZB_NONCLAIMS
        assert result.nonclaim_firewall.all_registered is True


# ── Hard-Gated Verdicts ──

class TestHardGatedVerdicts:
    def test_postulate(self, result):
        assert result.postulate_accounting_status == ZB_POSTULATE
        assert result.postulate_accounting_status in POSTULATE_OPTIONS
    def test_parameter(self, result):
        assert result.parameter_accounting_status == ZB_PARAMETER
        assert result.parameter_accounting_status in PARAMETER_OPTIONS
    def test_field_dof(self, result):
        assert result.field_dof_accounting_status == ZB_FIELD_DOF
        assert result.field_dof_accounting_status in FIELD_DOF_OPTIONS
    def test_economy(self, result):
        assert result.economy_status == ZB_ECONOMY
        assert result.economy_status in ECONOMY_OPTIONS
    def test_auth(self, result):
        assert result.authorization == ZB_AUTH
        assert result.authorization in AUTH_OPTIONS
    def test_overall(self, result):
        assert result.overall_appendix_p == ZB_OVERALL
        assert result.overall_appendix_p in OVERALL_OPTIONS
    def test_distinct(self, result):
        v = {result.postulate_accounting_status, result.parameter_accounting_status,
             result.field_dof_accounting_status, result.economy_status,
             result.authorization}
        assert len(v) == 5


# ── Diagnostics ──

class TestDiagnostics:
    def test_total(self, result):
        assert result.diagnostics["n_postulates_total"] == 7
    def test_true_new(self, result):
        assert result.diagnostics["n_true_new_postulates"] == 5
    def test_consequence(self, result):
        assert result.diagnostics["n_consequence_postulates"] == 2
    def test_params(self, result):
        assert result.diagnostics["n_params_free"] == 3
    def test_derived(self, result):
        assert result.diagnostics["n_params_derived"] == 4
    def test_fields(self, result):
        assert result.diagnostics["n_new_fields"] == 0
    def test_dof(self, result):
        assert result.diagnostics["n_new_dof"] == 0
    def test_formal(self, result):
        assert result.diagnostics["n_formal_objects"] == 6
    def test_absent(self, result):
        assert result.diagnostics["n_absent_sectors"] == 10
    def test_blocked(self, result):
        assert result.diagnostics["n_blocked"] == 2
    def test_absent_unbuilt(self, result):
        assert result.diagnostics["n_absent_unbuilt"] == 8
    def test_qm(self, result):
        assert result.diagnostics["full_qm"] is False
    def test_closure(self, result):
        assert result.diagnostics["unified_closure"] is False
    def test_toe(self, result):
        assert result.diagnostics["toe_status"] is False
    def test_eq_foundational(self, result):
        assert result.diagnostics["n_equations_foundational"] == 4
    def test_eq_operational(self, result):
        assert result.diagnostics["n_equations_operational"] == 3
    def test_eq_interface(self, result):
        assert result.diagnostics["n_equations_interface"] == 7


# ── Claims ──

class TestClaims:
    def test_allowed(self, result): assert len(result.allowed_claims) == N_ALLOWED
    def test_forbidden(self, result): assert len(result.forbidden_claims) == N_FORBIDDEN


# ── Master ──

class TestMaster:
    def test_valid(self, result): assert result.valid is True
    def test_key(self, result): assert len(result.key_findings) >= 6
    def test_nonclaims_list(self, result):
        assert len(result.exact_nonclaims) == N_ZB_NONCLAIMS
    def test_self_test(self): assert _self_test() is True
    def test_idempotent(self):
        r1 = run_zb_cumulative_postulate_parameter_accounting()
        r2 = run_zb_cumulative_postulate_parameter_accounting()
        assert r1.valid == r2.valid
        assert r1.n_postulates_total == r2.n_postulates_total
        assert r1.postulate_accounting_status == r2.postulate_accounting_status
