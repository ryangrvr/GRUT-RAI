#!/usr/bin/env python3
"""HISA-01 — REPAIR / RE-ADJUDICATE THE 43 FAILED EVIDENCE OCCURRENCES.

Repair population is derived MECHANICALLY from
program/HISA01_EVIDENCE_CONTAINMENT_AUDIT.json (every outcome not a
PASS_*).  The 19 passing occurrences are untouched.

For each failed occurrence a FRESH statement-level adjudication is applied.
The original independent adjudication is quarantined metadata only; it is
NEVER used as a semantic prior.  Every repaired citation is validated by
exact byte/string containment against the frozen package (no normalization,
no splicing, no reconstruction).  Candidate terms absent from the supplied
frozen evidence are recorded as SUPPORTED_ABSENCE (NOT_SPECIFIED /
NOT_COMPARABLE), never filled with conventional physics meaning.

Outputs:
    program/HISA01_REPAIRED_43_ADJUDICATION.json
    program/HISA01_REPAIRED_43_ADJUDICATION_REPORT.md
"""
import hashlib, json, os, re
from pathlib import Path

HERE = Path(__file__).resolve().parent
FROZEN = HERE / "HISA01_FROZEN_EVIDENCE_PACKAGE.json"
ORIG = HERE / "HISA01_INDEPENDENT_SEMANTIC_ADJUDICATION.json"
AUDIT = HERE / "HISA01_EVIDENCE_CONTAINMENT_AUDIT.json"
OUT = HERE / "HISA01_REPAIRED_43_ADJUDICATION.json"
MD = HERE / "HISA01_REPAIRED_43_ADJUDICATION_REPORT.md"

def sha(p):
    return hashlib.sha256(Path(p).read_bytes()).hexdigest()

# ---------------------------------------------------------------- templates
def T_ENUM(term, needle, role, desc):
    """Fresh re-grounding of an enumeration/presupposition mention."""
    return dict(kind="exact_source_line", quote=needle,
                typing_level="SEMANTIC", referent_status="NOT_SPECIFIED",
                mathematical_type="UNSPECIFIED",
                referent_description=desc,
                physical_role=role, comparison_status="UNRESOLVED")

def T_ABS(term):
    """Candidate term does not occur in the supplied frozen evidence."""
    return dict(kind="absent", quote=None,
                typing_level="NONE", referent_status="NOT_SPECIFIED",
                mathematical_type="UNSPECIFIED",
                referent_description=(
                    "NOT ESTABLISHED FROM SUPPLIED EVIDENCE. The candidate "
                    "term does not occur in the frozen exact_source_line or "
                    "its per-term context window for this statement; the "
                    "supplied evidence establishes no referent. (This is a "
                    "supported absence, not an inferred one.)"),
                physical_role="none established",
                comparison_status="NOT_COMPARABLE")

def J(term, typing, refstat, mtype, desc, role, comp, kind, quote):
    return dict(candidate_term=term, typing_level=typing, referent_status=refstat,
                mathematical_type=mtype, referent_description=desc,
                physical_role=role, comparison_status=comp,
                evidence_scope=kind, evidence_quote=quote)




# ============================================================ HAND ADJUDICATIONS
# Fresh decisions, each grounded ONLY in the frozen exact_source_line /
# bounded_context_window for that statement.  Every quote is an exact
# substring asserted at runtime against the frozen package.  No entry uses
# prior pair classifications as evidence.

FRESH = {}

# ---- S0: QBM boundary note -------------------------------------------------
FRESH[(0, "gauge")] = J("gauge", "SEMANTIC", "LOCALLY_TYPABLE", "UNSPECIFIED",
    "LOCALLY ESTABLISHED. The line names gauge as one of the "
    "dependence axes (gauge/scheme/prescription) that the low-omega TT "
    "transport class carries explicitly; no gauge transformation or gauge "
    "object is constructed on this line.",
    "gauge/scheme/prescription dependence axis of the low-omega TT class",
    "LEGITIMATE", "exact_source_line",
    "the gauge/scheme/prescription-dependent part of the object")

# ---- S1: Mori-Zwanzig ladder / kernel ambiguity ------------------------------
FRESH[(1, "Mori-Zwanzig")] = J("Mori-Zwanzig", "SEMANTIC", "EXPLICITLY_UNRESOLVED",
    "UNSPECIFIED",
    "EXPLICITLY UNRESOLVED BY THE SOURCE. The statement itself says the "
    "phrase 'the Mori-Zwanzig kernel' DOES NOT DENOTE A UNIQUE OBJECT; the "
    "frozen evidence preserves the ambiguity rather than resolving it.",
    "Mori-Zwanzig kernel terminology explicitly flagged as non-unique",
    "UNRESOLVED", "exact_source_line",
    "DOES NOT DENOTE A UNIQUE OBJECT")
