import * as BBCalc from "../../python/BBCalc.py";
// eslint-disable-next-line @typescript-eslint/ban-ts-comment
// @ts-ignore
import type { loadPyodide } from "pyodide";

declare const loadPyodide: loadPyodide;

async function runScript(
  scriptToRun: string,
  handleOutput: (text: string) => void,
  kwargs: Record<string, unknown> = {}
) {
  const pyodide = await loadPyodide({
    stdout: handleOutput,
  });
  pyodide.runPython(scriptToRun);
  const BBCalc = pyodide.globals.get("BBCalc");
  alert(BBCalc.callKwargs(kwargs));
}

export function runBBCalc(
  handleOutput: (text: string) => void,
  kwargs: Record<string, unknown> = {}
) {
  return runScript(BBCalc.default, handleOutput, kwargs);
}
