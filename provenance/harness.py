#!/usr/bin/env python3
"""GRUT Forward-Model Harness -- the generative face (consistency-and-phenomenology of candidate universes).

Extends the resident from CLAIMS to whole MODELS. Sample a responsive-medium vacuum (a response-kernel
spec), turn the shown formalism's crank (the forward map: kernel -> observables), filter for ADMISSIBILITY
(the no-go checks + the resident's dependency/consistency discipline), and -- in a STRUCTURALLY SEPARATE
downstream layer -- compare to DATA. It tells you which responsive-medium universes are admissible and what
they predict; it NEVER tells you which is ours.

================================ THE CARDINAL INVARIANT ================================
The machine tests ADMISSIBILITY; only DATA tests REALITY. They are structurally separate. Every candidate
universe carries TWO INDEPENDENT fields:
  * admissible      -- from the discipline + the no-gos. admissible() NEVER receives data.
  * data_consistent -- from comparison to observation. Computed DOWNSTREAM of admissibility; it NEVER
                       feeds back into admissible.
No universe is banked shown/real for passing the machine. The strongest a candidate earns is
'admissible + predicts X + consistent-with-data-Y-at-current-precision' -- a CANDIDATE tier, never shown.
Merge the two fields and you have rebuilt laundering at the scale of whole universes.

DEFAULT-BROKEN: 'no admissible kernel reproduces our universe' is a first-class, valuable output.
NO TUNING-AS-LAUNDERING: a kernel that matches data only by violating a no-go or needing an un-sourced
input does NOT pass -- the data layer raises a laundering flag.
BOUNDED FAMILY: only responsive-medium-with-finite-memory universes; off-premise specs are inadmissible.

Pure Python stdlib. Reads the register (claims.json/sources.json) for admissibility; never writes it.
"""
from resident import dependency_graph, _is_closed  # reuse the resident's DAG check + AUTHORITATIVE closed-check

# --------------------------------------------------------------------------- universe spec

# A "GRUT universe" = a response-kernel spec + provenance (each free choice sourced to a register rung).
# It is a CANDIDATE, never a banked truth. The free data:
KERNEL_FIELDS = ("spectral_form", "L0", "T", "alpha", "projector", "second_scale")

# the bounded family: only these spectral forms are inside the responsive-medium-with-finite-memory premise.
ON_PREMISE_FORMS = ("single-pole", "super-ohmic-cutoff")


def universe(id, spectral_form="single-pole", L0=1.0, T=1.0, alpha=1.0 / 3.0,
             projector="TT", x=None, second_scale=None, tuned_active=False, provenance=None):
    """Construct a candidate-universe spec. `provenance` maps each free choice -> a register rung id.
    `second_scale` = an inserted IR relaxation scale (rung7's two-scale commitment); `tuned_active` = an
    active/sign-changing response tuned to flip the w_a sign -- both are inputs the SHOWN spine does not
    derive (they are assumed, not shown), so a prediction relying on them carries the inserted-input flag."""
    prov = {
        "spectral_form": "rung3_single_pole", "L0": "rung1_inin_action", "T": "rung2_kms_gate",
        "alpha": "rung9a_value",
        "projector": ("zeta_interior_family" if projector == "interior" else "p_tt_ansatz"),
        "second_scale": "rung7_wz",   # the two-scale commitment is rung7's NAMED assumed input
        "tuned_active": "rung7_wz",    # the active/sign-changing response rung7 names as needed for DESI
    }
    if provenance:
        prov.update(provenance)
    return {
        "id": id,
        "kernel": {"spectral_form": spectral_form, "L0": L0, "T": T, "alpha": alpha,
                   "projector": projector, "x": x, "second_scale": second_scale, "tuned_active": tuned_active},
        "provenance": prov,
        "tier": "candidate",  # NEVER 'shown'; the harness cannot graduate a universe to real.
    }


# --------------------------------------------------------------------------- forward map (kernel -> observables)

def _chi(omega, L0):
    """Single-pole retarded susceptibility chi(omega) = 1/(1 - i*omega*L0); chi(0)=1."""
    return 1.0 / (1.0 - 1j * omega * L0)


