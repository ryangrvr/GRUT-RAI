#!/usr/bin/env python3
"""emergence_hypothesis: GENERATES GRUT_EMERGENCE_HYPOTHESIS.md from the register.

THE CANDIDATE-HYPOTHESIS ARTIFACT. The emergence chain answers "what is the story?"
This artifact answers the earlier question: "what, exactly, does GRUT claim about
reality that could be wrong?" -- stated as a LAYERED hypothesis whose first rung is
u3_split_origin (why a system/bath decomposition is warranted at all), NOT the
responsive vacuum.

STATUS (asserted on the artifact's face): CANDIDATE HYPOTHESIS -- NOT YET A DERIVED
THEORY. The register supports a candidate, not a derivation: 20 nodes are to-derive,
the quantum limit is assumed (+2), and Born outcomes are not banked at all.

THE SAME DESIGN RULE AS emergence_chain.py: the LAYER->CLAIMS MAPPING IS AUTHORED (it
is the construction), BUT EVERY STATUS IS GENERATED from claims.json (tier,
ledger_delta, disposition, grut_standing). A layer whose covering claims contain no
shown/derived/derived-pending result is printed TO-DERIVE by the generator, not by
prose. Softening a status means editing the register, which has a gate.

The artifact keeps THREE things strictly separate (they must never be merged, because
the 74-node register makes a stipulative framework look more complete than its
foundational derivation warrants):
  PART 1 -- the ontological hypothesis (what GRUT proposes about reality)
  PART 2 -- the derivation chain (what follows IF the hypothesis is granted)
  PART 3 -- the external inputs (what GRUT imports; generated from tier==assumed
            and grut_standing==borrowed, with prices)

Run:  python3 provenance/emergence_hypothesis.py          writes ../GRUT_EMERGENCE_HYPOTHESIS.md
      python3 provenance/emergence_hypothesis.py --check  diffs against the file on disk
"""
import json
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.join(HERE, "..", "GRUT_EMERGENCE_HYPOTHESIS.md")

