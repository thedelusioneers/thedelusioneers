import React, { useEffect, useMemo, useRef, useState } from "react";
import { createRoot } from "react-dom/client";
import { Activity, Eye, Focus, Headphones, Wind } from "lucide-react";
import "./styles.css";

const neon = "#B7FF3C";

function Panel({ icon: Icon, title, subtitle, children, className = "" }) {
  return (
    <section className={`panel ${className}`}>
      <div className="panel-head">
        <div className="panel-title">
          <Icon size={18} strokeWidth={2} />
          <div>
            <h2>{title}</h2>
            <p>{subtitle}</p>
          </div>
        </div>
      </div>
      {children}
    </section>
  );
}

function VisualStim() {
  const [pos, setPos] = useState({ x: 50, y: 50 });
  const [alive, setAlive] = useState(false);
  const [hits, setHits] = useState(0);
  const timer = useRef(null);

  useEffect(() => {
    const move = () => {
      setPos({ x: 8 + Math.random() * 84, y: 10 + Math.random() * 80 });
      setAlive(true);
      clearTimeout(timer.current);
      timer.current = setTimeout(() => setAlive(false), 1300);
    };
    move();
    const id = setInterval(move, 1500);
    return () => { clearInterval(id); clearTimeout(timer.current); };
  }, []);

  const catchDot = () => {
    if (!alive) return;
    setHits(v => v + 1);
    setAlive(false);
  };

  return (
    <Panel icon={Eye} title="VISUAL STIM" subtitle="Pursuit / sustained attention">
      <div className="visual-field" onClick={catchDot}>
        <div className={`target ${alive ? "active" : ""}`}
          style={{ left: `${pos.x}%`, top: `${pos.y}%` }}
          onClick={(e) => { e.stopPropagation(); catchDot(); }}
        />
        <div className="field-label">HOVER / CATCH THE SIGNAL</div>
        <div className="field-score">{String(hits).padStart(2, "0")}</div>
      </div>
    </Panel>
  );
}

const stroopColors = [
  { name: "GREEN", value: "#B7FF3C" },
  { name: "MAGENTA", value: "#FF3CAC" },
  { name: "CYAN", value: "#37E8FF" },
  { name: "YELLOW", value: "#FFE65B" },
];

function FrictionTask() {
  const [running, setRunning] = useState(false);
  const [time, setTime] = useState(60);
  const [score, setScore] = useState(0);
  const [correct, setCorrect] = useState(0);
  const [total, setTotal] = useState(0);
  const [round, setRound] = useState(() => Math.floor(Math.random() * 4));

  useEffect(() => {
    if (!running) return;
    if (time <= 0) { setRunning(false); return; }
    const id = setInterval(() => setTime(t => t - 1), 1000);
    return () => clearInterval(id);
  }, [running, time]);

  const next = (i) => {
    if (!running) return;
    const isCorrect = i === round;
    setCorrect(c => c + (isCorrect ? 1 : 0));
    setTotal(t => t + 1);
    setScore(s => Math.max(0, s + (isCorrect ? 10 : -5)));
    setRound(Math.floor(Math.random() * 4));
  };

  const start = () => {
    setTime(60); setScore(0); setCorrect(0); setTotal(0); setRunning(true);
    setRound(Math.floor(Math.random() * 4));
  };

  const accuracy = total ? Math.round(correct / total * 100) : 0;

  return (
    <Panel icon={Focus} title="FRICTION TASK" subtitle="Stroop / inhibit the automatic response">
      <div className="stroop">
        <div className="timer">{String(time).padStart(2, "0")}<span>SEC</span></div>
        <div className="stroop-word" style={{ color: stroopColors[(round + 1) % 4].value }}>
          {stroopColors[round].name}
        </div>
        <p className="instruction">CLICK THE <b>COLOR</b>, NOT THE WORD</p>
        <div className="color-grid">
          {stroopColors.map((c, i) => (
            <button key={c.name} className="color-btn" style={{ "--swatch": c.value }} onClick={() => next(i)}>
              <i /> {c.name}
            </button>
          ))}
        </div>
        <div className="metrics">
          <span>FOCUS SCORE <b>{score}</b></span>
          <span>ACCURACY <b>{accuracy}%</b></span>
          <button onClick={start}>{running ? "RESET" : "START 60S"}</button>
        </div>
      </div>
    </Panel>
  );
}

