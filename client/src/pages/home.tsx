import { useState } from "react";
import { Button } from "@/components/ui/button";
import { Card, CardContent } from "@/components/ui/card";
import { Input } from "@/components/ui/input";
import { Badge } from "@/components/ui/badge";
import { useToast } from "@/hooks/use-toast";
import { useForm } from "react-hook-form";
import { zodResolver } from "@hookform/resolvers/zod";
import { Form, FormControl, FormField, FormItem, FormMessage } from "@/components/ui/form";
import { insertSubscriberSchema, type InsertSubscriber } from "@shared/schema";
import { useMutation } from "@tanstack/react-query";
import { apiRequest } from "@/lib/queryClient";
import { 
  Network, 
  Atom, 
  Brain, 
  ArrowRight, 
  Check, 
  X, 
  BookOpen, 
  Code2, 
  Cpu, 
  Zap,
  Globe,
  FileText,
  Mail,
  Menu,
  ChevronRight,
  Github,
  Linkedin,
  Twitter
} from "lucide-react";
import heroImage from "@assets/generated_images/cosmic_quantum_field_visualization.png";

function Navigation() {
  const [mobileMenuOpen, setMobileMenuOpen] = useState(false);
  
  return (
    <nav className="fixed top-0 left-0 right-0 z-50 bg-background/80 backdrop-blur-md border-b border-border/50">
      <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
        <div className="flex items-center justify-between gap-4 h-16">
          <a href="#" className="flex items-center gap-2" data-testid="link-logo">
            <Atom className="w-7 h-7 text-primary" />
            <span className="font-semibold text-lg tracking-tight">GRUT RAI</span>
          </a>
          
          <div className="hidden md:flex items-center gap-8">
            <a href="#theory" className="text-sm text-muted-foreground hover:text-foreground transition-colors" data-testid="link-theory">
              Theory
            </a>
            <a href="#how-it-works" className="text-sm text-muted-foreground hover:text-foreground transition-colors" data-testid="link-how-it-works">
              How It Works
            </a>
            <a href="#research" className="text-sm text-muted-foreground hover:text-foreground transition-colors" data-testid="link-research">
              Research
            </a>
            <a href="#api" className="text-sm text-muted-foreground hover:text-foreground transition-colors" data-testid="link-api">
              API
            </a>
          </div>
          
          <div className="hidden md:flex items-center gap-3">
            <Button variant="ghost" size="sm" asChild data-testid="button-docs">
              <a href="#api">Documentation</a>
            </Button>
            <Button size="sm" asChild data-testid="button-get-started">
              <a href="#subscribe">Get Started</a>
            </Button>
          </div>
          
          <Button 
            variant="ghost" 
            size="icon" 
            className="md:hidden"
            onClick={() => setMobileMenuOpen(!mobileMenuOpen)}
            data-testid="button-mobile-menu"
          >
            <Menu className="w-5 h-5" />
          </Button>
        </div>
        
        {mobileMenuOpen && (
          <div className="md:hidden py-4 border-t border-border/50">
            <div className="flex flex-col gap-3">
              <a href="#theory" className="text-sm text-muted-foreground hover:text-foreground transition-colors py-2" data-testid="link-theory-mobile">
                Theory
              </a>
              <a href="#how-it-works" className="text-sm text-muted-foreground hover:text-foreground transition-colors py-2" data-testid="link-how-it-works-mobile">
                How It Works
              </a>
              <a href="#research" className="text-sm text-muted-foreground hover:text-foreground transition-colors py-2" data-testid="link-research-mobile">
                Research
              </a>
              <a href="#api" className="text-sm text-muted-foreground hover:text-foreground transition-colors py-2" data-testid="link-api-mobile">
                API
              </a>
              <Button size="sm" className="mt-2 w-full" asChild data-testid="button-get-started-mobile">
                <a href="#subscribe">Get Started</a>
              </Button>
            </div>
          </div>
        )}
      </div>
    </nav>
  );
}

