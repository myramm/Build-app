import React from 'react';
import {
  AbsoluteFill,
  useCurrentFrame,
} from 'remotion';
import { CodeWindow } from '../CodeWindow';
import { TutorialHeader } from '../TutorialHeader';
import { TutorialSubtitle } from '../TutorialSubtitle';

export const Scene6Code: React.FC = () => {
  const frame = useCurrentFrame();

  return (
    <AbsoluteFill
      style={{
        backgroundColor: '#0a0f1d',
        overflow: 'hidden',
      }}
    >
      <TutorialHeader step="KODING KOMPONEN REACT PERTAMA" stepNumber={6} />

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
        <CodeWindow title="VS Code — src/Composition.tsx" icon="📝">
          <div
            style={{
              fontSize: 22,
              lineHeight: 1.7,
              fontFamily: "'Fira Code', Consolas, monospace",
            }}
          >
            <div>
              <span style={{ color: '#c084fc' }}>import </span>
              <span style={{ color: '#38bdf8' }}>
                &#123; spring, interpolate, useCurrentFrame &#125;
              </span>
              <span style={{ color: '#c084fc' }}> from </span>
              <span style={{ color: '#a3e635' }}>'remotion'</span>;
            </div>

            <div style={{ marginTop: 12 }}>
              <span style={{ color: '#c084fc' }}>export const </span>
              <span style={{ color: '#67e8f9' }}>MyVideo = </span>
              <span style={{ color: '#fbbf24' }}>() =&gt; &#123;</span>
            </div>

            <div style={{ paddingLeft: 24, marginTop: 4 }}>
              <div>
                <span style={{ color: '#c084fc' }}>const </span>
                <span style={{ color: '#ffffff' }}>frame = </span>
                <span style={{ color: '#67e8f9' }}>useCurrentFrame()</span>;
              </div>

              <div style={{ marginTop: 8 }}>
                <span style={{ color: '#64748b' }}>// Animasi Spring Halus 60 FPS</span>
              </div>
              <div>
                <span style={{ color: '#c084fc' }}>const </span>
                <span style={{ color: '#ffffff' }}>scale = </span>
                <span style={{ color: '#67e8f9' }}>spring</span>
                <span style={{ color: '#fbbf24' }}>
                  &#40;&#123; frame, fps: 60 &#125;&#41;
                </span>;
              </div>

              <div style={{ marginTop: 8 }}>
                <span style={{ color: '#64748b' }}>// Transisi Opasitas Teks</span>
              </div>
              <div>
                <span style={{ color: '#c084fc' }}>const </span>
                <span style={{ color: '#ffffff' }}>opacity = </span>
                <span style={{ color: '#67e8f9' }}>interpolate</span>
                <span style={{ color: '#fbbf24' }}>
                  &#40;frame, [0, 30], [0, 1]&#41;
                </span>;
              </div>

              <div style={{ marginTop: 12 }}>
                <span style={{ color: '#c084fc' }}>return </span>
                <span style={{ color: '#38bdf8' }}>&lt;h1</span>
                <span style={{ color: '#f59e0b' }}>
                  {' '}
                  style=&#123;&#123; transform: `scale($&#123;scale&#125;)`, opacity &#125;&#125;
                </span>
                <span style={{ color: '#38bdf8' }}>&gt;</span>
              </div>
              <div style={{ paddingLeft: 24, color: '#4ade80', fontWeight: 800 }}>
                Halo Remotion!
              </div>
              <div>
                <span style={{ color: '#38bdf8' }}>&lt;/h1&gt;</span>;
              </div>
            </div>

            <div style={{ color: '#fbbf24' }}>&#125;;</div>
          </div>
        </CodeWindow>
      </div>

      <TutorialSubtitle
        text="Langkah lima, buat komponen video di Composition.tsx. Gunakan fungsi spring dan interpolate untuk animasi 60 FPS yang sangat halus."
        highlightWords={['composition.tsx', 'spring', 'interpolate', 'animasi', '60', 'fps', 'halus']}
      />
    </AbsoluteFill>
  );
};
