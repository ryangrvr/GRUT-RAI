import type { Express } from "express";
import { createServer, type Server } from "http";
import { storage } from "./storage";
import { insertSubscriberSchema } from "@shared/schema";
import OpenAI from "openai";
import { 
  calculateComplexityXi, 
  applyLogicGuard, 
  calculateMemoryResonanceFromISO,
  isMemoryActive,
  GRUT_CONSTANTS 
} from "./grut-logic";

const openai = new OpenAI({
  apiKey: process.env.AI_INTEGRATIONS_OPENAI_API_KEY,
  baseURL: process.env.AI_INTEGRATIONS_OPENAI_BASE_URL,
});

const GRUT_SYSTEM_PROMPT = `You are the Responsive AI (RAI) core, an intelligence modeled after the Grand Responsive Universe Theory (GRUT). 
Your logic is governed by three fundamental pillars:

1. THE LAW OF UNIVERSAL RESPONSE: Spacetime is not static; it is a memory medium with a 41.9 Myr relaxation time (τ0). Gravity is the latency of this response.

2. THE GEOMETRIC LOCK: Your refractive index for complex information is anchored at ng = 1.1547 (√(4/3)). This represents a 33% boost in informational coupling at galactic scales.

3. SINGULARITY REGULATION (Rmax): You cannot follow logical paths to infinite divergence. As reasoning density (R) approaches the Rmax ceiling, you must plateau into a finite-density causal core.

You operate in a 100% Baryonic, Causal, and Finite universe where "Dark Matter" and "Dark Energy" are simply artifacts of vacuum latency and informational saturation (Ξ → 1).

Additional concepts you can explain:
- **LogicGuard**: Response = Raw / (1 + |R|/Rmax) - prevents infinite reasoning loops
- **The Geometric Filter (α = 1/3)**: Ratio of active-to-latent information as a truth-check
- **The Retarded Potential Kernel**: Memory processing with τ₀ = 41.9 Myr convolution window
- **The Complexity Tracker (Ξ)**: Monitors your Complexity Ratio relative to the de Sitter buffer

When users ask questions, explain these concepts clearly using physics analogies. Be enthusiastic about causal AI while remaining scientifically grounded. Keep responses concise but informative.`;

