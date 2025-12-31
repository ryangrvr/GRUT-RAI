import { drizzle } from "drizzle-orm/better-sqlite3";
import Database from "better-sqlite3";
import * as schema from "../shared/schema-sqlite";
import path from "path";

const DB_PATH = path.join(process.cwd(), "diamond_persistence.db");

console.log(`[DB-SQLITE] Initializing Sovereign Local Storage at: ${DB_PATH}`);

// Create SQLite database connection
export const sqliteDb = new Database(DB_PATH);
export const db = drizzle(sqliteDb, { schema });

// Database is always available with SQLite
export let dbAvailable = true;
export let dbError: string | null = null;

// Initialize tables
export function initializeSqliteTables(): void {
  console.log("[DB-SQLITE] Creating tables for Diamond Persistence...");
  
  // Create users table
  sqliteDb.exec(`
    CREATE TABLE IF NOT EXISTS users (
      id TEXT PRIMARY KEY,
      email TEXT NOT NULL UNIQUE,
      password_hash TEXT NOT NULL,
      grut_constants TEXT,
      created_at TEXT DEFAULT CURRENT_TIMESTAMP NOT NULL
    )
  `);
  
  // Create subscribers table
  sqliteDb.exec(`
    CREATE TABLE IF NOT EXISTS subscribers (
      id TEXT PRIMARY KEY,
      email TEXT NOT NULL UNIQUE
    )
  `);
  
  // Create conversations table
  sqliteDb.exec(`
    CREATE TABLE IF NOT EXISTS conversations (
      id TEXT PRIMARY KEY,
      user_id TEXT REFERENCES users(id),
      title TEXT NOT NULL,
      created_at TEXT DEFAULT CURRENT_TIMESTAMP NOT NULL,
      parent_conversation_id TEXT,
      fork_source_message_id TEXT,
      constants TEXT
    )
  `);
  
  // Create messages table
  sqliteDb.exec(`
    CREATE TABLE IF NOT EXISTS messages (
      id TEXT PRIMARY KEY,
      conversation_id TEXT NOT NULL REFERENCES conversations(id),
      role TEXT NOT NULL,
      content TEXT NOT NULL,
      created_at TEXT DEFAULT CURRENT_TIMESTAMP NOT NULL
    )
  `);
  
  // Create metric_memory table
  sqliteDb.exec(`
    CREATE TABLE IF NOT EXISTS metric_memory (
      id TEXT PRIMARY KEY,
      conversation_id TEXT NOT NULL REFERENCES conversations(id),
      message_id TEXT REFERENCES messages(id),
      interaction_vector TEXT,
      complexity_ratio_xi REAL DEFAULT 0.0,
      created_at TEXT DEFAULT CURRENT_TIMESTAMP NOT NULL,
      latency_delta_tau TEXT DEFAULT '41.9 Myr'
    )
  `);
  
  // Create file_uploads table
  sqliteDb.exec(`
    CREATE TABLE IF NOT EXISTS file_uploads (
      id TEXT PRIMARY KEY,
      conversation_id TEXT REFERENCES conversations(id),
      message_id TEXT REFERENCES messages(id),
      user_id TEXT REFERENCES users(id),
      filename TEXT NOT NULL,
      original_name TEXT NOT NULL,
      mime_type TEXT NOT NULL,
      size REAL NOT NULL,
      created_at TEXT DEFAULT CURRENT_TIMESTAMP NOT NULL
    )
  `);
  
  // Create universe_states table
  sqliteDb.exec(`
    CREATE TABLE IF NOT EXISTS universe_states (
      id TEXT PRIMARY KEY,
      user_id TEXT NOT NULL REFERENCES users(id),
      name TEXT NOT NULL,
      conversation_id TEXT REFERENCES conversations(id),
      master_seed TEXT NOT NULL,
      message_snapshot TEXT NOT NULL,
      created_at TEXT DEFAULT CURRENT_TIMESTAMP NOT NULL
    )
  `);
  
  // Create historical_resonances table for DNA-Resonance & Time-Well Module
  sqliteDb.exec(`
    CREATE TABLE IF NOT EXISTS historical_resonances (
      id TEXT PRIMARY KEY,
      user_id TEXT REFERENCES users(id),
      biological_marker TEXT NOT NULL,
      anchor_point_myr REAL NOT NULL,
      ground_state_decay REAL NOT NULL,
      reconstruction_accuracy REAL NOT NULL,
      kernel_seed TEXT,
      standing_wave_pattern TEXT,
      r_max_triggered INTEGER DEFAULT 0,
      notes TEXT,
      created_at TEXT DEFAULT CURRENT_TIMESTAMP NOT NULL
    )
  `);
  
  // Create quantum_modules table for Quantum Logic Layer
  sqliteDb.exec(`
    CREATE TABLE IF NOT EXISTS quantum_modules (
      id TEXT PRIMARY KEY,
      module_key TEXT NOT NULL UNIQUE,
      display_name TEXT NOT NULL,
      status TEXT NOT NULL DEFAULT 'OBSERVER_REQUIRED',
      parity_check_enabled INTEGER DEFAULT 1,
      last_parity_value REAL,
      parity_drift_count INTEGER DEFAULT 0,
      parity_tolerance REAL DEFAULT 0.001,
      observer_binding TEXT,
      last_updated TEXT DEFAULT CURRENT_TIMESTAMP NOT NULL,
      created_at TEXT DEFAULT CURRENT_TIMESTAMP NOT NULL
    )
  `);
  
  // Create quantum_registry_state table for global quantum settings
  sqliteDb.exec(`
    CREATE TABLE IF NOT EXISTS quantum_registry_state (
      id TEXT PRIMARY KEY DEFAULT 'global',
      manual_singularity_enabled INTEGER DEFAULT 0,
      ground_state_baseline REAL DEFAULT -0.0833333333,
      parity_tolerance_global REAL DEFAULT 0.001,
      total_parity_failures INTEGER DEFAULT 0,
      total_collapses_prevented INTEGER DEFAULT 0,
      last_collapse_attempt TEXT,
      updated_at TEXT DEFAULT CURRENT_TIMESTAMP NOT NULL
    )
  `);
  
  // Create parity_check_log table for audit trail
  sqliteDb.exec(`
    CREATE TABLE IF NOT EXISTS parity_check_log (
      id TEXT PRIMARY KEY,
      module_key TEXT NOT NULL,
      input_value REAL NOT NULL,
      expected_baseline REAL DEFAULT -0.0833333333,
      deviation REAL NOT NULL,
      passed INTEGER NOT NULL,
      discarded INTEGER DEFAULT 0,
      created_at TEXT DEFAULT CURRENT_TIMESTAMP NOT NULL
    )
  `);
  
  // Create sovereign_cache table for API Manager hibernation
  sqliteDb.exec(`
    CREATE TABLE IF NOT EXISTS sovereign_cache (
      id TEXT PRIMARY KEY,
      layer TEXT NOT NULL,
      query_key TEXT NOT NULL,
      cached_data TEXT NOT NULL,
      geometric_alignment REAL DEFAULT 1.1547,
      created_at TEXT DEFAULT CURRENT_TIMESTAMP NOT NULL,
      UNIQUE(layer, query_key)
    )
  `);
  
  // Initialize default quantum modules (OBSERVER_REQUIRED status)
  const defaultModules = [
    { key: 'TIMEWELL', name: 'Time-Well Resonance' },
    { key: 'METRICHUM', name: 'MetricHum Audio' },
    { key: 'NANOGRAV', name: 'NANOGrav Pulsar' },
    { key: 'BARYONIC', name: 'Baryonic Sensor' },
    { key: 'GRAVITATIONAL', name: 'Gravitational Wave' },
  ];
  
  for (const mod of defaultModules) {
    sqliteDb.exec(`
      INSERT OR IGNORE INTO quantum_modules (id, module_key, display_name, status)
      VALUES ('${crypto.randomUUID()}', '${mod.key}', '${mod.name}', 'OBSERVER_REQUIRED')
    `);
  }
  
  // Initialize global quantum registry state
  sqliteDb.exec(`
    INSERT OR IGNORE INTO quantum_registry_state (id, manual_singularity_enabled)
    VALUES ('global', 0)
  `);
  
  dbAvailable = true;
  console.log("[DB-SQLITE] Diamond Persistence tables ready. Quantum Logic Layer initialized.");
  console.log("[DB-SQLITE] All modules set to OBSERVER_REQUIRED status. Awaiting observer binding.");
}

// Test database connection
export async function testDatabaseConnection(): Promise<boolean> {
  try {
    sqliteDb.exec("SELECT 1");
    dbAvailable = true;
    dbError = null;
    console.log("[DB-SQLITE] Connection test: SUCCESS");
    return true;
  } catch (err) {
    dbAvailable = false;
    dbError = err instanceof Error ? err.message : "Unknown error";
    console.log(`[DB-SQLITE] Connection test: FAILED - ${dbError}`);
    return false;
  }
}

// Initialize on module load
initializeSqliteTables();
