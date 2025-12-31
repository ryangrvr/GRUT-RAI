/**
 * GRUT RAI Multi-Layer Grounding & Hibernation Manager (TypeScript)
 * ====================================================================
 * 
 * Central API Broker for:
 * - Grit Layer (Live): Google Search for 2025 awareness
 * - Molecular Layer (Pharma): PubChem API for chemical geometries
 * - Cosmic Layer (NANOGrav): LIGO/NASA GW event listener
 * - Logic Guard: Wolfram|Alpha for K(t) calculation validation
 * 
 * Hibernation Protocol:
 * - When LIVE_GROUNDING_ACTIVE = False, return cached Sovereign values
 * - When LIVE_GROUNDING_ACTIVE = True, fetch from external APIs
 * 
 * Universal Schema Broker:
 * - Maps external data to Geometric Lock (n_g = 1.1547)
 * - Flags deviations > 0.08333 as 'High Entropy Grit'
 * - Validates Ξ > 0.95 calculations via Wolfram|Alpha
 */

import { GRUT_CONSTANTS } from "./grut-logic";

// --- GRUT CONSTANTS ---
export const GEOMETRIC_LOCK = 1.1547;  // n_g gravitational refractive index
export const ENTROPY_THRESHOLD = 0.08333;  // 1/12 deviation threshold
export const XI_VALIDATION_THRESHOLD = 0.95;  // Complexity threshold requiring Wolfram validation
export const CURRENT_ANCHOR_DATE = "December 2025";

export enum GroundingLayer {
  GRIT = "grit",           // Google Search - general 2025 awareness
  MOLECULAR = "molecular",  // PubChem - chemical geometries
  COSMIC = "cosmic",        // LIGO/NASA - gravitational wave events
  LOGIC = "logic"           // Wolfram|Alpha - mathematical validation
}

export enum APIStatus {
  ACTIVE = "active",
  HIBERNATING = "hibernating",
  ERROR = "error",
  SOVEREIGN_ONLY = "sovereign_only"
}

export interface GroundingResult {
  layer: GroundingLayer;
  status: APIStatus;
  data: any;
  geometricAlignment: number;
  entropyFlag: "LOW_ENTROPY" | "HIGH_ENTROPY_GRIT";
  timestamp: string;
  cached: boolean;
}

export interface SchemaMapping {
  inputValue: number;
  geometricAlignment: number;
  geometricLock: number;
  deviation: number;
  entropyFlag: "LOW_ENTROPY" | "HIGH_ENTROPY_GRIT";
  grutCompatible: boolean;
}

// --- Sovereign Cache (SQLite-backed for persistence) ---
import { sqliteDb } from "./db-sqlite";
import crypto from "crypto";

function getFromCache(layer: GroundingLayer, queryKey: string): { data: any; geometricAlignment: number } | null {
  try {
    const stmt = sqliteDb.prepare(
      "SELECT cached_data, geometric_alignment FROM sovereign_cache WHERE layer = ? AND query_key = ?"
    );
    const row = stmt.get(layer, queryKey) as { cached_data: string; geometric_alignment: number } | undefined;
    if (row) {
      return { data: JSON.parse(row.cached_data), geometricAlignment: row.geometric_alignment };
    }
  } catch (error) {
    console.error("[API_MANAGER] Cache read error:", error);
  }
  return null;
}

function setInCache(layer: GroundingLayer, queryKey: string, data: any, geometricAlignment: number): void {
  try {
    const id = crypto.randomUUID();
    const stmt = sqliteDb.prepare(`
      INSERT OR REPLACE INTO sovereign_cache (id, layer, query_key, cached_data, geometric_alignment)
      VALUES (?, ?, ?, ?, ?)
    `);
    stmt.run(id, layer, queryKey, JSON.stringify(data), geometricAlignment);
  } catch (error) {
    console.error("[API_MANAGER] Cache write error:", error);
  }
}

