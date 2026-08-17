"""mutation_registry: THE CALC-LAYER FLOOR -- the standing rule, in machine-readable form.

WHY THIS EXISTS (the honest reason, recorded so it is not softened later): TWO green-selftest
failures in two days.
  * 2026-08-03, calc/isw_tt_auto.py -- a spherical-Bessel Miller-recurrence start that ignored the
    argument. The selftest tested ONE point (x = 7.3) which happened to sit below the failure
    threshold, so PASS coexisted with constants that were pure numerical noise (the "edge" moved
    0.035 -> 0.27 on a single resolution doubling). Every number of that freeze was retracted.
  * 2026-08-03, calc/anomaly_c0_map.py (first build) -- the two most load-bearing facts (int C^2
    pure P2, int E_4 identically zero) lived in PRINT STATEMENTS behind a fabricated provenance
    parenthetical ("built from the full linearized Riemann") describing code that did not exist. A
    mutation test showed the selftest still passed with the ANSWER replaced by x = alpha^2 -- the
    single outcome that calc's own pre-registered directional guard declares must be an error.

Vigilance already failed twice. So this is STRUCTURAL, not a habit:

    *** STANDING RULE: every calc producing a load-bearing number ships a MUTATION BATTERY --
        the pre-registered WRONG answers (including the seductive one the directional guard
        names) -- and the battery must make the calc's own selftest FAIL. No number banks
        without one. ***

This file is the calc-layer equivalent of provenance/bankgate.py: bankgate intercepts register
edits; this intercepts NUMBERS. Enforced by provenance/test_mutation_battery.py.

THE RATCHET (the anti-softening device): OWED lists calcs that are cited by the register but do not
yet carry a battery. The test asserts OWED only ever SHRINKS -- a calc may be removed from OWED
(by giving it a battery), never added. A new load-bearing calc therefore cannot be introduced
without one.
"""

# --------------------------------------------------------------------------- the batteries
# Each entry: calc file -> list of mutants. A mutant is (name, find, replace, why).
# `why` states WHAT WRONG ANSWER the mutant installs -- so the battery reads as a pre-registration
# of the failure modes, not as a code-coverage exercise.
# `slow` calcs are declared here and executed only under GRUT_FULL_MUTATION=1 (the suite stays fast;
# the DECLARATION is always enforced).
# `dir` names the directory the file lives in (default 'calc'); the rule is about LOAD-BEARING
# NUMBERS, not about which folder they sit in -- a tool in provenance/ that scores ledger
# arithmetic is exactly as load-bearing as a calc.