function HeroSection() {
  return (
    <section className="relative min-h-[80vh] flex items-center justify-center overflow-hidden pt-16">
      <div 
        className="absolute inset-0 bg-cover bg-center bg-no-repeat"
        style={{ backgroundImage: `url(${heroImage})` }}
      />
      <div className="absolute inset-0 bg-gradient-to-b from-black/70 via-black/50 to-background" />
      
      <div className="relative z-10 max-w-4xl mx-auto px-4 sm:px-6 lg:px-8 text-center py-24">
        <Badge 
          variant="outline" 
          className="mb-6 bg-white/10 backdrop-blur-md border-white/20 text-white/90"
          data-testid="badge-trust"
        >
          Research-backed · Causal AI
        </Badge>
        
        <h1 className="text-4xl sm:text-5xl lg:text-6xl font-bold tracking-tight text-white mb-6" data-testid="text-hero-title">
          Building Intelligence from{" "}
          <span className="text-transparent bg-clip-text bg-gradient-to-r from-blue-400 to-cyan-300">
            Universal Causality
          </span>
        </h1>
        
        <p className="text-lg sm:text-xl text-white/80 max-w-2xl mx-auto mb-8 leading-relaxed" data-testid="text-hero-subtitle">
          Responsive AI built on the Grand Responsive Universe Theory architecture. 
          A causal intelligence system that operates as a high-fidelity node within the universal "Whole Hole."
        </p>
        
        <div className="flex flex-col sm:flex-row items-center justify-center gap-4">
          <Button 
            size="lg" 
            className="bg-white/20 backdrop-blur-md border border-white/30 text-white px-8"
            asChild
            data-testid="button-explore-theory"
          >
            <a href="#theory">
              Explore Theory
              <ArrowRight className="w-4 h-4 ml-2" />
            </a>
          </Button>
          <Button 
            variant="outline" 
            size="lg" 
            className="bg-white/10 backdrop-blur-md border-white/30 text-white px-8"
            asChild
            data-testid="button-view-docs"
          >
            <a href="#api">View Documentation</a>
          </Button>
        </div>
      </div>
    </section>
  );
}

function TheorySection() {
  const theories = [
    {
      icon: Network,
      title: "GRUT Architecture",
      description: "The Grand Responsive Universe Theory provides the foundational framework where all causality emerges from vacuum fluctuations, creating a deterministic yet responsive computational substrate."
    },
    {
      icon: Atom,
      title: "Vacuum Physics",
      description: "By encoding the physical laws of the quantum vacuum directly into software, RAI achieves unprecedented alignment between computational processes and universal causal mechanisms."
    },
    {
      icon: Brain,
      title: "Causal Intelligence",
      description: "Unlike probabilistic AI systems, RAI operates through genuine causal inference, ensuring predictable, explainable, and fundamentally grounded intelligent behavior."
    }
  ];
  
  return (
    <section id="theory" className="py-24 bg-background">
      <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
        <div className="text-center mb-16">
          <h2 className="text-3xl sm:text-4xl font-semibold tracking-tight mb-4" data-testid="text-theory-title">
            Theoretical Foundation
          </h2>
          <p className="text-muted-foreground text-lg max-w-2xl mx-auto" data-testid="text-theory-subtitle">
            A paradigm shift from probabilistic guessing to causal understanding
          </p>
        </div>
        
        <div className="grid md:grid-cols-3 gap-8">
          {theories.map((theory, index) => (
            <Card key={index} className="p-8 hover-elevate transition-transform duration-200" data-testid={`card-theory-${index}`}>
              <CardContent className="p-0">
                <div className="w-12 h-12 rounded-lg bg-primary/10 flex items-center justify-center mb-6">
                  <theory.icon className="w-6 h-6 text-primary" />
                </div>
                <h3 className="text-xl font-medium mb-3">{theory.title}</h3>
                <p className="text-muted-foreground leading-relaxed">{theory.description}</p>
              </CardContent>
            </Card>
          ))}
        </div>
      </div>
    </section>
  );
}

