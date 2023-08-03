export function containsSomeArg(options: any, args: Record<string, number>) {
  return Object.entries(args).some(([key]) =>
    options.some((option: any) => option.id === key)
  );
}
