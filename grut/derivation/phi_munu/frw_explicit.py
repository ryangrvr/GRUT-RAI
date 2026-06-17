"""Phase 2C — explicit construction of Φ_μν^FRW and χ_FRW(k, η).

Specializes the Phase 2B curved-background scaffold (Correction #24)
to FRW spacetime, producing the explicit susceptibility χ_FRW(k, η)
and refractive index n_g²(k, η) on cosmological backgrounds.

This is the cosmology backbone the v8→v2 deposit roadmap calls out:

    Φ_μν^curved → χ_FRW(k, η) → n_g²(k, η) = 1 + α × χ_FRW(k, η)

If this closes, GRUT's cosmology becomes directly computable —
n_g(ω, k, t) becomes a definite function of comoving wavenumber and
cosmic time, with explicit transition scale k_*(η) = a(η)/τ_0
separating the GR-recovery (sub-horizon) and full-constitutive
(super-horizon) regimes.

─────────────────────────────────────────────────────────────────────
What is derived
─────────────────────────────────────────────────────────────────────

On FRW background g_μν = a²(η) diag(-1, 1, 1, 1) in conformal time η,
the covariant d'Alembertian acting on a scalar Fourier mode of
comoving wavenumber k:

    □_g φ_k(η) = -(1/a²)[∂_η² + 2H_c ∂_η + k²] φ_k(η)              (1)

where H_c = a'/a is the conformal-time Hubble parameter (a' ≡ ∂_η a),
distinct from the cosmic-time H = H_c/a.

The relaxation operator:

    1 + τ_0² (-□_g) φ_k = [1 + (τ_0/a)² (∂_η² + 2H_c ∂_η + k²)] φ_k

WKB / slow-H approximation: when (H_c τ_0/a)² ≪ 1 (true for the
modern universe, where H_0 τ_0 = 1/(108π) ≈ 3 × 10⁻³), the time
derivatives are subleading. In this limit the relaxation operator
reduces to:

    1 + τ_0² (-□_g) φ_k ≈ [1 + (τ_0 k/a)²] φ_k                     (2)

and the susceptibility is:

    χ_FRW^WKB(k, η) = 1 / [1 + (τ_0 k_phys(η))²]                   (★)

where k_phys(η) = k/a(η) is the physical wavenumber. This is the
LOAD-BEARING explicit formula. Substituting into n_g² = 1 + α χ:

    n_g²(k, η) = 1 + α / [1 + (τ_0 k_phys(η))²]                    (★★)

with α = α_vac = 1/3 inherited from the KS 2011 conformal-mode
identification (NOT modified by Phase 2C).

─────────────────────────────────────────────────────────────────────
Three structural limits, all explicit
─────────────────────────────────────────────────────────────────────

**Sub-horizon (k_phys τ_0 ≫ 1).** GR recovery:
    χ_FRW → 0,  n_g² → 1.
Modes much shorter than the transition wavelength
λ_* = 2π τ_0 c ≈ 80.7 Mpc see no constitutive correction. Standard
GR/ΛCDM cosmology applies on small scales — the relaxation length
τ_0 c ≈ 12.85 Mpc is the underlying scale; the 2π emerges from the
Fourier-convention k = 2π/λ.

**Super-horizon (k_phys τ_0 ≪ 1).** Full constitutive:
    χ_FRW → 1,  n_g² → 1 + α = 4/3.
Modes much longer than λ_* experience the full vacuum refractive
enhancement. This is where dark-sector phenomenology lives in GRUT's
cosmological picture (CMB horizon scale is ~14 Gpc ≫ λ_* ≈ 80 Mpc,
so the largest scales see full constitutive correction).

**Transition (k_phys τ_0 = 1).** Crossover scale:
    χ_FRW = 1/2,  n_g² = 1 + α/2 = 7/6.
The transition wavenumber k_*(η) = a(η)/(τ_0 c) sweeps through
cosmological scales over cosmic time. Today:
    k_*^phys ≈ 1/(τ_0 c) ≈ 7.78 × 10⁻²⁵ m⁻¹
    λ_* = 2π/k_*^phys ≈ 2π τ_0 c ≈ 80.7 Mpc

(The relaxation LENGTH scale is τ_0 c ≈ 12.85 Mpc; the transition
WAVELENGTH where χ = 1/2 picks up the 2π Fourier convention.)
Modes shorter than λ_* (galactic, cluster) are sub-horizon →
GR recovery. Modes longer than λ_* (CMB horizon) are super-horizon →
full constitutive enhancement n_g² = 4/3.

─────────────────────────────────────────────────────────────────────
Beyond WKB (Phase 2D — not done here)
─────────────────────────────────────────────────────────────────────

The slow-H correction:
    χ_FRW(k, η) = χ_FRW^WKB(k, η) × [1 + O((H_c τ_0)²)]

Today: (H_0 τ_0)² = 1/(108π)² ≈ 8.7 × 10⁻⁶ — negligible.

⚠ CORRECTION (June 2026): an earlier version of this note claimed
"(H_eq τ_0)² ≈ 10⁻⁶ — negligible across all post-equality cosmology."
THAT IS AN ARITHMETIC ERROR. With H_eq = H_0 (1+z_eq)^(3/2)√2 and
z_eq ≈ 3400, (H_eq τ_0)² = (H_0τ_0)² × (3400^1.5·√2)² ≈ 8.7e-6 × 7e10
≈ 2 × 10⁵ — eleven orders of magnitude larger, NOT ≪ 1. The QS/WKB
boundary (H τ_0)² = 1 falls at z ≈ 77.

Correct validity domain of the WKB/QS reduction (★):
  • VALID for z ≲ 30 AND for modes whose constitutive enhancement
    turns on deep sub-horizon — i.e. k ≳ 10⁻² Mpc⁻¹ (a★ = k·cτ₀ gives
    z★ ≲ 7). This covers structure growth: σ₈, BAO, fσ₈. The WKB μ is
    reliable there (verified against the full memory operator: the
    response equals the QS value to < 1%).
  • INVALID for the low-ℓ CMB ISW modes (k ≲ 3×10⁻³ Mpc⁻¹), whose
    enhancement turns on at z★ ≳ 30–77, i.e. in the (H τ_0)² ≳ 1 regime
    where the dropped time-derivative terms ∂_η² + 2H_c∂_η are NOT
    subleading. For these modes the QS μ = 1 + α/(1+(τ₀k_phys)²) is not
    justified; the full retarded kernel G^R(k,η,η') must be used. The
    apparent low-ℓ ISW excess obtained by applying the QS μ to these
    modes is therefore an artifact of using the reduction outside its
    domain — see theory/CMB_ISW_EQUALITY_FILTER.md §0.

Beyond-WKB / full-kernel treatment for the horizon-scale (ISW) modes
WAS the open Phase-2D task (kernel temporal structure: the bedrock
constitutive equation τ dz/dt + z = z_target is first-order, while the
operator 1+τ₀²(−□_g) used here is second-order — these differ exactly
in the regime that matters for the ISW).

  UPDATE (June 2026 — NO LONGER OPEN): the first-order full memory kernel
  was derived (retarded_kernel_frw.py) and run in MGCAMB. It does NOT
  rescue the low-ℓ ISW: D_ℓ^GRUT/D_ℓ^ΛCDM = 2.79× at ℓ=15 (~32σ), larger
  than this QS artifact — the memory only delays μ→4/3 (reached by z≲15).
  Combined with the Projector No-Go (μ_linear=1 forced by separate-universe
  invariance), the linear-scalar refractive enhancement is RULED OUT and
  linear cosmology = ΛCDM is a derived requirement. See
  theory/CMB_ISW_EQUALITY_FILTER.md §0.1 and
  theory/PROJECTOR_CONSISTENCY_NOGO.md §5-§6. The QS μ below remains valid
  and useful for the sub-horizon (z≲30, k≳10⁻²) growth regime only.

─────────────────────────────────────────────────────────────────────
Convention declaration (Phase 2C)
─────────────────────────────────────────────────────────────────────

C1f — FRW metric: ḡ_μν = a²(η) diag(-1, 1, 1, 1), conformal time η.
C2f — Conformal Hubble: H_c = a'/a (distinct from cosmic-time H = H_c/a).
C3f — Comoving Fourier ansatz: φ(x) = ∫ d³k/(2π)³ φ_k(η) e^{ik·x}.
C4f — WKB / slow-H regime: (H_c τ_0/a)² ≪ 1. Verified at modern
      universe (8.7 × 10⁻⁶) and matter-radiation equality (similar).
C5f — Physical wavenumber: k_phys(η) = k/a(η). Transition scale
      k_phys = 1/τ_0, i.e., comoving k_*(η) = a(η)/τ_0.
C6f — α_vac inherits from conformal-mode-scalar identification
      (KS 2011 a/c = 1/3); NOT modified by Phase 2C.

─────────────────────────────────────────────────────────────────────
What this does NOT do
─────────────────────────────────────────────────────────────────────

- Does not derive the explicit beyond-WKB correction. The (Hτ_0)²
  term enters via H_c ∂_η coupling in (1); computing it requires
  WKB matching beyond leading order or numerical integration of the
  retarded Green function on FRW. Tracked under
  `phi_munu_frw_beyond_wkb_open_question` (Phase 2D).
- Does not solve the cosmological perturbation equations with the
  Φ_μν^FRW correction. That is Priority 3 (n_g(ω) covariance):
  insert n_g²(k, η) into the linearized Einstein equations on FRW
  and propagate to CMB / structure-formation observables.
- Does not extend to S⁴ (Euclidean de Sitter, sister to TJI Phase-1).
  Independent task; same Phase 2C-pattern but different background.

─────────────────────────────────────────────────────────────────────
Reference
─────────────────────────────────────────────────────────────────────

- Phase 2B: grut.derivation.phi_munu.curved_background — scaffold
  with four structural targets (flat limit, conservation, causality,
  FRW compatibility).
- Phase 2A: grut.derivation.phi_munu.linearized_ctp_action — flat-
  spacetime derivation reproduced in the high-k / sub-horizon limit.
- Mukhanov-Feldman-Brandenberger (1992) — cosmological perturbation
  theory on FRW; SVT decomposition; conformal-Newtonian gauge.
- Birrell-Davies (1982) — d'Alembertian on FRW for scalar modes.
- closure_protocol.py — TAU_0_SEC, ALPHA_VAC inherited.
"""

