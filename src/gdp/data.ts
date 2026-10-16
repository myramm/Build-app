import { CountryInfo, CountryRanked, Milestone } from './types';

export const COUNTRIES: Record<string, CountryInfo> = {
  US: { id: 'US', name: 'Amerika Serikat', flag: '🇺🇸', color: '#3B82F6' },
  CN: { id: 'CN', name: 'China', flag: '🇨🇳', color: '#EF4444' },
  JP: { id: 'JP', name: 'Jepang', flag: '🇯🇵', color: '#F59E0B' },
  DE: { id: 'DE', name: 'Jerman', flag: '🇩🇪', color: '#F97316' },
  GB: { id: 'GB', name: 'Inggris', flag: '🇬🇧', color: '#6366F1' },
  IN: { id: 'IN', name: 'India', flag: '🇮🇳', color: '#10B981' },
  FR: { id: 'FR', name: 'Prancis', flag: '🇫🇷', color: '#06B6D4' },
  IT: { id: 'IT', name: 'Italia', flag: '🇮🇹', color: '#84CC16' },
  RU: { id: 'RU', name: 'Rusia / USSR', flag: '🇷🇺', color: '#DC2626' },
  BR: { id: 'BR', name: 'Brasil', flag: '🇧🇷', color: '#EAB308' },
  CA: { id: 'CA', name: 'Kanada', flag: '🇨🇦', color: '#EC4899' },
  KR: { id: 'KR', name: 'Korea Selatan', flag: '🇰🇷', color: '#8B5CF6' },
  ID: { id: 'ID', name: 'Indonesia', flag: '🇮🇩', color: '#F43F5E' },
};

// GDP in Billion USD across benchmark years (1950 - 2026)
export const GDP_BENCHMARKS: { year: number; data: Record<string, number> }[] = [
  {
    year: 1950,
    data: {
      US: 300,
      RU: 126,
      GB: 71,
      FR: 52,
      DE: 48,
      CN: 31,
      IN: 30,
      IT: 29,
      JP: 32,
      CA: 22,
      BR: 15,
      KR: 3,
      ID: 7,
    },
  },
  {
    year: 1960,
    data: {
      US: 543,
      RU: 280,
      DE: 104,
      GB: 73,
      FR: 63,
      JP: 44,
      CN: 60,
      IT: 40,
      IN: 37,
      CA: 40,
      BR: 24,
      KR: 4,
      ID: 9,
    },
  },
  {
    year: 1970,
    data: {
      US: 1073,
      RU: 433,
      JP: 212,
      DE: 215,
      FR: 148,
      GB: 130,
      IT: 113,
      CN: 92,
      CA: 88,
      IN: 62,
      BR: 42,
      KR: 9,
      ID: 10,
    },
  },
  {
    year: 1980,
    data: {
      US: 2857,
      JP: 1105,
      RU: 940,
      DE: 950,
      FR: 702,
      GB: 603,
      IT: 483,
      CA: 276,
      BR: 235,
      CN: 191,
      IN: 186,
      KR: 65,
      ID: 78,
    },
  },
  {
    year: 1990,
    data: {
      US: 5963,
      JP: 3193,
      DE: 1772,
      FR: 1279,
      IT: 1181,
      GB: 1093,
      RU: 775,
      CA: 594,
      CN: 360,
      BR: 461,
      KR: 283,
      IN: 320,
      ID: 114,
    },
  },
  {
    year: 2000,
    data: {
      US: 10252,
      JP: 4968,
      DE: 1955,
      GB: 1668,
      FR: 1372,
      CN: 1211,
      IT: 1147,
      CA: 744,
      BR: 655,
      KR: 576,
      IN: 468,
      RU: 260,
      ID: 165,
    },
  },
  {
    year: 2010,
    data: {
      US: 15049,
      CN: 6087,
      JP: 5759,
      DE: 3416,
      FR: 2647,
      GB: 2491,
      IT: 2136,
      BR: 2209,
      RU: 1633,
      IN: 1708,
      CA: 1617,
      KR: 1143,
      ID: 755,
    },
  },
  {
    year: 2020,
    data: {
      US: 21060,
      CN: 14688,
      JP: 5048,
      DE: 3889,
      GB: 2697,
      IN: 2671,
      FR: 2639,
      IT: 1896,
      CA: 1647,
      KR: 1644,
      RU: 1493,
      BR: 1476,
      ID: 1060,
    },
  },
  {
    year: 2026,
    data: {
      US: 29800,
      CN: 19800,
      DE: 4700,
      JP: 4400,
      IN: 4300,
      GB: 3600,
      FR: 3200,
      IT: 2400,
      CA: 2300,
      BR: 2300,
      RU: 2200,
      KR: 1900,
      ID: 1500,
    },
  },
];

