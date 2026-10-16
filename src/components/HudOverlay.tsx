import React from 'react';
import { AbsoluteFill, useCurrentFrame } from 'remotion';

export const HudOverlay: React.FC = () => {
  const frame = useCurrentFrame();

  // Dynamic telemetry values based on frame
  const alt = Math.floor(24500 + Math.sin(frame / 45) * 350);
  const spd = (1.42 + Math.sin(frame / 60) * 0.08).toFixed(2);
  const latDeg = 34 + Math.floor(frame / 120);
  const latMin = ((frame * 1.37) % 60).toFixed(2);
  const lonDeg = 118 + Math.floor(frame / 180);
  const lonMin = ((frame * 2.11) % 60).toFixed(2);
  const heading = Math.floor((frame * 0.8) % 360);

  // Blinking recording dot
  const recOpacity = frame % 60 < 35 ? 1 : 0.2;

  return (
    <AbsoluteFill style={{ pointerEvents: 'none', zIndex: 90 }}>
      {/* Subtle CRT Scanlines & Vignette */}
      <div
        style={{
          position: 'absolute',
          inset: 0,
          background:
            'radial-gradient(circle at 50% 50%, rgba(10, 16, 28, 0) 45%, rgba(3, 7, 18, 0.75) 100%)',
        }}
      />
      <div
        style={{
          position: 'absolute',
          inset: 0,
          backgroundImage:
            'repeating-linear-gradient(0deg, rgba(0, 0, 0, 0.12) 0px, rgba(0, 0, 0, 0.12) 2px, transparent 2px, transparent 4px)',
          opacity: 0.6,
        }}
      />

      {/* Top Header: Mission & Telemetry */}
      <div
        style={{
          position: 'absolute',
          top: 36,
          left: 40,
          right: 40,
          display: 'flex',
          justifyContent: 'space-between',
          alignItems: 'center',
          fontFamily: 'monospace',
          fontSize: 20,
          color: 'rgba(56, 189, 248, 0.85)',
          textShadow: '0 0 10px rgba(56, 189, 248, 0.6)',
          letterSpacing: 2,
        }}
      >
        <div style={{ display: 'flex', alignItems: 'center', gap: 12 }}>
          <div
            style={{
              width: 14,
              height: 14,
              borderRadius: '50%',
              backgroundColor: '#ef4444',
              boxShadow: '0 0 12px #ef4444',
              opacity: recOpacity,
            }}
          />
          <span style={{ fontWeight: 800, color: '#f87171' }}>REC [60 FPS]</span>
          <span style={{ color: 'rgba(255,255,255,0.4)' }}>|</span>
          <span>TAC-NET: SECURE</span>
        </div>

        <div style={{ fontWeight: 700, color: '#38bdf8' }}>
          HDG: {String(heading).padStart(3, '0')}°
        </div>

        <div style={{ color: 'rgba(255,255,255,0.7)' }}>
          ALT: {alt.toLocaleString()} FT
        </div>
      </div>

      {/* Military Corner Brackets */}
      {/* Top Left */}
      <div
        style={{
          position: 'absolute',
          top: 80,
          left: 40,
          width: 40,
          height: 40,
          borderTop: '3px solid #38bdf8',
          borderLeft: '3px solid #38bdf8',
          boxShadow: '-2px -2px 10px rgba(56, 189, 248, 0.4)',
        }}
      />
      {/* Top Right */}
      <div
        style={{
          position: 'absolute',
          top: 80,
          right: 40,
          width: 40,
          height: 40,
          borderTop: '3px solid #38bdf8',
          borderRight: '3px solid #38bdf8',
          boxShadow: '2px -2px 10px rgba(56, 189, 248, 0.4)',
        }}
      />
      {/* Bottom Left */}
      <div
        style={{
          position: 'absolute',
          bottom: 220,
          left: 40,
          width: 40,
          height: 40,
          borderBottom: '3px solid #38bdf8',
          borderLeft: '3px solid #38bdf8',
          boxShadow: '-2px 2px 10px rgba(56, 189, 248, 0.4)',
        }}
      />
      {/* Bottom Right */}
      <div
        style={{
          position: 'absolute',
          bottom: 220,
          right: 40,
          width: 40,
          height: 40,
          borderBottom: '3px solid #38bdf8',
          borderRight: '3px solid #38bdf8',
          boxShadow: '2px 2px 10px rgba(56, 189, 248, 0.4)',
        }}
      />

      {/* Left Vertical Altitude Ladder */}
      <div
        style={{
          position: 'absolute',
          left: 44,
          top: '35%',
          display: 'flex',
          flexDirection: 'column',
          gap: 16,
          fontFamily: 'monospace',
          fontSize: 16,
          color: 'rgba(56, 189, 248, 0.65)',
        }}
      >
        <div>- 30K</div>
        <div style={{ color: '#38bdf8', fontWeight: 800 }}>▶ 25K</div>
        <div>- 20K</div>
        <div>- 15K</div>
      </div>

      {/* Right Vertical Speed / Mach Indicator */}
      <div
        style={{
          position: 'absolute',
          right: 44,
          top: '35%',
          display: 'flex',
          flexDirection: 'column',
          gap: 16,
          fontFamily: 'monospace',
          fontSize: 16,
          color: 'rgba(56, 189, 248, 0.65)',
          textAlign: 'right',
        }}
      >
        <div>M 2.0</div>
        <div style={{ color: '#fbbf24', fontWeight: 800 }}>◀ M {spd}</div>
        <div>M 1.2</div>
        <div>M 0.8</div>
      </div>

      {/* Bottom Coordinates & System Status Bar */}
      <div
        style={{
          position: 'absolute',
          bottom: 220,
          left: 100,
          right: 100,
          display: 'flex',
          justifyContent: 'space-between',
          fontFamily: 'monospace',
          fontSize: 18,
          color: 'rgba(255, 255, 255, 0.6)',
          letterSpacing: 2,
        }}
      >
        <div>
          POS: {latDeg}°{latMin}'N {lonDeg}°{lonMin}'E
        </div>
        <div style={{ color: '#10b981', fontWeight: 700 }}>AI SENSOR: ACTIVE</div>
      </div>
    </AbsoluteFill>
  );
};
