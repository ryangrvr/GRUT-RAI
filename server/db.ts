import { drizzle } from "drizzle-orm/node-postgres";
import pg from "pg";
import * as schema from "@shared/schema";

const { Pool } = pg;

if (!process.env.DATABASE_URL) {
  throw new Error(
    "DATABASE_URL must be set. Did you forget to provision a database?",
  );
}

// Use individual PG env vars if available, fall back to DATABASE_URL
const poolConfig: pg.PoolConfig = process.env.PGHOST ? {
  host: process.env.PGHOST,
  port: parseInt(process.env.PGPORT || "5432"),
  user: process.env.PGUSER,
  password: process.env.PGPASSWORD,
  database: process.env.PGDATABASE,
  connectionTimeoutMillis: 30000,
  idleTimeoutMillis: 60000,
  max: 5,
  ssl: { rejectUnauthorized: false }
} : {
  connectionString: process.env.DATABASE_URL,
  connectionTimeoutMillis: 30000,
  idleTimeoutMillis: 60000,
  max: 5,
  ssl: { rejectUnauthorized: false }
};

console.log(`[DB] Connecting to: ${process.env.PGHOST || 'DATABASE_URL'}:${process.env.PGPORT || '5432'}/${process.env.PGDATABASE || 'db'}`);

export const pool = new Pool(poolConfig);
export const db = drizzle(pool, { schema });
