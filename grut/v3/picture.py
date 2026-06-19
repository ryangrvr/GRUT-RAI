"""GRUT v3 — the corrected physical picture (operative root).

The launchpad for the v3 Theory-of-Everything path. This module does NOT
re-derive the backend; it ASSEMBLES the corrected physical picture from the
verified v2 backend (inherited at tag `v2-final`) under the v3 organizing
principle, with the v2 over-claims removed.

THE PICTURE IN ONE LINE
    GRUT is general relativity's long-wavelength rescaling redundancy, broken
    in a controlled way by exactly one scale L0 = c·τ0 ≈ 12.85 Mpc — the shape
    by which a mass breaks scale invariance.

THE FORWARD CHAIN (the v3 spine; full prose in theory/GRUT_V3.md)
    Q (CTP unitarity) → F (finite memory) → boundary (the no-gos)
      → organizing principle (F breaks D) → emergent universe → open frontiers

Sources of truth: theory/GRUT_V3_ORGANIZING_STRUCTURE.md,
theory/V2_TO_V3_SYNTHESIS.md, theory/PROJECTOR_CONSISTENCY_NOGO.md, and the
inherited modules imported below.
"""
from __future__ import annotations

from fractions import Fraction
from typing import Dict, List

# --- inherited, verified backend anchors (the "inherit the backend" link) ---
from grut.foundation.closure_protocol import ALPHA_VAC, R_REFRACTIVE, TAU_0_MYR
from grut.foundation.anomaly import S_CTP
from grut.foundation import organizing_structure as OS


# ─────────────────────────────────────────────────────────────────────
# The two pillars + the bridge (inherited verbatim from organizing_structure)
# ─────────────────────────────────────────────────────────────────────
PILLARS: Dict[str, str] = dict(OS.PILLARS)
#   Q_ctp_unitarity            : "proven"
#   F_finite_memory            : "postulated"
#   D_adiabatic_dilatation     : "conjectured_bridge_breaking_established"  (F breaks D)


# ─────────────────────────────────────────────────────────────────────
# The forward chain — the v3 spine, each step grounded in the backend
# ─────────────────────────────────────────────────────────────────────
FORWARD_CHAIN: List[Dict[str, str]] = [
    {
        "step": "1. responsive vacuum (Q)",
        "what": "Physics is the response to REALIZED differences: the closed-time-path "
                "(in-in) action vanishes on the classical diagonal, S_IF[φ_+=φ_-]=0; the "
                "physical response is δS_IF/δφ_q|_{q=0}.",
        "status": "proven (theorem of the formalism)",
        "inherits": "grut.foundation.ctp_action, grut.foundation.axioms",
    },
    {
        "step": "2. finite memory (F)",
        "what": "A single-pole susceptibility χ(ω)=1/(1−iωτ0) makes the response causal, "
                "bounded, and GR-recovering. One dimensionful input: τ0 ≈ 41.9 Myr.",
        "status": "postulated (τ0 anchored)",
        "inherits": "grut.foundation.closure_protocol",
    },
    {
        "step": "3. the boundary operator (the no-gos)",
        "what": "What the vacuum is FORBIDDEN to respond to: pure-gauge/adiabatic modes "
                "(⇒ μ_linear=1), bare (gauge-dependent) density, unbounded/infinite response. "
                "The no-gos map the shape of the allowed solution space.",
        "status": "derived constraints",
        "inherits": "grut.foundation.organizing_structure; theory/PROJECTOR_CONSISTENCY_NOGO.md §5",
    },
    {
        "step": "4. organizing principle (F breaks D)",
        "what": "The adiabatic spatial-dilatation redundancy D is exact only in the "
                "memoryless (L0→0) limit; finite memory F breaks it for every k≠0 at "
                "O((L0·k_phys)²), non-anomalously (α does not enter). GRUT = the "
                "dilatation-redundant GR limit + controlled breaking by one scale L0.",
        "status": "theorem (outcome B; independently verified)",
        "inherits": "grut.foundation.organizing_structure",
    },
    {
        "step": "5. emergent universe",
        "what": "Linear cosmology = ΛCDM (μ_linear=1, derived). Certified: gravitational "
                "decoherence plateau (~689 Hz), R=√(4/3), η_B≈6.6e-10, background H(z)/BAO, "
                "the cosmological constant as a terminal velocity. The dark-sector "
                "enhancement is RELOCATED out of the linear channel.",
        "status": "derived/certified (linear sector + lab + background)",
        "inherits": "grut.bridge.parameter, grut.foundation.noise_kernel, grut.foundation.anomaly",
    },
    {
        "step": "6. the dark-matter mechanism search is CLOSED; open frontiers lie elsewhere",
        "what": "The dark-MATTER-density mechanism search is exhausted: the linear/dielectric "
                "channel is ruled out (μ_linear=1), C5b (orbital-ω) is refuted (~1/√N), and C5a "
                "(W² second-order) is resolved — right magnitude but wrong radial profile, a "
                "THEOREM tied to locality (Test 06): every local tensor realization gives "
                "ρ_eff∝(Weyl)²∝(ρ−⟨ρ⟩)² — 1/r⁴ in the halo interior, steepening to 1/r⁶ in the "
                "outskirts (exterior tidal), always steeper than the 1/r² a flat-curve halo needs; "
                "shallowing to 1/r² needs the 1/∇² the locality result (no genuine 1/k² pole) "
                "forbids. So GRUT has NO derived dark-matter "
                "mechanism; dark matter is a HOSTED input (with the derived a₀ scale). The "
                "TT/GW (C5c) channel remains as a distinct NON-DM signature (the ~689 Hz "
                "decoherence falsifier), not a clustering mechanism. The GENUINELY open ToE "
                "frontiers are now: the first-principles value of α (4th-order Riegert) and the "
                "L0→0 underlying-redundancy proof. Flavor/Koide is HOSTED.",
        "status": "dark-matter mechanism CLOSED (pending covariant review); live frontiers = α-selection, L0→0",
        "inherits": "theory/GRUT_V3_K2_DERIVATION.md, theory/GRUT_V3_TEST_06_PROFILE_THEOREM.md",
    },
]