def forward_tidal(kernel):
    """rung4 (SHOWN): elastic (Love) storage Re chi + dissipative loss Im chi, KK-linked. Derived."""
    L0 = kernel["L0"]
    if not L0 or L0 <= 0:  # off-premise (no finite memory): no tidal response, do not divide by zero
        return {"derived": False, "rung": "rung4_love_kk", "samples": {},
                "note": "L0<=0 (off-premise): no finite-memory tidal response."}
    sample = {}
    for omega in (0.0, 0.5 / L0, 1.0 / L0):
        c = _chi(omega, L0)
        sample[omega] = {"storage_Re_chi": c.real, "loss_Im_chi": c.imag}
    # GW-dissipation observability is Planck-suppressed (banked rung4): real but ~10^22-10^62 below.
    return {"derived": True, "rung": "rung4_love_kk", "samples": sample,
            "gw_dissipation_orders_below_detectable": "22..62", "note": "real but invisible (Planck-suppressed)"}


def forward_wz(kernel):
    """rung7 (TO-DERIVE, guard tuning): a relaxing chi(omega) -> effective dark-energy w(z).
    DERIVED, not fit: a single UV-memory scale gives w=-1 FLAT (reproduces Lambda) -- the SOURCED prediction.
    Evolving w(z) REQUIRES a second, cosmologically-slow scale tau2 ~ 1/H0 -- an INSERTED input (rung7's
    two-scale commitment, living in the mu_linear-EXCLUDED trace sector). The wa SIGN of that inserted
    relaxor is FRONTIER-indeterminate (rung7_w2 sign screen, 2026-06-29). The second law fixes only the
    SIDE: passivity (zeta>=0 -> Pi=-3 zeta H <= 0) puts the dissipative branch at w<=-1 and the reactive
    (Re chi) branch at w>=-1 -- which forbids a crossing on each branch -- but NOT the wa SLOPE sign
    (sigma=Pi^2/(zeta T) is quadratic in Pi, blind to dPi/dt; the toy's wa<=0 is a zeta=const artifact,
    other passive zeta(a) scalings give wa>0). NEITHER sign is sourced. So a target evolving w(z), of
    EITHER sign, cannot be reproduced without the un-sourced second scale -> FLAGGED. The no-clean-DESI-
    match result is carried by the evolving => needs_unsourced_input INVARIANT, NOT by the sign."""
    if kernel.get("second_scale") is None:
        # single-scale responsive vacuum: w(z) does not evolve. Derived from the shown single-pole.
        # ('derived' here = map-derived-from-the-shown-single-pole, NOT a register-tier promotion;
        #  rung7's EVOLVING w(z) stays to-derive -- only the w=-1 FLAT structure is robust.)
        return {"derived": True, "needs_unsourced_input": False, "rung": "rung7_wz",
                "w0": -1.0, "wa": 0.0, "evolves": False,
                "note": "single UV-memory scale -> w=-1 flat (= LambdaCDM); no DE evolution derived."}
    if kernel.get("tuned_active"):
        # tuned active/sign-changing response: CAN be made to hit DESI's w_a<0, but ONLY by inserting an
        # active response the shown spine does not supply -- a second inserted input (heavier tuning).
        return {"derived": False, "needs_unsourced_input": True, "rung": "rung7_wz",
                "w0": -0.95, "wa": -0.4, "evolves": True, "sign_status": "tuned-to-DESI",
                "note": "w(z) hits DESI's w_a<0 ONLY via an inserted active/sign-changing response (un-sourced, "
                        ">=2 inserted inputs). A data MATCH bought this way is TUNING-AS-LAUNDERING."}
    # two-scale, passive: w(z) evolves, but ONLY because the second slow scale was INSERTED (un-sourced, in
    # the mu_linear-excluded trace sector). The wa SIGN is frontier-indeterminate (rung7_w2). This
    # representative is CHOSEN to carry a DESI-SIGN wa (the sign is a modeling choice, not fixed: the 2nd
    # law fixes only the phantom SIDE, not the wa slope) PRECISELY so it MATCHES DESI's sign within
    # precision yet is STILL laundering-flagged on inserted-input grounds alone -- the strongest showcase
    # that the machine refuses a DESI-looking universe without the sourcing.
    return {"derived": False, "needs_unsourced_input": True, "rung": "rung7_wz",
            "w0": -0.95, "wa": -0.3, "evolves": True, "sign_status": "frontier-indeterminate (DESI-sign representative chosen for the showcase)",
            "note": "w(z) evolves ONLY via an inserted 2nd slow scale tau2~1/H0 (un-sourced, mu_linear-excluded "
                    "trace sector). The wa SIGN is FRONTIER (rung7_w2): the 2nd law fixes the dissipative branch "
                    "on the phantom SIDE (w<=-1, forbids crossing) but NOT the wa slope sign; this representative "
                    "is chosen DESI-sign to demonstrate the guard. Matches DESI's SIGN yet STILL laundering-flagged "
                    "-- refused on inserted-input grounds, not on the sign. The SOURCED prediction is w=-1 FLAT."}


