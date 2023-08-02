import { Button } from "@mantine/core";
import { Preset } from "./attackers.ts";

type Props = {
  label: string;
  selectedPreset: string | null;
  onClick: () => void;
  onClear: () => void;
  presets: Preset[];
};

export function PresetButton({
  label,
  selectedPreset,
  onClick,
  onClear,
  presets,
}: Props) {
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
