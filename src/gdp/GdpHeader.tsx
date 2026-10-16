import React from 'react';
import { MonthDate } from './types';

interface GdpHeaderProps {
  date: MonthDate;
}

export const GdpHeader: React.FC<GdpHeaderProps> = ({ date }) => {
  return (
    <div
      style={{
        position: 'absolute',
        top: 0,
        left: 0,
        right: 0,
        padding: '48px 44px 22px 44px',
        display: 'flex',
        justifyContent: 'space-between',
        alignItems: 'center',
        zIndex: 50,
        borderBottom: '1px solid rgba(255, 255, 255, 0.08)',
        backgroundColor: 'rgba(5, 7, 17, 0.94)',
        backdropFilter: 'blur(16px)',
      }}
    >
      <div>
        {/* Live Monthly Status Eyebrow */}
        <div
          style={{
            display: 'flex',
            alignItems: 'center',
            gap: 8,
            fontFamily: "'Space Grotesk', monospace",
            fontSize: 16,
            color: '#10B981',
            letterSpacing: '0.12em',
            textTransform: 'uppercase',
            fontWeight: 800,
          }}
        >
          <span
            style={{
              width: 8,
              height: 8,
              borderRadius: '50%',
              backgroundColor: '#10B981',
              boxShadow: '0 0 10px #10B981',
            }}
          />
          DATA-VIZ HISTORIS · RESOLUSI PER BULAN
        </div>

        {/* Main Title */}
        <h1
          style={{
            margin: '6px 0 0 0',
            fontSize: 44,
            fontWeight: 900,
            fontFamily: "'Space Grotesk', sans-serif",
            color: '#FFFFFF',
            letterSpacing: '-1px',
            lineHeight: 1.1,
          }}
        >
          TOP 10 GDP NEGARA DI DUNIA
        </h1>

        {/* Subtitle */}
        <p
          style={{
            margin: '4px 0 0 0',
            fontSize: 19,
            color: '#94A3B8',
            fontFamily: "'DM Sans', sans-serif",
            fontWeight: 500,
          }}
        >
          Nilai Nominal dalam Dolar AS (USD) · 1950 – 2026
        </p>
      </div>

      {/* Modern High-End Date Display (Bulan + Tahun) */}
      <div
        style={{
          display: 'flex',
          flexDirection: 'column',
          alignItems: 'flex-end',
          justifyContent: 'center',
          backgroundColor: '#0A0F1D',
          padding: '12px 28px',
          borderRadius: 20,
          border: '1px solid rgba(255, 255, 255, 0.12)',
          boxShadow: '0 12px 30px rgba(0, 0, 0, 0.6), inset 0 1px 0 rgba(255, 255, 255, 0.1)',
          minWidth: 240,
        }}
      >
        {/* Month Label with accent badge */}
        <div
          style={{
            fontFamily: "'Space Grotesk', sans-serif",
            fontSize: 22,
            fontWeight: 800,
            letterSpacing: '0.15em',
            textTransform: 'uppercase',
            color: '#38BDF8',
            lineHeight: 1,
            marginBottom: 4,
          }}
        >
          {date.monthName}
        </div>

        {/* Year Label */}
        <div
          style={{
            fontFamily: "'Space Grotesk', monospace",
            fontSize: 64,
            fontWeight: 900,
            color: '#FFFFFF',
            lineHeight: 1,
            letterSpacing: '-2px',
          }}
        >
          {date.year}
        </div>

        {/* 12-Segment Micro Calendar Indicator */}
        <div
          style={{
            display: 'flex',
            gap: 4,
            marginTop: 8,
            alignItems: 'center',
          }}
        >
          {Array.from({ length: 12 }).map((_, i) => {
            const isCurrent = i + 1 === date.month;
            const isPassed = i + 1 < date.month;
            return (
              <div
                key={i}
                style={{
                  width: isCurrent ? 14 : 6,
                  height: 5,
                  borderRadius: 3,
                  backgroundColor: isCurrent ? '#38BDF8' : isPassed ? '#1E293B' : '#0F172A',
                  transition: 'all 0.1s ease',
                  boxShadow: isCurrent ? '0 0 8px #38BDF8' : 'none',
                }}
              />
            );
          })}
        </div>
      </div>
    </div>
  );
};
