#!/usr/bin/env python3
"""HISA-01 independent statement-level semantic referent adjudication.

Unit of adjudication: ONE frozen statement, per candidate term occurrence:
    mention -> referent -> type.

Inputs used for adjudication: exact_quote, bounded_context_window,
candidate_term, source_path, source_line, provenance -- from the frozen
package ONLY.

Prior machine output appears solely as contamination metadata and NEVER
determines any adjudication value. There is no prior-classification ->
new-classification mapping in this file.

Permitted values only:
  typing_level:      SYNTACTIC SEMANTIC INTERPRETIVE NONE
  referent_status:   EXPLICITLY_TYPED LOCALLY_TYPABLE EXPLICITLY_UNRESOLVED
                     NOT_SPECIFIED CONFLICTING_REFERENTS
  mathematical_type: EXPLICIT INFERABLE UNSPECIFIED
  comparison_status: LEGITIMATE NOT_LEGITIMATE UNRESOLVED NOT_COMPARABLE
"""
import json, hashlib, os, re

HERE = os.path.dirname(os.path.abspath(__file__))
FROZEN = os.path.join(HERE, "HISA01_FROZEN_EVIDENCE_PACKAGE.json")
OUT = os.path.join(HERE, "HISA01_INDEPENDENT_SEMANTIC_ADJUDICATION.json")

CONTAMINATION_WARNING = (
    "Prior machine pair classifications (SAME_CONSTRUCTION/DISTINCT_CONSTRUCTION "
    "etc.) exist in the failed prior artifact HISA01_INDEPENDENT_ADJUDICATION.json, "
    "which is QUARANTINED as an INVALID_PROTOCOL_ATTEMPT. They were NOT read as "
    "inputs to any adjudication decision here and appear only as contamination "
    "metadata."
)


def A(t, tl, rs, rd, mt, role, cs, ev):
    """One term-occurrence adjudication."""
    return {
        "candidate_term": t,
        "typing_level": tl,
        "referent_status": rs,
        "referent_description": rd,
        "mathematical_type": mt,
        "physical_role_established": role,
        "comparison_status": cs,
        "evidence_reference": ev,
    }


# Hand adjudications: statement_index -> list of term adjudications.
# Every decision below was made reading ONLY the frozen exact_source_line and
# bounded_context_window for that statement.
ADJ = {}

ADJ[0] = [
 A("system/bath","SEMANTIC","NOT_SPECIFIED",
   "NOT ESTABLISHED FROM SUPPLIED EVIDENCE. The line presupposes 'the standard QBM "
   "construction' but does not define any particular partition or its objects.",
   "UNSPECIFIED","none beyond a presupposed construction ingredient","UNRESOLVED",
   "exact_source_line: 'the confirmation holds for the standard QBM construction with a smooth UV cutoff + bilinear coupling'"),
 A("UV cutoff","SEMANTIC","LOCALLY_TYPABLE",
   "An unspecified smooth ultraviolet regulator of the bath in the standard QBM "
   "construction, per the line. No scale symbol (Lambda_UV, mu_RG, ...) is named; "
   "the evidence establishes only smoothness and QBM role.",
   "UNSPECIFIED","UV regulator of the bath correlator in the standard QBM construction","UNRESOLVED",
   "exact_source_line: 'the standard QBM construction with a smooth UV cutoff + bilinear coupling'"),
 A("gauge","SEMANTIC","NOT_SPECIFIED",
   "NOT ESTABLISHED FROM SUPPLIED EVIDENCE. 'gauge' occurs in the bounded context "
   "metadata only; the line defines no gauge object or transformation.",
   "UNSPECIFIED","none established","UNRESOLVED",
   "bounded_context_window only; absent from exact_source_line definition"),
]

ADJ[1] = [
 A("system/bath","SEMANTIC","NOT_SPECIFIED",
   "Named as a missing input ('committing the system/bath partition') whose "
   "commitment is not yet made; the line does not define the partition itself.",
   "UNSPECIFIED","a to-be-committed input of the transport fork","UNRESOLVED",
   "exact_source_line: '(1) committing the system/bath partition yields only the FREE bath correlator'"),
 A("Mori-Zwanzig","SEMANTIC","NOT_SPECIFIED",
   "NOT ESTABLISHED FROM SUPPLIED EVIDENCE. The term appears in context fields; "
   "this line does not define any Mori-Zwanzig object.",
   "UNSPECIFIED","none established on this line","UNRESOLVED",
   "bounded_context_window only"),
 A("inner product","SEMANTIC","NOT_SPECIFIED",
   "NOT ESTABLISHED FROM SUPPLIED EVIDENCE. No inner product is defined or chosen "
   "on this line.",
   "UNSPECIFIED","none established on this line","UNRESOLVED",
   "bounded_context_window only"),
 A("cutoff","SEMANTIC","NOT_SPECIFIED",
   "NOT ESTABLISHED FROM SUPPLIED EVIDENCE. This line names no cutoff; context "
   "mentions a collisional construction without defining a scale.",
   "UNSPECIFIED","none established on this line","UNRESOLVED",
   "bounded_context_window only"),
 A("correlator","SEMANTIC","LOCALLY_TYPABLE",
   "The FREE bath correlator: explicitly characterized as super-Ohmic and "
   "collisionless at free level, with G_R = 1/(G0^-1 - Sigma) and Sigma the "
   "transport self-energy named in the same line.",
   "INFERABLE","the free bath correlator C supplying G0 in the two-level transport fork","LEGITIMATE",
   "exact_source_line: 'the FREE bath correlator (super-Ohmic, collisionless-AT-FREE-LEVEL) ... the TRANSPORT SELF-ENERGY Sigma controlling G_R = 1/(G0^-1 - Sigma)'"),
]

