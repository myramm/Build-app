import React from 'react';
import { TimelineState } from './types';

interface GdpHeaderProps {
  timeline: TimelineState;
}

export const GdpHeader: React.FC<GdpHeaderProps> = ({ timeline }) => {
  const isProjection = timeline.isProjection;
  const is2026 = timeline.currentYear === 2026;

  // Exact editorial status label based on year
  const displayStatus = is2026
    ? 'PROYEKSI 2026'
    : isProjection
    ? 'PROYEKSI IMF WEO'
    : timeline.currentYear >= 2024
    ? 'ESTIMASI AWAL 2024'
    : timeline.currentYear >= 1960
    ? 'DATA AKTUAL RESMI'
    : 'ESTIMASI HISTORIS';

  const badgeBg = isProjection
    ? 'rgba(245, 158, 11, 0.15)'
    : timeline.currentYear >= 2024
    ? 'rgba(56, 189, 248, 0.15)'
    : timeline.currentYear >= 1960
    ? 'rgba(16, 185, 129, 0.15)'
    : 'rgba(148, 163, 184, 0.12)';

  const badgeBorder = isProjection
    ? '1px solid rgba(245, 158, 11, 0.4)'
    : timeline.currentYear >= 2024
    ? '1px solid rgba(56, 189, 248, 0.35)'
    : timeline.currentYear >= 1960
    ? '1px solid rgba(16, 185, 129, 0.35)'
    : '1px solid rgba(148, 163, 184, 0.25)';

  return (
    <div
      style={{
        position: 'absolute',
        top: 0,
        left: 0,
        right: 0,
        padding: '50px 48px 24px 48px',
        display: 'flex',
        justifyContent: 'space-between',
        alignItems: 'flex-start',
        zIndex: 50,
        backgroundColor: '#07090E',
        borderBottom: '1px solid rgba(255, 255, 255, 0.08)',
      }}
    >
      {/* Editorial Title & Methodology */}
      <div>
        <h1
          style={{
            margin: 0,
            fontSize: 48,
            fontWeight: 900,
            fontFamily: "'Space Grotesk', -apple-system, sans-serif",
            color: '#FFFFFF',
            letterSpacing: '-1.5px',
            lineHeight: 1.05,
          }}
        >
          GDP NEGARA DI DUNIA
        </h1>

        <div
          style={{
            display: 'flex',
            alignItems: 'center',
            gap: 12,
            marginTop: 8,
          }}
        >
          <span
            style={{
              fontSize: 22,
              fontWeight: 700,
              fontFamily: "'Space Grotesk', sans-serif",
              color: '#CBD5E1',
              letterSpacing: '-0.3px',
            }}
          >
            1950 – 2026
          </span>
          <span style={{ color: 'rgba(255, 255, 255, 0.2)' }}>•</span>
          <span
            style={{
              fontSize: 18,
              fontWeight: 500,
              fontFamily: "'DM Sans', sans-serif",
              color: '#94A3B8',
            }}
          >
            GDP nominal dalam dolar AS
          </span>
        </div>
      </div>

      {/* Prominent Editorial Year & Status Badge */}
      <div
        style={{
          display: 'flex',
          flexDirection: 'column',
          alignItems: 'flex-end',
        }}
      >
        {/* Dynamic Status Badge */}
        <div
          style={{
            display: 'inline-flex',
            alignItems: 'center',
            gap: 8,
            padding: '6px 14px',
            borderRadius: 8,
            backgroundColor: badgeBg,
            border: badgeBorder,
            marginBottom: 6,
          }}
        >
          <span
            style={{
              width: 7,
              height: 7,
              borderRadius: '50%',
              backgroundColor: timeline.statusBadgeColor,
            }}
          />
          <span
            style={{
              fontFamily: "'Space Grotesk', monospace",
              fontSize: 14,
              fontWeight: 800,
              letterSpacing: '0.08em',
              textTransform: 'uppercase',
              color: timeline.statusBadgeColor,
            }}
          >
            {displayStatus}
          </span>
        </div>

        {/* Large Year Display */}
        <div
          style={{
            fontFamily: "'Space Grotesk', monospace",
            fontSize: 72,
            fontWeight: 900,
            color: '#FFFFFF',
            lineHeight: 1,
            letterSpacing: '-2px',
          }}
        >
          {timeline.currentYear}
        </div>

        {/* Subtle Progress Bar (1950 to 2026) */}
        <div
          style={{
            width: 140,
            height: 4,
            backgroundColor: 'rgba(255, 255, 255, 0.08)',
            borderRadius: 2,
            marginTop: 8,
            overflow: 'hidden',
          }}
        >
          <div
            style={{
              width: `${timeline.progressPercent}%`,
              height: '100%',
              backgroundColor: timeline.statusBadgeColor,
              transition: 'width 0.1s linear',
            }}
          />
        </div>
      </div>
    </div>
  );
};