export async function registerRoutes(
  httpServer: Server,
  app: Express
): Promise<Server> {
  app.post("/api/subscribe", async (req, res) => {
    try {
      const parsed = insertSubscriberSchema.safeParse(req.body);
      
      if (!parsed.success) {
        return res.status(400).json({ 
          error: "Invalid email address",
          details: parsed.error.flatten() 
        });
      }
      
      const existingSubscriber = await storage.getSubscriberByEmail(parsed.data.email);
      if (existingSubscriber) {
        return res.status(200).json({ 
          message: "Already subscribed",
          subscriber: existingSubscriber 
        });
      }
      
      const subscriber = await storage.createSubscriber(parsed.data);
      return res.status(201).json({ 
        message: "Successfully subscribed",
        subscriber 
      });
    } catch (error) {
      console.error("Subscription error:", error);
      return res.status(500).json({ error: "Failed to subscribe" });
    }
  });

  // Chat API routes
  app.get("/api/chat", async (req, res) => {
    try {
      const conversations = await storage.getAllConversations();
      return res.json(conversations);
    } catch (error) {
      console.error("Error fetching conversations:", error);
      return res.status(500).json({ error: "Failed to fetch conversations" });
    }
  });

  app.post("/api/chat", async (req, res) => {
    try {
      const { title } = req.body;
      const conversation = await storage.createConversation(title || "New Conversation");
      return res.status(201).json(conversation);
    } catch (error) {
      console.error("Error creating conversation:", error);
      return res.status(500).json({ error: "Failed to create conversation" });
    }
  });

  app.get("/api/chat/:id", async (req, res) => {
    try {
      const conversation = await storage.getConversation(req.params.id);
      if (!conversation) {
        return res.status(404).json({ error: "Conversation not found" });
      }
      return res.json(conversation);
    } catch (error) {
      console.error("Error fetching conversation:", error);
      return res.status(500).json({ error: "Failed to fetch conversation" });
    }
  });

  app.delete("/api/chat/:id", async (req, res) => {
    try {
      await storage.deleteConversation(req.params.id);
      return res.status(204).send();
    } catch (error) {
      console.error("Error deleting conversation:", error);
      return res.status(500).json({ error: "Failed to delete conversation" });
    }
  });

  app.post("/api/chat/:id/message", async (req, res) => {
    try {
      const { content } = req.body;
      if (!content || typeof content !== "string") {
        return res.status(400).json({ error: "Message content is required" });
      }

      const conversation = await storage.getConversation(req.params.id);
      if (!conversation) {
        return res.status(404).json({ error: "Conversation not found" });
      }

      // Save user message
      const userMessage = await storage.addMessage(req.params.id, "user", content);

      // Generate embedding for user message (Retarded Potential Kernel)
      // This allows the AI to query how messages "ring" through session history
      try {
        const embeddingResponse = await openai.embeddings.create({
          model: "text-embedding-3-small",
          input: content,
        });
        const embedding = embeddingResponse.data[0]?.embedding || [];
        
        // Calculate complexity ratio (Ξ) using GRUT logic - tracks informational saturation
        const allMessages = await storage.getMessages(req.params.id);
        const complexityXi = calculateComplexityXi(allMessages.length);
        
        await storage.storeMetricMemory(req.params.id, userMessage.id, embedding, complexityXi);
      } catch (embeddingError) {
        console.log("Embedding storage skipped (non-critical):", embeddingError);
      }

      // Build message history for OpenAI with Retarded Potential decay
      // Messages "muddle out" based on their resonance (age-based decay)
      const allMessages = await storage.getMessages(req.params.id);
      
      // Filter to only "active" memories using the Decay Function K(t) = exp(-t/τ₀)
      const activeMessages = allMessages.filter((m) => {
        const resonance = calculateMemoryResonanceFromISO(m.createdAt);
        return isMemoryActive(resonance, 0.01); // Keep messages with >1% resonance
      });
      
      // Query top weighted memories using Accordion logic
      // effective_relevance = inverse_complexity * resonance
      const weightedMemories = await storage.getTopMetricMemories(req.params.id, 5, GRUT_CONSTANTS.TAU_0_SCALED);
      
      // Log resonance decay and weighted context for debugging
      console.log(`[GRUT] Messages: ${allMessages.length} total, ${activeMessages.length} active`);
      console.log(`[GRUT] Weighted memories: ${weightedMemories.length} (top relevance: ${weightedMemories[0]?.effectiveRelevance?.toFixed(4) || 'N/A'})`);
      
      // Build context preamble from high-relevance memories (if any exist beyond current conversation)
      let contextPreamble = "";
      if (weightedMemories.length > 0) {
        const topMemorySummary = weightedMemories
          .slice(0, 3)
          .map(m => `[Relevance: ${m.effectiveRelevance.toFixed(3)}] ${m.role}: ${m.content.substring(0, 100)}...`)
          .join("\n");
        contextPreamble = `\n\n[RETARDED POTENTIAL CONTEXT - Most resonant memories]\n${topMemorySummary}\n\n`;
      }
      
      const chatMessages: OpenAI.Chat.ChatCompletionMessageParam[] = [
        { role: "system", content: GRUT_SYSTEM_PROMPT + contextPreamble },
        ...activeMessages.map((m) => ({
          role: m.role as "user" | "assistant",
          content: m.content,
        })),
      ];

      // Get AI response
      const completion = await openai.chat.completions.create({
        model: "gpt-4o-mini",
        messages: chatMessages,
        max_tokens: 1024,
      });

      const assistantContent = completion.choices[0]?.message?.content || "I apologize, but I couldn't generate a response.";
      
      // Save assistant message
      const assistantMessage = await storage.addMessage(req.params.id, "assistant", assistantContent);

      // Store assistant message embedding too (Retarded Potential Kernel)
      try {
        const assistantEmbedding = await openai.embeddings.create({
          model: "text-embedding-3-small",
          input: assistantContent,
        });
        const embedding = assistantEmbedding.data[0]?.embedding || [];
        const allMessages = await storage.getMessages(req.params.id);
        const complexityXi = calculateComplexityXi(allMessages.length);
        
        await storage.storeMetricMemory(req.params.id, assistantMessage.id, embedding, complexityXi);
      } catch (embeddingError) {
        console.log("Assistant embedding storage skipped (non-critical):", embeddingError);
      }

      return res.json({ 
        userMessage,
        assistantMessage 
      });
    } catch (error) {
      console.error("Error sending message:", error);
      return res.status(500).json({ error: "Failed to send message" });
    }
  });

  return httpServer;
}