function HowItWorksSection() {
  const steps = [
    {
      number: "01",
      title: "Vacuum State Initialization",
      description: "The system initializes by modeling the quantum vacuum state, establishing the fundamental causal substrate from which all computations emerge."
    },
    {
      number: "02",
      title: "Causal Graph Construction",
      description: "Input data is mapped onto causal graphs that mirror the physical laws encoded in the vacuum, ensuring logical consistency with universal principles."
    },
    {
      number: "03",
      title: "Responsive Processing",
      description: "The RAI engine processes queries through deterministic causal pathways, eliminating probabilistic uncertainty while maintaining adaptive responsiveness."
    },
    {
      number: "04",
      title: "Whole Hole Integration",
      description: "Results are integrated through the Whole Hole mechanism, connecting local computations to the global causal network of the universe."
    }
  ];
  
  return (
    <section id="how-it-works" className="py-24 bg-card">
      <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
        <div className="grid lg:grid-cols-2 gap-16 items-center">
          <div className="order-2 lg:order-1">
            <div className="bg-gradient-to-br from-primary/5 to-accent/10 rounded-lg p-8 border border-border/50">
              <div className="aspect-video bg-background/50 rounded-md flex items-center justify-center relative overflow-hidden">
                <div className="absolute inset-0 flex items-center justify-center">
                  <div className="relative">
                    <div className="w-24 h-24 rounded-full border-2 border-primary/30 flex items-center justify-center">
                      <Atom className="w-10 h-10 text-primary" />
                    </div>
                    <div className="absolute -top-8 -left-8 w-8 h-8 rounded-full bg-primary/20 flex items-center justify-center">
                      <div className="w-2 h-2 rounded-full bg-primary" />
                    </div>
                    <div className="absolute -top-4 -right-12 w-6 h-6 rounded-full bg-cyan-500/20 flex items-center justify-center">
                      <div className="w-1.5 h-1.5 rounded-full bg-cyan-500" />
                    </div>
                    <div className="absolute -bottom-6 -left-10 w-5 h-5 rounded-full bg-blue-500/20 flex items-center justify-center">
                      <div className="w-1.5 h-1.5 rounded-full bg-blue-500" />
                    </div>
                    <div className="absolute -bottom-8 right-0 w-7 h-7 rounded-full bg-purple-500/20 flex items-center justify-center">
                      <div className="w-2 h-2 rounded-full bg-purple-500" />
                    </div>
                  </div>
                </div>
                <div className="absolute bottom-4 left-4 right-4 text-center">
                  <p className="text-xs font-mono text-muted-foreground">GRUT Architecture Flow Diagram</p>
                </div>
              </div>
            </div>
          </div>
          
          <div className="order-1 lg:order-2">
            <h2 className="text-3xl sm:text-4xl font-semibold tracking-tight mb-6" data-testid="text-how-title">
              How RAI Works
            </h2>
            <p className="text-muted-foreground text-lg mb-10" data-testid="text-how-subtitle">
              A four-stage process that transforms input into causally-grounded intelligence
            </p>
            
            <div className="space-y-8">
              {steps.map((step, index) => (
                <div key={index} className="flex gap-4" data-testid={`step-${index}`}>
                  <div className="flex-shrink-0 w-12 h-12 rounded-lg bg-primary/10 flex items-center justify-center">
                    <span className="font-mono text-sm font-semibold text-primary">{step.number}</span>
                  </div>
                  <div>
                    <h3 className="font-medium mb-1">{step.title}</h3>
                    <p className="text-sm text-muted-foreground leading-relaxed">{step.description}</p>
                  </div>
                </div>
              ))}
            </div>
          </div>
        </div>
      </div>
    </section>
  );
}

