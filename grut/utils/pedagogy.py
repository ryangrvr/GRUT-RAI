"""
Pedagogical Walkthroughs — Step-by-step derivations for GRUT concepts.

Each walkthrough is a sequence of steps with equations, explanations,
and checkpoints that can be rendered in the UI.
"""
import numpy as np
from grut.foundation.constants import G, HBAR, ZETA_3
from grut.foundation.axioms import TAU_I
from grut.foundation.anomaly import C_FINAL, R_ANOMALY, S_CTP


def walkthrough_constitutive_equation():
    """How A0 + A1 → the constitutive equation (3 routes)."""
    return {
        "title": "Deriving the Constitutive Equation",
        "subtitle": "Three independent routes to τ dz/dt + z = z_target[z]",
        "steps": [
            {"step": 1, "title": "Start: The CTP Effective Action (Axiom A0)",
             "equation": "S_CTP[z_r, z_a] = z_a F[z_r] + (i/2) z_a N z_a",
             "explanation": "The Schwinger-Keldysh formalism doubles the degrees of freedom. z_r is the classical field, z_a is the quantum field. F is the equation of motion. N is the noise kernel.",
             "key_insight": "Two terms: deterministic (z_a F) + stochastic (z_a N z_a). Both from ONE action."},
            {"step": 2, "title": "The Retarded Variation (Axiom A1)",
             "equation": "δS_CTP / δz_a |_{z_a=0} = 0  →  F[z_r] = 0",
             "explanation": "Varying with respect to z_a and setting z_a = 0 selects the retarded (causal) equation of motion. This IS the arrow of time.",
             "key_insight": "A1 breaks time-reversal symmetry. The universe evolves FORWARD, not backward."},
            {"step": 3, "title": "Route 1: CTP Variation → Constitutive Form",
             "equation": "F[z] = 0  →  (1/τ) dz/dt = z_target[z] - z  →  τ dz/dt + z = z_target[z]",
             "explanation": "For first-order sectors (QM, Dirac), the EOM is already first-order. For second-order sectors (Einstein), the constitutive projection replaces d²/dt² with (1/τ)d/dt.",
             "key_insight": "EXACT for first-order sectors. HEURISTIC for second-order. All COMPUTED results are projection-independent."},
            {"step": 4, "title": "Route 2: Mori-Zwanzig Memory Kernel",
             "equation": "dz/dt = F[z] + ∫K(t-t')z(t')dt' + ξ(t)  →  τ dz/dt + z = z_target[z]",
             "explanation": "Start from exact microscopic dynamics. Integrate out the environment. The finite-memory (Markovian) limit of the retarded kernel gives the constitutive form.",
             "key_insight": "The constitutive equation is the NATURAL effective dynamics of any open system with finite memory."},
            {"step": 5, "title": "Route 3: Gradient Flow",
             "equation": "dz/dt = -(1/τ) δF/δz  →  τ dz/dt + z = z - δF/δz = z_target[z]",
             "explanation": "A system minimizing a functional F[z] through gradient descent arrives at the same constitutive form.",
             "key_insight": "Thermodynamic relaxation, RG flow, and neural dynamics all have this structure."},
            {"step": 6, "title": "The Target Functional",
             "equation": "z_target[z] = z - (δF/δz)⁻¹ F[z]",
             "explanation": "This is the Newton-Raphson step toward F[z] = 0. The target is not postulated — it is algorithmically determined by the classical action through the CTP variation.",
             "key_insight": "The universe performs continuous root-finding toward self-consistent solutions of its own equations of motion."},
            {"step": 7, "title": "Convergence",
             "equation": "Three routes → one equation: τ dz/dt + z = z_target[z]",
             "explanation": "CTP variation, Mori-Zwanzig coarse-graining, and gradient flow all produce the same form. This strongly suggests universality.",
             "key_insight": "The constitutive equation is the ONLY stable first-order dynamics consistent with causality, finite memory, and self-consistent closure."},
        ]
    }


