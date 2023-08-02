import { useEffect, useState } from "react";
import { Button, NativeSelect, Text, TextInput } from "@mantine/core";
import { getScriptDefaults, runScript } from "./runners/runners.ts";
import { attackers } from "./presets/attackers.ts";
import { PresetSelectionPage } from "./presets/PresetSelectionPage.tsx";
import { PresetButton } from "./presets/PresetButton.tsx";
import { defenders } from "./presets/defender.ts";

const scripts = [
  "BB1HanderBattery",
  "BB2HanderBattery",
  "BBAttackerVsEnemies",
  "BBCalc",
  "BBEnemiesVsDefender",
  "BBHitChance",
  "BBNimbleBattery",
  "BBRaisingHp",
];

export function App() {
  const [output, setOutput] = useState<string[]>([]);
  const [error, setError] = useState(null as null | string);
  const [running, setRunning] = useState(false);
  const [args, setArgs] = useState(null as null | Record<string, number>);
  const [script, setScript] = useState(scripts[0]);
  const [selectedAttackerPreset, setSelectedAttackerPreset] = useState(
    null as null | string
  );
  const [selectedDefenderPreset, setSelectedDefenderPreset] = useState(
    null as null | string
  );
  const [showAttackerPresetSelection, setShowAttackerPresetSelection] =
    useState(false);
  const [showDefenderPresetSelection, setShowDefenderPresetSelection] =
    useState(false);

  useEffect(() => {
    getScriptDefaults(script).then((defaults) => {
      setArgs(Object.fromEntries(defaults));
    });
  }, [script]);

  const runScriptHandler = args
    ? () => {
        setError(null);
        setRunning(true);
        setOutput([]);
        runScript(
          script,
          (addition) => {
            setOutput((output) => [...output, addition]);
          },
          {
            ...args,
            [selectedAttackerPreset ?? ""]: 1,
            [selectedDefenderPreset ?? ""]: 1,
          }
        )
          .catch((e) => setError(e.toString()))
          .finally(() => setRunning(false));
      }
    : undefined;

  const canShowAttackerPreset =
    args &&
    Object.entries(args).some(([key]) =>
      attackers.some((preset) => preset.id === key)
    );
  const canShowDefenderPreset =
    args &&
    Object.entries(args).some(([key]) =>
      defenders.some((preset) => preset.id === key)
    );

  if (showAttackerPresetSelection) {
    return (
      <PresetSelectionPage
        presets={attackers}
        selectedPreset={selectedAttackerPreset}
        setSelectedPreset={(preset) => {
          setSelectedAttackerPreset(preset);
          setShowAttackerPresetSelection(false);
        }}
      />
    );
  }

  if (showDefenderPresetSelection) {
    return (
      <PresetSelectionPage
        presets={defenders}
        selectedPreset={selectedDefenderPreset}
        setSelectedPreset={(preset) => {
          setSelectedDefenderPreset(preset);
          setShowDefenderPresetSelection(false);
        }}
      />
    );
  }

  return (
    <>
      <NativeSelect
        data={scripts}
        value={script}
        onChange={(e) => {
          setOutput([]);
          setArgs(null);
          setScript(e.currentTarget.value);
        }}
        style={{ width: 250, display: "inline-block", marginRight: 15 }}
      />
      <Button
        disabled={running || !runScriptHandler}
        onClick={runScriptHandler}
      >
        Run
      </Button>
      {running && (
        <Text style={{ display: "inline-block" }}>Running {script}...</Text>
      )}
      {output.length > 0 && (
        <Text style={{ display: "inline-block" }}>
          Scroll down to see the output
        </Text>
      )}
      <br />

      {!args && <Text>Loading...</Text>}
      {canShowAttackerPreset && (
        <PresetButton
          label={"Attacker preset: "}
          selectedPreset={selectedAttackerPreset}
          onClick={() => setShowAttackerPresetSelection(true)}
          onClear={() => setSelectedAttackerPreset(null)}
          presets={attackers}
        />
      )}
      {canShowDefenderPreset && (
        <PresetButton
          label={"Defender preset: "}
          selectedPreset={selectedDefenderPreset}
          onClick={() => setShowDefenderPresetSelection(true)}
          onClear={() => setSelectedDefenderPreset(null)}
          presets={defenders}
        />
      )}
      <br />
      {args &&
        Object.entries(args)
          .filter(([key]) => !attackers.some((att) => att.id === key))
          .map(([key, value]) => (
            <TextInput
              style={{ width: 120, display: "inline-block" }}
              label={key}
              onChange={(e) =>
                setArgs({ ...args, [key]: Number(e.currentTarget.value) })
              }
              value={value}
            />
          ))}
      <Text c="red">{error}</Text>
      <Text span style={{ whiteSpace: "pre" }}>
        {running ? "Running script..." : output.join("\n")}
      </Text>
    </>
  );
}
