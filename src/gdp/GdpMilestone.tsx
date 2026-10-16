import React from 'react';
import { Milestone } from './types';

interface GdpMilestoneProps {
  milestone: Milestone | null;
}

export const GdpMilestone: React.FC<GdpMilestoneProps> = ({ milestone }) => {
  if (!milestone) return null;

  return (
    <div
      style={{
        position: 'absolute',
        bottom: 80,
        left: 48,
        right: 48,
        backgroundColor: '#0F172A',
        border: '2px solid #1E293B',
        borderRadius: 16,
        padding: '24px 32px',
        display: 'flex',
        alignItems: 'center',
        gap: 24,
        zIndex: 50,
        boxShadow: '0 20px 40px rgba(0, 0, 0, 0.7)',
        fontFamily: "'Space Grotesk', sans-serif",
      }}
    >
      <div
        style={{
          backgroundColor: '#E11D48',
          color: '#FFFFFF',
          fontWeight: 900,
          fontSize: 24,
          padding: '12px 18px',
          borderRadius: 10,
          fontFamily: 'monospace',
          lineHeight: 1,
        }}
      >
        {milestone.year}
      </div>

      <div style={{ flex: 1 }}>
        <div
          style={{
            fontSize: 26,
            fontWeight: 800,
            color: '#F8FAFC',
            letterSpacing: '-0.3px',
          }}
        >
          {milestone.title}
        </div>
        <div
          style={{
            fontSize: 20,
            color: '#94A3B8',
            marginTop: 4,
            fontFamily: "'DM Sans', sans-serif",
            lineHeight: 1.4,
          }}
        >
          {milestone.description}
        </div>
      </div>
    </div>
  );
};
