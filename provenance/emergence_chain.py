#!/usr/bin/env python3
"""emergence_chain: GENERATES the emergence-chain narrative from the register.

THE FIRST ARTIFACT OF THE BUILDING STAGE (2026-08-09). GRUT's nodes exist; the story does not --
nowhere is the sequence from origin to present laid end to end with each link's honest status.
This file constructs it. The construction asserts NO new physics: it places what the register
already holds into story order and marks each link.

THE ONE DESIGN RULE, and it is this build's own laundering guard: THE STAGE->CLAIMS MAPPING IS
AUTHORED (it is the construction -- position, story sentence, which claims cover the link, what
would strengthen it), BUT EVERY STATUS IS GENERATED from claims.json (tier, ledger_delta,
disposition, grut_standing). Narrative pressure is the laundering shape here -- a story wants to
flow, and the temptation is to soften a 'borrowed' into a 'follows from' so the chain reads
better. A generated status column cannot be softened without editing the register, and the
register has a gate. If a link needs something the register does not have, the link says OPEN /
SILENT / UNPOSED -- the story is not permitted to upgrade a claim to fit the sequence.

Run:  python3 emergence_chain.py          writes ../EMERGENCE_CHAIN.md and prints a summary
      python3 emergence_chain.py --check  regenerates to a temp string and DIFFS against the file
                                          (drift check: the wired-in defense against a narrative
                                          that wanders from its register)
"""
import json
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.join(HERE, "..", "EMERGENCE_CHAIN.md")