FRESH[(1, "inner product")] = J("inner product", "SEMANTIC", "LOCALLY_TYPABLE",
    "INFERABLE",
    "LOCALLY ESTABLISHED. The line states that the Mori-Zwanzig projection "
    "conventionally uses the Kubo-Mori (canonical) inner product, and that "
    "the Kubo correlation carries C_K. The inner-product object is "
    "conventionally identified, not formally defined here.",
    "the conventional (Kubo-Mori) inner product of the Mori-Zwanzig "
    "projection",
    "LEGITIMATE", "exact_source_line",
    "conventionally uses the KUBO-MORI (canonical) inner product")
FRESH[(1, "cutoff")] = J("cutoff", "SEMANTIC", "LOCALLY_TYPABLE", "INFERABLE",
    "LOCALLY ESTABLISHED. The line asserts 'memory stays cutoff-set "
    "(tau_c~1/omega_c)' in the context of the ladder / slowest-kernel "
    "timing argument; the cutoff referent is a memory-time scale, not a "
    "named UV regulator symbol.",
    "memory-time cutoff (tau_c ~ 1/omega_c) of the projected dynamics",
    "LEGITIMATE", "exact_source_line",
    "memory stays cutoff-set (tau_c~1/omega_c)")
FRESH[(1, "correlator")] = J("correlator", "SEMANTIC", "LOCALLY_TYPABLE",
    "INFERABLE",
    "LOCALLY ESTABLISHED. The free bath correlator is characterized as "
    "super-Ohmic and collisionless-AT-FREE-LEVEL and is the yield of the "
    "first transport-fork step; it does not by itself decide the fork.",
    "the free bath correlator, first-step yield of the transport fork",
    "LEGITIMATE", "exact_source_line",
    "committing the system/bath partition yields only the FREE bath "
    "correlator (super-Ohmic, collisionless-AT-FREE-LEVEL)")

# ---- S2: Ward-sourced gauge-orbit zero / GR response kernel ------------------
FRESH[(2, "GAUGE")] = J("GAUGE", "SEMANTIC", "LOCALLY_TYPABLE", "UNSPECIFIED",
    "LOCALLY ESTABLISHED. The line names the 4d-covariant availability of "
    "the Ward-sourced gauge-orbit zero (the KC5-reserved covariantization). "
    "The gauge prescription itself is not formally typed.",
    "the Ward-sourced gauge-orbit zero of K_R, on the full 4d gauge orbit",
    "LEGITIMATE", "exact_source_line",
    "THE 4D-COVARIANT AVAILABILITY OF THE WARD-SOURCED GAUGE-ORBIT ZERO")
FRESH[(2, "response kernel")] = J("response kernel", "SEMANTIC",
    "LOCALLY_TYPABLE", "INFERABLE",
    "LOCALLY ESTABLISHED. The line gives the linearized Einstein-Hilbert "
    "response structure (1/2)k^2[P^(2)-2P^(0,s)] and states GR's own "
    "response kernel carries a scalar component twice its spin-2 one.",
    "GR's own response kernel (linearized Einstein-Hilbert), scalar:spin-2 "
    "= 2:1 structure",
    "LEGITIMATE", "exact_source_line",
    "GR's own response kernel carries a scalar component TWICE its spin-2 "
    "one")

# ---- S4: alpha-bridge / projector -------------------------------------------
FRESH[(4, "projector")] = J("projector", "SEMANTIC", "LOCALLY_TYPABLE",
    "INFERABLE",
    "LOCALLY ESTABLISHED. The TT projector P^TT appears as the projector "
    "factor of the TT response kernel K^R = alpha*chi*P^TT and as the "
    "subject of the projector-orthogonality obstruction; no explicit "
    "projector formula is supplied in this statement.",
    "TT projector factor of the TT response kernel; subject of the "
    "projector-orthogonality obstruction",
    "LEGITIMATE", "exact_source_line",
    "K^R = alpha*chi*P^TT")

