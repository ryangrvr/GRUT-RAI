"""Tests for foundations_audit/ provenance documents.

Pins the existence and substantive content of the provenance audits.
These are not physics tests; they verify the discipline pattern: every
claimed-derived foundational constant has an audit document tracing
its actual derivation chain, including any historical inaccuracies.
"""

import math
from pathlib import Path

import pytest


REPO_ROOT = Path(__file__).resolve().parents[2]
AUDIT_DIR = REPO_ROOT / "theory" / "foundations_audit"


class TestAuditDirectoryExists:
    def test_directory_present(self):
        assert AUDIT_DIR.is_dir()

    def test_alpha_audit_present(self):
        doc = AUDIT_DIR / "ALPHA_VAC_PROVENANCE.md"
        assert doc.is_file()

    def test_tau_0_audit_present(self):
        doc = AUDIT_DIR / "TAU_0_PROVENANCE.md"
        assert doc.is_file()


class TestAlphaVacAudit:
    def test_substantive_content(self):
        doc = AUDIT_DIR / "ALPHA_VAC_PROVENANCE.md"
        text = doc.read_text(encoding="utf-8")
        assert len(text.splitlines()) > 30
        assert "1/3" in text
        # Should mention the historical back-derivation
        assert "v6.0" in text or "back" in text.lower() or "15.47" in text


class TestTau0Audit:
    def test_substantive_content(self):
        doc = AUDIT_DIR / "TAU_0_PROVENANCE.md"
        text = doc.read_text(encoding="utf-8")
        assert len(text.splitlines()) > 50

    def test_documents_unit_error(self):
        """The audit must surface the 80.8 fg vs 80.8 pg discrepancy."""
        doc = AUDIT_DIR / "TAU_0_PROVENANCE.md"
        text = doc.read_text(encoding="utf-8")
        assert "80.8 pg" in text or "picogram" in text.lower()
        assert "80.8 fg" in text or "femtogram" in text.lower()
        # Must explicitly call out the factor-1000 discrepancy
        assert "1000" in text or "factor" in text.lower()

    def test_documents_formula_inconsistency(self):
        """The audit must surface that ℏl/(Gm²) doesn't give 41.9 Myr."""
        doc = AUDIT_DIR / "TAU_0_PROVENANCE.md"
        text = doc.read_text(encoding="utf-8")
        assert "ℏl/(Gm²)" in text or "ℏ l / (G m²)" in text or "ℏl/(G m²)" in text

    def test_documents_actual_derivation(self):
        """The audit must state the cosmic-baseline 1/(H_0 × 108π) route."""
        doc = AUDIT_DIR / "TAU_0_PROVENANCE.md"
        text = doc.read_text(encoding="utf-8")
        assert "108π" in text or "108pi" in text.lower()
        assert "H_0" in text


class TestNumericalConsistency:
    """Sanity-check the audit's numerical claims."""

    def test_cosmic_baseline_gives_about_41_Myr(self):
        """1/(H_0 × 108π) at H_0 = 70 km/s/Mpc ≈ 41.2 Myr."""
        H_0 = 70 * 1e3 / 3.086e22  # km/s/Mpc → Hz
        S = 108 * math.pi
        tau_0_sec = 1.0 / (H_0 * S)
        year_sec = 3.156e7
        tau_0_Myr = tau_0_sec / (year_sec * 1e6)
        # Within 5% of canonical 41.9 Myr
        assert abs(tau_0_Myr - 41.9) / 41.9 < 0.05

    def test_codebase_uses_picogram_mass(self):
        """The codebase's gold-benchmark mass is 80.8e-15 kg = 80.8 pg.

        This pins the audit's central finding that 'fg' in some
        documentation should be 'pg'."""
        # noise_kernel.py and other files use 80.8e-15 kg
        from pathlib import Path
        nk = REPO_ROOT / "grut" / "foundation" / "noise_kernel.py"
        text = nk.read_text(encoding="utf-8")
        assert "80.8e-15" in text or "8.08e-14" in text

    def test_lambda_grav_at_pg_gives_689_Hz(self):
        """With m = 80.8 pg, gold density 19300 kg/m³, l = R = 1 μm,
        Λ_grav ≈ 689 Hz."""
        G = 6.674e-11
        HBAR = 1.055e-34
        m = 80.8e-15  # pg
        rho = 19300
        l = 1e-6
        V = m / rho
        R = (3 * V / (4 * math.pi)) ** (1 / 3)
        ratio = l / R
        S = min(1.0, ratio**3 / 6.0)
        Lambda = G * m**2 * S / (HBAR * l)
        assert 680 < Lambda < 700

    def test_lambda_grav_at_fg_does_not_give_689_Hz(self):
        """With m = 80.8 fg (the doc's stated value), Λ_grav ≈ 4 mHz —
        confirming the unit error."""
        G = 6.674e-11
        HBAR = 1.055e-34
        m = 80.8e-18  # fg
        rho = 19300
        l = 1e-6
        V = m / rho
        R = (3 * V / (4 * math.pi)) ** (1 / 3)
        ratio = l / R
        S = min(1.0, ratio**3 / 6.0)
        Lambda = G * m**2 * S / (HBAR * l)
        # Should be milliHz, not 689 Hz
        assert Lambda < 0.01

    def test_naive_tau_formula_does_not_give_41_Myr(self):
        """ℏl/(Gm²) at gold-benchmark parameters gives microseconds,
        not 41.9 Myr — confirming the formula is wrong."""
        G = 6.674e-11
        HBAR = 1.055e-34
        m = 80.8e-15  # pg
        l = 1e-6
        tau_0_naive = HBAR * l / (G * m**2)
        year_sec = 3.156e7
        tau_0_naive_Myr = tau_0_naive / (year_sec * 1e6)
        # Should be ~ 10⁻¹⁸ Myr (microseconds), not 41.9 Myr
        assert tau_0_naive_Myr < 1e-10


class TestRegistryReflectsAudit:
    """The registry's tau_0_derivation claim should reflect the audit
    findings."""

    def test_tau_0_claim_references_audit(self):
        from grut.toe.registry import by_id
        c = by_id("tau_0_derivation")
        refs_text = " ".join(c.refs)
        assert "TAU_0_PROVENANCE" in refs_text or "foundations_audit" in refs_text

    def test_tau_0_claim_uses_posited_framing(self):
        from grut.toe.registry import by_id
        c = by_id("tau_0_derivation")
        # Claim statement should use POSITED/posited or anchored
        # framing rather than "DERIVED from gold benchmark"
        assert "POSITED" in c.statement or "anchor" in c.statement.lower()

    def test_tau_0_claim_acknowledges_audit_correction(self):
        from grut.toe.registry import by_id
        c = by_id("tau_0_derivation")
        notes = c.notes or ""
        assert "audit" in notes.lower() or "corrected" in notes.lower()


class TestClosureProtocolDocstring:
    """The closure_protocol's TAU_0_SEC docstring should reflect the audit."""

    def test_docstring_mentions_two_anchors(self):
        from grut.foundation import closure_protocol
        # Get the module's source to check the docstring on TAU_0_SEC
        import inspect
        source = inspect.getsource(closure_protocol)
        # Should mention cosmic-baseline AND Bullet Cluster
        assert "cosmic-baseline" in source.lower() or "1/(H_0" in source
        assert "Bullet" in source

    def test_docstring_acknowledges_audit_correction(self):
        from grut.foundation import closure_protocol
        import inspect
        source = inspect.getsource(closure_protocol)
        assert (
            "audit" in source.lower()
            or "POSITED" in source
            or "TAU_0_PROVENANCE" in source
        )