# ================================ THE CONSTRUCTION (authored) ================================
# Each stage: (key, title, story, claim_ids, ordering_note_or_None, strengthen)
# claim_ids == "SILENT" / "UNPOSED" are honest labels, in the chain as links, not omissions.
STAGES = [
 ("origin", "The origin: a low-entropy past",
  "The story begins with a boundary condition, not a mechanism: the universe starts in a "
  "low-entropy macrostate. GRUT does not explain this; it imports it, priced, and its own arrow "
  "result says the direction of time REQUIRES it -- the framework sharpened the question and then "
  "declined to answer it.",
  ["past_hypothesis", "entropy_foundations", "second_law_h_theorem"],
  None,
  "Part 4 of the building brief: 'why this boundary state?' -- booked, never worked, and sitting "
  "directly beside the register's strongest original result."),

 ("medium", "The medium: a responsive vacuum with finite memory",
  "The constitutive posit: the gravitational vacuum is an open medium that responds and relaxes. "
  "This is the program's entry price (+3: the system/bath split, the Gaussian truncation, the "
  "causal background), booked openly as a stance, with the standard open-system toolkit borrowed "
  "as scaffolding.",
  ["rung1_inin_action", "u3_split_origin", "linear_response_viscoelastic",
   "relativistic_hydro_israel_stewart", "superfluid_bec_media"],
  None,
  "u3 (why a system/bath split exists at all) is the deepest open question at this link."),

 ("persistence", "Persistence: what the medium remembers",
  "The memory kernel -- what persists is what the kernel carries. The single-pole (finite-memory) "
  "form is the framework's load-bearing structural conjecture, and it is DERIVED-PENDING on the "
  "bath: the one decisive external question (pole vs cut) lives here, dispatched, unanswered.",
  ["rung3_single_pole", "rung4_love_kk", "eft_operator_basis", "u2_kernel_universality",
   "u4_constitutive_origin"],
  None,
  "The dispatch's answer (DISPATCH_ONE_PAGE.md). A cut-class answer kills this link as stated."),

 ("arrow", "The arrow: existence intrinsic, direction imported",
  "The register's strongest original result: an open medium HAS an arrow (existence is intrinsic "
  "to dissipation), but WHICH direction is state-dependent and rides the origin link's boundary "
  "condition. The decomposition clarifies the old question rather than dissolving it.",
  ["arrow_of_time", "rung2_kms_gate", "fluctuation_theorems"],
  "SHARED NODE: rung2_kms_gate also carries the thermality link -- the KMS condition is one fact "
  "doing two jobs (locking noise to dissipation, and tying equilibrium to temperature). The arrow "
  "and thermality links are CONCURRENT, not sequential; the chain forces no order between them.",
  "Nothing in-house: the existence half is done; the direction half is the origin question."),

 ("thermality", "Thermality: temperature as a consequence",
  "In equilibrium the fluctuation-dissipation/KMS structure forces the thermal form; the horizon "
  "temperature T = H/2pi enters as an IMPORT (Unruh), not a derivation -- the register prices it "
  "and refuses to let the recovery be sold as a prediction.",
  ["rung2_kms_gate", "entropy_area_unruh", "founding_h1_zeta_casimir"],
  "Concurrent with the arrow link (see its note).",
  "A derivation of the Unruh import from the medium's own kernel would move this link from "
  "priced-import toward derived; nothing in the register attempts it."),

 ("gravity", "Gravity: the stiff limit",
  "Taking the memory time to zero collapses the responsive kernel to a conservative local form -- "
  "GR is RECOVERED-WITH-IMPORTS (+2: area entropy, Unruh T), never derived. The coupling's "
  "normalization resisted derivation on named obstructions (settled-negative, frozen), and the "
  "response's tensor structure is a CHOICE, priced at +1, whose consequences the interior family "
  "explores.",
  ["rung5_gr_limit", "rung9a_value", "rung9b_bridge", "p_tt_ansatz", "analogue_gravity_acoustic"],
  None,
  "The rung9b reopen conditions are named in NO_GO_LEDGER entry 1; nothing else in-house."),

 ("quantum", "Quantum: the reduced state",
  "Integrating out the bath yields reduced-density-matrix dynamics (+2: the quantization "
  "condition, the Born measure -- both imported, both priced). GRUT uses quantum mechanics; it "
  "does not explain it.",
  ["rung6_qm_limit", "born_rule"],
  None,
  "The quantum-foundations map (prose artifact, nothing banked) locates the imports precisely: "
  "outcome-selection and the Born measure are TWO inputs, and einselection's edge runs "
  "basis <- measure."),

 ("classicality", "Classicality: mapped, not banked",
  "Why the world looks classical. The program MAPPED this (the quantum-foundations cluster: "
  "einselection dissociates from the Born measure only asymmetrically; 'decoherence explains "
  "classicality independently of probability' is folklore) -- but the map is labels, not register "
  "nodes. NOTHING AT THIS LINK IS BANKED.",
  "MAPPED-NOT-BANKED",
  "ORDERING AMBIGUOUS: classicality does not cleanly precede structure -- decoherence of "
  "cosmological perturbations happens DURING structure formation. The chain marks this "
  "concurrence rather than forcing a sequence for readability.",
  "Banking the QF map's inventory (a ruled, dated amendment) would give this link register "
  "status; the cross-cluster shared input S1 already connects it to the medium link."),

 ("structure", "Structure: linear cosmology",
  "At linear order the framework's cosmology is LCDM-shaped by a no-go export, not by derivation "
  "-- the trace-only endpoint is excluded (the retraction history is part of this link's record), "
  "and the interior family opens a computed ALLOWANCE (mu-1 up to ~20% at the loose edge, no "
  "floor) that predicts nothing.",
  ["mu_linear", "zeta_interior_family", "founding_h2_R_zeta_bridge", "l0_r2_exact_unique_breaker",
   "l0_r3_payoff_mu_linear"],
  "Concurrent with classicality (see its note).",
  "The two owed-or-retired calcs (TT-auto rigorous; xi_ij) both live at this link's edge."),

 ("darkenergy", "Dark energy: the relaxing vacuum",
  "Out of equilibrium the medium's slow relaxation is the candidate dark-energy story (+3: the "
  "amplitude, the two-scale commitment, the single-departure shape -- all priced). The value of "
  "Lambda is UNDETERMINED by every framework in the program, booked as such; DESI's w(z) is the "
  "live kill-channel.",
  ["rung7_wz", "rung7_w1_wz_map", "rung7_w2_wa_sign", "rung7_w3_nocrossing_export",
   "lambda_undetermined"],
  None,
  "DESI DR3 (termination condition channel C2)."),

 ("matter", "Matter: silent",
  "The Standard Model -- its spectrum, its couplings, its three generations -- appears NOWHERE in "
  "the register. The constitution's assumed-list names 'the SM spectrum' in prose, but no node "
  "books it: the chain's matter link is SILENT, and a silent link visible in the story is worth "
  "more than one tidied away.",
  "SILENT",
  None,
  "Booking the import honestly (one node, priced) would close the bookkeeping gap; DERIVING "
  "anything here is not on any current route."),

 ("observers", "Observers: unposed",
  "How observers arise, and what if anything the framework owes that question, has never been "
  "POSED in the register -- no node, no map, no artifact. Recorded as the chain's honest end.",
  "UNPOSED",
  None,
  "Posing the question well would itself be a node; nothing requires it be posed."),
]

