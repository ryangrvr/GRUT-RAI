#!/usr/bin/env python3
"""Phase D11 -- Exact Two-Field Closure Benchmark.

60 checks across 11 sections verifying the exact coupled macro/defect
closure analysis, D9 comparison, metric injection, scans, and classification.
"""

import math
import sys
import numpy as np

from grut.exact_two_field_closure import (
    # Constants
    ALPHA_VAC, R_S, M_EXT, R_EQ, R_EXT, TAU_CANONICAL, A_CRIT,
    LAMBDA_DEFAULT, ETA_TARGET, XI_DEFAULT, RHO_EQ_COEFF, MASS_COEFF,
    MAX_ITERATIONS_DEFAULT, CONVERGENCE_TOL_DEFAULT,
    RELAXATION_FACTOR_DEFAULT, G_PORTAL_DEFAULT,
    G_PORTAL_SCAN_VALUES, LAMBDA_SCAN_VALUES,
    CLASSIFICATION_OPTIONS, D9_PROXY_ASSESSMENT_OPTIONS,
    EXACT_TWO_FIELD_ASSUMPTIONS, EXACT_TWO_FIELD_NONCLAIMS,
    # Dataclasses
    ExactTwoFieldParams, CoupledFieldEquations,
    ExactTwoFieldSolution, D9ComparisonResult, ExactMetricResult,
    ExactLambdaScanEntry, ExactLambdaScanResult,
    ExactPortalScanEntry, ExactPortalScanResult,
    D9RetrospectiveAssessment, ExactTwoFieldClassification,
    ExactTwoFieldResult,
    # Functions
    document_field_equations, solve_exact_two_field,
    compare_to_d9, inject_exact_metric,
    scan_lambda_exact, scan_portal_exact,
    assess_d9_retrospective, classify_exact_two_field,
    compute_exact_two_field, exact_two_field_result_to_dict,
)


