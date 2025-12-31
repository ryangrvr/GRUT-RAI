import { 
  type User, type Subscriber, type GrutConstants, type HistoricalResonance,
  type QuantumModule, type QuantumRegistryState, type ParityCheckLog, type QuantumModuleStatus,
  users, subscribers, conversations, messages, metricMemory, fileUploads, universeStates, historicalResonances,
  quantumModules, quantumRegistryState, parityCheckLog,
  DEFAULT_GRUT_CONSTANTS, GROUND_STATE_BASELINE, PARITY_TOLERANCE_DEFAULT
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

  async saveHistoricalResonance(data: { userId?: string; biologicalMarker: string; anchorPointMyr: number; groundStateDecay: number; reconstructionAccuracy: number; kernelSeed?: unknown; standingWavePattern?: unknown; rMaxTriggered?: boolean; notes?: string }): Promise<HistoricalResonance> {
    const id = crypto.randomUUID();
    const result = db.insert(historicalResonances).values({
      id,
      userId: data.userId ?? null,
      biologicalMarker: data.biologicalMarker,
      anchorPointMyr: data.anchorPointMyr,
      groundStateDecay: data.groundStateDecay,
      reconstructionAccuracy: data.reconstructionAccuracy,
      kernelSeed: data.kernelSeed,
      standingWavePattern: data.standingWavePattern,
      rMaxTriggered: data.rMaxTriggered ?? false,
      notes: data.notes ?? null,
    }).returning().all();
    return result[0];
  }

  async getHistoricalResonances(userId?: string): Promise<HistoricalResonance[]> {
    if (userId) {
      return db.select().from(historicalResonances)
        .where(eq(historicalResonances.userId, userId))
        .orderBy(desc(historicalResonances.createdAt)).all();
    }
    return db.select().from(historicalResonances)
      .orderBy(desc(historicalResonances.createdAt)).all();
  }

  async deleteHistoricalResonance(id: string): Promise<void> {
    db.delete(historicalResonances).where(eq(historicalResonances.id, id)).run();
  }

  // ===== QUANTUM LOGIC LAYER METHODS =====

  async getAllQuantumModules(): Promise<QuantumModule[]> {
    return db.select().from(quantumModules).orderBy(quantumModules.moduleKey).all();
  }

  async getQuantumModule(moduleKey: string): Promise<QuantumModule | undefined> {
    const [mod] = db.select().from(quantumModules).where(eq(quantumModules.moduleKey, moduleKey)).all();
    return mod || undefined;
  }

  async updateQuantumModuleStatus(moduleKey: string, status: QuantumModuleStatus): Promise<QuantumModule | undefined> {
    const result = db.update(quantumModules)
      .set({ status, lastUpdated: new Date().toISOString() })
      .where(eq(quantumModules.moduleKey, moduleKey))
      .returning().all();
    return result[0] || undefined;
  }

  async recordParityCheck(moduleKey: string, inputValue: number, passed: boolean, discarded: boolean = false): Promise<ParityCheckLog> {
    const deviation = Math.abs(inputValue - GROUND_STATE_BASELINE);
    const id = crypto.randomUUID();
    
    const result = db.insert(parityCheckLog).values({
      id,
      moduleKey,
      inputValue,
      expectedBaseline: GROUND_STATE_BASELINE,
      deviation,
      passed,
      discarded,
    }).returning().all();

    if (!passed) {
      const currentModule = db.select().from(quantumModules).where(eq(quantumModules.moduleKey, moduleKey)).all()[0];
      const newDriftCount = (currentModule?.parityDriftCount ?? 0) + 1;
      
      db.update(quantumModules)
        .set({ 
          parityDriftCount: newDriftCount,
          lastParityValue: inputValue,
          lastUpdated: new Date().toISOString()
        })
        .where(eq(quantumModules.moduleKey, moduleKey))
        .run();
      
      const currentState = db.select().from(quantumRegistryState).where(eq(quantumRegistryState.id, 'global')).all()[0];
      const newFailureCount = (currentState?.totalParityFailures ?? 0) + 1;
      
      db.update(quantumRegistryState)
        .set({ totalParityFailures: newFailureCount })
        .where(eq(quantumRegistryState.id, 'global'))
        .run();
    }

    return result[0];
  }

  async getQuantumRegistryState(): Promise<QuantumRegistryState | undefined> {
    const [state] = db.select().from(quantumRegistryState).where(eq(quantumRegistryState.id, 'global')).all();
    return state || undefined;
  }

  async setManualSingularityEnabled(enabled: boolean): Promise<QuantumRegistryState | undefined> {
    const result = db.update(quantumRegistryState)
      .set({ 
        manualSingularityEnabled: enabled,
        updatedAt: new Date().toISOString()
      })
      .where(eq(quantumRegistryState.id, 'global'))
      .returning().all();
    return result[0] || undefined;
  }

  async recordCollapseAttempt(): Promise<void> {
    const current = await this.getQuantumRegistryState();
    db.update(quantumRegistryState)
      .set({
        lastCollapseAttempt: new Date().toISOString(),
        totalCollapsesPrevented: (current?.totalCollapsesPrevented ?? 0) + 1,
        updatedAt: new Date().toISOString()
      })
      .where(eq(quantumRegistryState.id, 'global'))
      .run();
  }

  async getRecentParityLogs(limit: number = 50): Promise<ParityCheckLog[]> {
    return db.select().from(parityCheckLog)
      .orderBy(desc(parityCheckLog.createdAt))
      .limit(limit).all();
  }
}

export const sqliteStorage = new SqliteStorage();
