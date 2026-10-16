import { CountryInfo, CountryRanked, Milestone, MonthDate } from './types';

export const COUNTRIES: Record<string, CountryInfo> = {
  US: {
    id: 'US',
    name: 'Amerika Serikat',
    flag: '🇺🇸',
    color: '#3B82F6',
    gradient: 'linear-gradient(90deg, #1D4ED8 0%, #3B82F6 100%)',
  },
  CN: {
    id: 'CN',
    name: 'China',
    flag: '🇨🇳',
    color: '#EF4444',
    gradient: 'linear-gradient(90deg, #B91C1C 0%, #EF4444 100%)',
  },
  JP: {
    id: 'JP',
    name: 'Jepang',
    flag: '🇯🇵',
    color: '#F59E0B',
    gradient: 'linear-gradient(90deg, #B45309 0%, #F59E0B 100%)',
  },
  DE: {
    id: 'DE',
    name: 'Jerman',
    flag: '🇩🇪',
    color: '#F97316',
    gradient: 'linear-gradient(90deg, #C2410C 0%, #F97316 100%)',
  },
  GB: {
    id: 'GB',
    name: 'Inggris',
    flag: '🇬🇧',
    color: '#6366F1',
    gradient: 'linear-gradient(90deg, #4338CA 0%, #6366F1 100%)',
  },
  IN: {
    id: 'IN',
    name: 'India',
    flag: '🇮🇳',
    color: '#10B981',
    gradient: 'linear-gradient(90deg, #047857 0%, #10B981 100%)',
  },
  FR: {
    id: 'FR',
    name: 'Prancis',
    flag: '🇫🇷',
    color: '#06B6D4',
    gradient: 'linear-gradient(90deg, #0E7490 0%, #06B6D4 100%)',
  },
  IT: {
    id: 'IT',
    name: 'Italia',
    flag: '🇮🇹',
    color: '#84CC16',
    gradient: 'linear-gradient(90deg, #4D7C0F 0%, #84CC16 100%)',
  },
  RU: {
    id: 'RU',
    name: 'Rusia / Uni Soviet',
    flag: '🇷🇺',
    color: '#DC2626',
    gradient: 'linear-gradient(90deg, #991B1B 0%, #DC2626 100%)',
  },
  CA: {
    id: 'CA',
    name: 'Kanada',
    flag: '🇨🇦',
    color: '#EC4899',
    gradient: 'linear-gradient(90deg, #BE185D 0%, #EC4899 100%)',
  },
  BR: {
    id: 'BR',
    name: 'Brasil',
    flag: '🇧🇷',
    color: '#EAB308',
    gradient: 'linear-gradient(90deg, #A16207 0%, #EAB308 100%)',
  },
  KR: {
    id: 'KR',
    name: 'Korea Selatan',
    flag: '🇰🇷',
    color: '#8B5CF6',
    gradient: 'linear-gradient(90deg, #6D28D9 0%, #8B5CF6 100%)',
  },
  ID: {
    id: 'ID',
    name: 'Indonesia',
    flag: '🇮🇩',
    color: '#F43F5E',
    gradient: 'linear-gradient(90deg, #BE123C 0%, #F43F5E 100%)',
  },
};

export const MONTH_NAMES_ID = [
  'Januari',
  'Februari',
  'Maret',
  'April',
  'Mei',
  'Juni',
  'Juli',
  'Agustus',
  'September',
  'Oktober',
  'November',
  'Desember',
];

export const MONTH_SHORTS = [
  'JAN',
  'FEB',
  'MAR',
  'APR',
  'MEI',
  'JUN',
  'JUL',
  'AGU',
  'SEP',
  'OKT',
  'NOV',
  'DES',
];

