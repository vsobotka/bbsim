import { useEffect, useState } from "react";

declare const loadPyodide: any;

async function hello_python() {
  const pyodide = await loadPyodide();
  return await pyodide.runPythonAsync("1+3");
}

export function App() {
  const [output, setOutput] = useState("(loading...)");

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
