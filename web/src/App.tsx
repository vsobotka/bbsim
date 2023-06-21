import { useState } from "react";
import * as pyscript from "../python/BBCalc.py";
import { Button, Text } from "@mantine/core";

declare const loadPyodide: any;

async function hello_python() {
  const pyodide = await loadPyodide();
  return await pyodide.runPythonAsync(pyscript.default);
}

export function App() {
  const [output, setOutput] = useState("");
  const [error, setError] = useState(null);
  const [running, setRunning] = useState(false);

  const run = async () => {
    const out = await hello_python();
    setOutput(out);
  };

  return (
    <>
      <Button
        onClick={() => {
          setError(null);
          setRunning(true);
          run()
            .catch((e) => setError(e.toString()))
            .finally(() => setRunning(false));
        }}
      >
        My Button
      </Button>
      <Text c="red">{error}</Text>
      <Text>{running ? "Running script..." : output}</Text>
    </>
  );
}
