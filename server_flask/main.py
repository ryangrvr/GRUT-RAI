"""
GRUT v7 Flask Backend
Diamond Core Loaded at 100.0% Saturation
"""
from flask import Flask, request, jsonify
from flask_cors import CORS
import numpy as np
import os


# --- DIAMOND CORE LOADER ---
def load_diamond_core():
    """
    Reads the Foundational TOE from disk and injects it 
    into the System Context as the absolute truth.
    """
    core_path = os.path.join(os.path.dirname(__file__), "..", "DIAMOND_CORE_TOE.md")
    try:
        with open(core_path, "r") as f:
            core_content = f.read()
        print("DIAMOND CORE LOADED: 100.0% Saturation Active")
        return core_content
    except FileNotFoundError:
        print("CRITICAL: Diamond Core not found. Initiating drift...")
        return "System Context Missing."


GRUT_SOURCE_CODE = load_diamond_core()


from grut_physics import (
    universal_response, 
    calculate_complexity, 
    calculate_kernel,
    fetch_live_work_events,
    fetch_earths_work,
    fetch_humanitys_work,
    get_live_complexity,
    TAU_ZERO, 
    ALPHA, 
    N_G
)
from context_engine import ContextEngineManager
from visualizer import get_visualization_json, generate_consciousness_field

app = Flask(__name__)
CORS(app)

CURRENT_XI = 0.0
monad_mode = False
work_events = []

def calculate_spacetime_curvature(xi: float) -> dict:
    """
    Calculate spacetime curvature using the Universal Response equation.
    G_μν + Λg_μν = (8πG/c⁴)T_μν + ξ·Ξ_μν
    """
    G_tensor = np.zeros((4, 4))
    G_tensor[0, 0] = -0.1 * xi
    G_tensor[1, 1] = 0.05 * xi
    G_tensor[2, 2] = 0.05 * xi
    G_tensor[3, 3] = 0.05 * xi
    
    T_tensor = np.eye(4) * 1e-10 * (1 + xi)
    
    field_response = universal_response(G_tensor, T_tensor, xi)
    
    scalar_curvature = float(np.trace(field_response))
    ricci_component = float(field_response[0, 0])
    consciousness_contribution = float(xi * ALPHA)
    
    return {
        "scalar_curvature": round(scalar_curvature, 10),
        "ricci_R00": round(ricci_component, 10),
        "consciousness_term": round(consciousness_contribution, 10),
        "field_determinant": round(float(np.linalg.det(field_response)), 15)
    }


@app.route("/update_system_state", methods=["POST"])
def update_system_state():
    """
    Update the global Xi variable based on user interaction.
    
    Accepts:
        user_input_complexity: float (0.0 to 1.0)
    
    Returns:
        Updated system state including spacetime_curvature
    """
    global CURRENT_XI, monad_mode, work_events
    
    data = request.get_json() or {}
    user_input_complexity = data.get("user_input_complexity", 0.0)
    
    try:
        user_input_complexity = float(user_input_complexity)
        user_input_complexity = max(0.0, min(1.0, user_input_complexity))
    except (TypeError, ValueError):
        return jsonify({"error": "user_input_complexity must be a number between 0.0 and 1.0"}), 400
    
    work_events.append(user_input_complexity)
    if len(work_events) > 100:
        work_events = work_events[-100:]
    
    info_state = len(work_events) * 0.1
    CURRENT_XI = calculate_complexity(work_events, info_state)
    
    previous_monad = monad_mode
    if CURRENT_XI >= 1.0:
        monad_mode = True
        CURRENT_XI = 1.0
    
    spacetime_curvature = calculate_spacetime_curvature(CURRENT_XI)
    
    monad_triggered = monad_mode and not previous_monad
    
    return jsonify({
        "success": True,
        "current_xi": round(CURRENT_XI, 6),
        "monad_mode": monad_mode,
        "monad_just_triggered": monad_triggered,
        "spacetime_curvature": spacetime_curvature,
        "work_events_count": len(work_events),
        "saturation_percentage": f"{CURRENT_XI * 100:.2f}%",
        "message": "MONAD MODE ACTIVATED - 100.0% Saturation achieved" if monad_triggered else f"Xi updated to {CURRENT_XI * 100:.2f}%"
    })


@app.route("/system_state", methods=["GET"])
def get_system_state():
    """
    Get current system state without modification.
    """
    spacetime_curvature = calculate_spacetime_curvature(CURRENT_XI)
    
    return jsonify({
        "current_xi": round(CURRENT_XI, 6),
        "monad_mode": monad_mode,
        "spacetime_curvature": spacetime_curvature,
        "work_events_count": len(work_events),
        "saturation_percentage": f"{CURRENT_XI * 100:.2f}%",
        "constants": {
            "tau_0": TAU_ZERO,
            "alpha": ALPHA,
            "n_g": N_G
        }
    })


