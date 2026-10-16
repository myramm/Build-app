import React from 'react';

interface FlagProps {
  countryCode: string;
  width?: number;
  height?: number;
  className?: string;
}

export const Flag: React.FC<FlagProps> = ({
  countryCode,
  width = 40,
  height = 28,
}) => {
  const code = countryCode.toUpperCase();

  const renderSvgContent = () => {
    switch (code) {
      case 'US':
        return (
          <svg viewBox="0 0 7410 3900" width="100%" height="100%">
            <rect width="7410" height="3900" fill="#B22234" />
            <path
              d="M0,450H7410M0,1050H7410M0,1650H7410M0,2250H7410M0,2850H7410M0,3450H7410"
              stroke="#FFF"
              strokeWidth="300"
            />
            <rect width="2964" height="2100" fill="#3C3B6E" />
            <g fill="#FFF">
              {/* 50 crisp vector stars */}
              {Array.from({ length: 9 }).map((_, r) => {
                const cols = r % 2 === 0 ? 6 : 5;
                const y = 175 + r * 210;
                return Array.from({ length: cols }).map((__, c) => {
                  const x = (r % 2 === 0 ? 247 : 494) + c * 494;
                  return (
                    <polygon
                      key={`star-${r}-${c}`}
                      points={`${x},${y - 65} ${x + 20},${y - 20} ${x + 65},${y - 15} ${x + 32},${y + 18} ${x + 40},${y + 65} ${x},${y + 35} ${x - 40},${y + 65} ${x - 32},${y + 18} ${x - 65},${y - 15} ${x - 20},${y - 20}`}
                    />
                  );
                });
              })}
            </g>
          </svg>
        );

      case 'CN':
        return (
          <svg viewBox="0 0 900 600" width="100%" height="100%">
            <rect width="900" height="600" fill="#DE2910" />
            {/* Big star */}
            <polygon
              fill="#FFDE00"
              points="150,55 178,140 268,140 195,193 223,278 150,225 77,278 105,193 32,140 122,140"
            />
            {/* 4 small arc stars */}
            <polygon
              fill="#FFDE00"
              transform="translate(300, 60) rotate(-55) scale(0.33)"
              points="150,55 178,140 268,140 195,193 223,278 150,225 77,278 105,193 32,140 122,140"
            />
            <polygon
              fill="#FFDE00"
              transform="translate(360, 120) rotate(-30) scale(0.33)"
              points="150,55 178,140 268,140 195,193 223,278 150,225 77,278 105,193 32,140 122,140"
            />
            <polygon
              fill="#FFDE00"
              transform="translate(360, 210) rotate(0) scale(0.33)"
              points="150,55 178,140 268,140 195,193 223,278 150,225 77,278 105,193 32,140 122,140"
            />
            <polygon
              fill="#FFDE00"
              transform="translate(300, 270) rotate(25) scale(0.33)"
              points="150,55 178,140 268,140 195,193 223,278 150,225 77,278 105,193 32,140 122,140"
            />
          </svg>
        );

      case 'JP':
        return (
          <svg viewBox="0 0 900 600" width="100%" height="100%">
            <rect width="900" height="600" fill="#FFFFFF" />
            <circle cx="450" cy="300" r="180" fill="#BC002D" />
          </svg>
        );

      case 'DE':
        return (
          <svg viewBox="0 0 5 3" width="100%" height="100%">
            <rect width="5" height="1" y="0" fill="#000000" />
            <rect width="5" height="1" y="1" fill="#DD0000" />
            <rect width="5" height="1" y="2" fill="#FFCE00" />
          </svg>
        );

      case 'IN':
        return (
          <svg viewBox="0 0 900 600" width="100%" height="100%">
            <rect width="900" height="200" y="0" fill="#FF9933" />
            <rect width="900" height="200" y="200" fill="#FFFFFF" />
            <rect width="900" height="200" y="400" fill="#138808" />
            <circle cx="450" cy="300" r="80" fill="none" stroke="#000080" strokeWidth="8" />
            <circle cx="450" cy="300" r="16" fill="#000080" />
            {Array.from({ length: 24 }).map((_, i) => (
              <line
                key={`spoke-${i}`}
                x1="450"
                y1="300"
                x2={450 + 78 * Math.cos((i * 15 * Math.PI) / 180)}
                y2={300 + 78 * Math.sin((i * 15 * Math.PI) / 180)}
                stroke="#000080"
                strokeWidth="4"
              />
            ))}
          </svg>
        );

      case 'GB':
        return (
          <svg viewBox="0 0 60 30" width="100%" height="100%">
            <clipPath id="s">
              <path d="M0,0 v30 h60 v-30 z" />
            </clipPath>
            <clipPath id="t">
              <path d="M30,15 h30 v15 z v15 h-30 z h-30 v-15 z v-15 h30 z" />
            </clipPath>
            <g clipPath="url(#s)">
              <path d="M0,0 v30 h60 v-30 z" fill="#012169" />
              <path d="M0,0 L60,30 M60,0 L0,30" stroke="#fff" strokeWidth="6" />
              <path d="M0,0 L60,30 M60,0 L0,30" clipPath="url(#t)" stroke="#C8102E" strokeWidth="4" />
              <path d="M30,0 v30 M0,15 h60" stroke="#fff" strokeWidth="10" />
              <path d="M30,0 v30 M0,15 h60" stroke="#C8102E" strokeWidth="6" />
            </g>
          </svg>
        );

      case 'FR':
        return (
          <svg viewBox="0 0 3 2" width="100%" height="100%">
            <rect width="1" height="2" x="0" fill="#002654" />
            <rect width="1" height="2" x="1" fill="#FFFFFF" />
            <rect width="1" height="2" x="2" fill="#ED2939" />
          </svg>
        );

      case 'IT':
        return (
          <svg viewBox="0 0 3 2" width="100%" height="100%">
            <rect width="1" height="2" x="0" fill="#009246" />
            <rect width="1" height="2" x="1" fill="#FFFFFF" />
            <rect width="1" height="2" x="2" fill="#CE2B37" />
          </svg>
        );

      case 'RU':
        return (
          <svg viewBox="0 0 3 2" width="100%" height="100%">
            <rect width="3" height="0.666" y="0" fill="#FFFFFF" />
            <rect width="3" height="0.666" y="0.666" fill="#0039A6" />
            <rect width="3" height="0.668" y="1.332" fill="#D52B1E" />
          </svg>
        );

      case 'CA':
        return (
          <svg viewBox="0 0 1000 500" width="100%" height="100%">
            <rect width="250" height="500" x="0" fill="#FF0000" />
            <rect width="500" height="500" x="250" fill="#FFFFFF" />
            <rect width="250" height="500" x="750" fill="#FF0000" />
            {/* Crisp Maple Leaf */}
            <path
              fill="#FF0000"
              d="M500,75 L525,175 L590,165 L570,220 L640,240 L620,285 L655,305 L580,345 L590,375 L520,355 L515,425 L485,425 L480,355 L410,375 L420,345 L345,305 L380,285 L360,240 L430,220 L410,165 L475,175 Z"
            />
          </svg>
        );

      case 'BR':
        return (
          <svg viewBox="0 0 1000 700" width="100%" height="100%">
            <rect width="1000" height="700" fill="#009739" />
            <polygon points="500,70 930,350 500,630 70,350" fill="#FEDD00" />
            <circle cx="500" cy="350" r="175" fill="#012169" />
            <path
              d="M 330,375 A 185,185 0 0,0 670,345"
              fill="none"
              stroke="#FFFFFF"
              strokeWidth="28"
            />
          </svg>
        );

      case 'KR':
        return (
          <svg viewBox="0 0 900 600" width="100%" height="100%">
            <rect width="900" height="600" fill="#FFFFFF" />
            {/* Taegeuk */}
            <path
              d="M450,180 A120,120 0 0,0 450,420 A60,60 0 0,0 450,300 A60,60 0 0,1 450,180"
              fill="#CD2E3A"
            />
            <path
              d="M450,420 A120,120 0 0,0 450,180 A60,60 0 0,0 450,300 A60,60 0 0,1 450,420"
              fill="#0047A0"
            />
          </svg>
        );

      case 'ID':
        return (
          <svg viewBox="0 0 3 2" width="100%" height="100%">
            <rect width="3" height="1" y="0" fill="#E70011" />
            <rect width="3" height="1" y="1" fill="#FFFFFF" />
          </svg>
        );

      default:
        return (
          <div
            style={{
              width: '100%',
              height: '100%',
              backgroundColor: '#334155',
              display: 'flex',
              alignItems: 'center',
              justifyContent: 'center',
              color: '#FFF',
              fontSize: 10,
              fontWeight: 800,
            }}
          >
            {code}
          </div>
        );
    }
  };

  return (
    <div
      style={{
        width,
        height,
        borderRadius: 4,
        overflow: 'hidden',
        boxShadow: '0 1px 4px rgba(0,0,0,0.4)',
        border: '1px solid rgba(255, 255, 255, 0.22)',
        display: 'flex',
        alignItems: 'center',
        justifyContent: 'center',
        flexShrink: 0,
      }}
    >
      {renderSvgContent()}
    </div>
  );
};
