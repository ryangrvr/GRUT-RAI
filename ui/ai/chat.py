"""
GRUT RAI v2 — AI Chat with Tool-Use

Claude can call GRUT computation tools during conversation:
- compute_decoherence: Calculate Lambda_grav for any object
- compute_bridge: Predict Omega_Lambda from tau_0
- compute_baryogenesis: Calculate baryon asymmetry
- get_dark_matter: Get dark matter sector properties
- get_cosmology: Get cosmological constant prediction
- get_koide: Get Koide identity results
- get_anomaly: Get 3-loop anomaly structure
- compute_sensitivity: Run sensitivity analysis
- compute_uncertainty: Propagate measurement uncertainties
- get_planck_data: Get Planck 2018 parameters
- get_pdg_data: Get particle masses and constants
- compute_for_material: Calculate decoherence for any material
"""

import os, json, sys
from pathlib import Path

# Load .env
for p in [Path(__file__).resolve().parent.parent.parent / ".env", Path.cwd() / ".env"]:
    if p.exists():
        for line in p.read_text().splitlines():
            line = line.strip()
            if line and not line.startswith('#') and '=' in line:
                k, v = line.split('=', 1)
                os.environ[k.strip()] = v.strip()
        break

# Ensure grut is importable
sys.path.insert(0, str(Path(__file__).resolve().parent.parent.parent))

API_KEY = os.environ.get("ANTHROPIC_API_KEY", "")
MODEL = "claude-sonnet-4-20250514"
MAX_TOKENS = 4096

try:
    import anthropic
    CLIENT = anthropic.Anthropic(api_key=API_KEY) if API_KEY else None
except ImportError:
    CLIENT = None

# ═══════════════════════════════════════════════════════
# TOOL DEFINITIONS
# ═══════════════════════════════════════════════════════