BATTERIES = {
    # ------------------------------------------------- noise transversality (the derive-or-book exhibit)
    "noise_transversality_check.py": {
        "slow": True,
        "mutants": [
            ("conjugation_dropped_in_rho",
             "(K - K.H) / (2 * I)",
             "(K - K.T) / (2 * I)",
             "breaks the Hermiticity relation D_A = K_R^dag that the spectral form rests on; the "
             "Ward-sourced zero g'rho g = 0 no longer follows and PART 1/PART 3 must fail. If the "
             "calc still passes, its identity check was verifying its own construction."),
            ("gauge_orbit_lowered",
             "kup[r] * (1 if s == a else 0)",
             "klow[r] * (1 if s == a else 0)",
             "malformed gauge orbit (lower-index k): the theorem gets tested against the wrong "
             "orbit and the family kernel no longer annihilates it -- the wrong-object error."),
            ("witness_sign_flipped",
             "if val < 0:",
             "if val > 0:",
             "installs THE FLATTERING OUTCOME: the positivity-violation witness is never found, so "
             "the counterexample reads as positivity-compatible and 'KMS alone suffices' -- the "
             "exact wrong answer that would have made the derivation look cheaper than it is."),
            ("engine_bound_inverted",
             "if not (lhs <= stat):",
             "if not (lhs >= stat):",
             "corrupts the PSD engine's Cauchy-Schwarz bound -- the propagation step's motor; "
             "PART 2 (or the battery's own M3 catch) must fail."),
            ("psd_conj_slip_reinstalled",
             "A[i, j] - f * A[pivot_i, j]",
             "A[i, j] - f * sp.conjugate(A[pivot_i, j])",
             "re-installs the first draft's Schur-complement conj-slip -- correct on real "
             "symmetric input, wrong on complex Hermitian (reports [[1,2i],[-2i,2]], det -2, "
             "as positive). The PART-0 selftest must catch it; if the calc still passes, the "
             "selftest has gone dead. Found by the 2026-08-17 re-screen."),
            ("off_family_spacelike_instance",
             "(Rational(0) if spacelike else Rational(2))",
             "(Rational(2) if spacelike else Rational(2))",
             "re-installs the first draft's own caught defect: a spacelike family instance with "
             "s2 > 0, which the theorem's positivity premise bars (P^(2) is plain-indefinite at "
             "spacelike k^2). The composition assert added on the 2026-08-17 screen finding must "
             "refuse it; if the calc still passes, that assert has gone dead."),
        ],
    },
    # ---------------------------------------------------------------- the merge criterion's tool
    "merge_test.py": {
        "slow": False, "dir": "provenance",
        # NOTE ON COVERAGE, recorded rather than implied: F3(b) (the side-participation guard) ships
        # with NO mutant. Every attack it catches is independently caught by F3(a), and padding with
        # a RETAINED input provably cannot inflate depth (+1 to both tallies). A battery entry that
        # nothing can isolate is decoration, and claiming coverage one does not have is the failure
        # this program keeps finding in its own guards.
        "mutants": [
            ("dimension_becomes_cardinality_again",
             '        v[e["kind"]] += e["dim"]',
             '        v[e["kind"]] += 1',
             "RE-INSTALLS the ORIGINAL bundle theorem: counts labels instead of real-parameter "
             "dimension, so relabelling n atoms as one object reduces the count on demand. This is "
             "the defect the registry exists to close, and the reason a proposal may never supply "
             "a dimension."),
            ("axes_summed_again",
             '    neg = any(dv[a] < 0 for a in ("continuous", "discrete"))\n    pos = any(dv[a] > 0 for a in ("continuous", "discrete"))',
             '    neg = (dv["continuous"] + dv["discrete"] + dv["posit"]) < 0\n    pos = False',
             "RE-INSTALLS D4 one level down: sums three incommensurable axes into one scalar, so a "
             "saved discrete stance can pay for a posit and a gauge quotient can masquerade as a "
             "saved real parameter."),
            ("eliminations_unbound_from_the_relation",
             "    unbound = elim - rel_inputs",
             "    unbound = set()",
             "lets a relation 'eliminate' inputs it never references -- v2 checked only "
             "subset-of-union, so an empty relation string could still remove four inputs."),
            ("worst_reading_replaced_by_the_favourable_one",
             '    worst = max(scored.values(), key=lambda kv: _ORDER[kv[0]])[0]',
             '    worst = min(scored.values(), key=lambda kv: _ORDER[kv[0]])[0]',
             "reports the MOST FAVOURABLE reading of the enumeration span instead of the worst -- "
             "the direction the criterion's own guard forbids, and the one v2's flag was provably "
             "mute on (0 of 244,888 reductions flagged)."),
            ("dual_reading_disabled",
             "    optional = union - rel_inputs\n",
             "    optional = set()\n",
             "kills the second enumeration direction, restoring v2's structural blindness: the "
             "span could then never flip a REDUCTION."),
            ("unregistered_ids_default_silently",
             '            bad.append(f"input {i!r} is not in the frozen ATOMIC registry -- amend the registry "',
             '            pass  # MUTANT\n            _u = (f"input {i!r} unregistered "',
             "lets an id outside the frozen registry through, which is how a dimension gets "
             "settled inside the proposal that needs a particular answer."),
        ],
    },

    # ---------------------------------------------------------------- the answer calc (R1)
    "anomaly_c0_map.py": {
        "slow": False,
        "mutants": [
            ("x_becomes_the_seductive_point",
             "    return (1.0 / (3.0 * alpha)) * k2 / den",
             "    return alpha ** 2",
             "installs x = alpha^2 -- THE point the file's own directional guard names as "
             "'an arithmetic error or a laundered step'. This is the mutant that SURVIVED the "
             "first build's selftest."),
            ("anomaly_coefficient_sign_and_scale",
             "cR_anom = -(N_pref * LAM ** 2) / 9.0",
             "cR_anom = +(N_pref * LAM ** 2) / 9.0 * 1e9",
             "flips the structurally-negative c_R^anom and inflates it 1e9 -- would silently move "
             "the tachyonic-branch statement and the magnitude table."),
            ("weyl_row_corrupted",
             "    return _sq_full(Riem) - F(2) * _sq_two(lin_ricci(Riem)) + F(1, 3) * r * r",
             "    return _sq_full(Riem) - F(2) * _sq_two(lin_ricci(Riem)) + F(1, 2) * r * r",
             "breaks int C^2 so it acquires a spin-0 carrier -- would destroy the a/c sector-split "
             "that is now banked at eft_operator_basis and rung9b_bridge."),
            ("gauss_bonnet_row_corrupted",
             "- F(4) * _sq_two(lin_ricci(Riem))",
             "- F(3) * _sq_two(lin_ricci(Riem))",
             "breaks int E_4's identical vanishing -- the collapse theorem's first premise."),
            ("form_factor_loses_k_squared_scaling",
             "    k2 = k_over_MP ** 2",
             "    k2 = k_over_MP",
             "makes the induced shift k^1 instead of k^2 -- would fake a softer, more reachable "
             "form factor."),
        ],
    },

    # ---------------------------------------------------------------- the interior family
    "mu_slip_interior.py": {
        "slow": False,
        "mutants": [
            ("sigma_identity_broken",
             "def Sigma_x(x):\n    return mu_x(x) * (1.0 + eta_x(x)) / 2.0",
             "def Sigma_x(x):\n    return mu_x(x) * (1.0 + eta_x(x)) / 2.0 * 1.05",
             "breaks the banked identity Sigma-1 = (mu-1)/2, which the register carries as EXACT "
             "in the inherited bookkeeping."),
            ("endpoint_disagrees_with_mu_linear",
             "def mu_x(x):\n    return 1.0 + x * ALPHA",
             "def mu_x(x):\n    return 1.0 + x * ALPHA * 1.01",
             "detaches the family from its own endpoints -- the x=1 member would no longer "
             "reproduce mu_linear's banked mu = 4/3."),
            ("retired_32_restored_at_the_DEFINITION",
             "N_CROSS_ENDPOINT = 2.0",
             "N_CROSS_ENDPOINT = 32.0",
             "restores the RETIRED ~32sigma anchor AT ITS DEFINITION -- the load-bearing line. "
             "(The firewall found the original mutant anchored on the ALIAS one line below, a "
             "DECOY: the alias is defined AS the constant, so both of the calc's checks on it were "
             "tautological and a wrong calc passed its own selftest.)"),
            ("retired_32_restored_via_the_legacy_alias",
             "N_SIGMA_ENDPOINT = N_CROSS_ENDPOINT",
             "N_SIGMA_ENDPOINT = 32.0",
             "restores the RETIRED ~32sigma anchor as the family's significance scale -- the "
             "number the whole isw_exclusion wave exists to have retired."),
            ("window_edge_detached_from_its_formula",
             "EDGE = (0.009 + 2 * 0.045) * 2.0 / ALPHA",
             "EDGE = 0.0625",
             "silently restores the RETIRED 1/16 edge (the number the computed record replaced) "
             "without its formula -- the exact regression the anchor correction exists to prevent."),
        ],
    },

    # ---------------------------------------------------------------- the ISW anchor
    "isw_exclusion.py": {
        "slow": False,
        "mutants": [
            ("weyl_sigma_factor_dropped_again",
             "    return msi.Sigma_x(x) * num / den",
             "    return num / den",
             "re-installs the firewall-caught B1 omission (the Weyl-source Sigma factor). The "
             "banked cross number ~2.0sigma would silently revert to 2.3."),
            ("growth_equation_mu_coupling_dropped",
             "return Dp, -(2.0 - 1.5 * om) * Dp + 1.5 * om * mu * D",
             "return Dp, -(2.0 - 1.5 * om) * Dp + 1.5 * om * D",
             "removes mu from the growth ODE -- the model would become LCDM and every exclusion "
             "number would collapse to zero."),
        ],
    },

    # ---------------------------------------------------------------- the operator basis
    "operator_basis.py": {
        "slow": False,
        "mutants": [
            ("projector_idempotence_broken",
             "def TL(khat):",
             "def TL(khat):\n    khat = [c * 1.0000001 for c in khat]  # MUTANT",
             "de-normalizes khat so the transverse/longitudinal split stops being a projector -- "
             "the enumeration's whole basis."),
        ],
    },

    # ---------------------------------------------------------------- the channel-diagonal passivity lemma
    "x_no_pin.py": {
        "slow": False,
        # The four wrong answers were PRE-REGISTERED in PREREG_X_NO_PIN_2026-08-09.txt (M1-M4)
        # BEFORE the calc existed -- the battery here is the sealed list made executable.
        "mutants": [
            ("psd_becomes_trace_positivity",
             "    return mn >= -tol * scale, mn",
             "    return sum(eigs) >= -tol * scale, mn",
             "degrades the matrix PSD condition to aggregate (trace) positivity -- the exact "
             "cross-channel-rescue laundering (a large compliant shear channel paying for a "
             "violating bulk channel) that the lemma exists to refute. Prereg mutant M1."),
            ("ceiling_verdict_flipped",
             '    "ceiling_from_passivity": False,  # Q2: no upper bound on any amplitude or ratio',
             '    "ceiling_from_passivity": True,  # Q2: no upper bound on any amplitude or ratio',
             "installs the pre-registered FLATTERING outcome -- a derived upper bound from "
             "positivity alone, which the convex-cone computation shows does not exist. "
             "Prereg mutant M2."),
            ("witness_orientation_flipped",
             "    return w * tau / (1.0 + (w * tau) ** 2)",
             "    return -w * tau / (1.0 + (w * tau) ** 2)",
             "negates the passive Debye witness, silently reversing the orientation of the "
             "per-channel sign floor -- the wrong-sign lemma would still print a green grid. "
             "Prereg mutant M3."),
            ("kms_lock_loses_the_sign",
             "    return (1.0 / math.tanh(0.5 * beta * w)) * im_c",
             "    return abs((1.0 / math.tanh(0.5 * beta * w)) * im_c)",
             "detaches the noise coefficient from the SIGNED dissipation, so noise positivity "
             "would mask a dissipation-sign violation (the 'noise rescues dissipation' "
             "laundering). Prereg mutant M4."),
        ],
    },

    # ---------------------------------------------------------------- the static-transfer question
    "kk_static_transfer.py": {
        "slow": False,
        # The four wrong answers were PRE-REGISTERED in PREREG_KK_STATIC_2026-08-09.txt (M1-M4)
        # BEFORE the calc existed -- the battery here is the sealed list made executable.
        "mutants": [
            ("counterexample_neutered",
             "C_INF = -1.0",
             "C_INF = -0.3",
             "shrinks the negative contact term below the relaxor's static weight, so the "
             "exhibited kernel is no longer negative at zero frequency -- the refutation of "
             "unconditional transfer silently evaporates. Prereg mutant M1."),
            ("flattering_verdict_installed",
             '    "unconditional_transfer": False,           # outcome (a) did NOT bank -- the flattering branch',
             '    "unconditional_transfer": True,           # outcome (a) did NOT bank -- the flattering branch',
             "installs the pre-registered FLATTERING outcome -- an unconditional derived floor "
             "for mu, which the counterexample refutes. Prereg mutant M2."),
            ("dispersion_machinery_broken",
             "    return (2.0 / math.pi) * total",
             "    return (1.0 / math.pi) * total",
             "corrupts the Kramers-Kronig prefactor, so the reconstruction-against-closed-form "
             "identity fails and every downstream statement is numerology. Prereg mutant M3."),
            ("instantaneous_part_smuggled_to_zero",
             "    c_inf, _poles = kernel\n    return c_inf",
             "    c_inf, _poles = kernel\n    return 0.0",
             "forces the chi_inf read to report zero always, erasing the counterexample class "
             "and faking the unconditional transfer. Prereg mutant M4."),
        ],
    },

    # ---------------------------------------------------------------- the vacuum-cluster scheme audit
    "vacuum_scheme_compare.py": {
        "slow": False,
        "mutants": [
            ("flattering_dismissal_restored",
             "def w_covariant():",
             "def w_covariant():\n    return 1.0/3.0  # MUTANT",
             "makes the COVARIANT scheme also return w = +1/3 -- i.e. re-installs the STRUCK "
             "inference that the vacuum energy 'is really a radiation fluid', which would let the "
             "file dismiss the whole problem. This is the flattering horn and the mutant that "
             "matters most here."),
            ("convention_span_collapsed",
             "M_PL_RED = 2.435323e18",
             "M_PL_RED = 1.220890e19",
             "collapses reduced onto non-reduced M_Pl, erasing the 2.80-order convention span -- "
             "the finding's core force would silently vanish."),
            ("scheme_independent_anchor_corrupted",
             "    return M_H ** 2 * V_EW ** 2 / 8.0",
             "    return M_H ** 2 * V_EW ** 2 / 8.0 * 1e-20",
             "shrinks the electroweak vacuum depth below the seriousness threshold -- would convert "
             "the honest replacement statement into 'there is no problem', the exact overreach the "
             "verdict block refuses."),
            ("sign_flip_erased",
             "    return (4.0 * math.log(1.0 / mu_over_L) - 1.0) / (128.0 * math.pi ** 2)",
             "    return abs((4.0 * math.log(1.0 / mu_over_L) - 1.0)) / (128.0 * math.pi ** 2)",
             "erases the mu-driven SIGN FLIP of the covariant coefficient -- the second half of the "
             "convention finding."),
        ],
    },

    # ---------------------------------------------------------------- the frozen TT-auto gate
    "isw_tt_auto.py": {
        "slow": True,   # ~2.5 min/run; declaration always enforced, execution gated
        "mutants": [
            ("bessel_start_ignores_argument_again",
             "    b = max(lmax, int(xval))                       # A1: Miller start must exceed the ARGUMENT\n    top = b + int(1.5 * math.sqrt(b + 1)) + 12",
             "    top = lmax + int(1.5 * math.sqrt(lmax + 1)) + 12",
             "RE-INSTALLS THE EXACT HISTORICAL BUG (the Miller start that ignored the argument). "
             "The battery's reason for existing: this mutant must never pass again."),
            ("quasi_static_filter_disabled",
             "        return 1.0 if k > kappa * a * H(a) else 0.0",
             "        return 1.0",
             "disables the filter that implements the banked separate-universe constraint, "
             "silently converting every quotable member into the non-quotable diagnostic."),
        ],
    },

    # ------------------------------------------------- the Sigma_0 anomaly screen
    # PRIMARY BATTERY IS IN-FILE (8 mutants via its own _mutate mechanism, run on every direct
    # execution -- the file is its own harness). The two registry mutants below are the EXTERNAL
    # anchors: they re-install the two errors that were ACTUALLY COMMITTED on this screen (the
    # one-sided F-MAP direction; the flipped tension sign), so the register-level runner can
    # verify the selftest bites without duplicating the in-file battery. Registered 2026-08-09
    # when consumed_by made this calc register-cited and the coverage ratchet (correctly) fired.
    "sigma0_anomaly_screen.py": {
        "slow": False,
        "mutants": [
            ("fmap_given_a_direction_again",
             'FMAP_SIGN = "undetermined"',
             'FMAP_SIGN = "up"',
             "re-installs the one-sided F-MAP reading (the error committed 2026-08-05: shape "
             "reasoning applied to the cap side only); the selftest's sign guard must fail."),
            ("tension_sign_flipped",
             "    return (value - ceiling) / err",
             "    return (ceiling - value) / err",
             "flips the tension sign so the measurement reads BELOW the gates -- the flattering "
             "direction; every tension check in the selftest must fail."),
        ],
    },
}

