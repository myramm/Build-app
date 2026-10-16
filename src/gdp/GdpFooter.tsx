import React from 'react';

interface GdpFooterProps {
  isFinalFrame: boolean;
}

export const GdpFooter: React.FC<GdpFooterProps> = ({ isFinalFrame }) => {
  return (
    <div
      style={{
        position: 'absolute',
        bottom: 24,
        left: 48,
        right: 48,
        display: 'flex',
        justifyContent: 'space-between',
        alignItems: 'center',
        paddingTop: 12,
        borderTop: '1px solid rgba(255, 255, 255, 0.06)',
        fontFamily: "'DM Sans', sans-serif",
        fontSize: 14,
        color: '#64748B',
        zIndex: 40,
      }}
    >
      <div>
        <span>Sumber: </span>
        <span style={{ color: '#94A3B8', fontWeight: 600 }}>
          World Bank Open Data (NY.GDP.MKTP.CD) · IMF WEO Database · UN Accounts
        </span>
      </div>

      <div>
        <span>Pembaruan Dataset: </span>
        <span style={{ color: '#94A3B8', fontWeight: 600 }}>
          Oktober 2026 (Otomasi Bulanan)
        </span>
      </div>
    </div>
  );
};
