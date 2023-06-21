import * as BBCalc from "../../python/BBCalc.py";

declare const loadPyodide: any;

async function runScript(
  scriptToRun: string,
  handleOutput: (text: string) => void
) {
  const pyodide = await loadPyodide({
    stdout: handleOutput,
  });
  return await pyodide.runPythonAsync(scriptToRun);
}

export function runBBCalc(handleOutput: (text: string) => void) {
  return runScript(BBCalc.default, handleOutput);
}
