import React from 'react';
import {
  AbsoluteFill,
  useCurrentFrame,
} from 'remotion';
import { CodeWindow } from '../CodeWindow';
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
        backgroundColor: '#0a0f1d',
        overflow: 'hidden',
      }}
    >
      <TutorialHeader step="MEMASANG AI SKILL REMOTION" stepNumber={4} />

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
        <CodeWindow title="bash — AI Agent Skills Integration" icon="🤖">
          {/* Main command */}
          <div style={{ fontSize: 26, lineHeight: 1.8 }}>
            <span style={{ color: '#4ade80' }}>user@dev:~/my-video$ </span>
            <span style={{ color: '#a855f7', fontWeight: 800 }}>
              {typedCommand}
            </span>
            {frame < 120 && frame % 30 < 15 && (
              <span style={{ color: '#ffffff' }}>▍</span>
            )}
          </div>

          {/* Installation log */}
          {frame >= 120 && (
            <div
              style={{
                marginTop: 20,
                fontSize: 22,
                color: '#cbd5e1',
                lineHeight: 1.6,
              }}
            >
              <div>● Antigravity / Gemini Agent detected</div>
              <div>◇ Source: https://github.com/remotion-dev/skills</div>
              <div style={{ color: '#38bdf8', marginTop: 6 }}>
                ✓ remotion-best-practices (installed)
              </div>
              <div style={{ color: '#38bdf8' }}>
                ✓ remotion-render & remotion-studio (ready)
              </div>
            </div>
          )}

          {/* Agent Capability Card */}
          {frame >= 200 && (
            <div
              style={{
                marginTop: 24,
                backgroundColor: 'rgba(168, 85, 247, 0.12)',
                border: '1.5px solid rgba(168, 85, 247, 0.4)',
                borderRadius: 14,
                padding: '18px 24px',
                display: 'flex',
                flexDirection: 'column',
                gap: 10,
              }}
            >
              <div
                style={{
                  color: '#c084fc',
                  fontWeight: 800,
                  fontSize: 22,
                  display: 'flex',
                  alignItems: 'center',
                  gap: 10,
                }}
              >
                <span>✨</span>
                <span>APA FUNGSI SKILL INI?</span>
              </div>
              <div style={{ color: '#e2e8f0', fontSize: 20, lineHeight: 1.5 }}>
                AI seperti <b>Gemini & Claude</b> sekarang paham aturan resmi Remotion (interpolasi, spring physics, durasi frame, dan render cloud).
              </div>
            </div>
          )}
        </CodeWindow>
      </div>

      <TutorialSubtitle
        text="Langkah tiga, pasang AI Skill resmi Remotion! Jalankan npx skills add remotion-dev/skills agar Gemini bisa menulis kode video otomatis."
        highlightWords={['ai', 'skill', 'resmi', 'remotion', 'npx', 'skills', 'add', 'gemini']}
      />
    </AbsoluteFill>
  );
};
