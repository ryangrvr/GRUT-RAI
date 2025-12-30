import { useState, useRef, useEffect, useCallback } from "react";
import { Button } from "@/components/ui/button";
import { Card, CardContent, CardHeader, CardTitle } from "@/components/ui/card";
import { Badge } from "@/components/ui/badge";
import { Volume2, VolumeX, Activity, Radio } from "lucide-react";

const GROUND_STATE_ALPHA = -1 / 12;
const BASE_FREQUENCY = 43.2;
const RESONANCE_FREQUENCY = 528;
const TAU_MYR = 41.9;
const LFO_PERIOD = 4.0;
const NG_GEOMETRIC_LOCK = 1.1547;

interface NANOGravData {
  absCorrelation: number;
  phaseTransitionActive: boolean;
  alignmentStatus: string;
}

export function MetricHum() {
  const [isPlaying, setIsPlaying] = useState(false);
  const [isSynced, setIsSynced] = useState(false);
  const [xiValue, setXiValue] = useState(0.999);
  const [nanoGravData, setNanoGravData] = useState<NANOGravData | null>(null);
  const [currentFrequency, setCurrentFrequency] = useState(BASE_FREQUENCY);

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
            onClick={syncWithVacuum}
            variant="default"
            className={`flex-1 transition-all duration-300 ${
              isSynced
                ? "bg-yellow-500 hover:bg-yellow-600 text-black"
                : ""
            }`}
            data-testid="button-sync-vacuum"
          >
            <Radio
              className={`h-4 w-4 mr-2 ${isSynced ? "animate-spin" : ""}`}
            />
            {isSynced ? "VACUUM ACTIVE" : "SYNC WITH VACUUM"}
          </Button>
        </div>

        {isSynced && (
          <div className="text-xs text-center text-yellow-400/80 animate-pulse">
            The Vacuum resonates at -1/12. MONAD coherence established.
          </div>
        )}
      </CardContent>
    </Card>
  );
}