# ---- S5 / S6 / S14: seven-construction enumerations --------------------------
FRESH[(5, "system/bath")] = T_ENUM("system/bath",
    "**B** system/bath partition",
    "enumerated distinct construction choice (B) in the candidate-mining "
    "registry",
    "NOT ESTABLISHED FROM SUPPLIED EVIDENCE. Named as a distinct enumerated "
    "construction choice; no definition, type, or construction is supplied "
    "on this line.")
FRESH[(5, "Mori-Zwanzig")] = T_ENUM("Mori-Zwanzig",
    "**C** the Mori-Zwanzig projection P",
    "enumerated distinct construction choice (C) in the candidate-mining "
    "registry",
    "NOT ESTABLISHED FROM SUPPLIED EVIDENCE. Named as a distinct enumerated "
    "construction choice; no definition of the projection is supplied.")
FRESH[(5, "projection P")] = T_ENUM("projection P",
    "**C** the Mori-Zwanzig projection P",
    "enumerated distinct construction choice (C) in the candidate-mining "
    "registry",
    "NOT ESTABLISHED FROM SUPPLIED EVIDENCE. Named (P, in the Mori-Zwanzig "
    "construction) but not defined; mathematical type unspecified.")
FRESH[(6, "cutoff")] = T_ENUM("cutoff",
    "**F** cutoff/separation",
    "enumerated distinct construction choice (F) in the candidate-mining "
    "registry",
    "NOT ESTABLISHED FROM SUPPLIED EVIDENCE. Named as a distinct enumerated "
    "construction choice; no cutoff/separation object is defined on this "
    "line.")
FRESH[(6, "inner product")] = J("inner product", "SEMANTIC", "NOT_SPECIFIED",
    "UNSPECIFIED",
    "LOCALLY ESTABLISHED ONLY AS ENUMERATED. The enumeration lists an "
    "inner-product choice (D) and separately 'the state supplying the inner "
    "product' (E) as distinct entries; neither is defined.",
    "enumerated distinct construction choice (D); the state supplying it "
    "enumerated separately (E)",
    "UNRESOLVED", "exact_source_line",
    "**D** inner-product choice")
FRESH[(14, "system/bath")] = T_ENUM("system/bath",
    "system/bath partition",
    "enumerated distinct construction choice in the registry-style list",
    "NOT ESTABLISHED FROM SUPPLIED EVIDENCE. Named in the enumeration "
    "> system/bath partition, the projection P, inner-product choice, the "
    "state supplying it, cutoff; not defined on this line.")
FRESH[(14, "projection P")] = T_ENUM("projection P",
    "the projection P",
    "enumerated distinct construction choice in the registry-style list",
    "NOT ESTABLISHED FROM SUPPLIED EVIDENCE. Named in the enumeration but "
    "not defined on this line.")

# ---- S7: declared inputs / gauge-orbit zero / symmetrized correlator ---------
FRESH[(7, "system/bath")] = J("system/bath", "SEMANTIC", "LOCALLY_TYPABLE",
    "UNSPECIFIED",
    "LOCALLY ESTABLISHED AS A DECLARED INPUT. The line lists '+3 declared "
    "inputs: system/bath split, Gaussian/linear-response truncation, "
    "background Lorentzian causal structure. STANCE, not derivation.' The "
    "split is declared as a construction input; its internal specification "
    "is not given.",
    "declared construction input (stance, not derivation)",
    "LEGITIMATE", "exact_source_line",
    "+3 declared inputs: system/bath split, Gaussian/linear-response "
    "truncation, background Lorentzian causal structure. STANCE, not "
    "derivation.")
FRESH[(7, "GAUGE")] = J("GAUGE", "SEMANTIC", "LOCALLY_TYPABLE", "UNSPECIFIED",
    "LOCALLY ESTABLISHED. The line states that K_R annihilates the FULL 4d "
    "gauge orbit (the Ward-sourced gauge-orbit zero). The gauge "
    "prescription object itself is not formally typed here.",
    "the gauge-orbit zero of K_R (annihilation of the full 4d gauge orbit)",
    "LEGITIMATE", "exact_source_line",
    "that K_R annihilates the FULL 4d gauge orbit")
FRESH[(7, "correlator")] = J("correlator", "SEMANTIC", "LOCALLY_TYPABLE",
    "INFERABLE",
    "LOCALLY ESTABLISHED. The line states the symmetrized correlator of "
    "any genuine state is PSD by construction, in the argument ruling out "
    "constitutive symmetrized correlators.",
    "the symmetrized correlator, ruled out as constitutive (PSD by "
    "construction)",
    "LEGITIMATE", "exact_source_line",
    "the symmetrized correlator of any genuine state is PSD by construction")