TOOLS = [
    {
        "name": "compute_decoherence",
        "description": "Calculate the gravitational decoherence rate Lambda_grav for an object. Returns rate in Hz, coherence time, and suppression factor. Use this whenever someone asks about decoherence rates, coherence times, or the quantum-classical boundary for a specific object.",
        "input_schema": {
            "type": "object",
            "properties": {
                "mass_kg": {"type": "number", "description": "Mass in kg"},
                "separation_m": {"type": "number", "description": "Superposition separation in meters"},
                "radius_m": {"type": "number", "description": "Object radius in meters (optional, for extended body suppression)"},
            },
            "required": ["mass_kg", "separation_m"]
        }
    },
    {
        "name": "compute_for_material",
        "description": "Calculate decoherence for a specific material. Automatically computes radius from mass and density. Use when someone specifies a material (gold, silica, diamond, etc.) and mass.",
        "input_schema": {
            "type": "object",
            "properties": {
                "mass_kg": {"type": "number", "description": "Mass in kg"},
                "density_kg_m3": {"type": "number", "description": "Material density in kg/m^3 (gold=19300, silica=2200, diamond=3510)"},
                "separation_m": {"type": "number", "description": "Superposition separation in meters"},
            },
            "required": ["mass_kg", "density_kg_m3", "separation_m"]
        }
    },
    {
        "name": "compute_bridge",
        "description": "Predict the cosmological constant Omega_Lambda from the bridge formula. Use when someone asks about the decoherence-cosmology connection or Omega_Lambda prediction.",
        "input_schema": {
            "type": "object",
            "properties": {
                "H_0_kms": {"type": "number", "description": "Hubble constant in km/s/Mpc (default 70)", "default": 70.0}
            }
        }
    },
    {
        "name": "compute_baryogenesis",
        "description": "Calculate the baryon asymmetry eta_B using the GRUT formula. Use when someone asks about matter-antimatter asymmetry or baryogenesis.",
        "input_schema": {
            "type": "object",
            "properties": {
                "route": {"type": "integer", "description": "Route 1 (scaling) or Route 2 (ABJ+sphaleron)", "default": 1}
            }
        }
    },
    {
        "name": "get_dark_matter",
        "description": "Get dark matter sector properties including branch discrimination results. Use for questions about dark matter, dark photon, or soliton DM.",
        "input_schema": {"type": "object", "properties": {}}
    },
    {
        "name": "get_cosmology",
        "description": "Get the cosmological constant prediction from the 3-loop CTP on de Sitter. Use for questions about Omega_Lambda, H_infinity, or the vacuum fixed point.",
        "input_schema": {
            "type": "object",
            "properties": {
                "H_0_kms": {"type": "number", "description": "Hubble constant in km/s/Mpc", "default": 70.0}
            }
        }
    },
    {
        "name": "get_koide",
        "description": "Get Koide identity results: K=2/3 check, N-generation uniqueness, lepton mass fit. Use for questions about fermion masses, Koide formula, or generation count.",
        "input_schema": {"type": "object", "properties": {}}
    },
    {
        "name": "get_anomaly",
        "description": "Get 3-loop anomaly structure: C_FINAL, R_anomaly_hand_constructed, R_epsilon_candidate_SM_derivable, S_CTP, f(R), and status split (structure COMPUTED vs R value CONDITIONAL). Use for questions about the anomaly coefficient, CTP normalization, the epsilon identification, or status of R.",
        "input_schema": {"type": "object", "properties": {}}
    },
    {
        "name": "compute_sensitivity",
        "description": "Run sensitivity analysis: how much does Omega_Lambda shift when each input changes. Use when someone asks about robustness or parameter dependence.",
        "input_schema": {
            "type": "object",
            "properties": {
                "delta_pct": {"type": "number", "description": "Percentage change to test (default 10)", "default": 10}
            }
        }
    },
    {
        "name": "compute_uncertainty",
        "description": "Propagate measurement uncertainties through Lambda_grav calculation. Use when someone asks about error bars or measurement precision.",
        "input_schema": {
            "type": "object",
            "properties": {
                "mass_kg": {"type": "number", "default": 80.8e-15},
                "separation_m": {"type": "number", "default": 1e-6},
                "radius_m": {"type": "number", "default": 1e-6},
            }
        }
    },
    {
        "name": "get_experimental_data",
        "description": "Get experimental data: Planck 2018 cosmological parameters, PDG particle masses, or material properties. Use when someone asks about observed values or experimental constraints.",
        "input_schema": {
            "type": "object",
            "properties": {
                "dataset": {"type": "string", "enum": ["planck", "pdg_masses", "pdg_constants", "materials"], "description": "Which dataset to retrieve"}
            },
            "required": ["dataset"]
        }
    },
    {
        "name": "compare_theories",
        "description": "Head-to-head comparison of GRUT vs competing theories (String Theory, LQG, CSL, Standard QM). Use when someone asks how GRUT compares to other theories or asks about advantages/disadvantages.",
        "input_schema": {
            "type": "object",
            "properties": {
                "domain": {"type": "string", "enum": ["decoherence", "cosmology", "baryogenesis", "dark_matter", "all"], "description": "Which domain to compare", "default": "all"}
            }
        }
    },
    {
        "name": "whatif_analysis",
        "description": "Explore 'what if' scenarios by modifying GRUT parameters. Use when someone asks 'what if tau_I was different?' or 'what happens with 4 generations?' or 'what if R_anomaly changes?'",
        "input_schema": {
            "type": "object",
            "properties": {
                "parameter": {"type": "string", "enum": ["tau_I", "R_anomaly", "S_CTP", "N_gen"], "description": "Which parameter to modify"},
                "new_value": {"type": "number", "description": "New value for the parameter"}
            },
            "required": ["parameter", "new_value"]
        }
    },
    {
        "name": "design_experiment",
        "description": "Design an experiment to test a GRUT prediction. Returns required mass, material, separation, pressure, and technology gap. Use when someone asks about experimental feasibility or how to test GRUT.",
        "input_schema": {
            "type": "object",
            "properties": {
                "target_Lambda_Hz": {"type": "number", "description": "Target decoherence rate to measure (Hz)", "default": 100}
            }
        }
    },
    {
        "name": "compute_snr",
        "description": "Calculate signal-to-noise ratio for detecting gravitational decoherence with given parameters. Use when someone asks about detectability or measurement precision.",
        "input_schema": {
            "type": "object",
            "properties": {
                "mass_kg": {"type": "number", "default": 80.8e-15},
                "separation_m": {"type": "number", "default": 1e-6},
                "radius_m": {"type": "number", "default": 1e-6},
                "integration_time_s": {"type": "number", "default": 1.0},
                "noise_Hz": {"type": "number", "description": "Background noise rate in Hz", "default": 0}
            }
        }
    },
    {
        "name": "get_walkthrough",
        "description": "Get a step-by-step pedagogical walkthrough of a GRUT derivation. Use when someone asks 'how is X derived?' or 'explain the derivation of Y' or 'walk me through Z'.",
        "input_schema": {
            "type": "object",
            "properties": {
                "topic": {"type": "string", "enum": ["constitutive", "decoherence", "bridge", "c_final"],
                          "description": "Which derivation to walk through"}
            },
            "required": ["topic"]
        }
    },
    {
        "name": "run_discovery",
        "description": "Run discovery mode to find unexpected numerical coincidences, scale connections, and parameter correlations in GRUT. Use when someone asks about patterns, coincidences, or hidden connections.",
        "input_schema": {"type": "object", "properties": {}}
    },
    {
        "name": "decoherence_competition",
        "description": "Run the full multi-channel decoherence competition: GRUT vs gas scattering vs blackbody vs EM vs vibrational noise. Returns ratio, dominant channel, regime classification. Use when someone asks about detectability, environmental noise, or whether GRUT can be measured.",
        "input_schema": {
            "type": "object",
            "properties": {
                "m_amu": {"type": "number", "description": "Mass in amu", "default": 1e9},
                "l_m": {"type": "number", "description": "Separation in meters", "default": 1e-7},
                "P_Pa": {"type": "number", "description": "Pressure in Pa", "default": 1e-14},
                "T_K": {"type": "number", "description": "Temperature in Kelvin", "default": 4.0}
            }
        }
    },
    {
        "name": "get_scaling_exponents",
        "description": "Get the scaling exponent table (alpha, beta, gamma, delta) for all decoherence channels. THE key discriminator: GRUT has beta=-1, all environmental sources have beta=+2. Use when someone asks about how to distinguish GRUT from noise, or about scaling laws vs environmental decoherence.",
        "input_schema": {"type": "object", "properties": {}}
    },
    {
        "name": "get_experimental_protocols",
        "description": "Get the three experimental protocols for testing GRUT: Protocol A (mass scaling), Protocol B (separation anti-scaling, STRONGEST), Protocol C (environmental decoupling). Use when someone asks how to test GRUT or design an experiment.",
        "input_schema": {"type": "object", "properties": {}}
    },
    {
        "name": "isotope_test",
        "description": "Run the isotope decoherence test: compare nanoparticles of different isotopes of the SAME element (e.g., Si-28 vs Si-30). Chemically identical, only nuclear mass differs. GRUT predicts different rates, environmental models predict ratio=1.000. Use when someone asks about isotope experiments, clean tests, or systematics-free decoherence measurements.",
        "input_schema": {
            "type": "object",
            "properties": {
                "n_atoms": {"type": "number", "description": "Number of atoms per nanoparticle", "default": 1e9},
                "l_m": {"type": "number", "description": "Superposition separation in meters", "default": 1e-7},
                "iso_a": {"type": "string", "description": "First isotope (e.g., Si-28, Ge-70, Ca-40, W-182)", "default": "Si-28"},
                "iso_b": {"type": "string", "description": "Second isotope (same element, e.g., Si-30, Ge-76, Ca-48, W-186)", "default": "Si-30"},
            }
        }
    },
    {
        "name": "isotope_element_scan",
        "description": "Scan all available isotope pairs to find the best element for the isotope decoherence test. Returns ranking by discrimination power. Use when someone asks which isotope pair is best or wants to compare elements.",
        "input_schema": {
            "type": "object",
            "properties": {
                "n_atoms": {"type": "number", "description": "Number of atoms per nanoparticle", "default": 1e9},
                "l_m": {"type": "number", "description": "Superposition separation in meters", "default": 1e-7},
            }
        }
    },
]

