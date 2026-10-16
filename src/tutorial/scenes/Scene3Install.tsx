import React from 'react';
import {
  AbsoluteFill,
  useCurrentFrame,
} from 'remotion';
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
        backgroundColor: '#030712',
        overflow: 'hidden',
      }}
    >
      <TutorialHeader step="Instalasi Remotion" stepNumber={3} />

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
            padding: '24px 28px',
            fontFamily: "'Fira Code', monospace",
          }}
        >
          <div style={{ color: '#64748b', fontSize: 16, marginBottom: 16 }}>
            CREATE-VIDEO SCAFFOLDING
          </div>

          <div style={{ fontSize: 26, lineHeight: 1.8 }}>
            <span style={{ color: '#64748b' }}>$ </span>
            <span style={{ color: '#10b981', fontWeight: 800 }}>{typedCommand}</span>
            {frame < 80 && frame % 30 < 15 && (
              <span style={{ color: '#10b981' }}>_</span>
            )}
          </div>

          {frame >= 85 && (
            <div style={{ marginTop: 12, fontSize: 20, color: '#94a3b8' }}>
              <div>? Nama proyek: <span style={{ color: '#f8fafc', fontWeight: 700 }}>my-video</span></div>
              <div style={{ marginTop: 4 }}>
                ? Template: <span style={{ color: '#10b981', fontWeight: 700 }}>TypeScript (Blank / Recommended)</span>
              </div>
            </div>
          )}
        </div>

        {/* Real File Structure Generated */}
        {frame >= 140 && (
          <div
            style={{
              backgroundColor: '#0f172a',
              border: '1px solid #1e293b',
              borderRadius: 12,
              padding: '24px 28px',
              fontFamily: "'Fira Code', monospace",
            }}
          >
            <div style={{ color: '#64748b', fontSize: 16, marginBottom: 14 }}>
              STRUKTUR PROYEK YANG DIHASILKAN
            </div>

            <div
              style={{
                fontSize: 19,
                lineHeight: 1.7,
                color: '#cbd5e1',
              }}
            >
              <div>my-video/</div>
              <div>├── <span style={{ color: '#f59e0b' }}>remotion.config.ts</span> <span style={{ color: '#64748b' }}># Konfigurasi Chromium & Gl</span></div>
              <div>├── <span style={{ color: '#38bdf8' }}>package.json</span>       <span style={{ color: '#64748b' }}># Dependensi Remotion</span></div>
              <div>└── src/</div>
              <div>&nbsp;&nbsp;&nbsp;&nbsp;├── <span style={{ color: '#10b981' }}>index.ts</span>         <span style={{ color: '#64748b' }}># Entry point render</span></div>
              <div>&nbsp;&nbsp;&nbsp;&nbsp;├── <span style={{ color: '#10b981' }}>Root.tsx</span>         <span style={{ color: '#64748b' }}># Registrasi durasi & FPS</span></div>
              <div>&nbsp;&nbsp;&nbsp;&nbsp;└── <span style={{ color: '#10b981' }}>Composition.tsx</span>  <span style={{ color: '#64748b' }}># Tempat koding video React</span></div>
            </div>
          </div>
        )}
      </div>

      <TutorialSubtitle
        text="Langkah kedua, instalasi Remotion. Ketik npx create-video@latest di terminal, pilih template TypeScript, lalu masuk ke folder proyek kalian."
        highlightWords={['kedua', 'instalasi', 'remotion', 'npx', 'create-video@latest', 'typescript', 'folder']}
      />
    </AbsoluteFill>
  );
};