// --- Universal Schema Broker ---
export class UniversalSchemaBroker {
  static calculateGeometricAlignment(value: number, reference: number = GEOMETRIC_LOCK): number {
    if (reference === 0) return 0;
    return value / reference;
  }

  static checkEntropyDeviation(value: number, baseline: number = GEOMETRIC_LOCK): { deviation: number; entropyFlag: "LOW_ENTROPY" | "HIGH_ENTROPY_GRIT" } {
    const deviation = baseline !== 0 ? Math.abs(value - baseline) / baseline : Math.abs(value);
    if (deviation > ENTROPY_THRESHOLD) {
      return { deviation, entropyFlag: "HIGH_ENTROPY_GRIT" };
    }
    return { deviation, entropyFlag: "LOW_ENTROPY" };
  }

  static mapChemicalBondToGrut(bondLengthAngstrom: number): SchemaMapping {
    const STANDARD_CC_BOND = 1.54;  // Angstroms
    const geometricRatio = (bondLengthAngstrom / STANDARD_CC_BOND) * GEOMETRIC_LOCK;
    const { deviation, entropyFlag } = this.checkEntropyDeviation(geometricRatio);

    return {
      inputValue: bondLengthAngstrom,
      geometricAlignment: parseFloat(geometricRatio.toFixed(6)),
      geometricLock: GEOMETRIC_LOCK,
      deviation: parseFloat(deviation.toFixed(6)),
      entropyFlag,
      grutCompatible: entropyFlag === "LOW_ENTROPY"
    };
  }

  static mapFrequencyToMetricHum(frequencyHz: number): SchemaMapping & { cosmicNormalized: number; groundStateOffset: number } {
    const GROUND_STATE = -1/12;  // -0.08333...
    const cosmicNormalized = frequencyHz / 1e9;  // Normalize to GHz
    const geometricAlignment = cosmicNormalized * GEOMETRIC_LOCK;
    const { deviation, entropyFlag } = this.checkEntropyDeviation(geometricAlignment);

    return {
      inputValue: frequencyHz,
      cosmicNormalized: parseFloat(cosmicNormalized.toFixed(9)),
      geometricAlignment: parseFloat(geometricAlignment.toFixed(6)),
      geometricLock: GEOMETRIC_LOCK,
      groundStateOffset: parseFloat((geometricAlignment + Math.abs(GROUND_STATE)).toFixed(6)),
      deviation: parseFloat(deviation.toFixed(6)),
      entropyFlag,
      grutCompatible: entropyFlag === "LOW_ENTROPY"
    };
  }

  static mapGenericValue(value: number): SchemaMapping {
    const alignment = this.calculateGeometricAlignment(value);
    const { deviation, entropyFlag } = this.checkEntropyDeviation(value);

    return {
      inputValue: value,
      geometricAlignment: parseFloat(alignment.toFixed(6)),
      geometricLock: GEOMETRIC_LOCK,
      deviation: parseFloat(deviation.toFixed(6)),
      entropyFlag,
      grutCompatible: entropyFlag === "LOW_ENTROPY"
    };
  }
}

// --- PubChem Client ---
export class PubChemClient {
  private static BASE_URL = "https://pubchem.ncbi.nlm.nih.gov/rest/pug";