def forward_decoherence(kernel):
    """rung8 (TO-DERIVE): noise kernel N -> Anastopoulos-Hu master equation -> decoherence signature.
    The signature FOLLOWS FROM N (energy-basis: Gamma scales with the energy gap dE, ignores spatial dx --
    orthogonal to Diosi-Penrose/CSL), it is NOT inserted. Magnitude is quiet-or-faint (banked rung8):
    the dominant diagonal coupling samples S(0)=0 (quiet); the off-diagonal wedge is 7-47 orders below
    detectable. Shape derived from N; magnitude not a working observable."""
    # super-Ohmic noise S(omega) ~ omega^3 coth(omega/2T) -> S(0)=0 (the quiet floor); energy-basis shape.
    return {"derived": True, "needs_unsourced_input": False, "rung": "rung8_falsifier",
            "basis": "energy", "signature": "Gamma(dE) ~ |A_nm|^2 S(dE/hbar)/hbar^2 (scales with energy gap, ignores dx)",
            "S_at_zero": 0.0, "off_diagonal_orders_below_detectable": "1e7..1e47",
            "note": "shape DERIVED from N (energy-basis wedge); magnitude quiet-or-faint, not a working observable."}


def forward_mu(kernel):
    """The mu-sector prediction across the banked interior family (source of truth:
    calc/mu_slip_interior.py -- these are its exact formulas; the cross-subsystem regression test
    imports that module and asserts agreement). TT is the x=0 member; 'interior' carries x."""
    proj = kernel.get("projector")
    alpha = kernel.get("alpha", 1.0 / 3.0)
    if proj == "TT":
        x = 0.0
    elif proj == "trace-only":
        # the banked x=1 ENDPOINT member (mu=4/3): mapping it keeps the ISW leg of the endpoint
        # exclusion EXPRESSIBLE in the data layer (defense-in-depth on top of the structural
        # separate-universe no-go -- x=1 sits far outside the window, so data_consistent fails too).
        x = 1.0
    elif proj == "interior":
        x = kernel.get("x")
        if x is None:
            return {"x": None, "note": "interior without x: mu-sector undefined (inadmissible upstream)."}
    else:
        return {"x": None, "note": f"projector {proj!r}: no banked mu-sector family prediction."}
    mu = 1.0 + x * alpha
    return {"x": x, "mu": mu, "eta": 1.0 / (1.0 + x * alpha), "Sigma": 1.0 + x * alpha / 2.0,
            "isw_sigma_nominal": 2.0 * x,  # cross-channel, COMPUTED (Sigma-corrected, firewall B1; == msi.isw_sigma, test-pinned)
            "note": ("banked family (mu_slip_interior; exact at the inherited-bookkeeping level -- eta=1/mu "
                     "is conditional on its one-sidedness, R2, owned by the demotion screen); the family "
                     "allows, it does not predict (x has no floor); isw_sigma_nominal carries the anchor's "
                     "provenance caveat.")}


