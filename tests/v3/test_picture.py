"""Tests for the GRUT v3 corrected physical picture (grut.v3.picture).

Locks the v3 foundation: the picture is internally consistent, faithfully
inherits the verified backend, asserts linear cosmology = ΛCDM (NOT the
ruled-out enhancement), and exposes the forward chain (the ToE spine).
"""
from grut.v3 import picture as P
from grut.foundation.organizing_structure import MU_LINEAR


def test_all_verify_legs_pass():
    r = P.verify()
    failed = [k for k, v in r.items() if not v]
    assert not failed, f"v3 picture verify legs failed: {failed}"


def test_forward_chain_is_six_ordered_steps():
    fc = P.forward_chain()
    assert len(fc) == 6
    assert [s["step"][0] for s in fc] == list("123456")
    for s in fc:
        assert s["what"] and s["status"] and s["inherits"]


def test_linear_cosmology_is_lcdm():
    # the v3 picture must carry μ_linear = 1 (ΛCDM), not a linear enhancement
    assert MU_LINEAR == 1


def test_linear_enhancement_is_ruled_out_in_boundary():
    assert any("RULED OUT" in b["consequence"] for b in P.BOUNDARY)


def test_pillars_inherited_correctly():
    assert P.PILLARS["Q_ctp_unitarity"] == "proven"
    assert P.PILLARS["F_finite_memory"] == "postulated"
    assert P.PILLARS["D_adiabatic_dilatation"].startswith("conjectured")


def test_dark_matter_mechanism_is_closed():
    # The dark-MATTER mechanism search is exhausted (C5a profile theorem, Test 06); it is no
    # longer an open frontier, and it is not resurrected as a linear channel.
    assert P.DARK_SECTOR_STATUS.startswith("CLOSED")
    assert not any(("C5a" in f or "Ω_dm" in f or "dark-matter" in f.lower())
                   for f in P.OPEN_FRONTIERS)


def test_summary_states_the_picture():
    s = P.summary()
    assert "ΛCDM" in s and "L0" in s and "redundancy" in s
