"""
Constitutive Cosmology v2 — Self-Referential Target Functional

The v1 model showed: pure constitutive relaxation gives H₀ within 17%
and natural de Sitter acceleration, but no matter era (τ₀ too short).

v2 explores two paths to reconstruct the full three-phase expansion:

PATH A: Self-referential z_target[z] with memory kernel
  z_target includes the actual energy content AND a memory integral
  over cosmic history. Past expansion feeds back into the target.

PATH B: Emergent vacuum energy from the constitutive fixed point
  The self-referential condition z = z_target[z] has a nontrivial
  vacuum solution that acts as effective Λ.

STATUS: Exploratory. Can it produce radiation → matter → acceleration
with τ₀ = 41.9 Myr and zero additional parameters?
"""

import numpy as np
from grut_solver.constants import G, HBAR, C, K_B

TAU_0_S = 41.9e6 * 3.1557e7  # 41.9 Myr in seconds
H0_SI = 70.0 * 1e3 / 3.086e22
OMEGA_R = 9.0e-5
OMEGA_M = 0.3
OMEGA_LAMBDA = 1.0 - OMEGA_M - OMEGA_R


# =========================================================================
# PATH A: MEMORY KERNEL CONSTITUTIVE FRIEDMANN
# =========================================================================

def memory_constitutive_friedmann(n_steps: int = 80000,
                                  memory_depth: int = 500) -> dict:
    """Constitutive Friedmann with integrated memory kernel.

    The constitutive equation with memory:

      H²(t) = z_target(a) - τ₀ dH²/dt + M(t)

    where M(t) = (1/τ₀) ∫₀ᵗ exp(-(t-t')/τ₀) [z_target(t') - H²(t')] dt'

    The memory integral accumulates past "relaxation debt" — how much
    the universe has deviated from its target over its history.

    In the early universe: H² tracks z_target closely (fast relaxation).
    Memory accumulates the integrated deviation.
    At late times: matter dilutes, z_target_matter → 0, but the MEMORY
    of past deviations persists as an effective positive energy density.

    This is the "dark memory" — the universe remembers having been
    out of equilibrium, and that memory acts like dark energy.
    """
    # Integrate in ln(a) for stability
    ln_a_init = np.log(1e-8)
    ln_a_final = 0.0
    ln_a = np.linspace(ln_a_init, ln_a_final, n_steps)
    d_ln_a = ln_a[1] - ln_a[0]
    a_array = np.exp(ln_a)

    H2_standard = np.zeros(n_steps)
    H2_constitutive = np.zeros(n_steps)
    memory = np.zeros(n_steps)
    t_array = np.zeros(n_steps)

    # Standard Friedmann (the target at each epoch)
    for i in range(n_steps):
        a = a_array[i]
        H2_standard[i] = H0_SI**2 * (OMEGA_R * a**(-4) + OMEGA_M * a**(-3) + OMEGA_LAMBDA)

    # Target WITHOUT Lambda — the constitutive memory should generate it
    def z_target_no_lambda(a):
        return H0_SI**2 * (OMEGA_R * a**(-4) + OMEGA_M * a**(-3))

    # Initial condition
    H2_constitutive[0] = z_target_no_lambda(a_array[0])

    for i in range(n_steps - 1):
        a = a_array[i]
        H = np.sqrt(max(H2_constitutive[i], 1e-50))

        # Time step: dt = d(ln a) / H
        dt = d_ln_a / H if H > 1e-50 else 1e30
        t_array[i + 1] = t_array[i] + dt

        # Target (without Lambda)
        zt = z_target_no_lambda(a)

        # Deviation (relaxation debt)
        deviation = zt - H2_constitutive[i]

        # Memory update: M(t+dt) = M(t) × exp(-dt/τ₀) + deviation × dt/τ₀
        decay = np.exp(-dt / TAU_0_S)
        memory[i + 1] = memory[i] * decay + deviation * (1 - decay)

        # Constitutive equation: H² relaxes toward target + memory
        # The memory acts as an ADDITIONAL source term
        effective_target = zt + memory[i]

        # Relaxation
        dH2_dt = (effective_target - H2_constitutive[i]) / TAU_0_S
        dH2_da = dH2_dt / (a * H) if H > 1e-50 else 0

        H2_constitutive[i + 1] = H2_constitutive[i] + dH2_da * d_ln_a * a
        H2_constitutive[i + 1] = max(H2_constitutive[i + 1], 1e-50)

    H_std = np.sqrt(H2_standard)
    H_con = np.sqrt(np.maximum(H2_constitutive, 0))
    E_std = H_std / H0_SI
    E_con = H_con / H0_SI

    # Extract at key redshifts
    z_redshift = 1.0 / a_array - 1
    comparison = []
    for zv in [0.0, 0.5, 1.0, 2.0, 5.0, 10.0, 100.0, 1000.0]:
        idx = np.argmin(np.abs(z_redshift - zv))
        E_s = float(E_std[idx])
        E_c = float(E_con[idx])
        m = float(memory[idx])
        delta = abs(E_c - E_s) / E_s * 100 if E_s > 0 else 0
        comparison.append({
            "z": zv, "E_standard": E_s, "E_constitutive": E_c,
            "memory_H2": m, "delta_pct": delta,
        })

    # Memory as fraction of total H² today
    idx_today = np.argmin(np.abs(z_redshift))
    memory_fraction = memory[idx_today] / H2_constitutive[idx_today] if H2_constitutive[idx_today] > 0 else 0

    return {
        "model": "memory_constitutive",
        "comparison": comparison,
        "memory_fraction_today": memory_fraction,
        "memory_acts_as_lambda": memory_fraction > 0.1,
        "E_today": float(E_con[idx_today]),
    }


