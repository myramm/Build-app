import React from 'react';
import {
  AbsoluteFill,
  interpolate,
  spring,
  useCurrentFrame,
  useVideoConfig,
} from 'remotion';
import { CodeWindow } from '../CodeWindow';
import { TutorialHeader } from '../TutorialHeader';
import { TutorialSubtitle } from '../TutorialSubtitle';

export const Scene7Render: React.FC = () => {
  const frame = useCurrentFrame();
  const { fps } = useVideoConfig();

  // Render progress simulation (0% to 100% over 250 frames)
  const renderPercent = Math.min(
    100,
    Math.floor(
      interpolate(frame, [40, 240], [0, 100], {
        extrapolateLeft: 'clamp',
        extrapolateRight: 'clamp',
      })
    )
  );

  const doneScale = spring({
    frame: frame - 250,
    fps,
    config: { damping: 12, mass: 0.6 },
  });

  return (
    <AbsoluteFill
      style={{
        backgroundColor: '#0a0f1d',
        overflow: 'hidden',
      }}
    >
      <TutorialHeader step="RENDER MENJADI MP4" stepNumber={7} />

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
        <CodeWindow title="terminal — render video" icon="🎬">
          {/* Command */}
          <div style={{ fontSize: 26, lineHeight: 1.8 }}>
            <span style={{ color: '#4ade80' }}>user@dev:~/my-video$ </span>
            <span style={{ color: '#38bdf8', fontWeight: 800 }}>
              npx remotion render Main out/video2.mp4
            </span>
          </div>

          {/* Progress Bar inside Terminal */}
          <div style={{ marginTop: 28 }}>
            <div
              style={{
                display: 'flex',
                justifyContent: 'space-between',
                color: '#e2e8f0',
                fontSize: 22,
                fontFamily: 'monospace',
                marginBottom: 10,
              }}
            >
              <span>Rendering 1080×1920 (60 FPS)...</span>
              <span style={{ color: '#38bdf8', fontWeight: 800 }}>
                {renderPercent}%
              </span>
            </div>

            <div
              style={{
                height: 16,
                backgroundColor: '#1e293b',
                borderRadius: 8,
                overflow: 'hidden',
              }}
            >
              <div
                style={{
                  height: '100%',
                  width: `${renderPercent}%`,
                  backgroundColor: '#38bdf8',
                  boxShadow: '0 0 16px #38bdf8',
                }}
              />
            </div>
          </div>

          {/* Success Box */}
          {frame >= 250 && (
            <div
              style={{
                marginTop: 32,
                transform: `scale(${Math.max(0, doneScale)})`,
                backgroundColor: 'rgba(34, 197, 94, 0.15)',
                border: '2px solid #22c55e',
                borderRadius: 16,
                padding: '20px 24px',
                display: 'flex',
                alignItems: 'center',
                gap: 20,
              }}
            >
              <div style={{ fontSize: 44 }}>🎉</div>
              <div>
                <div style={{ color: '#4ade80', fontSize: 26, fontWeight: 900 }}>
                  RENDER SUKSES: out/video2.mp4
                </div>
                <div style={{ color: '#ffffff', fontSize: 20, marginTop: 4 }}>
                  Resolusi 1080×1920 | 60 FPS Murni | Siap diupload!
                </div>
              </div>
            </div>
          )}

          {/* Call to action follow */}
          {frame >= 320 && (
            <div
              style={{
                marginTop: 24,
                backgroundColor: '#ef4444',
                color: '#ffffff',
                borderRadius: 12,
                padding: '14px 20px',
                textAlign: 'center',
                fontWeight: 900,
                fontSize: 22,
                letterSpacing: 2,
                boxShadow: '0 0 20px rgba(239, 68, 68, 0.6)',
              }}
            >
              🔔 FOLLOW UNTUK TUTORIAL AI & CODING LAINNYA!
            </div>
          )}
        </CodeWindow>
      </div>

      <TutorialSubtitle
        text="Terakhir, render videomu menjadi MP4 dengan npx remotion render! Video berhasil dibuat dan siap ditonton. Jangan lupa follow untuk tips AI lainnya!"
        highlightWords={['render', 'mp4', 'npx', 'remotion', 'render', 'video2.mp4', 'follow']}
      />
    </AbsoluteFill>
  );
};
