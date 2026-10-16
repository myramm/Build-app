import React from 'react';
import { interpolate, spring, useCurrentFrame, useVideoConfig } from 'remotion';

interface SubtitleBarProps {
  badge: string;
  badgeColor?: string;
  text: string;
  highlightWords?: string[];
}

export const SubtitleBar: React.FC<SubtitleBarProps> = ({
  badge,
  badgeColor = '#38bdf8',
  text,
  highlightWords = [],
}) => {
  const frame = useCurrentFrame();
  const { fps } = useVideoConfig();

  // Smooth slide-up spring entrance
  const translateY = spring({
    frame,
    fps,
    from: 50,
    to: 0,
    config: { damping: 16, mass: 0.7 },
  });

  const opacity = interpolate(frame, [0, 15], [0, 1], {
    extrapolateRight: 'clamp',
  });

  // Render text with highlighted keywords
  const renderFormattedText = () => {
    let result = text;
    const parts: React.ReactNode[] = [];
    const words = text.split(' ');

    words.forEach((word, index) => {
      const cleanWord = word.replace(/[.,!]/g, '').toLowerCase();
      const isHighlighted = highlightWords.some(
        (h) => h.toLowerCase() === cleanWord
      );

      if (isHighlighted) {
        parts.push(
          <span
            key={index}
            style={{
              color: '#fbbf24',
              fontWeight: 900,
              textShadow: '0 0 16px rgba(251, 191, 36, 0.7)',
            }}
          >
            {word}{' '}
          </span>
        );
      } else {
        parts.push(
          <span key={index} style={{ color: '#ffffff' }}>
            {word}{' '}
          </span>
        );
      }
    });

    return parts;
  };

  return (
    <div
      style={{
        position: 'absolute',
        bottom: 80,
        left: 40,
        right: 40,
        display: 'flex',
        flexDirection: 'column',
        alignItems: 'center',
        transform: `translateY(${translateY}px)`,
        opacity,
        zIndex: 100,
      }}
    >
      {/* Category Badge */}
      <div
        style={{
          backgroundColor: badgeColor,
          color: '#070a0e',
          fontFamily: 'sans-serif',
          fontWeight: 900,
          fontSize: 22,
          letterSpacing: 3,
          textTransform: 'uppercase',
          padding: '8px 24px',
          borderRadius: 999,
          marginBottom: 16,
          boxShadow: `0 6px 20px ${badgeColor}66`,
        }}
      >
        {badge}
      </div>

      {/* Main Subtitle Box */}
      <div
        style={{
          width: '100%',
          backgroundColor: 'rgba(7, 10, 17, 0.88)',
          backdropFilter: 'blur(16px)',
          border: '1.5px solid rgba(56, 189, 248, 0.35)',
          borderRadius: 24,
          padding: '24px 32px',
          textAlign: 'center',
          boxShadow: '0 20px 40px rgba(0, 0, 0, 0.85)',
        }}
      >
        <p
          style={{
            margin: 0,
            fontSize: 34,
            fontWeight: 700,
            lineHeight: 1.4,
            fontFamily: "'Segoe UI', Roboto, Helvetica, Arial, sans-serif",
            letterSpacing: '-0.5px',
          }}
        >
          {renderFormattedText()}
        </p>
      </div>
    </div>
  );
};