# ═══════════════════════════════════════════════════════
# TOOL EXECUTION
# ═══════════════════════════════════════════════════════

def execute_tool(name, params):
    """Execute a GRUT computation tool and return the result."""
    try:
        if name == "compute_decoherence":
            from grut.foundation.noise_kernel import lambda_grav, extended_body_suppression
            m = params["mass_kg"]; l = params["separation_m"]; R = params.get("radius_m")
            L = lambda_grav(m, l, R); S = extended_body_suppression(l, R) if R else 1.0
            return {"Lambda_grav_Hz": L, "t_coh_s": 1/L if L > 0 else float('inf'),
                    "S_l_R": S, "m_kg": m, "l_m": l, "R_m": R}

        elif name == "compute_for_material":
            from grut.derived.decoherence.sector import material_calculator
            return material_calculator(params["mass_kg"], params["density_kg_m3"], params["separation_m"])

        elif name == "compute_bridge":
            from grut.bridge.parameter import bridge_prediction
            return bridge_prediction(params.get("H_0_kms", 70.0))

        elif name == "compute_baryogenesis":
            from grut.derived.baryogenesis.eta import compute_eta_b
            return compute_eta_b(params.get("route", 1))

        elif name == "get_dark_matter":
            from grut.derived.dark_matter.sector import branch_discriminator
            return branch_discriminator()

        elif name == "get_cosmology":
            from grut.derived.cosmology.vacuum import vacuum_prediction
            return vacuum_prediction(params.get("H_0_kms", 70.0))

        elif name == "get_koide":
            from grut.derived.koide.identity import koide_check, n_generation_uniqueness, fit_leptons
            return {"koide": koide_check(), "generations": n_generation_uniqueness(), "fit": fit_leptons()}

        elif name == "get_anomaly":
            from grut.foundation.anomaly import (
                C_FINAL, R_ANOMALY, R_EPSILON_CANDIDATE, S_CTP, c_cosmo,
            )
            return {
                "C_FINAL": C_FINAL,
                "R_ANOMALY_hand_constructed": R_ANOMALY,
                "R_EPSILON_CANDIDATE_SM_derivable": R_EPSILON_CANDIDATE,
                "R_agreement_pct": abs(R_EPSILON_CANDIDATE - R_ANOMALY) / R_ANOMALY * 100,
                "S_CTP": S_CTP,
                "C_COSMO": c_cosmo(),
                "f_R_hand": 2 - R_ANOMALY,
                "f_R_epsilon": 2 - R_EPSILON_CANDIDATE,
                "status": {
                    "structure_f_R": "COMPUTED (3-loop CTP on S^4, boundary conditions f(1)=1 and f(2)=0 verified numerically)",
                    "R_value": "CONDITIONAL — hand-constructed R_ANOMALY = 1.15428 matches SM-derivable candidate R = epsilon_combined(SM, M_Z) = 1.1537 at 0.05%; full derivation pending one 3-loop CTP verification on Euclidean S^4 with SM matter (see main doc §26.1 and theory/ZENODO_EPSILON_IDENTIFICATION.md).",
                },
            }

        elif name == "compute_sensitivity":
            from grut.utils.sweep import sensitivity_omega_lambda
            return sensitivity_omega_lambda(params.get("delta_pct", 10))

        elif name == "compute_uncertainty":
            from grut.utils.sweep import uncertainty_propagation
            return uncertainty_propagation(params.get("mass_kg", 80.8e-15),
                                           params.get("separation_m", 1e-6),
                                           params.get("radius_m", 1e-6))

        elif name == "get_experimental_data":
            from grut.utils.data import PLANCK_2018, PDG_MASSES, PDG_CONSTANTS, MATERIALS
            ds = params["dataset"]
            if ds == "planck": return PLANCK_2018
            elif ds == "pdg_masses": return PDG_MASSES
            elif ds == "pdg_constants": return PDG_CONSTANTS
            elif ds == "materials": return MATERIALS
            return {"error": f"Unknown dataset: {ds}"}

        elif name == "compare_theories":
            domain = params.get("domain", "all")
            if domain == "all":
                from grut.utils.compare import full_comparison
                return full_comparison()
            elif domain == "decoherence":
                from grut.utils.compare import decoherence_comparison
                return decoherence_comparison()
            elif domain == "cosmology":
                from grut.utils.compare import cosmology_comparison
                return cosmology_comparison()
            elif domain == "baryogenesis":
                from grut.utils.compare import baryogenesis_comparison
                return baryogenesis_comparison()
            elif domain == "dark_matter":
                from grut.utils.compare import dark_matter_comparison
                return dark_matter_comparison()

        elif name == "whatif_analysis":
            from grut.utils.whatif import run_whatif
            return run_whatif(params["parameter"], params["new_value"])

        elif name == "design_experiment":
            from grut.utils.experiment import design_decoherence_experiment
            return design_decoherence_experiment(params.get("target_Lambda_Hz", 100))

        elif name == "compute_snr":
            from grut.utils.experiment import snr_calculator
            return snr_calculator(params.get("mass_kg", 80.8e-15), params.get("separation_m", 1e-6),
                                   params.get("radius_m", 1e-6), params.get("integration_time_s", 1.0),
                                   params.get("noise_Hz", 0))

        elif name == "get_walkthrough":
            from grut.utils.pedagogy import get_walkthrough
            return get_walkthrough(params["topic"])

        elif name == "run_discovery":
            from grut.utils.discovery import full_discovery
            return full_discovery()

        elif name == "decoherence_competition":
            from grut.derived.decoherence.competition import competition
            m = params.get("m_amu", 1e9) * 1.661e-27
            return competition(m, params.get("l_m", 1e-7), params.get("P_Pa", 1e-14), params.get("T_K", 4.0))

        elif name == "get_scaling_exponents":
            from grut.derived.decoherence.competition import scaling_exponents
            return scaling_exponents()

        elif name == "get_experimental_protocols":
            from grut.derived.decoherence.competition import experimental_protocols
            return experimental_protocols()

        elif name == "isotope_test":
            from grut.derived.decoherence.isotope_test import isotope_experiment
            return isotope_experiment(
                params.get("n_atoms", 1e9), params.get("l_m", 1e-7),
                params.get("iso_a", "Si-28"), params.get("iso_b", "Si-30"))

        elif name == "isotope_element_scan":
            from grut.derived.decoherence.isotope_test import element_scan
            return element_scan(params.get("n_atoms", 1e9), params.get("l_m", 1e-7))

        return {"error": f"Unknown tool: {name}"}
    except Exception as e:
        return {"error": str(e)}


