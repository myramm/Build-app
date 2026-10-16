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
        backgroundColor: '#000000',
        overflow: 'hidden',
        fontFamily: "'DM Sans', sans-serif",
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
            backgroundColor: '#0F0F23',
            border: '1px solid #1E1B4B',
            borderRadius: 12,
            padding: '24px 28px',
            fontFamily: "'Space Grotesk', monospace",
          }}
        >
          <div style={{ color: '#94A3B8', fontSize: 15, marginBottom: 16, letterSpacing: '0.05em' }}>
            CREATE-VIDEO SCAFFOLDING
          </div>

          <div style={{ fontSize: 26, lineHeight: 1.8 }}>
            <span style={{ color: '#64748B' }}>$ </span>
            <span style={{ color: '#E11D48', fontWeight: 800 }}>{typedCommand}</span>
            {frame < 80 && frame % 30 < 15 && (
              <span style={{ color: '#E11D48' }}>_</span>
            )}
          </div>

          {frame >= 85 && (
            <div style={{ marginTop: 12, fontSize: 20, color: '#94A3B8' }}>
              <div>? Nama proyek: <span style={{ color: '#F8FAFC', fontWeight: 700 }}>my-video</span></div>
              <div style={{ marginTop: 4 }}>
                ? Template: <span style={{ color: '#E11D48', fontWeight: 700 }}>TypeScript (Blank / Recommended)</span>
              </div>
            </div>
          )}
        </div>

        {/* Real File Structure Generated */}
        {frame >= 140 && (
          <div
            style={{
              backgroundColor: '#0F0F23',
              border: '1px solid #1E1B4B',
              borderRadius: 12,
              padding: '24px 28px',
              fontFamily: "'Space Grotesk', monospace",
            }}
          >
            <div style={{ color: '#94A3B8', fontSize: 15, marginBottom: 14, letterSpacing: '0.05em' }}>
              STRUKTUR PROYEK YANG DIHASILKAN
            </div>

            <div
              style={{
                fontSize: 19,
                lineHeight: 1.7,
                color: '#CBD5E1',
              }}
            >
              <div>my-video/</div>
              <div>├── <span style={{ color: '#F59E0B' }}>remotion.config.ts</span> <span style={{ color: '#64748B' }}># Konfigurasi Chromium & GL</span></div>
              <div>├── <span style={{ color: '#38BDF8' }}>package.json</span>       <span style={{ color: '#64748B' }}># Dependensi Remotion</span></div>
              <div>└── src/</div>
              <div>&nbsp;&nbsp;&nbsp;&nbsp;├── <span style={{ color: '#E11D48' }}>index.ts</span>         <span style={{ color: '#64748B' }}># Entry point render</span></div>
              <div>&nbsp;&nbsp;&nbsp;&nbsp;├── <span style={{ color: '#E11D48' }}>Root.tsx</span>         <span style={{ color: '#64748B' }}># Registrasi durasi & FPS</span></div>
              <div>&nbsp;&nbsp;&nbsp;&nbsp;└── <span style={{ color: '#E11D48' }}>Composition.tsx</span>  <span style={{ color: '#64748B' }}># Tempat koding video React</span></div>
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
