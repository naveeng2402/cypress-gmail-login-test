import InitialPage from "../pageObject/InitialPage";
import InitialData from "../fixtures/initialData.json";

describe("Gmail Initial Signup", () => {
  InitialData.slice(0, 2).forEach((data, index) => {
    it(`${data.title} ${index + 1}`, () => {
      const initialPage = new InitialPage();
      initialPage.navigate();
      initialPage.enterFirstName(data.firstName);
      initialPage.enterLastName(data.lastName);
      initialPage.enterUserName(data.userName);
      initialPage.enterPassword(data.password);
      initialPage.confirmPassword(data.confirmPassword);
      initialPage.moveNext();
      cy.screenshot();

      switch (data.err_type) {
        case "N":
          initialPage.checkNameError(data.err_text);
          break;
        case "UN":
          initialPage.checkUserNameError(data.err_text);
          break;
        case "P":
          initialPage.checkPasswordError(data.err_text);
          break;
        default:
          break;
      }
    });
  });
});
