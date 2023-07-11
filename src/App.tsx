import { useEffect, useState } from "react";
import { Button, Text, TextInput } from "@mantine/core";
import { getBBCalcDefaults, runBBCalc } from "./runners/runners.ts";

export function App() {
  const [output, setOutput] = useState<string[]>([]);
  const [error, setError] = useState(null as null | string);
  const [running, setRunning] = useState(false);
  const [args, setArgs] = useState(null as null | Record<string, number>);

  useEffect(() => {
    getBBCalcDefaults().then((defaults) => {
      setArgs(Object.fromEntries(defaults));
    });
  }, []);

  if (!args) return <Text>Loading...</Text>;

  return (
    <>
      {Object.entries(args).map(([key, value]) => (
        <TextInput
          style={{ width: 120, display: "inline-block" }}
          label={key}
          onChange={(e) =>
            setArgs({ ...args, [key]: Number(e.currentTarget.value) })
          }
          value={value}
        />
      ))}
      <Button
        onClick={() => {
          setError(null);
          setRunning(true);
          setOutput([]);
          runBBCalc((addition) => {
            setOutput((output) => [...output, addition]);
          }, args)
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
