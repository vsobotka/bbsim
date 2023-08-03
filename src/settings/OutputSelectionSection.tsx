import { containsSomeArg } from "../Utils.ts";
import { outputOptions } from "./output.ts";
import { Button, Checkbox } from "@mantine/core";
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

  return (
    <Page>
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
      <Button onClick={onClose}>Close</Button>
    </Page>
  );
}