# ---- S8: FRW gauge-allowed response space ------------------------------------
FRESH[(8, "gauge")] = J("gauge", "SEMANTIC", "LOCALLY_TYPABLE", "UNSPECIFIED",
    "LOCALLY ESTABLISHED. The line gives the FRW gauge-allowed bilinear "
    "response space as 11-dimensional with two independent constructions, "
    "countersigned. The gauge prescription itself is not formally typed.",
    "the FRW gauge-allowed bilinear response space (11-dimensional, two "
    "independent constructions)",
    "LEGITIMATE", "exact_source_line",
    "the FRW gauge-allowed bilinear response space is 11-dimensional (two "
    "independent constructions, countersigned)")

# ---- S9: vacuum susceptibility falsifier --------------------------------------
FRESH[(9, "susceptibility")] = J("susceptibility", "SEMANTIC",
    "LOCALLY_TYPABLE", "INFERABLE",
    "LOCALLY ESTABLISHED. The line names 'the vacuum susceptibility' as the "
    "object whose possible second dynamical scale (e.g. J~omega^3/(1+omega^2 "
    "tau^2) or an internal resonance/diffusive mode) is the remaining "
    "falsifier. Its construction is not defined on this line.",
    "the vacuum susceptibility whose second dynamical scale would be the "
    "remaining falsifier",
    "LEGITIMATE", "exact_source_line",
    "if the vacuum susceptibility contains a second dynamical scale")

# ---- S10: KUBO / Mori-Zwanzig conventional pairing ----------------------------
FRESH[(10, "KUBO")] = J("KUBO", "SEMANTIC", "LOCALLY_TYPABLE", "INFERABLE",
    "LOCALLY ESTABLISHED. The line states the Mori-Zwanzig projection "
    "conventionally uses the KUBO-MORI inner product; the convention is "
    "named, not formally defined here.",
    "Kubo-Mori as the conventional inner product of the Mori-Zwanzig "
    "projection",
    "LEGITIMATE", "exact_source_line",
    "conventionally uses the KUBO-MORI")
FRESH[(10, "Mori-Zwanzig")] = J("Mori-Zwanzig", "SEMANTIC", "LOCALLY_TYPABLE",
    "UNSPECIFIED",
    "LOCALLY ESTABLISHED. The Mori-Zwanzig projection is named with its "
    "conventional (Kubo-Mori) inner product pairing; the projection object "
    "is not formally defined on this line.",
    "the Mori-Zwanzig projection whose conventional inner product is "
    "Kubo-Mori",
    "LEGITIMATE", "exact_source_line",
    "Mori-Zwanzig projection for a quantum system conventionally uses the "
    "KUBO-MORI")

# ---- S11: projector annihilating trace mode / gauge CONTESTED / Green fn ------
FRESH[(11, "projector")] = J("projector", "SEMANTIC", "LOCALLY_TYPABLE",
    "INFERABLE",
    "LOCALLY ESTABLISHED. The line defines a tracefree projector P^TT that "
    "annihilates exactly the trace mode (the double-trace eta.eta.P^TT is "
    "identically zero); no explicit projector formula is supplied here.",
    "tracefree projector P^TT annihilating exactly the trace mode",
    "LEGITIMATE", "exact_source_line",
    "a tracefree projector P^TT that annihilates exactly that mode")
FRESH[(11, "gauge")] = J("gauge", "SEMANTIC", "NOT_SPECIFIED", "UNSPECIFIED",
    "The line leans 'gauge=harmless/stable' for the <T_ab T_cd> two-point "
    "and the critic flagged the synthesis for that lean; the gauge treatment "
    "is recorded as CONTESTED. No gauge object is defined on this line.",
    "gauge-invariance status of the <T_ab T_cd> two-point (recorded "
    "CONTESTED)",
    "UNRESOLVED", "exact_source_line",
    "leaning 'gauge=harmless/stable' -- so recorded as CONTESTED")
FRESH[(11, "Green's function")] = J("Green's function", "SEMANTIC",
    "LOCALLY_TYPABLE", "INFERABLE",
    "LOCALLY ESTABLISHED. The line poses the remaining open computation as "
    "whether the Delta_4 inverse on de Sitter admits a STABLE late-time "
    "Green's function without secular blow-up; a stability question, not a "
    "construction.",
    "late-time Green's function of the Delta_4 inverse on de Sitter "
    "(stability question, uncomputed)",
    "LEGITIMATE", "exact_source_line",
    "a STABLE late-time Green's function without SECULAR BLOW-UP")

