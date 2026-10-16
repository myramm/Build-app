import rawDataset from './dataset.json';
import {
  CountryInfo,
  CountryRanked,
  DataStatusCode,
  Milestone,
  TimelineState,
} from './types';

export const DATASET = rawDataset;
export const COUNTRIES: Record<string, CountryInfo> = DATASET.countries;

// Helper to get status label and badge color
export function getStatusMetadata(statusCode: DataStatusCode): {
  label: string;
  color: string;
  isProjection: boolean;
} {
  switch (statusCode) {
    case 'PROJECTION_IMF_WEO':
      return {
        label: 'PROYEKSI IMF WEO (2025–2026)',
        color: '#F59E0B', // Amber alert for projection
        isProjection: true,
      };
    case 'PRELIMINARY_ESTIMATE':
      return {
        label: 'ESTIMASI RESMI (2024)',
        color: '#38BDF8', // Cyan for preliminary
        isProjection: false,
      };
    case 'ACTUAL_OFFICIAL':
      return {
        label: 'DATA AKTUAL WORLD BANK (1960–2023)',
        color: '#10B981', // Emerald green for official actual data
        isProjection: false,
      };
    case 'ACTUAL_HISTORICAL_ESTIMATE':
    default:
      return {
        label: 'ESTIMASI HISTORIS PBB & MADDISON (1950–1959)',
        color: '#94A3B8', // Slate for early historical
        isProjection: false,
      };
  }
}

// Compute timeline state from frame
export function getTimelineState(
  frame: number,
  totalFrames: number = 3300
): TimelineState {
  // Frame 0-60: Hold at 1950.0 (1.0s)
  // Frame 60-3100: Progress 1950.0 to 2026.0 (50.6s)
  // Frame 3100-3300: Hold at 2026.0 (3.3s)
  let yearDecimal = 1950.0;
  if (frame <= 60) {
    yearDecimal = 1950.0;
  } else if (frame >= 3100) {
    yearDecimal = 2026.0;
  } else {
    const progress = (frame - 60) / (3100 - 60);
    yearDecimal = 1950.0 + progress * (2026.0 - 1950.0);
  }

  const currentYear = Math.min(2026, Math.floor(yearDecimal));
  const rawStatus =
    (DATASET.dataStatus as Record<string, string>)[String(currentYear)] ||
    'ACTUAL_OFFICIAL';
  const dataStatus = rawStatus as DataStatusCode;
  const statusMeta = getStatusMetadata(dataStatus);

  const progressPercent = Math.min(
    100,
    Math.max(0, ((yearDecimal - 1950) / (2026 - 1950)) * 100)
  );

  return {
    currentYear,
    yearDecimal,
    dataStatus,
    statusLabel: statusMeta.label,
    statusBadgeColor: statusMeta.color,
    isProjection: statusMeta.isProjection,
    progressPercent,
  };
}

// Smooth continuous interpolation helper
function smoothstep(edge0: number, edge1: number, x: number): number {
  const t = Math.max(0, Math.min(1, (x - edge0) / (edge1 - edge0)));
  return t * t * (3 - 2 * t);
}

// Interpolate continuous GDP for all countries at a decimal year
export function getInterpolatedGdp(yearDecimal: number): Record<string, number> {
  const clamped = Math.max(1950, Math.min(2026, yearDecimal));
  const lowerYear = Math.floor(clamped);
  const upperYear = Math.min(2026, lowerYear + 1);
  const fraction = clamped - lowerYear;

  const lowerData = (DATASET.series as Record<string, Record<string, number>>)[
    String(lowerYear)
  ];
  const upperData = (DATASET.series as Record<string, Record<string, number>>)[
    String(upperYear)
  ];

  if (!lowerData) return {};
  if (lowerYear === upperYear || !upperData) return { ...lowerData };

  const eased = smoothstep(0, 1, fraction);
  const result: Record<string, number> = {};

  for (const cid of Object.keys(COUNTRIES)) {
    const val0 = lowerData[cid] ?? 0;
    const val1 = upperData[cid] ?? val0;
    result[cid] = Math.round((val0 + (val1 - val0) * eased) * 10) / 10;
  }

  return result;
}

// Get ranked Top 10 countries with rank change delta detection
export function getRankedCountries(
  yearDecimal: number,
  prevYearDecimal?: number
): CountryRanked[] {
  const currentGdp = getInterpolatedGdp(yearDecimal);
  const prevGdp = prevYearDecimal ? getInterpolatedGdp(prevYearDecimal) : currentGdp;

  // Previous ranks
  const prevSorted = Object.keys(COUNTRIES)
    .map((id) => ({ id, gdp: prevGdp[id] || 0 }))
    .sort((a, b) => b.gdp - a.gdp);

  const prevRankMap = new Map<string, number>();
  prevSorted.forEach((item, index) => {
    prevRankMap.set(item.id, index + 1);
  });

  // Current sorted
  const currentSorted = Object.keys(COUNTRIES)
    .map((id) => ({
      ...COUNTRIES[id],
      gdp: currentGdp[id] || 0,
    }))
    .sort((a, b) => b.gdp - a.gdp);

  return currentSorted.slice(0, 10).map((c, index) => {
    const rank = index + 1;
    const prevRank = prevRankMap.get(c.id) || rank;
    const rankDelta = prevRank - rank; // >0 climbed up, <0 dropped down
    return {
      ...c,
      rank,
      prevRank,
      rankDelta,
    };
  });
}

