import React from 'react';
import { interpolate, spring, useCurrentFrame, useVideoConfig } from 'remotion';

export interface MainCompositionProps {
  titleText: string;
  subtitleText: string;
}

export const MainComposition: React.FC<MainCompositionProps> = ({
  titleText,
  subtitleText,
}) => {
  const frame = useCurrentFrame();
  const { fps } = useVideoConfig();

  const titleScale = spring({
    frame,
    fps,
    config: {
      damping: 12,
    },
  });

  const subtitleOpacity = interpolate(frame, [20, 45], [0, 1], {
    extrapolateLeft: 'clamp',
    extrapolateRight: 'clamp',
  });

  return (
    <div
      style={{
        flex: 1,
        backgroundColor: '#0f172a',
        display: 'flex',
        flexDirection: 'column',
        justifyContent: 'center',
        alignItems: 'center',
        fontFamily: 'sans-serif',
      }}
    >
      <h1
        style={{
          color: '#ffffff',
          fontSize: 80,
          fontWeight: 800,
          transform: `scale(${titleScale})`,
          margin: 0,
          letterSpacing: '-2px',
        }}
      >
        {titleText}
      </h1>
      <p
        style={{
          color: '#38bdf8',
          fontSize: 36,
          fontWeight: 500,
          opacity: subtitleOpacity,
          marginTop: 20,
        }}
      >
        {subtitleText}
      </p>
    </div>
  );
};
