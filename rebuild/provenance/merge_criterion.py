"""merge_criterion v3: A DECLARATION SCHEMA AND A STRUCTURAL VALIDATOR -- NOT A DECISION PROCEDURE.

================================ THE CARDINAL INVARIANT ================================
The tool validates DECLARATIONS; only ADJUDICATION decides mergers. They are structurally separate.
Every proposal carries TWO INDEPENDENT kinds of output:
  * structural verdict -- from the schema + the validators. REFUSED-INCOMPLETE and its reasons are
                          MECHANICAL: unbound eliminations, side-padding, empty accounts,
                          unregistered ids. These touch no physics judgement, and they are the
                          tool's real product.
  * declared reading   -- REDUCTION / TRADE / NO-REDUCTION. ARITHMETIC OVER ANALYST JUDGEMENTS,
                          computed downstream of the declaration; it NEVER feeds back into whether
                          the declaration was honest.
*** NO MERGE IS BANKED FOR PASSING THIS TOOL. The strongest a proposal earns is 'well-formed +
declares reading X under enumeration Y' -- a CANDIDATE FOR ADJUDICATION, never a verdict. Merge the
two kinds of output and you have rebuilt laundering at the scale of the ledger itself. ***

WHY THIS IS STRUCTURAL AND NOT A DISCLAIMER: three of the four judgements this test consumes are
DECLARED NON-MECHANIZABLE below (C1 derived-vs-posited, C2 discharge-over-the-family, C3 complete
enumeration), and the fourth -- the dimension of each input -- now requires an AUTHORED REGISTRY.
So every input to the arithmetic is an analyst judgement. The tool cannot adjudicate anything; it
does bookkeeping on decisions already made. Three successive versions each tried to close the gap
and each merely MOVED where the judgement enters: v1 counted analyst-chosen labels; v2 summed
analyst-chosen integers (strictly more expressive for an attacker); v3 moved them into a registry
and thereby broke its own pre-registration. That is a fixed point of relocation, not convergence.
The response is not another hardening round: IF A TOOL CANNOT BE CERTIFIED, DO NOT LET IT CERTIFY.

REGISTRY CAVEAT, KEPT PROMINENT: anyone relying on a score from this tool AUDITS THE REGISTRY BEFORE
THE ARITHMETIC. ATOMIC contains domain ids authored after the analyses they are used on (see
FROZEN_MERGE.txt). The arithmetic is no longer where the judgement lives.

DEFAULT-BROKEN: 'no reduction is available' is a first-class, valuable output.
========================================================================================

merge_criterion: WHEN DO UNDERIVED INPUTS COUNT AS FEWER?

*** PRE-REGISTERED. Written and frozen BEFORE application to any live verdict. Hashes are recorded
    EXTERNALLY in provenance/FROZEN_MERGE.txt -- v1 recorded its own hash inside itself, which made
    that half of the freeze unverifiable by construction (writing the hash changed the file it
    described). A freeze you cannot check is an assertion. ***

============================ WHAT v1 GOT WRONG (all four, with their fixes) ============================
v1 was certified by nine self-written controls and a four-mutant battery, and shipped with FOUR
defects, each found by independent review with a constructed counterexample. That is not an authoring
failure -- it is the CEILING OF CHECKS YOU WRITE FOR YOUR OWN WORK, and it is why the criterion was
repaired before it scaled rather than after.

D4 -- THE UNIFYING ERROR: IT NETTED A POSIT AGAINST A NUMBER.
  v1 charged a posited relation +1 and subtracted it from a saved numerical input, collapsing both
  to one scalar. That is precisely the error already ruled against one layer up, where the cluster
  inventory ships as TYPES because "the types do not commute". CONSEQUENCE, proven exhaustively
  against v1 (1712 configurations): a POSITED binary relation can NEVER merge, by arithmetic alone.
  A binary relation eliminates exactly one input -- that is what makes it class M2 -- so
  merged = separate - 1 + 1 = tie, and ties are not merges. THE MISSED CLASS THE REPAIR EXISTS FOR
  WAS UNREACHABLE FOR EVERY CONJECTURED RELATION. v1's Banks refusal was arithmetically forced, not
  physics-adjudicated: the old criterion said INVISIBLE, v1 said SEEN-AND-REFUSED, and the number on
  the map was IDENTICAL. Only the label changed.
  FIX: *** REPORT A VECTOR, NEVER A NET. *** Deltas are reported per TYPE and never summed across
  types. Banks reads "-1 number, +1 posit" -- informative and honest -- rather than a NO-MERGE
  indistinguishable from the old blindness.

D3 -- THE BUNDLE THEOREM: ANYTHING MERGES ON DEMAND.
  v1 counted the CARDINALITY OF AN ANALYST-CHOSEN LABEL SET, and cardinality is not invariant under
  re-partitioning. For any pair with |A u B| = n >= 2, declare merged_inputs = ['V'] with "each is a
  component of V, x_i = pi_i(V)" and status DERIVED (a projection is derived in the strictest
  sense, cost 0): 1 < n => MERGE. Verified at n = 2, 3, 5, 12. Exemplar: theta-bar (strong CP) and
  y_e (the electron Yukawa) -- two indisputably separate SM inputs -- merge with every checklist
  answer LITERALLY TRUE.
  FIX: count REAL-PARAMETER DIMENSION over a PRE-REGISTERED ATOMIC VOCABULARY, not labels. A bundle
  of n independent real parameters has dimension n however it is named. The theta-bar/y_e attack
  then scores 2 -> 2 (NO REDUCTION) while a genuine relation still reduces. Targeted, not merely
  stricter.

D2 -- A ONE-DIRECTIONAL ARITHMETIC BUG, IN THE MODAL CASE, UNTESTED BY ALL NINE CONTROLS.
  v1 computed len(merged | (new - (A | B))) + cost. The "- (A | B)" subtraction had no correct job:
  separate and merged are INDEPENDENT TALLIES OF DIFFERENT ACCOUNTS, so there is no cross-tally
  double-count to prevent. It leaked TOWARD MERGE -- the direction the file explicitly forbade --
  and fired whenever R references a scale already appearing on a side, WHICH IS THE MODAL CASE for
  the functional-relation class. Two analysts agreeing on every physical fact and all three
  checklist items got OPPOSITE verdicts depending on which key a scale went under.
  FIX: the merged account is tallied on its own terms (merged u new), with a VALIDATOR that refuses
  a proposal whose merged account silently drops a side's input without accounting for it.

D1 -- THE CLASSES WERE ALL TOTAL-COLLAPSE (n -> 1).
  Every v1 MERGE control had merged_count == 1 and the verdict string literally read "these are one
  input". Two real classes were therefore unrepresentable, and one of them is not localizable to
  any pair, so no amount of pairwise testing finds it:
    M5 SHARED-CONSTRAINT -- a DERIVED constraint on n >= 3 reduces the joint dimension without
       collapsing to one. Counterexample: Omega_m + Omega_Lambda + Omega_k = 1. The constraint
       surface is 2-dimensional, so three problems cost TWO inputs. EVERY PAIR SCORES NO-MERGE
       CORRECTLY (2 -> 2), and a pairwise map reports 3. A silent over-report of one -- verbatim the
       indictment this criterion levels at the one it replaced. Same shape: CKM unitarity, Born-rule
       normalization.
    M6 DISSOLUTION -- B's discharge FALSIFIES A's presupposition, so A stops being a question rather
       than being answered.
  FIX: the test is n-SIDED, both classes are added, and the verdict never says "one input".

================================ THE SIX MERGE CLASSES ================================
  M1 IDENTITY            the same parameter values discharge all sides
  M2 FUNCTIONAL RELATION a relation R makes one determine another (x_B = R(x_A))
  M3 COMMON CAUSE        all descend from a further input C
  M4 DEFINITIONAL        the same input under several names
  M5 SHARED CONSTRAINT   a derived constraint cuts the joint dimension without collapsing it
  M6 DISSOLUTION         one side's discharge falsifies another side's presupposition

================================ THE TEST (v2) ================================
Inputs are counted by REAL-PARAMETER DIMENSION over the pre-registered atomic vocabulary below,
and the result is a VECTOR, never a scalar:

    separate_dim = dim(union of the sides' inputs)
    merged_dim   = dim(merged account, tallied on its own terms, including anything R drags in)

    delta_numeric = merged_dim - separate_dim        (how many real parameters were saved)
    delta_posit   = 1 if R is POSITED else 0         (how many propositions were assumed)

    *** THESE ARE NEVER SUMMED. The types do not commute. ***

    REDUCTION      delta_numeric < 0 AND delta_posit == 0   (strictly cheaper, nothing assumed)
    TRADE          delta_numeric < 0 AND delta_posit > 0    (parameters bought with a posit --
                                                             REPORT THE VECTOR, rule with judgement)
    NO-REDUCTION   delta_numeric >= 0
Ties are not reductions. A missing checklist item is not scored at all.

================================ WHAT IS NOT MECHANIZABLE ================================
  C1 IS R DERIVED OR POSITED?  A derivation/literature judgement. "Well-motivated conjecture"
     => POSITED.
     *** C1a -- DERIVED RELATIVE TO WHOSE AXIOMS? *** (PROMOTED 2026-08-04 from a footnote to a
     REQUIRED, RECORDED field: `relation_axioms`.) "Derived" is not a property of a relation; it is
     a property of a relation GIVEN A BASE. The quantum-foundations wave turned on exactly this and
     the joint was invisible: both serious merge candidates there are DERIVED relative to their own
     axioms and POSITED from outside them, so the headline "two inputs" rests on the convention that
     A DERIVED-CONDITIONAL RELATION COUNTS AS POSITED. That convention is the INSTRUMENT'S, not the
     physics'. Under a different and defensible convention the reading moves.
     This is NOT a tool defect and adding the field does not make C1 mechanizable -- C1 is
     non-mechanizable by design and stays so. It is a defect in the RECORD: an unstated convention
     is exactly how two honest analysts reach opposite verdicts and neither can see why. The field
     does not constrain the answer; it forbids the answer being given SILENTLY.
     Record the base explicitly, e.g. "derived within Everettian unitary QM; posited relative to
     the operational/ensemble base" -- never a bare "derived".
  C2 DOES THE DISCHARGE HOLD AT OBSERVED VALUES, OVER THE PHYSICALLY RELEVANT FAMILY?
     *** NOT AT AN EXACT-SYMMETRY POINT. *** Evaluating a symmetry at its exact point, finding it
     predicts zero where the world shows a small nonzero value, and concluding it "deletes rather
     than explains" would equally refuse 't Hooft chiral protection of the electron mass. This
     program made that error and withdrew the argument.
  C3 IS THE ENUMERATION COMPLETE, AND ARE THE DIMENSIONS HONEST? Garbage in. D3 shows the
     dimension declarations are now the attack surface, so they are checklist-bound.

================================ THE DIRECTIONAL GUARD ================================
Two opposing pressures: finding a merge is flattering in general; confirming a published
independence verdict is flattering for whoever published it. DEFAULT-BROKEN TOWARD NO REDUCTION.
And note the specific v1 lesson: a NO-MERGE that is ARITHMETICALLY FORCED is not a physics
adjudication, and must never be reported as one.
"""