# ─────────────────────────────────────────────────────────────────────
# Certified constants (what stands — inherited values, corrected tiers)
# ─────────────────────────────────────────────────────────────────────
CERTIFIED: Dict[str, str] = {
    "alpha_vac": "1/3 — the single dimensionless AXIOM (genuine trace-anomaly result under one "
                 "identification; 4th-order Riegert closure OPEN)",
    "R_refractive": "√(4/3) ≈ 1.1547 — deep-IR gravitational refractive index (derived)",
    "tau_0": "41.9 Myr — the single dimensionful scale (anchored input)",
    "L0": "c·τ0 ≈ 12.85 Mpc — the symmetry-breaking memory length",
    "mu_linear": "1 — linear cosmology = ΛCDM (DERIVED requirement)",
    "S": "108π ≈ 339.3 — CTP path-counting normalization (= 12π/α²)",
    "eta_B": "≈ 6.6e-10 — baryon asymmetry (CTP path asymmetry)",
    "decoherence_plateau": "~689 Hz — gravitational-decoherence plateau (primary tabletop falsifier)",
}


# ─────────────────────────────────────────────────────────────────────
# The boundary operator — forbidden responses (the productive no-gos)
# ─────────────────────────────────────────────────────────────────────
BOUNDARY: List[Dict[str, str]] = [
    {"forbidden": "respond to the pure-gauge adiabatic (separate-universe) mode",
     "consequence": "μ_linear = 1 (linear cosmology = ΛCDM)",
     "basis": "PROJECTOR_CONSISTENCY_NOGO §5 (conformal ⊥ separate-universe at k→0)"},
    {"forbidden": "couple to the bare (gauge-dependent) density",
     "consequence": "only realized (gauge-invariant) structure gravitates",
     "basis": "PROJECTOR_CONSISTENCY_NOGO"},
    {"forbidden": "infinite / unbounded vacuum response",
     "consequence": "finite memory; n_g² ≤ 4/3; GR recovery at high ω",
     "basis": "finite single-pole susceptibility (F)"},
    {"forbidden": "linear refractive enhancement μ→4/3 (the v2 'μ−1=1/3' prediction)",
     "consequence": "RULED OUT — data (low-ℓ ISW ≈2.8×/32σ) + consistency (μ_linear=1)",
     "basis": "Correction #38; CMB_ISW_EQUALITY_FILTER §0.1"},
]


# ─────────────────────────────────────────────────────────────────────
# Open frontiers — the live v3 ToE targets (named, not closed)
# NOTE: the dark-MATTER mechanism is no longer here — it is CLOSED (see DARK_SECTOR_STATUS).
# ─────────────────────────────────────────────────────────────────────
OPEN_FRONTIERS: List[str] = [
    "First-principles value of α=1/3 — the 4th-order Riegert/Paneitz conformal-anomaly computation.",
    "The L0→0 underlying-redundancy proof (that the adiabatic dilatation is a true symmetry of "
    "the full CTP action before memory is switched on).",
    "Standard-Model closure beyond the neutrino hierarchy (Yukawas/CKM/PMNS/Higgs); flavor is hosted.",
    "The TT/GW (C5c) channel as a distinct NON-DM signature (e.g. the ~689 Hz decoherence plateau).",
]