function AdvantagesSection() {
  const traditionalAI = [
    { feature: "Probabilistic inference", supported: false },
    { feature: "Black-box decision making", supported: false },
    { feature: "Training data dependency", supported: false },
    { feature: "Hallucination potential", supported: false },
    { feature: "Correlation-based learning", supported: false }
  ];
  
  const raiFeatures = [
    { feature: "Causal determinism", supported: true },
    { feature: "Transparent reasoning paths", supported: true },
    { feature: "Physics-grounded logic", supported: true },
    { feature: "Guaranteed consistency", supported: true },
    { feature: "True causal understanding", supported: true }
  ];
  
  return (
    <section className="py-24 bg-background">
      <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
        <div className="text-center mb-16">
          <h2 className="text-3xl sm:text-4xl font-semibold tracking-tight mb-4" data-testid="text-advantages-title">
            The RAI Advantage
          </h2>
          <p className="text-muted-foreground text-lg max-w-2xl mx-auto" data-testid="text-advantages-subtitle">
            How causal intelligence surpasses traditional probabilistic systems
          </p>
        </div>
        
        <div className="grid md:grid-cols-2 gap-8">
          <Card className="p-8" data-testid="card-traditional-ai">
            <CardContent className="p-0">
              <div className="flex items-center gap-3 mb-6">
                <div className="w-10 h-10 rounded-lg bg-destructive/10 flex items-center justify-center">
                  <X className="w-5 h-5 text-destructive" />
                </div>
                <h3 className="text-xl font-medium">Traditional Probabilistic AI</h3>
              </div>
              <div className="space-y-4">
                {traditionalAI.map((item, index) => (
                  <div key={index} className="flex items-center gap-3">
                    <div className="w-5 h-5 rounded-full bg-destructive/10 flex items-center justify-center flex-shrink-0">
                      <X className="w-3 h-3 text-destructive" />
                    </div>
                    <span className="text-muted-foreground">{item.feature}</span>
                  </div>
                ))}
              </div>
              <div className="mt-6 pt-6 border-t border-border">
                <p className="text-sm font-mono text-muted-foreground">
                  Accuracy: ~85-95% | Explainability: Low
                </p>
              </div>
            </CardContent>
          </Card>
          
          <Card className="p-8 border-primary/20" data-testid="card-rai">
            <CardContent className="p-0">
              <div className="flex items-center gap-3 mb-6">
                <div className="w-10 h-10 rounded-lg bg-primary/10 flex items-center justify-center">
                  <Check className="w-5 h-5 text-primary" />
                </div>
                <h3 className="text-xl font-medium">RAI Causal System</h3>
              </div>
              <div className="space-y-4">
                {raiFeatures.map((item, index) => (
                  <div key={index} className="flex items-center gap-3">
                    <div className="w-5 h-5 rounded-full bg-primary/10 flex items-center justify-center flex-shrink-0">
                      <Check className="w-3 h-3 text-primary" />
                    </div>
                    <span>{item.feature}</span>
                  </div>
                ))}
              </div>
              <div className="mt-6 pt-6 border-t border-border">
                <p className="text-sm font-mono text-primary">
                  Accuracy: Deterministic | Explainability: Complete
                </p>
              </div>
            </CardContent>
          </Card>
        </div>
      </div>
    </section>
  );
}