# ---- S12 / S13: D3(iii) gauge prescription OWNER-DECLARED UNDERDEFINED --------
FRESH[(12, "gauge")] = J("gauge", "SEMANTIC", "EXPLICITLY_UNRESOLVED",
    "UNSPECIFIED",
    "EXPLICITLY UNRESOLVED BY THE SOURCE. The line states that the TT-bath "
    "declaration does not establish that the TT-bath declaration is the "
    "unique admissible gauge choice; D3(iii), the graviton-bath "
    "state/gauge prescription, is OWNER-DECLARED and UNDERDEFINED.",
    "D3(iii): the graviton-bath state / gauge prescription, owner-declared "
    "and underdefined",
    "UNRESOLVED", "exact_source_line",
    "OWNER-DECLARED and UNDERDEFINED")
FRESH[(13, "gauge")] = J("gauge", "SEMANTIC", "EXPLICITLY_UNRESOLVED",
    "UNSPECIFIED",
    "EXPLICITLY UNRESOLVED BY THE SOURCE (duplicate statement of S12). The "
    "TT-bath gauge prescription D3(iii) is OWNER-DECLARED and UNDERDEFINED.",
    "D3(iii): the graviton-bath state / gauge prescription, owner-declared "
    "and underdefined",
    "UNRESOLVED", "exact_source_line",
    "OWNER-DECLARED and UNDERDEFINED")

# ---- S15: constitutive equivalence class --------------------------------------
FRESH[(15, "response function")] = J("response function", "SEMANTIC",
    "LOCALLY_TYPABLE", "UNSPECIFIED",
    "LOCALLY ESTABLISHED. The line defines 'constitutive organization' "
    "(glossary, provisional/revisable per u0) as the equivalence class of "
    "response functionals chi(omega,k) producing identical observable "
    "transport under admissible coarse-grainings.",
    "response functionals chi(omega,k) in the equivalence-class definition "
    "of constitutive organization",
    "LEGITIMATE", "exact_source_line",
    "the equivalence class of response functionals chi(omega,k) producing "
    "identical observable transport under admissible coarse-grainings")

# ---- S17: u6 coarse-graining conditional ---------------------------------------
FRESH[(17, "coarse-grain")] = J("coarse-grain", "SEMANTIC", "NOT_SPECIFIED",
    "UNSPECIFIED",
    "The line names u6's already-held coarse-graining/slow-variable "
    "conditional (staying LIVE and un-discharged); the coarse-graining "
    "operation itself is not defined on this line.",
    "u6 conditional on coarse-graining/slow-variable selection (held, "
    "un-discharged)",
    "UNRESOLVED", "exact_source_line",
    "u6's already-held coarse-graining/slow-variable conditional")

# ---- S19: synchronous / gauge-unfixed equivalence ------------------------------
FRESH[(19, "gauge")] = J("gauge", "SEMANTIC", "LOCALLY_TYPABLE", "UNSPECIFIED",
    "LOCALLY ESTABLISHED. The line gives A4 PASS: the synchronous-gauge "
    "computation reproduces the gauge-invariant content of the "
    "gauge-unfixed computation; the transformation to synchronous exists "
    "with residual family zeta^0 = C(x)/a, zeta_i = C_i.",
    "gauge-equivalence verdict between the synchronous-gauge and "
    "gauge-unfixed computations",
    "LEGITIMATE", "exact_source_line",
    "the synchronous-gauge computation reproduces the gauge-invariant "
    "content of the gauge-unfixed computation")

# ---- S20: print block, conventional pairing ------------------------------------
FRESH[(20, "Mori-Zwanzig")] = J("Mori-Zwanzig", "SEMANTIC", "LOCALLY_TYPABLE",
    "UNSPECIFIED",
    "LOCALLY ESTABLISHED (print block). The statement says the Mori-Zwanzig "
    "projection conventionally uses the KUBO-MORI correlation; the pairing "
    "is stated, not formally defined.",
    "the Mori-Zwanzig projection with its conventional Kubo-Mori "
    "correlation/inner product",
    "LEGITIMATE", "exact_source_line",
    "the Mori-Zwanzig projection conventionally uses the KUBO-MORI "
    "correlation")

