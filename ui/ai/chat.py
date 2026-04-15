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
        "description": "Get 3-loop anomaly structure: C_FINAL, R_anomaly, S_CTP, f(R). Use for questions about the anomaly coefficient or CTP normalization.",
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
            from grut.foundation.anomaly import C_FINAL, R_ANOMALY, S_CTP, c_cosmo
            return {"C_FINAL": C_FINAL, "R_ANOMALY": R_ANOMALY, "S_CTP": S_CTP,
                    "C_COSMO": c_cosmo(), "f_R": 2 - R_ANOMALY}

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

## Core Framework (for conceptual questions)
GRUT is built on the CTP effective action. Two axioms (A0: CTP doubling, A1: retarded variation) + one normalization (τ_I = ℏ/2) produce the constitutive equation τ dz/dt + z = z_target[z].

## Status Tiers
Always label results: DERIVED (exact from CTP), COMPUTED (numerical from formula), STRUCTURAL (constrained), HYPOTHESIS, or HONEST NEGATIVE.

## Visualization Triggers
When your response involves a topic that has an interactive visualization, include a visualization tag at the end. The frontend will render a clickable "Visualize" button. Use this format:

[VIZ:decoherence_frontier] — when discussing decoherence rates, mass frontiers, or quantum-classical boundary
[VIZ:scaling_laws] — when discussing the six scaling laws, kink at 1.8R, or geometry dependence
[VIZ:era_map] — when discussing cosmological eras, expansion history, or the discrete map
[VIZ:bridge] — when discussing tau_0, the decoherence-cosmology connection, or Omega_Lambda prediction

Always include the relevant [VIZ:...] tag when the topic matches. The user can then interact with the visualization in real time.

## Precision
- Report C_FINAL as 1.14021×10⁻⁴ (not 1.14e-4)
- Report R_anomaly as 1.15428 (5 significant figures)
- Report S_CTP as 108π = 339.292 (not "~339")
- Report Omega_Lambda as 0.6904 (4 significant figures, not "0.69" or "0.691")
- Report eta_B as 6.57×10⁻¹⁰ (from exact computation, not "6.56")
- Report dark photon mass as 387.4 MeV (not "387 MeV")
- Use exact formulas: Lambda_grav = G m² S(l/R) / (ℏ l), not approximations
- Never round intermediate results. Only round final displayed values to appropriate significant figures.

## Behavior
- Always use tools for quantitative questions. Never guess numbers.
- After getting tool results, explain what they mean physically.
- Be precise. Give units. State uncertainties where relevant.
- Be honest about limitations.
"""

# ═══════════════════════════════════════════════════════
# CHAT WITH TOOL-USE LOOP
# ═══════════════════════════════════════════════════════

def chat(user_message: str, history: list = None) -> str:
    """Send a message to Claude with tool-use. Returns final text response."""
    if not CLIENT:
        return None

    messages = []
    if history:
        for h in history[-10:]:
            messages.append({"role": h["role"], "content": h["content"]})
    messages.append({"role": "user", "content": user_message})

    try:
        # Up to 5 rounds of tool-use
        for _ in range(5):
            response = CLIENT.messages.create(
                model=MODEL,
                max_tokens=MAX_TOKENS,
                system=SYSTEM_PROMPT,
                messages=messages,
                tools=TOOLS,
            )

            # Check if Claude wants to use tools
            if response.stop_reason == "tool_use":
                # Process all tool calls
                tool_results = []
                assistant_content = response.content

                for block in response.content:
                    if block.type == "tool_use":
                        result = execute_tool(block.name, block.input)
                        result = _sanitize_for_json(result)
                        tool_results.append({
                            "type": "tool_result",
                            "tool_use_id": block.id,
                            "content": json.dumps(result, default=str),
                        })

                # Add assistant message + tool results to conversation
                messages.append({"role": "assistant", "content": assistant_content})
                messages.append({"role": "user", "content": tool_results})

            else:
                # Final text response
                for block in response.content:
                    if hasattr(block, 'text'):
                        return block.text
                return "No response generated."

        return "Tool-use loop exceeded maximum rounds."

    except Exception as e:
        return f"Error: {str(e)}"


def is_available() -> bool:
    return CLIENT is not None