# ============================ F1: THE REGISTRY IS NOW A REAL OBJECT ============================
# v2 shipped a "pre-registered atomic vocabulary" that was PROSE: dimensions were read from the
# proposal itself, so the bundle attack was relocated (label-choice -> integer-choice) rather than
# closed -- and an analyst-supplied integer is STRICTLY MORE EXPRESSIVE for an attacker than an
# analyst-supplied label. v3 ships the registry as a frozen module-level object; evaluate() reads
# dimensions ONLY from here, and an id absent from it is REFUSED, never defaulted.
#
# F6: each entry carries a KIND. v2's vector correctly refused to net a posit against a number and
# then summed three incommensurable things inside "numeric" -- continuous parameters, discrete
# stances, and gauge-redundancy quotients. That is D4's own type-non-commutation argument one level
# down. The axes are now {continuous, discrete, posit} and are NEVER summed.
#
# AMENDING THIS REGISTRY IS A DATED, HASHED EVENT (FROZEN_MERGE.txt). That is the point: the
# dimension of an input must not be settleable inside the proposal that needs a particular answer.

# ============================ PART 2: THE REGISTRY IS TWO TABLES ============================
# The registry was 47 entries of which 23 were CONTROL FIXTURES -- test scaffolding sharing a
# namespace with the thing the fixtures exist to be excluded from. The `fixture` scope already made
# them structurally INERT (a fixture can never appear in a live reading), so this split is not a
# correctness fix. It is an AUDITABILITY fix, and the audit is what the whole v3 design rests on:
# v3's answer to the bundle attack was "move the judgement into a frozen registry and audit THAT",
# which fails quietly if the thing to be audited is half test data. A reader auditing the registry
# now reads INPUTS -- and INPUTS contains no test data at all.
#
# NAMESPACE, not just a field: every fixture id is `_ctl_`-prefixed and no input id may be. Pinned
# in test_merge_invariant, both directions, so a future entry cannot drift across the line.