# ---- S21: truncated print fragment ----------------------------------------------
FRESH[(21, "Mori-Zwanzig")] = J("Mori-Zwanzig", "SEMANTIC", "NOT_SPECIFIED",
    "UNSPECIFIED",
    "The mention occurs as a truncated print-block fragment (\"rung3's "
    "'Mori-Zwanzig\"); the frozen evidence does not establish which "
    "Mori-Zwanzig object is meant. The phrase is ambiguous in the supplied "
    "evidence.",
    "none established on this line (truncated fragment)",
    "UNRESOLVED", "exact_source_line",
    "rung3's 'Mori-Zwanzig")

# ---- S22: comoving gauge / trace-correlator route --------------------------------
FRESH[(22, "gauge")] = J("gauge", "SEMANTIC", "NOT_SPECIFIED", "UNSPECIFIED",
    "The line invokes comoving-gauge identification as gauge-choice "
    "terminology in the ISW/delta^0 computation context; no gauge object is "
    "defined on this line.",
    "gauge choice terminology (comoving gauge) in the ISW context",
    "UNRESOLVED", "exact_source_line",
    "comoving-gauge identification")
FRESH[(22, "correlator")] = J("correlator", "SEMANTIC", "LOCALLY_TYPABLE",
    "INFERABLE",
    "LOCALLY ESTABLISHED. The line names the rung3 trace-correlator route "
    "(ONLY) as the pending derivation route whose taking would cost a new "
    "+1 (relocation, not discharge).",
    "the rung3 trace-correlator route (named, un-taken derivation route)",
    "LEGITIMATE", "exact_source_line",
    "the rung3 trace-correlator route ONLY")

# ---- S23: Wilsonian coarse-graining motif ----------------------------------------
FRESH[(23, "coarse-grain")] = J("coarse-grain", "SEMANTIC", "LOCALLY_TYPABLE",
    "INFERABLE",
    "LOCALLY ESTABLISHED. The line states renormalization/coarse-graining "
    "is an information-projection and that Wilsonian coarse-graining as "
    "information loss is the Wilson motif -- explicitly a generic motif, "
    "NOT uniquely GRUT.",
    "Wilsonian coarse-graining as information loss (generic motif, "
    "explicitly not uniquely GRUT)",
    "LEGITIMATE", "exact_source_line",
    "renormalization/coarse-graining is an information-projection")

# ---- S24 / S25 / S26: rejected 'pure gauge by inspection' label -------------------
for _i in (24, 25, 26):
    FRESH[(_i, "gauge")] = J("gauge", "SEMANTIC", "NOT_SPECIFIED", "UNSPECIFIED",
        "The term 'gauge' occurs on this line only inside the explicitly "
        "REJECTED classification phrase 'pure gauge by inspection'; no "
        "gauge object is defined and none is constructed here.",
        "none established on this line (rejected classification phrase "
        "'pure gauge by inspection')",
        "UNRESOLVED", "exact_source_line",
        "not 'pure gauge by inspection', not an EOM cancellation")

# ---- S27 / S28: MZ ordering claim (print + markdown forms) ------------------------
FRESH[(27, "Mori-Zwanzig")] = J("Mori-Zwanzig", "SEMANTIC", "LOCALLY_TYPABLE",
    "INFERABLE",
    "LOCALLY ESTABLISHED. The statement states the MZ ordering claim: "
    "choosing a projector P IS the partition (coarse-graining -> split).",
    "the MZ ordering claim: projector choice P is the partition "
    "(coarse-graining -> split)",
    "LEGITIMATE", "exact_source_line",
    "Mori-Zwanzig: choosing a projector P IS the partition (coarse-graining "
    "-> split)")
FRESH[(28, "projector")] = J("projector", "SEMANTIC", "LOCALLY_TYPABLE",
    "INFERABLE",
    "LOCALLY ESTABLISHED. The markdown statement states the same MZ "
    "ordering claim: choosing the projector P *is* the partition "
    "(coarse-graining -> split).",
    "the projector P, whose choice IS the partition per the MZ ordering "
    "claim",
    "LEGITIMATE", "exact_source_line",
    "choosing the projector **P** *is* the partition")
FRESH[(28, "Mori-Zwanzig")] = J("Mori-Zwanzig", "SEMANTIC", "LOCALLY_TYPABLE",
    "INFERABLE",
    "LOCALLY ESTABLISHED (markdown form of the S27 claim). The statement "
    "states: Mori-Zwanzig -- choosing the projector P *is* the partition.",
    "the MZ ordering claim (markdown form): projector choice is the "
    "partition",
    "LEGITIMATE", "exact_source_line",
    "**Mori-Zwanzig:** choosing the projector **P** *is* the partition")

