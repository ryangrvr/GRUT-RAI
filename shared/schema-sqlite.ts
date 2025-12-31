import { sql } from "drizzle-orm";
import { sqliteTable, text, integer, real } from "drizzle-orm/sqlite-core";
import { createInsertSchema } from "drizzle-zod";
import { z } from "zod";

// GRUT Constants interface for timeline customization
export interface GrutConstants {
  tau_0: number;
  n_g: number;
  alpha: number;
  R_max: string;
}

export const DEFAULT_GRUT_CONSTANTS: GrutConstants = {
  tau_0: 41.9,
  n_g: 1.1547,
  alpha: 0.333333,
  R_max: "Lambda_Limit"
};

// SQLite uses text for UUIDs - we generate them in application code
function generateUUID() {
  return sql`(lower(hex(randomblob(4))) || '-' || lower(hex(randomblob(2))) || '-4' || substr(lower(hex(randomblob(2))),2) || '-' || substr('89ab',abs(random()) % 4 + 1, 1) || substr(lower(hex(randomblob(2))),2) || '-' || lower(hex(randomblob(6))))`;
}

export const users = sqliteTable("users", {
  id: text("id").primaryKey().$defaultFn(() => crypto.randomUUID()),
  email: text("email").notNull().unique(),
  passwordHash: text("password_hash").notNull(),
  grutConstants: text("grut_constants", { mode: "json" }).$type<GrutConstants>(),
  createdAt: text("created_at").default(sql`CURRENT_TIMESTAMP`).notNull(),
});

export const insertUserSchema = createInsertSchema(users).pick({
  email: true,
  passwordHash: true,
}).extend({
  email: z.string().email("Please enter a valid email address"),
});

export type InsertUser = z.infer<typeof insertUserSchema>;
export type User = typeof users.$inferSelect;

export const subscribers = sqliteTable("subscribers", {
  id: text("id").primaryKey().$defaultFn(() => crypto.randomUUID()),
  email: text("email").notNull().unique(),
});

export const insertSubscriberSchema = createInsertSchema(subscribers).pick({
  email: true,
}).extend({
  email: z.string().email("Please enter a valid email address"),
});

export type InsertSubscriber = z.infer<typeof insertSubscriberSchema>;
export type Subscriber = typeof subscribers.$inferSelect;

// Chat conversations table
export const conversations = sqliteTable("conversations", {
  id: text("id").primaryKey().$defaultFn(() => crypto.randomUUID()),
  userId: text("user_id").references(() => users.id),
  title: text("title").notNull(),
  createdAt: text("created_at").default(sql`CURRENT_TIMESTAMP`).notNull(),
  parentConversationId: text("parent_conversation_id"),
  forkSourceMessageId: text("fork_source_message_id"),
  constants: text("constants", { mode: "json" }).$type<GrutConstants>(),
});

export type Conversation = typeof conversations.$inferSelect;

// Chat messages table
export const messages = sqliteTable("messages", {
  id: text("id").primaryKey().$defaultFn(() => crypto.randomUUID()),
  conversationId: text("conversation_id").notNull().references(() => conversations.id),
  role: text("role").notNull(),
  content: text("content").notNull(),
  createdAt: text("created_at").default(sql`CURRENT_TIMESTAMP`).notNull(),
});

export type Message = typeof messages.$inferSelect;

// Metric Memory table
export const metricMemory = sqliteTable("metric_memory", {
  id: text("id").primaryKey().$defaultFn(() => crypto.randomUUID()),
  conversationId: text("conversation_id").notNull().references(() => conversations.id),
  messageId: text("message_id").references(() => messages.id),
  interactionVector: text("interaction_vector", { mode: "json" }),
  complexityRatioXi: real("complexity_ratio_xi").default(0.0),
  createdAt: text("created_at").default(sql`CURRENT_TIMESTAMP`).notNull(),
  latencyDeltaTau: text("latency_delta_tau").default("41.9 Myr"),
});

export type MetricMemory = typeof metricMemory.$inferSelect;

// File uploads table
export const fileUploads = sqliteTable("file_uploads", {
  id: text("id").primaryKey().$defaultFn(() => crypto.randomUUID()),
  conversationId: text("conversation_id").references(() => conversations.id),
  messageId: text("message_id").references(() => messages.id),
  userId: text("user_id").references(() => users.id),
  filename: text("filename").notNull(),
  originalName: text("original_name").notNull(),
  mimeType: text("mime_type").notNull(),
  size: real("size").notNull(),
  createdAt: text("created_at").default(sql`CURRENT_TIMESTAMP`).notNull(),
});

export type FileUpload = typeof fileUploads.$inferSelect;
export type InsertFileUpload = typeof fileUploads.$inferInsert;

// Universe states table
export const universeStates = sqliteTable("universe_states", {
  id: text("id").primaryKey().$defaultFn(() => crypto.randomUUID()),
  userId: text("user_id").notNull().references(() => users.id),
  name: text("name").notNull(),
  conversationId: text("conversation_id").references(() => conversations.id),
  masterSeed: text("master_seed", { mode: "json" }).notNull(),
  messageSnapshot: text("message_snapshot", { mode: "json" }).notNull(),
  createdAt: text("created_at").default(sql`CURRENT_TIMESTAMP`).notNull(),
});