# =========================================================================
# PATH B: SELF-REFERENTIAL VACUUM ENERGY
# =========================================================================

def self_referential_vacuum(n_steps: int = 80000) -> dict:
    """Self-referential constitutive Friedmann: z_target depends on z.

    The constitutive equation:
      τ₀ dH²/dt + H² = z_target[H², a]

    where z_target[H², a] = (8πG/3)(ρ_r/a⁴ + ρ_m/a³) + α(H²) × H²

    The self-referential term α(H²) × H² represents the vacuum
    contribution that emerges from the constitutive dynamics itself.

    The key insight: α is not a free parameter. It's determined by
    the constitutive equation's own structure.

    For the GRUT constitutive equation, the natural α comes from
    the self-referential condition at the fixed point:
      At fixed point: dH²/dt = 0, so H² = z_target[H²]
      This gives: H² = matter_terms + α H²
      So: (1-α) H² = matter_terms
      Late times (matter → 0): either H → 0 or α → 1

    If α depends on H: α(H) = 1 - (H/H_max)² (saturates at H_max)
    Then at low H: α ≈ 1, and H² ≈ matter/(1-α) → ∞ ... unstable.

    Better: α = const, determined by the CTP normalization.
    From the influence functional: α = 1 - Ω_m,0
    This is NOT derived — it would need the vacuum energy calculation.
    But it shows the STRUCTURE of how self-reference generates Λ.

    For this mock: we test whether a SELF-CONSISTENTLY DETERMINED α
    can reproduce ΛCDM from the constitutive equation alone.
    """
    ln_a_init = np.log(1e-8)
    ln_a_final = 0.0
    ln_a = np.linspace(ln_a_init, ln_a_final, n_steps)
    d_ln_a = ln_a[1] - ln_a[0]
    a_array = np.exp(ln_a)

    # Standard ΛCDM
    H2_standard = H0_SI**2 * (OMEGA_R * a_array**(-4) + OMEGA_M * a_array**(-3) + OMEGA_LAMBDA)

    # Self-referential: target = matter + α × current H²
    # where α is the fraction of H² that comes from self-reference
    # At the fixed point: H² = matter/(1-α) → Ω_Λ = α/(1-α) → α = Ω_Λ/(1+Ω_Λ)
    # But for ΛCDM: Ω_m + Ω_Λ = 1, so α = Ω_Λ
    alpha = OMEGA_LAMBDA  # = 0.7 — this IS the cosmological constant rewritten

    H2_self = np.zeros(n_steps)
    H2_self[0] = H2_standard[0]

    for i in range(n_steps - 1):
        a = a_array[i]
        H = np.sqrt(max(H2_self[i], 1e-50))
        dt = d_ln_a / H if H > 1e-50 else 1e30

        # Self-referential target
        matter = H0_SI**2 * (OMEGA_R * a**(-4) + OMEGA_M * a**(-3))
        zt = matter + alpha * H2_self[i]

        # Relaxation
        dH2_dt = (zt - H2_self[i]) / TAU_0_S
        dH2_da = dH2_dt / (a * H) if H > 1e-50 else 0

        H2_self[i + 1] = H2_self[i] + dH2_da * d_ln_a * a
        H2_self[i + 1] = max(H2_self[i + 1], 1e-50)

    E_std = np.sqrt(H2_standard) / H0_SI
    E_self = np.sqrt(np.maximum(H2_self, 0)) / H0_SI

    z_redshift = 1.0 / a_array - 1
    comparison = []
    for zv in [0.0, 0.5, 1.0, 2.0, 5.0, 10.0, 100.0, 1000.0]:
        idx = np.argmin(np.abs(z_redshift - zv))
        E_s = float(E_std[idx])
        E_sr = float(E_self[idx])
        delta = abs(E_sr - E_s) / E_s * 100 if E_s > 0 else 0
        comparison.append({"z": zv, "E_standard": E_s, "E_self_ref": E_sr, "delta_pct": delta})

    return {
        "model": "self_referential_vacuum",
        "alpha": alpha,
        "alpha_interpretation": (
            f"α = Ω_Λ = {alpha:.3f}. This IS the cosmological constant rewritten "
            f"as a self-referential fraction. The constitutive equation z_target = "
            f"matter + α z has α = Ω_Λ at the fixed point. The question is whether "
            f"α can be DERIVED from the constitutive framework rather than input."
        ),
        "comparison": comparison,
        "reproduces_lcdm": all(r["delta_pct"] < 1.0 for r in comparison),
    }


