import React from 'react';
import {
  AbsoluteFill,
  interpolate,
  useCurrentFrame,
} from 'remotion';
import { SubtitleBar } from '../components/SubtitleBar';

export const Scene3Satellite: React.FC = () => {
  const frame = useCurrentFrame();

  // Radar sweep angle (60 FPS = 360 deg every 90 frames)
  const sweepAngle = (frame * 4) % 360;

  // Blips blinking based on angle
  const blip1Active = Math.abs(sweepAngle - 45) < 30;
  const blip2Active = Math.abs(sweepAngle - 160) < 30;
  const blip3Active = Math.abs(sweepAngle - 280) < 30;

  return (
    <AbsoluteFill
      style={{
        backgroundColor: '#040813',
        overflow: 'hidden',
      }}
    >
      {/* Deep Space Background with Stars & Atmosphere Curvature */}
      <AbsoluteFill
        style={{
          background:
            'radial-gradient(circle at 50% 85%, #0284c7 0%, #0c1833 45%, #020611 100%)',
        }}
      />

      {/* Earth Horizon Curvature */}
      <div
        style={{
          position: 'absolute',
          bottom: 220,
          left: -400,
          right: -400,
          height: 600,
          borderRadius: '50% 50% 0 0',
          background: 'linear-gradient(180deg, #38bdf8 0%, #0369a1 20%, #0f172a 100%)',
          boxShadow: '0 -20px 60px rgba(56, 189, 248, 0.45)',
          opacity: 0.6,
        }}
      />

      {/* Radar / Satellite Container */}
      <div
        style={{
          position: 'absolute',
          top: '35%',
          left: '50%',
          transform: 'translate(-50%, -50%)',
          display: 'flex',
          flexDirection: 'column',
          alignItems: 'center',
        }}
      >
        {/* Radar Circular Display */}
        <div
          style={{
            position: 'relative',
            width: 440,
            height: 440,
            borderRadius: '50%',
            border: '2px solid rgba(56, 189, 248, 0.5)',
            boxShadow: '0 0 40px rgba(14, 165, 233, 0.25), inset 0 0 30px rgba(14, 165, 233, 0.15)',
            backgroundColor: 'rgba(7, 12, 23, 0.75)',
            overflow: 'hidden',
          }}
        >
          {/* Concentric Range Rings */}
          <div
            style={{
              position: 'absolute',
              inset: 45,
              borderRadius: '50%',
              border: '1px dashed rgba(56, 189, 248, 0.35)',
            }}
          />
          <div
            style={{
              position: 'absolute',
              inset: 95,
              borderRadius: '50%',
              border: '1px solid rgba(56, 189, 248, 0.25)',
            }}
          />
          <div
            style={{
              position: 'absolute',
              inset: 145,
              borderRadius: '50%',
              border: '1px dashed rgba(56, 189, 248, 0.2)',
            }}
          />

          {/* Cross Axes */}
          <div
            style={{
              position: 'absolute',
              top: '50%',
              left: 0,
              right: 0,
              height: 1,
              backgroundColor: 'rgba(56, 189, 248, 0.3)',
            }}
          />
          <div
            style={{
              position: 'absolute',
              left: '50%',
              top: 0,
              bottom: 0,
              width: 1,
              backgroundColor: 'rgba(56, 189, 248, 0.3)',
            }}
          />

          {/* Sweeping Radar Beam */}
          <div
            style={{
              position: 'absolute',
              top: '50%',
              left: '50%',
              width: 220,
              height: 220,
              transformOrigin: 'top left',
              transform: `rotate(${sweepAngle}deg)`,
              background:
                'conic-gradient(from 0deg, rgba(56, 189, 248, 0.45) 0deg, rgba(56, 189, 248, 0) 65deg)',
              pointerEvents: 'none',
            }}
          />

          {/* Target Blips */}
          {/* Blip 1 */}
          <div
            style={{
              position: 'absolute',
              top: 110,
              left: 280,
              width: 12,
              height: 12,
              borderRadius: '50%',
              backgroundColor: '#ef4444',
              boxShadow: blip1Active ? '0 0 16px #ef4444' : 'none',
              opacity: blip1Active ? 1 : 0.4,
            }}
          />
          {/* Blip 2 */}
          <div
            style={{
              position: 'absolute',
              top: 310,
              left: 140,
              width: 12,
              height: 12,
              borderRadius: '50%',
              backgroundColor: '#fbbf24',
              boxShadow: blip2Active ? '0 0 16px #fbbf24' : 'none',
              opacity: blip2Active ? 1 : 0.4,
            }}
          />
          {/* Blip 3 */}
          <div
            style={{
              position: 'absolute',
              top: 180,
              left: 80,
              width: 12,
              height: 12,
              borderRadius: '50%',
              backgroundColor: '#10b981',
              boxShadow: blip3Active ? '0 0 16px #10b981' : 'none',
              opacity: blip3Active ? 1 : 0.4,
            }}
          />
        </div>

        {/* Orbit Satellite Icon & Readout */}
        <div
          style={{
            marginTop: 35,
            display: 'flex',
            alignItems: 'center',
            gap: 20,
            backgroundColor: 'rgba(15, 23, 42, 0.9)',
            border: '1px solid rgba(56, 189, 248, 0.4)',
            borderRadius: 12,
            padding: '12px 28px',
            fontFamily: 'monospace',
            fontSize: 20,
            color: '#ffffff',
          }}
        >
          <span style={{ fontSize: 32 }}>🛰️</span>
          <div>
            <div style={{ color: '#38bdf8', fontWeight: 800 }}>ORBIT: LOW-EARTH (540 KM)</div>
            <div style={{ color: 'rgba(255,255,255,0.7)', fontSize: 16 }}>
              COVERAGE: 12,000 KM² | PHASED-ARRAY RADAR
            </div>
          </div>
        </div>
      </div>

      {/* Subtitle Narration */}
      <SubtitleBar
        badge="Satelit & Radar Militer"
        badgeColor="#0284c7"
        text="Satelit dan radar militer mendeteksi serta melacak objek di wilayah yang sangat luas."
        highlightWords={['satelit', 'radar', 'mendeteksi', 'melacak', 'luas']}
      />
    </AbsoluteFill>
  );
};