  static async getCompoundGeometry(compoundName: string): Promise<any> {
    try {
      // Get compound CID
      const cidResponse = await fetch(`${this.BASE_URL}/compound/name/${encodeURIComponent(compoundName)}/cids/JSON`, {
        signal: AbortSignal.timeout(10000)
      });

      if (!cidResponse.ok) {
        return { error: `Compound '${compoundName}' not found`, status: "error" };
      }

      const cidData = await cidResponse.json() as { IdentifierList?: { CID?: number[] } };
      const cid = cidData.IdentifierList?.CID?.[0];

      if (!cid) {
        return { error: "CID not found", status: "error" };
      }

      // Get molecular properties
      const propsResponse = await fetch(`${this.BASE_URL}/compound/cid/${cid}/property/MolecularWeight,ExactMass,Complexity/JSON`, {
        signal: AbortSignal.timeout(10000)
      });

      if (propsResponse.ok) {
        const propsData = await propsResponse.json() as { PropertyTable?: { Properties?: Array<{ MolecularWeight?: number; Complexity?: number }> } };
        const properties = propsData.PropertyTable?.Properties?.[0] || {};

        const molecularWeight = properties.MolecularWeight || 0;
        const complexity = properties.Complexity || 0;

        // Map to GRUT geometry
        const geometricAlignment = UniversalSchemaBroker.calculateGeometricAlignment(complexity / 100);
        const { deviation, entropyFlag } = UniversalSchemaBroker.checkEntropyDeviation(geometricAlignment);

        return {
          compound: compoundName,
          cid,
          molecularWeight,
          complexity,
          geometricAlignment: parseFloat(geometricAlignment.toFixed(6)),
          deviation: parseFloat(deviation.toFixed(6)),
          entropyFlag,
          grutCompatible: entropyFlag === "LOW_ENTROPY",
          status: "success"
        };
      }

      return { error: "Failed to fetch properties", status: "error" };

    } catch (error) {
      return { error: String(error), status: "error" };
    }
  }
}

// --- Wolfram Validator ---
export class WolframValidator {
  private static BASE_URL = "http://api.wolframalpha.com/v2/query";

  static async validateCalculation(expression: string, expectedResult: number, xiLevel: number): Promise<any> {
    if (xiLevel < XI_VALIDATION_THRESHOLD) {
      return {
        validated: true,
        method: "below_threshold",
        xiLevel,
        message: `Ξ = ${xiLevel} < 0.95, validation not required`
      };
    }

    const appId = process.env.WOLFRAM_APP_ID;
    if (!appId) {
      return {
        validated: false,
        method: "no_api_key",
        xiLevel,
        message: "Wolfram App ID not configured - cannot validate high-Ξ calculation",
        fallback: "SOVEREIGN_APPROXIMATION"
      };
    }

    try {
      const params = new URLSearchParams({
        appid: appId,
        input: expression,
        format: "plaintext",
        output: "json"
      });

      const response = await fetch(`${this.BASE_URL}?${params}`, {
        signal: AbortSignal.timeout(10000)
      });

      if (response.ok) {
        const data = await response.json() as any;
        const result = this.extractResult(data);

        if (result !== null) {
          const deviation = Math.abs(result - expectedResult);
          const isValid = deviation < ENTROPY_THRESHOLD;

          return {
            validated: isValid,
            method: "wolfram_alpha",
            xiLevel,
            wolframResult: result,
            expectedResult,
            deviation,
            entropyFlag: isValid ? "LOW_ENTROPY" : "HIGH_ENTROPY_GRIT",
            message: isValid ? "Mathematical truth confirmed" : "Potential hallucination detected"
          };
        }
      }

      return {
        validated: false,
        method: "wolfram_error",
        xiLevel,
        message: "Wolfram API returned error"
      };

    } catch (error) {
      return {
        validated: false,
        method: "exception",
        xiLevel,
        message: String(error)
      };
    }
  }

  private static extractResult(wolframData: any): number | null {
    try {
      const pods = wolframData?.queryresult?.pods || [];
      for (const pod of pods) {
        if (pod.id === "Result" || pod.id === "DecimalApproximation") {
          const subpods = pod.subpods || [];
          if (subpods.length > 0) {
            const text = subpods[0].plaintext || "";
            const cleaned = text.replace("...", "").trim();
            return parseFloat(cleaned);
          }
        }
      }
    } catch {
      // Ignore parsing errors
    }
    return null;
  }
}

// --- Cosmic Event Listener ---
export class CosmicEventListener {
  private static USGS_URL = "https://earthquake.usgs.gov/earthquakes/feed/v1.0/summary/2.5_hour.geojson";

