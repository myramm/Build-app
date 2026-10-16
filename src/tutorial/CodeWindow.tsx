import React from 'react';

interface CodeWindowProps {
  title: string;
  icon?: string;
  children: React.ReactNode;
}

export const CodeWindow: React.FC<CodeWindowProps> = ({
  title,
  icon = '💻',
  children,
}) => {
  return (
    <div
      style={{
        width: '92%',
        maxWidth: 980,
        backgroundColor: '#0d1117',
        border: '1.5px solid rgba(56, 189, 248, 0.3)',
        borderRadius: 20,
        overflow: 'hidden',
        boxShadow:
          '0 25px 50px -12px rgba(0, 0, 0, 0.85), 0 0 30px rgba(56, 189, 248, 0.15)',
        fontFamily: "'Fira Code', Consolas, 'Courier New', monospace",
      }}
    >
      {/* Window Title Bar */}
      <div
        style={{
          backgroundColor: '#161b22',
          padding: '16px 24px',
          display: 'flex',
          alignItems: 'center',
          justifyContent: 'space-between',
          borderBottom: '1px solid rgba(255, 255, 255, 0.1)',
        }}
      >
        {/* macOS Style Traffic Light Window Controls */}
        <div style={{ display: 'flex', gap: 10 }}>
          <div
            style={{
              width: 16,
              height: 16,
              borderRadius: '50%',
              backgroundColor: '#ff5f56',
            }}
          />
          <div
            style={{
              width: 16,
              height: 16,
              borderRadius: '50%',
              backgroundColor: '#ffbd2e',
            }}
          />
          <div
            style={{
              width: 16,
              height: 16,
              borderRadius: '50%',
              backgroundColor: '#27c93f',
            }}
          />
        </div>

        {/* Window Title */}
        <div
          style={{
            color: 'rgba(255, 255, 255, 0.8)',
            fontSize: 20,
            fontWeight: 600,
            display: 'flex',
            alignItems: 'center',
            gap: 10,
          }}
        >
          <span>{icon}</span>
          <span>{title}</span>
        </div>

        {/* Right side spacer */}
        <div style={{ width: 60 }} />
      </div>

      {/* Terminal / Code Body */}
      <div style={{ padding: '28px 32px' }}>{children}</div>
    </div>
  );
};
