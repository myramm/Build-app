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

  const titleEntrance = spring({
    frame,
    fps,
    from: 30,
    to: 0,
    config: { damping: 18, mass: 0.6 },
  });

  const pipelineOpacity = interpolate(frame, [25, 45], [0, 1], {
    extrapolateRight: 'clamp',
  });

  return (
    <AbsoluteFill
      style={{
        backgroundColor: '#000000',
        overflow: 'hidden',
        fontFamily: "'DM Sans', sans-serif",
      }}
    >
      <TutorialHeader step="Pengenalan Remotion" stepNumber={1} />

      {/* Main Editorial Block */}
      <div
        style={{
          position: 'absolute',
          top: '38%',
          left: '50%',
          transform: 'translate(-50%, -50%)',
          width: '88%',
          maxWidth: 950,
          display: 'flex',
          flexDirection: 'column',
          alignItems: 'flex-start',
        }}
      >
        {/* Brand Lockup SVGs (Zero Emojis, Clean Tech SVGs) */}
        <div
          style={{
            display: 'flex',
            alignItems: 'center',
            gap: 20,
            marginBottom: 24,
          }}
        >
          {/* React SVG */}
          <svg width="44" height="44" viewBox="-11.5 -10.23174 23 20.46348" fill="none">
            <circle cx="0" cy="0" r="2.05" fill="#61DAFB" />
            <g stroke="#61DAFB" strokeWidth="1">
              <ellipse rx="11" ry="4.2" />
              <ellipse rx="11" ry="4.2" transform="rotate(60)" />
              <ellipse rx="11" ry="4.2" transform="rotate(120)" />
            </g>
          </svg>

          <span style={{ color: '#475569', fontSize: 24 }}>+</span>

          {/* Remotion Triangle SVG */}
          <svg width="40" height="40" viewBox="0 0 100 100" fill="none">
            <polygon points="50,15 90,85 10,85" stroke="#38BDF8" strokeWidth="10" strokeLinejoin="round" />
            <polygon points="50,35 75,78 25,78" fill="#38BDF8" opacity="0.3" />
          </svg>

          <span style={{ color: '#475569', fontSize: 24 }}>+</span>

          {/* AI Gemini Sparkle SVG */}
          <svg width="40" height="40" viewBox="0 0 24 24" fill="none" stroke="#E11D48" strokeWidth="2.2" strokeLinecap="round" strokeLinejoin="round">
            <path d="M12 2v4M12 18v4M4.93 4.93l2.83 2.83M16.24 16.24l2.83 2.83M2 12h4M18 12h4M4.93 19.07l2.83-2.83M16.24 7.76l2.83-2.83" />
          </svg>
        </div>

        {/* Title */}
        <h1
          style={{
            fontSize: 66,
            fontWeight: 900,
            color: '#F8FAFC',
            lineHeight: 1.15,
            margin: '0 0 32px 0',
            fontFamily: "'Space Grotesk', sans-serif",
            letterSpacing: '-1.5px',
            transform: `translateY(${titleEntrance}px)`,
          }}
        >
          Membangun Video
          <br />
          <span style={{ color: '#E11D48' }}>Otomatis dengan React</span>
          <br />
          dan AI Coding Agent.
        </h1>

        {/* Real Architectural Pipeline */}
        <div
          style={{
            width: '100%',
            opacity: pipelineOpacity,
            backgroundColor: '#0F0F23',
            border: '1px solid #1E1B4B',
            borderRadius: 12,
            padding: '24px',
            display: 'flex',
            flexDirection: 'column',
            gap: 14,
            fontFamily: "'Space Grotesk', monospace",
          }}
        >
          <div style={{ color: '#94A3B8', fontSize: 16, fontWeight: 700, letterSpacing: '0.05em' }}>
            ALUR KERJA REMOTION PIPELINE:
          </div>

          <div style={{ display: 'grid', gridTemplateColumns: '1fr', gap: 10, fontSize: 19 }}>
            <div
              style={{
                backgroundColor: '#1E1B4B',
                padding: '12px 18px',
                borderRadius: 8,
                color: '#F8FAFC',
                display: 'flex',
                justifyContent: 'space-between',
              }}
            >
              <span>1. Kode React (.tsx / Canvas)</span>
              <span style={{ color: '#38BDF8', fontWeight: 700 }}>Definisi Frame</span>
            </div>

            <div
              style={{
                backgroundColor: '#1E1B4B',
                padding: '12px 18px',
                borderRadius: 8,
                color: '#F8FAFC',
                display: 'flex',
                justifyContent: 'space-between',
              }}
            >
              <span>2. Headless Chromium Engine</span>
              <span style={{ color: '#38BDF8', fontWeight: 700 }}>Render Web</span>
            </div>

            <div
              style={{
                backgroundColor: '#1E1B4B',
                padding: '12px 18px',
                borderRadius: 8,
                color: '#F8FAFC',
                display: 'flex',
                justifyContent: 'space-between',
              }}
            >
              <span>3. FFmpeg Encoder & Audio</span>
              <span style={{ color: '#38BDF8', fontWeight: 700 }}>Encode 60 FPS</span>
            </div>

            <div
              style={{
                backgroundColor: 'rgba(225, 29, 72, 0.15)',
                border: '1px solid #E11D48',
                padding: '12px 18px',
                borderRadius: 8,
                color: '#E11D48',
                fontWeight: 800,
                display: 'flex',
                justifyContent: 'space-between',
              }}
            >
              <span>4. File Output Video</span>
              <span>MP4 / WebM Siap Pakai</span>
            </div>
          </div>
        </div>
      </div>

      <TutorialSubtitle
        text="Halo teman-teman! Pernah kepikiran bikin video otomatis pakai kode React dan AI? Kenalkan Remotion! Framework keren berbasis kode yang super fleksibel."
        highlightWords={['video', 'otomatis', 'react', 'ai', 'remotion', 'kode']}
      />
    </AbsoluteFill>
  );
};