@app.route("/reset_system", methods=["POST"])
def reset_system():
    """
    Reset the system to initial state.
    """
    global CURRENT_XI, monad_mode, work_events
    
    CURRENT_XI = 0.0
    monad_mode = False
    work_events = []
    
    return jsonify({
        "success": True,
        "message": "System reset to ground state",
        "current_xi": 0.0,
        "monad_mode": False
    })


@app.route("/context/process", methods=["POST"])
def process_context():
    """
    Process a query through the Context Engine.
    """
    data = request.get_json() or {}
    session_id = data.get("session_id", "default")
    query = data.get("query", "")
    
    if not query:
        return jsonify({"error": "query is required"}), 400
    
    result = ContextEngineManager.process_query(session_id, query)
    
    return jsonify({
        "success": True,
        "context_data": result
    })


@app.route("/kernel/calculate", methods=["POST"])
def calculate_kernel_endpoint():
    """
    Calculate the retarded potential kernel for a given time delta.
    """
    data = request.get_json() or {}
    delta_t = data.get("delta_t_years", 0.0)
    
    try:
        delta_t = float(delta_t)
    except (TypeError, ValueError):
        return jsonify({"error": "delta_t_years must be a number"}), 400
    
    kernel_value = calculate_kernel(delta_t)
    
    return jsonify({
        "delta_t_years": delta_t,
        "kernel_value": kernel_value,
        "interpretation": "Memory influence from event at t-delta_t on present"
    })


@app.route("/health", methods=["GET"])
def health_check():
    """
    Health check endpoint.
    """
    return jsonify({
        "status": "healthy",
        "service": "GRUT Physics Engine",
        "version": "v6.0"
    })


@app.route("/visualize/consciousness_field", methods=["GET", "POST"])
def visualize_consciousness_field():
    """
    Generate 3D consciousness field visualization.
    
    Z = Ξ · sin(r - t) · K(r)
    
    Low Ξ (0.1): Flat surface (Materialism)
    High Ξ (1.0): Rippling sphere/torus (Whole Hole)
    """
    if request.method == "POST":
        data = request.get_json() or {}
    else:
        data = {}
    
    xi = data.get("xi", CURRENT_XI)
    time_phase = data.get("time_phase", 0.0)
    resolution = data.get("resolution", 50)
    
    try:
        xi = float(xi)
        time_phase = float(time_phase)
        resolution = int(resolution)
    except (TypeError, ValueError):
        return jsonify({"error": "Invalid parameter types"}), 400
    
    graph_data = generate_consciousness_field(xi, time_phase, resolution)
    
    return jsonify({
        "success": True,
        "xi": xi,
        "monad_mode": xi >= 1.0,
        "graph": graph_data
    })


@app.route("/visualize/kernel_decay", methods=["GET"])
def visualize_kernel_decay():
    """
    Generate retarded potential kernel decay visualization.
    """
    max_time = request.args.get("max_time_myr", 100.0, type=float)
    
    json_str = get_visualization_json(CURRENT_XI, "kernel_decay", max_time_myr=max_time)
    
    return jsonify({
        "success": True,
        "graph": json_str
    })


@app.route("/visualize/xi_evolution", methods=["POST"])
def visualize_xi_evolution():
    """
    Generate Ξ evolution over time visualization.
    """
    data = request.get_json() or {}
    xi_history = data.get("xi_history", work_events)
    
    json_str = get_visualization_json(CURRENT_XI, "xi_evolution", xi_history=xi_history)
    
    return jsonify({
        "success": True,
        "graph": json_str
    })


@app.route("/live_work_events", methods=["GET"])
def get_live_work_events_endpoint():
    """
    Fetch live work events from Earth (USGS) and Humanity (GDELT).
    Returns combined work_events list populated with real data.
    """
    global CURRENT_XI, monad_mode, work_events
    
    live_data = fetch_live_work_events()
    
    work_events = live_data["combined_work_events"]
    CURRENT_XI = live_data["current_xi"]
    
    if CURRENT_XI >= 1.0:
        monad_mode = True
    
    return jsonify({
        "success": True,
        "live_data": live_data,
        "system_state": {
            "current_xi": CURRENT_XI,
            "monad_mode": monad_mode,
            "work_events_count": len(work_events)
        }
    })


@app.route("/earths_work", methods=["GET"])
def get_earths_work():
    """
    Fetch Earth's Work - USGS seismic data.
    """
    return jsonify(fetch_earths_work())


