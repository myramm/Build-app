import React from 'react';
import {
  AbsoluteFill,
  interpolate,
  useCurrentFrame,
} from 'remotion';
import { TutorialHeader } from '../TutorialHeader';
import { TutorialSubtitle } from '../TutorialSubtitle';

export const Scene7Render: React.FC = () => {
  const frame = useCurrentFrame();

  const renderPercent = Math.min(
    100,
    Math.floor(
      interpolate(frame, [30, 240], [0, 100], {
        extrapolateLeft: 'clamp',
        extrapolateRight: 'clamp',
      })
    )
  );

  return (
    <AbsoluteFill
      style={{
        backgroundColor: '#030712',
        overflow: 'hidden',
      }}
    >
      <TutorialHeader step="Render Menjadi MP4" stepNumber={7} />

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
          <div style={{ color: '#64748b', fontSize: 16, marginBottom: 14 }}>
            PRODUCTION CLI RENDER
          </div>

          <div style={{ fontSize: 24, lineHeight: 1.8 }}>
            <span style={{ color: '#64748b' }}>my-video $ </span>
            <span style={{ color: '#10b981', fontWeight: 800 }}>
              npx remotion render Main out/video2.mp4
            </span>
          </div>

          {/* Progress Bar inside Terminal */}
          <div style={{ marginTop: 24 }}>
            <div
              style={{
                display: 'flex',
                justifyContent: 'space-between',
                color: '#94a3b8',
                fontSize: 18,
                marginBottom: 8,
              }}
            >
              <span>Encoding Chromium Frames to H.264...</span>
              <span style={{ color: '#10b981', fontWeight: 800 }}>
                {renderPercent}%
              </span>
            </div>

            <div
              style={{
                height: 10,
                backgroundColor: '#1e293b',
                borderRadius: 4,
                overflow: 'hidden',
              }}
            >
              <div
                style={{
                  height: '100%',
                  width: `${renderPercent}%`,
                  backgroundColor: '#10b981',
                }}
              />
            </div>
          </div>
        </div>

        {/* Render Specification & Output Card */}
        {frame >= 200 && (
          <div
            style={{
              backgroundColor: '#0f172a',
              border: '1px solid #10b981',
              borderRadius: 12,
              padding: '24px 28px',
              fontFamily: "'Fira Code', monospace",
            }}
          >
            <div
              style={{
                color: '#10b981',
                fontWeight: 800,
                fontSize: 20,
                marginBottom: 14,
              }}
            >
              ✔ RENDER COMPLETED SUCCESSFULLY
            </div>

            <div
              style={{
                display: 'grid',
                gridTemplateColumns: '1fr 1fr',
                gap: 16,
                fontSize: 18,
                color: '#cbd5e1',
              }}
            >
              <div>
                <span style={{ color: '#64748b' }}>File Output:</span>{' '}
                <span style={{ color: '#f8fafc', fontWeight: 700 }}>video2.mp4</span>
              </div>
              <div>
                <span style={{ color: '#64748b' }}>Resolusi:</span>{' '}
                <span style={{ color: '#f8fafc', fontWeight: 700 }}>1080 × 1920</span>
              </div>
              <div>
                <span style={{ color: '#64748b' }}>Frame Rate:</span>{' '}
                <span style={{ color: '#10b981', fontWeight: 700 }}>60.0 FPS</span>
              </div>
              <div>
                <span style={{ color: '#64748b' }}>Codec:</span>{' '}
                <span style={{ color: '#f8fafc', fontWeight: 700 }}>H.264 / AAC</span>
              </div>
            </div>
          </div>
        )}

        {/* Outro Call To Action */}
        {frame >= 280 && (
          <div
            style={{
              backgroundColor: '#1e293b',
              border: '1px solid #334155',
              borderRadius: 10,
              padding: '16px 24px',
              display: 'flex',
              justifyContent: 'space-between',
              alignItems: 'center',
              fontFamily: "'Segoe UI', Roboto, sans-serif",
            }}
          >
            <span style={{ color: '#f8fafc', fontWeight: 700, fontSize: 20 }}>
              Tutorial Selesai. Siap membuat video otomatis?
            </span>
            <span
              style={{
                color: '#10b981',
                fontFamily: "'Fira Code', monospace",
                fontWeight: 800,
                fontSize: 18,
              }}
            >
              FOLLOW FOR MORE →
            </span>
          </div>
        )}
      </div>

      <TutorialSubtitle
        text="Terakhir, render video kalian menjadi file MP4 dengan perintah npx remotion render! Video profesional siap dibagikan. Follow untuk tips teknologi lainnya!"
        highlightWords={['terakhir', 'render', 'mp4', 'npx', 'remotion', 'render', 'follow']}
      />
    </AbsoluteFill>
  );
};