// Historical Benchmark Anchor Points (1950 - 2026) in Billion USD
export const GDP_BENCHMARKS: { yearDecimal: number; data: Record<string, number> }[] = [
  {
    yearDecimal: 1950.0, // Jan 1950
    data: { US: 300, RU: 126, GB: 71, FR: 52, DE: 48, CN: 31, IN: 30, IT: 29, JP: 32, CA: 22, BR: 15, KR: 3, ID: 7 },
  },
  {
    yearDecimal: 1955.0, // Jan 1955
    data: { US: 426, RU: 200, GB: 72, DE: 78, FR: 58, JP: 38, CN: 42, IT: 35, IN: 33, CA: 30, BR: 19, KR: 4, ID: 8 },
  },
  {
    yearDecimal: 1960.0, // Jan 1960
    data: { US: 543, RU: 280, DE: 104, GB: 73, FR: 63, JP: 44, CN: 60, IT: 40, IN: 37, CA: 40, BR: 24, KR: 4, ID: 9 },
  },
  {
    yearDecimal: 1965.0, // Jan 1965
    data: { US: 744, RU: 360, DE: 148, GB: 101, FR: 102, JP: 91, IT: 68, CN: 70, IN: 60, CA: 54, BR: 30, KR: 6, ID: 10 },
  },
  {
    yearDecimal: 1968.8, // Oct 1968: Japan surpasses West Germany
    data: { US: 940, RU: 410, JP: 147, DE: 145, FR: 130, GB: 105, IT: 88, CN: 72, CA: 72, IN: 53, BR: 36, KR: 8, ID: 11 },
  },
  {
    yearDecimal: 1970.0, // Jan 1970: US reaches $1 Trillion
    data: { US: 1073, RU: 433, JP: 209, DE: 209, FR: 146, GB: 125, IT: 109, CN: 92, CA: 88, IN: 62, BR: 42, KR: 9, ID: 12 },
  },
  {
    yearDecimal: 1973.9, // Nov 1973: First Oil Shock
    data: { US: 1428, RU: 520, JP: 410, DE: 350, FR: 260, GB: 180, IT: 170, CA: 130, CN: 138, BR: 80, IN: 85, KR: 14, ID: 18 },
  },
  {
    yearDecimal: 1978.0, // Jan 1978: Deng Xiaoping Reforms
    data: { US: 2352, RU: 840, JP: 1010, DE: 690, FR: 520, GB: 330, IT: 310, CA: 220, CN: 150, BR: 160, IN: 135, KR: 52, ID: 48 },
  },
  {
    yearDecimal: 1980.0, // Jan 1980
    data: { US: 2857, RU: 1210, JP: 1105, DE: 853, FR: 702, GB: 565, IT: 470, CA: 274, BR: 235, CN: 191, IN: 186, KR: 65, ID: 72 },
  },
  {
    yearDecimal: 1985.7, // Sep 1985: Plaza Accord
    data: { US: 4339, JP: 1399, RU: 1350, DE: 660, FR: 558, GB: 489, IT: 459, CA: 365, BR: 223, CN: 309, IN: 233, KR: 101, ID: 87 },
  },
  {
    yearDecimal: 1989.9, // Dec 1989: Japan Asset Bubble Peak
    data: { US: 5642, JP: 3055, RU: 1580, DE: 1260, FR: 1025, IT: 922, GB: 875, CA: 565, CN: 348, BR: 425, IN: 296, KR: 244, ID: 102 },
  },
  {
    yearDecimal: 1991.9, // Dec 1991: Collapse of Soviet Union
    data: { US: 6158, JP: 3582, DE: 1870, FR: 1272, IT: 1243, GB: 1142, RU: 518, CA: 610, CN: 383, BR: 407, IN: 270, KR: 330, ID: 117 },
  },
  {
    yearDecimal: 1995.3, // Apr 1995: Yen Peak (USD/JPY 79)
    data: { US: 7639, JP: 5546, DE: 2590, FR: 1600, GB: 1340, IT: 1190, CN: 734, BR: 769, CA: 604, KR: 567, RU: 396, IN: 360, ID: 202 },
  },
  {
    yearDecimal: 1998.5, // Jun 1998: Asian Financial Crisis (Krismon)
    data: { US: 9063, JP: 4098, DE: 2240, GB: 1650, FR: 1500, IT: 1270, CN: 1029, BR: 864, CA: 632, KR: 383, RU: 271, IN: 421, ID: 95 },
  },
  {
    yearDecimal: 2001.9, // Dec 2001: China joins WTO
    data: { US: 10582, JP: 4375, DE: 1950, GB: 1640, FR: 1377, CN: 1339, IT: 1167, CA: 736, BR: 559, IN: 485, KR: 533, RU: 306, ID: 160 },
  },
  {
    yearDecimal: 2005.0, // Jan 2005
    data: { US: 13039, JP: 4755, DE: 2860, GB: 2540, FR: 2200, CN: 2286, IT: 1850, CA: 1170, BR: 882, IN: 809, RU: 764, KR: 898, ID: 285 },
  },
  {
    yearDecimal: 2008.7, // Sep 2008: Global Financial Crisis (Lehman)
    data: { US: 14718, JP: 5038, CN: 4598, DE: 3752, FR: 2923, GB: 2919, IT: 2392, RU: 1660, BR: 1695, IN: 1187, CA: 1549, KR: 1047, ID: 510 },
  },
  {
    yearDecimal: 2010.6, // Aug 2010: China overtakes Japan as #2
    data: { US: 14964, CN: 6087, JP: 5700, DE: 3417, FR: 2647, GB: 2485, BR: 2209, IT: 2125, IN: 1675, RU: 1525, CA: 1614, KR: 1094, ID: 755 },
  },
  {
    yearDecimal: 2015.0, // Jan 2015
    data: { US: 18238, CN: 11065, JP: 4395, DE: 3361, GB: 2896, FR: 2438, IN: 2104, IT: 1832, BR: 1802, CA: 1559, KR: 1466, RU: 1363, ID: 861 },
  },
  {
    yearDecimal: 2018.0, // Jan 2018
    data: { US: 20612, CN: 13895, JP: 5038, DE: 3962, GB: 2855, FR: 2788, IN: 2701, IT: 2092, BR: 1917, CA: 1725, KR: 1721, RU: 1658, ID: 1042 },
  },
  {
    yearDecimal: 2020.2, // Mar 2020: COVID-19 Shock
    data: { US: 21060, CN: 14688, JP: 5040, DE: 3846, GB: 2708, IN: 2668, FR: 2630, IT: 1886, CA: 1644, KR: 1644, RU: 1483, BR: 1445, ID: 1058 },
  },
  {
    yearDecimal: 2022.0, // Jan 2022: Global Recovery & Inflation
    data: { US: 25440, CN: 17963, JP: 4232, DE: 4072, IN: 3385, GB: 3070, FR: 2783, RU: 2240, CA: 2138, IT: 2010, BR: 1920, KR: 1673, ID: 1319 },
  },
  {
    yearDecimal: 2024.0, // Jan 2024: India reaches $4T
    data: { US: 27974, CN: 18566, DE: 4730, JP: 4290, IN: 4112, GB: 3592, FR: 3180, IT: 2280, BR: 2174, CA: 2140, RU: 2060, KR: 1760, ID: 1371 },
  },
  {
    yearDecimal: 2026.9, // Dec 2026: Projections
    data: { US: 29850, CN: 19800, DE: 4950, IN: 4680, JP: 4420, GB: 3850, FR: 3350, IT: 2410, BR: 2310, CA: 2250, RU: 2180, KR: 1850, ID: 1540 },
  },
];

