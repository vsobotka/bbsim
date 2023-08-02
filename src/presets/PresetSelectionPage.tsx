import { Factions, Preset } from "./attackers.ts";
import { Button, SimpleGrid, Title } from "@mantine/core";

type Props = {
  selectedPreset: string | null;
  setSelectedPreset: (preset: string | null) => void;
  presets: Preset[];
};

export function PresetSelectionPage({
  selectedPreset,
  setSelectedPreset,
  presets,
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
            {presets
              .filter(
                (preset) =>
                  preset.faction === Factions[faction as keyof typeof Factions]
              )
              .map((preset) => {
                return (
                  <Button
                    key={preset.id}
                    style={{ display: "block" }}
                    variant={selectedPreset === preset.id ? "filled" : "subtle"}
                    onClick={() => {
                      selectedPreset === preset.id
                        ? setSelectedPreset(null)
                        : setSelectedPreset(preset.id);
                    }}
                  >
                    {preset.name}
                  </Button>
                );
              })}
          </div>
        );
      })}
    </SimpleGrid>
  );
}