def forward_map(spec):
    """Turn the shown formalism's crank: kernel -> predicted observables. Returns predictions + any flags."""
    k = spec["kernel"]
    preds = {
        "tidal": forward_tidal(k),
        "wz": forward_wz(k),
        "decoherence": forward_decoherence(k),
        "mu_sector": forward_mu(k),
    }
    # LOAD-BEARING INVARIANT (the single line the whole anti-laundering guarantee rests on): an evolving
    # w(z) branch MUST carry the inserted-input flag, so a future edit cannot silently add a clean evolving
    # branch that the data layer would pass as a free DESI match.
    wz = preds["wz"]
    # NOTE: these asserts are a DEV-TIME aid (stripped under `python -O`); the REAL laundering guarantee
    # is the observable-keyed check in data_consistent (keyed on wa != 0 + needs_unsourced_input, not on
    # the `derived` flag), covered by test_omitted_evolves_key_cannot_smuggle_clean_match.
    assert "evolves" in wz and "needs_unsourced_input" in wz, \
        "INVARIANT: forward_wz must DECLARE 'evolves' and 'needs_unsourced_input' explicitly (no silent default)."
    assert (not wz.get("evolves")) or wz.get("needs_unsourced_input"), \
        "INVARIANT: an evolving w(z) must set needs_unsourced_input (no clean evolving branch)."
    unsourced = sorted(name for name, p in preds.items() if p.get("needs_unsourced_input"))
    return {"predictions": preds, "needs_unsourced_input": unsourced}


# --------------------------------------------------------------------------- admissibility (NEVER sees data)

def _mu_linear(kernel):
    """The mu-sector STRUCTURAL check (2026-08-02 refactor -- the interior-wave landing).

    The old form hard-coded the TT/trace-only DICHOTOMY the p_tt interrogation identified as
    non-exhaustive (KC5), and cited the ~32sigma ISW -- OBSERVATION -- inside admissible(), a data
    exclusion sitting in the structural layer. The screened split (relayed, not silent):
      * STRUCTURAL layer (here): the interior family K = c2*P^TT + c0*P0s is a LEGAL kernel family
        (eft_operator_basis + the p_tt interrogation, banked) -- projector 'interior' with admixture
        x in [0,1) is admissible; mu(x)/eta(x)/Sigma(x) come from calc/mu_slip_interior.py, the
        banked source of truth. The trace-only ENDPOINT stays structurally inadmissible on the
        SEPARATE-UNIVERSE consistency no-go ALONE (internal/structural, banked in mu_linear) --
        NOTE the no-go is banked for the ENDPOINT; its extension into the interior is UNSCREENED
        (flagged, not assumed either way).
      * DATA layer (data_consistent): the mu-sector window edge (COMPUTED 2026-08-03: lensing-bound
        x < ~0.594, central-inputs/loose-upper per the F-MAP fence -- the binding inversion; see
        calc/isw_exclusion.py) lives THERE -- observation can bound the family, never define
        admissibility.
    This STRENGTHENS the cardinal invariant. (Precisely -- firewall-corrected 2026-08-03: the OLD
    verdicts were hard-coded booleans, so no ISW-number edit could have flipped them; the old form's
    real defects were (a) DATA GROUNDS CITED inside the structural layer -- the ~32sigma appeared in
    an admissible() reason -- and (b) the hard-coded non-exhaustive dichotomy, KC5, which made the
    banked interior inadmissible. The split fixes both: observation now BOUNDS the family in the
    data layer; it never grounds, and cannot tune, admissibility.)"""
    proj = kernel.get("projector")
    alpha = kernel.get("alpha", 1.0 / 3.0)
    if proj == "TT":
        return 1.0, True, "TT projector -> mu=1 (LambdaCDM at linear order); admissible (the x=0 member).", None
    if proj == "interior":
        x = kernel.get("x")
        if x is None or not (0.0 <= x < 1.0):
            return None, False, (f"interior projector needs admixture x in [0,1); got {x!r}. (x=1 IS the "
                                 "trace-only ENDPOINT, excluded by the banked separate-universe no-go -- "
                                 "this fence is physics, not parameter validation.)"), "range-fence"
        mu = 1.0 + x * alpha
        return mu, True, (f"interior x={x:g} -> mu={mu:.4f} (banked family, mu_slip_interior); structurally "
                          "admissible -- the ISW window bound is a DATA-layer question, not admissibility. "
                          "(Separate-universe no-go banked for the x=1 ENDPOINT; interior extension unscreened.)"), None
    if proj == "trace-only":
        mu = 1.0 + alpha
        return mu, False, (f"trace-only projector -> mu={mu:.3f}: EXCLUDED structurally by the SEPARATE-"
                           "UNIVERSE consistency no-go (banked, internal; EdS-quantified in "
                           "isw_exclusion.py PART E). The empirical legs (ISW-cross COMPUTED ~2.0sigma + "
                           "DESI Sigma0 ~3.5sigma) are DATA-layer exclusions and live in data_consistent, "
                           "not here."), "separate-universe-endpoint"
    return None, False, f"unknown projector {proj!r}: cannot establish the mu sector; inadmissible.", "unknown-projector"


