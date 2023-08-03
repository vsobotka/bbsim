type Option = {
  id: string;
  label: string;
  description: string;
};

export const outputOptions: Option[] = [
  {
    id: "DeathMean",
    label: "Death Mean",
    description: "Returns the average number of hits until death.",
  },
  {
    id: "DeathStDev",
    label: "Death StDev",
    description: "Returns standard deviation of hits until death.",
  },
  {
    id: "DeathPercent",
    label: "Death Percent",
    description: "Returns % chance of death by each hit.",
  },
  {
    id: "InjuryMean",
    label: "Injury Mean",
    description: "Returns average number of hits until first injury.",
  },
  {
    id: "InjuryPercent",
    label: "Injury Percent",
    description: "Returns % chance of first injury by each hit.",
  },
  {
    id: "HeavyInjuryMean",
    label: "Heavy Injury Mean",
    description:
      "Returns average number of hits until chance of first heavy injury (heavy injuries are not guaranteed even when threshold is met).",
  },
  {
    id: "HeavyInjuryPercent",
    label: "Heavy Injury Percent",
    description: "Returns % chance of first heavy injury chance by each hit.",
  },
  {
    id: "MoraleMean",
    label: "Morale Mean",
    description: "Returns average number of hits until first morale check.",
  },
  {
    id: "MoralePercent",
    label: "Morale Percent",
    description: "Returns % chance of first morale check by each hit.",
  },
  {
    id: "TotalMean",
    label: "Total Mean",
    description:
      "Returns the total of mean hits to kill for each test added together at the very end.",
  },
  {
    id: "AverageMeanPerTest",
    label: "Average Mean Per Test",
    description: "Returns average hits to kill against the whole test group.",
  },
];
