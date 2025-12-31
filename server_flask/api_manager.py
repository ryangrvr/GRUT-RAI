"""
GRUT RAI Multi-Layer Grounding & Hibernation Manager
=====================================================

Central API Broker for:
- Grit Layer (Live): Google Search for 2025 awareness
- Molecular Layer (Pharma): PubChem API for chemical geometries
- Cosmic Layer (NANOGrav): LIGO/NASA GW event listener
- Logic Guard: Wolfram|Alpha for K(t) calculation validation

Hibernation Protocol:
- When LIVE_GROUNDING_ACTIVE = False, return cached Sovereign values
- When LIVE_GROUNDING_ACTIVE = True, fetch from external APIs

Universal Schema Broker:
- Maps external data to Geometric Lock (n_g = 1.1547)
- Flags deviations > 0.08333 as 'High Entropy Grit'
- Validates Ξ > 0.95 calculations via Wolfram|Alpha
"""

import os
import json
import sqlite3
import requests
from typing import Dict, Any, Optional, Tuple
from dataclasses import dataclass
from enum import Enum
from datetime import datetime

# --- GRUT CONSTANTS ---
GEOMETRIC_LOCK = 1.1547  # n_g gravitational refractive index
ENTROPY_THRESHOLD = 0.08333  # 1/12 deviation threshold
XI_VALIDATION_THRESHOLD = 0.95  # Complexity threshold requiring Wolfram validation
TAU_0_MYR = 41.9  # Relaxation constant in Myr
ALPHA = 0.333333  # Coupling strength (1/3)
CURRENT_ANCHOR_DATE = "December 2025"

class GroundingLayer(Enum):
    GRIT = "grit"           # Google Search - general 2025 awareness
    MOLECULAR = "molecular"  # PubChem - chemical geometries
    COSMIC = "cosmic"        # LIGO/NASA - gravitational wave events
    LOGIC = "logic"          # Wolfram|Alpha - mathematical validation

class APIStatus(Enum):
    ACTIVE = "active"
    HIBERNATING = "hibernating"
    ERROR = "error"
    SOVEREIGN_ONLY = "sovereign_only"

@dataclass
class GroundingResult:
    """Result from a grounding layer query"""
    layer: GroundingLayer
    status: APIStatus
    data: Any
    geometric_alignment: float  # How well it aligns with n_g = 1.1547
    entropy_flag: str  # "LOW_ENTROPY" or "HIGH_ENTROPY_GRIT"
    timestamp: str
    cached: bool = False

