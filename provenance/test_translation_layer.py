"""test_translation_layer: the glossary's translation table must exist and stay populated.

The rule 'any banking that coins a term adds its line here in the same commit' is process (not
mechanizable -- coining detection is a judgement); what IS pinnable is that the layer exists, that
the load-bearing dialect terms have lines, and that deleting the table breaks the build rather
than rotting silently. Ruled 2026-08-09 (Part 6): don't stop naming; translate."""
import os
import unittest

HERE = os.path.dirname(os.path.abspath(__file__))
GLOSSARY = os.path.join(HERE, "..", "GLOSSARY.md")

# The terms the overseer named explicitly, plus the ones load-bearing across waves.
REQUIRED = ("F-MAP fence", "earned-under-determined", "horn-conditional forward-only",
            "same-wave firewall", "laundering", "banked", "armed trigger",
            "insertion-contaminated", "blind-safe", "compound (node)", "omission",
            "edge-not-vertex", "no-go export", "D3 deposit")


class TestTranslationLayer(unittest.TestCase):

    def test_the_layer_exists_and_carries_the_required_terms(self):
        body = open(GLOSSARY).read()
        self.assertIn("The translation layer", body)
        self.assertIn("MAINTAINED AS PART OF BANKING", body)
        for term in REQUIRED:
            self.assertIn(f"**{term}**", body,
                          f"the dialect term {term!r} has no plain-English line -- precision that "
                          f"cannot be translated is private language")
