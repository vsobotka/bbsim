import { attackers, Factions } from "./attackers.ts";
import { Button, SimpleGrid, Title } from "@mantine/core";

type Props = {
  selectedPreset: string | null;
  setSelectedPreset: (preset: string | null) => void;
};

export function AttackerPresetSelection({
  selectedPreset,
  setSelectedPreset,
}: Props) {
  return (
    <SimpleGrid
      cols={3}
      spacing="xs"
      verticalSpacing="sm"
      breakpoints={[
        { maxWidth: "xs", cols: 1 },
        { maxWidth: "sm", cols: 2 },
      ]}
    >
      {Object.keys(Factions).map((faction) => {
        return (
          <div key={faction} style={{ width: 250 }}>
            <Title order={5}>{faction}</Title>
            {attackers
              .filter(
                (attacker) =>
                  attacker.faction ===
                  Factions[faction as keyof typeof Factions]
              )
              .map((attacker) => {
                return (
                  <Button
                    key={attacker.id}
                    style={{ display: "block" }}
                    variant={
                      selectedPreset === attacker.id ? "filled" : "subtle"
                    }
                    onClick={() => {
                      selectedPreset === attacker.id
                        ? setSelectedPreset(null)
                        : setSelectedPreset(attacker.id);
                    }}
                  >
                    {attacker.name}
                  </Button>
                );
              })}
          </div>
        );
      })}
    </SimpleGrid>
  );
}