# =========================================================================
# PATH C: THE HYBRID — MATTER-COUPLED CONSTITUTIVE RELAXATION
# =========================================================================

def hybrid_constitutive(n_steps: int = 80000) -> dict:
    """The hybrid model: standard matter/radiation content drives early
    expansion, constitutive relaxation takes over at late times.

    The constitutive equation for H(t):
      τ₀ dH/dt + H = H_target(a)

    where H_target(a) = H₀ × sqrt(Ω_r/a⁴ + Ω_m/a³ + Ω_relax)

    and Ω_relax = 1 - Ω_m - Ω_r is NOT the cosmological constant but
    the RELAXATION ATTRACTOR — the H² value the constitutive equation
    drives toward when matter dilutes.

    Why this is different from just putting in Λ:
    In standard ΛCDM, Ω_Λ is a constant energy density (ρ_Λ = const).
    Here, Ω_relax is the constitutive FIXED POINT — it's what the
    equation relaxes toward. The dynamics are different near the
    transition because the constitutive equation adds a time derivative
    term that smooths the transition.

    With τ₀ = 41.9 Myr << t_universe: the smoothing is minimal and
    we recover standard ΛCDM almost exactly. But the INTERPRETATION
    is different: Λ is not a mysterious energy density — it's the
    target state of the constitutive equation.
    """
    ln_a_init = np.log(1e-8)
    ln_a_final = 0.0
    ln_a = np.linspace(ln_a_init, ln_a_final, n_steps)
    d_ln_a = ln_a[1] - ln_a[0]
    a_array = np.exp(ln_a)

    # Standard ΛCDM
    H2_standard = H0_SI**2 * (OMEGA_R * a_array**(-4) + OMEGA_M * a_array**(-3) + OMEGA_LAMBDA)

    # Constitutive: H relaxes toward H_target with time constant τ₀
    H_standard = np.sqrt(H2_standard)
    H_constitutive = np.zeros(n_steps)
    H_constitutive[0] = H_standard[0]
    t_array = np.zeros(n_steps)

    # Deceleration parameter
    q_std = np.zeros(n_steps)
    q_con = np.zeros(n_steps)

    for i in range(n_steps - 1):
        a = a_array[i]
        H = max(H_constitutive[i], 1e-50)
        dt = d_ln_a / H if H > 1e-50 else 1e30
        t_array[i + 1] = t_array[i] + dt

        # Target: standard Friedmann H (including Ω_relax = Ω_Λ)
        H_target = H_standard[i]

        # Constitutive relaxation: τ₀ dH/dt + H = H_target
        dH_dt = (H_target - H) / TAU_0_S
        dH_dlna = dH_dt / H if H > 1e-50 else 0

        H_constitutive[i + 1] = H + dH_dlna * d_ln_a
        H_constitutive[i + 1] = max(H_constitutive[i + 1], 1e-50)

    E_std = H_standard / H0_SI
    E_con = H_constitutive / H0_SI

    # Deceleration parameter
    for i in range(1, n_steps - 1):
        if H_standard[i] > 0:
            dH = (H_standard[i+1] - H_standard[i-1]) / (2 * d_ln_a)
            q_std[i] = -1 - dH / H_standard[i]
        if H_constitutive[i] > 0:
            dH = (H_constitutive[i+1] - H_constitutive[i-1]) / (2 * d_ln_a)
            q_con[i] = -1 - dH / H_constitutive[i]

    z_redshift = 1.0 / a_array - 1
    comparison = []
    for zv in [0.0, 0.5, 1.0, 2.0, 5.0, 10.0, 100.0, 1000.0]:
        idx = np.argmin(np.abs(z_redshift - zv))
        E_s = float(E_std[idx])
        E_c = float(E_con[idx])
        delta = abs(E_c - E_s) / E_s * 100 if E_s > 0 else 0
        qs = float(q_std[idx])
        qc = float(q_con[idx])
        comparison.append({
            "z": zv, "E_standard": E_s, "E_constitutive": E_c,
            "delta_pct": delta, "q_standard": qs, "q_constitutive": qc,
        })

    # Transition redshift
    z_trans_std = z_trans_con = None
    for i in range(len(q_std) - 1):
        if q_std[i] > 0 and q_std[i+1] < 0 and z_trans_std is None:
            z_trans_std = float(z_redshift[i])
        if q_con[i] > 0 and q_con[i+1] < 0 and z_trans_con is None:
            z_trans_con = float(z_redshift[i])

    return {
        "model": "hybrid_constitutive",
        "comparison": comparison,
        "z_transition_standard": z_trans_std,
        "z_transition_constitutive": z_trans_con,
        "max_deviation_pct": max(r["delta_pct"] for r in comparison),
        "three_phases": z_trans_con is not None,
        "interpretation": (
            "Ω_Λ is reinterpreted as the constitutive relaxation attractor, "
            "not a mysterious vacuum energy density. The numerical value is "
            "the same (Ω_relax = 0.7) but the physical interpretation is "
            "different: it's the target state of the universal constitutive "
            "equation. The 'why Λ?' question becomes 'why does z_target have "
            "this value?' — which is answerable within the constitutive framework "
            "once z_target is derived from the CTP influence functional."
        ),
    }


# =========================================================================
# FULL ANALYSIS
# =========================================================================

def full_v2_analysis() -> dict:
    """Run all three paths and compare."""
    memory = memory_constitutive_friedmann()
    selfref = self_referential_vacuum()
    hybrid = hybrid_constitutive()

    return {
        "path_a_memory": memory,
        "path_b_self_referential": selfref,
        "path_c_hybrid": hybrid,
        "overall_verdict": {
            "memory_generates_lambda": memory["memory_acts_as_lambda"],
            "self_ref_reproduces_lcdm": selfref["reproduces_lcdm"],
            "hybrid_three_phases": hybrid["three_phases"],
            "honest_assessment": (
                "PATH A (memory): Tests whether accumulated relaxation debt "
                "acts as effective dark energy. "
                "PATH B (self-referential): Shows Ω_Λ = α at the fixed point "
                "(structural insight but does not derive α). "
                "PATH C (hybrid): Reinterprets Λ as the constitutive attractor — "
                "same numbers as ΛCDM, different physical interpretation. "
                "The three-phase reconstruction works with the hybrid model "
                "because it couples to the actual energy content. "
                "The open question: can α (or Ω_relax) be derived from "
                "the CTP influence functional without inputting it?"
            ),
        },
    }
