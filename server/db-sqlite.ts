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
  
  dbAvailable = true;
  console.log("[DB-SQLITE] Diamond Persistence tables ready. Sovereign Local Storage ACTIVE.");
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
