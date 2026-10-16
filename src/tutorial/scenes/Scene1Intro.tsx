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
        backgroundColor: '#030712',
        overflow: 'hidden',
      }}
    >
      <TutorialHeader step="Pengenalan Remotion" stepNumber={1} />

      {/* Main Editorial Layout */}
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
        {/* Category Label */}
        <div
          style={{
            fontFamily: "'Fira Code', monospace",
            fontSize: 20,
            color: '#10b981',
            letterSpacing: '0.1em',
            textTransform: 'uppercase',
            marginBottom: 16,
            fontWeight: 700,
          }}
        >
          DEVELOPER TUTORIAL · 2026
        </div>

        {/* Main Title */}
        <h1
          style={{
            fontSize: 68,
            fontWeight: 900,
            color: '#f8fafc',
            lineHeight: 1.15,
            margin: '0 0 32px 0',
            fontFamily: "'Segoe UI', Roboto, sans-serif",
            letterSpacing: '-1.5px',
            transform: `translateY(${titleEntrance}px)`,
          }}
        >
          Membangun Video
          <br />
          <span style={{ color: '#10b981' }}>Otomatis dengan React</span>
          <br />
          dan AI Coding Agent.
        </h1>

        {/* Real Architectural Pipeline */}
        <div
          style={{
            width: '100%',
            opacity: pipelineOpacity,
            backgroundColor: '#0f172a',
            border: '1px solid #1e293b',
            borderRadius: 12,
            padding: '24px',
            display: 'flex',
            flexDirection: 'column',
            gap: 16,
            fontFamily: "'Fira Code', monospace",
          }}
        >
          <div style={{ color: '#94a3b8', fontSize: 18, fontWeight: 700 }}>
            ALUR KERJA REMOTION PIPELINE:
          </div>

          <div
            style={{
              display: 'grid',
              gridTemplateColumns: '1fr',
              gap: 12,
              fontSize: 20,
            }}
          >
            <div
              style={{
                backgroundColor: '#1e293b',
                padding: '12px 18px',
                borderRadius: 8,
                color: '#f8fafc',
                display: 'flex',
                justifyContent: 'space-between',
              }}
            >
              <span>1. Kode React (.tsx / Canvas)</span>
              <span style={{ color: '#10b981' }}>Definisi Frame</span>
            </div>

            <div
              style={{
                backgroundColor: '#1e293b',
                padding: '12px 18px',
                borderRadius: 8,
                color: '#f8fafc',
                display: 'flex',
                justifyContent: 'space-between',
              }}
            >
              <span>2. Headless Chromium Engine</span>
              <span style={{ color: '#38bdf8' }}>Render Web</span>
            </div>

            <div
              style={{
                backgroundColor: '#1e293b',
                padding: '12px 18px',
                borderRadius: 8,
                color: '#f8fafc',
                display: 'flex',
                justifyContent: 'space-between',
              }}
            >
              <span>3. FFmpeg Encoder & Audio</span>
              <span style={{ color: '#f59e0b' }}>Encode 60 FPS</span>
            </div>

            <div
              style={{
                backgroundColor: 'rgba(16, 185, 129, 0.1)',
                border: '1px solid #10b981',
                padding: '12px 18px',
                borderRadius: 8,
                color: '#10b981',
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
