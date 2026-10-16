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
      }}
    >
      {/* Top Global Progress Bar */}
      <div
        style={{
          height: 10,
          backgroundColor: 'rgba(255, 255, 255, 0.1)',
          width: '100%',
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

      {/* Step Badge */}
      <div
        style={{
          display: 'flex',
          justifyContent: 'center',
          paddingTop: 36,
        }}
      >
        <div
          style={{
            display: 'flex',
            alignItems: 'center',
            gap: 12,
            backgroundColor: 'rgba(15, 23, 42, 0.85)',
            border: '1.5px solid rgba(56, 189, 248, 0.5)',
            borderRadius: 999,
            padding: '10px 24px',
            boxShadow: '0 8px 24px rgba(0, 0, 0, 0.6)',
          }}
        >
          <span
            style={{
              backgroundColor: '#38bdf8',
              color: '#030712',
              fontWeight: 900,
              fontSize: 18,
              borderRadius: 999,
              padding: '4px 12px',
              fontFamily: 'monospace',
            }}
          >
            STEP {stepNumber}/{totalSteps}
          </span>
          <span
            style={{
              color: '#ffffff',
              fontSize: 22,
              fontWeight: 800,
              fontFamily: 'sans-serif',
              letterSpacing: 1,
              textTransform: 'uppercase',
            }}
          >
            {step}
          </span>
        </div>
      </div>
    </div>
  );
};
