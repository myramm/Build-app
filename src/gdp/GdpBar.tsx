import React from 'react';
import { Flag } from './Flag';
import { CountryRanked } from './types';

interface GdpBarProps {
  country: CountryRanked;
  maxGdp: number;
}

export const GdpBar: React.FC<GdpBarProps> = ({ country, maxGdp }) => {
  // Editorial spacing: 114px slot, 84px bar height (30px breathing space)
  const slotHeight = 114;
  const startTop = 224;
  const targetTop = startTop + (country.rank - 1) * slotHeight;

  // Relative width (clamped between 18% and 100%)
  const widthPercent = Math.max(18, Math.min(100, (country.gdp / maxGdp) * 100));

  // Format GDP value ($B or $T)
  const formatGdp = (val: number): string => {
    if (val >= 1000) {
      return `$${(val / 1000).toFixed(2)} Triliun`;
    }
    return `$${val.toFixed(1)} Miliar`;
  };

  const isTop3 = country.rank <= 3;

  return (
    <div
      style={{
        position: 'absolute',
        top: targetTop,
        left: 48,
        right: 48,
        height: 84,
        display: 'flex',
        alignItems: 'center',
        transition: 'top 0.35s cubic-bezier(0.25, 1, 0.5, 1)',
        zIndex: 25 - country.rank,
      }}
    >
      {/* Rank & Change Indicator */}
      <div
        style={{
          width: 58,
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
            fontSize: isTop3 ? 28 : 22,
            fontWeight: 800,
            color:
              country.rank === 1
                ? '#F59E0B'
                : country.rank === 2
                ? '#E2E8F0'
                : country.rank === 3
                ? '#D97706'
                : '#94A3B8',
            lineHeight: 1,
          }}
        >
          #{country.rank}
        </div>

        {/* Simple Editorial Rank Delta */}
        {country.rankDelta !== undefined && country.rankDelta !== 0 && (
          <div
            style={{
              fontFamily: "'Space Grotesk', sans-serif",
              fontSize: 11,
              fontWeight: 800,
              color: country.rankDelta > 0 ? '#10B981' : '#EF4444',
              marginTop: 3,
              lineHeight: 1,
            }}
          >
            {country.rankDelta > 0 ? `▲ +${country.rankDelta}` : `▼ ${country.rankDelta}`}
          </div>
        )}
      </div>

      {/* Bar Horizontal Track */}
      <div
        style={{
          flex: 1,
          height: '100%',
          position: 'relative',
          display: 'flex',
          alignItems: 'center',
        }}
      >
        {/* Subtle background track */}
        <div
          style={{
            position: 'absolute',
            inset: 0,
            borderRadius: 10,
            backgroundColor: 'rgba(255, 255, 255, 0.02)',
          }}
        />

        {/* Bar Fill (Clean solid/subtle gradient with consistent country color) */}
        <div
          style={{
            position: 'absolute',
            left: 0,
            top: 0,
            bottom: 0,
            width: `${widthPercent}%`,
            background: country.gradient,
            borderRadius: 10,
            boxShadow: '0 2px 8px rgba(0, 0, 0, 0.3)',
            transition: 'width 0.1s linear',
          }}
        />

        {/* Content on Bar: Flag, Country Name & Value */}
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
          {/* Country Identity */}
          <div style={{ display: 'flex', alignItems: 'center', gap: 12 }}>
            <Flag countryCode={country.id} width={38} height={26} />
            <span
              style={{
                fontSize: 24,
                fontWeight: 800,
                color: '#FFFFFF',
                letterSpacing: '-0.3px',
                textShadow: '0 1px 4px rgba(0, 0, 0, 0.8)',
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
              fontFamily: "'Space Grotesk', monospace",
              letterSpacing: '-0.5px',
              textShadow: '0 2px 6px rgba(0, 0, 0, 0.9)',
            }}
          >
            {formatGdp(country.gdp)}
          </div>
        </div>
      </div>
    </div>
  );
};
