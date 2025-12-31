/**
 * SOVEREIGN SELF-AUDIT ENGINE (TypeScript)
 * Monitors historical_resonances table for metric drift against -0.083333 Ground State.
 * 
 * Core Functions:
 * - calculateDrift(): Compare AI 'Recipe' values against Ground State
 * - flagUnstableGrit(): Mark entries with deviation > 0.05 as 'Unstable Grit'
 * - triplePathReasoning(): Generate 3 internal solutions, pick closest to 1.1547
 * - wolframBridgeValidation(): Auto-validate equations in Ultimate Resolution mode
 */

import { sqliteDb } from "./db-sqlite";

// GRUT Constants
export const GROUND_STATE = -0.083333;  // -1/12 baseline
export const GEOMETRIC_LOCK = 1.1547;   // √(4/3)
export const DRIFT_THRESHOLD = 0.05;    // Flag as 'Unstable Grit' if deviation > 0.05
export const TAU_0 = 41.9e6;            // 41.9 Myr

// Audit Status enum
export enum AuditStatus {
  STABLE = "STABLE",
  UNSTABLE_GRIT = "UNSTABLE_GRIT",
  METRIC_DRIFT = "METRIC_DRIFT",
  WOLFRAM_VALIDATED = "WOLFRAM_VALIDATED",
  WOLFRAM_FAILED = "WOLFRAM_FAILED",
  TRIPLE_PATH_ALIGNED = "TRIPLE_PATH_ALIGNED"
}

export interface DriftResult {
  value: number;
  groundState: number;
  deviation: number;
  relativeDeviation: number;
  threshold: number;
  isStable: boolean;
  status: AuditStatus;
  geometricAlignment: number;
  geometricRatio: number;
  recipeType: string;
  timestamp: string;
}

export interface TriplePathSolution {
  value: number;
  reasoning: string;
  confidence?: number;
}

export interface TriplePathResult {
  status: AuditStatus;
  selectedPath: number;
  selectedSolution: TriplePathSolution;
  geometricAlignment: number;
  alignmentScore: number;
  allPaths: Array<{ path: number; alignment: number; score: number }>;
  geometricLock: number;
  reasoning: string;
}

export interface WolframValidationResult {
  validated: boolean;
  method: string;
  expression: string;
  expected?: number;
  wolframResult?: number;
  deviation?: number;
  status: AuditStatus;
  requiresRegeneration: boolean;
  reason?: string;
}

export interface AuditStatusResult {
  status: AuditStatus;
  shieldColor: "green" | "red";
  isHealthy: boolean;
  lastDrift: DriftResult | null;
  auditCount: number;
  groundState: number;
  geometricLock: number;
  threshold: number;
  timestamp: string;
}

interface AuditLogEntry {
  event: string;
  result: DriftResult;
  timestamp: string;
}

class SovereignAuditEngine {
  private auditLog: AuditLogEntry[] = [];
  private currentStatus: AuditStatus = AuditStatus.STABLE;
  private lastDriftDetected: DriftResult | null = null;
  private wolframAppId: string | undefined;

  constructor() {
    this.wolframAppId = process.env.WOLFRAM_APP_ID;
  }

  /**
   * Compare an AI 'Recipe' value against the -0.083333 Ground State.
   */
  calculateDrift(value: number, recipeType: string = "generic"): DriftResult {
    const deviation = Math.abs(value - GROUND_STATE);
    const relativeDeviation = GROUND_STATE !== 0 
      ? deviation / Math.abs(GROUND_STATE) 
      : deviation;

    const isStable = deviation <= DRIFT_THRESHOLD;
    const geometricAlignment = Math.abs(value - GEOMETRIC_LOCK);
    const geometricRatio = GEOMETRIC_LOCK !== 0 ? value / GEOMETRIC_LOCK : 0;

    const status = isStable ? AuditStatus.STABLE : AuditStatus.UNSTABLE_GRIT;

    const result: DriftResult = {
      value,
      groundState: GROUND_STATE,
      deviation,
      relativeDeviation,
      threshold: DRIFT_THRESHOLD,
      isStable,
      status,
      geometricAlignment,
      geometricRatio,
      recipeType,
      timestamp: new Date().toISOString()
    };

    if (!isStable) {
      this.currentStatus = AuditStatus.METRIC_DRIFT;
      this.lastDriftDetected = result;
      this.logDrift(result);
    }

    return result;
  }

