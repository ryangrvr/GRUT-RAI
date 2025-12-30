import { drizzle } from "drizzle-orm/node-postgres";
import pg from "pg";
import * as schema from "@shared/schema";

const { Pool } = pg;

// Database availability state for Sovereign Offline Mode
export let dbAvailable = false;
export let dbError: string | null = null;

// Check if DATABASE_URL requires SSL
function shouldUseSSL(url: string | undefined): boolean {
  if (!url) return false;
  // Only use SSL if explicitly required in the connection string
  if (url.includes('sslmode=disable')) return false;
  if (url.includes('sslmode=require')) return true;
  // Default: no SSL for internal Replit databases
  return false;
}

// Build pool config with proper SSL handling
function buildPoolConfig(): pg.PoolConfig {
  const baseConfig: pg.PoolConfig = {
    connectionTimeoutMillis: 15000,
    idleTimeoutMillis: 30000,
    max: 5,
  };
  
  const useSSL = shouldUseSSL(process.env.DATABASE_URL);
  if (useSSL) {
    baseConfig.ssl = { rejectUnauthorized: false };
  }
  
  if (process.env.PGHOST) {
    return {
      ...baseConfig,
      host: process.env.PGHOST,
      port: parseInt(process.env.PGPORT || "5432"),
      user: process.env.PGUSER,
      password: process.env.PGPASSWORD,
      database: process.env.PGDATABASE,
    };
  }
  
  return {
    ...baseConfig,
    connectionString: process.env.DATABASE_URL,
  };
}

const poolConfig = buildPoolConfig();
console.log(`[DB] Config: host=${process.env.PGHOST || 'from-url'}:${process.env.PGPORT || '5432'}/${process.env.PGDATABASE || 'db'}, ssl=${poolConfig.ssl ? 'enabled' : 'disabled'}`);

export const pool = process.env.DATABASE_URL ? new Pool(poolConfig) : null;
export const db = pool ? drizzle(pool, { schema }) : null;

// Test database connection and update availability state
export async function testDatabaseConnection(): Promise<boolean> {
  if (!pool) {
    dbError = "DATABASE_URL not configured";
    dbAvailable = false;
    return false;
  }
  
  try {
    const client = await pool.connect();
    await client.query('SELECT 1');
    client.release();
    dbAvailable = true;
    dbError = null;
    console.log("[DB] Connection test: SUCCESS");
    return true;
  } catch (err) {
    dbAvailable = false;
    dbError = err instanceof Error ? err.message : "Unknown error";
    console.log(`[DB] Connection test: FAILED - ${dbError}`);
    return false;
  }
}
