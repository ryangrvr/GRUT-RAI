"""GRUT RAI v2 — API Routes (complete with all derived modules)"""
import sys, os, json, numpy as np
from flask import Blueprint, request, Response

sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', '..'))

from grut.foundation import constants, axioms, constitutive, noise_kernel, anomaly
from ui.ai.chat import chat as ai_chat, is_available as ai_available

api = Blueprint('api', __name__)

def _sanitize(obj):
    if isinstance(obj, dict): return {k: _sanitize(v) for k, v in obj.items()}
    if isinstance(obj, list): return [_sanitize(v) for v in obj]
    if isinstance(obj, (np.bool_, np.generic)): return obj.item()
    if isinstance(obj, np.ndarray): return obj.tolist()
    if isinstance(obj, float) and (np.isnan(obj) or np.isinf(obj)): return str(obj)
    return obj

def jsonify(obj):
    return Response(json.dumps(_sanitize(obj)), mimetype='application/json')

# ═══ Foundation ═══
@api.route('/health')
def health():
    results = {}
    for name, mod in [('constants', constants), ('axioms', axioms),
                       ('constitutive', constitutive), ('noise_kernel', noise_kernel), ('anomaly', anomaly)]:
        results[name] = mod.verify()
    return jsonify({"status": "ok" if all(v for d in results.values() for v in d.values()) else "degraded", "modules": results})

@api.route('/constants')
def get_constants():
    return jsonify({"G": constants.G, "HBAR": constants.HBAR, "C": constants.C, "K_B": constants.K_B,
                     "AMU": constants.AMU, "M_PLANCK": constants.M_PLANCK, "L_PLANCK": constants.L_PLANCK,
                     "T_PLANCK": constants.T_PLANCK, "ALPHA_EM": constants.ALPHA_EM, "TAU_I": axioms.TAU_I,
                     "C_FINAL": anomaly.C_FINAL, "R_ANOMALY": anomaly.R_ANOMALY, "S_CTP": anomaly.S_CTP})

@api.route('/decoherence')
def decoherence():
    m = float(request.args.get('m', 80.8e-15)); l = float(request.args.get('l', 1e-6))
    R = request.args.get('R'); R = float(R) if R else None
    L = noise_kernel.lambda_grav(m, l, R); S = noise_kernel.extended_body_suppression(l, R) if R else 1.0
    return jsonify({"Lambda_grav_Hz": L, "t_coh_s": 1/L if L > 0 else float('inf'), "m_kg": m, "l_m": l, "R_m": R, "S_l_R": S})

@api.route('/decoherence/sweep_separation')
def sweep_sep():
    m=float(request.args.get('m',80.8e-15)); R=float(request.args.get('R',1e-6))
    l_min=float(request.args.get('l_min',1e-8)); l_max=float(request.args.get('l_max',1e-4)); n=int(request.args.get('n',80))
    ls=np.logspace(np.log10(l_min),np.log10(l_max),n)
    return jsonify({"m":m,"R":R,"kink_at":1.8*R,"data":[{"l":float(l),"Lambda":float(noise_kernel.lambda_grav(m,l,R)),"S":float(noise_kernel.extended_body_suppression(l,R))} for l in ls]})

@api.route('/decoherence/sweep_mass')
def sweep_mass():
    l=float(request.args.get('l',1e-6)); R=request.args.get('R'); R_f=float(R) if R else None
    m_min=float(request.args.get('m_min',1e-24)); m_max=float(request.args.get('m_max',1e-9)); n=int(request.args.get('n',80))
    ms=np.logspace(np.log10(m_min),np.log10(m_max),n)
    return jsonify({"l":l,"R":R_f,"data":[{"m":float(m),"Lambda":float(noise_kernel.lambda_grav(m,l,R_f))} for m in ms]})

@api.route('/decoherence/material')
def material():
    m=float(request.args.get('m',80.8e-15)); rho=float(request.args.get('rho',19300)); l=float(request.args.get('l',1e-6))
    from grut.derived.decoherence.sector import material_calculator
    return jsonify(material_calculator(m, rho, l))

@api.route('/anomaly')
def get_anomaly():
    return jsonify({"C_FINAL":anomaly.C_FINAL,"C_COSMO":float(anomaly.c_cosmo()),"R_ANOMALY":anomaly.R_ANOMALY,"S_CTP":anomaly.S_CTP,"f_R":2-anomaly.R_ANOMALY})

