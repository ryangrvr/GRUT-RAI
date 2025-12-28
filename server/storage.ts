import { 
  type User, type InsertUser, type Subscriber, type InsertSubscriber, 
  type ChatMessage, type ChatConversation,
  users, subscribers, conversations, messages, metricMemory
} from "@shared/schema";
import { db } from "./db";
import { eq, desc } from "drizzle-orm";

export interface IStorage {
  getUser(id: string): Promise<User | undefined>;
  getUserByUsername(username: string): Promise<User | undefined>;
  createUser(user: InsertUser): Promise<User>;
  getSubscriberByEmail(email: string): Promise<Subscriber | undefined>;
  createSubscriber(subscriber: InsertSubscriber): Promise<Subscriber>;
  getConversation(id: string): Promise<ChatConversation | undefined>;
  getAllConversations(): Promise<ChatConversation[]>;
  createConversation(title: string): Promise<ChatConversation>;
  deleteConversation(id: string): Promise<void>;
  addMessage(conversationId: string, role: "user" | "assistant" | "system", content: string): Promise<ChatMessage>;
  getMessages(conversationId: string): Promise<ChatMessage[]>;
  storeMetricMemory(conversationId: string, messageId: string, embedding: number[], complexityXi: number): Promise<void>;
}

export class DatabaseStorage implements IStorage {
  async getUser(id: string): Promise<User | undefined> {
    const [user] = await db.select().from(users).where(eq(users.id, id));
    return user || undefined;
  }

  async getUserByUsername(username: string): Promise<User | undefined> {
    const [user] = await db.select().from(users).where(eq(users.username, username));
    return user || undefined;
  }

  async createUser(insertUser: InsertUser): Promise<User> {
    const [user] = await db.insert(users).values(insertUser).returning();
    return user;
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

  async createConversation(title: string): Promise<ChatConversation> {
    const [conversation] = await db.insert(conversations).values({ title }).returning();
    return {
      id: conversation.id,
      title: conversation.title,
      createdAt: conversation.createdAt.toISOString(),
      messages: [],
    };
  }

  async deleteConversation(id: string): Promise<void> {
    await db.delete(conversations).where(eq(conversations.id, id));
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
}

export const storage = new DatabaseStorage();