# ================================ PART 2: THE LAYERS (authored) ================================
# Each layer: (key, title, transition, story, claim_ids)
# claim_ids == "SILENT" / "UNPOSED" / "MAPPED-NOT-BANKED" are honest markers, kept as layers.
LAYERS = [
 ("L0", "Fundamental origin -> distinction",
  "Can GRUT say why anything can be distinguished from anything else?",
  "This is the rung the whole hypothesis rests on, and it is NOT DERIVED. If the framework "
  "cannot ground the first distinction, then every later 'the vacuum responds' statement is a "
  "choice of vocabulary rather than a consequence. Recorded FIRST and honestly: nothing below "
  "this rung is derivation until it moves.",
  ["u3_split_origin"]),

 ("L1", "Distinction -> system/bath decomposition",
  "Why is an open-system description physically warranted (rather than chosen)?",
  "The deepest open question at the medium link, now promoted to its own layer. The register "
  "carries the question as a fence (u3_split_origin, tier to-derive). If the answer is negative, "
  "the responsive-medium posit is exposed as the decomposition that makes the mathematics "
  "possible -- the exact hidden-assumption shape this artifact exists to expose.",
  ["u3_split_origin"]),

 ("L2", "System/bath -> response",
  "The constitutive-response machinery (current entry price).",
  "The program's entry price: the INI-in open-system formalism (+4), the finite-memory ontology "
  "stance (+1), and the background TIME-TRANSLATION FLOW (+1) -- the presupposition that lets a "
  "kernel be written at a single frequency at all. The standard open-system toolkit is borrowed "
  "scaffolding. All of it is assumed, priced, and marked; none of it is derived.",
  ["rung1_inin_formalism", "rung1_ontology_finite_memory", "background_time_translation_flow",
   "linear_response_viscoelastic", "relativistic_hydro_israel_stewart", "superfluid_bec_media"]),

 ("L3", "Response -> finite memory",
  "The central GRUT conjecture: the vacuum's response has a finite-memory kernel.",
  "The load-bearing structural posit of the framework. Its status is DERIVED-PENDING at best: "
  "the pole-vs-cut question (below) is the one decisive external test, and a cut-class answer "
  "kills this layer as stated.",
  ["rung3_single_pole", "u2_kernel_universality", "u4_constitutive_origin", "eft_operator_basis"]),

 ("L4", "Finite memory -> single-pole structure",
  "Does the memory kernel reduce to a single pole? The decisive bath question.",
  "The one place the framework makes a structural bet it did not feed in by construction. The "
  "contract-level retarded kernel is computed and banked (delta 0); the transfer question is "
  "answered only conditionally (chi_inf >= 0 at class level, never unconditional); the "
  "classification and order-parameter branches are open. The KK/Love relations are the "
  "derived-pending export of the kernel's form. A cut answer refutes this layer, and "
  "with it L3 and everything above built on the kernel's form.",
  ["kr_contract_retarded_tier4", "kk_static_transfer", "rung4_love_kk", "u5_constitutive_phases",
   "u6_constitutive_order"]),

 ("L5", "Memory -> arrow (existence intrinsic, direction imported)",
  "An open medium HAS an arrow; WHICH direction is imported.",
  "The register's strongest original joint: existence of the arrow is intrinsic to dissipation "
  "(the KMS gate is also the ledger's only -1, discharging the noise kernel as an independent "
  "input). The DIRECTION is state-dependent and rides the low-entropy boundary -- a priced "
  "import the framework sharpened and then declined to answer. Thermality is the concurrent "
  "half of the same node: the KMS condition is one fact doing two jobs. The horizon "
  "temperature enters as an IMPORT (Unruh, priced), and founding_h1's two-levels-of-description "
  "claim is GENERIC -- true of any medium with a response, not uniquely GRUT.",
  ["arrow_of_time", "rung2_kms_gate", "fluctuation_theorems", "past_hypothesis",
   "entropy_foundations", "second_law_h_theorem", "entropy_area_unruh",
   "founding_h1_zeta_casimir"]),

 ("L6", "Memory -> gravity (the stiff limit)",
  "Memory time to zero collapses the kernel to the GR limit -- RECOVERED-WITH-IMPORTS.",
  "GR is recovered only with imports (+2: area entropy, Unruh temperature) and is never "
  "derived; the coupling's normalization resisted derivation on named obstructions "
  "(settled-negative, frozen); the response's tensor structure is a priced choice (+1 "
  "Lorentz-covariance licensing fence, discharged or not by the microscopic Sigma_R^TT at "
  "Wall A).",
  ["rung5_gr_limit", "rung9a_value", "rung9b_bridge", "p_tt_ansatz",
   "response_lorentz_covariance", "analogue_gravity_acoustic"]),

 ("L7", "Gravity -> quantum limit",
  "Reduced-density-matrix dynamics; quantum mechanics USED, not explained.",
  "The quantum limit is an ASSUMED node priced +2 (the quantization condition and the Born "
  "measure are both imported). This is where the emergence chain stops being a theory of "
  "emergence and starts importing structure -- the register's own accounting, printed "
  "mechanically.",
  ["rung6_qm_limit", "born_rule"]),

 ("L8", "Quantum -> Born outcomes",
  "Why definite outcomes with Born weights? NOT DERIVED.",
  "Mapped in the quantum-foundations cluster but never banked: einselection dissociates from "
  "the Born measure only asymmetrically, and 'decoherence explains classicality independently "
  "of probability' is folklore. Zero register nodes. An honest NOT-DERIVED layer, kept as a "
  "layer rather than tidied away.",
  "MAPPED-NOT-BANKED"),

 ("L9", "Classicality -> structure (linear cosmology)",
  "LCDM-shaped by a no-go export, with a computed but non-predictive mu allowance.",
  "The trace-only endpoint is excluded (retraction history on record); the interior family "
  "opens a computed allowance (mu-1 up to ~20% at the loose edge, no floor) that predicts "
  "nothing; the framework's own no-pin lemma closes route R3 as classifier. The two "
  "owed-or-retired calcs (TT-auto rigorous; xi_ij) live at this layer's edge.",
  ["mu_linear", "x_no_pin_theorem", "zeta_interior_family", "founding_h2_R_zeta_bridge",
   "l0_r2_exact_unique_breaker", "l0_r3_payoff_mu_linear"]),

 ("L10", "Structure -> cosmology (dark energy)",
  "The relaxing vacuum as the dark-energy story; DESI's w(z) is the live kill-channel.",
  "Out of equilibrium the medium's slow relaxation is the candidate story (+3: amplitude, "
  "two-scale commitment, single-departure shape -- all priced). The value of Lambda is "
  "UNDETERMINED by every framework in the program, booked as such. The sign computations "
  "(wz sign, w0-wa sign, no-crossing export) are the genuinely non-constructed consequences: "
  "they are independent of the kernel's detailed form, which is what makes them tests.",
  ["rung7_wz", "rung7_w1_wz_map", "rung7_w2_wa_sign", "rung7_w3_nocrossing_export",
   "lambda_undetermined"]),

 ("L11", "Cosmology -> matter",
  "The Standard Model appears NOWHERE in the register. SILENT.",
  "The constitution's assumed-list names 'the SM spectrum' in prose, but no node books it. A "
  "silent layer visible in the hypothesis is worth more than one tidied away.",
  "SILENT"),

 ("L12", "Matter -> observers",
  "How observers arise has never been POSED. UNPOSED.",
  "No node, no map, no artifact. Recorded as the hypothesis's honest end; posing the question "
  "well would itself be a node.",
  "UNPOSED"),
]

