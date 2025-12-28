import { sql, relations } from "drizzle-orm";
import { pgTable, text, varchar, timestamp, real, jsonb, interval } from "drizzle-orm/pg-core";
import { createInsertSchema } from "drizzle-zod";
import { z } from "zod";

export const users = pgTable("users", {
  id: varchar("id").primaryKey().default(sql`gen_random_uuid()`),
  username: text("username").notNull().unique(),
  password: text("password").notNull(),
});

export const insertUserSchema = createInsertSchema(users).pick({
  username: true,
  password: true,
});

export type InsertUser = z.infer<typeof insertUserSchema>;
export type User = typeof users.$inferSelect;

export const subscribers = pgTable("subscribers", {
  id: varchar("id").primaryKey().default(sql`gen_random_uuid()`),
  email: text("email").notNull().unique(),
});

export const insertSubscriberSchema = createInsertSchema(subscribers).pick({
  email: true,
}).extend({
  email: z.string().email("Please enter a valid email address"),
});

export type InsertSubscriber = z.infer<typeof insertSubscriberSchema>;
export type Subscriber = typeof subscribers.$inferSelect;

// Chat conversations table - persisted to database
export const conversations = pgTable("conversations", {
  id: varchar("id").primaryKey().default(sql`gen_random_uuid()`),
  title: text("title").notNull(),
  createdAt: timestamp("created_at").defaultNow().notNull(),
});

export type Conversation = typeof conversations.$inferSelect;

// Chat messages table - persisted to database
export const messages = pgTable("messages", {
  id: varchar("id").primaryKey().default(sql`gen_random_uuid()`),
  conversationId: varchar("conversation_id").notNull().references(() => conversations.id, { onDelete: "cascade" }),
  role: text("role").notNull(), // "user" | "assistant" | "system"
  content: text("content").notNull(),
  createdAt: timestamp("created_at").defaultNow().notNull(),
});

export type Message = typeof messages.$inferSelect;

// Metric Memory table - Retarded Potential Kernel storage
// Stores embeddings and complexity metrics for GRUT-style "ringing" through history
export const metricMemory = pgTable("metric_memory", {
  id: varchar("id").primaryKey().default(sql`gen_random_uuid()`),
  conversationId: varchar("conversation_id").notNull().references(() => conversations.id, { onDelete: "cascade" }),
  messageId: varchar("message_id").references(() => messages.id, { onDelete: "cascade" }),
  interactionVector: jsonb("interaction_vector"), // Embedding array (1536 dims for OpenAI)
  complexityRatioXi: real("complexity_ratio_xi").default(0.0), // Tracks informational saturation (Ξ)
  createdAt: timestamp("created_at").defaultNow().notNull(),
  latencyDeltaTau: text("latency_delta_tau").default("41.9 Myr"), // The GRUT constant τ₀
});

export type MetricMemory = typeof metricMemory.$inferSelect;

// File uploads table for chat attachments
export const fileUploads = pgTable("file_uploads", {
  id: varchar("id").primaryKey().default(sql`gen_random_uuid()`),
  conversationId: varchar("conversation_id").references(() => conversations.id, { onDelete: "cascade" }),
  messageId: varchar("message_id").references(() => messages.id, { onDelete: "cascade" }),
  userId: varchar("user_id").references(() => users.id, { onDelete: "cascade" }),
  filename: text("filename").notNull(),
  originalName: text("original_name").notNull(),
  mimeType: text("mime_type").notNull(),
  size: real("size").notNull(),
  createdAt: timestamp("created_at").defaultNow().notNull(),
});

export type FileUpload = typeof fileUploads.$inferSelect;
export type InsertFileUpload = typeof fileUploads.$inferInsert;

// Relations (defined after all tables to avoid temporal dead zone)
export const conversationsRelations = relations(conversations, ({ many }) => ({
  messages: many(messages),
  metricMemory: many(metricMemory),
}));

export const messagesRelations = relations(messages, ({ one }) => ({
  conversation: one(conversations, {
    fields: [messages.conversationId],
    references: [conversations.id],
  }),
}));

export const metricMemoryRelations = relations(metricMemory, ({ one }) => ({
  conversation: one(conversations, {
    fields: [metricMemory.conversationId],
    references: [conversations.id],
  }),
  message: one(messages, {
    fields: [metricMemory.messageId],
    references: [messages.id],
  }),
}));

// Universe state snapshots for Phase 6 synchronization
export const universeStates = pgTable("universe_states", {
  id: varchar("id").primaryKey().default(sql`gen_random_uuid()`),
  userId: varchar("user_id").references(() => users.id, { onDelete: "cascade" }),
  name: text("name").notNull(),
  masterSeed: jsonb("master_seed").notNull(), // GRUT Master Seed configuration
  messages: jsonb("messages").notNull(), // Last 20 messages
  conversationId: varchar("conversation_id").references(() => conversations.id, { onDelete: "set null" }),
  createdAt: timestamp("created_at").defaultNow().notNull(),
});

export type UniverseState = typeof universeStates.$inferSelect;
export type InsertUniverseState = typeof universeStates.$inferInsert;

// Types for API responses (with ISO string dates for JSON serialization)
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
  userId?: string;
}

export interface ChatFileUpload {
  id: string;
  conversationId?: string;
  messageId?: string;
  userId?: string;
  filename: string;
  originalName: string;
  mimeType: string;
  size: number;
  createdAt: string;
}
