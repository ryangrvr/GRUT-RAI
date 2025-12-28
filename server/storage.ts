import { 
  type User, type InsertUser, type Subscriber, type InsertSubscriber, 
  type ChatMessage, type ChatConversation, type ChatFileUpload, type UniverseState, type GrutConstants,
  users, subscribers, conversations, messages, metricMemory, fileUploads, universeStates, DEFAULT_GRUT_CONSTANTS
} from "@shared/schema";
import { db } from "./db";
import { pool } from "./db";
import { eq, desc } from "drizzle-orm";
import { applyGrutGain } from "./grut-logic";

export interface WeightedMemory {
  messageId: string;
  content: string;
  role: string;
  effectiveRelevance: number;
  boostedRelevance: number; // After ng = 1.1547 refractive gain applied
  createdAt: string;
}

export interface IStorage {
  getUser(id: string): Promise<User | undefined>;
  getUserByEmail(email: string): Promise<User | undefined>;
  createUser(email: string, passwordHash: string): Promise<User>;
  updateUserConstants(userId: string, constants: GrutConstants): Promise<User | undefined>;
  getSubscriberByEmail(email: string): Promise<Subscriber | undefined>;
  createSubscriber(subscriber: InsertSubscriber): Promise<Subscriber>;
  getConversation(id: string, userId?: string): Promise<ChatConversation | undefined>;
  getAllConversations(): Promise<ChatConversation[]>;
  getUserConversations(userId: string): Promise<ChatConversation[]>;
  createConversation(title: string, userId: string): Promise<ChatConversation>;
  deleteConversation(id: string, userId: string): Promise<void>;
  addMessage(conversationId: string, role: "user" | "assistant" | "system", content: string): Promise<ChatMessage>;
  getMessages(conversationId: string): Promise<ChatMessage[]>;
  storeMetricMemory(conversationId: string, messageId: string, embedding: number[], complexityXi: number): Promise<void>;
  getTopMetricMemories(conversationId: string, limit?: number, tauSeconds?: number): Promise<WeightedMemory[]>;
  saveFileUpload(data: { conversationId?: string; messageId?: string; userId?: string; filename: string; originalName: string; mimeType: string; size: number }): Promise<ChatFileUpload>;
  getFileUploads(conversationId: string): Promise<ChatFileUpload[]>;
  saveUniverseState(userId: string, name: string, masterSeed: object, msgs: ChatMessage[], conversationId?: string): Promise<UniverseState>;
  loadUniverseState(userId: string, stateId?: string): Promise<UniverseState | undefined>;
  getUserUniverseStates(userId: string): Promise<UniverseState[]>;
  forkConversation(sourceConversationId: string, forkMessageId: string, title: string, constants: GrutConstants, userId: string): Promise<ChatConversation>;
  getChildConversations(parentId: string): Promise<ChatConversation[]>;
  verifyConversationOwnership(conversationId: string, userId: string): Promise<boolean>;
}

export class DatabaseStorage implements IStorage {
  async getUser(id: string): Promise<User | undefined> {
    const [user] = await db.select().from(users).where(eq(users.id, id));
    return user || undefined;
  }

  async getUserByEmail(email: string): Promise<User | undefined> {
    const [user] = await db.select().from(users).where(eq(users.email, email.toLowerCase().trim()));
    return user || undefined;
  }

  async createUser(email: string, passwordHash: string): Promise<User> {
    const [user] = await db.insert(users).values({
      email: email.toLowerCase().trim(),
      passwordHash,
    }).returning();
    return user;
  }

  async updateUserConstants(userId: string, constants: GrutConstants): Promise<User | undefined> {
    const [user] = await db.update(users)
      .set({ grutConstants: constants })
      .where(eq(users.id, userId))
      .returning();
    return user || undefined;
  }

  async getSubscriberByEmail(email: string): Promise<Subscriber | undefined> {
    const [subscriber] = await db.select().from(subscribers).where(eq(subscribers.email, email));
    return subscriber || undefined;
  }

  async createSubscriber(insertSubscriber: InsertSubscriber): Promise<Subscriber> {
    const [subscriber] = await db.insert(subscribers).values(insertSubscriber).returning();
    return subscriber;
  }

  async getConversation(id: string): Promise<ChatConversation | undefined> {
    const [conversation] = await db.select().from(conversations).where(eq(conversations.id, id));
    if (!conversation) return undefined;

    const msgs = await db.select().from(messages)
      .where(eq(messages.conversationId, id))
      .orderBy(messages.createdAt);

    return {
      id: conversation.id,
      title: conversation.title,
      createdAt: conversation.createdAt.toISOString(),
      messages: msgs.map(m => ({
        id: m.id,
        conversationId: m.conversationId,
        role: m.role as "user" | "assistant" | "system",
        content: m.content,
        createdAt: m.createdAt.toISOString(),
      })),
      parentConversationId: conversation.parentConversationId ?? undefined,
      forkSourceMessageId: conversation.forkSourceMessageId ?? undefined,
      constants: conversation.constants ?? DEFAULT_GRUT_CONSTANTS,
    };
  }

