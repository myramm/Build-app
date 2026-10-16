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
      {/* UI/UX Pro Max Precision Indicator Bar */}
      <div
        style={{
          position: 'absolute',
          top: 0,
          left: 0,
          right: 0,
          height: 4,
          backgroundColor: '#1E1B4B',
        }}
      >
        <div
          style={{
            height: '100%',
            width: `${progress}%`,
            backgroundColor: '#E11D48',
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
          borderBottom: '1px solid #1E1B4B',
          paddingBottom: 16,
        }}
      >
        {/* Step Badge & Title */}
        <div
          style={{
            display: 'flex',
            alignItems: 'center',
            gap: 14,
            fontFamily: "'Space Grotesk', 'Segoe UI', sans-serif",
          }}
        >
          <div
            style={{
              backgroundColor: '#E11D48',
              color: '#FFFFFF',
              fontWeight: 800,
              fontSize: 16,
              borderRadius: 6,
              padding: '4px 10px',
              fontFamily: 'monospace',
            }}
          >
            {String(stepNumber).padStart(2, '0')} / {String(totalSteps).padStart(2, '0')}
          </div>
          <span
            style={{
              color: '#F8FAFC',
              fontWeight: 700,
              letterSpacing: '-0.5px',
              textTransform: 'uppercase',
              fontSize: 22,
            }}
          >
            {step}
          </span>
        </div>

        {/* Tech Stack Badge */}
        <div
          style={{
            fontFamily: 'monospace',
            fontSize: 15,
            color: '#94A3B8',
            letterSpacing: '0.05em',
            backgroundColor: '#0F0F23',
            border: '1px solid #1E1B4B',
            padding: '6px 14px',
            borderRadius: 6,
          }}
        >
          REMOTION 4.0 · 60 FPS
        </div>
      </div>
    </div>
  );
};
