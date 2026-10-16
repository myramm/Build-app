import React from 'react';
import {
  AbsoluteFill,
  interpolate,
  Sequence,
  spring,
  useCurrentFrame,
  useVideoConfig,
} from 'remotion';

// Komponen Card / Box Informasi
const InfoCard: React.FC<{
  badge: string;
  badgeColor?: string;
  title: string;
  highlightText?: string;
  description: string;
  icon: string;
  frameOffset?: number;
}> = ({ badge, badgeColor = '#f59e0b', title, highlightText, description, icon }) => {
  const frame = useCurrentFrame();
  const { fps } = useVideoConfig();

  const scale = spring({
    frame,
    fps,
    config: { damping: 14, mass: 0.8 },
  });

  const textOpacity = interpolate(frame, [10, 25], [0, 1], {
    extrapolateLeft: 'clamp',
    extrapolateRight: 'clamp',
  });

  const iconBounce = Math.sin(frame / 6) * 8;

  return (
    <div
      style={{
        display: 'flex',
        flexDirection: 'column',
        alignItems: 'center',
        justifyContent: 'center',
        padding: '0 60px',
        textAlign: 'center',
        width: '100%',
        maxWidth: 960,
        transform: `scale(${scale})`,
      }}
    >
      {/* Icon / Avatar */}
      <div
        style={{
          fontSize: 120,
          marginBottom: 30,
          transform: `translateY(${iconBounce}px)`,
          filter: 'drop-shadow(0 15px 25px rgba(0,0,0,0.5))',
        }}
      >
        {icon}
      </div>

      {/* Badge Tag */}
      <div
        style={{
          backgroundColor: badgeColor,
          color: '#000000',
          fontWeight: 800,
          fontSize: 26,
          padding: '10px 28px',
          borderRadius: 999,
          textTransform: 'uppercase',
          letterSpacing: 3,
          marginBottom: 28,
          boxShadow: '0 8px 24px rgba(245, 158, 11, 0.35)',
        }}
      >
        {badge}
      </div>

      {/* Title */}
      <h1
        style={{
          color: '#ffffff',
          fontSize: 68,
          fontWeight: 900,
          lineHeight: 1.15,
          margin: 0,
          letterSpacing: '-1.5px',
          textShadow: '0 4px 20px rgba(0,0,0,0.8)',
        }}
      >
        {title}
        {highlightText && (
          <span
            style={{
              display: 'block',
              color: '#fbbf24',
              marginTop: 10,
              fontSize: 74,
            }}
          >
            {highlightText}
          </span>
        )}
      </h1>

      {/* Description / Story text */}
      <p
        style={{
          color: '#e2e8f0',
          fontSize: 38,
          lineHeight: 1.45,
          fontWeight: 500,
          marginTop: 32,
          opacity: textOpacity,
          textShadow: '0 2px 10px rgba(0,0,0,0.7)',
        }}
      >
        {description}
      </p>
    </div>
  );
};

export const MainComposition: React.FC = () => {
  const frame = useCurrentFrame();
  const { durationInFrames } = useVideoConfig();

  // Progress Bar Width
  const progressPercent = (frame / durationInFrames) * 100;

  // Background Pulse
  const bgPulse = 1 + Math.sin(frame / 20) * 0.03;

  return (
    <AbsoluteFill
      style={{
        backgroundColor: '#0c0f14',
        fontFamily: "'Segoe UI', Roboto, Helvetica, Arial, sans-serif",
        color: '#ffffff',
        overflow: 'hidden',
      }}
    >
      {/* Background Military Glow / Vignette */}
      <AbsoluteFill
        style={{
          background:
            'radial-gradient(circle at 50% 40%, rgba(217, 119, 6, 0.18) 0%, rgba(15, 23, 42, 0.95) 70%, #05070a 100%)',
          transform: `scale(${bgPulse})`,
        }}
      />

      {/* Top Header & Progress Bar */}
      <div
        style={{
          position: 'absolute',
          top: 0,
          left: 0,
          right: 0,
          zIndex: 50,
        }}
      >
        {/* Progress Line */}
        <div
          style={{
            height: 10,
            width: `${progressPercent}%`,
            backgroundColor: '#f59e0b',
            boxShadow: '0 0 16px #f59e0b',
          }}
        />

        {/* Top Channel Header */}
        <div
          style={{
            display: 'flex',
            justifyContent: 'center',
            alignItems: 'center',
            padding: '40px 20px 0 20px',
          }}
        >
          <div
            style={{
              fontSize: 22,
              fontWeight: 800,
              letterSpacing: 4,
              color: 'rgba(255, 255, 255, 0.65)',
              textTransform: 'uppercase',
              borderBottom: '2px solid rgba(245, 158, 11, 0.4)',
              paddingBottom: 8,
            }}
          >
            ⚔️ FAKTA PERANG DUNIA II ⚔️
          </div>
        </div>
      </div>

      {/* Main Content Scenes (450 frames = 15 detik @ 30 fps) */}
      <AbsoluteFill
        style={{
          display: 'flex',
          alignItems: 'center',
          justifyContent: 'center',
        }}
      >
        {/* Scene 1: 0 - 100 frame (0 - 3.3 detik) - Hook */}
        <Sequence from={0} durationInFrames={100}>
          <InfoCard
            badge="Tahukah Kamu?"
            badgeColor="#ef4444"
            icon="🪖"
            title="Ada Tentara Beruang di"
            highlightText="Perang Dunia II!"
            description="Bukan sekadar maskot, beruang ini resmi terdaftar memiliki pangkat militer dan gaji!"
          />
        </Sequence>

        {/* Scene 2: 100 - 220 frame (3.3 - 7.3 detik) - Siapa dia? */}
        <Sequence from={100} durationInFrames={120}>
          <InfoCard
            badge="Kisah Nyata"
            badgeColor="#f59e0b"
            icon="🐻"
            title="Namanya Wojtek"
            highlightText="Beruang Suriah"
            description="Diadopsi tentara Polandia tahun 1942. Dia diajari memberi hormat dan minum kopi bersama prajurit."
          />
        </Sequence>

        {/* Scene 3: 220 - 340 frame (7.3 - 11.3 detik) - Peran di perang */}
        <Sequence from={220} durationInFrames={120}>
          <InfoCard
            badge="Medan Tempur"
            badgeColor="#10b981"
            icon="💣"
            title="Pertempuran"
            highlightText="Monte Cassino 1944"
            description="Wojtek membantu memindahkan peti amunisi peluru artileri seberat 45 kg tanpa pernah menjatuhkannya!"
          />
        </Sequence>

        {/* Scene 4: 340 - 450 frame (11.3 - 15 detik) - Naik pangkat & lambang */}
        <Sequence from={340} durationInFrames={110}>
          <InfoCard
            badge="Pahlawan Perang"
            badgeColor="#3b82f6"
            icon="🎖️"
            title="Diangkat Menjadi"
            highlightText="KOPRAL WOJTEK"
            description="Ia resmi diberi buku gaji, dan lambang kompinya diubah menjadi gambar beruang pembawa peluru!"
          />
        </Sequence>
      </AbsoluteFill>

      {/* Footer / Watermark */}
      <div
        style={{
          position: 'absolute',
          bottom: 60,
          left: 0,
          right: 0,
          textAlign: 'center',
          color: 'rgba(255, 255, 255, 0.45)',
          fontSize: 22,
          fontWeight: 600,
          letterSpacing: 2,
        }}
      >
        FOLLOW UNTUK FAKTA SEJARAH LAINNYA 🔔
      </div>
    </AbsoluteFill>
  );
};