def _kms_locked(kernel):
    """rung2/KMS detailed balance: the noise must be locked to Im chi by coth(omega/2T) (FDT). A spec that
    declares a non-KMS bath fails the hard admission gate. (Here the spec is KMS-locked by construction
    unless T<=0 or an explicit kms=False is set.)"""
    T = kernel.get("T", 1.0)
    if T is None or T <= 0:
        return False, "no positive KMS temperature -> FDT/detailed-balance gate fails; inadmissible."
    if kernel.get("kms") is False:
        return False, "declared non-KMS bath -> fails the rung2 detailed-balance gate; inadmissible."
    return True, "KMS-locked (N = coth(omega/2T) Im chi); passes the rung2 gate."


# NOTE: the local free-text PROV_CLOSED_MARKERS substring scan is RETIRED. The harness now consults the
# resident's AUTHORITATIVE structured closed-check (`_is_closed` / `CLOSED_DISPOSITIONS`), so the two
# subsystems can never diverge on closed-ness. The divergence this fixes: the old marker list scanned
# `sub_status` and was missing 'screened-dissolves' and 'frozen-V1', letting a spec source a kernel input
# to a closed claim (e.g. l0_r2_exact_unique_breaker, disposition='screened-dissolves') and pass
# admissibility, while resident._is_closed correctly reported it closed. See test_harness regressions.


def _active_kernel_inputs(kernel):
    """The kernel fields that are ACTIVELY in play and therefore REQUIRE a provenance source."""
    active = ["spectral_form", "L0", "T", "alpha", "projector"]
    if kernel.get("second_scale") is not None:
        active.append("second_scale")
    if kernel.get("tuned_active"):
        active.append("tuned_active")
    return active


def _provenance_consistent(spec, claims):
    """Every ACTIVE kernel input must be SOURCED to a real register claim that is NOT a CLOSED disposition.
    An inserted input with NO provenance entry (un-sourced), a dangling source, or a source leaning on a
    claim the resident deems closed (`_is_closed`: any of CLOSED_DISPOSITIONS -- settled-negative /
    no_go_export / screened-refuted / disfavored / frozen-V1 / moot / deferred / screened-dissolves /
    forbidden) is INADMISSIBLE -- you cannot source a model choice to closed ground, and you cannot
    smuggle an inserted input in un-sourced. Closed-ness is read from the resident's AUTHORITATIVE
    structured check so the harness and resident can never diverge (they share one closed-set)."""
    by_id = {c["id"]: c for c in claims}
    prov = spec.get("provenance", {})
    reasons, ok = [], True
    for field in _active_kernel_inputs(spec["kernel"]):
        rung = prov.get(field)
        if rung is None:
            ok = False
            reasons.append(f"active input '{field}' has NO provenance -> un-sourced inserted input.")
            continue
        dep = by_id.get(rung)
        if dep is None:
            ok = False
            reasons.append(f"provenance[{field}] -> '{rung}' does not resolve to a register claim.")
            continue
        if _is_closed(dep):  # AUTHORITATIVE structured closed-check (shared with the resident)
            ok = False
            reasons.append(f"provenance[{field}] -> '{rung}' is a CLOSED disposition "
                           f"({dep.get('disposition')!r}); cannot source a model choice to closed ground.")
    return ok, reasons