# Off-chain nodes, listed so the chain's coverage is auditable (chain + off-chain + scaffolding
# not cited above should account for every GRUT node; the generator CHECKS this).
OFF_CHAIN = {
 "rung8_falsifier": "the tabletop discriminator -- an instrument pointed at the chain, not a link",
 "method_novelty": "the method's own gauntlet -- about the program, not the universe",
 "founding_h3_doubleslit_anchor": "deferred anchor (disposition: deferred)",
 "info_i1_renorm_as_information": "information-principle triplet: generic half",
 "info_i2_beyond_standard_bridge": "information-principle triplet: screened-refuted",
 "info_i3_distinct_consequence": "information-principle triplet: moot",
 "l0_r1_redundancy_exists": "frontier-3 generic half (its crux nodes sit at the structure link)",
 "rung7_w1_wz_map": None,  # cited in chain; placeholder removed below
 "u1_form_universality": "V2 universality entries: about the FRAMEWORK's form, not a story stage",
 "emergence_chain": "the chain itself -- the artifact, not a link (its banking tripped this very "
                    "coverage guard, which is the guard working)",
 "u5_constitutive_phases": "V2 classification branch (see persistence link's u4)",
 "u6_constitutive_order": "V2 order-parameter branch (see persistence link's u4)",
 "passivity_channel_diagonal": "the general channel-diagonal passivity lemma -- frame-free "
                               "linear-response mathematics, not a stage of the story",
 "x_no_pin_theorem": "the lemma applied to the two-channel family (route R3 closed as "
                     "classifier) -- an instrument-grade fact about the framework's parameter "
                     "space, not a stage of the story",
 "kk_static_transfer": "the dissipative-to-static transfer question (answered 2026-08-09: "
                       "conditional at the class-level chi_inf >= 0, never unconditional) -- an instrument "
                       "pointed at the floor's reach, not a link",
}
OFF_CHAIN.pop("rung7_w1_wz_map")


def _status(c):
    """The GENERATED per-claim status token. Mechanical: register fields only."""
    bits = [c["tier"]]
    d = c.get("ledger_delta", 0)
    if isinstance(d, int) and d:
        bits.append(f"{d:+d}")
    if c.get("disposition"):
        bits.append(f"[{c['disposition']}]")
    if c.get("grut_standing") == "borrowed":
        bits.append("(borrowed)")
    return " ".join(bits)


def _link_grade(claims):
    """Mechanical link summary from the covering claims' registers fields. Worst-reading rules:
    a link is only as original as its register support."""
    if claims == "SILENT":
        return "SILENT -- no register node covers this link"
    if claims == "UNPOSED":
        return "UNPOSED -- the question has never been asked in the register"
    if claims == "MAPPED-NOT-BANKED":
        return "MAPPED, NOT BANKED -- prose artifacts only; zero register nodes"
    kinds = set()
    for c in claims:
        if c.get("grut_standing") == "borrowed":
            kinds.add("borrowed")
        elif c["tier"] in ("shown", "derived"):
            kinds.add("original-result")
        elif c["tier"] == "derived-pending":
            kinds.add("derived-pending")
        elif c["tier"] == "assumed":
            kinds.add("priced-import" if (c.get("ledger_delta") or 0) > 0 else "adopted-stance")
        else:
            kinds.add("open")
    order = ["original-result", "derived-pending", "priced-import", "adopted-stance", "open",
             "borrowed"]
    return " + ".join(k for k in order if k in kinds)


