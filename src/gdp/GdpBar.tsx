import React from 'react';
import { CountryRanked } from './types';

interface GdpBarProps {
  country: CountryRanked;
  maxGdp: number;
}

export const GdpBar: React.FC<GdpBarProps> = ({ country, maxGdp }) => {
  // Bar height and vertical positioning
  const slotHeight = 114;
  const startTop = 224;
  const targetTop = startTop + (country.rank - 1) * slotHeight;

  // Bar width percentage relative to #1 country
  // Minimum width 14% so flag, tag, and name are always readable
  const widthPercent = Math.max(14, Math.min(100, (country.gdp / maxGdp) * 100));

  // Format GDP value ($B or $T)
  const formatGdp = (val: number): string => {
    if (val >= 1000) {
      return `$${(val / 1000).toFixed(2)} Triliun`;
    }
    return `$${val.toFixed(1)} Miliar`;
  };

  const isLeader = country.rank === 1;

  return (
    <div
      style={{
        position: 'absolute',
        top: targetTop,
        left: 44,
        right: 44,
        height: 88,
        display: 'flex',
        alignItems: 'center',
        transition: 'top 0.28s cubic-bezier(0.25, 1, 0.5, 1)',
        zIndex: 25 - country.rank,
      }}
    >
      {/* Rank Number & Delta Indicator */}
      <div
        style={{
          width: 64,
          display: 'flex',
          flexDirection: 'column',
          alignItems: 'center',
          justifyContent: 'center',
          marginRight: 14,
        }}
      >
        <div
          style={{
            fontFamily: "'Space Grotesk', monospace",
            fontSize: country.rank <= 3 ? 30 : 24,
            fontWeight: 900,
            color:
              country.rank === 1
                ? '#F59E0B'
                : country.rank === 2
                ? '#E2E8F0'
                : country.rank === 3
                ? '#D97706'
                : '#94A3B8',
            lineHeight: 1,
            textShadow:
              country.rank === 1 ? '0 0 12px rgba(245, 158, 11, 0.6)' : 'none',
          }}
        >
          #{country.rank}
        </div>

        {/* Dynamic Overtake Indicator */}
        {country.rankDelta !== undefined && country.rankDelta !== 0 && (
          <div
            style={{
              fontFamily: "'Space Grotesk', sans-serif",
              fontSize: 12,
              fontWeight: 800,
              color: country.rankDelta > 0 ? '#10B981' : '#EF4444',
              marginTop: 2,
              lineHeight: 1,
            }}
          >
            {country.rankDelta > 0 ? `▲ +${country.rankDelta}` : `▼ ${country.rankDelta}`}
          </div>
        )}
      </div>

      {/* Bar Container */}
      <div
        style={{
          flex: 1,
          height: '100%',
          position: 'relative',
          display: 'flex',
          alignItems: 'center',
        }}
      >
        {/* Background track guide */}
        <div
          style={{
            position: 'absolute',
            inset: 0,
            borderRadius: 16,
            backgroundColor: 'rgba(255, 255, 255, 0.02)',
            border: '1px solid rgba(255, 255, 255, 0.04)',
          }}
        />

        {/* Animated Bar Fill with Gradient & Subtle Glow */}
        <div
          style={{
            position: 'absolute',
            left: 0,
            top: 0,
            bottom: 0,
            width: `${widthPercent}%`,
            background: country.gradient,
            borderRadius: 16,
            boxShadow: isLeader
              ? '0 6px 20px rgba(59, 130, 246, 0.4), inset 0 1px 0 rgba(255, 255, 255, 0.4)'
              : '0 4px 14px rgba(0, 0, 0, 0.35), inset 0 1px 0 rgba(255, 255, 255, 0.2)',
            border: isLeader
              ? '1.5px solid rgba(255, 255, 255, 0.6)'
              : '1px solid rgba(255, 255, 255, 0.15)',
            transition: 'width 0.1s linear',
          }}
        />

        {/* Bar Content: Flag, Tag, Name & Value */}
        <div
          style={{
            position: 'relative',
            zIndex: 10,
            display: 'flex',
            alignItems: 'center',
            justifyContent: 'space-between',
            width: '100%',
            padding: '0 20px',
            fontFamily: "'Space Grotesk', sans-serif",
          }}
        >
          {/* Flag + Country Identity */}
          <div style={{ display: 'flex', alignItems: 'center', gap: 12 }}>
            <span style={{ fontSize: 34, lineHeight: 1 }}>{country.flag}</span>
            
            {/* Country ISO Tag Badge */}
            <span
              style={{
                fontFamily: "'Fira Code', monospace",
                fontSize: 14,
                fontWeight: 800,
                color: '#FFFFFF',
                backgroundColor: 'rgba(0, 0, 0, 0.35)',
                padding: '3px 8px',
                borderRadius: 6,
                border: '1px solid rgba(255, 255, 255, 0.2)',
                lineHeight: 1,
              }}
            >
              {country.id}
            </span>

            <span
              style={{
                fontSize: 24,
                fontWeight: 800,
                color: '#FFFFFF',
                textShadow: '0 2px 6px rgba(0, 0, 0, 0.8)',
                letterSpacing: '-0.3px',
              }}
            >
              {country.name}
            </span>
          </div>

          {/* GDP Value Counter */}
          <div
            style={{
              fontSize: 26,
              fontWeight: 900,
              color: '#FFFFFF',
              fontFamily: "'Space Grotesk', monospace",
              textShadow: '0 2px 8px rgba(0, 0, 0, 0.9)',
              letterSpacing: '-0.5px',
              backgroundColor: 'rgba(0, 0, 0, 0.28)',
              padding: '6px 14px',
              borderRadius: 10,
              border: '1px solid rgba(255, 255, 255, 0.15)',
            }}
          >
            {formatGdp(country.gdp)}
          </div>
        </div>
      </div>
    </div>
  );
};