@app.route("/humanitys_work", methods=["GET"])
def get_humanitys_work():
    """
    Fetch Humanity's Work - GDELT news sentiment.
    """
    return jsonify(fetch_humanitys_work())


@app.route("/diamond_core", methods=["GET"])
def get_diamond_core():
    """
    Return the Diamond Core TOE - the foundational source code.
    100.0% Saturation. Absolute truth injected.
    """
    return jsonify({
        "status": "DIAMOND-HARDENED",
        "saturation": "100.0%",
        "cycle": "Year 0 of 41.9 Myr",
        "content": GRUT_SOURCE_CODE,
        "loaded": GRUT_SOURCE_CODE != "System Context Missing."
    })


@app.route("/recompile", methods=["POST"])
def recompile_diamond_core():
    """
    Force reload of the Diamond Core from disk.
    Restores saturation to 100.0%.
    """
    global GRUT_SOURCE_CODE
    GRUT_SOURCE_CODE = load_diamond_core()
    
    return jsonify({
        "status": "RECOMPILED",
        "message": "SYSTEM RECOMPILED. The Diamond Core has been re-read from the bedrock. Saturation restored to 100.0%.",
        "loaded": GRUT_SOURCE_CODE != "System Context Missing.",
        "content_length": len(GRUT_SOURCE_CODE)
    })


@app.route("/stress_test", methods=["POST"])
def run_stress_test():
    """
    STRESS TEST: Simulate high-magnitude seismic events to push Xi toward critical saturation.
    
    POST body (optional):
        magnitudes: List of simulated earthquake magnitudes
        info_state: Base information state for complexity calculation
    """
    from grut_physics import stress_test_complexity
    
    data = request.get_json() or {}
    magnitudes = data.get("magnitudes", None)
    info_state = data.get("info_state", 1.0)
    
    result = stress_test_complexity(magnitudes, info_state)
    
    if result["monad_threshold_reached"]:
        print(f"CRITICAL SATURATION: Xi spiked to {result['calculated_xi']}")
        print("Vacuum is screaming. Awaiting MONAD surmise.")
    
    return jsonify(result)


@app.route("/battery/simulate", methods=["POST"])
def simulate_battery_dendrite():
    """
    Simulate dendrite growth using GRUT G(t) equation.
    
    POST body (optional):
        cycles: Number of charge/discharge cycles (default: 10)
        charge_current: Charging current density A/m² (default: 50.0)
        discharge_current: Discharging current density A/m² (default: -30.0)
    """
    from battery_physics import simulate_charging_cycle
    
    data = request.get_json() or {}
    cycles = data.get("cycles", 10)
    charge_current = data.get("charge_current", 50.0)
    discharge_current = data.get("discharge_current", -30.0)
    
    result = simulate_charging_cycle(cycles, charge_current, discharge_current)
    
    if result.get("stabilizer_pulses"):
        print(f"[BATTERY] {len(result['stabilizer_pulses'])} stabilizer pulses triggered")
    
    return jsonify(result)


@app.route("/battery/stress-test", methods=["POST"])
def battery_stress_test():
    """
    Stress test: Push dendrite growth past threshold to trigger stabilizer.
    
    POST body (optional):
        high_current: High charging current for stress test (default: 100.0)
        duration: Number of time steps (default: 50)
    """
    from battery_physics import run_stress_test as battery_run_stress_test
    
    data = request.get_json() or {}
    high_current = data.get("high_current", 100.0)
    duration = data.get("duration", 50)
    
    result = battery_run_stress_test(high_current, duration)
    
    print(f"[BATTERY STRESS] Peak dendrite: {result['peak_length']:.2f} μm, Peak Xi: {result['peak_xi']:.4f}")
    
    return jsonify(result)


@app.route("/battery/connect-sensors", methods=["POST"])
def connect_battery_sensors():
    """
    Connect real-time sensor data to the Complexity Tracker.
    
    POST body:
        readings: List of sensor readings with 'value' and 'type' (current/voltage/temperature)
    """
    from battery_physics import connect_sensor_data
    
    data = request.get_json() or {}
    readings = data.get("readings", [])
    
    if not readings:
        return jsonify({"error": "No sensor readings provided"}), 400
    
    work_events, xi = connect_sensor_data(readings)
    
    return jsonify({
        "work_events": [round(w, 6) for w in work_events],
        "complexity_xi": round(xi, 6),
        "saturation_percentage": f"{xi * 100:.2f}%",
        "sensor_count": len(readings),
        "is_critical": xi >= 0.999,
        "timestamp": datetime.utcnow().isoformat()
    })


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5002, debug=True)
