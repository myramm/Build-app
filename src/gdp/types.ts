export interface CountryInfo {
  id: string;
  name: string;
  flag: string;
  color: string;
  gradient: string;
}

export interface CountryRanked extends CountryInfo {
  gdp: number; // in Billion USD
  rank: number;
  prevRank?: number;
  rankDelta?: number; // >0 climbed up, <0 dropped down
}

export interface MonthDate {
  year: number;
  month: number; // 1 to 12
  monthName: string;
  monthShort: string;
  yearDecimal: number;
}

export interface Milestone {
  id: string;
  year: number;
  month: number; // 1 to 12
  title: string;
  description: string;
  highlightCountryId?: string;
  startFrame: number;
  endFrame: number;
}