  static async getLatestEvents(): Promise<any> {
    const events: any[] = [];
    let metricTension = 0.0001;

    try {
      const response = await fetch(this.USGS_URL, {
        signal: AbortSignal.timeout(5000)
      });

      if (response.ok) {
        const data = await response.json() as { features?: Array<{ properties?: { mag?: number; place?: string; time?: number } }> };
        const features = data.features || [];

        for (const feature of features.slice(0, 5)) {
          const props = feature.properties || {};
          const magnitude = props.mag || 0;

          const tensionContribution = (magnitude / 10.0) * GEOMETRIC_LOCK;
          const { entropyFlag } = UniversalSchemaBroker.checkEntropyDeviation(tensionContribution);

          events.push({
            type: "seismic",
            magnitude,
            place: props.place,
            time: props.time,
            tensionContribution: parseFloat(tensionContribution.toFixed(6)),
            entropyFlag
          });

          metricTension = Math.max(metricTension, tensionContribution);
        }

        return {
          events,
          metricTension: parseFloat(metricTension.toFixed(6)),
          geometricLock: GEOMETRIC_LOCK,
          status: "success",
          source: "USGS"
        };
      }

      return { events: [], metricTension: 0.0001, status: "fallback" };

    } catch (error) {
      return { error: String(error), status: "error", metricTension: 0.0001 };
    }
  }
}

// --- Multi-Layer Grounding Manager ---
export class MultiLayerGroundingManager {
  private liveGroundingActive: boolean = false;
  private layerStatus: Map<GroundingLayer, APIStatus> = new Map();

  constructor(liveGroundingActive: boolean = false) {
    this.liveGroundingActive = liveGroundingActive;
    for (const layer of Object.values(GroundingLayer)) {
      this.layerStatus.set(layer as GroundingLayer, APIStatus.HIBERNATING);
    }
  }

  setGroundingState(active: boolean): void {
    this.liveGroundingActive = active;
    const newStatus = active ? APIStatus.ACTIVE : APIStatus.HIBERNATING;

    for (const layer of Object.values(GroundingLayer)) {
      this.layerStatus.set(layer as GroundingLayer, newStatus);
    }

    console.log(`[API_MANAGER] Grounding ${active ? 'ACTIVE' : 'HIBERNATING'} - All layers updated`);
  }

  isActive(): boolean {
    return this.liveGroundingActive;
  }

  getStatus(): any {
    const layers: Record<string, string> = {};
    this.layerStatus.forEach((status, layer) => {
      layers[layer] = status;
    });

    return {
      liveGroundingActive: this.liveGroundingActive,
      temporalAnchor: CURRENT_ANCHOR_DATE,
      layers,
      geometricLock: GEOMETRIC_LOCK,
      entropyThreshold: ENTROPY_THRESHOLD
    };
  }

  async queryMolecularLayer(compound: string): Promise<GroundingResult> {
    const layer = GroundingLayer.MOLECULAR;

    if (!this.liveGroundingActive) {
      const cached = getFromCache(layer, compound);
      if (cached) {
        return {
          layer,
          status: APIStatus.SOVEREIGN_ONLY,
          data: cached.data,
          geometricAlignment: cached.geometricAlignment,
          entropyFlag: "LOW_ENTROPY",
          timestamp: new Date().toISOString(),
          cached: true
        };
      }
      return {
        layer,
        status: APIStatus.HIBERNATING,
        data: { message: "Sovereign State - No cached molecular data" },
        geometricAlignment: GEOMETRIC_LOCK,
        entropyFlag: "LOW_ENTROPY",
        timestamp: new Date().toISOString(),
        cached: false
      };
    }

    const result = await PubChemClient.getCompoundGeometry(compound);

    if (result.status === "success") {
      const alignment = result.geometricAlignment || GEOMETRIC_LOCK;
      setInCache(layer, compound, result, alignment);

      return {
        layer,
        status: APIStatus.ACTIVE,
        data: result,
        geometricAlignment: alignment,
        entropyFlag: result.entropyFlag || "LOW_ENTROPY",
        timestamp: new Date().toISOString(),
        cached: false
      };
    }

    return {
      layer,
      status: APIStatus.ERROR,
      data: result,
      geometricAlignment: 0,
      entropyFlag: "HIGH_ENTROPY_GRIT",
      timestamp: new Date().toISOString(),
      cached: false
    };
  }