ADJ[2] = [
 A("GAUGE","SEMANTIC","LOCALLY_TYPABLE",
   "The gauge/diffeomorphism-invariance constraint question: the line records that "
   "the forced-vs-chosen interrogation was run, adversarially verified, and "
   "returned VERDICT = CHOSEN (the TT projector is a choice, not a derivation).",
   "UNSPECIFIED","the diffeomorphism-invariance constraint under interrogation; verdict CHOSEN","LEGITIMATE",
   "exact_source_line: 'INTERROGATION RESULT 2026-08-02 ... VERDICT = CHOSEN, unanimous. THE PHYSICS IN ONE LINE: diffeomorphism invariance gets you to TRANSVERSE'"),
 A("response kernel","SEMANTIC","EXPLICITLY_TYPED",
   "The vacuum response kernel, explicitly given in the supplied evidence as "
   "K^R = alpha*chi(omega)*P^TT with the projector P^TT chosen (not derived).",
   "EXPLICIT","vacuum response kernel K^R = alpha*chi(omega)*P^TT; structural input of the mu_linear no-go export","LEGITIMATE",
   "bounded_context_window ('statement' field): 'K^R = alpha*chi(omega)*P^TT, with the projector P^TT chosen (not derived)'"),
]

ADJ[3] = [
 A("susceptibility","SEMANTIC","NOT_SPECIFIED",
   "NOT ESTABLISHED FROM SUPPLIED EVIDENCE. 'chi' is named generically as an "
   "example of constitutive response; no specific susceptibility object is defined.",
   "UNSPECIFIED","illustrative constitutive-form ingredient only","UNRESOLVED",
   "exact_source_line: 'a susceptibility chi, memory, linear response'"),
 A("coarse-grain","SEMANTIC","NOT_SPECIFIED",
   "NOT ESTABLISHED FROM SUPPLIED EVIDENCE. Presupposed ('GIVEN coarse-graining') "
   "as the input of the U4 question; not defined on this line.",
   "UNSPECIFIED","presupposed input of the U4/Frontier-3 question","UNRESOLVED",
   "exact_source_line: 'GIVEN coarse-graining, WHY does the effective description take a RESPONSE / constitutive form'"),
 A("scale separation","SEMANTIC","NOT_SPECIFIED",
   "NOT ESTABLISHED FROM SUPPLIED EVIDENCE. 'timescale separation' appears only as "
   "one of U1's presupposed constitutive conditions; no separation object is defined.",
   "UNSPECIFIED","one of the presupposed conditions U1 takes as given","UNRESOLVED",
   "exact_source_line: 'which PRESUPPOSES the constitutive conditions (weak coupling / Gaussianity / near-equilibrium / timescale separation)'"),
]

ADJ[4] = [
 A("projector","SEMANTIC","LOCALLY_TYPABLE",
   "The TT projector P^TT appearing in the alpha-bridge kernel K^R = "
   "alpha*chi*P^TT, named in the same evidence; the projector-orthogonality "
   "mechanism is also named. No explicit projector formula is given here.",
   "INFERABLE","TT projector factor of the TT response kernel; subject of the projector-orthogonality obstruction","LEGITIMATE",
   "bounded_context_window: 'K^R = alpha*chi*P^TT ... Structural obstruction (projector-orthogonality PRIMARY / Ward / UV-IR no-RG-protection)'"),
 A("response kernel","SEMANTIC","EXPLICITLY_TYPED",
   "The TT response kernel K^R = alpha*chi*P^TT, explicitly typed in the supplied "
   "evidence as an adopted phenomenological DC normalization target.",
   "EXPLICIT","K^R = alpha*chi*P^TT; the object whose DC normalization c_0 = alpha is adopted","LEGITIMATE",
   "bounded_context_window: 'the TT response kernel (K^R = alpha*chi*P^TT)'"),
]

