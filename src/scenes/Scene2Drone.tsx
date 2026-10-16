import React from 'react';
import {
  AbsoluteFill,
  interpolate,
  spring,
  useCurrentFrame,
  useVideoConfig,
} from 'remotion';
import { SubtitleBar } from '../components/SubtitleBar';

export const Scene2Drone: React.FC = () => {
  const frame = useCurrentFrame();
  const { fps } = useVideoConfig();

  // Smooth drone banking & floating
  const droneY = Math.sin(frame / 35) * 20;
  const droneTilt = Math.sin(frame / 40) * 4;
  const droneEntrance = spring({
    frame,
    fps,
    from: -150,
    to: 0,
    config: { damping: 20 },
  });

  // Sensor beam pulse
  const beamPulse = (Math.sin(frame / 15) + 1) / 2;

  // Signal waves pulsing to command
  const signalRing1 = (frame * 3) % 200;
  const signalRing2 = (frame * 3 + 100) % 200;

  return (
    <AbsoluteFill
      style={{
        backgroundColor: '#070b14',
        overflow: 'hidden',
      }}
    >
      {/* Background Dark Night Battlefield with Thermal Gradients */}
      <AbsoluteFill
        style={{
          background:
            'radial-gradient(ellipse at 50% 30%, #172554 0%, #0c1527 50%, #030712 100%)',
        }}
      />

      {/* Grid Floor / Tactical Map Projection */}
      <div
        style={{
          position: 'absolute',
          bottom: 240,
          left: -200,
          right: -200,
          height: 500,
          background:
            'linear-gradient(rgba(56, 189, 248, 0.15) 1px, transparent 1px), linear-gradient(90deg, rgba(56, 189, 248, 0.15) 1px, transparent 1px)',
          backgroundSize: '50px 50px',
          transform: 'perspective(400px) rotateX(60deg)',
          opacity: 0.7,
        }}
      />

      {/* Tactical Drone SVG Visualization */}
      <div
        style={{
          position: 'absolute',
          top: '32%',
          left: '50%',
          transform: `translate(-50%, calc(-50% + ${droneY + droneEntrance}px)) rotate(${droneTilt}deg)`,
          display: 'flex',
          flexDirection: 'column',
          alignItems: 'center',
        }}
      >
        {/* Sensor Scanning Cone Beaming Down */}
        <div
          style={{
            position: 'absolute',
            top: 120,
            width: 0,
            height: 0,
            borderLeft: '220px solid transparent',
            borderRight: '220px solid transparent',
            borderBottom: '450px solid rgba(56, 189, 248, 0.12)',
            filter: 'blur(4px)',
            opacity: 0.6 + beamPulse * 0.4,
            pointerEvents: 'none',
          }}
        />

        {/* Signal transmission waves */}
        <div
          style={{
            position: 'absolute',
            top: 20,
            width: signalRing1 * 1.5,
            height: signalRing1 * 1.5,
            borderRadius: '50%',
            border: '2px solid rgba(56, 189, 248, 0.5)',
            opacity: 1 - signalRing1 / 200,
            pointerEvents: 'none',
          }}
        />
        <div
          style={{
            position: 'absolute',
            top: 20,
            width: signalRing2 * 1.5,
            height: signalRing2 * 1.5,
            borderRadius: '50%',
            border: '2px solid rgba(56, 189, 248, 0.5)',
            opacity: 1 - signalRing2 / 200,
            pointerEvents: 'none',
          }}
        />

        {/* Military Stealth Drone Silhouette */}
        <svg
          width="420"
          height="220"
          viewBox="0 0 420 220"
          style={{
            filter: 'drop-shadow(0 15px 30px rgba(0, 240, 255, 0.3))',
          }}
        >
          {/* Main Fuselage */}
          <path
            d="M210,15 L225,90 L390,125 L395,140 L230,135 L220,195 L245,210 L175,210 L200,195 L190,135 L25,140 L30,125 L195,90 Z"
            fill="#1e293b"
            stroke="#38bdf8"
            strokeWidth="3"
          />
          {/* Cockpit / Sensor Dome */}
          <ellipse cx="210" cy="65" rx="12" ry="24" fill="#38bdf8" opacity="0.85" />
          {/* Optical Targeting Gimbal */}
          <circle cx="210" cy="115" r="8" fill="#fbbf24" />
        </svg>

        {/* Telemetry Box Under Drone */}
        <div
          style={{
            marginTop: 40,
            backgroundColor: 'rgba(15, 23, 42, 0.85)',
            border: '1px solid rgba(56, 189, 248, 0.4)',
            borderRadius: 12,
            padding: '12px 28px',
            display: 'flex',
            gap: 24,
            fontFamily: 'monospace',
            fontSize: 20,
            color: '#38bdf8',
            boxShadow: '0 10px 25px rgba(0, 0, 0, 0.7)',
          }}
        >
          <div>
            STATUS: <span style={{ color: '#10b981', fontWeight: 800 }}>UNMANNED</span>
          </div>
          <div>
            LINK: <span style={{ color: '#fbbf24', fontWeight: 800 }}>SATCOM 100%</span>
          </div>
          <div>
            PILOT: <span style={{ color: '#ffffff' }}>8,400 KM</span>
          </div>
        </div>
      </div>

      {/* Subtitle Narration */}
      <SubtitleBar
        badge="Reconnaissance UAV"
        badgeColor="#38bdf8"
        text="Drone dapat mengawasi wilayah berbahaya dan mengirim data tanpa pilot di medan perang."
        highlightWords={['drone', 'berbahaya', 'tanpa', 'pilot']}
      />
    </AbsoluteFill>
  );
};
