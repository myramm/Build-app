import React from 'react';
import {
  AbsoluteFill,
  interpolate,
  spring,
  useCurrentFrame,
  useVideoConfig,
} from 'remotion';
import { SubtitleBar } from '../components/SubtitleBar';

export const Scene1Hook: React.FC = () => {
  const frame = useCurrentFrame();
  const { fps } = useVideoConfig();

  // Dramatic camera zoom
  const cameraZoom = interpolate(frame, [0, 300], [1.0, 1.15], {
    extrapolateRight: 'clamp',
  });

  // "TAUKAH KAMU?" entrance bounce
  const titleScale = spring({
    frame: frame - 15,
    fps,
    config: { damping: 12, mass: 0.8 },
  });

  const titleGlow = Math.sin(frame / 12) * 15 + 25;

  // Crosshair rotation and tracking
  const reticleRotate = frame * 0.4;
  const lockScale = spring({
    frame: frame - 40,
    fps,
    config: { damping: 10, mass: 0.5 },
  });

  return (
    <AbsoluteFill
      style={{
        backgroundColor: '#070a12',
        overflow: 'hidden',
        transform: `scale(${cameraZoom})`,
      }}
    >
      {/* Cinematic Sunset Sky Gradient & Volumetric Fog */}
      <AbsoluteFill
        style={{
          background:
            'radial-gradient(ellipse at 50% 65%, #ca8a04 0%, #b45309 25%, #1e293b 65%, #050811 100%)',
          opacity: 0.85,
        }}
      />

      {/* Atmospheric Horizon Mountains / Terrain Silhouette */}
      <svg
        style={{
          position: 'absolute',
          bottom: 180,
          left: 0,
          right: 0,
          width: '100%',
          opacity: 0.7,
        }}
        viewBox="0 0 1080 360"
        fill="#04060b"
      >
        <path d="M0,360 L0,220 L180,180 L360,240 L540,160 L720,230 L900,170 L1080,210 L1080,360 Z" />
      </svg>

      {/* Central Targeting Reticle & Drone Optics */}
      <div
        style={{
          position: 'absolute',
          top: '36%',
          left: '50%',
          transform: 'translate(-50%, -50%)',
          display: 'flex',
          flexDirection: 'column',
          alignItems: 'center',
          justifyContent: 'center',
        }}
      >
        {/* Outer Rotating HUD Ring */}
        <div
          style={{
            position: 'absolute',
            width: 480,
            height: 480,
            borderRadius: '50%',
            border: '2px dashed rgba(56, 189, 248, 0.45)',
            transform: `rotate(${reticleRotate}deg)`,
          }}
        />

        {/* Inner Lock-on Ring */}
        <div
          style={{
            position: 'absolute',
            width: 320,
            height: 320,
            borderRadius: '50%',
            border: '2px solid rgba(245, 158, 11, 0.55)',
            boxShadow: '0 0 30px rgba(245, 158, 11, 0.25)',
            transform: `scale(${lockScale})`,
          }}
        />

        {/* Lock Brackets */}
        <div
          style={{
            position: 'absolute',
            width: 240,
            height: 240,
            borderLeft: '4px solid #ef4444',
            borderRight: '4px solid #ef4444',
            transform: `scale(${lockScale})`,
          }}
        />

        {/* Target Status Tag */}
        <div
          style={{
            position: 'absolute',
            top: -70,
            fontFamily: 'monospace',
            fontSize: 20,
            fontWeight: 800,
            color: '#ef4444',
            backgroundColor: 'rgba(239, 68, 68, 0.15)',
            padding: '4px 16px',
            borderRadius: 6,
            border: '1px solid #ef4444',
            letterSpacing: 2,
          }}
        >
          TARGET: LOCKED [RADAR-9X]
        </div>

        {/* BIG HOOK TITLE: "TAUKAH KAMU?" */}
        <div
          style={{
            transform: `scale(${Math.max(0, titleScale)})`,
            textAlign: 'center',
            zIndex: 10,
          }}
        >
          <div
            style={{
              fontFamily: 'monospace',
              fontSize: 28,
              color: '#38bdf8',
              letterSpacing: 8,
              marginBottom: 10,
              textTransform: 'uppercase',
              fontWeight: 800,
            }}
          >
            [ INTEL REPORT ]
          </div>
          <h1
            style={{
              margin: 0,
              fontSize: 105,
              fontWeight: 900,
              fontFamily: "'Segoe UI', Impact, Arial Black, sans-serif",
              color: '#ffffff',
              letterSpacing: '-2px',
              textShadow: `0 0 ${titleGlow}px rgba(245, 158, 11, 0.9), 0 10px 40px rgba(0,0,0,0.9)`,
            }}
          >
            TAUKAH
            <br />
            <span style={{ color: '#fbbf24' }}>KAMU?</span>
          </h1>
        </div>
      </div>

      {/* Subtitle Narration */}
      <SubtitleBar
        badge="Sistem Perang Modern"
        badgeColor="#ef4444"
        text="Tahukah kamu? Perang modern bukan cuma soal siapa yang punya senjata paling kuat!"
        highlightWords={['bukan', 'senjata', 'kuat', 'modern']}
      />
    </AbsoluteFill>
  );
};