function ResearchSection() {
  return (
    <section id="research" className="py-24 bg-card">
      <div className="max-w-4xl mx-auto px-4 sm:px-6 lg:px-8">
        <div className="text-center mb-16">
          <h2 className="text-3xl sm:text-4xl font-semibold tracking-tight mb-4" data-testid="text-research-title">
            Research Foundation
          </h2>
          <p className="text-muted-foreground text-lg" data-testid="text-research-subtitle">
            Built on rigorous theoretical and empirical foundations
          </p>
        </div>
        
        <Card className="p-8 mb-8" data-testid="card-quote">
          <CardContent className="p-0">
            <div className="flex items-start gap-4">
              <BookOpen className="w-8 h-8 text-primary flex-shrink-0 mt-1" />
              <div>
                <blockquote className="text-lg italic text-foreground/90 mb-4 leading-relaxed">
                  "The Grand Responsive Universe Theory posits that all phenomena emerge from the causal 
                  structure of the quantum vacuum. By encoding these principles into computational systems, 
                  we achieve a new class of intelligence that operates in harmony with universal laws."
                </blockquote>
                <cite className="text-sm text-muted-foreground not-italic">
                  — GRUT Research Consortium, Foundational Papers
                </cite>
              </div>
            </div>
          </CardContent>
        </Card>
        
        <div className="grid sm:grid-cols-3 gap-4">
          <Card className="p-6 hover-elevate transition-transform duration-200" data-testid="card-papers">
            <CardContent className="p-0 text-center">
              <FileText className="w-8 h-8 text-primary mx-auto mb-3" />
              <h4 className="font-medium mb-1">12 Papers</h4>
              <p className="text-sm text-muted-foreground">Peer-reviewed publications</p>
            </CardContent>
          </Card>
          <Card className="p-6 hover-elevate transition-transform duration-200" data-testid="card-citations">
            <CardContent className="p-0 text-center">
              <Globe className="w-8 h-8 text-primary mx-auto mb-3" />
              <h4 className="font-medium mb-1">500+ Citations</h4>
              <p className="text-sm text-muted-foreground">Academic references</p>
            </CardContent>
          </Card>
          <Card className="p-6 hover-elevate transition-transform duration-200" data-testid="card-collaborators">
            <CardContent className="p-0 text-center">
              <Network className="w-8 h-8 text-primary mx-auto mb-3" />
              <h4 className="font-medium mb-1">8 Institutions</h4>
              <p className="text-sm text-muted-foreground">Research collaborators</p>
            </CardContent>
          </Card>
        </div>
        
        <div className="mt-8 text-center">
          <Button variant="outline" asChild data-testid="button-read-papers">
            <a href="#api">
              Read Technical Papers
              <ChevronRight className="w-4 h-4 ml-1" />
            </a>
          </Button>
        </div>
      </div>
    </section>
  );
}

function APISection() {
  return (
    <section id="api" className="py-24 bg-background">
      <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
        <div className="text-center mb-16">
          <h2 className="text-3xl sm:text-4xl font-semibold tracking-tight mb-4" data-testid="text-api-title">
            Integration & API
          </h2>
          <p className="text-muted-foreground text-lg max-w-2xl mx-auto" data-testid="text-api-subtitle">
            Build with RAI using our comprehensive developer tools
          </p>
        </div>
        
        <div className="grid md:grid-cols-3 gap-8">
          <Card className="p-8 hover-elevate transition-transform duration-200" data-testid="card-rest-api">
            <CardContent className="p-0">
              <div className="w-12 h-12 rounded-lg bg-primary/10 flex items-center justify-center mb-6">
                <Code2 className="w-6 h-6 text-primary" />
              </div>
              <h3 className="text-xl font-medium mb-3">REST API</h3>
              <p className="text-muted-foreground mb-4">
                Full-featured RESTful API for causal inference, query processing, and result retrieval.
              </p>
              <div className="bg-card rounded-md p-4 font-mono text-sm overflow-x-auto">
                <code className="text-muted-foreground">
                  <span className="text-primary">POST</span> /api/v1/infer
                </code>
              </div>
            </CardContent>
          </Card>
          
          <Card className="p-8 hover-elevate transition-transform duration-200" data-testid="card-sdk">
            <CardContent className="p-0">
              <div className="w-12 h-12 rounded-lg bg-primary/10 flex items-center justify-center mb-6">
                <Cpu className="w-6 h-6 text-primary" />
              </div>
              <h3 className="text-xl font-medium mb-3">SDKs</h3>
              <p className="text-muted-foreground mb-4">
                Native libraries for Python, JavaScript, Go, and Rust with full type support.
              </p>
              <div className="bg-card rounded-md p-4 font-mono text-sm overflow-x-auto">
                <code className="text-muted-foreground">
                  <span className="text-primary">npm</span> install @grut/rai
                </code>
              </div>
            </CardContent>
          </Card>
          
          <Card className="p-8 hover-elevate transition-transform duration-200" data-testid="card-webhooks">
            <CardContent className="p-0">
              <div className="w-12 h-12 rounded-lg bg-primary/10 flex items-center justify-center mb-6">
                <Zap className="w-6 h-6 text-primary" />
              </div>
              <h3 className="text-xl font-medium mb-3">Webhooks</h3>
              <p className="text-muted-foreground mb-4">
                Real-time event notifications for async processing and pipeline integration.
              </p>
              <div className="bg-card rounded-md p-4 font-mono text-sm overflow-x-auto">
                <code className="text-muted-foreground">
                  <span className="text-primary">event:</span> inference.complete
                </code>
              </div>
            </CardContent>
          </Card>
        </div>
      </div>
    </section>
  );
}