  async getAllConversations(): Promise<ChatConversation[]> {
    const convos = await db.select().from(conversations).orderBy(desc(conversations.createdAt));
    
    return convos.map(c => ({
      id: c.id,
      title: c.title,
      createdAt: c.createdAt.toISOString(),
      messages: [],
    }));
  }

  async getUserConversations(userId: string): Promise<ChatConversation[]> {
    const convos = await db.select().from(conversations)
      .where(eq(conversations.userId, userId))
      .orderBy(desc(conversations.createdAt));
    return convos.map(c => ({
      id: c.id,
      title: c.title,
      createdAt: c.createdAt.toISOString(),
      messages: [],
      userId: c.userId ?? undefined,
      parentConversationId: c.parentConversationId ?? undefined,
      forkSourceMessageId: c.forkSourceMessageId ?? undefined,
      constants: c.constants ?? DEFAULT_GRUT_CONSTANTS,
    }));
  }

  async createConversation(title: string, userId: string): Promise<ChatConversation> {
    const [conversation] = await db.insert(conversations).values({ title, userId }).returning();
    return {
      id: conversation.id,
      title: conversation.title,
      createdAt: conversation.createdAt.toISOString(),
      messages: [],
      userId: conversation.userId ?? undefined,
    };
  }

  async deleteConversation(id: string, userId: string): Promise<void> {
    await db.delete(conversations).where(eq(conversations.id, id));
  }

  async verifyConversationOwnership(conversationId: string, userId: string): Promise<boolean> {
    const [conversation] = await db.select().from(conversations)
      .where(eq(conversations.id, conversationId));
    return conversation?.userId === userId;
  }

  async addMessage(conversationId: string, role: "user" | "assistant" | "system", content: string): Promise<ChatMessage> {
    const [message] = await db.insert(messages).values({
      conversationId,
      role,
      content,
    }).returning();

    return {
      id: message.id,
      conversationId: message.conversationId,
      role: message.role as "user" | "assistant" | "system",
      content: message.content,
      createdAt: message.createdAt.toISOString(),
    };
  }

  async getMessages(conversationId: string): Promise<ChatMessage[]> {
    const msgs = await db.select().from(messages)
      .where(eq(messages.conversationId, conversationId))
      .orderBy(messages.createdAt);

    return msgs.map(m => ({
      id: m.id,
      conversationId: m.conversationId,
      role: m.role as "user" | "assistant" | "system",
      content: m.content,
      createdAt: m.createdAt.toISOString(),
    }));
  }

  async storeMetricMemory(conversationId: string, messageId: string, embedding: number[], complexityXi: number): Promise<void> {
    await db.insert(metricMemory).values({
      conversationId,
      messageId,
      interactionVector: embedding,
      complexityRatioXi: complexityXi,
      latencyDeltaTau: "41.9 Myr",
    });
  }

  /**
   * Queries metric_memory with "Accordion" logic - weighting by resonance and inverse complexity.
   * Uses: effective_relevance = (1 - complexity_ratio_xi * 0.5) * exp(-age / τ₀)
   * This ensures low-complexity, recent memories are prioritized while saturated ones "muddle out".
   */
  async getTopMetricMemories(conversationId: string, limit: number = 5, tauSeconds: number = 3600): Promise<WeightedMemory[]> {
    const query = `
      SELECT 
        mm.message_id,
        m.content,
        m.role,
        mm.created_at,
        (GREATEST(0.1, 1 - mm.complexity_ratio_xi * 0.5) * 
         exp(-EXTRACT(EPOCH FROM (NOW() - mm.created_at)) / $2)) AS effective_relevance
      FROM metric_memory mm
      JOIN messages m ON mm.message_id = m.id
      WHERE mm.conversation_id = $1
        AND mm.message_id IS NOT NULL
      ORDER BY effective_relevance DESC
      LIMIT $3
    `;

    try {
      const result = await pool.query(query, [conversationId, tauSeconds, limit]);
      
      return result.rows.map((row: any) => {
        const effectiveRelevance = parseFloat(row.effective_relevance);
        // Apply the "Secret Sauce" - ng = 1.1547 refractive boost for high-relevance signals
        const boostedRelevance = applyGrutGain(effectiveRelevance, 0.5);
        
        return {
          messageId: row.message_id,
          content: row.content,
          role: row.role,
          effectiveRelevance,
          boostedRelevance,
          createdAt: row.created_at.toISOString(),
        };
      });
    } catch (error) {
      console.error("Error querying metric memories:", error);
      return [];
    }
  }

