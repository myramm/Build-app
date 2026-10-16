import React from 'react';
import {
  AbsoluteFill,
  useCurrentFrame,
} from 'remotion';
import { CodeWindow } from '../CodeWindow';
import { TutorialHeader } from '../TutorialHeader';
import { TutorialSubtitle } from '../TutorialSubtitle';

export const Scene3Install: React.FC = () => {
  const frame = useCurrentFrame();

  const command = 'npx create-video@latest';
  const typedLength = Math.min(command.length, Math.floor(frame / 4));
  const typedCommand = command.slice(0, typedLength);

  return (
    <AbsoluteFill
      style={{
        backgroundColor: '#0a0f1d',
        overflow: 'hidden',
      }}
    >
      <TutorialHeader step="INSTALASI REMOTION" stepNumber={3} />

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
        <CodeWindow title="terminal — create-video installer" icon="📦">
          {/* Main command */}
          <div style={{ fontSize: 28, lineHeight: 1.8 }}>
            <span style={{ color: '#4ade80' }}>user@dev:~$ </span>
            <span style={{ color: '#38bdf8', fontWeight: 800 }}>
              {typedCommand}
            </span>
            {frame < 90 && frame % 30 < 15 && (
              <span style={{ color: '#ffffff' }}>▍</span>
            )}
          </div>

          {/* Interactive Prompt 1: Project Name */}
          {frame >= 95 && (
            <div style={{ marginTop: 20, fontSize: 24, color: '#e2e8f0' }}>
              <span style={{ color: '#38bdf8' }}>?</span>{' '}
              <span style={{ fontWeight: 700 }}>
                What would you like to name your video?
              </span>{' '}
              <span style={{ color: '#4ade80', fontWeight: 800 }}>my-video</span>
            </div>
          )}

          {/* Interactive Prompt 2: Template Selection */}
          {frame >= 150 && (
            <div style={{ marginTop: 14, fontSize: 24, color: '#e2e8f0' }}>
              <span style={{ color: '#38bdf8' }}>?</span>{' '}
              <span style={{ fontWeight: 700 }}>Select template:</span>
              <div
                style={{
                  marginTop: 8,
                  paddingLeft: 20,
                  display: 'flex',
                  flexDirection: 'column',
                  gap: 6,
                  fontSize: 22,
                }}
              >
                <div style={{ color: '#38bdf8', fontWeight: 800 }}>
                  ❯ TypeScript (Blank / Recommended)
                </div>
                <div style={{ color: '#64748b' }}>
                  React + Tailwind
                </div>
                <div style={{ color: '#64748b' }}>
                  Next.js App Router
                </div>
              </div>
            </div>
          )}

          {/* Success Output */}
          {frame >= 220 && (
            <div
              style={{
                marginTop: 24,
                backgroundColor: 'rgba(34, 197, 94, 0.1)',
                border: '1px solid rgba(34, 197, 94, 0.3)',
                borderRadius: 12,
                padding: '16px 20px',
                color: '#4ade80',
                fontSize: 22,
                fontFamily: 'monospace',
              }}
            >
              <div>✔ Project created successfully in ./my-video</div>
              <div style={{ color: '#ffffff', marginTop: 8 }}>
                Next steps: <span style={{ color: '#fbbf24' }}>cd my-video</span>
              </div>
            </div>
          )}
        </CodeWindow>
      </div>

      <TutorialSubtitle
        text="Langkah dua, instalasi Remotion. Cukup ketik npx create-video@latest di terminal, pilih template TypeScript, lalu masuk ke folder proyek."
        highlightWords={['instalasi', 'npx', 'create-video@latest', 'typescript', 'folder']}
      />
    </AbsoluteFill>
  );
};
