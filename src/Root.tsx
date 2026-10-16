import React from 'react';
import { Composition } from 'remotion';
import { MainComposition } from './Composition';

export const RemotionRoot: React.FC = () => {
  return (
    <>
      <Composition
        id="Main"
        component={MainComposition}
        durationInFrames={1850}
        fps={60}
        width={1080}
        height={1920}
      />
    </>
  );
};
