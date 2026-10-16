import React from 'react';
import { Composition } from 'remotion';
import { MainComposition } from './Composition';
import { GdpComposition } from './GdpComposition';
import { TutorialComposition } from './TutorialComposition';

export const RemotionRoot: React.FC = () => {
  return (
    <>
      {/* Video 1: Modern Warfare Military Documentary (60 FPS) */}
      <Composition
        id="Main"
        component={MainComposition}
        durationInFrames={1850}
        fps={60}
        width={1080}
        height={1920}
      />

      {/* Video 2: Remotion + AI Skill Full Tutorial (60 FPS) */}
      <Composition
        id="Tutorial"
        component={TutorialComposition}
        durationInFrames={4730}
        fps={60}
        width={1080}
        height={1920}
      />

      {/* Video 3: GDP Bar Chart Race 1950 - 2026 (60 FPS) */}
      <Composition
        id="GdpRace"
        component={GdpComposition}
        durationInFrames={3300}
        fps={60}
        width={1080}
        height={1920}
      />
    </>
  );
};
