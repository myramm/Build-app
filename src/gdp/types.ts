export type DataStatusCode =
  | 'ACTUAL_OFFICIAL'
  | 'ACTUAL_HISTORICAL_ESTIMATE'
  | 'PRELIMINARY_ESTIMATE'
  | 'PROJECTION_IMF_WEO';

export interface CountryInfo {
  id: string;
  iso3: string;
  name: string;
  flag: string;
  color: string;
  gradient: string;
}

export interface CountryRanked extends CountryInfo {
  gdp: number; // in Billion USD
  rank: number;
  prevRank?: number;
  rankDelta?: number;
}

export interface TimelineState {
  currentYear: number;
  yearDecimal: number;
  dataStatus: DataStatusCode;
  statusLabel: string;
  statusBadgeColor: string;
  isProjection: boolean;
  progressPercent: number;
}

export interface Milestone {
  id: string;
  year: number;
  title: string;
  description: string;
  verifiedSource: string;
  highlightCountryId?: string;
  startFrame: number;
  endFrame: number;
}
