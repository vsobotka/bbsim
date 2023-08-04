type Option = {
  id: string;
  label: string;
  description: string;
  example: string;
};

export const outputOptions: Option[] = [
  {
    id: "DeathMean",
    label: "Death Mean",
    description: "Returns the average number of hits until death.",
    example: "Death in 6.46895 hits on average.",
  },
  {
    id: "DeathStDev",
    label: "Death StDev",
    description: "Returns standard deviation of hits until death.",
    example: "StDev: 0.7763774372811534",
  },
  {
    id: "DeathPercent",
    label: "Death Percent",
    description: "Returns % chance of death by each hit.",
    example:
      "% Hits to die: [(4, 0.347), (5, 9.998999999999999), (6, 38.711), (7, 44.299), (8, 6.643000000000001), (9, 0.001)]",
  },
  {
    id: "InjuryMean",
    label: "Injury Mean",
    description: "Returns average number of hits until first injury.",
    example: "First injury in 4.90671 hits on average.",
  },
  {
    id: "InjuryPercent",
    label: "Injury Percent",
    description: "Returns % chance of first injury by each hit.",
    example:
      "% First injury in: [(2, 0.011000000000000001), (3, 4.279), (4, 34.304), (5, 33.827), (6, 21.593), (7, 5.985), (8, 0.001)]",
  },
  {
    id: "HeavyInjuryMean",
    label: "Heavy Injury Mean",
    description:
      "Returns average number of hits until chance of first heavy injury (heavy injuries are not guaranteed even when threshold is met).",
    example: "Chance of first heavy injury in 5.63518 hits on average.",
  },
  {
    id: "HeavyInjuryPercent",
    label: "Heavy Injury Percent",
    description: "Returns % chance of first heavy injury chance by each hit.",
    example:
      "% First heavy injury chance in: [(3, 0.009000000000000001), (4, 18.189), (5, 29.125), (6, 27.228), (7, 21.851000000000003), (8, 3.5970000000000004), (9, 0.001)]",
  },
  {
    id: "MoraleMean",
    label: "Morale Mean",
    description: "Returns average number of hits until first morale check.",
    example: "First morale check in 3.96615 hits on average.",
  },
  {
    id: "MoralePercent",
    label: "Morale Percent",
    description: "Returns % chance of first morale check by each hit.",
    example:
      "% First morale check in: [(1, 0.541), (2, 5.179), (3, 23.474), (4, 41.617), (5, 26.308), (6, 2.881)]",
  },
  {
    id: "TotalMean",
    label: "Total Mean",
    description:
      "Returns the total of mean hits to kill for each test added together at the very end.",
    example: "120.6074 hits to die total against this test group.",
  },
  {
    id: "AverageMeanPerTest",
    label: "Average Mean Per Test",
    description: "Returns average hits to kill against the whole test group.",
    example:
      "3.445925714285714 hits to die on average against this test group.",
  },
];