# ---- S29: conventional MZ inner product / no ladder --------------------------------
FRESH[(29, "inner product")] = J("inner product", "SEMANTIC", "LOCALLY_TYPABLE",
    "INFERABLE",
    "LOCALLY ESTABLISHED (print block). The statement says: on the "
    "CONVENTIONAL Mori-Zwanzig inner product there is no ladder to inherit "
    "(rung3 adverse reading).",
    "the conventional Mori-Zwanzig inner product, on which no ladder is "
    "inherited",
    "LEGITIMATE", "exact_source_line",
    "Mori-Zwanzig inner product there is no ladder to inherit")
FRESH[(29, "Mori-Zwanzig")] = J("Mori-Zwanzig", "SEMANTIC", "LOCALLY_TYPABLE",
    "INFERABLE",
    "LOCALLY ESTABLISHED (print block). The mention is the conventional "
    "Mori-Zwanzig inner product pairing in the rung3 adverse reading.",
    "the conventional Mori-Zwanzig inner product (no ladder to inherit)",
    "LEGITIMATE", "exact_source_line",
    "Mori-Zwanzig inner product there is no ladder to inherit")

print("FRESH entries defined:", len(FRESH))
assert len(FRESH) == 43, "FRESH table must have exactly 43 entries"


# ============================================================ DRIVER

