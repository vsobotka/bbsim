import { containsSomeArg } from "../Utils.ts";
import { outputOptions } from "./output.ts";
import { Button, Checkbox, Title } from "@mantine/core";
import { Page } from "../Layout/Page.tsx";

type Props = {
  args: Record<string, number> | null;
  setArgs: (args: Record<string, number>) => void;
  onClose: () => void;
};

export function OutputSelectionSection({ args, setArgs, onClose }: Props) {
  if (!args) {
    return null;
  }

  if (!containsSomeArg(outputOptions, args)) {
    return null;
  }

  const exampleOutput: string[] = [];
  exampleOutput.push("-----");
  exampleOutput.push("HP = 130, Helmet = 145, Armor = 140");
  outputOptions.forEach((option) => {
    if (
      option.id !== "TotalMean" &&
      option.id !== "AverageMeanPerTest" &&
      args[option.id] === 1
    ) {
      exampleOutput.push(option.example);
    }
  });
  exampleOutput.push("-----");
  if (args["TotalMean"] === 1)
    exampleOutput.push(
      outputOptions.find((option) => option.id === "TotalMean")?.example || ""
    );
  if (args["AverageMeanPerTest"] === 1)
    exampleOutput.push(
      outputOptions.find((option) => option.id === "AverageMeanPerTest")
        ?.example || ""
    );

  if (args)
    return (
      <Page>
        <Title order={5}>Output options:</Title>
        <br />
        {outputOptions
          .filter((option) =>
            Object.entries(args).some(([key]) => option.id === key)
          )
          .map((outputOption) => {
            return (
              <Checkbox
                key={outputOption.id}
                checked={args[outputOption.id] === 1}
                onChange={(event) => {
                  setArgs({
                    ...args,
                    [outputOption.id]: event.currentTarget.checked ? 1 : 0,
                  });
                }}
                label={outputOption.label}
                description={outputOption.description}
              />
            );
          })}
        <br />
        <div>
          <Title order={5}>Example output:</Title>
          <pre>{exampleOutput.join("\n")}</pre>
        </div>
        <Button onClick={onClose}>Close</Button>
      </Page>
    );
}
