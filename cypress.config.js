const { defineConfig } = require("cypress");

module.exports = defineConfig({
  e2e: {
    setupNodeEvents(on, config) {
      this.screenshotOnRunFailure = true;
      this.reporter = "mochawesome";
      this.reporterOptions = {
        reportDir: "cypress/results",
        overwrite: true,
        html: true,
        json: true,
        video: false,
      };
      // implement node event listeners here
    },
  },
});
