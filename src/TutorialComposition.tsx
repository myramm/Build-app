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
      {/* Background Ambience Audio */}
      <Audio
        src={staticFile('audio/ambience.mp3')}
        volume={0.12}
        loop
      />

      {/* Part 1: Pengenalan Remotion (0 - 500 frame) */}
      <Sequence from={0} durationInFrames={500}>
        <Audio src={staticFile('audio/tutorial/tut1.mp3')} volume={1.0} />
        <Scene1Intro />
      </Sequence>

      {/* Part 2: Persiapan Node.js & npm (500 - 1040 frame) */}
      <Sequence from={500} durationInFrames={540}>
        <Audio src={staticFile('audio/tutorial/tut2.mp3')} volume={1.0} />
        <Scene2Prereq />
      </Sequence>

      {/* Part 3: Instalasi Remotion (1040 - 1580 frame) */}
      <Sequence from={1040} durationInFrames={540}>
        <Audio src={staticFile('audio/tutorial/tut3.mp3')} volume={1.0} />
        <Scene3Install />
      </Sequence>

      {/* Part 4: Memasang AI Skill (1580 - 2110 frame) */}
      <Sequence from={1580} durationInFrames={530}>
        <Audio src={staticFile('audio/tutorial/tut4.mp3')} volume={1.0} />
        <Scene4AiSkill />
      </Sequence>

      {/* Part 5: Menjalankan Remotion Studio (2110 - 2640 frame) */}
      <Sequence from={2110} durationInFrames={530}>
        <Audio src={staticFile('audio/tutorial/tut5.mp3')} volume={1.0} />
        <Scene5Studio />
      </Sequence>

      {/* Part 6: Koding Komponen Pertama (2640 - 3170 frame) */}
      <Sequence from={2640} durationInFrames={530}>
        <Audio src={staticFile('audio/tutorial/tut6.mp3')} volume={1.0} />
        <Scene6Code />
      </Sequence>

      {/* Part 7: Render Menjadi MP4 (3170 - 3770 frame) */}
      <Sequence from={3170} durationInFrames={600}>
        <Audio src={staticFile('audio/tutorial/tut7.mp3')} volume={1.0} />
        <Scene7Render />
      </Sequence>
    </AbsoluteFill>
  );
};