def admissible(spec, claims):
    """Is this candidate universe ADMISSIBLE? Discipline + no-gos ONLY. *** NEVER receives data. ***
    Returns (admissible: bool, report: dict). The absence of a `data` parameter is the cardinal invariant
    in code: admissibility cannot see, and therefore cannot be tuned by, observation."""
    k = spec["kernel"]
    reasons = []

    # (precondition) reuse the resident: the register the harness certifies against must itself be a valid
    # DAG. If the discipline spine is broken, NO universe is admissible (the machine cannot certify against
    # a broken register).
    _, graph_errors = dependency_graph(claims)
    register_ok = not graph_errors
    if not register_ok:
        reasons.append(f"register integrity FAILED ({graph_errors[:1]}); no universe admissible until fixed.")

    # (0) bounded family: only responsive-medium-with-finite-memory specs.
    on_premise = k.get("spectral_form") in ON_PREMISE_FORMS and (k.get("L0") or 0) > 0
    if not on_premise:
        reasons.append(f"off-premise: spectral_form {k.get('spectral_form')!r} / L0={k.get('L0')} is outside "
                       "the responsive-medium-with-finite-memory family.")

    # (1) the mu_linear no-go.
    mu, mu_ok, mu_msg, mu_basis = _mu_linear(k)
    reasons.append(mu_msg)

    # (2) rung2/KMS detailed balance.
    kms_ok, kms_msg = _kms_locked(k)
    reasons.append(kms_msg)

    # (3) provenance / dependency consistency (resident reuse).
    prov_ok, prov_reasons = _provenance_consistent(spec, claims)
    reasons.extend(prov_reasons)

    is_admissible = register_ok and on_premise and mu_ok and kms_ok and prov_ok
    return is_admissible, {
        "admissible": is_admissible,
        "register_ok": register_ok,
        "mu_linear": {"mu": mu, "ok": mu_ok, "exclusion_basis": mu_basis},
        "kms_detailed_balance": kms_ok,
        "on_premise": on_premise,
        "provenance_consistent": prov_ok,
        "reasons": reasons,
    }


# --------------------------------------------------------------------------- data layer (DOWNSTREAM; never feeds admissibility)

# The truth-test inputs -- OBSERVATION, kept explicitly separate. Editing these can NEVER change admissibility.
OBSERVATIONS = {
    "desi_w0": -0.95,     # DESI 2024-25 hint: w0 > -1
    "desi_wa": -0.4,      #                    wa < 0 (quintom crossing)
    "lcdm_w": -1.0,       # LambdaCDM reference
    "w_precision": 0.2,   # current (w0,wa) precision scale
    "decoherence_bound_orders": 1,  # tabletop bound: a signal must be within ~1 order of detectable
    # the mu-sector window edge for the interior family (DATA, COMPUTED 2026-08-03 by
    # calc/isw_exclusion.py; Sigma-corrected per firewall B1): the old 1/16 rested on the retired
    # ~32sigma; the computed cross-channel exclusion is ~2.0sigma (NO in-family 2sigma cross edge at
    # central inputs) and the BINDING channel is DESI Sigma0 lensing under the banked slip
    # (x < ~0.594, CENTRAL-INPUTS + LOOSE-UPPER per the F-MAP fence: DESI's Sigma0 is
    # OmegaL(a)-shaped, the family's Sigma-1 constant -- shape-weighted mapping plausibly 2-3x
    # tighter). The TT-auto channel (estimate-grade edge band ~0.03-0.14) is OWED its own calc.
    "mu_window_edge_x": (0.009 + 2 * 0.045) * 2.0 * 3.0,  # = 0.594 (alpha = 1/3; == msi.EDGE, test-pinned)
}


