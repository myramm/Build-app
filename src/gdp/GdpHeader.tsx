import React from 'react';

interface GdpHeaderProps {
  currentYear: number;
}

export const GdpHeader: React.FC<GdpHeaderProps> = ({ currentYear }) => {
  const yearInt = Math.floor(currentYear);

  return (
    <div
      style={{
        position: 'absolute',
        top: 0,
        left: 0,
        right: 0,
        padding: '50px 48px 20px 48px',
        display: 'flex',
        justifyContent: 'space-between',
        alignItems: 'flex-start',
        zIndex: 40,
        borderBottom: '1px solid rgba(255, 255, 255, 0.1)',
        backgroundColor: 'rgba(5, 7, 15, 0.9)',
        backdropFilter: 'blur(10px)',
      }}
    >
      <div>
        <div
          style={{
            fontFamily: "'Fira Code', monospace",
            fontSize: 20,
            color: '#10B981',
            letterSpacing: '0.1em',
            textTransform: 'uppercase',
            fontWeight: 800,
          }}
        >
          GLOBAL ECONOMY DATA-VIZ · 1950–2026
        </div>
        <h1
          style={{
            margin: '8px 0 0 0',
            fontSize: 48,
            fontWeight: 900,
            fontFamily: "'Space Grotesk', sans-serif",
            color: '#FFFFFF',
            letterSpacing: '-1px',
          }}
        >
          TOP 10 GDP NEGARA DI DUNIA
        </h1>
        <p
          style={{
            margin: '6px 0 0 0',
            fontSize: 22,
            color: '#94A3B8',
            fontFamily: "'DM Sans', sans-serif",
          }}
        >
          Nilai Nominal dalam Dolar AS (USD)
        </p>
      </div>

      {/* Giant Animated Year Watermark */}
      <div
        style={{
          fontFamily: "'Space Grotesk', monospace",
          fontSize: 84,
          fontWeight: 900,
          color: '#F8FAFC',
          lineHeight: 1,
          letterSpacing: '-2px',
          backgroundColor: '#0F172A',
          padding: '12px 24px',
          borderRadius: 16,
          border: '2px solid #1E293B',
          boxShadow: '0 10px 25px rgba(0,0,0,0.5)',
        }}
      >
        {yearInt}
      </div>
    </div>
  );
};