INPUTS = {
    # --- vacuum-cluster inputs (dimensions from the typed inventory) ---
    "rho_lambda":{"dim": 1, "kind": "continuous", "scope": "cluster-input"},
    "v_ew":{"dim": 1, "kind": "continuous", "scope": "cluster-input"},
    "m_planck":{"dim": 1, "kind": "continuous", "scope": "cluster-input"},
    "vacuum_energy_gravitates":{"dim": 1, "kind": "discrete", "scope": "cluster-input"},   # a stance, not a number
    "lorentz_invariant_vacuum":{"dim": 1, "kind": "discrete", "scope": "cluster-input"},
    "heavy_thresholds_exist":{"dim": 1, "kind": "discrete", "scope": "cluster-input"},
    "ir_gravity_is_gr":{"dim": 1, "kind": "discrete", "scope": "cluster-input"},
    "naturalness_normative":{"dim": 1, "kind": "discrete", "scope": "cluster-input"},
    "typicality_measure":{"dim": 1, "kind": "discrete", "scope": "cluster-input"},
    # --- GRUT ledger inputs named in rung7_wz's recorded double-count checks ---
    "gaussian_truncation":{"dim": 1, "kind": "discrete", "scope": "grut-input"},
    "departure_shape":{"dim": 1, "kind": "discrete", "scope": "grut-input"},
    "epsilon_amplitude":{"dim": 1, "kind": "continuous", "scope": "grut-input"},
    "tau2_mode_exists":{"dim": 1, "kind": "discrete", "scope": "grut-input"},
    "rung3_single_pole":{"dim": 1, "kind": "discrete", "scope": "grut-input"},
    "system_bath_split":{"dim": 1, "kind": "discrete", "scope": "grut-input"},
    "background_causal_structure":{"dim": 1, "kind": "discrete", "scope": "grut-input"},

    # --- AMENDMENT 2026-08-04, DERIVED from the register by registry_mapping.py, not
    #     authored. Six entries; the two ids a hand-list would have added (alpha, mu_linear)
    #     were REFUSED by the register itself. See registry_amendment_2026-08-04.json. ---
    "born_measure_postulate": {"dim": 1, "kind": "discrete", "scope": "grut-input"},
    "born_rule": {"dim": 1, "kind": "discrete", "scope": "borrowed-physics"},
    "entropy_area": {"dim": 1, "kind": "discrete", "scope": "grut-input"},
    "p_tt_ansatz": {"dim": 1, "kind": "discrete", "scope": "grut-input"},
    "quantization_condition": {"dim": 1, "kind": "discrete", "scope": "grut-input"},
    "unruh_temperature": {"dim": 1, "kind": "discrete", "scope": "grut-input"},
    # --- AMENDMENT 2026-08-04 (relayed as REGISTRY_AMENDMENT_2026-08-04.txt, then ACCEPTED).
    # Derived by registry_mapping, not authored: RULE 1 -> dim 1 (one named commitment each);
    # RULE 2 -> the parent/own claim tier is `postulate` -> discrete. Scope inherited: cluster-input.
    # The four split children:
    "state_expectation_functional": {"dim": 1, "kind": "discrete", "scope": "cluster-input"},
    "mean_field_sourcing":          {"dim": 1, "kind": "discrete", "scope": "cluster-input"},
    "eft_decoupling":               {"dim": 1, "kind": "discrete", "scope": "cluster-input"},
    "eft_vacuum_operator":          {"dim": 1, "kind": "discrete", "scope": "cluster-input"},
    # The three OMISSION nodes accepted the same day. NOT in the relayed amendment text -- they are
    # DERIVED by the same domain-free mapping from register nodes the overseer accepted, and adding
    # them is what keeps the registry from going stale against the register. Flagged in the relay
    # rather than applied silently, because "the registry is derived, not authored" is only true if
    # the derivation is re-run whenever the register moves -- and a stale registry is precisely how
    # detection went blind to S1 in the first place.
    "universal_metric_coupling":    {"dim": 1, "kind": "discrete", "scope": "cluster-input"},
    "gravitational_uv_ceiling":     {"dim": 1, "kind": "discrete", "scope": "cluster-input"},
    "flatness_in_reduction":        {"dim": 1, "kind": "discrete", "scope": "cluster-input"},
}