ADJ[5] = [
 A("projection P","SYNTACTIC","NOT_SPECIFIED",
   "A named construction choice ('C the Mori-Zwanzig projection P') in an "
   "enumeration of distinct choices; the line defines no P.",
   "UNSPECIFIED","a named decision axis; object undefined on this line","UNRESOLVED",
      "exact_source_line: 'B system/bath partition · C the Mori-Zwanzig projection P'"),
   A("Mori-Zwanzig","SYNTACTIC","NOT_SPECIFIED",
     "A named construction choice ('the Mori-Zwanzig projection P'); the line "
     "defines no projection object, projector map, or inner product.",
     "UNSPECIFIED","none established on this line","UNRESOLVED",
     "exact_source_line: 'B system/bath partition · C the Mori-Zwanzig projection P'"),
   A("system/bath","SYNTACTIC","NOT_SPECIFIED",
   "A named construction choice ('B system/bath partition'); the line defines no "
   "partition.",
   "UNSPECIFIED","a named decision axis; object undefined on this line","UNRESOLVED",
   "exact_source_line: 'B system/bath partition'"),
]

ADJ[6] = [
 A("cutoff","SYNTACTIC","NOT_SPECIFIED",
   "A named construction choice ('F cutoff/separation scale'); no scale is defined "
   "on this line. No Lambda_UV/mu_RG symbol is established.",
   "UNSPECIFIED","a named decision axis; object undefined on this line","UNRESOLVED",
   "exact_source_line: 'F cutoff/separation scale'"),
 A("inner product","SYNTACTIC","NOT_SPECIFIED",
   "A named construction choice ('D inner-product choice'); not defined on this line.",
   "UNSPECIFIED","a named decision axis; object undefined on this line","UNRESOLVED",
   "exact_source_line: 'D inner-product choice'"),
]

ADJ[7] = [
 A("system/bath","SEMANTIC","NOT_SPECIFIED",
   "The system/bath split is named as a DECLARED INPUT ('STANCE, not derivation'); "
   "the line does not define the partition's objects.",
   "UNSPECIFIED","a declared stance-level input, not derived","UNRESOLVED",
   "exact_source_line: 'declared inputs: system/bath split ... STANCE, not derivation'"),
 A("GAUGE","SEMANTIC","NOT_SPECIFIED",
   "NOT ESTABLISHED FROM SUPPLIED EVIDENCE. Occurs in context fields; the line "
   "defines no gauge object.",
   "UNSPECIFIED","none established on this line","UNRESOLVED",
   "bounded_context_window only"),
 A("correlator","SEMANTIC","NOT_SPECIFIED",
   "NOT ESTABLISHED FROM SUPPLIED EVIDENCE. Context lists correlation-structure "
   "assumptions without defining a specific correlator object on this line.",
   "UNSPECIFIED","none established on this line","UNRESOLVED",
   "bounded_context_window only"),
]

ADJ[8] = [
 A("response kernel","SEMANTIC","LOCALLY_TYPABLE",
   "The vacuum response kernel, characterized on this line as belonging to the "
   "Lorentz-covariant subspace identified by the flat-limit membership test.",
   "INFERABLE","the vacuum response kernel; family membership priced by the ruling","LEGITIMATE",
   "exact_source_line: 'the vacuum response kernel itself belongs to the Lorentz-covariant subspace identified by the flat-limit membership test -- NOT that the background is Lorentz invariant'"),
 A("gauge","SEMANTIC","LOCALLY_TYPABLE",
   "The gauge/orbit constraint level of the response kernel: the line states the "
   "kernel belongs to the Lorentz-covariant subspace identified by the flat-limit "
   "membership test and explicitly fences this from background Lorentz invariance.",
   "INFERABLE","constraint level characterizing the response kernel's symmetry family","LEGITIMATE",
   "exact_source_line as above"),
]

ADJ[9] = [
 A("susceptibility","SEMANTIC","LOCALLY_TYPABLE",
   "The vacuum susceptibility, with its falsifier condition supplied: a second "
   "dynamical scale (e.g. J~omega^3/(1+omega^2 tau^2), or an internal "
   "resonance/diffusive mode) would produce a second slow pole.",
   "INFERABLE","vacuum noise/response spectrum whose pole structure is the short-memory falsifier","LEGITIMATE",
   "exact_source_line: 'if the vacuum susceptibility contains a second dynamical scale (e.g. J~omega^3/(1+omega^2 tau^2) ...), a second slow pole appears and short-memory breaks'"),
 A("Mori-Zwanzig","SEMANTIC","NOT_SPECIFIED",
   "The line names a step 'it does NOT take': a Mori-Zwanzig projection step is "
   "referenced but no MZ object (projection, inner product) is defined here.",
   "UNSPECIFIED","a not-taken step; object undefined on this line","UNRESOLVED",
   "exact_source_line: 'The falsifying step it does NOT take is Mori-Zwanzig i'"),
]

