"""Standing test: the CURRENT-STATE blocks in STATE.md and README.md match CURRENT_STATE.json."""
import json
import os
import unittest

from emit_current_state import BEGIN, END, DOCS, ROOT, render


class TestCurrentStateSync(unittest.TestCase):
    def test_blocks_match_source(self):
        with open(os.path.join(ROOT, "CURRENT_STATE.json")) as f:
            block = render(json.load(f))
        for doc in DOCS:
            with open(os.path.join(ROOT, doc)) as f:
                text = f.read()
            self.assertIn(BEGIN, text, f"{doc}: missing CURRENT-STATE block")
            got = text[text.index(BEGIN):text.index(END) + len(END)]
            self.assertEqual(got, block, f"{doc}: CURRENT-STATE block is stale; run provenance/emit_current_state.py")

    def test_floor_labels_are_terminal(self):
        with open(os.path.join(ROOT, "CURRENT_STATE.json")) as f:
            s = json.load(f)
        allowed = {"DISCHARGED", "FALSIFIED", "CLASS-SPLIT", "UNFORMULABLE-WITH-DOCUMENTED-REASON"}
        labels = s["program_status"]["level0"]["formulability_floor"]["labels"]
        self.assertEqual(sorted(labels), [f"O-{i}" for i in range(1, 8)])
        for k, v in labels.items():
            self.assertIn(v, allowed, k)


if __name__ == "__main__":
    unittest.main()
