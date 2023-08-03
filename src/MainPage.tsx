import { useEffect, useState } from "react";
import { Button, NativeSelect, Text, TextInput } from "@mantine/core";
import { getScriptDefaults, runScript } from "./runners/runners.ts";
import { attackers } from "./Presets/attackers.ts";
import { PresetSelectionPage } from "./Presets/PresetSelectionPage.tsx";
import { PresetButton } from "./Presets/PresetButton.tsx";
import { defenders } from "./Presets/defender.ts";
import { Page } from "./Layout/Page.tsx";
import { OutputSelectionSection } from "./Settings/OutputSelectionSection.tsx";
import { outputOptions } from "./Settings/output.ts";
import { ThemeToggleButton } from "./Settings/ThemeToggleButton.tsx";
import { OutputSettingsButton } from "./Settings/OutputSettingsButton.tsx";

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

export function MainPage() {
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
  const [showOutputSelection, setShowOutputSelection] = useState(false);

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

        const kwargs = { ...args };
        if (selectedAttackerPreset) {
          kwargs[selectedAttackerPreset] = 1;
        }
        if (selectedDefenderPreset) {
          kwargs[selectedDefenderPreset] = 1;
        }

        runScript(
          script,
          (addition) => {
            setOutput((output) => [...output, addition]);
          },
          {
            ...kwargs,
          }
        )
          .catch((e) => setError(e.toString()))
          .finally(() => setRunning(false));
      }
    : undefined;

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

  if (showOutputSelection) {
    return (
      <OutputSelectionSection
        args={args}
        setArgs={setArgs}
        onClose={() => setShowOutputSelection(false)}
      />
    );
  }

  return (
    <Page>
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
      <ThemeToggleButton />
      <OutputSettingsButton onClick={() => setShowOutputSelection(true)} />
      {running && (
        <Text style={{ display: "inline-block" }}>Running {script}...</Text>
      )}
      {output.length > 0 && (
        <Text style={{ display: "inline-block", marginLeft: 10 }}>
          ↓ Scroll down to see the output ↓
        </Text>
      )}
      {!args && <Text>Loading...</Text>}
      <br />
      <PresetButton
        label={"Attacker preset: "}
        selectedPreset={selectedAttackerPreset}
        onClick={() => setShowAttackerPresetSelection(true)}
        onClear={() => setSelectedAttackerPreset(null)}
        presets={attackers}
        args={args}
      />
      <PresetButton
        label={"Defender preset: "}
        selectedPreset={selectedDefenderPreset}
        onClick={() => setShowDefenderPresetSelection(true)}
        onClear={() => setSelectedDefenderPreset(null)}
        presets={defenders}
        args={args}
      />
      <br />
      {args &&
        Object.entries(args)
          .filter(([key]) => !attackers.some((att) => att.id === key))
          .filter(([key]) => !defenders.some((att) => att.id === key))
          .filter(([key]) => !outputOptions.some((att) => att.id === key))
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
    </Page>
  );
}
