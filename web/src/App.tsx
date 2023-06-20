import { useEffect, useState } from "react";
import * as pyscript from "../python/BBCalc.py";

declare const loadPyodide: any;

async function hello_python() {
  const pyodide = await loadPyodide();
  return await pyodide.runPythonAsync(pyscript.default);
}

export function App() {
  const [output, setOutput] = useState("(initializing...)");

  useEffect(() => {
    const run = async () => {
      const out = await hello_python();
      setOutput(out);
    };
    run()
      .then((result) => console.log(result))
      .catch((err) => console.log(err));
  }, []);

  return <h1>{output}</h1>;
}
