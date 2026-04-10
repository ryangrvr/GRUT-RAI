"""
Sector 13 — Falsifiability: Kill Conditions and Experimental Predictions

Every GRUT sector must document how it can be killed. Sector 13 is
speculative, so the kill conditions are especially important.

STATUS: Computed (structured kill conditions, testable predictions).
"""

import numpy as np
from grut_solver.sectors.consciousness.one_space import (
    one_space_entropy_bound, one_space_decomposition
)
from grut_solver.sectors.consciousness.boundary import (
    boundary_mass_at_temperature, boundary_width_neural
)
from grut_solver.sectors.consciousness.ordered_water import (
    ordered_water_decoherence_time, gap_analysis
)
from grut_solver.sectors.consciousness.pattern_survival import (
    topological_index_survival, entanglement_entropy_decay
)
from grut_solver.sectors.consciousness.resonance import (
    linear_resonance_condition
)
from grut_solver.sectors.consciousness.antenna import (
    coupling_efficiency, impedance_matching
)


def kill_conditions() -> list:
    """Structured list of conditions that would falsify Sector 13.

    Each entry has:
      description: what the test is
      measurement: how to test it
      threshold: what result kills the claim
      status: untested / testable / excluded
      kills: which speculative claim this invalidates
    """
    return [
        {
            "id": "K13-1",
            "description": "Ordered water in microtubules has bulk-like collision rates",
            "measurement": (
                "Neutron scattering or NMR relaxometry of water inside "
                "reconstituted microtubule channels"
            ),
            "threshold": "Confinement factor > 0.9 (within 10% of bulk)",
            "status": "testable",
            "kills": "ordered water correction (reduces gap improvement to < 1 order)",
        },
        {
            "id": "K13-2",
            "description": "No topological protection in microtubule lattice",
            "measurement": (
                "Measure vibrational coherence times of 13-protofilament "
                "vs disordered lattices at room temperature"
            ),
            "threshold": "No measurable difference in coherence time (< 2x)",
            "status": "testable",
            "kills": "topological index survival claim",
        },
        {
            "id": "K13-3",
            "description": "38,000-neuron number has no network significance",
            "measurement": (
                "Survey gamma-oscillation sources across species; check if "
                "the number of synchronized neurons correlates with tubulin mass"
            ),
            "threshold": "No correlation (r < 0.3) between neuron count and tubulin mass",
            "status": "testable",
            "kills": "resonance condition interpretation",
        },
        {
            "id": "K13-4",
            "description": "Gamma frequency varies with no mass dependence",
            "measurement": (
                "Compare gamma frequencies across species with different "
                "tubulin isoforms (different masses)"
            ),
            "threshold": "Gamma frequency uncorrelated with tubulin mass",
            "status": "testable",
            "kills": "mass-frequency gravitational resonance",
        },
        {
            "id": "K13-5",
            "description": "Anesthetics do not bind to microtubules",
            "measurement": (
                "High-resolution cryo-EM of anesthetic-microtubule complexes"
            ),
            "threshold": "No specific binding site found",
            "status": "partially tested (evidence supports binding)",
            "kills": "microtubule relevance to consciousness",
        },
        {
            "id": "K13-6",
            "description": "Consciousness persists with microtubule disruption",
            "measurement": (
                "Targeted microtubule disruption (e.g., colchicine) "
                "in cortical neurons; measure consciousness markers"
            ),
            "threshold": "Consciousness markers unchanged under disruption",
            "status": "testable (animal models)",
            "kills": "microtubule necessity for consciousness",
        },
        {
            "id": "K13-7",
            "description": "Mutual information decays at same rate as local coherence",
            "measurement": (
                "Quantum information experiment: measure I(A:B) decay in "
                "coupled spin chains under controlled dephasing"
            ),
            "threshold": "I(A:B) half-life equals single-spin T2",
            "status": "testable (NMR / ion trap)",
            "kills": "pattern survival mechanism (but our own computation already suggests this)",
        },
    ]


def experimental_predictions() -> list:
    """Specific testable predictions with numerical values.

    Each has:
      measurement: what to measure
      predicted_value: GRUT Sector 13 prediction
      uncertainty: range or error bar
      currently_testable: bool
      distinguishes_from: what standard physics predicts
    """
    # Get computed values
    water = ordered_water_decoherence_time()
    topo = topological_index_survival()
    res = linear_resonance_condition()

    return [
        {
            "id": "P13-1",
            "measurement": "Confined water decoherence time in MT-diameter pores",
            "predicted_value": f"{water['t_confined_s']:.2e} s",
            "predicted_range": "10^-14 to 10^-12 s (depending on confinement)",
            "bulk_value": f"{water['t_bulk_s']:.2e} s",
            "improvement": f"{water['improvement_orders']:.1f} orders",
            "currently_testable": True,
            "method": "Neutron spin echo in synthetic nanopores",
        },
        {
            "id": "P13-2",
            "measurement": "Topological coherence time on 13-site ring lattice",
            "predicted_value": f"{topo['t_survive_analytical_s']:.2e} s",
            "ratio_to_local": f"{topo['ratio_to_local']:.2f}x",
            "currently_testable": True,
            "method": "Engineered spin lattice (superconducting qubits / ion trap)",
        },
        {
            "id": "P13-3",
            "measurement": "Neuron count for gamma oscillation",
            "predicted_value": f"{res['N_neurons']:.0f} neurons",
            "predicted_range": "30,000 — 45,000 (varies with tubulin mass uncertainty)",
            "currently_testable": True,
            "method": "Calcium imaging of gamma-synchronized cortical networks",
        },
        {
            "id": "P13-4",
            "measurement": "Cross-species gamma frequency vs tubulin mass",
            "predicted_value": "f_gamma proportional to 1/m_tubulin^2",
            "currently_testable": True,
            "method": "Comparative neuroscience EEG + mass spectrometry",
        },
        {
            "id": "P13-5",
            "measurement": "GHZ entanglement entropy decay rate",
            "predicted_value": "N times faster than single-qubit T2",
            "currently_testable": True,
            "method": "Multi-qubit GHZ state preparation + dephasing",
            "note": "This DISFAVORS naive pattern survival — honest prediction",
        },
    ]