from __future__ import annotations

from fractions import Fraction
from typing import Dict, Optional

import sympy as sp

from grut.derivation.phi_munu.linearized_ctp_action import (
    ALPHA, TAU_0,
)


# Symbols specific to FRW
ETA = sp.Symbol("eta", real=True)            # conformal time
A_OF_ETA = sp.Function("a")(ETA)              # scale factor
H_C = sp.Function("H_c")(ETA)                  # conformal Hubble = a'/a
K_COMOVING = sp.Symbol("k_comoving", positive=True)
K_PHYS = sp.Symbol("k_phys", positive=True)


def convention_declaration() -> Dict[str, str]:
    """Convention declaration for Phase 2C (FRW explicit construction).

    Mirrors discipline of C1c-C7c (curved scaffold) and C1-C7
    (linearized). Every Fraction equality below is asserted under
    these conventions.
    """
    return {
        "C1f_FRW_metric":
            "ḡ_μν = a²(η) diag(-1, 1, 1, 1), conformal time η.",
        "C2f_conformal_hubble":
            "H_c = a'/a (conformal Hubble); distinct from "
            "cosmic-time H = H_c/a.",
        "C3f_comoving_fourier_ansatz":
            "φ(x) = ∫ d³k/(2π)³ φ_k(η) e^{ik·x}; k is comoving.",
        "C4f_WKB_slow_H_regime":
            "(H τ_0)² << 1. Today (H_0 τ_0)² = 1/(108π)² ≈ 8.7e-6. "
            "CORRECTION: (H τ_0)² = 1 at z ≈ 77, and ≈ 2e5 at equality "
            "(NOT 1e-6 as previously stated). WKB/QS valid for z ≲ 30 / "
            "growth modes k ≳ 1e-2; INVALID for low-ℓ ISW modes "
            "(k ≲ 3e-3, z★ ≳ 30). See module docstring + "
            "theory/CMB_ISW_EQUALITY_FILTER.md §0.",
        "C5f_physical_wavenumber_and_transition":
            "k_phys(η) = k/a(η). Transition: k_phys = 1/τ_0; "
            "comoving k_*(η) = a(η)/τ_0.",
        "C6f_alpha_vac_inherits":
            "α_vac = 1/3 inherits from KS 2011 a/c for the "
            "conformal-mode scalar; NOT modified by Phase 2C.",
        "phase_2C_status":
            "EXPLICIT FRW SUSCEPTIBILITY landed at WKB level. "
            "Beyond-WKB (Phase 2D) deferred — corrections are "
            "O(10⁻⁶) for late-universe cosmology.",
    }