def generate():
    reg = json.load(open(os.path.join(HERE, "claims.json")))["claims"]
    by = {c["id"]: c for c in reg}
    grut = [c for c in reg if c.get("ledger_scope", "grut") == "grut"]

    # guard: every cited id must exist; every GRUT node must be accounted for
    cited = set()
    for _k, _t, _s, ids, _o, _st in STAGES:
        if isinstance(ids, list):
            for i in ids:
                if i not in by:
                    raise SystemExit(f"chain cites {i!r}, which is not in the register")
                cited.add(i)
    unaccounted = [c["id"] for c in grut if c["id"] not in cited and c["id"] not in OFF_CHAIN]
    if unaccounted:
        raise SystemExit(f"GRUT nodes neither in the chain nor declared off-chain: {unaccounted} "
                         f"-- a gap you cannot see is the failure this generator exists to prevent")

    L = []
    L.append("# The emergence chain — origin to observers, each link at its honest status\n")
    L.append("*GENERATED by `provenance/emergence_chain.py` — the stage→claims mapping is authored"
             " (it is the construction); **every status is generated from the register** and cannot"
             " be softened without editing a gated file. Regenerate after any register change;"
             " `--check` diffs. This artifact asserts no new physics.*\n")
    L.append("**The chain at a glance:** origin → medium → persistence → arrow ∥ thermality → "
             "gravity → quantum → classicality ∥ structure → dark energy → matter (SILENT) → "
             "observers (UNPOSED). Two concurrences (∥) are marked as such — forcing them into "
             "sequence would be a readability lie.\n")
    for n, (key, title, story, ids, onote, strengthen) in enumerate(STAGES, 1):
        claims = ids if isinstance(ids, str) else [by[i] for i in ids]
        L.append(f"\n## {n}. {title}\n")
        L.append(story + "\n")
        L.append(f"**Link status (generated):** {_link_grade(claims)}\n")
        if isinstance(claims, list):
            L.append("| register claim | status (generated) |")
            L.append("|---|---|")
            for c in claims:
                L.append(f"| `{c['id']}` | {_status(c)} |")
            L.append("")
        if onote:
            L.append(f"**Ordering note:** {onote}\n")
        L.append(f"**What would strengthen it:** {strengthen}\n")

    L.append("""
## The finding — what the node list cannot show (Part 3; authored reading of the generated chain)

**1. The original content clusters in the middle, and both ends are borrowed or empty.** Links 2–6
(medium, persistence, arrow, thermality, gravity) every one carries an original result; links 3–5 —
the memory kernel, the KMS lock, the arrow decomposition — are the unambiguous core, and they are
exactly the open-system physics. Link 1 (origin) is **pure borrowed**. Links 7–8 (quantum,
classicality) are imports and an unbanked map. Links 11–12 (matter, observers) are silent and
unposed. The predicted shape holds, sharpened: **GRUT is a middle-of-the-story theory** — strongest
precisely where its own toolkit (dissipation, memory, detailed balance) does the work, empty where
that toolkit has nothing to grip.

**2. The chain's center of gravity sits on the ledger's only −1.** `rung2_kms_gate` — the shared
arrow/thermality node — is the one place in the register's history where the framework ever
*removed* an assumption (the KMS lock discharging the noise kernel as an independent input). The
story's strongest joint and the ledger's only negative delta are the same node. That is not
arranged; it is what the generated column shows.

**3. A soft marker, found by construction:** the register has NO structured field distinguishing
generic-shown ("true of any open medium") from GRUT-original-shown — the distinction lives only in
statement prose ("GENERIC — not uniquely GRUT"). The dark-energy and thermality links' original
markers partially ride generic halves (`rung7_w1_wz_map`, `founding_h1_zeta_casimir`). Any
generated status column inherits this blindness until the register grows the field; recorded here
rather than patched by prose-matching, per the resident's own precedent (prose scanning is a HINT,
never authoritative).

**4. The two ends differ in kind, and that decides where to build.** The origin end is a **priced
import sitting directly beside the strongest original result and the only −1** — the tools that
might work it (the arrow decomposition, the KMS structure) are adjacent and in-house. The matter
end is **silent with no adjacent original content** — nothing in the register grips it. If the
program builds anywhere, the chain says the origin end is the buildable end. (Part 4 of the brief
aims there; this finding confirms the aim from the artifact rather than from preference.)

**5. Bookkeeping gaps surfaced by the construction:** the constitution's assumed-list names "the
SM spectrum" and **no node books it** (the matter link's silence is a registry gap, not only a
physics one); classicality is entirely prose (mapped, zero nodes); and the generic-vs-original
field is missing (item 3).
""")
    L.append("\n## Off-chain nodes (accounted, not links)\n")
    L.append("*Every GRUT node is either in the chain above or listed here — the generator errors "
             "otherwise.*\n")
    L.append("| node | why off-chain |")
    L.append("|---|---|")
    for i, why in sorted(OFF_CHAIN.items()):
        L.append(f"| `{i}` | {why} |")
    L.append("")
    return "\n".join(L)


def main():
    doc = generate()
    if "--check" in sys.argv:
        on_disk = open(OUT).read() if os.path.exists(OUT) else ""
        if on_disk != doc:
            print("DRIFT: EMERGENCE_CHAIN.md does not match the register-generated chain. "
                  "Regenerate (python3 emergence_chain.py) -- never hand-edit the narrative.")
            return 1
        print("chain matches the register (no drift).")
        return 0
    open(OUT, "w").write(doc)
    print(f"EMERGENCE_CHAIN.md written ({len(doc)} chars, {len(STAGES)} links).")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
