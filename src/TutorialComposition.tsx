import React from 'react';
import {
  AbsoluteFill,
  Audio,
  Sequence,
  staticFile,
} from 'remotion';
import { Scene1Intro } from './tutorial/scenes/Scene1Intro';
import { Scene2Prereq } from './tutorial/scenes/Scene2Prereq';
import { Scene3Install } from './tutorial/scenes/Scene3Install';
import { Scene4AiSkill } from './tutorial/scenes/Scene4AiSkill';
import { Scene5Studio } from './tutorial/scenes/Scene5Studio';
import { Scene6Code } from './tutorial/scenes/Scene6Code';
import { Scene7Render } from './tutorial/scenes/Scene7Render';

export const TutorialComposition: React.FC = () => {
  return (
    <AbsoluteFill
      style={{
        backgroundColor: '#050811',
        overflow: 'hidden',
      }}
    >
      {/* Background Soft Ambience Audio */}
      <Audio
        src={staticFile('audio/ambience.mp3')}
        volume={0.08}
        loop
      />

      {/* Part 1: Pengenalan Remotion (0 - 700 frame, ~11.6s) */}
      <Sequence from={0} durationInFrames={700}>
        <Audio src={staticFile('audio/tutorial/tut1.mp3')} volume={1.0} />
        <Scene1Intro />
      </Sequence>

      {/* Part 2: Persiapan Node.js & npm (700 - 1420 frame, ~12.0s) */}
      <Sequence from={700} durationInFrames={720}>
        <Audio src={staticFile('audio/tutorial/tut2.mp3')} volume={1.0} />
        <Scene2Prereq />
      </Sequence>

      {/* Part 3: Instalasi Remotion (1420 - 2050 frame, ~10.5s) */}
      <Sequence from={1420} durationInFrames={630}>
        <Audio src={staticFile('audio/tutorial/tut3.mp3')} volume={1.0} />
        <Scene3Install />
      </Sequence>

      {/* Part 4: Memasang AI Skill (2050 - 2740 frame, ~11.5s) */}
      <Sequence from={2050} durationInFrames={690}>
        <Audio src={staticFile('audio/tutorial/tut4.mp3')} volume={1.0} />
        <Scene4AiSkill />
      </Sequence>

      {/* Part 5: Menjalankan Remotion Studio (2740 - 3370 frame, ~10.5s) */}
      <Sequence from={2740} durationInFrames={630}>
        <Audio src={staticFile('audio/tutorial/tut5.mp3')} volume={1.0} />
        <Scene5Studio />
      </Sequence>

      {/* Part 6: Koding Komponen Pertama (3370 - 4020 frame, ~10.8s) */}
      <Sequence from={3370} durationInFrames={650}>
        <Audio src={staticFile('audio/tutorial/tut6.mp3')} volume={1.0} />
        <Scene6Code />
      </Sequence>

      {/* Part 7: Render Menjadi MP4 (4020 - 4730 frame, ~11.8s) */}
      <Sequence from={4020} durationInFrames={710}>
        <Audio src={staticFile('audio/tutorial/tut7.mp3')} volume={1.0} />
        <Scene7Render />
      </Sequence>
    </AbsoluteFill>
  );
};
