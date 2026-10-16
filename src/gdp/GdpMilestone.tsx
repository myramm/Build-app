import React from 'react';
import { Milestone } from './types';

interface GdpMilestoneProps {
  milestone: Milestone | null;
  frame: number;
}

export const GdpMilestone: React.FC<GdpMilestoneProps> = ({ milestone, frame }) => {
  if (!milestone) return null;

  const framesIn = frame - milestone.startFrame;
  const framesLeft = milestone.endFrame - frame;
  const enterProgress = Math.min(1, Math.max(0, framesIn / 12));
  const exitProgress = Math.min(1, Math.max(0, framesLeft / 12));
  const opacity = Math.min(enterProgress, exitProgress);
  const translateY = (1 - enterProgress) * 8;

  return (
    <div
      style={{
        position: 'absolute',
        bottom: 80,
        left: 48,
        right: 48,
        zIndex: 60,
        opacity,
        transform: `translateY(${translateY}px)`,
      }}
    >
      <div
        style={{
          padding: '20px 26px',
          backgroundColor: '#0D111A',
          borderRadius: 14,
          borderLeft: '4px solid #38BDF8',
          borderTop: '1px solid rgba(255, 255, 255, 0.08)',
          borderRight: '1px solid rgba(255, 255, 255, 0.08)',
          borderBottom: '1px solid rgba(255, 255, 255, 0.08)',
          boxShadow: '0 12px 30px rgba(0, 0, 0, 0.6)',
        }}
      >
        <div
          style={{
            display: 'flex',
            justifyContent: 'space-between',
            alignItems: 'center',
            marginBottom: 4,
          }}
        >
          <span
            style={{
              fontFamily: "'Space Grotesk', monospace",
              fontSize: 14,
              fontWeight: 800,
              color: '#38BDF8',
              letterSpacing: '0.08em',
              textTransform: 'uppercase',
            }}
          >
            PERISTIWA EKONOMI · {milestone.year}
          </span>
          <span
            style={{
              fontFamily: "'DM Sans', sans-serif",
              fontSize: 13,
              color: '#64748B',
              fontWeight: 500,
            }}
          >
            Ref: {milestone.verifiedSource}
          </span>
        </div>

        <h3
          style={{
            margin: '2px 0 0 0',
            fontFamily: "'Space Grotesk', sans-serif",
            fontSize: 22,
            fontWeight: 800,
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
            fontSize: 17,
            color: '#94A3B8',
            lineHeight: 1.35,
          }}
        >
          {milestone.description}
        </p>
      </div>
    </div>
  );
};
