import { useState } from "react";
import { Button, Text } from "@mantine/core";
import { runBBCalc } from "./runners/runners.ts";

export function App() {
  const [output, setOutput] = useState<string[]>([]);
  const [error, setError] = useState(null);
  const [running, setRunning] = useState(false);

  return (
    <>
      <Button
        onClick={() => {
          setError(null);
          setRunning(true);
          setOutput([]);
          runBBCalc((addition) => {
            setOutput((output) => [...output, addition]);
          })
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
