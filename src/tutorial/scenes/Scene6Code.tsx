import React from 'react';
import {
  AbsoluteFill,
  useCurrentFrame,
} from 'remotion';
import { TutorialHeader } from '../TutorialHeader';
import { TutorialSubtitle } from '../TutorialSubtitle';

export const Scene6Code: React.FC = () => {
  const frame = useCurrentFrame();

  return (
    <AbsoluteFill
      style={{
        backgroundColor: '#030712',
        overflow: 'hidden',
      }}
    >
      <TutorialHeader step="Koding Komponen React" stepNumber={6} />

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
          gap: 16,
        }}
      >
        {/* Code Editor Block */}
        <div
          style={{
            backgroundColor: '#0f172a',
            border: '1px solid #1e293b',
            borderRadius: 12,
            padding: '24px 28px',
            fontFamily: "'Fira Code', monospace",
          }}
        >
          <div
            style={{
              display: 'flex',
              justifyContent: 'space-between',
              borderBottom: '1px solid #1e293b',
              paddingBottom: 12,
              marginBottom: 16,
              fontSize: 16,
              color: '#94a3b8',
            }}
          >
            <span>src/Composition.tsx</span>
            <span style={{ color: '#38bdf8' }}>TypeScript React</span>
          </div>

          <div
            style={{
              fontSize: 21,
              lineHeight: 1.75,
              color: '#f8fafc',
            }}
          >
            <div>
              <span style={{ color: '#c084fc' }}>import </span>
              <span style={{ color: '#38bdf8' }}>&#123; spring, interpolate, useCurrentFrame &#125;</span>
              <span style={{ color: '#c084fc' }}> from </span>
              <span style={{ color: '#a3e635' }}>'remotion'</span>;
            </div>

            <div style={{ marginTop: 12 }}>
              <span style={{ color: '#c084fc' }}>export const </span>
              <span style={{ color: '#67e8f9' }}>Video = </span>
              <span style={{ color: '#fbbf24' }}>() =&gt; &#123;</span>
            </div>

            <div style={{ paddingLeft: 24 }}>
              <div>
                <span style={{ color: '#c084fc' }}>const </span>
                <span style={{ color: '#f8fafc' }}>frame = </span>
                <span style={{ color: '#67e8f9' }}>useCurrentFrame()</span>;
              </div>

              <div style={{ marginTop: 8 }}>
                <span style={{ color: '#64748b' }}>// Animasi Spring 60 FPS</span>
              </div>
              <div>
                <span style={{ color: '#c084fc' }}>const </span>
                <span style={{ color: '#f8fafc' }}>scale = </span>
                <span style={{ color: '#67e8f9' }}>spring</span>
                <span style={{ color: '#fbbf24' }}>&#40;&#123; frame, fps: 60 &#125;&#41;</span>;
              </div>

              <div style={{ marginTop: 8 }}>
                <span style={{ color: '#64748b' }}>// Pemetaan Nilai Opasitas</span>
              </div>
              <div>
                <span style={{ color: '#c084fc' }}>const </span>
                <span style={{ color: '#f8fafc' }}>opacity = </span>
                <span style={{ color: '#67e8f9' }}>interpolate</span>
                <span style={{ color: '#fbbf24' }}>&#40;frame, [0, 30], [0, 1]&#41;</span>;
              </div>

              <div style={{ marginTop: 10 }}>
                <span style={{ color: '#c084fc' }}>return </span>
                <span style={{ color: '#38bdf8' }}>&lt;h1</span>
                <span style={{ color: '#f59e0b' }}> style=&#123;&#123; transform: `scale($&#123;scale&#125;)`, opacity &#125;&#125;</span>
                <span style={{ color: '#38bdf8' }}>&gt;</span>
                <span style={{ color: '#10b981', fontWeight: 700 }}> Halo Dunia! </span>
                <span style={{ color: '#38bdf8' }}>&lt;/h1&gt;</span>;
              </div>
            </div>

            <div style={{ color: '#fbbf24' }}>&#125;;</div>
          </div>
        </div>

        {/* Function Explanations */}
        <div
          style={{
            display: 'grid',
            gridTemplateColumns: '1fr 1fr',
            gap: 14,
            fontSize: 16,
            fontFamily: "'Fira Code', monospace",
          }}
        >
          <div
            style={{
              backgroundColor: '#0f172a',
              border: '1px solid #1e293b',
              borderRadius: 8,
              padding: '14px 18px',
            }}
          >
            <div style={{ color: '#10b981', fontWeight: 800 }}>spring()</div>
            <div style={{ color: '#94a3b8', marginTop: 4 }}>
              Fisika pegas alami, tidak kaku seperti linear ease.
            </div>
          </div>

          <div
            style={{
              backgroundColor: '#0f172a',
              border: '1px solid #1e293b',
              borderRadius: 8,
              padding: '14px 18px',
            }}
          >
            <div style={{ color: '#38bdf8', fontWeight: 800 }}>interpolate()</div>
            <div style={{ color: '#94a3b8', marginTop: 4 }}>
              Memetakan rentang frame ke nilai properti CSS.
            </div>
          </div>
        </div>
      </div>

      <TutorialSubtitle
        text="Langkah kelima, buat komponen video di Composition.tsx. Gunakan fungsi spring dan interpolate untuk menghasilkan animasi 60 FPS yang sangat halus."
        highlightWords={['kelima', 'komponen', 'composition.tsx', 'spring', 'interpolate', 'animasi', '60', 'fps', 'halus']}
      />
    </AbsoluteFill>
  );
};
