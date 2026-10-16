import React from 'react';
import {
  AbsoluteFill,
  useCurrentFrame,
} from 'remotion';
import { TutorialHeader } from '../TutorialHeader';
import { TutorialSubtitle } from '../TutorialSubtitle';

export const Scene5Studio: React.FC = () => {
  const frame = useCurrentFrame();

  return (
    <AbsoluteFill
      style={{
        backgroundColor: '#030712',
        overflow: 'hidden',
      }}
    >
      <TutorialHeader step="Remotion Studio Preview" stepNumber={5} />

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
          gap: 20,
        }}
      >
        {/* CLI Command Block */}
        <div
          style={{
            backgroundColor: '#0f172a',
            border: '1px solid #1e293b',
            borderRadius: 12,
            padding: '20px 28px',
            fontFamily: "'Fira Code', monospace",
          }}
        >
          <div style={{ fontSize: 24, lineHeight: 1.8 }}>
            <span style={{ color: '#64748b' }}>my-video $ </span>
            <span style={{ color: '#10b981', fontWeight: 800 }}>npm start</span>
          </div>
          <div style={{ fontSize: 18, color: '#94a3b8', marginTop: 4 }}>
            Local Preview: <span style={{ color: '#38bdf8' }}>http://localhost:3000</span>
          </div>
        </div>

        {/* Remotion Studio UI Mockup */}
        <div
          style={{
            backgroundColor: '#0f172a',
            border: '1px solid #1e293b',
            borderRadius: 12,
            padding: '24px',
            fontFamily: "'Fira Code', monospace",
          }}
        >
          <div
            style={{
              display: 'flex',
              justifyContent: 'space-between',
              alignItems: 'center',
              borderBottom: '1px solid #1e293b',
              paddingBottom: 12,
              marginBottom: 16,
              fontSize: 16,
              color: '#94a3b8',
            }}
          >
            <span>REMOTION STUDIO 4.0</span>
            <span style={{ color: '#10b981' }}>● STATUS: READY</span>
          </div>

          {/* Viewport Canvas Screen */}
          <div
            style={{
              height: 220,
              backgroundColor: '#020617',
              border: '1px solid #1e293b',
              borderRadius: 8,
              display: 'flex',
              flexDirection: 'column',
              alignItems: 'center',
              justifyContent: 'center',
              color: '#f8fafc',
            }}
          >
            <div style={{ fontSize: 26, fontWeight: 800 }}>
              CANVAS PREVIEW
            </div>
            <div style={{ fontSize: 18, color: '#64748b', marginTop: 6 }}>
              1080 × 1920 (9:16) · 60 FPS
            </div>
          </div>

          {/* Scrubber Controls */}
          <div style={{ marginTop: 16 }}>
            <div
              style={{
                display: 'flex',
                justifyContent: 'space-between',
                fontSize: 16,
                color: '#94a3b8',
                marginBottom: 8,
              }}
            >
              <span>TIMELINE CONTROLS</span>
              <span>Frame: {(frame * 4) % 1800} / 1800</span>
            </div>

            <div
              style={{
                height: 8,
                backgroundColor: '#1e293b',
                borderRadius: 4,
                overflow: 'hidden',
              }}
            >
              <div
                style={{
                  height: '100%',
                  width: `${((frame * 4) % 1800) / 18}%`,
                  backgroundColor: '#10b981',
                }}
              />
            </div>
          </div>
        </div>
      </div>

      <TutorialSubtitle
        text="Langkah keempat, jalankan npm start untuk membuka Remotion Studio di browser. Di sini kalian bisa melihat preview animasi dan timeline secara real-time."
        highlightWords={['keempat', 'npm', 'start', 'remotion', 'studio', 'browser', 'preview', 'timeline', 'real-time']}
      />
    </AbsoluteFill>
  );
};