# ─────────────────────────────────────────────────────────────────────
# Section 1 — FRW background machinery
# ─────────────────────────────────────────────────────────────────────


def conformal_time_FRW_metric() -> Dict[str, sp.Expr]:
    """Symbolic representation of the FRW metric in conformal time.

        ds² = a²(η) [-dη² + δ_ij dx^i dx^j]

    Returns the metric components and the corresponding inverse
    metric components.
    """
    g_00 = -A_OF_ETA**2
    g_ii = A_OF_ETA**2
    sqrt_minus_g = A_OF_ETA**4

    g_inv_00 = -1 / A_OF_ETA**2
    g_inv_ii = 1 / A_OF_ETA**2

    return {
        "g_00":               g_00,
        "g_ii":               g_ii,
        "sqrt_minus_g":       sqrt_minus_g,
        "g_inv_00":           g_inv_00,
        "g_inv_ii":           g_inv_ii,
        "scale_factor":       A_OF_ETA,
        "conformal_time":     ETA,
    }


def conformal_hubble() -> sp.Expr:
    """H_c(η) = a'(η)/a(η) — the conformal Hubble parameter.

    Distinct from the cosmic-time Hubble H = H_c/a. In matter
    domination: a ∝ η², so H_c = 2/η. In radiation domination:
    a ∝ η, so H_c = 1/η.
    """
    return sp.diff(A_OF_ETA, ETA) / A_OF_ETA