# ═══ Bridge ═══
@api.route('/bridge')
def bridge():
    from grut.bridge.parameter import bridge_prediction
    H0 = float(request.args.get('H_0', 70.0))
    return jsonify(bridge_prediction(H0))

@api.route('/bridge/experimental')
def bridge_exp():
    from grut.bridge.parameter import experimental_chain
    m=float(request.args.get('m',80.8e-15)); l=float(request.args.get('l',1e-6))
    R=float(request.args.get('R',1e-6)); L=float(request.args.get('lambda_grav',689))
    return jsonify(experimental_chain(m, l, R, L))

# ═══ Derived: Baryogenesis ═══
@api.route('/baryogenesis')
def baryogenesis():
    from grut.derived.baryogenesis.eta import compute_eta_b
    route = int(request.args.get('route', 1))
    return jsonify(compute_eta_b(route))

# ═══ Derived: Dark Matter ═══
@api.route('/dark_matter')
def dark_matter():
    from grut.derived.dark_matter.sector import branch_discriminator
    return jsonify(branch_discriminator())

@api.route('/dark_matter/route1')
def dm_route1():
    from grut.derived.dark_matter.sector import route_1
    return jsonify(route_1())

# ═══ Derived: Cosmology ═══
@api.route('/cosmology/vacuum')
def cosmo_vacuum():
    from grut.derived.cosmology.vacuum import vacuum_prediction
    H0 = float(request.args.get('H_0', 70.0))
    return jsonify(vacuum_prediction(H0))

@api.route('/cosmology/era_map')
def cosmo_era():
    from grut.derived.cosmology.vacuum import era_map
    return jsonify(era_map())

# ═══ Derived: Koide ═══
@api.route('/koide')
def koide():
    from grut.derived.koide.identity import koide_check, n_generation_uniqueness, fit_leptons
    return jsonify({"koide": koide_check(), "generations": n_generation_uniqueness(), "fit": fit_leptons()})

# ═══ Derived: SM Emergence ═══
@api.route('/sm_emergence')
def sm_emergence():
    from grut.derived.sm_emergence.constraints import five_constraints
    return jsonify(five_constraints())

# ═══ Derived: Quantum Gravity ═══
@api.route('/quantum_gravity')
def qg():
    from grut.derived.quantum_gravity.closure import closure_conditions, nonlinear_ladder
    return jsonify({"closure": closure_conditions(), "ladder": nonlinear_ladder()})

# ═══ Utils: Sensitivity ═══
@api.route('/sensitivity')
def sensitivity():
    from grut.utils.sweep import sensitivity_omega_lambda
    delta = float(request.args.get('delta_pct', 10))
    return jsonify(sensitivity_omega_lambda(delta))

@api.route('/uncertainty')
def uncertainty():
    from grut.utils.sweep import uncertainty_propagation
    m=float(request.args.get('m',80.8e-15)); l=float(request.args.get('l',1e-6)); R=float(request.args.get('R',1e-6))
    return jsonify(uncertainty_propagation(m, l, R))

# ═══ Utils: Experimental Data ═══
@api.route('/data/planck')
def data_planck():
    from grut.utils.data import PLANCK_2018
    return jsonify(PLANCK_2018)

@api.route('/data/pdg')
def data_pdg():
    from grut.utils.data import PDG_MASSES, PDG_CONSTANTS
    return jsonify({"masses": PDG_MASSES, "constants": PDG_CONSTANTS})

@api.route('/data/materials')
def data_materials():
    from grut.utils.data import MATERIALS
    return jsonify(MATERIALS)

# ═══ Utils: Dimensions ═══
@api.route('/dimensions')
def dimensions():
    from grut.utils.dimensions import check_all
    return jsonify(check_all())

# ═══ Constitutive Solver ═══
@api.route('/constitutive/evolve')
def evolve():
    z0=float(request.args.get('z0',1.0)); z_tgt=float(request.args.get('z_target',0.0))
    tau=float(request.args.get('tau',1.0)); dt=float(request.args.get('dt',0.1)); n=int(request.args.get('n_steps',100))
    data=[{"t":0,"z":z0}]; z=z0
    for i in range(1,n+1):
        z=constitutive.constitutive_step(z,z_tgt,tau,dt); data.append({"t":float(i*dt),"z":float(z)})
    return jsonify({"z0":z0,"z_target":z_tgt,"tau":tau,"data":data})