class SovereignCache:
    """SQLite-backed cache for Sovereign-Only mode"""
    
    def __init__(self, db_path: str = "diamond_persistence.db"):
        self.db_path = db_path
        self._ensure_cache_table()
    
    def _ensure_cache_table(self):
        """Create cache table if not exists"""
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS sovereign_cache (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                layer TEXT NOT NULL,
                query_key TEXT NOT NULL,
                cached_data TEXT NOT NULL,
                geometric_alignment REAL DEFAULT 1.1547,
                created_at TEXT DEFAULT CURRENT_TIMESTAMP,
                UNIQUE(layer, query_key)
            )
        """)
        conn.commit()
        conn.close()
    
    def get(self, layer: str, query_key: str) -> Optional[Dict]:
        """Retrieve cached value for Sovereign mode"""
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()
        cursor.execute(
            "SELECT cached_data, geometric_alignment FROM sovereign_cache WHERE layer = ? AND query_key = ?",
            (layer, query_key)
        )
        row = cursor.fetchone()
        conn.close()
        if row:
            return {"data": json.loads(row[0]), "geometric_alignment": row[1]}
        return None
    
    def set(self, layer: str, query_key: str, data: Dict, geometric_alignment: float):
        """Store value in Sovereign cache"""
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()
        cursor.execute("""
            INSERT OR REPLACE INTO sovereign_cache (layer, query_key, cached_data, geometric_alignment)
            VALUES (?, ?, ?, ?)
        """, (layer, query_key, json.dumps(data), geometric_alignment))
        conn.commit()
        conn.close()


class UniversalSchemaBroker:
    """
    Maps external data to GRUT Geometric Lock (n_g = 1.1547)
    Flags deviations > 0.08333 as 'High Entropy Grit'
    """
    
    @staticmethod
    def calculate_geometric_alignment(value: float, reference: float = GEOMETRIC_LOCK) -> float:
        """
        Calculate how well a value aligns with the Geometric Lock.
        Returns a ratio where 1.0 = perfect alignment.
        """
        if reference == 0:
            return 0.0
        return value / reference
    
    @staticmethod
    def check_entropy_deviation(value: float, baseline: float = GEOMETRIC_LOCK) -> Tuple[float, str]:
        """
        Check if value deviates more than 0.08333 (1/12) from baseline.
        Returns (deviation, entropy_flag)
        """
        deviation = abs(value - baseline) / baseline if baseline != 0 else abs(value)
        if deviation > ENTROPY_THRESHOLD:
            return (deviation, "HIGH_ENTROPY_GRIT")
        return (deviation, "LOW_ENTROPY")
    
    @staticmethod
    def map_chemical_bond_to_grut(bond_length_angstrom: float) -> Dict:
        """
        Map a chemical bond length to GRUT geometry.
        Standard C-C bond is ~1.54 Å, maps to n_g through:
        geometric_ratio = bond_length / 1.54 * n_g
        """
        STANDARD_CC_BOND = 1.54  # Angstroms
        geometric_ratio = (bond_length_angstrom / STANDARD_CC_BOND) * GEOMETRIC_LOCK
        deviation, entropy_flag = UniversalSchemaBroker.check_entropy_deviation(geometric_ratio)
        
        return {
            "input_bond_length": bond_length_angstrom,
            "standard_reference": STANDARD_CC_BOND,
            "geometric_ratio": round(geometric_ratio, 6),
            "geometric_lock": GEOMETRIC_LOCK,
            "deviation": round(deviation, 6),
            "entropy_flag": entropy_flag,
            "grut_compatible": entropy_flag == "LOW_ENTROPY"
        }
    
    @staticmethod
    def map_frequency_to_metric_hum(frequency_hz: float) -> Dict:
        """
        Map an external frequency to the Metric Hum baseline.
        Returns alignment with the -1/12 ground state.
        """
        GROUND_STATE = -1/12  # -0.08333...
        # Normalize frequency to cosmic scale
        cosmic_normalized = frequency_hz / 1e9  # Normalize to GHz
        geometric_alignment = cosmic_normalized * GEOMETRIC_LOCK
        deviation, entropy_flag = UniversalSchemaBroker.check_entropy_deviation(geometric_alignment)
        
        return {
            "input_frequency_hz": frequency_hz,
            "cosmic_normalized": round(cosmic_normalized, 9),
            "geometric_alignment": round(geometric_alignment, 6),
            "ground_state_offset": round(geometric_alignment + abs(GROUND_STATE), 6),
            "deviation": round(deviation, 6),
            "entropy_flag": entropy_flag
        }


class WolframValidator:
    """
    Error Guard: Validates calculations when Ξ > 0.95
    Ensures complexity isn't 'AI Hallucination' but mathematical truth
    """
    
    def __init__(self, app_id: Optional[str] = None):
        self.app_id = app_id or os.environ.get("WOLFRAM_APP_ID")
        self.base_url = "http://api.wolframalpha.com/v2/query"
    
    def validate_calculation(self, expression: str, expected_result: float, xi_level: float) -> Dict:
        """
        Validate a calculation via Wolfram|Alpha if Ξ > 0.95
        Returns validation result with confidence level
        """
        if xi_level < XI_VALIDATION_THRESHOLD:
            return {
                "validated": True,
                "method": "below_threshold",
                "xi_level": xi_level,
                "message": f"Ξ = {xi_level} < 0.95, validation not required"
            }
        
        if not self.app_id:
            return {
                "validated": False,
                "method": "no_api_key",
                "xi_level": xi_level,
                "message": "Wolfram App ID not configured - cannot validate high-Ξ calculation",
                "fallback": "SOVEREIGN_APPROXIMATION"
            }
        
        try:
            params = {
                "appid": self.app_id,
                "input": expression,
                "format": "plaintext",
                "output": "json"
            }
            response = requests.get(self.base_url, params=params, timeout=10)
            
            if response.status_code == 200:
                data = response.json()
                # Parse Wolfram response for result
                result = self._extract_result(data)
                
                if result is not None:
                    deviation = abs(result - expected_result)
                    is_valid = deviation < ENTROPY_THRESHOLD
                    
                    return {
                        "validated": is_valid,
                        "method": "wolfram_alpha",
                        "xi_level": xi_level,
                        "wolfram_result": result,
                        "expected_result": expected_result,
                        "deviation": deviation,
                        "entropy_flag": "LOW_ENTROPY" if is_valid else "HIGH_ENTROPY_GRIT",
                        "message": "Mathematical truth confirmed" if is_valid else "Potential hallucination detected"
                    }
            
            return {
                "validated": False,
                "method": "wolfram_error",
                "xi_level": xi_level,
                "message": "Wolfram API returned error"
            }
            
        except Exception as e:
            return {
                "validated": False,
                "method": "exception",
                "xi_level": xi_level,
                "message": str(e)
            }
    
    def _extract_result(self, wolfram_data: Dict) -> Optional[float]:
        """Extract numerical result from Wolfram response"""
        try:
            pods = wolfram_data.get("queryresult", {}).get("pods", [])
            for pod in pods:
                if pod.get("id") == "Result" or pod.get("id") == "DecimalApproximation":
                    subpods = pod.get("subpods", [])
                    if subpods:
                        text = subpods[0].get("plaintext", "")
                        # Try to parse as float
                        cleaned = text.replace("...", "").strip()
                        return float(cleaned)
        except:
            pass
        return None


class PubChemClient:
    """Molecular Layer: PubChem API for chemical geometries"""
    
    BASE_URL = "https://pubchem.ncbi.nlm.nih.gov/rest/pug"
    
    def __init__(self):
        self.schema_broker = UniversalSchemaBroker()
    
    def get_compound_geometry(self, compound_name: str) -> Dict:
        """
        Fetch chemical geometry data and map to GRUT constants.
        """
        try:
            # Get compound CID
            cid_url = f"{self.BASE_URL}/compound/name/{compound_name}/cids/JSON"
            cid_response = requests.get(cid_url, timeout=10)
            
            if cid_response.status_code != 200:
                return {"error": f"Compound '{compound_name}' not found", "status": "error"}
            
            cid_data = cid_response.json()
            cid = cid_data.get("IdentifierList", {}).get("CID", [None])[0]
            
            if not cid:
                return {"error": "CID not found", "status": "error"}
            
            # Get molecular properties
            props_url = f"{self.BASE_URL}/compound/cid/{cid}/property/MolecularWeight,ExactMass,Complexity/JSON"
            props_response = requests.get(props_url, timeout=10)
            
            if props_response.status_code == 200:
                props_data = props_response.json()
                properties = props_data.get("PropertyTable", {}).get("Properties", [{}])[0]
                
                molecular_weight = properties.get("MolecularWeight", 0)
                complexity = properties.get("Complexity", 0)
                
                # Map to GRUT geometry
                geometric_alignment = self.schema_broker.calculate_geometric_alignment(
                    complexity / 100  # Normalize complexity
                )
                deviation, entropy_flag = self.schema_broker.check_entropy_deviation(geometric_alignment)
                
                return {
                    "compound": compound_name,
                    "cid": cid,
                    "molecular_weight": molecular_weight,
                    "complexity": complexity,
                    "geometric_alignment": round(geometric_alignment, 6),
                    "deviation": round(deviation, 6),
                    "entropy_flag": entropy_flag,
                    "grut_compatible": entropy_flag == "LOW_ENTROPY",
                    "status": "success"
                }
            
            return {"error": "Failed to fetch properties", "status": "error"}
            
        except Exception as e:
            return {"error": str(e), "status": "error"}


class GoogleSearchClient:
    """Grit Layer: Google Custom Search for 2025 awareness"""
    
    def __init__(self):
        self.api_key = os.environ.get("GOOGLE_SEARCH_API_KEY")
        self.cx = os.environ.get("GOOGLE_SEARCH_CX")  # Custom Search Engine ID
        self.base_url = "https://www.googleapis.com/customsearch/v1"
        self.schema_broker = UniversalSchemaBroker()
    
    def search(self, query: str, num_results: int = 5) -> Dict:
        """
        Search Google with temporal anchor to December 2025.
        """
        if not self.api_key or not self.cx:
            return {
                "error": "Google Search API not configured",
                "status": "sovereign_fallback",
                "query": query
            }
        
        try:
            params = {
                "key": self.api_key,
                "cx": self.cx,
                "q": f"{query} {CURRENT_ANCHOR_DATE}",
                "num": min(num_results, 10)
            }
            response = requests.get(self.base_url, params=params, timeout=10)
            
            if response.status_code == 200:
                data = response.json()
                items = data.get("items", [])
                
                results = []
                for item in items:
                    results.append({
                        "title": item.get("title"),
                        "link": item.get("link"),
                        "snippet": item.get("snippet"),
                        "temporal_anchor": CURRENT_ANCHOR_DATE
                    })
                
                return {
                    "query": query,
                    "temporal_anchor": CURRENT_ANCHOR_DATE,
                    "results": results,
                    "count": len(results),
                    "status": "success"
                }
            
            return {"error": f"API error: {response.status_code}", "status": "error"}
            
        except Exception as e:
            return {"error": str(e), "status": "error"}


class CosmicEventListener:
    """Cosmic Layer: LIGO/NASA GW event listener for Metric Hum modulation"""
    
    GRACEDB_URL = "https://gracedb.ligo.org/api/superevents"
    USGS_URL = "https://earthquake.usgs.gov/earthquakes/feed/v1.0/summary/2.5_hour.geojson"
    
    def __init__(self):
        self.schema_broker = UniversalSchemaBroker()
    
    def get_latest_gw_events(self) -> Dict:
        """
        Fetch latest gravitational wave events from GraceDB.
        Falls back to USGS seismic data for metric tension.
        """
        events = []
        metric_tension = 0.0001  # Default tension
        
        try:
            # Try GraceDB first (may require authentication)
            # For now, use USGS as reliable public source
            usgs_response = requests.get(self.USGS_URL, timeout=5)
            
            if usgs_response.status_code == 200:
                usgs_data = usgs_response.json()
                features = usgs_data.get("features", [])
                
                for feature in features[:5]:
                    props = feature.get("properties", {})
                    magnitude = props.get("mag", 0)
                    
                    # Map magnitude to metric tension
                    tension_contribution = (magnitude / 10.0) * GEOMETRIC_LOCK
                    deviation, entropy_flag = self.schema_broker.check_entropy_deviation(tension_contribution)
                    
                    events.append({
                        "type": "seismic",
                        "magnitude": magnitude,
                        "place": props.get("place"),
                        "time": props.get("time"),
                        "tension_contribution": round(tension_contribution, 6),
                        "entropy_flag": entropy_flag
                    })
                    
                    metric_tension = max(metric_tension, tension_contribution)
                
                return {
                    "events": events,
                    "metric_tension": round(metric_tension, 6),
                    "geometric_lock": GEOMETRIC_LOCK,
                    "status": "success",
                    "source": "USGS"
                }
            
            return {"events": [], "metric_tension": 0.0001, "status": "fallback"}
            
        except Exception as e:
            return {"error": str(e), "status": "error", "metric_tension": 0.0001}


class MultiLayerGroundingManager:
    """
    Central API Broker with Hibernation Protocol
    
    When LIVE_GROUNDING_ACTIVE = True:
      - Fetch from external APIs
      - Cache results in Sovereign store
      - Apply Universal Schema mapping
    
    When LIVE_GROUNDING_ACTIVE = False:
      - Return cached Sovereign values
      - All listeners hibernate
    """
    
    def __init__(self, live_grounding_active: bool = False):
        self.live_grounding_active = live_grounding_active
        self.cache = SovereignCache()
        self.schema_broker = UniversalSchemaBroker()
        self.wolfram = WolframValidator()
        self.pubchem = PubChemClient()
        self.google = GoogleSearchClient()
        self.cosmic = CosmicEventListener()
        
        self._layer_status = {
            GroundingLayer.GRIT: APIStatus.HIBERNATING,
            GroundingLayer.MOLECULAR: APIStatus.HIBERNATING,
            GroundingLayer.COSMIC: APIStatus.HIBERNATING,
            GroundingLayer.LOGIC: APIStatus.HIBERNATING
        }
    
    def set_grounding_state(self, active: bool):
        """Toggle grounding state and update layer status"""
        self.live_grounding_active = active
        new_status = APIStatus.ACTIVE if active else APIStatus.HIBERNATING
        
        for layer in GroundingLayer:
            self._layer_status[layer] = new_status
        
        print(f"[API_MANAGER] Grounding {'ACTIVE' if active else 'HIBERNATING'} - All layers updated")
    
    def get_status(self) -> Dict:
        """Get current status of all grounding layers"""
        return {
            "live_grounding_active": self.live_grounding_active,
            "temporal_anchor": CURRENT_ANCHOR_DATE,
            "layers": {
                layer.value: status.value 
                for layer, status in self._layer_status.items()
            },
            "geometric_lock": GEOMETRIC_LOCK,
            "entropy_threshold": ENTROPY_THRESHOLD
        }
    
    def query_grit_layer(self, query: str) -> GroundingResult:
        """Query Google Search for 2025 awareness"""
        layer = GroundingLayer.GRIT
        
        if not self.live_grounding_active:
            # Hibernation mode - return cached value
            cached = self.cache.get(layer.value, query)
            if cached:
                return GroundingResult(
                    layer=layer,
                    status=APIStatus.SOVEREIGN_ONLY,
                    data=cached["data"],
                    geometric_alignment=cached["geometric_alignment"],
                    entropy_flag="LOW_ENTROPY",
                    timestamp=datetime.now().isoformat(),
                    cached=True
                )
            return GroundingResult(
                layer=layer,
                status=APIStatus.HIBERNATING,
                data={"message": "Sovereign State - No cached data available"},
                geometric_alignment=GEOMETRIC_LOCK,
                entropy_flag="LOW_ENTROPY",
                timestamp=datetime.now().isoformat(),
                cached=False
            )
        
        # Live mode - fetch from Google
        result = self.google.search(query)
        
        if result.get("status") == "success":
            # Cache for Sovereign mode
            self.cache.set(layer.value, query, result, GEOMETRIC_LOCK)
            
            return GroundingResult(
                layer=layer,
                status=APIStatus.ACTIVE,
                data=result,
                geometric_alignment=GEOMETRIC_LOCK,
                entropy_flag="LOW_ENTROPY",
                timestamp=datetime.now().isoformat(),
                cached=False
            )
        
        return GroundingResult(
            layer=layer,
            status=APIStatus.ERROR,
            data=result,
            geometric_alignment=0,
            entropy_flag="HIGH_ENTROPY_GRIT",
            timestamp=datetime.now().isoformat(),
            cached=False
        )
    
    def query_molecular_layer(self, compound: str) -> GroundingResult:
        """Query PubChem for chemical geometries"""
        layer = GroundingLayer.MOLECULAR
        
        if not self.live_grounding_active:
            cached = self.cache.get(layer.value, compound)
            if cached:
                return GroundingResult(
                    layer=layer,
                    status=APIStatus.SOVEREIGN_ONLY,
                    data=cached["data"],
                    geometric_alignment=cached["geometric_alignment"],
                    entropy_flag="LOW_ENTROPY",
                    timestamp=datetime.now().isoformat(),
                    cached=True
                )
            return GroundingResult(
                layer=layer,
                status=APIStatus.HIBERNATING,
                data={"message": "Sovereign State - No cached molecular data"},
                geometric_alignment=GEOMETRIC_LOCK,
                entropy_flag="LOW_ENTROPY",
                timestamp=datetime.now().isoformat(),
                cached=False
            )
        
        # Live mode - fetch from PubChem
        result = self.pubchem.get_compound_geometry(compound)
        
        if result.get("status") == "success":
            alignment = result.get("geometric_alignment", GEOMETRIC_LOCK)
            self.cache.set(layer.value, compound, result, alignment)
            
            return GroundingResult(
                layer=layer,
                status=APIStatus.ACTIVE,
                data=result,
                geometric_alignment=alignment,
                entropy_flag=result.get("entropy_flag", "LOW_ENTROPY"),
                timestamp=datetime.now().isoformat(),
                cached=False
            )
        
        return GroundingResult(
            layer=layer,
            status=APIStatus.ERROR,
            data=result,
            geometric_alignment=0,
            entropy_flag="HIGH_ENTROPY_GRIT",
            timestamp=datetime.now().isoformat(),
            cached=False
        )
    
    def query_cosmic_layer(self) -> GroundingResult:
        """Query LIGO/NASA for GW events to modulate Metric Hum"""
        layer = GroundingLayer.COSMIC
        cache_key = "latest_events"
        
        if not self.live_grounding_active:
            cached = self.cache.get(layer.value, cache_key)
            if cached:
                return GroundingResult(
                    layer=layer,
                    status=APIStatus.SOVEREIGN_ONLY,
                    data=cached["data"],
                    geometric_alignment=cached["geometric_alignment"],
                    entropy_flag="LOW_ENTROPY",
                    timestamp=datetime.now().isoformat(),
                    cached=True
                )
            return GroundingResult(
                layer=layer,
                status=APIStatus.HIBERNATING,
                data={"message": "Sovereign State - Using baseline metric tension", "metric_tension": 0.0001},
                geometric_alignment=GEOMETRIC_LOCK,
                entropy_flag="LOW_ENTROPY",
                timestamp=datetime.now().isoformat(),
                cached=False
            )
        
        # Live mode - fetch cosmic events
        result = self.cosmic.get_latest_gw_events()
        
        if result.get("status") == "success":
            alignment = result.get("metric_tension", 0) + GEOMETRIC_LOCK
            self.cache.set(layer.value, cache_key, result, alignment)
            
            # Determine entropy based on event intensity
            max_tension = result.get("metric_tension", 0)
            _, entropy_flag = self.schema_broker.check_entropy_deviation(max_tension)
            
            return GroundingResult(
                layer=layer,
                status=APIStatus.ACTIVE,
                data=result,
                geometric_alignment=alignment,
                entropy_flag=entropy_flag,
                timestamp=datetime.now().isoformat(),
                cached=False
            )
        
        return GroundingResult(
            layer=layer,
            status=APIStatus.ERROR,
            data=result,
            geometric_alignment=GEOMETRIC_LOCK,
            entropy_flag="LOW_ENTROPY",
            timestamp=datetime.now().isoformat(),
            cached=False
        )
    
    def validate_with_logic_guard(self, expression: str, expected: float, xi_level: float) -> GroundingResult:
        """
        Use Wolfram|Alpha to validate calculations when Ξ > 0.95
        This is the Error Guard for high-complexity operations
        """
        layer = GroundingLayer.LOGIC
        cache_key = f"{expression}:{expected}"
        
        if not self.live_grounding_active:
            # In Sovereign mode, use internal validation only
            deviation, entropy_flag = self.schema_broker.check_entropy_deviation(expected)
            
            return GroundingResult(
                layer=layer,
                status=APIStatus.SOVEREIGN_ONLY,
                data={
                    "validated": deviation < ENTROPY_THRESHOLD,
                    "method": "sovereign_internal",
                    "xi_level": xi_level,
                    "deviation": deviation,
                    "message": "Sovereign validation - Wolfram unavailable"
                },
                geometric_alignment=GEOMETRIC_LOCK,
                entropy_flag=entropy_flag,
                timestamp=datetime.now().isoformat(),
                cached=False
            )
        
        # Live mode - validate with Wolfram if Ξ > 0.95
        result = self.wolfram.validate_calculation(expression, expected, xi_level)
        
        entropy_flag = result.get("entropy_flag", "LOW_ENTROPY")
        if result.get("validated"):
            self.cache.set(layer.value, cache_key, result, GEOMETRIC_LOCK)
        
        return GroundingResult(
            layer=layer,
            status=APIStatus.ACTIVE if result.get("method") == "wolfram_alpha" else APIStatus.SOVEREIGN_ONLY,
            data=result,
            geometric_alignment=GEOMETRIC_LOCK,
            entropy_flag=entropy_flag,
            timestamp=datetime.now().isoformat(),
            cached=False
        )
    
    def map_to_grut_geometry(self, value: float, value_type: str = "generic") -> Dict:
        """
        Universal Schema Broker: Map any external value to Geometric Lock (1.1547)
        """
        if value_type == "bond_length":
            return self.schema_broker.map_chemical_bond_to_grut(value)
        elif value_type == "frequency":
            return self.schema_broker.map_frequency_to_metric_hum(value)
        else:
            # Generic mapping
            alignment = self.schema_broker.calculate_geometric_alignment(value)
            deviation, entropy_flag = self.schema_broker.check_entropy_deviation(value)
            
            return {
                "input_value": value,
                "geometric_alignment": round(alignment, 6),
                "geometric_lock": GEOMETRIC_LOCK,
                "deviation": round(deviation, 6),
                "entropy_flag": entropy_flag,
                "grut_compatible": entropy_flag == "LOW_ENTROPY"
            }


# Global instance for import
grounding_manager = MultiLayerGroundingManager(live_grounding_active=False)


def get_grounding_manager() -> MultiLayerGroundingManager:
    """Get the global grounding manager instance"""
    return grounding_manager