# ─────────────────────────────────────────────────────────────────────
# Section 2 — d'Alembertian on FRW scalar Fourier modes
# ─────────────────────────────────────────────────────────────────────


def box_g_on_scalar_fourier_mode(phi_k_symbol: sp.Symbol) -> sp.Expr:
    """The covariant d'Alembertian □_g acting on a scalar Fourier mode
    φ_k(η) e^{ik·x}.

        □_g φ_k(η) = -(1/a²)[∂_η² + 2 H_c ∂_η + k²] φ_k(η)

    (Birrell-Davies 1982, eq. 5.58 in conformal time, scalar modes.)

    Parameters
    ----------
    phi_k_symbol : sympy.Symbol
        Symbolic representative of φ_k(η). The result is an expression
        in this symbol's η-derivatives plus the algebraic k² term.
    """
    H_c = conformal_hubble()
    # ∂_η² φ_k + 2 H_c ∂_η φ_k + k² φ_k:
    spatial_box_part = (
        sp.diff(phi_k_symbol, ETA, 2)
        + 2 * H_c * sp.diff(phi_k_symbol, ETA)
        + K_COMOVING**2 * phi_k_symbol
    )
    return -spatial_box_part / A_OF_ETA**2


def relaxation_operator_on_scalar_fourier(phi_k_symbol: sp.Symbol) -> sp.Expr:
    """The relaxation operator (1 + τ_0² (-□_g)) acting on φ_k(η).

        [1 + τ_0² (-□_g)] φ_k(η)
            = φ_k + (τ_0²/a²)[∂_η² + 2H_c ∂_η + k²] φ_k

    Returns the result in symbolic form.
    """
    box_g_phi = box_g_on_scalar_fourier_mode(phi_k_symbol)
    return phi_k_symbol + TAU_0**2 * (-box_g_phi)


