export enum Factions {
  AncientDead = "Ancient Dead",
  Barbarians = "Barbarians",
  Beasts = "Beasts",
  Brigands = "Brigands",
  CityState = "City State",
  Company = "Company",
  Goblins = "Goblins",
  NobleHouse = "Noble House",
  Nomads = "Nomads",
  Orcs = "Orcs",
  Undead = "Undead",
}

export const attackers = [
  {
    name: "Ancient Dead - Sword",
    id: "APreAncientSword",
    faction: Factions.AncientDead,
  },
  {
    name: "Ancient Dead - Bladed Pike",
    id: "APreBladedPike",
    faction: Factions.AncientDead,
  },
  {
    name: "Ancient Dead - Warscythe",
    id: "APreWarscytheAoE",
    faction: Factions.AncientDead,
  },
  {
    name: "Ancient Dead - Crypt Cleaver",
    id: "APreCryptCleaver",
    faction: Factions.AncientDead,
  },
  {
    name: "Necrosavant - Khopesh",
    id: "APreKhopesh",
    faction: Factions.AncientDead,
  },
  {
    name: "Fallen Hero - Great Axe",
    id: "APreFHGreatAxe",
    faction: Factions.Undead,
  },
  {
    name: "Orc Berserker - Berserk Chain",
    id: "APreBerserkChain",
    faction: Factions.Orcs,
  },
  {
    name: "Orc Young/Warrior - Head Splitter",
    id: "APreHeadSplitter",
    faction: Factions.Orcs,
  },
  {
    name: "Orc Young/Warrior - Head Chopper",
    id: "APreHeadChopper",
    faction: Factions.Orcs,
  },
  {
    name: "Orc Warlord - Mansplitter",
    id: "APreMansplitter",
    faction: Factions.Orcs,
  },
  {
    name: "Goblin Ambusher - Reinforced Boondock",
    id: "APreReinBoondock",
    faction: Factions.Goblins,
  },
  {
    name: "Goblin Overseer - Spiked Impaler",
    id: "APreSpikedImpaler",
    faction: Factions.Goblins,
  },
  {
    name: "Chosen - Spiked Mace",
    id: "APre2HSpikedMace",
    faction: Factions.Barbarians,
  },
  {
    name: "Chosen - Skull Hammer",
    id: "APre2HSkullHammer",
    faction: Factions.Barbarians,
  },
  {
    name: "Chosen - Heavy Rusty Axe",
    id: "APreHeavyRustyAxe",
    faction: Factions.Barbarians,
  },
  {
    name: "Chosen - Rusty Warblade",
    id: "APreRustyWarblade",
    faction: Factions.Barbarians,
  },
  {
    name: "Billman - Billhook",
    id: "APreBillhook",
    faction: Factions.NobleHouse,
  },
  {
    name: "Arbalester - Heavy Crossbow",
    id: "APreHeavyXbow",
    faction: Factions.NobleHouse,
  },
  {
    name: "Knight - Fighting Axe",
    id: "APreFightingAxe",
    faction: Factions.NobleHouse,
  },
  {
    name: "Sergeant - Winged Mace",
    id: "APreWingedMace",
    faction: Factions.NobleHouse,
  },
  {
    name: "Zweihander - Greatsword",
    id: "APreGreatsword",
    faction: Factions.NobleHouse,
  },
  {
    name: "Raider - Flail",
    id: "APreFlailDGrip",
    faction: Factions.Brigands,
  },
  {
    name: "Raider - Long Axe",
    id: "APreLongAxe",
    faction: Factions.Brigands,
  },
  {
    name: "Marksman - Medium Crossbow",
    id: "APreMedXbow",
    faction: Factions.Brigands,
  },
  {
    name: "Swordmaster - Noble Sword",
    id: "APreNobleSword",
    faction: Factions.NobleHouse,
  },
  {
    name: "Master Archer - Warbow",
    id: "APreWarbow",
    faction: Factions.Brigands,
  },
  {
    name: "Conscript - Pole Mace",
    id: "APrePoleMace",
    faction: Factions.CityState,
  },
  {
    name: "Gunner - Handgonne",
    id: "APreHandgonne",
    faction: Factions.CityState,
  },
  {
    name: "Officer - 2H Scimitar",
    id: "APre2HScimitar",
    faction: Factions.CityState,
  },
  {
    name: "Assassin - Qatal Dagger",
    id: "APreQatal",
    faction: Factions.Nomads,
  },
  {
    name: "Frenzied Direwolf",
    id: "APreFDirewolf",
    faction: Factions.Beasts,
  },
  {
    name: "Tier 3 Nachzehrer",
    id: "APreNachTier3",
    faction: Factions.Beasts,
  },
];
