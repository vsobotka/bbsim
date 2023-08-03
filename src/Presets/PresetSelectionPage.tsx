import { Factions, Preset } from "./attackers.ts";
import { Button, SimpleGrid, Title } from "@mantine/core";
import { Page } from "../Layout/Page.tsx";

type Props = {
  selectedPreset: string | null;
  setSelectedPreset: (preset: string | null) => void;
  presets: Preset[];
  onClose: () => void;
};

export function PresetSelectionPage({
  selectedPreset,
  setSelectedPreset,
  presets,
  onClose,
}: Props) {
  return (
    <Page>
      <SimpleGrid
        spacing="sm"
        verticalSpacing="sm"
        breakpoints={[
          { maxWidth: "xs", cols: 1 },
          { maxWidth: "sm", cols: 2 },
          { maxWidth: "md", cols: 3 },
          { maxWidth: "lg", cols: 4 },
          { maxWidth: "xl", cols: 5 },
        ]}
      >
        {Object.keys(Factions).map((faction) => {
          const presetsToShow = presets.filter(
            (preset) =>
              preset.faction === Factions[faction as keyof typeof Factions]
          );

          if (presetsToShow.length === 0) {
            return null;
          }

          return (
            <div key={faction} style={{ width: 250 }}>
              <Title order={5}>{faction}</Title>
              {presetsToShow.map((preset) => {
                const selected = selectedPreset === preset.id;

                return (
                  <Button
                    key={preset.id}
                    style={{ display: "block" }}
                    variant={selected ? "filled" : "subtle"}
                    onClick={() => {
                      selected
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
      <Button onClick={onClose}>Close</Button>
    </Page>
  );
}