ADJ[10] = [
 A("KUBO","SEMANTIC","EXPLICITLY_TYPED",
   "Kubo-Mori: the line explicitly states the conventional MZ inner product for a "
   "quantum system is the KUBO-MORI (canonical) inner product, and the Kubo "
   "correlation function carries the ladder.",
   "UNSPECIFIED","defines the conventional inner-product choice for the MZ projection and the ladder carrier","LEGITIMATE",
   "exact_source_line: 'Mori-Zwanzig projection for a quantum system conventionally uses the KUBO-MORI (canonical) inner product, and the Kubo correlation function carries'"),
 A("Mori-Zwanzig","SEMANTIC","EXPLICITLY_TYPED",
   "The Mori-Zwanzig projection whose conventional inner product the line "
   "explicitly fixes as Kubo-Mori (canonical).",
   "UNSPECIFIED","the projection operator whose conventional inner product is fixed","LEGITIMATE",
   "exact_source_line as above"),
]

ADJ[11] = [
 A("projector","SEMANTIC","NOT_SPECIFIED",
   "NOT ESTABLISHED FROM SUPPLIED EVIDENCE. The line concerns the anomaly "
   "coefficient (Wess-Zumino/Komargodski-Schwimmer, cohomological/one-loop-exact); "
   "candidate terms occur only in context metadata.",
   "UNSPECIFIED","none established on this line","UNRESOLVED",
   "bounded_context_window only; exact_source_line is about the a/b'/alpha anomaly coefficient"),
 A("gauge","SEMANTIC","NOT_SPECIFIED",
   "NOT ESTABLISHED FROM SUPPLIED EVIDENCE (context-only occurrence).",
   "UNSPECIFIED","none established on this line","UNRESOLVED",
   "bounded_context_window only"),
 A("Green's function","SEMANTIC","NOT_SPECIFIED",
   "NOT ESTABLISHED FROM SUPPLIED EVIDENCE (context-only occurrence).",
   "UNSPECIFIED","none established on this line","UNRESOLVED",
   "bounded_context_window only"),
]

ADJ[12] = [
 A("gauge","SEMANTIC","LOCALLY_TYPABLE",
   "The gauge image inserted by the D4-C Part-2 test, which the record says was "
   "inserted WITHOUT the bath projector the loop actually applies.",
   "UNSPECIFIED","the inserted gauge transformation of the D4-C Part-2 test","LEGITIMATE",
   "exact_source_line: 'inserted the gauge image WITHOUT the bath projector the loop actually applies'"),
]

ADJ[13] = [
 A("gauge","SEMANTIC","LOCALLY_TYPABLE",
   "The internal-line gauge transformation within the declared TT bath: the line "
   "states moving it moves no TT amplitude, and explicitly fences the result from "
   "the D3(iii) gauge-prescription question.",
   "UNSPECIFIED","internal-line gauge transformation; invariance result explicitly scoped","LEGITIMATE",
   "exact_source_line: 'gauge-transforming the internal line moves no TT amplitude ... does NOT establish that the TT-bath DECLARATION itself is the unique admissible gauge choice -- that is D3(iii)'"),
]

ADJ[14] = [
 A("cutoff","SYNTACTIC","NOT_SPECIFIED",
   "A named construction choice in the enumeration line ('cutoff'); no scale, "
   "symbol, or object is defined.",
   "UNSPECIFIED","a named decision axis; object undefined on this line","UNRESOLVED",
   "exact_source_line: 'system/bath partition, the projection P, inner-product choice, the state supplying it, cutoff'"),
 A("projection P","SYNTACTIC","NOT_SPECIFIED",
   "A named construction choice ('the projection P'); not defined on this line.",
   "UNSPECIFIED","a named decision axis; object undefined on this line","UNRESOLVED",
   "exact_source_line as above"),
 A("system/bath","SYNTACTIC","NOT_SPECIFIED",
   "A named construction choice ('system/bath partition'); not defined on this line.",
   "UNSPECIFIED","a named decision axis; object undefined on this line","UNRESOLVED",
   "exact_source_line as above"),
]