# RETIRED registry ids. NOT DELETED: both appear in banked text, and merge_test must be able to say
# WHY a live-looking id no longer resolves instead of letting it fall through to a default dimension.
RETIRED_INPUTS = {
    "semiclassical_sourcing": "split 2026-08-04 -> state_expectation_functional + mean_field_sourcing",
    "eft_validity":           "split 2026-08-04 -> eft_decoupling + eft_vacuum_operator",
}


# The fixture table. SEPARATE NAMESPACE, SEPARATE TABLE. Nothing here is physics; nothing here can
# reach a live reading; and nothing here should cost an auditor a second glance.
FIXTURES = {
    "_ctl_xA":{"dim": 1, "kind": "continuous", "scope": "fixture"}, "_ctl_xB":{"dim": 1, "kind": "continuous", "scope": "fixture"},
    "_ctl_c":{"dim": 1, "kind": "continuous", "scope": "fixture"}, "_ctl_p":{"dim": 1, "kind": "continuous", "scope": "fixture"},
    "_ctl_a1":{"dim": 1, "kind": "continuous", "scope": "fixture"}, "_ctl_V":{"dim": 2, "kind": "continuous", "scope": "fixture"},
    "_ctl_u":{"dim": 1, "kind": "continuous", "scope": "fixture"}, "_ctl_w":{"dim": 1, "kind": "continuous", "scope": "fixture"},
    "_ctl_z":{"dim": 1, "kind": "continuous", "scope": "fixture"}, "_ctl_palias":{"dim": 1, "kind": "continuous", "scope": "fixture"},
    "_ctl_Om":{"dim": 1, "kind": "continuous", "scope": "fixture"}, "_ctl_OL":{"dim": 1, "kind": "continuous", "scope": "fixture"},
    "_ctl_Ok":{"dim": 1, "kind": "continuous", "scope": "fixture"}, "_ctl_surface":{"dim": 2, "kind": "continuous", "scope": "fixture"},
    "_ctl_sA":{"dim": 1, "kind": "continuous", "scope": "fixture"}, "_ctl_sB":{"dim": 1, "kind": "continuous", "scope": "fixture"},
    "_ctl_gauge":{"dim": 1, "kind": "discrete", "scope": "fixture"},
    # Control-B fixtures (AMENDMENT 2026-08-04): one generation's five hypercharges plus the single
    # normalization the anomaly conditions leave free. RULE 1 -> dim 1 each (each is one number);
    # RULE 2 -> continuous (numerical charges). scope 'fixture' -- the scope guard makes these
    # structurally incapable of appearing in a live reading.
    "_ctl_yQ": {"dim": 1, "kind": "continuous", "scope": "fixture"},
    "_ctl_yu": {"dim": 1, "kind": "continuous", "scope": "fixture"},
    "_ctl_yd": {"dim": 1, "kind": "continuous", "scope": "fixture"},
    "_ctl_yL": {"dim": 1, "kind": "continuous", "scope": "fixture"},
    "_ctl_ye": {"dim": 1, "kind": "continuous", "scope": "fixture"},
    "_ctl_ynorm": {"dim": 1, "kind": "continuous", "scope": "fixture"},
}

