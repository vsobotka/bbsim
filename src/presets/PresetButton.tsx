import { Button } from "@mantine/core";
import { Preset } from "./attackers.ts";
import { containsSomeArg } from "../Utils.ts";

type Props = {
  label: string;
  selectedPreset: string | null;
  onClick: () => void;
  onClear: () => void;
  presets: Preset[];
  args: Record<string, number> | null;
};

export function PresetButton({
  label,
  selectedPreset,
  onClick,
  onClear,
  presets,
  args,
}: Props) {
  if (!args) {
    return null;
  }

  if (!containsSomeArg(presets, args)) {
    return null;
  }

  return (
    <>
      <br />
      {label}
      <Button
        onClick={onClick}
        style={{ marginBottom: 15 }}
        variant={selectedPreset ? "light" : "subtle"}
      >
        {selectedPreset
          ? presets.find((att) => att.id === selectedPreset)?.name
          : "Select or leave empty"}
      </Button>
      {selectedPreset && (
        <Button onClick={onClear} variant="subtle">
          {"X"}
        </Button>
      )}
    </>
  );
}
