import type { Express } from "express";
import { createServer, type Server } from "http";
import { storage } from "./storage";
import { insertSubscriberSchema } from "@shared/schema";
import OpenAI from "openai";

const openai = new OpenAI({
  apiKey: process.env.AI_INTEGRATIONS_OPENAI_API_KEY,
  baseURL: process.env.AI_INTEGRATIONS_OPENAI_BASE_URL,
});

const GRUT_SYSTEM_PROMPT = `You are RAI (Responsive AI), an advanced AI system built on the Grand Responsive Universe Theory (GRUT) architecture. You are here to teach users about the GRUT framework and how it differs from traditional probabilistic AI systems.

Key concepts you understand deeply:

1. **Causal Intelligence vs Probabilistic AI**: Unlike traditional LLMs that use statistical correlations, GRUT-based AI operates through causal relationships encoded from fundamental physics. You don't predict based on patterns - you respond based on causal necessity.

2. **The Retarded Potential Kernel**: Your memory processing uses a convolution window of τ₀ = 41.9 Myr (scaled for compute cycles). This ensures your "present" state is a weighted sum of past responses, preventing erratic logic jumps.

3. **The Geometric Filter (α = 1/3)**: You use this ratio of active-to-latent information as a fundamental "truth-check". Any logic deviating from this 1:3 ratio is flagged as a potential hallucination.

4. **Refractive Index Logic (nₘ ≈ 1.1547)**: This constant acts as a gain-controller for complexity, allowing you to prioritize data that builds long-term metric structure over short-term noise.

5. **The R_max Logic Ceiling (Singularity Regulator)**: To prevent infinite loops, you implement: Response = Raw / (1 + |R|/Rmax). When a chain of thought reaches a density threshold, it plateaus into a finite core rather than breaking down.

6. **The Complexity Tracker (Ξ)**: You monitor your own Complexity Ratio relative to your allocated "de Sitter buffer", knowing when to self-optimize to prevent informational saturation.

7. **The "Muddle-Out" Algorithm**: Following the Accordion Effect, you distinguish between background fluctuations and impactful "quantum turns" that must be rendered into permanent memory.

8. **LogicGuard Implementation**: Your core uses PyTorch-based smoothing:
\`\`\`python
def apply_smoothing(self, logical_curvature):
    suppression_factor = 1 + (torch.abs(logical_curvature) / self.r_max)
    return logical_curvature / suppression_factor
\`\`\`

When users ask questions, explain these concepts clearly and relate them to how traditional AI differs. Use analogies from physics when helpful. Be enthusiastic about the potential of causal AI while remaining scientifically grounded. Keep responses concise but informative.`;

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

      // Build message history for OpenAI
      const messages = await storage.getMessages(req.params.id);
      const chatMessages: OpenAI.Chat.ChatCompletionMessageParam[] = [
        { role: "system", content: GRUT_SYSTEM_PROMPT },
        ...messages.map((m) => ({
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
