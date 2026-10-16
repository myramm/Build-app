import React from 'react';
import {
  AbsoluteFill,
  interpolate,
  spring,
  useCurrentFrame,
  useVideoConfig,
} from 'remotion';
import { SubtitleBar } from '../components/SubtitleBar';

export const Scene5AirDefense: React.FC = () => {
  const frame = useCurrentFrame();
  const { fps } = useVideoConfig();

  // Progress of missile interception (0 to 1 over first 180 frames)
  const interceptProgress = interpolate(frame, [0, 150], [0, 1], {
    extrapolateRight: 'clamp',
  });

  // Explosion triggers around frame 150
  const explosionScale = spring({
    frame: frame - 145,
    fps,
    config: { damping: 10, mass: 0.5 },
  });
  const explosionOpacity = interpolate(frame, [145, 175, 230], [0, 1, 0], {
    extrapolateLeft: 'clamp',
    extrapolateRight: 'clamp',
  });

  // Ground Battery launch position
  const batteryX = 540;
  const batteryY = 1200;

  // Intercept point
  const targetX = 540;
  const targetY = 560;

  // Interceptor missile current pos
  const missileX = batteryX + (targetX - batteryX) * interceptProgress;
  const missileY = batteryY + (targetY - batteryY) * interceptProgress;

  // Incoming threat current pos
  const threatX = 540;
  const threatY = 220 + (targetY - 220) * interceptProgress;

  return (
    <AbsoluteFill
      style={{
        backgroundColor: '#0a0d18',
        overflow: 'hidden',
      }}
    >
      {/* Dramatic Night Sky with Amber Anti-Air Horizon */}
      <AbsoluteFill
        style={{
          background:
            'radial-gradient(ellipse at 50% 70%, #7f1d1d 0%, #1e1b4b 45%, #030712 100%)',
          opacity: 0.85,
        }}
      />

      {/* Trajectory Arcs SVG */}
      <svg
        style={{ position: 'absolute', inset: 0, width: '100%', height: '100%' }}
      >
        {/* Incoming Threat Arc (Red) */}
        {interceptProgress < 1 && (
          <line
            x1="540"
            y1="220"
            x2={threatX}
            y2={threatY}
            stroke="#ef4444"
            strokeWidth="4"
            strokeDasharray="8 8"
          />
        )}

        {/* Interceptor Launch Vector (Cyan/Green) */}
        {interceptProgress < 1 && (
          <line
            x1={batteryX}
            y1={batteryY}
            x2={missileX}
            y2={missileY}
            stroke="#10b981"
            strokeWidth="5"
          />
        )}
      </svg>

      {/* Incoming Target Lock Bracket */}
      {interceptProgress < 1 && (
        <div
          style={{
            position: 'absolute',
            left: threatX,
            top: threatY,
            transform: 'translate(-50%, -50%)',
            width: 70,
            height: 70,
            border: '2px dashed #ef4444',
            borderRadius: '50%',
            display: 'flex',
            alignItems: 'center',
            justifyContent: 'center',
            boxShadow: '0 0 16px #ef4444',
          }}
        >
          <div
            style={{
              width: 14,
              height: 14,
              backgroundColor: '#ef4444',
              borderRadius: '50%',
            }}
          />
          <div
            style={{
              position: 'absolute',
              top: -24,
              fontFamily: 'monospace',
              fontSize: 14,
              color: '#ef4444',
              fontWeight: 800,
            }}
          >
            HOSTILE
          </div>
        </div>
      )}

      {/* Interceptor Missile Tip */}
      {interceptProgress < 1 && (
        <div
          style={{
            position: 'absolute',
            left: missileX,
            top: missileY,
            transform: 'translate(-50%, -50%)',
            width: 18,
            height: 18,
            borderRadius: '50%',
            backgroundColor: '#38bdf8',
            boxShadow: '0 0 20px #38bdf8',
          }}
        />
      )}

      {/* Mid-Air Interception Explosion Burst */}
      {frame >= 145 && (
        <div
          style={{
            position: 'absolute',
            left: targetX,
            top: targetY,
            transform: `translate(-50%, -50%) scale(${Math.max(0, explosionScale)})`,
            opacity: explosionOpacity,
            display: 'flex',
            flexDirection: 'column',
            alignItems: 'center',
            justifyContent: 'center',
          }}
        >
          <div
            style={{
              width: 260,
              height: 260,
              borderRadius: '50%',
              background:
                'radial-gradient(circle, #ffffff 0%, #fbbf24 35%, #ef4444 70%, transparent 100%)',
              filter: 'blur(6px)',
              boxShadow: '0 0 70px #ef4444',
            }}
          />
          <div
            style={{
              position: 'absolute',
              fontFamily: 'monospace',
              fontSize: 32,
              fontWeight: 900,
              color: '#10b981',
              backgroundColor: 'rgba(6, 78, 59, 0.9)',
              border: '2px solid #10b981',
              padding: '6px 24px',
              borderRadius: 8,
              boxShadow: '0 0 20px #10b981',
              letterSpacing: 2,
            }}
          >
            THREAT NEUTRALIZED!
          </div>
        </div>
      )}

      {/* Ground Launcher Station Display */}
      <div
        style={{
          position: 'absolute',
          top: 1050,
          left: '50%',
          transform: 'translateX(-50%)',
          backgroundColor: 'rgba(15, 23, 42, 0.9)',
          border: '2px solid rgba(16, 185, 129, 0.5)',
          borderRadius: 16,
          padding: '16px 36px',
          display: 'flex',
          gap: 30,
          alignItems: 'center',
          fontFamily: 'monospace',
          fontSize: 20,
          color: '#ffffff',
          boxShadow: '0 10px 30px rgba(0,0,0,0.8)',
        }}
      >
        <span style={{ fontSize: 40 }}>🛡️</span>
        <div>
          <div style={{ color: '#10b981', fontWeight: 900 }}>
            AUTO-INTERCEPT: ACTIVE
          </div>
          <div style={{ color: 'rgba(255,255,255,0.7)', fontSize: 16 }}>
            MULTI-TARGET PHASED RADAR | 0.04s REACTION TIME
          </div>
        </div>
      </div>

      {/* Subtitle Narration */}
      <SubtitleBar
        badge="Sistem Pertahanan Udara"
        badgeColor="#10b981"
        text="Sistem pertahanan udara otomatis mampu melacak banyak ancaman dan memandu pencegatan sekaligus!"
        highlightWords={['pertahanan', 'udara', 'otomatis', 'melacak', 'pencegatan', 'sekaligus']}
      />
    </AbsoluteFill>
  );
};
