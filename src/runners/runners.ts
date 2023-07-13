import * as BB1HanderBattery from "../../python/BB1HanderBattery.py";
import * as BB2HanderBattery from "../../python/BB2HanderBattery.py";
import * as BBAttackerVsEnemies from "../../python/BBAttackerVsEnemies.py";
import * as BBCalc from "../../python/BBCalc.py";
import * as BBEnemiesVsDefender from "../../python/BBEnemiesVsDefender.py";
import * as BBHitChance from "../../python/BBHitChance.py";
import * as BBNimbleBattery from "../../python/BBNimbleBattery.py";
import * as BBRaisingHp from "../../python/BBRaisingHp.py";
import * as utils from "../../python/utils.py";
// eslint-disable-next-line @typescript-eslint/ban-ts-comment
// @ts-ignore
import type { loadPyodide } from "pyodide";

declare const loadPyodide: loadPyodide;

export async function runScript(
  script: string,
  handleOutput: (text: string) => void,
  kwargs: Record<string, unknown> = {}
) {
  const pyodide = await loadPyodide({
    stdout: handleOutput,
  });
  pyodide.runPython(getScript(script).default);
  const functionToRun = pyodide.globals.get(script);
  functionToRun.callKwargs(kwargs);
}

export async function getScriptDefaults(script: string) {
  const pyodide = await loadPyodide();

  pyodide.runPython(getScript(script).default);
  pyodide.runPython(utils.default);

  const defArgs = pyodide.globals.get("get_default_args");
  const functionToRun = pyodide.globals.get(script);

  return defArgs(functionToRun).toJs();
}

function getScript(script: string) {
  switch (script) {
    case "BB1HanderBattery":
      return BB1HanderBattery;
    case "BB2HanderBattery":
      return BB2HanderBattery;
    case "BBAttackerVsEnemies":
      return BBAttackerVsEnemies;
    case "BBEnemiesVsDefender":
      return BBEnemiesVsDefender;
    case "BBHitChance":
      return BBHitChance;
    case "BBNimbleBattery":
      return BBNimbleBattery;
    case "BBRaisingHp":
      return BBRaisingHp;
    case "BBCalc":
      return BBCalc;
    default:
      throw new Error(`Script ${script} not found`);
  }
}