// Calculate exact month date from current frame (Duration: 3300 frames)
export function getDateFromFrame(frame: number): MonthDate {
  // Start month at frame 60 (Jan 1950) to frame 3100 (Dec 2026)
  // Total months: (2026 - 1950 + 1) * 12 = 924 months
  const totalMonths = (2026 - 1950 + 1) * 12; // 924
  
  let monthIndex = 0;
  if (frame <= 60) {
    monthIndex = 0;
  } else if (frame >= 3100) {
    monthIndex = totalMonths - 1;
  } else {
    const progress = (frame - 60) / (3100 - 60);
    monthIndex = Math.min(totalMonths - 1, Math.floor(progress * totalMonths));
  }

  const year = 1950 + Math.floor(monthIndex / 12);
  const month = (monthIndex % 12) + 1;
  const monthName = MONTH_NAMES_ID[month - 1];
  const monthShort = MONTH_SHORTS[month - 1];
  const yearDecimal = year + (month - 1) / 12;

  return {
    year,
    month,
    monthName,
    monthShort,
    yearDecimal,
  };
}

// Cubic Hermite / Smoothstep interpolation helper
function smoothstep(edge0: number, edge1: number, x: number): number {
  const t = Math.max(0, Math.min(1, (x - edge0) / (edge1 - edge0)));
  return t * t * (3 - 2 * t);
}

// Interpolate continuous monthly GDP for each country
export function getInterpolatedGdp(yearDecimal: number): Record<string, number> {
  const benchmarks = GDP_BENCHMARKS;
  if (yearDecimal <= benchmarks[0].yearDecimal) {
    return { ...benchmarks[0].data };
  }
  if (yearDecimal >= benchmarks[benchmarks.length - 1].yearDecimal) {
    return { ...benchmarks[benchmarks.length - 1].data };
  }

  // Find bounding benchmarks
  let lowerIdx = 0;
  for (let i = 0; i < benchmarks.length - 1; i++) {
    if (yearDecimal >= benchmarks[i].yearDecimal && yearDecimal <= benchmarks[i + 1].yearDecimal) {
      lowerIdx = i;
      break;
    }
  }

  const b0 = benchmarks[lowerIdx];
  const b1 = benchmarks[lowerIdx + 1];
  const fraction = (yearDecimal - b0.yearDecimal) / (b1.yearDecimal - b0.yearDecimal);
  const easedFraction = smoothstep(0, 1, fraction);

  const result: Record<string, number> = {};
  for (const cid of Object.keys(COUNTRIES)) {
    const val0 = b0.data[cid] || 1;
    const val1 = b1.data[cid] || 1;
    result[cid] = Math.round((val0 + (val1 - val0) * easedFraction) * 10) / 10;
  }

  return result;
}

