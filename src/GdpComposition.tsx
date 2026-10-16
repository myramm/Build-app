import React from 'react';
import {
  AbsoluteFill,
  Audio,
  Sequence,
  staticFile,
  useCurrentFrame,
  useVideoConfig,
} from 'remotion';
import {
  getActiveMilestone,
  getRankedCountries,
  getTimelineState,
  MILESTONES,
} from './gdp/data';
import { GdpBar } from './gdp/GdpBar';
import { GdpFooter } from './gdp/GdpFooter';
import { GdpHeader } from './gdp/GdpHeader';
import { GdpMilestone } from './gdp/GdpMilestone';

export const GdpComposition: React.FC = () => {
  const frame = useCurrentFrame();
  const { durationInFrames } = useVideoConfig();

  // Current timeline state (Year, Projection status, Progress)
  const timeline = getTimelineState(frame, durationInFrames);

  // Sample 24 frames prior to determine recent rank climb/fall
  const prevTimeline = getTimelineState(
    Math.max(0, frame - 24),
    durationInFrames
  );

  // Top 10 countries ranked at current year
  const rankedCountries = getRankedCountries(
    timeline.yearDecimal,
    prevTimeline.yearDecimal
  );
  const maxGdp = rankedCountries.length > 0 ? rankedCountries[0].gdp : 1;
  const activeMilestone = getActiveMilestone(frame);

  // Dynamic Scale Grid Lines based on maxGdp
  const gridMarks =
    maxGdp > 15000
      ? [5000, 10000, 20000, 25000]
      : maxGdp > 5000
      ? [1000, 2500, 5000, 7500]
      : maxGdp > 1000
      ? [250, 500, 1000, 1500]
      : [100, 250, 500, 750];

  const isFinalFrame = frame >= durationInFrames - 120;

  return (
    <AbsoluteFill
      style={{
        backgroundColor: '#080A10',
        overflow: 'hidden',
        fontFamily: "'Space Grotesk', -apple-system, sans-serif",
      }}
    >
      {/* ============================================================ */}
      {/* AUDIO SOUND EFFECTS (PURE SFX DESIGN)                        */}
      {/* ============================================================ */}

      {/* 1. Ambient Rhythmic Pulse (120 BPM driving tempo) */}
      <Audio src={staticFile('audio/gdp/pulse.mp3')} volume={0.22} loop />

      {/* 2. Crystal Chime on each Milestone Event */}
      {MILESTONES.map((m) => (
        <Sequence
          key={`chime-${m.id}`}
          from={m.startFrame}
          durationInFrames={120}
        >
          <Audio src={staticFile('audio/gdp/chime.mp3')} volume={0.65} />
        </Sequence>
      ))}

      {/* 3. Aerodynamic Whoosh for Major Rank Shifts */}
      {MILESTONES.map((m) => (
        <Sequence
          key={`whoosh-${m.id}`}
          from={m.startFrame + 4}
          durationInFrames={40}
        >
          <Audio src={staticFile('audio/gdp/whoosh.mp3')} volume={0.3} />
        </Sequence>
      ))}

      {/* 4. Periodic Subtle Ticks on Year Transitions (Every 40 frames) */}
      {Array.from({ length: 76 }).map((_, i) => (
        <Sequence key={`tick-${i}`} from={60 + i * 40} durationInFrames={8}>
          <Audio src={staticFile('audio/gdp/tick.mp3')} volume={0.1} />
        </Sequence>
      ))}

      {/* ============================================================ */}
      {/* VISUAL DESIGN: CLEAN EDITORIAL DATA VISUALIZATION            */}
      {/* ============================================================ */}

      {/* Vertical Scale Guideline Grid */}
      <div
        style={{
          position: 'absolute',
          left: 106,
          right: 48,
          top: 210,
          bottom: 70,
          pointerEvents: 'none',
        }}
      >
        {gridMarks.map((val) => {
          const leftPercent = Math.min(100, (val / maxGdp) * 100);
          if (leftPercent > 92 || leftPercent < 15) return null;
          return (
            <div
              key={val}
              style={{
                position: 'absolute',
                left: `${leftPercent}%`,
                top: 0,
                bottom: 0,
                borderLeft: '1px dashed rgba(255, 255, 255, 0.07)',
                display: 'flex',
                flexDirection: 'column',
                justifyContent: 'flex-end',
                paddingBottom: 8,
              }}
            >
              <span
                style={{
                  fontFamily: "'Space Grotesk', monospace",
                  fontSize: 14,
                  fontWeight: 700,
                  color: 'rgba(255, 255, 255, 0.28)',
                  transform: 'translateX(-50%)',
                }}
              >
                {val >= 1000 ? `$${val / 1000}T` : `$${val}B`}
              </span>
            </div>
          );
        })}
      </div>

      {/* Editorial Header */}
      <GdpHeader timeline={timeline} />

      {/* 10 Animated Country Bars */}
      <div style={{ position: 'relative', width: '100%', height: '100%' }}>
        {rankedCountries.map((c) => (
          <GdpBar key={c.id} country={c} maxGdp={maxGdp} />
        ))}
      </div>

      {/* Historical Context Milestone Toast */}
      <GdpMilestone milestone={activeMilestone} frame={frame} />

      {/* Editorial Footer & Attribution */}
      <GdpFooter isFinalFrame={isFinalFrame} />
    </AbsoluteFill>
  );
};