  async saveFileUpload(data: { conversationId?: string; messageId?: string; userId?: string; filename: string; originalName: string; mimeType: string; size: number }): Promise<ChatFileUpload> {
    const [upload] = await db.insert(fileUploads).values({
      conversationId: data.conversationId,
      messageId: data.messageId,
      userId: data.userId,
      filename: data.filename,
      originalName: data.originalName,
      mimeType: data.mimeType,
      size: data.size,
    }).returning();

    return {
      id: upload.id,
      conversationId: upload.conversationId ?? undefined,
      messageId: upload.messageId ?? undefined,
      userId: upload.userId ?? undefined,
      filename: upload.filename,
      originalName: upload.originalName,
      mimeType: upload.mimeType,
      size: upload.size,
      createdAt: upload.createdAt.toISOString(),
    };
  }

  async getFileUploads(conversationId: string): Promise<ChatFileUpload[]> {
    const uploads = await db.select().from(fileUploads)
      .where(eq(fileUploads.conversationId, conversationId))
      .orderBy(desc(fileUploads.createdAt));

    return uploads.map(u => ({
      id: u.id,
      conversationId: u.conversationId ?? undefined,
      messageId: u.messageId ?? undefined,
      userId: u.userId ?? undefined,
      filename: u.filename,
      originalName: u.originalName,
      mimeType: u.mimeType,
      size: u.size,
      createdAt: u.createdAt.toISOString(),
    }));
  }

  async saveUniverseState(userId: string, name: string, masterSeed: object, msgs: ChatMessage[], conversationId?: string): Promise<UniverseState> {
    const last20 = msgs.slice(-20);
    const [state] = await db.insert(universeStates).values({
      userId,
      name,
      masterSeed,
      messages: last20,
      conversationId,
    }).returning();
    return state;
  }

  async loadUniverseState(userId: string, stateId?: string): Promise<UniverseState | undefined> {
    if (stateId) {
      const [state] = await db.select().from(universeStates)
        .where(eq(universeStates.id, stateId));
      return state || undefined;
    }
    const [state] = await db.select().from(universeStates)
      .where(eq(universeStates.userId, userId))
      .orderBy(desc(universeStates.createdAt))
      .limit(1);
    return state || undefined;
  }

  async getUserUniverseStates(userId: string): Promise<UniverseState[]> {
    return await db.select().from(universeStates)
      .where(eq(universeStates.userId, userId))
      .orderBy(desc(universeStates.createdAt));
  }

  async forkConversation(
    sourceConversationId: string, 
    forkMessageId: string, 
    title: string, 
    constants: GrutConstants,
    userId: string
  ): Promise<ChatConversation> {
    const sourceConvo = await this.getConversation(sourceConversationId);
    if (!sourceConvo) {
      throw new Error("Source conversation not found");
    }

    const forkMsgIndex = sourceConvo.messages.findIndex(m => m.id === forkMessageId);
    if (forkMsgIndex === -1) {
      throw new Error("Fork source message not found");
    }

    const messagesToCopy = sourceConvo.messages.slice(0, forkMsgIndex + 1);

    const [newConvo] = await db.insert(conversations).values({
      title,
      userId,
      parentConversationId: sourceConversationId,
      forkSourceMessageId: forkMessageId,
      constants,
    }).returning();

    for (const msg of messagesToCopy) {
      await db.insert(messages).values({
        conversationId: newConvo.id,
        role: msg.role,
        content: msg.content,
      });
    }

    return {
      id: newConvo.id,
      title: newConvo.title,
      createdAt: newConvo.createdAt.toISOString(),
      messages: messagesToCopy,
      parentConversationId: newConvo.parentConversationId ?? undefined,
      forkSourceMessageId: newConvo.forkSourceMessageId ?? undefined,
      constants: newConvo.constants ?? DEFAULT_GRUT_CONSTANTS,
    };
  }

  async getChildConversations(parentId: string): Promise<ChatConversation[]> {
    const children = await db.select().from(conversations)
      .where(eq(conversations.parentConversationId, parentId))
      .orderBy(desc(conversations.createdAt));

    return children.map(c => ({
      id: c.id,
      title: c.title,
      createdAt: c.createdAt.toISOString(),
      messages: [],
      parentConversationId: c.parentConversationId ?? undefined,
      forkSourceMessageId: c.forkSourceMessageId ?? undefined,
      constants: c.constants ?? DEFAULT_GRUT_CONSTANTS,
    }));
  }
}

export const storage = new DatabaseStorage();