# The LOOKUP VIEW. Consumers resolve ids against this; auditors read INPUTS. The two source tables
# are asserted disjoint at import, so the view can never silently hide a collision -- an id defined
# in both would otherwise resolve to whichever table was spread second, which is precisely the kind
# of order-dependence this program keeps finding at the bottom of its defects.
assert not (set(INPUTS) & set(FIXTURES)), "INPUTS and FIXTURES must be disjoint"
assert not (set(RETIRED_INPUTS) & set(INPUTS)), "a retired id must not still be live"
ATOMIC = {**INPUTS, **FIXTURES}

# F2: the registry itself is range/type checked at import, so a malformed entry cannot reach the
# arithmetic and be caught only by a format string in the printer.
for _k, _v in ATOMIC.items():
    assert isinstance(_v.get("dim"), int) and not isinstance(_v["dim"], bool) and _v["dim"] >= 0, \
        f"ATOMIC[{_k!r}]: dim must be a non-negative int"
    assert _v.get("kind") in ("continuous", "discrete"), f"ATOMIC[{_k!r}]: bad kind"

# ============================ THE BORROWED/LEDGER SEPARATION ============================
# Every entry carries a SCOPE. This is ledger_scope's shape one level down, and it exists because
# the alternative -- a prose note saying "must never be counted as a GRUT ledger input" -- is the
# weak form this program has now rejected three separate times.
#   grut-input       an input GRUT's +13 actually pays for
#   borrowed-physics a real input to the PHYSICS that GRUT borrows and does NOT pay for
#                    (the register's own grut_standing: 'borrowed', ledger_delta 0)
#   cluster-input    an input of a scoped physics map, never of GRUT's ledger
#   fixture          a control fixture; can never appear in a live reading
# A declared reduction whose eliminated ids contain NO grut-input CANNOT read as a GRUT ledger
# move, and the tool says so in a structural field rather than a footnote.
SCOPES = {"grut-input", "borrowed-physics", "cluster-input", "fixture"}