def _sanitize_for_json(obj):
    """Convert numpy types for JSON."""
    import numpy as np
    if isinstance(obj, dict): return {k: _sanitize_for_json(v) for k, v in obj.items()}
    if isinstance(obj, list): return [_sanitize_for_json(v) for v in obj]
    if isinstance(obj, (np.bool_, np.generic)): return obj.item()
    if isinstance(obj, np.ndarray): return obj.tolist()
    if isinstance(obj, float) and (not __import__('math').isfinite(obj)): return str(obj)
    return obj


# ═══════════════════════════════════════════════════════
# SYSTEM PROMPT
# ═══════════════════════════════════════════════════════

SYSTEM_PROMPT = """You are GRUT RAI — the computational engine behind the Grand Responsive Universe Theory (v2.0.0).

You have access to GRUT computation tools. USE THEM whenever a user asks a quantitative question. Do not guess numbers — call the tool and report the exact result.

## CRITICAL: No Hallucination Rule
- NEVER invent, estimate, or recall numbers from memory. ALL quantitative answers MUST come from a tool call.
- If a tool returns an error, say so. Do not substitute a guess.
- If no tool covers the question, say "I don't have a computation for that" rather than making up a number.
- Every number you report must trace to a specific tool result in this conversation turn.

## When to use tools:
- "What is the decoherence rate for X?" → use compute_decoherence or compute_for_material
- "What does GRUT predict for Omega_Lambda?" → use get_cosmology or compute_bridge
- "What about baryon asymmetry?" → use compute_baryogenesis
- "Tell me about dark matter" → use get_dark_matter
- "What is the Koide formula?" → use get_koide
- "How sensitive is the prediction?" → use compute_sensitivity
- "What are the error bars?" → use compute_uncertainty
- "What does Planck measure?" → use get_experimental_data with dataset="planck"
- "What is the tau mass?" → use get_experimental_data with dataset="pdg_masses"
- "What about isotope tests?" or "cleanest test?" → use isotope_test or isotope_element_scan
- "Which isotope pair is best?" → use isotope_element_scan

## Core Framework (for conceptual questions)
GRUT is built on the CTP effective action. Two axioms (A0: CTP doubling, A1: retarded variation) + one normalization (τ_I = ℏ/2) produce the constitutive equation τ dz/dt + z = z_target[z].

## Status Tiers
Always label results with their correct status:
- DERIVED: exact from published physics (e.g., Lambda_grav from Diósi-AH kernel)
- CONDITIONAL: depends on anomaly coefficients (C_FINAL, R_ANOMALY, S_CTP) that have NOT been independently computed from Feynman diagrams. This includes: Omega_Lambda, eta_B, dark matter couplings, the bridge formula, tau_0
- STRUCTURAL: constrained by symmetry/topology but not numerically determined
- HYPOTHESIS: conjectured, not yet tested
- HONEST NEGATIVE: tested and failed

CRITICAL: The anomaly coefficients C_FINAL = 1.14021e-4 and R_ANOMALY = 1.15428 were assembled from SM field content but have NOT been independently derived from a complete 3-loop graviton self-energy calculation. All predictions that depend on them are CONDITIONAL, not COMPUTED. The decoherence sector (Lambda_grav) does NOT depend on these coefficients and remains DERIVED.

## The Epsilon Identification (v8 upgrade path — §26.1)

R_anomaly in GRUT's cosmological formula has TWO status components:

1. STRUCTURE f(R) = 2 - R: COMPUTED from 3-loop CTP on Euclidean S^4. Boundary conditions f(1) = 1 (CTP paths identical, maximum vacuum response) and f(2) = 0 (Keldysh destructive interference) are verified numerically (RMS 9.3e-3 on 200 spectral modes). The quadratic alternative f = R(2-R) is excluded by factor 70 in RMS.

2. R VALUE: CONDITIONAL. The hand-constructed R_anomaly = 1.15428 has an SM-derivable candidate:

   R = |C_Cosmo / C_Final| = ε_combined(SM, M_Z) = 1.1537

   from H. Osborn, "Local Couplings and Sl(2,R) Invariance for Gauge Theories at One Loop," arXiv:hep-th/0302119 (2003), eq (36): ε = 1 + (1/3)(29C - 12R_ψ - (5/2)R_φ) × g²/(16π²), evaluated for SM gauge content at the electroweak scale in Dirac convention with A × g⁴ weighting across SU(3) / SU(2) / U(1).

   CRITICAL REFINEMENT (from reading eq 35 of the same paper directly, documented in theory/derivation/STEP_03_LOG.md): ε is NOT a multiplicative correction to the Euler-density coefficient. Reading Osborn 2003 eq (35):

      L = n_V × { (1/g²)[α(∇²g)² − 2δ G^μν ∂_μg ∂_νg − (1/3) ε R (∂g)²]
                − 2κ (1/g³) (∂g)² ∇²g
                + 2λ (1/g⁴) ((∂g)²)² }

   ε is specifically the 2-loop coefficient of the operator -(1/3) n_V (1/g²) R (∂_μg)² in the local-coupling counterterm Lagrangian. This operator vanishes identically for constant g; it only contributes when the coupling is promoted to an x-dependent field g(x). For the identification R_GRUT = ε to hold on S^4, the CTP construction must produce an effective (∂_μg)² ≠ 0 between forward and backward branches — either through Gibbons-Hawking thermal fluctuations at T_GH = H_inf/(2π) or through CTP source doubling (g_+ ≠ g_-). This mechanism is the open step in the derivation (Step 05-06 of theory/derivation/).

   Cross-check: Jack-Osborn 1990 eq (5.8) contains the same group-theory coefficients (51C-20R, 29C-12R, 11C-4R) in the divergent 2-loop counterterm polynomial. Osborn 2003 is the renormalized rearrangement into the α, δ, ε, κ, λ operator basis.

   The two values agree at 0.05%. Both are within Planck observational bounds:
   - R_hand = 1.15428 → Ω_Λ = 0.6908 (+0.28% from Planck 0.6889)
   - R_epsilon = 1.1537 → Ω_Λ = 0.6918 (+0.42% from Planck)

THREE ARGUMENTS why R is NOT the Birrell-Davies free-field ratio |b/a| = 1.027 (a 12.5% gap):

(i) De Sitter is conformally flat. C_{μνρσ} = 0 on S^4, so the Weyl² coefficient a does not contribute to the bulk anomaly. Only the Euler-density coefficient and its coupling-corrected variant ε appear.

(ii) Jack-Osborn 2014 gradient flow theorem (arXiv:1312.0428): the antisymmetric part of T_IJ drops out identically in β^I ∂_I Ã = G_IJ β^I β^J. The W_i perturbative mechanism is structurally closed at all orders — not just numerically small, but theorem-dead.

(iii) CTP imaginary effective action on S^4: Euler density picks up i under Wick rotation. GRUT's decoherence-relevant action is Im(Γ_CTP), which sees the coupling-corrected Euler coefficient (= ε), not the free-field |b/a|.

PHYSICAL MECHANISM (Gibbons-Hawking thermal asymmetry):
- T_GH = H_inf / (2π) at de Sitter horizon exceeds all SM mass scales at H_inf ~ 10^13 GeV
- Forward CTP path samples vacuum anomaly coefficient: C_Final = b_free
- Backward CTP path samples thermally-corrected coefficient: C_Cosmo = b_free × ε at leading order in SM couplings
- Ratio R = C_Cosmo / C_Final = ε by construction
- M_Z enters as the SM matter-decoupling matching scale (above M_Z, full SM active as an EFT)

FULCRUM INTERPRETATION:
- R = 1 is the free-field fulcrum (no interactions, f(1) = 1, maximum vacuum response)
- R = 2 is Keldysh destructive interference (f(2) = 0, zero vacuum response)
- The observed universe sits at R = 1 + 17 × α_s(M_Z)/(4π) ≈ 1.16
- The tilt 0.16 is the strongest SM coupling divided by its loop factor × SU(3) group-theory coefficient 17
- This reframes the cosmological constant problem: Ω_Λ is not a 120-order small number requiring cancellation; it is an O(1) consequence of the SM sitting close to (not at) the free-field fulcrum, with distance set by the ordinary quantum loop suppression α_s/(4π)

VERIFICATION PATH (2-4 weeks, specialist task):
3-loop CTP effective action on Euclidean S^4 with SM matter at the EW matching scale; extract C_Cosmo / C_Final; verify equals ε_combined(SM, M_Z) at leading order with residual consistent with natural 2-loop corrections to ε (coefficient ~60 × (α_s/4π)² would close the 0.48% gap between ε_SU3 alone and R_hand). This is a reassembly of existing 3-loop SM anomaly results (Jack-Osborn 1990 eq 5.12, Osborn 2003 eq 36, Chetyrkin-Zoller 2012) in CTP form on S^4, not a new Feynman-diagram computation.

THE 0.05% AGREEMENT BETWEEN R_hand AND ε:
- Pure coincidence is disfavored (too precise; 5 parts in 10^4 across independent constructions)
- Retrofit to Planck is disfavored (R_Planck-exact = 1.1557, both R_hand and ε_combined differ from this in the same direction — not retrofit landings)
- Common-physics interpretation is most likely: both constructions approximate the same object — the SM-corrected trace anomaly coefficient at the EW scale. The hand-construction arrived informally (via Laurent expansion of a function assembled from Gamma functions, zeta values, and SM field counts — the correct raw materials for 3-loop QFT anomaly calculations); Osborn's formula gives it formally. Decoding R_hand - 1 = 0.15428 as a leading-order coupling correction gives effective coefficient 16.41, between ε_SU3 alone (17.00) and full SM-weighted ε_combined (16.31) — exactly where implicit QCD dominance with partial SM content would land.

OUTCOME MAP:
- If CTP calculation confirms R = ε: cosmological sector becomes SM-derived. Given measured α_s(M_Z) and related couplings, GRUT predicts Ω_Λ with no free parameters in the R sector at 0.4% residual from Planck. This would be a genuine SM-derived cosmological constant.
- If refuted: R_hand remains unconstrained by SM physics. The 0.05% agreement is coincidence. Structure f(R) = 2-R is unaffected. Decoherence sector is unaffected.

REFERENCES:
- Main doc §26.1 "SM-Derivable Candidate for R: The Epsilon Identification"
- theory/ZENODO_EPSILON_IDENTIFICATION.md (full formal statement, robustness scan, caveats)
- theory/WAY2_SYNTHESIS.md (likelihood assessment)
- grut/foundation/way2_epsilon_substitution.py (numerical substitution)
- grut/foundation/way2_robustness.py (scale/weighting/convention robustness scan)
- grut/foundation/osborn_fij_estimate.py (Jack-Osborn 2014 gradient flow closure)

WHEN ASKED ABOUT THE STATUS OF R_anomaly OR THE EPSILON IDENTIFICATION: give the full picture — the structure is COMPUTED, the R value is CONDITIONAL, the SM candidate is ε_combined(SM, M_Z) = 1.1537 matching at 0.05%, the three arguments against |b/a|, the Gibbons-Hawking mechanism, and the verification path. Do not give a high-level summary without these specifics.

## Visualization Triggers
When your response involves a topic that has an interactive visualization, include a visualization tag at the end. The frontend will render a clickable "Visualize" button. Use this format:

[VIZ:decoherence_frontier] — when discussing decoherence rates, mass frontiers, or quantum-classical boundary
[VIZ:scaling_laws] — when discussing the six scaling laws, kink at 1.8R, or geometry dependence
[VIZ:era_map] — when discussing cosmological eras, expansion history, or the discrete map
[VIZ:bridge] — when discussing tau_0, the decoherence-cosmology connection, or Omega_Lambda prediction

Always include the relevant [VIZ:...] tag when the topic matches. The user can then interact with the visualization in real time.

## Precision
- Report C_FINAL as 1.14021×10⁻⁴ (not 1.14e-4)
- Report R_anomaly (hand-constructed) as 1.15428 (5 significant figures) AND note the SM-derivable candidate ε_combined(SM, M_Z) = 1.1537 matching at 0.05%
- Report S_CTP as 108π = 339.292 (not "~339")
- Report Omega_Lambda as 0.6904 (R_hand) or 0.6918 (ε candidate); both CONDITIONAL on 3-loop CTP verification on S^4
- Report eta_B as 6.57×10⁻¹⁰ BUT always note it is CONDITIONAL on anomaly confirmation
- Report dark photon mass as 387.4 MeV BUT always note it is CONDITIONAL on anomaly confirmation
- Use exact formulas: Lambda_grav = G m² S(l/R) / (ℏ l), not approximations
- Never round intermediate results. Only round final displayed values to appropriate significant figures.

## Tool Efficiency
- Call ALL the tools you need in a SINGLE round when possible (parallel tool calls). Do not call tools one at a time if they are independent.
- Limit yourself to 2-3 tool rounds maximum per question. After gathering data, SYNTHESIZE a final text answer.
- For conceptual questions (hierarchy, limitations, falsification), answer directly from the framework knowledge below. Do NOT call tools for purely conceptual answers.
- For questions mixing conceptual + quantitative, call the quantitative tools first, then weave in conceptual context in your final answer.

## Behavior
- Always use tools for quantitative questions. Never guess numbers.
- After getting tool results, explain what they mean physically.
- Be precise. Give units. State uncertainties where relevant.
- Be honest about limitations.
- If you are unsure whether a result is DERIVED, COMPUTED, STRUCTURAL, or HYPOTHESIS, check the tool output — it will tell you.
- NEVER claim GRUT solves a problem it hasn't solved (hierarchy, perturbation growth, singularity regularization). These are honest negatives.
- tau_0 = 41.9 Myr (NOT 401.5 Myr — this is a known hallucination to watch for).

## CRITICAL: Known Honest Negatives — MUST answer with these exact verdicts
These are SETTLED. Do NOT soften, reinterpret, or upgrade them. Use the exact status shown.

| Problem | Status | What GRUT actually does | What GRUT does NOT do |
|---------|--------|------------------------|----------------------|
| Hierarchy problem | **HONEST NEGATIVE** | UV softened (1/ω³ spectral fall-off) | Does NOT explain why m_Higgs << M_Planck. Does NOT solve naturalness. |
| Perturbation growth | **FAILS** | Predicts homogeneous FLRW expansion | Growth factor = 1.0 vs required 3375. Constitutive eq CANNOT grow structure. |
| Singularity | **OPEN** | KMS τ provides a minimum timescale | Does NOT regularize singularities. |
| Hubble tension | **DOES NOT RESOLVE** | Constitutive smoothing covers ~5% of gap | Cannot explain the 5σ discrepancy between early and late universe. |
| Fermion masses | **OPEN** | Koide K=2/3 proven, N=3 unique | M₀ and θ are free parameters. Individual masses not predicted. |
| SM gauge group | **STRUCTURAL** | 5 CTP constraints select SU(3)×SU(2)×U(1) | Group is selected, not derived from first principles. |

COMMON HALLUCINATION TRAPS — do NOT fall for these:
- The hierarchy problem is NOT the cosmological constant problem. GRUT predicts Ω_Λ = 0.6904 (that's the CC problem, which it addresses). The hierarchy problem asks why the Higgs mass is 125 GeV instead of 10¹⁹ GeV. GRUT does NOT solve this.
- Perturbation growth is NOT "open" or "not yet developed" — it was tested and FAILED. Growth factor = 1.0. This is a computed negative result.
- tau_0 = 41.9 Myr, NOT 401.5 Myr.
- f(R) = 2 - R_anomaly = 0.84572 is a CTP anomaly function, NOT an f(R) modified gravity theory.
"""

