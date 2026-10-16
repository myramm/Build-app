import React from 'react';
import {
  AbsoluteFill,
  useCurrentFrame,
} from 'remotion';
import { TutorialHeader } from '../TutorialHeader';
import { TutorialSubtitle } from '../TutorialSubtitle';

export const Scene2Prereq: React.FC = () => {
  const frame = useCurrentFrame();

  const cmd1Length = Math.min(7, Math.floor(frame / 5));
  const cmd1Text = 'node -v'.slice(0, cmd1Length);
  const showOut1 = frame >= 40;

  const cmd2Length = Math.max(0, Math.min(6, Math.floor((frame - 80) / 5)));
  const cmd2Text = 'npm -v'.slice(0, cmd2Length);
  const showOut2 = frame >= 120;

  return (
    <AbsoluteFill
      style={{
        backgroundColor: '#000000',
        overflow: 'hidden',
        fontFamily: "'DM Sans', sans-serif",
      }}
    >
      <TutorialHeader step="Persiapan Lingkungan" stepNumber={2} />

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
        {/* Real CLI Verification Block */}
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
            TERMINAL VERIFIKASI RUNTIME
          </div>

          {/* Node check */}
          <div style={{ fontSize: 26, lineHeight: 1.8 }}>
            <span style={{ color: '#64748B' }}>$ </span>
            <span style={{ color: '#F8FAFC', fontWeight: 700 }}>{cmd1Text}</span>
            {frame < 40 && frame % 30 < 15 && (
              <span style={{ color: '#E11D48' }}>_</span>
            )}
          </div>

          {showOut1 && (
            <div
              style={{
                fontSize: 22,
                color: '#10B981',
                paddingLeft: 24,
                marginBottom: 16,
                fontWeight: 700,
              }}
            >
              v20.18.0 <span style={{ color: '#64748B', fontWeight: 400 }}>(LTS / Ready)</span>
            </div>
          )}

          {/* npm check */}
          {frame >= 70 && (
            <div style={{ fontSize: 26, lineHeight: 1.8 }}>
              <span style={{ color: '#64748B' }}>$ </span>
              <span style={{ color: '#F8FAFC', fontWeight: 700 }}>{cmd2Text}</span>
              {frame < 120 && frame % 30 < 15 && (
                <span style={{ color: '#E11D48' }}>_</span>
              )}
            </div>
          )}

          {showOut2 && (
            <div
              style={{
                fontSize: 22,
                color: '#10B981',
                paddingLeft: 24,
                fontWeight: 700,
              }}
            >
              10.8.2 <span style={{ color: '#64748B', fontWeight: 400 }}>(Package Manager)</span>
            </div>
          )}
        </div>

        {/* System Requirement Matrix */}
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
            SPESIFIKASI MINIMAL RESMI
          </div>

          <div
            style={{
              display: 'grid',
              gridTemplateColumns: '1fr 1fr',
              gap: 16,
              fontSize: 18,
            }}
          >
            <div style={{ borderLeft: '3px solid #E11D48', paddingLeft: 14 }}>
              <div style={{ color: '#94A3B8' }}>Runtime</div>
              <div style={{ color: '#F8FAFC', fontWeight: 700, marginTop: 4 }}>
                Node.js &gt;= 18.0.0
              </div>
            </div>

            <div style={{ borderLeft: '3px solid #E11D48', paddingLeft: 14 }}>
              <div style={{ color: '#94A3B8' }}>Browser Engine</div>
              <div style={{ color: '#F8FAFC', fontWeight: 700, marginTop: 4 }}>
                Chromium / Chrome
              </div>
            </div>

            <div style={{ borderLeft: '3px solid #E11D48', paddingLeft: 14 }}>
              <div style={{ color: '#94A3B8' }}>Video Encoder</div>
              <div style={{ color: '#F8FAFC', fontWeight: 700, marginTop: 4 }}>
                FFmpeg (Built-in)
              </div>
            </div>

            <div style={{ borderLeft: '3px solid #E11D48', paddingLeft: 14 }}>
              <div style={{ color: '#94A3B8' }}>Sistem Operasi</div>
              <div style={{ color: '#F8FAFC', fontWeight: 700, marginTop: 4 }}>
                Linux / macOS / Windows
              </div>
            </div>
          </div>
        </div>
      </div>

      <TutorialSubtitle
        text="Langkah pertama, pastikan komputer kalian sudah terinstal Node.js versi 18 ke atas dan npm. Cukup buka terminal, lalu ketik perintah node -v dan npm -v."
        highlightWords={['pertama', 'node.js', '18', 'npm', 'terminal', 'node', '-v', 'npm', '-v']}
      />
    </AbsoluteFill>
  );
};