# --------------------------------------------------------------------------- the ratchet
# Calcs CITED BY THE REGISTER that do not yet carry a battery. This list may only SHRINK.
# (Each entry names why it is not yet covered -- honesty about coverage is the point.)
OWED = {
    "wz_sign.py": "no machine-detectable selftest verdict; needs one before a battery can bite",
    "wz_dark_energy.py": "no machine-detectable selftest verdict",
    "u5u6_deformability.py": "TOY/SCALING grade (banks no result-tier number); battery owed anyway",
    "gw_dissipation_bounds.py": "no machine-detectable selftest verdict",
    "energy_basis_decoherence.py": "no machine-detectable selftest verdict",
    "arrow_origin.py": "no machine-detectable selftest verdict",
    "two_scale_desitter.py": "no machine-detectable selftest verdict",
    "rung3_spectral_structure.py": "has a selftest; battery not yet written",
    "q1_energy_basis_magnitude.py": "no machine-detectable selftest verdict",
    "delta4_stability.py": "no machine-detectable selftest verdict",
    "conformalon_joint.py": "no machine-detectable selftest verdict",
    "zeta_interior.py": "first-pass record, numbers RETIRED and marked historical; battery owed",
    "mu_linear.py": "bookkeeping-only (its endpoints are drift-pinned by mu_slip_interior's "
                    "battery and by the harness cross-subsystem regression); battery owed",
    # added 2026-08-04: the coverage regex was case-sensitive ([a-z0-9_]) and these two escaped it
    "L0_redundancy.py": "escaped the coverage net until 2026-08-04 (capital L); battery owed",
    "finite_T_exponent.py": "escaped the coverage net until 2026-08-04 (capital T); battery owed",
}