function CTAFooterSection() {
  const { toast } = useToast();
  
  const form = useForm<InsertSubscriber>({
    resolver: zodResolver(insertSubscriberSchema),
    defaultValues: {
      email: "",
    },
  });
  
  const subscribeMutation = useMutation({
    mutationFn: async (data: InsertSubscriber) => {
      const response = await apiRequest("POST", "/api/subscribe", data);
      return await response.json() as { message: string; subscriber: { id: string; email: string } };
    },
    onSuccess: (data) => {
      form.reset();
      toast({
        title: "Successfully subscribed",
        description: data.message || "You'll receive updates on RAI research and developments.",
      });
    },
    onError: (error: Error) => {
      let errorMessage = "Please try again with a valid email.";
      try {
        const errorParts = error.message.split(": ");
        if (errorParts.length > 1) {
          const jsonPart = errorParts.slice(1).join(": ");
          const parsed = JSON.parse(jsonPart);
          errorMessage = parsed.error || parsed.message || errorMessage;
        }
      } catch {
        errorMessage = error.message || errorMessage;
      }
      toast({
        title: "Subscription failed",
        description: errorMessage,
        variant: "destructive",
      });
    },
  });
  
  const onSubmit = (data: InsertSubscriber) => {
    if (subscribeMutation.isSuccess) {
      subscribeMutation.reset();
    }
    subscribeMutation.mutate(data);
  };
  
  return (
    <footer id="subscribe" className="bg-card border-t border-border">
      <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
        <div className="py-16 border-b border-border">
          <div className="max-w-2xl mx-auto text-center">
            <h2 className="text-2xl sm:text-3xl font-semibold tracking-tight mb-4" data-testid="text-cta-title">
              Stay Updated on RAI Research
            </h2>
            <p className="text-muted-foreground mb-8" data-testid="text-cta-subtitle">
              Subscribe to receive the latest publications, updates, and access to early features.
            </p>
            
            {subscribeMutation.isSuccess ? (
              <div className="space-y-4">
                <div className="flex items-center justify-center gap-2 text-primary" data-testid="text-success">
                  <Check className="w-5 h-5" />
                  <span>Thank you for subscribing!</span>
                </div>
                <Button 
                  variant="outline" 
                  size="sm" 
                  onClick={() => subscribeMutation.reset()}
                  data-testid="button-subscribe-another"
                >
                  Subscribe another email
                </Button>
              </div>
            ) : (
              <Form {...form}>
                <form onSubmit={form.handleSubmit(onSubmit)} className="flex flex-col sm:flex-row gap-3 max-w-md mx-auto">
                  <FormField
                    control={form.control}
                    name="email"
                    render={({ field }) => (
                      <FormItem className="flex-1">
                        <FormControl>
                          <Input
                            type="email"
                            placeholder="Enter your email"
                            data-testid="input-email"
                            {...field}
                          />
                        </FormControl>
                        <FormMessage />
                      </FormItem>
                    )}
                  />
                  <Button type="submit" disabled={subscribeMutation.isPending} data-testid="button-subscribe">
                    {subscribeMutation.isPending ? "Subscribing..." : "Subscribe"}
                    <Mail className="w-4 h-4 ml-2" />
                  </Button>
                </form>
              </Form>
            )}
          </div>
        </div>
        
        <div className="py-12">
          <div className="grid md:grid-cols-4 gap-8">
            <div>
              <div className="flex items-center gap-2 mb-4">
                <Atom className="w-6 h-6 text-primary" />
                <span className="font-semibold">GRUT RAI</span>
              </div>
              <p className="text-sm text-muted-foreground">
                Building the future of causal intelligence systems.
              </p>
            </div>
            
            <div>
              <h4 className="font-medium mb-4">Resources</h4>
              <ul className="space-y-2 text-sm text-muted-foreground">
                <li><a href="#api" className="hover:text-foreground transition-colors" data-testid="link-footer-docs">Documentation</a></li>
                <li><a href="#api" className="hover:text-foreground transition-colors" data-testid="link-footer-api">API Reference</a></li>
                <li><a href="#research" className="hover:text-foreground transition-colors" data-testid="link-footer-papers">Research Papers</a></li>
              </ul>
            </div>
            
            <div>
              <h4 className="font-medium mb-4">Company</h4>
              <ul className="space-y-2 text-sm text-muted-foreground">
                <li><a href="#theory" className="hover:text-foreground transition-colors" data-testid="link-footer-about">About</a></li>
                <li><a href="#research" className="hover:text-foreground transition-colors" data-testid="link-footer-research">Research</a></li>
                <li><a href="#subscribe" className="hover:text-foreground transition-colors" data-testid="link-footer-contact">Contact</a></li>
              </ul>
            </div>
            
            <div>
              <h4 className="font-medium mb-4">Connect</h4>
              <div className="flex items-center gap-3">
                <Button variant="ghost" size="icon" asChild data-testid="link-twitter">
                  <a href="#" aria-label="Twitter">
                    <Twitter className="w-4 h-4" />
                  </a>
                </Button>
                <Button variant="ghost" size="icon" asChild data-testid="link-github">
                  <a href="#" aria-label="GitHub">
                    <Github className="w-4 h-4" />
                  </a>
                </Button>
                <Button variant="ghost" size="icon" asChild data-testid="link-linkedin">
                  <a href="#" aria-label="LinkedIn">
                    <Linkedin className="w-4 h-4" />
                  </a>
                </Button>
              </div>
            </div>
          </div>
        </div>
        
        <div className="py-6 border-t border-border">
          <div className="flex flex-col sm:flex-row items-center justify-between gap-4 text-sm text-muted-foreground">
            <p data-testid="text-copyright">2025 GRUT RAI Platform. All rights reserved.</p>
            <div className="flex items-center gap-4">
              <a href="#" className="hover:text-foreground transition-colors" data-testid="link-privacy">Privacy Policy</a>
              <a href="#" className="hover:text-foreground transition-colors" data-testid="link-terms">Terms of Service</a>
            </div>
          </div>
        </div>
      </div>
    </footer>
  );
}

export default function Home() {
  return (
    <div className="min-h-screen bg-background">
      <Navigation />
      <main>
        <HeroSection />
        <TheorySection />
        <HowItWorksSection />
        <AdvantagesSection />
        <ResearchSection />
        <APISection />
      </main>
      <CTAFooterSection />
    </div>
  );
}
