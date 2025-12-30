import { 
  type User, type Subscriber, type GrutConstants,
  users, subscribers, conversations, messages, metricMemory, fileUploads, universeStates, DEFAULT_GRUT_CONSTANTS
} from "../shared/schema-sqlite";
import { db, dbAvailable, sqliteDb } from "./db-sqlite";
import { eq, desc } from "drizzle-orm";
import { applyGrutGain } from "./grut-logic";
import type { IStorage, WeightedMemory } from "./storage";
import type { ChatMessage, ChatConversation, ChatFileUpload, UniverseState } from "../shared/schema-sqlite";

// SQLite Storage Implementation for Sovereign Local Mode
export class SqliteStorage implements IStorage {
  async getUser(id: string): Promise<User | undefined> {
    const [user] = db.select().from(users).where(eq(users.id, id)).all();
    return user || undefined;
  }

  async getUserByEmail(email: string): Promise<User | undefined> {
    const [user] = db.select().from(users).where(eq(users.email, email.toLowerCase().trim())).all();
    return user || undefined;
  }

  async createUser(email: string, passwordHash: string): Promise<User> {
    const id = crypto.randomUUID();
    const result = db.insert(users).values({
      id,
      email: email.toLowerCase().trim(),
      passwordHash,
    }).returning().all();
    return result[0];
  }

  async updateUserConstants(userId: string, constants: GrutConstants): Promise<User | undefined> {
    const result = db.update(users)
      .set({ grutConstants: constants })
      .where(eq(users.id, userId))
      .returning().all();
    return result[0] || undefined;
  }

  async getSubscriberByEmail(email: string): Promise<Subscriber | undefined> {
    const [subscriber] = db.select().from(subscribers).where(eq(subscribers.email, email)).all();
    return subscriber || undefined;
  }

  async createSubscriber(insertSubscriber: { email: string }): Promise<Subscriber> {
    const id = crypto.randomUUID();
    const result = db.insert(subscribers).values({ id, ...insertSubscriber }).returning().all();
    return result[0];
  }

  async getConversation(id: string): Promise<ChatConversation | undefined> {
    const [conversation] = db.select().from(conversations).where(eq(conversations.id, id)).all();
    if (!conversation) return undefined;

    const msgs = db.select().from(messages)
      .where(eq(messages.conversationId, id))
      .orderBy(messages.createdAt).all();

    return {
      id: conversation.id,
      title: conversation.title,
      createdAt: conversation.createdAt,
      messages: msgs.map(m => ({
        id: m.id,
        conversationId: m.conversationId,
        role: m.role as "user" | "assistant" | "system",
        content: m.content,
        createdAt: m.createdAt,
      })),
      parentConversationId: conversation.parentConversationId ?? undefined,
      forkSourceMessageId: conversation.forkSourceMessageId ?? undefined,
      constants: conversation.constants ?? DEFAULT_GRUT_CONSTANTS,
    };
  }

  async getAllConversations(): Promise<ChatConversation[]> {
    const convos = db.select().from(conversations).orderBy(desc(conversations.createdAt)).all();
    
    return convos.map(c => ({
      id: c.id,
      title: c.title,
      createdAt: c.createdAt,
      messages: [],
    }));
  }

  async getUserConversations(userId: string): Promise<ChatConversation[]> {
    const convos = db.select().from(conversations)
      .where(eq(conversations.userId, userId))
      .orderBy(desc(conversations.createdAt)).all();
    return convos.map(c => ({
      id: c.id,
      title: c.title,
      createdAt: c.createdAt,
      messages: [],
    }));
  }

  async createConversation(title: string, userId: string): Promise<ChatConversation> {
    const id = crypto.randomUUID();
    const result = db.insert(conversations).values({
      id,
      userId,
      title,
      constants: DEFAULT_GRUT_CONSTANTS,
    }).returning().all();

    return {
      id: result[0].id,
      title: result[0].title,
      createdAt: result[0].createdAt,
      messages: [],
      constants: DEFAULT_GRUT_CONSTANTS,
    };
  }

  async deleteConversation(id: string, userId: string): Promise<void> {
    const [conv] = db.select().from(conversations).where(eq(conversations.id, id)).all();
    if (conv && conv.userId === userId) {
      db.delete(conversations).where(eq(conversations.id, id)).run();
    }
  }

  async addMessage(conversationId: string, role: "user" | "assistant" | "system", content: string): Promise<ChatMessage> {
    const id = crypto.randomUUID();
    const result = db.insert(messages).values({
      id,
      conversationId,
      role,
      content,
    }).returning().all();

    return {
      id: result[0].id,
      conversationId: result[0].conversationId,
      role: result[0].role as "user" | "assistant" | "system",
      content: result[0].content,
      createdAt: result[0].createdAt,
    };
  }

  async getMessages(conversationId: string): Promise<ChatMessage[]> {
    const msgs = db.select().from(messages)
      .where(eq(messages.conversationId, conversationId))
      .orderBy(messages.createdAt).all();

    return msgs.map(m => ({
      id: m.id,
      conversationId: m.conversationId,
      role: m.role as "user" | "assistant" | "system",
      content: m.content,
      createdAt: m.createdAt,
    }));
  }

