export type Script = {
  id: string;
  description: string;
};

export const scripts: Script[] = [
  {
    id: "BB1HanderBattery",
    description:
      "This version of the calculator will run all top line 1Hander options in the provided scenario.\n" +
      "Unique weapon logic is automatically applied when appropriate. Weapon Mastery is assumed.",
  },
  {
    id: "BB2HanderBattery",
    description:
      "This version of the calculator will run all top line 2Hander options in the provided scenario.\n" +
      "Unique weapon logic is automatically applied when appropriate. Weapon Mastery is assumed.",
  },
  {
    id: "BBAttackerVsEnemies",
    description:
      "This version of the calculator will run a given attacker against 30 different enemies.\n" +
      "Defender specific stats and perks are automatically applied.\n" +
      "If you wish to more easily compare two test cases, run the script once in two separate terminals.",
  },
  {
    id: "BBCalc",
    description:
      "The calculator expects you to make smart decisions, such as not giving Xbow Mastery to a Hammer.",
  },
  {
    id: "BBEnemiesVsDefender",
    description:
      "This version of the calculator will run 35 different enemies against a given defender.\n" +
      "Attacker specific perks, weapons, and traits are automatically applied.",
  },
  {
    id: "BBHitChance",
    description:
      "This version of the calculator is a very basic addition of Hit Chance to the regular calculator.\n" +
      "To use this, set the HitChance variable to whatever hit chance you wish to test.\n" +
      "This calculator is a good way to test how something like Gifted or some extra bit of melee defense would help in a specific scenario.",
  },
  {
    id: "BBNimbleBattery",
    description:
      "This version of the calculator will run 15 different Nimble lines given the scenario you provide.",
  },
  {
    id: "BBRaisingHp",
    description:
      "This version of the calculator will run the given scenario starting at 60hp and ending at 140hp and returning the outcome at every 10 hp interval.",
  },
];