# The dark-MATTER mechanism search — CLOSED (the audit + constructive phase exhausted it).
DARK_SECTOR_STATUS: str = (
    "CLOSED (pending covariant review). The local second-order kernel class is exhausted: linear/"
    "dielectric ruled out (μ_linear=1), C5b refuted (~1/√N), C5a resolved — right magnitude, wrong "
    "profile, a locality THEOREM (Test 06: every local tensor realization gives ρ_eff∝(Weyl)² — 1/r⁴ "
    "interior, 1/r⁶ outskirts, always steeper than a 1/r² halo; shallowing needs the 1/∇² the no-pole "
    "locality result forbids). GRUT has no derived dark-matter "
    "mechanism; dark matter is a HOSTED input (with derived a₀, μ_linear=1=ΛCDM). The only way back is "
    "to overturn a foundational result (locality, the No-Go, the CTP structure, or the profile theorem) "
    "— not to invent a new channel. Records: theory/GRUT_V3_K2_DERIVATION.md, "
    "theory/GRUT_V3_TEST_06_PROFILE_THEOREM.md; registry c5a_weyl_squared_dark_sector (open_negative)."
)


def forward_chain() -> List[Dict[str, str]]:
    """Return the v3 spine as ordered data (the ToE path)."""
    return list(FORWARD_CHAIN)


def summary() -> str:
    """One-paragraph operative statement of the v3 picture."""
    return (
        "GRUT v3: general relativity's long-wavelength rescaling redundancy, broken in a "
        "controlled way by exactly one scale L0 = c·τ0 ≈ 12.85 Mpc. Two pillars — Q (CTP "
        "unitarity, proven) and F (finite memory, postulated); finite memory F is the controlled "
        "breaking of the dilatation redundancy D. Linear cosmology = ΛCDM (μ_linear=1, derived); "
        "the dark-matter mechanism is CLOSED (the local second-order kernel class is exhausted — "
        "C5a's profile failure is a locality theorem; pending covariant review), so dark matter is a "
        "hosted input. α=1/3 is the single dimensionless axiom; flavor is hosted; the live frontiers "
        "are α-selection (4th-order Riegert) and the L0→0 redundancy proof."
    )


def verify() -> dict:
    """Self-test the assembled v3 picture for internal consistency and faithful inheritance."""
    os_legs = OS.verify()
    return {
        # inherited foundation passes all its own checks
        "organizing_structure_verified": all(os_legs.values()),
        # constants inherited and consistent
        "alpha_vac_is_one_third": abs(ALPHA_VAC - 1.0 / 3.0) < 1e-12,
        "R_is_sqrt_4_3": abs(R_REFRACTIVE - (4.0 / 3.0) ** 0.5) < 1e-9,
        "tau_0_is_41p9_Myr": abs(TAU_0_MYR - 41.9) < 1e-9,
        "S_is_108pi": abs(S_CTP - 108.0 * 3.141592653589793) < 1e-6,
        "L0_about_12p85_Mpc": abs(OS.L0_MPC - 12.85) < 0.5,
        "mu_linear_is_one": OS.MU_LINEAR == Fraction(1, 1),
        "outcome_is_B": OS.OUTCOME == "B_broken_by_kernel",
        # pillars faithfully inherited
        "two_pillars_plus_bridge": (
            PILLARS["Q_ctp_unitarity"] == "proven"
            and PILLARS["F_finite_memory"] == "postulated"
            and PILLARS["D_adiabatic_dilatation"].startswith("conjectured")
        ),
        # the picture is structurally complete and ordered
        "forward_chain_has_six_steps": len(FORWARD_CHAIN) == 6,
        "forward_chain_ordered": [s["step"][0] for s in FORWARD_CHAIN] == list("123456"),
        # the picture does NOT resurrect the ruled-out linear enhancement
        "linear_enhancement_marked_ruled_out": any(
            "RULED OUT" in b["consequence"] for b in BOUNDARY
        ),
        # the dark-matter mechanism is positioned as CLOSED (local-kernel class exhausted), not
        # an open search and not resurrected as linear; live frontiers no longer include a DM channel
        "dark_matter_mechanism_closed": DARK_SECTOR_STATUS.startswith("CLOSED"),
        "no_dark_matter_channel_in_open_frontiers": not any(
            ("C5a" in f or "C5b" in f or "Ω_dm" in f or "dark-matter" in f.lower()) for f in OPEN_FRONTIERS
        ),
    }