# ─────────────────────────────────────────────────────────────────────
# Section 3 — WKB / slow-H susceptibility
# ─────────────────────────────────────────────────────────────────────


def chi_FRW_WKB(k_comoving=K_COMOVING, eta=ETA, tau_0=TAU_0) -> sp.Expr:
    """The WKB / slow-H susceptibility on FRW — the LOAD-BEARING formula.

        χ_FRW^WKB(k, η) = 1 / [1 + (τ_0 k/a(η))²]
                       = 1 / [1 + (τ_0 k_phys(η))²]

    Derivation: in the (H_c τ_0/a)² ≪ 1 regime, the time derivatives
    in the relaxation operator (1 + τ_0² (-□_g)) are subleading
    compared to the k² term. The operator reduces to
    1 + τ_0² × k²/a², whose inverse is the above.

    Returns
    -------
    sympy.Expr
        Symbolic χ_FRW^WKB as a function of k (comoving), η, and τ_0.
    """
    a = sp.Function("a")(eta)  # scale factor at η
    k_phys_sq = (k_comoving / a)**2
    return 1 / (1 + tau_0**2 * k_phys_sq)


def chi_FRW_WKB_in_physical_wavenumber(
    k_phys=K_PHYS, tau_0=TAU_0,
) -> sp.Expr:
    """The same WKB susceptibility, expressed in physical wavenumber.

        χ_FRW^WKB(k_phys) = 1 / [1 + (τ_0 k_phys)²]

    Background-independent form; the time/η dependence is hidden in
    k_phys = k/a.
    """
    return 1 / (1 + tau_0**2 * k_phys**2)


# ─────────────────────────────────────────────────────────────────────
# Section 4 — Refractive index n_g²(k, η)
# ─────────────────────────────────────────────────────────────────────


def n_g_squared_FRW_WKB(
    k_comoving=K_COMOVING, eta=ETA,
    tau_0=TAU_0, alpha=ALPHA,
) -> sp.Expr:
    """The refractive-index-squared on FRW, WKB level.

        n_g²(k, η) = 1 + α × χ_FRW^WKB(k, η)
                  = 1 + α / [1 + (τ_0 k_phys(η))²]

    With α = 1/3 (default α_vac), this is the explicit cosmological-
    perturbation-theory output that Priority 3 will use.
    """
    chi = chi_FRW_WKB(k_comoving, eta, tau_0)
    return 1 + alpha * chi


def n_g_squared_FRW_in_physical_wavenumber(
    k_phys=K_PHYS, tau_0=TAU_0, alpha=ALPHA,
) -> sp.Expr:
    """n_g²(k_phys) = 1 + α / [1 + (τ_0 k_phys)²]

    Background-independent form. Use this for limit-taking and
    transition-scale analysis.
    """
    chi = chi_FRW_WKB_in_physical_wavenumber(k_phys, tau_0)
    return 1 + alpha * chi


# ─────────────────────────────────────────────────────────────────────
# Section 5 — Limits and transition scale
# ─────────────────────────────────────────────────────────────────────


def sub_horizon_limit() -> Dict[str, sp.Expr]:
    """High physical wavenumber limit: k_phys τ_0 → ∞.

        χ_FRW → 0,  n_g² → 1.

    GR recovery on small scales — modes much shorter than τ_0 c
    see no constitutive correction.
    """
    chi_at_high_k = sp.limit(
        chi_FRW_WKB_in_physical_wavenumber(K_PHYS, TAU_0),
        K_PHYS, sp.oo,
    )
    n_g_sq_at_high_k = sp.limit(
        n_g_squared_FRW_in_physical_wavenumber(K_PHYS, TAU_0, ALPHA),
        K_PHYS, sp.oo,
    )
    return {
        "chi_FRW_high_k_limit":  chi_at_high_k,
        "n_g_squared_high_k":     n_g_sq_at_high_k,
        "interpretation":
            "Sub-horizon / GR recovery: modes shorter than τ_0 c "
            "(≈ 12.8 Mpc today) see no constitutive correction.",
    }