function VagalPacer() {
  const [phase, setPhase] = useState("INHALE");
  useEffect(() => {
    const phases = ["INHALE", "HOLD", "EXHALE", "HOLD"];
    let i = 0;
    const id = setInterval(() => { i = (i + 1) % 4; setPhase(phases[i]); }, 4000);
    return () => clearInterval(id);
  }, []);
  return (
    <Panel icon={Wind} title="VAGAL PACER" subtitle="Box breathing / autonomic downshift">
      <div className="breath-area">
        <div className="breath-ring"><div className="breath-core"><span>{phase}</span><small>4 · 4 · 4 · 4</small></div></div>
        <p>FOLLOW THE RHYTHM · 4 SEC EACH PHASE</p>
      </div>
    </Panel>
  );
}

function SonicPrecision() {
  const [duration, setDuration] = useState(150);
  const [direction, setDirection] = useState(null);
  const [status, setStatus] = useState("READY");
  const audioRef = useRef(null);

  const playSweep = () => {
    const AudioCtx = window.AudioContext || window.webkitAudioContext;
    if (!AudioCtx) return;
    const ctx = audioRef.current || new AudioCtx();
    audioRef.current = ctx;
    if (ctx.state === "suspended") ctx.resume();
    const now = ctx.currentTime;
    const osc = ctx.createOscillator();
    const gain = ctx.createGain();
    const up = Math.random() > 0.5;
    setDirection(up ? "UP" : "DOWN");
    setStatus("LISTEN");
    const start = up ? 200 : 400;
    const end = up ? 400 : 200;
    osc.type = "sine";
    osc.frequency.setValueAtTime(start, now);
    osc.frequency.linearRampToValueAtTime(end, now + duration / 1000);
    gain.gain.setValueAtTime(0.0001, now);
    gain.gain.exponentialRampToValueAtTime(0.18, now + 0.006);
    gain.gain.exponentialRampToValueAtTime(0.0001, now + duration / 1000);
    osc.connect(gain).connect(ctx.destination);
    osc.start(now);
    osc.stop(now + duration / 1000 + 0.01);
  };

  useEffect(() => {
    const onKey = (e) => {
      if (!direction || !["ArrowUp", "ArrowDown"].includes(e.key)) return;
      const answer = e.key === "ArrowUp" ? "UP" : "DOWN";
      if (answer === direction) {
        setDuration(d => Math.max(20, d - 10));
        setStatus("CORRECT");
      } else {
        setDuration(d => Math.min(500, d + 20));
        setStatus("INCORRECT");
      }
      setDirection(null);
    };
    window.addEventListener("keydown", onKey);
    return () => window.removeEventListener("keydown", onKey);
  }, [direction]);

  return (
    <Panel icon={Headphones} title="SONIC PRECISION" subtitle="Auditory discrimination / adaptive staircase" className="sonic">
      <div className="sonic-main">
        <div>
          <div className="threshold"><strong>{duration}</strong><span>MS<br />THRESHOLD</span></div>
          <div className={`status ${status.toLowerCase()}`}>{status}</div>
          <p className="goal">TARGET <b>&lt; 40MS</b></p>
        </div>
        <div className="sonic-controls">
          <button className="play" onClick={playSweep}><Headphones size={20} /> PLAY SWEEP</button>
          <div className="keys"><kbd>↑</kbd><kbd>↓</kbd></div>
          <p>PRESS UP OR DOWN<br />TO IDENTIFY THE SWEEP</p>
        </div>
      </div>
      <div className="staircase">CORRECT <b>−10MS</b><span>•</span> INCORRECT <b>+20MS</b></div>
    </Panel>
  );
}

function App() {
  return (
    <main>
      <header>
        <div className="brand"><Activity size={24} /><span>SYNAPSE <b>PRIMER</b></span></div>
        <div className="live"><i /> SYSTEM READY</div>
      </header>
      <div className="grid">
        <VisualStim />
        <FrictionTask />
        <VagalPacer />
        <SonicPrecision />
      </div>
      <footer>FOCUS PROTOCOL · v1.0 <span>NEON / BLACK</span></footer>
    </main>
  );
}

createRoot(document.getElementById("root")).render(<App />);