def adversarial_summary() -> dict:
    """Complete honest assessment of Sector 13.

    Categorizes every result into:
      computed: derived from first principles or standard physics
      model_dependent: requires assumptions about parameters
      speculative: no formal derivation, conceptual framework only
    """
    computed = [
        {
            "name": "Bekenstein/holographic entropy bound",
            "value": "~10^122 bits",
            "source": "Standard physics (Bekenstein 1973, 't Hooft 1993)",
            "grut_specific": False,
        },
        {
            "name": "Gravitational decoherence per tubulin dimer",
            "value": "3.02e-11 Hz",
            "source": "USL with zero free parameters",
            "grut_specific": True,
        },
        {
            "name": "N neurons for 40 Hz (linear scaling)",
            "value": "~33,000-38,000",
            "source": "Direct division of USL rate",
            "grut_specific": True,
        },
        {
            "name": "Thermal wall at 310 K",
            "value": "~10^25 orders gap",
            "source": "Standard scattering physics",
            "grut_specific": False,
        },
        {
            "name": "Ordered water improvement",
            "value": "2-4 orders reduction (gap NOT closed)",
            "source": "Confined water literature + parametric scan",
            "grut_specific": False,
        },
        {
            "name": "Topological index survival",
            "value": "WORSE than local coherence for uncorrelated noise",
            "source": "Random walk on 13-site ring (analytical)",
            "grut_specific": False,
            "note": "Honest negative: winding number error grows as sqrt(N)",
        },
        {
            "name": "GHZ entropy decay",
            "value": "N times faster than single qubit",
            "source": "Standard Lindblad / decoherence theory",
            "grut_specific": False,
            "note": "DISFAVORS pattern survival via entanglement",
        },
    ]

    model_dependent = [
        {
            "name": "Confinement factor for MT water",
            "value": "0.5-0.95 (empirical model)",
            "assumption": "Exponential decay model for confinement effects",
        },
        {
            "name": "Network resonance correction",
            "value": "Depends on connectivity k and phase coherence",
            "assumption": "Random vs phase-locked neuron coupling",
        },
        {
            "name": "Coupling efficiency",
            "value": "~10^-80 (information-theoretic bound)",
            "assumption": "Holographic bound as D_total; binary dimer DOF",
        },
        {
            "name": "Information rate bound",
            "value": "Shannon-Hartley analogy",
            "assumption": "Classical channel capacity formula applied to quantum system",
        },
    ]

    speculative = [
        {
            "name": "1 Space as seat of consciousness",
            "status": "No formal derivation. Philosophical framework.",
            "testable": False,
        },
        {
            "name": "Consciousness as edge state at QC boundary",
            "status": "Conceptual. No dynamical equation proposed.",
            "testable": False,
        },
        {
            "name": "Brain as antenna coupling to F[z]",
            "status": "Analogy. Coupling mechanism not specified.",
            "testable": False,
        },
        {
            "name": "Pattern-level coupling survives thermal wall",
            "status": (
                "Our OWN computations suggest this is unlikely: "
                "GHZ states decohere FASTER with more qubits, "
                "topological protection gains < 2 orders, "
                "ordered water gains < 4 orders. "
                "The 25-order gap is NOT closed by any known mechanism."
            ),
            "testable": True,
            "note": "Sector 13's own adversarial finding.",
        },
        {
            "name": "Impedance matching has physical significance",
            "status": "The match at 38,000 neurons is by construction (tautology).",
            "testable": False,
        },
    ]

    # Overall verdict
    gap_analysis_result = gap_analysis()
    topo = topological_index_survival()

    topo_ratio = topo["ratio_to_local"]
    topo_log = np.log10(topo_ratio) if topo_ratio > 0 else 0
    total_improvement_orders = (
        gap_analysis_result["physical_estimate"]["improvement_orders"]
        + max(0, topo_log)  # only count if topology actually helps
    )
    remaining_gap = 25 - total_improvement_orders

    verdict = {
        "thermal_wall_original_gap": 25,
        "ordered_water_gain_orders": gap_analysis_result["physical_estimate"]["improvement_orders"],
        "topological_gain_orders": max(0, topo_log),
        "total_improvement_orders": total_improvement_orders,
        "remaining_gap_orders": remaining_gap,
        "gap_closed": remaining_gap <= 0,
        "honest_assessment": (
            f"Starting gap: ~25 orders. "
            f"Ordered water: ~{gap_analysis_result['physical_estimate']['improvement_orders']:.1f} orders. "
            f"Topological protection: ~{max(0, topo_log):.1f} orders (0 for uncorrelated noise). "
            f"Remaining gap: ~{remaining_gap:.0f} orders. "
            f"VERDICT: The thermal wall is NOT breached by any mechanism "
            f"we can compute. If consciousness involves gravitational "
            f"decoherence of tubulin, something beyond current physics "
            f"is required. Sector 13 documents what we CAN compute "
            f"and honestly reports the gap."
        ),
    }

    return {
        "computed": computed,
        "model_dependent": model_dependent,
        "speculative": speculative,
        "n_computed": len(computed),
        "n_model_dependent": len(model_dependent),
        "n_speculative": len(speculative),
        "verdict": verdict,
    }