  async queryCosmicLayer(): Promise<GroundingResult> {
    const layer = GroundingLayer.COSMIC;
    const cacheKey = "latest_events";

    if (!this.liveGroundingActive) {
      const cached = getFromCache(layer, cacheKey);
      if (cached) {
        return {
          layer,
          status: APIStatus.SOVEREIGN_ONLY,
          data: cached.data,
          geometricAlignment: cached.geometricAlignment,
          entropyFlag: "LOW_ENTROPY",
          timestamp: new Date().toISOString(),
          cached: true
        };
      }
      return {
        layer,
        status: APIStatus.HIBERNATING,
        data: { message: "Sovereign State - Using baseline metric tension", metricTension: 0.0001 },
        geometricAlignment: GEOMETRIC_LOCK,
        entropyFlag: "LOW_ENTROPY",
        timestamp: new Date().toISOString(),
        cached: false
      };
    }

    const result = await CosmicEventListener.getLatestEvents();

    if (result.status === "success") {
      const alignment = (result.metricTension || 0) + GEOMETRIC_LOCK;
      setInCache(layer, cacheKey, result, alignment);

      // For cosmic events, HIGH_ENTROPY_GRIT is triggered when metric tension exceeds 0.08333 (1/12)
      // This indicates significant seismic/cosmic activity that may affect unified field calculations
      const maxTension = result.metricTension || 0;
      const entropyFlag: "LOW_ENTROPY" | "HIGH_ENTROPY_GRIT" = maxTension > ENTROPY_THRESHOLD 
        ? "HIGH_ENTROPY_GRIT" 
        : "LOW_ENTROPY";

      return {
        layer,
        status: APIStatus.ACTIVE,
        data: result,
        geometricAlignment: alignment,
        entropyFlag,
        timestamp: new Date().toISOString(),
        cached: false
      };
    }

    return {
      layer,
      status: APIStatus.ERROR,
      data: result,
      geometricAlignment: GEOMETRIC_LOCK,
      entropyFlag: "LOW_ENTROPY",
      timestamp: new Date().toISOString(),
      cached: false
    };
  }

  async validateWithLogicGuard(expression: string, expected: number, xiLevel: number): Promise<GroundingResult> {
    const layer = GroundingLayer.LOGIC;

    if (!this.liveGroundingActive) {
      const { deviation, entropyFlag } = UniversalSchemaBroker.checkEntropyDeviation(expected);

      return {
        layer,
        status: APIStatus.SOVEREIGN_ONLY,
        data: {
          validated: deviation < ENTROPY_THRESHOLD,
          method: "sovereign_internal",
          xiLevel,
          deviation,
          message: "Sovereign validation - Wolfram unavailable"
        },
        geometricAlignment: GEOMETRIC_LOCK,
        entropyFlag,
        timestamp: new Date().toISOString(),
        cached: false
      };
    }

    const result = await WolframValidator.validateCalculation(expression, expected, xiLevel);
    const entropyFlag = result.entropyFlag || "LOW_ENTROPY";

    return {
      layer,
      status: result.method === "wolfram_alpha" ? APIStatus.ACTIVE : APIStatus.SOVEREIGN_ONLY,
      data: result,
      geometricAlignment: GEOMETRIC_LOCK,
      entropyFlag,
      timestamp: new Date().toISOString(),
      cached: false
    };
  }

