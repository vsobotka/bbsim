import { attacker, Factions } from "./attacker.ts";
import { Button } from "@mantine/core";

type Props = {
  selectedPreset: string | null;
  setSelectedPreset: (preset: string | null) => void;
};

export function AttackerPresetSelection({
  selectedPreset,
  setSelectedPreset,
}: Props) {
  return Object.keys(Factions).map((faction) => {
    return (
      <div>
        <div>{faction}</div>
        {attacker
          .filter(
            (attacker) =>
              attacker.faction === Factions[faction as keyof typeof Factions]
          )
          .map((attacker) => {
            return (
              <Button
                style={{ display: "block" }}
                variant={selectedPreset === attacker.id ? "filled" : "subtle"}
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
  });
}