# Off-layer nodes: accounted, not links (the generator CHECKS coverage).
OFF_LAYER = {
 "rung8_falsifier": "the tabletop discriminator -- an instrument pointed at the hypothesis, not a layer",
 "method_novelty": "about the program's method, not the universe",
 "founding_h3_doubleslit_anchor": "deferred anchor (disposition: deferred)",
 "info_i1_renorm_as_information": "information-principle triplet: generic half",
 "info_i2_beyond_standard_bridge": "information-principle triplet: screened-refuted",
 "info_i3_distinct_consequence": "information-principle triplet: moot",
 "l0_r1_redundancy_exists": "frontier-3 generic half (its crux nodes sit at L9)",
 "u1_form_universality": "about the FRAMEWORK's form, not a layer",
 "passivity_channel_diagonal": "frame-free linear-response mathematics, not a stage of the story",
 "emergence_chain": "the chain artifact itself -- tripped this same coverage guard before, which is the guard working",
}

# ================================ PART 1 (authored) ================================
ONTOLOGY = (
 "GRUT proposes, in one sentence: **the universe behaves as a finite-memory responsive medium** "
 "-- perturbations relax through a kernel that remembers, and the familiar structures "
 "(dissipation, thermality, the gravitational stiff limit, the quantum reduced dynamics) are "
 "limits of that response rather than independent posits. "
 "The hypothesis is CONDITIONAL and its ontology is STIPULATED, not derived: the medium "
 "response is the entry price (+4 founding node, +1 ontology stance, +1 time-translation "
 "flow), the first two rungs (distinction, system/bath) are open fences, and quantum mechanics "
 "is imported (+2) rather than emergent. What is GRUT's own is the middle: the memory kernel "
 "and its consequences. What is imported is priced and listed in Part 3. Nothing here is "
 "claimed to follow from nothing."
)

DECISIVE_TEST = (
 "The hypothesis's non-constructed consequence under test is the SINGLE-POLE structure "
 "(L4): the kernel's pole-vs-cut question, executed as rung8_falsifier / the Class-C "
 "calculation. The sign exports (wz sign, w0-wa sign, no-crossing, L10) are the second "
 "family of genuine tests: they are independent of the kernel's detailed form. A cut-class "
 "answer, or a measured sign against these exports, refutes layers -- this is what 'could be "
 "wrong' concretely means here."
)


# ================================ GENERATED machinery ================================

def _status(c):
    bits = [c["tier"]]
    d = c.get("ledger_delta", 0)
    if isinstance(d, int) and d:
        bits.append(f"{d:+d}")
    if c.get("disposition"):
        bits.append(f"[{c['disposition']}]")
    if c.get("grut_standing") == "borrowed":
        bits.append("(borrowed)")
    return " ".join(bits)


def _layer_grade(claims):
    """Mechanical layer summary. A layer with NO shown/derived/derived-pending covering claim
    is TO-DERIVE -- printed by the generator, not by prose."""
    if claims == "SILENT":
        return "SILENT -- no register node covers this layer"
    if claims == "UNPOSED":
        return "UNPOSED -- the question has never been asked in the register"
    if claims == "MAPPED-NOT-BANKED":
        return "MAPPED, NOT BANKED -- prose artifacts only; zero register nodes; NOT DERIVED"
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
    order = ["original-result", "derived-pending", "priced-import", "adopted-stance",
             "open", "borrowed"]
    grade = " + ".join(k for k in order if k in kinds)
    # the laundering guard: a layer is NOT-DERIVED unless something derived actually covers it.
    # TO-DERIVE = declared open (a fence); ASSUMED-ONLY = priced imports/stances (never derived).
    if not ({"original-result", "derived-pending"} & kinds):
        if "open" in kinds:
            grade = "TO-DERIVE (" + grade + ")" if grade else "TO-DERIVE"
        else:
            grade = "ASSUMED-ONLY (" + grade + ")" if grade else "ASSUMED-ONLY"
    return grade