ADJ[15] = [
 A("coarse-grain","SEMANTIC","NOT_SPECIFIED",
   "NOT ESTABLISHED FROM SUPPLIED EVIDENCE. The line states that deriving "
   "coarse-graining does NOT by itself yield a constitutive/response structure; "
   "the coarse-graining object itself is not defined.",
   "UNSPECIFIED","a derivation target of the U4 layer; object undefined","UNRESOLVED",
   "exact_source_line: 'deriving coarse-graining does NOT hand you a constitutive/response structure'"),
 A("scale separation","SEMANTIC","NOT_SPECIFIED",
   "'Timescale separation' appears as one of the extra conditions under which the "
   "constitutive/response structure follows; no separation object is defined.",
   "UNSPECIFIED","one of the enumerated extra conditions (weak coupling, Gaussianity, near-equilibrium, timescale separation)","UNRESOLVED",
   "exact_source_line: '(that follows only under extra conditions: weak coupling, Gaussianity, near-equilibrium, timescale separation)'"),
 A("response function","SEMANTIC","NOT_SPECIFIED",
   "The 'constitutive/response structure' is named as what does NOT follow from "
   "coarse-graining alone; the structure itself is not defined on this line.",
   "UNSPECIFIED","the U4-layer target structure; object undefined","UNRESOLVED",
   "exact_source_line as above"),
]

ADJ[16] = [
 A("gauge","SEMANTIC","LOCALLY_TYPABLE",
   "The gauge/orbit constraints: the line quantifies their effect -- gauge/orbit "
   "constraints ALONE leave an 11-dimensional FRW response family.",
   "INFERABLE","constraint orbit of the response kernel; 11-dimensional family left by gauge/orbit constraints alone","LEGITIMATE",
   "exact_source_line: 'gauge/orbit constraints alone leave an 11-dimensional FRW response family'"),
 A("response kernel","SEMANTIC","LOCALLY_TYPABLE",
   "The response kernel as priced property: the line states that descending to the "
   "3-dimensional Lorentz-compatible family is bought ONLY by an assumption and "
   "further descent to 2 by S7/closure; the property priced belongs to the "
   "response kernel, not to a background symmetry.",
   "INFERABLE","object whose symmetry-family dimension is priced by assumptions","LEGITIMATE",
   "exact_source_line: 'This +1 prices a property of the response kernel, not a symmetry of the background'"),
]

ADJ[17] = [
 A("coarse-grain","SEMANTIC","NOT_SPECIFIED",
   "NOT ESTABLISHED FROM SUPPLIED EVIDENCE. The line operationalizes the U4 "
   "question as enumerating universality classes of chi(omega,k); the "
   "coarse-graining object itself is not defined here.",
   "UNSPECIFIED","the derivation target of U4; object undefined on this line","UNRESOLVED",
   "exact_source_line: 'ENUMERATE the universality classes chi(omega,k) can occupy'"),
]

ADJ[18] = [
 A("projector","SEMANTIC","LOCALLY_TYPABLE",
   "The spin-projector decomposition of gravitational kernels as a technique, per "
   "the supplied evidence: it became routine in the higher-derivative-gravity "
   "propagator analysis associated with Stelle 1977. This is a literature-level "
   "technique attestation, not a specific projector object in this repository.",
   "UNSPECIFIED","a bibliographic technique (spin-projector decomposition), not a specific object here","NOT_COMPARABLE",
   "exact_source_line: 'the spin-projector decomposition of gravitational kernels became routine' (secondary-literature-verified attestation to Stelle 1977)"),
]

ADJ[19] = [
 A("gauge","SEMANTIC","LOCALLY_TYPABLE",
   "The synchronous-gauge vs gauge-unfixed computations: the line states the "
   "synchronous-gauge computation reproduces the gauge-invariant content of the "
   "gauge-unfixed one; their difference is the orbit variation, reducing "
   "identically to bath-EoM (friction included) + a total derivative; spatial-TT "
   "content is orbit-blind.",
   "UNSPECIFIED","gauge choice of the two computations compared in the A4 result","LEGITIMATE",
   "exact_source_line: 'the synchronous-gauge computation reproduces the gauge-invariant content of the gauge-unfixed computation ... the difference of the two computations is the orbit variation, which reduces identically to bath-EoM (friction included) + total derivative'"),
 A("projector","SEMANTIC","NOT_SPECIFIED",
   "'Projector vacuity' appears only as the name of one detected trap-plant in the "
   "A4 test suite; the line does not define a projector object.",
   "UNSPECIFIED","the name of a detected plant; object undefined on this line","NOT_COMPARABLE",
   "exact_source_line: 'plants (constant-H trap, wrong-a, projector vacuity) all detected'"),
]

ADJ[20] = [
 A("KUBO","SEMANTIC","EXPLICITLY_TYPED",
   "Kubo(-Mori): the conventional MZ correlation for a quantum system is the "
   "Kubo-Mori correlation, per the line.",
   "UNSPECIFIED","the conventional correlation used by the MZ projection","LEGITIMATE",
   "exact_source_line: 'the Mori-Zwanzig projection conventionally uses the KUBO-MORI correlation'"),
 A("Mori-Zwanzig","SEMANTIC","EXPLICITLY_TYPED",
   "The Mori-Zwanzig projection, whose conventional correlation the line fixes as "
   "Kubo-Mori.",
   "UNSPECIFIED","the projection whose conventional correlation is fixed","LEGITIMATE",
   "exact_source_line as above"),
]

