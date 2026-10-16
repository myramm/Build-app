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
        backgroundColor: '#000000',
        overflow: 'hidden',
        fontFamily: "'DM Sans', sans-serif",
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
            backgroundColor: '#0F0F23',
            border: '1px solid #1E1B4B',
            borderRadius: 12,
            padding: '24px 28px',
            fontFamily: "'Space Grotesk', monospace",
          }}
        >
          <div
            style={{
              display: 'flex',
              justifyContent: 'space-between',
              borderBottom: '1px solid #1E1B4B',
              paddingBottom: 12,
              marginBottom: 16,
              fontSize: 15,
              color: '#94A3B8',
            }}
          >
            <span>src/Composition.tsx</span>
            <span style={{ color: '#E11D48', fontWeight: 700 }}>TypeScript React</span>
          </div>

          <div
            style={{
              fontSize: 21,
              lineHeight: 1.75,
              color: '#F8FAFC',
            }}
          >
            <div>
              <span style={{ color: '#C084FC' }}>import </span>
              <span style={{ color: '#38BDF8' }}>&#123; spring, interpolate, useCurrentFrame &#125;</span>
              <span style={{ color: '#C084FC' }}> from </span>
              <span style={{ color: '#A3E635' }}>'remotion'</span>;
            </div>

            <div style={{ marginTop: 12 }}>
              <span style={{ color: '#C084FC' }}>export const </span>
              <span style={{ color: '#67E8F9' }}>Video = </span>
              <span style={{ color: '#FBBF24' }}>() =&gt; &#123;</span>
            </div>

            <div style={{ paddingLeft: 24 }}>
              <div>
                <span style={{ color: '#C084FC' }}>const </span>
                <span style={{ color: '#F8FAFC' }}>frame = </span>
                <span style={{ color: '#67E8F9' }}>useCurrentFrame()</span>;
              </div>

              <div style={{ marginTop: 8 }}>
                <span style={{ color: '#64748B' }}>// Animasi Spring 60 FPS</span>
              </div>
              <div>
                <span style={{ color: '#C084FC' }}>const </span>
                <span style={{ color: '#F8FAFC' }}>scale = </span>
                <span style={{ color: '#67E8F9' }}>spring</span>
                <span style={{ color: '#FBBF24' }}>&#40;&#123; frame, fps: 60 &#125;&#41;</span>;
              </div>

              <div style={{ marginTop: 8 }}>
                <span style={{ color: '#64748B' }}>// Pemetaan Nilai Opasitas</span>
              </div>
              <div>
                <span style={{ color: '#C084FC' }}>const </span>
                <span style={{ color: '#F8FAFC' }}>opacity = </span>
                <span style={{ color: '#67E8F9' }}>interpolate</span>
                <span style={{ color: '#FBBF24' }}>&#40;frame, [0, 30], [0, 1]&#41;</span>;
              </div>

              <div style={{ marginTop: 10 }}>
                <span style={{ color: '#C084FC' }}>return </span>
                <span style={{ color: '#38BDF8' }}>&lt;h1</span>
                <span style={{ color: '#F59E0B' }}> style=&#123;&#123; transform: `scale($&#123;scale&#125;)`, opacity &#125;&#125;</span>
                <span style={{ color: '#38BDF8' }}>&gt;</span>
                <span style={{ color: '#E11D48', fontWeight: 800 }}> Halo Dunia! </span>
                <span style={{ color: '#38BDF8' }}>&lt;/h1&gt;</span>;
              </div>
            </div>

            <div style={{ color: '#FBBF24' }}>&#125;;</div>
          </div>
        </div>

        {/* Function Explanations */}
        <div
          style={{
            display: 'grid',
            gridTemplateColumns: '1fr 1fr',
            gap: 14,
            fontSize: 16,
            fontFamily: "'Space Grotesk', monospace",
          }}
        >
          <div
            style={{
              backgroundColor: '#0F0F23',
              border: '1px solid #1E1B4B',
              borderRadius: 8,
              padding: '14px 18px',
            }}
          >
            <div style={{ color: '#E11D48', fontWeight: 800 }}>spring()</div>
            <div style={{ color: '#94A3B8', marginTop: 4 }}>
              Fisika pegas alami, tidak kaku seperti linear ease.
            </div>
          </div>

          <div
            style={{
              backgroundColor: '#0F0F23',
              border: '1px solid #1E1B4B',
              borderRadius: 8,
              padding: '14px 18px',
            }}
          >
            <div style={{ color: '#38BDF8', fontWeight: 800 }}>interpolate()</div>
            <div style={{ color: '#94A3B8', marginTop: 4 }}>
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