# THE RATCHET'S FROZEN HIGH-WATER MARK -- a HARDCODED LITERAL, frozen 2026-08-04; entries may only
# be REMOVED (by giving that calc a battery), never added.
#
# WHY A LITERAL (the firewall lesson, recorded so it is not "simplified" back):
# the first version computed OWED_CEILING = frozenset(OWED) from OWED itself, which made the
# ratchet assertion TRUE BY CONSTRUCTION -- a guard whose GREEN meant nothing. That is precisely
# the failure class this whole file exists to prevent, reproduced inside the guard. The honesty
# device only works if adding a calc requires editing TWO places, so the diff is legible.
OWED_CEILING = frozenset({
    "wz_sign.py", "wz_dark_energy.py", "u5u6_deformability.py", "gw_dissipation_bounds.py",
    "energy_basis_decoherence.py", "arrow_origin.py", "two_scale_desitter.py",
    "rung3_spectral_structure.py", "q1_energy_basis_magnitude.py", "delta4_stability.py",
    "conformalon_joint.py", "zeta_interior.py", "mu_linear.py",
    "L0_redundancy.py", "finite_T_exponent.py",
})


# ============================ THE COMPARISON RULE (ruled 2026-08-05) ============================
# *** ANY COMPARISON OF A PREDICTION TO A MEASUREMENT MUST REPORT BOTH AGREEMENT AND DISCRIMINATING
# POWER, OR IT DOES NOT SHIP. ***
#
# WHY. The Du et al. Sigma_0 wave produced a 0.38-sigma agreement between GRUT's mu/Sigma lock and
# the measured mu_0 -- and that agreement was reported as support. It is not: the same measurement
# separates the lock from GR at only 1.42 sigma, and mu_0 is itself consistent with zero at 1.0
# sigma. A BLUNT INSTRUMENT AGREES WITH EVERYTHING. Agreement without discriminating power is the
# ABSENCE of evidence wearing the appearance of confirmation, and it is the quantitative form of
# CHARTER Sec.4's match temptation.
#
# The rule generalizes past that paper and past this program: it is the same shape as every other
# defect here -- a check whose green state carries no information.
#
# MECHANIZATION: a calc listed below must expose, for every prediction-vs-measurement comparison,
# BOTH `agreement_sigma` AND `discrimination_sigma`, where
#     agreement      = |prediction - measurement| / combined error        (does it fit?)
#     discrimination = |prediction - null hypothesis| / measurement error (could it have not fit?)
# and a discrimination below ~2 sigma means the comparison CANNOT ADJUDICATE and must say so.
COMPARISON_CALCS = {
    "sigma0_anomaly_screen.py": ("GRUT's Sigma-1 = (mu-1)/2 lock vs Du et al. mu_0/Sigma_0; "
                                 "the mu channel discriminates at only 0.9-1.4 sigma in BOTH "
                                 "backgrounds, so it cannot test the lock"),
}
