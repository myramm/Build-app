import React from 'react';
import {
  AbsoluteFill,
  useCurrentFrame,
} from 'remotion';
import { CodeWindow } from '../CodeWindow';
import { TutorialHeader } from '../TutorialHeader';
import { TutorialSubtitle } from '../TutorialSubtitle';

export const Scene5Studio: React.FC = () => {
  const frame = useCurrentFrame();

  return (
    <AbsoluteFill
      style={{
        backgroundColor: '#0a0f1d',
        overflow: 'hidden',
      }}
    >
      <TutorialHeader step="MENJALANKAN REMOTION STUDIO" stepNumber={5} />

      <div
        style={{
          position: 'absolute',
          top: '42%',
          left: '50%',
          transform: 'translate(-50%, -50%)',
          width: '100%',
          display: 'flex',
          justifyContent: 'center',
        }}
      >
        <CodeWindow title="Browser — Remotion Studio Preview" icon="🌐">
          {/* Top URL Bar */}
          <div
            style={{
              backgroundColor: '#030712',
              border: '1px solid rgba(255, 255, 255, 0.1)',
              borderRadius: 8,
              padding: '8px 16px',
              color: '#38bdf8',
              fontSize: 20,
              fontFamily: 'monospace',
              marginBottom: 20,
              display: 'flex',
              alignItems: 'center',
              gap: 12,
            }}
          >
            <span style={{ color: '#4ade80' }}>🔒</span>
            <span>http://localhost:3000</span>
          </div>

          {/* Remotion Studio UI Mockup */}
          <div
            style={{
              backgroundColor: '#0b0f19',
              border: '1.5px solid rgba(56, 189, 248, 0.3)',
              borderRadius: 12,
              padding: '20px',
              display: 'flex',
              flexDirection: 'column',
              gap: 16,
            }}
          >
            {/* Studio Canvas Box */}
            <div
              style={{
                height: 200,
                backgroundColor: '#020617',
                border: '1px dashed rgba(56, 189, 248, 0.4)',
                borderRadius: 8,
                display: 'flex',
                alignItems: 'center',
                justifyContent: 'center',
                color: '#ffffff',
                fontSize: 24,
                fontWeight: 800,
                boxShadow: 'inset 0 0 20px rgba(56, 189, 248, 0.15)',
              }}
            >
              ▶ LIVE VIDEO PREVIEW CANVAS
            </div>

            {/* Scrubber & Controls */}
            <div
              style={{
                display: 'flex',
                justifyContent: 'space-between',
                alignItems: 'center',
                fontSize: 18,
                color: '#94a3b8',
                fontFamily: 'monospace',
              }}
            >
              <div style={{ display: 'flex', gap: 14, color: '#38bdf8' }}>
                <span>⏮</span>
                <span>▶ PLAY</span>
                <span>⏭</span>
              </div>
              <div style={{ color: '#4ade80', fontWeight: 800 }}>
                60 FPS | 1080 × 1920
              </div>
              <div>Frame: {frame} / 3600</div>
            </div>

            {/* Timeline Bar */}
            <div
              style={{
                height: 12,
                backgroundColor: '#1e293b',
                borderRadius: 999,
                overflow: 'hidden',
              }}
            >
              <div
                style={{
                  height: '100%',
                  width: `${(frame % 300) / 3}%`,
                  backgroundColor: '#38bdf8',
                  boxShadow: '0 0 10px #38bdf8',
                }}
              />
            </div>
          </div>
        </CodeWindow>
      </div>

      <TutorialSubtitle
        text="Langkah empat, jalankan npm start untuk membuka Remotion Studio di browser. Di sini kamu bisa preview animasi dan timeline secara real-time."
        highlightWords={['npm', 'start', 'remotion', 'studio', 'browser', 'preview', 'real-time']}
      />
    </AbsoluteFill>
  );
};