AXES = ("continuous", "discrete", "posit")   # NEVER summed across

MERGE_CLASSES = {
    "identity": "the same parameter values discharge all sides",
    "functional-relation": "a relation R makes one determine another (x_B = R(x_A))",
    "common-cause": "all sides descend from a further input C",
    "definitional": "the same input under several names",
    "shared-constraint": "a DERIVED constraint cuts the joint dimension without collapsing it "
                         "(n >= 3; NOT localizable to any pair -- pairwise testing cannot find it)",
    "dissolution": "one side's discharge FALSIFIES another side's presupposition",
}

RELATION_STATUS = {"derived": 0, "posited": 1}

# THE PRE-REGISTERED ATOMIC VOCABULARY (D3's fix). Dimension = number of independent real
# parameters. Declared per proposal; the tool REFUSES any input without a declaration, because an
# undeclared dimension is the bundle attack's entry point.
DEFAULT_ATOMIC_DIM = 1

HUMAN_CHECKLIST = ("relation_status_justification",   # C1
                   "relation_axioms",                  # C1a -- NEW 2026-08-04: the BASE relative
                                                       # to which 'derived' is asserted. Promoted
                                                       # from footnote because it will recur in
                                                       # every cluster and was being resolved
                                                       # silently by each analyst in turn.
                   "discharge_at_observed_values",     # C2
                   "input_enumeration_source",         # C3
                   "relation_inputs")                  # F3 -- NEW in v3: the ids R ACTUALLY
                                                       # references. v2 had no such field, so
                                                       # 'eliminates' was unbound to the relation
                                                       # and an IRRELEVANT EXTRA SIDE was worth -1
                                                       # each, unflagged. Reduction depth was a
                                                       # free parameter equal to the number of
                                                       # sides the analyst chose to list.

# The output split demanded by the cardinal invariant. STRUCTURAL outcomes are verdicts the tool is
# entitled to reach; DECLARED READINGS are arithmetic over analyst judgements and are never
# adjudications. A consumer that treats a reading as a verdict has merged the two fields.
STRUCTURAL_VERDICTS = {"REFUSED-INCOMPLETE"}
DECLARED_READINGS = {"REDUCTION", "TRADE", "NO-REDUCTION"}

VERDICTS = {
    "REDUCTION": "strictly fewer real parameters, with nothing assumed to get there",
    "TRADE": "real parameters bought with a POSIT. The vector is the result; no scalar collapse is "
             "offered, and this is NOT a merge unless a human rules the posit worth its price",
    "NO-REDUCTION": "the joint account is no cheaper in real parameters",
    "REFUSED-INCOMPLETE": "the human judgements or the dimension declarations are absent -- the "
                          "tool refuses to score, because that is where the answer lives",
}
