#!/usr/bin/env python3
"""Tests for the KMS / FDT admission gate (gate/kms.py).

Covers:
  - coth() edge branches: x == 0, |x| > 20 (overflow guard), |x| < 1e-8 (1/x limit)
  - T <= 0 is rejected (KMS undefined)
  - length mismatch raises ValueError
  - an FDT-consistent thermal kernel PASSES on an all-zero-safe grid
  - all-zero grid edge: no residuals accumulate, gate passes
  - a deliberately perturbed thermal kernel FAILS with the worst omega reported

Run: python3 gate/test_kms.py   (pure stdlib, unittest)
"""
import os
import sys
import unittest

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from kms import coth, gate  # noqa: E402


def lorentzian_chi(grid):
    """A toy susceptibility with a loss profile: chi(w) = re + i*im."""
    chi = []
    for w in grid:
        im = (w ** 3) / (1.0 + (w / 5.0) ** 2) ** 2
        re = 1.0 / (1.0 + (w / 5.0) ** 2)
        chi.append(complex(re, im))
    return chi


class TestCoth(unittest.TestCase):
    def test_zero_returns_infinity(self):
        self.assertEqual(coth(0.0), float("inf"))
        self.assertEqual(coth(-0.0), float("inf"))  # copysign sign, still inf branch

    def test_large_argument_saturates_to_sign(self):
        self.assertAlmostEqual(coth(25.0), 1.0)
        self.assertAlmostEqual(coth(-25.0), -1.0)

    def test_small_argument_is_one_over_x(self):
        x = 1e-9
        self.assertAlmostEqual(coth(x), 1.0 / x)

    def test_moderate_argument_matches_definition(self):
        import math
        for x in (0.1, 0.5, 1.0, 3.0, -2.0):
            self.assertAlmostEqual(coth(x), 1.0 / math.tanh(x))


class TestGate(unittest.TestCase):
    def setUp(self):
        self.grid = [10 ** (-3 + 6 * i / 400) for i in range(401)]
        self.T = 2.0
        self.chi = lorentzian_chi(self.grid)
        self.thermal = [coth(w / (2 * self.T)) * (c - c.conjugate())
                        for w, c in zip(self.grid, self.chi)]

    def test_thermal_kernel_passes(self):
        r = gate(self.grid, self.chi, self.thermal, self.T)
        self.assertTrue(r["passed"], r["reason"])
        self.assertLessEqual(r["max_residual"], 1e-6)

    def test_white_noise_kernel_fails(self):
        white = [complex(0.0, 2.0) for _ in self.grid]
        r = gate(self.grid, self.chi, white, self.T)
        self.assertFalse(r["passed"])

    def test_perturbed_thermal_kernel_fails_and_reports_worst_omega(self):
        perturbed = list(self.thermal)
        perturbed[137] = perturbed[137] * 1.1  # 10% spike at one frequency
        r = gate(self.grid, self.chi, perturbed, self.T)
        self.assertFalse(r["passed"])
        self.assertIsNotNone(r["worst_omega"])
        self.assertGreater(r["max_residual"], 1e-6)

    def test_negative_temperature_rejected(self):
        r = gate(self.grid, self.chi, self.thermal, -1.0)
        self.assertFalse(r["passed"])
        self.assertEqual(r["worst_omega"], None)
        self.assertIn("T<=0", r["reason"])

    def test_zero_temperature_rejected(self):
        r = gate(self.grid, self.chi, self.thermal, 0.0)
        self.assertFalse(r["passed"])

    def test_length_mismatch_raises(self):
        with self.assertRaises(ValueError):
            gate(self.grid[:-1], self.chi, self.thermal, self.T)
        with self.assertRaises(ValueError):
            gate(self.grid, self.chi[:-1], self.thermal, self.T)

    def test_all_zero_grid_passes_with_zero_residual(self):
        # No frequencies to compare (omega=0 entries are skipped): residual stays 0
        r = gate([0.0, 0.0, 0.0], [0j, 0j, 0j], [0j, 0j, 0j], self.T)
        self.assertTrue(r["passed"])
        self.assertEqual(r["max_residual"], 0.0)
        self.assertIsNone(r["worst_omega"])


if __name__ == "__main__":
    unittest.main(verbosity=2)