// Get sorted Top 10 countries with rank change detection
export function getRankedCountriesMonthly(
  currentYearDecimal: number,
  prevYearDecimal?: number
): CountryRanked[] {
  const currentGdp = getInterpolatedGdp(currentYearDecimal);
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
    const rankDelta = prevRank - rank; // positive means climbed up
    return {
      ...c,
      rank,
      prevRank,
      rankDelta,
    };
  });
}

// Curated Historical Milestones with active frame ranges
export const MILESTONES: Milestone[] = [
  {
    id: 'postwar',
    year: 1950,
    month: 1,
    title: 'Rekonstruksi Pasca-PD II',
    description: 'AS memimpin separuh manufaktur global, disusul blok Uni Soviet & Eropa.',
    startFrame: 0,
    endFrame: 180,
  },
  {
    id: 'japan_miracle',
    year: 1968,
    month: 10,
    title: 'Keajaiban Ekonomi Jepang',
    description: 'Jepang melampaui Jerman Barat menjadi kekuatan ekonomi terbesar ke-2 dunia.',
    highlightCountryId: 'JP',
    startFrame: 720,
    endFrame: 920,
  },
  {
    id: 'oil_shock',
    year: 1973,
    month: 11,
    title: 'Krisis Minyak Global Pertama',
    description: 'Embargo minyak memicu inflasi tajam dan merestrukturisasi rantai pasok energi.',
    startFrame: 960,
    endFrame: 1140,
  },
  {
    id: 'plaza_accord',
    year: 1985,
    month: 9,
    title: 'Plaza Accord & Bubble Jepang',
    description: 'Apresiasi Yen melonjakkan valuasi ekonomi Jepang hingga tembus $3 Triliun.',
    highlightCountryId: 'JP',
    startFrame: 1420,
    endFrame: 1620,
  },
  {
    id: 'ussr_dissolution',
    year: 1991,
    month: 12,
    title: 'Pembubaran Uni Soviet',
    description: 'Runtuhnya Uni Soviet mengakhiri Perang Dingin dan mengubah peta ekonomi Eropa.',
    highlightCountryId: 'RU',
    startFrame: 1700,
    endFrame: 1900,
  },
  {
    id: 'krismon',
    year: 1998,
    month: 6,
    title: 'Krisis Moneter Asia (Krismon)',
    description: 'Gejolak devaluasi mata uang melanda Asia Tenggara dan Korea Selatan.',
    highlightCountryId: 'ID',
    startFrame: 1960,
    endFrame: 2150,
  },
  {
    id: 'china_wto',
    year: 2001,
    month: 12,
    title: 'China Bergabung ke WTO',
    description: 'Integrasi perdagangan global memulai era ekspansi manufaktur tercepat di dunia.',
    highlightCountryId: 'CN',
    startFrame: 2180,
    endFrame: 2360,
  },
  {
    id: 'gfc_2008',
    year: 2008,
    month: 9,
    title: 'Krisis Keuangan Global (GFC)',
    description: 'Kejatuhan Wall Street memicu resesi global dan pergeseran likuiditas dunia.',
    startFrame: 2420,
    endFrame: 2590,
  },
  {
    id: 'china_number2',
    year: 2010,
    month: 8,
    title: 'China Geser Jepang ke Posisi #2',
    description: 'China resmi menyalip Jepang dengan nilai ekonomi melampaui $6 Triliun.',
    highlightCountryId: 'CN',
    startFrame: 2600,
    endFrame: 2780,
  },
  {
    id: 'india_rise',
    year: 2024,
    month: 1,
    title: 'Akselerasi Ekonomi India ($4T+)',
    description: 'India menembus $4 Triliun dan membidik posisi 3 besar menggeser Jerman & Jepang.',
    highlightCountryId: 'IN',
    startFrame: 2950,
    endFrame: 3120,
  },
  {
    id: 'multipolar_2026',
    year: 2026,
    month: 12,
    title: 'Era Ekonomi Multipolar 2026',
    description: 'AS mendekati $30T, China $20T, serta ekspansi kuat emerging economies.',
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
