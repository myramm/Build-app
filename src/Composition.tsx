import React from 'react';
import {
  AbsoluteFill,
  Audio,
  Sequence,
  staticFile,
  useCurrentFrame,
  useVideoConfig,
} from 'remotion';
import { HudOverlay } from './components/HudOverlay';
import { Scene1Hook } from './scenes/Scene1Hook';
import { Scene2Drone } from './scenes/Scene2Drone';
import { Scene3Satellite } from './scenes/Scene3Satellite';
import { Scene4Network } from './scenes/Scene4Network';
import { Scene5AirDefense } from './scenes/Scene5AirDefense';
import { Scene6Outro } from './scenes/Scene6Outro';

export const MainComposition: React.FC = () => {
  const frame = useCurrentFrame();
  const { durationInFrames } = useVideoConfig();

  // Top Progress Bar
  const progress = (frame / durationInFrames) * 100;

  return (
    <AbsoluteFill
      style={{
        backgroundColor: '#040711',
        overflow: 'hidden',
      }}
    >
      {/* Background Cinematic Drone Ambience Audio */}
      <Audio
        src={staticFile('audio/ambience.mp3')}
        volume={0.25}
        loop
      />

      {/* Dynamic Top Progress Bar */}
      <div
        style={{
          position: 'absolute',
          top: 0,
          left: 0,
          right: 0,
          height: 10,
          zIndex: 999,
          backgroundColor: 'rgba(255, 255, 255, 0.1)',
        }}
      >
        <div
          style={{
            height: '100%',
            width: `${progress}%`,
            backgroundColor: '#38bdf8',
            boxShadow: '0 0 16px #38bdf8',
          }}
        />
      </div>

      {/* Visual Scenes & Voiceover Narration */}

      {/* Scene 1: Hook (0 - 5.0 detik / 0 - 300 frame) */}
      <Sequence from={0} durationInFrames={300}>
        <Audio src={staticFile('audio/scene1.mp3')} volume={1.0} />
        <Scene1Hook />
      </Sequence>

      {/* Scene 2: Drone Militer (5.0 - 9.66 detik / 300 - 580 frame) */}
      <Sequence from={300} durationInFrames={280}>
        <Audio src={staticFile('audio/scene2.mp3')} volume={1.0} />
        <Scene2Drone />
      </Sequence>

      {/* Scene 3: Satelit & Radar (9.66 - 14.33 detik / 580 - 860 frame) */}
      <Sequence from={580} durationInFrames={280}>
        <Audio src={staticFile('audio/scene3.mp3')} volume={1.0} />
        <Scene3Satellite />
      </Sequence>

      {/* Scene 4: Jaringan Informasi (14.33 - 19.16 detik / 860 - 1150 frame) */}
      <Sequence from={860} durationInFrames={290}>
        <Audio src={staticFile('audio/scene4.mp3')} volume={1.0} />
        <Scene4Network />
      </Sequence>

      {/* Scene 5: Pertahanan Udara (19.16 - 24.16 detik / 1150 - 1450 frame) */}
      <Sequence from={1150} durationInFrames={300}>
        <Audio src={staticFile('audio/scene5.mp3')} volume={1.0} />
        <Scene5AirDefense />
      </Sequence>

      {/* Scene 6: Penutup & Outro (24.16 - 30.83 detik / 1450 - 1850 frame) */}
      <Sequence from={1450} durationInFrames={400}>
        <Audio src={staticFile('audio/scene6.mp3')} volume={1.0} />
        <Scene6Outro />
      </Sequence>

      {/* Persistent Military Tactical HUD Overlay */}
      <HudOverlay />
    </AbsoluteFill>
  );
};