def run_benchmark():
    passed = 0
    failed = 0
    total = 60

    def check(name, condition, detail=""):
        nonlocal passed, failed
        if condition:
            passed += 1
            print(f"  PASS  {name}")
        else:
            failed += 1
            print(f"  FAIL  {name} {detail}")

    # Pre-compute the full result
    print("Computing D11 exact two-field closure ...")
    params = ExactTwoFieldParams()
    result = compute_exact_two_field(params)
    print("Done.\n")

    # =================================================================
    # Section 1: Constants & Parameters (5 checks)
    # =================================================================
    print("Section 1: Constants & Parameters")
    check("1.1 R_EQ value", abs(R_EQ - 1.0 / 3.0) < 1e-12)
    check("1.2 TAU_CANONICAL", abs(TAU_CANONICAL - math.sqrt(1.5)) < 1e-12)
    check("1.3 RHO_EQ_COEFF", abs(RHO_EQ_COEFF - M_EXT ** 2 / (2 * TAU_CANONICAL ** 2)) < 1e-12)
    check("1.4 LAMBDA_DEFAULT", abs(LAMBDA_DEFAULT - 8 * math.pi) < 1e-10)
    check("1.5 ETA_TARGET", abs(ETA_TARGET - 1.0 / math.sqrt(8 * math.pi)) < 1e-12)
    print()

    # =================================================================
    # Section 2: Field Equations Documentation (5 checks)
    # =================================================================
    print("Section 2: Field Equations Documentation")
    fe = result.field_equations
    check("2.1 macro equation non-empty", len(fe.macro_equation) > 20)
    check("2.2 defect equation non-empty", len(fe.defect_equation) > 20)
    check("2.3 portal sign documented", "positive" in fe.portal_sign_verification.lower())
    check("2.4 source status is FIXED", "FIXED" in fe.source_status)
    check("2.5 energy density convention", "Phi(r)^2" in fe.energy_density_convention or
          "Phi^2" in fe.energy_density_convention)
    print()

    # =================================================================
    # Section 3: Exact BVP Solution (6 checks)
    # =================================================================
    print("Section 3: Exact BVP Solution")
    es = result.exact_solution
    check("3.1 solution converged", es.converged)
    check("3.2 method is string", isinstance(es.method, str) and len(es.method) > 0)
    check("3.3 r_grid spans [R_EQ, R_EXT]",
          abs(es.r_grid[0] - R_EQ) < 0.01 and abs(es.r_grid[-1] - R_EXT) < 0.01)
    check("3.4 phi > 0 everywhere", np.all(es.phi > 0))
    check("3.5 f_defect in [0, 1]",
          np.min(es.f_defect) >= -0.01 and np.max(es.f_defect) <= 1.01)
    check("3.6 epsilon_macro > 0 everywhere", np.all(es.epsilon_macro > 0))
    print()

    # =================================================================
    # Section 4: D8 Laplacian Enhancement (6 checks)
    # =================================================================
    print("Section 4: D8 Laplacian Enhancement")
    idx_req = np.argmin(np.abs(es.r_grid - R_EQ))
    phi_uncoupled_Req = M_EXT / R_EQ ** 2
    phi_exact_Req = es.phi[idx_req]
    phi_ratio = phi_exact_Req / phi_uncoupled_Req
    check("4.1 Phi(R_EQ) > M/R_EQ^2", phi_exact_Req > phi_uncoupled_Req,
          f"exact={phi_exact_Req:.2f}, uncoupled={phi_uncoupled_Req:.2f}")
    check("4.2 Phi enhancement ratio > 10", phi_ratio > 10,
          f"ratio={phi_ratio:.1f}")
    check("4.3 Phi enhancement ratio < 100", phi_ratio < 100,
          f"ratio={phi_ratio:.1f}")
    # eps_macro enhancement
    eps_d9_Req = RHO_EQ_COEFF / R_EQ ** 4
    eps_d11_Req = es.epsilon_macro[idx_req]
    check("4.4 eps_macro D11 >> eps_macro D9", eps_d11_Req / eps_d9_Req > 100,
          f"ratio={eps_d11_Req / eps_d9_Req:.1f}")
    # sigma_macro >> sigma_defect
    check("4.5 sigma_macro >> sigma_defect at R_EQ",
          es.sigma_macro_at_Req > 100 * es.sigma_defect_at_Req,
          f"macro={es.sigma_macro_at_Req:.2f}, defect={es.sigma_defect_at_Req:.4f}")
    # Phi at R_EXT closer to M/R_EXT^2
    idx_rext = np.argmin(np.abs(es.r_grid - R_EXT))
    phi_rext = es.phi[idx_rext]
    phi_uncoupled_rext = M_EXT / R_EXT ** 2
    check("4.6 Phi still enhanced at R_EXT", phi_rext > phi_uncoupled_rext,
          f"exact={phi_rext:.4f}, uncoupled={phi_uncoupled_rext:.4f}")
    print()

    # =================================================================
    # Section 5: D9 Comparison (6 checks)
    # =================================================================
    print("Section 5: D9 Comparison")
    dc = result.d9_comparison
    check("5.1 metric_positive both", dc.metric_positive_d11 and dc.metric_positive_d9)
    check("5.2 f_min_d11 > 0", dc.f_min_d11 > 0)
    check("5.3 f_min_d9 > 0", dc.f_min_d9 > 0)
    check("5.4 phi deviation large (Laplacian effect)",
          dc.phi_vs_proxy_max_deviation > 50,
          f"dev={dc.phi_vs_proxy_max_deviation:.2f}")
    check("5.5 d9_proxy_assessment valid",
          dc.d9_proxy_assessment in D9_PROXY_ASSESSMENT_OPTIONS)
    check("5.6 proxy_quality_score in [0,1]",
          0.0 <= dc.proxy_quality_score <= 1.0)
    print()

    # =================================================================
    # Section 6: Metric Injection (5 checks)
    # =================================================================
    print("Section 6: Metric Injection")
    met = result.metric_result
    check("6.1 metric positive", met.metric_positive)
    check("6.2 f_min > 0", met.f_min > 0)
    check("6.3 f_min at R_EXT boundary", abs(met.f_min_radius - R_EXT) < 0.1,
          f"r_min_radius={met.f_min_radius:.4f}")
    check("6.4 f_at_Req >> 1 (Laplacian enhancement)",
          met.f_at_Req > 100,
          f"f_at_Req={met.f_at_Req:.2f}")
    check("6.5 budget dict nonempty", len(met.budget) > 0)
    print()

    # =================================================================
    # Section 7: Lambda Scan (6 checks)
    # =================================================================
    print("Section 7: Lambda Scan")
    ls = result.lambda_scan
    check("7.1 scanned 6 lambda values", ls.n_scanned == 6)
    check("7.2 >= 5 converged", ls.n_converged >= 5,
          f"converged={ls.n_converged}")
    check("7.3 all positive D11", ls.n_positive_d11 == 6)
    check("7.4 all positive D9", ls.n_positive_d9 == 6)
    check("7.5 viability_comparison = same", ls.viability_comparison == "same")
    check("7.6 viable_d11 == viable_d9",
          set(ls.viable_d11) == set(ls.viable_d9))
    print()

    # =================================================================
    # Section 8: Portal Scan (6 checks)
    # =================================================================
    print("Section 8: Portal Scan")
    ps = result.portal_scan
    check("8.1 scanned 5 portal values", ps.n_scanned == 5)
    check("8.2 g_p=0 not viable",
          not ps.entries[0].metric_positive and ps.entries[0].g_portal == 0.0)
    check("8.3 g_p=0.1 viable",
          ps.entries[1].metric_positive and abs(ps.entries[1].g_portal - 0.1) < 1e-6)
    check("8.4 g_p=1.0 viable",
          ps.entries[3].metric_positive and abs(ps.entries[3].g_portal - 1.0) < 1e-6)
    check("8.5 n_positive >= 4", ps.n_positive >= 4)
    check("8.6 sensitivity_assessment valid",
          ps.sensitivity_assessment in [
              "mild_sensitivity", "moderate_sensitivity",
              "significant_sensitivity", "destructive"])
    print()

    # =================================================================
    # Section 9: D9 Retrospective (5 checks)
    # =================================================================
    print("Section 9: D9 Retrospective Assessment")
    retro = result.d9_retrospective
    check("9.1 assessment valid", retro.assessment in D9_PROXY_ASSESSMENT_OPTIONS)
    check("9.2 viability_agreement", retro.viability_agreement)
    check("9.3 max_metric_discrepancy < 0.2",
          retro.max_metric_discrepancy < 0.2,
          f"disc={retro.max_metric_discrepancy:.4f}")
    check("9.4 parameter_window_agreement is identical",
          retro.parameter_window_agreement == "identical")
    check("9.5 summary non-empty", len(retro.summary) > 10)
    print()

    # =================================================================
    # Section 10: Classification (6 checks)
    # =================================================================
    print("Section 10: Classification")
    cls = result.classification
    check("10.1 classification valid", cls.classification in CLASSIFICATION_OPTIONS)
    check("10.2 classification is strongly_supports or achieved",
          cls.classification in [
              "exact_closure_achieved",
              "exact_closure_strongly_supports_d9"])
    check("10.3 d9_viability_confirmed", cls.d9_viability_confirmed)
    check("10.4 exact_viability_across_lambda", cls.exact_viability_across_lambda)
    check("10.5 phase_lock_update has D11", "exact_two_field_D11" in cls.phase_lock_update)
    check("10.6 d9_assessment valid", cls.d9_assessment in D9_PROXY_ASSESSMENT_OPTIONS)
    print()

    # =================================================================
    # Section 11: Nonclaims, Serialization & Consistency (5 checks)
    # =================================================================
    print("Section 11: Nonclaims, Serialization & Consistency")
    check("11.1 assumptions count", len(result.assumptions) == 10)
    check("11.2 nonclaims count", len(result.nonclaims) == 10)
    d = exact_two_field_result_to_dict(result)
    check("11.3 serialization valid", d["valid"] is True)
    check("11.4 serialization has classification",
          "classification" in d and d["classification"]["classification"] in CLASSIFICATION_OPTIONS)
    print()

    # =================================================================
    # Summary
    # =================================================================
    print("=" * 60)
    print(f"D11 Benchmark: {passed}/{total} passed, {failed}/{total} failed")
    if passed == total:
        print("ALL CHECKS PASSED.")
    else:
        print(f"WARNING: {failed} check(s) failed.")
    print("=" * 60)

    return failed == 0


if __name__ == "__main__":
    success = run_benchmark()
    sys.exit(0 if success else 1)
