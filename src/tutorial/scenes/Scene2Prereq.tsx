import React from 'react';
import {
  AbsoluteFill,
  interpolate,
  useCurrentFrame,
} from 'remotion';
import { CodeWindow } from '../CodeWindow';
import { TutorialHeader } from '../TutorialHeader';
import { TutorialSubtitle } from '../TutorialSubtitle';

export const Scene2Prereq: React.FC = () => {
  const frame = useCurrentFrame();

  // Typing effect for command 1
  const cmd1Length = Math.min(7, Math.floor(frame / 6));
  const cmd1Text = 'node -v'.slice(0, cmd1Length);

  // Output 1 appears after frame 45
  const showOut1 = frame >= 45;

  // Typing effect for command 2 (after frame 90)
  const cmd2Length = Math.max(0, Math.min(6, Math.floor((frame - 90) / 6)));
  const cmd2Text = 'npm -v'.slice(0, cmd2Length);

  // Output 2 appears after frame 130
  const showOut2 = frame >= 130;

  return (
    <AbsoluteFill
      style={{
        backgroundColor: '#0a0f1d',
        overflow: 'hidden',
      }}
    >
      <TutorialHeader step="PERSIAPAN LINGKUNGAN" stepNumber={2} />

      {/* Terminal Window Card */}
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
        <CodeWindow title="bash — node & npm check" icon="⚡">
          {/* Node check */}
          <div style={{ fontSize: 28, lineHeight: 1.8 }}>
            <span style={{ color: '#4ade80' }}>user@dev:~$ </span>
            <span style={{ color: '#ffffff', fontWeight: 700 }}>{cmd1Text}</span>
            {frame < 45 && frame % 30 < 15 && (
              <span style={{ color: '#38bdf8' }}>▍</span>
            )}
          </div>

          {showOut1 && (
            <div
              style={{
                fontSize: 26,
                color: '#38bdf8',
                backgroundColor: 'rgba(56, 189, 248, 0.1)',
                padding: '8px 16px',
                borderRadius: 8,
                marginTop: 6,
                marginBottom: 20,
                display: 'flex',
                justifyContent: 'space-between',
              }}
            >
              <span>v20.18.0</span>
              <span style={{ color: '#4ade80', fontWeight: 800 }}>
                ✓ Node.js 18+ OK
              </span>
            </div>
          )}

          {/* npm check */}
          {frame >= 80 && (
            <div style={{ fontSize: 28, lineHeight: 1.8 }}>
              <span style={{ color: '#4ade80' }}>user@dev:~$ </span>
              <span style={{ color: '#ffffff', fontWeight: 700 }}>{cmd2Text}</span>
              {frame < 130 && frame % 30 < 15 && (
                <span style={{ color: '#38bdf8' }}>▍</span>
              )}
            </div>
          )}

          {showOut2 && (
            <div
              style={{
                fontSize: 26,
                color: '#38bdf8',
                backgroundColor: 'rgba(56, 189, 248, 0.1)',
                padding: '8px 16px',
                borderRadius: 8,
                marginTop: 6,
                display: 'flex',
                justifyContent: 'space-between',
              }}
            >
              <span>10.8.2</span>
              <span style={{ color: '#4ade80', fontWeight: 800 }}>
                ✓ npm Package Manager OK
              </span>
            </div>
          )}

          {/* Summary requirements box */}
          {frame >= 170 && (
            <div
              style={{
                marginTop: 32,
                borderTop: '1px dashed rgba(255, 255, 255, 0.15)',
                paddingTop: 20,
                display: 'flex',
                flexDirection: 'column',
                gap: 12,
                fontSize: 22,
                color: '#e2e8f0',
              }}
            >
              <div style={{ color: '#f59e0b', fontWeight: 800 }}>
                PERSYARATAN MINIMAL:
              </div>
              <div>• Node.js 18.0.0 atau lebih tinggi</div>
              <div>• Chrome / Chromium (untuk render video headless)</div>
              <div>• FFmpeg (sudah otomatis ditangani Remotion)</div>
            </div>
          )}
        </CodeWindow>
      </div>

      <TutorialSubtitle
        text="Langkah satu, pastikan sudah terinstal Node.js versi 18 ke atas dan npm. Cek di terminal dengan perintah node -v dan npm -v."
        highlightWords={['node.js', '18', 'npm', 'terminal', 'node', '-v', 'npm', '-v']}
      />
    </AbsoluteFill>
  );
};
