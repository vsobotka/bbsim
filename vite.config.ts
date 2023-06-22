import { defineConfig } from "vite";
import react from "@vitejs/plugin-react";
import markdownRawPlugin from "vite-raw-plugin";

// https://vitejs.dev/config/
export default defineConfig({
  base: "/bbsim/",
  plugins: [
    react(),
    markdownRawPlugin({
      fileRegex: /\.py$/,
    }),
  ],
});