  async storeMetricMemory(conversationId: string, messageId: string, embedding: number[], complexityXi: number): Promise<void> {
    const id = crypto.randomUUID();
    db.insert(metricMemory).values({
      id,
      conversationId,
      messageId,
      interactionVector: embedding,
      complexityRatioXi: complexityXi,
    }).run();
  }

  async getTopMetricMemories(conversationId: string, limit = 10, tauSeconds = 3600): Promise<WeightedMemory[]> {
    const memories = db.select({
      id: metricMemory.id,
      messageId: metricMemory.messageId,
      complexityXi: metricMemory.complexityRatioXi,
      createdAt: metricMemory.createdAt,
    }).from(metricMemory)
      .where(eq(metricMemory.conversationId, conversationId))
      .orderBy(desc(metricMemory.createdAt))
      .limit(limit * 2).all();

    const results: WeightedMemory[] = [];
    for (const mem of memories) {
      if (!mem.messageId) continue;
      const [msg] = db.select().from(messages).where(eq(messages.id, mem.messageId)).all();
      if (!msg) continue;

      const memoryAge = (Date.now() - new Date(mem.createdAt).getTime()) / 1000;
      const kernelWeight = (1/3) * Math.exp(-memoryAge / tauSeconds);
      const baseRelevance = mem.complexityXi ?? 0.5;
      const effectiveRelevance = baseRelevance * kernelWeight;
      const boostedRelevance = applyGrutGain(effectiveRelevance);

      results.push({
        messageId: mem.messageId,
        content: msg.content,
        role: msg.role,
        effectiveRelevance,
        boostedRelevance,
        createdAt: mem.createdAt,
      });
    }

    return results.sort((a, b) => b.boostedRelevance - a.boostedRelevance).slice(0, limit);
  }

  async saveFileUpload(data: { conversationId?: string; messageId?: string; userId?: string; filename: string; originalName: string; mimeType: string; size: number }): Promise<ChatFileUpload> {
    const id = crypto.randomUUID();
    const result = db.insert(fileUploads).values({
      id,
      ...data,
    }).returning().all();
    return {
      ...result[0],
      createdAt: result[0].createdAt,
    };
  }

  async getFileUploads(conversationId: string): Promise<ChatFileUpload[]> {
    const uploads = db.select().from(fileUploads).where(eq(fileUploads.conversationId, conversationId)).all();
    return uploads.map(u => ({
      ...u,
      createdAt: u.createdAt,
    }));
  }

  async saveUniverseState(userId: string, name: string, masterSeed: object, msgs: ChatMessage[], conversationId?: string): Promise<UniverseState> {
    const id = crypto.randomUUID();
    const result = db.insert(universeStates).values({
      id,
      userId,
      name,
      conversationId: conversationId ?? null,
      masterSeed,
      messageSnapshot: msgs,
    }).returning().all();
    return result[0];
  }

  async loadUniverseState(userId: string, stateId?: string): Promise<UniverseState | undefined> {
    if (stateId) {
      const [state] = db.select().from(universeStates)
        .where(eq(universeStates.id, stateId)).all();
      return state || undefined;
    }
    const [state] = db.select().from(universeStates)
      .where(eq(universeStates.userId, userId))
      .orderBy(desc(universeStates.createdAt))
      .limit(1).all();
    return state || undefined;
  }

  async getUserUniverseStates(userId: string): Promise<UniverseState[]> {
    return db.select().from(universeStates)
      .where(eq(universeStates.userId, userId))
      .orderBy(desc(universeStates.createdAt)).all();
  }

  async forkConversation(sourceConversationId: string, forkMessageId: string, title: string, constants: GrutConstants, userId: string): Promise<ChatConversation> {
    const id = crypto.randomUUID();
    const result = db.insert(conversations).values({
      id,
      userId,
      title,
      parentConversationId: sourceConversationId,
      forkSourceMessageId: forkMessageId,
      constants,
    }).returning().all();

    const sourceMsgs = db.select().from(messages)
      .where(eq(messages.conversationId, sourceConversationId))
      .orderBy(messages.createdAt).all();

    let reachedFork = false;
    for (const msg of sourceMsgs) {
      if (reachedFork) break;
      if (msg.id === forkMessageId) reachedFork = true;
      const newMsgId = crypto.randomUUID();
      db.insert(messages).values({
        id: newMsgId,
        conversationId: id,
        role: msg.role,
        content: msg.content,
      }).run();
    }

    return {
      id: result[0].id,
      title: result[0].title,
      createdAt: result[0].createdAt,
      messages: [],
      parentConversationId: sourceConversationId,
      forkSourceMessageId: forkMessageId,
      constants,
    };
  }

  async getChildConversations(parentId: string): Promise<ChatConversation[]> {
    const children = db.select().from(conversations)
      .where(eq(conversations.parentConversationId, parentId)).all();
    return children.map(c => ({
      id: c.id,
      title: c.title,
      createdAt: c.createdAt,
      messages: [],
      parentConversationId: c.parentConversationId ?? undefined,
    }));
  }

  async verifyConversationOwnership(conversationId: string, userId: string): Promise<boolean> {
    const [conv] = db.select().from(conversations).where(eq(conversations.id, conversationId)).all();
    return conv?.userId === userId;
  }
}

export const sqliteStorage = new SqliteStorage();