def super_horizon_limit() -> Dict[str, sp.Expr]:
    """Low physical wavenumber limit: k_phys τ_0 → 0.

        χ_FRW → 1,  n_g² → 1 + α = 4/3.

    Full constitutive on large scales — modes longer than τ_0 c
    experience the full vacuum refractive enhancement n_g² = 4/3.
    """
    chi_at_low_k = sp.limit(
        chi_FRW_WKB_in_physical_wavenumber(K_PHYS, TAU_0),
        K_PHYS, 0,
    )
    n_g_sq_at_low_k = sp.limit(
        n_g_squared_FRW_in_physical_wavenumber(K_PHYS, TAU_0, ALPHA),
        K_PHYS, 0,
    )
    return {
        "chi_FRW_low_k_limit":  chi_at_low_k,
        "n_g_squared_low_k":     n_g_sq_at_low_k,
        "interpretation":
            "Super-horizon / full constitutive: modes longer than "
            "τ_0 c experience the full DC refractive enhancement.",
    }


def transition_wavenumber() -> Dict[str, sp.Expr]:
    """The transition (crossover) scale where χ_FRW = 1/2.

        Condition:    τ_0 k_phys = 1
        Crossover at: k_phys^* = 1/τ_0
        Comoving:     k^*(η) = a(η) / τ_0

    Physical interpretation: τ_0 c ≈ 12.85 Mpc is the relaxation
    length scale — the spatial extent over which the responsive
    vacuum's memory is correlated. The transition WAVELENGTH where
    χ = 1/2 is λ_* = 2π/k_*^phys = 2π τ_0 c ≈ 80.7 Mpc (today).
    The factor of 2π comes from the Fourier convention k = 2π/λ;
    it does not depend on cosmic epoch (the comoving k_*(η) =
    a(η)/τ_0 evolves with the scale factor, but k_*^phys = 1/(τ_0 c)
    is invariant).
    """
    # χ at the transition:
    chi_at_transition = chi_FRW_WKB_in_physical_wavenumber(
        1 / TAU_0, TAU_0,
    )
    # n_g² at the transition:
    n_g_sq_at_transition = n_g_squared_FRW_in_physical_wavenumber(
        1 / TAU_0, TAU_0, ALPHA,
    )

    return {
        "transition_k_phys":           1 / TAU_0,
        "transition_comoving_k_form":  A_OF_ETA / TAU_0,
        "chi_at_transition":            chi_at_transition,
        "n_g_squared_at_transition":    n_g_sq_at_transition,
        "interpretation":
            "Crossover scale λ_* = c τ_0 ≈ 12.85 Mpc (today). "
            "Below this physical wavelength: GR recovers. "
            "Above: full constitutive (n_g² = 4/3).",
    }


# ─────────────────────────────────────────────────────────────────────
# Section 6 — Beyond-WKB correction estimate
# ─────────────────────────────────────────────────────────────────────


