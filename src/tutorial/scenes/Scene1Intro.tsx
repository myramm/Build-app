import React from 'react';
import {
  AbsoluteFill,
  interpolate,
  spring,
  useCurrentFrame,
  useVideoConfig,
} from 'remotion';
import { TutorialHeader } from '../TutorialHeader';
import { TutorialSubtitle } from '../TutorialSubtitle';

export const Scene1Intro: React.FC = () => {
  const frame = useCurrentFrame();
  const { fps } = useVideoConfig();

  const logoScale = spring({
    frame,
    fps,
    config: { damping: 12, mass: 0.8 },
  });

  const reactRotate = frame * 0.8;

  return (
    <AbsoluteFill
      style={{
        backgroundColor: '#0a0f1d',
        overflow: 'hidden',
      }}
    >
      <TutorialHeader step="PENGENALAN REMOTION" stepNumber={1} />

      {/* Background Gradient */}
      <AbsoluteFill
        style={{
          background:
            'radial-gradient(ellipse at 50% 40%, rgba(56, 189, 248, 0.25) 0%, rgba(13, 17, 23, 0.95) 60%, #030712 100%)',
        }}
      />

      {/* Center Hero Card */}
      <div
        style={{
          position: 'absolute',
          top: '42%',
          left: '50%',
          transform: 'translate(-50%, -50%)',
          display: 'flex',
          flexDirection: 'column',
          alignItems: 'center',
          textAlign: 'center',
          width: '90%',
        }}
      >
        {/* Animated Logos Lockup */}
        <div
          style={{
            display: 'flex',
            alignItems: 'center',
            gap: 28,
            marginBottom: 36,
            transform: `scale(${logoScale})`,
          }}
        >
          {/* React Logo */}
          <div
            style={{
              fontSize: 84,
              filter: 'drop-shadow(0 0 20px #00d8ff)',
              transform: `rotate(${reactRotate}deg)`,
            }}
          >
            ⚛️
          </div>
          <div style={{ fontSize: 48, color: '#94a3b8' }}>+</div>
          {/* Remotion Triangle Logo */}
          <div
            style={{
              fontSize: 84,
              filter: 'drop-shadow(0 0 20px #38bdf8)',
            }}
          >
            📐
          </div>
          <div style={{ fontSize: 48, color: '#94a3b8' }}>+</div>
          {/* Gemini AI Logo */}
          <div
            style={{
              fontSize: 84,
              filter: 'drop-shadow(0 0 20px #a855f7)',
            }}
          >
            ✨
          </div>
        </div>

        {/* Main Title */}
        <h1
          style={{
            fontSize: 66,
            fontWeight: 900,
            margin: 0,
            fontFamily: "'Segoe UI', Roboto, sans-serif",
            letterSpacing: '-1.5px',
            color: '#ffffff',
            lineHeight: 1.2,
          }}
        >
          CARA BIKIN VIDEO
          <br />
          <span style={{ color: '#38bdf8' }}>PAKAI REACT & AI!</span>
        </h1>

        {/* Feature Pills */}
        <div
          style={{
            display: 'flex',
            gap: 16,
            marginTop: 36,
            flexWrap: 'wrap',
            justifyContent: 'center',
          }}
        >
          <div
            style={{
              backgroundColor: 'rgba(56, 189, 248, 0.15)',
              border: '1.5px solid #38bdf8',
              borderRadius: 12,
              padding: '10px 20px',
              color: '#38bdf8',
              fontWeight: 700,
              fontSize: 22,
              fontFamily: 'monospace',
            }}
          >
            ✓ Video as Code
          </div>
          <div
            style={{
              backgroundColor: 'rgba(168, 85, 247, 0.15)',
              border: '1.5px solid #a855f7',
              borderRadius: 12,
              padding: '10px 20px',
              color: '#c084fc',
              fontWeight: 700,
              fontSize: 22,
              fontFamily: 'monospace',
            }}
          >
            ✓ AI Autonomous Coding
          </div>
          <div
            style={{
              backgroundColor: 'rgba(34, 197, 94, 0.15)',
              border: '1.5px solid #22c55e',
              borderRadius: 12,
              padding: '10px 20px',
              color: '#4ade80',
              fontWeight: 700,
              fontSize: 22,
              fontFamily: 'monospace',
            }}
          >
            ✓ 60 FPS Render
          </div>
        </div>
      </div>

      <TutorialSubtitle
        text="Mau bikin video otomatis pakai kode React dan AI? Kenalkan Remotion! Framework video berbasis kode yang super fleksibel."
        highlightWords={['video', 'otomatis', 'react', 'ai', 'remotion']}
      />
    </AbsoluteFill>
  );
};
