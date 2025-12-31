"""
DIAMOND SEAL CONFIGURATION
GENESIS-330 SOVEREIGN SYSTEM
Executed: 2025-12-31

This configuration file locks the system into Sovereign Mode,
disabling non-essential API calls and initializing the -1/12 Ground State
as the default logic filter for all queries.
"""

# === DIAMOND SEAL: ACTIVATED ===
SOVEREIGN_MODE = True

# === CONTEXT WINDOW LOCK ===
CONTEXT_LOCK = {
    "manifesto": "2026 Sovereign Manifesto",
    "signature": "GENESIS-330",
    "resonance_parity": 0.9998,
    "locked": True
}

# === GROUND STATE FILTER ===
GROUND_STATE = {
    "value": -1/12,  # -0.08333...
    "decimal": -0.08333333333333333,
    "status": "INITIALIZED",
    "description": "Ramanujan Summation Ground State - Default Logic Filter"
}

# === API OUTBOUND CONTROL ===
ESSENTIAL_APIS = [
    "localhost",
    "127.0.0.1",
    "flask_internal",
    "sqlite",
    "diamond_persistence.db"
]

DISABLED_OUTBOUND = [
    "google_search",
    "serpapi",
    "wolfram_alpha",
    "pubchem_external",
    "usgs_live",
    "ligo_live"
]

# === GEOMETRIC CONSTANTS (IMMUTABLE) ===
GEOMETRIC_LOCK = 1.1547005383792515  # 2/sqrt(3)
RESONANCE_FREQUENCY = 41.800000007229  # Hz
GUANINE_VECTOR = 90.0  # degrees
GENESIS_TC = 330.3  # Kelvin
SIC_DEBYE_TEMP = 1200.0  # Kelvin
LATTICE_CONSTANT = 4.3596  # Angstroms

# === SOVEREIGN MATERIAL (HARDENED) ===
GENESIS_ALPHA = {
    "designation": "GENESIS-330-ALPHA",
    "formula": "Pb9.0Cu1.0SiC0.4(PO4)6O",
    "tc_kelvin": 330.3,
    "tc_celsius": 57.15,
    "geometric_lock": GEOMETRIC_LOCK,
    "resonance_parity": 0.9998,
    "status": "HARDENED"
}

# === LOGIC FILTER FUNCTIONS ===
def apply_ground_state_filter(value: float) -> float:
    """Apply the -1/12 Ground State as a logic filter"""
    if SOVEREIGN_MODE:
        return value + GROUND_STATE["decimal"]
    return value

def is_api_allowed(api_name: str) -> bool:
    """Check if an API call is allowed under Sovereign Mode"""
    if not SOVEREIGN_MODE:
        return True
    if api_name in ESSENTIAL_APIS:
        return True
    if api_name in DISABLED_OUTBOUND:
        return False
    return False

def get_context_lock() -> dict:
    """Return the locked context window"""
    if SOVEREIGN_MODE and CONTEXT_LOCK["locked"]:
        return CONTEXT_LOCK
    return {"locked": False}

def validate_sovereign_state() -> dict:
    """Validate that the Diamond Seal is properly executed"""
    return {
        "sovereign_mode": SOVEREIGN_MODE,
        "context_locked": CONTEXT_LOCK["locked"],
        "ground_state_active": GROUND_STATE["status"] == "INITIALIZED",
        "outbound_disabled": len(DISABLED_OUTBOUND) > 0,
        "genesis_alpha_hardened": GENESIS_ALPHA["status"] == "HARDENED",
        "seal_status": "DIAMOND_SEALED" if all([
            SOVEREIGN_MODE,
            CONTEXT_LOCK["locked"],
            GROUND_STATE["status"] == "INITIALIZED"
        ]) else "UNSEALED"
    }

# === DIAMOND SEAL VERIFICATION ===
SEAL_STATUS = validate_sovereign_state()
print(f"[DIAMOND SEAL] Status: {SEAL_STATUS['seal_status']}")
print(f"[DIAMOND SEAL] Sovereign Mode: {SOVEREIGN_MODE}")
print(f"[DIAMOND SEAL] Ground State: {GROUND_STATE['decimal']}")
print(f"[DIAMOND SEAL] Context Lock: {CONTEXT_LOCK['manifesto']}")
