"""Render the CURRENT-STATE block of STATE.md and README.md from CURRENT_STATE.json.

The block sits between the markers below. Everything outside the markers
(historical banners included) is left untouched. Run after every edit of
CURRENT_STATE.json; provenance/test_current_state_sync.py fails if a block is
stale.

    python3 provenance/emit_current_state.py
"""
import json
import os

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
BEGIN = "<!-- CURRENT-STATE:BEGIN (rendered from CURRENT_STATE.json by provenance/emit_current_state.py; do not edit by hand) -->"
END = "<!-- CURRENT-STATE:END -->"
DOCS = ["STATE.md", "README.md"]


def render(s):
    l0 = s["program_status"]["level0"]
    fl = l0["formulability_floor"]
    labels = " · ".join(f"{k} {v}" for k, v in fl["labels"].items())
    hs = s["hard_stop"]
    stop = ("**HARD STOP active** — " if hs["active"] else "No hard stop active. ") + hs["note"]
    prb = s["public_record_boundary"]
    lines = [
        BEGIN,
        f"> **CURRENT BOUNDARY {s['as_of_date']} — source of truth: [`CURRENT_STATE.json`](CURRENT_STATE.json).**",
        f"> Canonical repository `{s['canonical_repository']}`; active research branch "
        f"`{s['active_research_branch']}` (state recorded through `{s['head_commit_at_sync']['commit']}`).",
        f"> - **v4:** {s['program_status']['v4']['status']} (`{s['program_status']['v4']['record']}`).",
        f"> - **GR2:** {s['program_status']['gr2']['status']} (`{s['program_status']['gr2']['ruling']}`).",
        f"> - **Level-0:** {l0['status']}. The L0-1 formulability floor is **{fl['status']}** "
        f"(`{fl['deposit']}`): {labels}. Never cite a label without its scope "
        f"(deposit §2).",
        f"> - **Post-floor:** {l0['post_floor']['status']}; new physics runs: {l0['post_floor']['new_physics_runs']}.",
        f"> - **Hard stop:** {stop}",
        f"> - **Public record:** paper DOI {prb['paper_doi']} (snapshot `{prb['snapshot_source_commit']}`, "
        f"{prb['snapshot_date']}), with the dated update of 2026-09-27. Not yet on the public face: "
        + "; ".join(prb["not_yet_on_public_face"]) + ".",
        "> - **Branches:** " + "; ".join(
            f"`{k}` = {v['role']}" for k, v in s["branch_roles"].items() if k != "other_remote_branches")
        + "; all other branches: role not ruled.",
        "> - **Successors:** " + "; ".join(f"{k}" for k in s["successor_list"]["items"])
        + f" (`{s['successor_list']['record']}`); S-7/S-8 are local follow-ups, not the priority front.",
        ">",
        "> Every banner below this block is **historical**.",
        END,
    ]
    return "\n".join(lines)


def apply(text, block):
    if BEGIN in text:
        a = text.index(BEGIN)
        b = text.index(END) + len(END)
        return text[:a] + block + text[b:]
    first_nl = text.index("\n") + 1  # insert right after the H1 title line
    return text[:first_nl] + "\n" + block + "\n" + text[first_nl:]


def main():
    with open(os.path.join(ROOT, "CURRENT_STATE.json")) as f:
        s = json.load(f)
    block = render(s)
    for doc in DOCS:
        p = os.path.join(ROOT, doc)
        with open(p) as f:
            t = f.read()
        n = apply(t, block)
        if n != t:
            with open(p, "w") as f:
                f.write(n)
            print("rendered", doc)


if __name__ == "__main__":
    main()