ADJ[21] = [
 A("Mori-Zwanzig","SEMANTIC","EXPLICITLY_UNRESOLVED",
   "The record explicitly states that rung3's 'Mori-Zwanzig kernel' does NOT "
   "denote a unique object, and that the two candidates answer oppositely under "
   "the ratio test. The referent is explicitly unresolved by the supplied "
   "evidence itself.",
   "UNSPECIFIED","explicitly non-unique kernel reference; no single object established","NOT_LEGITIMATE",
   "exact_source_line: 'rung3's \"Mori-Zwanzig kernel\" does not denote a unique object, and the two candidates answer oppositely'"),
]

ADJ[22] = [
 A("gauge","SEMANTIC","NOT_SPECIFIED",
   "NOT ESTABLISHED FROM SUPPLIED EVIDENCE (context-only occurrence). The line "
   "concerns the scalar projection's vanishing WITHOUT inserting P^TT, and the "
   "FORBIDDEN circular 'confirm P^TT annihilates scalars' check; no gauge object "
   "is defined.",
   "UNSPECIFIED","none established on this line","UNRESOLVED",
   "bounded_context_window only"),
 A("correlator","SEMANTIC","NOT_SPECIFIED",
   "NOT ESTABLISHED FROM SUPPLIED EVIDENCE (context-only occurrence).",
   "UNSPECIFIED","none established on this line","UNRESOLVED",
   "bounded_context_window only"),
]

ADJ[23] = [
 A("coarse-grain","SEMANTIC","LOCALLY_TYPABLE",
   "Per the record's own claim, coarse-graining (as its Wilsonian exemplar) is an "
   "information-projection that organizes RG flow through progressive "
   "correlation-breaking (St happens at rho-roots, not at a scale). This is the "
   "record's asserted referent.",
   "UNSPECIFIED","information-projection organizing RG flow (asserted claim of the record)","LEGITIMATE",
   "exact_source_line: 'renormalization/coarse-graining is an information-projection' with 'Wilsonian coarse-graining as information loss' in the same record"),
]

ADJ[24] = [
 A("gauge","SEMANTIC","LOCALLY_TYPABLE",
   "The gauge image/orbit direction inserted in the D4-C test: the record states "
   "the test BYPASSED the projector that defines the declared bath, and Routes A "
   "and B show that projector annihilates the orbit direction exactly.",
   "UNSPECIFIED","the gauge/orbit direction annihilated exactly by the declared-bath projector","LEGITIMATE",
   "exact_source_line: 'the D4-C test BYPASSED the projector that defines the declared bath. Routes A and B show that projector annihilates the orbit direction exactly'"),
]

ADJ[25] = [
 A("gauge","SEMANTIC","LOCALLY_TYPABLE",
   "Same scope as the classification line above: the gauge/orbit direction within "
   "the declared TT bath, annihilated exactly by its defining projector; result "
   "explicitly fenced from the D3(iii) gauge-prescription question.",
   "UNSPECIFIED","gauge/orbit direction of the declared bath; scope-fenced","LEGITIMATE",
   "exact_source_line: 'gauge-transforming the internal line moves no TT amplitude ... NOT D3(iii)'"),
]

ADJ[26] = [
 A("gauge","SEMANTIC","LOCALLY_TYPABLE",
   "The gauge image/orbit direction of the D4-C test, with the bypass made "
   "explicit; the projector of the declared bath annihilates it exactly.",
   "UNSPECIFIED","gauge/orbit direction of the declared bath","LEGITIMATE",
   "exact_source_line: 'the D4-C test BYPASSED the projector ... projector annihilates the orbit direction exactly'"),
]

ADJ[27] = [
 A("projector","SEMANTIC","LOCALLY_TYPABLE",
   "The MZ projector P: per the line, choosing P IS the partition "
   "(coarse-graining -> split), in contrast to the Zurek factorization-first "
   "ordering. No explicit P formula is given.",
   "UNSPECIFIED","the MZ projector whose choice constitutes the partition (ordering claim)","LEGITIMATE",
   "exact_source_line: 'Mori-Zwanzig: choosing a projector P IS the partition (coarse-graining -> split)'"),
 A("Mori-Zwanzig","SEMANTIC","LOCALLY_TYPABLE",
   "The Mori-Zwanzig route: P-first, where the projector choice constitutes the "
   "partition; explicitly contrasted with the Zurek factorization-first ordering.",
   "UNSPECIFIED","an ordering of partition construction (P first)","LEGITIMATE",
   "exact_source_line: 'Mori-Zwanzig: choosing a projector P IS the partition (coarse-graining -> split), while Zurek's approach assumes factorization'"),
]

