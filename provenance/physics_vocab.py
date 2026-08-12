"""physics_vocab: the tier vocabulary for auditing PHYSICS AT LARGE, as ruled 2026-08-04.

WHY A SECOND VOCABULARY. The inherited GRUT vocabulary {shown, derived, derived-pending, assumed,
to-derive} grades one framework's internal derivation state. Every tier's referent is "where is
this in OUR ladder", so an observed value has no home -- and the misfit was already realized:
CHARTER.md listed Lambda under **assumed**, alongside the Born rule, when Lambda_obs is a DATUM
every candidate theory must reproduce, not a discretionary posit. (Fixed 2026-08-04; the register's
own lambda_undetermined node had it right, so the node was correct and the constitution was wrong.)

*** THE RULING'S PRINCIPLE: tiers are mutually exclusive KINDS; riders carry orthogonal ATTRIBUTES.
    A claim can be MEASURED *and* scheme-conditioned; as competing tiers it would have to pick one,
    which is a false choice. Anything that is an attribute wearing a tier costume was collapsed. ***

The proposal offered ten tiers; four were collapsed into the riders that already carry them. That
halves the ceremony without losing a distinction -- which is what CHARTER Sec1.5 asks for when it
names over-elaborate tiering as baggage.
"""

# --------------------------------------------------------------------------- the six tiers
PHYSICS_TIERS = {
    # an explicit chain from an explicitly enumerated premise set, checkable step by step.
    # TEST: can you write the premise set out, and must a referee who accepts it and rejects the
    # conclusion identify a specific defective step?
    "derived",
    # a number from data, quoted with central value, uncertainty, confidence convention, dataset,
    # and the inference model used to reduce data to it.
    # TEST: name the experiment, the error bar AND its confidence convention, and the reduction
    # model. CARRIES NO IMPLICATION ABOUT EXPLANATORY OBLIGATION -- see RISK R2 below.
    "measured",
    # a number obtained by adjusting a free parameter so the framework reproduces an observation.
    # TEST: was the value selected by reference to the datum it is later said to account for?
    # If yes: FITTED, however good the fit and however few the parameters.
    "fitted",
    # load-bearing, not derived within the audit, not measured. MANDATORY SUBTYPE (see below).
    "postulate",
    # a criterion / expectation / selection principle: a rule for what one should be SURPRISED by.
    # TEST (both must hold): (i) name a case where competent practitioners decline to apply it;
    # (ii) it grades plausibility rather than asserting a fact.
    "heuristic",
    # a well-posed question with no answer at derived/attested standing.
    # TEST: state in advance what would count as an answer AND what would count as a demonstration
    # that no answer exists. If you cannot, it is not OPEN.
    "open",
}

# POSTULATE's mandatory subtype -- the one distinction the ruling kept inside a tier, because
# "is there a live published denial?" is a fact about the world, not an attribute of our audit.
POSTULATE_SUBTYPES = {
    "contested",   # a published, internally consistent, not-empirically-dead formulation DENIES it
    "standard",    # no such live denial; includes what the proposal called DEFINITIONAL
}

# --------------------------------------------------------------------------- the four riders
# Orthogonal attributes. Cheap, and each earned by a specific failure this program has already had.
RIDERS = {
    # earned directly by the "120 orders" finding: a magnitude without its scheme is UNGRADED,
    # which is a REJECTION, not a tier. Absorbs the proposal's SCHEME-CONDITIONED tier.
    "scheme_tag": "regulator/subtraction, gauge, frame, units+normalization, renormalization point "
                  "mu; for cosmological numbers the reduction model. MANDATORY on every "
                  "quantitative claim. Missing => UNGRADED (a rejection).",
    # +1 introduces a free input, 0 neutral, -1 removes one. Same spirit as auditor.py.
    "ledger_sign": "+1 / 0 / -1. FITTED carries a NON-WAIVABLE +1 floor (see FITTED_LEDGER_FLOOR).",
    # absorbs the proposal's ATTESTED tier: 'who checked' is an attribute, not a kind.
    # 'community-folklore' is a LEGAL value and the honest home for much of this cluster.
    "attestation": "in-house-rederived | primary-re-read | recalled-from-memory | "
                   "community-folklore. The last caps the claim's strength and bars it from being "
                   "an input to a DERIVED chain.",
    # prevents input-count inflation -- the failure mode symmetric to laundering, and equally
    # corrupting to a MAP deliverable whose output is a count.
    "load": "load-bearing | decorative, RELATIVE TO THE SPECIFIC CLAIM being audited. A decorative "
            "postulate does not count toward that claim's input total.",
}

