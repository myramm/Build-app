import React from 'react';
import {
  AbsoluteFill,
  Audio,
  Sequence,
  staticFile,
  useCurrentFrame,
} from 'remotion';
import {
  getActiveMilestone,
  getDateFromFrame,
  getRankedCountriesMonthly,
  MILESTONES,
} from './gdp/data';
import { GdpBar } from './gdp/GdpBar';
import { GdpHeader } from './gdp/GdpHeader';
import { GdpMilestone } from './gdp/GdpMilestone';

export const GdpComposition: React.FC = () => {
  const frame = useCurrentFrame();

  // Current exact month and year
  const currentDate = getDateFromFrame(frame);

  // Sample 20 frames prior to determine recent rank climb/fall
  const prevDate = getDateFromFrame(Math.max(0, frame - 20));

  // Current top 10 rankings
  const rankedCountries = getRankedCountriesMonthly(
    currentDate.yearDecimal,
    prevDate.yearDecimal
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

  return (
    <AbsoluteFill
      style={{
        backgroundColor: '#03050E',
        overflow: 'hidden',
        fontFamily: "'Space Grotesk', -apple-system, sans-serif",
      }}
    >
      {/* ============================================================ */}
      {/* AUDIO SOUND EFFECTS (PURE SFX - NO VOICEOVER)                */}
      {/* ============================================================ */}

      {/* 1. Continuous Driving Ambient Pulse / Synth Bass */}
      <Audio src={staticFile('audio/gdp/pulse.mp3')} volume={0.25} loop />

      {/* 2. Crystal Chime SFX triggered on each Milestone Event */}
      {MILESTONES.map((m) => (
        <Sequence
          key={`chime-${m.id}`}
          from={m.startFrame}
          durationInFrames={120}
        >
          <Audio src={staticFile('audio/gdp/chime.mp3')} volume={0.7} />
        </Sequence>
      ))}

      {/* 3. Aerodynamic Whoosh SFX for Major Overtakes */}
      {MILESTONES.map((m) => (
        <Sequence
          key={`whoosh-${m.id}`}
          from={m.startFrame + 5}
          durationInFrames={45}
        >
          <Audio src={staticFile('audio/gdp/whoosh.mp3')} volume={0.35} />
        </Sequence>
      ))}

      {/* 4. Periodic Subtle Ticks on Month Advances (Every 60 frames) */}
      {Array.from({ length: 54 }).map((_, i) => (
        <Sequence key={`tick-${i}`} from={i * 60} durationInFrames={10}>
          <Audio src={staticFile('audio/gdp/tick.mp3')} volume={0.12} />
        </Sequence>
      ))}

      {/* ============================================================ */}
      {/* VISUAL DESIGN: CINEMA DARK UI & DATA VISUALIZATION           */}
      {/* ============================================================ */}

      {/* Subtle Background Radial Glow */}
      <div
        style={{
          position: 'absolute',
          top: -200,
          right: -200,
          width: 800,
          height: 800,
          borderRadius: '50%',
          background: 'radial-gradient(circle, rgba(56, 189, 248, 0.06) 0%, transparent 70%)',
          pointerEvents: 'none',
        }}
      />
      <div
        style={{
          position: 'absolute',
          bottom: 200,
          left: -200,
          width: 700,
          height: 700,
          borderRadius: '50%',
          background: 'radial-gradient(circle, rgba(239, 68, 68, 0.05) 0%, transparent 70%)',
          pointerEvents: 'none',
        }}
      />

      {/* Vertical Scale Guideline Grid */}
      <div
        style={{
          position: 'absolute',
          left: 122,
          right: 44,
          top: 210,
          bottom: 180,
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
                  fontFamily: "'Fira Code', monospace",
                  fontSize: 14,
                  color: 'rgba(255, 255, 255, 0.25)',
                  transform: 'translateX(-50%)',
                }}
              >
                {val >= 1000 ? `$${val / 1000}T` : `$${val}B`}
              </span>
            </div>
          );
        })}
      </div>

      {/* Header: Title, Live Monthly Resolution & Giant Date Badge */}
      <GdpHeader date={currentDate} />

      {/* 10 Animated Country Bars */}
      <div style={{ position: 'relative', width: '100%', height: '100%' }}>
        {rankedCountries.map((c) => (
          <GdpBar key={c.id} country={c} maxGdp={maxGdp} />
        ))}
      </div>

      {/* Historical Context Milestone Toast */}
      <GdpMilestone milestone={activeMilestone} frame={frame} />
    </AbsoluteFill>
  );
};