@api.route('/constitutive/cosmology')
def cosmo_evolve():
    from grut.derived.cosmology.vacuum import constitutive_cosmology
    d = constitutive_cosmology(n_steps=500)
    # Subsample for JSON
    step = max(1, len(d["t"])//200)
    return jsonify({"t": d["t"][::step], "H": d["H"][::step], "H_inf": d["H_inf"]})

# ═══ AI Chat ═══
@api.route('/chat', methods=['POST'])
def chat_endpoint():
    data = request.get_json() or {}
    msg = data.get('message', ''); history = data.get('history', [])
    if not msg: return jsonify({"error": "No message"}), 400
    if ai_available():
        resp = ai_chat(msg, history)
        if resp: return jsonify({"response": resp, "source": "claude"})
    return jsonify({"response": None, "source": "fallback"})

@api.route('/chat/status')
def chat_status():
    return jsonify({"ai_available": ai_available()})

# ═══ Suppression ═══
@api.route('/suppression')
def suppression():
    R=float(request.args.get('R',1e-6)); n=int(request.args.get('n',100))
    ls=np.logspace(-9,-3,n)
    return jsonify({"R":R,"data":[{"l":float(l),"S":float(noise_kernel.extended_body_suppression(l,R)),"l_over_R":float(l/R)} for l in ls]})

@api.route('/tau_kms')
def tau_kms():
    T=float(request.args.get('T',300))
    return jsonify({"T_kelvin":T,"tau_kms_s":noise_kernel.tau_kms(T)})

# ═══ Theory Comparison ═══
@api.route('/compare/decoherence')
def compare_decoherence():
    from grut.utils.compare import decoherence_comparison
    m=float(request.args.get('m',80.8e-15)); l=float(request.args.get('l',1e-6)); R=float(request.args.get('R',1e-6))
    return jsonify(decoherence_comparison(m, l, R))

@api.route('/compare/cosmology')
def compare_cosmology():
    from grut.utils.compare import cosmology_comparison
    return jsonify(cosmology_comparison())

@api.route('/compare/baryogenesis')
def compare_baryogenesis():
    from grut.utils.compare import baryogenesis_comparison
    return jsonify(baryogenesis_comparison())

@api.route('/compare/dark_matter')
def compare_dark_matter():
    from grut.utils.compare import dark_matter_comparison
    return jsonify(dark_matter_comparison())

@api.route('/compare/all')
def compare_all():
    from grut.utils.compare import full_comparison
    return jsonify(full_comparison())

# ═══ What-If Theory Builder ═══
@api.route('/whatif')
def whatif():
    from grut.utils.whatif import run_whatif
    param = request.args.get('parameter', 'R_anomaly')
    value = float(request.args.get('value', 1.15428))
    return jsonify(run_whatif(param, value))

# ═══ Experiment Designer ═══
@api.route('/experiment/design')
def exp_design():
    from grut.utils.experiment import design_decoherence_experiment
    target = float(request.args.get('target_Lambda', 100))
    return jsonify(design_decoherence_experiment(target))

@api.route('/experiment/snr')
def exp_snr():
    from grut.utils.experiment import snr_calculator
    m=float(request.args.get('m',80.8e-15)); l=float(request.args.get('l',1e-6))
    R=float(request.args.get('R',1e-6)); t=float(request.args.get('t',1.0))
    noise=float(request.args.get('noise',0))
    return jsonify(snr_calculator(m, l, R, t, noise))

@api.route('/experiment/material')
def exp_material():
    from grut.utils.experiment import optimal_material
    m=float(request.args.get('m',80.8e-15)); l=float(request.args.get('l',1e-6))
    return jsonify(optimal_material(m, l))

# ═══ Pedagogy ═══
@api.route('/walkthrough')
def walkthrough_list():
    from grut.utils.pedagogy import list_walkthroughs
    return jsonify(list_walkthroughs())

@api.route('/walkthrough/<wid>')
def walkthrough(wid):
    from grut.utils.pedagogy import get_walkthrough
    return jsonify(get_walkthrough(wid))

# ═══ Discovery ═══
@api.route('/discovery')
def discovery():
    from grut.utils.discovery import full_discovery
    return jsonify(full_discovery())

@api.route('/discovery/coincidences')
def coincidences():
    from grut.utils.discovery import find_numerical_coincidences
    threshold = float(request.args.get('threshold', 0.05))
    return jsonify(find_numerical_coincidences(threshold))

@api.route('/discovery/connections')
def connections():
    from grut.utils.discovery import find_scale_connections
    return jsonify(find_scale_connections())

# ═══ Decoherence Competition ═══
@api.route('/decoherence/competition')
def decoherence_competition():
    from grut.derived.decoherence.competition import competition
    m=float(request.args.get('m_amu', 1e9))*1.661e-27
    l=float(request.args.get('l', 1e-7)); P=float(request.args.get('P', 1e-14))
    T=float(request.args.get('T', 4.0))
    return jsonify(competition(m, l, P, T))

@api.route('/decoherence/temperature_sweep')
def decoherence_temp_sweep():
    from grut.derived.decoherence.competition import temperature_sweep
    m=float(request.args.get('m_amu', 1e9))*1.661e-27
    l=float(request.args.get('l', 1e-7)); P=float(request.args.get('P', 1e-14))
    return jsonify(temperature_sweep(m, l, P))

@api.route('/decoherence/phase_diagram')
def decoherence_phase():
    from grut.derived.decoherence.competition import phase_diagram
    T=float(request.args.get('T', 4.0))
    return jsonify(phase_diagram(T_K=T))

@api.route('/decoherence/scaling_exponents')
def decoherence_exponents():
    from grut.derived.decoherence.competition import scaling_exponents
    return jsonify(scaling_exponents())

@api.route('/decoherence/protocols')
def decoherence_protocols():
    from grut.derived.decoherence.competition import experimental_protocols
    return jsonify(experimental_protocols())

@api.route('/decoherence/optimal')
def decoherence_optimal():
    from grut.derived.decoherence.competition import optimal_setup
    return jsonify(optimal_setup())

@api.route('/decoherence/full_analysis')
def decoherence_full():
    from grut.derived.decoherence.competition import full_competition_analysis
    m=float(request.args.get('m_amu', 1e9))
    l=float(request.args.get('l', 1e-7)); P=float(request.args.get('P', 1e-14))
    T=float(request.args.get('T', 4.0))
    return jsonify(full_competition_analysis(m, l, P, T))

# ═══ Geometry Kink Scan ═══
@api.route('/decoherence/kink_scan')
def kink_scan():
    from grut.derived.decoherence.kink_scan import kink_scan as ks
    m=float(request.args.get('m_amu', 1e9))*1.661e-27
    rho=float(request.args.get('rho', 19300))
    return jsonify(ks(m, rho))

@api.route('/decoherence/material_comparison')
def material_comp():
    from grut.derived.decoherence.kink_scan import material_comparison
    m=float(request.args.get('m_amu', 1e9))*1.661e-27
    l=float(request.args.get('l', 1e-7))
    return jsonify(material_comparison(m, l))

@api.route('/decoherence/kink_full')
def kink_full():
    from grut.derived.decoherence.kink_scan import full_kink_analysis
    m=float(request.args.get('m_amu', 1e9))
    return jsonify(full_kink_analysis(m))

# ═══ Material Swap Experiment ═══
@api.route('/decoherence/material_swap')
def mat_swap():
    from grut.derived.decoherence.material_swap import material_swap_experiment
    m=float(request.args.get('m_amu', 1e9)); l=float(request.args.get('l', 1e-7))
    a=request.args.get('mat_a', 'gold'); b=request.args.get('mat_b', 'silica')
    return jsonify(material_swap_experiment(m, l, a, b))

@api.route('/decoherence/optimal_pair')
def opt_pair():
    from grut.derived.decoherence.material_swap import optimal_material_pair
    m=float(request.args.get('m_amu', 1e9)); l=float(request.args.get('l', 1e-7))
    return jsonify(optimal_material_pair(m, l))

@api.route('/decoherence/ratio_scan')
def ratio_scan():
    from grut.derived.decoherence.material_swap import separation_scan_two_materials
    m=float(request.args.get('m_amu', 1e9))
    a=request.args.get('mat_a', 'gold'); b=request.args.get('mat_b', 'silica')
    return jsonify(separation_scan_two_materials(m, a, b))

# ═══ Hubble Tension ═══
@api.route('/cosmology/hubble_tension')
def hubble_tension():
    from grut.derived.cosmology.hubble_tension import hubble_tension_analysis
    return jsonify(hubble_tension_analysis())

@api.route('/cosmology/grut_curve')
def grut_curve():
    from grut.derived.cosmology.hubble_tension import grut_prediction_curve
    return jsonify(grut_prediction_curve())

@api.route('/cosmology/consistency')
def cosmo_consistency():
    from grut.derived.cosmology.hubble_tension import consistency_test
    return jsonify(consistency_test())
