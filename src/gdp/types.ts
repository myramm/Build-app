export interface CountryInfo {
  id: string;
  name: string;
  flag: string;
  color: string;
}

export interface CountryRanked extends CountryInfo {
  gdp: number; // in Billion USD
  rank: number;
}

export interface Milestone {
  year: number;
  title: string;
  description: string;
}
