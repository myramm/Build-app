import React from 'react';
import {
  AbsoluteFill,
  useCurrentFrame,
} from 'remotion';
import { TutorialHeader } from '../TutorialHeader';
import { TutorialSubtitle } from '../TutorialSubtitle';

export const Scene4AiSkill: React.FC = () => {
  const frame = useCurrentFrame();

  const command = 'npx skills add remotion-dev/skills';
  const typedLength = Math.min(command.length, Math.floor(frame / 4));
  const typedCommand = command.slice(0, typedLength);

  return (
    <AbsoluteFill
      style={{
        backgroundColor: '#030712',
        overflow: 'hidden',
      }}
    >
      <TutorialHeader step="Memasang AI Skill Remotion" stepNumber={4} />

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
            SKILLS CLI INTEGRATION
          </div>

          <div style={{ fontSize: 26, lineHeight: 1.8 }}>
            <span style={{ color: '#64748b' }}>my-video $ </span>
            <span style={{ color: '#10b981', fontWeight: 800 }}>{typedCommand}</span>
            {frame < 90 && frame % 30 < 15 && (
              <span style={{ color: '#10b981' }}>_</span>
            )}
          </div>

          {frame >= 95 && (
            <div
              style={{
                marginTop: 16,
                padding: '12px 16px',
                backgroundColor: '#1e293b',
                borderRadius: 8,
                fontSize: 18,
                color: '#cbd5e1',
                lineHeight: 1.6,
              }}
            >
              <div>✔ Source: github.com/remotion-dev/skills</div>
              <div style={{ color: '#10b981' }}>✔ Installed: remotion-best-practices</div>
              <div style={{ color: '#94a3b8' }}>Target: .agents/skills/ & Antigravity/Gemini</div>
            </div>
          )}
        </div>

        {/* Technical Architecture Table */}
        {frame >= 160 && (
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
              APA YANG DIPELAJARI AI SETELAH SKILL TERPASANG?
            </div>

            <div
              style={{
                display: 'flex',
                flexDirection: 'column',
                gap: 12,
                fontSize: 18,
                color: '#e2e8f0',
              }}
            >
              <div style={{ display: 'flex', gap: 12 }}>
                <span style={{ color: '#10b981', fontWeight: 800 }}>[1]</span>
                <span>Aturan Interpolasi: AI tidak lagi salah hitung frame vs detik</span>
              </div>
              <div style={{ display: 'flex', gap: 12 }}>
                <span style={{ color: '#10b981', fontWeight: 800 }}>[2]</span>
                <span>Fisika Spring: Menggunakan damping dan mass yang proporsional</span>
              </div>
              <div style={{ display: 'flex', gap: 12 }}>
                <span style={{ color: '#10b981', fontWeight: 800 }}>[3]</span>
                <span>Manajemen Aset: Penanganan audio dan font secara otomatis</span>
              </div>
            </div>
          </div>
        )}
      </div>

      <TutorialSubtitle
        text="Langkah ketiga, pasang AI Skill resmi Remotion. Jalankan perintah npx skills add remotion-dev/skills, agar AI seperti Gemini bisa coding video secara otomatis."
        highlightWords={['ketiga', 'ai', 'skill', 'resmi', 'remotion', 'npx', 'skills', 'add', 'gemini']}
      />
    </AbsoluteFill>
  );
};
