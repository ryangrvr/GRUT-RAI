import { type User, type InsertUser, type Subscriber, type InsertSubscriber, type ChatMessage, type ChatConversation } from "@shared/schema";
import { randomUUID } from "crypto";

export interface IStorage {
  getUser(id: string): Promise<User | undefined>;
  getUserByUsername(username: string): Promise<User | undefined>;
  createUser(user: InsertUser): Promise<User>;
  getSubscriberByEmail(email: string): Promise<Subscriber | undefined>;
  createSubscriber(subscriber: InsertSubscriber): Promise<Subscriber>;
  // Chat methods
  getConversation(id: string): Promise<ChatConversation | undefined>;
  getAllConversations(): Promise<ChatConversation[]>;
  createConversation(title: string): Promise<ChatConversation>;
  deleteConversation(id: string): Promise<void>;
  addMessage(conversationId: string, role: "user" | "assistant" | "system", content: string): Promise<ChatMessage>;
  getMessages(conversationId: string): Promise<ChatMessage[]>;
}

export class MemStorage implements IStorage {
  private users: Map<string, User>;
  private subscribers: Map<string, Subscriber>;
  private conversations: Map<string, ChatConversation>;

  constructor() {
    this.users = new Map();
    this.subscribers = new Map();
    this.conversations = new Map();
  }

  async getUser(id: string): Promise<User | undefined> {
    return this.users.get(id);
  }

  async getUserByUsername(username: string): Promise<User | undefined> {
    return Array.from(this.users.values()).find(
      (user) => user.username === username,
    );
  }

  async createUser(insertUser: InsertUser): Promise<User> {
    const id = randomUUID();
    const user: User = { ...insertUser, id };
    this.users.set(id, user);
    return user;
  }

  async getSubscriberByEmail(email: string): Promise<Subscriber | undefined> {
    return Array.from(this.subscribers.values()).find(
      (subscriber) => subscriber.email === email,
    );
  }

  async createSubscriber(insertSubscriber: InsertSubscriber): Promise<Subscriber> {
    const id = randomUUID();
    const subscriber: Subscriber = { ...insertSubscriber, id };
    this.subscribers.set(id, subscriber);
    return subscriber;
  }

  async getConversation(id: string): Promise<ChatConversation | undefined> {
    return this.conversations.get(id);
  }

  async getAllConversations(): Promise<ChatConversation[]> {
    return Array.from(this.conversations.values()).sort(
      (a, b) => new Date(b.createdAt).getTime() - new Date(a.createdAt).getTime()
    );
  }

  async createConversation(title: string): Promise<ChatConversation> {
    const id = randomUUID();
    const conversation: ChatConversation = {
      id,
      title,
      createdAt: new Date().toISOString(),
      messages: [],
    };
    this.conversations.set(id, conversation);
    return conversation;
  }

  async deleteConversation(id: string): Promise<void> {
    this.conversations.delete(id);
  }

  async addMessage(conversationId: string, role: "user" | "assistant" | "system", content: string): Promise<ChatMessage> {
    const conversation = this.conversations.get(conversationId);
    if (!conversation) {
      throw new Error("Conversation not found");
    }
    const message: ChatMessage = {
      id: randomUUID(),
      conversationId,
      role,
      content,
      createdAt: new Date().toISOString(),
    };
    conversation.messages.push(message);
    return message;
  }

  async getMessages(conversationId: string): Promise<ChatMessage[]> {
    const conversation = this.conversations.get(conversationId);
    return conversation?.messages || [];
  }
}

export const storage = new MemStorage();