export const MILESTONES: Milestone[] = [
  {
    year: 1950,
    title: 'Era Pasca Perang',
    description: 'AS & Uni Soviet memimpin dominasi industri ekonomi dunia.',
  },
  {
    year: 1968,
    title: 'Ledakan Ekonomi Jepang',
    description: 'Jepang bangkit pascaperang menjadi raksasa ekonomi baru.',
  },
  {
    year: 1991,
    title: 'Runtuhnya Uni Soviet',
    description: 'Perang Dingin usai, peta ekonomi Eropa & Asia bertransformasi.',
  },
  {
    year: 2010,
    title: 'China Geser Jepang ke #2',
    description: 'Pertumbuhan manufaktur masif China mengguncang dominasi barat.',
  },
  {
    year: 2023,
    title: 'India Tembus 5 Besar Dunia',
    description: 'Demografi & digitalisasi mendorong lonjakan ekonomi India.',
  },
  {
    year: 2026,
    title: 'Kekuatan Ekonomi Hari Ini',
    description: 'Persaingan AS & China makin sengit di era revolusi AI.',
  },
];

// Linear interpolation helper
function lerp(a: number, b: number, t: number): number {
  return a + (b - a) * t;
}

// Get interpolated GDP and rankings for any year (1950.0 to 2026.0)
export function getRankedCountries(currentYear: number): CountryRanked[] {
  const yearClamped = Math.max(1950, Math.min(2026, currentYear));

  // Find surrounding benchmarks
  let lower = GDP_BENCHMARKS[0];
  let upper = GDP_BENCHMARKS[GDP_BENCHMARKS.length - 1];

  for (let i = 0; i < GDP_BENCHMARKS.length - 1; i++) {
    if (yearClamped >= GDP_BENCHMARKS[i].year && yearClamped <= GDP_BENCHMARKS[i + 1].year) {
      lower = GDP_BENCHMARKS[i];
      upper = GDP_BENCHMARKS[i + 1];
      break;
    }
  }

  const span = upper.year - lower.year;
  const t = span === 0 ? 0 : (yearClamped - lower.year) / span;

  // Calculate current GDP for each country
  const list: { id: string; gdp: number }[] = [];
  for (const id of Object.keys(COUNTRIES)) {
    const gdpLower = lower.data[id] ?? 0;
    const gdpUpper = upper.data[id] ?? 0;
    const gdp = lerp(gdpLower, gdpUpper, t);
    list.push({ id, gdp });
  }

  // Sort descending by GDP
  list.sort((a, b) => b.gdp - a.gdp);

  // Return top 10 with ranks
  return list.slice(0, 10).map((item, index) => {
    const info = COUNTRIES[item.id];
    return {
      ...info,
      gdp: Math.round(item.gdp),
      rank: index + 1,
    };
  });
}

export function getCurrentMilestone(year: number): Milestone | null {
  const currentInt = Math.floor(year);
  for (let i = MILESTONES.length - 1; i >= 0; i--) {
    if (currentInt >= MILESTONES[i].year && currentInt < MILESTONES[i].year + 4) {
      return MILESTONES[i];
    }
  }
  return null;
}
