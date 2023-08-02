import { useEffect, useState } from "react";
import { Button, NativeSelect, Text, TextInput } from "@mantine/core";
import { getScriptDefaults, runScript } from "./runners/runners.ts";
import { AttackerPresetSelection } from "./presets/AttackerPresetSelection.tsx";
import { attacker } from "./presets/attacker.ts";

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
  const [selectedPreset, setSelectedPreset] = useState(null as null | string);
  const [showPresetSelection, setShowPresetSelection] = useState(false);

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
          { ...args, [selectedPreset ?? ""]: 1 }
        )
          .catch((e) => setError(e.toString()))
          .finally(() => setRunning(false));
      }
    : undefined;

  const canShowAttackerPreset =
    args &&
    Object.entries(args).some(([key]) =>
      attacker.some((attacker) => attacker.id === key)
    );

  if (showPresetSelection) {
    return (
      <AttackerPresetSelection
        selectedPreset={selectedPreset}
        setSelectedPreset={(preset) => {
          setSelectedPreset(preset);
          setShowPresetSelection(false);
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
        <>
          <br />
          {"Attacker preset: "}
          <Button
            onClick={() => setShowPresetSelection(true)}
            style={{ marginBottom: 15 }}
            variant={selectedPreset ? "light" : "subtle"}
          >
            {selectedPreset
              ? attacker.find((att) => att.id === selectedPreset)?.name
              : "Select attacker preset or leave empty"}
          </Button>
          <br />
        </>
      )}
      {args &&
        Object.entries(args)
          .filter(([key]) => !attacker.some((att) => att.id === key))
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