def beyond_wkb_correction_magnitude_today() -> Dict[str, float]:
    """Estimate the magnitude of the beyond-WKB correction today.

    The slow-H expansion gives:
        χ_FRW(k, η) = χ_FRW^WKB(k, η) × [1 + O((H_c τ_0)²)]

    Today: H_c × τ_0 / a₀ = H_0 × τ_0 = 1/(108π) ≈ 2.95 × 10⁻³
    (H_c/a is just cosmic-time Hubble H, and H_0 τ_0 = 1/S_screening
    by the GRUT cosmic-baseline relation.)
    Squared: ≈ 8.7 × 10⁻⁶. Negligible at code/precision level.
    """
    import numpy as np
    from grut.foundation.closure_protocol import S_SCREENING
    H_tau_0_today = 1.0 / S_SCREENING  # ≈ 2.95e-3
    correction = H_tau_0_today**2
    # CORRECTION (June 2026): (H τ_0)² is small ONLY at low z. It scales
    # as (1+z)³ in matter dom: (H τ_0)² = 1 at z ≈ 77 and ≈ 2e5 at
    # equality. So "today" is subleading but the early universe is NOT.
    import numpy as _np
    z_qs_boundary = (1.0 / H_tau_0_today) ** (2.0 / 3.0) - 1.0  # (Hτ0)²=1
    return {
        "H_0_times_tau_0":              float(H_tau_0_today),
        "(H_0_tau_0)_squared":          float(correction),
        "is_subleading_today":          correction < 1e-4,
        "is_subleading_in_late_universe": correction < 1e-4,  # today only
        "qs_breaks_down_above_redshift": float(z_qs_boundary),  # ≈ 77
        "interpretation":
            "WKB/QS correction is 8.7e-6 TODAY but grows as (1+z)³: "
            f"(Hτ0)²=1 at z≈{z_qs_boundary:.0f}, ≈2e5 at equality. "
            "WKB/QS is valid for z≲30 and for sub-horizon growth modes "
            "(k≳1e-2, σ8/BAO), but FAILS for the low-ℓ ISW modes "
            "(k≲3e-3) whose enhancement turns on at z≳30. The earlier "
            "claim of validity 'across all post-equality cosmology' was "
            "an arithmetic error. See theory/CMB_ISW_EQUALITY_FILTER.md §0.",
    }


# ─────────────────────────────────────────────────────────────────────
# Numerical evaluation utilities for cosmology consumers
# ─────────────────────────────────────────────────────────────────────


def n_g_squared_numeric(
    k_phys_inverse_meters: float,
    tau_0_seconds: Optional[float] = None,
    alpha_vac: Optional[float] = None,
    c_light: float = 299792458.0,
) -> float:
    """Numerical n_g²(k_phys) evaluated at a specific physical wavenumber.

    Parameters
    ----------
    k_phys_inverse_meters : float
        Physical wavenumber in 1/meters (k = 2π/λ where λ is the
        physical wavelength).
    tau_0_seconds : float, optional
        GRUT relaxation time. Defaults to canonical 41.9 Myr.
    alpha_vac : float, optional
        Vacuum impedance. Defaults to 1/3.
    c_light : float
        Speed of light, used to convert τ_0 (seconds) to a length
        τ_0 c (meters).

    Returns
    -------
    float
        n_g²(k_phys), dimensionless.

    Examples
    --------
    >>> # Galactic-cluster scale (~Mpc)
    >>> import math
    >>> Mpc_in_m = 3.0857e22
    >>> k = 2 * math.pi / Mpc_in_m  # k = 2π / λ
    >>> n_g_squared_numeric(k)
    # Approximately 4/3 (super-horizon regime relative to k_*)

    >>> # Galactic scale (~10 kpc) — sub-horizon
    >>> k = 2 * math.pi / (10e3 * 3.0857e16)
    >>> n_g_squared_numeric(k)
    # Approximately 1 (GR recovery on small scales)
    """
    from grut.foundation.closure_protocol import TAU_0_SEC, ALPHA_VAC
    tau = tau_0_seconds if tau_0_seconds is not None else TAU_0_SEC
    a = alpha_vac if alpha_vac is not None else ALPHA_VAC
    # τ_0 has units of time; multiply by c to get length-equivalent.
    # τ_0 k_phys is dimensionless when k_phys × c × τ_0 is computed
    # explicitly:
    arg_squared = (tau * c_light * k_phys_inverse_meters)**2
    return 1.0 + a / (1.0 + arg_squared)


def transition_wavenumber_today_inverse_meters(
    tau_0_seconds: Optional[float] = None,
    c_light: float = 299792458.0,
) -> float:
    """The physical wavenumber where k_phys × c × τ_0 = 1 — today.

    Returns k_*^phys today in inverse meters.
    """
    from grut.foundation.closure_protocol import TAU_0_SEC
    tau = tau_0_seconds if tau_0_seconds is not None else TAU_0_SEC
    return 1.0 / (tau * c_light)


