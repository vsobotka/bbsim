import { Button } from "@mantine/core";
import { Preset } from "./attackers.ts";

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

  if (
    !Object.entries(args).some(([key]) =>
      presets.some((preset) => preset.id === key)
    )
  ) {
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