def walkthrough_decoherence():
    """From noise kernel to zero-parameter decoherence prediction."""
    L_gold = G * (80.8e-15)**2 * (1/6) / (HBAR * 1e-6)
    return {
        "title": "Gravitational Decoherence: From Noise Kernel to Prediction",
        "subtitle": "Zero free parameters. Six scaling laws. No alternative matches all six.",
        "steps": [
            {"step": 1, "title": "The Noise Kernel (from S_CTP)",
             "equation": "δ²S_CTP / δz_a² = iN",
             "explanation": "The second variation of the CTP action gives the noise kernel N — the strength of intrinsic quantum fluctuations.",
             "computed": None},
            {"step": 2, "title": "Gravitational Noise (Newtonian Limit)",
             "equation": "N_grav(x, x') = G / (ℏ |x - x'|)",
             "explanation": "In the Newtonian limit, the noise kernel becomes the Diósi gravitational self-energy. Derived from the CTP influence functional (Anastopoulos & Hu, 2013).",
             "computed": None},
            {"step": 3, "title": "Integration Over Extended Body",
             "equation": "Λ_grav = G m² S(l/R) / (ℏ l)  where  S(l/R) = min(1, (l/R)³/6)",
             "explanation": "Integrating the noise kernel over a uniform sphere of mass m, radius R, at superposition separation l. The suppression factor S(l/R) arises from the finite extent of the mass distribution.",
             "computed": None},
            {"step": 4, "title": "The Gold Benchmark",
             "equation": f"Gold 1μm sphere: Λ_grav = {L_gold:.1f} Hz, t_coh = {1/L_gold*1000:.1f} ms",
             "explanation": f"R = 1 μm, m = 80.8 pg (ρ = 19,300 kg/m³), l = 1 μm → S(l/R) = 1/6 = 0.1667",
             "computed": {"Lambda_Hz": L_gold, "t_coh_ms": 1/L_gold*1000}},
            {"step": 5, "title": "Six Scaling Laws",
             "equation": "F1: m², F2: geometry, F3: plateau, F4: l⁻¹, F5: entanglement, F6: kink at 1.8R",
             "explanation": "No tested alternative (constant floor, CSL, Diósi-Penrose point-mass, Penrose OR) reproduces all six simultaneously. The scaling laws, not any single number, are the prediction.",
             "computed": None},
        ]
    }


def walkthrough_bridge():
    """The connection from lab measurement to cosmological constant."""
    H_0 = 70e3 / 3.0857e22
    H_inf = (2 - R_ANOMALY) / (S_CTP * 41.9e6 * 3.156e7)
    OL = (H_inf / H_0)**2
    return {
        "title": "The Bridge: Lab → Universe",
        "subtitle": "One measurement predicts the cosmological constant",
        "steps": [
            {"step": 1, "title": "The Decoherence Surface",
             "equation": "τ(m, l) = ℏ l / (G m²)",
             "explanation": "Every (m, l) pair defines a coherence time. This is a 2D surface in parameter space, derived from the noise kernel.",
             "computed": None},
            {"step": 2, "title": "The Anomaly Structure",
             "equation": f"C_FINAL = {C_FINAL:.6e} (3-loop, scheme-protected)",
             "explanation": "The 3-loop gravitational anomaly coefficient from SM field content: 3(99 + 2π² + 576 ln2 ζ₃)/(16384 π⁶). Hand-constructed in v7; status CONDITIONAL pending independent 3-loop verification (§26.1).",
             "computed": {"C_FINAL": C_FINAL}},
            {"step": 3, "title": "The Structural Formula",
             "equation": "f(R) = 2 - R  →  H_∞ = (2 - R) / (S × τ₀)",
             "explanation": f"Structure f(R) = 2-R is COMPUTED from 3-loop CTP on S⁴ (boundary conditions f(1)=1, f(2)=0, linear at 3-loop). Competing quadratic excluded by factor 70 in RMS. R value is COMPUTED: R = {R_ANOMALY} from 3-loop CTP Laurent expansion on S⁴ (V7 §26.2, primary-source audit — no coupling inputs). Independent confirmation via Osborn 2003 eq (36): ε_combined(SM, M_Z) = 1.1537 matches at 0.05% (§26.1). Here: R = {R_ANOMALY}, S = 108π = {S_CTP:.3f}.",
             "computed": {"R": R_ANOMALY, "R_epsilon_candidate": 1.1537, "S": S_CTP, "f_R": 2-R_ANOMALY}},
            {"step": 4, "title": "The Prediction",
             "equation": f"Ω_Λ = (H_∞ / H₀)² = {OL:.4f}  (Planck: 0.6889, +{(OL/0.6889-1)*100:.1f}%)",
             "explanation": "Four inputs: (2-R) derived, S derived, H₀ measured, τ₀ = the bridge parameter. Two computed + one measured + one bridge = one prediction.",
             "computed": {"H_inf": H_inf, "Omega_Lambda": OL}},
            {"step": 5, "title": "The Experimental Chain",
             "equation": "Measure Λ_grav → extract τ₀ → compute H_∞ → predict Ω_Λ",
             "explanation": "Before experiment: one-parameter framework. After experiment: zero-parameter prediction. A tabletop measurement determines the expansion of the universe.",
             "computed": None},
        ]
    }