def data_consistent(predictions, data=OBSERVATIONS):
    """Compare an ADMISSIBLE survivor's predictions to DATA. *** This is the TRUTH-TEST, and it is a
    SEPARATE FIELD, computed downstream of admissibility; it NEVER feeds back. *** Returns a report with a
    laundering_flag: a 'match' achieved only via an un-sourced input or a no-go violation does NOT pass."""
    wz = predictions["wz"]
    deco = predictions["decoherence"]
    report = {"per_observable": {}, "laundering_flag": False, "notes": []}

    # w(z): is the predicted (w0,wa) within current precision of DESI? of LambdaCDM?
    dw0 = abs(wz["w0"] - data["desi_w0"])
    near_desi = (dw0 <= data["w_precision"]) and (wz["wa"] * data["desi_wa"] > 0)  # same wa SIGN as DESI
    # LambdaCDM is w=-1 CONSTANT: require BOTH w0 ~ -1 AND wa ~ 0 (an evolving w(z) is not LambdaCDM).
    near_lcdm = (abs(wz["w0"] - data["lcdm_w"]) <= data["w_precision"]) and (abs(wz["wa"]) <= data["w_precision"])
    matched_wz = near_desi or near_lcdm
    report["per_observable"]["wz"] = {"near_desi_evolving": near_desi, "near_lcdm": near_lcdm,
                                      "w0": wz["w0"], "wa": wz["wa"]}
    # NO TUNING-AS-LAUNDERING: ANY w(z) match -- DESI *or* LambdaCDM -- achieved via an inserted/un-sourced
    # input is laundering. The guard fires on BOTH branches, so widening the precision cannot let an
    # inserted-input universe collect a clean 'data-consistent' label. DEFENSE-IN-DEPTH: a matched EVOLVING
    # w(z) that is NOT flagged is treated as laundering too (so the guarantee does not rest solely on the
    # forward_map assert, which `python -O` strips) -- there is no clean evolving match, by construction.
    # HARDENING (firewall 2026-06-29, omitted-key lens): `evolving` is keyed on the OBSERVABLE (wa != 0),
    # not only the self-declared 'evolves' flag -- a hand-built wz that OMITS 'evolves'/'needs_unsourced_input'
    # (where .get() would default False) cannot smuggle a clean DESI-sign match: a nonzero wa IS evolution.
    evolving = bool(wz.get("evolves")) or abs(wz.get("wa", 0.0)) > 0.0
    if matched_wz and (wz.get("needs_unsourced_input") or evolving):
        report["laundering_flag"] = True
        report["notes"].append("w(z) match relies on an inserted/un-sourced input (or evolves) -> "
                               "TUNING-AS-LAUNDERING, not a pass.")

    # mu sector (the interior family): OBSERVATION bounds the admixture -- x below the lensing-bound window edge
    # is data-consistent; above it is not. This bound lives HERE, never in admissible().
    mus = predictions.get("mu_sector")
    mu_ok = True
    if mus is not None and mus.get("x") is not None:
        mu_ok = mus["x"] < data["mu_window_edge_x"]
        report["per_observable"]["mu_sector"] = {
            "x": mus["x"], "mu": mus.get("mu"), "mu_window_edge_x": data["mu_window_edge_x"],
            "within_mu_window": mu_ok,
            "note": "the family ALLOWS up to the edge; it predicts nothing (x has no floor)."}

    # decoherence: quiet/faint -> consistent with the tabletop NULL (no signal expected, none seen).
    deco_consistent = (deco.get("S_at_zero") == 0.0)  # quiet floor -> below any bound, no false signal
    report["per_observable"]["decoherence"] = {"consistent_with_null": deco_consistent,
                                               "note": "quiet/faint, below detectability -> consistent with the null bound; "
                                                       "NON-DISCRIMINATING (passes every admissible kernel)"}

    # a CLEAN match: a NON-evolving w(z) match (=LambdaCDM) that needed NO inserted input, plus the null.
    # (uses the hardened `evolving` -- a nonzero-wa prediction can never be clean, key present or not.)
    clean_match = (matched_wz and not wz.get("needs_unsourced_input")
                   and not evolving and deco_consistent and mu_ok)
    report["data_consistent"] = bool(clean_match) and not report["laundering_flag"]
    return report


# --------------------------------------------------------------------------- evaluate + sample

def evaluate(spec, claims, data=OBSERVATIONS):
    """Full record for one candidate universe. admissible is computed WITHOUT data; data_consistent is
    computed DOWNSTREAM and only for the survivors. The two are stored as separate fields."""
    adm, adm_report = admissible(spec, claims)            # <-- no data passed in
    fwd = forward_map(spec)
    record = {
        "id": spec["id"], "tier": spec["tier"], "kernel": spec["kernel"],
        "admissible": adm, "admissibility": adm_report,
        "predictions": fwd["predictions"], "needs_unsourced_input": fwd["needs_unsourced_input"],
        "data_consistent": None,  # filled ONLY if admissible (truth-test runs downstream)
    }
    if adm:
        dc = data_consistent(fwd["predictions"], data)
        record["data_consistent"] = dc["data_consistent"]
        record["data_comparison"] = dc
    # the strongest earned label -- a CANDIDATE, never shown:
    if adm:
        record["earned_label"] = ("admissible + predicts(w0=%.2f,wa=%.2f; energy-basis decoherence; invisible tidal)"
                                  % (record["predictions"]["wz"]["w0"], record["predictions"]["wz"]["wa"])
                                  + (" + data-consistent-at-current-precision" if record["data_consistent"] else "")
                                  + " -- CANDIDATE, never shown")
    else:
        record["earned_label"] = "INADMISSIBLE (excluded by the machine)"
    return record