ADJ[28] = [
 A("projector","SEMANTIC","LOCALLY_TYPABLE",
   "The MZ projector P whose choice IS the partition (the record's ordering "
   "statement); no explicit formula supplied.",
   "UNSPECIFIED","the MZ projector defining the partition","LEGITIMATE",
   "exact_source_line: 'Mori-Zwanzig: choosing a projector P IS the partition (coarse-graining -> split)'"),
 A("Mori-Zwanzig","SEMANTIC","LOCALLY_TYPABLE",
   "The Mori-Zwanzig projection route, P-first, explicitly contrasted with Zurek "
   "factorization-first.",
   "UNSPECIFIED","P-first partition-construction ordering","LEGITIMATE",
   "exact_source_line as above"),
]

ADJ[29] = [
 A("inner product","SEMANTIC","LOCALLY_TYPABLE",
   "The CONVENTIONAL Mori-Zwanzig inner product: on it there is no ladder to "
   "inherit, and the friction kernel does not contain T at all.",
   "UNSPECIFIED","the conventional MZ inner product; no-ladder property asserted on it","LEGITIMATE",
   "exact_source_line: 'on the CONVENTIONAL Mori-Zwanzig inner product there is no ladder to inherit, and the friction kernel does not contain T at all'"),
 A("Mori-Zwanzig","SEMANTIC","LOCALLY_TYPABLE",
   "The Mori-Zwanzig projection route characterized on this line by the property "
   "of its conventional inner product (no ladder to inherit; friction kernel "
   "T-free).",
   "UNSPECIFIED","the MZ route whose conventional inner product carries no ladder","LEGITIMATE",
   "exact_source_line as above"),
]

ADJ[30] = [
 A("gauge","SEMANTIC","LOCALLY_TYPABLE",
   "Off-shell gauge artifacts: the line states no gauge-fixing term was ever added "
   "to the h-action, so the bare off-shell kernel can carry pole pieces with gauge "
   "dependence, which cancel in physical observables.",
   "UNSPECIFIED","pole pieces with gauge dependence of the bare off-shell kernel; cancel in observables","LEGITIMATE",
   "exact_source_line: 'off-shell gauge artifacts -- no gauge-fixing term was ever added to the h-action, so the bare off-shell kernel can carry gauge-dependent pole pieces'"),
]

ADJ_IDS = set(ADJ.keys())


VALID_TL = {"SYNTACTIC", "SEMANTIC", "INTERPRETIVE", "NONE"}
VALID_RS = {"EXPLICITLY_TYPED", "LOCALLY_TYPABLE", "EXPLICITLY_UNRESOLVED",
            "NOT_SPECIFIED", "CONFLICTING_REFERENTS"}
VALID_MT = {"EXPLICIT", "INFERABLE", "UNSPECIFIED"}
VALID_CS = {"LEGITIMATE", "NOT_LEGITIMATE", "UNRESOLVED", "NOT_COMPARABLE"}
FORBIDDEN_CLASSES = {"CONFLICT_IDENTIFIED", "NOT_A_CONFLICT", "SAME_CONSTRUCTION",
                     "DISTINCT_CONSTRUCTION", "EQUIVALENT", "DEPENDENT",
                     "RELATED", "INDEPENDENT"}
FORBIDDEN_FIELDS = {"prior_classification", "prior_pair", "pair", "pairs",
                    "pair_relation", "pair_relations", "conflict",
                    "conflicts", "conflict_count", "mapping",
                    "prior_classification_mapping"}


