import React from 'react';
import { CountryRanked } from './types';

interface GdpBarProps {
  country: CountryRanked;
  maxGdp: number;
}

export const GdpBar: React.FC<GdpBarProps> = ({ country, maxGdp }) => {
  // Bar height and slot calculation
  const slotHeight = 116;
  const startTop = 230;
  const targetTop = startTop + (country.rank - 1) * slotHeight;

  // Bar width percentage relative to #1 country
  const widthPercent = Math.max(8, Math.min(100, (country.gdp / maxGdp) * 100));

  // Format GDP value ($B or $T)
  const formatGdp = (val: number): string => {
    if (val >= 1000) {
      return `$${(val / 1000).toFixed(2)} Triliun`;
    }
    return `$${val.toLocaleString()} Miliar`;
  };

  return (
    <div
      style={{
        position: 'absolute',
        top: targetTop,
        left: 48,
        right: 48,
        height: 88,
        display: 'flex',
        alignItems: 'center',
        transition: 'top 0.25s cubic-bezier(0.2, 0, 0, 1)',
        zIndex: 20 - country.rank,
      }}
    >
      {/* Rank Number Badge */}
      <div
        style={{
          width: 52,
          fontFamily: "'Space Grotesk', monospace",
          fontSize: 26,
          fontWeight: 800,
          color: country.rank <= 3 ? '#F59E0B' : '#94A3B8',
          textAlign: 'right',
          marginRight: 18,
        }}
      >
        #{country.rank}
      </div>

      {/* Bar Container Area */}
      <div
        style={{
          flex: 1,
          height: '100%',
          position: 'relative',
          display: 'flex',
          alignItems: 'center',
        }}
      >
        {/* Animated Bar Background Fill */}
        <div
          style={{
            position: 'absolute',
            left: 0,
            top: 0,
            bottom: 0,
            width: `${widthPercent}%`,
            backgroundColor: country.color,
            borderRadius: 12,
            boxShadow: '0 4px 15px rgba(0, 0, 0, 0.4)',
            transition: 'width 0.1s linear',
          }}
        />

        {/* Content on top of bar */}
        <div
          style={{
            position: 'relative',
            zIndex: 10,
            display: 'flex',
            alignItems: 'center',
            justifyContent: 'space-between',
            width: '100%',
            padding: '0 24px',
            fontFamily: "'Space Grotesk', sans-serif",
          }}
        >
          {/* Flag & Country Name */}
          <div style={{ display: 'flex', alignItems: 'center', gap: 14 }}>
            <span style={{ fontSize: 36, lineHeight: 1 }}>{country.flag}</span>
            <span
              style={{
                fontSize: 26,
                fontWeight: 800,
                color: '#FFFFFF',
                textShadow: '0 2px 8px rgba(0,0,0,0.8)',
                letterSpacing: '-0.3px',
              }}
            >
              {country.name}
            </span>
          </div>

          {/* GDP Value Label */}
          <div
            style={{
              fontSize: 26,
              fontWeight: 900,
              color: '#FFFFFF',
              fontFamily: "'Fira Code', monospace",
              textShadow: '0 2px 8px rgba(0,0,0,0.8)',
            }}
          >
            {formatGdp(country.gdp)}
          </div>
        </div>
      </div>
    </div>
  );
};