def sample_family(claims, specs, data=OBSERVATIONS):
    """Run the sampler over a kernel family; return the honest map: admissible set, what they predict,
    and the data-consistent subset (with laundering flagged)."""
    records = [evaluate(s, claims, data) for s in specs]
    admissible_set = [r for r in records if r["admissible"]]
    data_matching = [r for r in admissible_set if r["data_consistent"]]
    laundered = [r for r in admissible_set if r.get("data_comparison", {}).get("laundering_flag")]
    return {
        "records": records,
        "n_total": len(records),
        "n_admissible": len(admissible_set),
        "n_data_consistent_clean": len(data_matching),
        "n_match_only_via_laundering": len(laundered),
        "admissible_ids": [r["id"] for r in admissible_set],
        "data_consistent_ids": [r["id"] for r in data_matching],
    }


# --------------------------------------------------------------------------- demo

def _load(name):
    import json
    import os
    with open(os.path.join(os.path.dirname(os.path.abspath(__file__)), name)) as f:
        return json.load(f)


def _demo():
    claims = _load("claims.json")["claims"]
    family = [
        universe("U_TT_1scale"),                                   # TT, single-scale, KMS -> admissible, w=-1 (clean LCDM)
        universe("U_TT_2scale", second_scale=1e3),                 # TT + inserted 2nd scale -> admissible, DESI-SIGN wa<0 but FLAGGED (inserted-input)
        universe("U_TT_tunedDESI", second_scale=1e3, tuned_active=True),  # tuned to hit DESI -> admissible, MATCH-VIA-LAUNDERING
        universe("U_interior_x03", projector="interior", x=0.03),  # interior x=0.03 -> mu~1.01, admissible, inside the mu window
        universe("U_traceonly", projector="trace-only"),           # trace-only -> mu=4/3 EXCLUDED (structural; x=1 endpoint)
        universe("U_nonKMS", projector="TT", T=0.0),               # no KMS -> inadmissible
        universe("U_offpremise", spectral_form="free-streaming"),  # off-premise -> inadmissible
    ]
    summary = sample_family(claims, family)
    print("=" * 80)
    print("GRUT FORWARD-MODEL HARNESS -- the generative face (demo)")
    print("=" * 80)
    print("\nCARDINAL INVARIANT: admissible (machine) and data_consistent (data) are SEPARATE fields;")
    print("admissible() never receives data. No universe is banked 'real' for passing the machine.\n")
    for r in summary["records"]:
        adm = "ADMISSIBLE" if r["admissible"] else "inadmissible"
        dc = ("" if not r["admissible"]
              else f"  data_consistent={r['data_consistent']}"
                   + ("  [MATCH-VIA-LAUNDERING: flagged, not a pass]" if r.get("data_comparison", {}).get("laundering_flag") else ""))
        print(f"  {r['id']:16} [{adm:12}] w0={r['predictions']['wz']['w0']:+.2f} wa={r['predictions']['wz']['wa']:+.2f}{dc}")
    print(f"\n  totals: {summary['n_admissible']}/{summary['n_total']} admissible; "
          f"{summary['n_data_consistent_clean']} data-consistent (clean); "
          f"{summary['n_match_only_via_laundering']} match-only-via-laundering (FLAGGED, excluded).")
    print("\n  HONEST MAP: the admissible family is the TT / KMS-locked / finite-memory vacua -> mu=1 LambdaCDM --")
    print("  PLUS the banked interior members (mu up to 1+x*alpha, structurally admissible for x in [0,1),")
    print("  data-BOUNDED by the computed mu-sector window x<~0.59 (lensing binds; the owed TT-auto")
    print("  calc likely re-tightens): the family allows, it does not predict) --")
    print("  w=-1 flat, energy-basis (quiet) decoherence, invisible tidal. They are consistent with LambdaCDM")
    print("  at current precision; reproducing DESI's EVOLVING w(z) requires an un-sourced 2nd scale -> the")
    print("  match is laundering, not a clean prediction. NO admissible kernel reproduces a distinctive")
    print("  matching universe without laundering. Default-broken result, reported straight.")
    return 0


if __name__ == "__main__":
    raise SystemExit(_demo())