def generate():
    reg = json.load(open(os.path.join(HERE, "claims.json")))["claims"]
    by = {c["id"]: c for c in reg}
    grut = [c for c in reg if c.get("ledger_scope", "grut") == "grut"]

    # coverage guard: every cited id must exist; every GRUT node accounted for
    cited = set()
    for _k, _t, _tr, _s, ids in LAYERS:
        if isinstance(ids, list):
            for i in ids:
                if i not in by:
                    raise SystemExit(f"hypothesis cites {i!r}, which is not in the register")
                cited.add(i)
    unaccounted = [c["id"] for c in grut
                   if c["id"] not in cited and c["id"] not in OFF_LAYER]
    if unaccounted:
        raise SystemExit(f"GRUT nodes neither in a layer nor declared off-layer: {unaccounted} "
                         f"-- declare them honestly, do not let them vanish")

    L = []
    L.append("# GRUT Emergence Hypothesis\n")
    L.append("> **STATUS: CANDIDATE HYPOTHESIS -- NOT YET A DERIVED THEORY.**\n")
    L.append("*GENERATED by `provenance/emergence_hypothesis.py` from `claims.json`. The "
             "layer->claims mapping is authored (it is the construction); **every status is "
             "generated from the register** and a layer with no derived support is printed "
             "TO-DERIVE mechanically. `--check` diffs against this file. This artifact asserts "
             "no new physics and upgrades nothing.*\n")
    L.append("**The first rung is `u3_split_origin`, not the responsive vacuum.** The disputed "
             "transition is nothing/fundamental ontology -> distinction -> system/bath; the "
             "responsive-medium machinery only begins once that decomposition is warranted, and "
             "it currently is not.\n")

    # PART 1
    L.append("\n## Part 1 -- The ontological hypothesis\n")
    L.append(ONTOLOGY + "\n")

    # PART 2
    L.append("\n## Part 2 -- The derivation chain (layered)\n")
    L.append("Each layer's status is generated. A layer is only as derived as its register "
             "support; a layer with zero derived covering claims prints TO-DERIVE.\n")
    L.append("| layer | transition | status (generated) |")
    L.append("|---|---|---|")
    for key, _t, trans, _s, ids in LAYERS:
        claims = ids if isinstance(ids, str) else [by[i] for i in ids]
        L.append(f"| `{key}` | {trans} | {_layer_grade(claims)} |")
    L.append("")
    for n, (key, title, trans, story, ids) in enumerate(LAYERS, 1):
        claims = ids if isinstance(ids, str) else [by[i] for i in ids]
        L.append(f"\n### {key}. {title}\n")
        L.append(f"**Transition:** {trans}\n")
        L.append(story + "\n")
        L.append(f"**Layer status (generated):** {_layer_grade(claims)}\n")
        if isinstance(claims, list):
            L.append("| register claim | status (generated) |")
            L.append("|---|---|")
            for c in claims:
                L.append(f"| `{c['id']}` | {_status(c)} |")
            L.append("")
    L.append("\n### The decisive test\n")
    L.append(DECISIVE_TEST + "\n")

    # PART 3 -- external inputs, GENERATED from the register
    L.append("\n## Part 3 -- External inputs (what GRUT imports)\n")
    L.append("*Generated mechanically: every GRUT-scope claim with tier `assumed` or "
             "`grut_standing == borrowed`, with its price. This is where the emergence stops "
             "and structure is imported; the largest single import is the quantum limit (+2) "
             "and the low-entropy past (+1).*\n")
    ext = [c for c in grut if c.get("tier") == "assumed" or c.get("grut_standing") == "borrowed"]
    L.append("| node | status (generated) |")
    L.append("|---|---|")
    for c in sorted(ext, key=lambda c: -(c.get("ledger_delta") or 0)):
        L.append(f"| `{c['id']}` | {_status(c)} |")
    L.append("")

    L.append("\n## Off-layer nodes (accounted, not layers)\n")
    L.append("*Every GRUT node is either in a layer above or listed here -- the generator "
              "errors otherwise.*\n")
    L.append("| node | why off-layer |")
    L.append("|---|---|")
    for i, why in sorted(OFF_LAYER.items()):
        L.append(f"| `{i}` | {why} |")
    L.append("")

    L.append("\n## The finding this artifact is built to state\n")
    L.append("**GRUT presently has a candidate hypothesis, not a derived hypothesis.** The "
             "register's own accounting says where the distinction occurs: layers L0-L1 are "
             "open fences (nothing/fundamental ontology -> distinction -> system/bath), L2 is "
             "assumed and priced, L3-L4 are derived-pending on one decisive bath question, and "
             "the quantum limit (L7) is an import (+2) -- the exact place the framework stops "
             "being a theory of emergence and starts importing structure. The research program "
             "this defines is not sector-filling; it is establishing whether a minimal "
             "generative mechanism exists underneath the sectors, beginning at `u3_split_origin`.\n")
    return "\n".join(L)


def main():
    doc = generate()
    if "--check" in sys.argv:
        on_disk = open(OUT).read() if os.path.exists(OUT) else ""
        if on_disk != doc:
            print("DRIFT: GRUT_EMERGENCE_HYPOTHESIS.md does not match the register-generated "
                  "hypothesis. Regenerate (python3 provenance/emergence_hypothesis.py) -- never "
                  "hand-edit the narrative.")
            return 1
        print("hypothesis artifact matches the register (no drift).")
        return 0
    open(OUT, "w").write(doc)
    print(f"GRUT_EMERGENCE_HYPOTHESIS.md written ({len(doc)} chars, {len(LAYERS)} layers).")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