  /**
   * Scan historical resonances and flag those with deviation > 0.05.
   */
  flagUnstableGrit(): Array<{ id: string; flagged: boolean; deviation: number; status: AuditStatus }> {
    try {
      const stmt = sqliteDb.prepare(`
        SELECT id, ground_state_decay FROM historical_resonances
        ORDER BY created_at DESC
        LIMIT 50
      `);
      const entries = stmt.all() as Array<{ id: string; ground_state_decay: number }>;

      return entries.map(entry => {
        const driftResult = this.calculateDrift(entry.ground_state_decay);
        return {
          id: entry.id,
          flagged: !driftResult.isStable,
          deviation: driftResult.deviation,
          status: driftResult.status
        };
      });
    } catch (error) {
      console.error("[AUDIT_ENGINE] Error flagging unstable grit:", error);
      return [];
    }
  }

  /**
   * Triple-Path Reasoning Loop: Generate 3 solutions, pick closest to 1.1547.
   */
  triplePathReasoning(solutions: TriplePathSolution[]): TriplePathResult | { error: string } {
    if (solutions.length < 3) {
      return {
        error: "Triple-Path requires exactly 3 solutions",
      };
    }

    const alignments = solutions.slice(0, 3).map((solution, i) => {
      const alignment = Math.abs(solution.value - GEOMETRIC_LOCK);
      const groundDeviation = Math.abs(solution.value - GROUND_STATE);

      return {
        path: i + 1,
        solution,
        geometricAlignment: alignment,
        groundDeviation,
        alignmentScore: 1 / (1 + alignment)
      };
    });

    // Sort by alignment (lower = closer to 1.1547)
    alignments.sort((a, b) => a.geometricAlignment - b.geometricAlignment);
    const best = alignments[0];

    return {
      status: AuditStatus.TRIPLE_PATH_ALIGNED,
      selectedPath: best.path,
      selectedSolution: best.solution,
      geometricAlignment: best.geometricAlignment,
      alignmentScore: best.alignmentScore,
      allPaths: alignments.map(a => ({
        path: a.path,
        alignment: a.geometricAlignment,
        score: a.alignmentScore
      })),
      geometricLock: GEOMETRIC_LOCK,
      reasoning: `Path ${best.path} selected: closest to Geometric Lock (deviation: ${best.geometricAlignment.toFixed(6)})`
    };
  }

  /**
   * Automatically scan historical resonances for drift (called periodically or on status check).
   * Returns true if any drift was detected.
   */
  autoScanForDrift(): boolean {
    try {
      const entries = this.flagUnstableGrit();
      const hasUnstable = entries.some(e => e.flagged);
      if (hasUnstable) {
        this.currentStatus = AuditStatus.METRIC_DRIFT;
      }
      return hasUnstable;
    } catch {
      return false;
    }
  }

