import { PropsWithChildren } from "react";

export function Page({ children }: PropsWithChildren) {
  return <div style={{ padding: 15 }}>{children}</div>;
}
