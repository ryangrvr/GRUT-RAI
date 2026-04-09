"""Sakharov conditions checklist."""

SAKHAROV_CONDITIONS = {
    "baryon_number_violation": {
        "required": True,
        "grut_status": "OPEN — no B-violating mechanism identified in constitutive sector",
    },
    "c_and_cp_violation": {
        "required": True,
        "grut_status": "OPEN — CKM CP violation exists in host; no constitutive CP source",
    },
    "departure_from_equilibrium": {
        "required": True,
        "grut_status": "STRUCTURAL — CTP/nonequilibrium dynamics is built into A0",
    },
}

def sakharov_checklist() -> dict:
    """Return Sakharov conditions with GRUT status for each."""
    all_met = all(v["grut_status"].startswith("STRUCTURAL") or "exists" in v["grut_status"]
                  for v in SAKHAROV_CONDITIONS.values())
    return {"conditions": SAKHAROV_CONDITIONS, "all_met": all_met,
            "note": "Only condition 3 has structural GRUT support (CTP). Conditions 1 and 2 are OPEN."}
