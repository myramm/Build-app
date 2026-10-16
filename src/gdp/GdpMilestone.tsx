import React from 'react';
import { Milestone } from './types';

interface GdpMilestoneProps {
  milestone: Milestone | null;
  frame: number;
}

export const GdpMilestone: React.FC<GdpMilestoneProps> = ({ milestone, frame }) => {
  if (!milestone) return null;

  // Calculate entrance/exit opacity
  const framesIn = frame - milestone.startFrame;
  const framesLeft = milestone.endFrame - frame;
  const enterProgress = Math.min(1, Math.max(0, framesIn / 12));
  const exitProgress = Math.min(1, Math.max(0, framesLeft / 12));
  const opacity = Math.min(enterProgress, exitProgress);
  const translateY = (1 - enterProgress) * 12;

  return (
    <div
      style={{
        position: 'absolute',
        bottom: 70,
        left: 44,
        right: 44,
        zIndex: 60,
        opacity,
        transform: `translateY(${translateY}px)`,
        transition: 'transform 0.2s ease, opacity 0.2s ease',
      }}
    >
      <div
        style={{
          display: 'flex',
          alignItems: 'center',
          gap: 20,
          padding: '20px 28px',
          backgroundColor: 'rgba(8, 12, 26, 0.94)',
          borderRadius: 22,
          border: '1px solid rgba(56, 189, 248, 0.3)',
          boxShadow: '0 16px 40px rgba(0, 0, 0, 0.7), 0 0 25px rgba(56, 189, 248, 0.15)',
          backdropFilter: 'blur(20px)',
        }}
      >
        {/* Pulsing Event Icon */}
        <div
          style={{
            width: 54,
            height: 54,
            borderRadius: 16,
            background: 'linear-gradient(135deg, #0284C7 0%, #38BDF8 100%)',
            display: 'flex',
            alignItems: 'center',
            justifyContent: 'center',
            fontSize: 26,
            flexShrink: 0,
            boxShadow: '0 6px 16px rgba(56, 189, 248, 0.4)',
          }}
        >
          ⚡
        </div>

        {/* Milestone Text Info */}
        <div style={{ flex: 1 }}>
          <div
            style={{
              display: 'flex',
              alignItems: 'center',
              gap: 10,
              fontFamily: "'Space Grotesk', monospace",
              fontSize: 15,
              fontWeight: 800,
              color: '#38BDF8',
              letterSpacing: '0.1em',
              textTransform: 'uppercase',
            }}
          >
            <span>MILESTONE HISTORIS</span>
            <span>•</span>
            <span>
              {milestone.year}
            </span>
          </div>

          <h3
            style={{
              margin: '3px 0 0 0',
              fontFamily: "'Space Grotesk', sans-serif",
              fontSize: 24,
              fontWeight: 900,
              color: '#FFFFFF',
              letterSpacing: '-0.3px',
            }}
          >
            {milestone.title}
          </h3>

          <p
            style={{
              margin: '4px 0 0 0',
              fontFamily: "'DM Sans', sans-serif",
              fontSize: 18,
              color: '#CBD5E1',
              lineHeight: 1.35,
            }}
          >
            {milestone.description}
          </p>
        </div>
      </div>
    </div>
  );
};
