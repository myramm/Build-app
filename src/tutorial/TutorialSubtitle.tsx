import React from 'react';
import { interpolate, spring, useCurrentFrame, useVideoConfig } from 'remotion';

interface TutorialSubtitleProps {
  text: string;
  highlightWords?: string[];
}

export const TutorialSubtitle: React.FC<TutorialSubtitleProps> = ({
  text,
  highlightWords = [],
}) => {
  const frame = useCurrentFrame();
  const { fps } = useVideoConfig();

  const translateY = spring({
    frame,
    fps,
    from: 40,
    to: 0,
    config: { damping: 16, mass: 0.6 },
  });

  const opacity = interpolate(frame, [0, 15], [0, 1], {
    extrapolateRight: 'clamp',
  });

  const renderWords = () => {
    return text.split(' ').map((word, i) => {
      const clean = word.replace(/[.,!]/g, '').toLowerCase();
      const isHigh = highlightWords.some((h) => h.toLowerCase() === clean);

      return (
        <span
          key={i}
          style={{
            color: isHigh ? '#38bdf8' : '#ffffff',
            fontWeight: isHigh ? 900 : 600,
            textShadow: isHigh ? '0 0 16px rgba(56, 189, 248, 0.7)' : 'none',
          }}
        >
          {word}{' '}
        </span>
      );
    });
  };

  return (
    <div
      style={{
        position: 'absolute',
        bottom: 70,
        left: 40,
        right: 40,
        transform: `translateY(${translateY}px)`,
        opacity,
        zIndex: 100,
      }}
    >
      <div
        style={{
          backgroundColor: 'rgba(13, 17, 23, 0.92)',
          border: '1.5px solid rgba(56, 189, 248, 0.4)',
          borderRadius: 24,
          padding: '24px 30px',
          textAlign: 'center',
          boxShadow: '0 20px 40px rgba(0, 0, 0, 0.85)',
        }}
      >
        <p
          style={{
            margin: 0,
            fontSize: 32,
            lineHeight: 1.45,
            fontFamily: "'Segoe UI', Roboto, sans-serif",
            letterSpacing: '-0.3px',
          }}
        >
          {renderWords()}
        </p>
      </div>
    </div>
  );
};
