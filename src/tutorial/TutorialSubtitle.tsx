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
    from: 20,
    to: 0,
    config: { damping: 18, mass: 0.5 },
  });

  const opacity = interpolate(frame, [0, 12], [0, 1], {
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
            color: isHigh ? '#10b981' : '#f8fafc',
            fontWeight: isHigh ? 800 : 500,
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
        bottom: 60,
        left: 40,
        right: 40,
        transform: `translateY(${translateY}px)`,
        opacity,
        zIndex: 100,
      }}
    >
      <div
        style={{
          backgroundColor: '#090d16',
          border: '1px solid #1e293b',
          borderRadius: 12,
          padding: '24px 28px',
          textAlign: 'left',
          boxShadow: '0 20px 40px rgba(0, 0, 0, 0.6)',
        }}
      >
        <p
          style={{
            margin: 0,
            fontSize: 30,
            lineHeight: 1.5,
            fontFamily: "'Segoe UI', Roboto, sans-serif",
            letterSpacing: '-0.2px',
          }}
        >
          {renderWords()}
        </p>
      </div>
    </div>
  );
};
