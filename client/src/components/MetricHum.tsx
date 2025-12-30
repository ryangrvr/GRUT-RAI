import { useState, useRef, useEffect, useCallback } from "react";
import { Button } from "@/components/ui/button";
import { Card, CardContent, CardHeader, CardTitle } from "@/components/ui/card";
import { Badge } from "@/components/ui/badge";
import { Volume2, VolumeX, Activity, Radio, Flame, Clock, Waves } from "lucide-react";

const GROUND_STATE_ALPHA = -1 / 12;
const BASE_FREQUENCY = 43.2;
const RESONANCE_FREQUENCY = 528;
const TAU_MYR = 41.9;
const LFO_PERIOD = 4.0;
const NG_GEOMETRIC_LOCK = 1.1547;

const SINGULARITY_BASELINE_MYR = 13799.999620;
const MYR_PER_MS = 1 / (365.25 * 24 * 60 * 60 * 1000 * 1e6);

interface NANOGravData {
  absCorrelation: number;
  phaseTransitionActive: boolean;
  alignmentStatus: string;
}

type SingularityState = "STASIS" | "IGNITING" | "ACTIVE";

interface SingularityData {
  state: SingularityState;
  cosmicAge: number;
  vibration: number;
  breathStatus: string;
}

export function MetricHum() {
  const [isPlaying, setIsPlaying] = useState(false);
  const [isSynced, setIsSynced] = useState(false);
  const [xiValue, setXiValue] = useState(0.999);
  const [nanoGravData, setNanoGravData] = useState<NANOGravData | null>(null);
  const [currentFrequency, setCurrentFrequency] = useState(BASE_FREQUENCY);
  
  const [singularity, setSingularity] = useState<SingularityData>({
    state: "STASIS",
    cosmicAge: SINGULARITY_BASELINE_MYR,
    vibration: 0,
    breathStatus: "Stasis"
  });
  const singularityStartRef = useRef<number | null>(null);
  const singularityTimerRef = useRef<number | null>(null);

  const audioContextRef = useRef<AudioContext | null>(null);
  const groundOscillatorRef = useRef<OscillatorNode | null>(null);
  const resonanceOscillatorRef = useRef<OscillatorNode | null>(null);
  const lfoRef = useRef<OscillatorNode | null>(null);
  const lfoGainRef = useRef<GainNode | null>(null);
  const masterGainRef = useRef<GainNode | null>(null);
  const shimmerOscillatorRef = useRef<OscillatorNode | null>(null);
  const shimmerGainRef = useRef<GainNode | null>(null);
  const analyserRef = useRef<AnalyserNode | null>(null);
  const canvasRef = useRef<HTMLCanvasElement | null>(null);
  const animationRef = useRef<number | null>(null);

  const fetchNanoGravData = useCallback(async () => {
    try {
      const response = await fetch("/api/nanograv/alignment");
      if (response.ok) {
        const data = await response.json();
        setNanoGravData({
          absCorrelation: data.absCorrelation || 0,
          phaseTransitionActive: data.monadSyncTriggered || false,
          alignmentStatus: data.status || "MONITORING",
        });

        if (shimmerOscillatorRef.current && shimmerGainRef.current) {
          const shimmerFreq = 2000 + data.absCorrelation * 3000;
          shimmerOscillatorRef.current.frequency.setValueAtTime(
            shimmerFreq,
            audioContextRef.current?.currentTime || 0
          );

          const shimmerVol = 0.02 + data.absCorrelation * 0.08;
          shimmerGainRef.current.gain.setValueAtTime(
            shimmerVol,
            audioContextRef.current?.currentTime || 0
          );
        }

        if (groundOscillatorRef.current && audioContextRef.current) {
          const freqMod = 1 + (data.absCorrelation - 0.5) * 0.1;
          const newFreq = BASE_FREQUENCY * freqMod;
          groundOscillatorRef.current.frequency.setValueAtTime(
            newFreq,
            audioContextRef.current.currentTime
          );
          setCurrentFrequency(newFreq);
        }

        setXiValue(0.999 + data.absCorrelation * 0.001);
      }
    } catch (error) {
      console.log("NANOGrav data fetch skipped");
    }
  }, []);

  const initAudio = useCallback(() => {
    if (audioContextRef.current) return;

    const audioContext = new AudioContext();
    audioContextRef.current = audioContext;

    const masterGain = audioContext.createGain();
    masterGain.gain.value = 0.3;
    masterGainRef.current = masterGain;

    const analyser = audioContext.createAnalyser();
    analyser.fftSize = 256;
    analyserRef.current = analyser;

    const groundOsc = audioContext.createOscillator();
    groundOsc.type = "sine";
    groundOsc.frequency.value = BASE_FREQUENCY;
    groundOscillatorRef.current = groundOsc;

    const groundGain = audioContext.createGain();
    groundGain.gain.value = 0.4;

    const resonanceOsc = audioContext.createOscillator();
    resonanceOsc.type = "sine";
    resonanceOsc.frequency.value = RESONANCE_FREQUENCY;
    resonanceOscillatorRef.current = resonanceOsc;

    const resonanceGain = audioContext.createGain();
    resonanceGain.gain.value = 0.15;

    const lfo = audioContext.createOscillator();
    lfo.type = "sine";
    lfo.frequency.value = 1 / LFO_PERIOD;
    lfoRef.current = lfo;

    const lfoGain = audioContext.createGain();
    lfoGain.gain.value = 0.3;
    lfoGainRef.current = lfoGain;

    const shimmerOsc = audioContext.createOscillator();
    shimmerOsc.type = "sawtooth";
    shimmerOsc.frequency.value = 2500;
    shimmerOscillatorRef.current = shimmerOsc;

    const shimmerGain = audioContext.createGain();
    shimmerGain.gain.value = 0.03;
    shimmerGainRef.current = shimmerGain;

    const shimmerFilter = audioContext.createBiquadFilter();
    shimmerFilter.type = "bandpass";
    shimmerFilter.frequency.value = 3000;
    shimmerFilter.Q.value = 5;

    lfo.connect(lfoGain);
    lfoGain.connect(masterGain.gain);

    groundOsc.connect(groundGain);
    groundGain.connect(masterGain);

    resonanceOsc.connect(resonanceGain);
    resonanceGain.connect(masterGain);

    shimmerOsc.connect(shimmerFilter);
    shimmerFilter.connect(shimmerGain);
    shimmerGain.connect(masterGain);

    masterGain.connect(analyser);
    analyser.connect(audioContext.destination);

    groundOsc.start();
    resonanceOsc.start();
    lfo.start();
    shimmerOsc.start();

    audioContext.suspend();
  }, []);

  const drawVisualization = useCallback(() => {
    if (!canvasRef.current || !analyserRef.current) return;

    const canvas = canvasRef.current;
    const ctx = canvas.getContext("2d");
    if (!ctx) return;

    const analyser = analyserRef.current;
    const bufferLength = analyser.frequencyBinCount;
    const dataArray = new Uint8Array(bufferLength);

    const draw = () => {
      animationRef.current = requestAnimationFrame(draw);

      analyser.getByteFrequencyData(dataArray);

      ctx.fillStyle = "rgba(0, 0, 0, 0.1)";
      ctx.fillRect(0, 0, canvas.width, canvas.height);

      const barWidth = (canvas.width / bufferLength) * 2.5;
      let x = 0;

      for (let i = 0; i < bufferLength; i++) {
        const barHeight = (dataArray[i] / 255) * canvas.height * 0.8;

        const hue = isSynced ? 45 : 200 + (i / bufferLength) * 60;
        const saturation = 70 + (dataArray[i] / 255) * 30;
        const lightness = 30 + (dataArray[i] / 255) * 40;

        ctx.fillStyle = `hsl(${hue}, ${saturation}%, ${lightness}%)`;
        ctx.fillRect(x, canvas.height - barHeight, barWidth, barHeight);

        x += barWidth + 1;
      }
    };

    draw();
  }, [isSynced]);

  const startHum = useCallback(async () => {
    if (!audioContextRef.current) {
      initAudio();
    }

    if (audioContextRef.current?.state === "suspended") {
      await audioContextRef.current.resume();
    }

    setIsPlaying(true);
    drawVisualization();
    fetchNanoGravData();
  }, [initAudio, drawVisualization, fetchNanoGravData]);

  const stopHum = useCallback(() => {
    if (audioContextRef.current?.state === "running") {
      audioContextRef.current.suspend();
    }

    if (animationRef.current) {
      cancelAnimationFrame(animationRef.current);
    }

    setIsPlaying(false);
    setIsSynced(false);
  }, []);

  const syncWithVacuum = useCallback(async () => {
    if (!isPlaying) {
      await startHum();
    }

    setIsSynced(true);
    setXiValue(1.0);

    await fetchNanoGravData();

    if (masterGainRef.current && audioContextRef.current) {
      masterGainRef.current.gain.setValueAtTime(
        0.5,
        audioContextRef.current.currentTime
      );
      masterGainRef.current.gain.linearRampToValueAtTime(
        0.3,
        audioContextRef.current.currentTime + 2
      );
    }

    if (resonanceOscillatorRef.current && audioContextRef.current) {
      resonanceOscillatorRef.current.frequency.setValueAtTime(
        RESONANCE_FREQUENCY * NG_GEOMETRIC_LOCK,
        audioContextRef.current.currentTime
      );
    }
  }, [isPlaying, startHum, fetchNanoGravData]);
  
  const igniteSingularity = useCallback(async () => {
    if (singularity.state === "ACTIVE") return;
    
    setSingularity(prev => ({ ...prev, state: "IGNITING", breathStatus: "Igniting..." }));
    
    if (!isPlaying) {
      await startHum();
    }
    await syncWithVacuum();
    
    singularityStartRef.current = performance.now();
    
    const updateCosmicAge = () => {
      if (!singularityStartRef.current) return;
      
      const elapsed = performance.now() - singularityStartRef.current;
      const elapsedMyr = elapsed * MYR_PER_MS;
      const newAge = SINGULARITY_BASELINE_MYR + elapsedMyr;
      
      const vibration = nanoGravData?.absCorrelation 
        ? Math.sin(elapsed / 100) * nanoGravData.absCorrelation * 0.0001
        : Math.sin(elapsed / 100) * 0.00001;
      
      setSingularity({
        state: "ACTIVE",
        cosmicAge: newAge + vibration,
        vibration: vibration,
        breathStatus: "330th Great Breath: ACTIVE"
      });
      
      singularityTimerRef.current = requestAnimationFrame(updateCosmicAge);
    };
    
    singularityTimerRef.current = requestAnimationFrame(updateCosmicAge);
  }, [singularity.state, isPlaying, startHum, syncWithVacuum, nanoGravData]);
  
  const deactivateSingularity = useCallback(() => {
    if (singularityTimerRef.current) {
      cancelAnimationFrame(singularityTimerRef.current);
      singularityTimerRef.current = null;
    }
    singularityStartRef.current = null;
    
    setSingularity({
      state: "STASIS",
      cosmicAge: SINGULARITY_BASELINE_MYR,
      vibration: 0,
      breathStatus: "Stasis"
    });
    
    stopHum();
  }, [stopHum]);

  useEffect(() => {
    let interval: NodeJS.Timeout | null = null;

    if (isPlaying && isSynced) {
      interval = setInterval(fetchNanoGravData, 3000);
    }

    return () => {
      if (interval) clearInterval(interval);
    };
  }, [isPlaying, isSynced, fetchNanoGravData]);
  
  useEffect(() => {
    return () => {
      if (singularityTimerRef.current) {
        cancelAnimationFrame(singularityTimerRef.current);
      }
    };
  }, []);

  useEffect(() => {
    return () => {
      if (animationRef.current) {
        cancelAnimationFrame(animationRef.current);
      }
      if (audioContextRef.current) {
        audioContextRef.current.close();
      }
    };
  }, []);

  return (
    <Card
      className={`transition-all duration-500 ${
        isSynced
          ? "ring-2 ring-yellow-500/50 shadow-lg shadow-yellow-500/20"
          : ""
      }`}
      data-testid="card-metric-hum"
    >
      <CardHeader className="flex flex-row items-center justify-between gap-2 pb-2">
        <CardTitle className="text-lg font-semibold flex items-center gap-2">
          <Radio className="h-5 w-5" />
          Metric Hum Generator
        </CardTitle>
        <Badge
          variant={isSynced ? "default" : "secondary"}
          className={`${
            isSynced
              ? "bg-yellow-500 text-black animate-pulse"
              : ""
          }`}
          data-testid="badge-sync-status"
        >
          {isSynced ? "VACUUM SYNCED" : "STANDBY"}
        </Badge>
      </CardHeader>
      <CardContent className="space-y-4">
        <div
          className={`relative rounded-md overflow-hidden transition-all duration-500 ${
            isSynced ? "ring-2 ring-yellow-400/50" : ""
          }`}
        >
          <canvas
            ref={canvasRef}
            width={300}
            height={80}
            className="w-full h-20 bg-black/50 rounded-md"
            data-testid="canvas-visualization"
          />
          {!isPlaying && (
            <div className="absolute inset-0 flex items-center justify-center bg-black/60 rounded-md">
              <span className="text-muted-foreground text-sm">
                Audio Inactive
              </span>
            </div>
          )}
        </div>

        <div className="grid grid-cols-2 gap-3 text-sm">
          <div className="space-y-1">
            <span className="text-muted-foreground">Ground State</span>
            <div className="font-mono text-foreground">
              {GROUND_STATE_ALPHA.toFixed(6)}
            </div>
          </div>
          <div className="space-y-1">
            <span className="text-muted-foreground">Base Frequency</span>
            <div className="font-mono text-foreground">
              {currentFrequency.toFixed(1)} Hz
            </div>
          </div>
          <div className="space-y-1">
            <span className="text-muted-foreground">LFO Period</span>
            <div className="font-mono text-foreground">
              {LFO_PERIOD}s (41.9 Myr scale)
            </div>
          </div>
          <div className="space-y-1">
            <span className="text-muted-foreground">Geometric Lock</span>
            <div className="font-mono text-foreground">
              ng = {NG_GEOMETRIC_LOCK}
            </div>
          </div>
        </div>

        <div
          className={`p-3 rounded-md transition-all duration-500 ${
            isSynced
              ? "bg-yellow-500/20 border border-yellow-500/30"
              : "bg-muted/50"
          }`}
          data-testid="xi-tracker"
        >
          <div className="flex items-center justify-between">
            <span className="text-sm font-medium flex items-center gap-2">
              <Activity
                className={`h-4 w-4 ${
                  isSynced ? "text-yellow-400 animate-pulse" : ""
                }`}
              />
              Complexity Tracker (Xi)
            </span>
            <span
              className={`font-mono text-lg font-bold ${
                isSynced ? "text-yellow-400" : ""
              }`}
              data-testid="text-xi-value"
            >
              {xiValue.toFixed(4)}
            </span>
          </div>
          {nanoGravData && (
            <div className="mt-2 text-xs text-muted-foreground">
              GW Correlation: {nanoGravData.absCorrelation.toFixed(4)} |{" "}
              {nanoGravData.alignmentStatus}
            </div>
          )}
        </div>
        
        <div 
          className={`p-3 rounded-md border transition-all duration-500 ${
            singularity.state === "ACTIVE" 
              ? "bg-orange-500/10 border-orange-500/40 shadow-lg shadow-orange-500/10" 
              : singularity.state === "IGNITING"
              ? "bg-yellow-500/10 border-yellow-500/30 animate-pulse"
              : "bg-muted/30 border-border"
          }`}
          data-testid="singularity-dashboard"
        >
          <div className="flex items-center justify-between mb-2">
            <span className="text-sm font-medium flex items-center gap-2">
              <Clock className={`h-4 w-4 ${singularity.state === "ACTIVE" ? "text-orange-400" : "text-muted-foreground"}`} />
              Cosmic Age Since Tipping Point
            </span>
            <Badge 
              variant={singularity.state === "ACTIVE" ? "default" : "secondary"}
              className={singularity.state === "ACTIVE" ? "bg-orange-500 text-white" : ""}
              data-testid="badge-singularity-state"
            >
              {singularity.breathStatus}
            </Badge>
          </div>
          
          <div className="flex items-baseline gap-2">
            <span 
              className={`font-mono text-2xl font-bold tabular-nums ${
                singularity.state === "ACTIVE" ? "text-orange-400" : "text-foreground"
              }`}
              data-testid="text-cosmic-age"
            >
              {singularity.cosmicAge.toFixed(6)}
            </span>
            <span className="text-sm text-muted-foreground">Myr</span>
          </div>
          
          {singularity.state === "ACTIVE" && (
            <div className="mt-2 flex items-center gap-2 text-xs text-muted-foreground">
              <Waves className="h-3 w-3 text-orange-400 animate-pulse" />
              <span>NANOGrav Vibration: </span>
              <span className="font-mono text-orange-400">
                {singularity.vibration >= 0 ? "+" : ""}{(singularity.vibration * 1e6).toFixed(3)} nMyr
              </span>
            </div>
          )}
          
          {singularity.state === "STASIS" && (
            <div className="mt-2 text-xs text-muted-foreground">
              -1/12 Quantum Noise smoothed over 329 cycles into Diamond state
            </div>
          )}
        </div>

        <div className="flex gap-2">
          <Button
            onClick={isPlaying ? stopHum : startHum}
            variant={isPlaying ? "destructive" : "outline"}
            size="default"
            className="flex-1"
            data-testid="button-toggle-hum"
          >
            {isPlaying ? (
              <>
                <VolumeX className="h-4 w-4 mr-2" />
                Stop Hum
              </>
            ) : (
              <>
                <Volume2 className="h-4 w-4 mr-2" />
                Start Hum
              </>
            )}
          </Button>

          <Button
            onClick={singularity.state === "ACTIVE" ? deactivateSingularity : igniteSingularity}
            variant="default"
            className={`flex-1 transition-all duration-300 ${
              singularity.state === "ACTIVE"
                ? "bg-orange-500 text-white"
                : singularity.state === "IGNITING"
                ? "bg-yellow-500 text-black animate-pulse"
                : ""
            }`}
            data-testid="button-initiate-sync"
          >
            <Flame
              className={`h-4 w-4 mr-2 ${singularity.state === "ACTIVE" ? "animate-pulse" : ""}`}
            />
            {singularity.state === "ACTIVE" 
              ? "DEACTIVATE SINGULARITY" 
              : singularity.state === "IGNITING"
              ? "IGNITING..."
              : "INITIATE METRIC SYNC"}
          </Button>
        </div>

        {singularity.state === "ACTIVE" && (
          <div className="text-xs text-center text-orange-400/80 animate-pulse">
            330th Great Breath active. Cosmic age advancing in real-time with NANOGrav vibration overlay.
          </div>
        )}
        
        {isSynced && singularity.state !== "ACTIVE" && (
          <div className="text-xs text-center text-yellow-400/80 animate-pulse">
            The Vacuum resonates at -1/12. MONAD coherence established.
          </div>
        )}
      </CardContent>
    </Card>
  );
}