export type UniverseState = typeof universeStates.$inferSelect;

// Historical Resonances table for DNA-Resonance & Time-Well Module
export const historicalResonances = sqliteTable("historical_resonances", {
  id: text("id").primaryKey().$defaultFn(() => crypto.randomUUID()),
  userId: text("user_id").references(() => users.id),
  biologicalMarker: text("biological_marker").notNull(),
  anchorPointMyr: real("anchor_point_myr").notNull(),
  groundStateDecay: real("ground_state_decay").notNull(),
  reconstructionAccuracy: real("reconstruction_accuracy").notNull(),
  kernelSeed: text("kernel_seed", { mode: "json" }),
  standingWavePattern: text("standing_wave_pattern", { mode: "json" }),
  rMaxTriggered: integer("r_max_triggered", { mode: "boolean" }).default(false),
  notes: text("notes"),
  createdAt: text("created_at").default(sql`CURRENT_TIMESTAMP`).notNull(),
});

export const insertHistoricalResonanceSchema = createInsertSchema(historicalResonances).pick({
  biologicalMarker: true,
  anchorPointMyr: true,
  notes: true,
}).extend({
  biologicalMarker: z.string().min(1, "Biological marker is required"),
  anchorPointMyr: z.number().min(0.00038).max(13800),
});

export type InsertHistoricalResonance = z.infer<typeof insertHistoricalResonanceSchema>;
export type HistoricalResonance = typeof historicalResonances.$inferSelect;

// Exported types for API responses
export interface ChatMessage {
  id: string;
  conversationId: string;
  role: "user" | "assistant" | "system";
  content: string;
  createdAt: string;
}

export interface ChatConversation {
  id: string;
  title: string;
  createdAt: string;
  messages: ChatMessage[];
  parentConversationId?: string;
  forkSourceMessageId?: string;
  constants?: GrutConstants;
}

export interface ChatFileUpload {
  id: string;
  conversationId?: string | null;
  messageId?: string | null;
  userId?: string | null;
  filename: string;
  originalName: string;
  mimeType: string;
  size: number;
  createdAt: string;
}

// Quantum Module Status Enum
export type QuantumModuleStatus = "OBSERVER_REQUIRED" | "ACTIVE" | "COLLAPSED" | "PARITY_FAILED";

// Quantum Modules Registry - tracks all quantum computation units
export const quantumModules = sqliteTable("quantum_modules", {
  id: text("id").primaryKey().$defaultFn(() => crypto.randomUUID()),
  moduleKey: text("module_key").notNull().unique(),
  displayName: text("display_name").notNull(),
  status: text("status").notNull().default("OBSERVER_REQUIRED"),
  parityCheckEnabled: integer("parity_check_enabled", { mode: "boolean" }).default(true),
  lastParityValue: real("last_parity_value"),
  parityDriftCount: integer("parity_drift_count").default(0),
  parityTolerance: real("parity_tolerance").default(0.001),
  observerBinding: text("observer_binding"),
  lastUpdated: text("last_updated").default(sql`CURRENT_TIMESTAMP`).notNull(),
  createdAt: text("created_at").default(sql`CURRENT_TIMESTAMP`).notNull(),
});

export type QuantumModule = typeof quantumModules.$inferSelect;
export type InsertQuantumModule = typeof quantumModules.$inferInsert;

// Quantum Registry State - global settings including Manual Singularity
export const quantumRegistryState = sqliteTable("quantum_registry_state", {
  id: text("id").primaryKey().default("global"),
  manualSingularityEnabled: integer("manual_singularity_enabled", { mode: "boolean" }).default(false),
  groundStateBaseline: real("ground_state_baseline").default(-0.0833333333),
  parityToleranceGlobal: real("parity_tolerance_global").default(0.001),
  totalParityFailures: integer("total_parity_failures").default(0),
  totalCollapsesPrevented: integer("total_collapses_prevented").default(0),
  lastCollapseAttempt: text("last_collapse_attempt"),
  updatedAt: text("updated_at").default(sql`CURRENT_TIMESTAMP`).notNull(),
});

export type QuantumRegistryState = typeof quantumRegistryState.$inferSelect;

// Parity Check Log - audit trail of all parity checks
export const parityCheckLog = sqliteTable("parity_check_log", {
  id: text("id").primaryKey().$defaultFn(() => crypto.randomUUID()),
  moduleKey: text("module_key").notNull(),
  inputValue: real("input_value").notNull(),
  expectedBaseline: real("expected_baseline").default(-0.0833333333),
  deviation: real("deviation").notNull(),
  passed: integer("passed", { mode: "boolean" }).notNull(),
  discarded: integer("discarded", { mode: "boolean" }).default(false),
  createdAt: text("created_at").default(sql`CURRENT_TIMESTAMP`).notNull(),
});

export type ParityCheckLog = typeof parityCheckLog.$inferSelect;

// GRUT Constants for Quantum Logic Layer
export const GROUND_STATE_BASELINE = -1/12;
export const GROUND_STATE_BASELINE_APPROX = -0.0833333333;
export const PARITY_TOLERANCE_DEFAULT = 0.001;