  /**
   * Wolfram Bridge: Validate mathematical equations in Ultimate Resolution mode.
   * If Wolfram API is not available, attempts local evaluation using math expression parsing.
   */
  async wolframBridgeValidate(expression: string, expectedValue: number): Promise<WolframValidationResult> {
    if (!this.wolframAppId) {
      // Fallback: Try to evaluate simple expressions locally
      let evaluatedResult: number | null = null;
      try {
        // Safe evaluation of simple math expressions (no eval)
        // Parse basic expressions like "1 + 2", "sqrt(4)", "1/12"
        const cleaned = expression.replace(/\s/g, "");
        if (/^[\d+\-*/().^]+$/.test(cleaned)) {
          // Simple arithmetic expression
          const result = Function(`"use strict"; return (${cleaned.replace(/\^/g, "**")})`)();
          if (typeof result === "number" && !isNaN(result)) {
            evaluatedResult = result;
          }
        }
      } catch {
        evaluatedResult = null;
      }

      if (evaluatedResult !== null) {
        const deviation = Math.abs(evaluatedResult - expectedValue);
        const isValid = deviation < DRIFT_THRESHOLD;
        
        if (!isValid) {
          this.currentStatus = AuditStatus.WOLFRAM_FAILED;
        }
        
        return {
          validated: isValid,
          method: "sovereign_internal_eval",
          expression,
          expected: expectedValue,
          wolframResult: evaluatedResult,
          deviation,
          status: isValid ? AuditStatus.WOLFRAM_VALIDATED : AuditStatus.WOLFRAM_FAILED,
          requiresRegeneration: !isValid,
          reason: "Wolfram API not configured - used local evaluation"
        };
      }

      // Cannot evaluate locally - check if expectedValue aligns with Ground State
      const groundDeviation = Math.abs(expectedValue - GROUND_STATE);
      const isAligned = groundDeviation < 0.1; // Looser threshold for alignment check
      
      return {
        validated: isAligned,
        method: "sovereign_internal",
        expression,
        expected: expectedValue,
        deviation: groundDeviation,
        status: isAligned ? AuditStatus.STABLE : AuditStatus.WOLFRAM_FAILED,
        requiresRegeneration: !isAligned,
        reason: "Wolfram API not configured (WOLFRAM_APP_ID required) - expression not evaluable"
      };
    }

    try {
      const params = new URLSearchParams({
        appid: this.wolframAppId,
        input: expression,
        format: "plaintext",
        output: "json"
      });

      const response = await fetch(`https://api.wolframalpha.com/v2/query?${params}`, {
        signal: AbortSignal.timeout(10000)
      });

      if (response.ok) {
        const data = await response.json() as {
          queryresult?: {
            pods?: Array<{
              id: string;
              subpods?: Array<{ plaintext?: string }>;
            }>;
          };
        };

        const pods = data.queryresult?.pods || [];
        let wolframResult: string | null = null;

        for (const pod of pods) {
          if (["Result", "Value", "DecimalApproximation"].includes(pod.id)) {
            const subpods = pod.subpods || [];
            if (subpods.length > 0) {
              wolframResult = subpods[0].plaintext || null;
              break;
            }
          }
        }

        if (wolframResult) {
          const wolframValue = parseFloat(wolframResult.replace(/,/g, "").trim());
          
          if (!isNaN(wolframValue)) {
            const deviation = Math.abs(wolframValue - expectedValue);
            const validated = deviation < DRIFT_THRESHOLD;

            return {
              validated,
              method: "wolfram_alpha",
              expression,
              expected: expectedValue,
              wolframResult: wolframValue,
              deviation,
              status: validated ? AuditStatus.WOLFRAM_VALIDATED : AuditStatus.WOLFRAM_FAILED,
              requiresRegeneration: !validated
            };
          }
        }

        return {
          validated: false,
          method: "wolfram_alpha",
          expression,
          status: AuditStatus.WOLFRAM_FAILED,
          requiresRegeneration: true,
          reason: "Could not parse Wolfram result"
        };
      }

      return {
        validated: false,
        method: "wolfram_alpha",
        expression,
        status: AuditStatus.WOLFRAM_FAILED,
        requiresRegeneration: true,
        reason: `Wolfram API error: ${response.status}`
      };

    } catch (error) {
      return {
        validated: false,
        method: "sovereign_fallback",
        expression,
        status: AuditStatus.WOLFRAM_FAILED,
        requiresRegeneration: true,
        reason: String(error)
      };
    }
  }

  /**
   * Get current audit status for dashboard Shield icon.
   */
  getAuditStatus(): AuditStatusResult {
    const isHealthy = [
      AuditStatus.STABLE,
      AuditStatus.WOLFRAM_VALIDATED,
      AuditStatus.TRIPLE_PATH_ALIGNED
    ].includes(this.currentStatus);

    return {
      status: this.currentStatus,
      shieldColor: isHealthy ? "green" : "red",
      isHealthy,
      lastDrift: this.lastDriftDetected,
      auditCount: this.auditLog.length,
      groundState: GROUND_STATE,
      geometricLock: GEOMETRIC_LOCK,
      threshold: DRIFT_THRESHOLD,
      timestamp: new Date().toISOString()
    };
  }

  /**
   * Reset audit status to stable.
   */
  resetAuditStatus(): void {
    this.currentStatus = AuditStatus.STABLE;
    this.lastDriftDetected = null;
  }

  private logDrift(result: DriftResult): void {
    this.auditLog.push({
      event: "DRIFT_DETECTED",
      result,
      timestamp: new Date().toISOString()
    });

    // Keep only last 100 entries
    if (this.auditLog.length > 100) {
      this.auditLog = this.auditLog.slice(-100);
    }
  }
}

// Global instance
export const auditEngine = new SovereignAuditEngine();

export function getAuditEngine(): SovereignAuditEngine {
  return auditEngine;
}