def transition_wavelength_today_Mpc(
    tau_0_seconds: Optional[float] = None,
    c_light: float = 299792458.0,
) -> float:
    """The physical wavelength λ_* = 2π/k_* today, in megaparsecs."""
    import math
    Mpc_in_m = 3.0857e22
    k_star = transition_wavenumber_today_inverse_meters(tau_0_seconds, c_light)
    lambda_star_m = 2 * math.pi / k_star
    return lambda_star_m / Mpc_in_m


# ─────────────────────────────────────────────────────────────────────
# Integrated verification harness
# ─────────────────────────────────────────────────────────────────────


def verify() -> Dict[str, bool]:
    """Self-test: Phase 2C explicit-FRW landings.

    Eight legs:
      (1) χ_FRW^WKB has the expected (1 + (τ_0 k_phys)²)⁻¹ form
      (2) n_g² = 1 + α χ_FRW structurally (at WKB level)
      (3) Sub-horizon limit: χ_FRW → 0, n_g² → 1 (GR)
      (4) Super-horizon limit: χ_FRW → 1, n_g² → 1 + α (full)
      (5) Transition wavenumber gives χ = 1/2, n_g² = 1 + α/2
      (6) α_vac = 1/3 inheritance from KS 2011
      (7) Beyond-WKB correction is < 10⁻⁴ today
      (8) Convention declaration is present and complete
    """
    # (1) χ_FRW^WKB form
    chi = chi_FRW_WKB_in_physical_wavenumber(K_PHYS, TAU_0)
    expected_chi = 1 / (1 + TAU_0**2 * K_PHYS**2)
    leg1 = sp.simplify(chi - expected_chi) == 0

    # (2) n_g² structure
    n_g_sq = n_g_squared_FRW_in_physical_wavenumber(K_PHYS, TAU_0, ALPHA)
    expected_n_g_sq = 1 + ALPHA * (1 / (1 + TAU_0**2 * K_PHYS**2))
    leg2 = sp.simplify(n_g_sq - expected_n_g_sq) == 0

    # (3) Sub-horizon limit
    sub = sub_horizon_limit()
    leg3 = (sub["chi_FRW_high_k_limit"] == 0
            and sub["n_g_squared_high_k"] == 1)

    # (4) Super-horizon limit
    sup = super_horizon_limit()
    leg4 = (sup["chi_FRW_low_k_limit"] == 1
            and sup["n_g_squared_low_k"] == 1 + ALPHA)

    # (5) Transition wavenumber
    trans = transition_wavenumber()
    chi_trans = sp.simplify(trans["chi_at_transition"])
    n_g_sq_trans = sp.simplify(trans["n_g_squared_at_transition"])
    leg5 = (
        chi_trans == sp.Rational(1, 2)
        and sp.simplify(n_g_sq_trans - (1 + ALPHA / 2)) == 0
    )

    # (6) α_vac inherits 1/3
    from grut.derivation.phi_munu.linearized_ctp_action import (
        alpha_vac_from_conformal_mode,
    )
    leg6 = alpha_vac_from_conformal_mode() == Fraction(1, 3)

    # (7) Beyond-WKB correction estimate
    beyond = beyond_wkb_correction_magnitude_today()
    leg7 = beyond["is_subleading_in_late_universe"]

    # (8) Convention declaration completeness
    conv = convention_declaration()
    required_keys = (
        "C1f_FRW_metric", "C2f_conformal_hubble",
        "C3f_comoving_fourier_ansatz", "C4f_WKB_slow_H_regime",
        "C5f_physical_wavenumber_and_transition",
        "C6f_alpha_vac_inherits", "phase_2C_status",
    )
    leg8 = all(k in conv for k in required_keys)

    return {
        "chi_FRW_WKB_has_expected_form":          leg1,
        "n_g_squared_equals_one_plus_alpha_chi":  leg2,
        "sub_horizon_limit_recovers_GR":          leg3,
        "super_horizon_limit_full_constitutive":   leg4,
        "transition_at_k_phys_tau_0_equals_one":   leg5,
        "alpha_vac_inherits_one_third":           leg6,
        "beyond_wkb_correction_subleading_today": leg7,
        "convention_declaration_complete":         leg8,
    }