# The sharpest device in the proposal, kept verbatim by ruling: it is what stops a fitted parameter
# inheriting a datum's error bar and citation and reading downstream as empirically grounded.
FITTED_LEDGER_FLOOR = 1   # non-waivable; laundering_ok cannot lower it

# --------------------------------------------------------------------------- what was collapsed
COLLAPSED = {
    "scheme-conditioned": "-> the scheme_tag rider (duplicating it as a tier is redundant, and as a "
                          "tier it would force a false choice against MEASURED)",
    "attested":           "-> postulate + the attestation rider ('who checked' is an attribute)",
    "definitional":       "-> postulate/standard, or a rider",
    "hope":               "-> open (it is an ATTITUDE, not an epistemic kind)",
}

# --------------------------------------------------------------------------- cross-scope reading
# So a reader of one scope can read the other. Lossy BY DESIGN in the empirical direction: that
# loss is exactly the category error the CHARTER Lambda line committed, and the map makes it
# visible instead of silent.
COLLAPSE_MAP_TO_LEGACY = {
    "derived":   "derived",
    "measured":  None,        # NO legacy equivalent -- this is the gap that caused the Lambda error
    "fitted":    "assumed",   # with the +1 floor, which legacy 'assumed' does not enforce
    "postulate": "assumed",
    "heuristic": "assumed",   # legacy cannot distinguish a criterion from a proposition
    "open":      "to-derive",
}

# --------------------------------------------------------------------------- named abuse channels
# Recorded because a vocabulary's risks are load-bearing: each of these is a way a label could make
# an unearned claim look earned.
RISKS = {
    "R1 measured-as-laundering": "a framework tunes a parameter, then reports the number carrying "
                                 "the DATUM's provenance. GUARD: the FITTED tier + its +1 floor.",
    "R2 measured-as-explanandum-erasure": "'it is just what it is, we measured it' would discharge "
                                          "the cluster by fiat. GUARD: MEASURED carries NO "
                                          "implication about explanatory obligation, by definition.",
    "R4 scheme-tag-as-dismissal": "declaring an inconvenient but invariant statement "
                                  "scheme-dependent by assertion. GUARD: membership requires "
                                  "EXHIBITING a second admissible scheme in which content changes.",
    "R5 heuristic-as-merge-channel": "'several problems are conditional on the same heuristic, "
                                     "therefore they share a root' -- KC1 in new clothes. A shared "
                                     "CONDITIONING is not a shared ROOT.",
    "R6 heuristic-as-demotion-weapon": "labelling a rival's premise HEURISTIC to make it look "
                                       "costless. GUARD: the two-part membership test must be "
                                       "EXHIBITED, not asserted.",
    "R8 tier-inflation-by-compound": "a sentence with a DERIVED clause and an OPEN clause grades by "
                                     "its strongest clause. GUARD: ATOMICITY is a precondition of "
                                     "grading; an ungradeable compound is UNGRADED. (This wave "
                                     "caught TWO compounds in its own enumeration.)",
    "R12 tiering-mistaken-for-analysis": "a complete tier assignment feels like understanding. It "
                                         "is a CLASSIFICATION and yields no merge, no separation, "
                                         "and no count by itself.",
}
