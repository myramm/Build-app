import React from 'react';
import {
  AbsoluteFill,
  Audio,
  interpolate,
  staticFile,
  useCurrentFrame,
  useVideoConfig,
} from 'remotion';
import { getCurrentMilestone, getRankedCountries } from './gdp/data';
import { GdpBar } from './gdp/GdpBar';
import { GdpHeader } from './gdp/GdpHeader';
import { GdpMilestone } from './gdp/GdpMilestone';

export const GdpComposition: React.FC = () => {
  const frame = useCurrentFrame();
  const { durationInFrames } = useVideoConfig();

  // Progress from 1950 to 2026
  // Hold at 1950 for the first 150 frames (2.5s) while voiceover introduces
  // Smoothly race from 1950 to 2026 between frame 150 and 3100
  // Hold at 2026 for the final 200 frames (3.3s)
  const currentYear = interpolate(frame, [150, 3100], [1950, 2026], {
    extrapolateLeft: 'clamp',
    extrapolateRight: 'clamp',
  });

  const rankedCountries = getRankedCountries(currentYear);
  const maxGdp = rankedCountries.length > 0 ? rankedCountries[0].gdp : 1;
  const milestone = getCurrentMilestone(currentYear);

  return (
    <AbsoluteFill
      style={{
        backgroundColor: '#03050C',
        overflow: 'hidden',
        fontFamily: "'Space Grotesk', sans-serif",
      }}
    >
      {/* Intro Narration Voiceover */}
      <Audio src={staticFile('audio/gdp/intro.mp3')} volume={1.0} />

      {/* Rhythmic Background Audio */}
      <Audio src={staticFile('audio/gdp/pulse.mp3')} volume={0.12} loop />

      {/* Subtle Background Grid */}
      <div
        style={{
          position: 'absolute',
          inset: 0,
          backgroundImage:
            'linear-gradient(rgba(255, 255, 255, 0.03) 1px, transparent 1px), linear-gradient(90deg, rgba(255, 255, 255, 0.03) 1px, transparent 1px)',
          backgroundSize: '80px 80px',
        }}
      />

      {/* Header with Title & Live Year Counter */}
      <GdpHeader currentYear={currentYear} />

      {/* 10 Animated Country Bars */}
      <div style={{ position: 'relative', width: '100%', height: '100%' }}>
        {rankedCountries.map((c) => (
          <GdpBar key={c.id} country={c} maxGdp={maxGdp} />
        ))}
      </div>

      {/* Milestone Toast Callout */}
      <GdpMilestone milestone={milestone} />
    </AbsoluteFill>
  );
};
