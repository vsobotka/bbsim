import { Page } from "../Layout/Page.tsx";
import { Script, scripts } from "./scripts.ts";
import { Fragment } from "react";
import { Button } from "@mantine/core";

type Props = {
  onClick: (script: Script) => void;
  selectedScript: Script;
  onClose: () => void;
};

export function ScenarioSelectionPage({
  onClick,
  selectedScript,
  onClose,
}: Props) {
  return (
    <Page>
      {scripts.map((script) => {
        return (
          <Fragment key={script.id}>
            <Button
              onClick={() => onClick(script)}
              variant={selectedScript.id === script.id ? "light" : "subtle"}
            >
              {script.id}
            </Button>
            <br />
            {script.description}
            <br />
          </Fragment>
        );
      })}
      <Button onClick={onClose}>Close</Button>
    </Page>
  );
}