// Verified Historical Milestones with source citations
export const MILESTONES: Milestone[] = [
  {
    id: 'postwar',
    year: 1950,
    title: 'Rekonstruksi Pasca-Perang Dunia II',
    description: 'AS memimpin separuh manufaktur global, disusul kebangkitan blok Uni Soviet dan Eropa Barat.',
    verifiedSource: 'United Nations National Accounts Database',
    startFrame: 0,
    endFrame: 180,
  },
  {
    id: 'japan_miracle',
    year: 1968,
    title: 'Keajaiban Ekonomi Jepang Melampaui Jerman',
    description: 'Jepang resmi melampaui Jerman Barat menjadi kekuatan ekonomi terbesar ke-2 di dunia.',
    verifiedSource: 'World Bank (NY.GDP.MKTP.CD)',
    highlightCountryId: 'JP',
    startFrame: 720,
    endFrame: 920,
  },
  {
    id: 'us_one_trillion',
    year: 1970,
    title: 'PDB Amerika Serikat Tembus $1 Triliun',
    description: 'Pertama kali dalam sejarah ekonomi modern, sebuah negara menembus valuasi $1 Triliun.',
    verifiedSource: 'World Bank Official Data',
    highlightCountryId: 'US',
    startFrame: 940,
    endFrame: 1100,
  },
  {
    id: 'oil_shock',
    year: 1973,
    title: 'Krisis Minyak Global Pertama (OPEC)',
    description: 'Embargo minyak memicu inflasi tajam dan merestrukturisasi rantai pasok energi dunia.',
    verifiedSource: 'IMF Historical Economic Statistics',
    startFrame: 1120,
    endFrame: 1300,
  },
  {
    id: 'plaza_accord',
    year: 1985,
    title: 'Plaza Accord & Ledakan Aset Jepang',
    description: 'Apresiasi Yen mendongkrak valuasi ekonomi Jepang hingga tembus lebih dari $3 Triliun.',
    verifiedSource: 'World Bank & Bank of Japan Archives',
    highlightCountryId: 'JP',
    startFrame: 1420,
    endFrame: 1620,
  },
  {
    id: 'ussr_dissolution',
    year: 1991,
    title: 'Pembubaran Uni Soviet & Pergeseran Eropa',
    description: 'Runtuhnya blok Soviet merombak tatanan ekonomi regional dan pasar internasional.',
    verifiedSource: 'World Bank & Goskomstat Records',
    highlightCountryId: 'RU',
    startFrame: 1700,
    endFrame: 1900,
  },
  {
    id: 'japan_peak',
    year: 1995,
    title: 'Puncak Valuasi Jepang ($5,64T)',
    description: 'Di puncak reli nilai tukar, ekonomi Jepang menyamai hampir 73% nilai ekonomi Amerika Serikat.',
    verifiedSource: 'World Bank Official Series',
    highlightCountryId: 'JP',
    startFrame: 1920,
    endFrame: 2080,
  },
  {
    id: 'krismon',
    year: 1998,
    title: 'Krisis Keuangan Asia (Krismon)',
    description: 'Gejolak devaluasi mata uang melanda Asia Tenggara dan Korea Selatan secara dramatis.',
    verifiedSource: 'Bank Indonesia & IMF Country Reports',
    highlightCountryId: 'ID',
    startFrame: 2100,
    endFrame: 2260,
  },
  {
    id: 'china_wto',
    year: 2001,
    title: 'China Resmi Bergabung ke WTO',
    description: 'Integrasi perdagangan global memulai era ekspansi manufaktur dan ekspor terbesar dunia.',
    verifiedSource: 'World Trade Organization & World Bank',
    highlightCountryId: 'CN',
    startFrame: 2280,
    endFrame: 2440,
  },
  {
    id: 'gfc_2008',
    year: 2008,
    title: 'Krisis Finansial Global (GFC)',
    description: 'Runtuhnya Wall Street memicu resesi global dan pergeseran likuiditas dunia.',
    verifiedSource: 'Federal Reserve & IMF Archives',
    startFrame: 2460,
    endFrame: 2620,
  },
  {
    id: 'china_number2',
    year: 2010,
    title: 'China Menggeser Jepang ke Posisi #2',
    description: 'China resmi menyalip Jepang dengan nilai ekonomi melampaui $6 Triliun.',
    verifiedSource: 'World Bank & IMF WEO Reports',
    highlightCountryId: 'CN',
    startFrame: 2640,
    endFrame: 2820,
  },
  {
    id: 'india_rise',
    year: 2024,
    title: 'Akselerasi India Membidik Top 3 Dunia',
    description: 'PDB India mendekati $4 Triliun dan membidik posisi 3 besar menggeser Jerman dan Jepang.',
    verifiedSource: 'IMF World Economic Outlook (Oct 2024)',
    highlightCountryId: 'IN',
    startFrame: 2950,
    endFrame: 3120,
  },
  {
    id: 'multipolar_2026',
    year: 2026,
    title: 'Era Ekonomi Multipolar (Proyeksi 2026)',
    description: 'AS diproyeksikan menembus $31T, China $20T, dan India memimpin pertumbuhan ekonomi utama.',
    verifiedSource: 'IMF WEO Projections (2025–2026)',
    startFrame: 3130,
    endFrame: 3300,
  },
];

export function getActiveMilestone(frame: number): Milestone | null {
  for (const m of MILESTONES) {
    if (frame >= m.startFrame && frame <= m.endFrame) {
      return m;
    }
  }
  return null;
}