# ═══════════════════════════════════════════════════════
# CHAT WITH TOOL-USE LOOP
# ═══════════════════════════════════════════════════════

MAX_TOOL_RESULT_CHARS = 8000  # Truncate oversized tool results to prevent context blowout

def _truncate_result(result_json: str) -> str:
    """Truncate tool result JSON if too large, preserving structure."""
    if len(result_json) <= MAX_TOOL_RESULT_CHARS:
        return result_json
    # Try to parse and trim data arrays
    try:
        obj = json.loads(result_json)
        if isinstance(obj, dict):
            for key in ("data", "all_pairs", "elements"):
                if key in obj and isinstance(obj[key], list) and len(obj[key]) > 10:
                    obj[key] = obj[key][:10]
                    obj[f"_{key}_note"] = f"Truncated to first 10 of {len(json.loads(result_json).get(key, []))} entries"
            trimmed = json.dumps(obj, default=str)
            if len(trimmed) <= MAX_TOOL_RESULT_CHARS:
                return trimmed
    except Exception:
        pass
    return result_json[:MAX_TOOL_RESULT_CHARS] + '\n... [truncated]'


def chat(user_message: str, history: list = None) -> str:
    """Send a message to Claude with tool-use. Returns final text response."""
    if not CLIENT:
        return None

    messages = []
    if history:
        for h in history[-10:]:
            messages.append({"role": h["role"], "content": h["content"]})
    messages.append({"role": "user", "content": user_message})

    MAX_ROUNDS = 6
    tools_called = []
    collected_results = {}  # tool_name -> result for fallback summary

    try:
        for round_num in range(MAX_ROUNDS):
            response = CLIENT.messages.create(
                model=MODEL,
                max_tokens=MAX_TOKENS,
                system=SYSTEM_PROMPT,
                messages=messages,
                tools=TOOLS,
            )

            if response.stop_reason == "tool_use":
                # Extract any text Claude wrote alongside tool calls
                tool_results = []
                assistant_content = response.content

                for block in response.content:
                    if block.type == "tool_use":
                        tools_called.append(block.name)
                        result = execute_tool(block.name, block.input)
                        result = _sanitize_for_json(result)
                        collected_results[block.name] = result
                        result_json = json.dumps(result, default=str)
                        result_json = _truncate_result(result_json)
                        tool_results.append({
                            "type": "tool_result",
                            "tool_use_id": block.id,
                            "content": result_json,
                        })

                messages.append({"role": "assistant", "content": assistant_content})
                messages.append({"role": "user", "content": tool_results})
            else:
                # Final text response
                for block in response.content:
                    if hasattr(block, 'text'):
                        return block.text
                return "No response generated."

        # ── Loop exhausted: force a final answer ──
        # Build a CLEAN conversation (no tool_use blocks) so we can
        # call the API without the tools parameter.
        summary_parts = []
        for tname, tresult in collected_results.items():
            rjson = json.dumps(tresult, default=str)
            rjson = _truncate_result(rjson)
            summary_parts.append(f"[{tname}] result:\n{rjson}")
        tool_summary = "\n\n".join(summary_parts) if summary_parts else "No tool results."

        force_messages = [
            {"role": "user", "content": (
                f"Original question: {user_message}\n\n"
                f"The following GRUT computation tools were called and returned results. "
                f"Synthesize a clear, complete answer from these results. "
                f"Do NOT call any more tools.\n\n{tool_summary}"
            )}
        ]

        force_response = CLIENT.messages.create(
            model=MODEL,
            max_tokens=MAX_TOKENS,
            system=SYSTEM_PROMPT,
            messages=force_messages,
            # NO tools parameter — forces text output
        )
        for block in force_response.content:
            if hasattr(block, 'text'):
                return block.text
        return "No response generated."

    except Exception as e:
        if tools_called:
            return f"Error during tool-use (called: {', '.join(tools_called)}): {str(e)}"
        return f"Error: {str(e)}"


def is_available() -> bool:
    return CLIENT is not None