def main():
    h_frozen_b, h_orig_b, h_audit_b = sha(FROZEN), sha(ORIG), sha(AUDIT)
    frozen = json.loads(FROZEN.read_text())
    audit = json.loads(AUDIT.read_text())
    orig = json.loads(ORIG.read_text())
    stmts = frozen["statements"]

    # ---- mechanical repair population ------------------------------------
    fails, passes = {}, {}
    for r in audit["results"]:
        key = (r["statement_index"], r["candidate_term"])
        (passes if r["failure_class"].startswith("PASS") else fails)[key] = r
    assert len(passes) == 19, "expected 19 passes, got %d" % len(passes)
    assert len(fails) == 43, "expected 43 failures, got %d" % len(fails)

    # ---- original adjudication lookup ------------------------------------
    orig_by = {}
    for rec in orig["adjudication_records"]:
        for a in rec["adjudications"]:
            orig_by[(rec["statement_index"], a["candidate_term"])] = a

    # ---- build repaired records -------------------------------------------
    out_records, errors = [], []
    change_counts = {}
    for (si, term), fr in sorted(FRESH.items()):
        if (si, term) not in fails:
            errors.append("FRESH key not in failure set: %r" % ((si, term),))
            continue
        st = stmts[si]
        line = st["exact_source_line"]
        bcw = st["bounded_context_window"]
        kind = fr.get("evidence_scope") or fr.get("kind")
        quote = fr.get("evidence_quote")
        if kind is None and quote is None:
            kind, quote = fr.get("kind"), fr.get("quote")
        quote = quote if quote is not None else fr.get("quote")

        # runtime exact containment validation (no normalization)
        if kind == "exact_source_line":
            ok = quote in line
        elif kind == "bounded_context_window":
            ok = term in bcw and quote in bcw[term]
        else:  # 'absent'
            ok = (term.lower() not in line.lower()
                  and not (term in bcw and term.lower() in bcw[term].lower()))
        if not ok:
            errors.append("CONTAINMENT FAIL: (%d, %r) kind=%s quote=%r"
                          % (si, term, kind, (quote or "")[:120]))
            continue

        orig_a = orig_by.get((si, term), {})
        if kind == "absent":
            ev_ref = ("supported absence: candidate term does not occur in "
                      "frozen exact_source_line or bounded_context_window")
            ev_text = None
            change = "JUDGMENT_CHANGED" if orig_a.get(
                "referent_status") != "NOT_SPECIFIED" else "SAME_JUDGMENT_RE_GROUNDED"
        else:
            ev_ref = "%s: '%s'" % (kind, quote)
            ev_text = (st["exact_source_line"] if kind == "exact_source_line"
                       else bcw.get(term, ""))
            if (fr["typing_level"], fr["referent_status"],
                    fr["mathematical_type"], fr["comparison_status"]) == (
                    orig_a.get("typing_level"), orig_a.get("referent_status"),
                    orig_a.get("mathematical_type"),
                    orig_a.get("comparison_status")):
                change = "SAME_JUDGMENT_RE_GROUNDED"
            elif fr["referent_status"] in ("NOT_SPECIFIED",
                                           "EXPLICITLY_UNRESOLVED") and \
                    orig_a.get("referent_status") in ("EXPLICITLY_TYPED",
                                                      "LOCALLY_TYPABLE"):
                change = "NEWLY_UNRESOLVED"
            else:
                change = "JUDGMENT_CHANGED"

        rec = {
            "statement_index": si,
            "candidate_term": term,
            "original_containment_failure": fails[(si, term)]["failure_class"],
            "original_adjudication_metadata": {
                "status": "PRIOR_QUARANTINED_OUTPUT / NOT_EVIDENCE",
                "typing_level": orig_a.get("typing_level"),
                "referent_status": orig_a.get("referent_status"),
            },
            "repaired_typing_level": fr["typing_level"],
            "repaired_referent_status": fr["referent_status"],
            "repaired_mathematical_type": fr["mathematical_type"],
            "repaired_referent_description": fr["referent_description"],
            "repaired_physical_role": fr["physical_role"],
            "repaired_comparison_status": fr["comparison_status"],
            "repaired_evidence_scope": kind,
            "repaired_evidence_text": quote if kind != "absent" else None,
            "repaired_evidence_reference": ev_ref,
            "source_path": st.get("source_path"),
            "source_line": st.get("source_line"),
            "exact_source_line": st.get("exact_source_line"),
            "provenance": st.get("provenance"),
            "repair_rationale": (
                "Fresh statement-level adjudication grounded solely in the "
                "frozen exact_source_line/bounded_context_window; citation "
                "validated by exact byte containment."),
            "adjudication_change_status": change,
        }
        change_counts[change] = change_counts.get(change, 0) + 1
        out_records.append(rec)

    if errors:
        print("VALIDATION FAILURES — no artifact written:")
        for e in errors:
            print(" ", e)
        return 1

    # ---- integrity ----------------------------------------------------------
    integ = {
        "frozen_sha256_before": h_frozen_b, "frozen_sha256_after": sha(FROZEN),
        "orig_sha256_before": h_orig_b, "orig_sha256_after": sha(ORIG),
        "audit_sha256_before": h_audit_b, "audit_sha256_after": sha(AUDIT),
        "failed_occurrences_processed": len(out_records),
        "passing_occurrences_untouched": len(passes),
        "total_occurrences": len(passes) + len(out_records),
    }
    ok = (integ["frozen_sha256_before"] == integ["frozen_sha256_after"]
          and integ["orig_sha256_before"] == integ["orig_sha256_after"]
          and integ["audit_sha256_before"] == integ["audit_sha256_after"]
          and integ["total_occurrences"] == 62)

    doc = {
        "artifact": "HISA01_REPAIRED_43_ADJUDICATION",
        "repair_population_rule": "mechanically derived from HISA01_EVIDENCE_CONTAINMENT_AUDIT.json (all non-PASS outcomes)",
        "counts": {"verified_before": 19, "repaired": 43, "total": 62},
        "change_status_counts": change_counts,
        "integrity": integ,
        "records": out_records,
    }
    OUT.write_text(json.dumps(doc, indent=2))

    md = ["# HISA-01 — Repaired / Re-adjudicated 43 Occurrences", "",
          "Repair population derived mechanically from the containment audit.",
          "19 passing occurrences untouched. 43 fresh adjudications, each",
          "validated by exact byte containment against the frozen package.",
          "", "## Accounting", "",
          "| population | count |", "|---|---|",
          "| verified before (PASS_*) | 19 |", "| repaired / re-adjudicated | 43 |",
          "| total | 62 |", "", "## Change status", "", "| status | count |",
          "|---|---|"]
    for k, v in sorted(change_counts.items()):
        md.append("| %s | %d |" % (k, v))
    md += ["", "## Repaired records", ""]
    for r in out_records:
        md.append("**stmt %s — `%s`** (%s)\n- original: %s\n- repaired: %s / %s / %s / %s\n- evidence (%s): %s\n- %s\n" % (
            r["statement_index"], r["candidate_term"],
            r["adjudication_change_status"],
            r["original_containment_failure"],
            r["repaired_typing_level"], r["repaired_referent_status"],
            r["repaired_mathematical_type"], r["repaired_comparison_status"],
            r["repaired_evidence_scope"],
            (r["repaired_evidence_reference"] or "")[:200],
            r["repaired_referent_description"][:400]))
    MD.write_text("\n".join(md) + "\n")

    print(json.dumps({"repaired": len(out_records),
                      "change_status": change_counts,
                      "integrity_ok": ok}, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