  mapToGrutGeometry(value: number, valueType: "generic" | "bond_length" | "frequency" = "generic"): SchemaMapping | any {
    switch (valueType) {
      case "bond_length":
        return UniversalSchemaBroker.mapChemicalBondToGrut(value);
      case "frequency":
        return UniversalSchemaBroker.mapFrequencyToMetricHum(value);
      default:
        return UniversalSchemaBroker.mapGenericValue(value);
    }
  }

  async queryGritLayer(query: string): Promise<GroundingResult> {
    const layer = GroundingLayer.GRIT;

    if (!this.liveGroundingActive) {
      const cached = getFromCache(layer, query);
      if (cached) {
        return {
          layer,
          status: APIStatus.SOVEREIGN_ONLY,
          data: cached.data,
          geometricAlignment: cached.geometricAlignment,
          entropyFlag: "LOW_ENTROPY",
          timestamp: new Date().toISOString(),
          cached: true
        };
      }
      return {
        layer,
        status: APIStatus.HIBERNATING,
        data: { message: "Sovereign State - No cached search data", query },
        geometricAlignment: GEOMETRIC_LOCK,
        entropyFlag: "LOW_ENTROPY",
        timestamp: new Date().toISOString(),
        cached: false
      };
    }

    // Grit layer uses Perplexity for live search (Google requires separate API key)
    // For now, return a placeholder indicating the layer is available
    const apiKey = process.env.GOOGLE_SEARCH_API_KEY;
    const cx = process.env.GOOGLE_SEARCH_CX;

    if (!apiKey || !cx) {
      return {
        layer,
        status: APIStatus.SOVEREIGN_ONLY,
        data: { 
          message: "Google Search not configured (GOOGLE_SEARCH_API_KEY, GOOGLE_SEARCH_CX required)",
          query,
          fallback: "Use /api/grounding/search with Perplexity API for live search"
        },
        geometricAlignment: GEOMETRIC_LOCK,
        entropyFlag: "LOW_ENTROPY",
        timestamp: new Date().toISOString(),
        cached: false
      };
    }

    try {
      const params = new URLSearchParams({
        key: apiKey,
        cx: cx,
        q: `${query} ${CURRENT_ANCHOR_DATE}`,
        num: "5"
      });

      const response = await fetch(`https://www.googleapis.com/customsearch/v1?${params}`, {
        signal: AbortSignal.timeout(10000)
      });

      if (response.ok) {
        const data = await response.json() as { items?: Array<{ title: string; link: string; snippet: string }> };
        const results = (data.items || []).map(item => ({
          title: item.title,
          link: item.link,
          snippet: item.snippet,
          temporalAnchor: CURRENT_ANCHOR_DATE
        }));

        const result = {
          query,
          temporalAnchor: CURRENT_ANCHOR_DATE,
          results,
          count: results.length,
          status: "success"
        };

        setInCache(layer, query, result, GEOMETRIC_LOCK);

        return {
          layer,
          status: APIStatus.ACTIVE,
          data: result,
          geometricAlignment: GEOMETRIC_LOCK,
          entropyFlag: "LOW_ENTROPY",
          timestamp: new Date().toISOString(),
          cached: false
        };
      }

      return {
        layer,
        status: APIStatus.ERROR,
        data: { error: `Google API error: ${response.status}`, query },
        geometricAlignment: 0,
        entropyFlag: "HIGH_ENTROPY_GRIT",
        timestamp: new Date().toISOString(),
        cached: false
      };

    } catch (error) {
      return {
        layer,
        status: APIStatus.ERROR,
        data: { error: String(error), query },
        geometricAlignment: 0,
        entropyFlag: "HIGH_ENTROPY_GRIT",
        timestamp: new Date().toISOString(),
        cached: false
      };
    }
  }
}

// Global instance
export const groundingManager = new MultiLayerGroundingManager(false);

export function getGroundingManager(): MultiLayerGroundingManager {
  return groundingManager;
}