def main():
    with open(FROZEN) as f:
        frozen = json.load(f)
    stmts = frozen["statements"]
    for n, s in enumerate(stmts):
        s.setdefault("statement_index", n)
    assert len(stmts) == 31, f"expected 31 frozen statements, got {len(stmts)}"
    assert set(int(s["statement_index"]) for s in stmts) == ADJ_IDS, \
        "adjudication indices do not cover exactly the frozen statements"

    records = []
    for s in stmts:
        i = int(s["statement_index"])
        terms = ADJ[i]
        assert [a["candidate_term"] for a in terms] == list(s["candidate_term"]), \
            f"statement {i}: candidate terms mismatch frozen package"
        rec = {
            "statement_index": i,
            "source_path": s["source_path"],
            "source_line": s["source_line"],
            "exact_source_line": s["exact_source_line"],
            "candidate_terms": s["candidate_term"],
            "statement_id": s.get("statement_id"),
            "frozen_context_digest": s.get("frozen_context_digest"),
            # Prior machine output is intentionally NOT copied into the record.
            # The frozen prior_classifier_trigger is contamination metadata only;
            # embedding it here would leak prior class values (DEPENDENT,
            # INDEPENDENT, ...) into the adjudication artifact.
            "prior_machine_output": None,
            "prior_trigger": None,
            "contamination_warning": CONTAMINATION_WARNING,
            "adjudications": terms,
        }
        records.append(rec)

    # ---- mechanical validation ----
    errors = []
    # 1-2: counts
    if not (len(stmts) == 31 and len(records) == 31):
        errors.append("count mismatch")
    # 3: correspondence
    if [r["statement_index"] for r in records] != \
       [int(s["statement_index"]) for s in stmts]:
        errors.append("record/order correspondence mismatch")
    # 4-5: no pair-level expansion or fields
    # 6: only permitted values
    for r in records:
        # Scan only the decision content (adjudications + decision fields),
        # NOT the record blob: the contamination_warning string legitimately
        # names the quarantined prior classes as disclosure metadata, and is
        # not a classification value.
        decision_blob = json.dumps(r["adjudications"]) + " " + " ".join(
            f"{k} {v}" for k, v in r.items()
            if k not in ("adjudications", "contamination_warning", "exact_quote"))
        for cls in FORBIDDEN_CLASSES:
            # Whole-token match only, and not as the tail of a hyphenated
            # compound: the frozen prose legitimately contains uppercase
            # "MULTIPOLE-DEPENDENT", which is not a classification value.
            if re.search(rf"(?<![A-Za-z-]){cls}(?![A-Za-z])", decision_blob):
                errors.append(f"forbidden class {cls} in record {r['statement_index']}")
        for a in r["adjudications"]:
            if a["typing_level"] not in VALID_TL:
                errors.append(f"bad typing_level in {r['statement_index']}")
            if a["referent_status"] not in VALID_RS:
                errors.append(f"bad referent_status in {r['statement_index']}")
            if a["mathematical_type"] not in VALID_MT:
                errors.append(f"bad mathematical_type in {r['statement_index']}")
            if a["comparison_status"] not in VALID_CS:
                errors.append(f"bad comparison_status in {r['statement_index']}")
            if (a["referent_status"] in {"EXPLICITLY_TYPED", "LOCALLY_TYPABLE"}
                    and "NOT ESTABLISHED" in a["referent_description"]):
                errors.append(
                    f"positive referent without evidence in {r['statement_index']}")
    # 7-8: prior machine output only as metadata
    if any(r["prior_machine_output"] is not None or r["prior_trigger"] is not None
           for r in records):
        errors.append("prior machine output leaked into records")
    # 10: exact quote unchanged
    for s, r in zip(stmts, records):
        if s["exact_source_line"] != r["exact_source_line"]:
            errors.append(f"exact quote altered at {s['statement_index']}")
    if errors:
        print("VALIDATION FAILED:")
        for e in errors:
            print("  -", e)
        raise SystemExit(1)

    counts = {"typing_level": {}, "referent_status": {}, "mathematical_type": {},
              "comparison_status": {}}
    for key in counts:
        pool = VALID_TL if key == "typing_level" else \
            VALID_RS if key == "referent_status" else \
            VALID_MT if key == "mathematical_type" else VALID_CS
        counts[key] = {v: 0 for v in sorted(pool)}
    total_occurrences = 0
    for r in records:
        for a in r["adjudications"]:
            total_occurrences += 1
            counts["typing_level"][a["typing_level"]] += 1
            counts["referent_status"][a["referent_status"]] += 1
            counts["mathematical_type"][a["mathematical_type"]] += 1
            counts["comparison_status"][a["comparison_status"]] += 1

    out = {
        "artifact": "HISA01_INDEPENDENT_SEMANTIC_ADJUDICATION",
        "protocol": "HISA-01 statement-level independent semantic referent adjudication",
        "unit_of_adjudication": "mention -> referent -> type (per frozen statement)",
        "input_package": "HISA01_FROZEN_EVIDENCE_PACKAGE.json",
        "frozen_package_sha256": hashlib.sha256(
            open(FROZEN, "rb").read()).hexdigest(),
        "superseded_artifact": {
            "file": "HISA01_INDEPENDENT_ADJUDICATION.json",
            "status": "INVALID_PROTOCOL_ATTEMPT (quarantined)",
        },
        "contamination_metadata": CONTAMINATION_WARNING,
        "totals": {
            "input_statements": len(stmts),
            "adjudication_records": len(records),
            "term_occurrences_adjudicated": total_occurrences,
        },
        "counts": counts,
        "independence_check": {
            "prior_classifications_used_as_inputs": False,
            "prior_mapping_dictionary_present": False,
            "external_knowledge_used": False,
            "adjudication_reproducible_from": [
                "exact_quote", "bounded_context_window", "candidate_term",
                "source_path", "source_line", "provenance",
            ],
        },
        "adjudication_records": records,
    }
    with open(OUT, "w") as f:
        json.dump(out, f, indent=2, ensure_ascii=False)
    print("WROTE", OUT)
    print("records:", len(records), "term occurrences:", total_occurrences)
    for k, v in counts.items():
        print(k, v)


if __name__ == "__main__":
    main()
