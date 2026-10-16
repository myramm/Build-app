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
        backgroundColor: '#000000',
        overflow: 'hidden',
        fontFamily: "'DM Sans', sans-serif",
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
            backgroundColor: '#0F0F23',
            border: '1px solid #1E1B4B',
            borderRadius: 12,
            padding: '20px 28px',
            fontFamily: "'Space Grotesk', monospace",
          }}
        >
          <div style={{ fontSize: 24, lineHeight: 1.8 }}>
            <span style={{ color: '#64748B' }}>my-video $ </span>
            <span style={{ color: '#E11D48', fontWeight: 800 }}>npm start</span>
          </div>
          <div style={{ fontSize: 18, color: '#94A3B8', marginTop: 4 }}>
            Local Preview: <span style={{ color: '#38BDF8' }}>http://localhost:3000</span>
          </div>
        </div>

        {/* Remotion Studio UI Mockup */}
        <div
          style={{
            backgroundColor: '#0F0F23',
            border: '1px solid #1E1B4B',
            borderRadius: 12,
            padding: '24px',
            fontFamily: "'Space Grotesk', monospace",
          }}
        >
          <div
            style={{
              display: 'flex',
              justifyContent: 'space-between',
              alignItems: 'center',
              borderBottom: '1px solid #1E1B4B',
              paddingBottom: 12,
              marginBottom: 16,
              fontSize: 15,
              color: '#94A3B8',
            }}
          >
            <span>REMOTION STUDIO 4.0</span>
            <span style={{ color: '#10B981', fontWeight: 700 }}>● SERVER: ACTIVE</span>
          </div>

          {/* Viewport Canvas Screen */}
          <div
            style={{
              height: 220,
              backgroundColor: '#050512',
              border: '1px solid #1E1B4B',
              borderRadius: 8,
              display: 'flex',
              flexDirection: 'column',
              alignItems: 'center',
              justifyContent: 'center',
              color: '#F8FAFC',
            }}
          >
            <div style={{ fontSize: 26, fontWeight: 800, color: '#E11D48' }}>
              CANVAS PREVIEW
            </div>
            <div style={{ fontSize: 18, color: '#64748B', marginTop: 6 }}>
              1080 × 1920 (9:16) · 60 FPS
            </div>
          </div>

          {/* Scrubber Controls */}
          <div style={{ marginTop: 16 }}>
            <div
              style={{
                display: 'flex',
                justifyContent: 'space-between',
                fontSize: 15,
                color: '#94A3B8',
                marginBottom: 8,
              }}
            >
              <span>TIMELINE SCRUBBER</span>
              <span>Frame: {(frame * 4) % 1800} / 1800</span>
            </div>

            <div
              style={{
                height: 8,
                backgroundColor: '#1E1B4B',
                borderRadius: 4,
                overflow: 'hidden',
              }}
            >
              <div
                style={{
                  height: '100%',
                  width: `${((frame * 4) % 1800) / 18}%`,
                  backgroundColor: '#E11D48',
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