def walkthrough_c_final():
    """How C_FINAL is computed from SM field content."""
    n1 = 99.0; n2 = 2*np.pi**2; n3 = 576*np.log(2)*ZETA_3
    total = n1 + n2 + n3
    return {
        "title": "The 3-Loop Anomaly Coefficient C_FINAL",
        "subtitle": "A pure number from the Standard Model, scheme-protected",
        "steps": [
            {"step": 1, "title": "The Formula",
             "equation": "C_FINAL = 3(99 + 2π² + 576 ln(2) ζ(3)) / (16384 π⁶)",
             "explanation": "Three terms from different loop structures, all involving SM field content.",
             "computed": None},
            {"step": 2, "title": "The Three Terms",
             "equation": f"99 (rational, {n1/total*100:.1f}%) + 2π² = {n2:.4f} (fermionic, {n2/total*100:.1f}%) + 576 ln(2)ζ(3) = {n3:.4f} (gauge, {n3/total*100:.1f}%)",
             "explanation": "99 from SM diagram combinatorics. 2π² from fermion trace structure. 576 ln(2)ζ(3) from gauge boson loops. The gauge term dominates (80%).",
             "computed": {"n_rational": n1, "n_fermionic": n2, "n_gauge": n3}},
            {"step": 3, "title": "The Result",
             "equation": f"C_FINAL = {C_FINAL:.15e}",
             "explanation": "This multiplies the nonlocal operator R ln(□/μ²) R in the gravitational effective action. It is scheme-protected because it multiplies a nonlocal operator — local counterterms cannot absorb it.",
             "computed": {"C_FINAL": C_FINAL}},
        ]
    }


def list_walkthroughs():
    """List all available walkthroughs."""
    return [
        {"id": "constitutive", "title": "Deriving the Constitutive Equation", "steps": 7},
        {"id": "decoherence", "title": "Gravitational Decoherence Prediction", "steps": 5},
        {"id": "bridge", "title": "The Bridge: Lab → Universe", "steps": 5},
        {"id": "c_final", "title": "The 3-Loop Anomaly Coefficient", "steps": 3},
    ]


def get_walkthrough(walkthrough_id):
    """Get a specific walkthrough by ID."""
    walkthroughs = {
        "constitutive": walkthrough_constitutive_equation,
        "decoherence": walkthrough_decoherence,
        "bridge": walkthrough_bridge,
        "c_final": walkthrough_c_final,
    }
    func = walkthroughs.get(walkthrough_id)
    return func() if func else {"error": f"Unknown walkthrough: {walkthrough_id}"}
