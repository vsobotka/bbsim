import { useState } from "react";
import { Button, Text, TextInput } from "@mantine/core";
import { runBBCalc } from "./runners/runners.ts";

export function App() {
  const [output, setOutput] = useState<string[]>([]);
  const [error, setError] = useState(null);
  const [running, setRunning] = useState(false);
  const [Def_HP, setDef_HP] = useState(100);
  const [Def_Helmet, setDef_Helmet] = useState(120);
  const [Def_Armor, setDef_Armor] = useState(95);

  return (
    <>
      <TextInput
        style={{ width: 100, display: "inline-block" }}
        label="Defender HP"
        description="Defender's HP"
        onChange={(e) => setDef_HP(Number(e.currentTarget.value))}
        value={Def_HP}
      />
      <TextInput
        style={{ width: 100, display: "inline-block" }}
        label="Defender Helmet"
        description="Defender's Helmet"
        onChange={(e) => setDef_Helmet(Number(e.currentTarget.value))}
        value={Def_Helmet}
      />
      <TextInput
        style={{ width: 100, display: "inline-block" }}
        label="Defender Armor"
        description="Defender's Armor"
        onChange={(e) => setDef_Armor(Number(e.currentTarget.value))}
        value={Def_Armor}
      />
      <Button
        onClick={() => {
          setError(null);
          setRunning(true);
          setOutput([]);
          runBBCalc(
            (addition) => {
              setOutput((output) => [...output, addition]);
            },
            { Def_HP, Def_Helmet, Def_Armor }
          )
            .catch((e) => setError(e.toString()))
            .finally(() => setRunning(false));
        }}
      >
        Run BBCalc
      </Button>
      <Text c="red">{error}</Text>
      <Text span style={{ whiteSpace: "pre" }}>
        {running ? "Running script..." : output.join("\n")}
      </Text>
    </>
  );
}
