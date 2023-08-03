import { ActionIcon } from "@mantine/core";
import { IconSettings } from "@tabler/icons-react";

type Props = {
  onClick: () => void;
};

export function OutputSettingsButton({ onClick }: Props) {
  return (
    <ActionIcon
      style={{ display: "inline-block", float: "right" }}
      onClick={onClick}
      title="Output options"
    >
      <IconSettings />
    </ActionIcon>
  );
}
