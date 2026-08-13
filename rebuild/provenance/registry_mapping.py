"""registry_mapping: how an ATOMIC registry entry is DERIVED from the register, not authored.

*** WRITTEN DOMAIN-FREE AND BEFORE LOOKING AT WHICH IDS IT WILL PRODUCE. *** That ordering is the
whole point and it is checkable: this file names no node, no input, no cluster and no number. It
states a rule; registry_derive.py applies it mechanically; the EXCEPTION LIST is what gets reviewed.

WHY THIS EXISTS. v3 closed the bundle attack by moving dimensions out of each proposal and into a
frozen registry -- and thereby broke its own pre-registration, because a registry must NAME INPUTS,
and those 35 entries were authored by whoever runs the analysis. The proposed remedy of having the
ADJUDICATOR hand-assign them instead is strictly worse: the table would then be authored by the
person who blesses the result. The freeze record already named the real fix -- "populate the
registry from a source independent of whoever runs the analysis" -- and the register itself is that
source. It was written for other reasons, by earlier waves, under a different question.

    35 analyst judgements  ->  ONE mapping + N justified exceptions.

The mapping can be wrong. But it is wrong in ONE place, visibly, and a diff shows it moving. A
hand-assigned table is wrong in up to N places, invisibly, and nothing shows it moving.

================================ RULE 1 -- DIMENSION ================================
dim = 1 for every named input. One node, one input; one named commitment, one commitment.
Any dim > 1 is an EXCEPTION: it must carry an explicit justification recorded in the entry and be
relayed before use. Rationale: a declared input is atomic by declaration. If it is secretly a bundle
of k independent parameters, that is a fact about the REGISTER's enumeration and belongs in a
register correction, not in a dimension integer chosen at scoring time -- which is exactly the
attack v3 exists to refuse.

================================ RULE 2 -- KIND ================================
kind is derived from the claim's own TIER, through the frozen table below, or -- for an input NAMED
INSIDE a claim's ledger_note rather than being a claim itself -- from RULE 2b.

RULE 2b: an input named in prose inside a ledger_note is a DECLARED COMMITMENT, and a commitment is
DISCRETE: you either adopt it or you do not, and there is no continuum between adopting and not.
It is CONTINUOUS only if the naming text itself identifies it as a numerical amplitude or parameter
(a value that could be measured or fitted). That second clause is an EXCEPTION and is justified
individually.

================================ RULE 3 -- NON-INDEPENDENCE ================================
A claim whose ledger_delta is 0 BECAUSE ITS COST IS BOOKED ELSEWHERE is NOT an independent input and
gets NO registry entry. Scoring it as a side would double-count against the ledger's own
anti-double-count rulings. This rule exists because the register already answers "what is this?" for
such claims, and re-deciding it at amendment time discards that answer.
"""

# The frozen tier -> kind table. Both vocabularies, one table, no domain content.
TIER_KIND = {
    # --- physics vocabulary (provenance/physics_vocab.py) ---
    "measured":        "continuous",   # a number obtained from data
    "fitted":          "continuous",   # a number obtained by adjustment
    "postulate":       "discrete",     # a proposition: asserted or not
    "heuristic":       "discrete",     # a criterion: applied or not
    "open":            "discrete",     # a question, not a quantity
    # --- GRUT vocabulary (provenance/auditor.py DEFAULT_TIERS) ---
    "assumed":         "discrete",     # an adopted stance
    "to-derive":       "discrete",     # an open commitment
    # --- tiers that assert a RESULT rather than an input ---
    "shown":           None,           # see EXCEPTION_KINDS: a result is not an underived input;
    "derived":         None,           #   its DECLARED INPUTS are, and those are named separately
    "derived-pending": None,
}

# A tier mapping to None means: this claim is not itself an underived input. Its ledger_note's
# NAMED INPUTS are the registry candidates, handled by RULE 2b.
RESULT_TIERS = {t for t, k in TIER_KIND.items() if k is None}

DEFAULT_DIM = 1
COMMITMENT_KIND = "discrete"           # RULE 2b default

# Every deviation from the rules above must appear here, with a reason, and is what gets reviewed.
# Populated by registry_derive.py's operator, NOT by the rules -- so the exception list is the
# audit surface and the mapping stays domain-free.
EXCEPTION_SCHEMA = ("id", "rule_deviated", "justification", "declared_by")
