import React from 'react';
import { useCurrentFrame, useVideoConfig } from 'remotion';

interface TutorialHeaderProps {
  step: string;
  stepNumber: number;
  totalSteps?: number;
}

export const TutorialHeader: React.FC<TutorialHeaderProps> = ({
  step,
  stepNumber,
  totalSteps = 7,
}) => {
  const frame = useCurrentFrame();
  const { durationInFrames } = useVideoConfig();

  const progress = (frame / durationInFrames) * 100;

  return (
    <div
      style={{
        position: 'absolute',
        top: 0,
        left: 0,
        right: 0,
        zIndex: 50,
        padding: '0 40px',
      }}
    >
      {/* Precision Top Progress Bar (Clean line, zero glow) */}
      <div
        style={{
          position: 'absolute',
          top: 0,
          left: 0,
          right: 0,
          height: 4,
          backgroundColor: '#1e293b',
        }}
      >
        <div
          style={{
            height: '100%',
            width: `${progress}%`,
            backgroundColor: '#10b981',
          }}
        />
      </div>

      {/* Structured Editorial Header */}
      <div
        style={{
          display: 'flex',
          justifyContent: 'space-between',
          alignItems: 'center',
          paddingTop: 36,
          borderBottom: '1px solid #1e293b',
          paddingBottom: 16,
        }}
      >
        {/* Step Indicator */}
        <div
          style={{
            display: 'flex',
            alignItems: 'center',
            gap: 12,
            fontFamily: "'Fira Code', Consolas, monospace",
            fontSize: 20,
          }}
        >
          <span style={{ color: '#10b981', fontWeight: 800 }}>
            {String(stepNumber).padStart(2, '0')}
          </span>
          <span style={{ color: '#64748b' }}>/</span>
          <span style={{ color: '#64748b' }}>
            {String(totalSteps).padStart(2, '0')}
          </span>
          <span
            style={{
              marginLeft: 8,
              color: '#f8fafc',
              fontWeight: 700,
              letterSpacing: '0.05em',
              textTransform: 'uppercase',
              fontSize: 20,
            }}
          >
            {step}
          </span>
        </div>

        {/* Project Tag */}
        <div
          style={{
            fontFamily: "'Fira Code', Consolas, monospace",
            fontSize: 16,
            color: '#94a3b8',
            letterSpacing: '0.05em',
          }}
        >
          REMOTION 4.0 · 60 FPS
        </div>
      </div>
    </div>
  );
};
