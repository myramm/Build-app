import React from 'react';
import {
  AbsoluteFill,
  interpolate,
  useCurrentFrame,
} from 'remotion';
import { SubtitleBar } from '../components/SubtitleBar';

export const Scene4Network: React.FC = () => {
  const frame = useCurrentFrame();

  // Packet animation along edges (0 to 1)
  const packetPos1 = (frame * 0.035) % 1;
  const packetPos2 = (frame * 0.045 + 0.5) % 1;
  const packetPos3 = (frame * 0.04) % 1;

  return (
    <AbsoluteFill
      style={{
        backgroundColor: '#070c18',
        overflow: 'hidden',
      }}
    >
      {/* Background Cyber Grid */}
      <AbsoluteFill
        style={{
          background:
            'radial-gradient(ellipse at 50% 40%, #0369a1 0%, #082f49 40%, #030712 100%)',
          opacity: 0.85,
        }}
      />

      {/* Center Tactical Command Hub */}
      <div
        style={{
          position: 'absolute',
          top: '36%',
          left: '50%',
          transform: 'translate(-50%, -50%)',
          width: 580,
          height: 520,
        }}
      >
        {/* Network Connection Lines (SVG) */}
        <svg
          width="580"
          height="520"
          style={{ position: 'absolute', inset: 0 }}
        >
          {/* Edges from Center (290, 260) to 4 Nodes */}
          {/* To Top Drone (290, 70) */}
          <line
            x1="290"
            y1="260"
            x2="290"
            y2="70"
            stroke="#38bdf8"
            strokeWidth="3"
            strokeDasharray="6 6"
            opacity="0.7"
          />
          {/* Packet 1 */}
          <circle
            cx="290"
            cy={260 - (260 - 70) * packetPos1}
            r="7"
            fill="#fbbf24"
            filter="drop-shadow(0 0 8px #fbbf24)"
          />

          {/* To Left Fighter Jet (90, 200) */}
          <line
            x1="290"
            y1="260"
            x2="90"
            y2="200"
            stroke="#38bdf8"
            strokeWidth="3"
            strokeDasharray="6 6"
            opacity="0.7"
          />
          {/* Packet 2 */}
          <circle
            cx={290 - (290 - 90) * packetPos2}
            cy={260 - (260 - 200) * packetPos2}
            r="7"
            fill="#38bdf8"
            filter="drop-shadow(0 0 8px #38bdf8)"
          />

          {/* To Right Missile Battery (490, 200) */}
          <line
            x1="290"
            y1="260"
            x2="490"
            y2="200"
            stroke="#38bdf8"
            strokeWidth="3"
            strokeDasharray="6 6"
            opacity="0.7"
          />
          {/* Packet 3 */}
          <circle
            cx={290 + (490 - 290) * packetPos3}
            cy={260 - (260 - 200) * packetPos3}
            r="7"
            fill="#10b981"
            filter="drop-shadow(0 0 8px #10b981)"
          />

          {/* To Bottom Naval Ship (290, 450) */}
          <line
            x1="290"
            y1="260"
            x2="290"
            y2="450"
            stroke="#38bdf8"
            strokeWidth="3"
            strokeDasharray="6 6"
            opacity="0.7"
          />
        </svg>

        {/* Central Hub: JOINT COMMAND CENTER */}
        <div
          style={{
            position: 'absolute',
            top: 260,
            left: 290,
            transform: 'translate(-50%, -50%)',
            width: 140,
            height: 140,
            borderRadius: '50%',
            backgroundColor: '#0f172a',
            border: '4px solid #fbbf24',
            boxShadow: '0 0 35px rgba(251, 191, 36, 0.5)',
            display: 'flex',
            flexDirection: 'column',
            alignItems: 'center',
            justifyContent: 'center',
            zIndex: 10,
          }}
        >
          <span style={{ fontSize: 36 }}>🏛️</span>
          <div
            style={{
              fontFamily: 'monospace',
              fontSize: 13,
              fontWeight: 800,
              color: '#fbbf24',
              marginTop: 4,
            }}
          >
            HQ INTEL
          </div>
        </div>

        {/* Node 1: DRONE RECON (Top) */}
        <div
          style={{
            position: 'absolute',
            top: 70,
            left: 290,
            transform: 'translate(-50%, -50%)',
            backgroundColor: '#0c1527',
            border: '2px solid #38bdf8',
            borderRadius: 16,
            padding: '10px 18px',
            display: 'flex',
            alignItems: 'center',
            gap: 10,
            fontFamily: 'monospace',
            color: '#38bdf8',
            boxShadow: '0 0 20px rgba(56, 189, 248, 0.4)',
          }}
        >
          <span style={{ fontSize: 24 }}>🛩️</span>
          <span style={{ fontWeight: 800 }}>UAV LIVE FEED</span>
        </div>

        {/* Node 2: JET FIGHTER (Left) */}
        <div
          style={{
            position: 'absolute',
            top: 200,
            left: 90,
            transform: 'translate(-50%, -50%)',
            backgroundColor: '#0c1527',
            border: '2px solid #38bdf8',
            borderRadius: 16,
            padding: '10px 18px',
            display: 'flex',
            alignItems: 'center',
            gap: 10,
            fontFamily: 'monospace',
            color: '#38bdf8',
          }}
        >
          <span style={{ fontSize: 24 }}>⚡</span>
          <span style={{ fontWeight: 800 }}>F-35 JET</span>
        </div>

        {/* Node 3: AIR DEFENSE BATTERY (Right) */}
        <div
          style={{
            position: 'absolute',
            top: 200,
            left: 490,
            transform: 'translate(-50%, -50%)',
            backgroundColor: '#0c1527',
            border: '2px solid #10b981',
            borderRadius: 16,
            padding: '10px 18px',
            display: 'flex',
            alignItems: 'center',
            gap: 10,
            fontFamily: 'monospace',
            color: '#10b981',
          }}
        >
          <span style={{ fontSize: 24 }}>🚀</span>
          <span style={{ fontWeight: 800 }}>MISSILE BATTERY</span>
        </div>

        {/* Node 4: NAVAL FLEET (Bottom) */}
        <div
          style={{
            position: 'absolute',
            top: 450,
            left: 290,
            transform: 'translate(-50%, -50%)',
            backgroundColor: '#0c1527',
            border: '2px solid #38bdf8',
            borderRadius: 16,
            padding: '10px 18px',
            display: 'flex',
            alignItems: 'center',
            gap: 10,
            fontFamily: 'monospace',
            color: '#38bdf8',
          }}
        >
          <span style={{ fontSize: 24 }}>⚓</span>
          <span style={{ fontWeight: 800 }}>AEGIS DESTROYER</span>
        </div>
      </div>

      {/* Subtitle Narration */}
      <SubtitleBar
        badge="Jaringan Informasi Taktis"
        badgeColor="#fbbf24"
        text="Dalam perang modern, akurasi dan kecepatan informasi adalah penentu kemenangan utama."
        highlightWords={['akurasi', 'kecepatan', 'informasi', 'penentu', 'kemenangan', 'utama']}
      />
    </AbsoluteFill>
  );
};
