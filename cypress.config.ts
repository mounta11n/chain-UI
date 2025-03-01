import { defineConfig } from "cypress";

export default defineConfig({
  projectId: "ij1tyk",
  component: {
    devServer: {
      framework: "react",
      bundler: "vite",
    },
  },

  e2e: {
    supportFile: false,
    defaultCommandTimeout: 10000,
    video: false,
    baseUrl: "http://127.0.0.1:8000",
    setupNodeEvents(on, config) {
      on("task", {
        log(message) {
          console.log(message);
          return null;
        }
      });
    },
  },
});
