import React from 'react';
import {
  AbsoluteFill,
  interpolate,
  spring,
  useCurrentFrame,
  useVideoConfig,
} from 'remotion';
import { SubtitleBar } from '../components/SubtitleBar';

export const Scene6Outro: React.FC = () => {
  const frame = useCurrentFrame();
  const { fps } = useVideoConfig();

  // Jet flight zoom & elevation
  const jetY = interpolate(frame, [0, 400], [250, -150], {
    extrapolateRight: 'clamp',
  });
  const jetScale = interpolate(frame, [0, 200, 400], [0.8, 1.1, 1.4], {
    extrapolateRight: 'clamp',
  });

  // Call to action button pulse & bounce
  const ctaScale = spring({
    frame: frame - 120,
    fps,
    config: { damping: 10, mass: 0.6 },
  });
  const ctaGlow = Math.sin(frame / 12) * 12 + 18;

  return (
    <AbsoluteFill
      style={{
        backgroundColor: '#05070d',
        overflow: 'hidden',
      }}
    >
      {/* Epic Stratosphere & Space View */}
      <AbsoluteFill
        style={{
          background:
            'radial-gradient(circle at 50% 80%, #0369a1 0%, #0f172a 45%, #02040a 100%)',
        }}
      />

      {/* Earth Horizon Curvature */}
      <div
        style={{
          position: 'absolute',
          bottom: 180,
          left: -400,
          right: -400,
          height: 500,
          borderRadius: '50% 50% 0 0',
          background: 'linear-gradient(180deg, #38bdf8 0%, #0284c7 30%, #0f172a 100%)',
          boxShadow: '0 -15px 50px rgba(56, 189, 248, 0.45)',
          opacity: 0.7,
        }}
      />

      {/* 5th-Gen Stealth Fighter Jet SVG */}
      <div
        style={{
          position: 'absolute',
          top: '35%',
          left: '50%',
          transform: `translate(-50%, calc(-50% + ${jetY}px)) scale(${jetScale})`,
          display: 'flex',
          flexDirection: 'column',
          alignItems: 'center',
        }}
      >
        <svg
          width="420"
          height="280"
          viewBox="0 0 420 280"
          style={{
            filter: 'drop-shadow(0 20px 40px rgba(56, 189, 248, 0.5))',
          }}
        >
          {/* Afterburner Thruster Flame */}
          <polygon
            points="195,240 210,280 225,240"
            fill="#38bdf8"
            opacity={0.8 + Math.sin(frame / 4) * 0.2}
          />
          <polygon
            points="200,240 210,270 220,240"
            fill="#ffffff"
            opacity={0.9}
          />

          {/* Stealth Wings & Fuselage */}
          <polygon
            points="210,20 225,90 400,195 350,225 240,210 235,245 185,245 180,210 70,225 20,195 195,90"
            fill="#1e293b"
            stroke="#38bdf8"
            strokeWidth="3"
          />

          {/* Canopy / Cockpit */}
          <polygon points="210,70 218,125 202,125" fill="#38bdf8" opacity="0.9" />
        </svg>

        {/* Conclusion Big Banner */}
        <div
          style={{
            marginTop: 40,
            textAlign: 'center',
          }}
        >
          <div
            style={{
              fontFamily: 'monospace',
              fontSize: 24,
              color: 'rgba(255,255,255,0.7)',
              letterSpacing: 4,
              textTransform: 'uppercase',
            }}
          >
            DOKTRIN MODERN
          </div>
          <h2
            style={{
              margin: '8px 0 0 0',
              fontSize: 52,
              fontWeight: 900,
              fontFamily: "'Segoe UI', Roboto, sans-serif",
              color: '#ffffff',
              letterSpacing: '-1px',
            }}
          >
            TEKNOLOGI & <span style={{ color: '#fbbf24' }}>KECEPATAN</span>
          </h2>
        </div>

        {/* Call to Action Follow Button */}
        {frame >= 120 && (
          <div
            style={{
              marginTop: 35,
              transform: `scale(${Math.max(0, ctaScale)})`,
              backgroundColor: '#ef4444',
              color: '#ffffff',
              padding: '18px 46px',
              borderRadius: 999,
              fontSize: 28,
              fontWeight: 900,
              fontFamily: 'sans-serif',
              letterSpacing: 2,
              boxShadow: `0 0 ${ctaGlow}px #ef4444`,
              display: 'flex',
              alignItems: 'center',
              gap: 16,
              border: '2px solid rgba(255,255,255,0.4)',
            }}
          >
            <span>🔔</span>
            <span>FOLLOW UNTUK INFO LAINNYA!</span>
          </div>
        )}
      </div>

      {/* Subtitle Narration */}
      <SubtitleBar
        badge="Doktrin Tempur Masa Depan"
        badgeColor="#ef4444"
        text="Perang modern adalah adu teknologi, kecerdasan data, dan kecepatan komando. Follow untuk fakta militer lainnya!"
        highlightWords={['teknologi', 'kecerdasan', 'data', 'kecepatan', 'komando', 'follow']}
      />
    </AbsoluteFill>
  );
};
